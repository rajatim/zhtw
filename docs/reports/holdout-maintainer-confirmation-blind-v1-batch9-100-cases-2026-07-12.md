<!-- zhtw:disable -->
# Maintainer Confirmation Packet - Blind V1 Batch9

Generated: `2026-07-12`

Source diff review:
`docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch9-100-cases-2026-07-12.json`

## Summary

- Review cases: 69
- Difference cases: 30
- Policy review cases: 39
- No immediate question: 31
- Ground truth: false
- Promotion allowed: false

## Review Queue

### blind-it-0190 (difference)

- Input: 任务队列会根据优先级重新排序消息。
- Codex: 工作佇列會根據優先順序重新排序訊息。
- Gemini: 任務佇列會根據優先順序重新排序訊息。
- Recommendation: gemini
- Recommended expected: 任務佇列會根據優先順序重新排序訊息。
- Acceptable variants: 工作佇列會根據優先順序重新排序訊息。, 任務佇列會根據優先權重新排序訊息。, 任務佇列會根據優先級重新排序訊息。
- Reason: Gemini primary is already listed as a Codex acceptable variant.

### blind-it-0192 (difference)

- Input: 请在命令行参数里保留原始文件名。
- Codex: 請在命令列參數裡保留原始檔名。
- Gemini: 請在命令列參數裡保留原始檔案名稱。
- Recommendation: codex
- Recommended expected: 請在命令列參數裡保留原始檔名。
- Acceptable variants: 請在命令列參數裡保留原始檔案名稱。, 請在命令列參數中保留原始檔名。
- Reason: Codex primary is already listed as a Gemini acceptable variant.

### blind-it-0195 (difference)

- Input: 数据库连接字符串不应该写入仓库。
- Codex: 資料庫連線字串不應該寫入儲存庫。
- Gemini: 資料庫連線字串不應該寫入存放庫。
- Recommendation: codex
- Recommended expected: 資料庫連線字串不應該寫入儲存庫。
- Acceptable variants: 資料庫連線字串不應該寫入存放庫。
- Reason: Codex primary is already listed as a Gemini acceptable variant.

### blind-it-0196 (difference)

- Input: 请把批处理任务拆成可重试的步骤。
- Codex: 請把批次處理工作拆成可重試的步驟。
- Gemini: 請把批次處理任務拆成可重試的步驟。
- Recommendation: gemini
- Recommended expected: 請把批次處理任務拆成可重試的步驟。
- Acceptable variants: 請把批次處理工作拆成可重試的步驟。, 請將批次處理任務拆成可重試的步驟。, 請把批次任務拆成可重試的步驟。
- Reason: Gemini primary is already listed as a Codex acceptable variant.

### blind-it-0197 (difference)

- Input: 服务发现会返回健康的实例列表。
- Codex: 服務探索會回傳健康的執行個體清單。
- Gemini: 服務發現會回傳健康的執行個體清單。
- Recommendation: gemini
- Recommended expected: 服務發現會回傳健康的執行個體清單。
- Acceptable variants: 服務探索會回傳健康的執行個體清單。, 服務發現會返回健康的執行個體清單。, 服務發現會回傳健康的實例清單。
- Reason: Codex marked this as a variant-sensitive case and Gemini gave a high-confidence alternative.

### blind-it-0198 (difference)

- Input: 构建产物会上传到内部制品库。
- Codex: 建置成品會上傳到內部成品庫。
- Gemini: 建置產物會上傳到內部製品庫。
- Recommendation: codex
- Recommended expected: 建置成品會上傳到內部成品庫。
- Acceptable variants: 建置產物會上傳到內部製品庫。, 建置產物會上傳到內部 artifact 儲存庫。, 組建產物會上傳到內部製品庫。, 建置產物會上傳到內部成品庫。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.

### blind-it-0199 (difference)

- Input: 如果锁文件变更，依赖安装会重新执行。
- Codex: 如果鎖定檔變更，相依套件安裝會重新執行。
- Gemini: 如果鎖定檔變更，相依性安裝會重新執行。
- Recommendation: codex
- Recommended expected: 如果鎖定檔變更，相依套件安裝會重新執行。
- Acceptable variants: 如果鎖定檔變更，相依性安裝會重新執行。, 如果鎖定檔案變更，相依性安裝會重新執行。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.

