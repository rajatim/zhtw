<!-- zhtw:disable -->
# Holdout Gemini CLI Advisory - blind-v1 batch6 100 cases

Generated: 2026-07-10

This is an independent advisory review. It is not ground truth and must not be promoted without maintainer confirmation.

## Summary

- Total cases: 100
- By domain: {"it": 25, "ui": 20, "llm": 15, "formal": 15, "social": 15, "high_risk": 10}
- By risk: {"candidate_gap": 60, "over_conversion_guard": 25, "baseline_guard": 15}
- By confidence: {"high": 100}
- Review needed: 70
- Promotion allowed: False
- CLI auth note: API-key env vars were unset for this run.

## Cases

### blind-it-0113

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 请求签名失败时，网关会返回可追踪的错误编号。
- Gemini expected: 請求簽名失敗時，閘道會傳回可追蹤的錯誤編號。
- Acceptable alternatives: 請求簽名失敗時，閘道會回傳可追蹤的錯誤編號。, 請求簽名失敗時，閘道器會傳回可追蹤的錯誤編號。, 請求簽名失敗時，閘道器會回傳可追蹤的錯誤編號。, 請求簽章失敗時，閘道會傳回可追蹤的錯誤編號。, 請求簽章失敗時，閘道會回傳可追蹤的錯誤編號。, 請求簽章失敗時，閘道器會傳回可追蹤的錯誤編號。, 請求簽章失敗時，閘道器會回傳可追蹤的錯誤編號。
- Issue tags: gateway_terminology, return_wording, signature_terminology
- Rationale: 網關在台灣常譯為閘道或閘道器，返回常譯為傳回或回傳，簽名可譯為簽名或簽章。

### blind-it-0114

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 请把部署参数写入版本化配置文件。
- Gemini expected: 請把部署參數寫入版本化設定檔。
- Acceptable alternatives: 請將部署參數寫入版本化設定檔。, 請把部署參數寫入版本化組態檔。, 請將部署參數寫入版本化組態檔。
- Issue tags: configuration_wording, preposition_wording
- Rationale: 配置文件在台灣習慣譯為設定檔或組態檔，請把可譯為請將。

### blind-it-0115

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 后端服务会按租户标识隔离缓存键。
- Gemini expected: 後端服務會按租用戶識別碼隔離快取索引鍵。
- Acceptable alternatives: 後端服務會按租用戶識別碼隔離快取鍵。, 後端服務會按照租用戶識別碼隔離快取索引鍵。, 後端服務會按租戶識別碼隔離快取索引鍵。, 後端服務會按租戶識別碼隔離快取鍵。
- Issue tags: tenant_terminology, identifier_terminology, cache_terminology
- Rationale: 租户標識在台灣習慣譯為租用戶識別碼，緩存鍵常譯為快取索引鍵或快取鍵。

### blind-it-0116

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 命令行工具会读取当前工作目录里的配置文件。
- Gemini expected: 命令列工具會讀取目前工作目錄裡的設定檔。
- Acceptable alternatives: 命令列工具會讀取目前工作目錄中的設定檔。, 命令列工具會讀取目前工作目錄裡的組態檔。, 命令列工具會讀取當前工作目錄裡的設定檔。
- Issue tags: cli_terminology, current_wording, configuration_wording
- Rationale: 命令行在台灣譯為命令列，当前譯為目前，配置文件譯為設定檔或組態檔。

### blind-it-0117

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 数据库迁移任务需要在低峰时段执行。
- Gemini expected: 資料庫移轉任務需要在離峰時段執行。
- Acceptable alternatives: 資料庫遷移任務需要在離峰時段執行。, 資料庫移轉任務需要在低峰時段執行。, 資料庫遷移任務需要在低峰時段執行。
- Issue tags: database_terminology, migration_terminology, peak_hours_wording
- Rationale: 数据库在台灣譯為資料庫，迁移常譯為移轉或遷移，低峰時段常稱離峰時段。

### blind-it-0118

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请在服务启动前检查证书链是否完整。
- Gemini expected: 請在服務啟動前檢查憑證鏈是否完整。
- Acceptable alternatives: (none)
- Issue tags: certificate_terminology, startup_wording
- Rationale: 证书在台灣譯為憑證，启动譯為啟動，此轉換相當標準。

### blind-it-0119

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这个 SDK 会把响应主体解析成结构化对象。
- Gemini expected: 這個 SDK 會把回應主體解析成結構化物件。
- Acceptable alternatives: 這個 SDK 會將回應主體解析成結構化物件。
- Issue tags: response_terminology, object_terminology
- Rationale: 响应主体在台灣譯為回應主體，对象常譯為物件，語境極其明確。

### blind-it-0120

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 构建脚本会在发布前生成校验清单。
- Gemini expected: 建置指令碼會在發布前產生校驗清單。
- Acceptable alternatives: 建置腳本會在發布前產生校驗清單。, 建置指令碼會在發布前產生驗證清單。, 建置腳本會在發布前產生驗證清單。, 建置指令碼會在發布前生成校驗清單。, 建置腳本會在發布前生成校驗清單。
- Issue tags: build_terminology, script_wording, checksum_terminology, generate_wording
- Rationale: 构建在台灣譯為建置，脚本常譯為指令碼或腳本，生成譯為產生，校验常譯為校驗或驗證。

