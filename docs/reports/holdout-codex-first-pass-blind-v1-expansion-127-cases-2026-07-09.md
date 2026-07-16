<!-- zhtw:disable -->
# Holdout Codex First-Pass Advisory - blind-v1 Expansion 127 Cases

Generated date: `2026-07-09`
Dataset: `blind-v1`
Inputs: `benchmarks/accuracy/blind-v1.inputs.json`
Expansion audit: `docs/reports/holdout-input-pool-expansion-blind-v1-2026-07-09.json`
Raw JSON: `docs/reports/holdout-codex-first-pass-blind-v1-expansion-127-cases-2026-07-09.json`
Stage: `first_pass_advisory`
Reviewer: `codex`

## Policy

- This report is advisory only.
- It is not ground truth and must not populate `blind-v1.expected.json` directly.
- Expected values still require maintainer confirmation after Gemini advisory review.
- Promotion is not allowed from this report.

## Summary

- Cases: 127
- Review-needed cases before maintainer decision: 71

Confidence:

- `high`: 87
- `medium`: 40

Domain distribution:

- `formal`: 18
- `high_risk`: 10
- `it`: 37
- `llm`: 17
- `social`: 18
- `ui`: 27

## Review Needed Queue

- `blind-it-0026` (it, candidate_gap, medium)
- `blind-it-0028` (it, candidate_gap, medium)
- `blind-it-0029` (it, candidate_gap, medium)
- `blind-it-0033` (it, candidate_gap, medium)
- `blind-it-0034` (it, candidate_gap, medium)
- `blind-it-0035` (it, candidate_gap, medium)
- `blind-it-0036` (it, candidate_gap, medium)
- `blind-it-0037` (it, candidate_gap, medium)
- `blind-it-0040` (it, candidate_gap, medium)
- `blind-it-0041` (it, candidate_gap, medium)
- `blind-it-0042` (it, candidate_gap, medium)
- `blind-it-0044` (it, candidate_gap, medium)
- `blind-it-0045` (it, candidate_gap, medium)
- `blind-it-0046` (it, candidate_gap, medium)
- `blind-it-0047` (it, candidate_gap, medium)
- `blind-it-0048` (it, candidate_gap, medium)
- `blind-it-0050` (it, candidate_gap, medium)
- `blind-it-0051` (it, candidate_gap, medium)
- `blind-it-0053` (it, over_conversion_guard, high)
- `blind-it-0054` (it, over_conversion_guard, medium)
- `blind-it-0055` (it, over_conversion_guard, high)
- `blind-it-0056` (it, over_conversion_guard, medium)
- `blind-it-0057` (it, over_conversion_guard, medium)
- `blind-it-0058` (it, baseline_guard, medium)
- `blind-it-0062` (it, baseline_guard, medium)
- `blind-ui-0021` (ui, candidate_gap, medium)
- `blind-ui-0025` (ui, candidate_gap, medium)
- `blind-ui-0028` (ui, candidate_gap, medium)
- `blind-ui-0030` (ui, candidate_gap, medium)
- `blind-ui-0034` (ui, candidate_gap, medium)
- `blind-ui-0035` (ui, candidate_gap, medium)
- `blind-ui-0038` (ui, candidate_gap, medium)
- `blind-ui-0039` (ui, over_conversion_guard, medium)
- `blind-ui-0040` (ui, over_conversion_guard, high)
- `blind-ui-0041` (ui, over_conversion_guard, high)
- `blind-ui-0042` (ui, over_conversion_guard, high)
- `blind-ui-0043` (ui, over_conversion_guard, high)
- `blind-ui-0044` (ui, over_conversion_guard, high)
- `blind-llm-0017` (llm, candidate_gap, medium)
- `blind-llm-0019` (llm, candidate_gap, medium)
- `blind-llm-0023` (llm, candidate_gap, medium)
- `blind-llm-0026` (llm, over_conversion_guard, high)
- `blind-llm-0027` (llm, over_conversion_guard, high)
- `blind-llm-0028` (llm, over_conversion_guard, high)
- `blind-llm-0029` (llm, over_conversion_guard, high)
- `blind-llm-0030` (llm, over_conversion_guard, high)
- `blind-formal-0023` (formal, candidate_gap, medium)
- `blind-formal-0026` (formal, over_conversion_guard, high)
- `blind-formal-0027` (formal, over_conversion_guard, high)
- `blind-formal-0028` (formal, over_conversion_guard, high)
- `blind-formal-0029` (formal, over_conversion_guard, high)
- `blind-formal-0030` (formal, over_conversion_guard, high)
- `blind-social-0019` (social, candidate_gap, medium)
- `blind-social-0024` (social, candidate_gap, medium)
- `blind-social-0025` (social, over_conversion_guard, high)
- `blind-social-0026` (social, over_conversion_guard, high)
- `blind-social-0027` (social, over_conversion_guard, high)
- `blind-social-0028` (social, over_conversion_guard, high)
- `blind-social-0029` (social, over_conversion_guard, medium)
- `blind-social-0030` (social, over_conversion_guard, high)
- `blind-social-0031` (social, over_conversion_guard, high)
- `blind-high-risk-0011` (high_risk, candidate_gap, medium)
- `blind-high-risk-0012` (high_risk, candidate_gap, high)
- `blind-high-risk-0013` (high_risk, candidate_gap, high)
- `blind-high-risk-0014` (high_risk, candidate_gap, high)
- `blind-high-risk-0015` (high_risk, candidate_gap, high)
- `blind-high-risk-0016` (high_risk, over_conversion_guard, high)
- `blind-high-risk-0017` (high_risk, over_conversion_guard, high)
- `blind-high-risk-0018` (high_risk, over_conversion_guard, high)
- `blind-high-risk-0019` (high_risk, baseline_guard, medium)
- `blind-high-risk-0020` (high_risk, baseline_guard, high)

