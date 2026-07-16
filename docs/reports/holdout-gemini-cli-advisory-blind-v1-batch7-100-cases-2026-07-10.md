<!-- zhtw:disable -->
# Holdout Gemini CLI Advisory - blind-v1 batch7 100 cases

Generated: 2026-07-10

This is an independent advisory review only. It is not ground truth and must not be promoted without maintainer confirmation.

Reviewer: `gemini_cli`
Model requested: `gemini-2.5-flash`
Raw JSON: `docs/reports/holdout-gemini-cli-advisory-blind-v1-batch7-100-cases-2026-07-10.raw.json`

## Summary

- Total cases: 100
- By domain: {"it": 25, "ui": 20, "llm": 15, "formal": 15, "social": 15, "high_risk": 10}
- By risk: {"candidate_gap": 60, "baseline_guard": 15, "over_conversion_guard": 25}
- By confidence: {"high": 100}
- Review needed: 32
- Promotion allowed: False

## Postprocess

- Removed malformed acceptable from `blind-social-0080`; raw stdout remains in raw JSON.

## Cases

### blind-it-0138

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请在 API 响应中加入请求标识，方便排查日志。
- Gemini expected: 請在 API 回應中加入請求識別碼，方便排查日誌。
- Acceptable alternatives: 請在 API 回應中加入請求識別碼，以利排查日誌。, 請在 API 回應中加入請求識別，方便排查日誌。
- Issue tags: terminology-conversion
- Rationale: API 响应轉換為 API 回應，请求标识轉換為請求識別碼，排查日志轉換為排查日誌。

### blind-it-0139

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 服务网格会根据路由规则转发流量。
- Gemini expected: 服務網格會根據路由規則轉發流量。
- Acceptable alternatives: 服務網格會依據路由規則轉發流量。
- Issue tags: standard-translation
- Rationale: 服务网格轉換為服務網格，根据轉換為根據，路由规则轉換為路由規則，转发轉換為轉發。

### blind-it-0140

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这个中间件会在认证失败时返回统一错误码。
- Gemini expected: 這個中介軟體會在認證失敗時回傳統一錯誤碼。
- Acceptable alternatives: 這個中間件會在認證失敗時回傳統一錯誤碼。, 這個中介軟體會在驗證失敗時回傳統一錯誤碼。
- Issue tags: terminology-conversion
- Rationale: 中间件轉換為台灣 IT 術語中介軟體，返回轉換為回傳，认证轉換為認證。

### blind-it-0141

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 批处理任务会把失败记录写入重试队列。
- Gemini expected: 批次處理任務會將失敗紀錄寫入重試佇列。
- Acceptable alternatives: 批次處理任務會把失敗記錄寫入重試佇列。, 批次處理任務會將失敗記錄寫入重試佇列。
- Issue tags: terminology-conversion
- Rationale: 批处理轉換為批次處理，记录轉換為紀錄，队列轉換為佇列，会把轉換為會將或會把。

### blind-it-0142

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请确认配置映射已经同步到所有命名空间。
- Gemini expected: 請確認設定對應已經同步到所有命名空間。
- Acceptable alternatives: 請確認設定對映已經同步到所有命名空間。, 請確認配置映射已經同步到所有命名空間。
- Issue tags: terminology-conversion
- Rationale: 请确认轉換為請確認，配置映射轉換為設定對應，命名空间轉換為命名空間。

### blind-it-0143

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 客户端 SDK 会自动刷新过期的访问令牌。
- Gemini expected: 用戶端 SDK 會自動更新過期的存取權杖。
- Acceptable alternatives: 用戶端 SDK 會自動刷新過期的存取權杖。, 客戶端 SDK 會自動更新過期的存取權杖。
- Issue tags: terminology-conversion
- Rationale: 客户端轉換為用戶端，刷新轉換為自動更新，访问令牌轉換為存取權杖。

### blind-it-0144

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 数据库索引重建期间，查询延迟可能升高。
- Gemini expected: 資料庫索引重建期間，查詢延遲可能升高。
- Acceptable alternatives: 資料庫索引重建期間，查詢延遲可能會增加。
- Issue tags: standard-translation
- Rationale: 数据库轉換為資料庫，查询轉換為查詢，延迟轉換為延遲。

### blind-it-0145

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 消息订阅者需要手动确认每条事件。
- Gemini expected: 訊息訂閱者需要手動確認每條事件。
- Acceptable alternatives: 訊息訂閱者需要手動確認每個事件。
- Issue tags: terminology-conversion
- Rationale: 消息轉換為訊息，订阅者轉換為訂閱者，手动轉換為手動，确认轉換為確認。

### blind-it-0146

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 部署脚本会先检查目标环境的依赖版本。
- Gemini expected: 部署腳本會先檢查目標環境的相依性版本。
- Acceptable alternatives: 部署腳本會先檢查目標環境的依賴版本。
- Issue tags: terminology-conversion
- Rationale: 脚本轉換為腳本，检查轉換為檢查，依赖轉換為相依性。