### blind-it-0121

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 队列消费者会记录每批消息的确认结果。
- Gemini expected: 佇列消費者會記錄每批訊息的確認結果。
- Acceptable alternatives: 佇列消費者會紀錄每批訊息的確認結果。, 佇列消費者會記錄每一批訊息的確認結果。
- Issue tags: queue_terminology, message_terminology, record_wording
- Rationale: 队列在台灣譯為佇列，消息譯為訊息，确认譯為確認，對應相當固定。

### blind-it-0122

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 代理服务器会保留原始请求标头。
- Gemini expected: 代理伺服器會保留原始請求標頭。
- Acceptable alternatives: (none)
- Issue tags: proxy_terminology, header_terminology
- Rationale: 代理服务器在台灣譯為代理伺服器，标头譯為標頭，轉換極為標準。

### blind-it-0123

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 请把调试信息写入单独的日志文件。
- Gemini expected: 請將偵錯資訊寫入單獨的日誌檔案。
- Acceptable alternatives: 請將除錯資訊寫入單獨的日誌檔案。, 請將偵錯資訊寫入個別的記錄檔。, 請把偵錯資訊寫入單獨的日誌檔案。, 請把除錯資訊寫入單獨的日誌檔案。, 請將偵錯資訊寫入單獨的記錄檔。, 請將除錯資訊寫入單獨的記錄檔。, 請把偵錯資訊寫入單獨的記錄檔。, 請把除錯資訊寫入單獨的記錄檔。
- Issue tags: debug_terminology, log_terminology, preposition_wording
- Rationale: 调试資訊在台灣譯為偵錯資訊或除錯資訊，日志文件常譯為日誌檔案或記錄檔。

### blind-it-0124

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 容器编排平台会根据资源限制调度实例。
- Gemini expected: 容器編排平台會根據資源限制排程實例。
- Acceptable alternatives: 容器編排平台會根據資源限制調度實例。, 容器協調平台會根據資源限制排程實例。, 容器協調平台會根據資源限制調度實例。, 容器編排平台會根據資源限制排程執行個體。, 容器編排平台會根據資源限制調度執行個體。, 容器協調平台會根據資源限制排程執行個體。, 容器協調平台會根據資源限制調度執行個體。
- Issue tags: container_orchestration, scheduler_terminology, instance_terminology
- Rationale: 编排常譯為編排或協調，调度常譯為排程或調度，实例常譯為實例或執行個體。

### blind-it-0125

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 上传任务完成后，接口会返回文件摘要。
- Gemini expected: 上傳任務完成後，介面會回傳檔案摘要。
- Acceptable alternatives: 上傳任務完成後，介面會傳回檔案摘要。, 上傳任務完成後，API會回傳檔案摘要。, 上傳任務完成後，API會傳回檔案摘要。, 上傳任務完成後，介面會回傳文件摘要。
- Issue tags: api_terminology, return_wording, file_terminology
- Rationale: 接口常譯為介面或 API，文件常譯為檔案，返回常譯為回傳或傳回。

### blind-it-0126

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这个缓存策略会根据区域代码设置过期时间。
- Gemini expected: 這個快取策略會根據區域代碼設定過期時間。
- Acceptable alternatives: 這個快取策略會根據區域代碼設置過期時間。
- Issue tags: cache_terminology, setup_wording
- Rationale: 缓存在台灣譯為快取，设置譯為設定，區域代碼已定義於詞庫中。

### blind-it-0127

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 监控仪表盘会显示最近十分钟的错误率。
- Gemini expected: 監控儀表板會顯示最近十分鐘的錯誤率。
- Acceptable alternatives: (none)
- Issue tags: dashboard_terminology
- Rationale: 监控在台灣維持監控，仪表盘譯為儀表板，此轉換相當標準。

### blind-it-0128

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 请保留 API 响应里的 TaiwanNorth 区域名称。
- Gemini expected: 請保留 API 回應裡的 TaiwanNorth 區域名稱。
- Acceptable alternatives: 請保留 API 回應中的 TaiwanNorth 區域名稱。, 請將 API 回應裡的 TaiwanNorth 區域名稱保留。
- Issue tags: over_conversion_guard, proper_noun_guard
- Rationale: TaiwanNorth 為特定之區域專用術語與代號，必須保持原樣防止被過度轉換。

### blind-it-0129

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 变量名 userTaiwanId 不应该被自动改写。
- Gemini expected: 變數名稱 userTaiwanId 不應該被自動改寫。
- Acceptable alternatives: 變數名 userTaiwanId 不應該被自動改寫。, 變數名稱 userTaiwanId 不應該自動被改寫。
- Issue tags: over_conversion_guard, proper_noun_guard, variable_terminology
- Rationale: userTaiwanId 為代碼中之變數名稱，必須維持原樣防止被任何規則過度轉換。

### blind-it-0130

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 配置文件中的 TaipeiCluster 标签必须保持原样。
- Gemini expected: 設定檔中的 TaipeiCluster 標籤必須維持原樣。
- Acceptable alternatives: 設定檔中的 TaipeiCluster 標籤必須保持原樣。, 組態檔中的 TaipeiCluster 標籤必須維持原樣。, 組態檔中的 TaipeiCluster 標籤必須保持原樣。
- Issue tags: over_conversion_guard, proper_noun_guard, configuration_wording, tag_terminology
- Rationale: TaipeiCluster 為叢集之特定代號，需維持原樣，標籤與設定檔已定義於詞庫。

