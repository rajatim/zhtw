<!-- zhtw:disable -->
# Holdout Codex/Gemini Diff Review - blind-v1 batch7 100 cases

Generated: 2026-07-10

This report is advisory only. It compares Codex and Gemini recommendations and prepares the maintainer queue; it is not ground truth.

## Summary

- total_cases: 100
- exact_matches: 72
- differences: 28
- exact_but_policy_review: 37
- no_immediate_question: 35
- maintainer_queue_total: 65
- difference_recommendations: {"codex": 19, "gemini": 6, "third": 3}
- zhtw_current_status_for_differences: {"in_recommended_acceptable": 5, "matches_recommended": 8, "needs_followup_if_confirmed": 15}
- promotion_allowed: False

## Differences

### blind-it-0139：recommend `codex`

- Domain: it
- Risk: candidate_gap
- Input: 服务网格会根据路由规则转发流量。
- zhtw current: 服務網格會根據路由規則轉發流量。
- Codex expected: 服務網格會根據路由規則轉送流量。
- Gemini expected: 服務網格會根據路由規則轉發流量。
- Recommended expected: 服務網格會根據路由規則轉送流量。
- Recommended acceptable: 服務網格會根據路由規則轉發流量。
- zhtw status: in_recommended_acceptable
- Rationale: 「轉送流量」較符合網路流量 routing 語境；Gemini 的「轉發」可作 variant。

### blind-it-0141：recommend `codex`

- Domain: it
- Risk: candidate_gap
- Input: 批处理任务会把失败记录写入重试队列。
- zhtw current: 批次處理任務會把失敗記錄寫入重試佇列。
- Codex expected: 批次處理任務會把失敗記錄寫入重試佇列。
- Gemini expected: 批次處理任務會將失敗紀錄寫入重試佇列。
- Recommended expected: 批次處理任務會把失敗記錄寫入重試佇列。
- Recommended acceptable: 批次處理任務會將失敗紀錄寫入重試佇列。
- zhtw status: matches_recommended
- Rationale: Codex 較保留原句語氣；「記錄/紀錄」皆常見。

### blind-it-0142：recommend `gemini`

- Domain: it
- Risk: candidate_gap
- Input: 请确认配置映射已经同步到所有命名空间。
- zhtw current: 請確認配置對映已經同步到所有命名空間。
- Codex expected: 請確認設定映射已經同步到所有命名空間。
- Gemini expected: 請確認設定對應已經同步到所有命名空間。
- Recommended expected: 請確認設定對應已經同步到所有命名空間。
- Recommended acceptable: 請確認設定映射已經同步到所有命名空間。, 請確認 ConfigMap 已經同步到所有命名空間。
- zhtw status: needs_followup_if_confirmed
- Rationale: Gemini 的「設定對應」比直譯「設定映射」自然；若指 Kubernetes 專名，ConfigMap 可作 acceptable。

### blind-it-0143：recommend `codex`

- Domain: it
- Risk: candidate_gap
- Input: 客户端 SDK 会自动刷新过期的访问令牌。
- zhtw current: 用戶端 SDK 會自動重新整理過期的存取權杖。
- Codex expected: 用戶端 SDK 會自動重新整理過期的存取權杖。
- Gemini expected: 用戶端 SDK 會自動更新過期的存取權杖。
- Recommended expected: 用戶端 SDK 會自動重新整理過期的存取權杖。
- Recommended acceptable: 用戶端 SDK 會自動更新過期的存取權杖。, 客戶端 SDK 會自動重新整理過期的存取權杖。
- zhtw status: matches_recommended
- Rationale: token refresh 在技術語境用「重新整理」較貼近 refresh。

### blind-it-0145：recommend `codex`

