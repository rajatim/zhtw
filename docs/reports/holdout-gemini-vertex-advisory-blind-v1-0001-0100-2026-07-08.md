<!-- zhtw:disable -->
# Holdout Gemini Vertex Advisory (2026-07-08)

Dataset: `blind-v1`
Inputs: `benchmarks/accuracy/blind-v1.inputs.json`
Codex advisory: `docs/reports/holdout-codex-first-pass-blind-v1-0001-0100-2026-07-08.json`
Raw JSON: `docs/reports/holdout-gemini-vertex-advisory-blind-v1-0001-0100-2026-07-08.json`
Reviewer: `gemini_vertex`
Model: `gemini-2.5-flash`

## Policy

- Gemini saw only the input cases, not Codex recommendations.
- This report is advisory only.
- It is not ground truth and must not populate `blind-v1.expected.json` directly.
- Maintainer confirmation is required before any expected value becomes human decision.

## Summary

- Cases: 100
- Exact matches with Codex: 70
- Differences from Codex: 30
- Needs maintainer review: 59

Gemini confidence:

- `high`: 100

Domain distribution:

- `formal`: 15
- `high_risk`: 10
- `it`: 25
- `llm`: 15
- `social`: 15
- `ui`: 20

## Maintainer Review Queue

- `blind-it-0002` (it, match, Codex medium, Gemini high)
- `blind-it-0003` (it, different, Codex high, Gemini high)
- `blind-it-0004` (it, match, Codex medium, Gemini high)
- `blind-it-0005` (it, match, Codex medium, Gemini high)
- `blind-it-0006` (it, match, Codex high, Gemini high)
- `blind-it-0007` (it, match, Codex medium, Gemini high)
- `blind-it-0008` (it, different, Codex high, Gemini high)
- `blind-it-0009` (it, different, Codex high, Gemini high)
- `blind-it-0010` (it, match, Codex medium, Gemini high)
- `blind-it-0011` (it, different, Codex high, Gemini high)
- `blind-it-0012` (it, different, Codex medium, Gemini high)
- `blind-it-0014` (it, different, Codex high, Gemini high)
- `blind-it-0015` (it, different, Codex high, Gemini high)
- `blind-it-0016` (it, different, Codex high, Gemini high)
- `blind-it-0017` (it, different, Codex medium, Gemini high)
- `blind-it-0018` (it, different, Codex medium, Gemini high)
- `blind-it-0019` (it, different, Codex medium, Gemini high)
- `blind-it-0020` (it, different, Codex high, Gemini high)
- `blind-it-0021` (it, different, Codex high, Gemini high)
- `blind-it-0022` (it, different, Codex high, Gemini high)
- `blind-it-0023` (it, different, Codex high, Gemini high)
- `blind-it-0025` (it, different, Codex high, Gemini high)
- `blind-ui-0001` (ui, different, Codex high, Gemini high)
- `blind-ui-0004` (ui, different, Codex high, Gemini high)
- `blind-ui-0006` (ui, different, Codex high, Gemini high)
- `blind-ui-0008` (ui, different, Codex medium, Gemini high)
- `blind-ui-0010` (ui, different, Codex high, Gemini high)
- `blind-ui-0011` (ui, different, Codex high, Gemini high)
- `blind-ui-0012` (ui, match, Codex medium, Gemini high)
- `blind-ui-0017` (ui, match, Codex high, Gemini high)
- `blind-ui-0018` (ui, different, Codex high, Gemini high)
- `blind-ui-0020` (ui, match, Codex medium, Gemini high)
- `blind-llm-0001` (llm, different, Codex high, Gemini high)
- `blind-llm-0002` (llm, different, Codex high, Gemini high)
- `blind-llm-0005` (llm, match, Codex high, Gemini high)
- `blind-llm-0006` (llm, match, Codex high, Gemini high)
- `blind-llm-0010` (llm, different, Codex high, Gemini high)
- `blind-llm-0011` (llm, match, Codex high, Gemini high)
- `blind-llm-0012` (llm, different, Codex high, Gemini high)
- `blind-llm-0013` (llm, different, Codex high, Gemini high)
- `blind-formal-0004` (formal, match, Codex high, Gemini high)
- `blind-formal-0007` (formal, match, Codex high, Gemini high)
- `blind-formal-0010` (formal, match, Codex medium, Gemini high)
- `blind-formal-0012` (formal, different, Codex medium, Gemini high)
- `blind-formal-0015` (formal, match, Codex high, Gemini high)
- `blind-social-0007` (social, match, Codex medium, Gemini high)
- `blind-social-0009` (social, match, Codex high, Gemini high)
- `blind-social-0011` (social, match, Codex high, Gemini high)
- `blind-social-0015` (social, different, Codex medium, Gemini high)
- `blind-high-risk-0001` (high_risk, match, Codex high, Gemini high)
- `blind-high-risk-0002` (high_risk, match, Codex high, Gemini high)
- `blind-high-risk-0003` (high_risk, match, Codex high, Gemini high)
- `blind-high-risk-0004` (high_risk, match, Codex high, Gemini high)
- `blind-high-risk-0005` (high_risk, match, Codex high, Gemini high)
- `blind-high-risk-0006` (high_risk, match, Codex high, Gemini high)
- `blind-high-risk-0007` (high_risk, match, Codex high, Gemini high)
- `blind-high-risk-0008` (high_risk, match, Codex high, Gemini high)
- `blind-high-risk-0009` (high_risk, match, Codex medium, Gemini high)
- `blind-high-risk-0010` (high_risk, match, Codex high, Gemini high)

## Comparisons

### blind-it-0001：match

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
这个函数会抛出异常，请在调用前检查返回值。
```

Codex expected:

```text
這個函式會拋出例外，請在呼叫前檢查回傳值。
```

Gemini expected:

```text
這個函式會拋出例外，請在呼叫前檢查回傳值。
```

Gemini acceptable variants:

```text
這個函數會拋出異常，請在呼叫前檢查回傳值。
這個函式會拋出異常，請在呼叫前檢查回傳值。
這個函數會拋出例外，請在呼叫前檢查回傳值。
```

Gemini notes:

```text
將「这个」轉為「這個」，「函数」轉為「函式」（IT術語），「抛出异常」轉為「拋出例外」（IT術語，臺灣IT領域常用「例外」），「调用」轉為「呼叫」（IT術語），「返回值」轉為「回傳值」（IT術語）。
```

### blind-it-0002：match

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
用户登录后，服务器会返回访问令牌和刷新令牌。
```

Codex expected:

```text
使用者登入後，伺服器會回傳存取權杖和重新整理權杖。
```

Gemini expected:

```text
使用者登入後，伺服器會回傳存取權杖和重新整理權杖。
```

Gemini acceptable variants:

```text
用戶登入後，伺服器會回傳存取權杖和刷新權杖。
使用者登入後，伺服器會返回存取權杖和刷新權杖。
```

Gemini notes:

```text
將「用户」轉為「使用者」（UI/IT術語），「登录」轉為「登入」（UI/IT術語），「服务器」轉為「伺服器」（IT術語），「返回」轉為「回傳」（IT術語），「访问令牌」轉為「存取權杖」（IT術語），「刷新令牌」轉為「重新整理權杖」（IT術語）。
```

