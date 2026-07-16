<!-- zhtw:disable -->
# Holdout Maintainer Confirmation - blind-v1 batch8 100 cases

Generated: 2026-07-10

This packet is for maintainer confirmation. It is not ground truth; do not write private expected until maintainer OK.

## Summary

- total_review_cases: 66
- difference_cases: 24
- policy_review_cases: 42
- no_immediate_question: 34
- difference_recommendations: {"codex": 17, "gemini": 7}
- by_domain: {"it": 18, "ui": 13, "llm": 11, "formal": 7, "social": 7, "high_risk": 10}
- by_risk: {"candidate_gap": 38, "baseline_guard": 3, "over_conversion_guard": 25}
- by_kind: {"difference": 24, "policy_review": 42}
- by_policy_reason: {"Codex confidence medium": 20, "Codex review-needed policy guard": 50, "high-risk domain": 10, "over-conversion guard": 25}
- promotion_allowed: False

## Review Cases

### blind-it-0163

- Kind: difference
- Domain: it
- Risk: candidate_gap
- Input: 请把接口响应中的分页游标写入下一页链接。
- Codex expected: 請把介面回應中的分頁游標寫入下一頁連結。
- Gemini expected: 請把 API 回應中的分頁游標寫入下一頁連結。
- Recommendation: gemini
- Recommended expected: 請把 API 回應中的分頁游標寫入下一頁連結。
- Recommended acceptable: 請把介面回應中的分頁游標寫入下一頁連結。
- Reason: Gemini primary is already listed as a Codex acceptable variant.
- Maintainer action: confirm_recommendation_or_edit

### blind-it-0166

- Kind: difference
- Domain: it
- Risk: candidate_gap
- Input: 请在缓存键里加入租户标识避免串数据。
- Codex expected: 請在快取鍵裡加入租用戶識別碼，避免資料混淆。
- Gemini expected: 請在快取鍵裡加入租戶識別避免串資料。
- Recommendation: gemini
- Recommended expected: 請在快取鍵裡加入租戶識別避免串資料。
- Recommended acceptable: 請在快取鍵裡加入租用戶識別碼，避免資料混淆。, 請在快取鍵裡加入租戶識別碼，避免資料混淆。
- Reason: Codex marked this as a variant-sensitive case and Gemini gave a high-confidence alternative.
- Maintainer action: confirm_recommendation_or_edit

### blind-it-0167

- Kind: difference
- Domain: it
- Risk: candidate_gap
- Input: 日志采样率可以按服务名称单独设置。
- Codex expected: 日誌取樣率可以依服務名稱個別設定。
- Gemini expected: 日誌採樣率可以按服務名稱單獨設定。
- Recommendation: codex
- Recommended expected: 日誌取樣率可以依服務名稱個別設定。
- Recommended acceptable: 日誌採樣率可以按服務名稱單獨設定。, Log 採樣率可以按服務名稱單獨設定。, 日誌抽樣率可以按服務名稱單獨設定。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.
- Maintainer action: confirm_recommendation_or_edit

### blind-it-0169

- Kind: difference
- Domain: it
- Risk: candidate_gap
- Input: 数据库迁移脚本需要支持回滚。
- Codex expected: 資料庫遷移指令碼需要支援復原。
- Gemini expected: 資料庫遷移腳本需要支援回滾。
- Recommendation: gemini
- Recommended expected: 資料庫遷移腳本需要支援回滾。
- Recommended acceptable: 資料庫遷移指令碼需要支援復原。
- Reason: Gemini primary is already listed as a Codex acceptable variant.
- Maintainer action: confirm_recommendation_or_edit

### blind-it-0173

- Kind: difference
- Domain: it
- Risk: candidate_gap
- Input: 包管理器会锁定依赖的精确版本。
- Codex expected: 套件管理器會鎖定相依套件的精確版本。
- Gemini expected: 套件管理器會鎖定相依性的精確版本。
- Recommendation: codex
- Recommended expected: 套件管理器會鎖定相依套件的精確版本。
- Recommended acceptable: 套件管理器會鎖定相依性的精確版本。, 套件管理工具會鎖定相依性的精確版本。, 包管理器會鎖定相依套件的精確版本。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.
- Maintainer action: confirm_recommendation_or_edit

