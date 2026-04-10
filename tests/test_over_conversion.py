"""過度轉換偵測測試。驗證不應被轉換的文字不會被誤轉。"""
# zhtw:disable  # 測試案例需要簡體字輸入

import pytest

from zhtw.charconv import get_translate_table
from zhtw.converter import convert_text
from zhtw.dictionary import load_dictionary
from zhtw.matcher import Matcher


@pytest.fixture(scope="module")
def matcher():
    """建立包含完整詞庫的 matcher。"""
    terms = load_dictionary(sources=["cn"])
    return Matcher(terms)


@pytest.fixture(scope="module")
def char_table():
    """取得字元級轉換表。"""
    return get_translate_table()


def convert(text: str, matcher: Matcher, char_table: dict) -> str:
    """走實際 converter pipeline，避免測試複製過時邏輯。"""
    result, _ = convert_text(text, matcher, fix=True, char_table=char_table)
    return result


# ---------------------------------------------------------------------------
# TestTraditionalPassthrough
# ---------------------------------------------------------------------------
class TestTraditionalPassthrough:
    """已經是繁體的文字應原封不動通過。"""

    def test_traditional_sentence_unchanged(self, matcher, char_table):
        """純繁體日常句子應完全不變。"""
        text = "台灣是個美麗的地方"
        assert convert(text, matcher, char_table) == text

    def test_traditional_technical(self, matcher, char_table):
        """繁體技術用語應完全不變。"""
        text = "這個軟體的記憶體使用量很大"
        assert convert(text, matcher, char_table) == text

    def test_traditional_mixed(self, matcher, char_table):
        """繁體網路設定句子應完全不變。"""
        text = "電腦的網路設定"
        assert convert(text, matcher, char_table) == text


# ---------------------------------------------------------------------------
# TestProperNounPreservation
# ---------------------------------------------------------------------------
class TestProperNounPreservation:
    """專有名詞不被誤轉。"""

    def test_japanese_kanji_untouched(self, matcher, char_table):
        """日文漢字不應被改動。"""
        assert convert("東京", matcher, char_table) == "東京"
        assert convert("大阪", matcher, char_table) == "大阪"

    def test_names_preserved(self, matcher, char_table):
        """中文人名的「周」不應被轉成「週」。"""
        result = convert("周杰倫", matcher, char_table)
        assert "周" in result
        assert "週" not in result

    def test_brand_names(self, matcher, char_table):
        """品牌名「周大福」不應被轉成「週大福」。"""
        result = convert("周大福", matcher, char_table)
        assert "周" in result
        assert "週" not in result


# ---------------------------------------------------------------------------
# TestCommonFalsePositives
# ---------------------------------------------------------------------------
class TestCommonFalsePositives:
    """常見誤轉案例。以 parametrize 驗證每個 (輸入, 必須包含, 不可包含)。"""

    @pytest.mark.parametrize(
        "source, must_contain, must_not_contain",
        [
            # 周 vs 週：非「星期/週期」語境不應轉 週
            ("众所周知", "周知", "週知"),
            ("周围环境", "周圍", "週圍"),
            ("周到的服务", "周到", "週到"),
            # 表 vs 錶：非手錶語境不應轉 錶（表情包 → 貼圖包 是台灣用語，屬正常轉換）
            ("表情包", "貼圖包", "錶"),
            # 合 不應轉 閤
            ("合理的方案", "合理", "閤理"),
            # 才 不應轉 纔
            ("才能成功", "才能", "纔能"),
            # 歷史 不應多出額外字元
            ("历史悠久", "歷史", None),
            # 斗（量詞）不應轉 鬥
            ("一斗米", "斗", "鬥"),
            # 后（皇后）不應轉 後
            ("皇后驾到", "皇后", None),
            # 几（小桌）不應轉 幾
            ("几案上", "几案", "幾案"),
        ],
        ids=[
            "众所周知-not-週知",
            "周围-not-週圍",
            "周到-not-週到",
            "表情-not-錶情",
            "合理-not-閤理",
            "才能-not-纔能",
            "历史-no-extra-chars",
            "一斗米-not-鬥",
            "皇后-not-後",
            "几案-not-幾案",
        ],
    )
    def test_no_false_positive(self, matcher, char_table, source, must_contain, must_not_contain):
        """驗證常見易誤轉詞彙不會被錯誤轉換。"""
        result = convert(source, matcher, char_table)
        assert must_contain in result, f"轉換結果 {result!r} 應包含 {must_contain!r}"
        if must_not_contain is not None:
            assert (
                must_not_contain not in result
            ), f"轉換結果 {result!r} 不應包含 {must_not_contain!r}"