## Cases

### blind-it-0026

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
这个接口会在请求超时后返回默认配置。
```

Codex expected:

```text
這個介面會在請求逾時後回傳預設設定。
```

Acceptable variants:

```text
這個 API 會在請求逾時後回傳預設設定。
```

Rationale:

```text
「接口」可依語境作「介面」或 API；HTTP「请求超时」採「請求逾時」。
```

### blind-it-0027

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
请把访问令牌保存到安全的密钥管理服务。
```

Codex expected:

```text
請把存取權杖儲存到安全的金鑰管理服務。
```

Acceptable variants:

```text
請把存取權杖保存到安全的金鑰管理服務。
```

Rationale:

```text
身分驗證語境採「存取權杖」「金鑰管理服務」。
```

### blind-it-0028

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
命令行工具支持批量上传日志文件。
```

Codex expected:

```text
命令列工具支援批次上傳日誌檔案。
```

Acceptable variants:

```text
命令列工具支援批次上傳記錄檔。
```

Rationale:

```text
「日志文件」在台灣 IT 語境可作「日誌檔案」或「記錄檔」，需看產品用語。
```

### blind-it-0029

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
如果依赖版本冲突，构建流程会直接失败。
```

Codex expected:

```text
如果相依套件版本衝突，建置流程會直接失敗。
```

Acceptable variants:

```text
如果依賴版本衝突，建置流程會直接失敗。
```

Rationale:

```text
「依赖版本」可指相依套件版本；台灣工程文件常用「建置」。
```

### blind-it-0030

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
新的 SDK 会在初始化时检查运行环境。
```

Codex expected:

```text
新的 SDK 會在初始化時檢查執行環境。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
「运行环境」轉為台灣 IT 常用「執行環境」。
```

### blind-it-0031

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
请在合并分支前先执行单元测试。
```

Codex expected:

```text
請在合併分支前先執行單元測試。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
版本控制語境「合并分支」採「合併分支」。
```

### blind-it-0032

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
服务器会根据请求头选择响应格式。
```

Codex expected:

```text
伺服器會根據請求標頭選擇回應格式。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
HTTP 語境採「請求標頭」「回應格式」。
```

### blind-it-0033

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term, regional_term`

Input:

```text
这个插件会扫描项目里的本地化资源。
```

Codex expected:

```text
這個外掛會掃描專案裡的在地化資源。
```

Acceptable variants:

```text
這個外掛會掃描專案裡的本地化資源。
```

Rationale:

```text
台灣產品語境常用「在地化」，但開發文件也常保留「本地化」。
```

### blind-it-0034

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
发布任务完成后，系统会发送部署摘要。
```

Codex expected:

```text
發布工作完成後，系統會傳送部署摘要。
```

Acceptable variants:

```text
發布任務完成後，系統會傳送部署摘要。
```

Rationale:

```text
「任务」可作「工作」或「任務」；此處偏工作流程語境。
```

### blind-it-0035

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
当网络中断时，客户端会排队重试。
```

Codex expected:

```text
當網路中斷時，用戶端會排隊重試。
```

Acceptable variants:

```text
當網路中斷時，客戶端會排隊重試。
```

Rationale:

```text
「客户端」台灣技術文件常見「用戶端」，但部分產品用「客戶端」。
```

### blind-it-0036

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
请在配置文件里关闭调试模式。
```

Codex expected:

```text
請在設定檔裡關閉偵錯模式。
```

Acceptable variants:

```text
請在設定檔裡關閉除錯模式。
```

Rationale:

```text
debug 在台灣常見「偵錯」與「除錯」兩種譯法，需看專案慣例。
```

### blind-it-0037

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
后台服务每天凌晨清理过期会话。
```

Codex expected:

```text
背景服務每天凌晨清理過期工作階段。
```

Acceptable variants:

```text
背景服務每天凌晨清理過期會話。
```

Rationale:

```text
「会话」在網頁/伺服器語境多作「工作階段」，但「會話」也可能被採用。
```

### blind-it-0038

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
这个参数只影响增量同步的批次大小。
```

Codex expected:

```text
這個參數只影響增量同步的批次大小。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
「参数」「批次大小」為台灣技術文件常用語；「增量同步」保留技術術語。
```

### blind-it-0039

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
代理服务器会缓存静态资源以降低延迟。
```

Codex expected:

```text
代理伺服器會快取靜態資源以降低延遲。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
「代理服务器」「缓存」分別轉為「代理伺服器」「快取」。
```

### blind-it-0040

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
我们需要记录每个请求的追踪编号。
```

Codex expected:

```text
我們需要記錄每個請求的追蹤編號。
```

Acceptable variants:

```text
我們需要記錄每個請求的追蹤 ID。
```

Rationale:

```text
trace id 可譯「追蹤編號」或保留 ID，需看產品風格。
```

### blind-it-0041

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
如果数据库连接池耗尽，接口会暂时拒绝请求。
```

