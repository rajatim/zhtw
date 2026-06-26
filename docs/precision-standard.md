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
| Golden battery | 225 句，且一次轉換與二次轉換都必須通過 | release gate |
| 精選 corpus | 21 筆人工 expected，且一次轉換與二次轉換都必須通過 | release gate |
| 手工詞庫 target 冪等性 | 0 issue | release gate |
| `zhtw validate` | 0 blocking issue | release gate |
| OpenCC 匯入詞庫 target 非冪等 | 404 issue | report-only |

OpenCC 匯入詞庫的 404 筆不是 release blocker。裡麵包含人名、古文、罕見詞與語境詞；硬追歸零會提高錯轉風險。

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
- 精選 corpus 從 21 筆擴到至少 100 筆。
- `news`、`tech`、`social`、`wiki`、`regressions` 每類至少 20 筆人工 expected。
- 手工詞庫 target 冪等性維持 0 issue。

中期目標：

- 精選 corpus 至少 300 筆，覆蓋常見 IT、CLI、文件、新聞、社群語氣。
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

## PR 檢查清單

精準度相關 PR 應回答：

- 這次修了哪些人工確認錯轉？
- 每個修正是否有 golden 或 corpus regression？
- 是否有裸詞或子字串過度轉換風險？
- 是否補了 identity mapping？
- release gate 是否全綠？
- OpenCC report-only 數字若下降，是否只處理高信心項目？
