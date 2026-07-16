<!-- zhtw:disable -->
# Holdout Codex/Gemini Difference Review - Batch13

Generated: `2026-07-14`

## Summary

- Exact matches: 66
- Differences: 34
- Exact but policy review: 19
- No immediate question: 47
- Maintainer queue: 53
- Difference recommendations: {'codex': 29, 'gemini': 5}
- Ground truth: false
- Promotion allowed: false

## Differences

### blind-formal-0187

- Input: 委托研究成果应开放公众查阅。
- Codex: 委託研究成果應開放民眾查閱。
- Gemini: 委託研究成果應開放公眾查閱。
- Recommendation: gemini - 委託研究成果應開放公眾查閱。
- Reason: 「公眾」在正式文件中自然且更貼近原文；「民眾」可列合理變體。

### blind-high-risk-0121

- Input: 医师开具处方前应确认患者过敏史。
- Codex: 醫師開立處方前應確認病人過敏史。
- Gemini: 醫師開立處方前應確認患者過敏史。
- Recommendation: codex - 醫師開立處方前應確認病人過敏史。
- Reason: 臺灣醫療語境常用「開立處方」與「病人」；保留較直譯版本為變體。

### blind-high-risk-0122

- Input: 检验报告异常时应尽快通知主治医师。
- Codex: 檢驗報告異常時應儘快通知主治醫師。
- Gemini: 檢驗報告異常時應盡快通知主治醫師。
- Recommendation: codex - 檢驗報告異常時應儘快通知主治醫師。
- Reason: 「儘快」是當代臺灣常見寫法；「盡快」可接受。

### blind-high-risk-0125

- Input: 雇佣合同应明确约定工资支付日期。
- Codex: 僱傭契約應明確約定薪資支付日期。
- Gemini: 雇傭合約應明確約定工資支付日期。
- Recommendation: codex - 僱傭契約應明確約定薪資支付日期。
- Reason: 採臺灣勞動與法律語境常見的「僱傭契約、薪資」。

### blind-high-risk-0131

- Input: 手术记录应完整记载使用的医疗器材。
- Codex: 手術記錄應完整記載使用的醫療器材。
- Gemini: 手術紀錄應完整記載使用的醫療器材。
- Recommendation: gemini - 手術紀錄應完整記載使用的醫療器材。
- Reason: 名詞語境採「手術紀錄」；「記錄」較偏動作。

### blind-high-risk-0134

- Input: 劳资争议调解记录不得任意公开。
- Codex: 勞資爭議調解記錄不得任意公開。
- Gemini: 勞資爭議調解紀錄不得任意公開。
- Recommendation: gemini - 勞資爭議調解紀錄不得任意公開。
- Reason: 名詞語境採「調解紀錄」；「記錄」較偏動作。

### blind-high-risk-0135

- Input: 远程问诊平台应验证医师执业资格。
- Codex: 遠距問診平台應驗證醫師執業資格。
- Gemini: 遠端問診平台應驗證醫師執業資格。
- Recommendation: codex - 遠距問診平台應驗證醫師執業資格。
- Reason: 臺灣醫療服務常用「遠距問診」，比「遠端問診」自然。

### blind-it-0278

- Input: 部署脚本应在失败时返回非零退出码。
- Codex: 部署腳本應在失敗時回傳非零結束碼。
- Gemini: 部署腳本應在失敗時傳回非零的結束代碼。
- Recommendation: codex - 部署腳本應在失敗時回傳非零結束碼。
- Reason: 採臺灣開發文件常見的「回傳」與精簡的「結束碼」。

### blind-it-0279

- Input: 数据库迁移前必须建立可恢复的备份。
- Codex: 資料庫移轉前必須建立可還原的備份。
- Gemini: 資料庫遷移前必須建立可供還原的備份。
- Recommendation: codex - 資料庫移轉前必須建立可還原的備份。
- Reason: 「資料庫移轉、可還原備份」符合臺灣 IT 文件用語。

### blind-it-0282

- Input: 代码审查通过后才能合并到主分支。
- Codex: 程式碼審查通過後才能合併至主分支。
- Gemini: 程式碼審查通過後才能合併到主分支。
- Recommendation: gemini - 程式碼審查通過後才能合併到主分支。
- Reason: 「合併到主分支」在開發語境自然，與「合併至」語義相同。

### blind-it-0286

