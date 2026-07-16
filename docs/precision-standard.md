# zhtw 精準度標準

本文件定義 zhtw 的轉換精準度如何判斷、如何證明有進步，以及標準如何隨語料成長更新。

核心原則維持不變：

> 寧可少轉，不要錯轉。

## 精準度定義

zhtw 的「精準度」不是追求把所有可疑字詞都轉掉，而是：

- 人工確認的輸入，輸出必須符合台灣繁體 expected。
- 已經是正確台灣繁體的 target，不應被第二輪轉換改壞。
- 模糊詞不做裸詞全域轉換，除非有足夠明確的長詞語境。
- 匯入型大詞庫的數字只能當偵測來源，不能當硬 KPI。

因此，精準度改善必須能說明「修掉哪個人工確認錯轉」，不能只說「詞庫變大」或「某個報表數字下降」。

## 目前基線

截至 2026-06-27：

| 項目 | 基線 | 性質 |
|------|------|------|
| Golden battery | 247 句，且一次轉換與二次轉換都必須通過 | release gate |
| 精選 corpus | 500 筆人工 expected，且一次轉換與二次轉換都必須通過 | release gate |
| 手工詞庫 target 冪等性 | 0 issue | release gate |
| `zhtw validate` | 0 blocking issue | release gate |
| OpenCC 匯入詞庫 target 非冪等 | 403 issue | report-only |

OpenCC 匯入詞庫的 403 筆不是 release blocker。裡麵包含人名、古文、罕見詞與語境詞；硬追歸零會提高錯轉風險。最新盤點紀錄見 `docs/reports/opencc-idempotency-2026-06-27.md`。

## Release Gate

詞庫、轉換邏輯、匯出資料或 corpus 相關變更，release 前必須通過：

```bash
uv run zhtw validate
uv run python scripts/audit_idempotency.py --sources cn,hk --curated-only --fail-on-issues
uv run pytest tests/test_golden_rule_battery.py tests/test_corpus.py -q
uv run pytest -q
make test-java
```

涉及 SDK data 或版本時，還必須通過：

```bash
make export
make version-check
```

硬性標準：

- Golden battery 通過率必須是 100%。
- 精選 corpus 通過率必須是 100%。
- 手工詞庫 target 冪等 issue 必須是 0。
- `zhtw validate` 不得有 blocking issue。
- 已知 P0/P1 錯轉不得留到 release。

## 改善如何認定

一個精準度 commit 要同時滿足：

1. 修正至少一個人工確認的錯轉，來源可以是使用者回報、corpus diff、golden failure、官方用語或明確台灣用語。
2. 新增或更新 regression case，通常放在 `tests/test_golden_rule_battery.py` 或 `zhtw-test-corpus`。
3. 若 target 可能被第二輪轉換破壞，補 identity mapping。
4. 若詞條有子字串風險，補保護詞或負向案例。
5. 所有 release gate 維持全綠。

不能算改善的情況：

- 只增加詞庫數量，沒有人工確認 expected。
- 只降低 OpenCC report-only 數字，但修正項目語境不明。
- 把裸詞全域轉換成台灣用語，卻沒有負向案例保護另一個語義。
- 為了通過測試修改 expected，但沒有說明 expected 原本錯在哪。

## 問題分級

| 等級 | 定義 | Release 要求 |
|------|------|--------------|
| P0 | 會破壞正確台灣繁體、二次轉換改壞手工 target、或造成 CI gate 失敗 | 必修 |
| P1 | 常見使用場景錯轉，例如 IT、UI、新聞、正式文件中的高頻詞 | 必修或明確延期 |
| P2 | 領域詞、低頻但可確認的台灣用語 | 可排入批次修 |
| P3 | OpenCC 匯入詞庫中的人名、古文、罕見詞、語境模糊詞 | report-only |

每次 release 前，P0/P1 應為 0 個未處理項目。P2/P3 可保留，但要避免它們變成錯誤 KPI。

## 成長目標

短期目標：

- Golden battery 持續 100%。
- 精選 corpus 維持至少 500 筆人工 expected。
- `news`、`tech`、`social`、`wiki`、`regressions` 每類維持至少 100 筆人工 expected。
- 下一批擴充優先補 IT、CLI、正式文件與社群語氣，每批新增後都必須維持 100% 通過。
- 手工詞庫 target 冪等性維持 0 issue。

中期目標：

- 精選 corpus 朝 750 筆擴充，持續覆蓋常見 IT、CLI、文件、新聞、社群語氣。
- 每個使用者回報都新增 regression case。
- 大型語料 audit 只用來找候選問題，不直接當 expected。

長期目標：

- 精選 corpus 至少 1000 筆人工 expected。
- 各 SDK 透過 shared `golden-test.json` 保持 byte-for-byte parity。
- 對主要場景宣稱品質時，必須附上當時 corpus 版本、case 數與 gate 結果。

不設定「OpenCC issue 必須歸零」這種目標。剩餘 OpenCC issue 只在高信心、可解釋、可測試時處理。

## 標準如何更新

標準應隨時間變嚴格，主要透過增加人工 expected，而不是放寬 gate。

更新規則：

- 新增真實錯轉回報時，先補 golden 或 corpus case，再修詞庫。
- 如果 corpus expected 錯了，修 corpus expected，並說明理由；不要為了錯 expected 修改 converter。
- corpus 樣本增加後，新的 100% 通過率就是下一版 baseline。
- 可以新增 gate 或提高門檻；降低門檻必須有明確紀錄與 maintainer 同意。
- `zhtw-test-corpus` 在 CI 取最新精選 samples，代表標準會隨人工校驗語料自然更新。

## 競品 Benchmark

競品只用來找候選問題，不作為 expected 來源，也不要求 zhtw 與競品輸出一致。預設工具：

```bash
uv run python scripts/competitor_benchmark.py
make precision-benchmark
```

工具會讀取 `benchmarks/precision_cases.json` 的人工標註 expected，並比較：

- `zhtw`：必跑，必須符合人工 expected。
- `opencc-s2twp`：若本機有安裝 OpenCC Python binding 才跑。
- `zhconv-zh-tw`：若本機有安裝 zhconv 才跑。

分類原則：

- `candidate_gap`：競品符合 expected、zhtw 不符合。這是候選改善，但仍要人工確認與補 regression。
- `zhtw_advantage`：zhtw 符合 expected、競品不符合。這通常代表少錯轉優勢或保護詞有效。
- `zhtw_miss`：zhtw 不符合 expected，且目前競品也沒提供可直接採用的答案。這是人工排查項。
- `all_match`：zhtw 與所有可用競品都符合 expected。
- `zhtw_only`：只跑 zhtw，常見於未安裝競品套件的環境。

競品 benchmark 產出的任何詞條都不能直接進詞庫；仍需符合「確認台灣不用該詞、避免裸詞過度轉換、必要時補 identity mapping、跑 validate 與 pytest」的既有流程。

最新盤點紀錄見 `docs/reports/competitor-benchmark-2026-07-05.md`。

## Accuracy Regression

公開 regression dataset 用來防止已知正確行為回歸，不作為新的 blind accuracy 宣稱依據。目前入口：

- `benchmarks/accuracy/regression-v1.json`
- `benchmarks/accuracy/regression-v1.schema.json`
- `tests/test_accuracy_regression.py`

執行：

```bash
uv run python -m pytest tests/test_accuracy_regression.py -q
```

`regression-v1` 目前有 1,251 筆，涵蓋現有 `zhtw-test-corpus` 全量人工 expected、
500 筆 approved annotation promotions、219 筆已從 sealed holdout 移出的 public
regression promotions，以及 32 筆 public reproduction promotions。選取規則與分布記錄在
`benchmarks/accuracy/README.md`。

M1 annotation backlog 狀態由 `benchmarks/accuracy/annotation-backlog-v1.json` 追蹤。查詢：

```bash
make accuracy-annotation-status
```

只有 promotion-ready 的 `approved` 案例可以進 `regression-v1.json`：`expected`
必須非空、`expected_source` 必須是 `human_first_pass` 或
`human_adjudication`，而且必須先通過 promotion gate。預設審核順序是 Codex
先產生 `ai_draft`、Gemini 再產生獨立 advisory、最後由 maintainer 寫入
`review.expected`。Codex 與 Gemini 都只能是 advisory；AI advisory 必須記錄在
`review.ai_advisory_draft` 或 maintainer 判定後的 `review.ai_advisory`，不可偽裝成
`blind_reviewer`。若 maintainer 拒用 Gemini advisory，必須標為
`decision = "rejected"`，且該案例必須是 `human_adjudication`、有
adjudicator、並標示 disagreement。不可用 zhtw、OpenCC、zhconv 或未經
maintainer 審核的 LLM 輸出補 expected。

`annotation-backlog-v1.json` 可以保留 `ai_draft` 與
`review.ai_advisory_draft` 作為 maintainer 審核參考，但它們不屬於 ground
truth，不能 promotion，也不能直接讓 `expected_source` 變成
`human_first_pass`。