### blind-it-0202 (difference)

- Input: 这个 Webhook 会验证时间戳避免重放攻击。
- Codex: 這個 Webhook 會驗證時間戳記以避免重放攻擊。
- Gemini: 這個 Webhook 會驗證時間戳記以避免重送攻擊。
- Recommendation: codex
- Recommended expected: 這個 Webhook 會驗證時間戳記以避免重放攻擊。
- Acceptable variants: 這個 Webhook 會驗證時間戳記以避免重送攻擊。, 這個 Webhook 會驗證時間戳記避免重送攻擊。, 這個 Webhook 會驗證時間戳記避免重放攻擊。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.

### blind-it-0203 (difference)

- Input: 部署清单会引用共享的配置模板。
- Codex: 部署清單會引用共用的設定範本。
- Gemini: 部署清單會參照共用的設定範本。
- Recommendation: codex
- Recommended expected: 部署清單會引用共用的設定範本。
- Acceptable variants: 部署清單會參照共用的設定範本。, 部署清單會引用共享的設定範本。, 部署資訊清單會引用共用的設定範本。
- Reason: Codex primary is already listed as a Gemini acceptable variant.

### blind-it-0204 (difference)

- Input: 日志聚合服务会按租户切分索引。
- Codex: 日誌彙整服務會依租戶切分索引。
- Gemini: 日誌彙總服務會依租戶切分索引。
- Recommendation: codex
- Recommended expected: 日誌彙整服務會依租戶切分索引。
- Acceptable variants: 日誌彙總服務會依租戶切分索引。, 日誌聚合服務會依租戶切分索引。, 日誌聚合服務會按租戶切分索引。, Log 彙總服務會依租戶切分索引。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.

### blind-it-0206 (difference)

- Input: 负载均衡器会把长连接转发到同一台节点。
- Codex: 負載平衡器會把長連線轉送到同一個節點。
- Gemini: 負載平衡器會把長連線轉發到同一台節點。
- Recommendation: codex
- Recommended expected: 負載平衡器會把長連線轉送到同一個節點。
- Acceptable variants: 負載平衡器會把長連線轉發到同一台節點。, 負載均衡器會把長連線轉送到同一個節點。, 負載平衡器會將長連線轉發到同一個節點。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.

### blind-it-0211 (difference)

- Input: 请为上传接口增加幂等键。
- Codex: 請為上傳介面新增冪等鍵。
- Gemini: 請為上傳介面增加冪等鍵。
- Recommendation: codex
- Recommended expected: 請為上傳介面新增冪等鍵。
- Acceptable variants: 請為上傳介面增加冪等鍵。, 請為上傳 API 新增冪等鍵。, 請為上傳 API 增加冪等鍵。, 請為上傳介面新增等冪鍵。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.

### blind-ui-0148 (difference)

- Input: 点击刷新按钮后列表会重新加载。
- Codex: 點選重新整理按鈕後清單會重新載入。
- Gemini: 點擊重新整理按鈕後，清單會重新載入。
- Recommendation: gemini
- Recommended expected: 點擊重新整理按鈕後，清單會重新載入。
- Acceptable variants: 點選重新整理按鈕後清單會重新載入。, 點選重新整理按鈕後，清單會重新載入。, 點擊重新整理按鈕後，列表會重新載入。, 點選重新整理按鈕後，列表會重新載入。
- Reason: Codex marked this as a variant-sensitive case and Gemini gave a high-confidence alternative.

### blind-ui-0149 (difference)

- Input: 请在下拉菜单里显示最近使用的项目。
- Codex: 請在下拉選單裡顯示最近使用的項目。
- Gemini: 請在下拉式選單裡顯示最近使用的項目。
- Recommendation: codex
- Recommended expected: 請在下拉選單裡顯示最近使用的項目。
- Acceptable variants: 請在下拉式選單裡顯示最近使用的項目。, 請在下拉選單中顯示最近使用的項目。, 請在下拉式選單中顯示最近使用的項目。
- Reason: Codex primary is already listed as a Gemini acceptable variant.

### blind-ui-0150 (difference)

