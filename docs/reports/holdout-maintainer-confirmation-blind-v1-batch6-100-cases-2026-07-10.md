<!-- zhtw:disable -->
# Holdout Maintainer Confirmation Packet - blind-v1 batch6 100 cases

Generated: 2026-07-10

This packet is for maintainer confirmation only. It is not ground truth and does not write private expected values.

## Summary

- Total review cases: 76
- Difference cases: 20
- Policy review cases: 56
- No immediate question: 24
- Difference recommendations: {"codex": 13, "gemini": 4, "third": 3}
- zhtw current status for differences: {"needs_followup_if_confirmed": 9, "in_recommended_acceptable": 8, "matches_recommended": 3}

## Difference Cases

### blind-it-0113

- Domain: it
- Risk: candidate_gap
- Recommendation: third
- zhtw current status: needs_followup_if_confirmed
- Reason: Input 的「请求」在此是 API request，應保留為「請求」；signature 在此可用台灣技術語境常見的「簽章」，並以「回傳」作為 API response primary。

Input:
```text
请求签名失败时，网关会返回可追踪的错误编号。
```

Codex:
```text
要求簽章失敗時，閘道會回傳可追蹤的錯誤編號。
```

Gemini:
```text
請求簽名失敗時，閘道會傳回可追蹤的錯誤編號。
```

Recommended:
```text
請求簽章失敗時，閘道會回傳可追蹤的錯誤編號。
```

zhtw current:
```text
要求簽章失敗時，閘道會返回可追蹤的錯誤編號。
```

### blind-it-0115

- Domain: it
- Risk: candidate_gap
- Recommendation: third
- zhtw current status: needs_followup_if_confirmed
- Reason: 「依」比「按」更符合台灣技術文件語氣；tenant 可作「租戶」或「租用戶」，cache key 以「快取鍵」較精簡自然。

Input:
```text
后端服务会按租户标识隔离缓存键。
```

Codex:
```text
後端服務會依租用戶識別碼隔離快取鍵。
```

Gemini:
```text
後端服務會按租用戶識別碼隔離快取索引鍵。
```

Recommended:
```text
後端服務會依租戶識別碼隔離快取鍵。
```

zhtw current:
```text
後端服務會按租戶標識隔離快取鍵。
```

### blind-it-0117

- Domain: it
- Risk: candidate_gap
- Recommendation: gemini
- zhtw current status: needs_followup_if_confirmed
- Reason: 台灣專案與資料庫語境常用「移轉」描述 migration；Codex 與 Gemini 都同意「離峰時段」優於直譯低峰。

Input:
```text
数据库迁移任务需要在低峰时段执行。
```

Codex:
```text
資料庫遷移任務需要在離峰時段執行。
```

Gemini:
```text
資料庫移轉任務需要在離峰時段執行。
```

Recommended:
```text
資料庫移轉任務需要在離峰時段執行。
```

zhtw current:
```text
資料庫遷移任務需要在低峰時段執行。
```

### blind-it-0123

- Domain: it
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: needs_followup_if_confirmed
- Reason: Codex 較保留原句「請把」語氣；「偵錯資訊」與「日誌檔案」是可接受的台灣技術寫法。

Input:
```text
请把调试信息写入单独的日志文件。
```

Codex:
```text
請把偵錯資訊寫入單獨的日誌檔案。
```

Gemini:
```text
請將偵錯資訊寫入單獨的日誌檔案。
```

Recommended:
```text
請把偵錯資訊寫入單獨的日誌檔案。
```

zhtw current:
```text
請把除錯資訊寫入單獨的日誌文件。
```

### blind-it-0124

- Domain: it
- Risk: candidate_gap
- Recommendation: third
- zhtw current status: needs_followup_if_confirmed
- Reason: 「容器編排平台」與「執行個體」較符合台灣雲端文件；資源限制下的 scheduling 以「排程」較自然。

Input:
```text
容器编排平台会根据资源限制调度实例。
```

Codex:
```text
容器編排平台會根據資源限制調度執行個體。
```

Gemini:
```text
容器編排平台會根據資源限制排程實例。
```

Recommended:
```text
容器編排平台會根據資源限制排程執行個體。
```

zhtw current:
```text
容器編排平臺會根據資源限制調度實例。
```

### blind-it-0130

- Domain: it
- Risk: over_conversion_guard
- Recommendation: codex
- zhtw current status: matches_recommended
- Reason: over-conversion guard 的重點是保留 TaipeiCluster；Codex primary 與目前 zhtw 較貼近原句「保持原樣」。