從 sealed holdout 移出的案例必須先進
`benchmarks/accuracy/holdout-regression-candidates-v1.json`，通過
`docs/reports/holdout-regression-promotion-gate-blind-v1-2026-07-09.json` 或
`docs/reports/holdout-regression-promotion-gate-blind-v1-batch2-2026-07-09.json` 或
`docs/reports/holdout-regression-promotion-gate-blind-v1-batch3-2026-07-09.json` 或
`docs/reports/holdout-regression-promotion-gate-blind-v1-batch4-recheck-2026-07-09.json` 或
`docs/reports/holdout-regression-promotion-gate-blind-v1-remaining-40-final-review-2026-07-09.json` 或
`docs/reports/holdout-regression-promotion-gate-blind-v1-338-miss-review-2026-07-09.json` 或
`docs/reports/holdout-regression-promotion-gate-blind-v1-batch6-miss-review-2026-07-10.json` 或
`docs/reports/holdout-regression-promotion-gate-blind-v1-batch7-miss-review-2026-07-10.json` 或
`docs/reports/holdout-regression-promotion-gate-blind-v1-batch8-miss-review-2026-07-11.json` 或
`docs/reports/holdout-regression-promotion-gate-blind-v1-batch9-miss-review-2026-07-12.json` 或
`docs/reports/holdout-regression-promotion-gate-blind-v1-batch10-miss-review-2026-07-13.json` 後才可進
`regression-v1.json`。這類案例的 regression source classification 必須是
`holdout_regression_promoted`，不可偽裝成一般 annotation promotion。

Public reproduction 案例必須先完成 Codex first-pass、Gemini independent advisory、
Codex/Gemini diff、maintainer final decision，且通過 public reproduction promotion
gate；只有 zhtw 輸出與 final primary expected 完全相同的案例才可進
`regression-v1.json`。這類案例的 regression source classification 必須是
`public_reproduction_promoted`，只命中 acceptable variant 的案例不得在目前單一
expected schema 下直接 promotion。

## Sealed Holdout

M2 開始使用 `blind-v1` 作為 sealed holdout 流程，用來支撐未來的 blind
accuracy 宣稱。它和 public regression 分離：

- `benchmarks/accuracy/blind-v1.inputs.json` 只保存輸入，不得包含
  `expected`、`acceptable`、`review` 或 `annotation`。
- `benchmarks/accuracy/blind-v1.expected.json` 是人工標註完成後才會產生的
  private ground truth；目前由 `.gitignore` 保護，發布 benchmark 前不得公開。
- `benchmarks/accuracy/blind-v1.expected.schema.json` 定義 expected 必須來自
  human review only；目前允許 `single_human_with_ai_advisory`，分歧必須由
  maintainer 裁決。
- `benchmarks/accuracy/competitors.lock.json` 記錄每個 adapter 的版本來源、命令與
  locale/config。未鎖定的競品不得進正式排名。
- `scripts/create_holdout_annotation_packet.py` 產生人工標註包，只能顯示 input 與空白
  expected 欄位，不得加入任何 converter 或 LLM 輸出。
- `scripts/run_accuracy_benchmark.py` 只在 private expected 已存在時產出報告；報告
  會記錄 inputs、expected、lockfile 的 sha256。

目前 `blind-v1.inputs.json` 保留 1,030 筆 input-only seed pool，目標為 2,000 筆；
1,030 筆皆已有本機 private expected；Batch13、Batch12 與 batch11 均已完成
maintainer review OK。
2026-07-09 先將 27 筆修正候選移出 sealed holdout 並 promotion，之後新增 127 筆
input-only seed。這 127 筆已完成 Codex first-pass、Gemini advisory、Codex/Gemini diff
review 與 maintainer OK，當時 private expected 已擴充到 200 筆；batch3 再從 200 筆 sanity
miss classification 移出 39 筆並 promotion。batch4 100 筆 maintainer OK 後，261 筆 sanity
recheck 又確認 9 筆 acceptable variant、5 筆移出 sealed 並 promotion、2 筆維持 strict。
remaining-40 final review 再確認 3 筆 acceptable variant、18 筆移出 sealed 並 promotion。
batch5 100 筆 maintainer OK 後，338 筆 sanity miss classification 再確認 3 筆
acceptable variant、12 筆移出 sealed 並 promotion、22 筆維持 private holdout signal。
batch6 100 筆 maintainer OK 後，426 筆 sanity miss classification 再確認 2 筆
acceptable variant、11 筆移出 sealed 並 promotion、24 筆維持 private holdout signal。
batch7 100 筆 maintainer OK 後，515 筆 sanity miss classification 再確認 7 筆
acceptable variant、17 筆移出 sealed 並 promotion、26 筆維持 private holdout signal。
batch8 100 筆 maintainer OK 後，598 筆 sanity miss classification 再確認 4 筆
acceptable variant、15 筆移出 sealed 並 promotion、30 筆維持 private holdout signal。
batch9 100 筆 maintainer OK 後，private expected 與 input pool 曾對齊 683 筆；
batch9 miss review 再確認 6 筆 acceptable variant、16 筆移出 sealed 並 promotion、31 筆維持 private holdout signal。
batch10 又新增 100 筆 input-only cases；Codex first-pass、Gemini CLI advisory、
Codex/Gemini diff review 與 maintainer confirmation packet 已完成。Maintainer final
decision 已確認 44 筆 review queue 與 56 筆 no-immediate-question cases，並寫入本機
private expected。batch10 miss review 後再確認 4 筆 acceptable variant、16 筆移出
sealed 並 promotion、32 筆維持 private holdout signal。
截至 Batch13 miss review，累計 219 筆已轉為 public regression，
batch4 已再新增 100 筆 input-only cases，並在 maintainer OK 後寫入本機 private
expected。batch5 再新增並完成 review 100 筆 input-only cases。batch6 100 筆也已
完成 Codex/Gemini advisory、diff review、maintainer confirmation 與 final
decision，batch6 miss review 後 private expected 對齊 415 筆 reviewed sealed input；415 筆 reviewed
sanity 可做 maintainer 內部 sanity。batch7 已再新增 100 筆 input-only cases，
且 Codex first-pass advisory、Gemini CLI advisory、Codex/Gemini diff review
與 maintainer confirmation packet 已完成；maintainer final decision 已確認
65 筆 review queue 與 35 筆 no-immediate-question cases，並寫入本機 private
expected。batch7 miss review 經 maintainer OK 後，17 筆已移出 sealed 並 promotion，
7 筆只加入 private acceptable variants，26 筆保留為 private holdout signal。batch7
miss review 後，private expected 對齊 498 筆 input pool；當時 zhtw-only sanity 為 472/498
accepted、26 misses、accepted accuracy 約 94.78%，miss mix 為 1 筆
`candidate_gap`、25 筆 `over_conversion_guard`。batch8 又新增 100 筆 public
input-only cases；Codex first-pass、Gemini CLI advisory、Codex/Gemini diff
review 與 maintainer confirmation packet 已完成，maintainer final decision 已確認
66 筆 review queue 與 34 筆 no-immediate-question cases，並寫入本機 private
expected。batch8 miss review 經 maintainer OK 後，15 筆已移出 sealed 並 promotion，
4 筆只加入 private acceptable variants，30 筆保留為 private holdout signal。batch9
又新增 100 筆 public input-only cases；Codex first-pass、Gemini CLI advisory、
Codex/Gemini diff review 與 maintainer confirmation packet 已完成，maintainer
final decision 已確認 69 筆 review queue 與 31 筆 no-immediate-question cases，
並寫入本機 private expected。batch9 miss review 後，private expected 對齊當時 667 筆；
latest zhtw-only sanity 為 636/667 accepted、31 misses、accepted accuracy 約
95.35%。batch10 曾讓公開 input pool 增至 767 筆，並在 maintainer OK 後重建
private expected；batch10 miss review 後 current sealed pool 為 751 筆，latest
zhtw-only sanity 為 719/751 accepted、32 misses、accepted accuracy 約 95.74%。
batch11 曾加入 100 筆 input-only cases，公開 input pool 增至 851 筆；Codex、
Gemini advisory 與 maintainer final decision 均已完成。後續語意複核確認 4 筆
acceptable variants、10 筆移出 sealed 並 promotion、11 筆保留 strict private
signal；當時 private expected 與 input pool 對齊 841 筆。若要支撐嚴格市場宣稱，
仍需補第二位 human reviewer 或在 benchmark
報告明確揭露 `single_human_with_ai_advisory`。

執行方式：

```bash
make accuracy-benchmark DATE=2026-07-07 COMPETITORS=zhtw
```

