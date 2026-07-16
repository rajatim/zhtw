<!-- zhtw:disable -->
# 「市面上最準」準確度宣稱計畫

日期：2026-07-04

## 目標

讓 zhtw 最終能負責任地宣稱：

> zhtw 是目前針對「簡體中文 → 台灣繁體」場景最準確的開源轉換器之一；在公開 benchmark 中，zhtw 於整體準確率與低錯轉率皆優於主要競品。

更激進的行銷語「zhtw 是市面上最準的簡繁轉換器」只能在完成公開、可重現、外部審核的 benchmark 後使用，而且必須附上範圍限制。

## 現況基線

截至 2026-07-09，已完成：

- `scripts/competitor_benchmark.py`：人工 fixture 對比工具。
- `scripts/discover_competitor_diffs.py`：corpus 競品差異探索工具。
- `benchmarks/precision_cases.json`：37 筆人工 expected 的精準度案例，其中 11 筆為 M1 新增 `over_conversion_guard`。
- `benchmarks/accuracy/regression-v1.json`：1,066 筆 public regression dataset，含五個 corpus 類別各 100 筆、500 筆 promoted annotation，以及 66 筆已從 sealed holdout 移出的 holdout regression promotions。
- `benchmarks/accuracy/holdout-regression-candidates-v1.json`：66 筆已移出 sealed holdout 的公開 regression candidates。
- `benchmarks/accuracy/annotation-backlog-v1.json`：500 筆 M1 缺口的人工標註 backlog。
- `tests/test_accuracy_regression.py`：public regression dataset gate。
- `benchmarks/accuracy/blind-v1.inputs.json`：M2 sealed holdout 目前保留 261 筆 input-only seed pool；66 筆已移出 sealed 並 promotion 到 public regression，另有 batch4 100 筆新 input 已完成 maintainer expected review 並納入 private expected。
- `benchmarks/accuracy/blind-v1.inputs.schema.json` 與 `blind-v1.expected.schema.json`：M2 input/expected schema。
- `benchmarks/accuracy/competitors.lock.json`：M2 draft competitor adapter lockfile。
- `scripts/create_holdout_annotation_packet.py`：M2 人工標註包產生工具，只輸出 input 與空白欄位。
- `scripts/run_accuracy_benchmark.py`：M2 benchmark runner，會記錄 inputs、expected、lockfile hash。
- `docs/reports/competitor-diffs-full-2026-07-03.json`：500 筆 corpus 完整競品探索。
- `docs/reports/competitor-advantage-review-2026-07-03.md`：30 筆 `zhtw_advantage` 人工摘要。
- README 已加入精準度案例。

目前可說：

> 在 500 筆人工 expected 的台灣繁中 corpus 上，zhtw 全部符合 expected；OpenCC/zhconv 沒有出現「競品符合 expected、zhtw 不符合」的案例。此輪比較中 `all_match = 192`、`zhtw_advantage = 308`、`candidate_gap = 0`。

目前不能直接說：

> zhtw 是市面上最準的簡繁轉換器。

原因：

- 目前 corpus 仍是內部 curated set，不是公開盲測。
- 競品集合還不夠完整。
- 尚未有外部審核者或第三方可重現報告。
- 尚未按領域公開統計錯轉率、漏轉率與信賴區間。

## 宣稱邊界

本計畫只追求以下範圍：

| 項目 | 範圍 |
|------|------|
| 方向 | 簡體中文 → 台灣繁體 |
| 主要場景 | IT/UI、技術文件、LLM 生成內容、i18n、本機化、新聞/正式文件、社群短句 |
| 非目標 | 中文翻譯、文風改寫、粵語/國語互譯、所有地區繁體互轉 |
| 評估單位 | 句子與短段落，不以長篇文學風格改寫為主要 KPI |
| 優先指標 | 錯轉率最低，其次才是覆蓋率 |
| 市場範圍 | 主要開源轉換器；商業/線上工具只作補充抽測，除非能被可重現地納入正式 benchmark |

核心原則維持：

> 寧可少轉，不要錯轉。

## 競品集合

第一階段必測：

| 競品 | 測試配置 | 來源 | 納入理由 |
|------|----------|------|----------|
| OpenCC | `s2twp` | <https://github.com/byvoid/opencc> | 最成熟、最常被拿來比較的通用簡繁轉換器 |
| opencc-js | `cn -> twp` | <https://github.com/nk2028/opencc-js> | JavaScript 生態常用；支援 `tw/twp/hk/hkp` locale |
| zhconv Python | `zh-tw` | <https://pypi.org/project/zhconv/> | MediaWiki 詞表與最大正向匹配；常見 Python 對照組 |
| zhconv-rs | 由 adapter lockfile 固定 exact CLI/config；未固定前不進正式排名 | <https://github.com/Gowee/zhconv-rs> | Rust/CLI/WASM 對照組；整合 MediaWiki/Wikipedia/OpenCC rulesets |

正式 benchmark 只納入可重現的 competitor adapter。每個 adapter 必須在 lockfile 記錄：

- package 名稱與版本。
- 安裝來源與安裝命令。
- exact invocation command。
- locale/config 名稱。
- config/hash 或 ruleset 版本。
- runner OS、Python/Node/Rust runtime 版本。

不得在正式報告中使用「相關配置」「預設設定」等無法重跑的描述。

第二階段視可自動化程度納入：

| 競品 | 納入方式 | 風險 |
|------|----------|------|
| Calibre TradSimpChinese | 若可 CLI 化則納入電子書場景 | GPLv3 與電子書場景偏重 |
| Microsoft Word 中文轉換 | 手動抽測或 UI 自動化抽測 | 不易重現，不作主要 benchmark |
| 其他 npm / Python / browser converter | 先進能力地圖，再決定是否納入 | 品質與維護狀態不一 |

## Benchmark 分層

### Layer 1：公開 regression set

目的：防止 zhtw 回歸。

規模：

