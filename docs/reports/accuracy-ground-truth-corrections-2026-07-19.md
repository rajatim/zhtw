# Accuracy Ground-truth Corrections（2026-07-19）

## 決策

- Maintainer：`tim`
- 決策：`fix_all`
- 審核方式：Codex 全量審查 → Gemini 2.5 Pro 獨立審查 → maintainer adjudication
- Approval policy：`single_human_with_ai_advisory_and_authoritative_sources`
- 歷史報告不回寫；更新目前詞庫、annotation、holdout candidates 與 public regression。

## Review 範圍

- 共 474 筆新增非 identity mapping。
- Formal 60、IT 238、Mixed 9、Social 45、UI 122。
- 更正 16 筆 dictionary mappings 與 public regression。
- 其中包含 6 筆 annotation、9 筆 holdout regression、1 筆 public reproduction。
- 移除 7 筆會接受舊錯譯或與新 expected 重複的 acceptable variants。

## 核心修正

- `密鑰／配置檔／遷移指令碼／鉤子` → `金鑰／設定檔／移轉指令碼／掛鉤`
- `儲存桶／雜湊值` → `儲存貯體／檢查碼`
- `返回首頁／倒序／分頁器／點擊` → `回到首頁／由新到舊／分頁控制項／點選`
- `修剪空白／截斷較舊訊息` → `移除前後空白／移除較舊訊息`
- 統一使用 `統計資料` 與 `發布`。

完整 case ID、理由及 Gemini 採納／駁回紀錄位於同名 JSON 報告。
