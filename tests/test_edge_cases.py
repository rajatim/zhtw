"""邊界案例測試。驗證極端輸入的穩健性。"""
# zhtw:disable  # 測試案例需要簡體字輸入

import pytest

from zhtw.charconv import get_translate_table
from zhtw.dictionary import load_dictionary
from zhtw.matcher import Matcher


@pytest.fixture
def terms():
    """載入 CN 詞庫。"""
    return load_dictionary(sources=["cn"])


@pytest.fixture
def matcher(terms):
    """建立 Matcher。"""
    return Matcher(terms)


@pytest.fixture
def char_table():
    """取得字元級轉換表。"""
    return get_translate_table()


def convert(text, matcher, char_table):
    """完整兩層轉換：詞彙層 + 字元層。"""
    result = matcher.replace_all(text)
    return result.translate(char_table)


# ──────────────────────────────────────────────
# 空字串與最小輸入
# ──────────────────────────────────────────────


class TestEmptyAndMinimal:
    """空字串與最小輸入。"""

    def test_empty_string(self, matcher, char_table):
        """空字串輸入應回傳空字串。"""
        assert convert("", matcher, char_table) == ""

    def test_whitespace_only(self, matcher, char_table):
        """純空白字元應原樣保留。"""
        assert convert("   ", matcher, char_table) == "   "

    def test_single_simplified_char(self, matcher, char_table):
        """單一簡體字應正確轉換。"""
        assert convert("这", matcher, char_table) == "這"

    def test_single_traditional_char(self, matcher, char_table):
        """已是繁體的單字不應改變。"""
        assert convert("這", matcher, char_table) == "這"

    def test_single_ascii(self, matcher, char_table):
        """單一 ASCII 字元應原樣保留。"""
        assert convert("a", matcher, char_table) == "a"

    def test_newline_only(self, matcher, char_table):
        """純換行字元應原樣保留。"""
        assert convert("\n", matcher, char_table) == "\n"


# ──────────────────────────────────────────────
# 特殊 Unicode 字元
# ──────────────────────────────────────────────


class TestSpecialUnicode:
    """特殊 Unicode 字元。"""

    def test_emoji_preserved(self, matcher, char_table):
        """Emoji 應保留，簡體部分正確轉換。"""
        result = convert("这个软件很好\U0001f44d", matcher, char_table)
        assert "\U0001f44d" in result
        assert "軟體" in result

    def test_zero_width_chars(self, matcher, char_table):
        """零寬空格不應導致轉換中斷。"""
        text = "软\u200b件"
        result = convert(text, matcher, char_table)
        # 零寬空格把「软件」拆開了，詞彙層不會匹配
        # 但字元層仍應轉換各自的字元
        assert "\u200b" in result

    def test_cjk_extension_b(self, matcher, char_table):
        """CJK 擴展 B 區罕見字應安全通過。"""
        text = "测试\U00020000字"
        result = convert(text, matcher, char_table)
        assert "\U00020000" in result

    def test_fullwidth_ascii(self, matcher, char_table):
        """全形 ASCII 字元應保留。"""
        assert convert("\uff21\uff22\uff23", matcher, char_table) == "\uff21\uff22\uff23"

    def test_bom_handling(self, matcher, char_table):
        """BOM 開頭的文字不應導致轉換中斷。"""
        text = "\ufeff这个软件"
        result = convert(text, matcher, char_table)
        assert "軟體" in result
        assert result.startswith("\ufeff")


# ──────────────────────────────────────────────
# 超長文字處理
# ──────────────────────────────────────────────


class TestLongText:
    """超長文字處理。"""

    def test_repeated_text_1mb(self, matcher, char_table):
        """1MB 重複簡體文字應正確轉換。"""
        unit = "这个软件很好用"
        # 每個 unit 約 21 bytes (UTF-8)，重複到約 1MB
        repeat_count = 1_000_000 // (len(unit.encode("utf-8")))
        text = unit * repeat_count
        result = convert(text, matcher, char_table)
        assert "软件" not in result
        assert "軟體" in result
        # 驗證結果長度合理（詞彙層替換後長度可能變化）
        assert len(result) > 0

    def test_single_long_line(self, matcher, char_table):
        """10 萬字元單行應正確處理。"""
        unit = "这个数据"
        text = unit * 25_000  # 約 100K 字元
        result = convert(text, matcher, char_table)
        assert "資料" in result
        assert len(result) > 0

    def test_many_short_lines(self, matcher, char_table):
        """一萬行短文字應正確處理。"""
        lines = ["这是信息"] * 10_000
        text = "\n".join(lines)
        result = convert(text, matcher, char_table)
        result_lines = result.split("\n")
        assert len(result_lines) == 10_000
        assert all("資訊" in line for line in result_lines)


