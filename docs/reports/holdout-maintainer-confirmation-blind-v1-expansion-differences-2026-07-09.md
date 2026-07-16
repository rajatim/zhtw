<!-- zhtw:disable -->
# Holdout Maintainer Confirmation Packet - blind-v1 Expansion Differences

Dataset: `blind-v1`
Source diff review: `docs/reports/holdout-codex-gemini-diff-review-blind-v1-expansion-127-cases-2026-07-09.json`
Raw JSON: `docs/reports/holdout-maintainer-confirmation-blind-v1-expansion-differences-2026-07-09.json`
Scope: `expansion_differences_only`

## Boundary

- This packet is for maintainer confirmation only.
- It includes only Codex/Gemini difference cases from the 127-case expansion.
- Codex/Gemini values are advisory; maintainer confirmation is the first human decision.
- Do not write these values into `blind-v1.expected.json` until maintainer decisions are recorded.
- `promotion_allowed = false` until expected values are confirmed and source metadata is updated.

## Summary

- Cases needing maintainer confirmation: 48
- Difference cases: 48
- Deferred policy-review cases: 33
- No immediate-question cases: 46

Difference recommendations:

- `codex`: 39
- `gemini`: 7
- `third_value`: 2

## How To Review

For each case, choose one:

- `OK` means accept `Recommended expected` unchanged.
- `EDIT` means write a replacement Taiwan Traditional expected value.
- `DROP` means remove the case from sealed holdout before benchmark.

## Difference Cases

### blind-it-0026：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

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

Recommended expected:

```text
這個介面會在請求逾時後回傳預設設定。
```

Reason:

IT/API 語境「回傳」比「傳回」更符合既有用語。

Maintainer decision:

```text

```

### blind-it-0027：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

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

Recommended expected:

```text
請把存取權杖儲存到安全的金鑰管理服務。
```

Reason:

Codex 較貼近原句「請把」，且不需提高正式語氣。

Maintainer decision:

```text

```

### blind-it-0028：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

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

Recommended expected:

```text
命令列工具支援批次上傳日誌檔案。
```

Reason:

「日誌檔案」較直接對應 log files；「記錄檔」可列 acceptable。

Maintainer decision:

```text

```

### blind-it-0029：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

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

Recommended expected:

```text
如果相依套件版本衝突，建置流程會直接失敗。
```

Reason:

「相依套件版本」「建置流程」比「相依性版本」「建置程序」更自然。

Maintainer decision:

```text

```

### blind-it-0032：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

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

Recommended expected:

```text
伺服器會根據請求標頭選擇回應格式。
```

Reason:

HTTP request header 建議作「請求標頭」，避免「要求標頭」。

Maintainer decision:

```text

```

### blind-it-0033：recommend `gemini`

- Domain: `it`
- Risk: `candidate_gap`

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

Recommended expected:

```text
這個外掛程式會掃描專案裡的在地化資源。
```

Reason:

「外掛程式」較完整正式，仍保留台灣軟體語境。

Maintainer decision:

```text

```

### blind-it-0034：recommend `third_value`

- Domain: `it`
- Risk: `candidate_gap`

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

Recommended expected:

```text
發布任務完成後，系統會傳送部署摘要。
```

Reason:

建議第三版「發布任務完成後，系統會傳送部署摘要。」：保留任務，但採 repo 慣用「發布」。

Maintainer decision:

```text

```

### blind-it-0035：recommend `gemini`

- Domain: `it`
- Risk: `candidate_gap`

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

Recommended expected:

```text
當網路中斷時，用戶端會排入佇列重試。
```

Reason:

「排入佇列重試」較符合系統行為描述。

Maintainer decision:

```text

```

### blind-it-0036：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

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

Recommended expected:

```text
請在設定檔裡關閉偵錯模式。
```

Reason:

此專案/一般開發者語境「設定檔」比「組態檔」更自然。

Maintainer decision:

```text

```

### blind-it-0037：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

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

Recommended expected:

```text
背景服務每天凌晨清理過期工作階段。
```

Reason:

「背景服務」「清理」較適合服務工作語境；避免「後台服務」。

Maintainer decision:

```text

```

### blind-it-0041：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

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

Recommended expected:

```text
如果資料庫連線池耗盡，API 會暫時拒絕請求。
```

Reason:

「連線池」較常見；「連線集區」偏特定廠商譯法。

Maintainer decision:

```text

```

### blind-it-0042：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

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

Recommended expected:

```text
遷移指令碼會先備份舊資料表再修改欄位。
```

Reason:

資料庫 migration 在工程文件中「遷移指令碼」可接受，Gemini 版可作 variant。

Maintainer decision:

```text

```

### blind-it-0043：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

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

Recommended expected:

```text
容器啟動失敗時，請檢查映像檔標籤是否正確。
```

Reason:

容器 image tag 建議「映像檔標籤」。

Maintainer decision:

```text

```

### blind-it-0044：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

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

Recommended expected:

```text
這個鉤子會在提交前格式化原始碼。
```

Reason:

Git commit 不宜譯成「認可」；Codex 版較自然。

Maintainer decision:

```text

```

### blind-it-0045：recommend `gemini`

- Domain: `it`
- Risk: `candidate_gap`

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

Recommended expected:

```text
監控面板顯示佇列長度持續升高。
```

Reason:

原句是「监控面板」，Gemini 的「監控面板」較貼近輸入且自然。

Maintainer decision:

```text

```

### blind-it-0046：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

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

Recommended expected:

```text
請把錯誤報告附加到問題單裡。
```

Reason:

Codex 保留「請把」語氣，Gemini 只是文體提高。

Maintainer decision:

```text

```

### blind-it-0047：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

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

Recommended expected:

```text
伺服器端會驗證回呼網址的簽章。
```

Reason:

callback address 在此較可能是 URL；「回呼網址」較明確。

Maintainer decision:

```text

```

### blind-it-0048：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

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

Recommended expected:

```text
測試環境使用獨立的物件儲存桶。
```

Reason:

「物件儲存桶」較泛用；「貯體」偏特定雲端廠商。

Maintainer decision:

```text

```

### blind-it-0050：recommend `third_value`

- Domain: `it`
- Risk: `candidate_gap`

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

Recommended expected:

```text
這個 API 端點只接受 JSON 請求主體。
```

Reason:

建議第三版「這個 API 端點只接受 JSON 請求主體。」：保留請求語境並採較自然的 body 譯法。

Maintainer decision:

```text

```

### blind-it-0051：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

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

Recommended expected:

```text
指令碼會把暫存檔寫入工作目錄。
```

Reason:

差異只在「把/將」，Codex 較貼近原句。

Maintainer decision:

```text

```

### blind-it-0052：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

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

Recommended expected:

```text
請確認防火牆規則允許健康檢查請求。
```

Reason:

「健康情況檢查」不如「健康檢查」自然。

Maintainer decision:

```text

```

### blind-it-0054：recommend `codex`

- Domain: `it`
- Risk: `over_conversion_guard`

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

Recommended expected:

```text
日誌頁面顯示的專案名稱不應該自動翻譯。
```

Reason:

log page 作「日誌頁面」比「記錄頁面」清楚。

Maintainer decision:

```text

```

### blind-it-0055：recommend `codex`

- Domain: `it`
- Risk: `over_conversion_guard`

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

Recommended expected:

```text
測試資料裡包含台北市政府開放資料的欄位名稱。
```

Reason:

repo 目前慣用「台灣/台北」，保留「台北市政府」。

Maintainer decision:

```text

```

### blind-it-0056：recommend `codex`

- Domain: `it`
- Risk: `over_conversion_guard`

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

Recommended expected:

```text
請不要修改已經在地化的選單文字。
```

Reason:

UI 語境「選單」比「功能表」更符合現代產品文案。

Maintainer decision:

```text

```

### blind-it-0057：recommend `codex`

