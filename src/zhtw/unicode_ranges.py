"""Unicode 17.0 Han block ranges used by scanning and term import.

The ranges are pinned to Unicode 17.0.0, Chapter 18, Table 18-1:
https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-18/
"""

from __future__ import annotations

UNICODE_VERSION = "17.0.0"

# Inclusive block boundaries. This intentionally follows the Unicode block
# definition used by the approved 4.5.0 contract, including unassigned slots.
HAN_BLOCKS: tuple[tuple[str, int, int], ...] = (
    ("CJK Unified Ideographs Extension A", 0x3400, 0x4DBF),
    ("CJK Unified Ideographs", 0x4E00, 0x9FFF),
    ("CJK Compatibility Ideographs", 0xF900, 0xFAFF),
    ("CJK Unified Ideographs Extension B", 0x20000, 0x2A6DF),
    ("CJK Unified Ideographs Extension C", 0x2A700, 0x2B73F),
    ("CJK Unified Ideographs Extension D", 0x2B740, 0x2B81F),
    ("CJK Unified Ideographs Extension E", 0x2B820, 0x2CEAF),
    ("CJK Unified Ideographs Extension F", 0x2CEB0, 0x2EBEF),
    ("CJK Unified Ideographs Extension I", 0x2EBF0, 0x2EE5F),
    ("CJK Compatibility Ideographs Supplement", 0x2F800, 0x2FA1F),
    ("CJK Unified Ideographs Extension G", 0x30000, 0x3134F),
    ("CJK Unified Ideographs Extension H", 0x31350, 0x323AF),
    ("CJK Unified Ideographs Extension J", 0x323B0, 0x3347F),
)


def is_han_codepoint(codepoint: int) -> bool:
    """Return whether an integer is inside a supported Han block."""

    if isinstance(codepoint, bool) or not isinstance(codepoint, int):
        return False
    return any(start <= codepoint <= end for _name, start, end in HAN_BLOCKS)


def is_han_character(value: str) -> bool:
    """Return whether a one-codepoint string is inside a supported Han block."""

    return isinstance(value, str) and len(value) == 1 and is_han_codepoint(ord(value))


def contains_han(text: str) -> bool:
    """Return whether text contains a code point from a supported Han block."""

    return any(is_han_codepoint(ord(character)) for character in text)
