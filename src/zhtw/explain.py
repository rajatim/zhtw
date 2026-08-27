"""Read-only conversion explanation built on the production scan and layers."""

from __future__ import annotations

import threading
from dataclasses import dataclass
from typing import Any, Iterable, Optional

from .converter import (
    VALID_AMBIGUITY_MODES,
    VALID_SOURCES,
    _apply_conversion_layers,
    inject_protect_terms,
)
from .dictionary import load_dictionary_catalog
from .matcher import Match, MatchDecision, Matcher
from .rules import RuleClass, SourceLocale, TrustLevel, legacy_rule_record

EXPLAIN_LAYERS = frozenset({"term", "identity", "balanced", "char"})
EXPLAIN_OUTCOMES = frozenset({"applied", "protected", "skipped"})
EXPLAIN_REASON_CODES = frozenset(
    {
        "term_selected",
        "identity_guard",
        "identity_contained",
        "overlap_loser",
        "protected_by_identity",
        "loader_conflict_winner",
        "loader_conflict_loser",
        "balanced_default",
        "char_map",
    }
)


@dataclass(frozen=True, slots=True)
class ExplainEvent:
    """One applied or skipped rule span without surrounding input context."""

    rule_id: str
    layer: str
    outcome: str
    input_start: int
    input_end: int
    output_start: int
    output_end: int
    source: str
    target: str
    reason_code: str

    def __post_init__(self) -> None:
        if self.layer not in EXPLAIN_LAYERS:
            raise ValueError(f"unknown explain layer: {self.layer!r}")
        if self.outcome not in EXPLAIN_OUTCOMES:
            raise ValueError(f"unknown explain outcome: {self.outcome!r}")
        if self.reason_code not in EXPLAIN_REASON_CODES:
            raise ValueError(f"unknown explain reason code: {self.reason_code!r}")
        if not 0 <= self.input_start < self.input_end:
            raise ValueError("invalid explain input span")
        if not 0 <= self.output_start <= self.output_end:
            raise ValueError("invalid explain output span")
        if not self.rule_id or not self.source or not self.target:
            raise ValueError("explain event strings must be non-empty")

    def to_mapping(self) -> dict[str, Any]:
        """Return the cross-SDK JSON shape."""

        return {
            "rule_id": self.rule_id,
            "layer": self.layer,
            "outcome": self.outcome,
            "input_start": self.input_start,
            "input_end": self.input_end,
            "output_start": self.output_start,
            "output_end": self.output_end,
            "source": self.source,
            "target": self.target,
            "reason_code": self.reason_code,
        }


@dataclass(frozen=True, slots=True)
class ExplainResult:
    """Converted output and its ordered explanation events."""

    output: str
    events: tuple[ExplainEvent, ...]

    def to_mapping(self) -> dict[str, Any]:
        """Return the cross-SDK JSON shape."""

        return {
            "output": self.output,
            "events": [event.to_mapping() for event in self.events],
        }


@dataclass(frozen=True, slots=True)
class _CharacterChange:
    position: int
    source: str
    target: str
    layer: str
    rule_id: str
    reason_code: str


def _character_changes(
    text: str,
    covered: frozenset[int],
    char_table: Optional[dict[int, str]],
    ambiguity_mode: str,
) -> tuple[_CharacterChange, ...]:
    defaults: dict[str, str] = {}
    if ambiguity_mode == "balanced":
        from .charconv import get_balanced_defaults

        defaults = get_balanced_defaults()

    changes: list[_CharacterChange] = []
    for position, source in enumerate(text):
        if position in covered:
            continue
        if source in defaults:
            default = defaults[source]
            target = char_table.get(ord(default), default) if char_table else default
            if target != source:
                changes.append(
                    _CharacterChange(
                        position=position,
                        source=source,
                        target=target,
                        layer="balanced",
                        rule_id=f"balanced:u{ord(source):x}",
                        reason_code="balanced_default",
                    )
                )
            continue
        if char_table:
            target = char_table.get(ord(source), source)
            if target != source:
                changes.append(
                    _CharacterChange(
                        position=position,
                        source=source,
                        target=target,
                        layer="char",
                        rule_id=f"charmap:u{ord(source):x}",
                        reason_code="char_map",
                    )
                )
    return tuple(changes)


def _build_position_spans(
    text: str,
    selected: Iterable[Match],
    character_changes: Iterable[_CharacterChange],
) -> tuple[str, tuple[tuple[int, int], ...]]:
    selected_by_start = {match.start: match for match in selected}
    changes_by_position = {change.position: change for change in character_changes}
    spans: list[tuple[int, int]] = [(0, 0)] * len(text)
    parts: list[str] = []
    input_position = 0
    output_position = 0

    while input_position < len(text):
        match = selected_by_start.get(input_position)
        if match is not None:
            output_end = output_position + len(match.target)
            for position in range(match.start, match.end):
                spans[position] = (output_position, output_end)
            parts.append(match.target)
            output_position = output_end
            input_position = match.end
            continue

        change = changes_by_position.get(input_position)
        target = change.target if change is not None else text[input_position]
        output_end = output_position + len(target)
        spans[input_position] = (output_position, output_end)
        parts.append(target)
        output_position = output_end
        input_position += 1

    return "".join(parts), tuple(spans)


def _output_span(
    position_spans: tuple[tuple[int, int], ...],
    start: int,
    end: int,
) -> tuple[int, int]:
    affected = position_spans[start:end]
    return min(span[0] for span in affected), max(span[1] for span in affected)


