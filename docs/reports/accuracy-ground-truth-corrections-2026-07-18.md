# Accuracy Ground-truth Corrections（2026-07-18）

## 決策

- Maintainer：`tim`
- 決策：修正 Codex review 與 Gemini 獨立複審確認的台灣繁體／IT 術語錯誤。
- 審核方式：`single_human_with_ai_advisory_and_authoritative_sources`
- 歷史報告不回寫；只更新目前詞庫、annotation backlog、holdout regression candidates 與 public regression。
- 移除 4 筆仍會接受「要求識別碼／排查日誌／派送」等舊錯譯的 acceptable variants。

## 範圍

- 14 筆 dictionary source mappings。
- 9 筆 annotation expected。
- 14 筆 public regression expected。
- 0 筆 dictionary-only phrase。

## 核心修正

- `要求簽章／要求逾時` → `請求簽章／請求逾時`
- `配置項／設定映射／校驗和` → `設定項目／設定對應／檢查碼`
- `令牌桶／回復步驟／灰度發佈` → `權杖桶／復原步驟／漸進式發布`
- `續約憑證` → `更新憑證`
- `排查日誌` → `透過記錄檔追查問題`
- `遷移腳本／回滾` → `移轉指令碼／復原`
- `派送功能開關` → `發布功能開關`

完整 case ID 與依據記錄於同名 JSON 報告。