Batch12 已新增 100 筆全新 input-only cases；Codex first pass、Gemini
`gemini-2.5-pro` input-only independent review 與差異彙整已完成。87 筆 primary
完全一致、13 筆不同、31 筆 exact policy review、56 筆 no-immediate-question；
maintainer queue 共 44 筆。Maintainer review OK 後 private expected 已對齊
941 筆；首次新盲測為 Batch12 85/100 accepted、15 misses，整體為 880/941
accepted、accepted accuracy 約 93.52%。Batch12 miss 分布為 IT 4、LLM 3、
high-risk 3、formal 2、social 2、UI 1：
`docs/reports/holdout-input-pool-expansion-blind-v1-batch12-100-cases-2026-07-14.md`、
`docs/reports/holdout-codex-first-pass-blind-v1-batch12-100-cases-2026-07-14.md`、
`docs/reports/holdout-gemini-cli-advisory-blind-v1-batch12-100-cases-2026-07-14.md`、
`docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch12-100-cases-2026-07-14.md`、
`docs/reports/holdout-maintainer-confirmation-blind-v1-batch12-100-cases-2026-07-14.md`、
`docs/reports/holdout-maintainer-final-decision-blind-v1-batch12-100-cases-2026-07-14.md`、
`docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch12-2026-07-14.md`。

Batch12 的 15 筆新 miss 已完成 Codex 語意分類與 Gemini `gemini-2.5-pro`
input-only 獨立審查。Codex 初判 7 筆 acceptable、8 筆 public candidate；Gemini
未看 Codex、private expected 或 zhtw output，tool calls 為 0。彙整後建議為 9 筆
acceptable、6 筆 public candidate、0 筆 strict private signal；其中 7 筆分類一致，
maintainer 已確認 `覈定`、`查覈` 不符合當代臺灣常用語，兩筆改列 public
candidate。最終人工決策為 4 筆 acceptable variant、11 筆 public regression
candidate、0 筆新增 strict private signal；11 筆均以完整句 mapping 與 identity mapping
修正並通過 promotion gate，已升格至 `regression-v1.json`：
`docs/reports/holdout-miss-classification-blind-v1-batch12-15-cases-2026-07-14.md`、
`docs/reports/holdout-gemini-independent-semantic-review-blind-v1-batch12-15-misses-2026-07-14.md`、
`docs/reports/holdout-codex-gemini-miss-review-diff-blind-v1-batch12-15-cases-2026-07-14.md`、
`docs/reports/holdout-maintainer-confirmation-blind-v1-batch12-miss-review-8-cases-2026-07-14.md`、
`docs/reports/holdout-maintainer-partial-decision-blind-v1-batch12-miss-review-2026-07-14.md`、
`docs/reports/holdout-maintainer-final-decision-blind-v1-batch12-miss-review-2026-07-14.md`、
`docs/reports/holdout-regression-promotion-gate-blind-v1-batch12-miss-review-2026-07-14.md`。

Batch12 miss review 後，private expected 與 input pool 對齊 930 筆；最新 private
sanity 為 884/930 accepted、46 misses、accepted accuracy 約 95.05%。此結果加入 4 筆
acceptable variants，且 11 筆在調整詞庫前已移出 sealed pool，分母已改變，因此不得把
它與 880/941 直接解讀為純能力提升：
`docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch12-miss-review-2026-07-14.md`。

注意：benchmark 指令只能在 inputs 與 private expected 對齊時使用；目前
1,030-case inputs 與 private expected 已對齊。

Batch13 已新增 100 筆當代常用語境的 input-only cases，分布為 formal 15、
high-risk 15、IT 20、UI 15、social 20、LLM 15。Codex first pass 為 78 筆高信心、
22 筆中信心；Gemini CLI 使用 `gemini-2.5-pro` 獨立審查 100/100 筆，未看 Codex、
private expected、zhtw 或競品輸出，tool calls 為 0，quality flags 為 0。主建議
66 筆完全一致、34 筆不同；另有 19 筆一致但因 high-risk 或變體政策需確認，
maintainer queue 共 53 筆，其餘 47 筆列為建議採用。Maintainer review OK 後已將
100 筆寫入 private expected，其中 35 筆為 human adjudication、65 筆為 human first
pass。首次調詞前盲測為 66/100 accepted、34 misses；整體為 950/1,030 accepted，
accepted accuracy 約 92.23%。新 miss 分布為 IT 10、UI 8、LLM 6、high-risk 5、
social 3、formal 2。這是有效的新鮮泛化訊號，但 approval policy 仍是
`single_human_with_ai_advisory`，且結果不支援 market-best 宣稱：
`docs/reports/holdout-input-pool-expansion-blind-v1-batch13-100-cases-2026-07-14.md`、
`docs/reports/holdout-codex-first-pass-blind-v1-batch13-100-cases-2026-07-14.md`、
`docs/reports/holdout-gemini-cli-advisory-blind-v1-batch13-100-cases-2026-07-14.md`、
`docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch13-100-cases-2026-07-14.md`、
`docs/reports/holdout-maintainer-confirmation-blind-v1-batch13-100-cases-2026-07-14.md`、
`docs/reports/holdout-maintainer-final-decision-blind-v1-batch13-100-cases-2026-07-14.md`、
`docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch13-2026-07-14.md`。

Batch13 的 34 筆 fresh misses 已完成 Codex first-pass classification 與 Gemini
`gemini-2.5-pro` input-only 獨立政策審查；Gemini 未看 Codex、private expected 或
zhtw output，tool calls 為 0。雙方分類一致 19 筆、不同 15 筆；彙整建議為 5 筆
acceptable variant、22 筆 public regression candidate、7 筆 strict private signal。
Maintainer queue 為 19 筆，其餘 15 筆是雙方一致的低風險 public candidate。Maintainer
review OK 後，5 筆已加入 private acceptable variants、22 筆先移出 sealed 再以完整句
mapping 與 identity mapping 通過 22/22 promotion gate、7 筆保留為 strict private signal。
目前 sealed pool 為 1,008 筆，private sanity 為 955/1,008 accepted（94.74%）；因新增
acceptable variants 且移除案例造成分母變更，不視為純能力提升或 market-best 證據：
`docs/reports/holdout-miss-classification-blind-v1-batch13-34-cases-2026-07-14.md`、
`docs/reports/holdout-gemini-independent-semantic-review-blind-v1-batch13-34-misses-2026-07-14.md`、
`docs/reports/holdout-codex-gemini-miss-review-diff-blind-v1-batch13-34-cases-2026-07-14.md`、
`docs/reports/holdout-maintainer-confirmation-blind-v1-batch13-miss-review-19-cases-2026-07-14.md`、
`docs/reports/holdout-maintainer-final-decision-blind-v1-batch13-miss-review-2026-07-14.md`、
`docs/reports/holdout-regression-promotion-gate-blind-v1-batch13-miss-review-2026-07-14.md`、
`docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch13-miss-review-2026-07-14.md`。

### 2026-07-16 發版前 expert re-audit

以同一批目前仍 sealed 的 1,008 筆比較 v4.4.1 與目前詞庫：v4.4.1 為
951/1,008 accepted，目前詞庫為 955/1,008，淨增 4 筆、accepted regression 0 筆，
約增加 0.40 個百分點。這是目前可支持的 like-for-like 改善幅度；不得用公開
regression 771/1,251 → 1,251/1,251 取代泛化指標。

完整句 audit 共檢查 373 組 source/target identity，移除 4 筆已由泛化規則覆蓋的
source mapping；其 target identity 因二次轉換保護仍須保留。其餘 369 組明確標示為
exact-sentence regression guards，不計入 fresh-blind generalization，也不得自動拆成
裸詞。另完成 500 筆 annotation expected 的 Gemini input/expected 獨立語意複核；
Gemini 標記的 10 筆均已符合目前 expected，沒有新增修正。

Expert review 另以權威來源重新裁決 3 筆已公開 ground truth，修正 rollback、future
型別與物業管理／管委會實體混淆。歷史 AI 原始報告不回寫；目前 backlog、regression
與詞庫已同步。詳見：
`docs/reports/accuracy-ground-truth-corrections-2026-07-16.md`、
`docs/reports/accuracy-gemini-independent-semantic-reaudit-500-cases-2026-07-16.md`、
`docs/reports/accuracy-exact-sentence-mapping-audit-2026-07-16.md`。

人工標註包：

```bash
make accuracy-holdout-annotation-packet DATE=2026-07-07
```

預設 review 節奏：

1. Codex 先做第一輪 expected 建議、風險判斷與理由。
2. Gemini 再從 input-only packet 獨立 review。
3. Codex 比對兩邊結果，整理一致、差異與低信心案例。
4. 只把需要 maintainer 確認的案例列出來；一致且低風險的案例可以列為建議採用。
5. maintainer 確認後才寫入 private expected。Codex/Gemini 結果都只能是 advisory。

若使用這個加速節奏，資料來源要標示為
`single_human_with_ai_advisory`。它可用於 maintainer 主導的快速迭代；若要支撐
嚴格 sealed benchmark 宣稱，仍需補第二位 human reviewer 或在報告中明確揭露審核方式。

目前第一份 Codex first-pass advisory：

- `docs/reports/holdout-codex-first-pass-blind-v1-0001-0100-2026-07-08.md`
- `docs/reports/holdout-codex-first-pass-blind-v1-0001-0100-2026-07-08.json`
- 100 筆 input 全部有 Codex expected 建議。
- 83 筆 high confidence，17 筆 medium confidence。
- 36 筆標示為後續需確認或需看 Gemini 差異。
- 這份報告不可直接寫入 `blind-v1.expected.json`。

