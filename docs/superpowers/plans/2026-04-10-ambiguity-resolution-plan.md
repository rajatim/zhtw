<!-- zhtw:disable -->
# 語義歧義消解 v1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 為 3 個高安全歧義字（几→幾、丰→豐、杰→傑）提供 opt-in `balanced` mode 預設映射。

**Architecture:** 在現有詞庫層（Aho-Corasick）和字元層（str.translate）之間插入歧義預設值層，僅在 `ambiguity_mode='balanced'` 時啟用。新增 `balanced_defaults.json` 資料檔，透過 `zhtw export` 寫入 `zhtw-data.json` 供跨 SDK 共享。

**Tech Stack:** Python 3.9+、click（CLI）、pytest、str.translate()

---

## File Structure

| 檔案 | 責任 | 動作 |
|------|------|------|
| `src/zhtw/data/charmap/balanced_defaults.json` | curated 歧義字預設映射來源檔 | **新增** |
| `src/zhtw/charconv.py` | 載入 balanced_defaults + apply 函式 | 修改 |
| `src/zhtw/converter.py` | 在管線中插入歧義層、穿透 ambiguity_mode 參數 | 修改 |
| `src/zhtw/cli.py` | fix/check 加 --ambiguity-mode flag | 修改 |
| `src/zhtw/export.py` | export_data() 輸出 balanced_defaults | 修改 |
| `tests/test_ambiguous_balanced.py` | balanced mode 專屬測試 | **新增** |

---

### Task 1: 建立 balanced_defaults.json 資料檔

**Files:**
- Create: `src/zhtw/data/charmap/balanced_defaults.json`

- [ ] **Step 1: 建立資料檔**

```json
{
  "_comment": "歧義字預設映射（balanced mode）。只收錄 >95% 主流義、罕用義幾乎死語的字。",
  "version": 1,
  "defaults": {
    "几": "幾",
    "丰": "豐",
    "杰": "傑"
  }
}
```

- [ ] **Step 2: 驗證資料檔可讀取**

Run: `python3 -c "import json; d=json.load(open('src/zhtw/data/charmap/balanced_defaults.json')); print(d['defaults'])"`
Expected: `{'几': '幾', '丰': '豐', '杰': '傑'}`

- [ ] **Step 3: Commit**

```bash
git add src/zhtw/data/charmap/balanced_defaults.json
git commit -m "feat: 新增 balanced_defaults.json（3 字歧義預設映射）"
```

---

### Task 2: charconv.py — 載入 balanced defaults + apply 函式

**Files:**
- Modify: `src/zhtw/charconv.py`
- Test: `tests/test_ambiguous_balanced.py`

- [ ] **Step 1: 寫失敗測試**

建立 `tests/test_ambiguous_balanced.py`：

```python
"""balanced mode 歧義預設值測試。"""
# zhtw:disable

from __future__ import annotations

import pytest

from zhtw.charconv import (
    apply_balanced_defaults,
    clear_cache,
    get_balanced_defaults,
)


@pytest.fixture(autouse=True)
def _clear_cache():
    clear_cache()
    yield
    clear_cache()


class TestGetBalancedDefaults:
    """載入 balanced_defaults.json。"""

    def test_returns_dict(self):
        defaults = get_balanced_defaults()
        assert isinstance(defaults, dict)

    def test_contains_curated_chars(self):
        defaults = get_balanced_defaults()
        assert defaults["几"] == "幾"
        assert defaults["丰"] == "豐"
        assert defaults["杰"] == "傑"

    def test_count_is_3(self):
        defaults = get_balanced_defaults()
        assert len(defaults) == 3


class TestApplyBalancedDefaults:
    """apply_balanced_defaults 函式。"""

    def test_replaces_ambiguous_char(self):
        result = apply_balanced_defaults("几个人")
        assert result == "幾个人"  # 只轉 几→幾，其他不動

    def test_does_not_touch_non_ambiguous(self):
        result = apply_balanced_defaults("你好世界")
        assert result == "你好世界"

    def test_empty_string(self):
        result = apply_balanced_defaults("")
        assert result == ""

    def test_multiple_ambiguous_chars(self):
        result = apply_balanced_defaults("丰杰")
        assert result == "豐傑"

    def test_covered_positions_skipped(self):
        """詞庫層已處理的位置不應被覆蓋。"""
        covered = {0, 1}  # 假設前兩個字元已被詞庫層處理
        result = apply_balanced_defaults("几几几", covered_positions=covered)
        assert result == "几几幾"  # 只有第 3 個 几 被轉換
```