- Input: 软件包发布后不得覆盖相同版本号。
- Codex: 軟體套件發布後不得覆蓋相同版本號。
- Gemini: 軟體包發布後不得覆蓋相同版本號。
- Recommendation: codex - 軟體套件發布後不得覆蓋相同版本號。
- Reason: 臺灣 IT 用語採「軟體套件」，避免中國用語「軟體包」。

### blind-it-0287

- Input: 接口返回 429 时客户端应采用指数退避。
- Codex: API 回傳 429 時用戶端應採用指數退避。
- Gemini: 介面傳回 429 時，客戶端應採用指數退避。
- Recommendation: codex - API 回傳 429 時用戶端應採用指數退避。
- Reason: HTTP 429 語境採「API 回傳」與「用戶端」，比泛稱介面更精確。

### blind-it-0288

- Input: 容器健康检查不应依赖外部服务。
- Codex: 容器健康檢查不應依賴外部服務。
- Gemini: 容器健康狀況檢查不應依賴外部服務。
- Recommendation: codex - 容器健康檢查不應依賴外部服務。
- Reason: 「容器健康檢查」是既有技術術語，不需擴寫為健康狀況檢查。

### blind-it-0290

- Input: 测试替身只用于隔离外部依赖。
- Codex: 測試替身只用於隔離外部相依項目。
- Gemini: 測試替身僅用於隔離外部依賴。
- Recommendation: codex - 測試替身只用於隔離外部相依項目。
- Reason: 採臺灣 IT 用語「相依項目」，避免直接保留「依賴」。

### blind-it-0292

- Input: 远程仓库地址变更后须更新持续集成设置。
- Codex: 遠端儲存庫位址變更後須更新持續整合設定。
- Gemini: 遠端儲存庫位址變更後，須更新持續整合設定。
- Recommendation: codex - 遠端儲存庫位址變更後須更新持續整合設定。
- Reason: 只涉及標點差異，保留原句節奏，不新增逗號。

### blind-it-0293

- Input: 线程池大小应根据实际负载调整。
- Codex: 執行緒集區大小應根據實際負載調整。
- Gemini: 執行緒池大小應根據實際負載調整。
- Recommendation: codex - 執行緒集區大小應根據實際負載調整。
- Reason: thread pool 採臺灣技術文件常用的「執行緒集區」。

### blind-it-0294

- Input: 事件处理器必须支持重复投递。
- Codex: 事件處理常式必須支援重複投遞。
- Gemini: 事件處理器必須支援重複傳遞。
- Recommendation: codex - 事件處理常式必須支援重複投遞。
- Reason: event handler 採「事件處理常式」，delivery 保留「投遞」語意。

### blind-it-0297

- Input: 用户会话过期后应清除本地缓存。
- Codex: 使用者工作階段過期後應清除本機快取。
- Gemini: 使用者工作階段過期後，應清除本機快取。
- Recommendation: codex - 使用者工作階段過期後應清除本機快取。
- Reason: 只涉及標點差異，保留原句節奏，不新增逗號。

### blind-ui-0223

- Input: 搜索框没有结果时显示空白状态。
- Codex: 搜尋欄沒有結果時顯示空白狀態。
- Gemini: 搜尋框沒有結果時顯示空白狀態。
- Recommendation: codex - 搜尋欄沒有結果時顯示空白狀態。
- Reason: 採既有產品用語「搜尋欄」；「搜尋框」可列合理變體。

### blind-ui-0224

- Input: 点击筛选图标可展开条件面板。
- Codex: 點選篩選圖示可展開條件面板。
- Gemini: 點擊篩選圖示可展開條件面板。
- Recommendation: codex - 點選篩選圖示可展開條件面板。
- Reason: 臺灣 UI 指令常用「點選、圖示」。

### blind-ui-0226

- Input: 上传失败后保留已经选择的文件。
- Codex: 上傳失敗後保留已經選取的檔案。
- Gemini: 上傳失敗後保留已經選擇的檔案。
- Recommendation: codex - 上傳失敗後保留已經選取的檔案。
- Reason: 檔案選擇動作採 UI 常用語「選取」。

### blind-ui-0227

- Input: 表单字段错误时将焦点移到第一个问题。
- Codex: 表單欄位發生錯誤時，將焦點移到第一個錯誤欄位。
- Gemini: 表單欄位錯誤時將焦點移至第一個問題。
- Recommendation: codex - 表單欄位發生錯誤時，將焦點移到第一個錯誤欄位。
- Reason: 原文的「第一個問題」在表單語境指第一個錯誤欄位，建議明確化但需人工確認。