### blind-it-0003：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
如果缓存过期，客户端应该重新请求配置文件。
```

Codex expected:

```text
如果快取過期，客戶端應該重新請求設定檔。
```

Gemini expected:

```text
如果快取過期，用戶端應該重新要求組態檔。
```

Gemini acceptable variants:

```text
如果緩存過期，用戶端應該重新請求配置文件。
如果快取過期，用戶端應該重新請求配置文件。
如果緩存過期，用戶端應該重新要求組態檔。
```

Gemini notes:

```text
將「缓存」轉為「快取」（IT術語），「客户端」轉為「用戶端」（IT術語），「应该」轉為「應該」，「重新请求」轉為「重新要求」（IT術語），「配置文件」轉為「組態檔」（IT術語）。
```

### blind-it-0004：match

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
部署脚本需要读取环境变量里的数据库凭证。
```

Codex expected:

```text
部署指令碼需要讀取環境變數裡的資料庫憑證。
```

Gemini expected:

```text
部署指令碼需要讀取環境變數裡的資料庫憑證。
```

Gemini acceptable variants:

```text
部署腳本需要讀取環境變數裡的資料庫憑證。
部署指令碼需要讀取環境變數裡的數據庫憑證。
```

Gemini notes:

```text
將「脚本」轉為「指令碼」（IT術語），「读取」轉為「讀取」，「环境变量」轉為「環境變數」（IT術語），「数据库」轉為「資料庫」（IT術語），「凭证」轉為「憑證」（IT術語）。
```

### blind-it-0005：match

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
这个接口会分页返回订单列表，每页最多五十条。
```

Codex expected:

```text
這個介面會分頁回傳訂單清單，每頁最多五十筆。
```

Gemini expected:

```text
這個介面會分頁回傳訂單清單，每頁最多五十筆。
```

Gemini acceptable variants:

```text
這個接口會分頁回傳訂單列表，每頁最多五十條。
這個介面會分頁回傳訂單列表，每頁最多五十條。
這個接口會分頁回傳訂單清單，每頁最多五十條。
```

Gemini notes:

```text
將「这个」轉為「這個」，「接口」轉為「介面」（IT術語），「返回」轉為「回傳」（IT術語），「订单列表」轉為「訂單清單」（UI/IT術語），「五十条」轉為「五十筆」（臺灣常用量詞）。
```

### blind-it-0006：match

- Domain: `it`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
当连接超时发生时，请不要重复提交表单。
```

Codex expected:

```text
當連線逾時發生時，請不要重複送出表單。
```

Gemini expected:

```text
當連線逾時發生時，請不要重複送出表單。
```

Gemini acceptable variants:

```text
當連接超時發生時，請不要重複提交表單。
當連線超時發生時，請不要重複提交表單。
當連接逾時發生時，請不要重複提交表單。
當連線超時發生時，請不要重複送出表單。
當連接逾時發生時，請不要重複送出表單。
```

Gemini notes:

```text
將「连接」轉為「連線」（IT術語），「超时」轉為「逾時」（IT術語），「请」轉為「請」，「重复」轉為「重複」，「提交」轉為「送出」（UI/IT術語）。
```

### blind-it-0007：match

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
我们在后台任务里记录每一次重试的原因。
```

Codex expected:

```text
我們在背景工作裡記錄每一次重試的原因。
```

Gemini expected:

```text
我們在背景工作裡記錄每一次重試的原因。
```

Gemini acceptable variants:

```text
我們在後台任務裡記錄每一次重試的原因。
我們在後台工作裡記錄每一次重試的原因。
```

Gemini notes:

```text
將「我们」轉為「我們」，「后台任务」轉為「背景工作」（IT術語），「里」轉為「裡」，「记录」轉為「記錄」。
```

### blind-it-0008：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
新版 SDK 支持批量上传文件和取消请求。
```

Codex expected:

```text
新版 SDK 支援批次上傳檔案和取消請求。
```

Gemini expected:

```text
新版 SDK 支援批次上傳檔案和取消要求。
```

Gemini acceptable variants:

```text
新版 SDK 支持批量上傳文件和取消請求。
新版 SDK 支援批量上傳文件和取消請求。
新版 SDK 支持批次上傳檔案和取消請求。
新版 SDK 支持批量上傳檔案和取消要求。
新版 SDK 支援批量上傳檔案和取消要求。
```

Gemini notes:

```text
將「支持」轉為「支援」（IT術語），「批量上传」轉為「批次上傳」（IT術語），「文件」轉為「檔案」（IT術語），「请求」轉為「要求」（IT術語）。
```

### blind-it-0009：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
这个命令会覆盖本地设置，请先备份原始文件。
```

Codex expected:

```text
這個命令會覆蓋本機設定，請先備份原始檔案。
```

Gemini expected:

```text
這個命令會覆寫本機設定，請先備份原始檔案。
```

Gemini acceptable variants:

```text
這個命令會覆蓋本地設置，請先備份原始文件。
這個命令會覆寫本地設置，請先備份原始文件。
這個命令會覆蓋本機設定，請先備份原始文件。
這個命令會覆蓋本地設置，請先備份原始檔案。
這個命令會覆寫本地設置，請先備份原始檔案。
```

Gemini notes:

```text
將「这个」轉為「這個」，「覆盖」轉為「覆寫」（IT術語），「本地设置」轉為「本機設定」（IT術語），「请」轉為「請」，「备份」轉為「備份」，「文件」轉為「檔案」（IT術語）。
```

### blind-it-0010：match

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
管理员可以在控制台停用异常的 API 密钥。
```

Codex expected:

```text
管理員可以在主控台停用異常的 API 金鑰。
```

Gemini expected:

```text
管理員可以在主控台停用異常的 API 金鑰。
```

Gemini acceptable variants:

```text
管理員可以在控制台停用異常的 API 密鑰。
管理員可以在主控台停用異常的 API 密鑰。
```

Gemini notes:

```text
將「管理员」轉為「管理員」，「控制台」轉為「主控台」（IT術語），「异常」轉為「異常」，「密钥」轉為「金鑰」（IT術語）。
```

### blind-it-0011：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
日志里显示用户权限不足，无法删除这个资源。
```

Codex expected:

```text
日誌裡顯示使用者權限不足，無法刪除這個資源。
```

Gemini expected:

```text
記錄檔裡顯示使用者權限不足，無法刪除這個資源。
```

Gemini acceptable variants:

```text
日誌裡顯示用戶權限不足，無法刪除這個資源。
記錄檔裡顯示用戶權限不足，無法刪除這個資源。
日誌裡顯示使用者權限不足，無法刪除這個資源。
```

Gemini notes:

```text
將「日志」轉為「記錄檔」（IT術語），「里」轉為「裡」，「用户」轉為「使用者」（UI/IT術語），「显示」轉為「顯示」，「这个」轉為「這個」。
```

### blind-it-0012：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
如果消息队列阻塞，消费者会延迟处理通知。
```

Codex expected:

```text
如果訊息佇列阻塞，消費者會延遲處理通知。
```

Gemini expected:

```text
如果訊息佇列阻塞，取用者會延遲處理通知。
```

Gemini acceptable variants:

```text
如果消息隊列阻塞，消費者會延遲處理通知。
如果訊息隊列阻塞，消費者會延遲處理通知。
如果消息佇列阻塞，消費者會延遲處理通知。
如果消息隊列阻塞，取用者會延遲處理通知。
如果訊息隊列阻塞，取用者會延遲處理通知。
```

Gemini notes:

```text
將「消息队列」轉為「訊息佇列」（IT術語），「消费者」轉為「取用者」（IT術語）。
```

### blind-it-0013：match

- Domain: `it`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
这个字段只接受小写字母和数字。
```

Codex expected:

```text
這個欄位只接受小寫字母和數字。
```

Gemini expected:

```text
這個欄位只接受小寫字母和數字。
```

Gemini acceptable variants:

```text
這個字段只接受小寫字母和數字。
```

Gemini notes:

```text
將「这个」轉為「這個」，「字段」轉為「欄位」（IT術語）。
```

### blind-it-0014：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
合并请求通过检查后，机器人会自动发布预览版本。
```

