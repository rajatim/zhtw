# Holdout Gemini CLI Advisory - blind-v1 batch5 100 cases

Generated: 2026-07-09

This is an independent advisory review. It is not ground truth and must not be promoted without maintainer confirmation.

## Summary

- Total cases: 100
- By domain: {"it": 25, "ui": 20, "llm": 15, "formal": 15, "social": 15, "high_risk": 10}
- By risk: {"candidate_gap": 60, "over_conversion_guard": 25, "baseline_guard": 15}
- By confidence: {"high": 95, "medium": 5}
- Review needed: 39
- Promotion allowed: False

## Cases

### blind-it-0088

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 部署平台会在发布前检查环境变量是否完整。
- Gemini expected: 部署平台會在發布前檢查環境變數是否完整。
- Acceptable alternatives: 部署平台會在發佈前檢查環境變數是否完整。
- Issue tags: technical_term, tw_usage
- Rationale: 環境變數、發布採台灣常用繁體詞彙與字元。

### blind-it-0089

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 这个 SDK 会缓存身份令牌并在过期前刷新。
- Gemini expected: 這個 SDK 會快取身分權杖並在過期前重新整理。
- Acceptable alternatives: 這個 SDK 會快取身分權杖並在過期前更新。
- Issue tags: technical_term, tw_usage
- Rationale: 快取、身分、權杖、重新整理採台灣常用資訊用語，刷新之譯法有重新整理與更新，需人工確認。

### blind-it-0090

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请把错误堆栈写入调试日志。
- Gemini expected: 請把錯誤堆疊寫入偵錯日誌。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 錯誤堆疊、偵錯、日誌採台灣常用資訊用語。

### blind-it-0091

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 服务发现组件会定期更新节点清单。
- Gemini expected: 服務探索元件會定期更新節點清單。
- Acceptable alternatives: 服務發現元件會定期更新節點清單。
- Issue tags: technical_term, tw_usage
- Rationale: 服務探索、元件採台灣常用資訊用語，服務探索與服務發現皆常見，需人工確認。

### blind-it-0092

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 命令行工具支持从配置文件读取默认区域。
- Gemini expected: 命令列工具支援從設定檔讀取預設區域。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 命令列、設定檔、預設採台灣常用資訊用語。

### blind-it-0093

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 代理服务器会把请求转发到内部网关。
- Gemini expected: 代理伺服器會把請求轉送到內部閘道。
- Acceptable alternatives: 代理伺服器會把請求轉發到內部閘道。
- Issue tags: technical_term, tw_usage
- Rationale: 代理伺服器、轉送、閘道採台灣常用資訊用語。

### blind-it-0094

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 请在迁移脚本里新增回滚步骤。
- Gemini expected: 請在遷移指令碼裡新增復原步驟。
- Acceptable alternatives: 請在移轉指令碼裡新增復原步驟。, 請在遷移腳本裡新增復原步驟。
- Issue tags: technical_term, tw_usage
- Rationale: 遷移、指令碼、復原採台灣常用資訊用語，遷移與移轉皆屬常見，需人工確認。

### blind-it-0095

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 当数据库连接失败时，应用会进入只读模式。
- Gemini expected: 當資料庫連線失敗時，應用程式會進入唯讀模式。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 資料庫、連線、應用程式、唯讀採台灣常用資訊用語。

### blind-it-0096

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这个端点会返回上传任务的处理状态。
- Gemini expected: 這個端點會回傳上傳任務的處理狀態。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 端點、回傳採台灣常用資訊用語。

### blind-it-0097

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 构建缓存命中后，流水线可以跳过编译步骤。
- Gemini expected: 建置快取命中後，管線可以略過編譯步驟。
- Acceptable alternatives: 建置快取命中後，管線可以跳過編譯步驟。
- Issue tags: technical_term, tw_usage
- Rationale: 建置快取、管線、略過採台灣常用資訊用語。

### blind-it-0098

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 管理员可以为服务账户轮换密钥。
- Gemini expected: 管理員可以為服務帳戶輪替金鑰。
- Acceptable alternatives: 管理員可以為服務帳戶輪換金鑰。
- Issue tags: technical_term, tw_usage
- Rationale: 服務帳戶、輪替金鑰採台灣常用資訊用語。

### blind-it-0099

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请检查响应主体里的分页游标。
- Gemini expected: 請檢查回應主體裡的分頁游標。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 回應主體、分頁游標採台灣常用資訊用語。

### blind-it-0100

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这个函数会把数组转换成逗号分隔的字符串。
- Gemini expected: 這個函式會把陣列轉換成逗號分隔的字串。
- Acceptable alternatives: 這個函數會把陣列轉換成逗號分隔的字串。
- Issue tags: technical_term, tw_usage
- Rationale: 函式、陣列、字串採台灣常用資訊用語。

### blind-it-0101

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 异步任务失败后会写入重试队列。
- Gemini expected: 非同步任務失敗後會寫入重試佇列。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 非同步、佇列採台灣常用資訊用語。

