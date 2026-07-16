<!-- zhtw:disable -->
# Holdout Codex First-Pass Advisory - blind-v1 batch6 100 cases

Generated: 2026-07-10

This is an advisory first pass only. It is not ground truth and must not be promoted without maintainer confirmation.

## Summary

- Total cases: 100
- By domain: {"it": 25, "ui": 20, "llm": 15, "formal": 15, "social": 15, "high_risk": 10}
- By risk: {"candidate_gap": 60, "over_conversion_guard": 25, "baseline_guard": 15}
- By confidence: {"high": 80, "medium": 20}
- Review needed: 50
- Promotion allowed: False

## Cases

### blind-it-0113

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 请求签名失败时，网关会返回可追踪的错误编号。
- Codex expected: 要求簽章失敗時，閘道會回傳可追蹤的錯誤編號。
- Acceptable alternatives: 請求簽章失敗時，閘道會回傳可追蹤的錯誤編號。
- Issue tags: technical_term, request_term_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-it-0114

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请把部署参数写入版本化配置文件。
- Codex expected: 請把部署參數寫入版本化設定檔。
- Acceptable alternatives: 請將部署參數寫入版本化設定檔。
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0115

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 后端服务会按租户标识隔离缓存键。
- Codex expected: 後端服務會依租用戶識別碼隔離快取鍵。
- Acceptable alternatives: 後端服務會依租用戶識別碼隔離快取索引鍵。
- Issue tags: technical_term, tenant_term_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-it-0116

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 命令行工具会读取当前工作目录里的配置文件。
- Codex expected: 命令列工具會讀取目前工作目錄裡的設定檔。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0117

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 数据库迁移任务需要在低峰时段执行。
- Codex expected: 資料庫遷移任務需要在離峰時段執行。
- Acceptable alternatives: 資料庫移轉任務需要在離峰時段執行。
- Issue tags: technical_term, style_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-it-0118

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请在服务启动前检查证书链是否完整。
- Codex expected: 請在服務啟動前檢查憑證鏈是否完整。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0119

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这个 SDK 会把响应主体解析成结构化对象。
- Codex expected: 這個 SDK 會把回應主體解析成結構化物件。
- Acceptable alternatives: 這個 SDK 會將回應主體解析成結構化物件。
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0120

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 构建脚本会在发布前生成校验清单。
- Codex expected: 建置指令碼會在發布前產生校驗清單。
- Acceptable alternatives: 建置腳本會在發布前產生校驗清單。, 建置指令碼會在發佈前產生校驗清單。
- Issue tags: technical_term, style_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-it-0121

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 队列消费者会记录每批消息的确认结果。
- Codex expected: 佇列消費者會記錄每批訊息的確認結果。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0122

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 代理服务器会保留原始请求标头。
- Codex expected: 代理伺服器會保留原始請求標頭。
- Acceptable alternatives: 代理伺服器會保留原始要求標頭。
- Issue tags: technical_term, request_term_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-it-0123

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 请把调试信息写入单独的日志文件。
- Codex expected: 請把偵錯資訊寫入單獨的日誌檔案。
- Acceptable alternatives: 請把除錯資訊寫入單獨的日誌檔案。, 請將偵錯資訊寫入單獨的記錄檔。
- Issue tags: technical_term, style_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-it-0124

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 容器编排平台会根据资源限制调度实例。
- Codex expected: 容器編排平台會根據資源限制調度執行個體。
- Acceptable alternatives: 容器編排平台會根據資源限制調度實例。
- Issue tags: technical_term, cloud_term_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-it-0125

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 上传任务完成后，接口会返回文件摘要。
- Codex expected: 上傳任務完成後，介面會回傳檔案摘要。
- Acceptable alternatives: 上傳任務完成後，API 會回傳檔案摘要。
- Issue tags: technical_term, api_term_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-it-0126

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这个缓存策略会根据区域代码设置过期时间。
- Codex expected: 這個快取策略會根據區域代碼設定過期時間。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0127

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 监控仪表盘会显示最近十分钟的错误率。
- Codex expected: 監控儀表板會顯示最近十分鐘的錯誤率。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0128

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 请保留 API 响应里的 TaiwanNorth 区域名称。
- Codex expected: 請保留 API 回應裡的 TaiwanNorth 區域名稱。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, proper_noun, technical_term
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-it-0129

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 变量名 userTaiwanId 不应该被自动改写。
- Codex expected: 變數名稱 userTaiwanId 不應該被自動改寫。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, proper_noun, technical_term
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-it-0130

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 配置文件中的 TaipeiCluster 标签必须保持原样。
- Codex expected: 設定檔中的 TaipeiCluster 標籤必須保持原樣。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, proper_noun, technical_term
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-it-0131

