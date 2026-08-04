<!-- zhtw:disable -->
# Disambiguation v2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace `balanced_defaults.json` with structured `disambiguation.json`, inject protect_terms as identity terms into the matcher, and add golden tests for balanced mode disambiguation (后→後、里→裡).

**Architecture:** Single canonical data file `disambiguation.json` with `default` + `protect_terms` per ambiguous character. Python loader extracts flat defaults and injects protect_terms as identity terms into the Aho-Corasick matcher. SDK export adds `balanced_protect_terms` field to `zhtw-data.json`.

**Tech Stack:** Python (ahocorasick), JSON data files, pytest

---

### Task 1: Create disambiguation.json and delete balanced_defaults.json

**Files:**
- Create: `src/zhtw/data/charmap/disambiguation.json`
- Delete: `src/zhtw/data/charmap/balanced_defaults.json`

- [ ] **Step 1: Create disambiguation.json**

Create `src/zhtw/data/charmap/disambiguation.json` with this exact content:

```json
{
  "schema_version": 1,
  "rules": {
    "几": { "default": "幾" },
    "丰": { "default": "豐" },
    "杰": { "default": "傑" },
    "卤": { "default": "滷" },
    "坛": { "default": "壇" },
    "弥": { "default": "彌" },
    "摆": { "default": "擺" },
    "纤": { "default": "纖" },
    "后": {
      "default": "後",
      "protect_terms": ["皇后", "太后", "后妃", "后土", "影后", "歌后", "后冠"]
    },
    "里": {
      "default": "裡",
      "protect_terms": ["公里", "英里", "海里", "里程", "里長", "鄰里", "故里", "里民", "里幹事", "三里屯"]
    }
  }
}
```

- [ ] **Step 2: Delete balanced_defaults.json**

```bash
rm src/zhtw/data/charmap/balanced_defaults.json
```

- [ ] **Step 3: Commit data file changes**

```bash
cd /Users/tim/GitHub/zhtw
git add src/zhtw/data/charmap/disambiguation.json
git rm src/zhtw/data/charmap/balanced_defaults.json
git commit -m "$(cat <<'EOF'
feat: 新增 disambiguation.json 取代 balanced_defaults.json

v2 歧義字消歧框架：default + protect_terms 模型。
合併 v1 的 8 個 entries，新增 后/里 含保護詞組。

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"
```

---

### Task 2: Update charconv.py to read disambiguation.json

**Files:**
- Modify: `src/zhtw/charconv.py`
- Test: `tests/test_ambiguous_balanced.py`

- [ ] **Step 1: Run existing tests to confirm baseline**

```bash
cd /Users/tim/GitHub/zhtw
uv run pytest tests/test_ambiguous_balanced.py -x -q 2>&1 | tail -5
```

Expected: FAIL (because `balanced_defaults.json` was deleted in Task 1).

- [ ] **Step 2: Update charconv.py**

In `src/zhtw/charconv.py`, make these changes:

**Change 1** — Update file path constant (line 17):

Replace:
```python
BALANCED_DEFAULTS_FILE = CHARMAP_DIR / "balanced_defaults.json"
```

With:
```python
DISAMBIGUATION_FILE = CHARMAP_DIR / "disambiguation.json"
```

**Change 2** — Add `_cached_protect_terms` to cache variables (line 24):

Replace:
```python
_cached_balanced_defaults: Optional[Dict[str, str]] = None
```

With:
```python
_cached_balanced_defaults: Optional[Dict[str, str]] = None
_cached_protect_terms: Optional[Dict[str, List[str]]] = None
```

**Change 3** — Rewrite `get_balanced_defaults()` (lines 95-109):

Replace the entire function with:
```python
def get_balanced_defaults(path: Optional[Path] = None) -> Dict[str, str]:
    """從 disambiguation.json 萃取 {char: default} flat view，有快取。"""
    global _cached_balanced_defaults
    if _cached_balanced_defaults is not None and path is None:
        return _cached_balanced_defaults

    p = path or DISAMBIGUATION_FILE
    with open(p, encoding="utf-8") as f:
        data = json.load(f)

    result: Dict[str, str] = {}
    for char, rule in data.get("rules", {}).items():
        result[char] = rule["default"]

    if path is None:
        with _lock:
            _cached_balanced_defaults = result
    return result
```

**Change 4** — Add `get_protect_terms()` after `get_balanced_defaults()`:

