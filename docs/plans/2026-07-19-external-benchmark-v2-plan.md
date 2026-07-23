<!-- zhtw:disable -->
# 外部 Benchmark 與 Blind-v2 準確度評測計畫

日期：2026-07-19

狀態：reviewed / execution-ready

關聯計畫：`docs/plans/2026-07-04-market-best-accuracy-plan.md`

本文件是 benchmark v2 的執行規格，**取代**舊計畫中的 benchmark 分層、sealed
holdout、人工標註、指標、runner 與市場宣稱章節。舊計畫只保留歷史背景與產品目標；
兩份文件衝突時，以本文件為準。

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

第一版最低規模為 600 句；正式 N 由預先登記的 paired power analysis 決定，不設
1,200 句硬上限。下表是 600 句基準配額；N 增加時依相同比例分層配置並以整數最佳化
保留 domain/risk 總數。

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

固定 risk 配額為 40% `candidate_gap`、40% `over_conversion_guard`、20%
`baseline_guard`，每個 domain 都使用相同比例：

| Domain | candidate | over-conversion | baseline | Total |
|---|---:|---:|---:|---:|
| IT / API / CLI | 60 | 60 | 30 | 150 |
| UI / i18n | 48 | 48 | 24 | 120 |
| LLM 生成內容 | 36 | 36 | 18 | 90 |
| 正式文件 / 新聞 | 36 | 36 | 18 | 90 |
| 社群 / 日常 | 36 | 36 | 18 | 90 |
| 法律 / 財經 / 醫療 | 24 | 24 | 12 | 60 |
| **Total** | **240** | **240** | **120** | **600** |

總體 micro accuracy 只代表這個預先登記的 challenge distribution，不宣稱是真實流量
盛行率；跨版本與跨競品必須使用相同權重。

#### Blind-v2 抽樣與污染防護

正式抽樣前先建立至少 `max(1,800, 3 × 正式 N)` 筆 input-only candidate pool，並遵守：

- 來源限 project-original、取得明確許可的使用者回報、public-domain 或 permissively
  licensed text；每筆保存 source class、citation/license 與建立日期。
- 任一單一來源不得超過 10%，任一 source class 不得超過 35%。
- 不得根據 zhtw、OpenCC、zhconv 或任何 converter output/miss 產生或篩選 input。
- 對 blind-v1、public regression、corpus、annotation backlog、public reproduction、
  詞庫完整句 source/target 做 exact normalization 去重。
- 以 Unicode NFC、空白正規化後的字元 5-gram Jaccard 做 near-duplicate 檢查；相似度
  `>= 0.85` 的群組只保留一筆，邊界案例由 maintainer 確認。
- 凍結 candidate pool hash 後，以固定 seed `20260719` 在 domain × risk strata 內抽樣；
  importer 必須能從相同 pool、seed 與正式 N 重建完全相同的 IDs。
- 抽樣後不得因任何 converter 表現替換案例；只允許因授權、重複、資料毀損或 expected
  無法裁決而排除，且 replacement 必須由同 stratum 的預先排序候補補入並留下 ledger。

正式固定資料集前執行 paired-proportion power analysis。以 80% power、雙尾
`alpha = 0.05` 為最低標準，預先假設／敏感度分析 competitor discordant rate，要求
可偵測差異（MDE）不高於 2 個百分點；正式 N 取 `max(600, required_cases)`，不得只因
標註成本而截斷至 1,200。以 discordant rate 10% 為例，normal approximation 約需
1,960 筆，600 與 1,200 均不足。報告必須說明 CI 是此 challenge sample 的不確定性，
不能推論所有真實流量。

審核流程：

1. Codex 先做 expected、acceptable、風險與理由建議。
2. Gemini 只看 input 與標註規則，獨立 advisory，不看 Codex/zhtw/競品輸出。
3. Codex 彙整一致、差異、低信心與高風險案例。
4. Maintainer 逐批查看所有 input/expected pairs；差異、高風險與語境不明案例逐筆裁決，
   Codex/Gemini 一致且低風險的案例可在完整 packet 上批次簽核。
5. Metadata 誠實標示 `single_human_with_ai_advisory`，不可宣稱雙 human blind review。