- Domain: it
- Risk: over_conversion_guard
- Confidence: medium
- Review needed: True
- Input: README 里的 zh-TW 示例路径不要转换成其他地区。
- Codex expected: README 裡的 zh-TW 範例路徑不要轉換成其他地區。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, locale, path
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-it-0132

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 请不要翻译日志字段 requestTaiwanCode。
- Codex expected: 請不要翻譯日誌欄位 requestTaiwanCode。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, proper_noun, technical_term
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-it-0133

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 产品代号 FormosaEdge 写在部署清单里。
- Codex expected: 產品代號 FormosaEdge 寫在部署清單裡。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, proper_noun, technical_term
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-it-0134

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 服务器每天凌晨重新启动一次。
- Codex expected: 伺服器每天凌晨重新啟動一次。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, technical_term
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0135

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 这个函数会读取本地文件。
- Codex expected: 這個函式會讀取本機檔案。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, technical_term
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0136

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请先保存修改再关闭窗口。
- Codex expected: 請先儲存修改再關閉視窗。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, common_term
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0137

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 网络中断后请重新连接。
- Codex expected: 網路中斷後請重新連線。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, common_term
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0088

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 筛选面板会记住上次选择的状态。
- Codex expected: 篩選面板會記住上次選擇的狀態。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0089

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 表格行可以展开查看详细信息。
- Codex expected: 表格列可以展開檢視詳細資訊。
- Acceptable alternatives: 表格列可以展開查看詳細資訊。
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0090

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请在提交按钮旁边显示加载动画。
- Codex expected: 請在送出按鈕旁邊顯示載入動畫。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0091

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 搜索结果会按照相关性排序。
- Codex expected: 搜尋結果會依相關性排序。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0092

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 语言切换菜单会显示当前地区。
- Codex expected: 語言切換選單會顯示目前地區。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0093

- Domain: ui
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 空状态页面需要提供返回按钮。
- Codex expected: 空狀態頁面需要提供返回按鈕。
- Acceptable alternatives: 空白狀態頁面需要提供返回按鈕。
- Issue tags: ui_term, style_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-ui-0094

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 通知列表会按未读状态分组。
- Codex expected: 通知清單會依未讀狀態分組。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0095

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 拖放上传区域会显示文件大小限制。
- Codex expected: 拖放上傳區域會顯示檔案大小限制。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0096

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 侧边栏折叠后只显示图标。
- Codex expected: 側邊欄收合後只顯示圖示。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0097

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 批量操作工具栏会显示已选数量。
- Codex expected: 批次操作工具列會顯示已選取數量。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0098

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 表单错误提示会保留用户输入内容。
- Codex expected: 表單錯誤提示會保留使用者輸入內容。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0099

- Domain: ui
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 分页器支持跳转到指定页码。
- Codex expected: 分頁器支援跳轉到指定頁碼。
- Acceptable alternatives: 分頁控制項支援跳至指定頁碼。
- Issue tags: ui_term, style_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-ui-0100

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 请保留按钮文案里的 Taiwan Rewards 名称。
- Codex expected: 請保留按鈕文案裡的 Taiwan Rewards 名稱。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, proper_noun, ui_term
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-ui-0101

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 活动页面标题中的 Taipei Pass 不要翻译。
- Codex expected: 活動頁面標題中的 Taipei Pass 不要翻譯。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, proper_noun, ui_term
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-ui-0102

- Domain: ui
- Risk: over_conversion_guard
- Confidence: medium
- Review needed: True
- Input: 语言包里已经本地化的「登入」不要改写。
- Codex expected: 語言套件裡已經在地化的「登入」不要改寫。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, traditional_text, ui_term
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-ui-0103

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 设置页的 iOS Shortcut 标签保持原样。
- Codex expected: 設定頁的 iOS Shortcut 標籤保持原樣。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, proper_noun, ui_term
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-ui-0104

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: URL 参数 locale=zh-TW 不应被替换。
- Codex expected: URL 參數 locale=zh-TW 不應被替換。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, locale, ui_term
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-ui-0105

