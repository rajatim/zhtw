# zhtw 下一階段精準度計畫 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把目前「看不見」的詞彙在地化正確率變成可量測的數字,並建立把真實錯轉變成 regression 的最短回饋路徑——而不是盲目把 corpus 從 500 加到 1000。

**Architecture:** 新增一條 **report-only** 的 held-out 量測線,與既有 release gate 完全分離。Gate(golden battery + curated corpus)維持 100% 鎖回歸;held-out eval 允許 < 100%,它的失敗案例就是 discovery 候選。再加一個 `zhtw report` 命令,把使用者回報一鍵變成 corpus 格式的 regression stub。純邏輯放可匯入的 `src/zhtw/` 模組(TDD),簡體輸入資料放 `zhtw-test-corpus` repo。

**Tech Stack:** Python 3、`click`(CLI)、`pytest`(測試)、`uv`(執行)、既有 `zhtw.converter.convert` 與 `zhtw.charconv.get_translate_table`。

## 為什麼是這個計畫(給沒有前情的工程師)

zhtw 已在 1 億 3500 萬字真實簡體書籍上稽核過:**殘留簡體 0、過度轉換 3(已修)**。代表「字形完整度」與「過度轉換率」幾乎已解決。唯一還沒被規模化量測的,是「詞彙在地化正確率」(例:`軟體`→`軟體`、HK 形 `軟體`→`軟體` 有沒有正確做)。curated corpus 是 100%-passing 的 gate,**設計上只裝得下我們已經轉對的句子**,所以它無法發現新缺陷;把它從 500 養到 1000 主要是擴大回歸面積,邊際效益遞減。因此本計畫不追 corpus 數字,而是補上量測 + 回饋這兩塊缺口。完整論證見 `docs/precision-standard.md` 與本 repo 對話紀錄。

## Global Constraints

- 黃金規則「寧可少轉,不要錯轉」優先於任何轉換率數字;不得為提高轉換率犧牲它。
- held-out eval **永遠是 report-only**,絕不可成為 release gate 或 CI 失敗條件(它允許 < 100%)。
- 簡體中文輸入資料**只能**放在 `zhtw-test-corpus` repo(clone 至 `tests/data/corpus/`);本 repo 的 pre-commit hook 會轉換簡體,放本 repo 會被汙染。
- 任何含簡體字面量的 Python 檔案,首行加 `# zhtw:disable`(對照 `tests/test_cli.py`、`tests/test_golden_rule_battery.py`)。
- 不得為了讓測試/eval 通過而修改 expected;若 expected 本身錯了,修 expected 並說明理由。
- 任何詞庫/轉換邏輯變動,仍須通過既有 release gate:`uv run zhtw validate`、`uv run python scripts/audit_idempotency.py --sources cn,hk --curated-only --fail-on-issues`、`uv run pytest tests/test_golden_rule_battery.py tests/test_corpus.py -q`。
- 若動到版本號或 `sdk/data/`,須遵守 mono-versioning(`make bump` + `make version-check`,見 CLAUDE.md 黃金規則 6)。
- 本計畫**不改動** `convert()` 的轉換行為,只新增量測與回報工具。

---

## ⚠️ 修訂 v2(2026-06-29，依 Phase 0 spike 結果)

**Phase 0 人工 spike 已執行**（30 句 Book held-out、獨立 agent 盲標、人工逐筆裁決並對照詞庫驗證）。結論改變了下方 Phase 1 的做法：

- **訊號確認存在**：句級 26/30 相符；4 筆真瑕疵跨三維度——`临时→暫時` 過度轉換 bug、`卧` 殘留簡體、`超声波/质量` 漏在地化。前 3 個已於 commit `d344352` 修復並鎖回歸（golden 247→255 句）。
- **決定：不建下方 Phase 1 的重型 harness（Task 1–6 的 `classify_result`/`EvalReport`/自動分桶）。** 理由：spike 證明價值全在「抽樣 → 盲標 → 人工裁決」這條人工流程；最貴且無法自動化的正是盲標 + 裁決；而自動分桶正是 review 抓到有 bug 的部分（`MISSED` 桶對真實句幾乎永遠空、`DIVERGENT` 變垃圾桶），人工裁決表現更好。
- **取而代之（已落地）**：輕量、可重複的兩支腳本 + 人工流程：
  - `scripts/spike_sample.py` — 抽 N 句 → 輸出待盲標 JSON
  - 人工 / 獨立 agent 盲標 expected（**不可看轉換器輸出**）
  - `scripts/spike_eval.py` — 跑 convert 比對 → 印 diff 表 + raw match rate（**不自動分桶**，人工裁決）