每個 batch final-decision artifact 必須列出所有 case ID、packet hash、決策方式
（`individual_adjudication` 或 `batch_human_confirmation`）、maintainer、日期與簽核摘要。
只有 final-decision artifact 明確涵蓋的案例才算 human decision；最終 N/N 都必須可稽核。

防洩漏規則：

- `blind-v2.inputs.json` 可公開 input-only，不能含 expected、acceptable、annotation。
- `blind-v2.expected.json` 必須 gitignored，並保存 inputs sha256。
- 第一次正式測試前，不執行任何 converter output 對照 expected。
- 一旦 maintainer 因調詞需要查看某筆詳細 miss，該案例先移出 blind-v2，建立 public
  regression candidate 後才可修正。
- 對外只發布 aggregate 時，blind-v2 仍可保留為 sealed；若發布任何 case-level
  expected/output，該版本立即降級為 published evaluation set。

#### Blind-v2 one-shot evaluation governance

- 在執行前提交 preregistration manifest：inputs hash、expected hash、候選 zhtw commit、
  competitor lock hash、normalization、primary endpoint、ranking policy 與 power result。
- 正式執行只允許 preregistered immutable commit；執行後才可讀 aggregate 結果。
- 建立 private `evaluation-ledger.jsonl`，記錄時間、操作者、原因、所有 hashes、exit
  status 與是否讀取 detailed rows。
- 同一 artifacts 的技術性重跑只限處理中斷，且所有 hashes 必須完全相同；不得更換
  程式碼、資料、競品或指標。
- 第一次看到任何分數後，blind-v2 對該發布候選即完成 one-shot 任務。若根據分數調整
  converter，調整後版本必須使用新的 blind-v3 才能稱為 fresh；blind-v2 只保留為
  monitoring/evaluation set。
