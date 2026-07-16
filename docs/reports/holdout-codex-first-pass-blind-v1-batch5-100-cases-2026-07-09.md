# Holdout Codex First-Pass Advisory - blind-v1 batch5 100 cases

Generated: 2026-07-09

This is an advisory first pass only. It is not ground truth and must not be promoted without maintainer confirmation.

## Summary

- Total cases: 100
- By domain: {"it": 25, "ui": 20, "llm": 15, "formal": 15, "social": 15, "high_risk": 10}
- By risk: {"candidate_gap": 60, "over_conversion_guard": 25, "baseline_guard": 15}
- By confidence: {"high": 80, "medium": 20}
- Review needed: 46
- Promotion allowed: False

## Cases

### blind-it-0088

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 部署平台会在发布前检查环境变量是否完整。
- Codex expected: 部署平台會在發布前檢查環境變數是否完整。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0089

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 这个 SDK 会缓存身份令牌并在过期前刷新。
- Codex expected: 這個 SDK 會快取身分權杖並在過期前重新整理。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0090

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请把错误堆栈写入调试日志。
- Codex expected: 請把錯誤堆疊寫入偵錯日誌。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0091

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 服务发现组件会定期更新节点清单。
- Codex expected: 服務探索元件會定期更新節點清單。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0092

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 命令行工具支持从配置文件读取默认区域。
- Codex expected: 命令列工具支援從設定檔讀取預設區域。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0093

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 代理服务器会把请求转发到内部网关。
- Codex expected: 代理伺服器會把請求轉送到內部閘道。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0094

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 请在迁移脚本里新增回滚步骤。
- Codex expected: 請在移轉指令碼裡新增復原步驟。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0095

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 当数据库连接失败时，应用会进入只读模式。
- Codex expected: 當資料庫連線失敗時，應用程式會進入唯讀模式。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0096

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这个端点会返回上传任务的处理状态。
- Codex expected: 這個端點會回傳上傳任務的處理狀態。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0097

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 构建缓存命中后，流水线可以跳过编译步骤。
- Codex expected: 建置快取命中後，管線可以略過編譯步驟。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0098

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 管理员可以为服务账户轮换密钥。
- Codex expected: 管理員可以為服務帳戶輪替金鑰。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0099

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请检查响应主体里的分页游标。
- Codex expected: 請檢查回應主體裡的分頁游標。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0100

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这个函数会把数组转换成逗号分隔的字符串。
- Codex expected: 這個函式會把陣列轉換成逗號分隔的字串。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0101

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 异步任务失败后会写入重试队列。
- Codex expected: 非同步任務失敗後會寫入重試佇列。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0102

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 请把静态资源上传到对象存储桶。
- Codex expected: 請把靜態資源上傳到物件儲存桶。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0103

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 监控面板会显示每分钟请求数。
- Codex expected: 監控面板會顯示每分鐘請求數。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0104

- Domain: it
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 权限中间件会验证用户角色。
- Codex expected: 權限中介軟體會驗證使用者角色。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0105

- Domain: it
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 容器启动前会先挂载配置卷。
- Codex expected: 容器啟動前會先掛載設定磁碟區。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-it-0106

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 日志中的 TaipeiService 标识必须保持原样。
- Codex expected: 日誌中的 TaipeiService 識別碼必須保持原樣。
- Acceptable alternatives: (none)
- Issue tags: technical_term, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-it-0107

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 请不要翻译 README 里的 CloudToken 参数名。
- Codex expected: 請不要翻譯 README 裡的 CloudToken 參數名稱。
- Acceptable alternatives: (none)
- Issue tags: technical_term, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-it-0108

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 错误样本里的台北节点名称不应改写。
- Codex expected: 錯誤樣本裡的台北節點名稱不應改寫。
- Acceptable alternatives: (none)
- Issue tags: technical_term, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-it-0109

- Domain: it
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 配置文件中的 zh_TW_locale 键必须保留。
- Codex expected: 設定檔中的 zh_TW_locale 鍵必須保留。
- Acceptable alternatives: (none)
- Issue tags: technical_term, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-it-0110

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 服务器会记录请求开始和结束时间。
- Codex expected: 伺服器會記錄請求開始和結束時間。
- Acceptable alternatives: (none)
- Issue tags: technical_term, baseline_guard, tw_usage
- Rationale: 基礎語句以自然台灣繁體為準，避免加入過度領域詞。