- 短期：1,000 筆。
- 中期：1,500 筆。
- 長期：2,000 筆。

來源：

- 現有 `zhtw-test-corpus`。
- 使用者回報。
- 競品 discovery 中的 `zhtw_advantage` 保護案例。
- 已修復的 `candidate_gap`。

用途：

- release gate。
- SDK golden parity。
- README / docs 的公開案例來源。

### Layer 2：sealed holdout set

目的：支撐「主要開源競品中最準」宣稱。

規模：

- 第一版：2,000 筆。
- 第二版：5,000 筆。

規則：

- 開發時不可用來調詞庫。
- expected 先由人工標註完成。
- 跑 benchmark 前不公開 expected，只公開輸入與標註規則。
- 發布報告時公開輸入、expected、所有工具輸出與版本。
- expected 公開後，該資料集降級為 public benchmark，不再支撐新的 blind 宣稱。
- 後續市場宣稱必須使用新的 sealed holdout，例如 `blind-v2`，或明確標示使用的是已公開資料集。
- 若開發過程因修 bug 參考過某個 blind case，該 case 必須移出 sealed set，改列 public regression。

用途：

- 對外準確度排名。
- 指標與信賴區間計算。
- 市場宣稱依據。

### Layer 3：真實場景 challenge set

目的：驗證 zhtw 在主要使用場景的實際價值。

領域與建議比例：

| 領域 | 比例 | 例子 |
|------|------|------|
| IT/API/CLI | 25% | 函式、例外、回傳、設定檔、憑證、伺服器 |
| UI/i18n | 20% | 登入、登出、復原、重新整理、我的最愛、選單 |
| LLM 生成內容 | 15% | 技術說明、README、產品文案、客服回答 |
| 新聞/正式文件 | 15% | 發布、文件、計畫、數據/資料、宣布 |
| 社群/日常 | 15% | 留言區、影片、腳踏車、週末、訊息 |
| 法律/財經/醫療 | 10% | 程序、憑證、申請、帳戶、症狀 |

用途：

- 產品定位。
- README 與官網案例。
- 與 OpenCC/zhconv 的場景差異化。

## 人工標註規範

每筆 case 至少包含：

```json
{
  "id": "blind-tech-0001",
  "domain": "it",
  "input": "这个函数会抛出异常。",
  "expected": "這個函式會拋出例外。",
  "acceptable": ["這個函式會拋出例外。"],
  "risk": "candidate",
  "notes": "台湾程式語境：函数→函式，异常→例外"
}
```

標註流程：

1. 第一位台灣繁中審核者標 `expected`。
2. 第二位台灣繁中審核者盲審。
3. 若兩人不一致，第三位裁決。
4. 保留 `acceptable`，但 benchmark 主指標以 normalized accepted match 為主。
5. 所有標註者不得先看 zhtw/OpenCC/zhconv 輸出。

品質要求：

- 每輪標註計算 inter-annotator agreement。
- 分歧率 > 10% 的領域需重寫標註規則。
- `both_acceptable` 不得用來粉飾模型分數；需另列。

計分 normalization：

- 比對前只做 Unicode NFC。
- CRLF/CR 轉為 LF。
- 移除 CLI 造成的單一結尾換行。
- 不轉換全形/半形標點。
- 不忽略句中空白。
- 不忽略標點差異。
- 不做任何簡繁、地區詞或同義詞 normalization。

計分欄位：

| 欄位 | 定義 |
|------|------|
| `primary_exact` | normalized output 等於 `expected` |
| `acceptable_exact` | normalized output 不等於 `expected`，但等於任一 `acceptable` |
| `accepted` | `primary_exact || acceptable_exact` |
| `miss` | 不符合 `expected` 或任何 `acceptable` |

排名主指標使用 `accepted_accuracy`，但報告必須同時列出 `primary_exact_accuracy`。若 competitor 只靠大量 `acceptable_exact` 拉高分數，需要在報告中揭露。

## 指標定義

主要指標：

| 指標 | 定義 | 用途 |
|------|------|------|
| accepted accuracy | 輸出等於 expected 或 acceptable | 排名主指標 |
| primary exact accuracy | 輸出等於 expected，不含 acceptable variants | 檢查標註一致性 |
| over-conversion rate | 把 expected 中應保留的台灣詞改壞 | zhtw 核心優勢 |
| under-conversion rate | 該轉的簡體/中國用語未轉 | 覆蓋率 |
| idempotency rate | convert(convert(x)) == convert(x) | 二次轉換安全 |
| domain accuracy | 各 domain accuracy | 找弱點 |
| severe error rate | P0/P1 錯轉比例 | release risk |

錯誤分級：

| 等級 | 定義 |
|------|------|
| P0 | 破壞正確台灣繁中、法律/醫療/財務高風險錯轉、二次轉換改壞 |
| P1 | IT/UI/正式文件高頻錯轉 |
| P2 | 領域詞或中頻在地化錯誤 |
| P3 | 低頻、罕見、人名、古文、語境模糊 |

排名規則：

1. P0 必須為 0。
2. P1 越少越好。
3. accepted accuracy 最高者排名優先。
4. 若 accepted accuracy 差距小於 0.5%，比較 over-conversion rate。
5. 若仍接近，按 primary exact accuracy、domain coverage 與 idempotency 排序。

## Benchmark 工具計畫

新增：

- `scripts/run_accuracy_benchmark.py`
- `benchmarks/accuracy/`
- `benchmarks/accuracy/competitors.lock.json`
- `docs/reports/accuracy-benchmark-YYYY-MM-DD.{json,md}`
- `docs/reports/accuracy-benchmark-YYYY-MM-DD.lock.json`

資料集建議結構：

```text
benchmarks/accuracy/
├── regression-v1.json
├── regression-v1.schema.json
├── blind-v1.inputs.json
├── blind-v1.expected.json
├── blind-v1.schema.json
├── competitors.lock.json
└── README.md
```

