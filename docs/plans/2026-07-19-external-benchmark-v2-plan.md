<!-- zhtw:disable -->
# 外部 Benchmark 與 Blind-v2 準確度評測計畫

日期：2026-07-19

狀態：proposed

關聯計畫：`docs/plans/2026-07-04-market-best-accuracy-plan.md`

## 1. 背景與決策

目前 `blind-v1` 仍可作為固定 evaluation set 與歷史版本的 like-for-like 比較，
但不能繼續支撐 fresh-blind 或「市場最準」宣稱，原因如下：

- `docs/reports/accuracy-benchmark-2026-07-19.json` 已公開完整 rows，包括 expected、
  acceptable variants 與各引擎輸出。
- 開發過程已多次檢視 `blind-v1` misses，部分案例也依既定政策移出 sealed pool、
  修正後轉為 public regression。
- 最新報告只執行 zhtw，競品 lockfile 仍為 `draft`，不能視為正式市場排名。
- 現行單一總準確率無法充分呈現「寧可少轉，不要錯轉」的非對稱風險。

因此採用以下決策：

1. 將 `blind-v1` 正式標示為 **published evaluation benchmark**。
2. 外部公開資料分成獨立 tracks，不混成一個無法解釋的總分。
3. 新建 `blind-v2` 作為未曝光 expected 的 fresh generalization track。
4. 詳細 benchmark rows 一律留在 gitignored private output；版控只收 aggregate。
5. 市場比較必須使用完全相同的 inputs、normalization、執行環境與鎖定競品版本。

## 2. 目標與非目標

### 2.1 目標

- 引入可合法重現的外部公開資料，降低只使用專案自建語料的偏差。
- 分別評估字形／上下文、臺灣地域術語、錯轉防禦與真實泛化能力。
- 建立不會意外公開 private expected 或 converter output 的 runner。
- 讓每份正式報告可追溯至資料 revision、sha256、zhtw commit 與競品版本。
- 產出足以支持「在指定 benchmark 與指定競品中表現最佳」的範圍限定證據。

### 2.2 非目標

- 不宣稱涵蓋所有繁體中文地區、所有文體或所有商業線上工具。
- 不把 LLM 理解 benchmark（例如 TMMLU+）當成簡繁轉換 benchmark。
- 不從 OpenCC、zhconv 或外部 benchmark 自動匯入詞庫。
- 不以公開 benchmark 的改善取代 fresh `blind-v2` 泛化結果。
- 不為提高總分而降低 identity、idempotency 或 P0/P1 安全標準。

## 3. Benchmark Tracks

### Track A：UD-GSD 外部句級字形與上下文

來源：

- UD Chinese GSD（Traditional）
- UD Chinese GSDSimp（Simplified）
- 官方說明：<https://universaldependencies.org/treebanks/zh_gsdsimp/>
- 授權：CC BY-SA 4.0
- 已知規模：4,997 sentences、123,289 tokens（以鎖定 revision 實測為準）

用途：

- 完整句 exact match。
- 字元／edit-span precision、recall 與 F1。
- 一簡多繁、專名、混合英數與長句上下文。
- idempotency。

限制與揭露：

- GSDSimp 最初由 OpenCC 轉換，再經人工修正，對 OpenCC 可能有來源偏差。
- 來源 genre 是 wiki，不代表臺灣 IT、UI、社群或正式文件分布。
- 此 track 只能列為 external compatibility，不得單獨決定競品總排名。

匯入要求：

- 以 `sent_id` 對齊兩個 treebanks，不用檔案列號猜測配對。
- 從 CoNLL-U `# text` 取得原句；若缺少或重複 `sent_id` 必須 fail closed。
- 固定 upstream release/tag、commit SHA、下載 URL 與檔案 sha256。
- 保存授權、attribution 與 importer 版本。

### Track B：國教院兩岸對照術語

第一批來源：

