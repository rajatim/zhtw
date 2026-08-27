"""Tests for the read-only explain contract."""
# zhtw:disable  # fixtures need simplified source text

from __future__ import annotations

import json
from pathlib import Path

import pytest

from zhtw import convert, explain
from zhtw.explain import explain_text
from zhtw.matcher import Matcher
from zhtw.rules import RuleClass, SourceLocale, TrustLevel, legacy_rule_record

ROOT = Path(__file__).resolve().parents[1]


def test_explain_output_matches_public_convert_for_shared_golden_cases() -> None:
    golden = json.loads((ROOT / "sdk/data/golden-test.json").read_text("utf-8"))

    for case in golden["convert"]:
        ambiguity_mode = case.get("ambiguity_mode", "strict")
        result = explain(
            case["input"],
            sources=case["sources"],
            ambiguity_mode=ambiguity_mode,
        )

        assert result.output == case["expected"]
        assert result.output == convert(
            case["input"],
            sources=case["sources"],
            ambiguity_mode=ambiguity_mode,
        )


def test_term_char_and_overlap_events_share_the_production_scan() -> None:
    matcher = Matcher({"应用": "應用", "用于": "用於"})
    original_automaton = matcher.automaton

    class CountingAutomaton:
        calls = 0

        def iter(self, text: str):
            self.calls += 1
            return original_automaton.iter(text)

    counting = CountingAutomaton()
    matcher.automaton = counting

    result = explain_text("应用于", matcher, {ord("于"): "於"})

    assert result.output == "應用於"
    assert counting.calls == 1
    assert [(event.source, event.outcome, event.reason_code) for event in result.events] == [
        ("应用", "applied", "term_selected"),
        ("用于", "skipped", "overlap_loser"),
        ("于", "applied", "char_map"),
    ]


def test_identity_guard_explains_protection_and_blocked_conversion() -> None:
    matcher = Matcher({"文檔": "文件", "檔案": "檔案"})

    result = explain_text("中文檔案", matcher)

    assert result.output == "中文檔案"
    reasons = {(event.source, event.outcome, event.reason_code) for event in result.events}
    assert ("文檔", "skipped", "protected_by_identity") in reasons
    assert ("檔案", "protected", "identity_guard") in reasons


def test_loader_conflict_reports_winner_and_loser_rule_ids() -> None:
    loser = legacy_rule_record(
        source_locale=SourceLocale.CN,
        source="软件",
        target="軟件",
        rule_class=RuleClass.BULK,
        trust_level=TrustLevel.IMPORTED,
        priority=100,
        evidence_source="bulk.json",
    )
    winner = legacy_rule_record(
        source_locale=SourceLocale.CN,
        source="软件",
        target="軟體",
        rule_class=RuleClass.CURATED,
        trust_level=TrustLevel.CURATED,
        priority=300,
        evidence_source="it.json",
    )
    matcher = Matcher({"软件": "軟體"}, [loser, winner])

    result = explain_text("软件", matcher)

    assert result.output == "軟體"
    assert [(event.rule_id, event.outcome, event.reason_code) for event in result.events] == [
        (winner.id, "applied", "loader_conflict_winner"),
        (loser.id, "skipped", "loader_conflict_loser"),
    ]


def test_balanced_and_char_layers_have_distinct_rule_ids() -> None:
    balanced = explain_text("几", Matcher({}), ambiguity_mode="balanced")
    character = explain_text("万", Matcher({}), {ord("万"): "萬"})

    assert balanced.output != "几"
    assert balanced.events[0].layer == "balanced"
    assert balanced.events[0].reason_code == "balanced_default"
    assert balanced.events[0].rule_id == "balanced:u51e0"
    assert character.output == "萬"
    assert character.events[0].layer == "char"
    assert character.events[0].rule_id == "charmap:u4e07"


def test_output_spans_use_codepoint_indexes_after_length_change() -> None:
    result = explain_text("软件!", Matcher({"软件": "application"}))

    event = result.events[0]
    assert result.output == "application!"
    assert (event.input_start, event.input_end) == (0, 2)
    assert (event.output_start, event.output_end) == (0, 11)


def test_spans_count_supplementary_characters_as_one_codepoint() -> None:
    result = explain_text(
        f"😀软件{chr(0x20000)}万",
        Matcher({"软件": "軟體"}),
        {ord("万"): "萬"},
    )

    term = next(event for event in result.events if event.layer == "term")
    character = next(event for event in result.events if event.layer == "char")
    assert (term.input_start, term.input_end) == (1, 3)
    assert (character.input_start, character.input_end) == (4, 5)


def test_event_mapping_does_not_include_context_or_full_input() -> None:
    result = explain_text("prefix软件suffix", Matcher({"软件": "軟體"}))

    event = result.events[0].to_mapping()
    assert set(event) == {
        "rule_id",
        "layer",
        "outcome",
        "input_start",
        "input_end",
        "output_start",
        "output_end",
        "source",
        "target",
        "reason_code",
    }
    assert "prefix" not in json.dumps(event, ensure_ascii=False)
    assert result.to_mapping()["output"] == "prefix軟體suffix"


def test_empty_and_invalid_public_explain_arguments() -> None:
    assert explain("").to_mapping() == {"output": "", "events": []}
    with pytest.raises(ValueError, match="sources"):
        explain("软件", sources=[])
    with pytest.raises(ValueError, match="Invalid source"):
        explain("软件", sources=["xx"])
    with pytest.raises(ValueError, match="ambiguity_mode"):
        explain("软件", ambiguity_mode="unknown")
