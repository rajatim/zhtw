<!-- zhtw:disable -->
# Holdout Maintainer Confirmation Packet - blind-v1 batch7 100 cases

Generated: 2026-07-10

This packet is for maintainer confirmation only. It is not ground truth and does not write private expected values.

## Summary

- Total review cases: 65
- Difference cases: 28
- Policy review cases: 37
- No immediate question: 35
- Difference recommendations: {"codex": 19, "gemini": 6, "third": 3}
- zhtw current status for differences: {"in_recommended_acceptable": 5, "matches_recommended": 8, "needs_followup_if_confirmed": 15}

## Difference Cases

### blind-it-0139

- Domain: it
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: in_recommended_acceptable
- Reason: 「轉送流量」較符合網路流量 routing 語境；Gemini 的「轉發」可作 variant。

Input:
```text
服务网格会根据路由规则转发流量。
```

Codex:
```text
服務網格會根據路由規則轉送流量。
```

Gemini:
```text
服務網格會根據路由規則轉發流量。
```

Recommended:
```text
服務網格會根據路由規則轉送流量。
```

zhtw current:
```text
服務網格會根據路由規則轉發流量。
```

### blind-it-0141

- Domain: it
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: matches_recommended
- Reason: Codex 較保留原句語氣；「記錄/紀錄」皆常見。

Input:
```text
批处理任务会把失败记录写入重试队列。
```

Codex:
```text
批次處理任務會把失敗記錄寫入重試佇列。
```

Gemini:
```text
批次處理任務會將失敗紀錄寫入重試佇列。
```

Recommended:
```text
批次處理任務會把失敗記錄寫入重試佇列。
```

zhtw current:
```text
批次處理任務會把失敗記錄寫入重試佇列。
```

### blind-it-0142

- Domain: it
- Risk: candidate_gap
- Recommendation: gemini
- zhtw current status: needs_followup_if_confirmed
- Reason: Gemini 的「設定對應」比直譯「設定映射」自然；若指 Kubernetes 專名，ConfigMap 可作 acceptable。

Input:
```text
请确认配置映射已经同步到所有命名空间。
```

Codex:
```text
請確認設定映射已經同步到所有命名空間。
```

Gemini:
```text
請確認設定對應已經同步到所有命名空間。
```

Recommended:
```text
請確認設定對應已經同步到所有命名空間。
```

zhtw current:
```text
請確認配置對映已經同步到所有命名空間。
```

### blind-it-0143

- Domain: it
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: matches_recommended
- Reason: token refresh 在技術語境用「重新整理」較貼近 refresh。

Input:
```text
客户端 SDK 会自动刷新过期的访问令牌。
```

Codex:
```text
用戶端 SDK 會自動重新整理過期的存取權杖。
```

Gemini:
```text
用戶端 SDK 會自動更新過期的存取權杖。
```

Recommended:
```text
用戶端 SDK 會自動重新整理過期的存取權杖。
```

zhtw current:
```text
用戶端 SDK 會自動重新整理過期的存取權杖。
```

### blind-it-0145

- Domain: it
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: needs_followup_if_confirmed
- Reason: 「每個事件」比「每條事件」更自然。

Input:
```text
消息订阅者需要手动确认每条事件。
```

Codex:
```text
訊息訂閱者需要手動確認每個事件。
```

Gemini:
```text
訊息訂閱者需要手動確認每條事件。
```

Recommended:
```text
訊息訂閱者需要手動確認每個事件。
```

zhtw current:
```text
消息訂閱者需要手動確認每條事件。
```

### blind-it-0146

- Domain: it
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: needs_followup_if_confirmed
- Reason: Gemini 的「相依性版本」不夠精確；Codex 的「相依套件版本」較適合開發文件。

Input:
```text
部署脚本会先检查目标环境的依赖版本。
```

Codex:
```text
部署指令碼會先檢查目標環境的相依套件版本。
```

Gemini:
```text
部署腳本會先檢查目標環境的相依性版本。
```

Recommended:
```text
部署指令碼會先檢查目標環境的相依套件版本。
```

zhtw current:
```text
部署指令碼會先檢查目標環境的相依性版本。
```

### blind-it-0147