- 計算機學術名詞：<https://data.gov.tw/dataset/15275>
- 地球科學名詞：<https://data.gov.tw/dataset/15249>
- 物理教科書名詞：<https://data.gov.tw/en/datasets/15318>
- 數學教科書名詞：<https://data.gov.tw/en/datasets/15444>
- 授權：政府資料開放授權條款第 1 版；仍須在 manifest 記錄每個 dataset 的實際
  metadata 與下載日期。

用途：

- 中國大陸譯名 → 臺灣中文名稱的 term conversion coverage。
- 臺灣中文名稱 → identity preservation。
- IT、科學、醫療等專業領域分數。

資料處理原則：

- `中文名稱` 與 `中國大陸譯名` 都非空且語義對齊才可成為候選。
- 多值、同義詞、括號註記、縮寫與大小寫差異先結構化，不用字串切割硬猜。
- 大陸詞與臺灣詞完全相同者列入 baseline/identity，不列為 conversion hit。
- 裸詞有多義風險者不得直接當唯一 expected，必須建立句級語境。
- 句級語境依 Codex → Gemini 獨立 advisory → maintainer confirmation 流程確認。
- 公開資料與衍生 expected 可進 public benchmark，但不能直接進詞庫。

### Track C：SC-TC-Bench 地域詞概念

來源：

- 論文：<https://arxiv.org/abs/2505.22645>
- Repository：<https://github.com/brucelyu17/SC-TC-Bench>
- 已知範圍：110 組地域詞概念；實際檔案授權與 revision 必須在導入前確認。

用途：

- 通訊、交通、居住、消費等生活地域詞。
- 補足國教院偏學術術語的分布。

限制：

- 原始任務是 LLM regional term choice，不是 deterministic conversion。
- 不直接沿用 LLM prompt 分數。
- 只採可追溯的概念／詞對；改造成轉換句後必須重新人工確認 expected。
- 若 repository 未提供可接受的資料授權，停止導入，不以論文 CC 授權推定資料授權。

### Track D：Blind-v2 Fresh Generalization

目的：支撐下一次真正未曝光的能力比較。

第一版規模：600 句；之後擴充至 1,200 句。

建議分布：

| Domain | 比例 | 600 句目標 |
|---|---:|---:|
| IT / API / CLI | 25% | 150 |
| UI / i18n | 20% | 120 |
| LLM 生成內容 | 15% | 90 |
| 正式文件 / 新聞 | 15% | 90 |
| 社群 / 日常 | 15% | 90 |
| 法律 / 財經 / 醫療 | 10% | 60 |

Risk strata 每個 domain 都要包含：

- `candidate_gap`：應轉換的中國用語或簡體歧義。
- `over_conversion_guard`：正確臺灣詞、專名或多義詞不得改壞。
- `baseline_guard`：一般字形與不需地域改寫的句子。

審核流程：

1. Codex 先做 expected、acceptable、風險與理由建議。
2. Gemini 只看 input 與標註規則，獨立 advisory，不看 Codex/zhtw/競品輸出。
3. Codex 彙整一致、差異、低信心與高風險案例。
4. Maintainer 只需確認差異、高風險與語境不明案例；最後寫入 human decision。
5. Metadata 誠實標示 `single_human_with_ai_advisory`，不可宣稱雙 human blind review。

防洩漏規則：

- `blind-v2.inputs.json` 可公開 input-only，不能含 expected、acceptable、annotation。
- `blind-v2.expected.json` 必須 gitignored，並保存 inputs sha256。
- 第一次正式測試前，不執行任何 converter output 對照 expected。
- 一旦 maintainer 因調詞需要查看某筆詳細 miss，該案例先移出 blind-v2，建立 public
  regression candidate 後才可修正。
- 對外只發布 aggregate 時，blind-v2 仍可保留為 sealed；若發布任何 case-level
  expected/output，該版本立即降級為 published evaluation set。

## 4. Runner 與資料架構

