"""Tests for lookup module."""
# zhtw:disable

from __future__ import annotations

import pytest

from zhtw.charconv import get_translate_table
from zhtw.dictionary import load_dictionary
from zhtw.lookup import lookup_word
from zhtw.matcher import Matcher


@pytest.fixture
def matcher():
    """載入完整詞庫的 Matcher。"""
    return Matcher(load_dictionary())


@pytest.fixture
def char_table():
    """載入字元轉換表。"""
    return get_translate_table()


class TestLookupWordTermLayer:
    """詞彙層歸因測試。"""

    def test_term_match(self, matcher, char_table):
        """结合 應由詞彙層處理。"""
        result = lookup_word("结合", matcher, char_table)
        assert result.changed is True
        assert result.output == "結合"
        assert len(result.details) == 1
        d = result.details[0]
        assert d.source == "结合"
        assert d.target == "結合"
        assert d.layer == "term"
        assert d.position == 0