目前第一份 Gemini independent advisory 與 Codex/Gemini diff review：

- `docs/reports/holdout-gemini-vertex-advisory-blind-v1-0001-0100-2026-07-08.md`
- `docs/reports/holdout-gemini-vertex-advisory-blind-v1-0001-0100-2026-07-08.json`
- `docs/reports/holdout-codex-gemini-diff-review-blind-v1-0001-0100-2026-07-08.md`
- `docs/reports/holdout-codex-gemini-diff-review-blind-v1-0001-0100-2026-07-08.json`
- 100 筆中 Codex/Gemini 完全一致 70 筆，差異 30 筆。
- policy filter 後 maintainer queue 共 59 筆。
- 差異初步建議：24 筆採 Codex、5 筆採 Gemini、1 筆採第三版。
- 這些報告仍不可直接寫入 `blind-v1.expected.json`。

目前 maintainer confirmation packet：

- `docs/reports/holdout-maintainer-confirmation-blind-v1-0001-0100-2026-07-08.md`
- `docs/reports/holdout-maintainer-confirmation-blind-v1-0001-0100-2026-07-08.json`
- 59 筆需要 maintainer 確認：30 筆 Codex/Gemini 差異，29 筆 policy quick confirm。
- 41 筆列為 no immediate question。
- 這份 packet 是確認用，不是 ground truth。

目前 maintainer final decision：

- `benchmarks/accuracy/blind-v1.expected.json` 已在本機產生，狀態為 `sealed_private`。
- 該檔由 `.gitignore` 保護，發布 benchmark 前不得公開。
- approval policy 是 `single_human_with_ai_advisory`，不是 two-human review。
- 初始 100 筆中 70 筆為 `human_first_pass`，30 筆為 `human_adjudication`。
- 2026-07-09 第一批移出 22 筆 public regression candidates 後，本機 private expected 與
  input-only seed pool 對齊為 78 筆。公開移出紀錄在
  `docs/reports/holdout-sealed-pool-update-blind-v1-2026-07-09.md`。
- 2026-07-09 第二批再移出 5 筆 public regression candidates 後，本機 private expected 與
  input-only seed pool 對齊為 73 筆。公開移出紀錄在
  `docs/reports/holdout-sealed-pool-update-blind-v1-batch2-2026-07-09.md`。
- 2026-07-09 後續新增 127 筆 input-only seed 後，公開 input pool 擴充為 200 筆。
  公開擴充紀錄在
  `docs/reports/holdout-input-pool-expansion-blind-v1-2026-07-09.md`。
- 這 127 筆已完成 Codex first-pass、Gemini advisory aggregate 與 Codex/Gemini diff review：
  `docs/reports/holdout-codex-first-pass-blind-v1-expansion-127-cases-2026-07-09.md`、
  `docs/reports/holdout-gemini-vertex-advisory-blind-v1-expansion-127-cases-2026-07-09.md`、
  `docs/reports/holdout-codex-gemini-diff-review-blind-v1-expansion-127-cases-2026-07-09.md`。
  結果是 79 筆 Codex/Gemini exact match、48 筆差異、81 筆 maintainer queue。
  這些報告本身仍只是 advisory，不可直接當作 ground truth。
- 已依照 review 節奏先產生 48 筆差異專用 maintainer confirmation packet：
  `docs/reports/holdout-maintainer-confirmation-blind-v1-expansion-differences-2026-07-09.md`。
  這份 packet 不含 33 筆一致但 policy review 的案例；那些案例延後處理。此 packet 仍不是
  ground truth，不可直接寫入 private expected。
- Maintainer 已確認 48 筆差異案例採用 recommended expected；公開決策摘要在
  `docs/reports/holdout-maintainer-final-decision-blind-v1-expansion-differences-2026-07-09.md`。
  這份 summary 只是 partial decision；完整寫入在後續 127 筆 final decision summary。
- 33 筆 Codex/Gemini exact-match policy-review 案例已整理成 maintainer confirmation
  packet 並由 maintainer OK：
  `docs/reports/holdout-maintainer-confirmation-blind-v1-expansion-policy-review-2026-07-09.md`。
  對應決策摘要在
  `docs/reports/holdout-maintainer-final-decision-blind-v1-expansion-policy-review-2026-07-09.md`。
- 已產生 127 筆 expansion final decision summary，並重建本機 private
  `benchmarks/accuracy/blind-v1.expected.json` 為 200 筆：
  `docs/reports/holdout-maintainer-final-decision-blind-v1-expansion-127-cases-2026-07-09.md`。
  Expansion 127 筆中 79 筆為 `human_first_pass`，48 筆為 `human_adjudication`；
  重建後全體 200 筆中 135 筆為 `human_first_pass`，65 筆為 `human_adjudication`。
- 公開摘要：
  `docs/reports/holdout-maintainer-final-decision-blind-v1-0001-0100-2026-07-08.md`
  與
  `docs/reports/holdout-maintainer-final-decision-blind-v1-0001-0100-2026-07-08.json`。
- 公開摘要只記錄 metadata/hash/counts，不含 expected values。

目前 private benchmark sanity check：

- 完整 benchmark rows 放在 `/tmp/zhtw-blind-v1-private-benchmark-2026-07-09.*`，不進 repo。
- repo 內只保存 aggregate-only summary：
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-2026-07-09.md`
  與
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-2026-07-09.json`。
- 這份 sanity summary 覆蓋目前 261 筆 private expected。
- zhtw accepted：207 / 261。
- accepted accuracy：0.7931。
- primary exact accuracy：0.7050。
- idempotency rate：0.9885。
- domain accuracy：formal 32/41、high_risk 22/28、it 39/53、llm 36/43、
  social 35/44、ui 43/52。
- 這是 holdout 訊號，不得直接用來調詞庫；若要修某筆，需先把該 case 移出 sealed
  holdout，改成 public regression 候選。

目前 261 筆 private sanity 的 miss classification：

- Codex classification：
  `docs/reports/holdout-miss-classification-blind-v1-261-cases-2026-07-09.md`。
- Gemini sanitized policy review：
  `docs/reports/holdout-gemini-policy-review-miss-classification-blind-v1-261-cases-2026-07-09.md`。
- 54 筆 miss 已分類：18 筆建議先移出 sealed 再轉 public regression candidate，16 筆
  需 expected/acceptable recheck，20 筆保留作 sealed holdout signal。
- Gemini 只收到 sanitized metadata，未收到 input、expected、acceptable、zhtw output
 或 benchmark rows；第一輪指出 7 筆 high-risk / over-conversion guard 應更保守，Codex
  已改為 `requires_expected_recheck`，最終 review 回覆 policy consistent，needs follow-up 0。

目前 261 筆 private sanity 的 requires-expected recheck：

- Codex recheck summary：
  `docs/reports/holdout-requires-expected-recheck-blind-v1-261-cases-2026-07-09.md`。
- Gemini sanitized policy review：
  `docs/reports/holdout-gemini-policy-review-requires-expected-recheck-blind-v1-261-cases-2026-07-09.md`。
- Private maintainer packet：
  `/tmp/zhtw-holdout-261-case-recheck-maintainer-review-packet-2026-07-09.md`。
- 16 筆 recheck 中，9 筆建議由 maintainer 確認是否加入 acceptable variant，5 筆建議
  maintainer 確認後移出 sealed 再轉 public regression candidate，2 筆建議維持 strict
  primary expected。
- 若 9 筆 acceptable variant 全部確認，hypothetical accepted 為 216/261；這不是更新後
  benchmark 結果，private expected 仍需 maintainer OK 後才可修改。
- Gemini 只收到 sanitized metadata，未收到 input、expected、acceptable、zhtw output
  或 benchmark rows；回覆 policy consistent，needs follow-up 0。

上一輪 200 筆 private sanity 的 miss classification：

- Codex classification：
  `docs/reports/holdout-miss-classification-blind-v1-200-cases-2026-07-09.md`。
- Gemini sanitized policy review：
  `docs/reports/holdout-gemini-policy-review-miss-classification-blind-v1-200-cases-2026-07-09.md`。
- 56 筆 miss 已分類：39 筆建議先移出 sealed 再轉 public regression candidate，11 筆
  需 expected/acceptable recheck，6 筆保留作 sealed holdout signal。
- Gemini 只收到 sanitized metadata，未收到 input、expected、acceptable、zhtw output
  或 benchmark rows；回覆 policy consistent，needs follow-up 0。

目前 post-batch3 miss recheck：

- Codex recheck：
  `docs/reports/holdout-post-batch3-miss-recheck-blind-v1-2026-07-09.md`。
- Gemini sanitized policy review：
  `docs/reports/holdout-gemini-policy-review-post-batch3-recheck-blind-v1-2026-07-09.md`。
- 17 筆 sealed miss 中，11 筆建議由 maintainer 確認是否加入 private acceptable
  variant，6 筆保留作 sealed holdout signal。
- maintainer final decision：
  `docs/reports/holdout-maintainer-final-decision-post-batch3-recheck-blind-v1-2026-07-09.md`。