`blind-v1.inputs.json` 可先公開；`blind-v1.expected.json` 在 benchmark 報告發布後公開，避免開發期間污染。

CLI 設計：

```bash
uv run python scripts/run_accuracy_benchmark.py \
  --inputs benchmarks/accuracy/blind-v1.inputs.json \
  --expected benchmarks/accuracy/blind-v1.expected.json \
  --competitors-lock benchmarks/accuracy/competitors.lock.json \
  --competitors zhtw,opencc,opencc-js,zhconv,zhconv-rs \
  --format md,json \
  --output docs/reports/accuracy-benchmark-2026-XX-XX
```

報告必須包含：

- dataset 名稱、版本、hash。
- case 數、domain 分布。
- 每個 competitor 的套件版本、設定、命令。
- accepted accuracy 與 primary exact accuracy。
- over/under conversion rate。
- P0/P1/P2/P3 數量。
- 每個錯誤 row 的 input、expected、actual、error type、domain。
- bootstrap confidence interval。
- sealed/public 狀態；若 expected 已公開，必須標明該資料集不再是 blind。

## 交付物清單

| 階段 | 交付物 | 檔案 |
|------|--------|------|
| M1 | regression dataset v1 | `benchmarks/accuracy/regression-v1.json` |
| M1 | regression schema | `benchmarks/accuracy/regression-v1.schema.json` |
| M1 | regression 驗證測試 | `tests/test_accuracy_regression.py` |
| M2 | blind inputs | `benchmarks/accuracy/blind-v1.inputs.json` |
| M2 | blind expected | `benchmarks/accuracy/blind-v1.expected.json` |
| M2 | competitor lockfile | `benchmarks/accuracy/competitors.lock.json` |
| M2 | benchmark runner | `scripts/run_accuracy_benchmark.py` |
| M2 | benchmark 報告 | `docs/reports/accuracy-benchmark-YYYY-MM-DD.md` |
| M2 | benchmark raw data | `docs/reports/accuracy-benchmark-YYYY-MM-DD.json` |
| M2 | benchmark lockfile | `docs/reports/accuracy-benchmark-YYYY-MM-DD.lock.json` |
| M3 | 外部審核紀錄 | `docs/reports/accuracy-audit-YYYY-MM-DD.md` |
| M4 | 市場宣稱摘要 | `docs/reports/market-claim-evidence-YYYY-MM-DD.md` |

所有 report 檔案第一行都必須加：

```html
<!-- zhtw:disable -->
```

並確認 `.zhtwignore` 保護以下路徑，避免資料集與報告中的簡體輸入被 hook 轉換：

- `benchmarks/accuracy/`
- `docs/reports/accuracy-benchmark-*`
- `docs/reports/accuracy-audit-*`
- `docs/reports/market-claim-evidence-*`

## 任務拆解

### M1 任務

- [x] 從 full discovery 與現有 corpus 建立 500 筆 public regression。
- [ ] 依 domain 分布補足 IT/UI、正式文件、社群與高風險領域。
- [x] 將案例整理成 `benchmarks/accuracy/regression-v1.json`。
- [x] 建立 `regression-v1.schema.json`。
- [x] 新增 `tests/test_accuracy_regression.py`。
- [x] 把 regression 測試加入 release gate 文件。
- [x] 跑 `uv run zhtw validate`。
- [x] 跑 `uv run python -m pytest -q`。
- [x] 建立 `annotation-backlog-v1.json` 追蹤剩餘 500 筆人工 expected 缺口。

### M2 任務

- [x] 建立 blind case source pool 第一批 100 筆 input-only seed。
- [ ] 去重與難度分層。
- [x] 產出 `blind-v1.inputs.json`。
- [x] 完成第一位標註者 expected。
- [ ] 完成第二位標註者盲審。
- [ ] 第三位裁決所有分歧。
- [x] 產出 `blind-v1.expected.json`。
- [x] 產出 draft `competitors.lock.json`，固定目前 runner 支援的 adapter command/config/version 來源。
- [x] 建立 first human review annotation packet 產生工具。
- [x] 實作 `scripts/run_accuracy_benchmark.py`。
- [ ] 接入 zhtw、OpenCC、opencc-js、zhconv、zhconv-rs。
- [ ] 產出 JSON/Markdown/lockfile 報告。
- [ ] 將報告與資料集 hash 固定。
- [ ] 發布後將 `blind-v1` 標記為 public benchmark，下一輪宣稱改用新的 sealed holdout。

### M3 任務

- [ ] 準備 200 筆外部抽審包。
- [ ] 找 3-5 位外部審核者。
- [ ] 收集異議與裁決結果。
- [ ] 修正標註規範中造成分歧的規則。
- [ ] 發布 `accuracy-audit-YYYY-MM-DD.md`。

### M4 任務

- [ ] 擴充到 5,000 筆 blind + challenge benchmark。
- [ ] 補齊所有主要競品。
- [ ] 重新跑 benchmark。
- [ ] 確認 P0 = 0，P1 未決議 = 0。
- [ ] 確認 zhtw 在 accuracy、over-conversion、IT/UI domain accuracy 皆排名第一。
- [ ] 撰寫 `market-claim-evidence-YYYY-MM-DD.md`。
- [ ] 更新 README 與文件宣稱。

## 完成定義

| 宣稱等級 | 完成條件 |
|----------|----------|
| 內部可用 | M1 完成，regression 至少 1,000 筆通過 |
| 文件可寫「主要開源競品中表現最佳」 | M2 完成，benchmark 公開且可重現，且 zhtw accepted accuracy 第一 |
| 文件可寫「最準確的開源轉換器之一」 | M3 完成，外部審核完成 |
| 可支撐「目前此場景下最準確的開源轉換器」 | M4 完成，5,000 筆 benchmark 排名第一 |
| 不建議單獨使用「市面上最準」 | 除非同時附範圍、資料集、競品版本與報告連結 |

## 建議時程