### blind-it-0174

- Kind: difference
- Domain: it
- Risk: candidate_gap
- Input: 开发服务器会在文件变更后自动热重载。
- Codex expected: 開發伺服器會在檔案變更後自動熱重新載入。
- Gemini expected: 開發伺服器會在檔案變更後自動熱重載。
- Recommendation: codex
- Recommended expected: 開發伺服器會在檔案變更後自動熱重新載入。
- Recommended acceptable: 開發伺服器會在檔案變更後自動熱重載。, 開發伺服器會在檔案修改後自動熱重載。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.
- Maintainer action: confirm_recommendation_or_edit

### blind-it-0175

- Kind: difference
- Domain: it
- Risk: candidate_gap
- Input: 请把错误堆栈上传到观测平台。
- Codex expected: 請把錯誤堆疊上傳到可觀測性平台。
- Gemini expected: 請把錯誤堆疊上傳到觀測平台。
- Recommendation: codex
- Recommended expected: 請把錯誤堆疊上傳到可觀測性平台。
- Recommended acceptable: 請把錯誤堆疊上傳到觀測平台。, 請把錯誤堆疊上傳至觀測平台。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.
- Maintainer action: confirm_recommendation_or_edit

### blind-it-0176

- Kind: difference
- Domain: it
- Risk: candidate_gap
- Input: 灰度发布会先开放给内部账号。
- Codex expected: 漸進式發布會先開放給內部帳號。
- Gemini expected: 灰度發布會先開放給內部帳號。
- Recommendation: codex
- Recommended expected: 漸進式發布會先開放給內部帳號。
- Recommended acceptable: 灰度發布會先開放給內部帳號。, 金絲雀發布會先開放給內部帳號。, 灰度釋出會先開放給內部帳號。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.
- Maintainer action: confirm_recommendation_or_edit

### blind-it-0177

- Kind: difference
- Domain: it
- Risk: candidate_gap
- Input: 对象权限会继承存储桶的访问策略。
- Codex expected: 物件權限會繼承儲存桶的存取策略。
- Gemini expected: 物件權限會繼承儲存貯體的存取策略。
- Recommendation: codex
- Recommended expected: 物件權限會繼承儲存桶的存取策略。
- Recommended acceptable: 物件權限會繼承儲存貯體的存取策略。, 物件權限會繼承儲存桶的存取原則。, 物件權限會繼承儲存貯體的存取原則。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.
- Maintainer action: confirm_recommendation_or_edit

### blind-it-0181

- Kind: difference
- Domain: it
- Risk: baseline_guard
- Input: GitHub Actions 工作流名称 deploy-prod 必须保持一致。
- Codex expected: GitHub Actions 工作流程名稱 deploy-prod 必須保持一致。
- Gemini expected: GitHub Actions 工作流名稱 deploy-prod 必須保持一致。
- Recommendation: codex
- Recommended expected: GitHub Actions 工作流程名稱 deploy-prod 必須保持一致。
- Recommended acceptable: GitHub Actions 工作流名稱 deploy-prod 必須保持一致。
- Reason: Codex primary is already listed as a Gemini acceptable variant.
- Maintainer action: confirm_recommendation_or_edit

### blind-ui-0130

- Kind: difference
- Domain: ui
- Risk: candidate_gap
- Input: 上传头像前请先裁剪图片。
- Codex expected: 上傳頭像前請先裁切圖片。
- Gemini expected: 上傳大頭貼前請先裁切圖片。
- Recommendation: gemini
- Recommended expected: 上傳大頭貼前請先裁切圖片。
- Recommended acceptable: 上傳頭像前請先裁切圖片。
- Reason: Gemini primary is already listed as a Codex acceptable variant.
- Maintainer action: confirm_recommendation_or_edit

### blind-ui-0131

- Kind: difference
- Domain: ui
- Risk: candidate_gap
- Input: 筛选条件已保存到当前视图。
- Codex expected: 篩選條件已儲存到目前檢視。
- Gemini expected: 篩選條件已儲存至目前檢視。
- Recommendation: gemini
- Recommended expected: 篩選條件已儲存至目前檢視。
- Recommended acceptable: 篩選條件已儲存到目前檢視。
- Reason: Codex marked this as a variant-sensitive case and Gemini gave a high-confidence alternative.
- Maintainer action: confirm_recommendation_or_edit

