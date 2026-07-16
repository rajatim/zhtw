<!-- zhtw:disable -->
# Holdout Codex/Gemini Diff Review - blind-v1 batch8 100 cases

Generated: 2026-07-10

This report is advisory only. It is not ground truth and does not use converter outputs.

## Summary

- total_cases: 100
- exact_matches: 76
- differences: 24
- exact_but_policy_review: 42
- no_immediate_question: 34
- maintainer_queue_total: 66
- difference_recommendations: {"codex": 17, "gemini": 7}
- by_policy_reason: {"Codex confidence medium": 20, "Codex review-needed policy guard": 50, "high-risk domain": 10, "over-conversion guard": 25}
- promotion_allowed: False

## Differences

### blind-it-0163

- Domain: it
- Risk: candidate_gap
- Input: 请把接口响应中的分页游标写入下一页链接。
- Codex expected: 請把介面回應中的分頁游標寫入下一頁連結。
- Gemini expected: 請把 API 回應中的分頁游標寫入下一頁連結。
- Recommendation: gemini
- Recommended expected: 請把 API 回應中的分頁游標寫入下一頁連結。
- Recommended acceptable: 請把介面回應中的分頁游標寫入下一頁連結。
- Reason: Gemini primary is already listed as a Codex acceptable variant.

### blind-it-0166

- Domain: it
- Risk: candidate_gap
- Input: 请在缓存键里加入租户标识避免串数据。
- Codex expected: 請在快取鍵裡加入租用戶識別碼，避免資料混淆。
- Gemini expected: 請在快取鍵裡加入租戶識別避免串資料。
- Recommendation: gemini
- Recommended expected: 請在快取鍵裡加入租戶識別避免串資料。
- Recommended acceptable: 請在快取鍵裡加入租用戶識別碼，避免資料混淆。, 請在快取鍵裡加入租戶識別碼，避免資料混淆。
- Reason: Codex marked this as a variant-sensitive case and Gemini gave a high-confidence alternative.

### blind-it-0167

- Domain: it
- Risk: candidate_gap
- Input: 日志采样率可以按服务名称单独设置。
- Codex expected: 日誌取樣率可以依服務名稱個別設定。
- Gemini expected: 日誌採樣率可以按服務名稱單獨設定。
- Recommendation: codex
- Recommended expected: 日誌取樣率可以依服務名稱個別設定。
- Recommended acceptable: 日誌採樣率可以按服務名稱單獨設定。, Log 採樣率可以按服務名稱單獨設定。, 日誌抽樣率可以按服務名稱單獨設定。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.

### blind-it-0169

- Domain: it
- Risk: candidate_gap
- Input: 数据库迁移脚本需要支持回滚。
- Codex expected: 資料庫遷移指令碼需要支援復原。
- Gemini expected: 資料庫遷移腳本需要支援回滾。
- Recommendation: gemini
- Recommended expected: 資料庫遷移腳本需要支援回滾。
- Recommended acceptable: 資料庫遷移指令碼需要支援復原。
- Reason: Gemini primary is already listed as a Codex acceptable variant.

### blind-it-0173

- Domain: it
- Risk: candidate_gap
- Input: 包管理器会锁定依赖的精确版本。
- Codex expected: 套件管理器會鎖定相依套件的精確版本。
- Gemini expected: 套件管理器會鎖定相依性的精確版本。
- Recommendation: codex
- Recommended expected: 套件管理器會鎖定相依套件的精確版本。
- Recommended acceptable: 套件管理器會鎖定相依性的精確版本。, 套件管理工具會鎖定相依性的精確版本。, 包管理器會鎖定相依套件的精確版本。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.

### blind-it-0174

- Domain: it
- Risk: candidate_gap
- Input: 开发服务器会在文件变更后自动热重载。
- Codex expected: 開發伺服器會在檔案變更後自動熱重新載入。
- Gemini expected: 開發伺服器會在檔案變更後自動熱重載。
- Recommendation: codex
- Recommended expected: 開發伺服器會在檔案變更後自動熱重新載入。
- Recommended acceptable: 開發伺服器會在檔案變更後自動熱重載。, 開發伺服器會在檔案修改後自動熱重載。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.

### blind-it-0175

