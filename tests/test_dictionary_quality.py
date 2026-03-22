"""詞庫品質驗證測試。驗證全部詞條的正確性、一致性和完整性。"""
# zhtw:disable  # 測試案例需要簡體字

from __future__ import annotations

import json
import unicodedata
from pathlib import Path

import pytest

from zhtw.charconv import load_charmap
from zhtw.dictionary import load_dictionary

TERMS_DIR = Path(__file__).parent.parent / "src" / "zhtw" / "data" / "terms"
CN_DIR = TERMS_DIR / "cn"
CN_FILES = sorted(CN_DIR.glob("*.json"))

# 已知古字/異體字（繁體側不應出現）
ARCHAIC_CHARS = set("纔閤纍衆爲牀竈糉")

# 已知異體字對照（錯誤 → 正確），繁體側不應出現左邊的字
VARIANT_FORMS = {
    "啓": "啟",
    "峯": "峰",
    "羣": "群",
    "衞": "衛",
    "粧": "妝",
    "綫": "線",
    "鏇": "旋",
}

# 常見歧義字：應在詞庫中有對應的複合詞處理
COMMON_AMBIGUOUS = ["发", "后", "里", "干", "面", "只", "台", "复", "系"]

# charmap 中明確的簡體字（用來判斷 identity mapping 的 key 是否含簡體）
_CHARMAP_CACHE: dict[str, str] | None = None


def _get_charmap() -> dict[str, str]:
    """取得字元映射（快取）。"""
    global _CHARMAP_CACHE
    if _CHARMAP_CACHE is None:
        _CHARMAP_CACHE = load_charmap()
    return _CHARMAP_CACHE


def _load_raw_terms(path: Path) -> dict[str, str]:
    """載入 JSON 檔案的原始 terms（含 _comment 鍵）。"""
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data.get("terms", data)


def _load_terms_only(path: Path) -> dict[str, str]:
    """載入 JSON 檔案，過濾掉 _comment 鍵。"""
    raw = _load_raw_terms(path)
    return {k: v for k, v in raw.items() if not k.startswith("_")}


# ──────────────────────────────────────────────
# 詞條數量驗證
# ──────────────────────────────────────────────


class TestTermCount:
    """詞條數量驗證。"""

    def test_cn_total_above_30000(self):
        """CN 詞庫總數應超過 30,000 條。"""
        terms = load_dictionary(sources=["cn"])
        assert len(terms) > 30_000, f"CN 詞條只有 {len(terms)} 條，低於 30,000"

    @pytest.mark.parametrize("json_file", CN_FILES, ids=lambda p: p.name)
    def test_each_file_nonempty(self, json_file: Path):
        """每個 CN JSON 檔案至少有 1 條詞彙。"""
        terms = _load_terms_only(json_file)
        assert len(terms) >= 1, f"{json_file.name} 沒有任何詞條"

    def test_no_empty_values(self):
        """所有詞條的繁體值不為空字串。"""
        terms = load_dictionary(sources=["cn"])
        empty = {k for k, v in terms.items() if v == ""}
        assert not empty, f"以下詞條的值為空字串: {empty}"


# ──────────────────────────────────────────────
# Identity mapping 驗證
# ──────────────────────────────────────────────