- Domain: ui
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 页面加载完成后会显示欢迎信息。
- Codex expected: 頁面載入完成後會顯示歡迎訊息。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, ui_term
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0106

- Domain: ui
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 用户可以上传一张头像图片。
- Codex expected: 使用者可以上傳一張大頭貼圖片。
- Acceptable alternatives: 使用者可以上傳一張頭像圖片。
- Issue tags: baseline_guard, ui_term
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0107

- Domain: ui
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请点击左上角的返回按钮。
- Codex expected: 請點選左上角的返回按鈕。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, ui_term
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0063

- Domain: llm
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 模型回复需要引用检索到的文档段落。
- Codex expected: 模型回覆需要引用檢索到的文件段落。
- Acceptable alternatives: 模型回覆需要引用檢索到的文檔段落。
- Issue tags: llm_term, style_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-llm-0064

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请把工具调用结果整理成项目符号清单。
- Codex expected: 請把工具呼叫結果整理成項目符號清單。
- Acceptable alternatives: (none)
- Issue tags: llm_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0065

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 系统提示会要求助理保持回答简洁。
- Codex expected: 系統提示會要求助理保持回答簡潔。
- Acceptable alternatives: (none)
- Issue tags: llm_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0066

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 摘要生成器会保留原文中的专有名词。
- Codex expected: 摘要產生器會保留原文中的專有名詞。
- Acceptable alternatives: (none)
- Issue tags: llm_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0067

- Domain: llm
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 代理会在执行计划前检查工具权限。
- Codex expected: 代理會在執行計畫前檢查工具權限。
- Acceptable alternatives: 代理會在執行規劃前檢查工具權限。
- Issue tags: llm_term, style_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-llm-0068

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请将用户意图分类为查询或操作。
- Codex expected: 請將使用者意圖分類為查詢或操作。
- Acceptable alternatives: (none)
- Issue tags: llm_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0069

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 输出解析器会验证 JSON 字段是否完整。
- Codex expected: 輸出解析器會驗證 JSON 欄位是否完整。
- Acceptable alternatives: (none)
- Issue tags: llm_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0070

- Domain: llm
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 评测脚本会比较模型回答和参考答案。
- Codex expected: 評測指令碼會比較模型回答和參考答案。
- Acceptable alternatives: 評測腳本會比較模型回答和參考答案。
- Issue tags: llm_term, style_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-llm-0071

- Domain: llm
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 这个提示模板会插入当前会话历史。
- Codex expected: 這個提示範本會插入目前對話歷史。
- Acceptable alternatives: 這個提示範本會插入目前會話歷史。
- Issue tags: llm_term, style_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-llm-0072

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 请不要改写提示词里的 TaiwanSupportBot 名称。
- Codex expected: 請不要改寫提示詞裡的 TaiwanSupportBot 名稱。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, proper_noun, llm_term
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-llm-0073

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 示例输出中的 TaipeiOffice 应保持原样。
- Codex expected: 範例輸出中的 TaipeiOffice 應保持原樣。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, proper_noun, llm_term
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-llm-0074

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 模型不得翻译变量 {{taiwan_user_name}}。
- Codex expected: 模型不得翻譯變數 {{taiwan_user_name}}。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, variable, llm_term
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-llm-0075

- Domain: llm
- Risk: over_conversion_guard
- Confidence: medium
- Review needed: True
- Input: 文档片段里的「台灣繁體」标签已是目标语言。
- Codex expected: 文件片段裡的「台灣繁體」標籤已是目標語言。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, traditional_text, llm_term
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-llm-0076

- Domain: llm
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 机器人会先询问缺少的资料。
- Codex expected: 機器人會先詢問缺少的資料。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, llm_term
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0077

- Domain: llm
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请用三句话总结这段文字。
- Codex expected: 請用三句話總結這段文字。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, llm_term
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0064

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 本公司将于下月调整服务条款。
- Codex expected: 本公司將於下月調整服務條款。
- Acceptable alternatives: (none)
- Issue tags: formal_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0065

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 会议纪要应列明各部门后续任务。
- Codex expected: 會議紀要應列明各部門後續任務。
- Acceptable alternatives: (none)
- Issue tags: formal_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0066

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 公告发布后，申请人可在线查询进度。
- Codex expected: 公告發布後，申請人可線上查詢進度。
- Acceptable alternatives: (none)
- Issue tags: formal_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0067

