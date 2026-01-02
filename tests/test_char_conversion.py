"""測試簡繁字形轉換（一對多危險字）"""
# zhtw:disable  # 測試案例需要簡體字

import pytest

from zhtw.dictionary import load_dictionary
from zhtw.matcher import Matcher


@pytest.fixture
def matcher():
    """建立包含完整詞庫的 matcher"""
    terms = load_dictionary(sources=["cn", "hk"])
    return Matcher(terms)


class TestSafeChars:
    """安全詞彙（一對一）"""

    def test_common_words(self, matcher: Matcher):
        """常見詞彙正常轉換"""
        cases = {
            "测试": "測試",
            "时间": "時間",
            "问题": "問題",
            "开发": "開發",
            "环境": "環境",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"


class TestFa:
    """发 → 發/髮"""

    def test_fa_default(self, matcher: Matcher):
        """預設轉「發」，但特定詞彙有台灣用語優先"""
        cases = {
            "发送": "傳送",  # base.json 有台灣特定翻譯
            "发布": "發布",
            "发展": "發展",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"

    def test_fa_hair(self, matcher: Matcher):
        """特例轉「髮」"""
        cases = {
            "头发": "頭髮",
            "理发": "理髮",
            "白发": "白髮",
            "洗发": "洗髮",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"


class TestMian:
    """面 → 面/麵"""

    def test_mian_default(self, matcher: Matcher):
        """面 詞彙已加入詞庫"""
        cases = {
            "面试": "面試",
            "面积": "面積",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"

    def test_mian_food(self, matcher: Matcher):
        """食物轉「麵」"""
        cases = {
            "面条": "麵條",
            "面包": "麵包",
            "方便面": "泡麵",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"


class TestLi:
    """里 → 裡/里"""

    def test_li_inside(self, matcher: Matcher):
        """內部轉「裡」"""
        cases = {
            "里面": "裡面",
            "心里": "心裡",
            "这里": "這裡",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"

    def test_li_distance(self, matcher: Matcher):
        """距離保持「里」（Identity 保護）"""
        cases = {
            "公里": "公里",
            "英里": "英里",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"


class TestHou:
    """后 → 後/后"""

    def test_hou_time(self, matcher: Matcher):
        """時間/位置轉「後」"""
        cases = {
            "之后": "之後",
            "后来": "後來",
            "最后": "最後",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"

    def test_hou_queen(self, matcher: Matcher):
        """皇后保持「后」"""
        assert matcher.replace_all("皇后") == "皇后"


class TestFu:
    """复 → 複/復"""

    def test_fu_complex(self, matcher: Matcher):
        """複雜轉「複」"""
        cases = {
            "复杂": "複雜",
            "复习": "複習",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"

    def test_fu_recover(self, matcher: Matcher):
        """復原轉「復」，恢复軟體用語轉「還原」"""
        cases = {
            "复原": "復原",
            "恢复": "還原",  # base.json 的軟體特定翻譯
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"


class TestZhun:
    """准 → 準/准"""

    def test_zhun_accurate(self, matcher: Matcher):
        """準確轉「準」"""
        cases = {
            "准确": "準確",
            "准备": "準備",
            "准时": "準時",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"

    def test_zhun_permit(self, matcher: Matcher):
        """批准保持「准」"""
        cases = {
            "批准": "批准",
            "准许": "准許",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"


class TestFan:
    """范 → 範/范"""

    def test_fan_scope(self, matcher: Matcher):
        """範圍轉「範」"""
        cases = {
            "范围": "範圍",
            "范本": "範本",
            "范例": "範例",
            "示范": "示範",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"


class TestJi:
    """几 → 幾/几"""

    def test_ji_how_many(self, matcher: Matcher):
        """幾乎轉「幾」"""
        cases = {
            "几乎": "幾乎",
            "几何": "幾何",
            "几个": "幾個",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"

    def test_ji_table(self, matcher: Matcher):
        """茶几保持「几」"""
        assert matcher.replace_all("茶几") == "茶几"


class TestMixedText:
    """混合文本測試"""

    def test_sentence(self, matcher: Matcher):
        """完整句子測試"""
        cases = {
            "测试时间是10公里": "測試時間是10公里",
            "发送头发图片": "傳送頭髮圖片",  # 发送 → 傳送（base.json）
            "面试之后吃面条": "面試之後吃麵條",
            "复杂的恢复过程": "複雜的還原過程",  # 恢复軟體用語轉「還原」
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"

    def test_no_false_positive(self, matcher: Matcher):
        """確保不會誤轉已是繁體的字"""
        cases = {
            "測試": "測試",
            "時間": "時間",
            "頭髮": "頭髮",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should stay as {expected}"


# Phase 2 新增測試
class TestYun:
    """云 → 雲/云"""

    def test_yun_cloud(self, matcher: Matcher):
        """雲彩轉「雲」"""
        cases = {
            "云": "雲",
            "白云": "白雲",
            "云端": "雲端",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"

    def test_yun_literary(self, matcher: Matcher):
        """古文「云」保持"""
        cases = {
            "人云亦云": "人云亦云",
            "子曰诗云": "子曰詩云",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should stay as {expected}"


class TestDang:
    """当 → 當"""

    def test_dang_time(self, matcher: Matcher):
        """當時轉「當」"""
        cases = {
            "当时": "當時",
            "当然": "當然",
            "当前": "當前",
            "应当": "應當",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"


class TestZang:
    """脏 → 髒/臟"""

    def test_zang_dirty(self, matcher: Matcher):
        """骯髒轉「髒」"""
        cases = {
            "肮脏": "骯髒",
            "脏话": "髒話",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"

    def test_zang_organ(self, matcher: Matcher):
        """內臟轉「臟」"""
        cases = {
            "心脏": "心臟",
            "内脏": "內臟",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"


class TestShe:
    """舍 → 捨/舍"""

    def test_she_give_up(self, matcher: Matcher):
        """捨棄轉「捨」"""
        cases = {
            "舍不得": "捨不得",
            "取舍": "取捨",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"

    def test_she_building(self, matcher: Matcher):
        """宿舍保持「舍」"""
        cases = {
            "宿舍": "宿舍",
            "校舍": "校舍",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should stay as {expected}"


class TestBing:
    """并 → 並"""

    def test_bing_and(self, matcher: Matcher):
        """並且轉「並」"""
        cases = {
            "并且": "並且",
            "并不": "並不",
            "合并": "合併",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"
