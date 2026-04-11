# zhtw:disable
"""balanced defaults 層的測試。"""

from __future__ import annotations

import pytest
from click.testing import CliRunner

from zhtw.charconv import (
    apply_balanced_defaults,
    clear_cache,
    get_balanced_defaults,
    get_translate_table,
)
from zhtw.cli import main
from zhtw.converter import convert, convert_text
from zhtw.dictionary import load_dictionary
from zhtw.matcher import Matcher


@pytest.fixture(autouse=True)
def _clear_all_cache():
    """每個測試前後清除快取。"""
    clear_cache()
    yield
    clear_cache()


# ──────────────────────────────────────────────
# TestDisambiguationData
# ──────────────────────────────────────────────


class TestDisambiguationData:
    """disambiguation.json 資料完整性。"""

    def test_schema_version_exists(self):
        import json
        from pathlib import Path

        path = (
            Path(__file__).parent.parent
            / "src"
            / "zhtw"
            / "data"
            / "charmap"
            / "disambiguation.json"
        )
        data = json.loads(path.read_text("utf-8"))
        assert isinstance(data["schema_version"], int)

    def test_every_rule_has_default(self):
        import json
        from pathlib import Path

        path = (
            Path(__file__).parent.parent
            / "src"
            / "zhtw"
            / "data"
            / "charmap"
            / "disambiguation.json"
        )
        data = json.loads(path.read_text("utf-8"))
        for char, rule in data["rules"].items():
            assert "default" in rule, f"{char!r} missing default"
            assert len(rule["default"]) == 1, f"{char!r} default is not single char"

    def test_protect_terms_contain_their_char(self):
        import json
        from pathlib import Path

        path = (
            Path(__file__).parent.parent
            / "src"
            / "zhtw"
            / "data"
            / "charmap"
            / "disambiguation.json"
        )
        data = json.loads(path.read_text("utf-8"))
        for char, rule in data["rules"].items():
            for term in rule.get("protect_terms", []):
                assert char in term, f"protect_term {term!r} does not contain {char!r}"

    def test_rule_keys_in_ambiguous_excluded(self):
        from zhtw.charconv import get_ambiguous_chars

        ambiguous = set(get_ambiguous_chars())
        import json
        from pathlib import Path

        path = (
            Path(__file__).parent.parent
            / "src"
            / "zhtw"
            / "data"
            / "charmap"
            / "disambiguation.json"
        )
        data = json.loads(path.read_text("utf-8"))
        for char in data["rules"]:
            assert char in ambiguous, f"rule key {char!r} not in ambiguous_excluded"

    def test_v1_entries_all_present(self):
        from zhtw.charconv import get_balanced_defaults

        defaults = get_balanced_defaults()
        v1_chars = {"几", "丰", "杰", "卤", "坛", "弥", "摆", "纤"}
        for char in v1_chars:
            assert char in defaults, f"v1 char {char!r} missing from disambiguation.json"


# ──────────────────────────────────────────────
# TestGetBalancedDefaults
# ──────────────────────────────────────────────


class TestGetBalancedDefaults:
    def test_load_returns_dict(self):
        defaults = get_balanced_defaults()
        assert isinstance(defaults, dict)

    def test_contains_ten_entries(self):
        defaults = get_balanced_defaults()
        assert len(defaults) == 10

    def test_keys_and_values(self):
        defaults = get_balanced_defaults()
        assert defaults.get("卤") == "滷"
        assert defaults.get("坛") == "壇"
        assert defaults.get("弥") == "彌"
        assert defaults.get("摆") == "擺"
        assert defaults.get("纤") == "纖"
        assert defaults.get("几") == "幾"
        assert defaults.get("丰") == "豐"
        assert defaults.get("杰") == "傑"
        assert defaults.get("后") == "後"
        assert defaults.get("里") == "裡"

    def test_values_are_strings(self):
        defaults = get_balanced_defaults()
        for k, v in defaults.items():
            assert isinstance(k, str)
            assert isinstance(v, str)

    def test_cache_returns_same_object(self):
        d1 = get_balanced_defaults()
        d2 = get_balanced_defaults()
        assert d1 is d2

    def test_clear_cache_invalidates(self):
        d1 = get_balanced_defaults()
        clear_cache()
        d2 = get_balanced_defaults()
        assert d1 is not d2
        assert d1 == d2