### blind-it-0102

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 请把静态资源上传到对象存储桶。
- Gemini expected: 請把靜態資源上傳到物件儲存桶。
- Acceptable alternatives: 請把靜態資源上傳到物件儲存體。
- Issue tags: technical_term, tw_usage
- Rationale: 靜態資源、物件儲存桶採台灣常用資訊用語，儲存桶之規格用語需確認。

### blind-it-0103

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 监控面板会显示每分钟请求数。
- Gemini expected: 監控面板會顯示每分鐘請求數。
- Acceptable alternatives: 監控儀表板會顯示每分鐘請求數。
- Issue tags: technical_term, tw_usage
- Rationale: 監控面板採台灣常用資訊用語。

### blind-it-0104

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 权限中间件会验证用户角色。
- Gemini expected: 權限中介軟體會驗證使用者角色。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 中介軟體、使用者採台灣常用資訊用語。

### blind-it-0105

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 容器启动前会先挂载配置卷。
- Gemini expected: 容器啟動前會先掛載設定磁碟區。
- Acceptable alternatives: 容器啟動前會先掛載設定卷。
- Issue tags: technical_term, tw_usage
- Rationale: 掛載、設定磁碟區採台灣常用資訊用語，磁碟區與卷之規格用語需確認。

### blind-it-0106

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 日志中的 TaipeiService 标识必须保持原样。
- Gemini expected: 日誌中的 TaipeiService 識別碼必須保持原樣。
- Acceptable alternatives: 日誌中的 TaipeiService 識別必須保持原樣。, 日誌中的 TaipeiService 標識必須保持原樣。
- Issue tags: technical_term, over_conversion_guard, tw_usage
- Rationale: 過度轉換防護：保留程式碼/英文 TaipeiService，其餘轉台灣常用繁體語彙。

### blind-it-0107

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 请不要翻译 README 里的 CloudToken 参数名。
- Gemini expected: 請不要翻譯 README 裡的 CloudToken 參數名稱。
- Acceptable alternatives: 請不要翻譯 README 裡的 CloudToken 參數名。
- Issue tags: technical_term, over_conversion_guard, tw_usage
- Rationale: 過度轉換防護：保留變數名稱 CloudToken，其餘轉台灣常用繁體語彙。

### blind-it-0108

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 错误样本里的台北节点名称不应改写。
- Gemini expected: 錯誤樣本裡的台北節點名稱不應改寫。
- Acceptable alternatives: 錯誤樣本裡的台北節點名稱不應修改。
- Issue tags: technical_term, over_conversion_guard, tw_usage
- Rationale: 過度轉換防護：保留專名台北，其餘轉台灣常用繁體語彙。

### blind-it-0109

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 配置文件中的 zh_TW_locale 键必须保留。
- Gemini expected: 設定檔中的 zh_TW_locale 鍵必須保留。
- Acceptable alternatives: 設定檔中的 zh_TW_locale 鍵必須保留。
- Issue tags: technical_term, over_conversion_guard, tw_usage
- Rationale: 過度轉換防護：保留變數名稱 zh_TW_locale，其餘轉台灣常用繁體語彙。

### blind-it-0110

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 服务器会记录请求开始和结束时间。
- Gemini expected: 伺服器會記錄請求開始和結束時間。
- Acceptable alternatives: (none)
- Issue tags: technical_term, baseline_guard, tw_usage
- Rationale: 基礎語句以自然台灣繁體為準，伺服器、請求採台灣常用詞彙。

### blind-it-0111

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 安装脚本会建立临时目录。
- Gemini expected: 安裝指令碼會建立暫存目錄。
- Acceptable alternatives: 安裝腳本會建立暫存目錄。, 安裝指令碼會建立臨時目錄。
- Issue tags: technical_term, baseline_guard, tw_usage
- Rationale: 基礎語句以自然台灣繁體為準，安裝指令碼、暫存目錄採台灣常用詞彙。

### blind-it-0112

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 测试报告会列出失败案例。
- Gemini expected: 測試報告會列出失敗案例。
- Acceptable alternatives: (none)
- Issue tags: technical_term, baseline_guard, tw_usage
- Rationale: 基礎語句以自然台灣繁體為準，測試報告、失敗案例採台灣常用詞彙。

### blind-ui-0068

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 设置页面会显示当前订阅方案。
- Gemini expected: 設定頁面會顯示當前訂閱方案。
- Acceptable alternatives: 設定頁面會顯示目前訂閱方案。
- Issue tags: (none)
- Rationale: 「设置」對應「設定」，「页面」對應「頁面」，「当前」對應「當前」或「目前」，「订阅」對應「訂閱」。

### blind-ui-0069

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 点击重试按钮后会重新加载列表。
- Gemini expected: 點擊重試按鈕後會重新載入清單。
- Acceptable alternatives: 點選重試按鈕後會重新載入清單。, 點擊重試按鈕後會重新載入列表。, 點選重試按鈕後會重新載入列表。
- Issue tags: (none)
- Rationale: 「点击」對應「點擊」或「點選」，「加载」對應「載入」，「列表」對應「清單」。