- Domain: it
- Risk: candidate_gap
- Input: 消息订阅者需要手动确认每条事件。
- zhtw current: 消息訂閱者需要手動確認每條事件。
- Codex expected: 訊息訂閱者需要手動確認每個事件。
- Gemini expected: 訊息訂閱者需要手動確認每條事件。
- Recommended expected: 訊息訂閱者需要手動確認每個事件。
- Recommended acceptable: 訊息訂閱者需要手動確認每條事件。, 訊息訂閱者需要手動確認每一則事件。
- zhtw status: needs_followup_if_confirmed
- Rationale: 「每個事件」比「每條事件」更自然。

### blind-it-0146：recommend `codex`

- Domain: it
- Risk: candidate_gap
- Input: 部署脚本会先检查目标环境的依赖版本。
- zhtw current: 部署指令碼會先檢查目標環境的相依性版本。
- Codex expected: 部署指令碼會先檢查目標環境的相依套件版本。
- Gemini expected: 部署腳本會先檢查目標環境的相依性版本。
- Recommended expected: 部署指令碼會先檢查目標環境的相依套件版本。
- Recommended acceptable: 部署腳本會先檢查目標環境的依賴版本。
- zhtw status: needs_followup_if_confirmed
- Rationale: Gemini 的「相依性版本」不夠精確；Codex 的「相依套件版本」較適合開發文件。

### blind-it-0147：recommend `codex`

- Domain: it
- Risk: candidate_gap
- Input: 日志聚合服务会按追踪编号关联请求。
- zhtw current: 日誌聚合服務會按追蹤編號關聯請求。
- Codex expected: 日誌彙整服務會依追蹤編號關聯請求。
- Gemini expected: 日誌聚合服務會依追蹤編號關聯請求。
- Recommended expected: 日誌彙整服務會依追蹤編號關聯請求。
- Recommended acceptable: 日誌聚合服務會依追蹤編號關聯請求。
- zhtw status: needs_followup_if_confirmed
- Rationale: 台灣技術文件常用「彙整」；「聚合」可作較技術化 variant。

### blind-it-0149：recommend `codex`

- Domain: it
- Risk: candidate_gap
- Input: 请把连接超时设置写入环境变量。
- zhtw current: 請把連線逾時設定寫入環境變數。
- Codex expected: 請把連線逾時設定寫入環境變數。
- Gemini expected: 請將連線逾時設定寫入環境變數。
- Recommended expected: 請把連線逾時設定寫入環境變數。
- Recommended acceptable: 請將連線逾時設定寫入環境變數。
- zhtw status: matches_recommended
- Rationale: Codex 較保留原句「把」語氣，Gemini variant 也可接受。

### blind-it-0150：recommend `codex`

- Domain: it
- Risk: candidate_gap
- Input: 这个适配器会把字段名称转换成蛇形命名。
- zhtw current: 這個變壓器會把欄位名稱轉換成蛇形命名。
- Codex expected: 這個轉接器會把欄位名稱轉換成蛇形命名。
- Gemini expected: 這個轉接器會將欄位名稱轉換成蛇形命名。
- Recommended expected: 這個轉接器會把欄位名稱轉換成蛇形命名。
- Recommended acceptable: 這個轉接器會將欄位名稱轉換成蛇形命名。, 這個轉接器會把欄位名稱轉換成蛇形命名法。
- zhtw status: needs_followup_if_confirmed
- Rationale: Codex 較保留原句語氣；Gemini 的「將」可作 variant。

### blind-it-0151：recommend `third`

- Domain: it
- Risk: candidate_gap
- Input: 构建系统会缓存依赖包以缩短流水线时间。
- zhtw current: 建置系統會快取相依性包以縮短流水線時間。
- Codex expected: 建置系統會快取相依套件，以縮短流水線時間。
- Gemini expected: 建置系統會快取相依套件以縮短管線時間。
- Recommended expected: 建置系統會快取相依套件，以縮短管線時間。
- Recommended acceptable: 建置系統會快取相依套件，以縮短流水線時間。, 建置系統會快取依賴套件，以縮短管線時間。
- zhtw status: needs_followup_if_confirmed
- Rationale: 結合 Codex 的標點與 Gemini 的「管線」作為 CI/CD pipeline primary。

### blind-it-0152：recommend `codex`