Codex expected:

```text
合併請求通過檢查後，機器人會自動發布預覽版本。
```

Gemini expected:

```text
合併要求通過檢查後，機器人會自動發佈預覽版本。
```

Gemini acceptable variants:

```text
合併請求通過檢查後，機器人會自動發布預覽版本。
合併要求通過檢查後，機器人會自動發布預覽版本。
合併請求通過檢查後，機器人會自動發佈預覽版本。
```

Gemini notes:

```text
將「合并请求」轉為「合併要求」（IT術語），「机器人」轉為「機器人」，「发布」轉為「發佈」。
```

### blind-it-0015：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
你可以用配置文件指定默认语言和时区。
```

Codex expected:

```text
你可以用設定檔指定預設語言和時區。
```

Gemini expected:

```text
你可以用組態檔指定預設語言和時區。
```

Gemini acceptable variants:

```text
你可以用配置文件指定默認語言和時區。
你可以用組態檔指定默認語言和時區。
你可以用配置文件指定預設語言和時區。
```

Gemini notes:

```text
將「配置文件」轉為「組態檔」（IT術語），「默认语言」轉為「預設語言」（IT術語）。
```

### blind-it-0016：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
数据迁移完成后，请验证索引是否已经重建。
```

Codex expected:

```text
資料遷移完成後，請驗證索引是否已經重建。
```

Gemini expected:

```text
資料移轉完成後，請驗證索引是否已經重建。
```

Gemini acceptable variants:

```text
數據遷移完成後，請驗證索引是否已經重建。
資料遷移完成後，請驗證索引是否已經重建。
數據移轉完成後，請驗證索引是否已經重建。
```

Gemini notes:

```text
將「数据」轉為「資料」（IT術語），「迁移」轉為「移轉」（IT術語），「请」轉為「請」。
```

### blind-it-0017：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
这个端点需要签名，否则网关会拒绝请求。
```

Codex expected:

```text
這個端點需要簽章，否則閘道會拒絕請求。
```

Gemini expected:

```text
這個端點需要簽章，否則閘道會拒絕要求。
```

Gemini acceptable variants:

```text
這個端點需要簽名，否則網關會拒絕請求。
這個端點需要簽章，否則網關會拒絕請求。
這個端點需要簽名，否則閘道會拒絕請求。
這個端點需要簽名，否則網關會拒絕要求。
這個端點需要簽章，否則網關會拒絕要求。
```

Gemini notes:

```text
將「这个」轉為「這個」，「端点」轉為「端點」（IT術語），「签名」轉為「簽章」（IT術語），「网关」轉為「閘道」（IT術語），「请求」轉為「要求」（IT術語）。
```

### blind-it-0018：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
我们把支付回调放进独立的工作线程处理。
```

Codex expected:

```text
我們把付款回呼放進獨立的工作執行緒處理。
```

Gemini expected:

```text
我們把支付回呼放進獨立的工作執行緒處理。
```

Gemini acceptable variants:

```text
我們把支付回調放進獨立的工作線程處理。
我們把支付回呼放進獨立的工作線程處理。
```

Gemini notes:

```text
將「我们」轉為「我們」，「回调」轉為「回呼」（IT術語），「放进」轉為「放進」，「工作线程」轉為「工作執行緒」（IT術語）。
```

### blind-it-0019：different

- Domain: `it`
- Risk: `over_conversion_guard`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
发生冲突时，客户端应该重新下载最新记录。
```

Codex expected:

```text
發生衝突時，客戶端應該重新下載最新記錄。
```

Gemini expected:

```text
發生衝突時，用戶端應該重新下載最新記錄。
```

Gemini acceptable variants:

```text
發生衝突時，客戶端應該重新下載最新記錄。
發生衝突時，用戶端應該重新下載最新紀錄。
```

Gemini notes:

```text
將「发生」轉為「發生」，「客户端」轉為「用戶端」（IT術語），「应该」轉為「應該」。
```

### blind-it-0020：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
请在测试环境启用详细日志，线上环境保持关闭。
```

Codex expected:

```text
請在測試環境啟用詳細日誌，正式環境保持關閉。
```

Gemini expected:

```text
請在測試環境啟用詳細記錄檔，線上環境保持關閉。
```

Gemini acceptable variants:

```text
請在測試環境啟用詳細日誌，線上環境保持關閉。
請在測試環境啟用詳細記錄檔，線上環境保持關閉。
```

Gemini notes:

```text
將「请」轉為「請」，「日志」轉為「記錄檔」（IT術語），「线上环境」轉為「線上環境」（IT術語）。
```

### blind-it-0021：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
压缩包解开后，把二进制文件移动到系统路径。
```

Codex expected:

```text
壓縮檔解開後，把二進位檔案移動到系統路徑。
```

Gemini expected:

```text
壓縮檔解壓縮後，把二進位檔案移動到系統路徑。
```

Gemini acceptable variants:

```text
壓縮包解開後，把二進位文件移動到系統路徑。
壓縮檔解開後，把二進位文件移動到系統路徑。
壓縮包解壓縮後，把二進位文件移動到系統路徑。
壓縮包解開後，把二進位檔案移動到系統路徑。
壓縮檔解開後，把二進位檔案移動到系統路徑。
```

Gemini notes:

```text
將「压缩包」轉為「壓縮檔」（IT術語），「解开」轉為「解壓縮」（IT術語），「二进制文件」轉為「二進位檔案」（IT術語）。
```

### blind-it-0022：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
这个插件会在保存文件时格式化代码。
```

Codex expected:

```text
這個外掛會在儲存檔案時格式化程式碼。
```

Gemini expected:

```text
這個外掛程式會在儲存檔案時格式化程式碼。
```

Gemini acceptable variants:

```text
這個插件會在保存文件時格式化代碼。
這個外掛程式會在保存文件時格式化代碼。
這個插件會在儲存檔案時格式化代碼。
這個插件會在保存文件時格式化程式碼。
這個外掛程式會在保存文件時格式化程式碼。
```

Gemini notes:

```text
將「这个」轉為「這個」，「插件」轉為「外掛程式」（IT術語），「保存文件」轉為「儲存檔案」（IT術語），「代码」轉為「程式碼」（IT術語）。
```

### blind-it-0023：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
任务失败后，调度器会在五分钟后再次尝试。
```

Codex expected:

```text
任務失敗後，排程器會在五分鐘後再次嘗試。
```

Gemini expected:

```text
工作失敗後，排程器會在五分鐘後再次嘗試。
```

Gemini acceptable variants:

```text
任務失敗後，調度器會在五分鐘後再次嘗試。
工作失敗後，調度器會在五分鐘後再次嘗試。
任務失敗後，排程器會在五分鐘後再次嘗試。
```

Gemini notes:

```text
將「任务」轉為「工作」（IT術語），「调度器」轉為「排程器」（IT術語），「五分钟」轉為「五分鐘」。
```

### blind-it-0024：match

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
请确认防火墙允许代理服务器访问内部服务。
```

Codex expected:

```text
請確認防火牆允許代理伺服器存取內部服務。
```

Gemini expected:

```text
請確認防火牆允許代理伺服器存取內部服務。
```

Gemini acceptable variants:

```text
請確認防火牆允許代理服務器訪問內部服務。
請確認防火牆允許代理伺服器訪問內部服務。
```

Gemini notes:

```text
將「请」轉為「請」，「确认」轉為「確認」，「代理服务器」轉為「代理伺服器」（IT術語），「访问」轉為「存取」（IT術語）。
```

