"""字元級轉換（charconv）的測試。"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from zhtw.charconv import (
    char_convert,
    clear_cache,
    get_ambiguous_chars,
    get_charmap_stats,
    get_translate_table,
    load_charmap,
)
from zhtw.converter import convert_text
from zhtw.matcher import Matcher

CHARMAP_PATH = (
    Path(__file__).parent.parent / "src" / "zhtw" / "data" / "charmap" / "safe_chars.json"
)


@pytest.fixture(autouse=True)
def _clear_charconv_cache():
    """每個測試前清除快取。"""
    clear_cache()
    yield
    clear_cache()


# ──────────────────────────────────────────────
# 字元對映資料完整性
# ──────────────────────────────────────────────


class TestCharmapData:
    """驗證 safe_chars.json 資料品質。"""

    def test_file_stats_match_actual_content(self):
        data = json.loads(CHARMAP_PATH.read_text(encoding="utf-8"))
        assert data["stats"]["safe_chars"] == len(data["chars"])
        assert data["stats"]["ambiguous_excluded"] == len(data["ambiguous_excluded"])

    def test_load_charmap(self):
        charmap = load_charmap()
        assert len(charmap) > 1500
        assert isinstance(charmap, dict)

    def test_charmap_count_reasonable(self):
        charmap = load_charmap()
        # 應在 2000-8000 之間（包含擴充套件區）
        assert 2000 <= len(charmap) <= 8000

    def test_keys_are_single_chars(self):
        charmap = load_charmap()
        for key in charmap:
            assert len(key) == 1, f"Key '{key}' 不是單字元"

    def test_values_are_single_chars(self):
        charmap = load_charmap()
        for key, val in charmap.items():
            assert len(val) == 1, f"Value '{val}' for '{key}' 不是單字元"

    def test_no_identity_mapping(self):
        charmap = load_charmap()
        for key, val in charmap.items():
            assert key != val, f"Identity mapping: '{key}' → '{val}'"

    def test_no_ambiguous_chars_in_charmap(self):
        """歧義字不應出現在安全對映中。"""
        charmap = load_charmap()
        ambiguous = get_ambiguous_chars()
        for char in ambiguous:
            assert char not in charmap, f"歧義字 '{char}' 出現在 safe charmap 中"

    def test_ambiguous_list_not_empty(self):
        ambiguous = get_ambiguous_chars()
        assert len(ambiguous) > 50  # 至少 50 個歧義字

    def test_well_known_safe_chars(self):
        """常見安全字元應在對映中。"""
        charmap = load_charmap()
        expected = {
            "這": "這",
            "個": "個",
            "說": "說",
            "國": "國",
            "時": "時",
            "會": "會",
            "為": "為",
            "過": "過",
            "還": "還",
            "發": "發",
            "學": "學",
            "車": "車",
        }
        for simplified, traditional in expected.items():
            assert (
                charmap.get(simplified) == traditional
            ), f"{simplified} → 期望 {traditional}, 實際 {charmap.get(simplified)}"

    def test_well_known_ambiguous_excluded(self):
        """已知歧義字不應在安全對映中。"""
        charmap = load_charmap()
        ambiguous_chars = ["後", "裡", "幹", "只", "台", "複", "系", "面", "折", "採"]
        for char in ambiguous_chars:
            assert char not in charmap, f"歧義字 '{char}' 不應在 safe charmap"

    def test_v12_promoted_safe_chars(self):
        """v1.2 升級到 safe_chars 的字應在 charmap 中。"""
        charmap = load_charmap()
        expected = {
            "帘": "簾",
            "凫": "鳧",
            "坝": "壩",
            "竖": "豎",
            "绣": "繡",
            "绷": "繃",
            "蕴": "蘊",
            "谣": "謠",
            "赃": "贓",
            "酝": "醞",
            "锈": "鏽",
            "颓": "頹",
            "鳄": "鱷",
        }
        for simplified, traditional in expected.items():
            assert charmap.get(simplified) == traditional

    def test_v12_true_ambiguous_chars_remain_excluded(self):
        """v1.2 仍保留為歧義的字不應誤升級到 safe_chars。"""
        charmap = load_charmap()
        ambiguous = set(get_ambiguous_chars())
        for char in ["仆", "尸", "卤", "坛", "弥", "摆", "纤"]:
            assert char not in charmap
            assert char in ambiguous


# ──────────────────────────────────────────────
# 字元轉換功能
# ──────────────────────────────────────────────


class TestCharConvert:
    """測試字元級轉換。"""

    def test_basic_conversion(self):
        table = get_translate_table()
        assert char_convert("東", table) == "東"
        assert char_convert("專", table) == "專"

    def test_multiple_chars(self):
        table = get_translate_table()
        result = char_convert("我們說中國話", table)
        assert result == "我們說中國話"

    def test_ambiguous_not_converted(self):
        """歧義字不應被字元層轉換。"""
        table = get_translate_table()
        # 後、面、裡、幹 是歧義字，不在 charmap 中
        assert char_convert("後", table) == "後"
        assert char_convert("裡", table) == "裡"
        assert char_convert("幹", table) == "幹"

    def test_v12_promoted_chars_convert_in_strict_char_layer(self):
        """v1.2 升級到 safe_chars 的字應在 strict 字元層直接轉換。"""
        table = get_translate_table()
        assert char_convert("帘凫坝竖绣绷蕴谣赃酝锈颓鳄", table) == "簾鳧壩豎繡繃蘊謠贓醞鏽頹鱷"

    def test_traditional_unchanged(self):
        """已經是繁體的字不應變。"""
        table = get_translate_table()
        assert char_convert("國語", table) == "國語"
        assert char_convert("學習", table) == "學習"

    def test_non_chinese_unchanged(self):
        """非中文字元不受影響。"""
        table = get_translate_table()
        assert char_convert("hello world", table) == "hello world"
        assert char_convert("123!@#", table) == "123!@#"
        assert char_convert("", table) == ""

    def test_mixed_content(self):
        table = get_translate_table()
        result = char_convert("hello 這個 world", table)
        assert result == "hello 這個 world"


# ──────────────────────────────────────────────
# 詞彙層 + 字元層整合
# ──────────────────────────────────────────────


class TestPipelineIntegration:
    """測試詞彙層和字元層協同運作。"""

    @pytest.fixture
    def matcher(self):
        """建立帶有基本詞彙的 matcher。"""
        terms = {"軟體": "軟體", "資訊": "資訊", "頭髮": "頭髮"}
        return Matcher(terms)

    @pytest.fixture
    def char_table(self):
        return get_translate_table()

    def test_term_then_char(self, matcher, char_table):
        """詞彙層先跑，字元層補底。"""
        text = "這個軟體"
        result, _ = convert_text(text, matcher, fix=True, char_table=char_table)
        # 軟體 被詞彙層轉為 軟體，這/個 被字元層轉
        assert result == "這個軟體"

    def test_mixed_real_text(self, matcher, char_table):
        text = "這是一個測試軟體"
        result, _ = convert_text(text, matcher, fix=True, char_table=char_table)
        assert "軟體" in result  # 詞彙層
        assert "這" in result  # 字元層
        assert "個" in result  # 字元層
        assert "測試" in result  # 字元層

    def test_ambiguous_in_term_context(self, matcher, char_table):
        """歧義字透過詞庫上下文正確轉換。"""
        text = "頭髮"
        result, _ = convert_text(text, matcher, fix=True, char_table=char_table)
        assert result == "頭髮"  # 詞庫層處理

    def test_char_convert_with_no_term_matches(self, char_table):
        """即使沒有詞彙匹配，字元層也要運作。"""
        terms = {"不存在的詞": "不存在的詞"}
        matcher = Matcher(terms)
        text = "學習程式設計"
        result, _ = convert_text(text, matcher, fix=True, char_table=char_table)
        assert result == "學習程式設計"  # 全部由字元層轉換

    def test_without_char_table(self, matcher):
        """不傳 char_table 時，行為和之前一樣。"""
        text = "這個軟體"
        result, _ = convert_text(text, matcher, fix=True, char_table=None)
        # 只有詞彙層的 軟體→軟體，這/個 不轉
        assert "軟體" in result
        assert "這" in result or "這" in result  # 取決於 這 是否在詞庫中

    def test_ignored_lines_respected(self, matcher, char_table):
        """字元轉換也要尊重忽略指令。"""
        text = "這個軟體\n這是測試"
        # 忽略第二行
        result, _ = convert_text(
            text,
            matcher,
            fix=True,
            ignored_lines={2},
            char_table=char_table,
        )
        lines = result.split("\n")
        assert "軟體" in lines[0]  # 第一行正常轉換
        assert lines[1] == "這是測試"  # 第二行完全不轉


# ──────────────────────────────────────────────
# 統計功能
# ──────────────────────────────────────────────


class TestCharmapStats:
    def test_stats_keys(self):
        stats = get_charmap_stats()
        assert "safe_chars" in stats
        assert "ambiguous_excluded" in stats
        assert "total_coverage" in stats

    def test_stats_values(self):
        stats = get_charmap_stats()
        assert stats["safe_chars"] > 2000
        assert stats["ambiguous_excluded"] > 50
        assert stats["total_coverage"] == stats["safe_chars"] + stats["ambiguous_excluded"]


# ──────────────────────────────────────────────
# 快取機制
# ──────────────────────────────────────────────


class TestCache:
    def test_cache_returns_same_object(self):
        table1 = get_translate_table()
        table2 = get_translate_table()
        assert table1 is table2  # 同一個物件

    def test_clear_cache(self):
        table1 = get_translate_table()
        clear_cache()
        table2 = get_translate_table()
        assert table1 is not table2  # 清除後重新載入
        assert table1 == table2  # 但內容相同