# ──────────────────────────────────────────────
# 混合腳本文字
# ──────────────────────────────────────────────


class TestMixedScripts:
    """混合腳本文字。"""

    def test_chinese_english(self, matcher, char_table):
        """中英夾雜：簡體轉換，英文保留。"""
        result = convert("hello这个world", matcher, char_table)
        assert result == "hello這個world"

    def test_chinese_japanese(self, matcher, char_table):
        """中日夾雜：簡體部分轉換，日文假名保留。"""
        result = convert("这个寿司おいしい", matcher, char_table)
        assert "おいしい" in result
        assert "這" in result

    def test_chinese_korean(self, matcher, char_table):
        """中韓夾雜：簡體部分轉換，韓文保留。"""
        result = convert("这个韩国菜한국어", matcher, char_table)
        assert "한국어" in result
        assert "這" in result

    def test_chinese_arabic(self, matcher, char_table):
        """中阿夾雜：阿拉伯數字保留。"""
        result = convert("这个数字\u0661\u0662\u0663", matcher, char_table)
        assert "\u0661\u0662\u0663" in result
        assert "這" in result

    def test_all_ascii(self, matcher, char_table):
        """純 ASCII 文字不應有任何變化。"""
        text = "Hello World 123"
        assert convert(text, matcher, char_table) == text


# ──────────────────────────────────────────────
# 重複字元
# ──────────────────────────────────────────────


class TestRepeatedCharacters:
    """重複字元。"""

    def test_repeated_simplified(self, matcher, char_table):
        """重複簡體字應每個都轉換。"""
        assert convert("这这这这这", matcher, char_table) == "這這這這這"

    def test_repeated_term(self, matcher, char_table):
        """重複詞彙應每次都正確轉換。"""
        assert convert("软件软件软件", matcher, char_table) == "軟體軟體軟體"

    def test_alternating(self, matcher, char_table):
        """簡體字與 ASCII 交替出現。"""
        assert convert("这a这a这", matcher, char_table) == "這a這a這"


# ──────────────────────────────────────────────
# 特殊文字模式
# ──────────────────────────────────────────────


class TestSpecialPatterns:
    """特殊文字模式。"""

    def test_overlapping_terms(self):
        """Aho-Corasick 重疊匹配：較長詞優先。"""
        # 「操作」和「操作系统」都可能匹配，應選最長
        terms = {"操作系统": "作業系統", "操作": "操作"}
        matcher = Matcher(terms)
        result = matcher.replace_all("这个操作系统")
        assert "作業系統" in result

    def test_term_at_boundary(self, matcher, char_table):
        """詞彙出現在字串開頭和結尾。"""
        assert "軟體" == convert("软件", matcher, char_table).rstrip()
        result = convert("用软件", matcher, char_table)
        assert result.endswith("軟體")
        result = convert("软件好", matcher, char_table)
        assert result.startswith("軟體")

    def test_consecutive_terms(self, matcher, char_table):
        """連續詞彙（無分隔）應分別轉換。"""
        result = convert("软件硬件", matcher, char_table)
        assert "軟體" in result
        assert "硬體" in result

    def test_nested_lookalike(self):
        """看起來像詞彙但不是的文字不應被轉換。"""
        # 只有「软件」是詞，「软」不是詞 → 「软」交給字元層
        terms = {"软件": "軟體"}
        matcher = Matcher(terms)
        result = matcher.replace_all("软的东西")
        # 「软」不在詞庫中，matcher 不處理
        assert "软" in result

    def test_numbers_in_chinese(self, matcher, char_table):
        """中文中夾帶數字不影響前後詞彙轉換。"""
        result = convert("第3个软件", matcher, char_table)
        assert "3" in result
        assert "軟體" in result
        assert "個" in result