- Domain: it
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: needs_followup_if_confirmed
- Reason: 台灣技術文件常用「彙整」；「聚合」可作較技術化 variant。

Input:
```text
日志聚合服务会按追踪编号关联请求。
```

Codex:
```text
日誌彙整服務會依追蹤編號關聯請求。
```

Gemini:
```text
日誌聚合服務會依追蹤編號關聯請求。
```

Recommended:
```text
日誌彙整服務會依追蹤編號關聯請求。
```

zhtw current:
```text
日誌聚合服務會按追蹤編號關聯請求。
```

### blind-it-0149

- Domain: it
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: matches_recommended
- Reason: Codex 較保留原句「把」語氣，Gemini variant 也可接受。

Input:
```text
请把连接超时设置写入环境变量。
```

Codex:
```text
請把連線逾時設定寫入環境變數。
```

Gemini:
```text
請將連線逾時設定寫入環境變數。
```

Recommended:
```text
請把連線逾時設定寫入環境變數。
```

zhtw current:
```text
請把連線逾時設定寫入環境變數。
```

### blind-it-0150

- Domain: it
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: needs_followup_if_confirmed
- Reason: Codex 較保留原句語氣；Gemini 的「將」可作 variant。

Input:
```text
这个适配器会把字段名称转换成蛇形命名。
```

Codex:
```text
這個轉接器會把欄位名稱轉換成蛇形命名。
```

Gemini:
```text
這個轉接器會將欄位名稱轉換成蛇形命名。
```

Recommended:
```text
這個轉接器會把欄位名稱轉換成蛇形命名。
```

zhtw current:
```text
這個變壓器會把欄位名稱轉換成蛇形命名。
```

### blind-it-0151

- Domain: it
- Risk: candidate_gap
- Recommendation: third
- zhtw current status: needs_followup_if_confirmed
- Reason: 結合 Codex 的標點與 Gemini 的「管線」作為 CI/CD pipeline primary。

Input:
```text
构建系统会缓存依赖包以缩短流水线时间。
```

Codex:
```text
建置系統會快取相依套件，以縮短流水線時間。
```

Gemini:
```text
建置系統會快取相依套件以縮短管線時間。
```

Recommended:
```text
建置系統會快取相依套件，以縮短管線時間。
```

zhtw current:
```text
建置系統會快取相依性包以縮短流水線時間。
```

### blind-it-0152

- Domain: it
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: needs_followup_if_confirmed
- Reason: 「容錯移轉/復原」較符合台灣技術文件語氣。

Input:
```text
故障转移完成后，监控系统会发送恢复通知。
```

Codex:
```text
容錯移轉完成後，監控系統會傳送復原通知。
```

Gemini:
```text
容錯移轉完成後，監控系統會發送恢復通知。
```

Recommended:
```text
容錯移轉完成後，監控系統會傳送復原通知。
```

zhtw current:
```text
故障轉移完成後，監控系統會發送恢復通知。
```

### blind-it-0153

- Domain: it
- Risk: candidate_gap
- Recommendation: third
- zhtw current status: needs_followup_if_confirmed
- Reason: 「漏洞」較貼近 input 的漏洞；保留 Codex/Gemini 共同的高風險與映像檔用法。

Input:
```text
容器镜像扫描会阻止含高危漏洞的版本发布。
```

Codex:
```text
容器映像檔掃描會阻止含高風險弱點的版本發布。
```

Gemini:
```text
容器映像檔掃描會阻止含有高風險漏洞的版本發布。
```

Recommended:
```text
容器映像檔掃描會阻止含高風險漏洞的版本發布。
```

zhtw current:
```text
容器映像檔掃描會阻止含高危漏洞的版本發布。
```

### blind-it-0154

- Domain: it
- Risk: candidate_gap
- Recommendation: gemini
- zhtw current status: matches_recommended
- Reason: 「租戶」較精簡自然；API 閘道可作 technical variant。

Input:
```text
接口网关会限制每个租户的请求速率。
```

Codex:
```text
介面閘道會限制每個租用戶的請求速率。
```

Gemini:
```text
介面閘道會限制每個租戶的請求速率。
```

Recommended:
```text
介面閘道會限制每個租戶的請求速率。
```