| 週期 | 目標 | 產出 |
|------|------|------|
| 第 1 週 | M1 planning + 100-200 筆保護案例 | regression draft |
| 第 2-3 週 | regression 擴到 1,000 筆 | regression-v1 + 測試 |
| 第 4-6 週 | blind-v1 標註 2,000 筆 | inputs + expected |
| 第 7 週 | benchmark runner 與競品 adapter | run_accuracy_benchmark.py |
| 第 8 週 | 第一版公開 benchmark | accuracy report |
| 第 9-10 週 | 外部審核 | audit report |
| 第 11-12 週 | 5,000 筆 market claim benchmark | market claim evidence |

時程可以壓縮，但不能跳過 blind holdout、外部審核與 report lockfile。

## 市場宣稱範圍

本計畫的正式排名預設只涵蓋主要開源競品。若要宣稱廣義「市面上最準」，必須額外完成：

- 列出非開源、線上服務、商業工具的納入/排除標準。
- 對不可自動化工具提供時間戳、版本、操作流程與原始輸出截圖或匯出檔。
- 明確標示哪些 competitor 不可完全重現，因此只作輔助證據。
- 報告中不得把「主要開源競品」偷換成「全市場」。

## 里程碑

### M0：目前狀態

已完成：

- 500 筆 corpus competitor discovery。
- `candidate_gap = 0`。
- `zhtw_advantage = 308`。
- README 已寫入精準度案例。

宣稱：

> 在 500 筆人工 expected corpus 上，zhtw 未發現競品正確而 zhtw 錯誤的案例。

### M1：公開 regression 擴到至少 1,000 筆

工作：

- 從 full discovery 的 `zhtw_advantage` 挑 100-200 筆保護案例。
- 收集使用者回報。
- 各 domain 至少 150 筆，IT/UI 至少 250 筆。

目前進度：

- 已建立 `benchmarks/accuracy/regression-v1.json`，目前共 1,066 筆。
- 分布為 `formal = 103`、`it = 187`、`llm = 2`、`mixed = 25`、`ui = 132`、`news = 100`、`regressions = 100`、`social = 178`、`tech = 100`、`wiki = 100`。
- 其中 `over_conversion_guard = 435`、`baseline_guard = 289`、`candidate_gap = 342`。
- 原始 corpus 的 `zhtw_advantage = 308` 中，141 筆為 OpenCC 與 zhconv 皆不符合 expected，167 筆為其中一個競品不符合 expected。
- 這是 public regression draft，不是 sealed holdout。
- 現有人工 expected corpus 已全數納入，且 500 筆 approved annotation 已 promotion；M1 1,000 筆 public regression 目標已完成。
- 不可用 zhtw 或競品輸出合成 expected 來補足 1,000 筆。
- 已建立 `benchmarks/accuracy/annotation-backlog-v1.json` 追蹤 500 筆缺口，配額為 IT/API/CLI 175、UI/i18n 125、正式/高風險 100、社群日常 75、混合歧義 25；目前已收集 500 筆，全部 500 筆已 approved。
- 已收集第一批 `it-api-cli` 候選 input 25 筆，並由 `tim` 完成 first pass。
- 已透過 Gemini Vertex advisory review 比對 25 筆；11 筆與 first pass 完全一致，14 筆由 `tim` 裁決採用 Gemini advisory 版本。
- 這 25 筆目前狀態為 `approved`，其中 14 筆標記為 `human_adjudication`；Gemini 記錄在 `review.ai_advisory`，不記為人類 `blind_reviewer`。
- 已建立 promotion gate：`make accuracy-promotion-gate DATE=2026-07-05`，用來確認 approved expected 是否已符合目前 zhtw 輸出。
- 2026-07-05 gate 結果：25 筆 approved 全部 promotion-ready，0 筆需要修 zhtw 輸出，報告在 `docs/reports/annotation-promotion-gate-2026-07-05.md`。
- 已將 500 筆 promotion-ready annotation cases promote 進 `regression-v1.json`；M1 public regression 1,000 筆目標完成。
- 已新增第二批 `it-api-cli` 候選 input 50 筆（`it-api-cli-0026` 到 `it-api-cli-0075`），Codex AI draft 報告在 `docs/reports/annotation-first-pass-ai-draft-it-api-cli-0026-0075-2026-07-05.md`。
- 已依新順序完成 Gemini Vertex advisory：`docs/reports/annotation-gemini-vertex-advisory-it-api-cli-0026-0075-2026-07-05.md`。50 筆中 25 筆與 Codex draft 完全一致，25 筆有差異；maintainer 已指定採用 Gemini 版本，這 50 筆目前狀態為 `approved` 並已 promotion。
- 已新增第三批 `it-api-cli` 候選 input 50 筆（`it-api-cli-0076` 到 `it-api-cli-0125`），Codex AI draft 報告在 `docs/reports/annotation-first-pass-ai-draft-it-api-cli-0076-0125-2026-07-06.md`。
- 已依新順序完成第三批 Gemini Vertex advisory：`docs/reports/annotation-gemini-vertex-advisory-it-api-cli-0076-0125-2026-07-06.md`。50 筆中 24 筆與 Codex draft 完全一致，26 筆有差異；maintainer 已指定採用 Codex 版本，這 50 筆目前狀態為 `approved` 並已 promotion。
- 已新增第四批 `it-api-cli` 候選 input 50 筆（`it-api-cli-0126` 到 `it-api-cli-0175`），Codex AI draft 報告在 `docs/reports/annotation-first-pass-ai-draft-it-api-cli-0126-0175-2026-07-06.md`。
- 已依新順序完成第四批 Gemini Vertex advisory：`docs/reports/annotation-gemini-vertex-advisory-it-api-cli-0126-0175-2026-07-06.md`。50 筆中 34 筆與 Codex draft 完全一致，16 筆有差異；maintainer 已指定採用 Gemini 版本，這 50 筆目前狀態為 `approved` 並已 promotion。
- 已新增第一個 `ui-i18n` 工作單位 100 筆（`ui-i18n-0001` 到 `ui-i18n-0100`），Codex AI draft 報告在 `docs/reports/annotation-first-pass-ai-draft-ui-i18n-0001-0100-2026-07-06.md`。
- 已依新順序分兩批完成 UI/i18n Gemini Vertex advisory：`docs/reports/annotation-gemini-vertex-advisory-ui-i18n-0001-0050-2026-07-06.md` 與 `docs/reports/annotation-gemini-vertex-advisory-ui-i18n-0051-0100-2026-07-06.md`。100 筆中 72 筆與 Codex draft 完全一致，28 筆有差異；maintainer 已指定採用 Codex review 建議，這 100 筆目前狀態為 `approved` 並已 promotion。
- 已新增第二個 `ui-i18n` 工作單位 25 筆（`ui-i18n-0101` 到 `ui-i18n-0125`），Codex AI draft 報告在 `docs/reports/annotation-first-pass-ai-draft-ui-i18n-0101-0125-2026-07-06.md`。
- 已完成第二個 UI/i18n Gemini Vertex advisory：`docs/reports/annotation-gemini-vertex-advisory-ui-i18n-0101-0125-2026-07-06.md`。25 筆中 18 筆與 Codex draft 完全一致，7 筆有差異；maintainer 已指定採用 Codex review 建議，這 25 筆目前狀態為 `approved` 並已 promotion。
- 已新增第一個 `formal-high-risk` 工作單位 100 筆（`formal-high-risk-0001` 到 `formal-high-risk-0100`），Codex AI draft 報告在 `docs/reports/annotation-first-pass-ai-draft-formal-high-risk-0001-0100-2026-07-06.md`。
- 已依新順序分兩批完成 formal-high-risk Gemini Vertex advisory：`docs/reports/annotation-gemini-vertex-advisory-formal-high-risk-0001-0050-2026-07-06.md` 與 `docs/reports/annotation-gemini-vertex-advisory-formal-high-risk-0051-0100-2026-07-06.md`。100 筆中 91 筆與 Codex draft 完全一致，9 筆有差異；maintainer 已指定 2 筆採 Codex、7 筆採 Gemini，這 100 筆目前狀態為 `approved` 並已 promotion。
- 已新增第一個 `social-daily` 工作單位 75 筆（`social-daily-0001` 到 `social-daily-0075`），Codex AI draft 報告在 `docs/reports/annotation-first-pass-ai-draft-social-daily-0001-0075-2026-07-07.md`。
- 已依新順序分兩批完成 social-daily Gemini Vertex advisory：`docs/reports/annotation-gemini-vertex-advisory-social-daily-0001-0050-2026-07-07.md` 與 `docs/reports/annotation-gemini-vertex-advisory-social-daily-0051-0075-2026-07-07.md`。75 筆中 60 筆與 Codex draft 完全一致，15 筆有差異；maintainer 已指定 13 筆採 Codex、2 筆採 Gemini，這 75 筆目前狀態為 `approved` 並已 promotion。
- 已新增第一個 `mixed-ambiguity` 工作單位 25 筆（`mixed-ambiguity-0001` 到 `mixed-ambiguity-0025`），Codex AI draft 報告在 `docs/reports/annotation-first-pass-ai-draft-mixed-ambiguity-0001-0025-2026-07-07.md`。
- 已完成 mixed-ambiguity Gemini Vertex advisory：`docs/reports/annotation-gemini-vertex-advisory-mixed-ambiguity-0001-0025-2026-07-07.md`。25 筆中 18 筆與 Codex draft 完全一致，7 筆有差異；maintainer 已指定 6 筆採 Codex、1 筆採 Gemini，這 25 筆目前狀態為 `approved` 並已 promotion。
- 已建立 blind review packet 產生工具，避免第二審看到 `review.expected` 或 `ai_draft`；目前預設流程改為 Codex first advisory -> Gemini independent advisory -> maintainer final review。
- 標註進度可用 `make accuracy-annotation-status` 查詢。
- Blind review packet 可用 `make accuracy-blind-review-packet BATCH=it-api-cli DATE=2026-07-05` 產生。