### blind-it-0147

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 日志聚合服务会按追踪编号关联请求。
- Gemini expected: 日誌聚合服務會依追蹤編號關聯請求。
- Acceptable alternatives: 日誌聚合服務會依據追蹤編號關聯請求。, 日誌聚合服務會按追蹤編號關聯請求。
- Issue tags: terminology-conversion
- Rationale: 日志轉換為日誌，会按轉換為會依，追踪编号轉換為追蹤編號。

### blind-it-0148

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 对象存储桶需要开启版本控制。
- Gemini expected: 物件儲存桶需要開啟版本控制。
- Acceptable alternatives: 物件儲存貯存桶需要開啟版本控制。, 物件儲存桶需要啟用版本控制。
- Issue tags: terminology-conversion
- Rationale: 对象存储桶轉換為物件儲存桶，开启轉換為開啟或啟用。

### blind-it-0149

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请把连接超时设置写入环境变量。
- Gemini expected: 請將連線逾時設定寫入環境變數。
- Acceptable alternatives: 請把連線逾時設定寫入環境變數。, 請將連接逾時設定寫入環境變數。
- Issue tags: terminology-conversion
- Rationale: 连接超时轉換為連線逾時，设置轉換為設定，环境变量轉換為環境變數。

### blind-it-0150

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这个适配器会把字段名称转换成蛇形命名。
- Gemini expected: 這個轉接器會將欄位名稱轉換成蛇形命名。
- Acceptable alternatives: 這個適配器會將欄位名稱轉換成蛇形命名。, 這個轉接器會把欄位名稱轉換成蛇形命名。
- Issue tags: terminology-conversion
- Rationale: 适配器（軟體設計模式）轉換為轉接器，字段名称轉換為欄位名稱。

### blind-it-0151

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 构建系统会缓存依赖包以缩短流水线时间。
- Gemini expected: 建置系統會快取相依套件以縮短管線時間。
- Acceptable alternatives: 建置系統會快取相依包以縮短管線時間。, 構建系統會快取相依套件以縮短流水線時間。
- Issue tags: terminology-conversion
- Rationale: 构建系统轉換為建置系統，缓存轉換為快取，依赖包轉換為相依套件，流水线轉換為管線。

### blind-it-0152

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 故障转移完成后，监控系统会发送恢复通知。
- Gemini expected: 容錯移轉完成後，監控系統會發送恢復通知。
- Acceptable alternatives: 故障轉移完成後，監控系統會發送恢復通知。
- Issue tags: terminology-conversion
- Rationale: 故障转移轉換為容錯移轉，完成后轉換為完成後，监控系统轉換為監控系統。

### blind-it-0153

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 容器镜像扫描会阻止含高危漏洞的版本发布。
- Gemini expected: 容器映像檔掃描會阻止含有高風險漏洞的版本發布。
- Acceptable alternatives: 容器映像掃描會阻止含高危漏洞的版本釋出。, 容器映像檔掃描會阻止含高危漏洞的版本發布。
- Issue tags: terminology-conversion
- Rationale: 容器镜像轉換為容器映像檔，高危漏洞轉換為高風險漏洞，发布轉換為發布或釋出。

### blind-it-0154

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 接口网关会限制每个租户的请求速率。
- Gemini expected: 介面閘道會限制每個租戶的請求速率。
- Acceptable alternatives: API 閘道會限制每個租戶的請求速率。, 接口閘道會限制每個租戶的請求速率。
- Issue tags: terminology-conversion
- Rationale: 接口网关（API Gateway）轉換為介面閘道或 API 閘道，租户轉換為租戶，请求速率轉換為請求速率。

### blind-it-0155

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 任务调度器会跳过已经停用的实例。
- Gemini expected: 任務排程器會跳過已經停用的執行個體。
- Acceptable alternatives: 任務排程器會跳過已經停用的實例。, 任務排程器會跳過已停用的執行個體。
- Issue tags: terminology-conversion
- Rationale: 任务调度器轉換為任務排程器，已经轉換為已經，实例轉換為執行個體。

### blind-it-0156

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请在迁移前导出当前表结构。
- Gemini expected: 請在遷移前匯出目前的資料表結構。
- Acceptable alternatives: 請在遷移前匯出當前資料表結構。, 請在移轉前匯出目前的資料表結構。
- Issue tags: terminology-conversion
- Rationale: 迁移轉換為遷移，导出轉換為匯出，当前轉換為目前，表结构轉換為資料表結構。

### blind-it-0157

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这个命令会列出所有可用的扩展模块。
- Gemini expected: 這個指令會列出所有可用的擴充模組。
- Acceptable alternatives: 這個命令會列出所有可用的擴充模組。
- Issue tags: terminology-conversion
- Rationale: 命令轉換為指令，扩展模块轉換為擴充模組。

### blind-it-0158

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: README 里的 TaipeiBridge 示例路径不能修改。
- Gemini expected: README 裡的 TaipeiBridge 範例路徑不能修改。
- Acceptable alternatives: README 中的 TaipeiBridge 範例路徑不能修改。
- Issue tags: proper-noun-preservation
- Rationale: README 里的轉換為 README 裡的，示例路径轉換為範例路徑，TaipeiBridge 專有名詞保留。