- Maintainer 已確認 11 筆 acceptable variant 建議；private expected 已更新，primary
  expected 未變更。
- private maintainer packet 在
  `/tmp/zhtw-holdout-post-batch3-maintainer-review-packet-2026-07-09.md`，含 sealed
  input、expected、zhtw output，不進 repo。
- Gemini 只收到 sanitized metadata，未收到 input、expected、acceptable、zhtw output
  或 benchmark rows；回覆 policy consistent，needs follow-up 0。
- batch4 前 sanity 曾為 155/161 accepted、6 misses；batch4 封存後最新 sanity 為
  207/261 accepted、54 misses。

目前 remaining signal summary：

- Codex summary：
  `docs/reports/holdout-remaining-signal-summary-blind-v1-2026-07-09.md`。
- Gemini sanitized policy review：
  `docs/reports/holdout-gemini-policy-review-remaining-signal-blind-v1-2026-07-09.md`。
- 剩餘 6 筆 sealed miss 全部保留為 holdout signal：5 筆 graph-variant
  over-conversion signal、1 筆 strict UI wording signal。
- 這 6 筆不得用於 converter 或 dictionary tuning；若未來要修，必須先移出 sealed
  holdout，建立 public regression candidate artifact，再進行修正。

目前 batch4 input expansion：

- `docs/reports/holdout-input-pool-expansion-blind-v1-batch4-100-cases-2026-07-09.md`
  記錄新增 100 筆 input-only cases，目前 input pool 為 261/2,000。
- Codex first-pass advisory：
  `docs/reports/holdout-codex-first-pass-blind-v1-batch4-100-cases-2026-07-09.md`。
- Gemini independent advisory：
  `docs/reports/holdout-gemini-vertex-advisory-blind-v1-batch4-100-cases-2026-07-09.md`。
- Codex/Gemini diff review：
  `docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch4-100-cases-2026-07-09.md`。
- Maintainer confirmation packet：
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch4-100-cases-2026-07-09.md`。
- Maintainer final decision：
  `docs/reports/holdout-maintainer-final-decision-blind-v1-batch4-100-cases-2026-07-09.md`。
- Batch4 100 筆中，Codex/Gemini exact match 74 筆、差異 26 筆；依 high-risk、
  over-conversion guard 與 medium-confidence policy，maintainer queue 共 64 筆。

目前 batch5 input expansion：

- `docs/reports/holdout-input-pool-expansion-blind-v1-batch5-100-cases-2026-07-09.md`
  記錄新增 100 筆 input-only cases，當時 input pool 為 338/2,000。
- 這批只含 public input 與 metadata，不含 expected、acceptable variants、converter
  output 或 benchmark rows。
- Codex first-pass advisory：
  `docs/reports/holdout-codex-first-pass-blind-v1-batch5-100-cases-2026-07-09.md`。
- Gemini CLI independent advisory：
  `docs/reports/holdout-gemini-cli-advisory-blind-v1-batch5-100-cases-2026-07-09.md`。
- Codex/Gemini diff review：
  `docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch5-100-cases-2026-07-09.md`。
- Maintainer confirmation packet：
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch5-100-cases-2026-07-09.md`。
- Maintainer final decision：
  `docs/reports/holdout-maintainer-final-decision-blind-v1-batch5-100-cases-2026-07-09.md`。
- Batch5 100 筆中，Codex/Gemini exact match 92 筆、差異 8 筆；依 high-risk、
  over-conversion guard 與 medium-confidence policy，maintainer queue 共 50 筆。
- Maintainer 已確認 batch5 packet；本機 private expected 已更新到 338 筆。Batch5
  100 筆中 92 筆為 `human_first_pass`，8 筆為 `human_adjudication`。
- `blind-v1.expected.schema.json` 已允許 `gemini_cli` 作為 AI advisory reviewer，
  以忠實記錄 batch5 的第二審來源。
- Gemini CLI 的 API-key 模式目前會回 `API_KEY_INVALID`；本輪 public promotion
  policy review 是 unset API-key env vars 後使用非 API-key CLI 認證成功完成。

目前 338 筆 private benchmark sanity：

- `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch5-2026-07-09.md`
  記錄 batch5 final decision 後的 private sanity aggregate。
- 338 筆中 zhtw accepted 301 筆、misses 37 筆，accepted accuracy 約 89.05%。
- 這份 sanity 報告是 private benchmark output；公開引用時只能使用 aggregate
  statistics，不得公開 sealed expected、input、converter output 或完整 rows。

目前 338 筆 miss classification：

- `docs/reports/holdout-miss-classification-blind-v1-338-cases-2026-07-09.md` 記錄
  37 筆 miss 的 sanitized classification。
- Gemini policy review：
  `docs/reports/holdout-gemini-policy-review-miss-classification-blind-v1-338-cases-2026-07-09.md`。
- 37 筆 miss 中，22 筆為 `keep_as_holdout_signal`，不得用來調詞庫；12 筆為
  `move_to_public_regression_candidate`，需 maintainer 確認並移出 sealed holdout
  後才能 promotion/tuning；3 筆為 `requires_expected_recheck`，需先確認
  expected 或 acceptable variants。
- Gemini policy review 確認分類政策通過，且未建議改分類。
- Maintainer `review OK` 後，3 筆 `requires_expected_recheck` 已只加入 private
  acceptable variants；12 筆 `move_to_public_regression_candidate` 已移出 sealed
  holdout，進 public candidate，再以完整句 mapping + identity tuning 後 promotion。
- 對應 final decision：
  `docs/reports/holdout-maintainer-final-decision-338-miss-classification-blind-v1-2026-07-09.md`。
- 對應 sealed pool update：
  `docs/reports/holdout-sealed-pool-update-blind-v1-338-miss-review-2026-07-09.md`。
- 對應 public promotion gate：
  `docs/reports/holdout-regression-promotion-gate-blind-v1-338-miss-review-2026-07-09.md`。
- Gemini public promotion policy review：
  `docs/reports/holdout-gemini-policy-review-338-miss-public-promotion-2026-07-09.md`。
- 最新 sealed pool 為 326 筆，private expected 對齊 326 筆；已重跑 zhtw-only
  private sanity aggregate：
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-338-miss-review-2026-07-09.md`。
- 實跑結果為 304/326 accepted、22 misses、accepted accuracy 約 93.25%；22 筆
  misses 全部是 `over_conversion_guard`。repo 內報告只含 aggregate statistics，
  不公開 sealed input、expected、acceptable variants、converter output 或完整 rows。

目前 batch6 input expansion：

- `docs/reports/holdout-input-pool-expansion-blind-v1-batch6-100-cases-2026-07-09.md`
  記錄新增 100 筆 input-only cases，當時 input pool 為 426/2,000。
- Batch6 配比：IT/API/CLI 25、UI/i18n 20、LLM/content 15、formal 15、social 15、
  high-risk 10；風險分布為 baseline 15、candidate_gap 60、over_conversion_guard 25。
- 這批只含 public input 與 metadata，不含 expected、acceptable variants、converter
  output 或 benchmark rows。
- Codex first-pass advisory：
  `docs/reports/holdout-codex-first-pass-blind-v1-batch6-100-cases-2026-07-10.md`。
- Codex 建議 100 筆 expected，80 筆 high confidence、20 筆 medium confidence；
  依 over-conversion guard、high-risk domain 與 medium confidence policy，
  maintainer queue 目前為 50 筆。
- Gemini CLI independent advisory：
  `docs/reports/holdout-gemini-cli-advisory-blind-v1-batch6-100-cases-2026-07-10.md`。
- Gemini 建議 100 筆 expected，100 筆 high confidence；依 Gemini 標示目前
  review-needed 為 70 筆。Gemini CLI 這次已 unset API-key env vars，使用非
  API-key CLI 認證完成。
- Codex/Gemini diff review：
  `docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch6-100-cases-2026-07-10.md`。
- Maintainer confirmation packet：
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch6-100-cases-2026-07-10.md`。
- Batch6 100 筆中，Codex/Gemini primary expected exact match 80 筆、差異
  20 筆；依 Gemini review-needed、over-conversion guard、high-risk domain
  與 Codex medium confidence policy，maintainer queue 共 76 筆。差異初步建議為
  13 筆採 Codex、4 筆採 Gemini、3 筆採第三版。
- Maintainer final decision：
  `docs/reports/holdout-maintainer-final-decision-blind-v1-batch6-100-cases-2026-07-10.md`。
- Maintainer 已確認 batch6 packet；本機 private expected 已更新到 426 筆。Batch6
  100 筆中 80 筆為 `human_first_pass`，20 筆為 `human_adjudication`。
