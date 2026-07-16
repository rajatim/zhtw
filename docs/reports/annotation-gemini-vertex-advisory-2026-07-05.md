<!-- zhtw:disable -->
# Gemini Vertex Advisory Review（2026-07-05）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`
Blind packet：`docs/reports/annotation-blind-review-packet-it-api-cli-2026-07-05.md`
Raw JSON：`docs/reports/annotation-gemini-vertex-advisory-2026-07-05.json`

## Scope

This is an AI advisory review generated through Vertex AI Gemini, not a human review and not Gemini CLI output.
It must not be recorded as `human_first_pass`, `human_adjudication`, or `blind_reviewer`.

## Summary

- Model: `gemini-2.5-flash`
- Project: `tw-el-gemini`
- Location: `us-central1`
- Cases: 25
- Exact matches with first pass: 11
- Differences: 14

## Maintainer Decision

Maintainer `tim` reviewed the 14 differences and accepted the Gemini advisory
version on 2026-07-05. The backlog was updated as follows:

- 11 exact-match cases remain `expected_source = "human_first_pass"`.
- 14 differing cases now use the Gemini advisory expected output with
  `expected_source = "human_adjudication"` and `adjudicator = "tim"`.
- Gemini is recorded under `review.ai_advisory`, not as a human
  `blind_reviewer`.
- All 25 cases are now `approved` under the
  `single_human_with_ai_advisory_or_independent_blind_review` policy.

## Comparison

### it-api-cli-0001：different

Input:

```text
这个函数会抛出异常并返回错误码。
```

First-pass expected:

```text
這個函式會拋出例外並回傳錯誤碼。
```

Gemini advisory expected:

```text
這個函式會拋出例外並傳回錯誤碼。
```

Gemini notes:

```text

```

### it-api-cli-0002：different

Input:

```text
请在配置文件中启用调试模式。
```

First-pass expected:

```text
請在設定檔中啟用除錯模式。
```

Gemini advisory expected:

```text
請在設定檔中啟用偵錯模式。
```

Gemini notes:

```text

```

### it-api-cli-0003：match

Input:

```text
服务器证书已经过期，请重新签发。
```

First-pass expected:

```text
伺服器憑證已經過期，請重新簽發。
```

Gemini advisory expected:

```text
伺服器憑證已經過期，請重新簽發。
```

Gemini notes:

```text

```

### it-api-cli-0004：match

Input:

```text
命令行工具会读取环境变量。
```

First-pass expected:

```text
命令列工具會讀取環境變數。
```

Gemini advisory expected:

```text
命令列工具會讀取環境變數。
```

Gemini notes:

```text

```

### it-api-cli-0005：different

Input:

```text
接口返回的响应头包含缓存策略。
```

First-pass expected:

```text
介面回傳的回應標頭包含快取策略。
```

Gemini advisory expected:

```text
介面傳回的回應標頭包含快取策略。
```

Gemini notes:

```text

```

### it-api-cli-0006：match

Input:

```text
请通过参数指定输出目录。
```

First-pass expected:

```text
請透過參數指定輸出目錄。
```

Gemini advisory expected:

```text
請透過參數指定輸出目錄。
```

Gemini notes:

```text

```

### it-api-cli-0007：different

Input:

```text
日志等级可以在启动时覆盖。
```

First-pass expected:

```text
日誌等級可以在啟動時覆寫。
```

Gemini advisory expected:

```text
記錄等級可以在啟動時覆寫。
```

Gemini notes:

```text

```

### it-api-cli-0008：different

Input:

```text
客户端会自动刷新访问令牌。
```

First-pass expected:

```text
用戶端會自動更新存取權杖。
```

Gemini advisory expected:

```text
用戶端會自動重新整理存取權杖。
```

Gemini notes:

```text

```

### it-api-cli-0009：different

Input:

```text
后端服务需要验证请求签名。
```

First-pass expected:

```text
後端服務需要驗證請求簽章。
```

Gemini advisory expected:

```text
後端服務需要驗證要求簽章。
```

Gemini notes:

```text

```

### it-api-cli-0010：match

Input:

```text
这个字段支持布尔值和字符串。
```

First-pass expected:

```text
這個欄位支援布林值和字串。
```

Gemini advisory expected:

```text
這個欄位支援布林值和字串。
```

