"""Tests for lookup module."""
# zhtw:disable

from __future__ import annotations

import pytest
from click.testing import CliRunner

from zhtw.charconv import get_translate_table
from zhtw.cli import main
from zhtw.dictionary import load_dictionary
from zhtw.lookup import lookup_word, lookup_words
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


class TestLookupWordCharLayer:
    """字元層歸因測試。"""

    def test_char_only(self, matcher, char_table):
        """盐 應由字元層處理。"""
        result = lookup_word("盐", matcher, char_table)
        assert result.changed is True
        assert result.output == "鹽"
        assert len(result.details) == 1
        d = result.details[0]
        assert d.source == "盐"
        assert d.target == "鹽"
        assert d.layer == "char"
        assert d.position == 0

    def test_multi_char(self, matcher, char_table):
        """摄入：摄 由字元層轉，入 繁簡同形不出現。"""
        result = lookup_word("摄入", matcher, char_table)
        assert result.changed is True
        assert result.output == "攝入"
        assert len(result.details) == 1
        assert result.details[0].source == "摄"
        assert result.details[0].layer == "char"

    def test_心态(self, matcher, char_table):
        """心态：心 同形不轉，态 由字元層轉。"""
        result = lookup_word("心态", matcher, char_table)
        assert result.changed is True
        assert result.output == "心態"
        assert len(result.details) == 1
        assert result.details[0].source == "态"
        assert result.details[0].layer == "char"


class TestLookupWordMixed:
    """混合層歸因測試。"""

    def test_mixed_layers(self, matcher, char_table):
        """营养：歸因不重疊。"""
        result = lookup_word("营养", matcher, char_table)
        assert result.changed is True
        assert result.output == "營養"
        positions = [d.position for d in result.details]
        assert len(positions) == len(set(positions))

    def test_sentence(self, matcher, char_table):
        """整句：多個轉換點，位置排序正確。"""
        result = lookup_word("摄入量过高会影响心态", matcher, char_table)
        assert result.changed is True
        assert result.output == "攝入量過高會影響心態"
        positions = [d.position for d in result.details]
        assert positions == sorted(positions)
        assert len(positions) == len(set(positions))


class TestLookupWordEdgeCases:
    """邊界條件測試。"""

    def test_no_change(self, matcher, char_table):
        """繁體字不需轉換。"""
        result = lookup_word("台灣", matcher, char_table)
        assert result.changed is False
        assert result.output == "台灣"
        assert result.details == []

    def test_empty_string(self, matcher, char_table):
        """空字串不炸。"""
        result = lookup_word("", matcher, char_table)
        assert result.changed is False
        assert result.output == ""
        assert result.details == []

    def test_no_char_table(self, matcher):
        """不傳 char_table 時只做詞彙層。"""
        result = lookup_word("盐", matcher)
        assert result.changed is False


class TestLookupWords:
    """批次查詢測試。"""

    def test_multiple_words(self, matcher, char_table):
        """多詞批次查詢。"""
        results = lookup_words(["摄入", "盐", "结合", "心态", "营养"], matcher, char_table)
        assert len(results) == 5
        assert all(r.changed for r in results)
        assert results[0].output == "攝入"
        assert results[1].output == "鹽"
        assert results[2].output == "結合"
        assert results[3].output == "心態"
        assert results[4].output == "營養"

    def test_empty_list(self, matcher, char_table):
        """空列表回傳空列表。"""
        results = lookup_words([], matcher, char_table)
        assert results == []


# ──────────────────────────────────────────────
# CLI 整合測試
# ──────────────────────────────────────────────


@pytest.fixture
def runner():
    return CliRunner()


class TestLookupCLI:
    """CLI 整合測試。"""

    def test_multiple_args(self, runner):
        """多個參數模式。"""
        result = runner.invoke(main, ["lookup", "摄入", "盐", "结合"])
        assert result.exit_code == 0
        assert "攝入" in result.output
        assert "鹽" in result.output
        assert "結合" in result.output

    def test_no_change(self, runner):
        """無需轉換時顯示提示。"""
        result = runner.invoke(main, ["lookup", "台灣"])
        assert result.exit_code == 0
        assert "無需轉換" in result.output