```python
def get_protect_terms(path: Optional[Path] = None) -> Dict[str, List[str]]:
    """從 disambiguation.json 萃取 {char: [term, ...]} protect_terms，有快取。"""
    global _cached_protect_terms
    if _cached_protect_terms is not None and path is None:
        return _cached_protect_terms

    p = path or DISAMBIGUATION_FILE
    with open(p, encoding="utf-8") as f:
        data = json.load(f)

    result: Dict[str, List[str]] = {}
    for char, rule in data.get("rules", {}).items():
        terms = rule.get("protect_terms")
        if terms:
            result[char] = terms

    if path is None:
        with _lock:
            _cached_protect_terms = result
    return result
```

**Change 5** — Update `clear_cache()` (lines 143-150):

Replace:
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

With:
```python
def clear_cache() -> None:
    """清除快取（供測試用）。"""
    global _cached_charmap, _cached_table, _cached_ambiguous, _cached_balanced_defaults, _cached_protect_terms
    with _lock:
        _cached_charmap = None
        _cached_table = None
        _cached_ambiguous = None
        _cached_balanced_defaults = None
        _cached_protect_terms = None
```

- [ ] **Step 3: Run existing balanced tests**

```bash
uv run pytest tests/test_ambiguous_balanced.py::TestGetBalancedDefaults -x -v 2>&1 | tail -15
uv run pytest tests/test_ambiguous_balanced.py::TestApplyBalancedDefaults -x -v 2>&1 | tail -15
```

Expected: all pass (same 8 entries, same behavior, just different source file).

- [ ] **Step 4: Commit charconv.py changes**

```bash
git add src/zhtw/charconv.py
git commit -m "$(cat <<'EOF'
refactor: charconv 改讀 disambiguation.json + 新增 get_protect_terms()

get_balanced_defaults() 從 rules 萃取 flat view，行為不變。
get_protect_terms() 回傳 {char: [term, ...]} 供 matcher 注入。

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"
```

---

### Task 3: Inject protect_terms into matcher via converter.py

**Files:**
- Modify: `src/zhtw/converter.py:554-570`

- [ ] **Step 1: Update converter.py `convert()` function**

In `src/zhtw/converter.py`, find the matcher construction block inside `convert()` (lines 561-569):

```python
            if cached is None:
                terms = load_dictionary(sources=sources)
                matcher = Matcher(terms)
                char_table = None
                if sources is None or "cn" in sources:
                    from .charconv import get_translate_table

                    char_table = get_translate_table()
                cached = (matcher, char_table)
```

Replace with:

```python
            if cached is None:
                terms = load_dictionary(sources=sources)
                # Inject protect_terms as identity terms (source == target).
                # These are no-ops in strict mode (ambiguous chars aren't in
                # safe_chars) but block balanced-layer default overwrite via
                # covered positions.
                if sources is None or "cn" in sources:
                    from .charconv import get_protect_terms, get_translate_table

                    for _char, pterms in get_protect_terms().items():
                        for term in pterms:
                            terms[term] = term  # identity mapping
                    char_table = get_translate_table()
                else:
                    char_table = None
                matcher = Matcher(terms)
                cached = (matcher, char_table)
```

Note: `Matcher(terms)` must come AFTER protect_terms injection so the automaton includes the identity terms.

- [ ] **Step 2: Run strict mode regression tests**

```bash
uv run pytest tests/test_ambiguous_balanced.py::TestStrictUnchanged -x -v 2>&1 | tail -15
```

Expected: all pass (identity terms are no-ops in strict mode).

- [ ] **Step 3: Run all balanced tests**

```bash
uv run pytest tests/test_ambiguous_balanced.py -x -v 2>&1 | tail -20
```

Expected: all pass.

- [ ] **Step 4: Commit converter.py changes**

```bash
git add src/zhtw/converter.py
git commit -m "$(cat <<'EOF'
feat: convert() 注入 protect_terms 為 identity terms

所有模式統一注入，strict 下是 no-op，balanced 下阻止 default 覆寫。
Matcher 建構移到 protect_terms 注入之後。

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"
```

---

### Task 4: Add disambiguation data integrity + integration tests

**Files:**
- Modify: `tests/test_ambiguous_balanced.py`

- [ ] **Step 1: Add data integrity tests**

Add this new test class to `tests/test_ambiguous_balanced.py`, after the existing imports (before `TestGetBalancedDefaults`):