- Input: 保存草稿后状态标签会变成已保存。
- Codex: 儲存草稿後狀態標籤會變成已儲存。
- Gemini: 儲存草稿後，狀態標籤會變成已儲存。
- Recommendation: codex
- Recommended expected: 儲存草稿後狀態標籤會變成已儲存。
- Acceptable variants: 儲存草稿後，狀態標籤會變成已儲存。
- Reason: Codex primary is already listed as a Gemini acceptable variant.

### blind-ui-0153 (difference)

- Input: 错误提示会固定在表单顶部。
- Codex: 錯誤提示會固定在表單頂端。
- Gemini: 錯誤提示會固定在表單頂部。
- Recommendation: gemini
- Recommended expected: 錯誤提示會固定在表單頂部。
- Acceptable variants: 錯誤提示會固定在表單頂端。, 錯誤訊息會固定在表單頂端。, 錯誤提示會固定在表單上方。
- Reason: Codex marked this as a variant-sensitive case and Gemini gave a high-confidence alternative.

### blind-ui-0154 (difference)

- Input: 请把已选标签显示在搜索框下方。
- Codex: 請把已選標籤顯示在搜尋框下方。
- Gemini: 請將已選標籤顯示在搜尋框下方。
- Recommendation: codex
- Recommended expected: 請把已選標籤顯示在搜尋框下方。
- Acceptable variants: 請將已選標籤顯示在搜尋框下方。
- Reason: Codex primary is already listed as a Gemini acceptable variant.

### blind-ui-0155 (difference)

- Input: 空状态页面会引导用户建立第一笔记录。
- Codex: 空狀態頁面會引導使用者建立第一筆紀錄。
- Gemini: 空白狀態頁面會引導使用者建立第一筆記錄。
- Recommendation: codex
- Recommended expected: 空狀態頁面會引導使用者建立第一筆紀錄。
- Acceptable variants: 空白狀態頁面會引導使用者建立第一筆記錄。, 空狀態頁面會引導使用者建立第一筆記錄。, 空白狀態頁面會引導使用者建立第一筆紀錄。
- Reason: Codex primary is already listed as a Gemini acceptable variant.

### blind-ui-0162 (difference)

- Input: 上传失败时进度条会变成红色。
- Codex: 上傳失敗時進度列會變成紅色。
- Gemini: 上傳失敗時進度條會變成紅色。
- Recommendation: codex
- Recommended expected: 上傳失敗時進度列會變成紅色。
- Acceptable variants: 上傳失敗時進度條會變成紅色。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.

### blind-ui-0164 (difference)

- Input: 请把当前视图固定到导航栏。
- Codex: 請把目前檢視釘選到導覽列。
- Gemini: 請將目前視圖固定到導覽列。
- Recommendation: codex
- Recommended expected: 請把目前檢視釘選到導覽列。
- Acceptable variants: 請將目前視圖固定到導覽列。, 請將目前檢視固定到導覽列。, 請把目前視圖固定到導覽列。, 請將目前視圖釘選到導覽列。, 請將目前檢視釘選到導覽列。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.

### blind-ui-0165 (difference)

- Input: 鼠标悬停时会显示完整文件名。
- Codex: 滑鼠游標停留時會顯示完整檔名。
- Gemini: 滑鼠懸停時會顯示完整檔案名稱。
- Recommendation: codex
- Recommended expected: 滑鼠游標停留時會顯示完整檔名。
- Acceptable variants: 滑鼠懸停時會顯示完整檔案名稱。, 滑鼠懸停時會顯示完整檔名。, 滑鼠游標移上時會顯示完整檔案名稱。, 滑鼠移過時會顯示完整檔案名稱。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.

### blind-ui-0166 (difference)

- Input: 已归档项目会移动到单独的标签页。
- Codex: 已封存項目會移到單獨的分頁。
- Gemini: 已封存項目會移動到獨立的頁籤。
- Recommendation: codex
- Recommended expected: 已封存項目會移到單獨的分頁。
- Acceptable variants: 已封存項目會移動到獨立的頁籤。, 已歸檔項目會移動到單獨的頁籤。, 已封存專案會移動到獨立的頁籤。, 已封存項目會移動到單獨的標籤頁。, 已歸檔項目會移動到單獨的標籤頁。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.