### blind-it-0111

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 安装脚本会建立临时目录。
- Codex expected: 安裝指令碼會建立暫存目錄。
- Acceptable alternatives: (none)
- Issue tags: technical_term, baseline_guard, tw_usage
- Rationale: 基礎語句以自然台灣繁體為準，避免加入過度領域詞。

### blind-it-0112

- Domain: it
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 测试报告会列出失败案例。
- Codex expected: 測試報告會列出失敗案例。
- Acceptable alternatives: (none)
- Issue tags: technical_term, baseline_guard, tw_usage
- Rationale: 基礎語句以自然台灣繁體為準，避免加入過度領域詞。

### blind-ui-0068

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 设置页面会显示当前订阅方案。
- Codex expected: 設定頁面會顯示目前訂閱方案。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0069

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 点击重试按钮后会重新加载列表。
- Codex expected: 點選重試按鈕後會重新載入清單。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0070

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 表格支持按更新时间筛选记录。
- Codex expected: 表格支援依更新時間篩選記錄。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0071

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请把确认对话框放在最上层。
- Codex expected: 請把確認對話框放在最上層。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0072

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 搜索框会保存最近输入的关键词。
- Codex expected: 搜尋框會儲存最近輸入的關鍵字。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0073

- Domain: ui
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 分页控件会显示总页数。
- Codex expected: 分頁控制項會顯示總頁數。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0074

- Domain: ui
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 拖动列标题可以调整显示顺序。
- Codex expected: 拖曳欄標題可以調整顯示順序。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0075

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 上传区域会显示文件大小限制。
- Codex expected: 上傳區域會顯示檔案大小限制。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0076

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 错误提示会在输入框失焦后出现。
- Codex expected: 錯誤提示會在輸入框失焦後出現。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0077

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 用户可以在侧边栏固定常用项目。
- Codex expected: 使用者可以在側邊欄釘選常用項目。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0078

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 下拉菜单会根据权限隐藏选项。
- Codex expected: 下拉式選單會根據權限隱藏選項。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0079

- Domain: ui
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 通知中心会按时间倒序排列消息。
- Codex expected: 通知中心會依時間倒序排列訊息。
- Acceptable alternatives: (none)
- Issue tags: ui_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-ui-0080

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 按钮标签里的 Taiwan Pass 不要翻译。
- Codex expected: 按鈕標籤裡的 Taiwan Pass 不要翻譯。
- Acceptable alternatives: (none)
- Issue tags: ui_term, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-ui-0081

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 示例账号 TaipeiAdmin 必须维持原样。
- Codex expected: 範例帳號 TaipeiAdmin 必須維持原樣。
- Acceptable alternatives: (none)
- Issue tags: ui_term, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-ui-0082

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 占位符里的 user_name 变量不应转换。
- Codex expected: 預留位置裡的 user_name 變數不應轉換。
- Acceptable alternatives: (none)
- Issue tags: ui_term, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-ui-0083

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 页面标题中的台中活动保持原文。
- Codex expected: 頁面標題中的台中活動保持原文。
- Acceptable alternatives: (none)
- Issue tags: ui_term, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-ui-0084

- Domain: ui
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 请保留按钮上的 Beta 字样。
- Codex expected: 請保留按鈕上的 Beta 字樣。
- Acceptable alternatives: (none)
- Issue tags: ui_term, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-ui-0085

- Domain: ui
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 页面加载完成后会隐藏骨架画面。
- Codex expected: 頁面載入完成後會隱藏骨架畫面。
- Acceptable alternatives: (none)
- Issue tags: ui_term, baseline_guard, tw_usage
- Rationale: 基礎語句以自然台灣繁體為準，避免加入過度領域詞。

### blind-ui-0086

- Domain: ui
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 开关关闭时不会发送提醒。
- Codex expected: 開關關閉時不會傳送提醒。
- Acceptable alternatives: (none)
- Issue tags: ui_term, baseline_guard, tw_usage
- Rationale: 基礎語句以自然台灣繁體為準，避免加入過度領域詞。

### blind-ui-0087

- Domain: ui
- Risk: baseline_guard
- Confidence: medium
- Review needed: True
- Input: 二维码失效后会显示提示文字。
- Codex expected: QR Code 失效後會顯示提示文字。
- Acceptable alternatives: (none)
- Issue tags: ui_term, baseline_guard, tw_usage
- Rationale: 基礎語句以自然台灣繁體為準，避免加入過度領域詞。