# ──────────────────────────────────────────────
# TestApplyBalancedDefaults
# ──────────────────────────────────────────────


class TestApplyBalancedDefaults:
    def test_replaces_ambiguous_char(self):
        result = apply_balanced_defaults("几个人")
        assert result == "幾个人"

    def test_replaces_all_defaults(self):
        result = apply_balanced_defaults("几丰杰")
        assert result == "幾豐傑"

    def test_no_replacement_when_covered(self):
        # 位置 0 被詞庫層覆蓋，不應被 balanced 替換
        result = apply_balanced_defaults("几个人", covered_positions={0})
        assert result[0] == "几"  # 未被替換
        assert result[1] == "个"  # 不在 defaults 中，原樣保留

    def test_empty_string(self):
        result = apply_balanced_defaults("")
        assert result == ""

    def test_no_ambiguous_chars(self):
        result = apply_balanced_defaults("你好世界")
        assert result == "你好世界"

    def test_covered_positions_none_is_same_as_empty_set(self):
        r1 = apply_balanced_defaults("几丰杰", covered_positions=None)
        r2 = apply_balanced_defaults("几丰杰", covered_positions=set())
        assert r1 == r2

    def test_partial_coverage(self):
        # 只有位置 2（杰）被覆蓋，几 和 丰 應被替換
        result = apply_balanced_defaults("几丰杰", covered_positions={2})
        assert result == "幾豐杰"

    def test_non_chinese_unchanged(self):
        result = apply_balanced_defaults("hello 几 world")
        assert result == "hello 幾 world"


# ──────────────────────────────────────────────
# TestConvertTextBalanced
# ──────────────────────────────────────────────


class TestConvertTextBalanced:
    @pytest.fixture
    def basic_matcher(self):
        """帶基本詞彙的 matcher（不含幾/丰/杰相關詞）。"""
        terms = {"个": "個"}
        return Matcher(terms)

    @pytest.fixture
    def chajii_matcher(self):
        """帶茶几詞彙的 matcher，測試詞庫層覆蓋。"""
        # 茶几 → 茶几（identity mapping，讓詞庫層「保護」茶几不被字元層改動）
        terms = {"茶几": "茶几"}
        return Matcher(terms)

    def test_balanced_converts_ambiguous(self, basic_matcher):
        """balanced mode 應替換歧義字。"""
        text = "几个人"
        result, _ = convert_text(text, basic_matcher, fix=True, ambiguity_mode="balanced")
        assert "幾" in result

    def test_strict_does_not_convert_ambiguous(self, basic_matcher):
        """strict mode 不應替換歧義字。"""
        text = "几个人"
        result, _ = convert_text(text, basic_matcher, fix=True, ambiguity_mode="strict")
        assert result[0] == "几"  # 未被替換

    def test_default_mode_is_strict(self, basic_matcher):
        """未傳 ambiguity_mode 時預設為 strict。"""
        text = "几个人"
        result, _ = convert_text(text, basic_matcher, fix=True)
        assert result[0] == "几"  # 未被替換

    def test_term_layer_coverage_prevents_balanced(self):
        """詞庫層覆蓋的位置不被 balanced 覆蓋。

        茶几 作為整體詞彙被詞庫層處理（identity mapping），
        其中的「几」不應被 balanced defaults 替換。
        """
        # 使用真實詞庫的 convert_text：先建立有「茶几」的 matcher
        terms = {"茶几": "茶几"}
        matcher = Matcher(terms)
        text = "茶几"
        result, _ = convert_text(text, matcher, fix=True, ambiguity_mode="balanced")
        # 詞庫層 identity mapping 保護了「茶几」，balanced 不應改「几」
        assert result == "茶几"

    def test_balanced_with_ignored_lines(self, basic_matcher):
        """ignored lines 在 balanced mode 也要被尊重。"""
        text = "几个人\n几个人"
        result, _ = convert_text(
            text,
            basic_matcher,
            fix=True,
            ignored_lines={2},
            ambiguity_mode="balanced",
        )
        lines = result.split("\n")
        assert "幾" in lines[0]  # 第一行應被替換
        assert lines[1] == "几个人"  # 第二行不變