### 4.1 建議目錄

```text
benchmarks/accuracy/
  manifests/
    ud-gsd-v1.json
    naer-terms-v1.json
    sc-tc-regional-v1.json
    blind-v2.json
  external/
    ud-gsd-v1.json
    naer-terms-v1.json
    sc-tc-regional-v1.json
  blind-v2.inputs.json
  blind-v2.expected.schema.json
  competitors.lock.json
scripts/
  import_ud_gsd_benchmark.py
  import_naer_terms_benchmark.py
  import_sc_tc_regional_benchmark.py
  run_accuracy_benchmark.py
  audit_benchmark_publication.py
```

外部 raw data 不一定提交；依授權與檔案大小決定。無論是否提交，都要能由 manifest
與 importer 重建相同 normalized dataset。

### 4.2 Dataset manifest 必填欄位

```json
{
  "id": "ud-gsd-v1",
  "track": "external_context",
  "source_urls": [],
  "upstream_revision": "",
  "retrieved_at": "",
  "license": "",
  "license_url": "",
  "raw_sha256": {},
  "normalized_sha256": "",
  "importer": "scripts/import_ud_gsd_benchmark.py",
  "known_biases": [],
  "allowed_uses": ["evaluation", "public_reporting"],
  "tuning_policy": "public_track_only"
}
```

缺少 revision、license 或 hash 時，正式 runner 必須拒絕執行該 track。

### 4.3 執行 provenance

正式報告必須記錄：

- zhtw package version。
- Git commit SHA 與 dirty state。
- Python、Node、Rust、OS 與架構。
- runner 版本／commit。
- 每個 dataset manifest hash。
- private expected hash，但 aggregate report 不記 private path 以外的內容。
- 每個 competitor 的 package、version、source/config hash 與 exact command。

若 zhtw metadata version 與 `src/zhtw/__init__.py`／`pyproject.toml` 不一致，正式模式
必須 fail closed。

### 4.4 Public 與 private output

Runner 增加兩種明確模式：

- `--report-mode aggregate`：預設；可提交 Git，只含分布、分數、CI、hash、版本與
  不可反推出 expected 的統計。
- `--report-mode detailed --output <ignored-path>`：僅本機審查，包含 rows、expected、
  acceptable 與 output；目的地若是 tracked path 必須拒絕。

新增 publication audit，至少檢查：

- tracked benchmark report 不得含 `rows`、`expected`、`acceptable`、`output`、
  `normalized_output` 或 case-level annotation。
- private expected patterns 必須持續被 `.gitignore` 命中。
- aggregate 報告不得列 miss case ID，避免逐案反推 sealed signal。

## 5. 評分與統計

### 5.1 每個 track 都要報告

- `accepted_accuracy`：符合 primary expected 或人工確認 acceptable。
- `primary_exact_accuracy`。
- `idempotency_rate`。
- `macro_domain_accuracy`：各 domain accuracy 等權平均。
- `micro_accuracy`：所有案例等權平均，僅作補充。
- 95% confidence interval。
- unavailable/error cases；不可從分母靜默排除。

### 5.2 依風險拆分

- `conversion_recall`：candidate_gap 中該轉而成功轉換的比例。
- `over_conversion_guard_accuracy`：應保留案例未被改壞的比例。
- `baseline_guard_accuracy`。
- `severe_error_rate`：P0/P1 錯誤比例。

zhtw 的核心產品原則以 guard accuracy 與 P0/P1 為優先；不得只用 conversion recall
掩蓋錯轉。

### 5.3 Changed-span 指標

UD 與句級外部 track 增加 source → expected 的 edit alignment：

- required edits correctly produced：recall。
- output 額外產生但 expected 不需要的 edits：over-conversion precision penalty。
- edit-span F1。

Alignment 必須使用可測試的 sequence alignment，不以逐字 zip 比較不同長度字串。

### 5.4 競品差異顯著性