- Domain: it
- Risk: candidate_gap
- Input: 请把错误堆栈上传到观测平台。
- Codex expected: 請把錯誤堆疊上傳到可觀測性平台。
- Gemini expected: 請把錯誤堆疊上傳到觀測平台。
- Recommendation: codex
- Recommended expected: 請把錯誤堆疊上傳到可觀測性平台。
- Recommended acceptable: 請把錯誤堆疊上傳到觀測平台。, 請把錯誤堆疊上傳至觀測平台。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.

### blind-it-0176

- Domain: it
- Risk: candidate_gap
- Input: 灰度发布会先开放给内部账号。
- Codex expected: 漸進式發布會先開放給內部帳號。
- Gemini expected: 灰度發布會先開放給內部帳號。
- Recommendation: codex
- Recommended expected: 漸進式發布會先開放給內部帳號。
- Recommended acceptable: 灰度發布會先開放給內部帳號。, 金絲雀發布會先開放給內部帳號。, 灰度釋出會先開放給內部帳號。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.

### blind-it-0177

- Domain: it
- Risk: candidate_gap
- Input: 对象权限会继承存储桶的访问策略。
- Codex expected: 物件權限會繼承儲存桶的存取策略。
- Gemini expected: 物件權限會繼承儲存貯體的存取策略。
- Recommendation: codex
- Recommended expected: 物件權限會繼承儲存桶的存取策略。
- Recommended acceptable: 物件權限會繼承儲存貯體的存取策略。, 物件權限會繼承儲存桶的存取原則。, 物件權限會繼承儲存貯體的存取原則。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.

### blind-it-0181

- Domain: it
- Risk: baseline_guard
- Input: GitHub Actions 工作流名称 deploy-prod 必须保持一致。
- Codex expected: GitHub Actions 工作流程名稱 deploy-prod 必須保持一致。
- Gemini expected: GitHub Actions 工作流名稱 deploy-prod 必須保持一致。
- Recommendation: codex
- Recommended expected: GitHub Actions 工作流程名稱 deploy-prod 必須保持一致。
- Recommended acceptable: GitHub Actions 工作流名稱 deploy-prod 必須保持一致。
- Reason: Codex primary is already listed as a Gemini acceptable variant.

### blind-ui-0130

- Domain: ui
- Risk: candidate_gap
- Input: 上传头像前请先裁剪图片。
- Codex expected: 上傳頭像前請先裁切圖片。
- Gemini expected: 上傳大頭貼前請先裁切圖片。
- Recommendation: gemini
- Recommended expected: 上傳大頭貼前請先裁切圖片。
- Recommended acceptable: 上傳頭像前請先裁切圖片。
- Reason: Gemini primary is already listed as a Codex acceptable variant.

### blind-ui-0131

- Domain: ui
- Risk: candidate_gap
- Input: 筛选条件已保存到当前视图。
- Codex expected: 篩選條件已儲存到目前檢視。
- Gemini expected: 篩選條件已儲存至目前檢視。
- Recommendation: gemini
- Recommended expected: 篩選條件已儲存至目前檢視。
- Recommended acceptable: 篩選條件已儲存到目前檢視。
- Reason: Codex marked this as a variant-sensitive case and Gemini gave a high-confidence alternative.

### blind-ui-0132

- Domain: ui
- Risk: candidate_gap
- Input: 订阅到期时会显示续费提示。
- Codex expected: 訂閱到期時會顯示續費提示。
- Gemini expected: 訂閱到期時會顯示續訂提示。
- Recommendation: codex
- Recommended expected: 訂閱到期時會顯示續費提示。
- Recommended acceptable: 訂閱到期時會顯示續訂提示。
- Reason: Codex primary is already listed as a Gemini acceptable variant.

### blind-ui-0133

- Domain: ui
- Risk: candidate_gap
- Input: 表单提交失败，请检查必填字段。
- Codex expected: 表單送出失敗，請檢查必填欄位。
- Gemini expected: 表單提交失敗，請檢查必填欄位。
- Recommendation: codex
- Recommended expected: 表單送出失敗，請檢查必填欄位。
- Recommended acceptable: 表單提交失敗，請檢查必填欄位。
- Reason: Codex primary is already listed as a Gemini acceptable variant.