# ---------------------------------------------------------------------------
# TestNoOverConversionInSentences
# ---------------------------------------------------------------------------
class TestNoOverConversionInSentences:
    """完整句子中無過度轉換。"""

    def test_it_article(self, matcher, char_table):
        """IT 文章段落：關鍵術語正確轉換，無過度轉換。"""
        source = "在软件开发过程中，代码质量和测试覆盖率非常重要。"
        result = convert(source, matcher, char_table)
        assert "軟體" in result
        assert "開發" in result
        assert "程式碼" in result
        # 不應出現簡體殘留
        assert "软" not in result
        assert "质" not in result

    def test_daily_conversation(self, matcher, char_table):
        """日常對話段落：自然轉換，無奇怪用字。"""
        source = "今天天气真好，我们出去散步吧。晚上一起吃饭怎么样？"
        result = convert(source, matcher, char_table)
        assert "天氣" in result
        assert "我們" in result
        assert "吃飯" in result
        assert "怎麼樣" in result
        # 不應有簡體殘留
        assert "气" not in result
        assert "们" not in result

    def test_literary_text(self, matcher, char_table):
        """古典/文學文字：已是繁體不應被引入多餘古字。"""
        text = "春風又綠江南岸，明月何時照我還。"
        result = convert(text, matcher, char_table)
        assert result == text, f"文學文字不應被改動：{result!r}"


# ---------------------------------------------------------------------------
# TestMixedLanguageStability
# ---------------------------------------------------------------------------
class TestMixedLanguageStability:
    """混合語言文字穩定性。"""

    def test_chinese_english_mix(self, matcher, char_table):
        """中英混合：英文部分不受影響。"""
        source = "这个API的response很快"
        result = convert(source, matcher, char_table)
        assert "這個" in result
        assert "API" in result
        assert "response" in result

    def test_code_comments(self, matcher, char_table):
        """程式碼註釋：中文轉換，程式碼不變。"""
        source = "// 这是注释 var x = 1"
        result = convert(source, matcher, char_table)
        assert "註釋" in result
        assert "var x = 1" in result
        assert "//" in result

    def test_urls_unchanged(self, matcher, char_table):
        """包含 URL 的文字：URL 不被破壞。"""
        source = "请访问 https://www.google.com 获取更多信息"
        result = convert(source, matcher, char_table)
        assert "https://www.google.com" in result
        # 中文部分仍應被轉換
        assert "請" in result

    def test_numbers_unchanged(self, matcher, char_table):
        """數字不應被改動。"""
        source = "第3个版本"
        result = convert(source, matcher, char_table)
        assert "3" in result
        assert "個" in result


# ---------------------------------------------------------------------------
# TestPunctuationHandling
# ---------------------------------------------------------------------------
class TestPunctuationHandling:
    """標點符號處理。"""

    def test_chinese_punctuation_preserved(self, matcher, char_table):
        """中文標點符號不應被改動。"""
        text = "你好，世界！這是測試。真的嗎？"
        result = convert(text, matcher, char_table)
        for punct in "，。！？":
            assert punct in result, f"中文標點 {punct!r} 應被保留"

    def test_english_punctuation_preserved(self, matcher, char_table):
        """英文標點符號不應被改動。"""
        source = "测试: a, b, c. done!"
        result = convert(source, matcher, char_table)
        for punct in ",:,.!":
            assert punct in result, f"英文標點 {punct!r} 應被保留"

    def test_brackets_preserved(self, matcher, char_table):
        """各類括號不應被改動。"""
        text = "（圓括號）[方括號]{花括號}《書名號》"
        result = convert(text, matcher, char_table)
        for bracket in ["（", "）", "[", "]", "{", "}", "《", "》"]:
            assert bracket in result, f"括號 {bracket!r} 應被保留"