Gemini notes:

```text

```

### it-api-cli-0011：different

Input:

```text
数据库连接池达到上限。
```

First-pass expected:

```text
資料庫連線池達到上限。
```

Gemini advisory expected:

```text
資料庫連線集區達到上限。
```

Gemini notes:

```text

```

### it-api-cli-0012：match

Input:

```text
部署流水线会先执行单元测试。
```

First-pass expected:

```text
部署管線會先執行單元測試。
```

Gemini advisory expected:

```text
部署管線會先執行單元測試。
```

Gemini notes:

```text

```

### it-api-cli-0013：different

Input:

```text
前端组件会监听窗口大小变化。
```

First-pass expected:

```text
前端元件會監聽視窗大小變化。
```

Gemini advisory expected:

```text
前端元件會監聽視窗大小變更。
```

Gemini notes:

```text

```

### it-api-cli-0014：different

Input:

```text
请把补丁合并到主分支。
```

First-pass expected:

```text
請把修補程式合併到主分支。
```

Gemini advisory expected:

```text
請將修補程式合併到主要分支。
```

Gemini notes:

```text

```

### it-api-cli-0015：match

Input:

```text
文件系统权限不足导致写入失败。
```

First-pass expected:

```text
檔案系統權限不足導致寫入失敗。
```

Gemini advisory expected:

```text
檔案系統權限不足導致寫入失敗。
```

Gemini notes:

```text

```

### it-api-cli-0016：match

Input:

```text
请上传配置文件并重新启动服务。
```

First-pass expected:

```text
請上傳設定檔並重新啟動服務。
```

Gemini advisory expected:

```text
請上傳設定檔並重新啟動服務。
```

Gemini notes:

```text

```

### it-api-cli-0017：different

Input:

```text
进程退出前会释放临时文件。
```

First-pass expected:

```text
行程結束前會釋放暫存檔。
```

Gemini advisory expected:

```text
處理程序結束前會釋放暫存檔案。
```

Gemini notes:

```text

```

### it-api-cli-0018：different

Input:

```text
请求超时后会重试三次。
```

First-pass expected:

```text
請求逾時後會重試三次。
```

Gemini advisory expected:

```text
要求逾時後會重試三次。
```

Gemini notes:

```text

```

### it-api-cli-0019：different

Input:

```text
缓存键包含用户标识和区域代码。
```

First-pass expected:

```text
快取鍵包含使用者識別碼和區域代碼。
```

Gemini advisory expected:

```text
快取索引鍵包含使用者識別碼和區域代碼。
```

Gemini notes:

```text

```

### it-api-cli-0020：different

Input:

```text
这个端点只接受 JSON 请求。
```

First-pass expected:

```text
這個端點只接受 JSON 請求。
```

Gemini advisory expected:

```text
這個端點只接受 JSON 要求。
```

Gemini notes:

```text

```

### it-api-cli-0021：match

Input:

```text
调用接口前请先取得访问令牌。
```

First-pass expected:

```text
呼叫介面前請先取得存取權杖。
```

Gemini advisory expected:

```text
呼叫介面前請先取得存取權杖。
```

Gemini notes:

```text

```

### it-api-cli-0022：match

Input:

```text
程序会在后台监听端口。
```

First-pass expected:

```text
程式會在背景監聽連接埠。
```

Gemini advisory expected:

```text
程式會在背景監聽連接埠。
```

Gemini notes:

```text

```

### it-api-cli-0023：match

Input:

```text
请检查响应主体中的错误消息。
```

First-pass expected:

```text
請檢查回應主體中的錯誤訊息。
```

Gemini advisory expected:

```text
請檢查回應主體中的錯誤訊息。
```

Gemini notes:

```text

```

### it-api-cli-0024：different

Input:

```text
安装依赖库后请重新构建项目。
```

First-pass expected:

```text
安裝相依函式庫後請重新建置專案。
```

Gemini advisory expected:

```text
安裝相依性程式庫後請重新建置專案。
```

Gemini notes:

```text

```

### it-api-cli-0025：match

Input:

```text
这个命令会递归扫描子目录。
```

First-pass expected:

```text
這個命令會遞迴掃描子目錄。
```

Gemini advisory expected:

```text
這個命令會遞迴掃描子目錄。
```

Gemini notes:

```text

```