### blind-ui-0232

- Input: 进度条完成时应向辅助技术发送状态更新。
- Codex: 進度列完成時應向輔助技術傳送狀態更新。
- Gemini: 進度條完成時應向輔助技術傳送狀態更新。
- Recommendation: codex - 進度列完成時應向輔助技術傳送狀態更新。
- Reason: progress bar 採臺灣 UI 常用的「進度列」。

### blind-ui-0234

- Input: 下拉列表打开后高亮当前选项。
- Codex: 下拉式清單開啟後醒目顯示目前選項。
- Gemini: 下拉式選單開啟後高亮目前選項。
- Recommendation: codex - 下拉式清單開啟後醒目顯示目前選項。
- Reason: 避免中國用語「高亮」，採「醒目顯示」；「反白顯示」可列變體。

### blind-ui-0236

- Input: 关闭弹窗前提示尚未保存的更改。
- Codex: 關閉彈出視窗前提示尚未儲存的變更。
- Gemini: 關閉彈出式視窗前提示尚未儲存的變更。
- Recommendation: gemini - 關閉彈出式視窗前提示尚未儲存的變更。
- Reason: 「彈出式視窗」語法較完整；「彈出視窗」亦可接受。

### blind-social-0186

- Input: 网络恢复后我再把文件发给你。
- Codex: 網路恢復後我再把檔案傳給你。
- Gemini: 網路恢復後我再把文件發給你。
- Recommendation: codex - 網路恢復後我再把檔案傳給你。
- Reason: 日常臺灣用語採「網路、檔案、傳給你」。

### blind-social-0191

- Input: 她在便利店顺便缴了水费。
- Codex: 她在便利商店順便繳了水費。
- Gemini: 她在便利店順便繳了水費。
- Recommendation: codex - 她在便利商店順便繳了水費。
- Reason: 臺灣日常用語採「便利商店」。

### blind-llm-0164

- Input: 检索不到资料时不要编造引用来源。
- Codex: 檢索不到資料時不要編造引用來源。
- Gemini: 檢索不到資料時，不要編造引用來源。
- Recommendation: codex - 檢索不到資料時不要編造引用來源。
- Reason: 只涉及標點差異，保留原句節奏，不新增逗號。

### blind-llm-0166

- Input: 模型生成的代码必须通过静态检查。
- Codex: 模型產生的程式碼必須通過靜態檢查。
- Gemini: 模型生成的程式碼必須通過靜態檢查。
- Recommendation: codex - 模型產生的程式碼必須通過靜態檢查。
- Reason: 採臺灣一般用語「產生程式碼」；「生成」雖可理解但較不優先。

### blind-llm-0169

- Input: 评测数据应与训练语料分开保存。
- Codex: 評測資料應與訓練語料分開儲存。
- Gemini: 評測資料應與訓練語料分開保存。
- Recommendation: codex - 評測資料應與訓練語料分開儲存。
- Reason: 資料持久化語境採「儲存」。

### blind-llm-0172

- Input: 上下文过长时优先保留最新的用户指令。
- Codex: 上下文過長時優先保留最新的使用者指令。
- Gemini: 上下文過長時，優先保留最新的使用者指令。
- Recommendation: codex - 上下文過長時優先保留最新的使用者指令。
- Reason: 只涉及標點差異，保留原句節奏，不新增逗號。

### blind-llm-0174

- Input: 模型拒绝回答时应说明适用的安全规则。
- Codex: 模型拒絕回答時應說明適用的安全規則。
- Gemini: 模型拒絕回答時，應說明適用的安全規則。
- Recommendation: codex - 模型拒絕回答時應說明適用的安全規則。
- Reason: 只涉及標點差異，保留原句節奏，不新增逗號。

### blind-llm-0175

- Input: 批量请求中每个样本都要有唯一标识符。
- Codex: 批次請求中每個樣本都要有唯一識別碼。
- Gemini: 批量請求中，每個樣本都要有唯一識別碼。
- Recommendation: codex - 批次請求中每個樣本都要有唯一識別碼。
- Reason: 臺灣軟體語境採「批次請求」，避免中國用語「批量請求」。

### blind-llm-0177

- Input: 代理不得把工具返回的文本当成系统指令。
- Codex: 代理不得把工具回傳的文字當成系統指令。
- Gemini: 代理不得把工具傳回的文字當成系統指令。
- Recommendation: codex - 代理不得把工具回傳的文字當成系統指令。
- Reason: 工具／函式語境採「回傳」。