- zhtw-only private sanity aggregate：
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch6-2026-07-10.md`。
  實跑結果為 389/426 accepted、37 misses、accepted accuracy 約 91.31%；repo
  內報告只含 aggregate statistics，不公開 sealed input、expected、acceptable
  variants、converter output 或完整 rows。
- 37 筆 misses 已完成 sanitized Codex first-pass classification：
  `docs/reports/holdout-miss-classification-blind-v1-426-cases-2026-07-10.md`。
  分流結果為 24 筆 `keep_as_holdout_signal`、11 筆
  `move_to_public_regression_candidate`、2 筆 `requires_expected_recheck`。
- Gemini CLI 已對 sanitized metadata 做 policy review，未看到 sealed input、
  expected、acceptable variants、converter output 或 rows；結果通過且不建議改分類：
  `docs/reports/holdout-gemini-policy-review-miss-classification-blind-v1-426-cases-2026-07-10.md`。
- 需要 maintainer 確認的 sanitized packet：
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch6-miss-classification-2026-07-10.md`。
  這份 packet 只含 case id 與 metadata；11 筆 public candidate 必須在移出 sealed
  holdout 後才可進 public regression，2 筆 expected recheck 需先確認 private
  expected 或 acceptable variants。
- Maintainer 已確認 batch6 miss classification；final decision：
  `docs/reports/holdout-maintainer-final-decision-batch6-miss-classification-blind-v1-2026-07-10.md`。
- Batch6 miss review sealed pool update：
  `docs/reports/holdout-sealed-pool-update-blind-v1-batch6-miss-review-2026-07-10.md`。
  11 筆已移出 sealed 並進 public regression candidates；2 筆 recheck 已加入 private
  expected acceptable variants，仍留在 sealed。
- 對應 public promotion gate：
  `docs/reports/holdout-regression-promotion-gate-blind-v1-batch6-miss-review-2026-07-10.md`。
  結果為 11/11 promotion-ready，zhtw output 與 expected 完全一致且 expected/output
  皆冪等。
- Gemini public promotion policy review：
  `docs/reports/holdout-gemini-policy-review-batch6-miss-public-promotion-2026-07-10.md`。
- 最新 sealed pool 為 498 筆，private expected 對齊 498 筆；已重跑 zhtw-only
  private sanity aggregate：
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch7-miss-review-2026-07-10.md`。
- 實跑結果為 472/498 accepted、26 misses、accepted accuracy 約 94.78%；miss
  mix 為 1 筆 `candidate_gap`、25 筆 `over_conversion_guard`。repo 內報告只含 aggregate statistics，
  不公開 sealed input、expected、acceptable variants、converter output 或完整 rows。
- Batch8 已新增 100 筆 input-only cases，且 maintainer final decision 已確認 66 筆
  review queue 與 34 筆 no-immediate-question cases；目前 input pool 與 private
  expected 曾對齊 598 筆。Batch8 review artifacts：
  `docs/reports/holdout-input-pool-expansion-blind-v1-batch8-100-cases-2026-07-10.md`、
  `docs/reports/holdout-codex-first-pass-blind-v1-batch8-100-cases-2026-07-10.md`、
  `docs/reports/holdout-gemini-cli-advisory-blind-v1-batch8-100-cases-2026-07-10.md`、
  `docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch8-100-cases-2026-07-10.md`、
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch8-100-cases-2026-07-10.md`、
  `docs/reports/holdout-maintainer-final-decision-blind-v1-batch8-100-cases-2026-07-10.md`。
- Batch8 後已重跑 zhtw-only private sanity aggregate：
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch8-2026-07-10.md`。
  實跑結果為 549/598 accepted、49 misses、accepted accuracy 約 91.81%；miss
  mix 為 1 筆 `baseline_guard`、21 筆 `candidate_gap`、27 筆
  `over_conversion_guard`。repo 內報告只含 aggregate statistics，不公開 sealed
  input、expected、acceptable variants、converter output 或完整 rows。
- 49 筆 miss 已整理成 sanitized classification，不公開 sealed values：
  `docs/reports/holdout-miss-classification-blind-v1-598-cases-2026-07-10.md`。
  Codex 建議為 30 筆保留 private holdout signal、15 筆轉 public regression
  candidate、4 筆 expected recheck。
- Gemini CLI 已對該 sanitized classification 做 policy review，確認政策通過且
  0 筆分類變更建議；本次 CLI 執行已 unset 無效 API-key 相關環境變數：
  `docs/reports/holdout-gemini-policy-review-miss-classification-blind-v1-598-cases-2026-07-10.md`。
- 19 筆需要 maintainer 確認的項目已整理成 review packet：
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch8-miss-classification-2026-07-10.md`。
- Batch8 miss classification 已 maintainer OK，final decision：
  `docs/reports/holdout-maintainer-final-decision-batch8-miss-classification-blind-v1-2026-07-11.md`。
  結果為 15 筆移出 sealed 並 promotion、4 筆只加入 private acceptable
  variants、30 筆保留為 private holdout signal。
- Batch8 miss review sealed pool update：
  `docs/reports/holdout-sealed-pool-update-blind-v1-batch8-miss-review-2026-07-11.md`。
- Batch8 miss review public promotion gate：
  `docs/reports/holdout-regression-promotion-gate-blind-v1-batch8-miss-review-2026-07-11.md`。
- Gemini public promotion policy review：
  `docs/reports/holdout-gemini-policy-review-batch8-miss-public-promotion-2026-07-11.md`。
- Batch8 miss review 後已重跑 zhtw-only private sanity aggregate：
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch8-miss-review-2026-07-11.md`。
  實跑結果為 553/583 accepted、30 misses、accepted accuracy 約 94.85%；miss
  mix 為 1 筆 `baseline_guard`、2 筆 `candidate_gap`、27 筆
  `over_conversion_guard`。repo 內報告只含 aggregate statistics，不公開 sealed
  input、expected、acceptable variants、converter output 或完整 rows。
- Batch9 已新增 100 筆 input-only cases，並完成 maintainer final decision；private
  expected 曾對齊 683 筆，miss review 後目前對齊 667 筆。Batch9 review artifacts：
  `docs/reports/holdout-input-pool-expansion-blind-v1-batch9-100-cases-2026-07-12.md`、
  `docs/reports/holdout-codex-first-pass-blind-v1-batch9-100-cases-2026-07-12.md`、
  `docs/reports/holdout-gemini-cli-advisory-blind-v1-batch9-100-cases-2026-07-12.md`、
  `docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch9-100-cases-2026-07-12.md`、
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch9-100-cases-2026-07-12.md`、
  `docs/reports/holdout-maintainer-final-decision-blind-v1-batch9-100-cases-2026-07-12.md`。
  分流結果為 69 筆 maintainer queue、31 筆 no-immediate-question；queue 中 30
  筆為 Codex/Gemini 差異，39 筆為 exact match 但需 policy review。
- Batch9 miss review 後已重跑 zhtw-only private sanity aggregate：
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch9-miss-review-2026-07-12.md`。
  實跑結果為 636/667 accepted、31 misses、accepted accuracy 約 95.35%；miss
  mix 為 1 筆 `baseline_guard`、2 筆 `candidate_gap`、28 筆
  `over_conversion_guard`。repo 內報告只含 aggregate statistics，不公開 sealed
  input、expected、acceptable variants、converter output 或完整 rows。
- 53 筆 miss 已整理成 sanitized classification，不公開 sealed values：
  `docs/reports/holdout-miss-classification-blind-v1-683-cases-2026-07-12.md`。
  Codex 建議為 31 筆保留 private holdout signal、16 筆轉 public regression
  candidate、6 筆 expected recheck；Gemini CLI policy review 通過且 0 筆分類變更建議：
  `docs/reports/holdout-gemini-policy-review-miss-classification-blind-v1-683-cases-2026-07-12.md`。
  需要 maintainer 確認的 22 筆已整理成 review packet：
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch9-miss-classification-2026-07-12.md`。
  Maintainer OK 後，6 筆加入 private acceptable variants、16 筆移出 sealed 並 promotion、31 筆保留 private holdout signal；final decision / sealed pool update / promotion gate / Gemini public promotion review 分別為
  `docs/reports/holdout-maintainer-final-decision-batch9-miss-classification-blind-v1-2026-07-12.md`、
  `docs/reports/holdout-sealed-pool-update-blind-v1-batch9-miss-review-2026-07-12.md`、
  `docs/reports/holdout-regression-promotion-gate-blind-v1-batch9-miss-review-2026-07-12.md`、
  `docs/reports/holdout-gemini-policy-review-batch9-miss-public-promotion-2026-07-12.md`。
- Batch10 已新增 100 筆 input-only cases，且 maintainer final decision 已寫入
  private expected。Batch10
  review artifacts：
  `docs/reports/holdout-input-pool-expansion-blind-v1-batch10-100-cases-2026-07-12.md`、
  `docs/reports/holdout-codex-first-pass-blind-v1-batch10-100-cases-2026-07-12.md`、
  `docs/reports/holdout-gemini-cli-advisory-blind-v1-batch10-100-cases-2026-07-12.md`、
  `docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch10-100-cases-2026-07-12.md`、
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch10-100-cases-2026-07-12.md`、
  `docs/reports/holdout-maintainer-final-decision-blind-v1-batch10-100-cases-2026-07-12.md`。
  分流結果為 44 筆 maintainer review queue、56 筆 no-immediate-question；queue 中
  17 筆為 Codex/Gemini 差異，27 筆為 exact match 但需 policy review。Batch10
  100 筆中 17 筆為 `human_adjudication`、83 筆為 `human_first_pass`。
- Batch10 後已重跑 zhtw-only private sanity aggregate：
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch10-2026-07-12.md`。
  實跑結果為 715/767 accepted、52 misses、accepted accuracy 約 93.22%；miss
  mix 為 4 筆 `baseline_guard`、19 筆 `candidate_gap`、29 筆
  `over_conversion_guard`。repo 內報告只含 aggregate statistics，不公開 sealed
  input、expected、acceptable variants、converter output 或完整 rows。
