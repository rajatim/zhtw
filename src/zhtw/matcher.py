"""
Matcher module using Aho-Corasick algorithm for efficient multi-pattern matching.

This allows O(n) scanning of text regardless of the number of terms in the dictionary.
"""

from dataclasses import dataclass
from typing import Dict, Iterator

import ahocorasick


@dataclass
class Match:
    """Represents a match found in text."""

    start: int  # Start position in text
    end: int  # End position in text (exclusive)
    source: str  # Original term found
    target: str  # Replacement term


class Matcher:
    """
    Aho-Corasick based matcher for efficient multi-pattern matching.

    Example:
        >>> terms = {"软件": "軟體", "硬件": "硬體"}
        >>> matcher = Matcher(terms)
        >>> list(matcher.find_matches("这是软件和硬件"))
        [Match(start=2, end=4, source='软件', target='軟體'),
         Match(start=5, end=7, source='硬件', target='硬體')]
    """

    def __init__(self, terms: Dict[str, str]):
        """
        Initialize matcher with a dictionary of terms.

        Args:
            terms: Dictionary mapping source terms to target terms.
        """
        self.terms = terms
        self.automaton = self._build_automaton()

    def _build_automaton(self) -> ahocorasick.Automaton:
        """Build Aho-Corasick automaton from terms."""
        automaton = ahocorasick.Automaton()

        for source, target in self.terms.items():
            # Store both source and target for each pattern
            automaton.add_word(source, (source, target))

        automaton.make_automaton()
        return automaton

    def find_matches(self, text: str) -> Iterator[Match]:
        """
        Find all matches in text.

        Uses longest-match-first strategy to avoid substring issues.
        For example, if both "算法" and "演算法" are in the dictionary,
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

        # Sort by start position, then by length (longer first)
        all_matches.sort(key=lambda m: (m.start, -(m.end - m.start)))

        # Build "protected ranges" from identity mappings
        # These ranges should not be modified by overlapping conversions
        # This ensures "檔案"→"檔案" protects against "文檔"→"文件"
        # when they overlap in "中文檔案"
        protected: set[int] = set()
        for match in all_matches:
            if match.source == match.target:
                protected.update(range(match.start, match.end))

        # Filter overlapping matches
        last_end = -1
        for match in all_matches:
            if match.start >= last_end:
                # Skip if this conversion overlaps with a protected range
                if match.source != match.target:
                    if any(i in protected for i in range(match.start, match.end)):
                        continue
                last_end = match.end
                # Skip identity matches (no actual change needed)
                if match.source != match.target:
                    yield match

    def find_matches_with_lines(
        self, text: str
    ) -> Iterator[tuple[Match, int, int]]:
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
        # Collect matches and sort by position (in reverse to replace from end)
        matches = list(self.find_matches(text))

        if not matches:
            return text

        # Sort by start position in reverse
        matches.sort(key=lambda m: m.start, reverse=True)

        # Replace from end to start to preserve positions
        result = text
        for match in matches:
            result = result[: match.start] + match.target + result[match.end :]

        return result

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