### blind-llm-0048

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 模型摘要会列出三点主要结论。
- Codex expected: 模型摘要會列出三點主要結論。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0049

- Domain: llm
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 请让助理用条列方式回答问题。
- Codex expected: 請讓助理用條列方式回答問題。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0050

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 系统提示词要求先确认用户意图。
- Codex expected: 系統提示詞要求先確認使用者意圖。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0051

- Domain: llm
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 这个代理会读取工具返回的 JSON 结果。
- Codex expected: 這個代理會讀取工具回傳的 JSON 結果。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0052

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请把长段落改写成客服回复。
- Codex expected: 請把長段落改寫成客服回覆。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0053

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 检索结果会附上来源编号。
- Codex expected: 檢索結果會附上來源編號。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0054

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 提示模板会插入用户上传的文件名。
- Codex expected: 提示範本會插入使用者上傳的檔名。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0055

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 聊天记录会保留最近五轮对话。
- Codex expected: 聊天紀錄會保留最近五輪對話。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0056

- Domain: llm
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 评估脚本会比较模型输出和人工答案。
- Codex expected: 評估指令碼會比較模型輸出和人工答案。
- Acceptable alternatives: (none)
- Issue tags: technical_term, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-llm-0057

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 提示词里的 TaipeiBot 名称不得改写。
- Codex expected: 提示詞裡的 TaipeiBot 名稱不得改寫。
- Acceptable alternatives: (none)
- Issue tags: technical_term, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-llm-0058

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 请保留 Markdown 表格中的 zhTW 字段。
- Codex expected: 請保留 Markdown 表格中的 zhTW 欄位。
- Acceptable alternatives: (none)
- Issue tags: technical_term, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-llm-0059

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 引用标题里的台湾 AI 年会保持原样。
- Codex expected: 引用標題裡的台灣 AI 年會保持原樣。
- Acceptable alternatives: (none)
- Issue tags: technical_term, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-llm-0060

- Domain: llm
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 变量 assistant_name 不应该被翻译。
- Codex expected: 變數 assistant_name 不應該被翻譯。
- Acceptable alternatives: (none)
- Issue tags: technical_term, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-llm-0061

- Domain: llm
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 回答前请先阅读用户提供的上下文。
- Codex expected: 回答前請先閱讀使用者提供的上下文。
- Acceptable alternatives: (none)
- Issue tags: technical_term, baseline_guard, tw_usage
- Rationale: 基礎語句以自然台灣繁體為準，避免加入過度領域詞。

### blind-llm-0062

- Domain: llm
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 如果资料不足，请说明无法判断。
- Codex expected: 如果資料不足，請說明無法判斷。
- Acceptable alternatives: (none)
- Issue tags: technical_term, baseline_guard, tw_usage
- Rationale: 基礎語句以自然台灣繁體為準，避免加入過度領域詞。

### blind-formal-0049

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 主管机关将于月底公布审查结果。
- Codex expected: 主管機關將於月底公布審查結果。
- Acceptable alternatives: (none)
- Issue tags: formal_register, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0050

- Domain: formal
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 申请文件须附最近三个月的缴费证明。
- Codex expected: 申請文件須附最近三個月的繳費證明。
- Acceptable alternatives: (none)
- Issue tags: formal_register, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0051

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 本条例修正案预计下会期审议。
- Codex expected: 本條例修正案預計下會期審議。
- Acceptable alternatives: (none)
- Issue tags: formal_register, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0052

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 新闻稿指出合作计划不会影响既有权益。
- Codex expected: 新聞稿指出合作計畫不會影響既有權益。
- Acceptable alternatives: (none)
- Issue tags: formal_register, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0053

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 会议资料将同步上传至机关网站。
- Codex expected: 會議資料將同步上傳至機關網站。
- Acceptable alternatives: (none)
- Issue tags: formal_register, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0054

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 承办单位应在期限内完成补正通知。
- Codex expected: 承辦單位應在期限內完成補正通知。
- Acceptable alternatives: (none)
- Issue tags: formal_register, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0055

- Domain: formal
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 调查报告建议提高资料保存年限。
- Codex expected: 調查報告建議提高資料保存年限。
- Acceptable alternatives: (none)
- Issue tags: formal_register, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0056

