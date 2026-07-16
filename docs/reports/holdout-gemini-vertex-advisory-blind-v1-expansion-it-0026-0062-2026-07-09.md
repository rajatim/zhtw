<!-- zhtw:disable -->
# Holdout Gemini Vertex Advisory (2026-07-09)

Dataset: `blind-v1`
Inputs: `benchmarks/accuracy/blind-v1.inputs.json`
Codex advisory: `docs/reports/holdout-codex-first-pass-blind-v1-expansion-127-cases-2026-07-09.json`
Raw JSON: `docs/reports/holdout-gemini-vertex-advisory-blind-v1-expansion-it-0026-0062-2026-07-09.json`
Reviewer: `gemini_vertex`
Model: `gemini-2.5-flash`

## Policy

- Gemini saw only the input cases, not Codex recommendations.
- This report is advisory only.
- It is not ground truth and must not populate `blind-v1.expected.json` directly.
- Maintainer confirmation is required before any expected value becomes human decision.

## Summary

- Cases: 37
- Exact matches with Codex: 10
- Differences from Codex: 27
- Needs maintainer review: 30

Gemini confidence:

- `high`: 37

Domain distribution:

- `it`: 37

## Maintainer Review Queue

- `blind-it-0026` (it, different, Codex medium, Gemini high)
- `blind-it-0027` (it, different, Codex high, Gemini high)
- `blind-it-0028` (it, different, Codex medium, Gemini high)
- `blind-it-0029` (it, different, Codex medium, Gemini high)
- `blind-it-0032` (it, different, Codex high, Gemini high)
- `blind-it-0033` (it, different, Codex medium, Gemini high)
- `blind-it-0034` (it, different, Codex medium, Gemini high)
- `blind-it-0035` (it, different, Codex medium, Gemini high)
- `blind-it-0036` (it, different, Codex medium, Gemini high)
- `blind-it-0037` (it, different, Codex medium, Gemini high)
- `blind-it-0040` (it, match, Codex medium, Gemini high)
- `blind-it-0041` (it, different, Codex medium, Gemini high)
- `blind-it-0042` (it, different, Codex medium, Gemini high)
- `blind-it-0043` (it, different, Codex high, Gemini high)
- `blind-it-0044` (it, different, Codex medium, Gemini high)
- `blind-it-0045` (it, different, Codex medium, Gemini high)
- `blind-it-0046` (it, different, Codex medium, Gemini high)
- `blind-it-0047` (it, different, Codex medium, Gemini high)
- `blind-it-0048` (it, different, Codex medium, Gemini high)
- `blind-it-0050` (it, different, Codex medium, Gemini high)
- `blind-it-0051` (it, different, Codex medium, Gemini high)
- `blind-it-0052` (it, different, Codex high, Gemini high)
- `blind-it-0053` (it, match, Codex high, Gemini high)
- `blind-it-0054` (it, different, Codex medium, Gemini high)
- `blind-it-0055` (it, different, Codex high, Gemini high)
- `blind-it-0056` (it, different, Codex medium, Gemini high)
- `blind-it-0057` (it, different, Codex medium, Gemini high)
- `blind-it-0058` (it, different, Codex medium, Gemini high)
- `blind-it-0059` (it, different, Codex high, Gemini high)
- `blind-it-0062` (it, match, Codex medium, Gemini high)

## Comparisons

### blind-it-0026：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
这个接口会在请求超时后返回默认配置。
```

Codex expected:

```text
這個介面會在請求逾時後回傳預設設定。
```

Gemini expected:

```text
這個介面會在請求逾時後傳回預設設定。
```

Gemini acceptable variants:

```text
這個介面會在請求逾時後返回預設設定。
這個接口會在請求逾時後傳回預設設定。
```

Gemini notes:

```text
「这个」轉「這個」，「接口」轉「介面」，「超时」轉「逾時」，「返回」轉「傳回」，「配置」轉「設定」。
```

### blind-it-0027：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
请把访问令牌保存到安全的密钥管理服务。
```