Input:
```text
配置文件中的 TaipeiCluster 标签必须保持原样。
```

Codex:
```text
設定檔中的 TaipeiCluster 標籤必須保持原樣。
```

Gemini:
```text
設定檔中的 TaipeiCluster 標籤必須維持原樣。
```

Recommended:
```text
設定檔中的 TaipeiCluster 標籤必須保持原樣。
```

zhtw current:
```text
設定檔中的 TaipeiCluster 標籤必須保持原樣。
```

### blind-it-0133

- Domain: it
- Risk: over_conversion_guard
- Recommendation: codex
- zhtw current status: matches_recommended
- Reason: over-conversion guard 的重點是保留 FormosaEdge；原文「清单」不必強制擴成「資訊清單」。

Input:
```text
产品代号 FormosaEdge 写在部署清单里。
```

Codex:
```text
產品代號 FormosaEdge 寫在部署清單裡。
```

Gemini:
```text
產品代號 FormosaEdge 寫在部署資訊清單裡。
```

Recommended:
```text
產品代號 FormosaEdge 寫在部署清單裡。
```

zhtw current:
```text
產品代號 FormosaEdge 寫在部署清單裡。
```

### blind-it-0136

- Domain: it
- Risk: baseline_guard
- Recommendation: gemini
- zhtw current status: needs_followup_if_confirmed
- Reason: 台灣 UI 文字常用「儲存變更」，比「儲存修改」更自然；兩者語義一致。

Input:
```text
请先保存修改再关闭窗口。
```

Codex:
```text
請先儲存修改再關閉視窗。
```

Gemini:
```text
請先儲存變更再關閉視窗。
```

Recommended:
```text
請先儲存變更再關閉視窗。
```

zhtw current:
```text
請先保存修改再關閉視窗。
```

### blind-ui-0089

- Domain: ui
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: needs_followup_if_confirmed
- Reason: 台灣 UI 常用「檢視」作為查看動作；表格 row 在台灣可作「列」或更明確的「資料列」。

Input:
```text
表格行可以展开查看详细信息。
```

Codex:
```text
表格列可以展開檢視詳細資訊。
```

Gemini:
```text
表格列可以展開查看詳細資訊。
```

Recommended:
```text
表格列可以展開檢視詳細資訊。
```

zhtw current:
```text
表格行可以展開查看詳細資訊。
```

### blind-ui-0090

- Domain: ui
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: in_recommended_acceptable
- Reason: 台灣產品 UI primary action 通常使用「送出」；「載入動畫」維持兩邊共識。

Input:
```text
请在提交按钮旁边显示加载动画。
```

Codex:
```text
請在送出按鈕旁邊顯示載入動畫。
```

Gemini:
```text
請在提交按鈕旁邊顯示載入動畫。
```

Recommended:
```text
請在送出按鈕旁邊顯示載入動畫。
```

zhtw current:
```text
請在提交按鈕旁邊顯示載入動畫。
```

### blind-ui-0091

- Domain: ui
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: in_recommended_acceptable
- Reason: 「依相關性排序」比「按照相關性」更符合精簡 UI 文案。

Input:
```text
搜索结果会按照相关性排序。
```

Codex:
```text
搜尋結果會依相關性排序。
```

Gemini:
```text
搜尋結果會按照相關性排序。
```

Recommended:
```text
搜尋結果會依相關性排序。
```

zhtw current:
```text
搜尋結果會按照相關性排序。
```

### blind-ui-0094

- Domain: ui
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: in_recommended_acceptable
- Reason: 台灣 UI 中 list 通常譯為「清單」；「依」也比「按」更自然。

Input:
```text
通知列表会按未读状态分组。
```

Codex:
```text
通知清單會依未讀狀態分組。
```

Gemini:
```text
通知列表會按未讀狀態分組。
```

Recommended:
```text
通知清單會依未讀狀態分組。
```

zhtw current:
```text
通知清單會按未讀狀態分組。
```

### blind-ui-0096

- Domain: ui
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: needs_followup_if_confirmed
- Reason: 可收合式 sidebar 的台灣 UI primary 用語通常是「收合」。

Input:
```text
侧边栏折叠后只显示图标。
```

Codex:
```text
側邊欄收合後只顯示圖示。
```

Gemini:
```text
側邊欄折疊後只顯示圖示。
```

Recommended:
```text
側邊欄收合後只顯示圖示。
```