### blind-it-0131

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: README 里的 zh-TW 示例路径不要转换成其他地区。
- Gemini expected: README 裡的 zh-TW 範例路徑不要轉換成其他地區。
- Acceptable alternatives: README 中的 zh-TW 範例路徑不要轉換成其他地區。
- Issue tags: over_conversion_guard, proper_noun_guard, example_terminology
- Rationale: zh-TW 為標準地區及語言代號需維持原樣，示例在台灣譯為範例。

### blind-it-0132

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 请不要翻译日志字段 requestTaiwanCode。
- Gemini expected: 請不要翻譯日誌欄位 requestTaiwanCode。
- Acceptable alternatives: 請不要翻譯記錄欄位 requestTaiwanCode。, 請不要翻譯記錄檔欄位 requestTaiwanCode。
- Issue tags: over_conversion_guard, proper_noun_guard, field_terminology
- Rationale: requestTaiwanCode 為特定資料欄位名稱，應維持原樣，字段譯為欄位。

### blind-it-0133

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 产品代号 FormosaEdge 写在部署清单里。
- Gemini expected: 產品代號 FormosaEdge 寫在部署資訊清單裡。
- Acceptable alternatives: 產品代號 FormosaEdge 寫在部署清單裡。, 產品代號 FormosaEdge 寫在部署資訊清單中。, 產品代碼 FormosaEdge 寫在部署資訊清單裡。
- Issue tags: over_conversion_guard, proper_noun_guard, manifest_terminology
- Rationale: FormosaEdge 為產品代號需維持原樣，部署清单常譯為部署資訊清單或部署清單。

### blind-it-0134

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 服务器每天凌晨重新启动一次。
- Gemini expected: 伺服器每天凌晨重新啟動一次。
- Acceptable alternatives: 伺服器每天凌晨重啟一次。
- Issue tags: server_terminology, restart_wording
- Rationale: 服务器在台灣譯為伺服器，重新启动譯為重新啟動，轉換相當固定。

### blind-it-0135

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 这个函数会读取本地文件。
- Gemini expected: 這個函式會讀取本機檔案。
- Acceptable alternatives: 這個函數會讀取本機檔案。, 這個函式會讀取本地檔案。, 這個函數會讀取本地檔案。, 這個函式會讀取本機文件。
- Issue tags: function_terminology, local_terminology, file_terminology
- Rationale: 函数在台灣常譯為函式，本地譯為本機，文件常譯為檔案。

### blind-it-0136

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请先保存修改再关闭窗口。
- Gemini expected: 請先儲存變更再關閉視窗。
- Acceptable alternatives: 請先儲存修改再關閉視窗。, 請先保存修改再關閉視窗。, 請先保存變更再關閉視窗。
- Issue tags: save_terminology, window_terminology
- Rationale: 保存修改在台灣常譯為儲存變更，窗口在台灣譯為視窗。

### blind-it-0137

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 网络中断后请重新连接。
- Gemini expected: 網路中斷後請重新連線。
- Acceptable alternatives: 網路中斷後請重新連接。
- Issue tags: network_terminology, connect_terminology
- Rationale: 网络在台灣譯為網路，连接常譯為連線，對應極其固定。

### blind-ui-0088

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 筛选面板会记住上次选择的状态。
- Gemini expected: 篩選面板會記住上次選擇的狀態。
- Acceptable alternatives: 過濾面板會記住上次選擇的狀態。
- Issue tags: filter_translation
- Rationale: 「篩選」、「面板」及「狀態」均為臺灣 UI 的標準對應翻譯，無複雜語意風險。

### blind-ui-0089

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 表格行可以展开查看详细信息。
- Gemini expected: 表格列可以展開查看詳細資訊。
- Acceptable alternatives: 表格列可以展開檢視詳細資訊。, 表格列可以展開檢視詳細資料。, 表格列可以展開查看詳細資料。, 資料列可以展開查看詳細資訊。
- Issue tags: table_row_column_mapping, detailed_info_translation
- Rationale: 簡體「表格行」指 table row，在臺灣對應為「表格列」，「詳細信息」常譯為「詳細資訊」或「詳細資料」。

### blind-ui-0090

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 请在提交按钮旁边显示加载动画。
- Gemini expected: 請在提交按鈕旁邊顯示載入動畫。
- Acceptable alternatives: 請在送出按鈕旁邊顯示載入動畫。, 請在提交按鈕旁邊顯示讀取動畫。, 請在送出按鈕旁邊顯示讀取動畫。
- Issue tags: submit_button_translation, loading_animation_translation
- Rationale: 「提交」在臺灣常作「送出」或保留「提交」，「加載」則常對應「載入」或「讀取」。

### blind-ui-0091

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 搜索结果会按照相关性排序。
- Gemini expected: 搜尋結果會按照相關性排序。
- Acceptable alternatives: 搜尋結果會依相關性排序。
- Issue tags: search_translation
- Rationale: 「搜尋」與「相關性」在臺灣為標準翻譯，句意明確無歧義。

### blind-ui-0092

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 语言切换菜单会显示当前地区。
- Gemini expected: 語言切換選單會顯示目前地區。
- Acceptable alternatives: 語言切換選單會顯示當前地區。
- Issue tags: menu_translation, current_translation
- Rationale: 簡體「菜单」對應臺灣的「選單」，「当前」在臺灣通常慣用「目前」。