Codex expected:

```text
請把存取權杖儲存到安全的金鑰管理服務。
```

Gemini expected:

```text
請將存取權杖儲存到安全的金鑰管理服務。
```

Gemini acceptable variants:

```text
請把存取權杖儲存到安全的金鑰管理服務。
請將訪問令牌儲存到安全的金鑰管理服務。
```

Gemini notes:

```text
「请」轉「請」，「把」轉「將」，「访问令牌」轉「存取權杖」，「保存」轉「儲存」，「密钥」轉「金鑰」。
```

### blind-it-0028：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
命令行工具支持批量上传日志文件。
```

Codex expected:

```text
命令列工具支援批次上傳日誌檔案。
```

Gemini expected:

```text
命令列工具支援批次上傳記錄檔。
```

Gemini acceptable variants:

```text
命令列工具支持批次上傳記錄檔。
命令行工具支援批次上傳記錄檔。
```

Gemini notes:

```text
「命令行」轉「命令列」，「支持」轉「支援」，「批量」轉「批次」，「上传」轉「上傳」，「日志」轉「記錄」。
```

### blind-it-0029：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
如果依赖版本冲突，构建流程会直接失败。
```

Codex expected:

```text
如果相依套件版本衝突，建置流程會直接失敗。
```

Gemini expected:

```text
如果相依性版本衝突，建置程序會直接失敗。
```

Gemini acceptable variants:

```text
如果依賴版本衝突，建置程序會直接失敗。
如果相依性版本衝突，構建流程會直接失敗。
```

Gemini notes:

```text
「依赖」轉「相依性」，「构建」轉「建置」，「流程」轉「程序」。
```

### blind-it-0030：match

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
新的 SDK 会在初始化时检查运行环境。
```

Codex expected:

```text
新的 SDK 會在初始化時檢查執行環境。
```

Gemini expected:

```text
新的 SDK 會在初始化時檢查執行環境。
```

Gemini acceptable variants:

```text
新的 SDK 會在初始化時檢查運行環境。
```

Gemini notes:

```text
「检查」轉「檢查」，「运行环境」轉「執行環境」。
```

### blind-it-0031：match

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
请在合并分支前先执行单元测试。
```

Codex expected:

```text
請在合併分支前先執行單元測試。
```

Gemini expected:

```text
請在合併分支前先執行單元測試。
```

Gemini acceptable variants:

```text
請在合併分支前先執行單元測試。
请在合并分支前先执行单元测试。
```

Gemini notes:

```text
「请」轉「請」，「合并」轉「合併」，「执行」轉「執行」，「单元测试」轉「單元測試」。
```

### blind-it-0032：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
服务器会根据请求头选择响应格式。
```

Codex expected:

```text
伺服器會根據請求標頭選擇回應格式。
```

Gemini expected:

```text
伺服器會根據要求標頭選擇回應格式。
```

Gemini acceptable variants:

```text
伺服器會根據請求頭選擇回應格式。
服务器會根據要求標頭選擇回應格式。
```

Gemini notes:

```text
「服务器」轉「伺服器」，「请求头」轉「要求標頭」，「选择」轉「選擇」，「响应」轉「回應」。
```

### blind-it-0033：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
这个插件会扫描项目里的本地化资源。
```

Codex expected:

```text
這個外掛會掃描專案裡的在地化資源。
```

Gemini expected:

```text
這個外掛程式會掃描專案裡的在地化資源。
```

Gemini acceptable variants:

```text
這個外掛程式會掃描專案裡的本地化資源。
这个插件會掃描專案裡的在地化資源。
```

Gemini notes:

```text
「这个」轉「這個」，「插件」轉「外掛程式」，「扫描」轉「掃描」，「项目」轉「專案」，「本地化」轉「在地化」。
```