- [ ] **Step 2: 執行測試確認失敗**

Run: `pytest tests/test_ambiguous_balanced.py -v`
Expected: FAIL — `cannot import name 'apply_balanced_defaults'`

- [ ] **Step 3: 實作 charconv.py 新增函式**

在 `src/zhtw/charconv.py` 的 `get_ambiguous_chars()` 之後（行 79 後）新增：

```python
BALANCED_DEFAULTS_FILE = CHARMAP_DIR / "balanced_defaults.json"

_cached_balanced_defaults: Optional[Dict[str, str]] = None


def get_balanced_defaults(path: Optional[Path] = None) -> Dict[str, str]:
    """取得 balanced mode 歧義字預設映射。"""
    global _cached_balanced_defaults
    if _cached_balanced_defaults is not None and path is None:
        return _cached_balanced_defaults

    p = path or BALANCED_DEFAULTS_FILE
    with open(p, encoding="utf-8") as f:
        data = json.load(f)

    result = data.get("defaults", {})
    if path is None:
        with _lock:
            _cached_balanced_defaults = result
    return result


def apply_balanced_defaults(
    text: str,
    covered_positions: Optional[set[int]] = None,
) -> str:
    """對文字中未被詞庫層覆蓋的歧義字套用 balanced 預設映射。

    Args:
        text: 經過詞庫層處理後的文字。
        covered_positions: 詞庫層已處理的字元位置集合（0-based index）。
            這些位置不會被覆蓋。

    Returns:
        套用預設映射後的文字。
    """
    if not text:
        return text

    defaults = get_balanced_defaults()
    if not defaults:
        return text

    if covered_positions is None:
        covered_positions = set()

    chars = list(text)
    for i, ch in enumerate(chars):
        if i not in covered_positions and ch in defaults:
            chars[i] = defaults[ch]
    return "".join(chars)
```

同時在 `clear_cache()` 中新增：

```python
def clear_cache() -> None:
    """清除快取（供測試用）。"""
    global _cached_charmap, _cached_table, _cached_ambiguous, _cached_balanced_defaults
    with _lock:
        _cached_charmap = None
        _cached_table = None
        _cached_ambiguous = None
        _cached_balanced_defaults = None
```

- [ ] **Step 4: 執行測試確認通過**

Run: `pytest tests/test_ambiguous_balanced.py -v`
Expected: all PASS

- [ ] **Step 5: Commit**

```bash
git add src/zhtw/charconv.py tests/test_ambiguous_balanced.py
git commit -m "feat: charconv 新增 balanced defaults 載入與套用"
```

---

### Task 3: converter.py — 穿透 ambiguity_mode 參數

**Files:**
- Modify: `src/zhtw/converter.py`
- Modify: `tests/test_ambiguous_balanced.py`

- [ ] **Step 1: 寫失敗的整合測試**

在 `tests/test_ambiguous_balanced.py` 新增：

