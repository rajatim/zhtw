"""歧義字驗證測試。確保剩餘一對多歧義字被正確處理。

歧義字（一對多）被排除在字元級安全對映之外，
由詞庫層（Aho-Corasick 複合詞）根據上下文做正確轉換。
"""
# zhtw:disable  # 測試案例需要簡體字

from __future__ import annotations

import pytest

from zhtw.charconv import (
    char_convert,
    clear_cache,
    get_ambiguous_chars,
    get_translate_table,
    load_charmap,
)
from zhtw.converter import convert_text
from zhtw.dictionary import load_dictionary
from zhtw.matcher import Matcher

# ──────────────────────────────────────────────
# 共用 fixtures
# ──────────────────────────────────────────────


@pytest.fixture(autouse=True)
def _clear_charconv_cache():
    """每個測試前後清除快取。"""
    clear_cache()
    yield
    clear_cache()


@pytest.fixture
def charmap():
    """載入字元映射表。"""
    return load_charmap()


@pytest.fixture
def char_table():
    """載入字元轉換表。"""
    return get_translate_table()


@pytest.fixture
def ambiguous():
    """載入歧義字清單。"""
    return get_ambiguous_chars()


@pytest.fixture
def terms():
    """載入完整詞庫。"""
    return load_dictionary(sources=["cn", "hk"])


@pytest.fixture
def matcher(terms):
    """建立完整詞庫 matcher。"""
    return Matcher(terms)


# ──────────────────────────────────────────────
# TestAmbiguousExclusion：歧義字未出現在安全字元映射中
# ──────────────────────────────────────────────


class TestAmbiguousExclusion:
    """歧義字未出現在安全字元映射中。"""

    def test_none_in_charmap(self, charmap, ambiguous):
        """歧義字都不在安全字元映射的 key 中。"""
        violations = [c for c in ambiguous if c in charmap]
        assert violations == [], f"以下歧義字不應出現在 safe charmap 中：{violations}"

    def test_v13_promotions_and_deferred_chars(self, ambiguous):
        """v1.2/v1.3 升級/保留的分類應反映在 ambiguous 清單。"""
        promoted_to_safe = {
            "帘",
            "凫",
            "坝",
            "竖",
            "绣",
            "绷",
            "蕴",
            "谣",
            "赃",
            "酝",
            "锈",
            "颓",
            "鳄",
            "仆",
            "尸",
            "赝",
            "镋",
            "镌",
        }
        still_ambiguous = {"卤", "坛", "弥", "摆", "纤"}

        for char in promoted_to_safe:
            assert char not in ambiguous, f"{char} 已升級到 safe_chars，不應留在 ambiguous"
        for char in still_ambiguous:
            assert char in ambiguous, f"{char} 仍應保留在 ambiguous_excluded"

    def test_ambiguous_are_single_chars(self, ambiguous):
        """每個歧義字都是單一字元。"""
        multi = [c for c in ambiguous if len(c) != 1]
        assert multi == [], f"以下項目不是單字元：{multi}"

    def test_no_duplicates(self, ambiguous):
        """歧義字清單無重複。"""
        assert len(ambiguous) == len(set(ambiguous)), "歧義字清單有重複項目"

    def test_charmap_and_ambiguous_disjoint(self, charmap, ambiguous):
        """安全映射和歧義字清單完全互斥。"""
        overlap = set(charmap.keys()) & set(ambiguous)
        assert overlap == set(), f"字元映射與歧義字重疊：{overlap}"


# ──────────────────────────────────────────────
# TestAmbiguousContextConversion：歧義字在上下文中正確轉換
# ──────────────────────────────────────────────

# 注意：发 不在歧義字清單中（安全映射 发→發），
# 但複合詞 头发→頭髮 由詞庫層正確處理兩種語義。

