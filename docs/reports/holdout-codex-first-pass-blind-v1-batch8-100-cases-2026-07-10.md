<!-- zhtw:disable -->
# Holdout Codex First-Pass Advisory - blind-v1 batch8 100 cases

Generated: 2026-07-10

This is an advisory first pass only. It is not ground truth and must not be promoted without maintainer confirmation.

## Summary

- Total cases: 100
- By domain: {"it": 25, "ui": 20, "llm": 15, "formal": 15, "social": 15, "high_risk": 10}
- By risk: {"candidate_gap": 60, "baseline_guard": 15, "over_conversion_guard": 25}
- By confidence: {"medium": 20, "high": 80}
- Review needed: 50
- Promotion allowed: False

## Cases

### blind-it-0163

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 请把接口响应中的分页游标写入下一页链接。
- Codex expected: 請把介面回應中的分頁游標寫入下一頁連結。
- Acceptable alternatives: 請把 API 回應中的分頁游標寫入下一頁連結。
- Issue tags: technical_term, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-it-0164

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 构建流水线会在单元测试失败时停止部署。
- Codex expected: 建置管線會在單元測試失敗時停止部署。
- Acceptable alternatives: 建置流水線會在單元測試失敗時停止部署。
- Issue tags: technical_term, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-it-0165

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这个命令行工具支持从标准输入读取配置。
- Codex expected: 這個命令列工具支援從標準輸入讀取設定。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0166

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 请在缓存键里加入租户标识避免串数据。
- Codex expected: 請在快取鍵裡加入租用戶識別碼，避免資料混淆。
- Acceptable alternatives: 請在快取鍵裡加入租戶識別碼，避免資料混淆。
- Issue tags: technical_term, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-it-0167

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 日志采样率可以按服务名称单独设置。
- Codex expected: 日誌取樣率可以依服務名稱個別設定。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0168

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 异步任务完成后会写入审计事件。
- Codex expected: 非同步任務完成後會寫入稽核事件。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-it-0169

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 数据库迁移脚本需要支持回滚。
- Codex expected: 資料庫遷移指令碼需要支援復原。
- Acceptable alternatives: 資料庫遷移腳本需要支援回滾。
- Issue tags: technical_term, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-it-0170

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 前端组件会根据断点切换布局。
- Codex expected: 前端元件會根據斷點切換版面配置。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0171

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请为每个 Webhook 请求生成签名摘要。
- Codex expected: 請為每個 Webhook 請求產生簽章摘要。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0172

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 服务端渲染会把初始状态注入页面。
- Codex expected: 伺服器端渲染會把初始狀態注入頁面。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0173

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 包管理器会锁定依赖的精确版本。
- Codex expected: 套件管理器會鎖定相依套件的精確版本。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0174

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 开发服务器会在文件变更后自动热重载。
- Codex expected: 開發伺服器會在檔案變更後自動熱重新載入。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0175

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请把错误堆栈上传到观测平台。
- Codex expected: 請把錯誤堆疊上傳到可觀測性平台。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0176

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 灰度发布会先开放给内部账号。
- Codex expected: 漸進式發布會先開放給內部帳號。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0177

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 对象权限会继承存储桶的访问策略。
- Codex expected: 物件權限會繼承儲存桶的存取策略。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0178

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: API Gateway v2 不應被翻成中文。
- Codex expected: API Gateway v2 不應被翻成中文。
- Acceptable alternatives: (none)
- Issue tags: identifier_or_proper_noun_guard
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0179

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请保留环境变量 ZHTW_CACHE_TTL。
- Codex expected: 請保留環境變數 ZHTW_CACHE_TTL。
- Acceptable alternatives: (none)
- Issue tags: identifier_or_proper_noun_guard
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0180

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 错误码 ERR_RATE_LIMIT 不要改写。
- Codex expected: 錯誤碼 ERR_RATE_LIMIT 不要改寫。
- Acceptable alternatives: (none)
- Issue tags: identifier_or_proper_noun_guard
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0181

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: GitHub Actions 工作流名称 deploy-prod 必须保持一致。
- Codex expected: GitHub Actions 工作流程名稱 deploy-prod 必須保持一致。
- Acceptable alternatives: (none)
- Issue tags: identifier_or_proper_noun_guard
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0182

