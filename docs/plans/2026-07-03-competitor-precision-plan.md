<!-- zhtw:disable -->
# 競品研究與精準度提升計畫

日期：2026-07-03

## 結論

要先看競品，但不要抄競品詞庫。

競品的正確用途是：

- 建立能力地圖：知道市面工具支援哪些轉換方向、地區詞、平台與資料來源。
- 建立 benchmark：用同一批人工 expected 比較 zhtw、OpenCC、zhconv 等工具。
- 找候選問題：只把「競品正確、zhtw 錯」當成候選，不直接採用。
- 證明差異化：把「zhtw 正確、競品錯」保留下來，作為少錯轉策略的證據。

不能做的是：

- 不批次匯入 OpenCC、zhconv、MediaWiki 或其他競品詞庫。
- 不以「競品有轉」作為加入詞庫理由。
- 不追求和競品輸出一致。
- 不犧牲「寧可少轉，不要錯轉」來提高轉換覆蓋率。

## 競品能力地圖

第一批優先研究這些工具與資料來源：

| 競品 / 來源 | 能力 | 對 zhtw 的用途 | 風險 |
|-------------|------|----------------|------|
| OpenCC | 簡繁、台灣、香港、日本新字體、字級/詞級、地區詞 | 主要比較基準；找常見詞級差異 | 通用轉換容易過度轉換，不可當 expected |
| opencc-js | OpenCC JavaScript 版本；支援 `cn/tw/twp/hk/hkp/jp/t` locale 與網頁轉換 | 對照瀏覽器/JS SDK 能力與 locale 設計 | phrase conversion 不等於台灣 expected |
| opencc-data | OpenCC 詞庫、設定與測試資料集合 | 只作來源盤點與授權確認 | 詞庫不能直接匯入，需逐條人工確認 |
| zhconv Python | MediaWiki 詞表、最大正向匹配、支援 `zh-cn/zh-tw/zh-hk/zh-sg/zh-hans/zh-hant` | 找 Wikipedia/MediaWiki 風格差異 | MediaWiki/GPL/授權與語境問題，不可直接採用 |
| zhconv-rs | Rust/CLI/WASM；整合 MediaWiki/Wikipedia/OpenCC 規則並預編譯 automata | 對照 CLI、WASM、效能與跨語言資料設計 | 來源混合，不能當詞庫真相 |
| Calibre TradSimpChinese plugin | 電子書簡繁、地區詞、文字方向 | 對照長文本、EPUB 場景 | GPLv3 外掛與場景偏電子書 |
| Microsoft Word 中文轉換 | 文件工作流中的簡繁轉換 | 對照一般使用者期待與文件場景 | 難自動化、輸出不可當詞庫來源 |

參考來源：

- OpenCC GitHub：<https://github.com/byvoid/opencc>
- opencc-js GitHub：<https://github.com/nk2028/opencc-js>
- opencc-data GitHub：<https://github.com/nk2028/opencc-data>
- zhconv PyPI：<https://pypi.org/project/zhconv/>
- zhconv-rs GitHub：<https://github.com/Gowee/zhconv-rs>
- Calibre TradSimpChinese plugin：<https://github.com/Hopkins1/TradSimpChinese>

## 目前已完成的基線

已建立 report-only benchmark：

- `benchmarks/precision_cases.json`
- `scripts/competitor_benchmark.py`
- `docs/reports/competitor-benchmark-2026-07-03.md`
- `docs/reports/competitor-benchmark-2026-07-03.json`
- `make precision-benchmark`

2026-07-03 初始結果：

| 分類 | 數量 | 判讀 |
|------|------|------|
| `candidate_gap` | 0 | 沒有發現競品正確但 zhtw 錯 |
| `zhtw_miss` | 0 | 沒有發現 zhtw 不符合人工 expected |
| `zhtw_advantage` | 21 | zhtw 符合 expected，但至少一個競品不符合 |
| `all_match` | 5 | zhtw 與競品都符合 expected |

這代表第一批資料不應導入詞庫修改，應先擴大探索樣本。

## Phase 1：競品能力盤點

目標：知道市面工具有哪些能力，而不是急著改 zhtw。

工作項目：

- 盤點轉換方向：`s2t`、`s2tw`、`s2twp`、`s2hk`、`s2hkp`、`t2s`、`tw2s`、`hk2s`。
- 盤點平台：Python、JavaScript、Rust、CLI、WASM、Office/文件工具、電子書工具。
- 盤點資料來源與授權：Apache-2.0、GPL、MediaWiki/Wikipedia、第三方派生資料。
- 盤點場景：IT/UI、新聞、正式文件、社群、電子書、長文本、混合繁簡文本。