```python
class TestDisambiguationData:
    """disambiguation.json 資料完整性。"""

    def test_schema_version_exists(self):
        import json
        from pathlib import Path

        path = Path(__file__).parent.parent / "src" / "zhtw" / "data" / "charmap" / "disambiguation.json"
        data = json.loads(path.read_text("utf-8"))
        assert isinstance(data["schema_version"], int)

    def test_every_rule_has_default(self):
        import json
        from pathlib import Path

        path = Path(__file__).parent.parent / "src" / "zhtw" / "data" / "charmap" / "disambiguation.json"
        data = json.loads(path.read_text("utf-8"))
        for char, rule in data["rules"].items():
            assert "default" in rule, f"{char!r} missing default"
            assert len(rule["default"]) == 1, f"{char!r} default is not single char"

    def test_protect_terms_contain_their_char(self):
        import json
        from pathlib import Path

        path = Path(__file__).parent.parent / "src" / "zhtw" / "data" / "charmap" / "disambiguation.json"
        data = json.loads(path.read_text("utf-8"))
        for char, rule in data["rules"].items():
            for term in rule.get("protect_terms", []):
                assert char in term, f"protect_term {term!r} does not contain {char!r}"

    def test_rule_keys_in_ambiguous_excluded(self):
        from zhtw.charconv import get_ambiguous_chars
        import json
        from pathlib import Path

        ambiguous = set(get_ambiguous_chars())
        path = Path(__file__).parent.parent / "src" / "zhtw" / "data" / "charmap" / "disambiguation.json"
        data = json.loads(path.read_text("utf-8"))
        for char in data["rules"]:
            assert char in ambiguous, f"rule key {char!r} not in ambiguous_excluded"

    def test_v1_entries_all_present(self):
        from zhtw.charconv import get_balanced_defaults

        defaults = get_balanced_defaults()
        v1_chars = {"几", "丰", "杰", "卤", "坛", "弥", "摆", "纤"}
        for char in v1_chars:
            assert char in defaults, f"v1 char {char!r} missing from disambiguation.json"
```

- [ ] **Step 2: Add protect_terms integration tests**

Add this new test class after the existing `TestConvertConvenienceBalanced`:

```python
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

    def test_strict_mode_unchanged(self):
        """strict mode 下后/里不轉。"""
        assert convert("\u4ee5\u540e\u518d\u8bf4", ambiguity_mode="strict") == "以后再說"
        assert convert("\u7687\u540e\u5f88\u7f8e", ambiguity_mode="strict") == "皇后很美"
        assert convert("\u5bb6\u91cc\u5f88\u5927", ambiguity_mode="strict") == "家里很大"
        assert convert("\u516c\u91cc\u6570\u5f88\u5927", ambiguity_mode="strict") == "公里數很大"
```

- [ ] **Step 3: Update test_contains_eight_entries → ten entries**

In `tests/test_ambiguous_balanced.py`, find `TestGetBalancedDefaults.test_contains_eight_entries` (line 39-41):

Replace:
```python
    def test_contains_eight_entries(self):
        defaults = get_balanced_defaults()
        assert len(defaults) == 8
```

With:
```python
    def test_contains_ten_entries(self):
        defaults = get_balanced_defaults()
        assert len(defaults) == 10
```

Also in `TestGetBalancedDefaults.test_keys_and_values` (lines 43-52), add the two new entries:

After `assert defaults.get("杰") == "傑"` add:
```python
        assert defaults.get("后") == "後"
        assert defaults.get("里") == "裡"
```

- [ ] **Step 4: Run all tests**

```bash
uv run pytest tests/test_ambiguous_balanced.py -x -v 2>&1 | tail -30
```

Expected: all pass.

- [ ] **Step 5: Run full test suite to verify no regressions**

```bash
uv run pytest tests/ -x -q 2>&1 | tail -5
```

Expected: all pass (735+).

- [ ] **Step 6: Commit test changes**

```bash
git add tests/test_ambiguous_balanced.py
git commit -m "$(cat <<'EOF'
test: disambiguation v2 資料完整性 + 后/里 protect_terms 整合測試

- 驗證 disambiguation.json schema、protect_terms 包含歧義字
- 后 default 後 + 皇后/太后保護
- 里 default 裡 + 公里/英里/里程保護
- strict mode 不變性回歸

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"
```

---

### Task 5: Update export.py and regenerate SDK data

**Files:**
- Modify: `src/zhtw/export.py`

- [ ] **Step 1: Update export_data() to include balanced_protect_terms**