- Domain: it
- Risk: over_conversion_guard
- Confidence: medium
- Review needed: True
- Input: 這段 TypeScript 註解已是繁體，請保持原樣。
- Codex expected: 這段 TypeScript 註解已是繁體，請保持原樣。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。

### blind-it-0183

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 伺服器憑證更新說明已核准，請勿改寫。
- Codex expected: 伺服器憑證更新說明已核准，請勿改寫。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。

### blind-it-0184

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 用戶端快取設定中的繁體文字不要再轉換。
- Codex expected: 用戶端快取設定中的繁體文字不要再轉換。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。

### blind-it-0185

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 這份 API 文件保留「回應」這個用字。
- Codex expected: 這份 API 文件保留「回應」這個用字。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。

### blind-it-0186

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 請不要改動已校對的佇列監控訊息。
- Codex expected: 請不要改動已校對的佇列監控訊息。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。

### blind-it-0187

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 繁體錯誤提示「連線逾時」應保持不變。
- Codex expected: 繁體錯誤提示「連線逾時」應保持不變。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。

### blind-ui-0128

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 点击继续按钮后会显示付款明细。
- Codex expected: 點擊繼續按鈕後會顯示付款明細。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0129

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请在设置页面打开深色模式。
- Codex expected: 請在設定頁面開啟深色模式。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0130

- Domain: ui
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 上传头像前请先裁剪图片。
- Codex expected: 上傳頭像前請先裁切圖片。
- Acceptable alternatives: 上傳大頭貼前請先裁切圖片。
- Issue tags: ui_term, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-ui-0131

- Domain: ui
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 筛选条件已保存到当前视图。
- Codex expected: 篩選條件已儲存到目前檢視。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-ui-0132

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 订阅到期时会显示续费提示。
- Codex expected: 訂閱到期時會顯示續費提示。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0133

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 表单提交失败，请检查必填字段。
- Codex expected: 表單送出失敗，請檢查必填欄位。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0134

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 拖动滑块可以调整透明度。
- Codex expected: 拖曳滑桿可以調整透明度。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0135

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请选择要导出的列。
- Codex expected: 請選擇要匯出的欄。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0136

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 对话框关闭前会保存草稿。
- Codex expected: 對話框關閉前會儲存草稿。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0137

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 通知中心会按优先级排序。
- Codex expected: 通知中心會依優先順序排序。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0138

- Domain: ui
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 请在侧边栏固定常用项目。
- Codex expected: 請在側邊欄釘選常用項目。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-ui-0139

- Domain: ui
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 搜索结果会突出显示匹配词。
- Codex expected: 搜尋結果會醒目顯示相符詞。
- Acceptable alternatives: 搜尋結果會突出顯示符合的詞。
- Issue tags: ui_term, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-ui-0140

- Domain: ui
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 按钮文字 Beta 不应被翻译。
- Codex expected: 按鈕文字 Beta 不應被翻譯。
- Acceptable alternatives: (none)
- Issue tags: identifier_or_proper_noun_guard
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0141

- Domain: ui
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请保留 SKU-7788 在商品卡片上。
- Codex expected: 請保留 SKU-7788 在商品卡片上。
- Acceptable alternatives: (none)
- Issue tags: identifier_or_proper_noun_guard
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0142

- Domain: ui
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 页面标题 Taipei Pro 保持原样。
- Codex expected: 頁面標題 Taipei Pro 保持原樣。
- Acceptable alternatives: (none)
- Issue tags: identifier_or_proper_noun_guard
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0143

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 這個設定頁已是繁體，請勿修改。
- Codex expected: 這個設定頁已是繁體，請勿修改。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。

### blind-ui-0144

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 付款按鈕上的「下一步」不要改寫。
- Codex expected: 付款按鈕上的「下一步」不要改寫。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。

### blind-ui-0145

- Domain: ui
- Risk: over_conversion_guard
- Confidence: medium
- Review needed: True
- Input: 繁體錯誤訊息已完成審核，請保留。
- Codex expected: 繁體錯誤訊息已完成審核，請保留。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。