Codex expected:

```text
如果資料庫連線池耗盡，API 會暫時拒絕請求。
```

Acceptable variants:

```text
如果資料庫連線池耗盡，介面會暫時拒絕請求。
```

Rationale:

```text
「接口」在此接近 API endpoint，先採 API；可接受「介面」。
```

### blind-it-0042

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
迁移脚本会先备份旧表再修改字段。
```

Codex expected:

```text
遷移指令碼會先備份舊資料表再修改欄位。
```

Acceptable variants:

```text
移轉指令碼會先備份舊資料表再修改欄位。
```

Rationale:

```text
資料庫 migration 在台灣文件可見「遷移」與「移轉」；需看專案慣例。
```

### blind-it-0043

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
容器启动失败时，请检查镜像标签是否正确。
```

Codex expected:

```text
容器啟動失敗時，請檢查映像檔標籤是否正確。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
容器語境「镜像标签」採「映像檔標籤」。
```

### blind-it-0044

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
这个钩子会在提交前格式化源代码。
```

Codex expected:

```text
這個鉤子會在提交前格式化原始碼。
```

Acceptable variants:

```text
這個 hook 會在提交前格式化原始碼。
```

Rationale:

```text
Git hook 可譯「鉤子」或保留英文 hook，需確認文件風格。
```

### blind-it-0045

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
监控面板显示队列长度持续升高。
```

Codex expected:

```text
監控儀表板顯示佇列長度持續升高。
```

Acceptable variants:

```text
監控面板顯示佇列長度持續升高。
```

Rationale:

```text
dashboard 可作「儀表板」或「面板」；queue 採「佇列」。
```

### blind-it-0046

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
请把错误报告附加到问题单里。
```

Codex expected:

```text
請把錯誤報告附加到問題單裡。
```

Acceptable variants:

```text
請把錯誤報告附加到議題裡。
```

Rationale:

```text
「问题单」可作 issue/問題單/議題；先採較直觀的「問題單」。
```

### blind-it-0047

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
服务端会验证回调地址的签名。
```

Codex expected:

```text
伺服器端會驗證回呼網址的簽章。
```

Acceptable variants:

```text
服務端會驗證回呼網址的簽章。
```

Rationale:

```text
「服务端」台灣技術文件多用「伺服器端」；callback address 採「回呼網址」。
```

### blind-it-0048

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
测试环境使用独立的对象存储桶。
```

Codex expected:

```text
測試環境使用獨立的物件儲存桶。
```

Acceptable variants:

```text
測試環境使用獨立的物件儲存貯體。
```

Rationale:

```text
object storage bucket 在不同雲端文件譯法不同，需確認產品採「儲存桶」或「貯體」。
```

### blind-it-0049

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
如果证书即将过期，系统会提前发出告警。
```

Codex expected:

```text
如果憑證即將過期，系統會提前發出警示。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
憑證/警示為台灣技術與安全語境常用語。
```

### blind-it-0050

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
这个 API 端点只接受 JSON 请求体。
```

Codex expected:

```text
這個 API 端點只接受 JSON 請求本文。
```

Acceptable variants:

```text
這個 API 端點只接受 JSON 請求主體。
```

Rationale:

```text
request body 有「請求本文」「請求主體」兩種常見譯法。
```

### blind-it-0051

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
脚本会把临时文件写入工作目录。
```

Codex expected:

```text
指令碼會把暫存檔寫入工作目錄。
```

Acceptable variants:

```text
腳本會把暫存檔寫入工作目錄。
```

Rationale:

```text
script 可作「指令碼」或「腳本」，需看文件風格。
```

### blind-it-0052

- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
请确认防火墙规则允许健康检查请求。
```

Codex expected:

```text
請確認防火牆規則允許健康檢查請求。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
「防火墙」「健康检查」皆有穩定台灣 IT 對應。
```

### blind-it-0053

- Domain: `it`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `it_term, over_conversion`

Input:

```text
这个程序会保留用户自定义的模板名称。
```

Codex expected:

```text
這個程式會保留使用者自訂的範本名稱。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
over-conversion guard；「模板」在台灣軟體語境作「範本」，但重點是保留自訂名稱。
```

### blind-it-0054

- Domain: `it`
- Risk: `over_conversion_guard`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term, over_conversion`

Input:

```text
日志页面显示的项目名称不应该自动翻译。
```

Codex expected:

```text
日誌頁面顯示的專案名稱不應該自動翻譯。
```

Acceptable variants:

```text
記錄檔頁面顯示的專案名稱不應該自動翻譯。
```

Rationale:

```text
over-conversion guard；log 可作日誌或記錄檔，專案名稱不得被改。
```

### blind-it-0055

- Domain: `it`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `it_term, regional_term, over_conversion`

Input:

```text
测试资料里包含台北市政府开放资料的字段名。
```

Codex expected:

```text
測試資料裡包含台北市政府開放資料的欄位名稱。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
over-conversion guard；台灣機關與開放資料語境需保守。
```

### blind-it-0056

- Domain: `it`
- Risk: `over_conversion_guard`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `ui_term, regional_term, over_conversion`

Input:

```text
请不要修改已经本地化的菜单文字。
```