```python
from zhtw.converter import convert_text, convert
from zhtw.charconv import get_translate_table
from zhtw.dictionary import load_dictionary
from zhtw.matcher import Matcher


@pytest.fixture
def matcher():
    terms = load_dictionary(sources=["cn", "hk"])
    return Matcher(terms)


@pytest.fixture
def char_table():
    return get_translate_table()


class TestConvertTextBalanced:
    """convert_text() 的 balanced mode。"""

    def test_balanced_converts_ambiguous_char(self, matcher, char_table):
        """balanced mode 轉換單獨出現的歧義字。"""
        result, _ = convert_text(
            "几个人来了",
            matcher,
            fix=True,
            char_table=char_table,
            ambiguity_mode="balanced",
        )
        assert "幾個人" in result

    def test_strict_does_not_convert_ambiguous_char(self, matcher, char_table):
        """strict mode 不轉換單獨的歧義字（現行行為不變）。"""
        result, _ = convert_text(
            "几个人",
            matcher,
            fix=True,
            char_table=char_table,
            ambiguity_mode="strict",
        )
        # 几 不在 safe charmap 中，strict mode 不會轉
        assert "几" in result

    def test_term_layer_overrides_balanced(self, matcher, char_table):
        """詞庫層的轉換優先於 balanced 預設值。"""
        result, _ = convert_text(
            "茶几",
            matcher,
            fix=True,
            char_table=char_table,
            ambiguity_mode="balanced",
        )
        # 茶几 是 identity protect 詞，不應被改
        assert result == "茶几" or "几" in result  # 詞庫層保護

    def test_default_mode_is_strict(self, matcher, char_table):
        """不傳 ambiguity_mode 時預設為 strict。"""
        result_default, _ = convert_text(
            "几个人",
            matcher,
            fix=True,
            char_table=char_table,
        )
        result_strict, _ = convert_text(
            "几个人",
            matcher,
            fix=True,
            char_table=char_table,
            ambiguity_mode="strict",
        )
        assert result_default == result_strict


class TestConvertConvenienceBalanced:
    """convert() 便利函式的 balanced mode。"""

    def test_balanced_mode(self):
        result = convert("几个人", ambiguity_mode="balanced")
        assert "幾" in result

    def test_strict_mode(self):
        result = convert("几个人", ambiguity_mode="strict")
        assert "几" in result

    def test_invalid_mode_raises(self):
        with pytest.raises(ValueError, match="ambiguity_mode"):
            convert("test", ambiguity_mode="invalid")
```

- [ ] **Step 2: 執行測試確認失敗**

Run: `pytest tests/test_ambiguous_balanced.py::TestConvertTextBalanced -v`
Expected: FAIL — `convert_text() got an unexpected keyword argument 'ambiguity_mode'`

- [ ] **Step 3: 修改 convert_text()**

在 `src/zhtw/converter.py` 修改 `convert_text()` 簽名和邏輯（行 310）：

```python
VALID_AMBIGUITY_MODES = {"strict", "balanced"}


def convert_text(
    text: str,
    matcher: Matcher,
    fix: bool = False,
    ignored_lines: Optional[Set[int]] = None,
    char_table: Optional[dict[int, str]] = None,
    ambiguity_mode: str = "strict",
) -> tuple[str, List[tuple[Match, int, int]]]:
    """
    Convert text using matcher.

    Args:
        text: Text to process.
        matcher: Matcher instance.
        fix: Whether to apply fixes.
        ignored_lines: Set of line numbers to skip.
        char_table: Character-level translate table (str.translate format).
        ambiguity_mode: "strict" (default, no ambiguous char defaults) or
            "balanced" (apply curated defaults for high-confidence chars).

    Returns:
        Tuple of (processed_text, list of (match, line, col)).
    """
    if ambiguity_mode not in VALID_AMBIGUITY_MODES:
        raise ValueError(
            f"ambiguity_mode must be one of {sorted(VALID_AMBIGUITY_MODES)}, "
            f"got {ambiguity_mode!r}"
        )

    if ignored_lines is None:
        ignored_lines = set()

    all_matches = list(matcher.find_matches_with_lines(text))

    # Filter out matches on ignored lines
    matches = [(m, line, col) for m, line, col in all_matches if line not in ignored_lines]

    if fix and (matches or char_table or ambiguity_mode == "balanced"):
        text = _replace_with_ignores(
            text, matcher, ignored_lines, char_table,
            ambiguity_mode=ambiguity_mode,
        )

    # In check mode, also detect char-level conversions
    if not fix and char_table:
        char_matches = _find_char_matches(text, char_table, ignored_lines)
        matches = matches + char_matches

    return text, matches
```

