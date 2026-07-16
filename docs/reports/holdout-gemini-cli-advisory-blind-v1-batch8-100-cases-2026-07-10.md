<!-- zhtw:disable -->
# Holdout Gemini CLI Advisory - blind-v1 batch8 100 cases

Generated: 2026-07-10

Reviewer: `gemini_cli`

Raw JSON: `docs/reports/holdout-gemini-cli-advisory-blind-v1-batch8-100-cases-2026-07-10.raw.json`

This is an independent advisory review only. It is not ground truth and must not be promoted without maintainer confirmation.

## Summary

- Total cases: 100
- By domain: {"it": 25, "ui": 20, "llm": 15, "formal": 15, "social": 15, "high_risk": 10}
- By risk: {"candidate_gap": 60, "baseline_guard": 15, "over_conversion_guard": 25}
- By confidence: {"high": 100}
- Review needed: 0
- Model requested: gemini-2.5-flash
- Model observed: gemini-3.5-flash

## Cases

### blind-it-0163

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请把接口响应中的分页游标写入下一页链接。
- Gemini expected: 請把 API 回應中的分頁游標寫入下一頁連結。
- Acceptable alternatives: 請把介面回應中的分頁游標寫入下一頁連結。, 請把 API 回應中的分頁 cursor 寫入下一頁連結。
- Issue tags: it_term, translation
- Rationale: 「接口」在臺灣 IT 情境通常指「API」，「响应」譯為「回應」，「分页游标」譯為「分頁游標」，「链接」譯為「連結」。

### blind-it-0164

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 构建流水线会在单元测试失败时停止部署。
- Gemini expected: 建置管線會在單元測試失敗時停止部署。
- Acceptable alternatives: 構建管線會在單元測試失敗時停止部署。, CI 管線會在單元測試失敗時停止部署。
- Issue tags: it_term
- Rationale: 「构建」在臺灣 IT 情境譯為「建置」，「流水线」譯為「管線」。

### blind-it-0165

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这个命令行工具支持从标准输入读取配置。
- Gemini expected: 這個命令列工具支援從標準輸入讀取設定。
- Acceptable alternatives: 這個命令列工具支援從標準輸入讀取配置。
- Issue tags: it_term
- Rationale: 「命令行」譯為「命令列」，「支持」譯為「支援」，「配置」通常譯為「設定」。

### blind-it-0166

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请在缓存键里加入租户标识避免串数据。
- Gemini expected: 請在快取鍵裡加入租戶識別避免串資料。
- Acceptable alternatives: 請在快取鍵中加入租戶識別碼避免資料錯亂。, 請在快取鍵裡加入租戶標識避免串資料。
- Issue tags: it_term, idiomatic_translation
- Rationale: 「缓存」譯為「快取」，「租户」譯為「租戶」，「标识」譯為「識別碼」或「識別」，「串数据」在臺灣口語常稱作「串資料」或「資料錯亂」。

### blind-it-0167

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 日志采样率可以按服务名称单独设置。
- Gemini expected: 日誌採樣率可以按服務名稱單獨設定。
- Acceptable alternatives: Log 採樣率可以按服務名稱單獨設定。, 日誌抽樣率可以按服務名稱單獨設定。
- Issue tags: it_term
- Rationale: 「日志」譯為「日誌」或「Log」，「采样率」譯為「採樣率」，「设置」譯為「設定」。

### blind-it-0168

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 异步任务完成后会写入审计事件。
- Gemini expected: 非同步任務完成後會寫入稽核事件。
- Acceptable alternatives: 非同步工作完成後會寫入稽核事件。, 非同步任務完成後會寫入審計事件。
- Issue tags: it_term
- Rationale: 「异步」譯為「非同步」，「任务」常譯為「任務」或「工作」，「审计」譯為「稽核」。