- 同一批 paired cases 使用 paired bootstrap CI 或 McNemar test。
- 同時報 absolute delta 與 95% CI。
- 差距落在 CI 內時標示 `statistical_tie`，不得宣稱勝出。
- 預先固定 ranking policy，看到結果後不得更換主指標。

## 6. 競品鎖定與公平執行

第一階段正式競品：

- zhtw。
- OpenCC `s2twp`。
- zhconv `zh-tw`。
- opencc-js `cn -> twp`。
- zhconv-rs：只有 exact CLI/config 可固定後才納入。

要求：

- 使用隔離 container 或可重建 lock environment。
- 禁止使用浮動 `latest`。
- 每個 adapter 有 smoke test、version probe、timeout 與 nonzero exit handling。
- 任一正式競品 unavailable 時，market comparison 必須 fail，不得以 skipped 報告排名。
- 同源實作（例如不同 OpenCC binding）需標示 engine family，不能當成多個獨立競品
  放大證據。
- 線上工具若無固定 API/version/config，只能放 appendix manual snapshot。

## 7. 實作階段

### Phase 0：修正 benchmark 安全與語意（P0）

- [ ] 將 `blind-v1` metadata/docs 改為 published evaluation。
- [ ] Runner 預設改為 aggregate-only。
- [ ] detailed output 強制寫入 ignored path。
- [ ] 新增 publication audit 與 regression tests。
- [ ] 修正 zhtw 版本／commit provenance，版本不一致時 fail closed。
- [ ] 修正現有文件中「sealed」與實際審核 protocol 不一致之處。

完成條件：任何 tracked report 都無法讀到 private expected 或 case-level output。

### Phase 1：資料 manifest 與共用評分核心（P0）

- [ ] 定義 manifest schema 與 validation。
- [ ] 將 micro、macro、risk-stratified、idempotency 指標加入 runner。
- [ ] 實作 changed-span alignment 與單元測試。
- [ ] 實作 paired comparison、CI 與 statistical tie。
- [ ] 報告 unavailable/error 分母政策。

完成條件：固定 fixture 可重現相同 JSON、hash 與統計結果。

### Phase 2：導入外部公開 tracks（P1）

- [ ] UD GSD/GSDSimp 授權與 revision audit。
- [ ] 實作 UD importer，驗證 4,997 sentence pairs 或記錄 upstream 差異。
- [ ] 國教院 datasets 授權、欄位與下載 URL audit。
- [ ] 先導入計算機名詞，再擴充其他領域。
- [ ] 建立 term identity 與 context candidate packet。
- [ ] SC-TC-Bench repository 資料授權確認。
- [ ] 授權通過後建立 regional-term candidate packet；否則記錄 blocked。

完成條件：三個 track 各有 manifest、來源 attribution、固定 hash、測試與限制說明。

### Phase 3：鎖定競品環境（P1）

- [ ] `competitors.lock.json` 從 draft 升為可重建格式。
- [ ] 固定 OpenCC、zhconv、opencc-js 版本與 config hash。
- [ ] 評估並固定 zhconv-rs；無法重建則正式排除並說明。
- [ ] 建立 container/lock bootstrap 與 adapter conformance tests。
- [ ] 正式模式啟用 `fail-on-unavailable`。

完成條件：乾淨環境可一鍵重建並產生一致 version probes。

### Phase 4：建立 Blind-v2（P1）

- [ ] 建立 input-only schema、expected schema 與 leakage tests。
- [ ] 收集第一批 600 筆且符合 domain/risk quotas。
- [ ] 執行 Codex first pass。
- [ ] 執行 Gemini independent advisory。
- [ ] 產生差異與 maintainer review packet。
- [ ] Maintainer confirmation 後寫入 private expected。
- [ ] 封存 inputs、expected 與 protocol hash，再執行第一次 benchmark。

完成條件：600/600 human decisions 完成，來源標示誠實，第一次執行前無 converter
output 接觸 expected。

