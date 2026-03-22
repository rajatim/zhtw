"""字元級轉換（charconv）的測試。"""

from __future__ import annotations

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


@pytest.fixture(autouse=True)
def _clear_charconv_cache():
    """每個測試前清除快取。"""
    clear_cache()
    yield
    clear_cache()


# ──────────────────────────────────────────────
# 字元映射資料完整性
# ──────────────────────────────────────────────


class TestCharmapData:
    """驗證 safe_chars.json 資料品質。"""

    def test_load_charmap(self):
        charmap = load_charmap()
        assert len(charmap) > 1500
        assert isinstance(charmap, dict)

    def test_charmap_count_reasonable(self):
        charmap = load_charmap()
        # 應在 2000-8000 之間（包含擴展區）
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
        """歧義字不應出現在安全映射中。"""
        charmap = load_charmap()
        ambiguous = get_ambiguous_chars()
        for char in ambiguous:
            assert char not in charmap, f"歧義字 '{char}' 出現在 safe charmap 中"

    def test_ambiguous_list_not_empty(self):
        ambiguous = get_ambiguous_chars()
        assert len(ambiguous) > 50  # 至少 50 個歧義字

    def test_well_known_safe_chars(self):
        """常見安全字元應在映射中。"""
        charmap = load_charmap()
        expected = {
            "这": "這",
            "个": "個",
            "说": "說",
            "国": "國",
            "时": "時",
            "会": "會",
            "为": "為",
            "过": "過",
            "还": "還",
            "发": "發",
            "学": "學",
            "车": "車",
        }
        for simplified, traditional in expected.items():
            assert (
                charmap.get(simplified) == traditional
            ), f"{simplified} → 期望 {traditional}, 實際 {charmap.get(simplified)}"

    def test_well_known_ambiguous_excluded(self):
        """已知歧義字不應在安全映射中。"""
        charmap = load_charmap()
        ambiguous_chars = ["后", "里", "干", "只", "台", "复", "系", "面", "折", "采"]
        for char in ambiguous_chars:
            assert char not in charmap, f"歧義字 '{char}' 不應在 safe charmap"


# ──────────────────────────────────────────────
# 字元轉換功能
# ──────────────────────────────────────────────


class TestCharConvert:
    """測試字元級轉換。"""

    def test_basic_conversion(self):
        table = get_translate_table()
        assert char_convert("东", table) == "東"
        assert char_convert("专", table) == "專"

    def test_multiple_chars(self):
        table = get_translate_table()
        result = char_convert("我们说中国话", table)
        assert result == "我們說中國話"

    def test_ambiguous_not_converted(self):
        """歧義字不應被字元層轉換。"""
        table = get_translate_table()
        # 后、面、里、干 是歧義字，不在 charmap 中
        assert char_convert("后", table) == "后"
        assert char_convert("里", table) == "里"
        assert char_convert("干", table) == "干"

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
        result = char_convert("hello 这个 world", table)
        assert result == "hello 這個 world"


# ──────────────────────────────────────────────
# 詞彙層 + 字元層整合
# ──────────────────────────────────────────────


class TestPipelineIntegration:
    """測試詞彙層和字元層協同運作。"""

    @pytest.fixture
    def matcher(self):
        """建立帶有基本詞彙的 matcher。"""
        terms = {"软件": "軟體", "信息": "資訊", "头发": "頭髮"}
        return Matcher(terms)

    @pytest.fixture
    def char_table(self):
        return get_translate_table()

    def test_term_then_char(self, matcher, char_table):
        """詞彙層先跑，字元層補底。"""
        text = "这个软件"
        result, _ = convert_text(text, matcher, fix=True, char_table=char_table)
        # 软件 被詞彙層轉為 軟體，这/个 被字元層轉
        assert result == "這個軟體"

    def test_mixed_real_text(self, matcher, char_table):
        text = "这是一个测试软件"
        result, _ = convert_text(text, matcher, fix=True, char_table=char_table)
        assert "軟體" in result  # 詞彙層
        assert "這" in result  # 字元層
        assert "個" in result  # 字元層
        assert "測試" in result  # 字元層

    def test_ambiguous_in_term_context(self, matcher, char_table):
        """歧義字透過詞庫上下文正確轉換。"""
        text = "头发"
        result, _ = convert_text(text, matcher, fix=True, char_table=char_table)
        assert result == "頭髮"  # 詞庫層處理

    def test_char_convert_with_no_term_matches(self, char_table):
        """即使沒有詞彙匹配，字元層也要運作。"""
        terms = {"不存在的词": "不存在的詞"}
        matcher = Matcher(terms)
        text = "学习编程"
        result, _ = convert_text(text, matcher, fix=True, char_table=char_table)
        assert result == "學習編程"  # 全部由字元層轉換

    def test_without_char_table(self, matcher):
        """不傳 char_table 時，行為和之前一樣。"""
        text = "这个软件"
        result, _ = convert_text(text, matcher, fix=True, char_table=None)
        # 只有詞彙層的 软件→軟體，这/个 不轉
        assert "軟體" in result
        assert "这" in result or "這" in result  # 取決於 这 是否在詞庫中

    def test_ignored_lines_respected(self, matcher, char_table):
        """字元轉換也要尊重忽略指令。"""
        text = "这个软件\n这是测试"
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
        assert lines[1] == "这是测试"  # 第二行完全不轉


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