In `src/zhtw/export.py`, add `get_protect_terms` to the import (line 10):

Replace:
```python
from .charconv import get_ambiguous_chars, get_balanced_defaults, get_translate_table, load_charmap
```

With:
```python
from .charconv import (
    get_ambiguous_chars,
    get_balanced_defaults,
    get_protect_terms,
    get_translate_table,
    load_charmap,
)
```

Then in `export_data()`, update the charmap section (lines 47-51):

Replace:
```python
        "charmap": {
            "chars": charmap,
            "ambiguous": sorted(ambiguous),
            "balanced_defaults": get_balanced_defaults(),
        },
```

With:
```python
        "charmap": {
            "chars": charmap,
            "ambiguous": sorted(ambiguous),
            "balanced_defaults": get_balanced_defaults(),
            "balanced_protect_terms": get_protect_terms(),
        },
```

- [ ] **Step 2: Add balanced mode golden test cases**

In `_GOLDEN_CASES`, add balanced mode cases. The tuple format needs a 4th element for ambiguity_mode. Update the tuple format:

Replace the entire `_GOLDEN_CASES` list with:

```python
_GOLDEN_CASES = [
    # (input_text, sources, description, ambiguity_mode)
    # ambiguity_mode defaults to "strict" if omitted (3-tuple)
    ("\u8f6f\u4ef6\u6d4b\u8bd5", ["cn"], "term layer: multi-term"),
    ("\u8fd9\u4e2a\u670d\u52a1\u5668\u7684\u5185\u5b58\u4e0d\u591f", ["cn"], "mixed"),
    ("\u5934\u53d1\u5f88\u5e72", ["cn"], "ambiguous chars"),
    ("\u8edf\u4ef6\u5de5\u7a0b\u5e2b", ["hk"], "HK source: term only"),
    ("\u5df2\u7d93\u662f\u7e41\u9ad4", ["cn"], "no conversion needed"),
    ("\u6570\u636e\u5e93\u670d\u52a1\u5668", ["cn"], "term layer: compound terms"),
    ("\u4e91\u8ba1\u7b97", ["cn"], "ambiguous: cloud"),
    ("\u53d1\u5c55\u5f88\u5feb", ["cn"], "ambiguous: fa"),
    # Identity-term protection: char layer must NOT convert chars inside identity terms
    ("\u5c38\u4f4d\u7d20\u9910", ["cn"], "identity: \u5c38\u4f4d\u7d20\u9910 protects \u5c38"),
    ("\u4eba\u4e91\u4ea6\u4e91", ["cn"], "identity: \u4eba\u4e91\u4ea6\u4e91 protects \u4e91"),
    (
        "\u6025\u75c7\u5f88\u4e25\u91cd",
        ["cn"],
        "identity+char: \u6025\u75c7 protected, \u4e25\u91cd char-converted",
    ),
    ("\u708e\u75c7", ["cn"], "identity: \u708e\u75c7 protects \u75c7 (medical pattern)"),
    (
        "\u515a\u592a\u5c09\u5403\u5339\u98df",
        ["cn"],
        "identity: \u515a\u592a\u5c09\u5403\u5339\u98df protects \u515a (proper name)",
    ),
    # Balanced mode: disambiguation v2 protect_terms
    ("\u4ee5\u540e\u518d\u8bf4", ["cn"], "balanced: \u540e default \u5f8c", "balanced"),
    ("\u7687\u540e\u5f88\u7f8e", ["cn"], "balanced: \u7687\u540e protected", "balanced"),
    ("\u5bb6\u91cc\u5f88\u5927", ["cn"], "balanced: \u91cc default \u88e1", "balanced"),
    ("\u516c\u91cc\u6570\u5f88\u5927", ["cn"], "balanced: \u516c\u91cc protected", "balanced"),
]
```

- [ ] **Step 3: Update generate_golden_test() to handle ambiguity_mode**

In `generate_golden_test()`, the loop over `_GOLDEN_CASES` (line 110) unpacks 3-tuples. Update to handle optional 4th element:

Replace:
```python
    for input_text, srcs, _desc in _GOLDEN_CASES:
        if sources is not None and not all(s in sources for s in srcs):
            continue
        terms = load_dictionary(sources=srcs)
        matcher = Matcher(terms)
        char_table = get_translate_table() if "cn" in srcs else None

        # Convert
        converted, _ = convert_text(input_text, matcher, fix=True, char_table=char_table)
        convert_cases.append(
            {
                "input": input_text,
                "sources": srcs,
                "expected": converted,
            }
        )

        # Check — get matches with positions
        _, matches = convert_text(input_text, matcher, fix=False, char_table=char_table)
        check_cases.append(
            {
                "input": input_text,
                "sources": srcs,
                "expected_matches": [
                    {
                        "start": m.start,
                        "end": m.end,
                        "source": m.source,
                        "target": m.target,
                    }
                    for m, _line, _col in matches
                ],
            }
        )
```

With:
```python
    for case in _GOLDEN_CASES:
        input_text, srcs, _desc = case[0], case[1], case[2]
        mode = case[3] if len(case) > 3 else "strict"

        if sources is not None and not all(s in sources for s in srcs):
            continue

        terms = load_dictionary(sources=srcs)
        # Inject protect_terms for balanced mode golden tests
        if "cn" in srcs:
            from .charconv import get_protect_terms

            for _char, pterms in get_protect_terms().items():
                for term in pterms:
                    terms[term] = term
        matcher = Matcher(terms)
        char_table = get_translate_table() if "cn" in srcs else None

        # Convert
        converted, _ = convert_text(
            input_text, matcher, fix=True, char_table=char_table, ambiguity_mode=mode,
        )
        entry: Dict[str, Any] = {
            "input": input_text,
            "sources": srcs,
            "expected": converted,
        }
        if mode != "strict":
            entry["ambiguity_mode"] = mode
        convert_cases.append(entry)

        # Check — get matches with positions
        _, matches = convert_text(
            input_text, matcher, fix=False, char_table=char_table, ambiguity_mode=mode,
        )
        check_entry: Dict[str, Any] = {
            "input": input_text,
            "sources": srcs,
            "expected_matches": [
                {
                    "start": m.start,
                    "end": m.end,
                    "source": m.source,
                    "target": m.target,
                }
                for m, _line, _col in matches
            ],
        }
        if mode != "strict":
            check_entry["ambiguity_mode"] = mode
        check_cases.append(check_entry)
```

- [ ] **Step 4: Run export and regenerate SDK data**

```bash
cd /Users/tim/GitHub/zhtw
make export 2>&1 | tail -5
```

Expected: success, files regenerated.

- [ ] **Step 5: Verify golden-test.json contains balanced cases**

```bash
grep -c "ambiguity_mode" sdk/data/golden-test.json
```

Expected: 8 (4 balanced convert + 4 balanced check cases).

- [ ] **Step 6: Run full Python test suite**

```bash
uv run pytest tests/ -x -q 2>&1 | tail -5
```

Expected: all pass.

- [ ] **Step 7: Commit export changes and regenerated data**

```bash
git add src/zhtw/export.py sdk/data/zhtw-data.json sdk/data/golden-test.json sdk/rust/zhtw/data/zhtw-data.json
git commit -m "$(cat <<'EOF'
feat: export balanced_protect_terms + balanced mode golden cases

- zhtw-data.json 新增 balanced_protect_terms 欄位
- golden-test.json 新增 后/里 balanced mode 測試案例
- 含 ambiguity_mode 欄位（預設 strict 時省略）

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"
```

---

### Task 6: Cross-SDK verification

**Files:** (no changes — verification only)

- [ ] **Step 1: Run Python tests**

```bash
cd /Users/tim/GitHub/zhtw
uv run pytest tests/ -x -q 2>&1 | tail -5
```

Expected: all pass.

- [ ] **Step 2: Run Java SDK tests**

```bash
cd /Users/tim/GitHub/zhtw/sdk/java
mvn test -q --batch-mode 2>&1 | tail -10
```

Expected: pass (Java golden test runner skips cases with unknown `ambiguity_mode` or passes existing strict cases unchanged).

- [ ] **Step 3: Run TypeScript SDK tests**

```bash
cd /Users/tim/GitHub/zhtw/sdk/typescript
npm test 2>&1 | tail -10
```

Expected: pass.

- [ ] **Step 4: Run Rust SDK tests**

```bash
export PATH="$HOME/.cargo/bin:$PATH"
cd /Users/tim/GitHub/zhtw/sdk/rust
cargo test --package zhtw 2>&1 | tail -10
```

Expected: pass.

- [ ] **Step 5: Verify git status is clean**

```bash
cd /Users/tim/GitHub/zhtw
git status --short
```

Expected: clean working tree.

- [ ] **Step 6: Push all changes**

```bash
git push
```