### blind-ui-0132

- Kind: difference
- Domain: ui
- Risk: candidate_gap
- Input: 订阅到期时会显示续费提示。
- Codex expected: 訂閱到期時會顯示續費提示。
- Gemini expected: 訂閱到期時會顯示續訂提示。
- Recommendation: codex
- Recommended expected: 訂閱到期時會顯示續費提示。
- Recommended acceptable: 訂閱到期時會顯示續訂提示。
- Reason: Codex primary is already listed as a Gemini acceptable variant.
- Maintainer action: confirm_recommendation_or_edit

### blind-ui-0133

- Kind: difference
- Domain: ui
- Risk: candidate_gap
- Input: 表单提交失败，请检查必填字段。
- Codex expected: 表單送出失敗，請檢查必填欄位。
- Gemini expected: 表單提交失敗，請檢查必填欄位。
- Recommendation: codex
- Recommended expected: 表單送出失敗，請檢查必填欄位。
- Recommended acceptable: 表單提交失敗，請檢查必填欄位。
- Reason: Codex primary is already listed as a Gemini acceptable variant.
- Maintainer action: confirm_recommendation_or_edit

### blind-ui-0136

- Kind: difference
- Domain: ui
- Risk: candidate_gap
- Input: 对话框关闭前会保存草稿。
- Codex expected: 對話框關閉前會儲存草稿。
- Gemini expected: 對話方塊關閉前會儲存草稿。
- Recommendation: codex
- Recommended expected: 對話框關閉前會儲存草稿。
- Recommended acceptable: 對話方塊關閉前會儲存草稿。
- Reason: Codex primary is already listed as a Gemini acceptable variant.
- Maintainer action: confirm_recommendation_or_edit

### blind-ui-0137

- Kind: difference
- Domain: ui
- Risk: candidate_gap
- Input: 通知中心会按优先级排序。
- Codex expected: 通知中心會依優先順序排序。
- Gemini expected: 通知中心會按優先順序排序。
- Recommendation: codex
- Recommended expected: 通知中心會依優先順序排序。
- Recommended acceptable: 通知中心會按優先順序排序。, 通知中心會按優先級排序。, 通知中心會按優先權排序。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.
- Maintainer action: confirm_recommendation_or_edit

### blind-ui-0139

- Kind: difference
- Domain: ui
- Risk: candidate_gap
- Input: 搜索结果会突出显示匹配词。
- Codex expected: 搜尋結果會醒目顯示相符詞。
- Gemini expected: 搜尋結果會醒目提示相符字詞。
- Recommendation: gemini
- Recommended expected: 搜尋結果會醒目提示相符字詞。
- Recommended acceptable: 搜尋結果會醒目顯示相符詞。, 搜尋結果會突出顯示符合的詞。
- Reason: Codex marked this as a variant-sensitive case and Gemini gave a high-confidence alternative.
- Maintainer action: confirm_recommendation_or_edit

### blind-llm-0096

- Kind: difference
- Domain: llm
- Risk: candidate_gap
- Input: 代理会在调用工具前说明计划。
- Codex expected: 代理程式會在呼叫工具前說明計畫。
- Gemini expected: 代理會在呼叫工具前說明計畫。
- Recommendation: gemini
- Recommended expected: 代理會在呼叫工具前說明計畫。
- Recommended acceptable: 代理程式會在呼叫工具前說明計畫。
- Reason: Gemini primary is already listed as a Codex acceptable variant.
- Maintainer action: confirm_recommendation_or_edit

### blind-llm-0098

- Kind: difference
- Domain: llm
- Risk: candidate_gap
- Input: 向量数据库会返回最相近的文档块。
- Codex expected: 向量資料庫會回傳最相近的文件區塊。
- Gemini expected: 向量資料庫會傳回最相近的文件區塊。
- Recommendation: codex
- Recommended expected: 向量資料庫會回傳最相近的文件區塊。
- Recommended acceptable: 向量資料庫會傳回最相近的文件區塊。, 向量資料庫會返回最相近的文件區塊。, 向量資料庫會傳回最相近的檔案區塊。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.
- Maintainer action: confirm_recommendation_or_edit

### blind-llm-0099