### blind-it-0159

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请保留变量名 userID 和 orderID。
- Gemini expected: 請保留變數名稱 userID 和 orderID。
- Acceptable alternatives: 請保留變數名 userID 和 orderID。
- Issue tags: identifier-preservation
- Rationale: 请保留轉換為請保留，变量名轉換為變數名稱，userID、orderID 程式碼標識符保留。

### blind-it-0160

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 错误码 E_CONN_TIMEOUT 必须维持原样。
- Gemini expected: 錯誤碼 E_CONN_TIMEOUT 必須維持原樣。
- Acceptable alternatives: 錯誤碼 E_CONN_TIMEOUT 必須保持原樣。
- Issue tags: identifier-preservation
- Rationale: 错误码轉換為錯誤碼，必须轉換為必須，E_CONN_TIMEOUT 保留。

### blind-it-0161

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 台灣 CDN 節點名稱已經是繁體，不要改寫。
- Gemini expected: 台灣 CDN 節點名稱已經是繁體，不要改寫。
- Acceptable alternatives: 台灣 CDN 節點名稱已經是繁體，不要改寫。
- Issue tags: over-conversion-guard
- Rationale: over_conversion_guard 案例，原本已是台灣繁體，原樣保留不改寫。

### blind-it-0162

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 這段繁體設定說明應原樣保留在輸出中。
- Gemini expected: 這段繁體設定說明應原樣保留在輸出中。
- Acceptable alternatives: 這段繁體設定說明應原樣保留在輸出中。
- Issue tags: over-conversion-guard
- Rationale: over_conversion_guard 案例，原本已是繁體，原樣保留不改寫。

### blind-ui-0108

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 筛选器面板可以按状态折叠。
- Gemini expected: 篩選器面板可以依狀態收合。
- Acceptable alternatives: 篩選器面板可以依狀態摺疊。, 篩選器面板可以按狀態收合。, 篩選器面板可以按狀態摺疊。
- Issue tags: terminology
- Rationale: 將「筛选器」轉換為「篩選器」，「折叠」在台灣 UI 介面常譯為「收合」或「摺疊」，並將「按」改為更通順的「依」。

### blind-ui-0109

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 用户点击头像后会打开账户菜单。
- Gemini expected: 使用者點擊頭像後會開啟帳戶選單。
- Acceptable alternatives: 使用者點選頭像後會開啟帳戶選單。, 使用者點擊頭像後會打開帳戶選單。
- Issue tags: terminology
- Rationale: 將「用户」轉換為「使用者」，「账户」轉換為「帳戶」，「菜单」轉換為台灣常用的「選單」，「打开」改為「開啟」更符合軟體介面習慣。

### blind-ui-0110

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 表格分页控件会显示当前页码。
- Gemini expected: 表格分頁控制項會顯示目前頁碼。
- Acceptable alternatives: 表格分頁元件會顯示目前頁碼。, 表格分頁控制項會顯示當前頁碼。
- Issue tags: terminology
- Rationale: 將「分页」轉換為「分頁」，「控件」轉換為台灣常用的「控制項」或「元件」，「当前」轉換為「目前」。

### blind-ui-0111

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 上传进度条需要显示剩余时间。
- Gemini expected: 上傳進度條需要顯示剩餘時間。
- Acceptable alternatives: 上傳進度條需顯示剩餘時間。
- Issue tags: character-conversion
- Rationale: 進行繁簡字元轉換，「上传」對應「上傳」，「进度条」對應「進度條」，「剩余」對應「剩餘」。

### blind-ui-0112

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请在空状态页面加入重新加载按钮。
- Gemini expected: 請在空狀態頁面加入重新載入按鈕。
- Acceptable alternatives: 請在空狀態頁面新增重新載入按鈕。
- Issue tags: terminology
- Rationale: 將「请」轉換為「請」，「重新加载」轉換為台灣常用的「重新載入」，「按钮」轉換為「按鈕」。

### blind-ui-0113

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 侧边栏项目可以拖动调整顺序。
- Gemini expected: 側邊欄項目可以拖曳調整順序。
- Acceptable alternatives: 側邊欄項目可以拖動調整順序。
- Issue tags: terminology
- Rationale: 將「侧边栏」轉換為「側邊欄」，「拖动」轉換為台灣 UI 慣用的「拖曳」。

### blind-ui-0114

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 设置页面会保存上次选择的语言。
- Gemini expected: 設定頁面會儲存上次選擇的語言。
- Acceptable alternatives: 設定頁面會保存上次選擇的語言。
- Issue tags: terminology
- Rationale: 將「设置」轉換為「設定」，「保存」在軟體領域通常轉換為「儲存」，「语言」轉換為「語言」。

### blind-ui-0115

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 弹窗底部需要固定主要操作按钮。
- Gemini expected: 彈出視窗底部需要固定主要操作按鈕。
- Acceptable alternatives: 彈出框底部與固定主要操作按鈕。, 對話框底部需要固定主要操作按鈕。
- Issue tags: terminology
- Rationale: 將大陸用語「弹窗」轉換為台灣慣用的「彈出視窗」，並將「按钮」轉為「按鈕」。