zhtw current:
```text
側邊欄摺疊後只顯示圖示。
```

### blind-ui-0097

- Domain: ui
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: in_recommended_acceptable
- Reason: 「已選取數量」在 UI 狀態文字中比「已選數量」更完整自然。

Input:
```text
批量操作工具栏会显示已选数量。
```

Codex:
```text
批次操作工具列會顯示已選取數量。
```

Gemini:
```text
批次操作工具列會顯示已選數量。
```

Recommended:
```text
批次操作工具列會顯示已選取數量。
```

zhtw current:
```text
批次操作工具列會顯示已選數量。
```

### blind-ui-0102

- Domain: ui
- Risk: over_conversion_guard
- Recommendation: codex
- zhtw current status: needs_followup_if_confirmed
- Reason: 此 over-conversion guard 應保留已是台灣用語的「登入」；「在地化」也比「本地化」更符合台灣軟體語境。

Input:
```text
语言包里已经本地化的「登入」不要改写。
```

Codex:
```text
語言套件裡已經在地化的「登入」不要改寫。
```

Gemini:
```text
語言包裡已經本地化的「登入」不要改寫。
```

Recommended:
```text
語言套件裡已經在地化的「登入」不要改寫。
```

zhtw current:
```text
語言包裡已經本機化的「登入」不要改寫。
```

### blind-ui-0106

- Domain: ui
- Risk: baseline_guard
- Recommendation: codex
- zhtw current status: in_recommended_acceptable
- Reason: 台灣社群與個人資料 UI 常用「大頭貼」；「頭像」可作接受變體。

Input:
```text
用户可以上传一张头像图片。
```

Codex:
```text
使用者可以上傳一張大頭貼圖片。
```

Gemini:
```text
使用者可以上傳一張頭像圖片。
```

Recommended:
```text
使用者可以上傳一張大頭貼圖片。
```

zhtw current:
```text
使用者可以上傳一張頭像圖片。
```

### blind-ui-0107

- Domain: ui
- Risk: baseline_guard
- Recommendation: codex
- zhtw current status: in_recommended_acceptable
- Reason: 台灣 UI 指令文字常以「點選」作為 primary；「點擊」可作可接受變體。

Input:
```text
请点击左上角的返回按钮。
```

Codex:
```text
請點選左上角的返回按鈕。
```

Gemini:
```text
請點擊左上角的返回按鈕。
```

Recommended:
```text
請點選左上角的返回按鈕。
```

zhtw current:
```text
請點擊左上角的返回按鈕。
```

### blind-llm-0069

- Domain: llm
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: matches_recommended
- Reason: parser 在開發者語境中「解析器」較常見；Gemini 的「剖析器」可接受但較正式。

Input:
```text
输出解析器会验证 JSON 字段是否完整。
```

Codex:
```text
輸出解析器會驗證 JSON 欄位是否完整。
```

Gemini:
```text
輸出剖析器會驗證 JSON 欄位是否完整。
```

Recommended:
```text
輸出解析器會驗證 JSON 欄位是否完整。
```

zhtw current:
```text
輸出解析器會驗證 JSON 欄位是否完整。
```

### blind-llm-0070

- Domain: llm
- Risk: candidate_gap
- Recommendation: gemini
- zhtw current status: in_recommended_acceptable
- Reason: LLM 評測語境中「評測腳本」是常見實務用語；「指令碼」較正式但可接受。

Input:
```text
评测脚本会比较模型回答和参考答案。
```

Codex:
```text
評測指令碼會比較模型回答和參考答案。
```

Gemini:
```text
評測腳本會比較模型回答和參考答案。
```

Recommended:
```text
評測腳本會比較模型回答和參考答案。
```

zhtw current:
```text
評測指令碼會比較模型回答和參考答案。
```

### blind-formal-0065

- Domain: formal
- Risk: candidate_gap
- Recommendation: gemini
- zhtw current status: in_recommended_acceptable
- Reason: 台灣正式文件較常用「會議紀錄」表示 meeting minutes；「會議紀要」可接受但較書面。

Input:
```text
会议纪要应列明各部门后续任务。
```

Codex:
```text
會議紀要應列明各部門後續任務。
```

Gemini:
```text
會議紀錄應列明各部門後續任務。
```

Recommended:
```text
會議紀錄應列明各部門後續任務。
```

zhtw current:
```text
會議紀要應列明各部門後續任務。
```

## Policy Review Cases

### blind-it-0114

- Domain: it
- Risk: candidate_gap
- Reason: Gemini review-needed variant
- zhtw current status: matches_recommended