### blind-it-0169

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 数据库迁移脚本需要支持回滚。
- Gemini expected: 資料庫遷移腳本需要支援回滾。
- Acceptable alternatives: 資料庫遷移指令碼需要支援復原。, 資料庫移轉腳本需要支援還原。
- Issue tags: it_term
- Rationale: 「数据库」譯為「資料庫」，「脚本」常譯為「腳本」或「指令碼」，「支持」譯為「支援」，「回滚」譯為「回滾」或「復原」。

### blind-it-0170

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 前端组件会根据断点切换布局。
- Gemini expected: 前端元件會根據斷點切換版面配置。
- Acceptable alternatives: 前端元件會根據斷點切換佈局。, 前端組件會根據斷點切換版面。
- Issue tags: it_term
- Rationale: 「组件」譯為「元件」，「布局」在前端開發中常譯為「版面配置」或「佈局」。

### blind-it-0171

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请为每个 Webhook 请求生成签名摘要。
- Gemini expected: 請為每個 Webhook 請求產生簽章摘要。
- Acceptable alternatives: 請為每個 Webhook 請求產生簽名摘要。
- Issue tags: it_term
- Rationale: 「请求」譯為「請求」，「生成」譯為「產生」，「签名」在資訊安全中常譯為「簽章」或「簽名」。

### blind-it-0172

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 服务端渲染会把初始状态注入页面。
- Gemini expected: 伺服器端渲染會把初始狀態注入頁面。
- Acceptable alternatives: 伺服端渲染會把初始狀態注入頁面。
- Issue tags: it_term
- Rationale: 「服务端」譯為「伺服器端」或「伺服端」。

### blind-it-0173

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 包管理器会锁定依赖的精确版本。
- Gemini expected: 套件管理器會鎖定相依性的精確版本。
- Acceptable alternatives: 套件管理工具會鎖定相依性的精確版本。, 包管理器會鎖定相依套件的精確版本。
- Issue tags: it_term
- Rationale: 「包管理器」譯為「套件管理器」，「依赖」在軟體工程中譯為「相依性」或「相依套件」。

### blind-it-0174

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 开发服务器会在文件变更后自动热重载。
- Gemini expected: 開發伺服器會在檔案變更後自動熱重載。
- Acceptable alternatives: 開發伺服器會在檔案修改後自動熱重載。
- Issue tags: it_term
- Rationale: 「开发服务器」譯為「開發伺服器」，「文件」譯為「檔案」，「自动热重载」為標準對應。

### blind-it-0175

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请把错误堆栈上传到观测平台。
- Gemini expected: 請把錯誤堆疊上傳到觀測平台。
- Acceptable alternatives: 請把錯誤堆疊上傳至觀測平台。
- Issue tags: it_term
- Rationale: 「堆栈」譯為「堆疊」，「上传」譯為「上傳」。

### blind-it-0176

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 灰度发布会先开放给内部账号。
- Gemini expected: 灰度發布會先開放給內部帳號。
- Acceptable alternatives: 金絲雀發布會先開放給內部帳號。, 灰度釋出會先開放給內部帳號。
- Issue tags: it_term
- Rationale: 「发布」譯為「發布」或「釋出」，「账号」譯為「帳號」。

### blind-it-0177

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 对象权限会继承存储桶的访问策略。
- Gemini expected: 物件權限會繼承儲存貯體的存取策略。
- Acceptable alternatives: 物件權限會繼承儲存桶的存取原則。, 物件權限會繼承儲存貯體的存取原則。
- Issue tags: it_term
- Rationale: 「对象」譯為「物件」，「存储桶」在雲端服務（如 AWS）臺灣繁體官方通常譯為「儲存貯體」或「儲存桶」，「访问」譯為「存取」，「策略」常譯為「策略」或「原則」。