### blind-ui-0116

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 日期选择器会禁用已经过去的日期。
- Gemini expected: 日期選擇器會停用已經過去的日期。
- Acceptable alternatives: 日期選擇器會禁用已經過去的日期。
- Issue tags: terminology
- Rationale: 進行繁簡字元轉換，並將「禁用」轉換為台灣軟體更常用的「停用」（「禁用」亦可接受）。

### blind-ui-0117

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 多选菜单会显示已选择项目数量。
- Gemini expected: 複選選單會顯示已選擇項目數量。
- Acceptable alternatives: 多選選單會顯示已選擇項目數量。, 複選選單會顯示已選項目數量。
- Issue tags: terminology
- Rationale: 將「多选」轉換為台灣 UI 慣用的「複選」（「多選」亦可），「菜单」轉換為「選單」，「项目数量」轉為「項目數量」。

### blind-ui-0118

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 搜索框聚焦后会显示最近查询记录。
- Gemini expected: 搜尋框聚焦後會顯示最近查詢紀錄。
- Acceptable alternatives: 搜尋框取得焦點後會顯示最近查詢紀錄。, 搜尋框聚焦後會顯示最近查詢記錄。
- Issue tags: terminology
- Rationale: 將「搜索框」轉換為「搜尋框」，「后」轉為「後」，「记录」在台灣作名詞時常用「紀錄」。

### blind-ui-0119

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 通知卡片支持向右滑动关闭。
- Gemini expected: 通知卡片支援向右滑動關閉。
- Acceptable alternatives: 通知卡片支援向右滑動以關閉。
- Issue tags: terminology
- Rationale: 將「支持」轉換為台灣常用的「支援」，並轉換其餘繁體字元「滑动」至「滑動」、「关闭」至「關閉」。

### blind-ui-0120

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 表单字段验证失败时会显示辅助说明。
- Gemini expected: 表單欄位驗證失敗時會顯示輔助說明。
- Acceptable alternatives: 表單欄位驗證失敗時會顯示說明文字。
- Issue tags: terminology
- Rationale: 將「表单」轉換為「表單」，「字段」轉換為台灣資訊業標準用語「欄位」，「验证」轉換為「驗證」。

### blind-ui-0121

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 分页列表会在滚动到底部时加载更多内容。
- Gemini expected: 分頁清單會在捲動到底部時載入更多內容。
- Acceptable alternatives: 分頁列表會在捲動到底部時載入更多內容。, 分頁清單會在滾動到底部時載入更多內容。
- Issue tags: terminology
- Rationale: 將「分页」轉換為「分頁」，「列表」通常在台灣譯為「清單」或「列表」，「滚动」譯為「捲動」，「加载」譯為「載入」。

### blind-ui-0122

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请把确认按钮放在对话框右下角。
- Gemini expected: 請把確認按鈕放在對話框右下角。
- Acceptable alternatives: 請將確認按鈕放在對話框右下角。
- Issue tags: character-conversion
- Rationale: 進行繁簡字元轉換，「请」轉「請」，「确认」轉「確認」，「按钮」轉「按鈕」，「对话框」轉「對話框」。

### blind-ui-0123

- Domain: ui
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 按钮标签「儲存」已经通过台湾团队审核。
- Gemini expected: 按鈕標籤「儲存」已經通過台灣團隊審核。
- Acceptable alternatives: 按鈕標籤「儲存」已經通過臺灣團隊審核。
- Issue tags: character-conversion
- Rationale: 保留已審核的繁體字「儲存」，並將其他簡體字元正確轉換（「按钮标签」轉為「按鈕標籤」、「已经通过」轉為「已經通過」、「团队审核」轉為「團隊審核」）。

### blind-ui-0124

- Domain: ui
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请不要翻译产品名 CloudDesk。
- Gemini expected: 請不要翻譯產品名 CloudDesk。
- Acceptable alternatives: 請勿翻譯產品名 CloudDesk。
- Issue tags: product-name-preservation
- Rationale: 保留產品名稱「CloudDesk」不進行翻譯，並將簡體字「请」、「翻译」與「产品名」轉換為對應的繁體「請」、「翻譯」與「產品名」。

### blind-ui-0125

- Domain: ui
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 保留 URL 参数 redirect_uri 的原始写法。
- Gemini expected: 保留 URL 參數 redirect_uri 的原始寫法。
- Acceptable alternatives: 保留 URL 參數 redirect_uri 的原生寫法。
- Issue tags: code-preservation
- Rationale: 保留英文 URL 及變數名稱「redirect_uri」不予變動，其餘簡體字元「参数」與「写法」分別轉換為「參數」與「寫法」。

### blind-ui-0126

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 這個繁體介面文案不需要再次轉換。
- Gemini expected: 這個繁體介面文案不需要再次轉換。
- Acceptable alternatives: 這個繁體介面文案不需要再次轉換。
- Issue tags: over-conversion-guard
- Rationale: 輸入已是完全合規的台灣繁體中文，故不做任何修改，直接保留原樣以防止過度轉換。

### blind-ui-0127

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 使用者名稱欄位已是繁體，請保持原樣。
- Gemini expected: 使用者名稱欄位已是繁體，請保持原樣。
- Acceptable alternatives: 使用者名稱欄位已是繁體，請保持原樣。
- Issue tags: over-conversion-guard
- Rationale: 輸入已是完全合規的台灣繁體中文，故不做任何修改，直接保留原樣以防止過度轉換。