### blind-ui-0146

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 使用者選單中的繁體項目維持原樣。
- Codex expected: 使用者選單中的繁體項目維持原樣。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。

### blind-ui-0147

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 請不要轉換已核准的客服視窗文案。
- Codex expected: 請不要轉換已核准的客服視窗文案。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。

### blind-llm-0093

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 模型会根据系统提示调整回答格式。
- Codex expected: 模型會根據系統提示調整回答格式。
- Acceptable alternatives: (none)
- Issue tags: llm_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0094

- Domain: llm
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 请把检索到的片段附在答案后面。
- Codex expected: 請把檢索到的片段附在答案後面。
- Acceptable alternatives: (none)
- Issue tags: llm_term, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-llm-0095

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 摘要生成器会忽略重复段落。
- Codex expected: 摘要產生器會忽略重複段落。
- Acceptable alternatives: (none)
- Issue tags: llm_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0096

- Domain: llm
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 代理会在调用工具前说明计划。
- Codex expected: 代理程式會在呼叫工具前說明計畫。
- Acceptable alternatives: 代理會在呼叫工具前說明計畫。
- Issue tags: llm_term, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-llm-0097

- Domain: llm
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 提示词模板需要保留变量占位符。
- Codex expected: 提示詞範本需要保留變數預留位置。
- Acceptable alternatives: (none)
- Issue tags: llm_term, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-llm-0098

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 向量数据库会返回最相近的文档块。
- Codex expected: 向量資料庫會回傳最相近的文件區塊。
- Acceptable alternatives: (none)
- Issue tags: llm_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0099

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 评估脚本会比较回答的一致性。
- Codex expected: 評估指令碼會比較回答的一致性。
- Acceptable alternatives: (none)
- Issue tags: llm_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0100

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请限制模型输出为三条要点。
- Codex expected: 請限制模型輸出為三個重點。
- Acceptable alternatives: (none)
- Issue tags: llm_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0101

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 聊天机器人需要识别用户意图。
- Codex expected: 聊天機器人需要辨識使用者意圖。
- Acceptable alternatives: (none)
- Issue tags: llm_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0102

- Domain: llm
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: Prompt ID qa_router_v3 不应被改写。
- Codex expected: Prompt ID qa_router_v3 不應被改寫。
- Acceptable alternatives: (none)
- Issue tags: identifier_or_proper_noun_guard
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0103

- Domain: llm
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请保留模型名称 GPT-5-Codex。
- Codex expected: 請保留模型名稱 GPT-5-Codex。
- Acceptable alternatives: (none)
- Issue tags: identifier_or_proper_noun_guard
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0104

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 這段繁體提示詞已經過審核。
- Codex expected: 這段繁體提示詞已經過審核。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。

### blind-llm-0105

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 請保留「使用者意圖」這個繁體用語。
- Codex expected: 請保留「使用者意圖」這個繁體用語。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。

### blind-llm-0106

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 繁體摘要範本不要被自動改寫。
- Codex expected: 繁體摘要範本不要被自動改寫。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。

### blind-llm-0107

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 這份工具說明已是繁體，請勿轉換。
- Codex expected: 這份工具說明已是繁體，請勿轉換。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。

### blind-formal-0094

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 董事会将于下周审议年度预算。
- Codex expected: 董事會將於下週審議年度預算。
- Acceptable alternatives: (none)
- Issue tags: formal_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0095

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 公告内容应说明申请资格和截止日期。
- Codex expected: 公告內容應說明申請資格和截止日期。
- Acceptable alternatives: (none)
- Issue tags: formal_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0096

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 承办单位会汇整意见后提交报告。
- Codex expected: 承辦單位會彙整意見後提交報告。
- Acceptable alternatives: (none)
- Issue tags: formal_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0097