驗收：

```bash
uv run zhtw validate
uv run python scripts/audit_idempotency.py --sources cn,hk --curated-only --fail-on-issues
uv run python -m pytest tests/test_golden_rule_battery.py tests/test_corpus.py -q
uv run python -m pytest -q
```

宣稱：

> zhtw 在 1,066 筆公開 regression corpus 維持 100% 通過。

### M2：完成 2,000 筆 blind holdout v1

工作：

- 建立 `benchmarks/accuracy/blind-v1.inputs.json` 與 `benchmarks/accuracy/blind-v1.expected.json`。
- 先以 maintainer single-human + AI advisory 完成內部 sanity；嚴格市場宣稱前再補第二位 human reviewer 或明確揭露審核方式。
- 建立 benchmark runner。
- 對 zhtw、OpenCC、opencc-js、zhconv、zhconv-rs 全部跑一次。

目前進度：

- 已建立 `benchmarks/accuracy/blind-v1.inputs.json`，目前 261 / 2,000 筆 input-only seed pool。
- 目前分布為 IT/API/CLI 53、UI/i18n 52、LLM 內容 43、正式文件 41、社群日常 44、高風險 28。
- 已建立 `blind-v1.inputs.schema.json`，明確禁止 input cases 出現 `expected`、`acceptable`、`review`、`annotation`。
- 已建立 `blind-v1.expected.schema.json`，要求 expected 來自 human review only；目前允許
  `single_human_with_ai_advisory`，分歧需 maintainer 裁決。