### blind-ui-0070

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 表格支持按更新时间筛选记录。
- Gemini expected: 表格支援依更新時間篩選記錄。
- Acceptable alternatives: 表格支援按更新時間篩選記錄。, 表格支援依更新時間篩選紀錄。, 表格支援按更新時間篩選紀錄。
- Issue tags: (none)
- Rationale: 「支持」對應「支援」，「按」對應「依」或「按」，「筛选」對應「篩選」，「记录」對應「記錄」或「紀錄」。

### blind-ui-0071

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请把确认对话框放在最上层。
- Gemini expected: 請把確認對話框放在最上層。
- Acceptable alternatives: 請把確認對話方塊放在最上層。
- Issue tags: (none)
- Rationale: 「对话框」對應「對話框」或「對話方塊」，「最上层」對應「最上層」。

### blind-ui-0072

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 搜索框会保存最近输入的关键词。
- Gemini expected: 搜尋框會儲存最近輸入的關鍵字。
- Acceptable alternatives: 搜尋框會保存最近輸入的關鍵字。
- Issue tags: (none)
- Rationale: 「搜索框」對應「搜尋框」，「保存」在 UI 語境對應「儲存」或「保存」，「关键词」對應「關鍵字」。

### blind-ui-0073

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 分页控件会显示总页数。
- Gemini expected: 分頁控制項會顯示總頁數。
- Acceptable alternatives: 分頁元件會顯示總頁數。
- Issue tags: (none)
- Rationale: 「分页控件」對應「分頁控制項」，「显示」對應「顯示」，「总页数」對應「總頁數」。

### blind-ui-0074

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 拖动列标题可以调整显示顺序。
- Gemini expected: 拖曳欄位標題可以調整顯示順序。
- Acceptable alternatives: 拖曳欄標題可以調整顯示順序。, 拖曳列標題可以調整顯示順序。
- Issue tags: (none)
- Rationale: 「拖动」對應「拖曳」，表格的「列」（column）在台灣習慣稱為「欄」，「列标题」對應「欄位標題」或「欄標題」。

### blind-ui-0075

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 上传区域会显示文件大小限制。
- Gemini expected: 上傳區域會顯示檔案大小限制。
- Acceptable alternatives: 上傳區域會顯示檔案大小限制
- Issue tags: (none)
- Rationale: 「上传」對應「上傳」，「文件大小」對應「檔案大小」。

### blind-ui-0076

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 错误提示会在输入框失焦后出现。
- Gemini expected: 錯誤提示會在輸入框失焦後出現。
- Acceptable alternatives: 錯誤提示會在輸入框失去焦點後出現。, 錯誤提示會在輸入框離開焦點後出現。
- Issue tags: (none)
- Rationale: 「失焦」對應「失焦」或「失去焦點」，「输入框」對應「輸入框」，「出现」對應「出現」。

### blind-ui-0077

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 用户可以在侧边栏固定常用项目。
- Gemini expected: 使用者可以在側邊欄固定常用項目。
- Acceptable alternatives: 用戶可以在側邊欄固定常用項目。
- Issue tags: (none)
- Rationale: 「用户」對應「使用者」或「用戶」，「侧边栏」對應「側邊欄」，「项目」對應「項目」。

### blind-ui-0078

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 下拉菜单会根据权限隐藏选项。
- Gemini expected: 下拉式選單會根據權限隱藏選項。
- Acceptable alternatives: 下拉選單會根據權限隱藏選項。
- Issue tags: (none)
- Rationale: 「下拉菜单」對應「下拉式選單」或「下拉選單」，「根据」對應「根據」，「权限」對應「權限」。

### blind-ui-0079

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 通知中心会按时间倒序排列消息。
- Gemini expected: 通知中心會依時間倒序排列訊息。
- Acceptable alternatives: 通知中心會按時間倒序排列訊息。, 通知中心會依時間反序排列訊息。
- Issue tags: (none)
- Rationale: 「按」對應「依」或「按」，「消息」對應「訊息」。

### blind-ui-0080

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 按钮标签里的 Taiwan Pass 不要翻译。
- Gemini expected: 按鈕標籤裡的 Taiwan Pass 不要翻譯。
- Acceptable alternatives: 按鈕標籤中的 Taiwan Pass 不要翻譯。
- Issue tags: (none)
- Rationale: 「Taiwan Pass」為英文專有名詞，應維持原樣不翻譯，其他詞彙正常轉換為台灣繁體。

### blind-ui-0081

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 示例账号 TaipeiAdmin 必须维持原样。
- Gemini expected: 範例帳號 TaipeiAdmin 必須維持原樣。
- Acceptable alternatives: 範例帳號 TaipeiAdmin 必須維持原貌。
- Issue tags: (none)
- Rationale: 「示例」對應「範例」，「账号」對應「帳號」，「TaipeiAdmin」為英文標示應維持原文。

### blind-ui-0082

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 占位符里的 user_name 变量不应转换。
- Gemini expected: 預留位置裡的 user_name 變數不應轉換。
- Acceptable alternatives: 預留位置中的 user_name 變數不應轉換。, 佔位符裡的 user_name 變數不應轉換。
- Issue tags: (none)
- Rationale: 「占位符」對應「預留位置」，「user_name」為變數名稱不應轉換，「变量」對應「變數」。