### blind-ui-0093

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 空状态页面需要提供返回按钮。
- Gemini expected: 空狀態頁面需要提供返回按鈕。
- Acceptable alternatives: 空白狀態頁面需要提供返回按鈕。
- Issue tags: empty_state_translation
- Rationale: 「空狀態」或「空白狀態」及「返回按鈕」皆為臺灣 UI 常用標準詞彙。

### blind-ui-0094

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 通知列表会按未读状态分组。
- Gemini expected: 通知列表會按未讀狀態分組。
- Acceptable alternatives: 通知清單會按未讀狀態分組。, 通知列表會依未讀狀態分組。, 通知清單會依未讀狀態分組。
- Issue tags: list_translation
- Rationale: 簡體「列表」在臺灣 UI 語境下可對應「列表」或「清單」，兩者皆十分常用。

### blind-ui-0095

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 拖放上传区域会显示文件大小限制。
- Gemini expected: 拖放上傳區域會顯示檔案大小限制。
- Acceptable alternatives: (none)
- Issue tags: file_translation
- Rationale: 簡體 IT 語境中的「文件」在臺灣標準對應為「檔案」，轉換極為明確。

### blind-ui-0096

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 侧边栏折叠后只显示图标。
- Gemini expected: 側邊欄折疊後只顯示圖示。
- Acceptable alternatives: 側邊欄收合後只顯示圖示。, 側欄折疊後只顯示圖示。
- Issue tags: collapse_translation, icon_translation
- Rationale: 「折叠」在臺灣 UI 常用「折疊」或「收合」，「图标」標準對應為「圖示」。

### blind-ui-0097

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 批量操作工具栏会显示已选数量。
- Gemini expected: 批次操作工具列會顯示已選數量。
- Acceptable alternatives: 批次操作工具欄會顯示已選數量。, 批量操作工具列會顯示已選數量。, 批次操作工具列會顯示已選擇數量。
- Issue tags: bulk_batch_translation, toolbar_translation
- Rationale: 簡體「批量」在臺灣對應「批次」，「工具栏」標準對應為「工具列」。

### blind-ui-0098

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 表单错误提示会保留用户输入内容。
- Gemini expected: 表單錯誤提示會保留使用者輸入內容。
- Acceptable alternatives: 表單錯誤提示會保留用戶輸入內容。
- Issue tags: user_translation
- Rationale: 簡體「用户」在臺灣 IT 領域慣用「使用者」，「用戶」亦屬常見用法。

### blind-ui-0099

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 分页器支持跳转到指定页码。
- Gemini expected: 分頁器支援跳轉到指定頁碼。
- Acceptable alternatives: 分頁器支援跳轉至指定頁碼。, 分頁器支持跳轉到指定頁碼。
- Issue tags: support_translation, jump_to_translation
- Rationale: 「支持」於臺灣 IT 領域對應為「支援」，「跳转」在臺灣對應「跳轉」。

### blind-ui-0100

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 请保留按钮文案里的 Taiwan Rewards 名称。
- Gemini expected: 請保留按鈕文案裡的 Taiwan Rewards 名稱。
- Acceptable alternatives: 請保留按鈕文案中的 Taiwan Rewards 名稱。
- Issue tags: proper_noun_guard, over_conversion_guard
- Rationale: 「Taiwan Rewards」為品牌專有名詞，應遵循過度轉換保護原則完整保留。

### blind-ui-0101

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 活动页面标题中的 Taipei Pass 不要翻译。
- Gemini expected: 活動頁面標題中的 Taipei Pass 不要翻譯。
- Acceptable alternatives: 活動頁面標題中的 Taipei Pass 請勿翻譯。, 活動網頁標題中的 Taipei Pass 不要翻譯。
- Issue tags: proper_noun_guard, over_conversion_guard
- Rationale: 「Taipei Pass」為特定服務專有名詞，轉換時需完整保留不得翻譯。

### blind-ui-0102

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 语言包里已经本地化的「登入」不要改写。
- Gemini expected: 語言包裡已經本地化的「登入」不要改寫。
- Acceptable alternatives: 語言包裡已經在地化的「登入」不要改寫。, 語言包中已經本地化的「登入」不要改寫。, 語言包中已經在地化的「登入」不要改寫。
- Issue tags: localization_translation, identity_guard
- Rationale: 「登入」已是臺灣在地化詞彙應予以保留，簡體「本地化」在臺灣亦可作「在地化」。

### blind-ui-0103

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 设置页的 iOS Shortcut 标签保持原样。
- Gemini expected: 設定頁的 iOS Shortcut 標籤保持原樣。
- Acceptable alternatives: (none)
- Issue tags: settings_translation, label_translation, proper_noun_guard
- Rationale: 「设置」對應「設定」，「标签」對應「標籤」，「iOS Shortcut」為專有名詞應保持原樣。

### blind-ui-0104

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: URL 参数 locale=zh-TW 不应被替换。
- Gemini expected: URL 參數 locale=zh-TW 不應被替換。
- Acceptable alternatives: URL 參數 locale=zh-TW 不應被取代。
- Issue tags: parameter_translation, replace_translation, identity_guard
- Rationale: 「参数」對應「參數」，「locale=zh-TW」為技術參數標識應維持原樣不作任何轉換。

### blind-ui-0105

- Domain: ui
- Risk: baseline_guard
- Confidence: high
- Review needed: True
- Input: 页面加载完成后会显示欢迎信息。
- Gemini expected: 頁面載入完成後會顯示歡迎訊息。
- Acceptable alternatives: 頁面載入完成後會顯示歡迎資訊。
- Issue tags: page_load_translation, message_translation
- Rationale: 「加载」對應「載入」，「欢迎信息」在 UI 語境指 welcome message，在臺灣對應「歡迎訊息」。

