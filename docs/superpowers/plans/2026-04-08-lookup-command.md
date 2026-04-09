# zhtw lookup 指令 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 新增 `zhtw lookup` CLI 指令，讓使用者能快速查詢任意詞/句的簡繁轉換結果與來源歸因（詞彙層 vs 字元層）。

**Architecture:** 核心歸因邏輯獨立為 `src/zhtw/lookup.py` 模組，CLI 層（`cli.py`）只負責輸入解析和輸出格式化。歸因流程：先跑 Matcher 取得詞彙層命中範圍，再逐字掃描 charmap 處理剩餘位置，兩層不重疊。

**Tech Stack:** Python 3.9+、Click（CLI）、ahocorasick（Matcher）、dataclasses

**Spec:** `docs/superpowers/specs/2026-04-08-lookup-command-design.md`

---

## File Structure

| 操作 | 檔案 | 職責 |
|------|------|------|
| Create | `src/zhtw/lookup.py` | `Con1.0Detail`、`LookupResult` dataclass + `lookup_word`、`lookup_words` 函式 |
| Modify | `src/zhtw/__init__.py` | `__all__` 加入 lookup 公開 API |
| Modify | `src/zhtw/cli.py` | 新增 `lookup` command |
| Create | `tests/test_lookup.py` | lookup 模組單元測試 + CLI 整合測試 |

---

### Task 1: lookup 核心模組 — 資料模型 + 純詞彙層歸因

**Files:**
- Create: `src/zhtw/lookup.py`
- Create: `tests/test_lookup.py`

- [ ] **Step 1: 建立測試檔案，寫純詞彙層命中的 failing test**

```python
# tests/test_lookup.py
"""Tests for lookup module."""
# zhtw:disable

from __future__ import annotations

import pytest

from zhtw.charconv import get_translate_table
from zhtw.dictionary import load_dictionary
from zhtw.lookup import ConversionDetail, LookupResult, lookup_word
from zhtw.matcher import Matcher


@pytest.fixture
def matcher():
    """載入完整詞庫的 Matcher。"""
    return Matcher(load_dictionary())


@pytest.fixture
def char_table():
    """載入字元轉換表。"""
    return get_translate_table()


class TestLookupWordTermLayer:
    """詞彙層歸因測試。"""

    def test_term_match(self, matcher, char_table):
        """结合 應由詞彙層處理。"""
        result = lookup_word("结合", matcher, char_table)
        assert result.changed is True
        assert result.output == "結合"
        assert len(result.details) == 1
        d = result.details[0]
        assert d.source == "结合"
        assert d.target == "結合"
        assert d.layer == "term"
        assert d.position == 0
```

- [ ] **Step 2: 執行測試確認失敗**

Run: `uv run pytest tests/test_lookup.py::TestLookupWordTermLayer::test_term_match -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'zhtw.lookup'`

- [ ] **Step 3: 實作 lookup.py — 資料模型 + lookup_word（僅詞彙層）**

```python
# src/zhtw/lookup.py
"""
Lookup module for querying conversion results with layer attribution.

Provides word/sentence lookup with detail on which conversion layer
(term dictionary vs character map) is responsible for each change.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

from .matcher import Match, Matcher


@dataclass
class ConversionDetail:
    """單一轉換點的資訊。"""

    source: str
    target: str
    layer: str  # "term" | "char"
    position: int
    term_key: Optional[str] = None


@dataclass
class LookupResult:
    """一個查詢詞/句的完整結果。"""

    input: str
    output: str
    details: List[ConversionDetail] = field(default_factory=list)
    changed: bool = False


def lookup_word(
    word: str,
    matcher: Matcher,
    char_table: Optional[dict[int, str]] = None,
) -> LookupResult:
    """查詢單一詞/句的轉換結果與來源歸因。"""
    if not word:
        return LookupResult(input="", output="", details=[], changed=False)

    details: List[ConversionDetail] = []
    covered: set[int] = set()

    # 1. 詞彙層：Aho-Corasick 匹配
    for match in matcher.find_matches(word):
        details.append(
            ConversionDetail(
                source=match.source,
                target=match.target,
                layer="term",
                position=match.start,
                term_key=match.source,
            )
        )
        covered.update(range(match.start, match.end))

    # 2. 字元層：逐字掃描未被詞彙層覆蓋的位置
    if char_table:
        for i, ch in enumerate(word):
            if i not in covered:
                cp = ord(ch)
                if cp in char_table and char_table[cp] != ch:
                    details.append(
                        ConversionDetail(
                            source=ch,
                            target=char_table[cp],
                            layer="char",
                            position=i,
                        )
                    )

    # 按位置排序
    details.sort(key=lambda d: d.position)

    # 產生轉換後文字
    output = _build_output(word, details)
    changed = output != word

    return LookupResult(input=word, output=output, details=details, changed=changed)


def _build_output(text: str, details: List[ConversionDetail]) -> str:
    """根據 details 組合轉換後文字。"""
    if not details:
        return text

    parts: list[str] = []
    last_end = 0

    for d in details:
        parts.append(text[last_end : d.position])
        parts.append(d.target)
        last_end = d.position + len(d.source)

    parts.append(text[last_end:])
    return "".join(parts)


def lookup_words(
    words: List[str],
    matcher: Matcher,
    char_table: Optional[dict[int, str]] = None,
) -> List[LookupResult]:
    """批次查詢多個詞/句。"""
    return [lookup_word(w, matcher, char_table) for w in words]
```