### blind-ui-0136

- Domain: ui
- Risk: candidate_gap
- Input: 对话框关闭前会保存草稿。
- Codex expected: 對話框關閉前會儲存草稿。
- Gemini expected: 對話方塊關閉前會儲存草稿。
- Recommendation: codex
- Recommended expected: 對話框關閉前會儲存草稿。
- Recommended acceptable: 對話方塊關閉前會儲存草稿。
- Reason: Codex primary is already listed as a Gemini acceptable variant.

### blind-ui-0137

- Domain: ui
- Risk: candidate_gap
- Input: 通知中心会按优先级排序。
- Codex expected: 通知中心會依優先順序排序。
- Gemini expected: 通知中心會按優先順序排序。
- Recommendation: codex
- Recommended expected: 通知中心會依優先順序排序。
- Recommended acceptable: 通知中心會按優先順序排序。, 通知中心會按優先級排序。, 通知中心會按優先權排序。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.

### blind-ui-0139

- Domain: ui
- Risk: candidate_gap
- Input: 搜索结果会突出显示匹配词。
- Codex expected: 搜尋結果會醒目顯示相符詞。
- Gemini expected: 搜尋結果會醒目提示相符字詞。
- Recommendation: gemini
- Recommended expected: 搜尋結果會醒目提示相符字詞。
- Recommended acceptable: 搜尋結果會醒目顯示相符詞。, 搜尋結果會突出顯示符合的詞。
- Reason: Codex marked this as a variant-sensitive case and Gemini gave a high-confidence alternative.

### blind-llm-0096

- Domain: llm
- Risk: candidate_gap
- Input: 代理会在调用工具前说明计划。
- Codex expected: 代理程式會在呼叫工具前說明計畫。
- Gemini expected: 代理會在呼叫工具前說明計畫。
- Recommendation: gemini
- Recommended expected: 代理會在呼叫工具前說明計畫。
- Recommended acceptable: 代理程式會在呼叫工具前說明計畫。
- Reason: Gemini primary is already listed as a Codex acceptable variant.

### blind-llm-0098

- Domain: llm
- Risk: candidate_gap
- Input: 向量数据库会返回最相近的文档块。
- Codex expected: 向量資料庫會回傳最相近的文件區塊。
- Gemini expected: 向量資料庫會傳回最相近的文件區塊。
- Recommendation: codex
- Recommended expected: 向量資料庫會回傳最相近的文件區塊。
- Recommended acceptable: 向量資料庫會傳回最相近的文件區塊。, 向量資料庫會返回最相近的文件區塊。, 向量資料庫會傳回最相近的檔案區塊。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.

### blind-llm-0099

- Domain: llm
- Risk: candidate_gap
- Input: 评估脚本会比较回答的一致性。
- Codex expected: 評估指令碼會比較回答的一致性。
- Gemini expected: 評估腳本會比較回答的一致性。
- Recommendation: codex
- Recommended expected: 評估指令碼會比較回答的一致性。
- Recommended acceptable: 評估腳本會比較回答的一致性。, 評估腳本會比較回覆的一致性。
- Reason: Codex primary is already listed as a Gemini acceptable variant.

### blind-llm-0100

- Domain: llm
- Risk: candidate_gap
- Input: 请限制模型输出为三条要点。
- Codex expected: 請限制模型輸出為三個重點。
- Gemini expected: 請限制模型輸出為三條要點。
- Recommendation: codex
- Recommended expected: 請限制模型輸出為三個重點。
- Recommended acceptable: 請限制模型輸出為三條要點。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.

### blind-llm-0101

- Domain: llm
- Risk: candidate_gap
- Input: 聊天机器人需要识别用户意图。
- Codex expected: 聊天機器人需要辨識使用者意圖。
- Gemini expected: 聊天機器人需要識別使用者意圖。
- Recommendation: codex
- Recommended expected: 聊天機器人需要辨識使用者意圖。
- Recommended acceptable: 聊天機器人需要識別使用者意圖。, 聊天機器人需要識別用戶意圖。
- Reason: Codex primary is already listed as a Gemini acceptable variant.

### blind-formal-0102

