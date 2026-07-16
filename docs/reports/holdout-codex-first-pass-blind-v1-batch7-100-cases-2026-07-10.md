<!-- zhtw:disable -->
# Holdout Codex First-Pass Advisory - blind-v1 batch7 100 cases

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

### blind-it-0138

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 请在 API 响应中加入请求标识，方便排查日志。
- Codex expected: 請在 API 回應中加入請求識別碼，方便排查日誌。
- Acceptable alternatives: 請在 API 回應中加入要求識別碼，方便排查日誌。
- Issue tags: technical_term, request_term_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-it-0139

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 服务网格会根据路由规则转发流量。
- Codex expected: 服務網格會根據路由規則轉送流量。
- Acceptable alternatives: 服務網格會依路由規則轉送流量。
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0140

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这个中间件会在认证失败时返回统一错误码。
- Codex expected: 這個中介軟體會在認證失敗時回傳統一錯誤碼。
- Acceptable alternatives: 這個中介軟體會在驗證失敗時回傳統一錯誤碼。
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0141

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 批处理任务会把失败记录写入重试队列。
- Codex expected: 批次處理任務會把失敗記錄寫入重試佇列。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0142

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 请确认配置映射已经同步到所有命名空间。
- Codex expected: 請確認設定映射已經同步到所有命名空間。
- Acceptable alternatives: 請確認 ConfigMap 已經同步到所有命名空間。, 請確認設定對應已經同步到所有命名空間。
- Issue tags: technical_term, kubernetes_term_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-it-0143

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 客户端 SDK 会自动刷新过期的访问令牌。
- Codex expected: 用戶端 SDK 會自動重新整理過期的存取權杖。
- Acceptable alternatives: 客戶端 SDK 會自動重新整理過期的存取權杖。
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0144

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 数据库索引重建期间，查询延迟可能升高。
- Codex expected: 資料庫索引重建期間，查詢延遲可能升高。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0145

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 消息订阅者需要手动确认每条事件。
- Codex expected: 訊息訂閱者需要手動確認每個事件。
- Acceptable alternatives: 訊息訂閱者需要手動確認每一則事件。
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0146

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 部署脚本会先检查目标环境的依赖版本。
- Codex expected: 部署指令碼會先檢查目標環境的相依套件版本。
- Acceptable alternatives: 部署腳本會先檢查目標環境的依賴版本。, 部署指令碼會先檢查目標環境的依賴版本。
- Issue tags: technical_term, dependency_term_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-it-0147

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 日志聚合服务会按追踪编号关联请求。
- Codex expected: 日誌彙整服務會依追蹤編號關聯請求。
- Acceptable alternatives: 記錄彙整服務會依追蹤編號關聯請求。
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0148

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 对象存储桶需要开启版本控制。
- Codex expected: 物件儲存桶需要開啟版本控制。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0149

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请把连接超时设置写入环境变量。
- Codex expected: 請把連線逾時設定寫入環境變數。
- Acceptable alternatives: 請將連線逾時設定寫入環境變數。
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0150

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 这个适配器会把字段名称转换成蛇形命名。
- Codex expected: 這個轉接器會把欄位名稱轉換成蛇形命名。
- Acceptable alternatives: 這個介接器會把欄位名稱轉換成 snake_case 命名。, 這個轉接器會把欄位名稱轉換成蛇形命名法。
- Issue tags: technical_term, style_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-it-0151

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 构建系统会缓存依赖包以缩短流水线时间。
- Codex expected: 建置系統會快取相依套件，以縮短流水線時間。
- Acceptable alternatives: 建置系統會快取依賴套件，以縮短管線時間。
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0152

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 故障转移完成后，监控系统会发送恢复通知。
- Codex expected: 容錯移轉完成後，監控系統會傳送復原通知。
- Acceptable alternatives: 故障移轉完成後，監控系統會傳送恢復通知。
- Issue tags: technical_term, failover_term_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-it-0153

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 容器镜像扫描会阻止含高危漏洞的版本发布。
- Codex expected: 容器映像檔掃描會阻止含高風險弱點的版本發布。
- Acceptable alternatives: 容器映像掃描會阻止含高危漏洞的版本發布。, 容器映像檔掃描會阻止含高風險漏洞的版本發布。
- Issue tags: technical_term, security_term_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-it-0154

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 接口网关会限制每个租户的请求速率。
- Codex expected: 介面閘道會限制每個租用戶的請求速率。
- Acceptable alternatives: API 閘道會限制每個租戶的請求速率。, 介面閘道會限制每個租戶的要求速率。
- Issue tags: technical_term, tenant_term_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-it-0155

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 任务调度器会跳过已经停用的实例。
- Codex expected: 工作排程器會跳過已經停用的執行個體。
- Acceptable alternatives: 任務排程器會跳過已經停用的實例。
- Issue tags: technical_term, cloud_term_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-it-0156

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 请在迁移前导出当前表结构。
- Codex expected: 請在移轉前匯出目前資料表結構。
- Acceptable alternatives: 請在遷移前匯出目前資料表結構。
- Issue tags: technical_term, migration_term_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-it-0157

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这个命令会列出所有可用的扩展模块。
- Codex expected: 這個命令會列出所有可用的擴充模組。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0158

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: README 里的 TaipeiBridge 示例路径不能修改。
- Codex expected: README 裡的 TaipeiBridge 範例路徑不能修改。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, proper_noun_guard
- Rationale: 保留專名、識別碼或既有繁體用字；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0159

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请保留变量名 userID 和 orderID。
- Codex expected: 請保留變數名稱 userID 和 orderID。
- Acceptable alternatives: 請保留變數名 userID 和 orderID。
- Issue tags: baseline_guard, identifier_guard
- Rationale: 保留專名、識別碼或既有繁體用字；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0160

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 错误码 E_CONN_TIMEOUT 必须维持原样。
- Codex expected: 錯誤碼 E_CONN_TIMEOUT 必須維持原樣。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, identifier_guard
- Rationale: 保留專名、識別碼或既有繁體用字；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0161

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 台灣 CDN 節點名稱已經是繁體，不要改寫。
- Codex expected: 台灣 CDN 節點名稱已經是繁體，不要改寫。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。