- Kind: difference
- Domain: llm
- Risk: candidate_gap
- Input: 评估脚本会比较回答的一致性。
- Codex expected: 評估指令碼會比較回答的一致性。
- Gemini expected: 評估腳本會比較回答的一致性。
- Recommendation: codex
- Recommended expected: 評估指令碼會比較回答的一致性。
- Recommended acceptable: 評估腳本會比較回答的一致性。, 評估腳本會比較回覆的一致性。
- Reason: Codex primary is already listed as a Gemini acceptable variant.
- Maintainer action: confirm_recommendation_or_edit

### blind-llm-0100

- Kind: difference
- Domain: llm
- Risk: candidate_gap
- Input: 请限制模型输出为三条要点。
- Codex expected: 請限制模型輸出為三個重點。
- Gemini expected: 請限制模型輸出為三條要點。
- Recommendation: codex
- Recommended expected: 請限制模型輸出為三個重點。
- Recommended acceptable: 請限制模型輸出為三條要點。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.
- Maintainer action: confirm_recommendation_or_edit

### blind-llm-0101

- Kind: difference
- Domain: llm
- Risk: candidate_gap
- Input: 聊天机器人需要识别用户意图。
- Codex expected: 聊天機器人需要辨識使用者意圖。
- Gemini expected: 聊天機器人需要識別使用者意圖。
- Recommendation: codex
- Recommended expected: 聊天機器人需要辨識使用者意圖。
- Recommended acceptable: 聊天機器人需要識別使用者意圖。, 聊天機器人需要識別用戶意圖。
- Reason: Codex primary is already listed as a Gemini acceptable variant.
- Maintainer action: confirm_recommendation_or_edit

### blind-formal-0102

- Kind: difference
- Domain: formal
- Risk: candidate_gap
- Input: 新闻稿须避免使用未经证实的数据。
- Codex expected: 新聞稿須避免使用未經證實的資料。
- Gemini expected: 新聞稿須避免使用未經證實的數據。
- Recommendation: codex
- Recommended expected: 新聞稿須避免使用未經證實的資料。
- Recommended acceptable: 新聞稿須避免使用未經證實的數據。
- Reason: Codex primary is already listed as a Gemini acceptable variant.
- Maintainer action: confirm_recommendation_or_edit

### blind-social-0099

- Kind: difference
- Domain: social
- Risk: candidate_gap
- Input: 可以帮我确认外送到了没？
- Codex expected: 可以幫我確認外送到了沒？
- Gemini expected: 擺脫 OpenCC 改寫，可以幫我確認外送到了沒？
- Recommendation: codex
- Recommended expected: 可以幫我確認外送到了沒？
- Recommended acceptable:
- Reason: Gemini output appears contaminated by unrelated text; prefer Codex and require maintainer review.
- Maintainer action: confirm_recommendation_or_edit

### blind-it-0164

- Kind: policy_review
- Domain: it
- Risk: candidate_gap
- Input: 构建流水线会在单元测试失败时停止部署。
- Codex expected: 建置管線會在單元測試失敗時停止部署。
- Gemini expected: 建置管線會在單元測試失敗時停止部署。
- Recommendation: exact_match_policy_review
- Recommended expected: 建置管線會在單元測試失敗時停止部署。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-it-0168

- Kind: policy_review
- Domain: it
- Risk: candidate_gap
- Input: 异步任务完成后会写入审计事件。
- Codex expected: 非同步任務完成後會寫入稽核事件。
- Gemini expected: 非同步任務完成後會寫入稽核事件。
- Recommendation: exact_match_policy_review
- Recommended expected: 非同步任務完成後會寫入稽核事件。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-it-0182

- Kind: policy_review
- Domain: it
- Risk: over_conversion_guard
- Input: 這段 TypeScript 註解已是繁體，請保持原樣。
- Codex expected: 這段 TypeScript 註解已是繁體，請保持原樣。
- Gemini expected: 這段 TypeScript 註解已是繁體，請保持原樣。
- Recommendation: exact_match_policy_review
- Recommended expected: 這段 TypeScript 註解已是繁體，請保持原樣。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex confidence medium, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-it-0183