# ──────────────────────────────────────────────
# TestConvertConvenienceBalanced
# ──────────────────────────────────────────────


class TestConvertConvenienceBalanced:
    def test_balanced_mode_converts_ambiguous(self):
        """convert() balanced mode 應替換歧義字。"""
        result = convert("几个人", ambiguity_mode="balanced")
        assert "幾" in result
        assert "個" in result  # 个 是安全字，字元層轉換

    def test_strict_mode_does_not_convert_ambiguous(self):
        """convert() strict mode 不應替換歧義字（balanced_defaults 中的字）。

        「桌上只有几张纸」中的「几」不在任何詞條裡，strict mode 不應透過
        balanced defaults 替換它；但 balanced mode 會替換。
        """
        # 先確認 balanced mode 會替換
        balanced_result = convert("桌上只有几张纸", ambiguity_mode="balanced")
        assert "幾" in balanced_result

        # strict mode 不替換
        strict_result = convert("桌上只有几张纸", ambiguity_mode="strict")
        assert "幾" not in strict_result

    def test_invalid_mode_raises_value_error(self):
        """無效的 ambiguity_mode 應拋出 ValueError。"""
        with pytest.raises(ValueError, match="ambiguity_mode"):
            convert("几个人", ambiguity_mode="invalid")

    def test_invalid_mode_message_shows_valid_modes(self):
        """錯誤訊息應包含有效的模式列表。"""
        with pytest.raises(ValueError) as exc_info:
            convert("几", ambiguity_mode="auto")
        assert "balanced" in str(exc_info.value)
        assert "strict" in str(exc_info.value)

    def test_default_is_strict(self):
        """不傳 ambiguity_mode 預設是 strict。"""
        result_default = convert("几个人")
        result_strict = convert("几个人", ambiguity_mode="strict")
        assert result_default == result_strict

    def test_balanced_converts_v12_chars(self):
        """v1.2 新增的真歧義字在 balanced mode 應替換。"""
        expectations = {
            "卤": "滷",
            "坛": "壇",
            "弥": "彌",
            "摆": "擺",
            "纤": "纖",
        }
        for char, expected in expectations.items():
            assert convert(char, ambiguity_mode="balanced") == expected

    def test_balanced_respects_existing_term_protection(self):
        """既有詞庫保護詞在 balanced mode 不應被預設值覆寫。"""
        cases = {
            "卤素": "鹵素",
            "酒坛": "酒罈",
            "弥漫": "瀰漫",
            "下摆": "下襬",
            "纤夫": "縴夫",
        }
        for source, expected in cases.items():
            assert convert(source, ambiguity_mode="balanced") == expected

    def test_hk_source_does_not_apply_balanced_defaults(self):
        """HK-only source 不應套用 CN balanced defaults。"""
        assert convert("几个人", sources=["hk"], ambiguity_mode="balanced") == "几个人"
        assert convert("卤肉", sources=["hk"], ambiguity_mode="balanced") == "卤肉"


# ──────────────────────────────────────────────
# TestProtectTermsIntegration
# ──────────────────────────────────────────────