- Domain: it
- Risk: candidate_gap
- Input: 故障转移完成后，监控系统会发送恢复通知。
- zhtw current: 故障轉移完成後，監控系統會發送恢復通知。
- Codex expected: 容錯移轉完成後，監控系統會傳送復原通知。
- Gemini expected: 容錯移轉完成後，監控系統會發送恢復通知。
- Recommended expected: 容錯移轉完成後，監控系統會傳送復原通知。
- Recommended acceptable: 容錯移轉完成後，監控系統會發送恢復通知。
- zhtw status: needs_followup_if_confirmed
- Rationale: 「容錯移轉/復原」較符合台灣技術文件語氣。

### blind-it-0153：recommend `third`

- Domain: it
- Risk: candidate_gap
- Input: 容器镜像扫描会阻止含高危漏洞的版本发布。
- zhtw current: 容器映像檔掃描會阻止含高危漏洞的版本發布。
- Codex expected: 容器映像檔掃描會阻止含高風險弱點的版本發布。
- Gemini expected: 容器映像檔掃描會阻止含有高風險漏洞的版本發布。
- Recommended expected: 容器映像檔掃描會阻止含高風險漏洞的版本發布。
- Recommended acceptable: 容器映像檔掃描會阻止含高風險弱點的版本發布。, 容器映像檔掃描會阻止含有高風險漏洞的版本發布。
- zhtw status: needs_followup_if_confirmed
- Rationale: 「漏洞」較貼近 input 的漏洞；保留 Codex/Gemini 共同的高風險與映像檔用法。

### blind-it-0154：recommend `gemini`

- Domain: it
- Risk: candidate_gap
- Input: 接口网关会限制每个租户的请求速率。
- zhtw current: 介面閘道會限制每個租戶的請求速率。
- Codex expected: 介面閘道會限制每個租用戶的請求速率。
- Gemini expected: 介面閘道會限制每個租戶的請求速率。
- Recommended expected: 介面閘道會限制每個租戶的請求速率。
- Recommended acceptable: 介面閘道會限制每個租用戶的請求速率。, API 閘道會限制每個租戶的請求速率。
- zhtw status: matches_recommended
- Rationale: 「租戶」較精簡自然；API 閘道可作 technical variant。

### blind-it-0155：recommend `codex`

- Domain: it
- Risk: candidate_gap
- Input: 任务调度器会跳过已经停用的实例。
- zhtw current: 任務調度器會跳過已經停用的實例。
- Codex expected: 工作排程器會跳過已經停用的執行個體。
- Gemini expected: 任務排程器會跳過已經停用的執行個體。
- Recommended expected: 工作排程器會跳過已經停用的執行個體。
- Recommended acceptable: 任務排程器會跳過已經停用的執行個體。, 任務排程器會跳過已經停用的實例。
- zhtw status: needs_followup_if_confirmed
- Rationale: Codex 的「工作排程器」較符合 scheduler 在台灣軟體語境的常見說法。

### blind-it-0156：recommend `codex`

- Domain: it
- Risk: candidate_gap
- Input: 请在迁移前导出当前表结构。
- zhtw current: 請在遷移前匯出當前表結構。
- Codex expected: 請在移轉前匯出目前資料表結構。
- Gemini expected: 請在遷移前匯出目前的資料表結構。
- Recommended expected: 請在移轉前匯出目前資料表結構。
- Recommended acceptable: 請在遷移前匯出目前資料表結構。, 請在移轉前匯出目前的資料表結構。
- zhtw status: needs_followup_if_confirmed
- Rationale: 「移轉」較符合台灣資料庫 migration 文件語境。

### blind-it-0157：recommend `gemini`

- Domain: it
- Risk: candidate_gap
- Input: 这个命令会列出所有可用的扩展模块。
- zhtw current: 這個命令會列出所有可用的擴充功能模組。
- Codex expected: 這個命令會列出所有可用的擴充模組。
- Gemini expected: 這個指令會列出所有可用的擴充模組。
- Recommended expected: 這個指令會列出所有可用的擴充模組。
- Recommended acceptable: 這個命令會列出所有可用的擴充模組。
- zhtw status: needs_followup_if_confirmed
- Rationale: CLI 語境用「指令」較自然。