- [ ] **Step 4: 執行測試確認通過**

Run: `uv run pytest tests/test_lookup.py::TestLookupWordTermLayer::test_term_match -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/zhtw/lookup.py tests/test_lookup.py
git commit -m "feat: 新增 lookup 模組 — 資料模型 + 詞彙層歸因"
```

---

### Task 2: lookup 核心模組 — 字元層歸因 + 混合場景

**Files:**
- Modify: `tests/test_lookup.py`
- (lookup.py 已在 Task 1 實作完成，此 Task 只加測試驗證)

- [ ] **Step 1: 新增字元層、混合、無變化、空字串測試**

在 `tests/test_lookup.py` 末尾新增：

```python
class TestLookupWordCharLayer:
    """字元層歸因測試。"""

    def test_char_only(self, matcher, char_table):
        """盐 應由字元層處理。"""
        result = lookup_word("盐", matcher, char_table)
        assert result.changed is True
        assert result.output == "鹽"
        assert len(result.details) == 1
        d = result.details[0]
        assert d.source == "盐"
        assert d.target == "鹽"
        assert d.layer == "char"
        assert d.position == 0

    def test_multi_char(self, matcher, char_table):
        """摄入：摄 由字元層轉，入 繁簡同形不出現。"""
        result = lookup_word("摄入", matcher, char_table)
        assert result.changed is True
        assert result.output == "攝入"
        assert len(result.details) == 1
        assert result.details[0].source == "摄"
        assert result.details[0].layer == "char"

    def test_心态(self, matcher, char_table):
        """心态：心 同形不轉，态 由字元層轉。"""
        result = lookup_word("心态", matcher, char_table)
        assert result.changed is True
        assert result.output == "心態"
        assert len(result.details) == 1
        assert result.details[0].source == "态"
        assert result.details[0].layer == "char"


class TestLookupWordMixed:
    """混合層歸因測試。"""

    def test_mixed_layers(self, matcher, char_table):
        """营养：营 可能由字元層，养 由字元層，但若整詞在詞庫則為詞彙層。"""
        result = lookup_word("营养", matcher, char_table)
        assert result.changed is True
        assert result.output == "營養"
        # 不管哪層處理，結果要正確且歸因不重疊
        positions = [d.position for d in result.details]
        assert len(positions) == len(set(positions))

    def test_sentence(self, matcher, char_table):
        """整句：多個轉換點，位置排序正確。"""
        result = lookup_word("摄入量过高会影响心态", matcher, char_table)
        assert result.changed is True
        assert result.output == "攝入量過高會影響心態"
        # 位置應遞增
        positions = [d.position for d in result.details]
        assert positions == sorted(positions)
        # 歸因不重疊
        assert len(positions) == len(set(positions))


class TestLookupWordEdgeCases:
    """邊界條件測試。"""

    def test_no_change(self, matcher, char_table):
        """繁體字不需轉換。"""
        result = lookup_word("台灣", matcher, char_table)
        assert result.changed is False
        assert result.output == "台灣"
        assert result.details == []

    def test_empty_string(self, matcher, char_table):
        """空字串不炸。"""
        result = lookup_word("", matcher, char_table)
        assert result.changed is False
        assert result.output == ""
        assert result.details == []

    def test_no_char_table(self, matcher):
        """不傳 char_table 時只做詞彙層。"""
        result = lookup_word("盐", matcher)
        # 盐 不在詞庫（只有複合詞），所以不會轉換
        assert result.changed is False
```