- Domain: formal
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 合同附件应与正文具有同等效力。
- Codex expected: 合約附件應與正文具有同等效力。
- Acceptable alternatives: 契約附件應與正文具有同等效力。
- Issue tags: formal_term, style_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-formal-0068

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 主管机关将说明资料补正期限。
- Codex expected: 主管機關將說明資料補正期限。
- Acceptable alternatives: (none)
- Issue tags: formal_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0069

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 年度报告须揭露主要风险因素。
- Codex expected: 年度報告須揭露主要風險因素。
- Acceptable alternatives: (none)
- Issue tags: formal_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0070

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 采购结果将在官方网站公布。
- Codex expected: 採購結果將在官方網站公布。
- Acceptable alternatives: (none)
- Issue tags: formal_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0071

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请依规定提交身分证明文件副本。
- Codex expected: 請依規定提交身分證明文件副本。
- Acceptable alternatives: (none)
- Issue tags: formal_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0072

- Domain: formal
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 该计划将优先补助偏远地区学校。
- Codex expected: 該計畫將優先補助偏遠地區學校。
- Acceptable alternatives: 該計劃將優先補助偏遠地區學校。
- Issue tags: formal_term, style_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-formal-0073

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 新闻稿中的 Taiwan Green Fund 名称应保持原样。
- Codex expected: 新聞稿中的 Taiwan Green Fund 名稱應保持原樣。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, proper_noun, formal_term
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-formal-0074

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 合约编号 Taipei-2026-A 不得自动改写。
- Codex expected: 合約編號 Taipei-2026-A 不得自動改寫。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, proper_noun, formal_term
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-formal-0075

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 附件标题「台灣示例」已经由法务确认。
- Codex expected: 附件標題「台灣示例」已經由法務確認。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, traditional_text, formal_term
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-formal-0076

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 公告里的 Formosa Research Center 不需翻译。
- Codex expected: 公告裡的 Formosa Research Center 不需翻譯。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, proper_noun, formal_term
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-formal-0077

- Domain: formal
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 会议将于下午三点开始。
- Codex expected: 會議將於下午三點開始。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, formal_term
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0078

- Domain: formal
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请在期限内完成报名手续。
- Codex expected: 請在期限內完成報名手續。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, formal_term
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0064

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 我们今晚要不要一起点外送？
- Codex expected: 我們今晚要不要一起點外送？
- Acceptable alternatives: (none)
- Issue tags: social_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0065

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请把聚餐地点发到群组里。
- Codex expected: 請把聚餐地點發到群組裡。
- Acceptable alternatives: (none)
- Issue tags: social_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0066

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这篇留言已经被管理员隐藏。
- Codex expected: 這篇留言已經被管理員隱藏。
- Acceptable alternatives: (none)
- Issue tags: social_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0067

- Domain: social
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 我把照片上传到共享相册了。
- Codex expected: 我把照片上傳到共享相簿了。
- Acceptable alternatives: 我把照片上傳到共享相冊了。
- Issue tags: social_term, style_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-social-0068

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这张优惠券明天就会过期。
- Codex expected: 這張優惠券明天就會過期。
- Acceptable alternatives: (none)
- Issue tags: social_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0069

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 你可以先帮我保留两个座位吗？
- Codex expected: 你可以先幫我保留兩個座位嗎？
- Acceptable alternatives: (none)
- Issue tags: social_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0070

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 他的昵称会显示在排行榜上。
- Codex expected: 他的暱稱會顯示在排行榜上。
- Acceptable alternatives: (none)
- Issue tags: social_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0071

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 记得把活动链接分享给朋友。
- Codex expected: 記得把活動連結分享給朋友。
- Acceptable alternatives: (none)
- Issue tags: social_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0072

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这个贴文的通知可以先关闭。
- Codex expected: 這個貼文的通知可以先關閉。
- Acceptable alternatives: (none)
- Issue tags: social_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0073

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 个人简介里的 TaipeiRunner 名称不要改。
- Codex expected: 個人簡介裡的 TaipeiRunner 名稱不要改。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, proper_noun, social_term
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-social-0074

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 请保留留言中的 Happy Taiwan Weekend。
- Codex expected: 請保留留言中的 Happy Taiwan Weekend。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, proper_noun, social_term
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-social-0075

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 标签 #台灣生活 已经是原始写法。
- Codex expected: 標籤 #台灣生活 已經是原始寫法。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, traditional_text, social_term
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-social-0076

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 活动代号 NightMarketGo 不需要翻译。
- Codex expected: 活動代號 NightMarketGo 不需要翻譯。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, proper_noun, social_term
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-social-0077