產出：

- `docs/reports/competitor-capability-map-YYYY-MM-DD.md`

驗收：

- 每個競品只記錄能力與風險，不產生詞庫修改。
- 每個外部資料來源都有來源連結與授權註記。

## Phase 2：差異探索工具

目標：從真實 corpus 找出 zhtw 與競品輸出不同的句子，降低人工審核量。

新增工具：

- `scripts/discover_competitor_diffs.py`

功能：

- 讀取 `tests/data/corpus/{news,tech,social,wiki,regressions}/*.json`。
- 跑 `zhtw`、`opencc-s2twp`、`zhconv-zh-tw`。
- 只輸出三者結果不同的句子。
- 若 corpus case 已有 `expected`，必須用 expected 判斷誰正確；不能只因兩個競品一致就提高優先級。
- 支援 `--limit`、`--category`、`--seed`、`--format json|md`。
- 缺少 OpenCC 或 zhconv 時 skipped，不讓 CI 失敗。
- 預設輸出到 `docs/reports/competitor-diffs-YYYY-MM-DD.{json,md}`。

差異分類：

有 corpus expected 時，優先使用正確性分類：

- `candidate_gap`：至少一個競品符合 expected，但 zhtw 不符合。
- `zhtw_advantage`：zhtw 符合 expected，但至少一個競品不符合。
- `all_match`：zhtw 與所有可用競品都符合 expected。
- `all_wrong`：zhtw 與所有可用競品都不符合 expected。
- `mixed_expected`：多個輸出可接受或 expected 需要人工確認。

沒有 corpus expected 時，才使用結構性差異分類：

- `competitors_agree`：OpenCC/zhconv 一致，但 zhtw 不同。
- `zhtw_unique`：zhtw 和兩個競品都不同。
- `opencc_unique`：OpenCC 和其他不同。
- `zhconv_unique`：zhconv 和其他不同。
- `all_different`：三者全不同。

優先審核順序：

1. `candidate_gap`
2. `all_wrong`
3. `mixed_expected`
4. 沒有 expected 的 `competitors_agree`
5. `all_different`
6. IT/UI/正式文件
7. 高頻詞或短句
8. 使用者真實回報

驗收：

- 可以在不安裝競品套件時正常輸出 skipped。
- 有 corpus expected 的案例必須輸出 correctness-aware 分類，避免兩個競品一起錯時被誤判為候選。
- 沒有 corpus expected 的案例必須標記 `review = pending`，不能直接進 benchmark。
- 可以用臨時依賴執行：

```bash
uv run --with opencc-python-reimplemented --with zhconv python scripts/discover_competitor_diffs.py --limit 300
```

## Phase 3：人工審核格式

目標：讓競品差異進入人工判斷，而不是進詞庫。

審核 JSON 欄位：

```json
{
  "id": "tech-0001",
  "category": "tech",
  "source_file": "tests/data/corpus/tech/samples.json",
  "case_id": "tech-001",
  "sample_seed": 42,
  "input": "原始簡體句子",
  "corpus_expected": "corpus 既有 expected，若無則為 null",
  "outputs": {
    "zhtw": "zhtw 輸出",
    "opencc-s2twp": "OpenCC 輸出",
    "zhconv-zh-tw": "zhconv 輸出"
  },
  "engine_versions": {
    "zhtw": "4.4.1",
    "opencc-s2twp": "0.1.7",
    "zhconv-zh-tw": "1.4.3"
  },
  "classification": "candidate_gap",
  "review": "pending",
  "expected": null,
  "decision": null,
  "notes": ""
}
```

人工只填：

- `expected`
- `decision`
- `notes`

工具必填、人工不改：

- `source_file`
- `case_id`
- `corpus_expected`
- `sample_seed`
- `outputs`
- `engine_versions`
- `classification`

`decision` 可用值：

- `zhtw_correct`
- `competitor_correct`
- `both_acceptable`
- `ambiguous_skip`
- `needs_more_context`

驗收：

- 沒有 `expected` 的案例不能進 benchmark。
- `ambiguous_skip` 與 `needs_more_context` 不得進詞庫。
- `both_acceptable` 預設不進 benchmark；只有能作為明確過度轉換保護案例時，才可用 `over_conversion_guard` 收錄。
- 每筆人工審核必須保留來源與 engine version，確保日後可重現。