class TestProtectTermsIntegration:
    """protect_terms identity mapping 保護歧義字在 balanced mode 不被錯轉。"""

    def test_hou_default_converts(self):
        """后 在 balanced mode default 轉為 後。"""
        result = convert("\u4ee5\u540e\u518d\u8bf4", ambiguity_mode="balanced")
        assert result == "以後再說"

    def test_hou_huanghou_protected(self):
        """皇后 被 protect_term 保護。"""
        result = convert("\u7687\u540e\u5f88\u7f8e", ambiguity_mode="balanced")
        assert result == "皇后很美"

    def test_hou_taihou_protected(self):
        """太后 被 protect_term 保護，char layer 仍轉其他字。"""
        result = convert("\u592a\u540e\u9a7e\u5230", ambiguity_mode="balanced")
        assert result == "太后駕到"

    def test_li_default_converts(self):
        """里 在 balanced mode default 轉為 裡。"""
        result = convert("\u5bb6\u91cc\u5f88\u5927", ambiguity_mode="balanced")
        assert result == "家裡很大"

    def test_li_gongli_protected(self):
        """公里 被 protect_term 保護。"""
        result = convert("\u516c\u91cc\u6570\u5f88\u5927", ambiguity_mode="balanced")
        assert result == "公里數很大"

    def test_li_yingli_protected(self):
        """英里 被 protect_term 保護。"""
        result = convert("\u82f1\u91cc", ambiguity_mode="balanced")
        assert result == "英里"

    def test_li_licheng_protected(self):
        """里程 被 protect_term 保護。"""
        result = convert("\u91cc\u7a0b\u7891", ambiguity_mode="balanced")
        assert result == "里程碑"

    def test_hou_yinghou_protected(self):
        """影后 被 protect_term 保護（此詞不在詞庫，純靠 inject_protect_terms）。"""
        result = convert("\u5f71\u540e\u5f97\u5956", ambiguity_mode="balanced")
        assert result == "影后得獎"

    def test_hou_yinghou_protected_strict(self):
        """影后 在 strict mode 也被保護。"""
        result = convert("\u5f71\u540e\u5f97\u5956", ambiguity_mode="strict")
        assert result == "影后得獎"

    def test_li_licheng_via_convert_text(self):
        """里程 透過 convert_text + inject_protect_terms 也被保護。"""
        from zhtw.charconv import get_translate_table
        from zhtw.converter import convert_text, inject_protect_terms
        from zhtw.dictionary import load_dictionary
        from zhtw.matcher import Matcher

        terms = load_dictionary(sources=["cn"])
        inject_protect_terms(terms, ["cn"])
        matcher = Matcher(terms)
        char_table = get_translate_table()
        result, _ = convert_text("\u91cc\u7a0b\u7891", matcher, fix=True, char_table=char_table)
        assert result == "里程碑"

    def test_strict_mode_unchanged(self):
        """strict mode 下后/里的詞庫層行為與 balanced 一致。

        后→後、里→裡 本來就是詞庫層的單字詞條（非 balanced default），
        皇后、公里等多字詞條也有 identity mapping 保護。
        strict/balanced 的差異只在「無詞條覆蓋的歧義字」。
        """
        assert convert("\u4ee5\u540e\u518d\u8bf4", ambiguity_mode="strict") == "以後再說"
        assert convert("\u7687\u540e\u5f88\u7f8e", ambiguity_mode="strict") == "皇后很美"
        assert convert("\u5bb6\u91cc\u5f88\u5927", ambiguity_mode="strict") == "家裡很大"
        assert convert("\u516c\u91cc\u6570\u5f88\u5927", ambiguity_mode="strict") == "公里數很大"


# ──────────────────────────────────────────────
# TestProcessDirectoryProtection
# ──────────────────────────────────────────────


class TestProcessDirectoryProtection:
    """process_directory 也正確注入 protect_terms。"""

    def test_yinghou_protected_via_process_directory(self, tmp_path):
        """影后 透過 process_directory 路徑也被保護（不在詞庫，靠 inject_protect_terms）。"""
        from zhtw.converter import process_directory

        test_file = tmp_path / "test.txt"
        # 影后得奖
        test_file.write_text("\u5f71\u540e\u5f97\u5956", encoding="utf-8")
        process_directory(tmp_path, sources=["cn"], fix=True, ambiguity_mode="strict")
        content = test_file.read_text(encoding="utf-8")
        assert content == "影后得獎"