### blind-it-0025：different

- Domain: `it`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
如果版本号不匹配，安装程序会停止更新。
```

Codex expected:

```text
如果版本號不相符，安裝程式會停止更新。
```

Gemini expected:

```text
如果版本號不符，安裝程式會停止更新。
```

Gemini acceptable variants:

```text
如果版本號不匹配，安裝程序會停止更新。
```

Gemini notes:

```text
將「版本号」轉為「版本號」，「不匹配」轉為「不符」（IT/正式用語），「安装程序」轉為「安裝程式」（IT術語）。
```

### blind-ui-0001：different

- Domain: `ui`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
点击保存后，页面会显示上次更新时间。
```

Codex expected:

```text
點選儲存後，頁面會顯示上次更新時間。
```

Gemini expected:

```text
點擊儲存後，頁面會顯示上次更新時間。
```

Gemini acceptable variants:

```text
點擊保存後，頁面會顯示上次更新時間。
點擊儲存後，頁面會顯示上次更新時間。
```

Gemini notes:

```text
將「点击」轉為「點擊」（UI術語），「保存」轉為「儲存」（UI術語），「页面」轉為「頁面」，「显示」轉為「顯示」。
```

### blind-ui-0002：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
请输入验证码，系统会发送简讯到你的手机。
```

Codex expected:

```text
請輸入驗證碼，系統會傳送簡訊到你的手機。
```

Gemini expected:

```text
請輸入驗證碼，系統會傳送簡訊到你的手機。
```

Gemini acceptable variants:

```text
請輸入驗證碼，系統會發送簡訊到你的手機。
```

Gemini notes:

```text
將「请」轉為「請」，「发送」轉為「傳送」。
```

### blind-ui-0003：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
你可以在设置页面关闭桌面通知。
```

Codex expected:

```text
你可以在設定頁面關閉桌面通知。
```

Gemini expected:

```text
你可以在設定頁面關閉桌面通知。
```

Gemini acceptable variants:

```text
你可以在設置頁面關閉桌面通知。
```

Gemini notes:

```text
將「设置页面」轉為「設定頁面」（UI術語）。
```

### blind-ui-0004：different

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
拖动滑块调整音量，然后点击应用。
```

Codex expected:

```text
拖曳滑桿調整音量，然後點選套用。
```

Gemini expected:

```text
拖曳滑桿調整音量，然後點擊套用。
```

Gemini acceptable variants:

```text
拖動滑塊調整音量，然後點擊應用。
拖曳滑塊調整音量，然後點擊應用。
拖動滑桿調整音量，然後點擊應用。
拖動滑塊調整音量，然後點擊套用。
拖曳滑塊調整音量，然後點擊套用。
```

Gemini notes:

```text
將「拖动」轉為「拖曳」（UI術語），「滑块」轉為「滑桿」（UI術語），「点击」轉為「點擊」（UI術語），「应用」轉為「套用」（UI術語）。
```

### blind-ui-0005：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
搜索结果为空时，显示重置筛选按钮。
```

Codex expected:

```text
搜尋結果為空時，顯示重設篩選按鈕。
```

Gemini expected:

```text
搜尋結果為空時，顯示重設篩選按鈕。
```

Gemini acceptable variants:

```text
搜索結果為空時，顯示重置篩選按鈕。
搜尋結果為空時，顯示重置篩選按鈕。
搜索結果為空時，顯示重設篩選按鈕。
```

Gemini notes:

```text
將「搜索」轉為「搜尋」（UI術語），「显示」轉為「顯示」，「重置」轉為「重設」（UI術語），「筛选」轉為「篩選」（UI術語）。
```

### blind-ui-0006：different

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
这个对话框会在离开页面前提醒尚未保存的更改。
```

Codex expected:

```text
這個對話框會在離開頁面前提醒尚未儲存的變更。
```

Gemini expected:

```text
這個對話方塊會在離開頁面前提醒尚未儲存的變更。
```

Gemini acceptable variants:

```text
這個對話框會在離開頁面前提醒尚未保存的更改。
這個對話方塊會在離開頁面前提醒尚未保存的更改。
這個對話框會在離開頁面前提醒尚未儲存的更改。
這個對話框會在離開頁面前提醒尚未保存的變更。
這個對話方塊會在離開頁面前提醒尚未保存的變更。
```

Gemini notes:

```text
將「这个」轉為「這個」，「对话框」轉為「對話方塊」（UI術語），「保存」轉為「儲存」（UI術語），「更改」轉為「變更」（UI術語）。
```

### blind-ui-0007：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
下载完成后，通知中心会显示打开文件的按钮。
```

Codex expected:

```text
下載完成後，通知中心會顯示開啟檔案的按鈕。
```

Gemini expected:

```text
下載完成後，通知中心會顯示開啟檔案的按鈕。
```

Gemini acceptable variants:

```text
下載完成後，通知中心會顯示打開文件的按鈕。
下載完成後，通知中心會顯示開啟文件的按鈕。
下載完成後，通知中心會顯示打開檔案的按鈕。
```

Gemini notes:

```text
將「显示」轉為「顯示」，「打开」轉為「開啟」（UI術語），「文件」轉為「檔案」（IT/UI術語）。
```

### blind-ui-0008：different

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
会员可以在个人资料里修改头像。
```

Codex expected:

```text
會員可以在個人資料裡修改大頭貼。
```

Gemini expected:

```text
會員可以在個人檔案裡修改大頭貼。
```

Gemini acceptable variants:

```text
會員可以在個人資料裡修改頭像。
會員可以在個人檔案裡修改頭像。
```

Gemini notes:

```text
將「个人资料」轉為「個人檔案」（UI術語），「里」轉為「裡」，「头像」轉為「大頭貼」（UI術語）。
```

### blind-ui-0009：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
表格支持按创建时间排序和按状态筛选。
```

Codex expected:

```text
表格支援依建立時間排序和依狀態篩選。
```

Gemini expected:

```text
表格支援依建立時間排序和依狀態篩選。
```

Gemini acceptable variants:

```text
表格支持按創建時間排序和按狀態篩選。
表格支援按創建時間排序和按狀態篩選。
表格支持依建立時間排序和按狀態篩選。
```

Gemini notes:

```text
將「支持」轉為「支援」（IT/UI術語），「按创建时间」轉為「依建立時間」（UI術語），「按状态」轉為「依狀態」（UI術語），「筛选」轉為「篩選」（UI術語）。
```

### blind-ui-0010：different

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
如果密码太短，输入框下方会显示错误消息。
```

Codex expected:

```text
如果密碼太短，輸入框下方會顯示錯誤訊息。
```

Gemini expected:

```text
如果密碼太短，輸入方塊下方會顯示錯誤訊息。
```

Gemini acceptable variants:

```text
如果密碼太短，輸入框下方會顯示錯誤消息。
如果密碼太短，輸入方塊下方會顯示錯誤消息。
```

Gemini notes:

```text
將「输入框」轉為「輸入方塊」（UI術語），「显示」轉為「顯示」，「错误消息」轉為「錯誤訊息」（UI術語）。
```

### blind-ui-0011：different

- Domain: `ui`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
点击返回箭头会回到上一层目录。
```

Codex expected:

```text
點選返回箭頭會回到上一層目錄。
```

Gemini expected:

```text
點擊返回箭頭會回到上一層目錄。
```

Gemini acceptable variants:

```text
點擊返回箭頭會回到上一層目錄。
```

Gemini notes:

```text
將「点击」轉為「點擊」（UI術語）。
```