- Domain: formal
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 本公司将根据合约条款办理退款。
- Codex expected: 本公司將根據合約條款辦理退款。
- Acceptable alternatives: 本公司將依合約條款辦理退款。
- Issue tags: formal_term, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-formal-0098

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 会议记录应载明出席人员名单。
- Codex expected: 會議紀錄應載明出席人員名單。
- Acceptable alternatives: (none)
- Issue tags: formal_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0099

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 采购案将在评选完成后公告结果。
- Codex expected: 採購案將在評選完成後公告結果。
- Acceptable alternatives: (none)
- Issue tags: formal_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0100

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 主管机关可要求业者限期改善。
- Codex expected: 主管機關可要求業者限期改善。
- Acceptable alternatives: (none)
- Issue tags: formal_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0101

- Domain: formal
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 申请人应检附身份证明文件。
- Codex expected: 申請人應檢附身分證明文件。
- Acceptable alternatives: 申請人應檢附身份證明文件。
- Issue tags: formal_term, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-formal-0102

- Domain: formal
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 新闻稿须避免使用未经证实的数据。
- Codex expected: 新聞稿須避免使用未經證實的資料。
- Acceptable alternatives: (none)
- Issue tags: formal_term, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-formal-0103

- Domain: formal
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请保留项目名称 RiverLink 2026。
- Codex expected: 請保留專案名稱 RiverLink 2026。
- Acceptable alternatives: (none)
- Issue tags: identifier_or_proper_noun_guard
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0104

- Domain: formal
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 公文编号 GOV-AB-2026-07 不得改写。
- Codex expected: 公文編號 GOV-AB-2026-07 不得改寫。
- Acceptable alternatives: (none)
- Issue tags: identifier_or_proper_noun_guard
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0105

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 本繁體公告已核定，請勿改寫。
- Codex expected: 本繁體公告已核定，請勿改寫。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。

### blind-formal-0106

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 合約中的繁體條款應保持原樣。
- Codex expected: 合約中的繁體條款應保持原樣。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。

### blind-formal-0107

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 請保留「品質管理」這個正式用語。
- Codex expected: 請保留「品質管理」這個正式用語。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。

### blind-formal-0108

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 已發布的繁體新聞標題不應再轉換。
- Codex expected: 已發布的繁體新聞標題不應再轉換。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。

### blind-social-0094

- Domain: social
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 这个周末想找朋友一起吃早午餐。
- Codex expected: 這個週末想找朋友一起吃早午餐。
- Acceptable alternatives: (none)
- Issue tags: daily_term, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-social-0095

- Domain: social
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 请帮我把地址发到群组里。
- Codex expected: 請幫我把地址傳到群組裡。
- Acceptable alternatives: (none)
- Issue tags: daily_term, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-social-0096

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 我刚刚预约了明天下午的课程。
- Codex expected: 我剛剛預約了明天下午的課程。
- Acceptable alternatives: (none)
- Issue tags: daily_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0097

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这家店的服务态度真的很好。
- Codex expected: 這家店的服務態度真的很好。
- Acceptable alternatives: (none)
- Issue tags: daily_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0098

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 等等我，我还在找停车位。
- Codex expected: 等等我，我還在找停車位。
- Acceptable alternatives: (none)
- Issue tags: daily_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0099

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 可以帮我确认外送到了没？
- Codex expected: 可以幫我確認外送到了沒？
- Acceptable alternatives: (none)
- Issue tags: daily_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0100

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 今天的活动照片已经上传相册。
- Codex expected: 今天的活動照片已經上傳相簿。
- Acceptable alternatives: 今天的活動照片已經上傳相冊。
- Issue tags: daily_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0101

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请提醒大家记得带雨具。
- Codex expected: 請提醒大家記得帶雨具。
- Acceptable alternatives: (none)
- Issue tags: daily_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0102

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这篇心得文想改成比较自然的语气。
- Codex expected: 這篇心得文想改成比較自然的語氣。
- Acceptable alternatives: (none)
- Issue tags: daily_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0103

- Domain: social
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请保留昵称 MiniTim 不要翻译。
- Codex expected: 請保留暱稱 MiniTim 不要翻譯。
- Acceptable alternatives: (none)
- Issue tags: identifier_or_proper_noun_guard
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0104

- Domain: social
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 活动标签 #TaipeiFood 不要改写。
- Codex expected: 活動標籤 #TaipeiFood 不要改寫。
- Acceptable alternatives: (none)
- Issue tags: identifier_or_proper_noun_guard
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0105