- **`zhtw report` 維持延後**：spike 印證「維護者主動 discovery」才是抓 bug 來源，非使用者回報。
- **不變**：strict 預設、三套語料分離（gate / discovery / frozen eval）、Phase 2/3 方向、所有 Global Constraints。

> 下方「## File Structure(Phase 1)」與 Task 1–6 **已 SUPERSEDED**，僅保留作為決策記錄，請勿執行。Phase 2/3 outline 仍有效，應於累積數輪 spike 後另開 plan。
> **下一步（需 Tim）**：擴大 spike——再抽 50–100 句由台灣母語者親自盲標，把 ~13% 這個指示性數字確認得更準。

---

## 階段總覽(完整 roadmap)

| 階段 | 內容 | 本文件詳細度 | 完成判準 |
|------|------|--------------|----------|
| **Phase 1(短期,本計畫詳列)** | A. held-out 在地化 eval(report-only)；B. `zhtw report` 回報命令 | ✅ 逐步 TDD(Task 1–6) | eval 能對 ≥50 筆 held-out 算出 C 維度數字並產報告;`zhtw report` 能一鍵產生 regression stub;既有 gate 全綠 |
| **Phase 2(中期,gated outline)** | 用 eval 對 2–3 個新領域(法律/醫療/CLI)做 discovery sweep;設計 transcode vs localize 模式分離 | 🔲 觸發條件 + 判準(下方) | 每個確認錯轉 → 一個 regression;script-safe 模式在 1 億字稽核上過度轉換 = 0 |
| **Phase 3(長期,gated outline)** | held-out eval 擴到可信規模,成為對外宣稱品質的官方數字;每次 release 附「四件套」揭露 | 🔲 觸發條件 + 判準(下方) | release notes 附 corpus 版本 + case 數 + held-out 分數 + gate 結果 |

> Phase 2/3 刻意**不**寫成 TDD 步驟:它們的具體任務取決於 Phase 1 量出來的數字(哪個領域漏轉最多就先做哪個)。現在寫死步驟會變成臆測,違反「No Placeholders」。各自應在 Phase 1 完成後另開 plan。

---

## File Structure(Phase 1)

新增 / 修改的檔案與職責:

- **Create `src/zhtw/holdout_eval.py`** — held-out 量測純邏輯:`EvalCase`/`EvalReport` 資料結構、`classify_result()`(把單一結果分桶)、`score_cases()`(聚合)、`load_holdout_cases()`(讀資料)、`render_report()`(產 markdown)、`main()`(`python -m` 入口,report-only)。
- **Create `tests/test_holdout_eval.py`** — 上述純函式的單元測試(用合成 fixture,不依賴真實 corpus)。
- **Create `src/zhtw/report.py`** — `build_regression_stub()`(產 corpus 格式 case)、`github_issue_url()`(產預填 issue 連結)。
- **Create `tests/test_report.py`** — `report.py` 單元測試。
- **Modify `src/zhtw/cli.py`** — 新增 `@main.command() report`(在現有 commands 之後、`main.add_command(_export, ...)` 之前)。
- **Modify `tests/test_cli.py`** — 新增 `report` 命令的 CliRunner 整合測試。
- **Modify `Makefile`** — 新增 `eval-holdout` target。
- **Create(在 `zhtw-test-corpus` repo)`holdout/*.json`** — 人工標註的 held-out 資料(Task 7,人工步驟)。
- **產出(自動生成,不進版控)`docs/reports/holdout-eval-<date>.md`** — eval 報告。

---

### Task 1: held-out 結果分桶器 `classify_result`

把單一 (input, expected, actual) 結果分到四桶之一,讓報告能把 A/B/C 維度分開呈現。

**Files:**
- Create: `src/zhtw/holdout_eval.py`
- Test: `tests/test_holdout_eval.py`

**Interfaces:**
- Produces: 常數 `PASS="pass"`、`RESIDUAL="residual_simplified"`、`MISSED="missed_conversion"`、`DIVERGENT="divergent"`;函式 `classify_result(src: str, expected: str, actual: str, convertible: frozenset[int]) -> str`。`convertible` 是「轉換器認得、能轉的簡體碼位集合」(Task 3 用 `frozenset(get_translate_table())` 注入)。

- [ ] **Step 1: 寫失敗測試**

`tests/test_holdout_eval.py`:

```python
# zhtw:disable  # 測試需要簡體字輸入

import json

from zhtw.holdout_eval import (
    DIVERGENT,
    MISSED,
    PASS,
    RESIDUAL,
    classify_result,
)

# 合成的「可轉換碼位」集合,不依賴真實字表
CONVERTIBLE = frozenset({ord("软"), ord("数"), ord("据"), ord("只"), ord("鸟")})


def test_classify_pass():
    assert classify_result("软件", "軟體", "軟體", CONVERTIBLE) == PASS


def test_classify_residual():
    # 輸出仍含 converter 認得的簡體字 → A 維度洩漏
    assert classify_result("数据", "資料", "数据", CONVERTIBLE) == RESIDUAL


def test_classify_missed_hk_form():
    # 輸入全為繁體(HK 形),converter 原樣輸出,但期望要在地化 → C recall 缺口
    assert classify_result("軟件", "軟體", "軟件", CONVERTIBLE) == MISSED


def test_classify_divergent():
    # converter 有改但改錯(過度轉換 / 錯誤在地化) → 需人工分辨
    assert classify_result("一只鸟", "一隻鳥", "一支鳥", CONVERTIBLE) == DIVERGENT
```

- [ ] **Step 2: 跑測試確認失敗**

Run: `uv run pytest tests/test_holdout_eval.py -q`
Expected: FAIL，`ModuleNotFoundError: No module named 'zhtw.holdout_eval'`

- [ ] **Step 3: 寫最小實作**

`src/zhtw/holdout_eval.py`:

```python
"""Held-out 在地化精準度量測（report-only，絕不作為 release gate）。"""

from __future__ import annotations

PASS = "pass"
RESIDUAL = "residual_simplified"
MISSED = "missed_conversion"
DIVERGENT = "divergent"


def classify_result(
    src: str,
    expected: str,
    actual: str,
    convertible: frozenset[int],
) -> str:
    """把單一轉換結果分桶。

    Args:
        src: 原始輸入。
        expected: 人工標註的正確台灣繁體。
        actual: convert(src) 的實際輸出。
        convertible: 轉換器認得、能轉的碼位集合（簡體碼位）。
    """
    if actual == expected:
        return PASS
    # A 維度:輸出仍含可轉換的簡體字 → 漏掉字形轉換
    if any(ord(c) in convertible for c in actual):
        return RESIDUAL
    # C recall:converter 幾乎沒動輸入,但期望要改 → 漏在地化
    if actual == src:
        return MISSED
    # B + C precision:有改但與期望不符 → 過度轉換或錯誤在地化
    return DIVERGENT
```

- [ ] **Step 4: 跑測試確認通過**

Run: `uv run pytest tests/test_holdout_eval.py -q`
Expected: PASS（4 passed）

- [ ] **Step 5: Commit**

```bash
git add src/zhtw/holdout_eval.py tests/test_holdout_eval.py
git commit -m "feat: 新增 held-out 結果分桶器 classify_result"
```

---

### Task 2: 聚合計分器 `score_cases` 與 `EvalReport`

把一批 case 跑過 converter、分桶、算出通過率與各桶清單。

**Files:**
- Modify: `src/zhtw/holdout_eval.py`
- Test: `tests/test_holdout_eval.py`

**Interfaces:**
- Consumes: `classify_result`、桶常數(Task 1)。
- Produces:
  - `@dataclass(frozen=True) class EvalCase` 欄位 `id: str`、`src: str`、`expected: str`。
  - `@dataclass class EvalReport` 欄位 `total: int`、`passed: int`、`by_bucket: dict[str, list[dict]]`;property `pass_rate -> float`。
  - `score_cases(cases: list[EvalCase], convert_fn: Callable[[str], str], convertible: frozenset[int]) -> EvalReport`。失敗 case 在 `by_bucket[bucket]` 存 `{"id","input","expected","actual"}`。

- [ ] **Step 1: 寫失敗測試**(附加到 `tests/test_holdout_eval.py`)

```python
from zhtw.holdout_eval import EvalCase, EvalReport, score_cases  # noqa: E402


def test_score_cases_aggregates():
    cases = [
        EvalCase("c1", "软件", "軟體"),  # fake_convert → 軟體 → pass
        EvalCase("c2", "数据", "資料"),  # fake_convert → 数据 → residual
    ]

    def fake_convert(s: str) -> str:
        return {"软件": "軟體", "数据": "数据"}[s]

    report = score_cases(cases, fake_convert, CONVERTIBLE)
    assert report.total == 2
    assert report.passed == 1
    assert report.pass_rate == 0.5
    assert len(report.by_bucket[RESIDUAL]) == 1
    assert report.by_bucket[RESIDUAL][0]["id"] == "c2"
    assert report.by_bucket[RESIDUAL][0]["actual"] == "数据"
```

- [ ] **Step 2: 跑測試確認失敗**

Run: `uv run pytest tests/test_holdout_eval.py::test_score_cases_aggregates -q`
Expected: FAIL，`ImportError: cannot import name 'EvalCase'`

- [ ] **Step 3: 寫最小實作**(附加到 `src/zhtw/holdout_eval.py`,在桶常數下方加 import 與類別)

檔案頂部 import 區改為:

```python
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable
```

在 `classify_result` 之後新增:

```python
@dataclass(frozen=True)
class EvalCase:
    id: str
    src: str
    expected: str


@dataclass
class EvalReport:
    total: int
    passed: int
    by_bucket: dict[str, list[dict]]

    @property
    def pass_rate(self) -> float:
        return self.passed / self.total if self.total else 1.0


def score_cases(
    cases: list[EvalCase],
    convert_fn: Callable[[str], str],
    convertible: frozenset[int],
) -> EvalReport:
    by_bucket: dict[str, list[dict]] = {RESIDUAL: [], MISSED: [], DIVERGENT: []}
    passed = 0
    for case in cases:
        actual = convert_fn(case.src)
        bucket = classify_result(case.src, case.expected, actual, convertible)
        if bucket == PASS:
            passed += 1
            continue
        by_bucket[bucket].append(
            {
                "id": case.id,
                "input": case.src,
                "expected": case.expected,
                "actual": actual,
            }
        )
    return EvalReport(total=len(cases), passed=passed, by_bucket=by_bucket)
```

- [ ] **Step 4: 跑測試確認通過**

Run: `uv run pytest tests/test_holdout_eval.py -q`
Expected: PASS（5 passed）

- [ ] **Step 5: Commit**

```bash
git add src/zhtw/holdout_eval.py tests/test_holdout_eval.py
git commit -m "feat: 新增 held-out 聚合計分器 score_cases"
```

---

### Task 3: 載入資料 `load_holdout_cases` 與報告 `render_report`

從 corpus repo 的 `holdout/` 讀資料(不存在則回空清單),把 `EvalReport` 渲染成 report-only markdown。

**Files:**
- Modify: `src/zhtw/holdout_eval.py`
- Test: `tests/test_holdout_eval.py`

**Interfaces:**
- Consumes: `EvalCase`、`EvalReport`、桶常數。
- Produces:
  - `load_holdout_cases(corpus_dir: Path) -> list[EvalCase]` — 讀 `corpus_dir/holdout/*.json`(格式同 curated corpus:`{"corpus":[{"id","input","expected"}]}`);目錄不存在回 `[]`。
  - `render_report(report: EvalReport, generated_at: str) -> str` — markdown,首段標明 report-only。

- [ ] **Step 1: 寫失敗測試**(附加到 `tests/test_holdout_eval.py`)

```python
from pathlib import Path  # noqa: E402

from zhtw.holdout_eval import load_holdout_cases, render_report  # noqa: E402


def test_load_holdout_cases(tmp_path: Path):
    holdout = tmp_path / "holdout"
    holdout.mkdir()
    (holdout / "a.json").write_text(
        json.dumps(
            {"corpus": [{"id": "h1", "input": "软件", "expected": "軟體"}]},
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    cases = load_holdout_cases(tmp_path)
    assert len(cases) == 1
    assert cases[0].id == "h1"
    assert cases[0].src == "软件"


def test_load_holdout_cases_absent(tmp_path: Path):
    assert load_holdout_cases(tmp_path) == []


def test_render_report_marks_report_only():
    report = EvalReport(
        total=1,
        passed=0,
        by_bucket={
            RESIDUAL: [
                {"id": "h1", "input": "数据", "expected": "資料", "actual": "数据"}
            ],
            MISSED: [],
            DIVERGENT: [],
        },
    )
    md = render_report(report, "2026-06-28")
    assert "report-only" in md
    assert "数据" in md
```

- [ ] **Step 2: 跑測試確認失敗**

Run: `uv run pytest tests/test_holdout_eval.py -q`
Expected: FAIL，`ImportError: cannot import name 'load_holdout_cases'`

- [ ] **Step 3: 寫最小實作**(附加到 `src/zhtw/holdout_eval.py`;頂部 import 補 `import json` 與 `from pathlib import Path`)