zhtw current:
```text
介面閘道會限制每個租戶的請求速率。
```

### blind-it-0155

- Domain: it
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: needs_followup_if_confirmed
- Reason: Codex 的「工作排程器」較符合 scheduler 在台灣軟體語境的常見說法。

Input:
```text
任务调度器会跳过已经停用的实例。
```

Codex:
```text
工作排程器會跳過已經停用的執行個體。
```

Gemini:
```text
任務排程器會跳過已經停用的執行個體。
```

Recommended:
```text
工作排程器會跳過已經停用的執行個體。
```

zhtw current:
```text
任務調度器會跳過已經停用的實例。
```

### blind-it-0156

- Domain: it
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: needs_followup_if_confirmed
- Reason: 「移轉」較符合台灣資料庫 migration 文件語境。

Input:
```text
请在迁移前导出当前表结构。
```

Codex:
```text
請在移轉前匯出目前資料表結構。
```

Gemini:
```text
請在遷移前匯出目前的資料表結構。
```

Recommended:
```text
請在移轉前匯出目前資料表結構。
```

zhtw current:
```text
請在遷移前匯出當前表結構。
```

### blind-it-0157

- Domain: it
- Risk: candidate_gap
- Recommendation: gemini
- zhtw current status: needs_followup_if_confirmed
- Reason: CLI 語境用「指令」較自然。

Input:
```text
这个命令会列出所有可用的扩展模块。
```

Codex:
```text
這個命令會列出所有可用的擴充模組。
```

Gemini:
```text
這個指令會列出所有可用的擴充模組。
```

Recommended:
```text
這個指令會列出所有可用的擴充模組。
```

zhtw current:
```text
這個命令會列出所有可用的擴充功能模組。
```

### blind-ui-0108

- Domain: ui
- Risk: candidate_gap
- Recommendation: gemini
- zhtw current status: needs_followup_if_confirmed
- Reason: UI 狀態常用「收合」描述 collapse。

Input:
```text
筛选器面板可以按状态折叠。
```

Codex:
```text
篩選器面板可以依狀態摺疊。
```

Gemini:
```text
篩選器面板可以依狀態收合。
```

Recommended:
```text
篩選器面板可以依狀態收合。
```

zhtw current:
```text
篩選器面板可以按狀態摺疊。
```

### blind-ui-0111

- Domain: ui
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: matches_recommended
- Reason: 台灣 UI 文件常用「進度列」。

Input:
```text
上传进度条需要显示剩余时间。
```

Codex:
```text
上傳進度列需要顯示剩餘時間。
```

Gemini:
```text
上傳進度條需要顯示剩餘時間。
```

Recommended:
```text
上傳進度列需要顯示剩餘時間。
```

zhtw current:
```text
上傳進度列需要顯示剩餘時間。
```

### blind-ui-0117

- Domain: ui
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: in_recommended_acceptable
- Reason: 「多選選單/已選取」較符合 UI 文案。

Input:
```text
多选菜单会显示已选择项目数量。
```

Codex:
```text
多選選單會顯示已選取項目數量。
```

Gemini:
```text
複選選單會顯示已選擇項目數量。
```

Recommended:
```text
多選選單會顯示已選取項目數量。
```

zhtw current:
```text
多選選單會顯示已選擇項目數量。
```

### blind-ui-0118

- Domain: ui
- Risk: candidate_gap
- Recommendation: third
- zhtw current status: needs_followup_if_confirmed
- Reason: 結合 Codex 的「取得焦點」與 Gemini 的名詞「紀錄」。

Input:
```text
搜索框聚焦后会显示最近查询记录。
```

Codex:
```text
搜尋框取得焦點後會顯示最近查詢記錄。
```

Gemini:
```text
搜尋框聚焦後會顯示最近查詢紀錄。
```

Recommended:
```text
搜尋框取得焦點後會顯示最近查詢紀錄。
```

zhtw current:
```text
搜尋框聚焦後會顯示最近查詢記錄。
```

### blind-ui-0124

- Domain: ui
- Risk: baseline_guard
- Recommendation: codex
- zhtw current status: in_recommended_acceptable
- Reason: Codex 較完整正式，且保留 CloudDesk。

