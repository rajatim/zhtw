<!-- zhtw:disable -->
# Holdout Maintainer Confirmation - Batch12

- Review queue: 44
- Primary differences: 13
- Exact policy review: 31
- No immediate question: 56
- Private expected modified: false

## Primary Differences

### blind-formal-0156

- Input: 会议记录须载明出席人员及决议事项。
- Codex: 會議記錄須載明出席人員及決議事項。
- Gemini: 會議紀錄須載明出席人員及決議事項。
- Suggested: 會議紀錄須載明出席人員及決議事項。
- Suggested acceptable: 會議記錄須載明出席人員及決議事項。
- Reason: 正式文件中的 record 建議以「紀錄」為 primary，「記錄」可接受。

### blind-formal-0157

- Input: 承办单位应汇整各部门反馈意见。
- Codex: 承辦單位應彙整各部門回饋意見。
- Gemini: 承辦單位應彙整各部門的回饋意見。
- Suggested: 承辦單位應彙整各部門回饋意見。
- Suggested acceptable: 承辦單位應彙整各部門的回饋意見。, 承辦單位應彙整各部門的意見。
- Reason: 兩者語意相同；Codex 版本較貼近原句結構。

### blind-formal-0167

- Input: 该报道引用了公开会议的发言记录。
- Codex: 該報導引用了公開會議的發言記錄。
- Gemini: 該報導引用了公開會議的發言紀錄。
- Suggested: 該報導引用了公開會議的發言紀錄。
- Suggested acceptable: 該報導引用了公開會議的發言記錄。
- Reason: 發言內容作名詞時以「紀錄」較自然，「記錄」仍可接受。

### blind-high-risk-0116

- Input: 护理记录中的原始数值不得改写。
- Codex: 護理記錄中的原始數值不得改寫。
- Gemini: 護理紀錄中的原始數值不得改寫。
- Suggested: 護理紀錄中的原始數值不得改寫。
- Suggested acceptable: 護理記錄中的原始數值不得改寫。
- Reason: 醫療文書名詞建議使用「護理紀錄」，避免把 house style 當唯一答案。

### blind-it-0265

- Input: 部署流水线应在合并前执行静态检查。
- Codex: 部署管線應在合併前執行靜態檢查。
- Gemini: 部署流水線應在合併前執行靜態檢查。
- Suggested: 部署管線應在合併前執行靜態檢查。
- Suggested acceptable: 部署流水線應在合併前執行靜態檢查。
- Reason: 臺灣 CI/CD 語境較常用「部署管線」；「流水線」列 acceptable。

### blind-it-0267

- Input: 遥测代理会批量上传追踪数据。
- Codex: 遙測代理程式會批次上傳追蹤資料。
- Gemini: 遙測代理會批次上傳追蹤資料。
- Suggested: 遙測代理程式會批次上傳追蹤資料。
- Suggested acceptable: 遙測代理會批次上傳追蹤資料。, 遙測代理會批量上傳追蹤資料。, 遙測代理會批次上傳追蹤數據。
- Reason: 「代理程式」能明確表達 software agent；簡稱「代理」可接受。

### blind-it-0269

- Input: 消息代理应保存尚未确认的事件。
- Codex: 訊息代理程式應保存尚未確認的事件。
- Gemini: 訊息代理應儲存尚未確認的事件。
- Suggested: 訊息代理應儲存尚未確認的事件。
- Suggested acceptable: 訊息代理程式應保存尚未確認的事件。, 訊息代理應保存尚未確認的事件。
- Reason: 事件持久化語境使用「儲存」較精確；「保存」不算語意錯誤。

### blind-it-0275

- Input: 错误消息包含原始字段名 user_id。
- Codex: 錯誤訊息包含原始欄位名稱 user_id。
- Gemini: 錯誤訊息包含原始欄位名 user_id。
- Suggested: 錯誤訊息包含原始欄位名稱 user_id。
- Suggested acceptable: 錯誤訊息包含原始欄位名 user_id。
- Reason: 臺灣技術文件較常寫「欄位名稱」。

### blind-ui-0212

- Input: 批量操作完成后要更新选中项目数量。
- Codex: 批次操作完成後要更新選取項目數量。
- Gemini: 批次操作完成後要更新選中項目數量。
- Suggested: 批次操作完成後要更新選取項目數量。
- Suggested acceptable: 批次操作完成後要更新選中項目數量。, 批次操作完成後要更新已選項目數量。, 批次操作完成後要更新所選項目數量。, 大量操作完成後要更新選取項目數量。
- Reason: 臺灣 UI 用語採「選取項目」，不採「選中項目」。