- 已建立 `.gitignore` 保護 `benchmarks/accuracy/blind-v*.expected.json`，避免 sealed ground truth 在發布前誤 commit。
- 已建立 draft `competitors.lock.json`。目前 runner 支援 `zhtw`、`opencc-s2twp`、`zhconv-zh-tw`；`opencc-js` 與 `zhconv-rs` 仍是 pending adapter lock。
- 已建立 `scripts/create_holdout_annotation_packet.py`，可從 input-only pool 產生人類 reviewer packet，不包含任何 converter/LLM 輸出。
- 已建立 `scripts/run_accuracy_benchmark.py`，會輸出 JSON/Markdown report 並記錄 inputs、expected、lockfile 的 sha256。
- 已產生第一份 first human review packet：
  `docs/reports/holdout-annotation-packet-blind-v1-first_human_review-2026-07-07.md`。
- 已確認 maintainer 加速 review 節奏：Codex 先做第一版建議，Gemini 再獨立看，
  Codex 彙整一致/差異/低信心案例，最後只把需要確認的列給 maintainer。Codex 與
  Gemini 結果都只能是 advisory；maintainer 確認後才算 human decision。
- 已完成 Codex first-pass advisory：
  `docs/reports/holdout-codex-first-pass-blind-v1-0001-0100-2026-07-08.md` 與
  `docs/reports/holdout-codex-first-pass-blind-v1-0001-0100-2026-07-08.json`。100 筆
  全部有建議 expected，其中 83 筆 high confidence、17 筆 medium confidence、36 筆
  標示為後續需確認或需看 Gemini 差異。
- 已完成 Gemini independent advisory：
  `docs/reports/holdout-gemini-vertex-advisory-blind-v1-0001-0100-2026-07-08.md` 與
  `docs/reports/holdout-gemini-vertex-advisory-blind-v1-0001-0100-2026-07-08.json`。100 筆
  中 70 筆與 Codex 完全一致、30 筆有差異，policy filter 後 maintainer queue 共
  59 筆。
- 已完成 Codex/Gemini diff review：
  `docs/reports/holdout-codex-gemini-diff-review-blind-v1-0001-0100-2026-07-08.md` 與
  `docs/reports/holdout-codex-gemini-diff-review-blind-v1-0001-0100-2026-07-08.json`。
  30 筆差異的初步建議為 24 筆採 Codex、5 筆採 Gemini、1 筆採第三版。
- 已產生 maintainer confirmation packet：
  `docs/reports/holdout-maintainer-confirmation-blind-v1-0001-0100-2026-07-08.md` 與
  `docs/reports/holdout-maintainer-confirmation-blind-v1-0001-0100-2026-07-08.json`。
  59 筆需要確認，其中 30 筆為差異、29 筆為 policy quick confirm；41 筆 no immediate
  question。
- Maintainer 已於 2026-07-08 回覆 OK，採用 confirmation packet 建議。
- 已產生本機 private `benchmarks/accuracy/blind-v1.expected.json`，狀態為
  `sealed_private`，approval policy 為 `single_human_with_ai_advisory`。100 筆中
  70 筆為 `human_first_pass`，30 筆為 `human_adjudication`。該檔由 `.gitignore`
  保護，不公開。
- 已產生 final decision summary：
  `docs/reports/holdout-maintainer-final-decision-blind-v1-0001-0100-2026-07-08.md` 與
  `docs/reports/holdout-maintainer-final-decision-blind-v1-0001-0100-2026-07-08.json`。
  公開摘要只含 metadata/hash/counts，不含 expected values。
- 已用 private expected 跑本機 benchmark sanity check，完整 rows 僅保存在 `/tmp`。
  Aggregate-only summary 在
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-2026-07-09.md` 與
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-2026-07-09.json`。這份 sanity
  已更新為覆蓋目前 261 筆 private expected；zhtw accepted 207/261，accepted accuracy
  0.7931，primary exact accuracy 0.7050，idempotency 0.9885。
- 已完成 private miss classification，報告在
  `docs/reports/holdout-miss-classification-blind-v1-2026-07-08.md` 與
  `docs/reports/holdout-miss-classification-blind-v1-2026-07-08.json`。43 筆 miss 中，
  22 筆建議先移出 sealed 再轉 public regression 候選，7 筆保留作 sealed holdout
  訊號，14 筆需先重審 expected/acceptable variants。公開報告不含 expected、input、
  converter output 或完整 rows。
- 已於 2026-07-09 將 22 筆 `move_to_public_regression_candidate` 從 sealed holdout 移出，
  建立 `benchmarks/accuracy/holdout-regression-candidates-v1.json`，以完整句 mapping +
  identity mapping 修正，promotion gate 22/22 通過，並以
  `holdout_regression_promoted` 加入 `regression-v1.json`。公開紀錄在
  `docs/reports/holdout-sealed-pool-update-blind-v1-2026-07-09.md` 與
  `docs/reports/holdout-regression-promotion-gate-blind-v1-2026-07-09.md`。
- 已完成 14 筆 `requires_expected_recheck`，報告在
  `docs/reports/holdout-expected-recheck-blind-v1-2026-07-09.md` 與
  `docs/reports/holdout-expected-recheck-blind-v1-2026-07-09.json`。其中 12 筆只在 private
  expected 加入 acceptable variant，2 筆維持 strict miss；公開報告不含 expected、
  acceptable variants、input、converter output 或完整 rows。
- 已完成剩餘 9 筆 sealed miss 的二次分類，報告在
  `docs/reports/holdout-remaining-miss-classification-blind-v1-2026-07-09.md` 與
  `docs/reports/holdout-remaining-miss-classification-blind-v1-2026-07-09.json`。其中 5 筆
  建議下一步先移出 sealed 再轉 public regression candidate，4 筆保留作 sealed
  holdout 訊號。
- 已於 2026-07-09 將上述 5 筆 `move_to_public_regression_candidate` 從 sealed holdout 移出，
  追加到 `benchmarks/accuracy/holdout-regression-candidates-v1.json`，以完整句 mapping +
  identity mapping 修正，batch2 promotion gate 5/5 通過，並以
  `holdout_regression_promoted` 加入 `regression-v1.json`。公開紀錄在
  `docs/reports/holdout-sealed-pool-update-blind-v1-batch2-2026-07-09.md` 與
  `docs/reports/holdout-regression-promotion-gate-blind-v1-batch2-2026-07-09.md`。