- [ ] **Step 4: 修改 _replace_with_ignores()**

修改 `_replace_with_ignores()`（行 479）以支援 balanced mode：

```python
def _replace_with_ignores(
    text: str,
    matcher: Matcher,
    ignored_lines: Set[int],
    char_table: Optional[dict[int, str]] = None,
    ambiguity_mode: str = "strict",
) -> str:
    """Replace matches while respecting ignored lines."""
    if not ignored_lines:
        result, covered = _apply_term_layer(text, matcher)
        if ambiguity_mode == "balanced":
            from .charconv import apply_balanced_defaults
            result = apply_balanced_defaults(result, covered)
        if char_table:
            result = result.translate(char_table)
        return result

    # Process line by line
    lines = text.split("\n")
    result_lines = []

    for i, line in enumerate(lines):
        line_num = i + 1
        if line_num in ignored_lines:
            result_lines.append(line)
        else:
            converted, covered = _apply_term_layer(line, matcher)
            if ambiguity_mode == "balanced":
                from .charconv import apply_balanced_defaults
                converted = apply_balanced_defaults(converted, covered)
            if char_table:
                converted = converted.translate(char_table)
            result_lines.append(converted)

    return "\n".join(result_lines)
```

- [ ] **Step 5: 新增 _apply_term_layer() helper**

在 `_replace_with_ignores()` 之前新增：

```python
def _apply_term_layer(text: str, matcher: Matcher) -> tuple[str, set[int]]:
    """Apply term-layer replacements and return covered char positions.

    Returns:
        Tuple of (replaced_text, set of original char positions covered by matches).
    """
    matches = list(matcher.find_matches(text))
    if not matches:
        return text, set()

    covered: set[int] = set()
    for m in matches:
        for pos in range(m.start, m.end):
            covered.add(pos)

    result = matcher.replace_all(text)
    return result, covered
```

- [ ] **Step 6: 修改 convert() 便利函式**

修改 `convert()`（行 362）簽名，新增 `ambiguity_mode` 參數：

在函式簽名中新增：
```python
def convert(
    text: str,
    sources: Optional[List[str]] = None,
    ambiguity_mode: str = "strict",
) -> str:
```

在函式尾部（行 449）修改呼叫：
```python
    matcher, char_table = cached
    if ambiguity_mode not in VALID_AMBIGUITY_MODES:
        raise ValueError(
            f"ambiguity_mode must be one of {sorted(VALID_AMBIGUITY_MODES)}, "
            f"got {ambiguity_mode!r}"
        )
    result, _ = convert_text(
        text, matcher, fix=True, char_table=char_table,
        ambiguity_mode=ambiguity_mode,
    )
    return result
```

- [ ] **Step 7: 執行測試確認通過**

Run: `pytest tests/test_ambiguous_balanced.py -v`
Expected: all PASS

- [ ] **Step 8: 執行現有測試確認 strict 行為不變**

Run: `pytest tests/ -v`
Expected: all PASS（現有測試全部預設 strict，行為不變）

- [ ] **Step 9: Commit**

```bash
git add src/zhtw/converter.py tests/test_ambiguous_balanced.py
git commit -m "feat: convert_text/convert 支援 ambiguity_mode 參數"
```

---

### Task 4: converter.py — 穿透 ambiguity_mode 到檔案層

**Files:**
- Modify: `src/zhtw/converter.py`

convert_file()、convert_directory()、process_directory() 都需要穿透 ambiguity_mode。

- [ ] **Step 1: 修改 convert_file()**

在 `convert_file()` 簽名（行 511 附近）新增參數：