### blind-llm-0078

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这个代理会根据系统提示选择工具。
- Gemini expected: 這個代理會根據系統提示選擇工具。
- Acceptable alternatives: 這個代理會根據系統提示詞選擇工具。, 這個 Agent 會根據系統提示選擇工具。
- Issue tags: (none)
- Rationale: 「代理」對應 Agent，「系統提示」對應 system prompt。

### blind-llm-0079

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请把摘要结果写成三段式回复。
- Gemini expected: 請把摘要結果寫成三段式回覆。
- Acceptable alternatives: 請將摘要結果寫成三段式回覆。, 請把摘要結果寫成三段式回答。
- Issue tags: (none)
- Rationale: 「回复」轉換為台灣慣用的「回覆」或「回答」。

### blind-llm-0080

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 模型输出需要附上引用来源列表。
- Gemini expected: 模型輸出需要附上引用來源列表。
- Acceptable alternatives: 模型輸出需要附上引用來源清單。
- Issue tags: (none)
- Rationale: 「输出」轉換為「輸出」，「来源」轉換為「來源」，「列表」可使用「列表」或「清單」。

### blind-llm-0081

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 提示模板会插入用户最近的问题。
- Gemini expected: 提示範本會插入使用者最近的問題。
- Acceptable alternatives: 提示詞範本會插入使用者最近的問題。, 提示樣板會插入使用者最近的問題。, 提示模板會插入使用者最近的問題。
- Issue tags: (none)
- Rationale: 「模板」在台灣慣用「範本」或「樣板」，「用户」轉換為「使用者」。

### blind-llm-0082

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 如果工具调用失败，代理会重试一次。
- Gemini expected: 如果工具呼叫失敗，代理會重試一次。
- Acceptable alternatives: 如果工具呼叫失敗，Agent 會重試一次。
- Issue tags: (none)
- Rationale: 「调用」在台灣開發習慣中應轉換為「呼叫」。

### blind-llm-0083

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请在回答中保留代码块格式。
- Gemini expected: 請在回答中保留程式碼區塊格式。
- Acceptable alternatives: 請在回覆中保留程式碼區塊格式。
- Issue tags: (none)
- Rationale: 「代码块」轉換為台灣資工慣用的「程式碼區塊」。

### blind-llm-0084

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这个评测脚本会比较模型回答和参考答案。
- Gemini expected: 這個評測腳本會比較模型回答和參考答案。
- Acceptable alternatives: 這個評測指令碼會比較模型回答和參考答案。, 這個評測腳本會比較模型回覆和參考答案。
- Issue tags: (none)
- Rationale: 「评测」轉換為「評測」，「脚本」在台灣常稱作「腳本」或「指令碼」。

### blind-llm-0085

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 对话历史过长时，系统会裁剪较旧消息。
- Gemini expected: 對話歷史過長時，系統會裁剪較舊訊息。
- Acceptable alternatives: 對話紀錄過長時，系統會裁剪較舊訊息。, 對話歷史過長時，系統會截斷較舊訊息。
- Issue tags: (none)
- Rationale: 「对话」轉換為「對話」，「消息」在此語境中指 message，故轉換為「訊息」。

### blind-llm-0086

- Domain: llm
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 提示詞中的 TaiwanPolicy 不應被翻譯。
- Gemini expected: 提示詞中的 TaiwanPolicy 不應被翻譯。
- Acceptable alternatives: 提示詞中的 TaiwanPolicy 不應被翻譯。
- Issue tags: (none)
- Rationale: 輸入已是繁體中文且包含專有名詞 TaiwanPolicy，應原樣保留。

### blind-llm-0087

- Domain: llm
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请保留变量 {{user_locale}} 的占位符。
- Gemini expected: 請保留變數 {{user_locale}} 的佔位符。
- Acceptable alternatives: 請保留變數 {{user_locale}} 的預留位置。
- Issue tags: (none)
- Rationale: 「变量」轉換為「變數」，「占位符」轉換為「佔位符」或「預留位置」，並保留預留變數。

### blind-llm-0088

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 以下繁體回答已經審核，不要自動改寫。
- Gemini expected: 以下繁體回答已經審核，不要自動改寫。
- Acceptable alternatives: 以下繁體回答已經審核，不要自動改寫。
- Issue tags: (none)
- Rationale: 輸入已是繁體中文，過度轉換保護，應完整保留原樣。

### blind-llm-0089

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 臺北示例句在提示中應保持原樣。
- Gemini expected: 臺北示例句在提示中應保持原樣。
- Acceptable alternatives: 台北示例句在提示中應保持原樣。
- Issue tags: (none)
- Rationale: 輸入已是繁體中文，過度轉換保護，維持原字與「臺北」不變。

### blind-llm-0090

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 這段繁體系統訊息只需要原樣輸出。
- Gemini expected: 這段繁體系統訊息只需要原樣輸出。
- Acceptable alternatives: 這段繁體系統訊息只需要原樣輸出。
- Issue tags: (none)
- Rationale: 繁體輸入且語意正確，過度轉換保護，原樣輸出。