### blind-it-0034：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
发布任务完成后，系统会发送部署摘要。
```

Codex expected:

```text
發布工作完成後，系統會傳送部署摘要。
```

Gemini expected:

```text
發佈任務完成後，系統會傳送部署摘要。
```

Gemini acceptable variants:

```text
發佈任務完成後，系統會發送部署摘要。
发布任务完成後，系統會傳送部署摘要。
```

Gemini notes:

```text
「发布」轉「發佈」，「任务」轉「任務」，「发送」轉「傳送」。
```

### blind-it-0035：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
当网络中断时，客户端会排队重试。
```

Codex expected:

```text
當網路中斷時，用戶端會排隊重試。
```

Gemini expected:

```text
當網路中斷時，用戶端會排入佇列重試。
```

Gemini acceptable variants:

```text
當網路中斷時，用戶端會排隊重試。
当网络中断时，客户端會排入佇列重试。
```

Gemini notes:

```text
「当」轉「當」，「网络」轉「網路」，「客户端」轉「用戶端」，「排队」轉「排入佇列」。
```

### blind-it-0036：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
请在配置文件里关闭调试模式。
```

Codex expected:

```text
請在設定檔裡關閉偵錯模式。
```

Gemini expected:

```text
請在組態檔裡關閉偵錯模式。
```

Gemini acceptable variants:

```text
請在組態檔裡關閉偵錯模式。
请在配置文件里关闭调试模式。
```

Gemini notes:

```text
「请」轉「請」，「配置文件」轉「組態檔」，「关闭」轉「關閉」，「调试」轉「偵錯」。
```

### blind-it-0037：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
后台服务每天凌晨清理过期会话。
```

Codex expected:

```text
背景服務每天凌晨清理過期工作階段。
```

Gemini expected:

```text
後台服務每天凌晨清除過期工作階段。
```

Gemini acceptable variants:

```text
後台服務每天凌晨清理過期工作階段。
后台服务每天凌晨清除过期会话。
```

Gemini notes:

```text
「后台」轉「後台」，「清理」轉「清除」，「会话」轉「工作階段」。
```

### blind-it-0038：match

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
这个参数只影响增量同步的批次大小。
```

Codex expected:

```text
這個參數只影響增量同步的批次大小。
```

Gemini expected:

```text
這個參數只影響增量同步的批次大小。
```

Gemini acceptable variants:

```text
這個參數只影響增量同步的批次大小。
这个参数只影响增量同步的批次大小。
```

Gemini notes:

```text
「这个」轉「這個」，「影响」轉「影響」。
```

### blind-it-0039：match

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
代理服务器会缓存静态资源以降低延迟。
```

Codex expected:

```text
代理伺服器會快取靜態資源以降低延遲。
```

Gemini expected:

```text
代理伺服器會快取靜態資源以降低延遲。
```

Gemini acceptable variants:

```text
代理伺服器會快取靜態資源以降低延遲。
代理服务器會缓存静态资源以降低延迟。
```

Gemini notes:

```text
「代理服务器」轉「代理伺服器」，「缓存」轉「快取」，「延迟」轉「延遲」。
```

### blind-it-0040：match

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
我们需要记录每个请求的追踪编号。
```

Codex expected:

```text
我們需要記錄每個請求的追蹤編號。
```

Gemini expected:

```text
我們需要記錄每個請求的追蹤編號。
```

Gemini acceptable variants:

```text
我們需要記錄每個請求的追蹤編號。
我们需要记录每个请求的追踪编号。
```

Gemini notes:

```text
「我们」轉「我們」，「记录」轉「記錄」，「追踪编号」轉「追蹤編號」。
```

### blind-it-0041：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
如果数据库连接池耗尽，接口会暂时拒绝请求。
```

Codex expected:

```text
如果資料庫連線池耗盡，API 會暫時拒絕請求。
```

Gemini expected:

```text
如果資料庫連線集區用盡，介面會暫時拒絕請求。
```

Gemini acceptable variants:

```text
如果資料庫連線集區用盡，介面會暫時拒絕請求。
如果数据库连接池耗尽，接口会暂时拒绝请求。
```

Gemini notes:

```text
「数据库」轉「資料庫」，「连接池」轉「連線集區」，「耗尽」轉「用盡」，「接口」轉「介面」，「拒绝」轉「拒絕」。
```

### blind-it-0042：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
迁移脚本会先备份旧表再修改字段。
```

Codex expected:

```text
遷移指令碼會先備份舊資料表再修改欄位。
```

Gemini expected:

```text
移轉指令碼會先備份舊資料表再修改欄位。
```

Gemini acceptable variants:

```text
移轉指令碼會先備份舊資料表再修改欄位。
迁移脚本会先备份旧表再修改字段。
```

Gemini notes:

```text
「迁移」轉「移轉」，「脚本」轉「指令碼」，「备份」轉「備份」，「旧表」轉「舊資料表」，「字段」轉「欄位」。
```

### blind-it-0043：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
容器启动失败时，请检查镜像标签是否正确。
```

Codex expected:

```text
容器啟動失敗時，請檢查映像檔標籤是否正確。
```

Gemini expected:

```text
容器啟動失敗時，請檢查映像標籤是否正確。
```

Gemini acceptable variants:

```text
容器啟動失敗時，請檢查映像標籤是否正確。
容器启动失败时，请检查镜像标签是否正确。
```

Gemini notes:

```text
「启动」轉「啟動」，「失败」轉「失敗」，「请」轉「請」，「检查」轉「檢查」，「镜像」轉「映像」，「标签」轉「標籤」。
```

### blind-it-0044：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
这个钩子会在提交前格式化源代码。
```

Codex expected:

```text
這個鉤子會在提交前格式化原始碼。
```

Gemini expected:

```text
這個掛鉤會在認可前格式化原始碼。
```

Gemini acceptable variants:

```text
這個掛鉤會在認可前格式化原始碼。
这个钩子会在提交前格式化源代码。
```

Gemini notes:

```text
「这个」轉「這個」，「钩子」轉「掛鉤」，「提交」轉「認可」，「源代码」轉「原始碼」。
```

### blind-it-0045：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
监控面板显示队列长度持续升高。
```

Codex expected:

```text
監控儀表板顯示佇列長度持續升高。
```

Gemini expected:

```text
監控面板顯示佇列長度持續升高。
```

Gemini acceptable variants:

```text
監控面板顯示佇列長度持續升高。
监控面板显示队列长度持续升高。
```

Gemini notes:

```text
「监控」轉「監控」，「显示」轉「顯示」，「队列」轉「佇列」。
```

### blind-it-0046：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
请把错误报告附加到问题单里。
```

Codex expected:

```text
請把錯誤報告附加到問題單裡。
```

Gemini expected:

```text
請將錯誤報告附加到問題單裡。
```

Gemini acceptable variants:

```text
請將錯誤報告附加到問題單裡。
请把错误报告附加到问题单里。
```

Gemini notes:

```text
「请」轉「請」，「把」轉「將」，「问题单」轉「問題單」。
```

### blind-it-0047：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
服务端会验证回调地址的签名。
```

Codex expected:

```text
伺服器端會驗證回呼網址的簽章。
```

Gemini expected:

```text
伺服器端會驗證回呼位址的簽章。
```

Gemini acceptable variants:

```text
伺服器端會驗證回呼位址的簽章。
服务端会验证回调地址的签名。
```

Gemini notes:

```text
「服务端」轉「伺服器端」，「验证」轉「驗證」，「回调」轉「回呼」，「签名」轉「簽章」。
```

### blind-it-0048：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
测试环境使用独立的对象存储桶。
```

Codex expected:

```text
測試環境使用獨立的物件儲存桶。
```

Gemini expected:

```text
測試環境使用獨立的物件儲存貯體。
```

Gemini acceptable variants:

```text
測試環境使用獨立的物件儲存貯體。
测试环境使用独立的对象存储桶。
```

Gemini notes:

```text
「测试环境」轉「測試環境」，「独立」轉「獨立」，「对象存储桶」轉「物件儲存貯體」。
```

### blind-it-0049：match

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
如果证书即将过期，系统会提前发出告警。
```