Input:
```text
请不要翻译产品名 CloudDesk。
```

Codex:
```text
請不要翻譯產品名稱 CloudDesk。
```

Gemini:
```text
請不要翻譯產品名 CloudDesk。
```

Recommended:
```text
請不要翻譯產品名稱 CloudDesk。
```

zhtw current:
```text
請不要翻譯產品名 CloudDesk。
```

### blind-llm-0080

- Domain: llm
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: matches_recommended
- Reason: 台灣文件中「清單」比「列表」更自然。

Input:
```text
模型输出需要附上引用来源列表。
```

Codex:
```text
模型輸出需要附上引用來源清單。
```

Gemini:
```text
模型輸出需要附上引用來源列表。
```

Recommended:
```text
模型輸出需要附上引用來源清單。
```

zhtw current:
```text
模型輸出需要附上引用來源清單。
```

### blind-llm-0084

- Domain: llm
- Risk: candidate_gap
- Recommendation: gemini
- zhtw current status: in_recommended_acceptable
- Reason: LLM 評測語境常直接稱「腳本」。

Input:
```text
这个评测脚本会比较模型回答和参考答案。
```

Codex:
```text
這個評測指令碼會比較模型回答和參考答案。
```

Gemini:
```text
這個評測腳本會比較模型回答和參考答案。
```

Recommended:
```text
這個評測腳本會比較模型回答和參考答案。
```

zhtw current:
```text
這個評測指令碼會比較模型回答和參考答案。
```

### blind-llm-0085

- Domain: llm
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: needs_followup_if_confirmed
- Reason: token/history 處理語境用「截斷」更精確。

Input:
```text
对话历史过长时，系统会裁剪较旧消息。
```

Codex:
```text
對話歷史過長時，系統會截斷較舊訊息。
```

Gemini:
```text
對話歷史過長時，系統會裁剪較舊訊息。
```

Recommended:
```text
對話歷史過長時，系統會截斷較舊訊息。
```

zhtw current:
```text
對話歷史過長時，系統會裁剪較舊消息。
```

### blind-llm-0087

- Domain: llm
- Risk: baseline_guard
- Recommendation: gemini
- zhtw current status: matches_recommended
- Reason: 若採「佔位符」術語，繁體字形應為「佔」。

Input:
```text
请保留变量 {{user_locale}} 的占位符。
```

Codex:
```text
請保留變數 {{user_locale}} 的占位符。
```

Gemini:
```text
請保留變數 {{user_locale}} 的佔位符。
```

Recommended:
```text
請保留變數 {{user_locale}} 的佔位符。
```

zhtw current:
```text
請保留變數 {{user_locale}} 的佔位符。
```

### blind-social-0080

- Domain: social
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: in_recommended_acceptable
- Reason: 「傳送簡訊」較自然；Gemini malformed acceptable 已從 normalized report 移除。

Input:
```text
这家店的排队系统会发送简讯提醒。
```

Codex:
```text
這家店的排隊系統會傳送簡訊提醒。
```

Gemini:
```text
這家店的排隊系統會發送簡訊提醒。
```

Recommended:
```text
這家店的排隊系統會傳送簡訊提醒。
```

zhtw current:
```text
這家店的排隊系統會發送簡訊提醒。
```

### blind-high-risk-0053

- Domain: high_risk
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: needs_followup_if_confirmed
- Reason: 金融語境「付款指令」較精確。

Input:
```text
银行会在交易异常时暂停付款指令。
```

Codex:
```text
銀行會在交易異常時暫停付款指令。
```

Gemini:
```text
銀行會在交易異常時暫停付款指示。
```

Recommended:
```text
銀行會在交易異常時暫停付款指令。
```

zhtw current:
```text
銀行會在交易例外時暫停付款指令。
```

### blind-high-risk-0057

- Domain: high_risk
- Risk: baseline_guard
- Recommendation: codex
- zhtw current status: matches_recommended
- Reason: input 是病例編號，Codex 較忠實；病歷編號可由 maintainer 視語境確認。

Input:
```text
请保留病例编号 TW-MED-7788。
```

Codex:
```text
請保留病例編號 TW-MED-7788。
```

Gemini:
```text
請保留病歷編號 TW-MED-7788。
```