### blind-ui-0083

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 页面标题中的台中活动保持原文。
- Gemini expected: 頁面標題中的台中活動保持原文。
- Acceptable alternatives: 頁面標題中的臺中活動保持原文。
- Issue tags: (none)
- Rationale: 「台中」通常轉換為「臺中」，但在此句中指定保持原文，故可維持「台中」或轉換為「臺中」。

### blind-ui-0084

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 请保留按钮上的 Beta 字样。
- Gemini expected: 請保留按鈕上的 Beta 字樣。
- Acceptable alternatives: 請保留按鈕上的 Beta 字樣。
- Issue tags: (none)
- Rationale: 「Beta」字樣為英文專有名詞保持原樣，其餘轉換。

### blind-ui-0085

- Domain: ui
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 页面加载完成后会隐藏骨架画面。
- Gemini expected: 頁面載入完成後會隱藏骨架畫面。
- Acceptable alternatives: 頁面加載完成後會隱藏骨架畫面。
- Issue tags: (none)
- Rationale: 「骨架画面」在台灣習慣稱為「骨架畫面」，「加载」對應「載入」。

### blind-ui-0086

- Domain: ui
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 开关关闭时不会发送提醒。
- Gemini expected: 開關關閉時不會傳送提醒。
- Acceptable alternatives: 開關關閉時不會發送提醒。
- Issue tags: (none)
- Rationale: 「开关」對應「開關」，「发送」對應「傳送」或「發送」。

### blind-ui-0087

- Domain: ui
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 二维码失效后会显示提示文字。
- Gemini expected: QR Code 失效後會顯示提示文字。
- Acceptable alternatives: 二維條碼失效後會顯示提示文字。, 二維碼失效後會顯示提示文字。
- Issue tags: (none)
- Rationale: 「二维码」對應「QR Code」或「二維條碼」。

### blind-llm-0048

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 模型摘要会列出三点主要结论。
- Gemini expected: 模型摘要會列出三點主要結論。
- Acceptable alternatives: (none)
- Issue tags: regional_term
- Rationale: 常規繁簡轉換，『會』轉為『會』，『三点』轉為『三點』，『结论』轉為『結論』。

### blind-llm-0049

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请让助理用条列方式回答问题。
- Gemini expected: 請讓助理用條列方式回答問題。
- Acceptable alternatives: (none)
- Issue tags: regional_term
- Rationale: 常規轉換，『請』、『讓』、『條列』、『問題』。

### blind-llm-0050

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 系统提示词要求先确认用户意图。
- Gemini expected: 系統提示詞要求先確認使用者意圖。
- Acceptable alternatives: 系統提示詞要求先確認用戶意圖。
- Issue tags: it_term, regional_term
- Rationale: 『系统提示词』轉為『系統提示詞』；『用户』轉換為台灣 IT 習慣的『使用者』，意圖轉為『意圖』。

### blind-llm-0051

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这个代理会读取工具返回的 JSON 结果。
- Gemini expected: 這個代理會讀取工具回傳的 JSON 結果。
- Acceptable alternatives: 這個代理會讀取工具傳回的 JSON 結果。
- Issue tags: it_term, regional_term
- Rationale: 『代理』在台灣語境下常用；『返回』對應台灣 IT 語境的『回傳』或『傳回』，『JSON』保留。

### blind-llm-0052

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请把长段落改写成客服回复。
- Gemini expected: 請把長段落改寫成客服回覆。
- Acceptable alternatives: 請將長段落改寫成客服回覆。
- Issue tags: regional_term
- Rationale: 『请』轉為『請』；『回复』在客訴/通訊語境下對應台灣習慣的『回覆』。

### blind-llm-0053

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 检索结果会附上来源编号。
- Gemini expected: 檢索結果會附上來源編號。
- Acceptable alternatives: (none)
- Issue tags: regional_term
- Rationale: 常規 IT/LLM 詞彙轉換：『檢索』、『結果』、『會』、『來源』、『編號』。

### blind-llm-0054

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 提示模板会插入用户上传的文件名。
- Gemini expected: 提示範本會插入使用者上傳的檔名。
- Acceptable alternatives: 提示範本會插入使用者上傳的檔案名稱。
- Issue tags: it_term, regional_term
- Rationale: 『模板』轉為『範本』，『用户』轉為『使用者』，『文件名』轉為『檔名』或『檔案名稱』。

### blind-llm-0055

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 聊天记录会保留最近五轮对话。
- Gemini expected: 聊天記錄會保留最近五輪對話。
- Acceptable alternatives: 聊天紀錄會保留最近五輪對話。
- Issue tags: regional_term
- Rationale: 『聊天记录』對應台灣習慣的『聊天記錄』或『聊天紀錄』，『对话』轉為『對話』。

### blind-llm-0056

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 评估脚本会比较模型输出和人工答案。
- Gemini expected: 評估指令碼會比較模型輸出和人工答案。
- Acceptable alternatives: 評估腳本會比較模型輸出和人工答案。
- Issue tags: it_term, regional_term
- Rationale: 『评估』轉為『評估』；『脚本』轉為台灣 IT 習慣的『指令碼』（亦可接受『腳本』）。