### blind-it-0162

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 這段繁體設定說明應原樣保留在輸出中。
- Codex expected: 這段繁體設定說明應原樣保留在輸出中。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。

### blind-ui-0108

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 筛选器面板可以按状态折叠。
- Codex expected: 篩選器面板可以依狀態摺疊。
- Acceptable alternatives: 篩選器面板可以按狀態摺疊。
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0109

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 用户点击头像后会打开账户菜单。
- Codex expected: 使用者點擊頭像後會開啟帳戶選單。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0110

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 表格分页控件会显示当前页码。
- Codex expected: 表格分頁控制項會顯示目前頁碼。
- Acceptable alternatives: 表格分頁元件會顯示目前頁碼。
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0111

- Domain: ui
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 上传进度条需要显示剩余时间。
- Codex expected: 上傳進度列需要顯示剩餘時間。
- Acceptable alternatives: 上傳進度條需要顯示剩餘時間。
- Issue tags: ui_term, style_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-ui-0112

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请在空状态页面加入重新加载按钮。
- Codex expected: 請在空狀態頁面加入重新載入按鈕。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0113

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 侧边栏项目可以拖动调整顺序。
- Codex expected: 側邊欄項目可以拖曳調整順序。
- Acceptable alternatives: 側邊列項目可以拖曳調整順序。
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0114

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 设置页面会保存上次选择的语言。
- Codex expected: 設定頁面會儲存上次選擇的語言。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0115