class TestNoIdentityMapping:
    """驗證 identity mapping（key == value）不是純簡體漏轉。

    zhtw 詞庫中 identity mapping 有多種合理用途：
    - 子字串保護（防止 longest-match 誤判）
    - 歧義字保護（如 后、里、干）
    - charmap 字元覆蓋（如 症→癥 在「病症」中不應轉、云→雲 在「人云亦云」中不應轉）
    - 領域詞宣告（明確標記已是繁體的領域術語）

    真正的品質問題是：identity mapping 的 key 全部 CJK 字元都在 charmap 中
    （純簡體），代表整個詞都是簡體卻沒轉換（如 "软件"="软件"）。
    部分字元在 charmap 中是正常的（identity mapping 正是為了阻止 charmap 錯轉）。
    """

    @staticmethod
    def _find_fully_simplified_identity(
        terms_to_check: dict[str, str], charmap: dict[str, str]
    ) -> dict[str, list[str]]:
        """找出所有 CJK 字元都在 charmap 中的 identity mapping（純簡體漏轉）。"""
        bad = {}
        for key, value in terms_to_check.items():
            if key != value or key.startswith("_"):
                continue
            cjk_chars = [ch for ch in key if "\u4e00" <= ch <= "\u9fff"]
            if cjk_chars and all(ch in charmap for ch in cjk_chars):
                bad[key] = [f"{ch}->{charmap[ch]}" for ch in cjk_chars]
        return bad

    def test_no_identity_in_merged(self):
        """合併詞庫中不應有純簡體的 identity mapping。"""
        terms = load_dictionary(sources=["cn"])
        charmap = _get_charmap()
        bad = self._find_fully_simplified_identity(terms, charmap)

        assert not bad, (
            f"identity mapping 全為簡體字（疑似漏轉）: " f"{dict(list(bad.items())[:10])}"
        )

    @pytest.mark.parametrize("json_file", CN_FILES, ids=lambda p: p.name)
    def test_no_identity_per_file(self, json_file: Path):
        """每個檔案不應有純簡體的 identity mapping。"""
        terms = _load_terms_only(json_file)
        charmap = _get_charmap()
        bad = self._find_fully_simplified_identity(terms, charmap)

        assert not bad, (
            f"{json_file.name} identity mapping 全為簡體字: " f"{dict(list(bad.items())[:5])}"
        )


# ──────────────────────────────────────────────
# 跨檔案重複/衝突偵測
# ──────────────────────────────────────────────


class TestNoDuplicateConflicts:
    """跨檔案重複/衝突偵測。"""

    def test_no_conflicting_terms(self):
        """同一個簡體詞若出現在多個檔案，繁體值必須一致。"""
        registry: dict[str, list[tuple[str, str]]] = {}

        for json_file in CN_FILES:
            terms = _load_terms_only(json_file)
            for key, value in terms.items():
                registry.setdefault(key, []).append((json_file.name, value))

        conflicts = {}
        for key, entries in registry.items():
            values = {v for _, v in entries}
            if len(values) > 1:
                conflicts[key] = entries

        assert not conflicts, (
            f"發現 {len(conflicts)} 條衝突詞彙: " f"{dict(list(conflicts.items())[:5])}"
        )


# ──────────────────────────────────────────────
# 繁體側不含古字或異體字
# ──────────────────────────────────────────────


class TestNoArchaicChars:
    """繁體側不含古字或異體字。

    opencc.json 來自 OpenCC 專案匯入，已知含有部分古字/異體字，
    這些是已知的待清理項目，測試時排除 opencc.json。
    """

    def _non_opencc_terms(self) -> dict[str, str]:
        """載入排除 opencc.json 的所有 CN 詞條。"""
        merged = {}
        for json_file in CN_FILES:
            if json_file.name == "opencc.json":
                continue
            merged.update(_load_terms_only(json_file))
        return merged

    def test_no_archaic_in_values(self):
        """非 OpenCC 詞條的繁體值不應包含已知古字。"""
        terms = self._non_opencc_terms()
        found = {}
        for key, value in terms.items():
            archaic_in_value = ARCHAIC_CHARS & set(value)
            if archaic_in_value:
                found[key] = (value, archaic_in_value)

        assert not found, f"繁體值含古字: " f"{dict(list(found.items())[:10])}"

    def test_no_variant_forms(self):
        """非 OpenCC 詞條的繁體值不應使用異體字。"""
        terms = self._non_opencc_terms()
        found = {}
        for key, value in terms.items():
            for variant, standard in VARIANT_FORMS.items():
                if variant in value:
                    found[key] = (value, f"{variant}->應為{standard}")

        assert not found, f"繁體值含異體字: " f"{dict(list(found.items())[:10])}"


# ──────────────────────────────────────────────
# 鍵值字元完整性
# ──────────────────────────────────────────────