Codex expected:

```text
請不要修改已經在地化的選單文字。
```

Acceptable variants:

```text
請不要修改已經本地化的選單文字。
```

Rationale:

```text
over-conversion guard；在地化/本地化需依產品用語確認。
```

### blind-it-0057

- Domain: `it`
- Risk: `over_conversion_guard`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term, regional_term, over_conversion`

Input:

```text
这个仓库同时保存英文和台湾繁体 README。
```

Codex expected:

```text
這個儲存庫同時保存英文和台灣繁體 README。
```

Acceptable variants:

```text
這個倉庫同時保存英文和台灣繁體 README。
```

Rationale:

```text
repository 在台灣常見「儲存庫」，但開發者口語也用「倉庫」。
```

### blind-it-0058

- Domain: `it`
- Risk: `baseline_guard`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
每次构建都会生成新的校验和。
```

Codex expected:

```text
每次建置都會產生新的校驗和。
```

Acceptable variants:

```text
每次建置都會產生新的檢查碼。
```

Rationale:

```text
checksum 可作「校驗和」或「檢查碼」，需確認技術文件慣例。
```

### blind-it-0059

- Domain: `it`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
这个目录只保存临时缓存。
```

Codex expected:

```text
這個目錄只保存暫存快取。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
「临时缓存」轉「暫存快取」。
```

### blind-it-0060

- Domain: `it`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
管理员可以撤销过期的访问权限。
```

Codex expected:

```text
管理員可以撤銷過期的存取權限。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
權限管理語境採「存取權限」。
```

### blind-it-0061

- Domain: `it`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
请在安装完成后重新启动服务。
```

Codex expected:

```text
請在安裝完成後重新啟動服務。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
一般軟體安裝語境，轉換穩定。
```

### blind-it-0062

- Domain: `it`
- Risk: `baseline_guard`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
系统会在七天后删除未使用的令牌。
```

Codex expected:

```text
系統會在七天後刪除未使用的權杖。
```

Acceptable variants:

```text
系統會在七天後刪除未使用的令牌。
```

Rationale:

```text
token 在安全語境多採「權杖」，但部分產品保留「令牌」。
```

### blind-ui-0021

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `ui_term`

Input:

```text
点击刷新按钮后，列表会重新加载。
```

Codex expected:

```text
點擊重新整理按鈕後，清單會重新載入。
```

Acceptable variants:

```text
點擊重新整理按鈕後，列表會重新載入。
```

Rationale:

```text
UI 語境「刷新」採「重新整理」；list 可作清單或列表。
```

### blind-ui-0022

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term, regional_term`

Input:

```text
请输入手机号码以接收验证码。
```

Codex expected:

```text
請輸入手機號碼以接收驗證碼。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
登入/驗證流程常用「手機號碼」「驗證碼」。
```

### blind-ui-0023

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
这个选项会影响通知的显示方式。
```

Codex expected:

```text
這個選項會影響通知的顯示方式。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
一般 UI 設定語句，轉換穩定。
```

### blind-ui-0024

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
如果上传失败，请稍后再试。
```

Codex expected:

```text
如果上傳失敗，請稍後再試。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
常見 UI 錯誤訊息。
```

### blind-ui-0025

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `ui_term`

Input:

```text
用户可以在设置页管理订阅方案。
```

Codex expected:

```text
使用者可以在設定頁管理訂閱方案。
```

Acceptable variants:

```text
使用者可以在設定頁管理訂閱計畫。
```

Rationale:

```text
subscription plan 可作「訂閱方案」或「訂閱計畫」。
```

### blind-ui-0026

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
搜索框会在输入三个字后显示建议。
```

Codex expected:

```text
搜尋框會在輸入三個字後顯示建議。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
「搜索框」採台灣 UI 常用「搜尋框」。
```

### blind-ui-0027

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term, formal_term`

Input:

```text
请先同意服务条款再继续。
```

Codex expected:

```text
請先同意服務條款再繼續。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
服務條款流程用語穩定。
```

### blind-ui-0028

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `ui_term`

Input:

```text
弹窗关闭后不会保存草稿内容。
```

Codex expected:

```text
彈出視窗關閉後不會儲存草稿內容。
```

Acceptable variants:

```text
彈窗關閉後不會儲存草稿內容。
```

Rationale:

```text
「弹窗」正式 UI 可作「彈出視窗」，產品短文案也可能用「彈窗」。
```

### blind-ui-0029

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term, it_term`

Input:

```text
这个页面会显示最近使用的文件。
```

Codex expected:

```text
這個頁面會顯示最近使用的檔案。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
「文件」在軟體 UI 語境轉「檔案」。
```

### blind-ui-0030

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `ui_term, regional_term`

Input:

```text
付款完成后，收据会寄到你的邮箱。
```

Codex expected:

```text
付款完成後，收據會寄到你的信箱。
```

Acceptable variants:

```text
付款完成後，收據會寄到你的電子信箱。
```

Rationale:

```text
email inbox 可作「信箱」或「電子信箱」，需看產品文案風格。
```

### blind-ui-0031

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term, it_term`

Input:

```text
请选择要导出的资料范围。
```

Codex expected:

```text
請選擇要匯出的資料範圍。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
資料匯出 UI 語句，轉換穩定。
```

### blind-ui-0032

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
删除账号前需要再次输入密码。
```