### blind-ui-0012：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
你可以把常用页面加入收藏夹。
```

Codex expected:

```text
你可以把常用頁面加入我的最愛。
```

Gemini expected:

```text
你可以把常用頁面加入我的最愛。
```

Gemini acceptable variants:

```text
你可以把常用頁面加入收藏夾。
```

Gemini notes:

```text
將「收藏夹」轉為「我的最愛」（UI術語）。
```

### blind-ui-0013：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
开启深色模式后，图表颜色会自动调整。
```

Codex expected:

```text
開啟深色模式後，圖表顏色會自動調整。
```

Gemini expected:

```text
開啟深色模式後，圖表顏色會自動調整。
```

Gemini acceptable variants:

```text
開啟深色模式後，圖表顏色會自動調整。
```

Gemini notes:

```text
將「开启」轉為「開啟」。
```

### blind-ui-0014：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
语言切换后，当前草稿不会被清除。
```

Codex expected:

```text
語言切換後，目前草稿不會被清除。
```

Gemini expected:

```text
語言切換後，目前草稿不會被清除。
```

Gemini acceptable variants:

```text
語言切換後，當前草稿不會被清除。
```

Gemini notes:

```text
將「当前」轉為「目前」（UI術語）。
```

### blind-ui-0015：match

- Domain: `ui`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
订单取消成功后，按钮会变成灰色。
```

Codex expected:

```text
訂單取消成功後，按鈕會變成灰色。
```

Gemini expected:

```text
訂單取消成功後，按鈕會變成灰色。
```

Gemini acceptable variants:

```text
訂單取消成功後，按鈕會變成灰色。
```

Gemini notes:

```text
無轉換。
```

### blind-ui-0016：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
当网络中断时，页面顶部显示离线提示。
```

Codex expected:

```text
當網路中斷時，頁面頂端顯示離線提示。
```

Gemini expected:

```text
當網路中斷時，頁面頂端顯示離線提示。
```

Gemini acceptable variants:

```text
當網絡中斷時，頁面頂部顯示離線提示。
當網路中斷時，頁面頂部顯示離線提示。
```

Gemini notes:

```text
將「网络」轉為「網路」，「顶部」轉為「頂端」（UI術語）。
```

### blind-ui-0017：match

- Domain: `ui`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
请在删除账号前再次输入你的电子邮件。
```

Codex expected:

```text
請在刪除帳號前再次輸入你的電子郵件。
```

Gemini expected:

```text
請在刪除帳號前再次輸入你的電子郵件。
```

Gemini acceptable variants:

```text
請在刪除賬號前再次輸入你的電子郵件。
```

Gemini notes:

```text
將「请」轉為「請」，「账号」轉為「帳號」（UI術語）。
```

### blind-ui-0018：different

- Domain: `ui`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
管理页面左侧菜单可以折叠。
```

Codex expected:

```text
管理頁面左側選單可以收合。
```

Gemini expected:

```text
管理頁面左側選單可以摺疊。
```

Gemini acceptable variants:

```text
管理頁面左側菜單可以折疊。
```

Gemini notes:

```text
將「菜单」轉為「選單」（UI術語），「折叠」轉為「摺疊」（UI術語）。
```

### blind-ui-0019：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
图片上传失败时，缩略图旁边会显示重试图标。
```

Codex expected:

```text
圖片上傳失敗時，縮圖旁邊會顯示重試圖示。
```

Gemini expected:

```text
圖片上傳失敗時，縮圖旁邊會顯示重試圖示。
```

Gemini acceptable variants:

```text
圖片上傳失敗時，縮略圖旁邊會顯示重試圖標。
圖片上傳失敗時，縮圖旁邊會顯示重試圖標。
```

Gemini notes:

```text
將「图片」轉為「圖片」，「缩略图」轉為「縮圖」（UI術語），「显示」轉為「顯示」，「图标」轉為「圖示」（UI術語）。
```

### blind-ui-0020：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
系统会在会话即将过期时弹出提示。
```

Codex expected:

```text
系統會在工作階段即將過期時彈出提示。
```

Gemini expected:

```text
系統會在工作階段即將過期時彈出提示。
```

Gemini acceptable variants:

```text
系統會在會話即將過期時彈出提示。
```

Gemini notes:

```text
將「系统」轉為「系統」，「会话」轉為「工作階段」（IT/UI術語）。
```

### blind-llm-0001：different

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
这段说明可以放在 README 的快速开始章节。
```

Codex expected:

```text
這段說明可以放在 README 的快速開始章節。
```

Gemini expected:

```text
這段說明可以放在 README 的快速入門章節。
```

Gemini acceptable variants:

```text
這段說明可以放在 README 的快速開始章節。
```

Gemini notes:

```text
將「这段」轉為「這段」，「快速开始」轉為「快速入門」（IT/正式用語）。
```

### blind-llm-0002：different

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
请把客服回复改写成更自然的台湾用语。
```

Codex expected:

```text
請把客服回覆改寫成更自然的台灣用語。
```

Gemini expected:

```text
請把客服回覆改寫成更自然的臺灣用語。
```

Gemini acceptable variants:

```text
請把客服回复改寫成更自然的台灣用语。
請把客服回覆改寫成更自然的台灣用语。
請把客服回复改寫成更自然的臺灣用语。
```

Gemini notes:

```text
將「请」轉為「請」，「回复」轉為「回覆」，「改写」轉為「改寫」，「台湾用语」轉為「臺灣用語」（臺灣的正式寫法）。
```

### blind-llm-0003：match

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
模型生成的摘要保留了原文的关键限制。
```

Codex expected:

```text
模型產生的摘要保留了原文的關鍵限制。
```

Gemini expected:

```text
模型產生的摘要保留了原文的關鍵限制。
```

Gemini acceptable variants:

```text
模型生成的摘要保留了原文的關鍵限制。
```

Gemini notes:

```text
將「生成」轉為「產生」（正式/IT用語），「关键」轉為「關鍵」。
```

### blind-llm-0004：match

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
这份产品文案强调团队协作和权限管理。
```

Codex expected:

```text
這份產品文案強調團隊協作和權限管理。
```

Gemini expected:

```text
這份產品文案強調團隊協作和權限管理。
```

Gemini acceptable variants:

```text
這份產品文案強調團隊協作和權限管理。
```

Gemini notes:

```text
將「这份」轉為「這份」。
```

### blind-llm-0005：match

- Domain: `llm`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
如果回答涉及医疗建议，请提醒用户咨询专业人员。
```

Codex expected:

```text
如果回答涉及醫療建議，請提醒使用者諮詢專業人員。
```

Gemini expected:

```text
如果回答涉及醫療建議，請提醒使用者諮詢專業人員。
```

Gemini acceptable variants:

```text
如果回答涉及醫療建議，請提醒用戶諮詢專業人員。
```

Gemini notes:

```text
將「请」轉為「請」，「用户」轉為「使用者」（UI/IT術語），「咨询」轉為「諮詢」。
```

### blind-llm-0006：match

- Domain: `llm`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
生成测试资料时，不要使用真实的个人信息。
```

Codex expected:

```text
產生測試資料時，不要使用真實的個人資訊。
```

Gemini expected:

```text
產生測試資料時，不要使用真實的個人資訊。
```

Gemini acceptable variants:

```text
生成測試資料時，不要使用真實的個人信息。
產生測試資料時，不要使用真實的個人信息。
```

Gemini notes:

```text
將「生成」轉為「產生」（正式/IT用語），「个人信息」轉為「個人資訊」（正式/IT用語）。
```

### blind-llm-0007：match

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
这段提示词要求模型先列出假设再给结论。
```

Codex expected:

```text
這段提示詞要求模型先列出假設再給結論。
```