### blind-llm-0057

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 提示词里的 TaipeiBot 名称不得改写。
- Gemini expected: 提示詞裡的 TaipeiBot 名稱不得改寫。
- Acceptable alternatives: 提示詞中的 TaipeiBot 名稱不得改寫。
- Issue tags: over_conversion_guard
- Rationale: 『TaipeiBot』為專有名詞，應完整保留大小寫及英文；『里』對應『裡』。

### blind-llm-0058

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 请保留 Markdown 表格中的 zhTW 字段。
- Gemini expected: 請保留 Markdown 表格中的 zhTW 欄位。
- Acceptable alternatives: (none)
- Issue tags: it_term, over_conversion_guard
- Rationale: 『Markdown』與『zhTW』為代碼及特定標記應予保留；『字段』轉為台灣 IT 術語的『欄位』。

### blind-llm-0059

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 引用标题里的台湾 AI 年会保持原样。
- Gemini expected: 引用標題裡的台灣 AI 年會保持原樣。
- Acceptable alternatives: 引用標題裡的臺灣 AI 年會保持原樣。, 引用標題中的台灣 AI 年會保持原樣。
- Issue tags: over_conversion_guard, regional_term
- Rationale: 『AI』為專有名詞英文，應保留；『台湾』轉換為『台灣』或『臺灣』；『标题』轉為『標題』。

### blind-llm-0060

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 变量 assistant_name 不应该被翻译。
- Gemini expected: 變數 assistant_name 不應該被翻譯。
- Acceptable alternatives: 變數 assistant_name 不應被翻譯。
- Issue tags: it_term, over_conversion_guard
- Rationale: 『assistant_name』為變數代號，應保留；『变量』轉為台灣術語的『變數』。

### blind-llm-0061

- Domain: llm
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 回答前请先阅读用户提供的上下文。
- Gemini expected: 回答前請先閱讀使用者提供的上下文。
- Acceptable alternatives: 回答前請先閱讀使用者提供的脈絡。
- Issue tags: regional_term
- Rationale: 『用户』轉換為台灣習慣的『使用者』；『阅读』轉為『閱讀』；『上下文』在 IT/LLM 語境下保留為『上下文』。

### blind-llm-0062

- Domain: llm
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 如果资料不足，请说明无法判断。
- Gemini expected: 如果資料不足，請說明無法判斷。
- Acceptable alternatives: (none)
- Issue tags: regional_term
- Rationale: 『资料』轉換為台灣常用的『資料』；『说明』轉為『說明』；『无法判断』轉為『無法判斷』。

### blind-formal-0049

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 主管机关将于月底公布审查结果。
- Gemini expected: 主管機關將於月底公布審查結果。
- Acceptable alternatives: 主管機關將於月底公佈審查結果。
- Issue tags: formal_term, regional_term
- Rationale: 將「主管机关」轉換為台灣常用之「主管機關」（正式用語），「将于」轉換為「將於」，「公布」在台灣公務標準中較「公佈」常見，但也保留「公佈」為可接受寫法。

### blind-formal-0050

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 申请文件须附最近三个月的缴费证明。
- Gemini expected: 申請文件須附最近三個月的繳費證明。
- Acceptable alternatives: 申請文件需附最近三個月的繳費證明。
- Issue tags: formal_term, regional_term
- Rationale: 將「申请」轉換為「申請」，「须」轉換為「須」（或「需」），「三个月」轉換為「三個月」，「缴费证明」轉換為「繳費證明」。因涉及財務繳費證明文件，標記為需人工審查。

### blind-formal-0051

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 本条例修正案预计下会期审议。
- Gemini expected: 本條例修正案預計下會期審議。
- Acceptable alternatives: (none)
- Issue tags: formal_term, regional_term
- Rationale: 將「条例」轉換為「條例」，「预计」轉換為「預計」，「会期」轉換為「會期」，「审议」轉換為「審議」，均為標準之繁體字轉換。

### blind-formal-0052

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 新闻稿指出合作计划不会影响既有权益。
- Gemini expected: 新聞稿指出合作計畫不會影響既有權益。
- Acceptable alternatives: 新聞稿指出合作計劃不會影響既有權益。
- Issue tags: formal_term, regional_term
- Rationale: 將「新闻稿」轉換為「新聞稿」，「计划」依台灣公文標準轉換為「計畫」（「計劃」亦為常見可接受寫法），「不会」轉換為「不會」，「影响」轉換為「影響」，「权益」轉換為「權益」。

### blind-formal-0053

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 会议资料将同步上传至机关网站。
- Gemini expected: 會議資料將同步上傳至機關網站。
- Acceptable alternatives: (none)
- Issue tags: formal_term, it_term, regional_term
- Rationale: 將「会议资料」轉換為「會議資料」，「将」轉換為「將」，「上传」轉換為「上傳」，「机关」轉換為「機關」，「网站」轉換為「網站」。

### blind-formal-0054

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 承办单位应在期限内完成补正通知。
- Gemini expected: 承辦單位應在期限內完成補正通知。
- Acceptable alternatives: (none)
- Issue tags: formal_term, regional_term
- Rationale: 將「承办单位」轉換為「承辦單位」，「应」轉換為「應」，「内」轉換為「內」，「补正」轉換為「補正」。