### blind-ui-0106

- Domain: ui
- Risk: baseline_guard
- Confidence: high
- Review needed: True
- Input: 用户可以上传一张头像图片。
- Gemini expected: 使用者可以上傳一張頭像圖片。
- Acceptable alternatives: 用戶可以上傳一張頭像圖片。
- Issue tags: user_translation
- Rationale: 簡體「用户」對應臺灣慣用的「使用者」或「用戶」，「头像」轉為繁體「頭像」。

### blind-ui-0107

- Domain: ui
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请点击左上角的返回按钮。
- Gemini expected: 請點擊左上角的返回按鈕。
- Acceptable alternatives: 請點選左上角的返回按鈕。
- Issue tags: click_translation
- Rationale: 「点击」在臺灣通常作「點擊」或「點選」，「返回按钮」轉換為繁體「返回按鈕」。

### blind-llm-0063

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 模型回复需要引用检索到的文档段落。
- Gemini expected: 模型回覆需要引用檢索到的文件段落。
- Acceptable alternatives: (none)
- Issue tags: terminology_it
- Rationale: 「回覆」為台灣常用詞，「文檔」在台灣IT領域應對應為「文件」。

### blind-llm-0064

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 请把工具调用结果整理成项目符号清单。
- Gemini expected: 請把工具呼叫結果整理成項目符號清單。
- Acceptable alternatives: 請將工具呼叫結果整理成項目符號清單。, 請把工具呼叫結果整理成項目符號列表。, 請將工具呼叫結果整理成項目符號列表。
- Issue tags: terminology_variant
- Rationale: 「调用」在台灣IT領域應轉為「呼叫」；「項目符號清單」為「bulleted list」之常用翻譯。

### blind-llm-0065

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 系统提示会要求助理保持回答简洁。
- Gemini expected: 系統提示會要求助理保持回答簡潔。
- Acceptable alternatives: 系統提示會要求助理保持回覆簡潔。
- Issue tags: straightforward_translation
- Rationale: 此句轉換極為直觀，語意在台灣非常自然，無特定學術或方言歧義。

### blind-llm-0066

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 摘要生成器会保留原文中的专有名词。
- Gemini expected: 摘要產生器會保留原文中的專有名詞。
- Acceptable alternatives: 摘要生成器會保留原文中的專有名詞。
- Issue tags: terminology_variant
- Rationale: 「生成器」在台灣IT與一般工具常對應為「產生器」；「專有名詞」直譯為「專有名詞」。

### blind-llm-0067

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 代理会在执行计划前检查工具权限。
- Gemini expected: 代理會在執行計畫前檢查工具權限。
- Acceptable alternatives: 代理會在執行計劃前檢查工具權限。
- Issue tags: terminology_variant
- Rationale: 「计划」對應為「計畫」（或「計劃」），「代理」與「工具權限」均為標準台灣科技詞彙。

### blind-llm-0068

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 请将用户意图分类为查询或操作。
- Gemini expected: 請將使用者意圖分類為查詢或操作。
- Acceptable alternatives: 請將用戶意圖分類為查詢或操作。
- Issue tags: terminology_variant
- Rationale: 「用戶」在台灣科技領域常譯為「使用者」（或「用戶」）；「意圖」、「查詢」和「操作」均為標準台灣科技語彙。

### blind-llm-0069

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 输出解析器会验证 JSON 字段是否完整。
- Gemini expected: 輸出剖析器會驗證 JSON 欄位是否完整。
- Acceptable alternatives: 輸出解析器會驗證 JSON 欄位是否完整。
- Issue tags: terminology_variant
- Rationale: 「解析器」對應台灣標準 IT 術語「剖析器」（或「解析器」）；「字段」對應「欄位」。

### blind-llm-0070

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 评测脚本会比较模型回答和参考答案。
- Gemini expected: 評測腳本會比較模型回答和參考答案。
- Acceptable alternatives: 評測腳本會比較模型回覆和參考答案。, 評估腳本會比較模型回答和參考答案。, 評估腳本會比較模型回覆和參考答案。
- Issue tags: terminology_variant
- Rationale: 「評測」對應為「評測」或「評估」；「回答」與「參考答案」在台灣使用非常普遍且自然。

### blind-llm-0071

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 这个提示模板会插入当前会话历史。
- Gemini expected: 這個提示範本會插入目前對話歷史。
- Acceptable alternatives: 這個提示範本會插入目前會話歷史。, 這個提示範本會插入目前工作階段歷史。
- Issue tags: terminology_variant
- Rationale: 「模板」對應「範本」；「当前」對應「目前」；「会话」可翻譯為「對話」、「會話」或「工作階段」。

### blind-llm-0072

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 请不要改写提示词里的 TaiwanSupportBot 名称。
- Gemini expected: 請不要改寫提示詞裡的 TaiwanSupportBot 名稱。
- Acceptable alternatives: 請不要改寫提示詞中的 TaiwanSupportBot 名稱。
- Issue tags: over_conversion_guard
- Rationale: 「TaiwanSupportBot」為專有名詞，應保持原樣不作任何轉換。