```python
def load_holdout_cases(corpus_dir: Path) -> list[EvalCase]:
    """讀 corpus_dir/holdout/*.json；目錄不存在回空清單（如同 test_corpus 的 skip）。"""
    holdout = corpus_dir / "holdout"
    if not holdout.exists():
        return []
    cases: list[EvalCase] = []
    for path in sorted(holdout.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        for c in data.get("corpus", []):
            cases.append(
                EvalCase(id=c.get("id", path.stem), src=c["input"], expected=c["expected"])
            )
    return cases


def render_report(report: EvalReport, generated_at: str) -> str:
    lines = [
        "# Held-out 在地化精準度報告（report-only）",
        "",
        "<!-- zhtw:disable -->",
        "",
        f"生成日期：{generated_at}",
        "",
        "> 此為 held-out 量測，**不是 release gate**，允許 < 100%。",
        "> 失敗案例即 discovery 候選，逐一人工確認後補進 golden battery 或 curated corpus。",
        "",
        "| 指標 | 數值 |",
        "|------|------|",
        f"| 樣本數 | {report.total} |",
        f"| 通過 | {report.passed} |",
        f"| 通過率 | {report.pass_rate:.1%} |",
        f"| 殘留簡體（A 維度） | {len(report.by_bucket[RESIDUAL])} |",
        f"| 漏轉（C recall） | {len(report.by_bucket[MISSED])} |",
        f"| 分歧（B + C precision） | {len(report.by_bucket[DIVERGENT])} |",
        "",
    ]
    sections = [
        (RESIDUAL, "殘留簡體（最高優先，A 維度洩漏，應為 0）"),
        (MISSED, "漏轉（C 維度 recall 缺口）"),
        (DIVERGENT, "分歧（需人工分辨：過度轉換 vs 錯誤在地化）"),
    ]
    for bucket, title in sections:
        rows = report.by_bucket[bucket]
        if not rows:
            continue
        lines.append(f"## {title}（{len(rows)}）")
        lines.append("")
        lines.append("| id | input | expected | actual |")
        lines.append("|----|-------|----------|--------|")
        for r in rows:
            lines.append(f"| {r['id']} | {r['input']} | {r['expected']} | {r['actual']} |")
        lines.append("")
    return "\n".join(lines)
```

- [ ] **Step 4: 跑測試確認通過**

Run: `uv run pytest tests/test_holdout_eval.py -q`
Expected: PASS（8 passed）

- [ ] **Step 5: Commit**

```bash
git add src/zhtw/holdout_eval.py tests/test_holdout_eval.py
git commit -m "feat: 新增 held-out 資料載入與報告渲染"
```

---

### Task 4: `main()` 入口 + `make eval-holdout`(report-only,永不 gate)

把所有零件接起來:讀真實字表 + 真實 `convert` + held-out 資料 → 產報告到 `docs/reports/` → 印摘要 → **永遠 exit 0**。

**Files:**
- Modify: `src/zhtw/holdout_eval.py`
- Modify: `Makefile`
- Test: `tests/test_holdout_eval.py`

**Interfaces:**
- Consumes: `load_holdout_cases`、`score_cases`、`render_report`;`zhtw.charconv.get_translate_table`、`zhtw.converter.convert`。
- Produces: `main() -> int`(永遠回 0);`python -m zhtw.holdout_eval` 可執行。

- [ ] **Step 1: 寫失敗測試**(附加到 `tests/test_holdout_eval.py`;驗證「即使有失敗案例也回 0」這個 report-only 不變式)

```python
from unittest.mock import patch  # noqa: E402

import zhtw.holdout_eval as he  # noqa: E402


def test_main_is_report_only_even_with_failures(tmp_path: Path, capsys, monkeypatch):
    # 準備一個一定會失敗的 held-out 資料
    corpus = tmp_path / "corpus"
    (corpus / "holdout").mkdir(parents=True)
    (corpus / "holdout" / "a.json").write_text(
        json.dumps(
            {"corpus": [{"id": "h1", "input": "数据", "expected": "資料"}]},
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    reports = tmp_path / "reports"

    monkeypatch.setattr(he, "_corpus_dir", lambda: corpus)
    monkeypatch.setattr(he, "_reports_dir", lambda: reports)
    # 強制 convert 留下殘留(模擬失敗),確認仍 exit 0
    monkeypatch.setattr(he, "_convert", lambda s: s)
    monkeypatch.setattr(he, "_convertible", lambda: frozenset({ord("数"), ord("据")}))

    rc = he.main()
    assert rc == 0  # report-only:有失敗也不能非 0
    assert (reports / "holdout-eval-").parent.exists()
    assert list(reports.glob("holdout-eval-*.md"))


def test_main_skips_when_no_data(tmp_path: Path, monkeypatch, capsys):
    monkeypatch.setattr(he, "_corpus_dir", lambda: tmp_path)  # 無 holdout/
    rc = he.main()
    assert rc == 0
    assert "略過" in capsys.readouterr().out
```

- [ ] **Step 2: 跑測試確認失敗**

Run: `uv run pytest tests/test_holdout_eval.py -k main -q`
Expected: FAIL，`AttributeError: module 'zhtw.holdout_eval' has no attribute 'main'`

- [ ] **Step 3: 寫最小實作**(附加到 `src/zhtw/holdout_eval.py` 末端;用小 helper 包裝外部相依,讓測試好 monkeypatch)