Codex expected:

```text
如果憑證即將過期，系統會提前發出警示。
```

Gemini expected:

```text
如果憑證即將過期，系統會提前發出警示。
```

Gemini acceptable variants:

```text
如果憑證即將過期，系統會提前發出警示。
如果证书即将过期，系统会提前发出告警。
```

Gemini notes:

```text
「证书」轉「憑證」，「发出」轉「發出」，「告警」轉「警示」。
```

### blind-it-0050：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
这个 API 端点只接受 JSON 请求体。
```

Codex expected:

```text
這個 API 端點只接受 JSON 請求本文。
```

Gemini expected:

```text
這個 API 端點只接受 JSON 要求主體。
```

Gemini acceptable variants:

```text
這個 API 端點只接受 JSON 要求主體。
这个 API 端点只接受 JSON 请求体。
```

Gemini notes:

```text
「这个」轉「這個」，「请求体」轉「要求主體」。
```

### blind-it-0051：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
脚本会把临时文件写入工作目录。
```

Codex expected:

```text
指令碼會把暫存檔寫入工作目錄。
```

Gemini expected:

```text
指令碼會將暫存檔寫入工作目錄。
```

Gemini acceptable variants:

```text
指令碼會將暫存檔寫入工作目錄。
脚本会把临时文件写入工作目录。
```

Gemini notes:

```text
「脚本」轉「指令碼」，「把」轉「將」，「写入」轉「寫入」，「工作目录」轉「工作目錄」。
```

### blind-it-0052：different

- Domain: `it`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
请确认防火墙规则允许健康检查请求。
```

Codex expected:

```text
請確認防火牆規則允許健康檢查請求。
```

Gemini expected:

```text
請確認防火牆規則允許健康情況檢查請求。
```

Gemini acceptable variants:

```text
請確認防火牆規則允許健康情況檢查請求。
请确认防火墙规则允许健康检查请求。
```

Gemini notes:

```text
「请」轉「請」，「确认」轉「確認」，「防火墙」轉「防火牆」，「允许」轉「允許」，「健康检查」轉「健康情況檢查」。
```

### blind-it-0053：match

- Domain: `it`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
这个程序会保留用户自定义的模板名称。
```

Codex expected:

```text
這個程式會保留使用者自訂的範本名稱。
```

Gemini expected:

```text
這個程式會保留使用者自訂的範本名稱。
```

Gemini acceptable variants:

```text
這個程式會保留使用者自訂的範本名稱。
这个程序会保留用户自定义的模板名称。
```

Gemini notes:

```text
「这个」轉「這個」，「程序」轉「程式」，「用户」轉「使用者」，「自定义」轉「自訂」，「模板」轉「範本」。
```

### blind-it-0054：different

- Domain: `it`
- Risk: `over_conversion_guard`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
日志页面显示的项目名称不应该自动翻译。
```

Codex expected:

```text
日誌頁面顯示的專案名稱不應該自動翻譯。
```

Gemini expected:

```text
記錄頁面顯示的專案名稱不應該自動翻譯。
```

Gemini acceptable variants:

```text
記錄頁面顯示的專案名稱不應該自動翻譯。
日志页面显示的项目名称不应该自动翻译。
```

Gemini notes:

```text
「日志」轉「記錄」，「显示」轉「顯示」，「项目」轉「專案」，「应该」轉「應該」，「翻译」轉「翻譯」。
```

### blind-it-0055：different

- Domain: `it`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
测试资料里包含台北市政府开放资料的字段名。
```

Codex expected:

```text
測試資料裡包含台北市政府開放資料的欄位名稱。
```

Gemini expected:

```text
測試資料裡包含臺北市政府開放資料的欄位名稱。
```

Gemini acceptable variants:

```text
測試資料裡包含臺北市政府開放資料的欄位名稱。
测试资料里包含台北市政府开放资料的字段名。
```

Gemini notes:

```text
「测试」轉「測試」，「资料」轉「資料」，「台北」轉「臺北」，「开放资料」轉「開放資料」，「字段名」轉「欄位名稱」。
```

### blind-it-0056：different

- Domain: `it`
- Risk: `over_conversion_guard`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
请不要修改已经本地化的菜单文字。
```

Codex expected:

```text
請不要修改已經在地化的選單文字。
```

Gemini expected:

```text
請不要修改已經在地化的功能表文字。
```

Gemini acceptable variants:

```text
請不要修改已經在地化的功能表文字。
请不要修改已经本地化的菜单文字。
```

Gemini notes:

```text
「请」轉「請」，「已经」轉「已經」，「本地化」轉「在地化」，「菜单」轉「功能表」。
```

### blind-it-0057：different

- Domain: `it`
- Risk: `over_conversion_guard`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
这个仓库同时保存英文和台湾繁体 README。
```

Codex expected:

```text
這個儲存庫同時保存英文和台灣繁體 README。
```

Gemini expected:

```text
這個儲存庫同時儲存英文和臺灣繁體 README。
```

Gemini acceptable variants:

```text
這個儲存庫同時儲存英文和臺灣繁體 README。
这个仓库同时保存英文和台湾繁体 README。
```

Gemini notes:

```text
「这个」轉「這個」，「仓库」轉「儲存庫」，「保存」轉「儲存」，「台湾繁体」轉「臺灣繁體」。
```

### blind-it-0058：different

- Domain: `it`
- Risk: `baseline_guard`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
每次构建都会生成新的校验和。
```

Codex expected:

```text
每次建置都會產生新的校驗和。
```

Gemini expected:

```text
每次建置都會產生新的檢查碼。
```

Gemini acceptable variants:

```text
每次建置都會產生新的檢查碼。
每次构建都会生成新的校验和。
```

Gemini notes:

```text
「构建」轉「建置」，「生成」轉「產生」，「校验和」轉「檢查碼」。
```

### blind-it-0059：different

- Domain: `it`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
这个目录只保存临时缓存。
```

Codex expected:

```text
這個目錄只保存暫存快取。
```

Gemini expected:

```text
這個目錄只儲存暫存快取。
```

Gemini acceptable variants:

```text
這個目錄只儲存暫存快取。
这个目录只保存临时缓存。
```

Gemini notes:

```text
「这个」轉「這個」，「保存」轉「儲存」，「临时」轉「暫存」，「缓存」轉「快取」。
```

### blind-it-0060：match

- Domain: `it`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
管理员可以撤销过期的访问权限。
```

Codex expected:

```text
管理員可以撤銷過期的存取權限。
```

Gemini expected:

```text
管理員可以撤銷過期的存取權限。
```

Gemini acceptable variants:

```text
管理員可以撤銷過期的存取權限。
管理员可以撤销过期的访问权限。
```

Gemini notes:

```text
「管理员」轉「管理員」，「撤销」轉「撤銷」，「访问权限」轉「存取權限」。
```

### blind-it-0061：match

- Domain: `it`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
请在安装完成后重新启动服务。
```

Codex expected:

```text
請在安裝完成後重新啟動服務。
```

Gemini expected:

```text
請在安裝完成後重新啟動服務。
```

Gemini acceptable variants:

```text
請在安裝完成後重新啟動服務。
请在安装完成后重新启动服务。
```

Gemini notes:

```text
「请」轉「請」，「启动」轉「啟動」。
```

### blind-it-0062：match

- Domain: `it`
- Risk: `baseline_guard`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
系统会在七天后删除未使用的令牌。
```

Codex expected:

```text
系統會在七天後刪除未使用的權杖。
```

Gemini expected:

```text
系統會在七天後刪除未使用的權杖。
```

Gemini acceptable variants:

```text
系統會在七天後刪除未使用的權杖。
系统会在七天后删除未使用的令牌。
```

Gemini notes:

```text
「删除」轉「刪除」，「令牌」轉「權杖」。
```