Input:
```text
请把部署参数写入版本化配置文件。
```

Recommended:
```text
請把部署參數寫入版本化設定檔。
```

zhtw current:
```text
請把部署參數寫入版本化設定檔。
```

### blind-it-0116

- Domain: it
- Risk: candidate_gap
- Reason: Gemini review-needed variant
- zhtw current status: in_recommended_acceptable

Input:
```text
命令行工具会读取当前工作目录里的配置文件。
```

Recommended:
```text
命令列工具會讀取目前工作目錄裡的設定檔。
```

zhtw current:
```text
命令列工具會讀取當前工作目錄裡的設定檔。
```

### blind-it-0120

- Domain: it
- Risk: candidate_gap
- Reason: Codex confidence medium, Gemini review-needed variant
- zhtw current status: in_recommended_acceptable

Input:
```text
构建脚本会在发布前生成校验清单。
```

Recommended:
```text
建置指令碼會在發布前產生校驗清單。
```

zhtw current:
```text
建置指令碼會在發布前生成校驗清單。
```

### blind-it-0122

- Domain: it
- Risk: candidate_gap
- Reason: Codex confidence medium
- zhtw current status: matches_recommended

Input:
```text
代理服务器会保留原始请求标头。
```

Recommended:
```text
代理伺服器會保留原始請求標頭。
```

zhtw current:
```text
代理伺服器會保留原始請求標頭。
```

### blind-it-0125

- Domain: it
- Risk: candidate_gap
- Reason: Codex confidence medium, Gemini review-needed variant
- zhtw current status: needs_followup_if_confirmed

Input:
```text
上传任务完成后，接口会返回文件摘要。
```

Recommended:
```text
上傳任務完成後，介面會回傳檔案摘要。
```

zhtw current:
```text
上傳任務完成後，介面會返迴文件摘要。
```

### blind-it-0128

- Domain: it
- Risk: over_conversion_guard
- Reason: over-conversion guard
- zhtw current status: matches_recommended

Input:
```text
请保留 API 响应里的 TaiwanNorth 区域名称。
```

Recommended:
```text
請保留 API 回應裡的 TaiwanNorth 區域名稱。
```

zhtw current:
```text
請保留 API 回應裡的 TaiwanNorth 區域名稱。
```

### blind-it-0129

- Domain: it
- Risk: over_conversion_guard
- Reason: over-conversion guard
- zhtw current status: in_recommended_acceptable

Input:
```text
变量名 userTaiwanId 不应该被自动改写。
```

Recommended:
```text
變數名稱 userTaiwanId 不應該被自動改寫。
```

zhtw current:
```text
變數名 userTaiwanId 不應該被自動改寫。
```

### blind-it-0131

- Domain: it
- Risk: over_conversion_guard
- Reason: Codex confidence medium, over-conversion guard
- zhtw current status: needs_followup_if_confirmed

Input:
```text
README 里的 zh-TW 示例路径不要转换成其他地区。
```

Recommended:
```text
README 裡的 zh-TW 範例路徑不要轉換成其他地區。
```

zhtw current:
```text
README 裡的 zh-TW 示例路徑不要轉換成其他地區。
```

### blind-it-0132

- Domain: it
- Risk: over_conversion_guard
- Reason: over-conversion guard
- zhtw current status: matches_recommended

Input:
```text
请不要翻译日志字段 requestTaiwanCode。
```

Recommended:
```text
請不要翻譯日誌欄位 requestTaiwanCode。
```

zhtw current:
```text
請不要翻譯日誌欄位 requestTaiwanCode。
```

### blind-ui-0092

- Domain: ui
- Risk: candidate_gap
- Reason: Gemini review-needed variant
- zhtw current status: in_recommended_acceptable

Input:
```text
语言切换菜单会显示当前地区。
```

Recommended:
```text
語言切換選單會顯示目前地區。
```

zhtw current:
```text
語言切換選單會顯示當前地區。
```

### blind-ui-0093

- Domain: ui
- Risk: candidate_gap
- Reason: Codex confidence medium
- zhtw current status: matches_recommended

Input:
```text
空状态页面需要提供返回按钮。
```

Recommended:
```text
空狀態頁面需要提供返回按鈕。
```

zhtw current:
```text
空狀態頁面需要提供返回按鈕。
```

### blind-ui-0098

- Domain: ui
- Risk: candidate_gap
- Reason: Gemini review-needed variant
- zhtw current status: matches_recommended