- Domain: social
- Risk: over_conversion_guard
- Confidence: medium
- Review needed: True
- Input: 這則繁體留言已經確認，請勿改寫。
- Codex expected: 這則繁體留言已經確認，請勿改寫。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。

### blind-social-0106

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 我想保留「週末」這個寫法。
- Codex expected: 我想保留「週末」這個寫法。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。

### blind-social-0107

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 繁體社團公告不要自動轉換。
- Codex expected: 繁體社團公告不要自動轉換。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。

### blind-social-0108

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 這段聊天紀錄已是繁體，請保持原樣。
- Codex expected: 這段聊天紀錄已是繁體，請保持原樣。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。

### blind-high-risk-0061

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 医师会评估过敏史后调整处方。
- Codex expected: 醫師會評估過敏史後調整處方。
- Acceptable alternatives: (none)
- Issue tags: high_risk_term, tw_usage
- Rationale: 高風險領域詞彙需 maintainer 確認；此為 first-pass 建議。

### blind-high-risk-0062

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 银行应确认汇款账户的实名资料。
- Codex expected: 銀行應確認匯款帳戶的實名資料。
- Acceptable alternatives: (none)
- Issue tags: high_risk_term, tw_usage
- Rationale: 高風險領域詞彙需 maintainer 確認；此為 first-pass 建議。

### blind-high-risk-0063

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 保险公司须说明除外责任范围。
- Codex expected: 保險公司須說明除外責任範圍。
- Acceptable alternatives: (none)
- Issue tags: high_risk_term, tw_usage
- Rationale: 高風險領域詞彙需 maintainer 確認；此為 first-pass 建議。

### blind-high-risk-0064

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 法院可依申请核发支付命令。
- Codex expected: 法院可依申請核發支付命令。
- Acceptable alternatives: (none)
- Issue tags: high_risk_term, tw_usage
- Rationale: 高風險領域詞彙需 maintainer 確認；此為 first-pass 建議。

### blind-high-risk-0065

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 投资人应阅读公开说明书后再决定。
- Codex expected: 投資人應閱讀公開說明書後再決定。
- Acceptable alternatives: (none)
- Issue tags: high_risk_term, tw_usage
- Rationale: 高風險領域詞彙需 maintainer 確認；此為 first-pass 建議。

### blind-high-risk-0066

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 药袋标签应载明服用频率。
- Codex expected: 藥袋標籤應載明服用頻率。
- Acceptable alternatives: (none)
- Issue tags: high_risk_term, tw_usage
- Rationale: 高風險領域詞彙需 maintainer 確認；此為 first-pass 建議。

### blind-high-risk-0067

- Domain: high_risk
- Risk: baseline_guard
- Confidence: high
- Review needed: True
- Input: 病历号 MED-TW-2026-11 不应被改写。
- Codex expected: 病歷號 MED-TW-2026-11 不應被改寫。
- Acceptable alternatives: (none)
- Issue tags: identifier_or_proper_noun_guard
- Rationale: 高風險領域詞彙需 maintainer 確認；此為 first-pass 建議。

### blind-high-risk-0068

- Domain: high_risk
- Risk: baseline_guard
- Confidence: high
- Review needed: True
- Input: 请保留金融机构代码 812。
- Codex expected: 請保留金融機構代碼 812。
- Acceptable alternatives: (none)
- Issue tags: identifier_or_proper_noun_guard
- Rationale: 高風險領域詞彙需 maintainer 確認；此為 first-pass 建議。

### blind-high-risk-0069

- Domain: high_risk
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 這份繁體醫囑已由醫師確認。
- Codex expected: 這份繁體醫囑已由醫師確認。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。

### blind-high-risk-0070

- Domain: high_risk
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 契約中的繁體免責條款請保持原樣。
- Codex expected: 契約中的繁體免責條款請保持原樣。
- Acceptable alternatives: (none)
- Issue tags: traditional_guard, already_traditional
- Rationale: 此案例用來防止已正確的繁體輸入被二次轉換改壞；需維持人工確認流程。