### blind-llm-0111 (difference)

- Input: 工具调用失败时，助理应该解释下一步。
- Codex: 工具呼叫失敗時，助理應該說明下一步。
- Gemini: 工具呼叫失敗時，助理應該解釋下一步。
- Recommendation: gemini
- Recommended expected: 工具呼叫失敗時，助理應該解釋下一步。
- Acceptable variants: 工具呼叫失敗時，助理應該說明下一步。, 工具呼叫失敗時，助理應解釋下一步。
- Reason: Codex marked this as a variant-sensitive case and Gemini gave a high-confidence alternative.

### blind-llm-0112 (difference)

- Input: 提示词模板会把上下文插入占位符。
- Codex: 提示詞範本會把上下文插入佔位符。
- Gemini: 提示詞範本會把上下文插入預留位置。
- Recommendation: codex
- Recommended expected: 提示詞範本會把上下文插入佔位符。
- Acceptable variants: 提示詞範本會把上下文插入預留位置。, 提示詞模板會把上下文插入佔位符。
- Reason: Codex primary is already listed as a Gemini acceptable variant.

### blind-llm-0117 (difference)

- Input: 请把长答案压缩成三条要点。
- Codex: 請把長答案壓縮成三點重點。
- Gemini: 請把長答案壓縮成三條要點。
- Recommendation: gemini
- Recommended expected: 請把長答案壓縮成三條要點。
- Acceptable variants: 請把長答案壓縮成三點重點。, 請將長答案壓縮成三條要點。
- Reason: Gemini primary is already listed as a Codex acceptable variant.

### blind-llm-0118 (difference)

- Input: 评测脚本会比较模型输出和参考答案。
- Codex: 評測指令碼會比較模型輸出和參考答案。
- Gemini: 評測腳本會比較模型輸出和參考答案。
- Recommendation: codex
- Recommended expected: 評測指令碼會比較模型輸出和參考答案。
- Acceptable variants: 評測腳本會比較模型輸出和參考答案。, 評測腳本會比對模型輸出和參考答案。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.

### blind-llm-0119 (difference)

- Input: 用户意图识别失败时需要回问。
- Codex: 使用者意圖辨識失敗時需要追問。
- Gemini: 使用者意圖辨識失敗時需要回問。
- Recommendation: codex
- Recommended expected: 使用者意圖辨識失敗時需要追問。
- Acceptable variants: 使用者意圖辨識失敗時需要回問。, 使用者意圖識別失敗時需要回問。, 用戶意圖辨識失敗時需要回問。, 用戶意圖識別失敗時需要回問。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.

### blind-llm-0121 (difference)

- Input: 对话记忆只保存用户明确同意的内容。
- Codex: 對話記憶只儲存使用者明確同意的內容。
- Gemini: 對話記憶只保存使用者明確同意的內容。
- Recommendation: codex
- Recommended expected: 對話記憶只儲存使用者明確同意的內容。
- Acceptable variants: 對話記憶只保存使用者明確同意的內容。, 對話記憶僅保存使用者明確同意的內容。, 對話記憶只保存用戶明確同意的內容。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.

### blind-llm-0122 (difference)

- Input: 模型回答不能泄露隐藏的系统消息。
- Codex: 模型回答不能洩露隱藏的系統訊息。
- Gemini: 模型回答不能洩漏隱藏的系統訊息。
- Recommendation: codex
- Recommended expected: 模型回答不能洩露隱藏的系統訊息。
- Acceptable variants: 模型回答不能洩漏隱藏的系統訊息。, 模型回答不得洩漏隱藏的系統訊息。
- Reason: Codex primary is already listed as a Gemini acceptable variant.

### blind-social-0116 (difference)

- Input: 你看一下这个优惠券还能不能用。
- Codex: 你看一下這張優惠券還能不能用。
- Gemini: 你看一下這個優惠券還能不能用。
- Recommendation: codex
- Recommended expected: 你看一下這張優惠券還能不能用。
- Acceptable variants: 你看一下這個優惠券還能不能用。, 你看一下這個折價券還能不能用。
- Reason: Prefer Codex first-pass wording pending maintainer confirmation.