class TestKeyValueCharacterIntegrity:
    """鍵值字元完整性。"""

    def test_keys_not_empty(self):
        """所有鍵不為空字串。"""
        for json_file in CN_FILES:
            terms = _load_raw_terms(json_file)
            for key in terms:
                assert key != "", f"{json_file.name} 含有空字串鍵"

    def test_values_not_empty(self):
        """所有值不為空字串。"""
        for json_file in CN_FILES:
            terms = _load_terms_only(json_file)
            empty = [k for k, v in terms.items() if v == ""]
            assert not empty, f"{json_file.name} 含有空值: {empty[:5]}"

    def test_no_leading_trailing_whitespace(self):
        """鍵和值不應有前後空白。"""
        terms = load_dictionary(sources=["cn"])
        bad_keys = [k for k in terms if k != k.strip()]
        bad_vals = [(k, v) for k, v in terms.items() if v != v.strip()]
        assert not bad_keys, f"鍵含前後空白: {bad_keys[:10]}"
        assert not bad_vals, f"值含前後空白: {bad_vals[:10]}"

    def test_no_control_characters(self):
        """鍵和值不應包含控制字元。"""
        terms = load_dictionary(sources=["cn"])
        bad = {}
        for key, value in terms.items():
            for text, label in [(key, "key"), (value, "value")]:
                for ch in text:
                    if unicodedata.category(ch) == "Cc" and ch not in ("\n", "\r", "\t"):
                        bad[key] = (value, label, repr(ch))
                        break

        assert not bad, f"含有控制字元: {dict(list(bad.items())[:10])}"


# ──────────────────────────────────────────────
# 字元映射與詞庫的一致性
# ──────────────────────────────────────────────


class TestCharmapTermConsistency:
    """字元映射與詞庫的一致性。

    charmap 是安全的一對一字元映射，詞庫的單字詞條可能刻意覆蓋
    charmap（例如選擇台灣慣用字形），這屬於正常設計。
    """

    @pytest.mark.parametrize("char", COMMON_AMBIGUOUS)
    def test_ambiguous_chars_have_compound_terms(self, char: str):
        """常見歧義字在詞庫中至少有一個包含該字的複合詞。"""
        terms = load_dictionary(sources=["cn"])
        compound = [k for k in terms if char in k and len(k) > 1]
        assert compound, f"歧義字「{char}」在詞庫中沒有任何複合詞處理"

    def test_charmap_does_not_conflict_with_terms(self):
        """單字詞條與 charmap 的差異應在已知允許清單內。

        詞庫單字詞條可能刻意覆蓋 charmap（選擇台灣慣用形），
        這些已知差異記錄在允許清單中，新增差異需人工審核。
        """
        # 已知的合理覆蓋（詞庫選擇台灣慣用形，與 charmap 不同）
        known_overrides = {"净", "账"}

        charmap = _get_charmap()
        terms = load_dictionary(sources=["cn"])
        conflicts = {}
        for key, value in terms.items():
            if len(key) == 1 and key in charmap and charmap[key] != value:
                if key not in known_overrides:
                    conflicts[key] = (f"詞庫={value}", f"charmap={charmap[key]}")

        assert not conflicts, (
            f"單字詞條與 charmap 有未知衝突（需人工審核是否加入允許清單）: "
            f"{dict(list(conflicts.items())[:10])}"
        )


# ──────────────────────────────────────────────
# 註解鍵格式正確
# ──────────────────────────────────────────────


class TestCommentKeysValid:
    """註解鍵格式正確。"""

    @pytest.mark.parametrize("json_file", CN_FILES, ids=lambda p: p.name)
    def test_comment_keys_start_with_underscore(self, json_file: Path):
        """metadata 鍵必須以底線開頭。"""
        raw = _load_raw_terms(json_file)
        for key, value in raw.items():
            if key.startswith("_"):
                assert isinstance(value, str), f"{json_file.name}: _comment 鍵「{key}」的值應為字串"
            # 非底線開頭的鍵不應是純註解文字
            if not key.startswith("_") and isinstance(value, str):
                assert not value.startswith(
                    "==="
                ), f"{json_file.name}: 鍵「{key}」的值像是註解但鍵名沒有底線前綴"