- Domain: formal
- Risk: candidate_gap
- Input: 新闻稿须避免使用未经证实的数据。
- Codex expected: 新聞稿須避免使用未經證實的資料。
- Gemini expected: 新聞稿須避免使用未經證實的數據。
- Recommendation: codex
- Recommended expected: 新聞稿須避免使用未經證實的資料。
- Recommended acceptable: 新聞稿須避免使用未經證實的數據。
- Reason: Codex primary is already listed as a Gemini acceptable variant.

### blind-social-0099

- Domain: social
- Risk: candidate_gap
- Input: 可以帮我确认外送到了没？
- Codex expected: 可以幫我確認外送到了沒？
- Gemini expected: 擺脫 OpenCC 改寫，可以幫我確認外送到了沒？
- Recommendation: codex
- Recommended expected: 可以幫我確認外送到了沒？
- Recommended acceptable:
- Reason: Gemini output appears contaminated by unrelated text; prefer Codex and require maintainer review.

## Exact But Policy Review

- `blind-it-0164` (it, candidate_gap): Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard.
- `blind-it-0168` (it, candidate_gap): Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard.
- `blind-it-0182` (it, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex confidence medium, Codex review-needed policy guard.
- `blind-it-0183` (it, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- `blind-it-0184` (it, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- `blind-it-0185` (it, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- `blind-it-0186` (it, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- `blind-it-0187` (it, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- `blind-ui-0138` (ui, candidate_gap): Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard.
- `blind-ui-0143` (ui, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- `blind-ui-0144` (ui, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- `blind-ui-0145` (ui, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex confidence medium, Codex review-needed policy guard.
- `blind-ui-0146` (ui, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- `blind-ui-0147` (ui, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- `blind-llm-0094` (llm, candidate_gap): Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard.
- `blind-llm-0097` (llm, candidate_gap): Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard.
- `blind-llm-0104` (llm, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- `blind-llm-0105` (llm, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- `blind-llm-0106` (llm, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- `blind-llm-0107` (llm, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- `blind-formal-0097` (formal, candidate_gap): Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard.
- `blind-formal-0101` (formal, candidate_gap): Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard.
- `blind-formal-0105` (formal, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- `blind-formal-0106` (formal, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- `blind-formal-0107` (formal, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- `blind-formal-0108` (formal, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- `blind-social-0094` (social, candidate_gap): Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard.
- `blind-social-0095` (social, candidate_gap): Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard.
- `blind-social-0105` (social, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex confidence medium, Codex review-needed policy guard.
- `blind-social-0106` (social, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- `blind-social-0107` (social, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- `blind-social-0108` (social, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: over-conversion guard, Codex review-needed policy guard.
- `blind-high-risk-0061` (high_risk, candidate_gap): Exact match, but policy requires maintainer confirmation because: high-risk domain, Codex review-needed policy guard.
- `blind-high-risk-0062` (high_risk, candidate_gap): Exact match, but policy requires maintainer confirmation because: high-risk domain, Codex review-needed policy guard.
- `blind-high-risk-0063` (high_risk, candidate_gap): Exact match, but policy requires maintainer confirmation because: high-risk domain, Codex review-needed policy guard.
- `blind-high-risk-0064` (high_risk, candidate_gap): Exact match, but policy requires maintainer confirmation because: high-risk domain, Codex review-needed policy guard.
- `blind-high-risk-0065` (high_risk, candidate_gap): Exact match, but policy requires maintainer confirmation because: high-risk domain, Codex review-needed policy guard.
- `blind-high-risk-0066` (high_risk, candidate_gap): Exact match, but policy requires maintainer confirmation because: high-risk domain, Codex review-needed policy guard.
- `blind-high-risk-0067` (high_risk, baseline_guard): Exact match, but policy requires maintainer confirmation because: high-risk domain, Codex review-needed policy guard.
- `blind-high-risk-0068` (high_risk, baseline_guard): Exact match, but policy requires maintainer confirmation because: high-risk domain, Codex review-needed policy guard.
- `blind-high-risk-0069` (high_risk, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: high-risk domain, over-conversion guard, Codex review-needed policy guard.
- `blind-high-risk-0070` (high_risk, over_conversion_guard): Exact match, but policy requires maintainer confirmation because: high-risk domain, over-conversion guard, Codex review-needed policy guard.

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