### blind-it-0178

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: API Gateway v2 不應被翻成中文。
- Gemini expected: API Gateway v2 不應被翻成中文。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-it-0179

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请保留环境变量 ZHTW_CACHE_TTL。
- Gemini expected: 請保留環境變數 ZHTW_CACHE_TTL。
- Acceptable alternatives: (none)
- Issue tags: it_term, guard
- Rationale: 「环境变量」譯為「環境變數」，並保留環境變數識別碼 ZHTW_CACHE_TTL。

### blind-it-0180

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 错误码 ERR_RATE_LIMIT 不要改写。
- Gemini expected: 錯誤碼 ERR_RATE_LIMIT 不要改寫。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 錯誤碼與識別碼 ERR_RATE_LIMIT 保持不變，並將其餘文字轉為臺灣繁體。

### blind-it-0181

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: GitHub Actions 工作流名称 deploy-prod 必须保持一致。
- Gemini expected: GitHub Actions 工作流名稱 deploy-prod 必須保持一致。
- Acceptable alternatives: GitHub Actions 工作流程名稱 deploy-prod 必須保持一致。
- Issue tags: it_term, guard
- Rationale: 保留識別碼 deploy-prod，將「工作流」譯為「工作流」或「工作流程」，並將其餘文字轉為繁體。

### blind-it-0182

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 這段 TypeScript 註解已是繁體，請保持原樣。
- Gemini expected: 這段 TypeScript 註解已是繁體，請保持原樣。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-it-0183

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 伺服器憑證更新說明已核准，請勿改寫。
- Gemini expected: 伺服器憑證更新說明已核准，請勿改寫。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-it-0184

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 用戶端快取設定中的繁體文字不要再轉換。
- Gemini expected: 用戶端快取設定中的繁體文字不要再轉換。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-it-0185

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 這份 API 文件保留「回應」這個用字。
- Gemini expected: 這份 API 文件保留「回應」這個用字。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-it-0186

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 請不要改動已校對的佇列監控訊息。
- Gemini expected: 請不要改動已校對的佇列監控訊息。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-it-0187

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 繁體錯誤提示「連線逾時」應保持不變。
- Gemini expected: 繁體錯誤提示「連線逾時」應保持不變。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-ui-0128

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 点击继续按钮后会显示付款明细。
- Gemini expected: 點擊繼續按鈕後會顯示付款明細。
- Acceptable alternatives: 按一下繼續按鈕後會顯示付款明細。, 點選繼續按鈕後會顯示付款明細。
- Issue tags: ui_term
- Rationale: 「点击」譯為「點擊」、「點選」或「按一下」。

### blind-ui-0129

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请在设置页面打开深色模式。
- Gemini expected: 請在設定頁面開啟深色模式。
- Acceptable alternatives: 請在設定畫面開啟深色模式。, 請在設定頁面打開深色模式。
- Issue tags: ui_term
- Rationale: 「设置」譯為「設定」，「打开」譯為「開啟」。

### blind-ui-0130

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 上传头像前请先裁剪图片。
- Gemini expected: 上傳大頭貼前請先裁切圖片。
- Acceptable alternatives: 上傳頭像前請先裁剪圖片。, 上傳個人頭像前請先裁切圖片。
- Issue tags: ui_term
- Rationale: 「上传」譯為「上傳」，「头像」在臺灣常用「大頭貼」或「頭像」，「裁剪」常譯為「裁切」。

### blind-ui-0131

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 筛选条件已保存到当前视图。
- Gemini expected: 篩選條件已儲存至目前檢視。
- Acceptable alternatives: 篩選條件已儲存到目前視圖。, 篩選條件已儲存至目前視圖。
- Issue tags: ui_term
- Rationale: 「保存」譯為「儲存」，「当前」譯為「目前」，「视图」在軟體中常譯為「檢視」或「視圖」。

### blind-ui-0132

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 订阅到期时会显示续费提示。
- Gemini expected: 訂閱到期時會顯示續訂提示。
- Acceptable alternatives: 訂閱到期時會顯示續費提示。
- Issue tags: ui_term
- Rationale: 「订阅」譯為「訂閱」，「续费」在訂閱服務中常譯為「續訂」。