- [ ] **Step 2: 執行所有 lookup 測試確認通過**

Run: `uv run pytest tests/test_lookup.py -v`
Expected: ALL PASS

- [ ] **Step 3: Commit**

```bash
git add tests/test_lookup.py
git commit -m "test: lookup 模組完整單元測試 — 字元層、混合、邊界條件"
```

---

### Task 3: lookup_words 批次查詢測試

**Files:**
- Modify: `tests/test_lookup.py`

- [ ] **Step 1: 新增 lookup_words 測試**

在 `tests/test_lookup.py` 末尾新增：

```python
from zhtw.lookup import lookup_words


class TestLookupWords:
    """批次查詢測試。"""

    def test_multiple_words(self, matcher, char_table):
        """多詞批次查詢。"""
        results = lookup_words(["摄入", "盐", "结合", "心态", "营养"], matcher, char_table)
        assert len(results) == 5
        assert all(r.changed for r in results)
        assert results[0].output == "攝入"
        assert results[1].output == "鹽"
        assert results[2].output == "結合"
        assert results[3].output == "心態"
        assert results[4].output == "營養"

    def test_empty_list(self, matcher, char_table):
        """空列表回傳空列表。"""
        results = lookup_words([], matcher, char_table)
        assert results == []
```

- [ ] **Step 2: 執行測試確認通過**

Run: `uv run pytest tests/test_lookup.py::TestLookupWords -v`
Expected: ALL PASS

- [ ] **Step 3: Commit**

```bash
git add tests/test_lookup.py
git commit -m "test: lookup_words 批次查詢測試"
```

---

### Task 4: __init__.py 匯出

**Files:**
- Modify: `src/zhtw/__init__.py`

- [ ] **Step 1: 更新 __init__.py**

在 `src/zhtw/__init__.py` 加入 lookup 的公開 API：

```python
from .lookup import ConversionDetail, LookupResult, lookup_word, lookup_words
```

並在 `__all__` 中加入：

```python
__all__ = [
    "__version__",
    "convert_file",
    "convert_text",
    "load_dictionary",
    "Matcher",
    "ConversionDetail",
    "LookupResult",
    "lookup_word",
    "lookup_words",
]
```

- [ ] **Step 2: 驗證 import 正常**

Run: `uv run python -c "from zhtw import lookup_word, LookupResult; print('OK')"`
Expected: `OK`

- [ ] **Step 3: 執行全部現有測試確認無 regression**

Run: `uv run pytest tests/ -x -q`
Expected: ALL PASS

- [ ] **Step 4: Commit**

```bash
git add src/zhtw/__init__.py
git commit -m "feat: 匯出 lookup 公開 API"
```

---

### Task 5: CLI lookup 指令 — 基本多詞模式

**Files:**
- Modify: `src/zhtw/cli.py`
- Modify: `tests/test_lookup.py`

- [ ] **Step 1: 寫 CLI 多詞模式的 failing test**

在 `tests/test_lookup.py` 末尾新增：

```python
from click.testing import CliRunner
from zhtw.cli import main


@pytest.fixture
def runner():
    return CliRunner()


class TestLookupCLI:
    """CLI 整合測試。"""

    def test_multiple_args(self, runner):
        """多個參數模式。"""
        result = runner.invoke(main, ["lookup", "摄入", "盐", "结合"])
        assert result.exit_code == 0
        assert "攝入" in result.output
        assert "鹽" in result.output
        assert "結合" in result.output

    def test_no_change(self, runner):
        """無需轉換時顯示提示。"""
        result = runner.invoke(main, ["lookup", "台灣"])
        assert result.exit_code == 0
        assert "無需轉換" in result.output
```

- [ ] **Step 2: 執行測試確認失敗**