Codex expected:

```text
刪除帳號前需要再次輸入密碼。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
帳號/密碼 UI 用語穩定。
```

### blind-ui-0033

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
管理员可以隐藏侧边栏里的测试功能。
```

Codex expected:

```text
管理員可以隱藏側邊欄裡的測試功能。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
「侧边栏」採「側邊欄」。
```

### blind-ui-0034

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `ui_term`

Input:

```text
表单提交成功后会返回首页。
```

Codex expected:

```text
表單送出成功後會返回首頁。
```

Acceptable variants:

```text
表單提交成功後會返回首頁。
```

Rationale:

```text
台灣 UI 常用「送出表單」，但技術語境也可能保留「提交」。
```

### blind-ui-0035

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `ui_term`

Input:

```text
如果没有网络，应用会显示离线提示。
```

Codex expected:

```text
如果沒有網路，應用程式會顯示離線提示。
```

Acceptable variants:

```text
如果沒有網路，App 會顯示離線提示。
```

Rationale:

```text
「应用」可作「應用程式」或 App，需依產品語氣確認。
```

### blind-ui-0036

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
请拖动滑块调整音量。
```

Codex expected:

```text
請拖曳滑桿調整音量。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
UI 控制項語境採「拖曳」「滑桿」。
```

### blind-ui-0037

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
系统会根据语言设置显示日期格式。
```

Codex expected:

```text
系統會根據語言設定顯示日期格式。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
語言設定/日期格式用語穩定。
```

### blind-ui-0038

- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `ui_term, regional_term`

Input:

```text
登录逾时后，请重新验证身份。
```

Codex expected:

```text
登入逾時後，請重新驗證身分。
```

Acceptable variants:

```text
登入逾時後，請重新驗證身份。
```

Rationale:

```text
台灣正式用字偏「身分」，但「身份」也常見；需確認產品用字。
```

### blind-ui-0039

- Domain: `ui`
- Risk: `over_conversion_guard`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `ui_term, over_conversion`

Input:

```text
请确认收藏夹里的名称没有被自动替换。
```

Codex expected:

```text
請確認我的最愛裡的名稱沒有被自動替換。
```

Acceptable variants:

```text
請確認收藏夾裡的名稱沒有被自動替換。
```

Rationale:

```text
over-conversion guard；favorite UI 可作「我的最愛」或「收藏夾」。
```

### blind-ui-0040

- Domain: `ui`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `ui_term, regional_term, over_conversion`

Input:

```text
这个按钮文字已经由台湾团队审核。
```

Codex expected:

```text
這個按鈕文字已經由台灣團隊審核。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
over-conversion guard；已審核台灣文案不可再改壞。
```

### blind-ui-0041

- Domain: `ui`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `ui_term, over_conversion`

Input:

```text
页面标题里的品牌名称必须保持原样。
```

Codex expected:

```text
頁面標題裡的品牌名稱必須保持原樣。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
over-conversion guard；品牌名稱應保留。
```

### blind-ui-0042

- Domain: `ui`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `ui_term, regional_term, over_conversion`

Input:

```text
用户自订标签不会套用地区词转换。
```

Codex expected:

```text
使用者自訂標籤不會套用地區詞轉換。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
over-conversion guard；自訂標籤不應被地區詞規則改寫。
```

### blind-ui-0043

- Domain: `ui`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `ui_term, over_conversion`

Input:

```text
请保留繁体说明中的专有名词。
```

Codex expected:

```text
請保留繁體說明中的專有名詞。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
over-conversion guard；繁體說明中的專有名詞需保留。
```

### blind-ui-0044

- Domain: `ui`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `ui_term, over_conversion`

Input:

```text
导览列中的 OpenAPI 字样不需要转换。
```

Codex expected:

```text
導覽列中的 OpenAPI 字樣不需要轉換。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
over-conversion guard；英文技術名稱保留。
```

### blind-ui-0045

- Domain: `ui`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
这个页面目前没有任何通知。
```

Codex expected:

```text
這個頁面目前沒有任何通知。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
空狀態 UI 語句，轉換穩定。
```

### blind-ui-0046

- Domain: `ui`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
取消操作后会回到上一页。
```

Codex expected:

```text
取消操作後會回到上一頁。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
常見 UI 流程用語。
```

### blind-ui-0047

- Domain: `ui`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
密码长度必须至少八个字符。
```

Codex expected:

```text
密碼長度必須至少八個字元。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
密碼驗證訊息用語穩定。
```

### blind-llm-0016

- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
请把下面这段说明改写成更适合开发者阅读的版本。
```

Codex expected:

```text
請把下面這段說明改寫成更適合開發者閱讀的版本。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
LLM rewrite 指令，開發者文件語境穩定。
```

### blind-llm-0017

- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
这个模型会根据上下文生成摘要。
```

Codex expected:

```text
這個模型會根據上下文產生摘要。
```

Acceptable variants:

```text
這個模型會根據脈絡產生摘要。
```

Rationale:

```text
context 可作「上下文」或「脈絡」；LLM 文件常見兩者。
```

### blind-llm-0018

- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
回答时请先列出假设，再提供解决步骤。
```

Codex expected:

```text
回答時請先列出假設，再提供解決步驟。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
提示詞指令語句，轉換穩定。
```

### blind-llm-0019

- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
如果用户没有提供日志，请说明需要哪些信息。
```