### blind-formal-0055

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 调查报告建议提高资料保存年限。
- Gemini expected: 調查報告建議提高資料保存年限。
- Acceptable alternatives: 調查報告建議提高數據保存年限。
- Issue tags: formal_term, regional_term
- Rationale: 將「调查报告」轉換為「調查報告」，「建议」轉換為「建議」，「资料」轉換為台灣常用的「資料」（「數據」在此語境中亦為可接受譯法），「保存年限」轉為繁體。

### blind-formal-0056

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 公司应于股东会前寄发议事手册。
- Gemini expected: 公司應於股東會前寄發議事手冊。
- Acceptable alternatives: (none)
- Issue tags: formal_term, regional_term
- Rationale: 將「应于」轉換為「應於」，「股东会前」轉換為「股東會前」，「寄发」轉換為「寄發」，「议事手册」轉換為「議事手冊」，皆為標準公文法規繁體化。

### blind-formal-0057

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 附件中的 Taipei Office 名称不得翻译。
- Gemini expected: 附件中的 Taipei Office 名稱不得翻譯。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, english_term
- Rationale: 英文專專有名詞「Taipei Office」應保持原文，不得翻譯或轉換，僅將周邊字詞「名称」轉為「名稱」、「翻译」轉為「翻譯」。因含有特別防護指令，標記為需人工確認。

### blind-formal-0058

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 法规标题中的台湾关系法保持原文。
- Gemini expected: 法規標題中的台灣關係法保持原文。
- Acceptable alternatives: 法規標題中的臺灣關係法保持原文。
- Issue tags: over_conversion_guard, regional_term
- Rationale: 「保持原文」在語境中指不應翻譯成英文名，故仍將中文字轉換為台灣繁體（「法规标题」->「法規標題」）。台灣官方標準寫法常作「臺灣關係法」（故列為可接受），日常及多數情境下「台灣關係法」極其通用（設為預期）。

### blind-formal-0059

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 请保留公告里的 Taichung Branch 英文名称。
- Gemini expected: 請保留公告裡的 Taichung Branch 英文名稱。
- Acceptable alternatives: (none)
- Issue tags: over_conversion_guard, english_term
- Rationale: 英文專有名詞「Taichung Branch」應保持原文不予更動，僅將周邊字詞「请」->「請」、「里」->「裡」（亦有「里」但「公告裡」表內部，用「裡」較佳）、「名称」->「名稱」做轉換。

### blind-formal-0060

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 会议纪录中的 #台北专案 标签不应改写。
- Gemini expected: 會議紀錄中的 #台北專案 標籤不應改寫。
- Acceptable alternatives: 會議紀錄中的 #臺北專案 標籤不應改寫。, 會議記錄中的 #台北專案 標籤不應改寫。, 會議記錄中的 #臺北專案 標籤不應改寫。
- Issue tags: over_conversion_guard, regional_term
- Rationale: 標籤「#台北专案」應保留 hashtag 形式並將文字轉為台灣繁體「#台北專案」或「#臺北專案」。「会议纪录」在台灣多用「紀錄」，但「記錄」亦屬通用，皆列入可接受範圍。

### blind-formal-0061

- Domain: formal
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 本案经审查后准予备案。
- Gemini expected: 本案經審查後准予備案。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, over_conversion_guard
- Rationale: 將「经」轉換為「經」，「审查后」轉換為「審查後」，「备案」轉換為「備案」。特別注意「准予」的「准」為許可之意，不應過度轉換為「準」，須精準保留「准」字。

### blind-formal-0062

- Domain: formal
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 相关单位应配合后续稽查。
- Gemini expected: 相關單位應配合後續稽查。
- Acceptable alternatives: (none)
- Issue tags: baseline_guard, regional_term
- Rationale: 將「相关」轉換為「相關」，「单位」轉換為「單位」，「应」轉換為「應」，「后续」轉換為「後續」，語意非常明確且無歧義。

### blind-formal-0063

- Domain: formal
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 公告内容自发布日起生效。
- Gemini expected: 公告內容自發布日起生效。
- Acceptable alternatives: 公告內容自發佈日起生效。
- Issue tags: baseline_guard, regional_term
- Rationale: 將「内容」轉換為「內容」。「发布日」在台灣法規與官方公文書中常用「發布日」，但常民與大眾媒體常混用「發佈日」，故列為可接受寫法。

### blind-social-0049

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 我晚点再把订位信息传给你。
- Gemini expected: 我晚點再把訂位資訊傳給你。
- Acceptable alternatives: 我晚點再把訂位訊息傳給你。, 我晚一點再把訂位資訊傳給你。
- Issue tags: colloquial_register, tw_usage
- Rationale: 「晚點」為口語常用詞，「資訊」與「訊息」皆為台灣對應「信息」之常用詞彙。

### blind-social-0050

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这家店的评价比上个月好多了。
- Gemini expected: 這家店的評價比上個月好多了。
- Acceptable alternatives: (none)
- Issue tags: colloquial_register, tw_usage
- Rationale: 日常用語之字元繁體化（這、評價、個月），符合台灣日常習慣。