- Domain: formal
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 公司应于股东会前寄发议事手册。
- Codex expected: 公司應於股東會前寄發議事手冊。
- Acceptable alternatives: (none)
- Issue tags: formal_register, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-formal-0057

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 附件中的 Taipei Office 名称不得翻译。
- Codex expected: 附件中的 Taipei Office 名稱不得翻譯。
- Acceptable alternatives: (none)
- Issue tags: formal_register, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-formal-0058

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 法规标题中的台湾关系法保持原文。
- Codex expected: 法規標題中的台灣關係法保持原文。
- Acceptable alternatives: (none)
- Issue tags: formal_register, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-formal-0059

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 请保留公告里的 Taichung Branch 英文名称。
- Codex expected: 請保留公告裡的 Taichung Branch 英文名稱。
- Acceptable alternatives: (none)
- Issue tags: formal_register, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-formal-0060

- Domain: formal
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 会议纪录中的 #台北专案 标签不应改写。
- Codex expected: 會議紀錄中的 #台北專案 標籤不應改寫。
- Acceptable alternatives: (none)
- Issue tags: formal_register, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-formal-0061

- Domain: formal
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 本案经审查后准予备案。
- Codex expected: 本案經審查後准予備案。
- Acceptable alternatives: (none)
- Issue tags: formal_register, baseline_guard, tw_usage
- Rationale: 基礎語句以自然台灣繁體為準，避免加入過度領域詞。

### blind-formal-0062

- Domain: formal
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 相关单位应配合后续稽查。
- Codex expected: 相關單位應配合後續稽查。
- Acceptable alternatives: (none)
- Issue tags: formal_register, baseline_guard, tw_usage
- Rationale: 基礎語句以自然台灣繁體為準，避免加入過度領域詞。

### blind-formal-0063

- Domain: formal
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 公告内容自发布日起生效。
- Codex expected: 公告內容自發布日起生效。
- Acceptable alternatives: (none)
- Issue tags: formal_register, baseline_guard, tw_usage
- Rationale: 基礎語句以自然台灣繁體為準，避免加入過度領域詞。

### blind-social-0049

- Domain: social
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 我晚点再把订位信息传给你。
- Codex expected: 我晚點再把訂位資訊傳給你。
- Acceptable alternatives: (none)
- Issue tags: colloquial_register, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0050

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 这家店的评价比上个月好多了。
- Codex expected: 這家店的評價比上個月好多了。
- Acceptable alternatives: (none)
- Issue tags: colloquial_register, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0051

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 你可以先把购物车里的东西结账。
- Codex expected: 你可以先把購物車裡的東西結帳。
- Acceptable alternatives: (none)
- Issue tags: colloquial_register, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0052

- Domain: social
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 朋友说这部剧的结局很催泪。
- Codex expected: 朋友說這部影集的結局很催淚。
- Acceptable alternatives: (none)
- Issue tags: colloquial_register, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0053

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 我已经把聚餐照片上传到相册。
- Codex expected: 我已經把聚餐照片上傳到相簿。
- Acceptable alternatives: (none)
- Issue tags: colloquial_register, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0054

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 群组公告提醒大家准时到场。
- Codex expected: 群組公告提醒大家準時到場。
- Acceptable alternatives: (none)
- Issue tags: colloquial_register, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0055

- Domain: social
- Risk: candidate_gap
- Confidence: high
- Review needed: False
- Input: 请把路线链接发到聊天室。
- Codex expected: 請把路線連結傳到聊天室。
- Acceptable alternatives: (none)
- Issue tags: colloquial_register, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0056

- Domain: social
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 这条动态的留言已经关闭。
- Codex expected: 這則動態的留言已經關閉。
- Acceptable alternatives: (none)
- Issue tags: colloquial_register, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-social-0057

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 照片说明里的台南小吃保持原样。
- Codex expected: 照片說明裡的台南小吃保持原樣。
- Acceptable alternatives: (none)
- Issue tags: colloquial_register, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-social-0058

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 昵称 TaipeiWalker 不要自动翻译。
- Codex expected: 暱稱 TaipeiWalker 不要自動翻譯。
- Acceptable alternatives: (none)
- Issue tags: colloquial_register, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-social-0059

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 请保留朋友写的 Happy Taiwan Day。
- Codex expected: 請保留朋友寫的 Happy Taiwan Day。
- Acceptable alternatives: (none)
- Issue tags: colloquial_register, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-social-0060

- Domain: social
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 标签 #台湾旅行 不要被改成其他词。
- Codex expected: 標籤 #台灣旅行 不要被改成其他詞。
- Acceptable alternatives: (none)
- Issue tags: colloquial_register, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-social-0061