- detailed rows 只有 maintainer 在決定將案例移出 sealed 時可讀；讀取行為必須入 ledger。

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
  "output_license": "",
  "attribution": "",
  "modification_notice": "",
  "raw_sha256": {},
  "normalized_sha256": "",
  "importer": "scripts/import_ud_gsd_benchmark.py",
  "known_biases": [],
  "allowed_uses": ["evaluation", "public_reporting"],
  "tuning_policy": "public_track_only"
}
```

缺少 revision、license、output license、attribution 或 hash 時，正式 runner 必須拒絕
執行該 track。

### 4.3 授權與發布義務

- 新增 `benchmarks/accuracy/LICENSES.md`，逐一記錄 upstream copyright、license、
  attribution、修改內容與衍生資料授權。
- UD 衍生 normalized dataset 依 CC BY-SA 4.0 發布，保留 attribution 與修改聲明。
- 國教院資料依政府資料開放授權條款第 1 版標示來源、更新日期與衍生處理；不得暗示
  國教院為 zhtw 背書。
- SC-TC-Bench 只有 repository 資料檔授權可確認且允許此用途時才能提交衍生資料。
- importer 產出的 manifest 必須帶入 attribution；publication audit 驗證對應 NOTICE
  存在，不能只靠人工記憶。

### 4.4 執行 provenance

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

### 4.5 Public 與 private output

Runner 增加兩種明確模式：

- `--report-mode aggregate`：預設；可提交 Git，只含分布、分數、CI、hash、版本與
  不可反推出 expected 的統計。
- `--report-mode detailed --output <ignored-path>`：僅本機審查，包含 rows、expected、
  acceptable 與 output；目的地若是 tracked path 必須拒絕。

Private benchmark 只能在 maintainer 控制的本機或無 artifact upload 的受控 self-hosted
runner 執行。GitHub-hosted Actions 不得取得 blind-v2 expected。Runner 在 private 模式
不得將 case-level input/expected/output 寫到 stdout/stderr；例外訊息只能含 aggregate
count 與 opaque run ID。

新增 publication audit，至少檢查：

- 禁止 JSONPath `$.rows`，以及任何 case-level object 中的 `expected`、`acceptable`、
  `output`、`normalized_output`、`annotation` 與 miss case ID。
- 允許頂層 `expected_sha256`，但禁止 private expected 的絕對路徑、檔名與內容。
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

正式模式中，整個 engine unavailable 會使 run 失敗；個別 case timeout、exception、
invalid encoding 或空輸出一律計為 miss 並保留 error category，不得從分母移除。

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
實作需固定 edit costs、Unicode unit 與 tie-break order，重複字元造成多個最短路徑時仍須
產生唯一結果；golden fixtures 必須涵蓋插入、刪除、替換與重複字元。

### 5.4 競品差異顯著性

- 同一批 paired cases 使用 paired bootstrap CI 或 McNemar test。
- 同時報 absolute delta 與 95% CI。
- 差距落在 CI 內時標示 `statistical_tie`，不得宣稱勝出。
- 預先固定 ranking policy，看到結果後不得更換主指標。

### 5.5 預先登記排名規則

正式 market comparison 不合併四個 tracks，也不產生跨資料集加權總分：

1. Blind-v2 是唯一 primary market endpoint；external tracks 是 secondary evidence。
2. 任一 P0 error 會使該 engine 標為 `safety_disqualified`，不得排名第一。
3. 合格 engines 以 Blind-v2 `accepted_accuracy` 比較，並使用 paired 95% CI。
4. zhtw 與最高競品的 paired delta CI 必須完全大於 0，才能宣稱 benchmark winner。
5. CI 包含 0 時標示 `statistical_tie`；不得再用其他指標改判勝負。
6. `over_conversion_guard_accuracy`、P1 count、macro domain、primary exact、changed-span
   F1 與 idempotency 均為必要 secondary metrics，用於解釋風險，不事後改成主指標。
7. External tracks 若與 Blind-v2 結論衝突，報告必須揭露，不能用挑選 track 隱藏。

## 6. 競品鎖定與公平執行

第一階段正式競品：

- zhtw。
- OpenCC `s2twp`。
- zhconv `zh-tw`。
- opencc-js `cn -> twp`。
- zhconv-rs：只有 exact CLI/config 可固定後才納入。

要求：

- 使用 digest-pinned container image；Dockerfile、base image digest、OS packages 與各語言
  lockfiles 都納入 competitor environment hash，不接受只有文字描述的「可重建環境」。
- 禁止使用浮動 `latest`。
- 每個 adapter 有 smoke test、version probe、timeout 與 nonzero exit handling。
- 任一正式競品 unavailable 時，market comparison 必須 fail，不得以 skipped 報告排名。
- 同源實作（例如不同 OpenCC binding）需標示 engine family，不能當成多個獨立競品
  放大證據。
- 線上工具若無固定 API/version/config，只能放 appendix manual snapshot。

## 7. 實作階段

### Phase 0：修正 benchmark 安全與語意（P0）

- [x] 將 `blind-v1` metadata/docs 改為 published evaluation。
- [x] Runner 預設改為 aggregate-only。
- [x] detailed output 強制寫入 ignored path。
- [x] 新增 publication audit 與 regression tests。
- [x] 修正 zhtw 版本／commit provenance，版本不一致時 fail closed。
- [x] 修正現有文件中「sealed」與實際審核 protocol 不一致之處。
- [x] 明確標示本計畫取代舊計畫的 benchmark 執行規格。

完成條件：任何 tracked report 都無法讀到 private expected 或 case-level output。

完成日期：2026-07-19；實作與驗證追蹤於 GitHub Issue #38。

### Phase 1：資料 manifest 與共用評分核心（P0）

- [x] 定義 manifest schema 與 validation。
- [x] 新增 `LICENSES.md`、attribution 與 output-license validation。
- [x] 將 micro、macro、risk-stratified、idempotency 指標加入 runner。
- [x] 實作 changed-span alignment 與單元測試。
- [x] 實作 paired comparison、CI 與 statistical tie。
- [x] 實作 sample-size/power analysis 與 preregistration schema。
- [x] 報告 unavailable/error 分母政策。

完成條件：固定 fixture 可重現相同 JSON、hash 與統計結果。

完成日期：2026-07-19；實作與驗證追蹤於 GitHub Issue #39。

### Phase 2：導入外部公開 tracks（P1）

- [x] UD GSD/GSDSimp 授權與 revision audit。
- [x] 實作 UD importer，驗證 4,997 sentence pairs 或記錄 upstream 差異。
- [x] 國教院 datasets 授權、欄位與下載 URL audit。
- [x] 導入計算機名詞先導資料；其他領域待先導結果審查後再擴充。
- [x] 建立 term identity 與 context candidate packet。
- [ ] SC-TC-Bench repository 資料授權確認。
- [ ] 授權通過後建立 regional-term candidate packet；否則記錄 blocked。

完成條件：三個 track 各有 manifest、來源 attribution、固定 hash、測試與限制說明。

國教院計算機名詞先導完成日期：2026-07-19；實作與驗證追蹤於 GitHub Issue #41。

### Phase 3：鎖定競品環境（P1）

- [x] `competitors.lock.json` 從 draft 升為可重建格式。
- [x] 固定 OpenCC、zhconv、opencc-js 版本與 config hash。
- [x] 評估並固定 zhconv-rs 0.4.1 `zh-TW` adapter，歸入 MediaWiki-derived family。
- [x] 建立 container/lock bootstrap 與 adapter conformance tests。
- [x] 正式模式對完整 locked engine set 啟用 fail-closed unavailable/version/config checks。

完成條件：乾淨環境可一鍵重建並產生一致 version probes。

完成日期：2026-07-19；本機 macOS/arm64 已重建並通過 probes，Ubuntu/amd64 由
`benchmark-competitors.yml` 重建驗證；實作追蹤於 GitHub Issue #42。

### Phase 4：建立 Blind-v2（P1）

- [x] 建立 input-only schema、expected schema 與 leakage tests。
- [x] 固定並匯入 FLORES-200 zho_Hans（2,009 筆）與 UD Chinese-CFL（451 筆）
  input-only source pilots；尚未填 domain/risk，亦未使用 converter output。
- [x] 稽核 2026-07-18 Tatoeba Mandarin CC0 snapshot；僅 1 筆且內容格式錯誤，
  依來源品質 gate 拒絕，不以 CC BY／翻譯句替代。
- [x] 逐項核實並匯入 CDC Stacks `cdc:111808`、`cdc:120024`、`cdc:116683`；
  以原始 PDF checksum 與保守的 pypdf 句界抽取固定 62 筆 `public_domain`
  input-only candidates。舊 `cdc:154488` 會轉址，已改用 canonical `cdc:120024`。
- [x] CDC classification batch 003 已完成 Codex first pass、Gemini CLI
  independent advisory 與 maintainer confirmation：33 筆完全一致，29 筆差異於
  2026-07-22 全部採 Codex；61 筆納入、1 筆 malformed 排除。
- [x] 將 batch 003 的 61 筆 eligible inputs 寫入 `collecting` candidate pool；
  經 tracked-reference exact 與 character 5-gram Jaccard 0.85 near dedupe 後
  61 筆全數保留。此 partial pool 尚未達來源比例、strata 與 5,880 筆 ready gate。
- [x] 將 classification batches 001-003 合併重建 collecting pool；共 228 筆
  maintainer-confirmed eligible inputs，跨批／reference exact 與 near dedupe 均
  無排除。現有 domain 仍缺 `ui_i18n`、`llm_generated`。
- [x] 建立 project-original UI/i18n 與 LLM product input-only pilots，各 50 筆；
  原始檔明確標示 Codex 起草、非自然市場流量，且未使用 converter output 或
  expected。Classification batch 004 已完成 Codex first pass 與 Gemini CLI
  independent advisory：69 筆四欄完全一致，31 筆差異經 Codex synthesis 後由
  maintainer 於 2026-07-23 確認。100 筆全數通過 dedupe 並寫入 collecting
  pool；pool 現為 328 筆，六個 domain 均已有覆蓋，距最低 5,880 筆仍差 5,552。
- [x] 固定 MASSIVE 1.0 `zh-CN` archive checksum 與 CC BY 4.0 attribution，從
  16,521 筆原始列建立 15,619 筆唯一 input-only pilot；未匯入 intent、slot、worker、
  judgment、converter output 或 expected。Classification batch 005 以獨立的
  `selection_round=1` 抽取 100 筆，已完成 Codex first pass、Gemini independent
  advisory 與 Codex synthesis：35 筆完全一致、65 筆有欄位差異，建議 98 筆納入、
  2 筆排除。Maintainer 於 2026-07-23 整批確認 synthesis；98 筆全數通過 dedupe
  並寫入 collecting pool。Pool 現為 426 筆，距最低 5,880 筆仍差 5,454。
- [x] 建立 project-original IT/API/CLI input-only pilot 100 筆，補強目前僅 9 筆的
  domain 缺口；來源明確標示 Codex 起草與 synthetic coverage，未使用 converter
  output 或 expected。Classification batch 006 已完成 Codex first pass、Gemini CLI
  independent advisory 與 Codex synthesis：58 筆完全一致、42 筆欄位差異，建議
  100 筆皆 eligible；第二輪 Codex 逐筆複核後 risk 為 82 candidate-gap、8
  over-conversion guard、10 baseline。Maintainer 於 2026-07-23 確認修正版
  synthesis；100 筆全數通過 dedupe 並寫入 pool。Pool 現為 526 筆，距最低
  5,880 筆仍差 5,354。
- [x] 建立 project-original formal/LLM semantic input-only pilot 100 筆：正式文字
  與 LLM 語義保留情境各 50 筆。來源明確標示 Codex 起草與 synthetic coverage，
  未執行任何 converter，也未建立 expected；raw 與 normalized snapshot 均以
  SHA-256 固定。Codex 與 Gemini via Antigravity CLI 已完成 100/100 independent
  classification：57 筆四欄一致、43 筆差異；Codex synthesis 建議 100 筆皆
  eligible，selection basis 為 agreement 57、Gemini 24、Codex 16、Codex
  field-level synthesis 3。Maintainer 於 2026-07-24 確認完整 synthesis；100 筆
  全數通過 exact/reference 與 character 5-gram Jaccard 0.85 promotion gate 並
  寫入 pool。Pool 現為 1,081 筆，距最低 5,880 筆仍差 4,799。
- [x] 稽核 FTC 官方簡體中文《Scams and Your Small Business》PDF 與 FTC
  public-domain policy，固定原始 checksum，保守抽取 81 筆完整 input-only 句子；
  排除圖片、印章、第三方內容、導覽、電話操作與版面碎片。Classification batch
  007 已完成 Codex first pass、Gemini independent advisory 與 Codex synthesis：
  53 筆完全一致、28 筆欄位差異，建議 55 筆納入、26 筆因缺少可獨立指涉而排除。
  Maintainer 於 2026-07-23 確認 synthesis；55 筆全數通過 dedupe 並寫入 pool。
  Pool 現為 581 筆，距最低 5,880 筆仍差 5,299。
- [x] 稽核 NPS 官方簡體中文 *Essential Acadia* HTML 與 NPS public-domain
  policy，固定原始 checksum，僅抽取 article content 內 32 筆完整句子；排除導覽、
  圖片、標誌、英文標籤、無完整句子的 URL 尾段與截斷內容。Classification batch
  008 已完成 Codex first pass、Gemini independent advisory 與 Codex synthesis：
  7 筆完全一致、25 筆欄位差異，建議 30 筆納入、2 筆排除。Maintainer 於
  2026-07-23 確認 synthesis；30 筆全數通過 dedupe 並寫入 pool。Pool 現為
  611 筆，距最低 5,880 筆仍差 5,269。
- [x] 稽核並固定 Ready.gov `earthquakes`、`floods`、`hurricanes` 三個官方
  `zh-hans` 頁面；每頁使用獨立 source ID、manifest、原始 HTML checksum 與
  normalized checksum，僅抽取 FEMA 撰寫的主要文字，排除導覽、URL、電話、圖片、
  標誌及第三方內容。共建立 154 筆 input-only candidates。
- [x] 以三來源等量 deterministic selection 建立 classification batch 009 共
  100 筆，完成 Codex first pass、Gemini CLI independent advisory 與 Codex
  synthesis：68 筆四欄完全一致、32 筆差異；綜合建議 86 筆納入、14 筆來源品質
  排除。Gemini 100/100 ID 覆蓋、零工具呼叫、零 API 錯誤。
- [x] Maintainer 於 2026-07-23 確認 batch 009 synthesis，建立 human decision
  artifact 並完成 exact/near dedupe promotion：86 筆 eligible 中 85 筆寫入 pool；
  `floods/sentence-045` 與 `earthquakes/sentence-047` 完全重複而排除。Pool 現為
  696 筆，距最低 5,880 筆仍差 5,184。
- [x] 稽核 OSHA 官方簡體中文出版品清單與 DOL reuse policy，固定七份 OSHA
  PDF 的原始 checksum；以指定中文頁面、標題與 corporate author fail-closed
  驗證後，保守抽取 185 筆 input-only candidates。排除英文頁、URL、電話、頁面
  元件、圖片、標誌與具名第三方見證內容。
- [x] 以七個獨立 OSHA source IDs 等量 deterministic selection 建立
  classification batch 010 共 100 筆，完成 Codex first pass、Gemini CLI
  independent advisory 與 Codex synthesis：41 筆四欄完全一致、59 筆差異；
  綜合建議 85 筆納入、15 筆來源品質排除。Gemini 100/100 ID 覆蓋、零工具
  呼叫、零 API 錯誤。
- [x] Maintainer 於 2026-07-24 確認 batch 010 synthesis，建立 human decision
  artifact 並完成 exact/near dedupe promotion；85 筆 eligible 全數寫入 pool。
  Pool 現為 781 筆，距最低 5,880 筆仍差 5,099。
- [x] 固定 Microsoft `vscode-loc` commit、MIT license、原始 JSON checksum 與
  normalized checksum；從 18,290 筆預篩訊息移除 2,672 筆來源內 exact duplicate，
  建立 15,618 筆唯一 input-only candidates。來源屬產品在地化翻譯，僅作 UI／IT
  覆蓋，不宣稱為自然市場頻率。
- [x] 以 deterministic selection round 1 建立 batch 011 共 100 筆，完成 Codex
  first pass、Gemini CLI 0.52.0 (`gemini-2.5-pro`) independent advisory 與 Codex
  synthesis：35 筆四欄完全一致、65 筆差異。Gemini 100/100 ID 覆蓋、零工具
  呼叫、零 API 錯誤。
- [x] Maintainer 於 2026-07-24 確認 batch 011 全部 100 筆 eligible，並明確修正
  四筆：三筆臺灣可接受用語改列 `baseline_guard`；`Web 视图` 因非臺灣用法保留為
  `candidate_gap`。最終 synthesis 為 agreement 35、Codex 57、Gemini 4、maintainer
  adjustment 4。100 筆全數通過 exact/reference 與 character 5-gram Jaccard 0.85
  promotion gate。Pool 現為 881 筆，距最低 5,880 筆仍差 4,999。
- [x] 固定 FTC public-domain 簡體中文 *Heads Up: Stop. Think. Connect.* PDF
  checksum 與 author/page/title anchors；保守抽取 117 筆完整 input-only 句子，
  排除英文平行內容、標題、頁面元件、URL、圖片與標誌。
- [x] 以 deterministic selection round 1 建立 batch 012 共 100 筆，完成 Codex
  first pass、Gemini CLI 0.52.0 (`gemini-2.5-pro`) independent advisory 與 Codex
  synthesis：49 筆四欄完全一致、51 筆差異。Gemini 100/100 ID 覆蓋、零工具
  呼叫、零 API 錯誤。
- [x] Maintainer 於 2026-07-24 確認 batch 012 全部 100 筆 eligible，並明確將
  `优惠卷 → 優惠券` 列為 `candidate_gap`，因正確臺灣繁體需要詞彙正規化而非
  直轉 `優惠卷`。最終 synthesis 為 agreement 49、Codex 50、maintainer
  adjustment 1。100 筆全數通過 exact/reference 與 character 5-gram Jaccard 0.85
  promotion gate。Pool 現為 981 筆，距最低 5,880 筆仍差 4,899。
- [x] 建立 permissioned-user-report 收集管線與第一批 100 筆空白模板：GitHub
  issue form 要求提交者確認原創／授權、CC0、公開再散布、無敏感資料與 input-only；
  schema 只接受公開 issue provenance，禁止 expected／converter output，並攔截重複
  input 與常見敏感資料。收集狀態可在未滿 100 筆時驗證，但 importer 與 ready gate
  均要求恰好 100 筆。偵測到敏感內容時拒絕並要求重送，不靜默改寫。目前 batch 001
  為 `collecting` 0/100，尚未加入目前 1,081 筆 candidate pool。
- [x] 檢查公開 `benchmark-user-report` issues；截至 2026-07-24 仍為 0 筆，沒有
  可合法代填或匯入的 permissioned input。
- [x] 固定 AOSP `platform/frameworks/base` commit
  `1cdfff555f4a21f71ccc978290e2e212e2f8b168` 與 Apache-2.0 檔頭；建立專用
  XML parser，保留 1,697 筆唯一單行簡體 framework UI inputs，排除 escaped
  multiline、URL、email、短非文字值與 138 筆 exact duplicates，且未執行
  converter 或建立 expected。
- [x] 建立 AOSP classification batch 014 共 100 筆，完成 Codex first pass、
  Gemini via Antigravity CLI independent advisory 與 Codex synthesis：75 筆
  完全一致、25 筆 domain/risk 差異；綜合建議 100 筆皆 eligible，selection
  basis 為 agreement 75、Codex 19、Gemini 5、Codex field-level synthesis 1。
- [ ] Maintainer 確認 batch 014 synthesis 後，才可建立 human decision artifact
  並執行 exact/near dedupe promotion；目前 pool 仍為 1,081 筆。
- [x] 建立 GitHub issue fail-closed 匯入器：預設只產生 dry-run preview，驗證表單
  sections、五項 consent、1–10 筆 input、公開 issue URL、容量、敏感資料與 normalized
  duplicate；只有 maintainer 確認並提供含時區 review timestamp 才原子寫入。每筆保存
  reviewer、decision 與 reviewed issue body SHA-256，不匯入 context。
- [ ] 從公開 permissioned-user-report issues 收滿 batch 001 的 100 筆原創簡體
  input；逐筆保留 issue URL 與 consent，人工確認自動敏感資料檢查沒有漏報後，才將
  狀態改為 `ready_for_import`。
- [x] 以 seed `20260719` 建立第一批 100 筆 input-only source classification
  packet（FLORES／UD-CFL 各 50 筆）。
- [x] 完成 classification batch 001 的 Codex first pass 與 Gemini independent
  advisory；60 筆四欄完全一致，40 筆差異由 maintainer 於 2026-07-21 全部採用
  Codex 建議；其餘 60 筆一致案例經 Codex 保守複核後，由 maintainer 於同日批次
  確認。第一批已完成 100/100 human decisions，並已透過可重現 promotion 寫入 pool。
- [x] 建立 classification batch 002 並完成 Codex first pass 與 Gemini CLI
  independent advisory；55 筆四欄完全一致，45 筆差異由 maintainer 於
  2026-07-21 全部採用 Codex。第二批已完成 100/100 human decisions，並已透過
  可重現 promotion 寫入 pool。
- [ ] 建立至少 `max(1,800, 3 × 正式 N)` 筆 candidate pool，完成來源、授權、
  exact/near dedupe audit。
- [ ] 凍結 pool hash，以 seed `20260719` 依固定 domain/risk quotas 抽樣。
- [ ] 完成 power analysis；正式 N 取 `max(600, required_cases)`，不得以 1,200 為硬上限。
- [ ] 執行 Codex first pass。
- [ ] 執行 Gemini independent advisory。
- [ ] 產生差異與 maintainer review packet。
- [ ] Maintainer confirmation 後寫入 private expected。
- [ ] 驗證 final decisions 明確涵蓋 N/N cases。
- [ ] 封存 inputs、expected、protocol 與 preregistration hash，再執行 one-shot benchmark。

完成條件：最終抽樣 N/N human decisions 完成，N 滿足預先登記的 power analysis，來源
標示誠實，第一次執行前無 converter output 接觸 expected。

### Phase 5：正式比較與發布（P1）

- [ ] 在不可變 zhtw tag/commit 上執行所有 tracks。
- [ ] Blind-v2 只在受控本機／self-hosted 環境執行並寫入 evaluation ledger。
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
- 公開 external benchmark：手動 workflow，指定 immutable zhtw ref 與 competitor lock hash。
- Private blind-v2：不得使用 GitHub-hosted runner；使用受控本機／self-hosted runner，
  禁止 artifact upload，且 workflow logs 不得包含 case-level data。
- release gate 不執行 private blind-v2 詳細 benchmark，避免 CI logs/artifacts 洩漏。

## 9. 發布宣稱規則

完成 external tracks 但尚未完成 blind-v2 時，可說：

> 在指定版本的公開 UD、國教院衍生術語與地域詞 benchmark 上，zhtw 的結果為
> X；完整版本、資料 hash 與競品配置見報告。

完成 blind-v2 且差異具統計意義時，可說：

> 在「簡體中文 → 臺灣繁體」的指定至少 600 筆（報告列出實際 N）fresh benchmark，
> 以及列出的主要開源
> 競品版本中，zhtw 的 accepted accuracy／過度轉換防禦率最高。

不能說：

- 「所有簡繁轉換器中最準」。
- 「臺灣繁中 99% 準確」但不說資料、領域與分母。
- 差異未達統計顯著仍說明顯勝出。
- 把 public regression 100% 當 fresh generalization。

## 10. Definition of Done

- [x] `blind-v1` 不再被描述為 fresh sealed benchmark。
- [x] tracked reports 皆為 aggregate-only，publication audit 全綠。
- [ ] 每個外部 track 有授權、revision、hash、attribution 與 known bias。
- [ ] `LICENSES.md` 與各衍生資料 output license 通過自動驗證。
- [x] runner 記錄 zhtw commit/dirty/version，且版本矛盾時中止。
- [x] 至少 UD 與國教院兩個外部 tracks 可離線重現評分。
- [x] 正式競品版本與 config 全部鎖定，不允許 unavailable 被忽略。
- [ ] 報告包含 macro/micro、risk strata、idempotency、CI 與 paired delta。
- [ ] Blind-v2 candidate pool、去重、固定抽樣與 power analysis 可重現。
- [ ] blind-v2 的正式 N 滿足 power analysis，且 N/N 完成 maintainer human decision。
- [ ] preregistration 與 evaluation ledger 證明正式比較是 one-shot frozen evaluation。
- [ ] GitHub-hosted Actions 無法存取 private expected。
- [ ] 公開報告未洩漏 blind-v2 expected、output、miss IDs 或詳細 rows。
- [ ] 宣稱文字經 maintainer 確認且不超出 benchmark 證據。

## 11. 建議交付拆分

| 順序 | Child Issue | 內容 | 依賴 |
|---:|---|---|---|
| 1 | [#38](https://github.com/rajatim/zhtw/issues/38) | Benchmark safety：aggregate-only、publication audit、blind-v1 reclassification | 無 |
| 2 | [#39](https://github.com/rajatim/zhtw/issues/39) | Metrics and provenance：manifest、license、macro/risk metrics、power、preregistration | #38 |
| 3 | [#40](https://github.com/rajatim/zhtw/issues/40) | UD external track：importer、license、hash、report | #39 |
| 4 | [#41](https://github.com/rajatim/zhtw/issues/41) | NAER terminology track：計算機先導、context review、identity guards | #39 |
| 5 | [#42](https://github.com/rajatim/zhtw/issues/42) | Competitor environment：digest-pinned adapters 與 reproducible runner | #39 |
| 6 | [#43](https://github.com/rajatim/zhtw/issues/43) | Blind-v2：candidate pool、固定抽樣、AI advisory、human decisions、one-shot ledger | #38、#39、#42 |
| 7 | [#44](https://github.com/rajatim/zhtw/issues/44) | Formal report：統計比較、第三方重現與範圍限定宣稱 | #38–#43 |

每一項獨立提交、獨立測試；不得等全部完成後才一次審查。