### blind-llm-0091

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 模型回覆中的「品質」用字不應被改動。
- Gemini expected: 模型回覆中的「品質」用字不應被改動。
- Acceptable alternatives: 模型回覆中的「品質」用字不應被改動。
- Issue tags: (none)
- Rationale: 繁體輸入且包含台灣特色詞「品質」，過度轉換保護，原樣保留。

### blind-llm-0092

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 請保留既有繁體摘要，不要重新轉換。
- Gemini expected: 請保留既有繁體摘要，不要重新轉換。
- Acceptable alternatives: 請保留既有繁體摘要，不要重新轉換。
- Issue tags: (none)
- Rationale: 繁體輸入，過度轉換保護，原樣保留。

### blind-formal-0079

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 公告发布后，主管机关会更新申请流程。
- Gemini expected: 公告發布後，主管機關會更新申請流程。
- Acceptable alternatives: 公告發佈後，主管機關會更新申請流程。
- Issue tags: sc-to-tc
- Rationale: 簡轉繁：發布、主管機關、會、申請流程。

### blind-formal-0080

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 会议记录应载明出席人员和表决结果。
- Gemini expected: 會議紀錄應載明出席人員和表決結果。
- Acceptable alternatives: 會議記錄應載明出席人員和表決結果。, 會議紀錄應載明出席人員及表決結果。, 會議記錄應載明出席人員及表決結果。
- Issue tags: sc-to-tc
- Rationale: 簡轉繁：會議紀錄/記錄、應、載明、人員、表決結果。

### blind-formal-0081

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 本办法自公布日起三十日后施行。
- Gemini expected: 本辦法自公布日起三十日後施行。
- Acceptable alternatives: 本辦法自公布之日起三十日後施行。
- Issue tags: sc-to-tc
- Rationale: 簡轉繁：辦法、後。

### blind-formal-0082

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 申请人应于期限内补正相关文件。
- Gemini expected: 申請人應於期限內補正相關文件。
- Acceptable alternatives: (none)
- Issue tags: sc-to-tc
- Rationale: 簡轉繁：申請、應於、內、補正、相關。

### blind-formal-0083

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 采购合约应载明验收标准和付款条件。
- Gemini expected: 採購合約應載明驗收標準和付款條件。
- Acceptable alternatives: 採購合約應載明驗收標準及付款條件。, 採購契約應載明驗收標準和付款條件。, 採購契約應載明驗收標準及付款條件。
- Issue tags: sc-to-tc
- Rationale: 簡轉繁：採購、合約/契約、應、驗收、標準、付款條件。

### blind-formal-0084

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 董事会决议通过后，秘书处会发布通知。
- Gemini expected: 董事會決議通過後，秘書處會發布通知。
- Acceptable alternatives: 董事會決議通過後，秘書處會發佈通知。
- Issue tags: sc-to-tc
- Rationale: 簡轉繁：董事會、決議、通過後、秘書處、會發布。

### blind-formal-0085

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 研究计划应说明资料保存期限。
- Gemini expected: 研究計畫應說明資料保存期限。
- Acceptable alternatives: 研究計劃應說明資料保存期限。
- Issue tags: sc-to-tc, term-translation
- Rationale: 計畫與計劃在臺灣皆通用，偏好計畫。簡轉繁：應、資料。

### blind-formal-0086

- Domain: formal
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 法規名稱「個人資料保護法」不得改寫。
- Gemini expected: 法規名稱「個人資料保護法」不得改寫。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 輸入已是符合臺灣法律名稱的繁體中文，應保留不變。

### blind-formal-0087

- Domain: formal
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请保留文件编号 TW-LEGAL-2026-07。
- Gemini expected: 請保留文件編號 TW-LEGAL-2026-07。
- Acceptable alternatives: 請保留文件號碼 TW-LEGAL-2026-07。
- Issue tags: guard, sc-to-tc
- Rationale: 簡轉繁：請、編號。完整保留英文編號 TW-LEGAL-2026-07。

### blind-formal-0088

- Domain: formal
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 合约附件中的公司英文名称不得翻译。
- Gemini expected: 合約附件中的公司英文名稱不得翻譯。
- Acceptable alternatives: 契約附件中的公司英文名稱不得翻譯。
- Issue tags: guard, sc-to-tc
- Rationale: 簡轉繁：合約/契約、名稱、翻譯。保護指示：英文名稱不得翻譯。

### blind-formal-0089

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 本繁體公告內容已定稿，請勿再次轉換。
- Gemini expected: 本繁體公告內容已定稿，請勿再次轉換。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 輸入已為繁體中文，應完全保留原文以防止過度轉換。

### blind-formal-0090

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 臺灣主管機關名稱已是正式繁體用語。
- Gemini expected: 臺灣主管機關名稱已是正式繁體用語。
- Acceptable alternatives: 台灣主管機關名稱已是正式繁體用語。
- Issue tags: guard
- Rationale: 輸入已為繁體中文，應完全保留原文以防止過度轉換。