- 第二批 promotion 後 sealed pool 曾剩 73 筆；當時 private sanity 為 69/73 accepted、4 misses。
- 已於 2026-07-09 追加 127 筆 input-only seed，將 `blind-v1.inputs.json` 擴充到 200 筆。
  擴充紀錄在 `docs/reports/holdout-input-pool-expansion-blind-v1-2026-07-09.md`。
- 已對上述 127 筆完成 Codex first-pass advisory、Gemini Vertex advisory aggregate 與
  Codex/Gemini diff review。報告在
  `docs/reports/holdout-codex-first-pass-blind-v1-expansion-127-cases-2026-07-09.md`、
  `docs/reports/holdout-gemini-vertex-advisory-blind-v1-expansion-127-cases-2026-07-09.md`、
  `docs/reports/holdout-codex-gemini-diff-review-blind-v1-expansion-127-cases-2026-07-09.md`。
  127 筆中 79 筆 Codex/Gemini 完全一致、48 筆有差異；policy filter 後 maintainer
  queue 共 81 筆。這些報告本身仍是 advisory，不可單獨作為 ground truth。
- 已產生 48 筆差異專用 maintainer confirmation packet：
  `docs/reports/holdout-maintainer-confirmation-blind-v1-expansion-differences-2026-07-09.md`。
  這份 packet 只列 Codex/Gemini 差異；33 筆一致但 policy review 的案例延後處理。
- Maintainer 已確認這 48 筆差異案例採用 recommended expected，決策摘要在
  `docs/reports/holdout-maintainer-final-decision-blind-v1-expansion-differences-2026-07-09.md`。
  這份是 partial decision；完整 private expected 重建記錄在 127 筆 final decision。
- 33 筆 Codex/Gemini exact-match policy-review 案例已整理成 confirmation packet，且
  Maintainer 已回覆 OK：
  `docs/reports/holdout-maintainer-confirmation-blind-v1-expansion-policy-review-2026-07-09.md`。
  對應決策摘要在
  `docs/reports/holdout-maintainer-final-decision-blind-v1-expansion-policy-review-2026-07-09.md`。
- 已產生 127 筆 expansion final decision summary：
  `docs/reports/holdout-maintainer-final-decision-blind-v1-expansion-127-cases-2026-07-09.md`。
  本機 private `benchmarks/accuracy/blind-v1.expected.json` 曾重建為 200 筆；batch3 移出 39 筆後，目前對齊 161 筆
  `blind-v1.inputs.json` sha256。Expansion 127 筆中 79 筆為 `human_first_pass`、48 筆為
  `human_adjudication`；當時全體 200 筆中 135 筆為 `human_first_pass`、65 筆為
  `human_adjudication`。
- Batch4 前可做 161 筆 private benchmark sanity check；batch4 封存後目前可做
  261 筆 private benchmark sanity check。若要支撐嚴格 sealed benchmark 宣稱，仍需補第二位
  human reviewer 或明確揭露 single-human + AI advisory policy。
- 已完成 200 筆 sanity 的 56 筆 miss classification，公開摘要在
  `docs/reports/holdout-miss-classification-blind-v1-200-cases-2026-07-09.md`。
  分類結果：39 筆建議先移出 sealed 再轉 public regression candidate，11 筆需
  expected/acceptable recheck，6 筆保留作 sealed holdout signal。
- Gemini 已 review sanitized classification metadata，報告在
  `docs/reports/holdout-gemini-policy-review-miss-classification-blind-v1-200-cases-2026-07-09.md`；
  Gemini 未收到 input、expected、acceptable、zhtw output 或 benchmark rows，回覆
  policy consistent，needs follow-up 0。
- 已於 2026-07-09 將 39 筆 `move_to_public_regression_candidate` 從 200 筆 sanity miss classification 移出 sealed，追加到 `benchmarks/accuracy/holdout-regression-candidates-v1.json`，以完整句 mapping + identity mapping 修正，batch3 promotion gate 39/39 通過，並以 `holdout_regression_promoted` 加入 `regression-v1.json`。公開紀錄在 `docs/reports/holdout-sealed-pool-update-blind-v1-batch3-2026-07-09.md` 與 `docs/reports/holdout-regression-promotion-gate-blind-v1-batch3-2026-07-09.md`。
- Batch3 後 public regression 為 1,066 筆；sealed pool 為 161 筆；post-batch3 recheck
  final decision 後 private sanity 為 155/161 accepted、6 misses。Batch4 封存後最新
  private sanity 為 207/261 accepted、54 misses。
- 已完成 post-batch3 17 筆 miss recheck first pass：
  `docs/reports/holdout-post-batch3-miss-recheck-blind-v1-2026-07-09.md`。Codex 建議
  11 筆由 maintainer 確認是否加入 private acceptable variant，6 筆保留 sealed
  holdout signal；Gemini sanitized policy review 在
  `docs/reports/holdout-gemini-policy-review-post-batch3-recheck-blind-v1-2026-07-09.md`，
  回覆 policy consistent、needs follow-up 0。Maintainer 已確認 11 筆 acceptable
  variant 建議，private expected 已更新，primary expected 未變更；final decision 在
  `docs/reports/holdout-maintainer-final-decision-post-batch3-recheck-blind-v1-2026-07-09.md`。
  maintainer review packet 在 `/tmp/zhtw-holdout-post-batch3-maintainer-review-packet-2026-07-09.md`。
- 已整理剩餘 6 筆 sealed holdout signal，公開 metadata summary 在
  `docs/reports/holdout-remaining-signal-summary-blind-v1-2026-07-09.md`；Gemini
  sanitized policy review 在
  `docs/reports/holdout-gemini-policy-review-remaining-signal-blind-v1-2026-07-09.md`。
  6 筆全數保留 sealed，不作為 converter/dictionary tuning 來源；未來若要修，必須先移出
  sealed holdout 並建立 public regression candidate artifact。