Input:
```text
表单错误提示会保留用户输入内容。
```

Recommended:
```text
表單錯誤提示會保留使用者輸入內容。
```

zhtw current:
```text
表單錯誤提示會保留使用者輸入內容。
```

### blind-ui-0099

- Domain: ui
- Risk: candidate_gap
- Reason: Codex confidence medium, Gemini review-needed variant
- zhtw current status: in_recommended_acceptable

Input:
```text
分页器支持跳转到指定页码。
```

Recommended:
```text
分頁器支援跳轉到指定頁碼。
```

zhtw current:
```text
分頁器支持跳轉到指定頁碼。
```

### blind-ui-0100

- Domain: ui
- Risk: over_conversion_guard
- Reason: over-conversion guard
- zhtw current status: matches_recommended

Input:
```text
请保留按钮文案里的 Taiwan Rewards 名称。
```

Recommended:
```text
請保留按鈕文案裡的 Taiwan Rewards 名稱。
```

zhtw current:
```text
請保留按鈕文案裡的 Taiwan Rewards 名稱。
```

### blind-ui-0101

- Domain: ui
- Risk: over_conversion_guard
- Reason: over-conversion guard
- zhtw current status: matches_recommended

Input:
```text
活动页面标题中的 Taipei Pass 不要翻译。
```

Recommended:
```text
活動頁面標題中的 Taipei Pass 不要翻譯。
```

zhtw current:
```text
活動頁面標題中的 Taipei Pass 不要翻譯。
```

### blind-ui-0103

- Domain: ui
- Risk: over_conversion_guard
- Reason: over-conversion guard
- zhtw current status: matches_recommended

Input:
```text
设置页的 iOS Shortcut 标签保持原样。
```

Recommended:
```text
設定頁的 iOS Shortcut 標籤保持原樣。
```

zhtw current:
```text
設定頁的 iOS Shortcut 標籤保持原樣。
```

### blind-ui-0104

- Domain: ui
- Risk: over_conversion_guard
- Reason: over-conversion guard
- zhtw current status: matches_recommended

Input:
```text
URL 参数 locale=zh-TW 不应被替换。
```

Recommended:
```text
URL 參數 locale=zh-TW 不應被替換。
```

zhtw current:
```text
URL 參數 locale=zh-TW 不應被替換。
```

### blind-ui-0105

- Domain: ui
- Risk: baseline_guard
- Reason: Gemini review-needed variant
- zhtw current status: in_recommended_acceptable

Input:
```text
页面加载完成后会显示欢迎信息。
```

Recommended:
```text
頁面載入完成後會顯示歡迎訊息。
```

zhtw current:
```text
頁面載入完成後會顯示歡迎資訊。
```

### blind-llm-0063

- Domain: llm
- Risk: candidate_gap
- Reason: Codex confidence medium
- zhtw current status: matches_recommended

Input:
```text
模型回复需要引用检索到的文档段落。
```

Recommended:
```text
模型回覆需要引用檢索到的文件段落。
```

zhtw current:
```text
模型回覆需要引用檢索到的文件段落。
```

### blind-llm-0064

- Domain: llm
- Risk: candidate_gap
- Reason: Gemini review-needed variant
- zhtw current status: matches_recommended

Input:
```text
请把工具调用结果整理成项目符号清单。
```

Recommended:
```text
請把工具呼叫結果整理成項目符號清單。
```

zhtw current:
```text
請把工具呼叫結果整理成項目符號清單。
```

### blind-llm-0066

- Domain: llm
- Risk: candidate_gap
- Reason: Gemini review-needed variant
- zhtw current status: in_recommended_acceptable

Input:
```text
摘要生成器会保留原文中的专有名词。
```

Recommended:
```text
摘要產生器會保留原文中的專有名詞。
```

zhtw current:
```text
摘要生成器會保留原文中的專有名詞。
```

### blind-llm-0067

- Domain: llm
- Risk: candidate_gap
- Reason: Codex confidence medium, Gemini review-needed variant
- zhtw current status: matches_recommended

Input:
```text
代理会在执行计划前检查工具权限。
```

Recommended:
```text
代理會在執行計畫前檢查工具權限。
```

zhtw current:
```text
代理會在執行計畫前檢查工具權限。
```

### blind-llm-0068

- Domain: llm
- Risk: candidate_gap
- Reason: Gemini review-needed variant
- zhtw current status: matches_recommended

Input:
```text
请将用户意图分类为查询或操作。
```