### blind-llm-0073

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 示例输出中的 TaipeiOffice 应保持原样。
- Gemini expected: 範例輸出中的 TaipeiOffice 應保持原樣。
- Acceptable alternatives: 示例輸出中的 TaipeiOffice 應保持原樣。
- Issue tags: over_conversion_guard
- Rationale: 「示例」在台灣IT領域通常轉換為「範例」；「TaipeiOffice」為專有名詞，應保持原樣。

### blind-llm-0074

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 模型不得翻译变量 {{taiwan_user_name}}。
- Gemini expected: 模型不得翻譯變數 {{taiwan_user_name}}。
- Acceptable alternatives: 模型不能翻譯變數 {{taiwan_user_name}}。
- Issue tags: over_conversion_guard
- Rationale: 「变量」對應為台灣 IT 術語「變數」；預留的位置變數「{{taiwan_user_name}}」應原樣保留。

### blind-llm-0075

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 文档片段里的「台灣繁體」标签已是目标语言。
- Gemini expected: 文件片段裡的「台灣繁體」標籤已是目標語言。
- Acceptable alternatives: 文件片段中的「台灣繁體」標籤已是目標語言。
- Issue tags: over_conversion_guard
- Rationale: 「文档」在台灣譯為「文件」；「台灣繁體」本身即為目標語言且包含專用詞，應完整保護。

### blind-llm-0076

- Domain: llm
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 机器人会先询问缺少的资料。
- Gemini expected: 機器人會先詢問缺少的資料。
- Acceptable alternatives: (none)
- Issue tags: straightforward_translation
- Rationale: 整句為極直觀的簡繁一對一轉換，在台灣使用極為普遍且無歧義。

### blind-llm-0077

- Domain: llm
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请用三句话总结这段文字。
- Gemini expected: 請用三句話總結這段文字。
- Acceptable alternatives: 請以三句話總結這段文字。
- Issue tags: straightforward_translation
- Rationale: 基礎命令提示，各字詞轉換皆為一對一，極為標準且無歧義。

### blind-formal-0064

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 本公司将于下月调整服务条款。
- Gemini expected: 本公司將於下月調整服務條款。
- Acceptable alternatives: 本公司將於下個月調整服務條款。
- Issue tags: legal_finance_terms
- Rationale: 「本公司將於下月調整服務條款」為標準台灣繁體合約條款書面語，下月亦可作下個月。

### blind-formal-0065

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 会议纪要应列明各部门后续任务。
- Gemini expected: 會議紀錄應列明各部門後續任務。
- Acceptable alternatives: 會議紀要應列明各部門後續任務。
- Issue tags: meeting_minutes
- Rationale: 台灣常用「會議紀錄」代表會議紀要，亦可保留「會議紀要」作為摘要之意。

### blind-formal-0066

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 公告发布后，申请人可在线查询进度。
- Gemini expected: 公告發布後，申請人可線上查詢進度。
- Acceptable alternatives: 公告發布後，申請人可於線上查詢進度。
- Issue tags: online_query
- Rationale: 台灣習慣使用「線上」代替「在線」。

### blind-formal-0067

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 合同附件应与正文具有同等效力。
- Gemini expected: 合約附件應與正文具有同等效力。
- Acceptable alternatives: 契約附件應與正文具有同等效力。
- Issue tags: legal_contract
- Rationale: 台灣商務或法律情境常用「合約」或「契約」代替「合同」。

### blind-formal-0068

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 主管机关将说明资料补正期限。
- Gemini expected: 主管機關將說明資料補正期限。
- Acceptable alternatives: 主管機關將說明資料補正之期限。
- Issue tags: legal_terms
- Rationale: 「主管機關」與「補正」為台灣法律與行政程序標準用語。

### blind-formal-0069

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 年度报告须揭露主要风险因素。
- Gemini expected: 年度報告須揭露主要風險因素。
- Acceptable alternatives: 年度報告須揭露主要風險因子。
- Issue tags: finance_terms
- Rationale: 「年度報告」、「揭露」、「風險因素」為台灣證券與商務標準用語。

### blind-formal-0070

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 采购结果将在官方网站公布。
- Gemini expected: 採購結果將在官方網站公布。
- Acceptable alternatives: 採購結果將於官方網站公布。, 採購結果將在官網公布。
- Issue tags: straightforward
- Rationale: 採購與官方網站為台灣標準書面語，轉換無歧義。

### blind-formal-0071

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 请依规定提交身分证明文件副本。
- Gemini expected: 請依規定提交身分證明文件副本。
- Acceptable alternatives: 請依規定提交身份證明文件副本。, 請依規定提出身分證明文件副本。
- Issue tags: identity_terms
- Rationale: 台灣法規標準用字為「身分」，但常規公文亦極通用「身份」。

### blind-formal-0072

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 该计划将优先补助偏远地区学校。
- Gemini expected: 該計畫將優先補助偏遠地區學校。
- Acceptable alternatives: 該計劃將優先補助偏遠地區學校。
- Issue tags: project_terms
- Rationale: 台灣習慣使用名詞「計畫」，但「計劃」亦常混用。

### blind-formal-0073

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 新闻稿中的 Taiwan Green Fund 名称应保持原样。
- Gemini expected: 新聞稿中的 Taiwan Green Fund 名稱應保持原樣。
- Acceptable alternatives: (none)
- Issue tags: proper_noun, over_conversion_guard
- Rationale: 專有名詞「Taiwan Green Fund」應保持英文原樣，其餘轉為台灣標準繁體。

