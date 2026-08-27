"""
Matcher module using Aho-Corasick algorithm for efficient multi-pattern matching.

This allows O(n) scanning of text regardless of the number of terms in the dictionary.
"""

from bisect import bisect_right
from dataclasses import dataclass
from typing import Dict, Iterable, Iterator

import ahocorasick

from .rules import ReviewStatus, RuleClass, RuleRecord, SourceLocale, legacy_rule_id


@dataclass
class Match:
    """Represents a match found in text."""

    start: int  # Start position in text
    end: int  # End position in text (exclusive)
    source: str  # Original term found
    target: str  # Replacement term


@dataclass(frozen=True, slots=True)
class MatchDecision:
    """One raw automaton candidate and the shared selection outcome."""

    match: Match
    outcome: str
    reason_code: str


@dataclass(frozen=True, slots=True)
class MatchScan:
    """Detailed result from one automaton traversal."""

    raw_matches: tuple[Match, ...]
    selected: tuple[Match, ...]
    covered: frozenset[int]
    decisions: tuple[MatchDecision, ...]


class Matcher:
    """
    Aho-Corasick based matcher for efficient multi-pattern matching.

    Example:
        # zhtw:disable
        >>> terms = {"软件": "軟體", "硬件": "硬體"}
        >>> matcher = Matcher(terms)
        >>> list(matcher.find_matches("这是软件和硬件"))
        [Match(start=2, end=4, source='软件', target='軟體'),
         Match(start=5, end=7, source='硬件', target='硬體')]
        # zhtw:enable
    """

    def __init__(
        self,
        terms: Dict[str, str],
        rule_records: Iterable[RuleRecord] = (),
    ):
        """
        Initialize matcher with a dictionary of terms.

        Args:
            terms: Dictionary mapping source terms to target terms.
        """
        self.terms = terms
        self._rule_records_by_source: dict[str, tuple[RuleRecord, ...]] = {}
        grouped: dict[str, list[RuleRecord]] = {}
        for record in rule_records:
            if record.review_status is ReviewStatus.APPROVED:
                grouped.setdefault(record.source, []).append(record)
        self._rule_records_by_source = {
            source: tuple(records) for source, records in grouped.items()
        }
        self.automaton = self._build_automaton()

    def _build_automaton(self) -> ahocorasick.Automaton:
        """Build Aho-Corasick automaton from terms."""
        automaton = ahocorasick.Automaton()

        for source, target in self.terms.items():
            # Store both source and target for each pattern
            automaton.add_word(source, (source, target))

        automaton.make_automaton()
        return automaton

    def scan(self, text: str) -> tuple[list[Match], set[int]]:
        """Scan once and return selected matches plus effective coverage.

        等價於 ``(list(find_matches(text)), get_covered_positions(text))``，
        但 automaton 只走訪一次。fix/check 熱路徑應優先使用本方法，
        避免重複掃描（automaton.iter 是整條轉換管線的主要成本）。

        Returns:
            Tuple of (selected non-identity matches, covered positions).
            Coverage contains selected conversions and effective identity guards.
            A losing overlapping conversion must not hide its unmatched suffix
            from the character layer.
        """
        all_matches = self._scan_raw(text)
        selected, covered, _decisions = self._select_with_coverage(all_matches)
        return selected, covered

    def scan_detailed(self, text: str) -> MatchScan:
        """Scan once and retain raw candidates plus selection reasons."""

        all_matches = self._scan_raw(text)
        raw_matches = tuple(all_matches)
        selected, covered, decisions = self._select_with_coverage(
            all_matches,
            collect_decisions=True,
        )
        return MatchScan(
            raw_matches=raw_matches,
            selected=tuple(selected),
            covered=frozenset(covered),
            decisions=tuple(decisions),
        )

    def _scan_raw(self, text: str) -> list[Match]:
        """Collect raw candidates from exactly one automaton traversal."""

        if not self.terms:
            return []
        return [
            Match(
                start=end_pos - len(source) + 1,
                end=end_pos + 1,
                source=source,
                target=target,
            )
            for end_pos, (source, target) in self.automaton.iter(text)
        ]

    def find_matches(self, text: str) -> Iterator[Match]:
        """
        Find all matches in text.

        Uses longest-match-first strategy to avoid substring issues.
        For example, if both "算法" and "演算法" are in the dictionary,  # zhtw:disable-line
        "演算法" in text will match the longer pattern first.

        Args:
            text: Text to search in.

        Yields:
            Match objects for each found term (excluding identity matches).
        """
        if not self.terms:
            return

        # Collect all matches first (including identity matches for overlap detection)
        all_matches = []
        for end_pos, (source, target) in self.automaton.iter(text):
            start_pos = end_pos - len(source) + 1
            all_matches.append(
                Match(
                    start=start_pos,
                    end=end_pos + 1,
                    source=source,
                    target=target,
                )
            )

        yield from self._select(all_matches)

    def _select(self, all_matches: list[Match]) -> Iterator[Match]:
        """從全部命中中選出實際要套用的轉換（共用的選擇邏輯）。"""
        selected, _covered, _decisions = self._select_with_coverage(all_matches)
        yield from selected

    def _select_with_coverage(
        self,
        all_matches: list[Match],
        *,
        collect_decisions: bool = False,
    ) -> tuple[list[Match], set[int], list[MatchDecision]]:
        """Select conversions and return only coverage that affects output."""
        if not all_matches:
            return [], set(), []

        # Sort by start position, then by length (longer first)
        all_matches.sort(key=lambda m: (m.start, -(m.end - m.start)))

        # Build "protected ranges" from identity mappings that are NOT fully contained
        # within a longer match. This ensures:
        # - "檔案"→"檔案" protects against overlapping "檔案"→"檔案"
        # - "件"→"件" does NOT block longer "軟體"→"軟體" (件 is contained)
        protected: set[int] = set()

        # Separate identity and non-identity matches
        identity_matches = [m for m in all_matches if m.source == m.target]
        non_identity = [(m.start, m.end) for m in all_matches if m.source != m.target]
        effective_identity_keys: set[tuple[int, int, str, str]] = set()

        # Use binary search to check containment: O(m log m) instead of O(n*m)
        if non_identity:
            non_identity.sort()
            ni_starts = [s for s, _e in non_identity]
            # prefix_max_end[i] = max(end) among non_identity[0..i]
            ni_max_end: list[int] = []
            max_e = 0
            for _s, e in non_identity:
                max_e = max(max_e, e)
                ni_max_end.append(max_e)

            for identity in identity_matches:
                idx = bisect_right(ni_starts, identity.start) - 1
                is_contained = idx >= 0 and ni_max_end[idx] >= identity.end
                if not is_contained:
                    protected.update(range(identity.start, identity.end))
                    effective_identity_keys.add(
                        (identity.start, identity.end, identity.source, identity.target)
                    )
        else:
            for identity in identity_matches:
                protected.update(range(identity.start, identity.end))
                effective_identity_keys.add(
                    (identity.start, identity.end, identity.source, identity.target)
                )

        # Filter overlapping matches. Only selected conversions and effective
        # identity guards count as covered. Raw candidates that lose overlap
        # selection must remain available to the character layer.
        selected: list[Match] = []
        decisions: list[MatchDecision] = []
        covered = set(protected)
        last_end = -1
        for match in all_matches:
            identity_key = (match.start, match.end, match.source, match.target)
            if match.start >= last_end:
                # Skip if this conversion overlaps with a protected range
                if match.source != match.target:
                    if any(i in protected for i in range(match.start, match.end)):
                        if collect_decisions:
                            decisions.append(
                                MatchDecision(match, "skipped", "protected_by_identity")
                            )
                        continue
                last_end = match.end
                # Skip identity matches (no actual change needed)
                if match.source != match.target:
                    selected.append(match)
                    covered.update(range(match.start, match.end))
                    if collect_decisions:
                        decisions.append(MatchDecision(match, "applied", "term_selected"))
                elif collect_decisions:
                    reason = (
                        "identity_guard"
                        if identity_key in effective_identity_keys
                        else "identity_contained"
                    )
                    decisions.append(MatchDecision(match, "protected", reason))
            elif collect_decisions:
                if match.source == match.target and identity_key in effective_identity_keys:
                    decisions.append(MatchDecision(match, "protected", "identity_guard"))
                else:
                    reason = (
                        "identity_contained" if match.source == match.target else "overlap_loser"
                    )
                    decisions.append(MatchDecision(match, "skipped", reason))

        return selected, covered, decisions

    def rule_record_for(self, match: Match) -> RuleRecord | None:
        """Return the effective descriptive record for a runtime match."""

        candidates = self._rule_records_by_source.get(match.source, ())
        for record in reversed(candidates):
            if record.target == match.target:
                return record
        return None

    def rule_id_for(self, match: Match) -> str:
        """Return a stable rule ID, including for ad-hoc matchers."""

        record = self.rule_record_for(match)
        if record is not None:
            return record.id
        return legacy_rule_id(
            SourceLocale.CN,
            match.source,
            match.target,
            RuleClass.CUSTOM,
        )

    def loader_conflicts_for(self, match: Match) -> tuple[RuleRecord, ...]:
        """Return approved records hidden by the effective source winner."""

        winner = self.rule_record_for(match)
        return tuple(
            record
            for record in self._rule_records_by_source.get(match.source, ())
            if winner is None or record.id != winner.id
        )

    def get_covered_positions(self, text: str) -> set[int]:
        """Return positions covered by selected terms or effective identity guards."""
        return self.scan(text)[1]

    def find_matches_with_lines(self, text: str) -> Iterator[tuple[Match, int, int]]:
        """
        Find all matches with line and column information.

        Args:
            text: Text to search in.

        Yields:
            Tuple of (Match, line_number, column) for each found term.
            Line numbers are 1-based.
        """
        # Pre-compute line starts for efficient line number lookup
        line_starts = [0]
        for i, char in enumerate(text):
            if char == "\n":
                line_starts.append(i + 1)

        def get_line_col(pos: int) -> tuple[int, int]:
            """Get 1-based line number and column for a position."""
            # Binary search for line
            lo, hi = 0, len(line_starts) - 1
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if line_starts[mid] <= pos:
                    lo = mid
                else:
                    hi = mid - 1
            line = lo + 1  # 1-based
            col = pos - line_starts[lo] + 1  # 1-based
            return line, col

        for match in self.find_matches(text):
            line, col = get_line_col(match.start)
            yield match, line, col

    def replace_all(self, text: str) -> str:
        """
        Replace all matches in text.

        Args:
            text: Text to process.

        Returns:
            Text with all matches replaced.
        """
        # Collect matches (already in forward order from find_matches)
        matches = list(self.find_matches(text))

        if not matches:
            return text

        # Build result with forward scan + list join: O(n) instead of O(n*m)
        parts: list[str] = []
        last_end = 0
        for match in matches:
            parts.append(text[last_end : match.start])
            parts.append(match.target)
            last_end = match.end
        parts.append(text[last_end:])

        return "".join(parts)

    def has_matches(self, text: str) -> bool:
        """
        Check if text contains any matches.

        Args:
            text: Text to check.

        Returns:
            True if any matches found.
        """
        try:
            next(self.find_matches(text))
            return True
        except StopIteration:
            return False

    def count_matches(self, text: str) -> int:
        """
        Count number of matches in text.

        Args:
            text: Text to count matches in.

        Returns:
            Number of matches.
        """
        return sum(1 for _ in self.find_matches(text))

    def get_statistics(self, text: str) -> Dict[str, int]:
        """
        Get statistics about matches in text.

        Args:
            text: Text to analyze.

        Returns:
            Dictionary with term counts.
        """
        stats: Dict[str, int] = {}
        for match in self.find_matches(text):
            stats[match.source] = stats.get(match.source, 0) + 1
        return stats