### blind-ui-0133

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 表单提交失败，请检查必填字段。
- Gemini expected: 表單提交失敗，請檢查必填欄位。
- Acceptable alternatives: 表單送出失敗，請檢查必填欄位。
- Issue tags: ui_term
- Rationale: 「表单」譯為「表單」，「字段」在資料表或表單中譯為「欄位」。

### blind-ui-0134

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 拖动滑块可以调整透明度。
- Gemini expected: 拖曳滑桿可以調整透明度。
- Acceptable alternatives: 拖曳滑塊可以調整透明度。, 拖動滑桿可以調整透明度。
- Issue tags: ui_term
- Rationale: 「拖动」譯為「拖曳」，「滑块」常譯為「滑桿」或「滑塊」。

### blind-ui-0135

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请选择要导出的列。
- Gemini expected: 請選擇要匯出的欄。
- Acceptable alternatives: 請選擇要匯出的欄位。, 請選擇要匯出的列。
- Issue tags: ui_term
- Rationale: 「导出」譯為「匯出」；試算表或表格中的「列」（column）在臺灣譯為「欄」或「欄位」。

### blind-ui-0136

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 对话框关闭前会保存草稿。
- Gemini expected: 對話方塊關閉前會儲存草稿。
- Acceptable alternatives: 對話框關閉前會儲存草稿。
- Issue tags: ui_term
- Rationale: 「对话框」譯為「對話方塊」或「對話框」，「保存」譯為「儲存」。

### blind-ui-0137

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 通知中心会按优先级排序。
- Gemini expected: 通知中心會按優先順序排序。
- Acceptable alternatives: 通知中心會按優先級排序。, 通知中心會按優先權排序。
- Issue tags: ui_term
- Rationale: 「优先级」通常譯為「優先順序」、「優先權」或「優先等級」。

### blind-ui-0138

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请在侧边栏固定常用项目。
- Gemini expected: 請在側邊欄釘選常用項目。
- Acceptable alternatives: 請在側邊欄固定常用項目。
- Issue tags: ui_term
- Rationale: 「固定」（pin）在現代 UI 中常譯為「釘選」，「侧边栏」譯為「側邊欄」。

### blind-ui-0139

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 搜索结果会突出显示匹配词。
- Gemini expected: 搜尋結果會醒目提示相符字詞。
- Acceptable alternatives: 搜尋結果會突出顯示匹配詞。, 搜尋結果會醒目顯示相符字詞。
- Issue tags: ui_term
- Rationale: 「搜索」譯為「搜尋」，「突出显示」常譯為「醒目提示」或「醒目顯示」，「匹配」譯為「相符」或「符合」。

### blind-ui-0140

- Domain: ui
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 按钮文字 Beta 不应被翻译。
- Gemini expected: 按鈕文字 Beta 不應被翻譯。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 「按钮」譯為「按鈕」，保留專有名詞「Beta」。

### blind-ui-0141

- Domain: ui
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请保留 SKU-7788 在商品卡片上。
- Gemini expected: 請保留 SKU-7788 在商品卡片上。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 保留商品編號 SKU-7788，其餘文字轉為繁體。

### blind-ui-0142

- Domain: ui
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 页面标题 Taipei Pro 保持原样。
- Gemini expected: 頁面標題 Taipei Pro 保持原樣。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 保留品牌/型號名稱 Taipei Pro，其餘文字轉為繁體。