CONTEXT_CASES = [
    # (簡體輸入, 期望繁體輸出, 說明)
    # 发：安全映射 发→發，詞庫層處理特殊語義
    pytest.param("发送邮件", "傳送郵件", id="发-send"),
    pytest.param("头发很长", "頭髮很長", id="发-hair"),
    # 后：歧義字，後(time) vs 后(queen)
    pytest.param("以后再说", "以後再說", id="后-after"),
    pytest.param("皇后", "皇后", id="后-queen"),
    # 里：歧義字，裡(inside) vs 里(distance)
    pytest.param("这里很好", "這裡很好", id="里-inside"),
    pytest.param("公里", "公里", id="里-distance"),
    # 干：歧義字，乾(dry) vs 幹(do/cadre)
    pytest.param("干净", "乾淨", id="干-clean"),
    pytest.param("干部", "幹部", id="干-cadre"),
    # 面：歧義字，麵(noodle) vs 面(face/surface)
    pytest.param("面条", "麵條", id="面-noodle"),
    pytest.param("面对", "面對", id="面-face"),
    # 只：歧義字，隻(measure word) vs 只(only)
    pytest.param("只有", "只有", id="只-only"),
    pytest.param("一只猫", "一隻貓", id="只-measure"),
    # 台：歧義字，颱(typhoon) vs 臺/台
    pytest.param("台风", "颱風", id="台-typhoon"),
    pytest.param("台湾", "臺灣", id="台-taiwan"),
    # 复：歧義字，復(recover) vs 複(complex)
    pytest.param("恢复", "還原", id="复-recover"),
    pytest.param("复杂", "複雜", id="复-complex"),
    # 系：歧義字，係(relation) vs 系(system)
    pytest.param("关系", "關係", id="系-relation"),
    pytest.param("系统", "系統", id="系-system"),
    # 钟：歧義字，鐘(clock) vs 鍾(affection)
    pytest.param("钟表", "鐘錶", id="钟-clock"),
    pytest.param("钟情", "鍾情", id="钟-affection"),
    # 冲：歧義字，衝(rush) vs 沖(rinse)
    pytest.param("冲动", "衝動", id="冲-rush"),
    pytest.param("冲洗", "沖洗", id="冲-rinse"),
]


class TestAmbiguousContextConversion:
    """歧義字在上下文中正確轉換。"""

    @pytest.mark.parametrize("source,expected", CONTEXT_CASES)
    def test_context_conversion(self, matcher, char_table, source, expected):
        """詞庫層根據上下文將歧義字轉換為正確的繁體。"""
        result, _ = convert_text(
            source,
            matcher,
            fix=True,
            char_table=char_table,
        )
        assert result == expected, f"「{source}」期望「{expected}」，實際「{result}」"


# ──────────────────────────────────────────────
# TestAmbiguousAloneUnchanged：單獨歧義字不被字元層轉換
# ──────────────────────────────────────────────

# 這些常用歧義字在字元層 (str.translate) 中不應被轉換。
# 注意：像 后、舍 這類已採用「預設值 + 詞庫 identity 保護」策略的字不在此列。
TOP_20_AMBIGUOUS = [
    "里",
    "干",
    "面",
    "只",
    "台",
    "复",
    "系",
    "钟",
    "冲",
    "余",
    "几",
    "卷",
    "采",
    "折",
    "并",
    "表",
    "志",
    "松",
]


class TestAmbiguousAloneUnchanged:
    """單獨出現的歧義字不被字元層轉換。"""

    @pytest.mark.parametrize("char", TOP_20_AMBIGUOUS)
    def test_bare_ambiguous_unchanged(self, char_table, char):
        """字元層不轉換單獨的歧義字。"""
        result = char_convert(char, char_table)
        assert result == char, f"歧義字「{char}」被字元層錯誤轉換為「{result}」"

    @pytest.mark.parametrize("char", TOP_20_AMBIGUOUS)
    def test_ambiguous_in_sentence_char_level(self, char_table, char):
        """歧義字在句子中也不被字元層轉換（字元層只做安全映射）。"""
        sentence = f"这是{char}的测试"
        result = char_convert(sentence, char_table)
        # 这→這、测→測、试→試 會被轉換，但歧義字本身不變
        assert char in result, f"歧義字「{char}」在字元層被錯誤替換，結果：「{result}」"

    def test_all_ambiguous_untouched_by_char_layer(self, char_table, ambiguous):
        """全部剩餘歧義字都不被字元層轉換。"""
        changed = []
        for char in ambiguous:
            if char_convert(char, char_table) != char:
                changed.append(char)
        assert changed == [], f"以下歧義字被字元層錯誤轉換：{changed}"