### blind-ui-0108：recommend `gemini`

- Domain: ui
- Risk: candidate_gap
- Input: 筛选器面板可以按状态折叠。
- zhtw current: 篩選器面板可以按狀態摺疊。
- Codex expected: 篩選器面板可以依狀態摺疊。
- Gemini expected: 篩選器面板可以依狀態收合。
- Recommended expected: 篩選器面板可以依狀態收合。
- Recommended acceptable: 篩選器面板可以依狀態摺疊。, 篩選器面板可以按狀態收合。
- zhtw status: needs_followup_if_confirmed
- Rationale: UI 狀態常用「收合」描述 collapse。

### blind-ui-0111：recommend `codex`

- Domain: ui
- Risk: candidate_gap
- Input: 上传进度条需要显示剩余时间。
- zhtw current: 上傳進度列需要顯示剩餘時間。
- Codex expected: 上傳進度列需要顯示剩餘時間。
- Gemini expected: 上傳進度條需要顯示剩餘時間。
- Recommended expected: 上傳進度列需要顯示剩餘時間。
- Recommended acceptable: 上傳進度條需要顯示剩餘時間。
- zhtw status: matches_recommended
- Rationale: 台灣 UI 文件常用「進度列」。

### blind-ui-0117：recommend `codex`

- Domain: ui
- Risk: candidate_gap
- Input: 多选菜单会显示已选择项目数量。
- zhtw current: 多選選單會顯示已選擇項目數量。
- Codex expected: 多選選單會顯示已選取項目數量。
- Gemini expected: 複選選單會顯示已選擇項目數量。
- Recommended expected: 多選選單會顯示已選取項目數量。
- Recommended acceptable: 多選選單會顯示已選擇項目數量。
- zhtw status: in_recommended_acceptable
- Rationale: 「多選選單/已選取」較符合 UI 文案。

### blind-ui-0118：recommend `third`

- Domain: ui
- Risk: candidate_gap
- Input: 搜索框聚焦后会显示最近查询记录。
- zhtw current: 搜尋框聚焦後會顯示最近查詢記錄。
- Codex expected: 搜尋框取得焦點後會顯示最近查詢記錄。
- Gemini expected: 搜尋框聚焦後會顯示最近查詢紀錄。
- Recommended expected: 搜尋框取得焦點後會顯示最近查詢紀錄。
- Recommended acceptable: 搜尋框取得焦點後會顯示最近查詢記錄。, 搜尋框聚焦後會顯示最近查詢紀錄。
- zhtw status: needs_followup_if_confirmed
- Rationale: 結合 Codex 的「取得焦點」與 Gemini 的名詞「紀錄」。

### blind-ui-0124：recommend `codex`

- Domain: ui
- Risk: baseline_guard
- Input: 请不要翻译产品名 CloudDesk。
- zhtw current: 請不要翻譯產品名 CloudDesk。
- Codex expected: 請不要翻譯產品名稱 CloudDesk。
- Gemini expected: 請不要翻譯產品名 CloudDesk。
- Recommended expected: 請不要翻譯產品名稱 CloudDesk。
- Recommended acceptable: 請不要翻譯產品名 CloudDesk。, 請勿翻譯產品名稱 CloudDesk。
- zhtw status: in_recommended_acceptable
- Rationale: Codex 較完整正式，且保留 CloudDesk。

### blind-llm-0080：recommend `codex`

- Domain: llm
- Risk: candidate_gap
- Input: 模型输出需要附上引用来源列表。
- zhtw current: 模型輸出需要附上引用來源清單。
- Codex expected: 模型輸出需要附上引用來源清單。
- Gemini expected: 模型輸出需要附上引用來源列表。
- Recommended expected: 模型輸出需要附上引用來源清單。
- Recommended acceptable: 模型輸出需要附上引用來源列表。
- zhtw status: matches_recommended
- Rationale: 台灣文件中「清單」比「列表」更自然。