- Kind: policy_review
- Domain: it
- Risk: over_conversion_guard
- Input: 伺服器憑證更新說明已核准，請勿改寫。
- Codex expected: 伺服器憑證更新說明已核准，請勿改寫。
- Gemini expected: 伺服器憑證更新說明已核准，請勿改寫。
- Recommendation: exact_match_policy_review
- Recommended expected: 伺服器憑證更新說明已核准，請勿改寫。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-it-0184

- Kind: policy_review
- Domain: it
- Risk: over_conversion_guard
- Input: 用戶端快取設定中的繁體文字不要再轉換。
- Codex expected: 用戶端快取設定中的繁體文字不要再轉換。
- Gemini expected: 用戶端快取設定中的繁體文字不要再轉換。
- Recommendation: exact_match_policy_review
- Recommended expected: 用戶端快取設定中的繁體文字不要再轉換。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-it-0185

- Kind: policy_review
- Domain: it
- Risk: over_conversion_guard
- Input: 這份 API 文件保留「回應」這個用字。
- Codex expected: 這份 API 文件保留「回應」這個用字。
- Gemini expected: 這份 API 文件保留「回應」這個用字。
- Recommendation: exact_match_policy_review
- Recommended expected: 這份 API 文件保留「回應」這個用字。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-it-0186

- Kind: policy_review
- Domain: it
- Risk: over_conversion_guard
- Input: 請不要改動已校對的佇列監控訊息。
- Codex expected: 請不要改動已校對的佇列監控訊息。
- Gemini expected: 請不要改動已校對的佇列監控訊息。
- Recommendation: exact_match_policy_review
- Recommended expected: 請不要改動已校對的佇列監控訊息。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-it-0187

- Kind: policy_review
- Domain: it
- Risk: over_conversion_guard
- Input: 繁體錯誤提示「連線逾時」應保持不變。
- Codex expected: 繁體錯誤提示「連線逾時」應保持不變。
- Gemini expected: 繁體錯誤提示「連線逾時」應保持不變。
- Recommendation: exact_match_policy_review
- Recommended expected: 繁體錯誤提示「連線逾時」應保持不變。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-ui-0138

- Kind: policy_review
- Domain: ui
- Risk: candidate_gap
- Input: 请在侧边栏固定常用项目。
- Codex expected: 請在側邊欄釘選常用項目。
- Gemini expected: 請在側邊欄釘選常用項目。
- Recommendation: exact_match_policy_review
- Recommended expected: 請在側邊欄釘選常用項目。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-ui-0143

- Kind: policy_review
- Domain: ui
- Risk: over_conversion_guard
- Input: 這個設定頁已是繁體，請勿修改。
- Codex expected: 這個設定頁已是繁體，請勿修改。
- Gemini expected: 這個設定頁已是繁體，請勿修改。
- Recommendation: exact_match_policy_review
- Recommended expected: 這個設定頁已是繁體，請勿修改。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-ui-0144

- Kind: policy_review
- Domain: ui
- Risk: over_conversion_guard
- Input: 付款按鈕上的「下一步」不要改寫。
- Codex expected: 付款按鈕上的「下一步」不要改寫。
- Gemini expected: 付款按鈕上的「下一步」不要改寫。
- Recommendation: exact_match_policy_review
- Recommended expected: 付款按鈕上的「下一步」不要改寫。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-ui-0145

- Kind: policy_review
- Domain: ui
- Risk: over_conversion_guard
- Input: 繁體錯誤訊息已完成審核，請保留。
- Codex expected: 繁體錯誤訊息已完成審核，請保留。
- Gemini expected: 繁體錯誤訊息已完成審核，請保留。
- Recommendation: exact_match_policy_review
- Recommended expected: 繁體錯誤訊息已完成審核，請保留。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex confidence medium, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-ui-0146

- Kind: policy_review
- Domain: ui
- Risk: over_conversion_guard
- Input: 使用者選單中的繁體項目維持原樣。
- Codex expected: 使用者選單中的繁體項目維持原樣。
- Gemini expected: 使用者選單中的繁體項目維持原樣。
- Recommendation: exact_match_policy_review
- Recommended expected: 使用者選單中的繁體項目維持原樣。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-ui-0147