```python
def _corpus_dir() -> Path:
    return Path(__file__).resolve().parents[2] / "tests" / "data" / "corpus"


def _reports_dir() -> Path:
    return Path(__file__).resolve().parents[2] / "docs" / "reports"


def _convert(text: str) -> str:
    from zhtw.converter import convert

    return convert(text)


def _convertible() -> frozenset[int]:
    from zhtw.charconv import get_translate_table

    return frozenset(get_translate_table())


def _today() -> str:
    from datetime import datetime

    return datetime.now().strftime("%Y-%m-%d")


def main() -> int:
    cases = load_holdout_cases(_corpus_dir())
    if not cases:
        print(
            "[holdout-eval] 無 held-out 資料（tests/data/corpus/holdout/），略過。"
        )
        return 0
    report = score_cases(cases, _convert, _convertible())
    generated_at = _today()
    out_dir = _reports_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"holdout-eval-{generated_at}.md"
    out_path.write_text(render_report(report, generated_at), encoding="utf-8")
    print(
        f"[holdout-eval] {report.passed}/{report.total} "
        f"pass ({report.pass_rate:.1%}) → {out_path}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: 加 Makefile target**

在 `Makefile` 的 `test-python:` target 之前(或 help 區塊任一處)新增:

```makefile
eval-holdout: ## Held-out 精準度量測（report-only，永不 gate CI）
	uv run python -m zhtw.holdout_eval
```

- [ ] **Step 5: 跑測試 + 手動驗證**

Run: `uv run pytest tests/test_holdout_eval.py -q`
Expected: PASS（10 passed）

Run: `make eval-holdout`
Expected（此時 holdout/ 尚無資料）:印出 `[holdout-eval] 無 held-out 資料... 略過。`,exit code 0。

- [ ] **Step 6: Commit**

```bash
git add src/zhtw/holdout_eval.py tests/test_holdout_eval.py Makefile
git commit -m "feat: 新增 eval-holdout 入口（report-only）"
```

---

### Task 5: `zhtw report` 純邏輯 `build_regression_stub` / `github_issue_url`

把「一筆錯轉」變成可直接貼進 corpus 的 stub,以及一個預填好的 GitHub issue 連結。

**Files:**
- Create: `src/zhtw/report.py`
- Test: `tests/test_report.py`

**Interfaces:**
- Produces:
  - `build_regression_stub(src: str, expected: str, id_hint: str | None = None) -> dict` — 回 `{"id","input","expected","tags","notes"}`;`id` 用 sha1 前綴,**穩定可重現**(同輸入同 id)。
  - `github_issue_url(src: str, actual: str, expected: str, repo: str = "rajatim/zhtw") -> str` — URL-encode 的 issue 連結。

- [ ] **Step 1: 寫失敗測試**

`tests/test_report.py`:

```python
# zhtw:disable  # 測試需要簡體字輸入

from zhtw.report import build_regression_stub, github_issue_url


def test_build_regression_stub_shape():
    stub = build_regression_stub("软件", "軟體")
    assert stub["input"] == "软件"
    assert stub["expected"] == "軟體"
    assert stub["id"].startswith("report_")
    assert stub["tags"] == ["user-report"]


def test_build_regression_stub_stable_id():
    a = build_regression_stub("软件", "軟體")["id"]
    b = build_regression_stub("软件", "軟體")["id"]
    assert a == b  # 同輸入必須產生同 id（可重現）


def test_build_regression_stub_id_hint():
    assert build_regression_stub("软件", "軟體", id_hint="tech_999")["id"] == "tech_999"


def test_github_issue_url_encodes():
    url = github_issue_url("软件", "軟件", "軟體")
    assert url.startswith("https://github.com/rajatim/zhtw/issues/new?")
    assert "title=" in url
    assert "body=" in url
```

- [ ] **Step 2: 跑測試確認失敗**

Run: `uv run pytest tests/test_report.py -q`
Expected: FAIL，`ModuleNotFoundError: No module named 'zhtw.report'`

- [ ] **Step 3: 寫最小實作**

`src/zhtw/report.py`:

```python
"""把使用者回報的錯轉變成 regression stub 與預填的 issue 連結。"""

from __future__ import annotations

import hashlib
from urllib.parse import urlencode


def build_regression_stub(src: str, expected: str, id_hint: str | None = None) -> dict:
    """產生 corpus 格式的 regression case（可直接貼進 zhtw-test-corpus）。"""
    case_id = id_hint or "report_" + hashlib.sha1(src.encode("utf-8")).hexdigest()[:6]
    return {
        "id": case_id,
        "input": src,
        "expected": expected,
        "tags": ["user-report"],
        "notes": "",
    }


def github_issue_url(
    src: str,
    actual: str,
    expected: str,
    repo: str = "rajatim/zhtw",
) -> str:
    """產生預填標題與內文的 GitHub issue 連結。"""
    title = f"[mis-conversion] {src} → {actual}"
    body = (
        f"輸入：{src}\n"
        f"目前輸出：{actual}\n"
        f"期望輸出：{expected}\n\n"
        f"（由 `zhtw report` 產生）"
    )
    query = urlencode({"title": title, "body": body, "labels": "mis-conversion"})
    return f"https://github.com/{repo}/issues/new?{query}"