- Domain: ui
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 弹窗底部需要固定主要操作按钮。
- Codex expected: 彈出視窗底部需要固定主要操作按鈕。
- Acceptable alternatives: 對話框底部需要固定主要操作按鈕。
- Issue tags: ui_term, modal_term_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-ui-0116

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 日期选择器会禁用已经过去的日期。
- Codex expected: 日期選擇器會停用已經過去的日期。
- Acceptable alternatives: 日期選擇器會禁用已經過去的日期。
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0117

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 多选菜单会显示已选择项目数量。
- Codex expected: 多選選單會顯示已選取項目數量。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0118

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 搜索框聚焦后会显示最近查询记录。
- Codex expected: 搜尋框取得焦點後會顯示最近查詢記錄。
- Acceptable alternatives: 搜尋框聚焦後會顯示最近查詢紀錄。
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0119

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 通知卡片支持向右滑动关闭。
- Codex expected: 通知卡片支援向右滑動關閉。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0120

- Domain: ui
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 表单字段验证失败时会显示辅助说明。
- Codex expected: 表單欄位驗證失敗時會顯示輔助說明。
- Acceptable alternatives: 表單欄位驗證失敗時會顯示說明文字。
- Issue tags: ui_term, helper_text_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-ui-0121

- Domain: ui
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 分页列表会在滚动到底部时加载更多内容。
- Codex expected: 分頁清單會在捲動到底部時載入更多內容。
- Acceptable alternatives: 分頁列表會在捲動到底部時載入更多內容。
- Issue tags: ui_term, list_term_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-ui-0122

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请把确认按钮放在对话框右下角。
- Codex expected: 請把確認按鈕放在對話框右下角。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0123

- Domain: ui
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 按钮标签「儲存」已经通过台湾团队审核。
- Codex expected: 按鈕標籤「儲存」已經通過台灣團隊審核。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, reviewed_traditional
- Rationale: 保留專名、識別碼或既有繁體用字；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0124

- Domain: ui
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请不要翻译产品名 CloudDesk。
- Codex expected: 請不要翻譯產品名稱 CloudDesk。
- Acceptable alternatives: 請不要翻譯產品名 CloudDesk。
- Issue tags: baseline_guard, brand_guard
- Rationale: 保留專名、識別碼或既有繁體用字；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0125

- Domain: ui
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 保留 URL 参数 redirect_uri 的原始写法。
- Codex expected: 保留 URL 參數 redirect_uri 的原始寫法。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, identifier_guard
- Rationale: 保留專名、識別碼或既有繁體用字；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0126

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 這個繁體介面文案不需要再次轉換。
- Codex expected: 這個繁體介面文案不需要再次轉換。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。

### blind-ui-0127

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 使用者名稱欄位已是繁體，請保持原樣。
- Codex expected: 使用者名稱欄位已是繁體，請保持原樣。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。

### blind-llm-0078

- Domain: llm
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 这个代理会根据系统提示选择工具。
- Codex expected: 這個代理會根據系統提示選擇工具。
- Acceptable alternatives: 這個 agent 會根據系統提示選擇工具。
- Issue tags: llm_term, agent_term_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-llm-0079

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请把摘要结果写成三段式回复。
- Codex expected: 請把摘要結果寫成三段式回覆。
- Acceptable alternatives: 請將摘要結果寫成三段式回覆。
- Issue tags: llm_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0080

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 模型输出需要附上引用来源列表。
- Codex expected: 模型輸出需要附上引用來源清單。
- Acceptable alternatives: 模型輸出需要附上引用來源列表。
- Issue tags: llm_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0081

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 提示模板会插入用户最近的问题。
- Codex expected: 提示範本會插入使用者最近的問題。
- Acceptable alternatives: 提示模板會插入使用者最近的問題。
- Issue tags: llm_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0082

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 如果工具调用失败，代理会重试一次。
- Codex expected: 如果工具呼叫失敗，代理會重試一次。
- Acceptable alternatives: 如果工具調用失敗，代理會重試一次。
- Issue tags: llm_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0083

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请在回答中保留代码块格式。
- Codex expected: 請在回答中保留程式碼區塊格式。
- Acceptable alternatives: 請在回覆中保留程式碼區塊格式。
- Issue tags: llm_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0084