### blind-llm-0084：recommend `gemini`

- Domain: llm
- Risk: candidate_gap
- Input: 这个评测脚本会比较模型回答和参考答案。
- zhtw current: 這個評測指令碼會比較模型回答和參考答案。
- Codex expected: 這個評測指令碼會比較模型回答和參考答案。
- Gemini expected: 這個評測腳本會比較模型回答和參考答案。
- Recommended expected: 這個評測腳本會比較模型回答和參考答案。
- Recommended acceptable: 這個評測指令碼會比較模型回答和參考答案。
- zhtw status: in_recommended_acceptable
- Rationale: LLM 評測語境常直接稱「腳本」。

### blind-llm-0085：recommend `codex`

- Domain: llm
- Risk: candidate_gap
- Input: 对话历史过长时，系统会裁剪较旧消息。
- zhtw current: 對話歷史過長時，系統會裁剪較舊消息。
- Codex expected: 對話歷史過長時，系統會截斷較舊訊息。
- Gemini expected: 對話歷史過長時，系統會裁剪較舊訊息。
- Recommended expected: 對話歷史過長時，系統會截斷較舊訊息。
- Recommended acceptable: 對話歷史過長時，系統會裁剪較舊訊息。
- zhtw status: needs_followup_if_confirmed
- Rationale: token/history 處理語境用「截斷」更精確。

### blind-llm-0087：recommend `gemini`

- Domain: llm
- Risk: baseline_guard
- Input: 请保留变量 {{user_locale}} 的占位符。
- zhtw current: 請保留變數 {{user_locale}} 的佔位符。
- Codex expected: 請保留變數 {{user_locale}} 的占位符。
- Gemini expected: 請保留變數 {{user_locale}} 的佔位符。
- Recommended expected: 請保留變數 {{user_locale}} 的佔位符。
- Recommended acceptable: 請保留變數 {{user_locale}} 的預留位置。, 請保留變數 {{user_locale}} 的占位符。
- zhtw status: matches_recommended
- Rationale: 若採「佔位符」術語，繁體字形應為「佔」。

### blind-social-0080：recommend `codex`

- Domain: social
- Risk: candidate_gap
- Input: 这家店的排队系统会发送简讯提醒。
- zhtw current: 這家店的排隊系統會發送簡訊提醒。
- Codex expected: 這家店的排隊系統會傳送簡訊提醒。
- Gemini expected: 這家店的排隊系統會發送簡訊提醒。
- Recommended expected: 這家店的排隊系統會傳送簡訊提醒。
- Recommended acceptable: 這家店的排隊系統會發送簡訊提醒。, 這間店的排隊系統會發送簡訊提醒。
- zhtw status: in_recommended_acceptable
- Rationale: 「傳送簡訊」較自然；Gemini malformed acceptable 已從 normalized report 移除。

### blind-high-risk-0053：recommend `codex`

- Domain: high_risk
- Risk: candidate_gap
- Input: 银行会在交易异常时暂停付款指令。
- zhtw current: 銀行會在交易例外時暫停付款指令。
- Codex expected: 銀行會在交易異常時暫停付款指令。
- Gemini expected: 銀行會在交易異常時暫停付款指示。
- Recommended expected: 銀行會在交易異常時暫停付款指令。
- Recommended acceptable: 銀行會在交易異常時暫停付款指示。
- zhtw status: needs_followup_if_confirmed
- Rationale: 金融語境「付款指令」較精確。

### blind-high-risk-0057：recommend `codex`

- Domain: high_risk
- Risk: baseline_guard
- Input: 请保留病例编号 TW-MED-7788。
- zhtw current: 請保留病例編號 TW-MED-7788。
- Codex expected: 請保留病例編號 TW-MED-7788。
- Gemini expected: 請保留病歷編號 TW-MED-7788。
- Recommended expected: 請保留病例編號 TW-MED-7788。
- Recommended acceptable: 請保留病歷編號 TW-MED-7788。
- zhtw status: matches_recommended
- Rationale: input 是病例編號，Codex 較忠實；病歷編號可由 maintainer 視語境確認。