def _term_events(
    matcher: Matcher,
    decisions: Iterable[MatchDecision],
    position_spans: tuple[tuple[int, int], ...],
) -> list[ExplainEvent]:
    events: list[ExplainEvent] = []
    for decision in decisions:
        match = decision.match
        output_start, output_end = _output_span(position_spans, match.start, match.end)
        conflicts = matcher.loader_conflicts_for(match)
        reason_code = decision.reason_code
        if decision.outcome == "applied" and conflicts:
            reason_code = "loader_conflict_winner"
        events.append(
            ExplainEvent(
                rule_id=matcher.rule_id_for(match),
                layer="identity" if match.source == match.target else "term",
                outcome=decision.outcome,
                input_start=match.start,
                input_end=match.end,
                output_start=output_start,
                output_end=output_end,
                source=match.source,
                target=match.target,
                reason_code=reason_code,
            )
        )
        if decision.outcome == "applied":
            events.extend(
                ExplainEvent(
                    rule_id=record.id,
                    layer="term",
                    outcome="skipped",
                    input_start=match.start,
                    input_end=match.end,
                    output_start=output_start,
                    output_end=output_end,
                    source=record.source,
                    target=record.target,
                    reason_code="loader_conflict_loser",
                )
                for record in conflicts
            )
    return events


def explain_text(
    text: str,
    matcher: Matcher,
    char_table: Optional[dict[int, str]] = None,
    ambiguity_mode: str = "strict",
) -> ExplainResult:
    """Explain one conversion using one production automaton traversal."""

    if ambiguity_mode not in VALID_AMBIGUITY_MODES:
        raise ValueError(
            f"Invalid ambiguity_mode: {ambiguity_mode!r}. "
            f"Valid modes are: {sorted(VALID_AMBIGUITY_MODES)}"
        )
    if not text:
        return ExplainResult(output=text, events=())

    scan = matcher.scan_detailed(text)
    output = _apply_conversion_layers(
        text,
        matcher,
        char_table,
        ambiguity_mode,
        scan=(list(scan.selected), set(scan.covered)),
    )
    character_changes = _character_changes(text, scan.covered, char_table, ambiguity_mode)
    traced_output, position_spans = _build_position_spans(
        text,
        scan.selected,
        character_changes,
    )
    if traced_output != output:
        raise RuntimeError("explain trace diverged from the production conversion output")

    events = _term_events(matcher, scan.decisions, position_spans)
    events.extend(
        ExplainEvent(
            rule_id=change.rule_id,
            layer=change.layer,
            outcome="applied",
            input_start=change.position,
            input_end=change.position + 1,
            output_start=position_spans[change.position][0],
            output_end=position_spans[change.position][1],
            source=change.source,
            target=change.target,
            reason_code=change.reason_code,
        )
        for change in character_changes
    )
    outcome_order = {"applied": 0, "protected": 1, "skipped": 2}
    events.sort(
        key=lambda event: (
            event.input_start,
            event.input_end,
            outcome_order[event.outcome],
            event.rule_id,
        )
    )
    return ExplainResult(output=output, events=tuple(events))


_DEFAULT_EXPLAIN_CACHE: dict[tuple[str, ...] | None, tuple[Matcher, Optional[dict[int, str]]]] = {}
_DEFAULT_EXPLAIN_LOCK = threading.Lock()


def _build_default_explainer(
    sources: Optional[list[str]],
) -> tuple[Matcher, Optional[dict[int, str]]]:
    loaded = load_dictionary_catalog(sources=sources)
    terms = loaded.terms
    records = list(loaded.catalog)
    inject_protect_terms(terms, sources)
    if sources is None or "cn" in sources:
        from .charconv import get_protect_terms, get_translate_table

        for protected_terms in get_protect_terms().values():
            for term in protected_terms:
                records.append(
                    legacy_rule_record(
                        source_locale=SourceLocale.CN,
                        source=term,
                        target=term,
                        rule_class=RuleClass.GENERATED_GUARD,
                        domain="general",
                        trust_level=TrustLevel.GENERATED,
                        priority=200,
                        evidence_source="data/charmap/disambiguation.json",
                    )
                )
        char_table = get_translate_table()
    else:
        char_table = None
    return Matcher(terms, records), char_table


def explain(
    text: str,
    sources: Optional[list[str]] = None,
    ambiguity_mode: str = "strict",
) -> ExplainResult:
    """Convert text and return output plus minimal rule events."""

    if sources is not None:
        if not sources:
            raise ValueError(
                "sources must be None or a non-empty list. "
                f"Valid sources are: {sorted(VALID_SOURCES)}"
            )
        invalid = sorted({source for source in sources if source not in VALID_SOURCES})
        if invalid:
            raise ValueError(
                f"Invalid source(s): {invalid}. Valid sources are: {sorted(VALID_SOURCES)}"
            )
    if ambiguity_mode not in VALID_AMBIGUITY_MODES:
        raise ValueError(
            f"Invalid ambiguity_mode: {ambiguity_mode!r}. "
            f"Valid modes are: {sorted(VALID_AMBIGUITY_MODES)}"
        )

    key = tuple(sorted(sources)) if sources else None
    cached = _DEFAULT_EXPLAIN_CACHE.get(key)
    if cached is None:
        with _DEFAULT_EXPLAIN_LOCK:
            cached = _DEFAULT_EXPLAIN_CACHE.get(key)
            if cached is None:
                cached = _build_default_explainer(sources)
                _DEFAULT_EXPLAIN_CACHE[key] = cached

    matcher, char_table = cached
    effective_mode = ambiguity_mode
    if ambiguity_mode == "balanced" and sources is not None and "cn" not in sources:
        effective_mode = "strict"
    return explain_text(text, matcher, char_table, effective_mode)