Recommended:
```text
請將使用者意圖分類為查詢或操作。
```

zhtw current:
```text
請將使用者意圖分類為查詢或操作。
```

### blind-llm-0071

- Domain: llm
- Risk: candidate_gap
- Reason: Codex confidence medium, Gemini review-needed variant
- zhtw current status: needs_followup_if_confirmed

Input:
```text
这个提示模板会插入当前会话历史。
```

Recommended:
```text
這個提示範本會插入目前對話歷史。
```

zhtw current:
```text
這個提示範本會插入當前會話歷史。
```

### blind-llm-0072

- Domain: llm
- Risk: over_conversion_guard
- Reason: over-conversion guard
- zhtw current status: matches_recommended

Input:
```text
请不要改写提示词里的 TaiwanSupportBot 名称。
```

Recommended:
```text
請不要改寫提示詞裡的 TaiwanSupportBot 名稱。
```

zhtw current:
```text
請不要改寫提示詞裡的 TaiwanSupportBot 名稱。
```

### blind-llm-0073

- Domain: llm
- Risk: over_conversion_guard
- Reason: over-conversion guard
- zhtw current status: in_recommended_acceptable

Input:
```text
示例输出中的 TaipeiOffice 应保持原样。
```

Recommended:
```text
範例輸出中的 TaipeiOffice 應保持原樣。
```

zhtw current:
```text
示例輸出中的 TaipeiOffice 應保持原樣。
```

### blind-llm-0074

- Domain: llm
- Risk: over_conversion_guard
- Reason: over-conversion guard
- zhtw current status: matches_recommended

Input:
```text
模型不得翻译变量 {{taiwan_user_name}}。
```

Recommended:
```text
模型不得翻譯變數 {{taiwan_user_name}}。
```

zhtw current:
```text
模型不得翻譯變數 {{taiwan_user_name}}。
```

### blind-llm-0075

- Domain: llm
- Risk: over_conversion_guard
- Reason: Codex confidence medium, over-conversion guard
- zhtw current status: matches_recommended

Input:
```text
文档片段里的「台灣繁體」标签已是目标语言。
```

Recommended:
```text
文件片段裡的「台灣繁體」標籤已是目標語言。
```

zhtw current:
```text
文件片段裡的「台灣繁體」標籤已是目標語言。
```

### blind-formal-0064

- Domain: formal
- Risk: candidate_gap
- Reason: Gemini review-needed variant
- zhtw current status: matches_recommended

Input:
```text
本公司将于下月调整服务条款。
```

Recommended:
```text
本公司將於下月調整服務條款。
```

zhtw current:
```text
本公司將於下月調整服務條款。
```

### blind-formal-0066

- Domain: formal
- Risk: candidate_gap
- Reason: Gemini review-needed variant
- zhtw current status: matches_recommended

Input:
```text
公告发布后，申请人可在线查询进度。
```

Recommended:
```text
公告發布後，申請人可線上查詢進度。
```

zhtw current:
```text
公告發布後，申請人可線上查詢進度。
```

### blind-formal-0067

- Domain: formal
- Risk: candidate_gap
- Reason: Codex confidence medium, Gemini review-needed variant
- zhtw current status: matches_recommended

Input:
```text
合同附件应与正文具有同等效力。
```

Recommended:
```text
合約附件應與正文具有同等效力。
```

zhtw current:
```text
合約附件應與正文具有同等效力。
```

### blind-formal-0068

- Domain: formal
- Risk: candidate_gap
- Reason: Gemini review-needed variant
- zhtw current status: matches_recommended

Input:
```text
主管机关将说明资料补正期限。
```

Recommended:
```text
主管機關將說明資料補正期限。
```

zhtw current:
```text
主管機關將說明資料補正期限。
```

### blind-formal-0069

- Domain: formal
- Risk: candidate_gap
- Reason: Gemini review-needed variant
- zhtw current status: matches_recommended

Input:
```text
年度报告须揭露主要风险因素。
```

Recommended:
```text
年度報告須揭露主要風險因素。
```

zhtw current:
```text
年度報告須揭露主要風險因素。
```

### blind-formal-0071

- Domain: formal
- Risk: candidate_gap
- Reason: Gemini review-needed variant
- zhtw current status: matches_recommended

Input:
```text
请依规定提交身分证明文件副本。
```

Recommended:
```text
請依規定提交身分證明文件副本。
```

zhtw current:
```text
請依規定提交身分證明文件副本。
```

### blind-formal-0072