### blind-formal-0091

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 以下繁體條款應保持原文不變。
- Gemini expected: 以下繁體條款應保持原文不變。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 輸入已為繁體中文，應完全保留原文以防止過度轉換。

### blind-formal-0092

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 董事會紀錄中的繁體職稱不得改寫。
- Gemini expected: 董事會紀錄中的繁體職稱不得改寫。
- Acceptable alternatives: 董事會記錄中的繁體職稱不得改寫。
- Issue tags: guard
- Rationale: 輸入已為繁體中文，應完全保留原文以防止過度轉換。

### blind-formal-0093

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 契約本文已完成繁體校對，請保留原樣。
- Gemini expected: 契約本文已完成繁體校對，請保留原樣。
- Acceptable alternatives: (none)
- Issue tags: guard
- Rationale: 輸入已為繁體中文，應完全保留原文以防止過度轉換。

### blind-social-0079

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 我刚刚把照片上传到共享相册了。
- Gemini expected: 我剛剛把照片上傳到共享相簿了。
- Acceptable alternatives: 我剛剛把照片上傳到共用相簿了。
- Issue tags: lexicon-adaptation
- Rationale: 「刚刚」轉換為「剛剛」，「上传」轉換為「上傳」，「共享相册」轉換為台灣常用的「共享相簿」或「共用相簿」。

### blind-social-0080

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这家店的排队系统会发送简讯提醒。
- Gemini expected: 這家店的排隊系統會發送簡訊提醒。
- Acceptable alternatives: 這間店的排隊系統會發送簡訊提醒。
- Issue tags: char-conversion
- Rationale: 「这家店」轉換為「這家店」，「排队系统」轉換為「排隊系統」，「会发送简讯」轉換為台灣慣用的「會發送簡訊」。

### blind-social-0081

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 周末活动如果延期，会在群组公告。
- Gemini expected: 週末活動如果延期，會在群組公告。
- Acceptable alternatives: 周末活動如果延期，會在群組公告。
- Issue tags: char-conversion
- Rationale: 「周末活动」轉換為「週末活動」，「会」轉換為「會」，「群组」轉換為台灣習慣寫法「群組」。

### blind-social-0082

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请帮我确认包裹的取件编号。
- Gemini expected: 請幫我確認包裹的取件編號。
- Acceptable alternatives: 請幫我確認包裹的取貨編號。
- Issue tags: char-conversion
- Rationale: 「请」轉換為「請」，「确认」轉換為「確認」，「编号」轉換為「編號」。取件編號亦可稱為取貨編號。

### blind-social-0083

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 我想把行程同步到手机日历。
- Gemini expected: 我想把行程同步到手機行事曆。
- Acceptable alternatives: 我想把行程同步到手機日曆。
- Issue tags: lexicon-adaptation
- Rationale: 「手机」轉換為「手機」，「日历」轉換為台灣更慣用的「行事曆」。

### blind-social-0084

- Domain: social
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 我喜歡 TaipeiWalk 這個活動名稱，不要翻譯。
- Gemini expected: 我喜歡 TaipeiWalk 這個活動名稱，不要翻譯。
- Acceptable alternatives: (none)
- Issue tags: guard-preservation
- Rationale: 原文已是繁體中文且包含專有名詞「TaipeiWalk」，應完整保留，不作任何修改。

### blind-social-0085

- Domain: social
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 请保留昵称小K和阿Ben。
- Gemini expected: 請保留暱稱小K和阿Ben。
- Acceptable alternatives: 請保留昵稱小K和阿Ben。
- Issue tags: char-conversion, proper-noun-preservation
- Rationale: 「请」轉換為「請」，「昵称」轉換為台灣標準字體「暱稱」，保留暱稱「小K」與「阿Ben」之原文。

### blind-social-0086

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 這句繁體留言已經很好，不需要修改。
- Gemini expected: 這句繁體留言已經很好，不需要修改。
- Acceptable alternatives: (none)
- Issue tags: over-conversion-guard
- Rationale: 原文已是繁體，且屬於過度轉換保護（over_conversion_guard），應完全保留原樣。

### blind-social-0087

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 臺中朋友傳來的繁體訊息請保持原樣。
- Gemini expected: 臺中朋友傳來的繁體訊息請保持原樣。
- Acceptable alternatives: (none)
- Issue tags: over-conversion-guard
- Rationale: 原文已是繁體，且屬於過度轉換保護（over_conversion_guard），應完全保留原樣。

### blind-social-0088

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 這段繁體貼文不要再轉成別的用字。
- Gemini expected: 這段繁體貼文不要再轉成別的用字。
- Acceptable alternatives: (none)
- Issue tags: over-conversion-guard
- Rationale: 原文已是繁體，且屬於過度轉換保護（over_conversion_guard），應完全保留原樣。

### blind-social-0089

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 我今天想保留「品質」這個寫法。
- Gemini expected: 我今天想保留「品質」這個寫法。
- Acceptable alternatives: (none)
- Issue tags: over-conversion-guard
- Rationale: 原文已是繁體，且包含特定用字習慣「品質」，應完全保留原樣。