```python
def convert_file(
    path: Path,
    matcher: Matcher,
    fix: bool = False,
    input_encoding: str | None = None,
    output_encoding: str = "auto",
    char_table: Optional[dict[int, str]] = None,
    ambiguity_mode: str = "strict",
) -> FileResult:
```

在函式內呼叫 `convert_text()` 的地方加上 `ambiguity_mode=ambiguity_mode`。

- [ ] **Step 2: 修改 convert_directory()**

找到 `convert_directory()` 或 `process_directory()`，同樣新增 `ambiguity_mode: str = "strict"` 參數並穿透到 `convert_file()`。

- [ ] **Step 3: 執行全部測試**

Run: `pytest tests/ -v`
Expected: all PASS

- [ ] **Step 4: Commit**

```bash
git add src/zhtw/converter.py
git commit -m "feat: ambiguity_mode 穿透到 convert_file/directory 層"
```

---

### Task 5: CLI — --ambiguity-mode flag

**Files:**
- Modify: `src/zhtw/cli.py`
- Modify: `tests/test_ambiguous_balanced.py`

- [ ] **Step 1: 寫 CLI 測試**

在 `tests/test_ambiguous_balanced.py` 新增：

```python
from click.testing import CliRunner
from zhtw.cli import main
import tempfile
import os


class TestCLIAmbiguityMode:
    """CLI --ambiguity-mode flag。"""

    def test_fix_balanced_mode(self, tmp_path):
        """fix --ambiguity-mode balanced 轉換歧義字。"""
        test_file = tmp_path / "test.txt"
        test_file.write_text("几个人", encoding="utf-8")

        runner = CliRunner()
        result = runner.invoke(main, [
            "fix", str(test_file),
            "--ambiguity-mode", "balanced",
            "--yes",
        ])
        assert result.exit_code == 0
        content = test_file.read_text(encoding="utf-8")
        assert "幾" in content

    def test_fix_strict_mode_default(self, tmp_path):
        """fix 不帶 flag 時預設 strict，不轉換歧義字。"""
        test_file = tmp_path / "test.txt"
        test_file.write_text("几个人", encoding="utf-8")

        runner = CliRunner()
        result = runner.invoke(main, [
            "fix", str(test_file), "--yes",
        ])
        assert result.exit_code == 0
        content = test_file.read_text(encoding="utf-8")
        assert "几" in content

    def test_invalid_mode_error(self):
        """無效的 ambiguity-mode 值應報錯。"""
        runner = CliRunner()
        result = runner.invoke(main, [
            "check", ".", "--ambiguity-mode", "invalid",
        ])
        assert result.exit_code != 0
```

- [ ] **Step 2: 執行測試確認失敗**

Run: `pytest tests/test_ambiguous_balanced.py::TestCLIAmbiguityMode -v`
Expected: FAIL — `No such option: --ambiguity-mode`

- [ ] **Step 3: 在 check 和 fix 命令加 flag**

在 `src/zhtw/cli.py` 的 `check` 命令裝飾器中新增（在 `--no-char-convert` 之後）：

```python
@click.option(
    "--ambiguity-mode",
    type=click.Choice(["strict", "balanced"], case_sensitive=False),
    default="strict",
    help="歧義字處理模式。strict（預設）：不轉換歧義字。balanced：套用高信心預設映射。",
)
```

在 `check()` 函式簽名新增 `ambiguity_mode` 參數，並傳遞到 `process_directory()` 呼叫。

在 `fix` 命令做同樣的修改。

- [ ] **Step 4: 執行測試確認通過**

Run: `pytest tests/test_ambiguous_balanced.py::TestCLIAmbiguityMode -v`
Expected: all PASS

- [ ] **Step 5: 執行全部測試**

Run: `pytest tests/ -v`
Expected: all PASS

- [ ] **Step 6: Commit**

```bash
git add src/zhtw/cli.py tests/test_ambiguous_balanced.py
git commit -m "feat: CLI fix/check 新增 --ambiguity-mode flag"
```

---