### blind-formal-0074

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 合约编号 Taipei-2026-A 不得自动改写。
- Gemini expected: 合約編號 Taipei-2026-A 不得自動改寫。
- Acceptable alternatives: 契約編號 Taipei-2026-A 不得自動改寫。
- Issue tags: proper_noun, over_conversion_guard
- Rationale: 合約編號「Taipei-2026-A」為唯一識別碼，必須保持原樣不作任何轉換。

### blind-formal-0075

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 附件标题「台灣示例」已经由法务确认。
- Gemini expected: 附件標題「台灣示例」已經由法務確認。
- Acceptable alternatives: 附件標題「臺灣示例」已經由法務確認。
- Issue tags: proper_noun, traditional_text_guard
- Rationale: 引號內之標題「台灣示例」已由法務確認，故保留其原字「台灣」不強制轉為「臺灣」以防不一致。

### blind-formal-0076

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 公告里的 Formosa Research Center 不需翻译。
- Gemini expected: 公告裡的 Formosa Research Center 不需翻譯。
- Acceptable alternatives: 公告中的 Formosa Research Center 不需翻譯。, 公告裏的 Formosa Research Center 不需翻譯。
- Issue tags: proper_noun, over_conversion_guard
- Rationale: 專有名詞「Formosa Research Center」應保持英文原樣，其餘部件轉為台灣繁體。

### blind-formal-0077

- Domain: formal
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 会议将于下午三点开始。
- Gemini expected: 會議將於下午三點開始。
- Acceptable alternatives: 會議將在下午三點開始。
- Issue tags: straightforward
- Rationale: 會議將於下午三點開始為標準台灣繁體書面語，無特殊歧義。

### blind-formal-0078

- Domain: formal
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请在期限内完成报名手续。
- Gemini expected: 請在期限內完成報名手續。
- Acceptable alternatives: 請於期限內完成報名手續。
- Issue tags: straightforward
- Rationale: 請在期限內完成報名手續為標準台灣繁體書面語，無特殊歧義。

### blind-social-0064

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 我们今晚要不要一起点外送？
- Gemini expected: 我們今晚要不要一起點外送？
- Acceptable alternatives: 擺脫「點外送」也可以說「叫外送」
- Issue tags: food_delivery
- Rationale: 外送在台灣為常用語，點外送或叫外送均極為自然。

### blind-social-0065

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 请把聚餐地点发到群组里。
- Gemini expected: 請把聚餐地點發到群組裡。
- Acceptable alternatives: 請把聚餐地點傳到群組裡。
- Issue tags: chat_group
- Rationale: 群組為台灣常用詞，發到或傳到群組均為常見說法。

### blind-social-0066

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这篇留言已经被管理员隐藏。
- Gemini expected: 這篇留言已經被管理員隱藏。
- Acceptable alternatives: (none)
- Issue tags: comment_moderation
- Rationale: 留言、管理員與隱藏在台灣皆為標準用語，直接進行繁簡轉換即可。

### blind-social-0067

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 我把照片上传到共享相册了。
- Gemini expected: 我把照片上傳到共享相簿了。
- Acceptable alternatives: 我把照片上傳到共用相簿了。, 我把照片上傳到共享相冊了。
- Issue tags: shared_album, terminology_conversion
- Rationale: 台灣多使用「相簿」，「共享」或「共用」皆為可接受的說法。

### blind-social-0068

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这张优惠券明天就会过期。
- Gemini expected: 這張優惠券明天就會過期。
- Acceptable alternatives: (none)
- Issue tags: coupon
- Rationale: 優惠券與過期在台灣皆為標準且唯一的常用詞彙。

### blind-social-0069

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 你可以先帮我保留两个座位吗？
- Gemini expected: 你可以先幫我保留兩個座位嗎？
- Acceptable alternatives: (none)
- Issue tags: seat_reservation
- Rationale: 單純的繁簡字元轉換，無特定詞彙差異。

### blind-social-0070

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 他的昵称会显示在排行榜上。
- Gemini expected: 他的暱稱會顯示在排行榜上。
- Acceptable alternatives: (none)
- Issue tags: nickname
- Rationale: 「昵称」在台灣標準寫法為「暱稱」，「排行榜」與「顯示」無差異。

### blind-social-0071

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 记得把活动链接分享给朋友。
- Gemini expected: 記得把活動連結分享給朋友。
- Acceptable alternatives: (none)
- Issue tags: link, terminology_conversion
- Rationale: 台灣將「链接」稱為「連結」，活動與分享為標準詞彙。

### blind-social-0072

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这个贴文的通知可以先关闭。
- Gemini expected: 這個貼文的通知可以先關閉。
- Acceptable alternatives: (none)
- Issue tags: post_notification
- Rationale: 「貼文」與「關閉」為標準轉換，無特殊術語需要調整。

### blind-social-0073

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 个人简介里的 TaipeiRunner 名称不要改。
- Gemini expected: 個人簡介裡的 TaipeiRunner 名稱不要改。
- Acceptable alternatives: 個人簡介裏的 TaipeiRunner 名稱不要改。
- Issue tags: over_conversion_guard, proper_noun
- Rationale: 保留英文專有名詞 TaipeiRunner，其餘部分進行繁體轉換。

### blind-social-0074

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 请保留留言中的 Happy Taiwan Weekend。
- Gemini expected: 請保留留言中的 Happy Taiwan Weekend。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, english_text
- Rationale: 保留英文祝賀詞 Happy Taiwan Weekend 不作任何轉換。