# ──────────────────────────────────────────────
# TestCLIAmbiguityMode
# ──────────────────────────────────────────────


class TestCLIAmbiguityMode:
    """CLI --ambiguity-mode flag。"""

    def test_fix_balanced_mode(self, tmp_path):
        """fix --ambiguity-mode balanced 轉換歧義字。"""
        test_file = tmp_path / "test.txt"
        test_file.write_text("几个人", encoding="utf-8")

        runner = CliRunner()
        result = runner.invoke(
            main,
            [
                "fix",
                str(test_file),
                "--ambiguity-mode",
                "balanced",
                "--yes",
            ],
        )
        assert result.exit_code == 0
        content = test_file.read_text(encoding="utf-8")
        assert "幾" in content

    def test_fix_strict_mode_default(self, tmp_path):
        """fix 不帶 flag 時預設 strict，不轉換歧義字。

        使用「桌上只有几张纸」—「几张」不在詞庫中，strict mode 不應透過
        balanced_defaults 將「几」替換為「幾」。
        """
        test_file = tmp_path / "test.txt"
        test_file.write_text("桌上只有几张纸", encoding="utf-8")

        runner = CliRunner()
        result = runner.invoke(
            main,
            [
                "fix",
                str(test_file),
                "--yes",
            ],
        )
        assert result.exit_code == 0
        content = test_file.read_text(encoding="utf-8")
        assert "几" in content

    def test_invalid_mode_error(self):
        """無效的 ambiguity-mode 值應報錯。"""
        runner = CliRunner()
        result = runner.invoke(
            main,
            [
                "check",
                ".",
                "--ambiguity-mode",
                "invalid",
            ],
        )
        assert result.exit_code != 0

    def test_fix_hk_source_balanced_keeps_cn_only_defaults_disabled(self, tmp_path):
        """CLI 在 --source hk 時不應套用 CN balanced defaults。"""
        test_file = tmp_path / "test.txt"
        test_file.write_text("几个人 卤肉", encoding="utf-8")

        runner = CliRunner()
        result = runner.invoke(
            main,
            [
                "fix",
                str(test_file),
                "--source",
                "hk",
                "--ambiguity-mode",
                "balanced",
                "--yes",
            ],
        )
        assert result.exit_code == 0
        assert test_file.read_text(encoding="utf-8") == "几个人 卤肉"


# ──────────────────────────────────────────────
# Shared fixtures for TestStrictUnchanged
# ──────────────────────────────────────────────


@pytest.fixture(scope="module")
def matcher():
    """建立包含完整詞庫的 matcher。"""
    terms = load_dictionary(sources=["cn"])
    return Matcher(terms)


@pytest.fixture(scope="module")
def char_table():
    """取得字元級轉換表。"""
    return get_translate_table()


# ──────────────────────────────────────────────
# TestStrictUnchanged
# ──────────────────────────────────────────────