- 52 筆 miss 已整理成 sanitized classification，不公開 sealed values：
  `docs/reports/holdout-miss-classification-blind-v1-767-cases-2026-07-12.md`。
  Codex 建議為 32 筆保留 private holdout signal、16 筆轉 public regression
  candidate、4 筆 expected recheck；Gemini CLI policy review 通過且 0 筆分類變更建議：
  `docs/reports/holdout-gemini-policy-review-miss-classification-blind-v1-767-cases-2026-07-12.md`。
  需要 maintainer 確認的 20 筆已整理成 review packet：
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch10-miss-classification-2026-07-12.md`。
- Maintainer review OK 後已完成 batch10 miss final decision：
  `docs/reports/holdout-maintainer-final-decision-batch10-miss-classification-blind-v1-2026-07-13.md`。
  16 筆已移出 sealed 並加入 public regression；4 筆只在 private expected 加入
  acceptable variant；32 筆保留為 private holdout signal。更新後 private sanity 為
  719/751 accepted、32 misses、accepted accuracy 約 95.74%：
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch10-miss-review-2026-07-13.md`。
- 32 筆剩餘 private holdout signal 已整理成 sanitized summary，不含 sealed input、
  expected、acceptable、zhtw output 或完整 rows；本輪 0 筆需要 maintainer review、
  0 筆 public candidate、0 筆 expected recheck，且未改 converter、詞庫或 private
  expected：
  `docs/reports/holdout-remaining-signal-summary-blind-v1-after-batch10-miss-review-2026-07-13.md`。
- Gemini CLI 已使用 Vertex AI auth 與 `gemini-2.5-pro` 完成該 remaining-signal
  summary 的 policy review；結果為 policy passed、0 blocking findings、0 changes
  recommended：
  `docs/reports/holdout-gemini-policy-review-remaining-signal-blind-v1-after-batch10-miss-review-2026-07-13.md`。
- 已建立 32 筆 independent public reproduction seeds，只使用 sanitized metadata themes
  設計全新公開 input，不含 expected、acceptable、zhtw output 或 sealed rows；seed
  檔仍維持 input-only，不直接當 regression 或 tuning data：
  `benchmarks/accuracy/public-reproduction-seeds-v1.json`、
  `docs/reports/holdout-independent-public-reproduction-seeds-after-batch10-remaining-signal-2026-07-13.md`。
- 這 32 筆 public reproduction inputs 已完成 Codex first-pass expected advisory、
  Gemini independent advisory、Codex/Gemini diff review 與 maintainer confirmation
  packet；結果為 26 筆 primary exact match、6 筆 primary difference、17 筆進
  maintainer review packet、15 筆 no-immediate-question。Maintainer review OK 後，
  final decision 已確認 32 筆 public expected/acceptable，但尚未建立 public expected
  dataset、尚未進 regression，也沒有修改 converter 或詞庫：
  `docs/reports/public-reproduction-codex-first-pass-after-batch10-remaining-signal-2026-07-13.md`、
  `docs/reports/public-reproduction-gemini-advisory-after-batch10-remaining-signal-2026-07-13.md`、
  `docs/reports/public-reproduction-codex-gemini-diff-after-batch10-remaining-signal-2026-07-13.md`、
  `docs/reports/public-reproduction-maintainer-confirmation-after-batch10-remaining-signal-2026-07-13.md`、
  `docs/reports/public-reproduction-maintainer-final-decision-after-batch10-remaining-signal-2026-07-13.md`。
- Public reproduction promotion gate 已完成：經保守完整句 mapping 後，32 筆 final
  primary expected 皆與目前 zhtw output exact match，已全數 promotion 至
  `regression-v1.json`；0 筆暫留：
  `docs/reports/public-reproduction-promotion-gate-after-batch10-remaining-signal-2026-07-13.md`。
- Batch11 已新增 100 筆 input-only cases，公開 input pool 增至 851 筆；Codex
  first pass 與 Gemini CLI independent advisory 均已完成。兩者有 79 筆 primary
  exact match、21 筆差異；另有 29 筆 exact match 因低信心或高風險需 policy
  review，因此 maintainer packet 維持 50 筆一批。其餘 50 筆為
  no-immediate-question。Codex 對 21 筆差異已提出明確建議：18 筆採 Codex、3 筆採
  Gemini、0 筆無建議。Maintainer review OK 後，100 筆已寫入 private expected；
  其中 23 筆為 `human_adjudication`、77 筆為 `human_first_pass`，本輪未自動新增
  acceptable variants：
  `docs/reports/holdout-input-pool-expansion-blind-v1-batch11-100-cases-2026-07-13.md`、
  `docs/reports/holdout-codex-first-pass-blind-v1-batch11-100-cases-2026-07-13.md`、
  `docs/reports/holdout-gemini-cli-advisory-blind-v1-batch11-100-cases-2026-07-14.md`、
  `docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch11-100-cases-2026-07-14.md`、
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch11-100-cases-2026-07-14.md`、
  `docs/reports/holdout-maintainer-final-decision-blind-v1-batch11-100-cases-2026-07-14.md`。
  Batch11 後 zhtw-only private sanity 為 791/851 accepted、60 misses、accepted
  accuracy 約 92.95%；repo 內只保留 aggregate statistics：
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch11-2026-07-14.md`。
  60 筆 miss 已完成 Codex sanitized classification 與 Gemini policy review；32 筆
  既有 holdout signal 不翻案，整體建議為 35 筆保留 private signal、14 筆轉 public
  regression candidate、11 筆 expected/acceptable recheck。Gemini policy passed 且
  0 筆分類變更建議；這份 25 筆 maintainer packet 後續已由語意複核取代：
  `docs/reports/holdout-miss-classification-blind-v1-851-cases-2026-07-14.md`、
  `docs/reports/holdout-gemini-policy-review-miss-classification-blind-v1-851-cases-2026-07-14.md`、
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch11-miss-classification-2026-07-14.md`。
  Maintainer 指出可能矯枉過正後，25 筆 review cases 已改用「轉換語義正確性，不是
  house style」重新審查；Gemini 僅看 input-only cases，未看 Codex、現有 expected
  或 zhtw output。修訂建議為 4 筆 acceptable variant、10 筆 true public
  regression candidate、11 筆 strict private holdout signal；strict signal 不得用於
  tuning。19 筆已有 maintainer 明確偏好，其餘 6 筆也已確認 review OK。最終 4 筆
  加入 private acceptable variants、10 筆移出 sealed 並以保守完整句 mapping 加
  identity mapping 後 promotion、11 筆保留 strict private signal。更新後密封集為
  841 筆，private sanity 為 795/841 accepted、46 misses、accepted accuracy 約
  94.53%；這個變化同時包含 acceptable 修正與分母縮減，不應解讀為純模型能力增幅：
  `docs/reports/holdout-codex-semantic-reaudit-blind-v1-batch11-25-cases-2026-07-14.md`、
  `docs/reports/holdout-gemini-independent-semantic-reaudit-blind-v1-batch11-25-cases-2026-07-14.md`、
  `docs/reports/holdout-semantic-reaudit-diff-blind-v1-batch11-25-cases-2026-07-14.md`、
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch11-semantic-reaudit-6-cases-2026-07-14.md`、
  `docs/reports/holdout-maintainer-final-decision-blind-v1-batch11-semantic-reaudit-2026-07-14.md`、
  `docs/reports/holdout-regression-promotion-gate-blind-v1-batch11-semantic-reaudit-2026-07-14.md`、
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch11-semantic-reaudit-2026-07-14.md`。
  Gemini High-risk raw response 的自述模型版本與 CLI 指定的
  `gemini-2.5-pro` 不一致；已保留原始輸出並列為 metadata quality flag，不影響其
  advisory-only 身分。
- 50 筆 miss 已整理成 sanitized classification，不公開 sealed values：
  `docs/reports/holdout-miss-classification-blind-v1-515-cases-2026-07-10.md`。
  Codex 建議為 26 筆保留 private holdout signal、17 筆轉 public regression
  candidate、7 筆 expected recheck；maintainer 已確認這個分流。
- Gemini CLI 已對該 sanitized classification 做 policy review，確認政策通過且
  0 筆分類變更建議；本次 CLI 執行已 unset 無效的 `GEMINI_API_KEY`，改用本機
  可用認證：
  `docs/reports/holdout-gemini-policy-review-miss-classification-blind-v1-515-cases-2026-07-10.md`。
- 24 筆需要 maintainer 確認的項目已整理成 review packet，並已經 maintainer OK：
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch7-miss-classification-2026-07-10.md`。
- Batch7 miss classification final decision：
  `docs/reports/holdout-maintainer-final-decision-batch7-miss-classification-blind-v1-2026-07-10.md`。