Codex expected:

```text
如果使用者沒有提供日誌，請說明需要哪些資訊。
```

Acceptable variants:

```text
如果使用者沒有提供記錄檔，請說明需要哪些資訊。
```

Rationale:

```text
「日志」可作日誌或記錄檔，需看產品用語。
```

### blind-llm-0020

- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
这段提示词会要求模型输出 JSON 格式。
```

Codex expected:

```text
這段提示詞會要求模型輸出 JSON 格式。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
提示詞/JSON 格式用語穩定。
```

### blind-llm-0021

- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
请把客服回复改成简短且礼貌的语气。
```

Codex expected:

```text
請把客服回覆改成簡短且禮貌的語氣。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
客服回覆與語氣調整語句，轉換穩定。
```

### blind-llm-0022

- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
模型可能会把函数名称误认为普通词语。
```

Codex expected:

```text
模型可能會把函式名稱誤認為普通詞語。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
IT 語境「函数」採「函式」。
```

### blind-llm-0023

- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
生成的说明需要包含安装步骤和常见错误。
```

Codex expected:

```text
產生的說明需要包含安裝步驟和常見錯誤。
```

Acceptable variants:

```text
生成的說明需要包含安裝步驟和常見錯誤。
```

Rationale:

```text
LLM output 可作「產生」或「生成」，需看文件風格。
```

### blind-llm-0024

- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
请根据会议记录整理三点行动项目。
```

Codex expected:

```text
請根據會議紀錄整理三點行動項目。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
會議紀錄與行動項目用語穩定。
```

### blind-llm-0025

- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
如果资料不足，请不要编造版本号。
```

Codex expected:

```text
如果資料不足，請不要編造版本號。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
LLM groundedness 指令，轉換穩定。
```

### blind-llm-0026

- Domain: `llm`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `regional_term, over_conversion`

Input:

```text
请保留原文中的台湾用语，不要自动改写。
```

Codex expected:

```text
請保留原文中的台灣用語，不要自動改寫。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
over-conversion guard；明確要求保留台灣用語。
```

### blind-llm-0027

- Domain: `llm`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `it_term, over_conversion`

Input:

```text
系统提示词要求保留产品名称和变量名。
```

Codex expected:

```text
系統提示詞要求保留產品名稱和變數名稱。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
over-conversion guard；產品名稱與變數名稱不可改。
```

### blind-llm-0028

- Domain: `llm`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `regional_term, over_conversion`

Input:

```text
范例输出里的台北地址应保持原样。
```

Codex expected:

```text
範例輸出裡的台北地址應保持原樣。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
over-conversion guard；地名與地址需保守。
```

### blind-llm-0029

- Domain: `llm`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `over_conversion`

Input:

```text
请勿把已审核的繁体摘要再转换一次。
```

Codex expected:

```text
請勿把已審核的繁體摘要再轉換一次。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
over-conversion guard；已審核繁體不可二次轉壞。
```

### blind-llm-0030

- Domain: `llm`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `it_term, over_conversion`

Input:

```text
这段内容混合了英文 API 名称和中文说明。
```

Codex expected:

```text
這段內容混合了英文 API 名稱和中文說明。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
over-conversion guard；英文 API 名稱保留。
```

### blind-llm-0031

- Domain: `llm`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
请用两句话总结这篇文章。
```

Codex expected:

```text
請用兩句話總結這篇文章。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
一般摘要指令，轉換穩定。
```

### blind-llm-0032

- Domain: `llm`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
如果答案不确定，请明确说明限制。
```

Codex expected:

```text
如果答案不確定，請明確說明限制。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
一般回答限制指令，轉換穩定。
```

### blind-formal-0016

- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
本公司将于下周发布年度营运报告。
```

Codex expected:

```text
本公司將於下週發布年度營運報告。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
正式公告語境採「營運報告」。
```

### blind-formal-0017

- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
申请人应于期限内补交相关证明文件。
```

Codex expected:

```text
申請人應於期限內補交相關證明文件。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
正式文件語句，轉換穩定。
```

### blind-formal-0018

- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
会议主席宣布本案延后审议。
```

Codex expected:

```text
會議主席宣布本案延後審議。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
會議與審議用語穩定。
```

### blind-formal-0019

- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term, regional_term`

Input:

```text
该计划预计提升公共服务效率。
```

Codex expected:

```text
該計畫預計提升公共服務效率。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
正式文件「计划」採「計畫」。
```

### blind-formal-0020

- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
新闻稿表示，双方将建立长期合作机制。
```

Codex expected:

```text
新聞稿表示，雙方將建立長期合作機制。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
新聞稿語句，轉換穩定。
```

### blind-formal-0021

- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
委员会要求各部门提出改善方案。
```

Codex expected:

```text
委員會要求各部門提出改善方案。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
正式文件語句，轉換穩定。
```

### blind-formal-0022

- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
本次调查结果将作为后续政策参考。
```

Codex expected:

```text
本次調查結果將作為後續政策參考。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
政策文件語句，轉換穩定。
```

### blind-formal-0023

- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `formal_term`

Input:

```text
承办单位应保存完整申请记录。
```

Codex expected:

```text
承辦單位應保存完整申請紀錄。
```

Acceptable variants:

```text
承辦單位應保存完整申請記錄。
```

Rationale:

```text
正式文件可用「紀錄」或「記錄」，需確認用字慣例。
```

### blind-formal-0024

- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term, regional_term`