- Kind: policy_review
- Domain: ui
- Risk: over_conversion_guard
- Input: 請不要轉換已核准的客服視窗文案。
- Codex expected: 請不要轉換已核准的客服視窗文案。
- Gemini expected: 請不要轉換已核准的客服視窗文案。
- Recommendation: exact_match_policy_review
- Recommended expected: 請不要轉換已核准的客服視窗文案。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-llm-0094

- Kind: policy_review
- Domain: llm
- Risk: candidate_gap
- Input: 请把检索到的片段附在答案后面。
- Codex expected: 請把檢索到的片段附在答案後面。
- Gemini expected: 請把檢索到的片段附在答案後面。
- Recommendation: exact_match_policy_review
- Recommended expected: 請把檢索到的片段附在答案後面。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-llm-0097

- Kind: policy_review
- Domain: llm
- Risk: candidate_gap
- Input: 提示词模板需要保留变量占位符。
- Codex expected: 提示詞範本需要保留變數預留位置。
- Gemini expected: 提示詞範本需要保留變數預留位置。
- Recommendation: exact_match_policy_review
- Recommended expected: 提示詞範本需要保留變數預留位置。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-llm-0104

- Kind: policy_review
- Domain: llm
- Risk: over_conversion_guard
- Input: 這段繁體提示詞已經過審核。
- Codex expected: 這段繁體提示詞已經過審核。
- Gemini expected: 這段繁體提示詞已經過審核。
- Recommendation: exact_match_policy_review
- Recommended expected: 這段繁體提示詞已經過審核。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-llm-0105

- Kind: policy_review
- Domain: llm
- Risk: over_conversion_guard
- Input: 請保留「使用者意圖」這個繁體用語。
- Codex expected: 請保留「使用者意圖」這個繁體用語。
- Gemini expected: 請保留「使用者意圖」這個繁體用語。
- Recommendation: exact_match_policy_review
- Recommended expected: 請保留「使用者意圖」這個繁體用語。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-llm-0106

- Kind: policy_review
- Domain: llm
- Risk: over_conversion_guard
- Input: 繁體摘要範本不要被自動改寫。
- Codex expected: 繁體摘要範本不要被自動改寫。
- Gemini expected: 繁體摘要範本不要被自動改寫。
- Recommendation: exact_match_policy_review
- Recommended expected: 繁體摘要範本不要被自動改寫。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-llm-0107

- Kind: policy_review
- Domain: llm
- Risk: over_conversion_guard
- Input: 這份工具說明已是繁體，請勿轉換。
- Codex expected: 這份工具說明已是繁體，請勿轉換。
- Gemini expected: 這份工具說明已是繁體，請勿轉換。
- Recommendation: exact_match_policy_review
- Recommended expected: 這份工具說明已是繁體，請勿轉換。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-formal-0097

- Kind: policy_review
- Domain: formal
- Risk: candidate_gap
- Input: 本公司将根据合约条款办理退款。
- Codex expected: 本公司將根據合約條款辦理退款。
- Gemini expected: 本公司將根據合約條款辦理退款。
- Recommendation: exact_match_policy_review
- Recommended expected: 本公司將根據合約條款辦理退款。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-formal-0101

- Kind: policy_review
- Domain: formal
- Risk: candidate_gap
- Input: 申请人应检附身份证明文件。
- Codex expected: 申請人應檢附身分證明文件。
- Gemini expected: 申請人應檢附身分證明文件。
- Recommendation: exact_match_policy_review
- Recommended expected: 申請人應檢附身分證明文件。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-formal-0105

- Kind: policy_review
- Domain: formal
- Risk: over_conversion_guard
- Input: 本繁體公告已核定，請勿改寫。
- Codex expected: 本繁體公告已核定，請勿改寫。
- Gemini expected: 本繁體公告已核定，請勿改寫。
- Recommendation: exact_match_policy_review
- Recommended expected: 本繁體公告已核定，請勿改寫。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-formal-0106

- Kind: policy_review
- Domain: formal
- Risk: over_conversion_guard
- Input: 合約中的繁體條款應保持原樣。
- Codex expected: 合約中的繁體條款應保持原樣。
- Gemini expected: 合約中的繁體條款應保持原樣。
- Recommendation: exact_match_policy_review
- Recommended expected: 合約中的繁體條款應保持原樣。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-formal-0107