- Domain: social
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 明天晚上我们一起看电影。
- Codex expected: 明天晚上我們一起看電影。
- Acceptable alternatives: (none)
- Issue tags: colloquial_register, baseline_guard, tw_usage
- Rationale: 基礎語句以自然台灣繁體為準，避免加入過度領域詞。

### blind-social-0062

- Domain: social
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 这件外套的颜色很好看。
- Codex expected: 這件外套的顏色很好看。
- Acceptable alternatives: (none)
- Issue tags: colloquial_register, baseline_guard, tw_usage
- Rationale: 基礎語句以自然台灣繁體為準，避免加入過度領域詞。

### blind-social-0063

- Domain: social
- Risk: baseline_guard
- Confidence: high
- Review needed: False
- Input: 我先去便利店买早餐。
- Codex expected: 我先去便利商店買早餐。
- Acceptable alternatives: (none)
- Issue tags: colloquial_register, baseline_guard, tw_usage
- Rationale: 基礎語句以自然台灣繁體為準，避免加入過度領域詞。

### blind-high-risk-0031

- Domain: high_risk
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 医师应向患者说明手术风险和替代方案。
- Codex expected: 醫師應向病患說明手術風險和替代方案。
- Acceptable alternatives: (none)
- Issue tags: high_risk_domain, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-high-risk-0032

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 保险公司须在期限内回复理赔申请。
- Codex expected: 保險公司須在期限內回覆理賠申請。
- Acceptable alternatives: (none)
- Issue tags: high_risk_domain, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-high-risk-0033

- Domain: high_risk
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 银行不得在未告知前提下调整手续费。
- Codex expected: 銀行不得在未告知前提下調整手續費。
- Acceptable alternatives: (none)
- Issue tags: high_risk_domain, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-high-risk-0034

- Domain: high_risk
- Risk: candidate_gap
- Confidence: high
- Review needed: True
- Input: 契约解除通知应以书面送达。
- Codex expected: 契約解除通知應以書面送達。
- Acceptable alternatives: (none)
- Issue tags: high_risk_domain, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-high-risk-0035

- Domain: high_risk
- Risk: candidate_gap
- Confidence: medium
- Review needed: True
- Input: 药品说明应列明常见副作用。
- Codex expected: 藥品說明應列明常見副作用。
- Acceptable alternatives: (none)
- Issue tags: high_risk_domain, tw_usage
- Rationale: 建議採台灣常用繁體詞彙；此為 first-pass 建議，需維持人工確認流程。

### blind-high-risk-0036

- Domain: high_risk
- Risk: over_conversion_guard
- Confidence: medium
- Review needed: True
- Input: 病例编号 TW-Clinic-01 不得自动转换。
- Codex expected: 病例編號 TW-Clinic-01 不得自動轉換。
- Acceptable alternatives: (none)
- Issue tags: high_risk_domain, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-high-risk-0037

- Domain: high_risk
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 契约中的 Taipei Holdings 名称应保持原样。
- Codex expected: 契約中的 Taipei Holdings 名稱應保持原樣。
- Acceptable alternatives: (none)
- Issue tags: high_risk_domain, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-high-risk-0038

- Domain: high_risk
- Risk: over_conversion_guard
- Confidence: high
- Review needed: True
- Input: 汇款附言里的 Taiwan Relief Fund 不需翻译。
- Codex expected: 匯款附言裡的 Taiwan Relief Fund 不需翻譯。
- Acceptable alternatives: (none)
- Issue tags: high_risk_domain, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-high-risk-0039

- Domain: high_risk
- Risk: over_conversion_guard
- Confidence: medium
- Review needed: True
- Input: 病历附件里的台北院区代码不可改写。
- Codex expected: 病歷附件裡的台北院區代碼不可改寫。
- Acceptable alternatives: (none)
- Issue tags: high_risk_domain, over_conversion_guard, tw_usage
- Rationale: 保留專名、代碼、變數或既有台灣繁體片段，僅轉換周邊簡體文字。

### blind-high-risk-0040

- Domain: high_risk
- Risk: baseline_guard
- Confidence: high
- Review needed: True
- Input: 申请人应亲自签署授权书。
- Codex expected: 申請人應親自簽署授權書。
- Acceptable alternatives: (none)
- Issue tags: high_risk_domain, baseline_guard, tw_usage
- Rationale: 基礎語句以自然台灣繁體為準，避免加入過度領域詞。