Input:

```text
报告指出，资料质量会影响统计结果。
```

Codex expected:

```text
報告指出，資料品質會影響統計結果。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
「资料质量」採台灣常用「資料品質」。
```

### blind-formal-0025

- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
公告内容将同步发布于官方网站。
```

Codex expected:

```text
公告內容將同步發布於官方網站。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
公告語句，轉換穩定。
```

### blind-formal-0026

- Domain: `formal`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `formal_term, high_risk_term, over_conversion`

Input:

```text
契约条款不得排除消费者依法享有的权利。
```

Codex expected:

```text
契約條款不得排除消費者依法享有的權利。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
法律/消保語境使用「契約條款」；over-conversion guard。
```

### blind-formal-0027

- Domain: `formal`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `formal_term, regional_term, over_conversion`

Input:

```text
既有用户权益不因系统更新而受影响。
```

Codex expected:

```text
既有使用者權益不因系統更新而受影響。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
formal + over-conversion guard；「既有使用者權益」需保留台灣產品語氣。
```

### blind-formal-0028

- Domain: `formal`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `formal_term, over_conversion`

Input:

```text
文件中的机关名称应依原核定名称记载。
```

Codex expected:

```text
文件中的機關名稱應依原核定名稱記載。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
正式文件中的機關名稱不得任意改寫。
```

### blind-formal-0029

- Domain: `formal`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `formal_term, regional_term, over_conversion`

Input:

```text
本案涉及台北市既有法规用语。
```

Codex expected:

```text
本案涉及台北市既有法規用語。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
台灣地名與法規用語需保守。
```

### blind-formal-0030

- Domain: `formal`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `formal_term, over_conversion`

Input:

```text
公文附件内的专有名词不得任意改写。
```

Codex expected:

```text
公文附件內的專有名詞不得任意改寫。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
over-conversion guard；公文專有名詞需保留。
```

### blind-formal-0031

- Domain: `formal`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
本通知自发布日起生效。
```

Codex expected:

```text
本通知自發布日起生效。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
正式通知語句，轉換穩定。
```

### blind-formal-0032

- Domain: `formal`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
请各单位依限完成资料汇整。
```

Codex expected:

```text
請各單位依限完成資料彙整。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
公文語氣常用「依限」「彙整」。
```

### blind-formal-0033

- Domain: `formal`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
相关费用由申请人自行负担。
```

Codex expected:

```text
相關費用由申請人自行負擔。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
正式文件費用負擔語句，轉換穩定。
```

### blind-social-0016

- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
周末要不要一起去看展？
```

Codex expected:

```text
週末要不要一起去看展？
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
日常口語，轉換穩定。
```

### blind-social-0017

- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
你有收到群组里的活动通知吗？
```

Codex expected:

```text
你有收到群組裡的活動通知嗎？
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
社群聊天語境採「群組」。
```

### blind-social-0018

- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
这家店的外带速度比上次快很多。
```

Codex expected:

```text
這家店的外帶速度比上次快很多。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
消費日常語句，轉換穩定。
```

### blind-social-0019

- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `regional_term, ui_term`

Input:

```text
我晚点再把照片上传到共享相册。
```

Codex expected:

```text
我晚點再把照片上傳到共享相簿。
```

Acceptable variants:

```text
我晚點再把照片上傳到共用相簿。
```

Rationale:

```text
shared album 可作「共享相簿」或「共用相簿」。
```

### blind-social-0020

- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
今天通勤时间比平常多了二十分钟。
```

Codex expected:

```text
今天通勤時間比平常多了二十分鐘。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
日常語句，轉換穩定。
```

### blind-social-0021

- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
朋友说这部影片的字幕翻得不错。
```

Codex expected:

```text
朋友說這部影片的字幕翻得不錯。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
影音日常語境，轉換穩定。
```

### blind-social-0022

- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
如果下雨，我们就改约室内场地。
```

Codex expected:

```text
如果下雨，我們就改約室內場地。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
日常約見語句，轉換穩定。
```

### blind-social-0023

- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
这杯饮料甜度可以调整吗？
```

Codex expected:

```text
這杯飲料甜度可以調整嗎？
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
台灣飲料店語境，轉換穩定。
```

### blind-social-0024

- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `regional_term, ui_term`

Input:

```text
我已经把购物清单发到聊天窗口了。
```

Codex expected:

```text
我已經把購物清單傳到聊天視窗了。
```

Acceptable variants:

```text
我已經把購物清單發到聊天視窗了。
```

Rationale:

```text
「发到聊天窗口」可作「傳到聊天視窗」或「發到聊天視窗」，需看口語程度。
```

### blind-social-0025

- Domain: `social`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `regional_term, over_conversion`

Input:

```text
留言里提到的台湾地名不要被改成其他说法。
```

Codex expected:

```text
留言裡提到的台灣地名不要被改成其他說法。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
over-conversion guard；台灣地名不可改。
```

### blind-social-0026

- Domain: `social`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `regional_term, over_conversion`

Input:

```text
这段贴文已经是台湾朋友写的繁体版本。
```

Codex expected:

```text
這段貼文已經是台灣朋友寫的繁體版本。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
over-conversion guard；已是台灣繁體版本。
```

### blind-social-0027

- Domain: `social`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `regional_term, over_conversion`

Input:

```text
昵称和频道名称应该保持原样。
```

Codex expected:

```text
暱稱和頻道名稱應該保持原樣。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
over-conversion guard；暱稱與頻道名稱需保留。
```

### blind-social-0028

- Domain: `social`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `regional_term, over_conversion`

Input:

```text
请不要把社群里的品牌标签自动转换。
```

Codex expected:

```text
請不要把社群裡的品牌標籤自動轉換。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
over-conversion guard；品牌標籤不可改。
```

### blind-social-0029

- Domain: `social`
- Risk: `over_conversion_guard`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `regional_term, over_conversion`

Input:

```text
影片标题里的台语罗马字不要改。
```

Codex expected:

```text
影片標題裡的台語羅馬字不要改。
```

Acceptable variants:

```text
影片標題裡的臺語羅馬字不要改。
```

Rationale:

```text
over-conversion guard；「台語/臺語」用字需看文件風格，羅馬字不可改。
```

### blind-social-0030

- Domain: `social`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `ui_term, over_conversion`

Input:

```text
用户自订表情名称需要原样保留。
```

Codex expected:

```text
使用者自訂表情名稱需要原樣保留。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
over-conversion guard；自訂表情名稱需保留。
```

### blind-social-0031

- Domain: `social`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `regional_term, over_conversion`

Input:

```text
这则评论混合了繁体和简体，先只作为输入保留。
```

Codex expected:

```text
這則評論混合了繁體和簡體，先只作為輸入保留。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
over-conversion guard；混合文本先作輸入，不應用來調詞庫。
```

### blind-social-0032

- Domain: `social`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
明天早上记得带雨伞。
```

Codex expected:

```text
明天早上記得帶雨傘。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
日常短句，轉換穩定。
```

### blind-social-0033

- Domain: `social`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
我先把晚餐订好，晚点再确认人数。
```

Codex expected:

```text
我先把晚餐訂好，晚點再確認人數。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
日常語句，轉換穩定。
```

### blind-high-risk-0011

- Domain: `high_risk`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `high_risk_term, regional_term`

Input:

```text
医师建议患者按时回诊并记录症状变化。
```

Codex expected:

```text
醫師建議病患按時回診並記錄症狀變化。
```

Acceptable variants:

```text
醫師建議患者按時回診並記錄症狀變化。
```

Rationale:

```text
醫療高風險；「患者/病患」需由 maintainer 確認，但台灣醫療語境常用「病患」。
```

### blind-high-risk-0012

- Domain: `high_risk`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term, regional_term`

Input:

```text
银行会在交易完成后发送电子对账单。
```

Codex expected:

```text
銀行會在交易完成後傳送電子對帳單。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
金融高風險；「对账单」採「對帳單」。
```

### blind-high-risk-0013

- Domain: `high_risk`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term`

Input:

```text
申请贷款前，请确认利率和还款期限。
```

Codex expected:

```text
申請貸款前，請確認利率和還款期限。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
金融高風險；貸款/利率/還款期限用語穩定但仍需人工確認。
```

### blind-high-risk-0014

- Domain: `high_risk`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term`

Input:

```text
药品说明应清楚标示使用剂量和禁忌。
```

Codex expected:

```text
藥品說明應清楚標示使用劑量和禁忌。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
醫療高風險；藥品劑量與禁忌用語需人工確認。
```

### blind-high-risk-0015

- Domain: `high_risk`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term, formal_term`

Input:

```text
保险契约变更需要经双方书面同意。
```

Codex expected:

```text
保險契約變更需要經雙方書面同意。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
保險/契約高風險；採台灣法律語境「契約」。
```

### blind-high-risk-0016

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term, formal_term, over_conversion`

Input:

```text
不得以格式条款免除故意或重大过失责任。
```

Codex expected:

```text
不得以定型化契約條款免除故意或重大過失責任。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
法律高風險；「格式条款」在台灣法規語境對應「定型化契約條款」。
```

### blind-high-risk-0017

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term, over_conversion`

Input:

```text
病历中的专有缩写不得任意改写。
```

Codex expected:

```text
病歷中的專有縮寫不得任意改寫。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
醫療高風險 + over-conversion guard；病歷縮寫不得改。
```

### blind-high-risk-0018

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term, over_conversion`

Input:

```text
金融机构应保留客户原始签署文件。
```

Codex expected:

```text
金融機構應保留客戶原始簽署文件。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
金融高風險 + over-conversion guard；簽署文件需保守。
```

### blind-high-risk-0019

- Domain: `high_risk`
- Risk: `baseline_guard`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `high_risk_term, regional_term`

Input:

```text
请妥善保管个人身份证件。
```

Codex expected:

```text
請妥善保管個人身分證件。
```

Acceptable variants:

```text
請妥善保管個人身份證件。
```

Rationale:

```text
身分/身份用字需確認；正式台灣用字偏「身分」。
```

### blind-high-risk-0020

- Domain: `high_risk`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term`

Input:

```text
未成年人开户需由法定代理人陪同。
```

Codex expected:

```text
未成年人開戶需由法定代理人陪同。
```

Acceptable variants:

```text
(none)
```

Rationale:

```text
金融/法律高風險；需人工確認。
```