- Batch7 miss review sealed pool update：
  `docs/reports/holdout-sealed-pool-update-blind-v1-batch7-miss-review-2026-07-10.md`。
- Batch7 miss review public promotion gate：
  `docs/reports/holdout-regression-promotion-gate-blind-v1-batch7-miss-review-2026-07-10.md`。
- Gemini public promotion policy review：
  `docs/reports/holdout-gemini-policy-review-batch7-miss-public-promotion-2026-07-10.md`。
- 26 筆剩餘 private holdout signal 繼續留在 sealed pool，不改 private expected
  或詞庫；目前只在 final decision 與 aggregate sanity 中記錄不含 sealed values 的
  統計。
- Batch6 的 24 筆剩餘 sealed signal sanitized 風險摘要是歷史附件：
  `docs/reports/holdout-remaining-signal-summary-blind-v1-after-batch6-miss-review-2026-07-10.md`。
- Gemini CLI 已對該 batch6 sanitized signal summary 做 policy review，確認未使用 sealed
  values 調詞庫，且未來若要調整必須先移出 sealed：
  `docs/reports/holdout-gemini-policy-review-remaining-signal-blind-v1-after-batch6-miss-review-2026-07-10.md`。

目前 private miss classification：

- repo 內只保存不含 expected/input/output/rows 的分類報告：
  `docs/reports/holdout-miss-classification-blind-v1-2026-07-08.md` 與
  `docs/reports/holdout-miss-classification-blind-v1-2026-07-08.json`。
- 43 筆 miss 中，22 筆建議先移出 sealed holdout 再轉為 public regression 候選。
- 7 筆保留作 sealed holdout 訊號，不得用來調詞庫。
- 14 筆需先重審 expected 或 acceptable variants。
- 5 筆 miss 帶有 idempotency follow-up flag；另有 1 筆 accepted 但非冪等，後續需獨立排查。
- `move_to_public_regression_candidate` 只是分類，不是修詞庫授權；實作前必須先完成 holdout
  移出、公開 regression/backlog 紀錄、再補測試。

目前 expected/acceptable recheck：

- `docs/reports/holdout-expected-recheck-blind-v1-2026-07-09.md` 與
  `docs/reports/holdout-expected-recheck-blind-v1-2026-07-09.json` 記錄 14 筆
  `requires_expected_recheck` 的處理結果。
- 12 筆確認為有效台灣用語 variant，已只在 private expected 中加入 acceptable variant。
- 2 筆維持 strict primary expected，仍是 sealed holdout miss，不得直接調詞庫。
- 此公開 recheck 報告不含 expected、acceptable variants、input、converter output 或完整 rows。
- recheck 後當時 sealed sanity 為 69/78 accepted、9 misses；第二批 promotion 後當時為
  69/73 accepted、4 misses。最新 161 筆 sanity 見前面的 private benchmark sanity check。

早期 remaining miss classification：

- `docs/reports/holdout-remaining-miss-classification-blind-v1-2026-07-09.md` 與
  `docs/reports/holdout-remaining-miss-classification-blind-v1-2026-07-09.json` 記錄剩餘
  9 筆 sealed miss 的處理建議。
- 5 筆已在第二批先移出 sealed holdout，再建立 public regression candidate 並 promotion。
- 4 筆保留作 sealed holdout 訊號，不得調詞庫。
- 這份公開報告不含 expected、acceptable variants、input、converter output 或完整 rows。

目前 remaining-40 final review：

- `docs/reports/holdout-remaining-40-miss-classification-blind-v1-2026-07-09.md` 與
  `docs/reports/holdout-remaining-40-miss-classification-blind-v1-2026-07-09.json` 記錄
  40 筆 miss 的 sanitized classification。
- `docs/reports/holdout-maintainer-final-decision-remaining-40-miss-classification-blind-v1-2026-07-09.json`
  記錄 maintainer final decision：3 筆加入 private acceptable variants、18 筆移出 sealed
  並 promotion、19 筆保留為 sealed holdout signal。
- final review 後 private benchmark sanity 為 219/238 accepted、19 misses、accepted
  accuracy 92.02%。公開 sanity 報告只含 aggregate statistics，不含 expected、input、
  converter output 或完整 rows。

目前 holdout-to-regression promotion：

- `benchmarks/accuracy/holdout-regression-candidates-v1.json` 公開 219 筆已移出的 candidate。
- `docs/reports/holdout-regression-promotion-gate-blind-v1-2026-07-09.json` 顯示第一批
  22/22 promotion-ready，zhtw output 與 expected 完全一致且 expected/output 皆冪等。
- `docs/reports/holdout-regression-promotion-gate-blind-v1-batch2-2026-07-09.json` 顯示第二批
  5/5 promotion-ready，zhtw output 與 expected 完全一致且 expected/output 皆冪等。
- `docs/reports/holdout-regression-promotion-gate-blind-v1-batch3-2026-07-09.json` 顯示第三批
  39/39 promotion-ready，zhtw output 與 expected 完全一致且 expected/output 皆冪等。
- `docs/reports/holdout-regression-promotion-gate-blind-v1-batch4-recheck-2026-07-09.json` 顯示
  batch4 recheck 5/5 promotion-ready，zhtw output 與 expected 完全一致且 expected/output 皆冪等。
- `docs/reports/holdout-regression-promotion-gate-blind-v1-remaining-40-final-review-2026-07-09.json`
  顯示 remaining-40 final review 18/18 promotion-ready，zhtw output 與 expected
  完全一致且 expected/output 皆冪等。
- `docs/reports/holdout-regression-promotion-gate-blind-v1-338-miss-review-2026-07-09.json`
  顯示 338-case miss review 12/12 promotion-ready，zhtw output 與 expected
  完全一致且 expected/output 皆冪等。
- `docs/reports/holdout-regression-promotion-gate-blind-v1-batch6-miss-review-2026-07-10.json`
  顯示 batch6 miss review 11/11 promotion-ready，zhtw output 與 expected
  完全一致且 expected/output 皆冪等。
- `docs/reports/holdout-regression-promotion-gate-blind-v1-batch7-miss-review-2026-07-10.json`
  顯示 batch7 miss review 17/17 promotion-ready，zhtw output 與 expected
  完全一致且 expected/output 皆冪等。
- `docs/reports/holdout-regression-promotion-gate-blind-v1-batch8-miss-review-2026-07-11.json`
  顯示 batch8 miss review 15/15 promotion-ready，zhtw output 與 expected
  完全一致且 expected/output 皆冪等。
- `docs/reports/holdout-regression-promotion-gate-blind-v1-batch9-miss-review-2026-07-12.json`
  顯示 batch9 miss review 16/16 promotion-ready，zhtw output 與 expected
  完全一致且 expected/output 皆冪等。
- `docs/reports/holdout-regression-promotion-gate-blind-v1-batch10-miss-review-2026-07-13.json`
  顯示 batch10 miss review 16/16 promotion-ready，zhtw output 與 expected
  完全一致且 expected/output 皆冪等。
- `docs/reports/holdout-regression-promotion-gate-blind-v1-batch11-semantic-reaudit-2026-07-14.json`
  顯示 batch11 semantic re-audit 10/10 promotion-ready，採完整句 mapping 與 identity
  mapping，zhtw output 與 expected 完全一致。
- `docs/reports/holdout-regression-promotion-gate-blind-v1-batch12-miss-review-2026-07-14.json`
  顯示 batch12 miss review 11/11 promotion-ready，採完整句 mapping 與 identity
  mapping，zhtw output 與 expected 完全一致且 expected 冪等。
- `docs/reports/holdout-regression-promotion-gate-blind-v1-batch13-miss-review-2026-07-14.json`
  顯示 batch13 miss review 22/22 promotion-ready，採完整句 mapping 與 identity
  mapping，zhtw output 與 expected 完全一致且 expected 冪等。
- `regression-v1.json` 已加入這 219 筆，classification 為
  `holdout_regression_promoted`。
- 詞庫策略是完整句 mapping + 完整句 identity mapping，不新增裸詞全域轉換。

禁止事項：

- 不得用 zhtw、OpenCC、zhconv 或 competitor majority vote 產生 expected。
- 不得在 expected sealed 期間用 blind miss 調詞庫；若必須修 bug，該 case 要先移出
  sealed set，改列 public regression 候選。
- expected 公開後，該資料集降級為 public benchmark，後續 blind 宣稱必須使用新的
  sealed set。

## PR 檢查清單

精準度相關 PR 應回答：

- 這次修了哪些人工確認錯轉？
- 每個修正是否有 golden 或 corpus regression？
- 是否有裸詞或子字串過度轉換風險？
- 是否補了 identity mapping？
- release gate 是否全綠？
- OpenCC report-only 數字若下降，是否只處理高信心項目？