Gemini expected:

```text
這段提示詞要求模型先列出假設再給結論。
```

Gemini acceptable variants:

```text
這段提示詞要求模型先列出假設再給結論。
```

Gemini notes:

```text
將「这段」轉為「這段」，「假设」轉為「假設」。
```

### blind-llm-0008：match

- Domain: `llm`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
机器人应该在不知道答案时明确说明限制。
```

Codex expected:

```text
機器人應該在不知道答案時明確說明限制。
```

Gemini expected:

```text
機器人應該在不知道答案時明確說明限制。
```

Gemini acceptable variants:

```text
機器人應該在不知道答案時明確說明限制。
```

Gemini notes:

```text
將「机器人」轉為「機器人」，「应该」轉為「應該」。
```

### blind-llm-0009：match

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
请把长段落拆成三点，方便使用者快速阅读。
```

Codex expected:

```text
請把長段落拆成三點，方便使用者快速閱讀。
```

Gemini expected:

```text
請把長段落拆成三點，方便使用者快速閱讀。
```

Gemini acceptable variants:

```text
請把長段落拆成三點，方便使用者快速閱讀。
```

Gemini notes:

```text
將「请」轉為「請」，「使用者」轉為「使用者」。
```

### blind-llm-0010：different

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
这份教程适合第一次部署服务的开发者。
```

Codex expected:

```text
這份教學適合第一次部署服務的開發者。
```

Gemini expected:

```text
這份教學課程適合第一次部署服務的開發者。
```

Gemini acceptable variants:

```text
這份教程適合第一次部署服務的開發者。
```

Gemini notes:

```text
將「这份」轉為「這份」，「教程」轉為「教學課程」（正式/IT用語）。
```

### blind-llm-0011：match

- Domain: `llm`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
自动回复需要避免承诺无法保证的处理时间。
```

Codex expected:

```text
自動回覆需要避免承諾無法保證的處理時間。
```

Gemini expected:

```text
自動回覆需要避免承諾無法保證的處理時間。
```

Gemini acceptable variants:

```text
自動回复需要避免承諾無法保證的處理時間。
```

Gemini notes:

```text
將「回复」轉為「回覆」。
```

### blind-llm-0012：different

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
模型输出的代码片段应该包含必要的导入语句。
```

Codex expected:

```text
模型輸出的程式碼片段應該包含必要的匯入語句。
```

Gemini expected:

```text
模型輸出的程式碼片段應該包含必要的匯入陳述式。
```

Gemini acceptable variants:

```text
模型輸出的代碼片段應該包含必要的導入語句。
模型輸出的程式碼片段應該包含必要的導入語句。
模型輸出的代碼片段應該包含必要的匯入語句。
模型輸出的程式碼片段應該包含必要的匯入語句。
```

Gemini notes:

```text
將「输出」轉為「輸出」（IT術語），「代码片段」轉為「程式碼片段」（IT術語），「应该」轉為「應該」，「导入语句」轉為「匯入陳述式」（IT術語）。
```

### blind-llm-0013：different

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
这条系统消息限制助理不能泄露内部规则。
```

Codex expected:

```text
這則系統訊息限制助理不能洩露內部規則。
```

Gemini expected:

```text
這條系統訊息限制助理不能洩漏內部規則。
```

Gemini acceptable variants:

```text
這條系統消息限制助理不能泄露內部規則。
這條系統訊息限制助理不能泄露內部規則。
```

Gemini notes:

```text
將「这条」轉為「這條」，「系统消息」轉為「系統訊息」（IT術語），「泄露」轉為「洩漏」。
```

### blind-llm-0014：match

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
使用者要求比较方案时，请先说明评估标准。
```

Codex expected:

```text
使用者要求比較方案時，請先說明評估標準。
```

Gemini expected:

```text
使用者要求比較方案時，請先說明評估標準。
```

Gemini acceptable variants:

```text
使用者要求比較方案時，請先說明評估標準。
```

Gemini notes:

```text
將「请」轉為「請」。
```

### blind-llm-0015：match

- Domain: `llm`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
这段公告要同时适合网页和电子邮件使用。
```

Codex expected:

```text
這段公告要同時適合網頁和電子郵件使用。
```

Gemini expected:

```text
這段公告要同時適合網頁和電子郵件使用。
```

Gemini acceptable variants:

```text
這段公告要同時適合網頁和電子郵件使用。
```

Gemini notes:

```text
將「这段」轉為「這段」。
```

### blind-formal-0001：match

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
本计划将分阶段公布实施细则和申请流程。
```

Codex expected:

```text
本計畫將分階段公布實施細則和申請流程。
```

Gemini expected:

```text
本計畫將分階段公布實施細則和申請流程。
```

Gemini acceptable variants:

```text
本計劃將分階段公布實施細則和申請流程。
```

Gemini notes:

```text
將「本计划」轉為「本計畫」（正式用語），「将」轉為「將」，「实施细则」轉為「實施細則」（正式用語）。
```

### blind-formal-0002：match

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
公司董事会已经核准年度预算调整案。
```

Codex expected:

```text
公司董事會已經核准年度預算調整案。
```

Gemini expected:

```text
公司董事會已經核准年度預算調整案。
```

Gemini acceptable variants:

```text
公司董事會已經核准年度預算調整案。
```

Gemini notes:

```text
將「董事会」轉為「董事會」，「已经」轉為「已經」。
```

### blind-formal-0003：match

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
研究团队发现数据来源存在明显偏差。
```

Codex expected:

```text
研究團隊發現資料來源存在明顯偏差。
```

Gemini expected:

```text
研究團隊發現資料來源存在明顯偏差。
```

Gemini acceptable variants:

```text
研究團隊發現數據來源存在明顯偏差。
```

Gemini notes:

```text
將「研究团队」轉為「研究團隊」，「发现」轉為「發現」，「数据来源」轉為「資料來源」（正式/IT用語）。
```

### blind-formal-0004：match

- Domain: `formal`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
主管机关提醒业者不得误导消费者。
```

Codex expected:

```text
主管機關提醒業者不得誤導消費者。
```

Gemini expected:

```text
主管機關提醒業者不得誤導消費者。
```

Gemini acceptable variants:

```text
主管機關提醒業者不得誤導消費者。
```

Gemini notes:

```text
將「主管机关」轉為「主管機關」（正式用語）。
```

### blind-formal-0005：match

- Domain: `formal`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
新制度预计明年第一季度开始试办。
```

Codex expected:

```text
新制度預計明年第一季開始試辦。
```

Gemini expected:

```text
新制度預計明年第一季開始試辦。
```

Gemini acceptable variants:

```text
新制度預計明年第一季度開始試辦。
```

Gemini notes:

```text
將「预计」轉為「預計」，「第一季度」轉為「第一季」（正式用語）。
```

### blind-formal-0006：match

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
会议记录应列明出席人员和决议事项。
```

Codex expected:

```text
會議紀錄應列明出席人員和決議事項。
```

Gemini expected:

```text
會議紀錄應列明出席人員和決議事項。
```

Gemini acceptable variants:

```text
會議記錄應列明出席人員和決議事項。
```

Gemini notes:

```text
將「会议记录」轉為「會議紀錄」。
```

### blind-formal-0007：match

- Domain: `formal`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
申请人须在期限内补交相关证明文件。
```

Codex expected:

```text
申請人須在期限內補交相關證明文件。
```

Gemini expected:

```text
申請人須在期限內補交相關證明文件。
```

Gemini acceptable variants:

```text
申請人須在期限內補交相關證明文件。
```

Gemini notes:

```text
無轉換。
```

### blind-formal-0008：match

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
该报告建议提高资讯安全审查频率。
```

