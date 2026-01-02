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


# Phase 3 新增測試
class TestJuan:
    """卷 → 捲/卷"""

    def test_juan_roll(self, matcher: Matcher):
        """捲起轉「捲」"""
        cases = {
            "卷起": "捲起",
            "卷入": "捲入",
            "席卷": "席捲",
            "卷土重来": "捲土重來",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"

    def test_juan_volume(self, matcher: Matcher):
        """書卷保持「卷」"""
        cases = {
            "试卷": "試卷",
            "画卷": "畫卷",
            "卷宗": "卷宗",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should stay as {expected}"


class TestXu:
    """须 → 鬚/須"""

    def test_xu_beard(self, matcher: Matcher):
        """鬍鬚轉「鬚」"""
        cases = {
            "胡须": "鬍鬚",
            "须发": "鬚髮",
            "触须": "觸鬚",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"

    def test_xu_must(self, matcher: Matcher):
        """必須轉「須」"""
        cases = {
            "必须": "必須",
            "无须": "無須",
            "须知": "須知",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"


class TestHu:
    """胡 → 鬍"""

    def test_hu_beard(self, matcher: Matcher):
        """鬍子轉「鬍」"""
        cases = {
            "胡子": "鬍子",
            "刮胡子": "刮鬍子",
            "大胡子": "大鬍子",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"

    def test_hu_nonsense(self, matcher: Matcher):
        """胡說保持「胡」"""
        cases = {
            "胡说": "胡說",
            "胡闹": "胡鬧",
            "胡同": "胡同",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should stay as {expected}"


class TestJin:
    """尽 → 盡/儘"""

    def test_jin_exhaust(self, matcher: Matcher):
        """盡力轉「盡」"""
        cases = {
            "尽力": "盡力",
            "尽情": "盡情",
            "穷尽": "窮盡",
            "用尽": "用盡",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"

    def test_jin_despite(self, matcher: Matcher):
        """儘管轉「儘」"""
        cases = {
            "尽管": "儘管",
            "尽量": "儘量",
            "尽快": "儘快",
            "尽可能": "儘可能",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"


class TestYu2:
    """于 → 於"""

    def test_yu_at(self, matcher: Matcher):
        """於轉「於」"""
        cases = {
            "于是": "於是",
            "对于": "對於",
            "由于": "由於",
            "属于": "屬於",
            "终于": "終於",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"


class TestYou:
    """游 → 遊/游"""

    def test_you_travel(self, matcher: Matcher):
        """旅遊轉「遊」"""
        cases = {
            "旅游": "旅遊",
            "游客": "遊客",
            "游戏": "遊戲",
            "漫游": "漫遊",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"

    def test_you_swim(self, matcher: Matcher):
        """游泳保持「游」"""
        cases = {
            "游泳": "游泳",
            "游水": "游水",
            "蛙泳": "蛙泳",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should stay as {expected}"


class TestCai:
    """采 → 採/采"""

    def test_cai_gather(self, matcher: Matcher):
        """採集轉「採」"""
        cases = {
            "采集": "採集",
            "采访": "採訪",
            "采取": "採取",
            "开采": "開採",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"

    def test_cai_style(self, matcher: Matcher):
        """風采保持「采」"""
        cases = {
            "风采": "風采",
            "神采": "神采",
            "文采": "文采",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should stay as {expected}"


class TestBiao:
    """表 → 錶"""

    def test_biao_watch(self, matcher: Matcher):
        """手錶轉「錶」"""
        cases = {
            "手表": "手錶",
            "腕表": "腕錶",
            "怀表": "懷錶",
            "秒表": "碼錶",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"

    def test_biao_surface(self, matcher: Matcher):
        """表面保持「表」"""
        cases = {
            "表面": "表面",
            "表示": "表示",
            "代表": "代表",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should stay as {expected}"


class TestZheng2:
    """症 → 癥"""

    def test_zheng_symptom(self, matcher: Matcher):
        """症狀保持「症」"""
        cases = {
            "症状": "症狀",
            "病症": "病症",
            "并发症": "併發症",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should stay as {expected}"

    def test_zheng_illness(self, matcher: Matcher):
        """癥結轉「癥」"""
        cases = {
            "症结": "癥結",
            "顽症": "頑癥",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"


# Phase 4 新增測試
class TestFeng:
    """风 → 風"""

    def test_feng_wind(self, matcher: Matcher):
        """風轉「風」"""
        cases = {
            "风": "風",
            "大风": "大風",
            "刮风": "颳風",
            "台风": "颱風",
            "风景": "風景",
            "风险": "風險",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"


class TestLuan:
    """乱 → 亂"""

    def test_luan_chaos(self, matcher: Matcher):
        """亂轉「亂」"""
        cases = {
            "乱": "亂",
            "混乱": "混亂",
            "吹乱": "吹亂",
            "乱七八糟": "亂七八糟",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"


class TestKai:
    """开 → 開"""

    def test_kai_open(self, matcher: Matcher):
        """開轉「開」"""
        cases = {
            "开": "開",
            "打开": "打開",
            "开始": "開始",
            "开发": "開發",
            "离开": "離開",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"


class TestHouExtended:
    """后 系列擴展"""

    def test_hou_after(self, matcher: Matcher):
        """X后 轉「X後」"""
        cases = {
            "完成后": "完成後",
            "结束后": "結束後",
            "然后": "然後",
            "随后": "隨後",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"{src} should convert to {expected}"


class TestRealText:
    """真實文本測試"""

    def test_software_doc(self, matcher: Matcher):
        """軟體文檔轉換"""
        cases = {
            "软件开发文档": "軟體開發文件",
            "用户可以通过简单的操作完成任务": "使用者可以透過簡單的操作完成任務",
            "安装完成后，请尽快配置相关参数": "安裝完成後，請儘快設定相關參數",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"Failed: {src}"

    def test_daily_text(self, matcher: Matcher):
        """日常文本轉換"""
        cases = {
            "头发被风吹乱了": "頭髮被風吹亂了",
            "我们一起去旅游": "我們一起去旅遊",
            "游泳之后吃面条": "游泳之後吃麵條",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected, f"Failed: {src}"