```

- [ ] **Step 4: 跑測試確認通過**

Run: `uv run pytest tests/test_report.py -q`
Expected: PASS（4 passed）

- [ ] **Step 5: Commit**

```bash
git add src/zhtw/report.py tests/test_report.py
git commit -m "feat: 新增 zhtw report 純邏輯（stub + issue 連結）"
```

---

### Task 6: 接上 `zhtw report` CLI 命令

讓使用者一行回報:`zhtw report "这个软件" --expected "這個軟體"`。

**Files:**
- Modify: `src/zhtw/cli.py`
- Test: `tests/test_cli.py`

**Interfaces:**
- Consumes: `build_regression_stub`、`github_issue_url`(Task 5);`zhtw.converter.convert`。
- Produces: click 命令 `report`,接受 `TEXT` 位置參數與必填 `--expected/-e`。

- [ ] **Step 1: 寫失敗測試**(附加到 `tests/test_cli.py`)

```python
def test_report_command(runner):
    result = runner.invoke(main, ["report", "这个软件", "--expected", "這個軟體"])
    assert result.exit_code == 0
    assert "這個軟體" in result.output  # expected 出現在 stub
    assert "issues/new" in result.output  # 有回報連結
```

- [ ] **Step 2: 跑測試確認失敗**

Run: `uv run pytest tests/test_cli.py::test_report_command -q`
Expected: FAIL（`Error: No such command 'report'.`,exit code 2）

- [ ] **Step 3: 寫最小實作**(在 `src/zhtw/cli.py` 中,`@main.command("validate-llm")` 區塊之後、`from .export_cmd import export as _export` 之前新增)

```python
@main.command()
@click.argument("text", type=str)
@click.option(
    "--expected",
    "-e",
    type=str,
    required=True,
    help="你認為正確的台灣繁體輸出",
)
def report(text: str, expected: str):
    """回報一個錯轉：印出 regression stub 與預填的 GitHub issue 連結。

    Example:

        zhtw report "这个软件" --expected "這個軟體"
    """
    from .converter import convert
    from .report import build_regression_stub, github_issue_url

    actual = convert(text)
    stub = build_regression_stub(text, expected)

    click.echo("📋 regression case（貼到 zhtw-test-corpus 的 regressions/）:")
    click.echo(json.dumps(stub, ensure_ascii=False, indent=2))
    click.echo(f"\n目前輸出: {actual}")
    click.echo(f"期望輸出: {expected}")
    if actual == expected:
        click.echo(click.style("\n✅ 目前輸出已等於期望，可能已修正", fg="green"))
    click.echo(f"\n🔗 回報連結:\n{github_issue_url(text, actual, expected)}")