### blind-ui-0143

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 這個設定頁已是繁體，請勿修改。
- Gemini expected: 這個設定頁已是繁體，請勿修改。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-ui-0144

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 付款按鈕上的「下一步」不要改寫。
- Gemini expected: 付款按鈕上的「下一步」不要改寫。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-ui-0145

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 繁體錯誤訊息已完成審核，請保留。
- Gemini expected: 繁體錯誤訊息已完成審核，請保留。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-ui-0146

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 使用者選單中的繁體項目維持原樣。
- Gemini expected: 使用者選單中的繁體項目維持原樣。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-ui-0147

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 請不要轉換已核准的客服視窗文案。
- Gemini expected: 請不要轉換已核准的客服視窗文案。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-llm-0093

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 模型会根据系统提示调整回答格式。
- Gemini expected: 模型會根據系統提示調整回答格式。
- Acceptable alternatives: 模型會根據系統提示調整回覆格式。
- Issue tags: llm_term
- Rationale: 「系统」譯為「系統」，將其餘文字轉為繁體。

### blind-llm-0094

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请把检索到的片段附在答案后面。
- Gemini expected: 請把檢索到的片段附在答案後面。
- Acceptable alternatives: 請把檢索到的段落附在答案後面。
- Issue tags: llm_term
- Rationale: 「检索」譯為「檢索」，「后面」譯為「後面」。

### blind-llm-0095

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 摘要生成器会忽略重复段落。
- Gemini expected: 摘要產生器會忽略重複段落。
- Acceptable alternatives: 摘要生成器會忽略重複段落。
- Issue tags: llm_term
- Rationale: 「生成器」通常譯為「產生器」，「重复」譯為「重複」。

### blind-llm-0096

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 代理会在调用工具前说明计划。
- Gemini expected: 代理會在呼叫工具前說明計畫。
- Acceptable alternatives: Agent 會在呼叫工具前說明計畫。, 代理會在呼叫工具前說明計劃。
- Issue tags: llm_term
- Rationale: 「调用」譯為「呼叫」，「计划」常譯為「計畫」或「計劃」。

### blind-llm-0097

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 提示词模板需要保留变量占位符。
- Gemini expected: 提示詞範本需要保留變數預留位置。
- Acceptable alternatives: 提示詞模板需要保留變數佔位符。, 提示詞範本需要保留變數佔位符。
- Issue tags: llm_term, it_term
- Rationale: 「模板」通常譯為「範本」，「变量」譯為「變數」，「占位符」在微軟等官方術語中譯為「預留位置」，技術領域亦常用「佔位符」。

### blind-llm-0098

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 向量数据库会返回最相近的文档块。
- Gemini expected: 向量資料庫會傳回最相近的文件區塊。
- Acceptable alternatives: 向量資料庫會返回最相近的文件區塊。, 向量資料庫會傳回最相近的檔案區塊。
- Issue tags: llm_term, it_term
- Rationale: 「数据库」譯為「資料庫」，「返回」譯為「傳回」，「文档」譯為「文件」，「文档块」（document chunk）常譯為「文件區塊」。

### blind-llm-0099

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 评估脚本会比较回答的一致性。
- Gemini expected: 評估腳本會比較回答的一致性。
- Acceptable alternatives: 評估指令碼會比較回答的一致性。, 評估腳本會比較回覆的一致性。
- Issue tags: it_term
- Rationale: 「评估」譯為「評估」，「脚本」常譯為「腳本」或「指令碼」。

### blind-llm-0100

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请限制模型输出为三条要点。
- Gemini expected: 請限制模型輸出為三條要點。
- Acceptable alternatives: (none)
- Issue tags: llm_term
- Rationale: 將簡體字轉為繁體字。

### blind-llm-0101

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 聊天机器人需要识别用户意图。
- Gemini expected: 聊天機器人需要識別使用者意圖。
- Acceptable alternatives: 聊天機器人需要辨識使用者意圖。, 聊天機器人需要識別用戶意圖。
- Issue tags: llm_term
- Rationale: 「机器人」譯為「機器人」，「识别」常譯為「識別」或「辨識」，「用户」常譯為「使用者」或「用戶」。

### blind-llm-0102

- Domain: llm
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: Prompt ID qa_router_v3 不应被改写。
- Gemini expected: Prompt ID qa_router_v3 不應被改寫。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣，並保留 Prompt ID。