### blind-social-0075

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 标签 #台灣生活 已经是原始写法。
- Gemini expected: 標籤 #台灣生活 已經是原始寫法。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, hashtag, already_traditional
- Rationale: 標籤內部的「台灣生活」已是繁體，應完好保留避免重複轉換。

### blind-social-0076

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 活动代号 NightMarketGo 不需要翻译。
- Gemini expected: 活動代號 NightMarketGo 不需要翻譯。
- Acceptable alternatives: 活動代碼 NightMarketGo 不需要翻譯。
- Issue tags: over_conversion_guard, codename
- Rationale: 英文活動代號 NightMarketGo 保持原樣，其餘詞彙翻譯為台灣習慣用法。

### blind-social-0077

- Domain: social
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 今天的天气很适合散步。
- Gemini expected: 今天的天氣很適合散步。
- Acceptable alternatives: (none)
- Issue tags: weather
- Rationale: 基礎日常語句，直接進行繁簡轉換即可。

### blind-social-0078

- Domain: social
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 我下午会去超市买水果。
- Gemini expected: 我下午會去超市買水果。
- Acceptable alternatives: (none)
- Issue tags: daily_life
- Rationale: 日常購物語句，「超市」與「水果」在兩岸用法一致。

### blind-high-risk-0041

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 医疗机构应保存患者同意书副本。
- Gemini expected: 醫療機構應保存患者同意書副本。
- Acceptable alternatives: 醫療機構應保存病患同意書副本。, 醫療機構應保存病人同意書副本。
- Issue tags: medical_terms, legal_style
- Rationale: 「醫療機構應保存患者同意書副本」為法定用法，患者在台灣通常也稱為病患或病人。

### blind-high-risk-0042

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 银行应在交易完成后提供明细。
- Gemini expected: 銀行應在交易完成後提供明細。
- Acceptable alternatives: 銀行應於交易完成後提供明細。
- Issue tags: finance_terms
- Rationale: 「銀行應在交易完成後提供明細」符合台灣金融實務，明細代表交易明細帳目。

### blind-high-risk-0043

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 保险契约变更须经双方书面同意。
- Gemini expected: 保險契約變更須經雙方書面同意。
- Acceptable alternatives: (none)
- Issue tags: legal_style, insurance_terms
- Rationale: 「保險契約變更須經雙方書面同意」符合台灣保險法與民法債編契約之標準用語。

### blind-high-risk-0044

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 医师开立处方前应确认过敏记录。
- Gemini expected: 醫師開立處方前應確認過敏紀錄。
- Acceptable alternatives: 醫師開立處方前應確認過敏記錄。
- Issue tags: medical_terms, noun_vs_verb_record
- Rationale: 台灣醫療情境習慣使用「開立處方」與名詞「過敏紀錄」而非動詞性記錄。

### blind-high-risk-0045

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 使用者须先阅读个人资料告知事项。
- Gemini expected: 使用者須先閱讀個人資料告知事項。
- Acceptable alternatives: 用戶須先閱讀個人資料告知事項。
- Issue tags: privacy_terms, legal_style
- Rationale: 「個人資料告知事項」符合台灣個人資料保護法第八條規定之告知義務標準稱呼。

### blind-high-risk-0046

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 法院通知应载明应到时间和地点。
- Gemini expected: 法院通知應載明應到時間和地點。
- Acceptable alternatives: 法院通知應載明應到時間與地點。
- Issue tags: legal_style
- Rationale: 「法院通知應載明應到時間和地點」符合訴訟文書用語，應載明為典型法律條文格式。

### blind-high-risk-0047

- Domain: high_risk
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 病历中的 TaiwanCare 方案名称不得改写。
- Gemini expected: 病歷中的 TaiwanCare 方案名稱不得改寫。
- Acceptable alternatives: 病歷中的 TaiwanCare 方案名稱不得修改。
- Issue tags: proper_noun_guard, medical_terms
- Rationale: 「病歷」為醫療法法定名稱，TaiwanCare 為英文專有名詞應受保護不予翻譯。

### blind-high-risk-0048

- Domain: high_risk
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 契约当事人 Taipei BioLab 名称应保持原样。
- Gemini expected: 契約當事人 Taipei BioLab 名稱應保持原樣。
- Acceptable alternatives: 契約當事人 Taipei BioLab 名稱應維持原樣。
- Issue tags: proper_noun_guard, legal_style
- Rationale: 「契約當事人」為台灣法律習慣用語，專有名詞 Taipei BioLab 保持不變。

### blind-high-risk-0049

- Domain: high_risk
- Risk: baseline_guard
- Confidence: high
- Review needed: True
- Input: 申请人应提供有效证件。
- Gemini expected: 申請人應提供有效證件。
- Acceptable alternatives: 申請人應提供有效證明文件。
- Issue tags: baseline_conversion
- Rationale: 「申請人應提供有效證件」為台灣一般行政機關及私人契約中標準且清楚的字詞對應。

### blind-high-risk-0050

- Domain: high_risk
- Risk: baseline_guard
- Confidence: high
- Review needed: True
- Input: 未成年人签约须经法定代理人同意。
- Gemini expected: 未成年人簽約須經法定代理人同意。
- Acceptable alternatives: (none)
- Issue tags: legal_style
- Rationale: 「法定代理人」為台灣民法標準法律術語，描述未成年人行為之法律效力。