class TestStrictUnchanged:
    """strict mode 行為完全不變（回歸測試）。"""

    def test_existing_ambiguous_tests_still_pass(self, matcher, char_table):
        """現有歧義字測試案例在 strict mode 下行為不變。"""
        cases = [
            ("以后再说", "以後再說"),
            ("皇后", "皇后"),
            ("干净", "乾淨"),
            ("干部", "幹部"),
            ("面条", "麵條"),
            ("面对", "面對"),
        ]
        for source, expected in cases:
            result, _ = convert_text(
                source,
                matcher,
                fix=True,
                char_table=char_table,
                ambiguity_mode="strict",
            )
            assert result == expected, f"strict: {source!r} → {result!r}, expected {expected!r}"

    def test_bare_ambiguous_unchanged_in_strict(self):
        """單獨歧義字在 strict mode 不被轉換。"""
        for char in ["卤", "坛", "弥", "摆", "纤", "几", "丰", "杰"]:
            result = convert(char, ambiguity_mode="strict")
            assert result == char, f"strict should not convert bare {char!r}, got {result!r}"

    def test_v13_promoted_safe_chars_convert_in_strict(self):
        """v1.3 升級到 safe_chars 的字在 strict mode 應直接轉換。"""
        expectations = {
            "仆": "僕",
            "尸": "屍",
            "赝": "贗",
            "镋": "鎲",
            "镌": "鐫",
        }
        for char, expected in expectations.items():
            result = convert(char, ambiguity_mode="strict")
            assert result == expected, f"strict: {char!r} → {result!r}, expected {expected!r}"

    def test_balanced_converts_bare_ambiguous(self):
        """單獨歧義字在 balanced mode 被轉換。"""
        expectations = {
            "卤": "滷",
            "坛": "壇",
            "弥": "彌",
            "摆": "擺",
            "纤": "纖",
            "几": "幾",
            "丰": "豐",
            "杰": "傑",
        }
        for char, expected in expectations.items():
            result = convert(char, ambiguity_mode="balanced")
            assert result == expected, f"balanced: {char!r} → {result!r}, expected {expected!r}"


class TestCheckModeBalanced:
    """check mode（fix=False）在 balanced mode 下偵測歧義字。"""

    def test_check_balanced_reports_ambiguous_chars(self, matcher, char_table):
        """check --ambiguity-mode balanced 應報告可轉換的歧義字。"""
        _text, matches = convert_text(
            "桌上只有几张纸",
            matcher,
            fix=False,
            char_table=char_table,
            ambiguity_mode="balanced",
        )
        sources = [m.source for m, _line, _col in matches]
        assert "几" in sources

    def test_check_strict_does_not_report_bare_ambiguous(self, matcher, char_table):
        """check --ambiguity-mode strict 不報告獨立歧義字。"""
        _text, matches = convert_text(
            "桌上只有几张纸",
            matcher,
            fix=False,
            char_table=char_table,
            ambiguity_mode="strict",
        )
        sources = [m.source for m, _line, _col in matches]
        assert "几" not in sources


class TestBalancedSourcesGuard:
    """balanced mode 在 sources=["hk"] 時不應啟用（CN→TW only）。"""

    def test_hk_only_balanced_does_not_convert(self):
        """sources=["hk"] 時 balanced 不轉換歧義字。"""
        result = convert("几个人", sources=["hk"], ambiguity_mode="balanced")
        assert "幾" not in result

    def test_cn_balanced_converts(self):
        """sources=["cn"] 時 balanced 正常轉換歧義字。"""
        result = convert("几个人", sources=["cn"], ambiguity_mode="balanced")
        assert "幾" in result

    def test_default_sources_balanced_converts(self):
        """sources=None 時 balanced 正常轉換歧義字。"""
        result = convert("几个人", ambiguity_mode="balanced")
        assert "幾" in result


class TestFileAPIValidation:
    """file/directory API 的 ambiguity_mode 驗證。"""

    def test_convert_file_invalid_mode_raises(self, tmp_path, matcher):
        """convert_file() 對無效 ambiguity_mode 立即報錯。"""
        from zhtw.converter import convert_file

        test_file = tmp_path / "latin.txt"
        test_file.write_text("hello world", encoding="utf-8")
        with pytest.raises(ValueError, match="ambiguity_mode"):
            convert_file(test_file, matcher, ambiguity_mode="invalid")

    def test_process_directory_invalid_mode_raises(self, tmp_path):
        """process_directory() 對無效 ambiguity_mode 立即報錯。"""
        from zhtw.converter import process_directory

        test_file = tmp_path / "latin.txt"
        test_file.write_text("hello world", encoding="utf-8")
        with pytest.raises(ValueError, match="ambiguity_mode"):
            process_directory(tmp_path, ambiguity_mode="invalid")