### Task 6: export.py — 輸出 balanced_defaults 到 zhtw-data.json

**Files:**
- Modify: `src/zhtw/export.py`

- [ ] **Step 1: 修改 export_data()**

在 `src/zhtw/export.py` 的 `export_data()` 中，import 新函式並加入 balanced_defaults：

```python
from .charconv import get_ambiguous_chars, get_balanced_defaults, get_translate_table, load_charmap
```

在 `return` 語句的 `"charmap"` 區段新增：

```python
    "charmap": {
        "chars": charmap,
        "ambiguous": sorted(ambiguous),
        "balanced_defaults": get_balanced_defaults(),
    },
```

- [ ] **Step 2: 驗證 export 輸出**

Run: `python3 -m zhtw export --output /tmp/test-export && python3 -c "import json; d=json.load(open('/tmp/test-export/zhtw-data.json')); print(d['charmap']['balanced_defaults'])"`
Expected: `{'几': '幾', '丰': '豐', '杰': '傑'}`

- [ ] **Step 3: 重新產生 sdk/data**

Run: `python3 -m zhtw export --output sdk/data && cp sdk/data/zhtw-data.json sdk/rust/zhtw/data/zhtw-data.json`

- [ ] **Step 4: Commit**

```bash
git add src/zhtw/export.py sdk/data/zhtw-data.json sdk/data/golden-test.json sdk/rust/zhtw/data/zhtw-data.json
git commit -m "feat: export 輸出 balanced_defaults 到 zhtw-data.json"
```

---

### Task 7: strict 不變性驗證 + 最終測試

**Files:**
- Modify: `tests/test_ambiguous_balanced.py`

- [ ] **Step 1: 新增 strict 不變性回歸測試**

在 `tests/test_ambiguous_balanced.py` 新增：

```python
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
        for char in ["几", "丰", "杰"]:
            result = convert(char, ambiguity_mode="strict")
            assert result == char, f"strict should not convert bare {char!r}, got {result!r}"

    def test_balanced_converts_bare_ambiguous(self):
        """單獨歧義字在 balanced mode 被轉換。"""
        expectations = {"几": "幾", "丰": "豐", "杰": "傑"}
        for char, expected in expectations.items():
            result = convert(char, ambiguity_mode="balanced")
            assert result == expected, f"balanced: {char!r} → {result!r}, expected {expected!r}"
```

- [ ] **Step 2: 執行全部測試**

Run: `pytest tests/ -v`
Expected: all PASS

- [ ] **Step 3: 執行 ruff 和 format**

Run: `ruff check src/ tests/ && ruff format --check src/ tests/`
Expected: no issues

- [ ] **Step 4: Commit**

```bash
git add tests/test_ambiguous_balanced.py
git commit -m "test: balanced mode 完整測試 + strict 不變性回歸"
```

---

## Self-Review Checklist

**Spec coverage:**
- ✅ §1 設計決定：2 modes, 3 chars, converter-level API → Task 3, 5
- ✅ §2 轉換管線：歧義層插在詞庫層和字元層之間 → Task 3 (_apply_term_layer + apply_balanced_defaults)
- ✅ §3 v1 字表：几→幾、丰→豐、杰→傑 → Task 1
- ✅ §4 API 設計：Python Converter + CLI flag → Task 3, 5
- ✅ §5 資料格式：balanced_defaults in zhtw-data.json → Task 6
- ✅ §6 實作位置：所有檔案都有對應 task
- ✅ §7 測試策略：正向/負向/strict 不變/API 驗證 → Task 2, 3, 5, 7
- ✅ §8 不做的事：不做全域 config、不做其他 SDK、不改 strict

**Placeholder scan:** 無 TBD/TODO。所有步驟都有完整程式碼。

**Type consistency:** `ambiguity_mode: str = "strict"` 一致使用。`apply_balanced_defaults(text, covered_positions)` 簽名一致。`VALID_AMBIGUITY_MODES` 定義一次，多處引用。