## Phase 4：候選進入 benchmark

目標：只有人工確認的案例，才能變成品質基準。

進入 `benchmarks/precision_cases.json` 的條件：

- `decision = competitor_correct` 或人工確認 zhtw 錯。
- `decision = zhtw_correct` 且競品錯轉時，也可以進 benchmark；此類案例只能作為 `over_conversion_guard` 或差異化證據，不得導向詞庫擴張。
- 有明確 `expected`。
- 有 `domain`、`risk`、`notes`。
- 能說明為什麼台灣繁中應該這樣轉。

`risk` 建議值：

- `candidate`
- `over_conversion_guard`
- `identity_required`
- `ambiguous_skip`

驗收：

```bash
uv run python scripts/competitor_benchmark.py --format json --fail-on-zhtw-mismatch
uv run python -m pytest tests/test_competitor_benchmark.py -q
```

不進 benchmark 的情況：

- `decision = both_acceptable`，且沒有明確過度轉換保護價值。
- `decision = ambiguous_skip`。
- `decision = needs_more_context`。
- 只有競品一致，但沒有 corpus expected 或人工 expected。

## Phase 5：詞庫修正流程

目標：只修人工確認的 zhtw 錯轉。

每個詞庫修改都必須先回答：

- 這是不是台灣確實不用的詞？
- 轉換後是不是台灣常用？
- 是否有裸詞過度轉換風險？
- 是否有子字串問題？
- 是否需要 identity mapping？
- 是否已補 regression？

修改流程：

1. 先補 benchmark/golden/corpus regression。
2. 再改 `src/zhtw/data/terms/{cn,hk}/*.json`。
3. 若 target 可能被第二輪轉壞，補 identity mapping。
4. 若詞條有子字串風險，補保護詞或負向案例。
5. 跑驗證。

驗證：

```bash
uv run zhtw validate
uv run python scripts/audit_idempotency.py --sources cn,hk --curated-only --fail-on-issues
uv run python -m pytest tests/test_golden_rule_battery.py tests/test_corpus.py -q
uv run python -m pytest -q
```

## Phase 6：報告與決策節奏

每輪探索都產出：

- `docs/reports/competitor-diffs-YYYY-MM-DD.md`
- `docs/reports/competitor-diffs-YYYY-MM-DD.json`

報告保護規則：

- Markdown 報告第一行必須是 `<!-- zhtw:disable -->`。
- `.zhtwignore` 必須包含 `docs/reports/competitor-diffs-*`。
- 報告內的簡體 input、corpus expected、競品輸出不可被 repo 自身 hook 自動轉換。

報告摘要包含：

- 掃描 corpus 數量
- 含 corpus expected 的案例數量
- 差異筆數
- `candidate_gap` 數量
- `competitors_agree` 數量
- `zhtw_advantage` 數量
- `all_wrong` 數量
- 已人工審核數量
- 進入 benchmark 的案例數量
- 實際詞庫修改數量
- `zhtw_advantage` 案例摘要

決策規則：

- 有 `candidate_gap`：進 Phase 5。
- 沒有 `candidate_gap`：把結果當差異化證據，不改詞庫。
- 有大量 `all_different`：先加人工 expected，不急著改。
- 發現競品過度轉換：加入 `over_conversion_guard` 類案例。

## Phase 7：成功標準

短期：

- 完成 300 筆 corpus 差異探索。
- 至少人工審核 30 筆差異。
- 只把高信心案例加入 benchmark。
- `candidate_gap` 若為 0，明確記錄為「目前不改詞庫」。

中期：

- 每輪新增 20-50 筆人工 expected。
- 精選 corpus 往 750 筆前進。
- IT/UI/正式文件各自形成穩定 benchmark。

長期：

- 精選 corpus 至少 1000 筆。
- 每次品質宣稱都附 case 數、corpus 版本與 gate 結果。
- 競品 benchmark 成為 release 前 report-only 檢查，不成為硬 KPI。

## 第一個實作切片

先做最小可用版本：

1. 新增 `scripts/discover_competitor_diffs.py`。
2. 只支援 corpus JSON、`--limit`、`--format json|md`。
3. 輸出 report-only，不改詞庫。
4. 補一個不依賴 OpenCC/zhconv 的測試。
5. 用臨時依賴跑 300 筆：

```bash
uv run --with opencc-python-reimplemented --with zhconv python scripts/discover_competitor_diffs.py --limit 300
```

完成後根據報告決定是否進人工審核，不直接進詞庫。