### blind-social-0051

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 你可以先把购物车里的东西结账。
- Gemini expected: 你可以先把購物車裡的東西結帳。
- Acceptable alternatives: 你可以先把購物車中的東西結帳。
- Issue tags: colloquial_register, tw_usage
- Rationale: 「購物車」與「結帳」為台灣電子商務標準用語，「裡」為內空間標準字。

### blind-social-0052

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 朋友说这部剧的结局很催泪。
- Gemini expected: 朋友說這部劇的結局很催淚。
- Acceptable alternatives: 朋友說這部影集的結局很催淚。
- Issue tags: colloquial_register, tw_usage
- Rationale: 「劇」在台灣日常口語（如追劇）中極為常用，保留「這部劇」之譯法，同時容許「影集」作為替代詞。

### blind-social-0053

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 我已经把聚餐照片上传到相册。
- Gemini expected: 我已經把聚餐照片上傳到相簿。
- Acceptable alternatives: 我已經把聚餐照片上傳到相冊。
- Issue tags: colloquial_register, tw_usage
- Rationale: 「相簿」為台灣日常口語及系統介面最常用詞（如相簿功能），「相冊」亦屬可接受範圍。

### blind-social-0054

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 群组公告提醒大家准时到场。
- Gemini expected: 群組公告提醒大家準時到場。
- Acceptable alternatives: (none)
- Issue tags: colloquial_register, tw_usage
- Rationale: 群組、公告、準時、到場皆為台灣標準用語，進行純字元轉換即可。

### blind-social-0055

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请把路线链接发到聊天室。
- Gemini expected: 請把路線連結傳到聊天室。
- Acceptable alternatives: 請把路線連結發到聊天室。
- Issue tags: colloquial_register, tw_usage
- Rationale: 「連結」對應簡體「链接」為台灣網路標準術語，「傳到聊天室」較「發到」更符合台灣口語習慣。

### blind-social-0056

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这条动态的留言已经关闭。
- Gemini expected: 這則動態的留言已經關閉。
- Acceptable alternatives: 這篇動態的留言已經關閉。, 這條動態的留言已經關閉。
- Issue tags: colloquial_register, tw_usage
- Rationale: 台灣對於社群貼文（動態）的量詞習慣使用「則」或「篇」，「條」亦可接受但較不口語。

### blind-social-0057

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 照片说明里的台南小吃保持原样。
- Gemini expected: 照片說明裡的台南小吃保持原樣。
- Acceptable alternatives: 照片說明裡的臺南小吃保持原樣。
- Issue tags: colloquial_register, over_conversion_guard, tw_usage
- Rationale: 「台南」本身在台灣已被廣泛使用，為避免過度轉換（如強制改為臺），保留原形並將「臺南」列為可接受寫法。

### blind-social-0058

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 昵称 TaipeiWalker 不要自动翻译。
- Gemini expected: 暱稱 TaipeiWalker 不要自動翻譯。
- Acceptable alternatives: (none)
- Issue tags: colloquial_register, over_conversion_guard, tw_usage
- Rationale: 保留英文暱稱「TaipeiWalker」不予翻譯，僅轉換周邊文字（暱稱、自動、翻譯）。

### blind-social-0059

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 请保留朋友写的 Happy Taiwan Day。
- Gemini expected: 請保留朋友寫的 Happy Taiwan Day。
- Acceptable alternatives: (none)
- Issue tags: colloquial_register, over_conversion_guard, tw_usage
- Rationale: 保留英文祝賀片段「Happy Taiwan Day」不予翻譯，僅轉換周邊簡體字。

### blind-social-0060

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 标签 #台湾旅行 不要被改成其他词。
- Gemini expected: 標籤 #台灣旅行 不要被改成其他詞。
- Acceptable alternatives: 標籤 #臺灣旅行 不要被改成其他詞。
- Issue tags: colloquial_register, over_conversion_guard, tw_usage
- Rationale: 主題標籤中的「台湾」轉為繁體「台灣」或「臺灣」，不更改「旅行」一詞，其餘字元（標籤、被、改、詞）正確繁體化。

### blind-social-0061

- Domain: social
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 明天晚上我们一起看电影。
- Gemini expected: 明天晚上我們一起看電影。
- Acceptable alternatives: (none)
- Issue tags: colloquial_register, baseline_guard, tw_usage
- Rationale: 基礎日常句字元轉換，無特定習慣或學術術語歧義。

### blind-social-0062

- Domain: social
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 这件外套的颜色很好看。
- Gemini expected: 這件外套的顏色很好看。
- Acceptable alternatives: (none)
- Issue tags: colloquial_register, baseline_guard, tw_usage
- Rationale: 日常一般語句，無特定用語轉換，直接轉為台灣常用繁體字元。

### blind-social-0063

- Domain: social
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 我先去便利店买早餐。
- Gemini expected: 我先去便利商店買早餐。
- Acceptable alternatives: 我先去超商買早餐。, 我先去便利店買早餐。
- Issue tags: colloquial_register, baseline_guard, tw_usage
- Rationale: 「便利店」在台灣的典型、道地說法為「便利商店」或「超商」，進行語意化調整以符合在地習慣。