## Exact But Policy Review

### blind-it-0138

- Domain: it
- Risk: candidate_gap
- Policy reason: Codex confidence medium
- Recommended expected: 請在 API 回應中加入請求識別碼，方便排查日誌。
- zhtw status: needs_followup_if_confirmed

### blind-it-0161

- Domain: it
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, Gemini review-needed variant
- Recommended expected: 台灣 CDN 節點名稱已經是繁體，不要改寫。
- zhtw status: matches_recommended

### blind-it-0162

- Domain: it
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, Gemini review-needed variant
- Recommended expected: 這段繁體設定說明應原樣保留在輸出中。
- zhtw status: matches_recommended

### blind-ui-0115

- Domain: ui
- Risk: candidate_gap
- Policy reason: Codex confidence medium
- Recommended expected: 彈出視窗底部需要固定主要操作按鈕。
- zhtw status: matches_recommended

### blind-ui-0120

- Domain: ui
- Risk: candidate_gap
- Policy reason: Codex confidence medium
- Recommended expected: 表單欄位驗證失敗時會顯示輔助說明。
- zhtw status: matches_recommended

### blind-ui-0121

- Domain: ui
- Risk: candidate_gap
- Policy reason: Codex confidence medium
- Recommended expected: 分頁清單會在捲動到底部時載入更多內容。
- zhtw status: in_recommended_acceptable

### blind-ui-0126

- Domain: ui
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, Gemini review-needed variant
- Recommended expected: 這個繁體介面文案不需要再次轉換。
- zhtw status: matches_recommended

### blind-ui-0127

- Domain: ui
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, Gemini review-needed variant
- Recommended expected: 使用者名稱欄位已是繁體，請保持原樣。
- zhtw status: matches_recommended

### blind-llm-0078

- Domain: llm
- Risk: candidate_gap
- Policy reason: Codex confidence medium
- Recommended expected: 這個代理會根據系統提示選擇工具。
- zhtw status: matches_recommended

### blind-llm-0088

- Domain: llm
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, Gemini review-needed variant
- Recommended expected: 以下繁體回答已經審核，不要自動改寫。
- zhtw status: matches_recommended

### blind-llm-0089

- Domain: llm
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, Gemini review-needed variant
- Recommended expected: 臺北示例句在提示中應保持原樣。
- zhtw status: matches_recommended

### blind-llm-0090

- Domain: llm
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, Gemini review-needed variant
- Recommended expected: 這段繁體系統訊息只需要原樣輸出。
- zhtw status: matches_recommended

### blind-llm-0091

- Domain: llm
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, Gemini review-needed variant
- Recommended expected: 模型回覆中的「品質」用字不應被改動。
- zhtw status: matches_recommended

### blind-llm-0092

- Domain: llm
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, Gemini review-needed variant
- Recommended expected: 請保留既有繁體摘要，不要重新轉換。
- zhtw status: matches_recommended

### blind-formal-0081

- Domain: formal
- Risk: candidate_gap
- Policy reason: Codex confidence medium
- Recommended expected: 本辦法自公布日起三十日後施行。
- zhtw status: matches_recommended

### blind-formal-0083

- Domain: formal
- Risk: candidate_gap
- Policy reason: Codex confidence medium
- Recommended expected: 採購合約應載明驗收標準和付款條件。
- zhtw status: matches_recommended

### blind-formal-0089

- Domain: formal
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, Gemini review-needed variant
- Recommended expected: 本繁體公告內容已定稿，請勿再次轉換。
- zhtw status: matches_recommended

### blind-formal-0090

- Domain: formal
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, Gemini review-needed variant
- Recommended expected: 臺灣主管機關名稱已是正式繁體用語。
- zhtw status: matches_recommended

### blind-formal-0091