- Domain: formal
- Risk: candidate_gap
- Reason: Codex confidence medium, Gemini review-needed variant
- zhtw current status: matches_recommended

Input:
```text
该计划将优先补助偏远地区学校。
```

Recommended:
```text
該計畫將優先補助偏遠地區學校。
```

zhtw current:
```text
該計畫將優先補助偏遠地區學校。
```

### blind-formal-0073

- Domain: formal
- Risk: over_conversion_guard
- Reason: over-conversion guard
- zhtw current status: matches_recommended

Input:
```text
新闻稿中的 Taiwan Green Fund 名称应保持原样。
```

Recommended:
```text
新聞稿中的 Taiwan Green Fund 名稱應保持原樣。
```

zhtw current:
```text
新聞稿中的 Taiwan Green Fund 名稱應保持原樣。
```

### blind-formal-0074

- Domain: formal
- Risk: over_conversion_guard
- Reason: over-conversion guard
- zhtw current status: matches_recommended

Input:
```text
合约编号 Taipei-2026-A 不得自动改写。
```

Recommended:
```text
合約編號 Taipei-2026-A 不得自動改寫。
```

zhtw current:
```text
合約編號 Taipei-2026-A 不得自動改寫。
```

### blind-formal-0075

- Domain: formal
- Risk: over_conversion_guard
- Reason: over-conversion guard
- zhtw current status: matches_recommended

Input:
```text
附件标题「台灣示例」已经由法务确认。
```

Recommended:
```text
附件標題「台灣示例」已經由法務確認。
```

zhtw current:
```text
附件標題「台灣示例」已經由法務確認。
```

### blind-formal-0076

- Domain: formal
- Risk: over_conversion_guard
- Reason: over-conversion guard
- zhtw current status: matches_recommended

Input:
```text
公告里的 Formosa Research Center 不需翻译。
```

Recommended:
```text
公告裡的 Formosa Research Center 不需翻譯。
```

zhtw current:
```text
公告裡的 Formosa Research Center 不需翻譯。
```

### blind-social-0065

- Domain: social
- Risk: candidate_gap
- Reason: Gemini review-needed variant
- zhtw current status: matches_recommended

Input:
```text
请把聚餐地点发到群组里。
```

Recommended:
```text
請把聚餐地點發到群組裡。
```

zhtw current:
```text
請把聚餐地點發到群組裡。
```

### blind-social-0067

- Domain: social
- Risk: candidate_gap
- Reason: Codex confidence medium, Gemini review-needed variant
- zhtw current status: in_recommended_acceptable

Input:
```text
我把照片上传到共享相册了。
```

Recommended:
```text
我把照片上傳到共享相簿了。
```

zhtw current:
```text
我把照片上傳到共享相冊了。
```

### blind-social-0071

- Domain: social
- Risk: candidate_gap
- Reason: Gemini review-needed variant
- zhtw current status: matches_recommended

Input:
```text
记得把活动链接分享给朋友。
```

Recommended:
```text
記得把活動連結分享給朋友。
```

zhtw current:
```text
記得把活動連結分享給朋友。
```

### blind-social-0073

- Domain: social
- Risk: over_conversion_guard
- Reason: over-conversion guard
- zhtw current status: matches_recommended

Input:
```text
个人简介里的 TaipeiRunner 名称不要改。
```

Recommended:
```text
個人簡介裡的 TaipeiRunner 名稱不要改。
```

zhtw current:
```text
個人簡介裡的 TaipeiRunner 名稱不要改。
```

### blind-social-0074

- Domain: social
- Risk: over_conversion_guard
- Reason: over-conversion guard
- zhtw current status: matches_recommended

Input:
```text
请保留留言中的 Happy Taiwan Weekend。
```

Recommended:
```text
請保留留言中的 Happy Taiwan Weekend。
```

zhtw current:
```text
請保留留言中的 Happy Taiwan Weekend。
```

### blind-social-0075

- Domain: social
- Risk: over_conversion_guard
- Reason: over-conversion guard
- zhtw current status: matches_recommended

Input:
```text
标签 #台灣生活 已经是原始写法。
```

Recommended:
```text
標籤 #台灣生活 已經是原始寫法。
```

zhtw current:
```text
標籤 #台灣生活 已經是原始寫法。
```

### blind-social-0076

- Domain: social
- Risk: over_conversion_guard
- Reason: over-conversion guard
- zhtw current status: matches_recommended

Input:
```text
活动代号 NightMarketGo 不需要翻译。
```