```

- [ ] **Step 4: 跑測試確認通過**

Run: `uv run pytest tests/test_cli.py::test_report_command -q`
Expected: PASS

- [ ] **Step 5: 手動驗證 + Commit**

Run: `uv run zhtw report "这个软件" --expected "這個軟體"`
Expected:印出 JSON stub(`"input": "这个软件"`)、目前/期望輸出、issues/new 連結。

```bash
git add src/zhtw/cli.py tests/test_cli.py
git commit -m "feat: 新增 zhtw report 命令"
```

---

### Task 7: 種下 held-out 資料集(人工步驟,在 zhtw-test-corpus repo)

> ⚠️ 這是**人工標註**任務,不是 TDD。資料必須放 `zhtw-test-corpus` repo,不能放本 repo。

**Files:**
- Create(在 `zhtw-test-corpus` repo):`holdout/holdout-001.json`(格式同 curated corpus)。

- [ ] **Step 1: 從 Book 語料抽未用過的句子**

在 `tests/data/corpus/`(= zhtw-test-corpus clone)內:

```bash
uv run python scripts/sample_corpus.py --source Book/ --count 80
```

(或手動從 `Book/` 各書挑句子。)目標 50–100 句,涵蓋 curated 五類較少觸及的語境(對話、長句、領域混合)。

- [ ] **Step 2: 人工標註 expected**

對每句:先看 `uv run zhtw report "<句子>" --expected "<暫填>"` 的目前輸出,再由台灣母語者判斷正確的 expected。寫成:

```json
{
  "metadata": { "source": "Book corpus held-out", "license": "見來源", "collected_date": "2026-06-28",
                "description": "held-out 在地化量測,report-only,不是 gate" },
  "corpus": [
    { "id": "holdout_001", "input": "<簡體句>", "expected": "<人工確認台灣繁體>", "tags": [], "notes": "" }
  ]
}
```

- [ ] **Step 3: 放進 corpus repo 並 commit(在 corpus repo,不是 zhtw repo)**

```bash
# 於 tests/data/corpus/ (zhtw-test-corpus working copy)
mkdir -p holdout
# 存檔為 holdout/holdout-001.json
git add holdout/holdout-001.json
git commit -m "test: 新增 held-out 在地化量測資料（report-only）"
```

- [ ] **Step 4: 跑 eval,產出第一個 baseline 數字**

Run(於 zhtw repo):`make eval-holdout`
Expected:印出 `[holdout-eval] N/總數 pass (X%)`,並在 `docs/reports/holdout-eval-<date>.md` 生成報告。**X% 允許 < 100%**——這正是我們第一次看見 C 維度。

- [ ] **Step 5: 把報告裡的失敗案例,逐一走 discovery → 修復 → 鎖回歸**

對每個 `residual_simplified`(最高優先)與經人工確認的真錯轉:用 `zhtw report` 產 stub → 放進 corpus `regressions/` 或 golden battery → 修詞庫 → 確認既有 gate 全綠。**不要為了讓 held-out 變好看而改 expected。**

---

## Phase 2(gated outline,完成 Phase 1 後另開 plan)

**觸發條件:** Phase 1 的 held-out baseline 已存在,且 `docs/reports/holdout-eval-*.md` 顯示 `divergent`/`missed` 有實際內容(代表有可做的 C 維度工作)。

1. **領域 discovery sweep** —— 對法律/醫療/CLI 各補一批 held-out 資料,跑 eval,量「每百萬字新確認錯轉數」。
   - *驗證:* 每個確認錯轉 → 一個 regression case;corpus 因此**自然成長**(不設目標數字);某領域連續兩批 sweep 新確認錯轉趨近 0 → 宣告該領域覆蓋完成。
2. **transcode vs localize 模式分離** —— 新增「只做安全字形 + 高信心無歧義詞」的保守模式,給全自動 CI hook 用;完整在地化留給人工審閱情境。
   - *驗證:* 保守模式在 1 億字 Book 稽核上**過度轉換必須為 0**(比現行 default 更保守);各 SDK 行為一致,golden-test.json parity。

## Phase 3(gated outline)

**觸發條件:** held-out eval 樣本數達可信規模(如 ≥300 且涵蓋多領域),數字穩定。

1. **held-out 成為官方精準度數字** —— 對外宣稱品質時引用 held-out 分數,而非 corpus 案例數。
   - *驗證:* 每次 release notes 附「四件套」:corpus 版本 + case 數 + held-out 分數(含日期)+ gate 結果;不得出現沒有分母的百分比或「市場最佳」這類無法證明的字眼。
2. **標準文件更新** —— 把三維度(字形完整度 / 過度轉換率 / 在地化正確率)正式寫進 `docs/precision-standard.md`,held-out 列為 report-only 量測線。
   - *驗證:* `precision-standard.md` 的「成長目標」段落從「corpus 朝 750/1000」改為「held-out C 維度趨勢 + discovery 收斂」。

---

## Self-Review(作者自查,已執行)

**1. Spec 覆蓋** — handoff 六問與本計畫對應:下一步投資什麼(Phase 1 量測+回饋)✅;精準度定義(三維度 + Task 1 分桶)✅;500→1000 是否最佳(總覽說明改為自然成長,Phase 3 改標準)✅;哪些不轉(Global Constraints + 沿用 strict 預設,Phase 2 保守模式)✅;如何不誇大描述(Phase 3「四件套」)✅;短中長 roadmap + 判準(總覽表 + Phase 2/3 觸發條件)✅。

**2. Placeholder 掃描** — Phase 1 每個 code step 都有完整可執行程式與測試;Phase 2/3 刻意標為 gated outline(非 TDD),並說明原因(取決於 Phase 1 數字),非偷懶留白。

**3. 型別一致** — `EvalCase(id, src, expected)`、`EvalReport(total, passed, by_bucket, pass_rate)`、`classify_result(src, expected, actual, convertible)`、`score_cases(cases, convert_fn, convertible)`、桶常數 `PASS/RESIDUAL/MISSED/DIVERGENT`、`build_regression_stub(src, expected, id_hint)`、`github_issue_url(src, actual, expected, repo)` 跨 Task 1–6 命名一致;Task 4 的 `_convert`/`_convertible`/`_corpus_dir`/`_reports_dir`/`_today` helper 與其測試 monkeypatch 目標一致。

**4. 不變式** — held-out `main()` 永遠 exit 0(Task 4 測試強制驗證);資料放 corpus repo(Task 7);含簡體的 .py 加 `# zhtw:disable`(Task 1/5 測試、cli.py 既有)。