### Phase 5：正式比較與發布（P1）

- [ ] 在不可變 zhtw tag/commit 上執行所有 tracks。
- [ ] 產生 aggregate-only public report 與 private detailed audit。
- [ ] 驗證所有競品可用、版本相符、case count 相同。
- [ ] 完成統計顯著性與 error taxonomy review。
- [ ] Maintainer review 報告措辭與宣稱範圍。
- [ ] 第三方依公開 manifest 重跑 external tracks。

完成條件：公開報告可重現、不洩漏 blind-v2 expected，且宣稱只涵蓋實際測試方向、
資料與競品。

## 8. 測試與 CI

新增或擴充測試：

- `tests/test_accuracy_holdout.py`：blind-v2 schema、hash 與 leakage。
- `tests/test_accuracy_benchmark.py`：aggregate/detailed mode、provenance、metrics。
- `tests/test_benchmark_manifests.py`：license/revision/hash 必填與 normalized freshness。
- `tests/test_benchmark_publication.py`：掃描 tracked reports 的敏感欄位。
- importer fixture tests：不依賴網路即可測 parsing 與 fail-closed 行為。

CI 分層：

- 每次 PR：schema、fixture、publication audit、public track regression。
- 排程／手動：下載 upstream 並驗證 revision/hash，不自動追最新。
- 正式 benchmark：手動 workflow，指定 immutable zhtw ref 與 competitor lock hash。
- release gate 不執行 private blind-v2 詳細 benchmark，避免 CI logs/artifacts 洩漏。

## 9. 發布宣稱規則

完成 external tracks 但尚未完成 blind-v2 時，可說：

> 在指定版本的公開 UD、國教院衍生術語與地域詞 benchmark 上，zhtw 的結果為
> X；完整版本、資料 hash 與競品配置見報告。

完成 blind-v2 且差異具統計意義時，可說：

> 在「簡體中文 → 臺灣繁體」的指定 600 筆 fresh benchmark，以及列出的主要開源
> 競品版本中，zhtw 的 accepted accuracy／過度轉換防禦率最高。

不能說：

- 「所有簡繁轉換器中最準」。
- 「臺灣繁中 99% 準確」但不說資料、領域與分母。
- 差異未達統計顯著仍說明顯勝出。
- 把 public regression 100% 當 fresh generalization。

## 10. Definition of Done

- [ ] `blind-v1` 不再被描述為 fresh sealed benchmark。
- [ ] tracked reports 皆為 aggregate-only，publication audit 全綠。
- [ ] 每個外部 track 有授權、revision、hash、attribution 與 known bias。
- [ ] runner 記錄 zhtw commit/dirty/version，且版本矛盾時中止。
- [ ] 至少 UD 與國教院兩個外部 tracks 可離線重現評分。
- [ ] 正式競品版本與 config 全部鎖定，不允許 unavailable 被忽略。
- [ ] 報告包含 macro/micro、risk strata、idempotency、CI 與 paired delta。
- [ ] blind-v2 第一版 600 筆完成 maintainer human decision。
- [ ] 公開報告未洩漏 blind-v2 expected、output、miss IDs 或詳細 rows。
- [ ] 宣稱文字經 maintainer 確認且不超出 benchmark 證據。

## 11. 建議交付拆分

1. **Benchmark safety**：aggregate-only、publication audit、blind-v1 reclassification。
2. **Metrics and provenance**：manifest、macro/risk metrics、Git/version provenance。
3. **UD external track**：importer、license、hash、report。
4. **NAER terminology track**：計算機先導、context review、identity guards。
5. **Competitor environment**：locked adapters 與 reproducible runner。
6. **Blind-v2 collection**：600 筆收集、AI advisory、maintainer decisions。
7. **Formal report**：統計比較、第三方重現與範圍限定宣稱。

每一項獨立提交、獨立測試；不得等全部完成後才一次審查。