Run: `uv run pytest tests/test_lookup.py::TestLookupCLI::test_multiple_args -v`
Expected: FAIL — `No such command 'lookup'`

- [ ] **Step 3: 在 cli.py 實作 lookup command**

在 `cli.py` 的 `validate` command 之前（約 `@main.command()` 區塊），新增：

```python
@main.command()
@click.argument("words", nargs=-1)
@click.option("--verbose", "-v", is_flag=True, help="詳細模式（樹狀逐項列表）")
@click.option("--json", "json_output", is_flag=True, help="JSON 輸出")
@click.option(
    "--source",
    "-s",
    type=str,
    default="cn,hk",
    help="詞庫來源: cn (簡體), hk (港式), 或 cn,hk (預設)",
)
def lookup(words: tuple, verbose: bool, json_output: bool, source: str):
    """
    查詢詞彙的轉換結果與來源歸因。

    支援三種輸入方式：

    \b
      zhtw lookup 摄入 盐 结合        # 多個單詞
      echo "摄入" | zhtw lookup       # stdin 管線
      zhtw lookup "摄入量过高会影响心态"  # 整句
    """
    import sys as _sys

    from .charconv import get_translate_table
    from .lookup import lookup_word, lookup_words

    # 載入詞庫
    sources = [s.strip() for s in source.split(",")]
    terms = load_dictionary(sources=sources)
    from .matcher import Matcher

    matcher = Matcher(terms)

    # 字元轉換表（僅 cn 來源）
    char_table = get_translate_table() if "cn" in sources else None

    # 收集輸入
    input_words: list[str] = []
    if words:
        input_words = list(words)
    elif not _sys.stdin.isatty():
        for line in _sys.stdin:
            stripped = line.strip()
            if stripped:
                input_words.append(stripped)

    if not input_words:
        click.echo("用法: zhtw lookup <詞彙>...", err=True)
        raise SystemExit(1)

    # 判斷整句 vs 多個單詞
    is_sentence = len(input_words) == 1 and len(input_words[0]) >= 4

    # 執行查詢
    results = lookup_words(input_words, matcher, char_table)

    # 輸出
    if json_output:
        _print_lookup_json(results)
    elif is_sentence:
        _print_lookup_sentence(results[0], verbose)
    else:
        _print_lookup_words(results, verbose)


def _print_lookup_json(results):
    """JSON 格式輸出。"""
    data = {
        "results": [
            {
                "input": r.input,
                "output": r.output,
                "changed": r.changed,
                "details": [
                    {
                        "source": d.source,
                        "target": d.target,
                        "layer": d.layer,
                        "position": d.position,
                    }
                    for d in r.details
                ],
            }
            for r in results
        ]
    }
    click.echo(json.dumps(data, ensure_ascii=False, indent=2))


def _print_lookup_words(results, verbose: bool):
    """多個單詞的輸出格式。"""
    for r in results:
        if not r.changed:
            click.echo(f"{r.input} {click.style('✓ 無需轉換', fg='green')}")
            continue

        if verbose:
            click.echo(f"{r.input} → {click.style(r.output, fg='cyan')}")
            for i, d in enumerate(r.details):
                layer_label = "詞彙層" if d.layer == "term" else "字元層"
                prefix = "└──" if i == len(r.details) - 1 else "├──"
                click.echo(f"  {prefix} {d.source} → {d.target}  ({layer_label})")
        else:
            # 簡潔模式：列出轉換來源
            layer_parts = []
            for d in r.details:
                layer_label = "詞彙層" if d.layer == "term" else "字元層"
                layer_parts.append(f"{d.source}→{d.target}")

            # 歸類：如果全部同層就只寫一次層名
            layers = {d.layer for d in r.details}
            if len(layers) == 1:
                layer_name = "詞彙層" if "term" in layers else "字元層"
                detail_str = f"({layer_name}: {', '.join(layer_parts)})"
            else:
                parts_with_layer = []
                for d in r.details:
                    tag = "詞" if d.layer == "term" else "字"
                    parts_with_layer.append(f"{d.source}→{d.target}[{tag}]")
                detail_str = f"({', '.join(parts_with_layer)})"

            click.echo(
                f"{r.input} → {click.style(r.output, fg='cyan')}  {detail_str}"
            )


def _print_lookup_sentence(result, verbose: bool):
    """整句的輸出格式。"""
    if not result.changed:
        click.echo(f"{result.input} {click.style('✓ 無需轉換', fg='green')}")
        return

    click.echo(result.input)
    click.echo(f"→ {click.style(result.output, fg='cyan')}")
    click.echo()

    if verbose:
        for i, d in enumerate(result.details):
            layer_label = "詞彙層" if d.layer == "term" else "字元層"
            prefix = "└──" if i == len(result.details) - 1 else "├──"
            click.echo(f"{prefix} {d.source} → {d.target}  ({layer_label})")
    else:
        parts = [f"{d.source}→{d.target}" for d in result.details]
        click.echo(f"轉換明細 ({len(result.details)} 處):")
        click.echo(f"  {' '.join(parts)}")
```