Codex expected:

```text
該報告建議提高資訊安全審查頻率。
```

Gemini expected:

```text
該報告建議提高資訊安全審查頻率。
```

Gemini acceptable variants:

```text
該報告建議提高信息安全審查頻率。
```

Gemini notes:

```text
將「资讯安全」轉為「資訊安全」（正式/IT用語）。
```

### blind-formal-0009：match

- Domain: `formal`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
政府将持续追踪政策执行效果。
```

Codex expected:

```text
政府將持續追蹤政策執行效果。
```

Gemini expected:

```text
政府將持續追蹤政策執行效果。
```

Gemini acceptable variants:

```text
政府將持續追踪政策執行效果。
```

Gemini notes:

```text
將「将」轉為「將」，「追踪」轉為「追蹤」。
```

### blind-formal-0010：match

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
新闻稿指出，合作项目不会影响现有用户权益。
```

Codex expected:

```text
新聞稿指出，合作專案不會影響現有使用者權益。
```

Gemini expected:

```text
新聞稿指出，合作專案不會影響現有使用者權益。
```

Gemini acceptable variants:

```text
新聞稿指出，合作項目不會影響現有用戶權益。
新聞稿指出，合作專案不會影響現有用戶權益。
新聞稿指出，合作項目不會影響現有使用者權益。
```

Gemini notes:

```text
將「合作项目」轉為「合作專案」（正式用語），「用户权益」轉為「使用者權益」（正式/UI/IT用語）。
```

### blind-formal-0011：match

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
委员会要求承办单位重新评估风险。
```

Codex expected:

```text
委員會要求承辦單位重新評估風險。
```

Gemini expected:

```text
委員會要求承辦單位重新評估風險。
```

Gemini acceptable variants:

```text
委員會要求承辦單位重新評估風險。
```

Gemini notes:

```text
將「委员会」轉為「委員會」，「承办单位」轉為「承辦單位」（正式用語）。
```

### blind-formal-0012：different

- Domain: `formal`
- Risk: `over_conversion_guard`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
合同签署前，双方应确认付款条件。
```

Codex expected:

```text
契約簽署前，雙方應確認付款條件。
```

Gemini expected:

```text
合約簽署前，雙方應確認付款條件。
```

Gemini acceptable variants:

```text
合同簽署前，雙方應確認付款條件。
```

Gemini notes:

```text
將「合同」轉為「合約」（正式/法律用語）。
```

### blind-formal-0013：match

- Domain: `formal`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
统计资料显示，服务使用量持续增加。
```

Codex expected:

```text
統計資料顯示，服務使用量持續增加。
```

Gemini expected:

```text
統計資料顯示，服務使用量持續增加。
```

Gemini acceptable variants:

```text
統計資料顯示，服務使用量持續增加。
```

Gemini notes:

```text
無轉換。
```

### blind-formal-0014：match

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
采购案将依公开程序办理。
```

Codex expected:

```text
採購案將依公開程序辦理。
```

Gemini expected:

```text
採購案將依公開程序辦理。
```

Gemini acceptable variants:

```text
採購案將依公開程序辦理。
```

Gemini notes:

```text
將「采购案」轉為「採購案」（正式用語），「将」轉為「將」。
```

### blind-formal-0015：match

- Domain: `formal`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
本声明不构成任何投资建议。
```

Codex expected:

```text
本聲明不構成任何投資建議。
```

Gemini expected:

```text
本聲明不構成任何投資建議。
```

Gemini acceptable variants:

```text
本聲明不構成任何投資建議。
```

Gemini notes:

```text
無轉換。
```

### blind-social-0001：match

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
我今天下班后想去买一杯珍珠奶茶。
```

Codex expected:

```text
我今天下班後想去買一杯珍珠奶茶。
```

Gemini expected:

```text
我今天下班後想去買一杯珍珠奶茶。
```

Gemini acceptable variants:

```text
我今天下班後想去買一杯珍珠奶茶。
```

Gemini notes:

```text
將「后」轉為「後」，「买」轉為「買」。
```

### blind-social-0002：match

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
这个视频的字幕有点太快，我来不及看完。
```

Codex expected:

```text
這個影片的字幕有點太快，我來不及看完。
```

Gemini expected:

```text
這個影片的字幕有點太快，我來不及看完。
```

Gemini acceptable variants:

```text
這個視頻的字幕有點太快，我來不及看完。
```

Gemini notes:

```text
將「这个」轉為「這個」，「视频」轉為「影片」（臺灣常用語），「有点」轉為「有點」，「来不及」轉為「來不及」。
```

### blind-social-0003：match

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
周末如果没下雨，我们就去骑脚踏车。
```

Codex expected:

```text
週末如果沒下雨，我們就去騎腳踏車。
```

Gemini expected:

```text
週末如果沒下雨，我們就去騎腳踏車。
```

Gemini acceptable variants:

```text
週末如果沒下雨，我們就去騎腳踏車。
```

Gemini notes:

```text
將「周末」轉為「週末」，「没下雨」轉為「沒下雨」，「我们」轉為「我們」。
```

### blind-social-0004：match

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
群组里有人分享了新的餐厅名单。
```

Codex expected:

```text
群組裡有人分享了新的餐廳名單。
```

Gemini expected:

```text
群組裡有人分享了新的餐廳名單。
```

Gemini acceptable variants:

```text
群組裡有人分享了新的餐廳名單。
```

Gemini notes:

```text
將「群组」轉為「群組」，「里」轉為「裡」。
```

### blind-social-0005：match

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
你把照片传给我，我晚点再整理相册。
```

Codex expected:

```text
你把照片傳給我，我晚點再整理相簿。
```

Gemini expected:

```text
你把照片傳給我，我晚點再整理相簿。
```

Gemini acceptable variants:

```text
你把照片傳給我，我晚點再整理相冊。
```

Gemini notes:

```text
將「传给我」轉為「傳給我」，「晚点」轉為「晚點」，「相册」轉為「相簿」（臺灣常用語）。
```

### blind-social-0006：match

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
这件外套颜色很好看，不过尺寸好像偏小。
```

Codex expected:

```text
這件外套顏色很好看，不過尺寸好像偏小。
```

Gemini expected:

```text
這件外套顏色很好看，不過尺寸好像偏小。
```

Gemini acceptable variants:

```text
這件外套顏色很好看，不過尺寸好像偏小。
```

Gemini notes:

```text
將「这件」轉為「這件」，「颜色」轉為「顏色」。
```

### blind-social-0007：match

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
我刚刚在便利店看到同款充电线。
```

Codex expected:

```text
我剛剛在便利商店看到同款充電線。
```

Gemini expected:

```text
我剛剛在便利商店看到同款充電線。
```

Gemini acceptable variants:

```text
我剛剛在便利店看到同款充電線。
```

Gemini notes:

```text
將「刚刚」轉為「剛剛」，「便利店」轉為「便利商店」（臺灣常用語）。
```

### blind-social-0008：match

- Domain: `social`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
明天早上记得带雨伞，天气预报说会下雨。
```

Codex expected:

```text
明天早上記得帶雨傘，天氣預報說會下雨。
```

Gemini expected:

```text
明天早上記得帶雨傘，天氣預報說會下雨。
```

Gemini acceptable variants:

```text
明天早上記得帶雨傘，天氣預報說會下雨。
```

Gemini notes:

```text
將「记得」轉為「記得」，「带」轉為「帶」，「雨伞」轉為「雨傘」，「说」轉為「說」。
```

### blind-social-0009：match

- Domain: `social`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
这首歌的副歌很洗脑，大家都在哼。
```