### blind-social-0090

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 請不要改動這則繁體社群公告。
- Gemini expected: 請不要改動這則繁體社群公告。
- Acceptable alternatives: (none)
- Issue tags: over-conversion-guard
- Rationale: 原文已是繁體，且屬於過度轉換保護（over_conversion_guard），應完全保留原樣。

### blind-social-0091

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 晚餐訂位確認訊息已是繁體，請保持原樣。
- Gemini expected: 晚餐訂位確認訊息已是繁體，請保持原樣。
- Acceptable alternatives: (none)
- Issue tags: over-conversion-guard
- Rationale: 原文已是繁體，且屬於過度轉換保護（over_conversion_guard），應完全保留原樣。

### blind-social-0092

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 臨時改地點的繁體通知不要再改寫。
- Gemini expected: 臨時改地點的繁體通知不要再改寫。
- Acceptable alternatives: (none)
- Issue tags: over-conversion-guard
- Rationale: 原文已是繁體，且屬於過度轉換保護（over_conversion_guard），應完全保留原樣。

### blind-social-0093

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 活動報名連結旁的繁體說明請保留。
- Gemini expected: 活動報名連結旁的繁體說明請保留。
- Acceptable alternatives: (none)
- Issue tags: over-conversion-guard
- Rationale: 原文已是繁體，且屬於過度轉換保護（over_conversion_guard），應完全保留原樣。

### blind-high-risk-0051

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 医师会根据检查结果调整用药剂量。
- Gemini expected: 醫師會根據檢查結果調整用藥劑量。
- Acceptable alternatives: 醫師會依據檢查結果調整用藥劑量。
- Issue tags: medical_terminology
- Rationale: 將簡體字正確轉換為台灣常用的醫療專業繁體術語（如「醫師」、「調整」與「劑量」）。

### blind-high-risk-0052

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 保险契约应明确说明等待期间。
- Gemini expected: 保險契約應明確說明等待期間。
- Acceptable alternatives: 保險契約應明確說明等待期。
- Issue tags: insurance_terminology
- Rationale: 保險合約在台灣習慣法規上稱為「保險契約」，等待期間（waiting period）亦為台灣保險法規與實務之標準術語。

### blind-high-risk-0053

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 银行会在交易异常时暂停付款指令。
- Gemini expected: 銀行會在交易異常時暫停付款指示。
- Acceptable alternatives: 銀行會在交易異常時暫停付款指令。
- Issue tags: banking_terminology
- Rationale: 台灣金融與銀行交易系統中，payment instruction 常用「付款指示」，「付款指令」亦屬可接受範圍。

### blind-high-risk-0054

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 投资人应确认风险揭露文件内容。
- Gemini expected: 投資人應確認風險揭露文件內容。
- Acceptable alternatives: 投資者應確認風險揭露文件內容。
- Issue tags: investment_terminology
- Rationale: 台灣證券及金融法規用語習慣使用「投資人」與「風險揭露文件」（risk disclosure document）。

### blind-high-risk-0055

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 法院判决确定后，执行程序才会开始。
- Gemini expected: 法院判決確定後，執行程序才會開始。
- Acceptable alternatives: 法院判決確定後，強制執行程序才會開始。
- Issue tags: legal_terminology
- Rationale: 「判決確定」與「執行程序」或「強制執行程序」為台灣民事訴訟與強制執行法之標準法律用語。

### blind-high-risk-0056

- Domain: high_risk
- Risk: baseline_guard
- Confidence: high
- Review needed: True
- Input: 藥品名稱 Panadol 不應被翻譯或改寫。
- Gemini expected: 藥品名稱 Panadol 不應被翻譯或改寫。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard
- Rationale: 原文已為繁體中文，且包含應予保留之英文品牌名稱/專有名詞 Panadol，應維持原樣不予變動。

### blind-high-risk-0057

- Domain: high_risk
- Risk: baseline_guard
- Confidence: high
- Review needed: True
- Input: 请保留病例编号 TW-MED-7788。
- Gemini expected: 請保留病歷編號 TW-MED-7788。
- Acceptable alternatives: 請保留病例編號 TW-MED-7788。
- Issue tags: medical_terminology
- Rationale: 轉換簡體字，且在台灣醫療體系中「病歷」（medical record）比「病例」（medical case）更常搭配「編號/號碼」，同時保留 TW-MED-7788 識別碼。

### blind-high-risk-0058

- Domain: high_risk
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 本繁體醫療聲明已經核准，請勿改寫。
- Gemini expected: 本繁體醫療聲明已經核准，請勿改寫。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard
- Rationale: 輸入文字已完全是繁體中文，應啟動過度轉換防禦，直接維持原樣。

### blind-high-risk-0059

- Domain: high_risk
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 金融契約中的繁體條款應維持原樣。
- Gemini expected: 金融契約中的繁體條款應維持原樣。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard
- Rationale: 輸入文字已完全是繁體中文，應啟動過度轉換防禦，直接維持原樣。

### blind-high-risk-0060

- Domain: high_risk
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 法院公告的繁體案號不得被轉換。
- Gemini expected: 法院公告的繁體案號不得被轉換。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard
- Rationale: 輸入文字已完全是繁體中文，應啟動過度轉換防禦，直接維持原樣。