- Domain: social
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 今天的天气很适合散步。
- Codex expected: 今天的天氣很適合散步。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, social_term
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0078

- Domain: social
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 我下午会去超市买水果。
- Codex expected: 我下午會去超市買水果。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, social_term
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-high-risk-0041

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 医疗机构应保存患者同意书副本。
- Codex expected: 醫療機構應保存患者同意書副本。
- Acceptable alternatives: (none)
- Issue tags: high_risk_term, medical, tw_usage
- Rationale: 高風險領域需 maintainer 確認用語；此為 first-pass 建議，不是 ground truth。

### blind-high-risk-0042

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 银行应在交易完成后提供明细。
- Codex expected: 銀行應在交易完成後提供明細。
- Acceptable alternatives: (none)
- Issue tags: high_risk_term, finance, tw_usage
- Rationale: 高風險領域需 maintainer 確認用語；此為 first-pass 建議，不是 ground truth。

### blind-high-risk-0043

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 保险契约变更须经双方书面同意。
- Codex expected: 保險契約變更須經雙方書面同意。
- Acceptable alternatives: (none)
- Issue tags: high_risk_term, legal, tw_usage
- Rationale: 高風險領域需 maintainer 確認用語；此為 first-pass 建議，不是 ground truth。

### blind-high-risk-0044

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 医师开立处方前应确认过敏记录。
- Codex expected: 醫師開立處方前應確認過敏紀錄。
- Acceptable alternatives: (none)
- Issue tags: high_risk_term, medical, tw_usage
- Rationale: 高風險領域需 maintainer 確認用語；此為 first-pass 建議，不是 ground truth。

### blind-high-risk-0045

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 使用者须先阅读个人资料告知事项。
- Codex expected: 使用者須先閱讀個人資料告知事項。
- Acceptable alternatives: (none)
- Issue tags: high_risk_term, privacy, tw_usage
- Rationale: 高風險領域需 maintainer 確認用語；此為 first-pass 建議，不是 ground truth。

### blind-high-risk-0046

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 法院通知应载明应到时间和地点。
- Codex expected: 法院通知應載明應到時間和地點。
- Acceptable alternatives: (none)
- Issue tags: high_risk_term, legal, tw_usage
- Rationale: 高風險領域需 maintainer 確認用語；此為 first-pass 建議，不是 ground truth。

### blind-high-risk-0047

- Domain: high_risk
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 病历中的 TaiwanCare 方案名称不得改写。
- Codex expected: 病歷中的 TaiwanCare 方案名稱不得改寫。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, proper_noun, high_risk_term
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-high-risk-0048

- Domain: high_risk
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 契约当事人 Taipei BioLab 名称应保持原样。
- Codex expected: 契約當事人 Taipei BioLab 名稱應保持原樣。
- Acceptable alternatives: (none)
- Issue tags: over_conversion, proper_noun, high_risk_term
- Rationale: 保留專名、變數、既有繁中或品牌字串；此為 first-pass 建議，需 maintainer 確認。

### blind-high-risk-0049

- Domain: high_risk
- Risk: baseline_guard
- Confidence: high
- Review needed: True
- Input: 申请人应提供有效证件。
- Codex expected: 申請人應提供有效證件。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, high_risk_term
- Rationale: 高風險領域需 maintainer 確認用語；此為 first-pass 建議，不是 ground truth。

### blind-high-risk-0050

- Domain: high_risk
- Risk: baseline_guard
- Confidence: high
- Review needed: True
- Input: 未成年人签约须经法定代理人同意。
- Codex expected: 未成年人簽約須經法定代理人同意。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, high_risk_term
- Rationale: 高風險領域需 maintainer 確認用語；此為 first-pass 建議，不是 ground truth。