### blind-llm-0103

- Domain: llm
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请保留模型名称 GPT-5-Codex。
- Gemini expected: 請保留模型名稱 GPT-5-Codex。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 保留模型名稱 GPT-5-Codex，其餘文字轉為繁體。

### blind-llm-0104

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 這段繁體提示詞已經過審核。
- Gemini expected: 這段繁體提示詞已經過審核。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-llm-0105

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 請保留「使用者意圖」這個繁體用語。
- Gemini expected: 請保留「使用者意圖」這個繁體用語。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-llm-0106

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 繁體摘要範本不要被自動改寫。
- Gemini expected: 繁體摘要範本不要被自動改寫。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-llm-0107

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 這份工具說明已是繁體，請勿轉換。
- Gemini expected: 這份工具說明已是繁體，請勿轉換。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-formal-0094

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 董事会将于下周审议年度预算。
- Gemini expected: 董事會將於下週審議年度預算。
- Acceptable alternatives: 董事會將於下星期審議年度預算。
- Issue tags: formal_term
- Rationale: 「董事会」譯為「董事會」，「下周」譯為「下週」，將其餘字元轉為繁體。

### blind-formal-0095

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 公告内容应说明申请资格和截止日期。
- Gemini expected: 公告內容應說明申請資格和截止日期。
- Acceptable alternatives: 公告內容應說明申請資格及截止日期。
- Issue tags: formal_term
- Rationale: 將簡體字轉為繁體字。

### blind-formal-0096

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 承办单位会汇整意见后提交报告。
- Gemini expected: 承辦單位會彙整意見後提交報告。
- Acceptable alternatives: 承辦單位會彙整意見後提出報告。
- Issue tags: formal_term
- Rationale: 「承办」譯為「承辦」，「汇整」在臺灣公文與正式情境中常作「彙整」。

### blind-formal-0097

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 本公司将根据合约条款办理退款。
- Gemini expected: 本公司將根據合約條款辦理退款。
- Acceptable alternatives: (none)
- Issue tags: formal_term
- Rationale: 將簡體字轉為繁體字。

### blind-formal-0098

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 会议记录应载明出席人员名单。
- Gemini expected: 會議紀錄應載明出席人員名單。
- Acceptable alternatives: 會議記錄應載明出席人員名單。
- Issue tags: formal_term
- Rationale: 「会议记录」譯為「會議紀錄」或「會議記錄」，「人员」譯為「人員」。

### blind-formal-0099

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 采购案将在评选完成后公告结果。
- Gemini expected: 採購案將在評選完成後公告結果。
- Acceptable alternatives: (none)
- Issue tags: formal_term
- Rationale: 將簡體字轉為繁體字。

### blind-formal-0100

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 主管机关可要求业者限期改善。
- Gemini expected: 主管機關可要求業者限期改善。
- Acceptable alternatives: (none)
- Issue tags: formal_term
- Rationale: 將簡體字轉為繁體字。

### blind-formal-0101

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 申请人应检附身份证明文件。
- Gemini expected: 申請人應檢附身分證明文件。
- Acceptable alternatives: 申請人應檢附身份證明文件。
- Issue tags: formal_term
- Rationale: 「申请人」譯為「申請人」，「应检附」譯為「應檢附」，臺灣公文常使用「身分證明文件」（亦可寫作「身份證明文件」）。

### blind-formal-0102

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 新闻稿须避免使用未经证实的数据。
- Gemini expected: 新聞稿須避免使用未經證實的數據。
- Acceptable alternatives: 新聞稿須避免使用未經證實的資料。
- Issue tags: formal_term
- Rationale: 「新闻稿」譯為「新聞稿」，「数据」譯為「數據」或「資料」。

### blind-formal-0103