Codex expected:

```text
這首歌的副歌很洗腦，大家都在哼。
```

Gemini expected:

```text
這首歌的副歌很洗腦，大家都在哼。
```

Gemini acceptable variants:

```text
這首歌的副歌很洗腦，大家都在哼。
```

Gemini notes:

```text
將「这首歌」轉為「這首歌」，「洗脑」轉為「洗腦」。
```

### blind-social-0010：match

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
他把会议链接贴在留言区了。
```

Codex expected:

```text
他把會議連結貼在留言區了。
```

Gemini expected:

```text
他把會議連結貼在留言區了。
```

Gemini acceptable variants:

```text
他把會議鏈接貼在留言區了。
```

Gemini notes:

```text
將「会议」轉為「會議」，「链接」轉為「連結」（IT/UI術語）。
```

### blind-social-0011：match

- Domain: `social`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
我们先在捷运站出口集合。
```

Codex expected:

```text
我們先在捷運站出口集合。
```

Gemini expected:

```text
我們先在捷運站出口集合。
```

Gemini acceptable variants:

```text
我們先在捷運站出口集合。
```

Gemini notes:

```text
將「我们」轉為「我們」，「捷运站」轉為「捷運站」（臺灣常用語）。
```

### blind-social-0012：match

- Domain: `social`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
晚餐想吃面还是便当？
```

Codex expected:

```text
晚餐想吃麵還是便當？
```

Gemini expected:

```text
晚餐想吃麵還是便當？
```

Gemini acceptable variants:

```text
晚餐想吃面還是便當？
```

Gemini notes:

```text
將「面」轉為「麵」。
```

### blind-social-0013：match

- Domain: `social`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
这家店排队人很多，可能要等半小时。
```

Codex expected:

```text
這家店排隊人很多，可能要等半小時。
```

Gemini expected:

```text
這家店排隊人很多，可能要等半小時。
```

Gemini acceptable variants:

```text
這家店排隊人很多，可能要等半小時。
```

Gemini notes:

```text
將「这家店」轉為「這家店」，「排队」轉為「排隊」，「半小时」轉為「半小時」。
```

### blind-social-0014：match

- Domain: `social`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
我把票放在钱包里，别让我忘记拿。
```

Codex expected:

```text
我把票放在錢包裡，別讓我忘記拿。
```

Gemini expected:

```text
我把票放在錢包裡，別讓我忘記拿。
```

Gemini acceptable variants:

```text
我把票放在錢包裡，別讓我忘記拿。
```

Gemini notes:

```text
將「钱包」轉為「錢包」，「里」轉為「裡」，「别让」轉為「別讓」，「忘记」轉為「忘記」。
```

### blind-social-0015：different

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
今天的直播回放什么时候会上架？
```

Codex expected:

```text
今天的直播重播什麼時候會上架？
```

Gemini expected:

```text
今天的直播回放什麼時候會上架？
```

Gemini acceptable variants:

```text
今天的直播回放什麼時候會上架？
```

Gemini notes:

```text
將「什么时候」轉為「什麼時候」。
```

### blind-high-risk-0001：match

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
不得以定型化契约条款排除责任。
```

Codex expected:

```text
不得以定型化契約條款排除責任。
```

Gemini expected:

```text
不得以定型化契約條款排除責任。
```

Gemini acceptable variants:

```text
不得以定型化契约條款排除責任。
```

Gemini notes:

```text
將「定型化契约」轉為「定型化契約」（法律用語）。
```

### blind-high-risk-0002：match

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
跨行汇款手续费由使用者负担。
```

Codex expected:

```text
跨行匯款手續費由使用者負擔。
```

Gemini expected:

```text
跨行匯款手續費由使用者負擔。
```

Gemini acceptable variants:

```text
跨行匯款手續費由使用者負擔。
```

Gemini notes:

```text
將「汇款」轉為「匯款」（金融用語），「负担」轉為「負擔」。
```

### blind-high-risk-0003：match

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
请依医师指示服用本药，并留意过敏反应。
```

Codex expected:

```text
請依醫師指示服用本藥，並留意過敏反應。
```

Gemini expected:

```text
請依醫師指示服用本藥，並留意過敏反應。
```

Gemini acceptable variants:

```text
請依醫師指示服用本藥，並留意過敏反應。
```

Gemini notes:

```text
將「医师」轉為「醫師」，「本药」轉為「本藥」。
```

### blind-high-risk-0004：match

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
投保前应详阅保单条款和除外责任。
```

Codex expected:

```text
投保前應詳閱保單條款和除外責任。
```

Gemini expected:

```text
投保前應詳閱保單條款和除外責任。
```

Gemini acceptable variants:

```text
投保前應詳閱保單條款和除外責任。
```

Gemini notes:

```text
將「详阅」轉為「詳閱」（正式用語）。
```

### blind-high-risk-0005：match

- Domain: `high_risk`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
申请补助时，必须提供有效的身分证明文件。
```

Codex expected:

```text
申請補助時，必須提供有效的身分證明文件。
```

Gemini expected:

```text
申請補助時，必須提供有效的身分證明文件。
```

Gemini acceptable variants:

```text
申請補助時，必須提供有效的身分證明文件。
```

Gemini notes:

```text
將「申请」轉為「申請」，「身分证明文件」轉為「身分證明文件」（正式/法律用語）。
```

### blind-high-risk-0006：match

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
病人出现胸痛或呼吸困难时，应立即就医。
```

Codex expected:

```text
病人出現胸痛或呼吸困難時，應立即就醫。
```

Gemini expected:

```text
病人出現胸痛或呼吸困難時，應立即就醫。
```

Gemini acceptable variants:

```text
病人出現胸痛或呼吸困難時，應立即就醫。
```

Gemini notes:

```text
將「出现」轉為「出現」，「就医」轉為「就醫」。
```

### blind-high-risk-0007：match

- Domain: `high_risk`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
贷款利率可能随市场条件调整。
```

Codex expected:

```text
貸款利率可能隨市場條件調整。
```

Gemini expected:

```text
貸款利率可能隨市場條件調整。
```

Gemini acceptable variants:

```text
貸款利率可能隨市場條件調整。
```

Gemini notes:

```text
將「贷款」轉為「貸款」（金融用語），「随」轉為「隨」。
```

### blind-high-risk-0008：match

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
个人资料不得用于原申请目的以外的用途。
```

Codex expected:

```text
個人資料不得用於原申請目的以外的用途。
```

Gemini expected:

```text
個人資料不得用於原申請目的以外的用途。
```

Gemini acceptable variants:

```text
個人資料不得用於原申請目的以外的用途。
```

Gemini notes:

```text
將「个人资料」轉為「個人資料」（法律/隱私用語）。
```

### blind-high-risk-0009：match

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
本合约争议适用中华民国法律。
```

Codex expected:

```text
本合約爭議適用中華民國法律。
```

Gemini expected:

```text
本合約爭議適用中華民國法律。
```

Gemini acceptable variants:

```text
本合約爭議適用中華民國法律。
```

Gemini notes:

```text
將「合约」轉為「合約」（法律用語），「争议」轉為「爭議」。
```

### blind-high-risk-0010：match

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
医疗纪录应依法保存，不得任意删除。
```

Codex expected:

```text
醫療紀錄應依法保存，不得任意刪除。
```

Gemini expected:

```text
醫療紀錄應依法保存，不得任意刪除。
```

Gemini acceptable variants:

```text
醫療紀錄應依法保存，不得任意刪除。
```

Gemini notes:

```text
將「医疗纪录」轉為「醫療紀錄」（醫療/法律用語），「删除」轉為「刪除」。
```