- [ ] **Step 4: 執行 CLI 測試確認通過**

Run: `uv run pytest tests/test_lookup.py::TestLookupCLI -v`
Expected: ALL PASS

- [ ] **Step 5: Commit**

```bash
git add src/zhtw/cli.py tests/test_lookup.py
git commit -m "feat: 新增 zhtw lookup CLI 指令 — 多詞 + 整句模式"
```

---

### Task 6: CLI lookup — stdin、--verbose、--json 測試

**Files:**
- Modify: `tests/test_lookup.py`

- [ ] **Step 1: 新增 stdin、verbose、json 測試**

在 `tests/test_lookup.py` 的 `TestLookupCLI` class 末尾新增：

```python
    def test_stdin_pipe(self, runner):
        """stdin 管線模式。"""
        result = runner.invoke(main, ["lookup"], input="摄入\n盐\n")
        assert result.exit_code == 0
        assert "攝入" in result.output
        assert "鹽" in result.output

    def test_sentence_mode(self, runner):
        """整句模式（單一參數 >= 4 字元）。"""
        result = runner.invoke(main, ["lookup", "摄入量过高"])
        assert result.exit_code == 0
        assert "→" in result.output
        assert "轉換明細" in result.output

    def test_verbose_mode(self, runner):
        """--verbose 模式顯示樹狀結構。"""
        result = runner.invoke(main, ["lookup", "-v", "摄入量过高"])
        assert result.exit_code == 0
        assert "├──" in result.output or "└──" in result.output
        assert "字元層" in result.output or "詞彙層" in result.output

    def test_json_output(self, runner):
        """--json 輸出可被解析。"""
        result = runner.invoke(main, ["lookup", "--json", "摄入", "盐"])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert "results" in data
        assert len(data["results"]) == 2
        assert data["results"][0]["output"] == "攝入"
        assert data["results"][0]["changed"] is True
        assert len(data["results"][0]["details"]) > 0

    def test_no_input(self, runner):
        """無輸入時報錯。"""
        result = runner.invoke(main, ["lookup"])
        assert result.exit_code == 1
```

- [ ] **Step 2: 執行測試確認通過**

Run: `uv run pytest tests/test_lookup.py::TestLookupCLI -v`
Expected: ALL PASS

- [ ] **Step 3: Commit**

```bash
git add tests/test_lookup.py
git commit -m "test: lookup CLI 完整整合測試 — stdin、verbose、json"
```

---

### Task 7: 全套回歸測試 + import 新增

**Files:**
- Modify: `tests/test_lookup.py` (新增 json import)

- [ ] **Step 1: 確認 test_lookup.py 頂部有 json import**

確認 `tests/test_lookup.py` 檔案頂部包含：

```python
import json
```

（Task 6 的 `test_json_output` 需要用到，若漏了要補上）

- [ ] **Step 2: 執行完整測試套件確認無 regression**

Run: `uv run pytest tests/ -x -q`
Expected: ALL PASS，無新的失敗

- [ ] **Step 3: 手動煙霧測試**

Run:
```bash
uv run zhtw lookup 摄入 盐 结合 心态 营养
uv run zhtw lookup -v "摄入量过高会影响心态"
uv run zhtw lookup --json 结合
echo "营养\n心态" | uv run zhtw lookup
```

驗證輸出格式符合設計 spec。

- [ ] **Step 4: Commit（若有修正）**

```bash
git add -A
git commit -m "chore: lookup 功能收尾 — 全套回歸測試通過"
```