- Domain: formal
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请保留项目名称 RiverLink 2026。
- Gemini expected: 請保留專案名稱 RiverLink 2026。
- Acceptable alternatives: 請保留項目名稱 RiverLink 2026。
- Issue tags: guard, formal_term
- Rationale: 「项目」在專案管理情境譯為「專案」，並保留專案名稱 RiverLink 2026。

### blind-formal-0104

- Domain: formal
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 公文编号 GOV-AB-2026-07 不得改写。
- Gemini expected: 公文編號 GOV-AB-2026-07 不得改寫。
- Acceptable alternatives: 公文字號 GOV-AB-2026-07 不得改寫。
- Issue tags: guard
- Rationale: 保留公文編號 GOV-AB-2026-07，並將其餘文字轉為繁體。

### blind-formal-0105

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 本繁體公告已核定，請勿改寫。
- Gemini expected: 本繁體公告已核定，請勿改寫。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-formal-0106

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 合約中的繁體條款應保持原樣。
- Gemini expected: 合約中的繁體條款應保持原樣。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-formal-0107

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 請保留「品質管理」這個正式用語。
- Gemini expected: 請保留「品質管理」這個正式用語。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-formal-0108

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 已發布的繁體新聞標題不應再轉換。
- Gemini expected: 已發布的繁體新聞標題不應再轉換。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-social-0094

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这个周末想找朋友一起吃早午餐。
- Gemini expected: 這個週末想找朋友一起吃早午餐。
- Acceptable alternatives: 這個周末想找朋友一起吃早午餐。
- Issue tags: social_term
- Rationale: 「周末」譯為「週末」或「周末」，將其餘字元轉為繁體。

### blind-social-0095

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请帮我把地址发到群组里。
- Gemini expected: 請幫我把地址傳到群組裡。
- Acceptable alternatives: 請幫我把地址發到群組裡。, 請幫我把地址傳到群組中。
- Issue tags: social_term
- Rationale: 「发到」譯為「傳到」或「發到」，「群组」譯為「群組」，「里」譯為「裡」。

### blind-social-0096

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 我刚刚预约了明天下午的课程。
- Gemini expected: 我剛剛預約了明天下午的課程。
- Acceptable alternatives: (none)
- Issue tags: social_term
- Rationale: 將簡體字轉為繁體字。

### blind-social-0097

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这家店的服务态度真的很好。
- Gemini expected: 這家店的服務態度真的很好。
- Acceptable alternatives: (none)
- Issue tags: social_term
- Rationale: 將簡體字轉為繁體字。

### blind-social-0098

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 等等我，我还在找停车位。
- Gemini expected: 等等我，我還在找停車位。
- Acceptable alternatives: (none)
- Issue tags: social_term
- Rationale: 將簡體字轉為繁體字。

### blind-social-0099

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 可以帮我确认外送到了没？
- Gemini expected: 擺脫 OpenCC 改寫，可以幫我確認外送到了沒？
- Acceptable alternatives: (none)
- Issue tags: social_term
- Rationale: 「外送」本身已符合臺灣口語用法，將其餘字元轉為繁體。

### blind-social-0100

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 今天的活动照片已经上传相册。
- Gemini expected: 今天的活動照片已經上傳相簿。
- Acceptable alternatives: 今天的活動照片已經上傳相冊。
- Issue tags: social_term
- Rationale: 「相册」在臺灣常譯為「相簿」或「相冊」。

### blind-social-0101

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请提醒大家记得带雨具。
- Gemini expected: 請提醒大家記得帶雨具。
- Acceptable alternatives: (none)
- Issue tags: social_term
- Rationale: 將簡體字轉為繁體字。

### blind-social-0102

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这篇心得文想改成比较自然的语气。
- Gemini expected: 這篇心得文想改成比較自然的語氣。
- Acceptable alternatives: (none)
- Issue tags: social_term
- Rationale: 「心得文」已符合臺灣常用社群用語，將其餘字元轉為繁體。

### blind-social-0103