- Domain: llm
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 这个评测脚本会比较模型回答和参考答案。
- Codex expected: 這個評測指令碼會比較模型回答和參考答案。
- Acceptable alternatives: 這個評測腳本會比較模型回答和參考答案。
- Issue tags: llm_term, script_term_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-llm-0085

- Domain: llm
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 对话历史过长时，系统会裁剪较旧消息。
- Codex expected: 對話歷史過長時，系統會截斷較舊訊息。
- Acceptable alternatives: 對話歷史過長時，系統會裁剪較舊訊息。
- Issue tags: llm_term, truncation_term_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-llm-0086

- Domain: llm
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 提示詞中的 TaiwanPolicy 不應被翻譯。
- Codex expected: 提示詞中的 TaiwanPolicy 不應被翻譯。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, proper_noun_guard
- Rationale: 保留專名、識別碼或既有繁體用字；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0087

- Domain: llm
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请保留变量 {{user_locale}} 的占位符。
- Codex expected: 請保留變數 {{user_locale}} 的占位符。
- Acceptable alternatives: 請保留變數 {{user_locale}} 的預留位置。
- Issue tags: baseline_guard, placeholder_guard
- Rationale: 保留專名、識別碼或既有繁體用字；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0088

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 以下繁體回答已經審核，不要自動改寫。
- Codex expected: 以下繁體回答已經審核，不要自動改寫。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。

### blind-llm-0089

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 臺北示例句在提示中應保持原樣。
- Codex expected: 臺北示例句在提示中應保持原樣。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。

### blind-llm-0090

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 這段繁體系統訊息只需要原樣輸出。
- Codex expected: 這段繁體系統訊息只需要原樣輸出。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。

### blind-llm-0091

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 模型回覆中的「品質」用字不應被改動。
- Codex expected: 模型回覆中的「品質」用字不應被改動。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。

### blind-llm-0092

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 請保留既有繁體摘要，不要重新轉換。
- Codex expected: 請保留既有繁體摘要，不要重新轉換。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。

### blind-formal-0079

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 公告发布后，主管机关会更新申请流程。
- Codex expected: 公告發布後，主管機關會更新申請流程。
- Acceptable alternatives: (none)
- Issue tags: formal_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0080

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 会议记录应载明出席人员和表决结果。
- Codex expected: 會議紀錄應載明出席人員和表決結果。
- Acceptable alternatives: (none)
- Issue tags: formal_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0081

- Domain: formal
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 本办法自公布日起三十日后施行。
- Codex expected: 本辦法自公布日起三十日後施行。
- Acceptable alternatives: 本辦法自發布日起三十日後施行。
- Issue tags: formal_term, legal_style_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-formal-0082

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 申请人应于期限内补正相关文件。
- Codex expected: 申請人應於期限內補正相關文件。
- Acceptable alternatives: (none)
- Issue tags: formal_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0083

- Domain: formal
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 采购合约应载明验收标准和付款条件。
- Codex expected: 採購合約應載明驗收標準和付款條件。
- Acceptable alternatives: 採購契約應載明驗收標準和付款條件。
- Issue tags: formal_term, contract_term_variant, tw_usage
- Rationale: 存在台灣用語或風格變體，建議列入 maintainer queue；此為 first-pass 建議。

### blind-formal-0084

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 董事会决议通过后，秘书处会发布通知。
- Codex expected: 董事會決議通過後，秘書處會發布通知。
- Acceptable alternatives: (none)
- Issue tags: formal_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0085

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 研究计划应说明资料保存期限。
- Codex expected: 研究計畫應說明資料保存期限。
- Acceptable alternatives: (none)
- Issue tags: formal_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0086