- Domain: `it`
- Risk: `over_conversion_guard`

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

Recommended expected:

```text
這個儲存庫同時保存英文和台灣繁體 README。
```

Reason:

repo 慣用「台灣」；「保存」在此可接受。

Maintainer decision:

```text

```

### blind-it-0058：recommend `gemini`

- Domain: `it`
- Risk: `baseline_guard`

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

Recommended expected:

```text
每次建置都會產生新的檢查碼。
```

Reason:

checksum 在台灣使用者文件中「檢查碼」較自然。

Maintainer decision:

```text

```

### blind-it-0059：recommend `gemini`

- Domain: `it`
- Risk: `baseline_guard`

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

Recommended expected:

```text
這個目錄只儲存暫存快取。
```

Reason:

「儲存」比「保存」更符合一般台灣軟體用語。

Maintainer decision:

```text

```

### blind-ui-0030：recommend `codex`

- Domain: `ui`
- Risk: `candidate_gap`

Input:

```text
付款完成后，收据会寄到你的邮箱。
```

Codex expected:

```text
付款完成後，收據會寄到你的信箱。
```

Gemini expected:

```text
付款完成後，收據會寄到你的電子郵件信箱。
```

Recommended expected:

```text
付款完成後，收據會寄到你的信箱。
```

Reason:

UI 文案「信箱」較短且自然，Gemini 版過長。

Maintainer decision:

```text

```

### blind-ui-0034：recommend `codex`

- Domain: `ui`
- Risk: `candidate_gap`

Input:

```text
表单提交成功后会返回首页。
```

Codex expected:

```text
表單送出成功後會返回首頁。
```

Gemini expected:

```text
表單提交成功後會返回首頁。
```

Recommended expected:

```text
表單送出成功後會返回首頁。
```

Reason:

UI 動作採「送出表單」較符合台灣產品文案。

Maintainer decision:

```text

```

### blind-ui-0039：recommend `gemini`

- Domain: `ui`
- Risk: `over_conversion_guard`

Input:

```text
请确认收藏夹里的名称没有被自动替换。
```

Codex expected:

```text
請確認我的最愛裡的名稱沒有被自動替換。
```

Gemini expected:

```text
請確認我的最愛裡的名稱沒有被自動取代。
```

Recommended expected:

```text
請確認我的最愛裡的名稱沒有被自動取代。
```

Reason:

「取代」比「替換」更常見於台灣 UI 文案。

Maintainer decision:

```text

```

### blind-ui-0040：recommend `codex`

- Domain: `ui`
- Risk: `over_conversion_guard`

Input:

```text
这个按钮文字已经由台湾团队审核。
```

Codex expected:

```text
這個按鈕文字已經由台灣團隊審核。
```

Gemini expected:

```text
這個按鈕文字已經由臺灣團隊審核。
```

Recommended expected:

```text
這個按鈕文字已經由台灣團隊審核。
```

Reason:

repo 慣用「台灣」。

Maintainer decision:

```text

```

### blind-llm-0016：recommend `codex`

- Domain: `llm`
- Risk: `candidate_gap`

Input:

```text
请把下面这段说明改写成更适合开发者阅读的版本。
```

Codex expected:

```text
請把下面這段說明改寫成更適合開發者閱讀的版本。
```

Gemini expected:

```text
請將下方這段說明改寫成更適合開發者閱讀的版本。
```

Recommended expected:

```text
請把下面這段說明改寫成更適合開發者閱讀的版本。
```

Reason:

Codex 較貼近原句「下面」，不需改成「下方」。

Maintainer decision:

```text

```

### blind-llm-0017：recommend `codex`

- Domain: `llm`
- Risk: `candidate_gap`

Input:

```text
这个模型会根据上下文生成摘要。
```

Codex expected:

```text
這個模型會根據上下文產生摘要。
```

Gemini expected:

```text
這個模型會根據上下文生成摘要。
```

Recommended expected:

```text
這個模型會根據上下文產生摘要。
```

Reason:

「產生摘要」較自然；「生成」可列 acceptable。

Maintainer decision:

```text

```

### blind-llm-0021：recommend `codex`

- Domain: `llm`
- Risk: `candidate_gap`

Input:

```text
请把客服回复改成简短且礼貌的语气。
```

Codex expected:

```text
請把客服回覆改成簡短且禮貌的語氣。
```

Gemini expected:

```text
請將客服回覆改為簡短且禮貌的語氣。
```

Recommended expected:

```text
請把客服回覆改成簡短且禮貌的語氣。
```

Reason:

Codex 較貼近原句語氣。

Maintainer decision:

```text

```

### blind-llm-0022：recommend `codex`

- Domain: `llm`
- Risk: `candidate_gap`

Input:

```text
模型可能会把函数名称误认为普通词语。
```

Codex expected:

```text
模型可能會把函式名稱誤認為普通詞語。
```

Gemini expected:

```text
模型可能會將函式名稱誤認為普通詞語。
```

Recommended expected:

```text
模型可能會把函式名稱誤認為普通詞語。
```

Reason:

差異只在「把/將」，Codex 較貼近原句。

Maintainer decision:

```text

```

### blind-llm-0024：recommend `codex`

- Domain: `llm`
- Risk: `candidate_gap`

Input:

```text
请根据会议记录整理三点行动项目。
```

Codex expected:

```text
請根據會議紀錄整理三點行動項目。
```

Gemini expected:

```text
請根據會議記錄整理三點行動項目。
```

Recommended expected:

```text
請根據會議紀錄整理三點行動項目。
```

Reason:

「會議紀錄」是台灣常用固定寫法。

Maintainer decision:

```text

```

### blind-llm-0026：recommend `codex`

- Domain: `llm`
- Risk: `over_conversion_guard`

Input:

```text
请保留原文中的台湾用语，不要自动改写。
```

Codex expected:

```text
請保留原文中的台灣用語，不要自動改寫。
```

Gemini expected:

```text
請保留原文中的臺灣用語，不要自動改寫。
```

Recommended expected:

```text
請保留原文中的台灣用語，不要自動改寫。
```

Reason:

repo 慣用「台灣」。

Maintainer decision:

```text

```

### blind-llm-0028：recommend `codex`

- Domain: `llm`
- Risk: `over_conversion_guard`

Input:

```text
范例输出里的台北地址应保持原样。
```

Codex expected:

```text
範例輸出裡的台北地址應保持原樣。
```

Gemini expected:

```text
範例輸出裡的臺北地址應保持原樣。
```

Recommended expected:

```text
範例輸出裡的台北地址應保持原樣。
```

Reason:

repo 慣用「台北」。

Maintainer decision:

```text

```

### blind-llm-0029：recommend `codex`

- Domain: `llm`
- Risk: `over_conversion_guard`

Input:

```text
请勿把已审核的繁体摘要再转换一次。
```

Codex expected:

```text
請勿把已審核的繁體摘要再轉換一次。
```

Gemini expected:

```text
請勿將已審核的繁體摘要再轉換一次。
```

Recommended expected:

```text
請勿把已審核的繁體摘要再轉換一次。
```

Reason:

差異只在「把/將」，Codex 較貼近原句。

Maintainer decision:

```text

```

### blind-formal-0027：recommend `codex`

- Domain: `formal`
- Risk: `over_conversion_guard`

Input:

```text
既有用户权益不因系统更新而受影响。
```

Codex expected:

```text
既有使用者權益不因系統更新而受影響。
```

Gemini expected:

```text
既有用戶權益不因系統更新而受影響。
```

Recommended expected:

```text
既有使用者權益不因系統更新而受影響。
```

Reason:

產品/權益語境「使用者」比「用戶」更符合既有 policy。

Maintainer decision:

```text

```

### blind-formal-0029：recommend `codex`

- Domain: `formal`
- Risk: `over_conversion_guard`

Input:

```text
本案涉及台北市既有法规用语。
```

Codex expected:

```text
本案涉及台北市既有法規用語。
```

Gemini expected:

```text
本案涉及臺北市既有法規用語。
```

Recommended expected:

```text
本案涉及台北市既有法規用語。
```

Reason:

repo 慣用「台北」。

Maintainer decision:

```text

```

### blind-social-0016：recommend `codex`

- Domain: `social`
- Risk: `candidate_gap`

Input:

```text
周末要不要一起去看展？
```

Codex expected:

```text
週末要不要一起去看展？
```

Gemini expected:

```text
週末要不要一起去看展覽？
```

Recommended expected:

```text
週末要不要一起去看展？
```

Reason:

「看展」是自然社群口語，不需擴成「看展覽」。

Maintainer decision:

```text

```

### blind-social-0024：recommend `codex`

- Domain: `social`
- Risk: `candidate_gap`

Input:

```text
我已经把购物清单发到聊天窗口了。
```

Codex expected:

```text
我已經把購物清單傳到聊天視窗了。
```

Gemini expected:

```text
我已經把購物清單發到聊天視窗了。
```

Recommended expected:

```text
我已經把購物清單傳到聊天視窗了。
```

Reason:

聊天語境「傳到聊天視窗」較自然。

Maintainer decision:

```text

```

### blind-social-0025：recommend `codex`

- Domain: `social`
- Risk: `over_conversion_guard`

Input:

```text
留言里提到的台湾地名不要被改成其他说法。
```

Codex expected:

```text
留言裡提到的台灣地名不要被改成其他說法。
```

Gemini expected:

```text
留言裡提到的臺灣地名不要被改成其他說法。
```

Recommended expected:

```text
留言裡提到的台灣地名不要被改成其他說法。
```

Reason:

repo 慣用「台灣」。

Maintainer decision:

```text

```

### blind-social-0026：recommend `codex`

- Domain: `social`
- Risk: `over_conversion_guard`

Input:

```text
这段贴文已经是台湾朋友写的繁体版本。
```

Codex expected:

```text
這段貼文已經是台灣朋友寫的繁體版本。
```

Gemini expected:

```text
這段貼文已經是臺灣朋友寫的繁體版本。
```

Recommended expected:

```text
這段貼文已經是台灣朋友寫的繁體版本。
```

Reason:

repo 慣用「台灣」。

Maintainer decision:

```text

```

### blind-social-0029：recommend `codex`

- Domain: `social`
- Risk: `over_conversion_guard`

Input:

```text
影片标题里的台语罗马字不要改。
```

Codex expected:

```text
影片標題裡的台語羅馬字不要改。
```

Gemini expected:

```text
影片標題裡的臺語羅馬字不要改。
```

Recommended expected:

```text
影片標題裡的台語羅馬字不要改。
```

Reason:

repo 慣用「台語」，羅馬字保留。

Maintainer decision:

```text

```

### blind-high-risk-0012：recommend `gemini`

- Domain: `high_risk`
- Risk: `candidate_gap`

Input:

```text
银行会在交易完成后发送电子对账单。
```

Codex expected:

```text
銀行會在交易完成後傳送電子對帳單。
```

Gemini expected:

```text
銀行會在交易完成後寄送電子對帳單。
```

Recommended expected:

```text
銀行會在交易完成後寄送電子對帳單。
```

Reason:

金融通知語境「寄送電子對帳單」較自然。

Maintainer decision:

```text

```

### blind-high-risk-0016：recommend `codex`

- Domain: `high_risk`
- Risk: `over_conversion_guard`

Input:

```text
不得以格式条款免除故意或重大过失责任。
```

Codex expected:

```text
不得以定型化契約條款免除故意或重大過失責任。
```

Gemini expected:

```text
不得以格式條款免除故意或重大過失責任。
```

Recommended expected:

```text
不得以定型化契約條款免除故意或重大過失責任。
```

Reason:

台灣法律語境應採「定型化契約條款」，Gemini 直譯不宜。

Maintainer decision:

```text

```