# ──────────────────────────────────────────────
# TestAmbiguousCoverage：常用歧義字有足夠的複合詞覆蓋
# ──────────────────────────────────────────────


class TestAmbiguousCoverage:
    """常用歧義字有足夠的複合詞覆蓋。"""

    @pytest.mark.parametrize(
        "char,min_terms",
        [
            pytest.param("后", 3, id="后-terms"),
            pytest.param("里", 3, id="里-terms"),
            pytest.param("干", 3, id="干-terms"),
            pytest.param("面", 3, id="面-terms"),
            pytest.param("只", 3, id="只-terms"),
            pytest.param("台", 3, id="台-terms"),
            pytest.param("复", 3, id="复-terms"),
            pytest.param("系", 3, id="系-terms"),
            pytest.param("钟", 3, id="钟-terms"),
            pytest.param("冲", 3, id="冲-terms"),
            pytest.param("余", 3, id="余-terms"),
            pytest.param("几", 3, id="几-terms"),
            pytest.param("卷", 3, id="卷-terms"),
            pytest.param("采", 3, id="采-terms"),
            pytest.param("折", 3, id="折-terms"),
            pytest.param("并", 3, id="并-terms"),
            pytest.param("表", 3, id="表-terms"),
            pytest.param("舍", 3, id="舍-terms"),
            pytest.param("志", 3, id="志-terms"),
            pytest.param("松", 3, id="松-terms"),
        ],
    )
    def test_common_ambiguous_have_terms(self, terms, char, min_terms):
        """常用歧義字在詞庫中至少有 3 個包含該字的複合詞。"""
        matching = [k for k in terms if char in k and len(k) >= 2]
        assert len(matching) >= min_terms, (
            f"歧義字「{char}」只有 {len(matching)} 個複合詞"
            f"（需要至少 {min_terms} 個）：{matching[:10]}"
        )

    def test_ambiguous_coverage_summary(self, terms, ambiguous):
        """統計所有歧義字的複合詞覆蓋率。"""
        uncovered = []
        for char in ambiguous:
            matching = [k for k in terms if char in k and len(k) >= 2]
            if len(matching) == 0:
                uncovered.append(char)
        # 允許少量罕見字無覆蓋，但常用字必須有
        coverage_rate = 1 - len(uncovered) / len(ambiguous)
        assert coverage_rate >= 0.5, (
            f"歧義字複合詞覆蓋率僅 {coverage_rate:.1%}，" f"無覆蓋字：{uncovered}"
        )

    def test_both_meanings_covered(self, terms):
        """重要歧義字的兩種語義都有對應的複合詞。"""
        # 每組：(歧義字, 語義A的詞, 語義B的詞)
        both_meanings = [
            ("后", "之后", "皇后"),  # 後(after) vs 后(queen)
            ("里", "这里", "公里"),  # 裡(inside) vs 里(distance)
            ("干", "干净", "干部"),  # 乾(dry) vs 幹(cadre)
            ("面", "面条", "面对"),  # 麵(noodle) vs 面(face)
            ("只", "一只", "只有"),  # 隻(measure) vs 只(only)
            ("复", "复杂", "恢复"),  # 複(complex) vs 復(recover)
            ("钟", "钟表", "钟情"),  # 鐘(clock) vs 鍾(affection)
            ("冲", "冲动", "冲洗"),  # 衝(rush) vs 沖(rinse)
            ("卷", "卷起", "试卷"),  # 捲(roll) vs 卷(volume)
            ("采", "采集", "风采"),  # 採(gather) vs 采(elegance)
        ]
        missing = []
        for char, term_a, term_b in both_meanings:
            if term_a not in terms:
                missing.append(f"{char}: 缺少語義A「{term_a}」")
            if term_b not in terms:
                missing.append(f"{char}: 缺少語義B「{term_b}」")
        assert missing == [], "以下歧義字缺少雙語義覆蓋：\n" + "\n".join(missing)