Recommended:
```text
請保留病例編號 TW-MED-7788。
```

zhtw current:
```text
請保留病例編號 TW-MED-7788。
```

## Exact But Policy Review

### blind-it-0138

- Domain: it
- Risk: candidate_gap
- Reason: Codex confidence medium
- zhtw current status: needs_followup_if_confirmed

Recommended:
```text
請在 API 回應中加入請求識別碼，方便排查日誌。
```

### blind-it-0161

- Domain: it
- Risk: over_conversion_guard
- Reason: over-conversion guard, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
台灣 CDN 節點名稱已經是繁體，不要改寫。
```

### blind-it-0162

- Domain: it
- Risk: over_conversion_guard
- Reason: over-conversion guard, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
這段繁體設定說明應原樣保留在輸出中。
```

### blind-ui-0115

- Domain: ui
- Risk: candidate_gap
- Reason: Codex confidence medium
- zhtw current status: matches_recommended

Recommended:
```text
彈出視窗底部需要固定主要操作按鈕。
```

### blind-ui-0120

- Domain: ui
- Risk: candidate_gap
- Reason: Codex confidence medium
- zhtw current status: matches_recommended

Recommended:
```text
表單欄位驗證失敗時會顯示輔助說明。
```

### blind-ui-0121

- Domain: ui
- Risk: candidate_gap
- Reason: Codex confidence medium
- zhtw current status: in_recommended_acceptable

Recommended:
```text
分頁清單會在捲動到底部時載入更多內容。
```

### blind-ui-0126

- Domain: ui
- Risk: over_conversion_guard
- Reason: over-conversion guard, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
這個繁體介面文案不需要再次轉換。
```

### blind-ui-0127

- Domain: ui
- Risk: over_conversion_guard
- Reason: over-conversion guard, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
使用者名稱欄位已是繁體，請保持原樣。
```

### blind-llm-0078

- Domain: llm
- Risk: candidate_gap
- Reason: Codex confidence medium
- zhtw current status: matches_recommended

Recommended:
```text
這個代理會根據系統提示選擇工具。
```

### blind-llm-0088

- Domain: llm
- Risk: over_conversion_guard
- Reason: over-conversion guard, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
以下繁體回答已經審核，不要自動改寫。
```

### blind-llm-0089

- Domain: llm
- Risk: over_conversion_guard
- Reason: over-conversion guard, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
臺北示例句在提示中應保持原樣。
```

### blind-llm-0090

- Domain: llm
- Risk: over_conversion_guard
- Reason: over-conversion guard, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
這段繁體系統訊息只需要原樣輸出。
```

### blind-llm-0091

- Domain: llm
- Risk: over_conversion_guard
- Reason: over-conversion guard, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
模型回覆中的「品質」用字不應被改動。
```

### blind-llm-0092

- Domain: llm
- Risk: over_conversion_guard
- Reason: over-conversion guard, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
請保留既有繁體摘要，不要重新轉換。
```

### blind-formal-0081

- Domain: formal
- Risk: candidate_gap
- Reason: Codex confidence medium
- zhtw current status: matches_recommended

Recommended:
```text
本辦法自公布日起三十日後施行。
```

### blind-formal-0083

- Domain: formal
- Risk: candidate_gap
- Reason: Codex confidence medium
- zhtw current status: matches_recommended

Recommended:
```text
採購合約應載明驗收標準和付款條件。
```

### blind-formal-0089

- Domain: formal
- Risk: over_conversion_guard
- Reason: over-conversion guard, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
本繁體公告內容已定稿，請勿再次轉換。
```

### blind-formal-0090

- Domain: formal
- Risk: over_conversion_guard
- Reason: over-conversion guard, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
臺灣主管機關名稱已是正式繁體用語。
```

### blind-formal-0091

- Domain: formal
- Risk: over_conversion_guard
- Reason: over-conversion guard, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
以下繁體條款應保持原文不變。
```

### blind-formal-0092

- Domain: formal
- Risk: over_conversion_guard
- Reason: over-conversion guard, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
董事會紀錄中的繁體職稱不得改寫。
```

### blind-formal-0093

- Domain: formal
- Risk: over_conversion_guard
- Reason: over-conversion guard, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
契約本文已完成繁體校對，請保留原樣。
```