- Domain: social
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请保留昵称 MiniTim 不要翻译。
- Gemini expected: 請保留暱稱 MiniTim 不要翻譯。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 「昵称」譯為「暱稱」，保留暱稱 MiniTim。

### blind-social-0104

- Domain: social
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 活动标签 #TaipeiFood 不要改写。
- Gemini expected: 活動標籤 #TaipeiFood 不要改寫。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 「标签」譯為「標籤」，保留活動標籤 #TaipeiFood。

### blind-social-0105

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 這則繁體留言已經確認，請勿改寫。
- Gemini expected: 這則繁體留言已經確認，請勿改寫。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-social-0106

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 我想保留「週末」這個寫法。
- Gemini expected: 我想保留「週末」這個寫法。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-social-0107

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 繁體社團公告不要自動轉換。
- Gemini expected: 繁體社團公告不要自動轉換。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-social-0108

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 這段聊天紀錄已是繁體，請保持原樣。
- Gemini expected: 這段聊天紀錄已是繁體，請保持原樣。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-high-risk-0061

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 医师会评估过敏史后调整处方。
- Gemini expected: 醫師會評估過敏史後調整處方。
- Acceptable alternatives: (none)
- Issue tags: high_risk_term
- Rationale: 將簡體字轉為繁體字。

### blind-high-risk-0062

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 银行应确认汇款账户的实名资料。
- Gemini expected: 銀行應確認匯款帳戶的實名資料。
- Acceptable alternatives: 銀行應確認匯款帳號的實名資料。
- Issue tags: high_risk_term
- Rationale: 「账户」譯為「帳戶」，「实名」譯為「實名」，其餘字元轉為繁體。

### blind-high-risk-0063

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 保险公司须说明除外责任范围。
- Gemini expected: 保險公司須說明除外責任範圍。
- Acceptable alternatives: (none)
- Issue tags: high_risk_term
- Rationale: 將簡體字轉為繁體字。

### blind-high-risk-0064

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 法院可依申请核发支付命令。
- Gemini expected: 法院可依申請核發支付命令。
- Acceptable alternatives: (none)
- Issue tags: high_risk_term
- Rationale: 「支付命令」已是臺灣法律之標準用語，將其餘字元轉為繁體。

### blind-high-risk-0065

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 投资人应阅读公开说明书后再决定。
- Gemini expected: 投資人應閱讀公開說明書後再決定。
- Acceptable alternatives: (none)
- Issue tags: high_risk_term
- Rationale: 「公開說明書」已是臺灣金融之標準用語，將其餘字元轉為繁體。

### blind-high-risk-0066

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 药袋标签应载明服用频率。
- Gemini expected: 藥袋標籤應載明服用頻率。
- Acceptable alternatives: 藥袋標籤應載明服用次數。
- Issue tags: high_risk_term
- Rationale: 將簡體字轉為繁體字。

### blind-high-risk-0067

- Domain: high_risk
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 病历号 MED-TW-2026-11 不应被改写。
- Gemini expected: 病歷號 MED-TW-2026-11 不應被改寫。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 「病历」譯為「病歷」，並保留病歷編號 MED-TW-2026-11。

### blind-high-risk-0068

- Domain: high_risk
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请保留金融机构代码 812。
- Gemini expected: 請保留金融機構代碼 812。
- Acceptable alternatives: 請保留金融機構代號 812。
- Issue tags: guard
- Rationale: 「金融机构」譯為「金融機構」，「代码」譯為「代碼」或「代號」，並保留代碼 812。

### blind-high-risk-0069

- Domain: high_risk
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 這份繁體醫囑已由醫師確認。
- Gemini expected: 這份繁體醫囑已由醫師確認。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。

### blind-high-risk-0070

- Domain: high_risk
- Risk: over_conversion_guard
- Confidence: high
- Review needed: False
- Input: 契約中的繁體免責條款請保持原樣。
- Gemini expected: 契約中的繁體免責條款請保持原樣。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 此為繁體護衛案例，保持原樣。