### blind-it-0188 (policy_review)

- Input: 这个 SDK 会在请求失败时自动刷新访问令牌。
- Codex: 這個 SDK 會在請求失敗時自動重新整理存取權杖。
- Gemini: 這個 SDK 會在請求失敗時自動重新整理存取權杖。
- Recommendation: codex_gemini_match
- Recommended expected: 這個 SDK 會在請求失敗時自動重新整理存取權杖。
- Acceptable variants: 這個 SDK 會在請求失敗時自動刷新存取權杖。, 這個 SDK 會在請求失敗時自動更新存取權杖。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard

### blind-it-0189 (policy_review)

- Input: 请把错误码映射到统一的异常类型。
- Codex: 請把錯誤碼對應到統一的例外類型。
- Gemini: 請把錯誤碼對應到統一的例外類型。
- Recommendation: codex_gemini_match
- Recommended expected: 請把錯誤碼對應到統一的例外類型。
- Acceptable variants: 請把錯誤碼映射到統一的例外類型。, 請將錯誤碼對應到統一的例外類型。, 請把錯誤碼對應到統一的異常類型。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard

### blind-it-0191 (policy_review)

- Input: 如果配置文件缺少字段，启动检查会失败。
- Codex: 如果設定檔缺少欄位，啟動檢查會失敗。
- Gemini: 如果設定檔缺少欄位，啟動檢查會失敗。
- Recommendation: codex_gemini_match
- Recommended expected: 如果設定檔缺少欄位，啟動檢查會失敗。
- Acceptable variants: 如果配置檔案缺少欄位，啟動檢查會失敗。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard

### blind-it-0193 (policy_review)

- Input: 这个中间件会记录每个请求的追踪编号。
- Codex: 這個中介軟體會記錄每個請求的追蹤編號。
- Gemini: 這個中介軟體會記錄每個請求的追蹤編號。
- Recommendation: codex_gemini_match
- Recommended expected: 這個中介軟體會記錄每個請求的追蹤編號。
- Acceptable variants: 這個中間件會記錄每個請求的追蹤編號。, 這個中介軟體會記錄每個請求的追蹤 ID。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard

### blind-it-0194 (policy_review)

- Input: 缓存预热完成后再切换流量。
- Codex: 快取預熱完成後再切換流量。
- Gemini: 快取預熱完成後再切換流量。
- Recommendation: codex_gemini_match
- Recommended expected: 快取預熱完成後再切換流量。
- Acceptable variants: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard

### blind-ui-0151 (policy_review)

- Input: 这个开关控制是否显示高级选项。
- Codex: 這個開關控制是否顯示進階選項。
- Gemini: 這個開關控制是否顯示進階選項。
- Recommendation: codex_gemini_match
- Recommended expected: 這個開關控制是否顯示進階選項。
- Acceptable variants: 此開關控制是否顯示進階選項。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard

### blind-ui-0152 (policy_review)

- Input: 拖动滑块可以调整预览大小。
- Codex: 拖曳滑桿可以調整預覽大小。
- Gemini: 拖曳滑桿可以調整預覽大小。
- Recommendation: codex_gemini_match
- Recommended expected: 拖曳滑桿可以調整預覽大小。
- Acceptable variants: 拖動滑塊可以調整預覽大小。, 拖曳滑塊可以調整預覽大小。, 拖動滑桿可以調整預覽大小。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard

### blind-llm-0108 (policy_review)

- Input: 系统提示词会限制模型输出 JSON。
- Codex: 系統提示詞會限制模型輸出 JSON。
- Gemini: 系統提示詞會限制模型輸出 JSON。
- Recommendation: codex_gemini_match
- Recommended expected: 系統提示詞會限制模型輸出 JSON。
- Acceptable variants: 系統提示會限制模型輸出 JSON。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard

### blind-llm-0109 (policy_review)

- Input: 请把用户问题改写成检索查询。
- Codex: 請把使用者問題改寫成檢索查詢。
- Gemini: 請把使用者問題改寫成檢索查詢。
- Recommendation: codex_gemini_match
- Recommended expected: 請把使用者問題改寫成檢索查詢。
- Acceptable variants: 請把用戶問題改寫成檢索查詢。, 請將使用者問題改寫為檢索查詢。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard

### blind-llm-0110 (policy_review)

- Input: 摘要需要保留每个段落的关键数字。
- Codex: 摘要需要保留每個段落的關鍵數字。
- Gemini: 摘要需要保留每個段落的關鍵數字。
- Recommendation: codex_gemini_match
- Recommended expected: 摘要需要保留每個段落的關鍵數字。
- Acceptable variants: 摘要需要保留每段的關鍵數字。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex confidence medium, Codex review-needed policy guard

### blind-formal-0109 (policy_review)

- Input: 本公告自发布日起生效。
- Codex: 本公告自發布日起生效。
- Gemini: 本公告自發布日起生效。
- Recommendation: codex_gemini_match
- Recommended expected: 本公告自發布日起生效。
- Acceptable variants: 本公告自發佈日起生效。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard

### blind-formal-0110 (policy_review)

- Input: 申请资料不完整者，将通知补正。
- Codex: 申請資料不完整者，將通知補正。
- Gemini: 申請資料不完整者，將通知補正。
- Recommendation: codex_gemini_match
- Recommended expected: 申請資料不完整者，將通知補正。
- Acceptable variants: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard

### blind-formal-0111 (policy_review)

- Input: 会议记录应保存三年以上。
- Codex: 會議紀錄應保存三年以上。
- Gemini: 會議紀錄應保存三年以上。
- Recommendation: codex_gemini_match
- Recommended expected: 會議紀錄應保存三年以上。
- Acceptable variants: 會議記錄應保存三年以上。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard

### blind-formal-0112 (policy_review)

- Input: 本公司保留调整服务内容的权利。
- Codex: 本公司保留調整服務內容的權利。
- Gemini: 本公司保留調整服務內容的權利。
- Recommendation: codex_gemini_match
- Recommended expected: 本公司保留調整服務內容的權利。
- Acceptable variants: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard

### blind-formal-0113 (policy_review)

- Input: 请于期限内完成线上确认程序。
- Codex: 請於期限內完成線上確認程序。
- Gemini: 請於期限內完成線上確認程序。
- Recommendation: codex_gemini_match
- Recommended expected: 請於期限內完成線上確認程序。
- Acceptable variants: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard

### blind-social-0109 (policy_review)

- Input: 我晚点把截图发给你。
- Codex: 我晚點把截圖傳給你。
- Gemini: 我晚點把截圖傳給你。
- Recommendation: codex_gemini_match
- Recommended expected: 我晚點把截圖傳給你。
- Acceptable variants: 我晚點把截圖發給你。, 我晚點把螢幕截圖傳給你。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard, over-conversion guard

### blind-social-0110 (policy_review)

- Input: 这家店的菜单更新了吗？
- Codex: 這家店的菜單更新了嗎？
- Gemini: 這家店的菜單更新了嗎？
- Recommendation: codex_gemini_match
- Recommended expected: 這家店的菜單更新了嗎？
- Acceptable variants: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard, over-conversion guard

### blind-social-0111 (policy_review)

- Input: 你先帮我把行程加到日历。
- Codex: 你先幫我把行程加到行事曆。
- Gemini: 你先幫我把行程加到行事曆。
- Recommendation: codex_gemini_match
- Recommended expected: 你先幫我把行程加到行事曆。
- Acceptable variants: 你先幫我把行程加到日曆。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard, over-conversion guard

### blind-social-0112 (policy_review)

- Input: 他刚刚在群里说要改时间。
- Codex: 他剛剛在群組裡說要改時間。
- Gemini: 他剛剛在群組裡說要改時間。
- Recommendation: codex_gemini_match
- Recommended expected: 他剛剛在群組裡說要改時間。
- Acceptable variants: 他剛剛在群裡說要改時間。, 他剛剛在群組中說要改時間。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard, over-conversion guard

### blind-social-0113 (policy_review)

- Input: 这张照片不要上传到公开相册。
- Codex: 這張照片不要上傳到公開相簿。
- Gemini: 這張照片不要上傳到公開相簿。
- Recommendation: codex_gemini_match
- Recommended expected: 這張照片不要上傳到公開相簿。
- Acceptable variants: 這張照片不要上傳到公開相冊。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard, over-conversion guard