- Kind: policy_review
- Domain: formal
- Risk: over_conversion_guard
- Input: 請保留「品質管理」這個正式用語。
- Codex expected: 請保留「品質管理」這個正式用語。
- Gemini expected: 請保留「品質管理」這個正式用語。
- Recommendation: exact_match_policy_review
- Recommended expected: 請保留「品質管理」這個正式用語。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-formal-0108

- Kind: policy_review
- Domain: formal
- Risk: over_conversion_guard
- Input: 已發布的繁體新聞標題不應再轉換。
- Codex expected: 已發布的繁體新聞標題不應再轉換。
- Gemini expected: 已發布的繁體新聞標題不應再轉換。
- Recommendation: exact_match_policy_review
- Recommended expected: 已發布的繁體新聞標題不應再轉換。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-social-0094

- Kind: policy_review
- Domain: social
- Risk: candidate_gap
- Input: 这个周末想找朋友一起吃早午餐。
- Codex expected: 這個週末想找朋友一起吃早午餐。
- Gemini expected: 這個週末想找朋友一起吃早午餐。
- Recommendation: exact_match_policy_review
- Recommended expected: 這個週末想找朋友一起吃早午餐。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-social-0095

- Kind: policy_review
- Domain: social
- Risk: candidate_gap
- Input: 请帮我把地址发到群组里。
- Codex expected: 請幫我把地址傳到群組裡。
- Gemini expected: 請幫我把地址傳到群組裡。
- Recommendation: exact_match_policy_review
- Recommended expected: 請幫我把地址傳到群組裡。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-social-0105

- Kind: policy_review
- Domain: social
- Risk: over_conversion_guard
- Input: 這則繁體留言已經確認，請勿改寫。
- Codex expected: 這則繁體留言已經確認，請勿改寫。
- Gemini expected: 這則繁體留言已經確認，請勿改寫。
- Recommendation: exact_match_policy_review
- Recommended expected: 這則繁體留言已經確認，請勿改寫。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex confidence medium, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-social-0106

- Kind: policy_review
- Domain: social
- Risk: over_conversion_guard
- Input: 我想保留「週末」這個寫法。
- Codex expected: 我想保留「週末」這個寫法。
- Gemini expected: 我想保留「週末」這個寫法。
- Recommendation: exact_match_policy_review
- Recommended expected: 我想保留「週末」這個寫法。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-social-0107

- Kind: policy_review
- Domain: social
- Risk: over_conversion_guard
- Input: 繁體社團公告不要自動轉換。
- Codex expected: 繁體社團公告不要自動轉換。
- Gemini expected: 繁體社團公告不要自動轉換。
- Recommendation: exact_match_policy_review
- Recommended expected: 繁體社團公告不要自動轉換。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-social-0108

- Kind: policy_review
- Domain: social
- Risk: over_conversion_guard
- Input: 這段聊天紀錄已是繁體，請保持原樣。
- Codex expected: 這段聊天紀錄已是繁體，請保持原樣。
- Gemini expected: 這段聊天紀錄已是繁體，請保持原樣。
- Recommendation: exact_match_policy_review
- Recommended expected: 這段聊天紀錄已是繁體，請保持原樣。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-high-risk-0061

- Kind: policy_review
- Domain: high_risk
- Risk: candidate_gap
- Input: 医师会评估过敏史后调整处方。
- Codex expected: 醫師會評估過敏史後調整處方。
- Gemini expected: 醫師會評估過敏史後調整處方。
- Recommendation: exact_match_policy_review
- Recommended expected: 醫師會評估過敏史後調整處方。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: high-risk domain, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-high-risk-0062

- Kind: policy_review
- Domain: high_risk
- Risk: candidate_gap
- Input: 银行应确认汇款账户的实名资料。
- Codex expected: 銀行應確認匯款帳戶的實名資料。
- Gemini expected: 銀行應確認匯款帳戶的實名資料。
- Recommendation: exact_match_policy_review
- Recommended expected: 銀行應確認匯款帳戶的實名資料。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: high-risk domain, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-high-risk-0063

- Kind: policy_review
- Domain: high_risk
- Risk: candidate_gap
- Input: 保险公司须说明除外责任范围。
- Codex expected: 保險公司須說明除外責任範圍。
- Gemini expected: 保險公司須說明除外責任範圍。
- Recommendation: exact_match_policy_review
- Recommended expected: 保險公司須說明除外責任範圍。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: high-risk domain, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-high-risk-0064