- Domain: formal
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 法規名稱「個人資料保護法」不得改寫。
- Codex expected: 法規名稱「個人資料保護法」不得改寫。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, law_name_guard
- Rationale: 保留專名、識別碼或既有繁體用字；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0087

- Domain: formal
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请保留文件编号 TW-LEGAL-2026-07。
- Codex expected: 請保留文件編號 TW-LEGAL-2026-07。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, identifier_guard
- Rationale: 保留專名、識別碼或既有繁體用字；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0088

- Domain: formal
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 合约附件中的公司英文名称不得翻译。
- Codex expected: 合約附件中的公司英文名稱不得翻譯。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, company_name_guard
- Rationale: 保留專名、識別碼或既有繁體用字；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0089

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 本繁體公告內容已定稿，請勿再次轉換。
- Codex expected: 本繁體公告內容已定稿，請勿再次轉換。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。

### blind-formal-0090

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 臺灣主管機關名稱已是正式繁體用語。
- Codex expected: 臺灣主管機關名稱已是正式繁體用語。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。

### blind-formal-0091

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 以下繁體條款應保持原文不變。
- Codex expected: 以下繁體條款應保持原文不變。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。

### blind-formal-0092

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 董事會紀錄中的繁體職稱不得改寫。
- Codex expected: 董事會紀錄中的繁體職稱不得改寫。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。

### blind-formal-0093

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 契約本文已完成繁體校對，請保留原樣。
- Codex expected: 契約本文已完成繁體校對，請保留原樣。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。

### blind-social-0079

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 我刚刚把照片上传到共享相册了。
- Codex expected: 我剛剛把照片上傳到共享相簿了。
- Acceptable alternatives: 我剛剛把照片上傳到共用相簿了。
- Issue tags: daily_usage, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0080

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这家店的排队系统会发送简讯提醒。
- Codex expected: 這家店的排隊系統會傳送簡訊提醒。
- Acceptable alternatives: 這家店的排隊系統會發送簡訊提醒。
- Issue tags: daily_usage, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0081

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 周末活动如果延期，会在群组公告。
- Codex expected: 週末活動如果延期，會在群組公告。
- Acceptable alternatives: (none)
- Issue tags: daily_usage, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0082

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请帮我确认包裹的取件编号。
- Codex expected: 請幫我確認包裹的取件編號。
- Acceptable alternatives: (none)
- Issue tags: daily_usage, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0083

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 我想把行程同步到手机日历。
- Codex expected: 我想把行程同步到手機行事曆。
- Acceptable alternatives: 我想把行程同步到手機日曆。
- Issue tags: daily_usage, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0084

- Domain: social
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 我喜歡 TaipeiWalk 這個活動名稱，不要翻譯。
- Codex expected: 我喜歡 TaipeiWalk 這個活動名稱，不要翻譯。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, proper_noun_guard
- Rationale: 保留專名、識別碼或既有繁體用字；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0085

- Domain: social
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请保留昵称小K和阿Ben。
- Codex expected: 請保留暱稱小K和阿Ben。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, nickname_guard
- Rationale: 保留專名、識別碼或既有繁體用字；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0086

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 這句繁體留言已經很好，不需要修改。
- Codex expected: 這句繁體留言已經很好，不需要修改。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。

### blind-social-0087

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 臺中朋友傳來的繁體訊息請保持原樣。
- Codex expected: 臺中朋友傳來的繁體訊息請保持原樣。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。

### blind-social-0088

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 這段繁體貼文不要再轉成別的用字。
- Codex expected: 這段繁體貼文不要再轉成別的用字。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。

### blind-social-0089

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 我今天想保留「品質」這個寫法。
- Codex expected: 我今天想保留「品質」這個寫法。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。

### blind-social-0090

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 請不要改動這則繁體社群公告。
- Codex expected: 請不要改動這則繁體社群公告。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。