Recommended:
```text
活動代號 NightMarketGo 不需要翻譯。
```

zhtw current:
```text
活動代號 NightMarketGo 不需要翻譯。
```

### blind-high-risk-0041

- Domain: high_risk
- Risk: candidate_gap
- Reason: high-risk domain
- zhtw current status: matches_recommended

Input:
```text
医疗机构应保存患者同意书副本。
```

Recommended:
```text
醫療機構應保存患者同意書副本。
```

zhtw current:
```text
醫療機構應保存患者同意書副本。
```

### blind-high-risk-0042

- Domain: high_risk
- Risk: candidate_gap
- Reason: high-risk domain
- zhtw current status: matches_recommended

Input:
```text
银行应在交易完成后提供明细。
```

Recommended:
```text
銀行應在交易完成後提供明細。
```

zhtw current:
```text
銀行應在交易完成後提供明細。
```

### blind-high-risk-0043

- Domain: high_risk
- Risk: candidate_gap
- Reason: high-risk domain
- zhtw current status: matches_recommended

Input:
```text
保险契约变更须经双方书面同意。
```

Recommended:
```text
保險契約變更須經雙方書面同意。
```

zhtw current:
```text
保險契約變更須經雙方書面同意。
```

### blind-high-risk-0044

- Domain: high_risk
- Risk: candidate_gap
- Reason: high-risk domain
- zhtw current status: in_recommended_acceptable

Input:
```text
医师开立处方前应确认过敏记录。
```

Recommended:
```text
醫師開立處方前應確認過敏紀錄。
```

zhtw current:
```text
醫師開立處方前應確認過敏記錄。
```

### blind-high-risk-0045

- Domain: high_risk
- Risk: candidate_gap
- Reason: high-risk domain
- zhtw current status: matches_recommended

Input:
```text
使用者须先阅读个人资料告知事项。
```

Recommended:
```text
使用者須先閱讀個人資料告知事項。
```

zhtw current:
```text
使用者須先閱讀個人資料告知事項。
```

### blind-high-risk-0046

- Domain: high_risk
- Risk: candidate_gap
- Reason: high-risk domain
- zhtw current status: matches_recommended

Input:
```text
法院通知应载明应到时间和地点。
```

Recommended:
```text
法院通知應載明應到時間和地點。
```

zhtw current:
```text
法院通知應載明應到時間和地點。
```

### blind-high-risk-0047

- Domain: high_risk
- Risk: over_conversion_guard
- Reason: over-conversion guard, high-risk domain
- zhtw current status: matches_recommended

Input:
```text
病历中的 TaiwanCare 方案名称不得改写。
```

Recommended:
```text
病歷中的 TaiwanCare 方案名稱不得改寫。
```

zhtw current:
```text
病歷中的 TaiwanCare 方案名稱不得改寫。
```

### blind-high-risk-0048

- Domain: high_risk
- Risk: over_conversion_guard
- Reason: over-conversion guard, high-risk domain
- zhtw current status: matches_recommended

Input:
```text
契约当事人 Taipei BioLab 名称应保持原样。
```

Recommended:
```text
契約當事人 Taipei BioLab 名稱應保持原樣。
```

zhtw current:
```text
契約當事人 Taipei BioLab 名稱應保持原樣。
```

### blind-high-risk-0049

- Domain: high_risk
- Risk: baseline_guard
- Reason: high-risk domain
- zhtw current status: matches_recommended

Input:
```text
申请人应提供有效证件。
```

Recommended:
```text
申請人應提供有效證件。
```

zhtw current:
```text
申請人應提供有效證件。
```

### blind-high-risk-0050

- Domain: high_risk
- Risk: baseline_guard
- Reason: high-risk domain
- zhtw current status: matches_recommended

Input:
```text
未成年人签约须经法定代理人同意。
```

Recommended:
```text
未成年人簽約須經法定代理人同意。
```

zhtw current:
```text
未成年人簽約須經法定代理人同意。
```

## No Immediate Question

blind-it-0118, blind-it-0119, blind-it-0121, blind-it-0126, blind-it-0127, blind-it-0134, blind-it-0135, blind-it-0137, blind-ui-0088, blind-ui-0095, blind-llm-0065, blind-llm-0076, blind-llm-0077, blind-formal-0070, blind-formal-0077, blind-formal-0078, blind-social-0064, blind-social-0066, blind-social-0068, blind-social-0069, blind-social-0070, blind-social-0072, blind-social-0077, blind-social-0078