### blind-social-0086

- Domain: social
- Risk: over_conversion_guard
- Reason: over-conversion guard, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
這句繁體留言已經很好，不需要修改。
```

### blind-social-0087

- Domain: social
- Risk: over_conversion_guard
- Reason: over-conversion guard, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
臺中朋友傳來的繁體訊息請保持原樣。
```

### blind-social-0088

- Domain: social
- Risk: over_conversion_guard
- Reason: over-conversion guard, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
這段繁體貼文不要再轉成別的用字。
```

### blind-social-0089

- Domain: social
- Risk: over_conversion_guard
- Reason: over-conversion guard, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
我今天想保留「品質」這個寫法。
```

### blind-social-0090

- Domain: social
- Risk: over_conversion_guard
- Reason: over-conversion guard, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
請不要改動這則繁體社群公告。
```

### blind-social-0091

- Domain: social
- Risk: over_conversion_guard
- Reason: over-conversion guard, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
晚餐訂位確認訊息已是繁體，請保持原樣。
```

### blind-social-0092

- Domain: social
- Risk: over_conversion_guard
- Reason: over-conversion guard, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
臨時改地點的繁體通知不要再改寫。
```

### blind-social-0093

- Domain: social
- Risk: over_conversion_guard
- Reason: over-conversion guard, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
活動報名連結旁的繁體說明請保留。
```

### blind-high-risk-0051

- Domain: high_risk
- Risk: candidate_gap
- Reason: high-risk domain, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
醫師會根據檢查結果調整用藥劑量。
```

### blind-high-risk-0052

- Domain: high_risk
- Risk: candidate_gap
- Reason: high-risk domain, Codex confidence medium, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
保險契約應明確說明等待期間。
```

### blind-high-risk-0054

- Domain: high_risk
- Risk: candidate_gap
- Reason: high-risk domain, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
投資人應確認風險揭露文件內容。
```

### blind-high-risk-0055

- Domain: high_risk
- Risk: candidate_gap
- Reason: high-risk domain, Codex confidence medium, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
法院判決確定後，執行程序才會開始。
```

### blind-high-risk-0056

- Domain: high_risk
- Risk: baseline_guard
- Reason: high-risk domain, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
藥品名稱 Panadol 不應被翻譯或改寫。
```

### blind-high-risk-0058

- Domain: high_risk
- Risk: over_conversion_guard
- Reason: over-conversion guard, high-risk domain, Gemini review-needed variant
- zhtw current status: needs_followup_if_confirmed

Recommended:
```text
本繁體醫療聲明已經核准，請勿改寫。
```

### blind-high-risk-0059

- Domain: high_risk
- Risk: over_conversion_guard
- Reason: over-conversion guard, high-risk domain, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
金融契約中的繁體條款應維持原樣。
```

### blind-high-risk-0060

- Domain: high_risk
- Risk: over_conversion_guard
- Reason: over-conversion guard, high-risk domain, Gemini review-needed variant
- zhtw current status: matches_recommended

Recommended:
```text
法院公告的繁體案號不得被轉換。
```

## No Immediate Question

- `blind-it-0140`
- `blind-it-0144`
- `blind-it-0148`
- `blind-it-0158`
- `blind-it-0159`
- `blind-it-0160`
- `blind-ui-0109`
- `blind-ui-0110`
- `blind-ui-0112`
- `blind-ui-0113`
- `blind-ui-0114`
- `blind-ui-0116`
- `blind-ui-0119`
- `blind-ui-0122`
- `blind-ui-0123`
- `blind-ui-0125`
- `blind-llm-0079`
- `blind-llm-0081`
- `blind-llm-0082`
- `blind-llm-0083`
- `blind-llm-0086`
- `blind-formal-0079`
- `blind-formal-0080`
- `blind-formal-0082`
- `blind-formal-0084`
- `blind-formal-0085`
- `blind-formal-0086`
- `blind-formal-0087`
- `blind-formal-0088`
- `blind-social-0079`
- `blind-social-0081`
- `blind-social-0082`
- `blind-social-0083`
- `blind-social-0084`
- `blind-social-0085`