### blind-social-0114 (policy_review)

- Input: 我已经把地址贴到聊天窗口。
- Codex: 我已經把地址貼到聊天視窗。
- Gemini: 我已經把地址貼到聊天視窗。
- Recommendation: codex_gemini_match
- Recommended expected: 我已經把地址貼到聊天視窗。
- Acceptable variants: 我已經把地址貼到聊天視窗裡。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard, over-conversion guard

### blind-social-0115 (policy_review)

- Input: 周末如果下雨就改成线上聚会。
- Codex: 週末如果下雨就改成線上聚會。
- Gemini: 週末如果下雨就改成線上聚會。
- Recommendation: codex_gemini_match
- Recommended expected: 週末如果下雨就改成線上聚會。
- Acceptable variants: 周末如果下雨就改成線上聚會。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard, over-conversion guard

### blind-social-0117 (policy_review)

- Input: 我把票券存在手机钱包里。
- Codex: 我把票券存在手機錢包裡。
- Gemini: 我把票券存在手機錢包裡。
- Recommendation: codex_gemini_match
- Recommended expected: 我把票券存在手機錢包裡。
- Acceptable variants: 我把票券存在手機錢包中。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard, over-conversion guard

### blind-social-0118 (policy_review)

- Input: 这则贴文先不要分享出去。
- Codex: 這則貼文先不要分享出去。
- Gemini: 這則貼文先不要分享出去。
- Recommendation: codex_gemini_match
- Recommended expected: 這則貼文先不要分享出去。
- Acceptable variants: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard, over-conversion guard

### blind-social-0119 (policy_review)

- Input: 他在留言区回复得很快。
- Codex: 他在留言區回覆得很快。
- Gemini: 他在留言區回覆得很快。
- Recommendation: codex_gemini_match
- Recommended expected: 他在留言區回覆得很快。
- Acceptable variants: 他在留言區回得快。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard, over-conversion guard

### blind-social-0120 (policy_review)

- Input: 晚餐要不要改订附近的餐厅？
- Codex: 晚餐要不要改訂附近的餐廳？
- Gemini: 晚餐要不要改訂附近的餐廳？
- Recommendation: codex_gemini_match
- Recommended expected: 晚餐要不要改訂附近的餐廳？
- Acceptable variants: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard, over-conversion guard

### blind-social-0121 (policy_review)

- Input: 我们先把名单整理到共享表格。
- Codex: 我們先把名單整理到共用表格。
- Gemini: 我們先把名單整理到共用表格。
- Recommendation: codex_gemini_match
- Recommended expected: 我們先把名單整理到共用表格。
- Acceptable variants: 我們先把名單整理到共享表格。, 我們先把名單整理到共用試算表。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard, over-conversion guard

### blind-social-0122 (policy_review)

- Input: 这个账号昨天已经解除绑定。
- Codex: 這個帳號昨天已經解除綁定。
- Gemini: 這個帳號昨天已經解除綁定。
- Recommendation: codex_gemini_match
- Recommended expected: 這個帳號昨天已經解除綁定。
- Acceptable variants: (none)
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard, over-conversion guard

### blind-social-0123 (policy_review)

- Input: 你帮我确认包裹是不是送到了。
- Codex: 你幫我確認包裹是不是送到了。
- Gemini: 你幫我確認包裹是不是送到了。
- Recommendation: codex_gemini_match
- Recommended expected: 你幫我確認包裹是不是送到了。
- Acceptable variants: 你幫我確認包裹是不是寄到了。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard, over-conversion guard

### blind-high-risk-0071 (policy_review)

- Input: 医师会依据检查结果调整用药剂量。
- Codex: 醫師會依據檢查結果調整用藥劑量。
- Gemini: 醫師會依據檢查結果調整用藥劑量。
- Recommendation: codex_gemini_match
- Recommended expected: 醫師會依據檢查結果調整用藥劑量。
- Acceptable variants: 醫師會根據檢查結果調整用藥劑量。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard, high-risk domain, over-conversion guard

### blind-high-risk-0072 (policy_review)

