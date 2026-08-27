"""Tests for the pinned Unicode 17.0 Han block definition."""

from __future__ import annotations

import pytest

from zhtw.unicode_ranges import (
    HAN_BLOCKS,
    UNICODE_VERSION,
    contains_han,
    is_han_character,
    is_han_codepoint,
)


def test_unicode_version_is_pinned() -> None:
    assert UNICODE_VERSION == "17.0.0"


@pytest.mark.parametrize(("name", "start", "end"), HAN_BLOCKS)
def test_every_han_block_includes_both_boundaries(name: str, start: int, end: int) -> None:
    assert is_han_codepoint(start), name
    assert is_han_codepoint(end), name


@pytest.mark.parametrize(("name", "start", "end"), HAN_BLOCKS)
def test_every_han_block_excludes_adjacent_non_block_codepoints(
    name: str, start: int, end: int
) -> None:
    previous_is_another_han_block = any(
        other_end == start - 1
        for other_name, _other_start, other_end in HAN_BLOCKS
        if other_name != name
    )
    next_is_another_han_block = any(
        other_start == end + 1
        for other_name, other_start, _other_end in HAN_BLOCKS
        if other_name != name
    )

    assert is_han_codepoint(start - 1) is previous_is_another_han_block, name
    assert is_han_codepoint(end + 1) is next_is_another_han_block, name


def test_character_and_text_helpers_cover_supplementary_and_compatibility_han() -> None:
    extension_b = chr(0x20000)
    extension_j = chr(0x323B0)
    compatibility = chr(0xF900)

    assert is_han_character(extension_b)
    assert contains_han(f"ASCII {extension_j}")
    assert contains_han(compatibility)


@pytest.mark.parametrize("value", ["", "ab", "A", "😀"])
def test_character_helper_rejects_non_han_values(value: str) -> None:
    assert not is_han_character(value)


def test_codepoint_helper_rejects_non_integer_values() -> None:
    assert not is_han_codepoint(True)
    assert not is_han_codepoint("4e00")  # type: ignore[arg-type]