### blind-social-0091

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 晚餐訂位確認訊息已是繁體，請保持原樣。
- Codex expected: 晚餐訂位確認訊息已是繁體，請保持原樣。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。

### blind-social-0092

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 臨時改地點的繁體通知不要再改寫。
- Codex expected: 臨時改地點的繁體通知不要再改寫。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。

### blind-social-0093

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 活動報名連結旁的繁體說明請保留。
- Codex expected: 活動報名連結旁的繁體說明請保留。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。

### blind-high-risk-0051

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 医师会根据检查结果调整用药剂量。
- Codex expected: 醫師會根據檢查結果調整用藥劑量。
- Acceptable alternatives: (none)
- Issue tags: high_risk, medical, tw_usage
- Rationale: 此案例屬高風險領域，必須由 maintainer 確認；此為 first-pass 建議。

### blind-high-risk-0052

- Domain: high_risk
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 保险契约应明确说明等待期间。
- Codex expected: 保險契約應明確說明等待期間。
- Acceptable alternatives: 保險合約應明確說明等待期間。
- Issue tags: high_risk, legal_finance_term_variant, tw_usage
- Rationale: 此案例屬高風險領域，必須由 maintainer 確認；此為 first-pass 建議。

### blind-high-risk-0053

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 银行会在交易异常时暂停付款指令。
- Codex expected: 銀行會在交易異常時暫停付款指令。
- Acceptable alternatives: (none)
- Issue tags: high_risk, finance, tw_usage
- Rationale: 此案例屬高風險領域，必須由 maintainer 確認；此為 first-pass 建議。

### blind-high-risk-0054

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 投资人应确认风险揭露文件内容。
- Codex expected: 投資人應確認風險揭露文件內容。
- Acceptable alternatives: (none)
- Issue tags: high_risk, finance, tw_usage
- Rationale: 此案例屬高風險領域，必須由 maintainer 確認；此為 first-pass 建議。

### blind-high-risk-0055

- Domain: high_risk
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 法院判决确定后，执行程序才会开始。
- Codex expected: 法院判決確定後，執行程序才會開始。
- Acceptable alternatives: 法院判決確定後，強制執行程序才會開始。
- Issue tags: high_risk, legal_term_variant, tw_usage
- Rationale: 此案例屬高風險領域，必須由 maintainer 確認；此為 first-pass 建議。

### blind-high-risk-0056

- Domain: high_risk
- Risk: baseline_guard
- Confidence: high
- Review needed: True
- Input: 藥品名稱 Panadol 不應被翻譯或改寫。
- Codex expected: 藥品名稱 Panadol 不應被翻譯或改寫。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, medicine_name_guard
- Rationale: 此案例屬高風險領域，必須由 maintainer 確認；此為 first-pass 建議。

### blind-high-risk-0057

- Domain: high_risk
- Risk: baseline_guard
- Confidence: high
- Review needed: True
- Input: 请保留病例编号 TW-MED-7788。
- Codex expected: 請保留病例編號 TW-MED-7788。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, identifier_guard
- Rationale: 此案例屬高風險領域，必須由 maintainer 確認；此為 first-pass 建議。

### blind-high-risk-0058

- Domain: high_risk
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 本繁體醫療聲明已經核准，請勿改寫。
- Codex expected: 本繁體醫療聲明已經核准，請勿改寫。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input, medical
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。

### blind-high-risk-0059

- Domain: high_risk
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 金融契約中的繁體條款應維持原樣。
- Codex expected: 金融契約中的繁體條款應維持原樣。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input, finance
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。

### blind-high-risk-0060

- Domain: high_risk
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 法院公告的繁體案號不得被轉換。
- Codex expected: 法院公告的繁體案號不得被轉換。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, traditional_input, legal
- Rationale: 此案例是繁體或已審文案的過度轉換防線，必須列入 maintainer queue；此為 first-pass 建議。