- Input: 投资人应自行评估汇率波动风险。
- Codex: 投資人應自行評估匯率波動風險。
- Gemini: 投資人應自行評估匯率波動風險。
- Recommendation: codex_gemini_match
- Recommended expected: 投資人應自行評估匯率波動風險。
- Acceptable variants: 投資者應自行評估匯率波動風險。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard, high-risk domain, over-conversion guard

### blind-high-risk-0073 (policy_review)

- Input: 未经授权不得调阅病历资料。
- Codex: 未經授權不得調閱病歷資料。
- Gemini: 未經授權不得調閱病歷資料。
- Recommendation: codex_gemini_match
- Recommended expected: 未經授權不得調閱病歷資料。
- Acceptable variants: 未經授權不得調閱病歷紀錄。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard, high-risk domain, over-conversion guard

### blind-high-risk-0074 (policy_review)

- Input: 保险契约的除外责任应以条款载明。
- Codex: 保險契約的除外責任應以條款載明。
- Gemini: 保險契約的除外責任應以條款載明。
- Recommendation: codex_gemini_match
- Recommended expected: 保險契約的除外責任應以條款載明。
- Acceptable variants: 保險合約的除外責任應以條款載明。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard, high-risk domain, over-conversion guard

### blind-high-risk-0075 (policy_review)

- Input: 借款人逾期未缴时，银行得依约催收。
- Codex: 借款人逾期未繳時，銀行得依約催收。
- Gemini: 借款人逾期未繳時，銀行得依約催收。
- Recommendation: codex_gemini_match
- Recommended expected: 借款人逾期未繳時，銀行得依約催收。
- Acceptable variants: 借款人逾期未付時，銀行得依約催收。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard, high-risk domain, over-conversion guard

### blind-high-risk-0076 (policy_review)

- Input: 药品保存条件应符合仿单说明。
- Codex: 藥品保存條件應符合仿單說明。
- Gemini: 藥品保存條件應符合仿單說明。
- Recommendation: codex_gemini_match
- Recommended expected: 藥品保存條件應符合仿單說明。
- Acceptable variants: 藥品保存條件應符合仿單。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard, high-risk domain, over-conversion guard

### blind-high-risk-0077 (policy_review)

- Input: 受监护宣告者应由法定代理人签署。
- Codex: 受監護宣告者應由法定代理人簽署。
- Gemini: 受監護宣告者應由法定代理人簽署。
- Recommendation: codex_gemini_match
- Recommended expected: 受監護宣告者應由法定代理人簽署。
- Acceptable variants: 受監護宣告之人應由法定代理人簽署。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard, high-risk domain, over-conversion guard

### blind-high-risk-0078 (policy_review)

- Input: 跨境汇款可能产生中转银行费用。
- Codex: 跨境匯款可能產生中轉銀行費用。
- Gemini: 跨境匯款可能產生中轉銀行費用。
- Recommendation: codex_gemini_match
- Recommended expected: 跨境匯款可能產生中轉銀行費用。
- Acceptable variants: 跨境匯款可能產生轉匯銀行費用。, 跨境匯款可能產生中間銀行費用。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard, high-risk domain, over-conversion guard

### blind-high-risk-0079 (policy_review)

- Input: 手术同意书应由本人或家属签名。
- Codex: 手術同意書應由本人或家屬簽名。
- Gemini: 手術同意書應由本人或家屬簽名。
- Recommendation: codex_gemini_match
- Recommended expected: 手術同意書應由本人或家屬簽名。
- Acceptable variants: 手術同意書應由本人或家屬簽署。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard, high-risk domain, over-conversion guard

### blind-high-risk-0080 (policy_review)

- Input: 个人资料删除请求应在法定期限内处理。
- Codex: 個人資料刪除請求應在法定期限內處理。
- Gemini: 個人資料刪除請求應在法定期限內處理。
- Recommendation: codex_gemini_match
- Recommended expected: 個人資料刪除請求應在法定期限內處理。
- Acceptable variants: 個人資料刪除要求應在法定期限內處理。
- Reason: Exact match, but policy requires maintainer confirmation because: Codex review-needed policy guard, high-risk domain, over-conversion guard