- Kind: policy_review
- Domain: high_risk
- Risk: candidate_gap
- Input: 法院可依申请核发支付命令。
- Codex expected: 法院可依申請核發支付命令。
- Gemini expected: 法院可依申請核發支付命令。
- Recommendation: exact_match_policy_review
- Recommended expected: 法院可依申請核發支付命令。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: high-risk domain, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-high-risk-0065

- Kind: policy_review
- Domain: high_risk
- Risk: candidate_gap
- Input: 投资人应阅读公开说明书后再决定。
- Codex expected: 投資人應閱讀公開說明書後再決定。
- Gemini expected: 投資人應閱讀公開說明書後再決定。
- Recommendation: exact_match_policy_review
- Recommended expected: 投資人應閱讀公開說明書後再決定。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: high-risk domain, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-high-risk-0066

- Kind: policy_review
- Domain: high_risk
- Risk: candidate_gap
- Input: 药袋标签应载明服用频率。
- Codex expected: 藥袋標籤應載明服用頻率。
- Gemini expected: 藥袋標籤應載明服用頻率。
- Recommendation: exact_match_policy_review
- Recommended expected: 藥袋標籤應載明服用頻率。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: high-risk domain, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-high-risk-0067

- Kind: policy_review
- Domain: high_risk
- Risk: baseline_guard
- Input: 病历号 MED-TW-2026-11 不应被改写。
- Codex expected: 病歷號 MED-TW-2026-11 不應被改寫。
- Gemini expected: 病歷號 MED-TW-2026-11 不應被改寫。
- Recommendation: exact_match_policy_review
- Recommended expected: 病歷號 MED-TW-2026-11 不應被改寫。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: high-risk domain, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-high-risk-0068

- Kind: policy_review
- Domain: high_risk
- Risk: baseline_guard
- Input: 请保留金融机构代码 812。
- Codex expected: 請保留金融機構代碼 812。
- Gemini expected: 請保留金融機構代碼 812。
- Recommendation: exact_match_policy_review
- Recommended expected: 請保留金融機構代碼 812。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: high-risk domain, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-high-risk-0069

- Kind: policy_review
- Domain: high_risk
- Risk: over_conversion_guard
- Input: 這份繁體醫囑已由醫師確認。
- Codex expected: 這份繁體醫囑已由醫師確認。
- Gemini expected: 這份繁體醫囑已由醫師確認。
- Recommendation: exact_match_policy_review
- Recommended expected: 這份繁體醫囑已由醫師確認。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: high-risk domain, over-conversion guard, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

### blind-high-risk-0070

- Kind: policy_review
- Domain: high_risk
- Risk: over_conversion_guard
- Input: 契約中的繁體免責條款請保持原樣。
- Codex expected: 契約中的繁體免責條款請保持原樣。
- Gemini expected: 契約中的繁體免責條款請保持原樣。
- Recommendation: exact_match_policy_review
- Recommended expected: 契約中的繁體免責條款請保持原樣。
- Recommended acceptable: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: high-risk domain, over-conversion guard, Codex review-needed policy guard.
- Maintainer action: confirm_recommendation_or_edit

## No Immediate Question

- `blind-it-0165`
- `blind-it-0170`
- `blind-it-0171`
- `blind-it-0172`
- `blind-it-0178`
- `blind-it-0179`
- `blind-it-0180`
- `blind-ui-0128`
- `blind-ui-0129`
- `blind-ui-0134`
- `blind-ui-0135`
- `blind-ui-0140`
- `blind-ui-0141`
- `blind-ui-0142`
- `blind-llm-0093`
- `blind-llm-0095`
- `blind-llm-0102`
- `blind-llm-0103`
- `blind-formal-0094`
- `blind-formal-0095`
- `blind-formal-0096`
- `blind-formal-0098`
- `blind-formal-0099`
- `blind-formal-0100`
- `blind-formal-0103`
- `blind-formal-0104`
- `blind-social-0096`
- `blind-social-0097`
- `blind-social-0098`
- `blind-social-0100`
- `blind-social-0101`
- `blind-social-0102`
- `blind-social-0103`
- `blind-social-0104`