### blind-high-risk-0031

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 医师应向患者说明手术风险和替代方案。
- Gemini expected: 醫師應向患者說明手術風險和替代方案。
- Acceptable alternatives: 醫師應向病患說明手術風險和替代方案。
- Issue tags: high_risk_domain, tw_usage
- Rationale: 「醫師」、「說明」、「手術」、「風險」、「替代方案」皆為台灣標準醫療語境用語。「患者」與「病患」在台灣醫療情境均通用，保留字面轉換之「患者」為首選，而「病患」亦完全可接受。

### blind-high-risk-0032

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 保险公司须在期限内回复理赔申请。
- Gemini expected: 保險公司須在期限內回覆理賠申請。
- Acceptable alternatives: 保險公司需在期限內回覆理賠申請。, 保險公司須在期限內答覆理賠申請。
- Issue tags: high_risk_domain, tw_usage
- Rationale: 「保險」、「須」、「期限內」、「回覆」、「理賠」、「申請」皆為台灣標準法律與保險公文語彙。

### blind-high-risk-0033

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 银行不得在未告知前提下调整手续费。
- Gemini expected: 銀行不得在未告知前提下調整手續費。
- Acceptable alternatives: 銀行不得在未告知情況下調整手續費。
- Issue tags: high_risk_domain, tw_usage
- Rationale: 「銀行」、「調整」、「手續費」為標準金融用語，其餘字詞字面轉換正確且語意清晰。

### blind-high-risk-0034

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 契约解除通知应以书面送达。
- Gemini expected: 契約解除通知應以書面送達。
- Acceptable alternatives: (none)
- Issue tags: high_risk_domain, tw_usage
- Rationale: 「契約」、「解除」、「書面」、「送達」皆為台灣民法體系標準法律術語，無歧義。

### blind-high-risk-0035

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 药品说明应列明常见副作用。
- Gemini expected: 藥品說明應列明常見副作用。
- Acceptable alternatives: 藥品說明應載明常見副作用。, 藥品說明應標明常見副作用。
- Issue tags: high_risk_domain, tw_usage
- Rationale: 「藥品」、「說明」、「常見」、「副作用」皆為標準台灣醫藥用語。「列明」在告示與法規情境也常表述為「載明」或「標明」。

### blind-high-risk-0036

- Domain: high_risk
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 病例编号 TW-Clinic-01 不得自动转换。
- Gemini expected: 病例編號 TW-Clinic-01 不得自動轉換。
- Acceptable alternatives: 病歷編號 TW-Clinic-01 不得自動轉換。
- Issue tags: high_risk_domain, over_conversion_guard, tw_usage
- Rationale: 保護英文編碼「TW-Clinic-01」不被轉換，其餘字詞正確轉換。「病例」與「病歷」在不同情境皆適用，前者著重個案，後者著重病史紀錄。

### blind-high-risk-0037

- Domain: high_risk
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 契约中的 Taipei Holdings 名称应保持原样。
- Gemini expected: 契約中的 Taipei Holdings 名稱應保持原樣。
- Acceptable alternatives: 契約中的 Taipei Holdings 名稱應保持原貌。
- Issue tags: high_risk_domain, over_conversion_guard, tw_usage
- Rationale: 完整保留英文專利/公司名稱「Taipei Holdings」，其餘周邊簡體字「契約」、「名稱」、「應」、「原樣」正確轉換。

### blind-high-risk-0038

- Domain: high_risk
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 汇款附言里的 Taiwan Relief Fund 不需翻译。
- Gemini expected: 匯款附言裡的 Taiwan Relief Fund 不需翻譯。
- Acceptable alternatives: 匯款備註裡的 Taiwan Relief Fund 不需翻譯。, 匯款留言裡的 Taiwan Relief Fund 不需翻譯。
- Issue tags: high_risk_domain, over_conversion_guard, tw_usage
- Rationale: 保留英文專有名詞「Taiwan Relief Fund」不變。台灣金融匯款情境常以「備註」或「留言」代替「附言」，故列入可接受欄位。

### blind-high-risk-0039

- Domain: high_risk
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 病历附件里的台北院区代码不可改写。
- Gemini expected: 病歷附件裡的台北院區代碼不可改寫。
- Acceptable alternatives: 病歷附件裡的臺北院區代碼不可改寫。
- Issue tags: high_risk_domain, over_conversion_guard, tw_usage
- Rationale: 「病歷」、「院區」、「代碼」、「改寫」為標準台灣用法。「台北」與「臺北」在台灣皆通用，預設保留原文字面，並將「臺北」列為可接受選項。

### blind-high-risk-0040

- Domain: high_risk
- Risk: baseline_guard
- Confidence: high
- Review needed: True
- Input: 申请人应亲自签署授权书。
- Gemini expected: 申請人應親自簽署授權書。
- Acceptable alternatives: (none)
- Issue tags: high_risk_domain, baseline_guard, tw_usage
- Rationale: 「申請人」、「親自」、「簽署」、「授權書」皆為台灣標準法律文書用語，轉換極為明確。