- 已新增 batch4 100 筆 input-only cases，目前 `blind-v1.inputs.json` 為 261/2,000；
  expansion audit 在
  `docs/reports/holdout-input-pool-expansion-blind-v1-batch4-100-cases-2026-07-09.md`。
  Codex first-pass、Gemini advisory、diff review 與 maintainer confirmation packet 已完成：
  `docs/reports/holdout-codex-first-pass-blind-v1-batch4-100-cases-2026-07-09.md`、
  `docs/reports/holdout-gemini-vertex-advisory-blind-v1-batch4-100-cases-2026-07-09.md`、
  `docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch4-100-cases-2026-07-09.md`、
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch4-100-cases-2026-07-09.md`。
  Batch4 中 Codex/Gemini exact match 74 筆、差異 26 筆、maintainer queue 64 筆；
  Maintainer 已回覆 OK，final decision summary 在
  `docs/reports/holdout-maintainer-final-decision-blind-v1-batch4-100-cases-2026-07-09.md`。
  本機 private expected 已更新到 261 筆；batch4 100 筆中 74 筆為 `human_first_pass`、
  26 筆為 `human_adjudication`。
- 已完成 261 筆 sanity 的 54 筆 miss classification，公開摘要在
  `docs/reports/holdout-miss-classification-blind-v1-261-cases-2026-07-09.md`。分類結果：
  18 筆建議先移出 sealed 再轉 public regression candidate，16 筆需 expected/acceptable
  recheck，20 筆保留作 sealed holdout signal。Gemini 已 review sanitized classification
  metadata，報告在
  `docs/reports/holdout-gemini-policy-review-miss-classification-blind-v1-261-cases-2026-07-09.md`；
  Gemini 未收到 input、expected、acceptable、zhtw output 或 benchmark rows，最終回覆
  policy consistent，needs follow-up 0。Codex 已依 Gemini policy finding 把 7 筆
  high-risk / over-conversion guard 案例改為 `requires_expected_recheck`。
- 已完成 261 筆 sanity 中 16 筆 `requires_expected_recheck` 的 Codex first-pass
  recheck summary，公開摘要在
  `docs/reports/holdout-requires-expected-recheck-blind-v1-261-cases-2026-07-09.md`。
  Private maintainer packet 在
  `/tmp/zhtw-holdout-261-case-recheck-maintainer-review-packet-2026-07-09.md`，含 sealed
  input、expected、acceptable、zhtw output，不進 repo。Codex 建議 9 筆由 maintainer
  確認是否加入 acceptable variant，5 筆確認後移出 sealed 再轉 public regression
  candidate，2 筆維持 strict primary expected。Gemini sanitized policy review 在
  `docs/reports/holdout-gemini-policy-review-requires-expected-recheck-blind-v1-261-cases-2026-07-09.md`，
  Gemini 未收到 sealed values，回覆 policy consistent、needs follow-up 0。

驗收：

- dataset hash 固定。
- benchmark 可重跑。
- 報告公開。
- zhtw accepted accuracy 第一。
- zhtw P0 = 0，P1 未決議 = 0。
- over-conversion rate 最低或並列最低；若不是最低，只能作「accuracy 第一」宣稱，不能作「錯轉率最低」宣稱。
- 發布後將 `blind-v1` 降級為 public benchmark，後續 blind 宣稱需使用 `blind-v2` 或更新 sealed set。

宣稱：

> 在 2,000 筆 sealed holdout benchmark 中，zhtw 於主要開源競品內達到最高 accepted accuracy。

### M3：完成外部審核

工作：

- 找 3-5 位外部台灣使用者或譯者抽審。
- 抽審 200 筆 benchmark 結果。
- 記錄異議與修正。

驗收：

- 外部審核分歧率 < 5%。
- P0/P1 未決議 issue = 0。

宣稱：

> zhtw 是目前針對簡體 → 台灣繁體最準確的開源轉換器之一。

### M4：市場宣稱版

前提：

- 5,000 筆新的 sealed holdout + real-world benchmark。
- 主要開源競品全納入。
- 報告公開、命令可重現。
- 外部審核完成。
- zhtw 在總體 accepted accuracy、over-conversion rate、IT/UI domain accepted accuracy 皆排名第一。

可用宣稱：

> zhtw 是目前針對簡體 → 台灣繁體場景最準確的開源轉換器。

若要使用「市面上最準」：

> zhtw 在公開、可重現的 5,000 筆簡體 → 台灣繁體 benchmark 中，準確率與錯轉率皆優於主要開源競品；因此可稱為目前此場景下最準確的開源轉換器之一。

避免單獨使用沒有上下文的：

> zhtw 是市面上最準的簡繁轉換器。

## 風險與防護

| 風險 | 防護 |
|------|------|
| 為了追 accuracy 過度加詞 | 每個詞庫修改必須有 regression 與 identity mapping 檢查 |
| benchmark 被調參污染 | blind holdout 開發時不可看 expected |
| expected 太主觀 | 多審核者 + acceptable variants + 分歧紀錄 |
| 競品版本變動 | 每次報告記錄版本與 dataset hash |
| 行銷宣稱過度 | README 使用宣稱階梯，不跳到「市面最準」 |
| 授權污染 | 競品詞庫只比較，不匯入 |

## 第一個實作切片

下一步先做 M1 的前半段：

1. 從 `docs/reports/competitor-advantage-review-2026-07-03.md` 選 10-15 筆保護案例。
2. 加入 `benchmarks/precision_cases.json`，risk 設為 `over_conversion_guard`。
3. 補測試確保 zhtw 符合 expected。
4. 不改詞庫。
5. 跑：

```bash
uv run python scripts/competitor_benchmark.py --format json --fail-on-zhtw-mismatch
uv run python -m pytest tests/test_competitor_benchmark.py -q
uv run zhtw validate
```

完成後再規劃 1,000 筆公開 regression 擴充。