- Domain: formal
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, Gemini review-needed variant
- Recommended expected: 以下繁體條款應保持原文不變。
- zhtw status: matches_recommended

### blind-formal-0092

- Domain: formal
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, Gemini review-needed variant
- Recommended expected: 董事會紀錄中的繁體職稱不得改寫。
- zhtw status: matches_recommended

### blind-formal-0093

- Domain: formal
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, Gemini review-needed variant
- Recommended expected: 契約本文已完成繁體校對，請保留原樣。
- zhtw status: matches_recommended

### blind-social-0086

- Domain: social
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, Gemini review-needed variant
- Recommended expected: 這句繁體留言已經很好，不需要修改。
- zhtw status: matches_recommended

### blind-social-0087

- Domain: social
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, Gemini review-needed variant
- Recommended expected: 臺中朋友傳來的繁體訊息請保持原樣。
- zhtw status: matches_recommended

### blind-social-0088

- Domain: social
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, Gemini review-needed variant
- Recommended expected: 這段繁體貼文不要再轉成別的用字。
- zhtw status: matches_recommended

### blind-social-0089

- Domain: social
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, Gemini review-needed variant
- Recommended expected: 我今天想保留「品質」這個寫法。
- zhtw status: matches_recommended

### blind-social-0090

- Domain: social
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, Gemini review-needed variant
- Recommended expected: 請不要改動這則繁體社群公告。
- zhtw status: matches_recommended

### blind-social-0091

- Domain: social
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, Gemini review-needed variant
- Recommended expected: 晚餐訂位確認訊息已是繁體，請保持原樣。
- zhtw status: matches_recommended

### blind-social-0092

- Domain: social
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, Gemini review-needed variant
- Recommended expected: 臨時改地點的繁體通知不要再改寫。
- zhtw status: matches_recommended

### blind-social-0093

- Domain: social
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, Gemini review-needed variant
- Recommended expected: 活動報名連結旁的繁體說明請保留。
- zhtw status: matches_recommended

### blind-high-risk-0051

- Domain: high_risk
- Risk: candidate_gap
- Policy reason: high-risk domain, Gemini review-needed variant
- Recommended expected: 醫師會根據檢查結果調整用藥劑量。
- zhtw status: matches_recommended

### blind-high-risk-0052

- Domain: high_risk
- Risk: candidate_gap
- Policy reason: high-risk domain, Codex confidence medium, Gemini review-needed variant
- Recommended expected: 保險契約應明確說明等待期間。
- zhtw status: matches_recommended

### blind-high-risk-0054

- Domain: high_risk
- Risk: candidate_gap
- Policy reason: high-risk domain, Gemini review-needed variant
- Recommended expected: 投資人應確認風險揭露文件內容。
- zhtw status: matches_recommended

### blind-high-risk-0055

- Domain: high_risk
- Risk: candidate_gap
- Policy reason: high-risk domain, Codex confidence medium, Gemini review-needed variant
- Recommended expected: 法院判決確定後，執行程序才會開始。
- zhtw status: matches_recommended

### blind-high-risk-0056

- Domain: high_risk
- Risk: baseline_guard
- Policy reason: high-risk domain, Gemini review-needed variant
- Recommended expected: 藥品名稱 Panadol 不應被翻譯或改寫。
- zhtw status: matches_recommended

### blind-high-risk-0058

- Domain: high_risk
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, high-risk domain, Gemini review-needed variant
- Recommended expected: 本繁體醫療聲明已經核准，請勿改寫。
- zhtw status: needs_followup_if_confirmed

### blind-high-risk-0059

- Domain: high_risk
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, high-risk domain, Gemini review-needed variant
- Recommended expected: 金融契約中的繁體條款應維持原樣。
- zhtw status: matches_recommended

### blind-high-risk-0060

- Domain: high_risk
- Risk: over_conversion_guard
- Policy reason: over-conversion guard, high-risk domain, Gemini review-needed variant
- Recommended expected: 法院公告的繁體案號不得被轉換。
- zhtw status: matches_recommended

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