### blind-ui-0221

- Input: 对话框关闭后焦点回到原按钮。
- Codex: 對話框關閉後焦點回到原按鈕。
- Gemini: 對話方塊關閉後焦點回到原按鈕。
- Suggested: 對話框關閉後焦點回到原按鈕。
- Suggested acceptable: 對話方塊關閉後焦點回到原按鈕。
- Reason: 「對話框」與「對話方塊」皆通行，原專案慣例採前者。

### blind-llm-0153

- Input: 代理执行工具前应检查参数是否完整。
- Codex: 代理執行工具前應檢查參數是否完整。
- Gemini: 代理在執行工具前應檢查參數是否完整。
- Suggested: 代理執行工具前應檢查參數是否完整。
- Suggested acceptable: 代理在執行工具前應檢查參數是否完整。
- Reason: 兩者語意完全相同；Codex 版本較精簡。

### blind-llm-0155

- Input: 模型输出被截断时应标记未完成状态。
- Codex: 模型輸出被截斷時應標記未完成狀態。
- Gemini: 模型輸出被截斷時應標記為未完成狀態。
- Suggested: 模型輸出被截斷時應標記為未完成狀態。
- Suggested acceptable: 模型輸出被截斷時應標記未完成狀態。
- Reason: 「標記為未完成狀態」語法較完整。

### blind-llm-0158

- Input: 工具名称 web.run 不得本地化。
- Codex: 工具名稱 web.run 不得本地化。
- Gemini: 工具名稱 web.run 不得在地化。
- Suggested: 工具名稱 web.run 不得在地化。
- Suggested acceptable: 工具名稱 web.run 不得本地化。
- Reason: 臺灣軟體語境建議使用「在地化」，「本地化」列 acceptable。

## Exact Policy Review

These cases have identical Codex/Gemini primary expected values but remain in the queue due to medium confidence, proposed variants, or high-risk domain policy.

- blind-formal-0172: 預算書中的金額均以新臺幣列示。
- blind-high-risk-0101: 病歷摘要不得包含與治療無關的個人資料。
- blind-high-risk-0102: 藥品開封後應依標籤註明的溫度保存。
- blind-high-risk-0103: 投保人應據實填寫健康告知事項。
- blind-high-risk-0104: 銀行應於扣款前揭露手續費計算方式。
- blind-high-risk-0105: 雇主不得扣留勞動者的身分證件。
- blind-high-risk-0106: 手術同意書應由醫師說明風險後簽署。
- blind-high-risk-0107: 契約解除不影響已經發生的損害賠償請求。
- blind-high-risk-0108: 信用報告更正申請應附上證明文件。
- blind-high-risk-0109: 發生職業災害時應立即通報主管機關。
- blind-high-risk-0110: 檢體運輸過程必須維持規定溫度。
- blind-high-risk-0111: 受託人處理個人資料不得逾越委託範圍。
- blind-high-risk-0112: 貸款提前清償違約金應記載於契約。
- blind-high-risk-0113: 醫師確認病人意識清楚後再詢問意願。
- blind-high-risk-0114: 法院命令停止執行原處分。
- blind-high-risk-0115: 保險給付不得重複計算同一項損失。
- blind-high-risk-0117: 匯款備註欄請保留案件編號 A-204。
- blind-high-risk-0118: 當事人聲明其意思表示未受強迫。
- blind-high-risk-0119: 診斷證明書已由醫院加蓋關防。
- blind-high-risk-0120: 新臺幣存款受到存款保險保障。
- blind-social-0154: 我把定位傳到群組，你到了再說。
- blind-social-0158: 捷運臨時停駛，我們改搭公車吧。
- blind-social-0170: 週末去臺中看展覽。
- blind-it-0263: 服務網格會記錄跨命名空間的請求延遲。
- blind-it-0264: 物件儲存的生命週期規則會自動刪除舊版本。
- blind-it-0270: 快取失效通知會透過發布訂閱通道傳播。
- blind-ui-0213: 空白狀態應提供建立第一個項目的入口。
- blind-ui-0215: 預留位置 {team_name} 不得改寫。
- blind-ui-0216: 分頁標籤中的 Beta 字樣維持原樣。
- blind-llm-0156: 評測腳本必須區分拒答與空白回答。
- blind-llm-0157: 系統提示更新後應重新執行安全測試。
