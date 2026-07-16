<!-- zhtw:disable -->
# Holdout Maintainer Confirmation Packet (2026-07-08)

Dataset: `blind-v1`
Source diff review: `docs/reports/holdout-codex-gemini-diff-review-blind-v1-0001-0100-2026-07-08.json`
Raw JSON: `docs/reports/holdout-maintainer-confirmation-blind-v1-0001-0100-2026-07-08.json`

## Boundary

- This packet is for maintainer confirmation only.
- Codex/Gemini values are advisory; maintainer confirmation is the first human decision.
- Do not write these values into `blind-v1.expected.json` until maintainer decisions are recorded.
- `promotion_allowed = false` until expected values are confirmed and source metadata is updated.

## Summary

- Cases needing maintainer confirmation: 59
- Difference cases: 30
- Exact but policy-review cases: 29
- No immediate-question cases: 41

Difference recommendations:

- `codex`: 24
- `gemini`: 5
- `third_value`: 1

## How To Review

For each case, choose one:

- `OK` means accept `Recommended expected` unchanged.
- `EDIT` means write a replacement Taiwan Traditional expected value.
- `DROP` means remove the case from sealed holdout before benchmark.

## Difference Cases

### blind-it-0003：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

Input:

```text
如果缓存过期，客户端应该重新请求配置文件。
```

Codex expected:

```text
如果快取過期，客戶端應該重新請求設定檔。
```

Gemini expected:

```text
如果快取過期，用戶端應該重新要求組態檔。
```

Recommended expected:

```text
如果快取過期，客戶端應該重新請求設定檔。
```

Reason:

API/設定檔語境中「客戶端」「請求」「設定檔」較自然；Gemini 的「要求」「組態檔」偏正式/微軟風格。

Maintainer decision:

```text

```

### blind-it-0008：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

Input:

```text
新版 SDK 支持批量上传文件和取消请求。
```

Codex expected:

```text
新版 SDK 支援批次上傳檔案和取消請求。
```

Gemini expected:

```text
新版 SDK 支援批次上傳檔案和取消要求。
```

Recommended expected:

```text
新版 SDK 支援批次上傳檔案和取消請求。
```

Reason:

API request 在台灣技術文件通常譯「請求」，不是「要求」。

Maintainer decision:

```text

```

### blind-it-0009：recommend `gemini`

- Domain: `it`
- Risk: `candidate_gap`

Input:

```text
这个命令会覆盖本地设置，请先备份原始文件。
```

Codex expected:

```text
這個命令會覆蓋本機設定，請先備份原始檔案。
```

Gemini expected:

```text
這個命令會覆寫本機設定，請先備份原始檔案。
```

Recommended expected:

```text
這個命令會覆寫本機設定，請先備份原始檔案。
```

Reason:

「覆寫本機設定」比「覆蓋本機設定」更貼近 overwrite/override 的技術語境。

Maintainer decision:

```text

```

### blind-it-0011：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

Input:

```text
日志里显示用户权限不足，无法删除这个资源。
```

Codex expected:

```text
日誌裡顯示使用者權限不足，無法刪除這個資源。
```

Gemini expected:

```text
記錄檔裡顯示使用者權限不足，無法刪除這個資源。
```

Recommended expected:

```text
日誌裡顯示使用者權限不足，無法刪除這個資源。
```

Reason:

原文是「日志里」不是明確「日志文件」，「日誌裡」比「記錄檔裡」保留語義。

Maintainer decision:

```text

```

### blind-it-0012：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

Input:

```text
如果消息队列阻塞，消费者会延迟处理通知。
```

Codex expected:

```text
如果訊息佇列阻塞，消費者會延遲處理通知。
```

Gemini expected:

```text
如果訊息佇列阻塞，取用者會延遲處理通知。
```

Recommended expected:

```text
如果訊息佇列阻塞，消費者會延遲處理通知。
```

Reason:

訊息佇列 consumer 台灣工程語境常用「消費者」，「取用者」較少見。

Maintainer decision:

```text

```

### blind-it-0014：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

Input:

```text
合并请求通过检查后，机器人会自动发布预览版本。
```

Codex expected:

```text
合併請求通過檢查後，機器人會自動發布預覽版本。
```

Gemini expected:

```text
合併要求通過檢查後，機器人會自動發佈預覽版本。
```

Recommended expected:

```text
合併請求通過檢查後，機器人會自動發布預覽版本。
```

Reason:

GitLab/Git 語境「合併請求」比「合併要求」自然；「發布」也可接受。

Maintainer decision:

```text

```

### blind-it-0015：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

Input:

```text
你可以用配置文件指定默认语言和时区。
```

Codex expected:

```text
你可以用設定檔指定預設語言和時區。
```

Gemini expected:

```text
你可以用組態檔指定預設語言和時區。
```

Recommended expected:

```text
你可以用設定檔指定預設語言和時區。
```

Reason:

一般 config file 在產品/開發文件中「設定檔」較常見；「組態檔」偏特定風格。

Maintainer decision:

```text

```

### blind-it-0016：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

Input:

```text
数据迁移完成后，请验证索引是否已经重建。
```

Codex expected:

```text
資料遷移完成後，請驗證索引是否已經重建。
```

Gemini expected:

```text
資料移轉完成後，請驗證索引是否已經重建。
```

Recommended expected:

```text
資料遷移完成後，請驗證索引是否已經重建。
```

Reason:

「資料遷移」在資料庫/開發者文件中常見；Gemini「資料移轉」可列 acceptable。

Maintainer decision:

```text

```

### blind-it-0017：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

Input:

```text
这个端点需要签名，否则网关会拒绝请求。
```

Codex expected:

```text
這個端點需要簽章，否則閘道會拒絕請求。
```

Gemini expected:

```text
這個端點需要簽章，否則閘道會拒絕要求。
```

Recommended expected:

```text
這個端點需要簽章，否則閘道會拒絕請求。
```

Reason:

API request 應用「請求」，不是「要求」；「簽章」「閘道」採 Gemini/Codex 一致部分。

Maintainer decision:

```text

```

### blind-it-0018：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

Input:

```text
我们把支付回调放进独立的工作线程处理。
```

Codex expected:

```text
我們把付款回呼放進獨立的工作執行緒處理。
```

Gemini expected:

```text
我們把支付回呼放進獨立的工作執行緒處理。
```

Recommended expected:

```text
我們把付款回呼放進獨立的工作執行緒處理。
```

Reason:

台灣金融/付款流程常用「付款」，「支付」較偏中國用語或泛稱。

Maintainer decision:

```text

```

### blind-it-0019：recommend `gemini`

- Domain: `it`
- Risk: `over_conversion_guard`

Input:

```text
发生冲突时，客户端应该重新下载最新记录。
```

Codex expected:

```text
發生衝突時，客戶端應該重新下載最新記錄。
```

Gemini expected:

```text
發生衝突時，用戶端應該重新下載最新記錄。
```

Recommended expected:

```text
發生衝突時，用戶端應該重新下載最新記錄。
```

Reason:

client-side/客户端 在台灣技術文件常用「用戶端」，比「客戶端」更少歧義。

Maintainer decision:

```text

```

### blind-it-0020：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

Input:

```text
请在测试环境启用详细日志，线上环境保持关闭。
```

Codex expected:

```text
請在測試環境啟用詳細日誌，正式環境保持關閉。
```

Gemini expected:

```text
請在測試環境啟用詳細記錄檔，線上環境保持關閉。
```

Recommended expected:

```text
請在測試環境啟用詳細日誌，正式環境保持關閉。
```

Reason:

中國「线上环境」在部署語境通常是 production，台灣寫「正式環境」較準；「記錄檔」不適合詳細 log 泛稱。

Maintainer decision:

```text

```

### blind-it-0021：recommend `gemini`

- Domain: `it`
- Risk: `candidate_gap`

Input:

```text
压缩包解开后，把二进制文件移动到系统路径。
```

Codex expected:

```text
壓縮檔解開後，把二進位檔案移動到系統路徑。
```

Gemini expected:

```text
壓縮檔解壓縮後，把二進位檔案移動到系統路徑。
```

Recommended expected:

```text
壓縮檔解壓縮後，把二進位檔案移動到系統路徑。
```

Reason:

「解壓縮」比「解開」更明確對應壓縮檔操作。

Maintainer decision:

```text

```

### blind-it-0022：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

Input:

```text
这个插件会在保存文件时格式化代码。
```

Codex expected:

```text
這個外掛會在儲存檔案時格式化程式碼。
```

Gemini expected:

```text
這個外掛程式會在儲存檔案時格式化程式碼。
```

Recommended expected:

```text
這個外掛會在儲存檔案時格式化程式碼。
```

Reason:

「外掛」較簡潔自然；「外掛程式」可接受但較冗。

Maintainer decision:

```text

```

### blind-it-0023：recommend `codex`

- Domain: `it`
- Risk: `candidate_gap`

Input:

```text
任务失败后，调度器会在五分钟后再次尝试。
```

Codex expected:

```text
任務失敗後，排程器會在五分鐘後再次嘗試。
```

Gemini expected:

```text
工作失敗後，排程器會在五分鐘後再次嘗試。
```

Recommended expected:

```text
任務失敗後，排程器會在五分鐘後再次嘗試。
```

Reason:

scheduler task 可譯「任務」，「工作失敗」會稍微改變語感。

Maintainer decision:

```text

```

### blind-it-0025：recommend `gemini`

- Domain: `it`
- Risk: `baseline_guard`

Input:

```text
如果版本号不匹配，安装程序会停止更新。
```

Codex expected:

```text
如果版本號不相符，安裝程式會停止更新。
```

Gemini expected:

```text
如果版本號不符，安裝程式會停止更新。
```

Recommended expected:

```text
如果版本號不符，安裝程式會停止更新。
```

Reason:

「版本號不符」是台灣正式/技術文件中更精簡自然的寫法。

Maintainer decision:

```text

```

### blind-ui-0001：recommend `codex`

- Domain: `ui`
- Risk: `baseline_guard`

Input:

```text
点击保存后，页面会显示上次更新时间。
```

Codex expected:

```text
點選儲存後，頁面會顯示上次更新時間。
```

Gemini expected:

```text
點擊儲存後，頁面會顯示上次更新時間。
```

Recommended expected:

```text
點選儲存後，頁面會顯示上次更新時間。
```

Reason:

UI 操作中「點選」較符合台灣介面文案風格。

Maintainer decision:

```text

```

### blind-ui-0004：recommend `codex`

- Domain: `ui`
- Risk: `candidate_gap`

Input:

```text
拖动滑块调整音量，然后点击应用。
```

Codex expected:

```text
拖曳滑桿調整音量，然後點選套用。
```

Gemini expected:

```text
拖曳滑桿調整音量，然後點擊套用。
```

Recommended expected:

```text
拖曳滑桿調整音量，然後點選套用。
```

Reason:

同上，UI 操作用「點選套用」較穩定。

Maintainer decision:

```text

```

### blind-ui-0006：recommend `codex`

- Domain: `ui`
- Risk: `candidate_gap`

Input:

```text
这个对话框会在离开页面前提醒尚未保存的更改。
```

Codex expected:

```text
這個對話框會在離開頁面前提醒尚未儲存的變更。
```

Gemini expected:

```text
這個對話方塊會在離開頁面前提醒尚未儲存的變更。
```

Recommended expected:

```text
這個對話框會在離開頁面前提醒尚未儲存的變更。
```

Reason:

Web/產品文案常用「對話框」；「對話方塊」偏 Windows/微軟風格。

Maintainer decision:

```text

```

### blind-ui-0008：recommend `codex`

- Domain: `ui`
- Risk: `candidate_gap`

Input:

```text
会员可以在个人资料里修改头像。
```

Codex expected:

```text
會員可以在個人資料裡修改大頭貼。
```

Gemini expected:

```text
會員可以在個人檔案裡修改大頭貼。
```

Recommended expected:

```text
會員可以在個人資料裡修改大頭貼。
```

Reason:

原文「个人资料」直譯台灣產品常用「個人資料」；「個人檔案」較偏 profile 特定產品。

Maintainer decision:

```text

```

### blind-ui-0010：recommend `codex`

- Domain: `ui`
- Risk: `candidate_gap`

Input:

```text
如果密码太短，输入框下方会显示错误消息。
```

Codex expected:

```text
如果密碼太短，輸入框下方會顯示錯誤訊息。
```

Gemini expected:

```text
如果密碼太短，輸入方塊下方會顯示錯誤訊息。
```

Recommended expected:

```text
如果密碼太短，輸入框下方會顯示錯誤訊息。
```

Reason:

台灣產品文案常用「輸入框」；「輸入方塊」較偏微軟風格。

Maintainer decision:

```text

```

### blind-ui-0011：recommend `codex`

- Domain: `ui`
- Risk: `baseline_guard`

Input:

```text
点击返回箭头会回到上一层目录。
```

Codex expected:

```text
點選返回箭頭會回到上一層目錄。
```

Gemini expected:

```text
點擊返回箭頭會回到上一層目錄。
```

Recommended expected:

```text
點選返回箭頭會回到上一層目錄。
```

Reason:

UI 操作用「點選」較一致。

Maintainer decision:

```text

```

### blind-ui-0018：recommend `codex`

- Domain: `ui`
- Risk: `baseline_guard`

Input:

```text
管理页面左侧菜单可以折叠。
```

Codex expected:

```text
管理頁面左側選單可以收合。
```

Gemini expected:

```text
管理頁面左側選單可以摺疊。
```

Recommended expected:

```text
管理頁面左側選單可以收合。
```

Reason:

選單狀態用「收合」較自然；「摺疊」較機械直譯。

Maintainer decision:

```text

```

### blind-llm-0001：recommend `codex`

- Domain: `llm`
- Risk: `candidate_gap`

Input:

```text
这段说明可以放在 README 的快速开始章节。
```

Codex expected:

```text
這段說明可以放在 README 的快速開始章節。
```

Gemini expected:

```text
這段說明可以放在 README 的快速入門章節。
```

Recommended expected:

```text
這段說明可以放在 README 的快速開始章節。
```

Reason:

README section 名稱可用「快速開始」，比「快速入門章節」更貼近 quick start。

Maintainer decision:

```text

```

### blind-llm-0002：recommend `codex`

- Domain: `llm`
- Risk: `candidate_gap`

Input:

```text
请把客服回复改写成更自然的台湾用语。
```

Codex expected:

```text
請把客服回覆改寫成更自然的台灣用語。
```

Gemini expected:

```text
請把客服回覆改寫成更自然的臺灣用語。
```

Recommended expected:

```text
請把客服回覆改寫成更自然的台灣用語。
```

Reason:

專案文件與既有用語多使用「台灣」；不改成較正式的「臺灣」。

Maintainer decision:

```text

```

### blind-llm-0010：recommend `codex`

- Domain: `llm`
- Risk: `candidate_gap`

Input:

```text
这份教程适合第一次部署服务的开发者。
```

Codex expected:

```text
這份教學適合第一次部署服務的開發者。
```

Gemini expected:

```text
這份教學課程適合第一次部署服務的開發者。
```

Recommended expected:

```text
這份教學適合第一次部署服務的開發者。
```

Reason:

「教程」在台灣常轉「教學」；「教學課程」多了課程語意。

Maintainer decision:

```text

```

### blind-llm-0012：recommend `gemini`

- Domain: `llm`
- Risk: `candidate_gap`

Input:

```text
模型输出的代码片段应该包含必要的导入语句。
```

Codex expected:

```text
模型輸出的程式碼片段應該包含必要的匯入語句。
```

Gemini expected:

```text
模型輸出的程式碼片段應該包含必要的匯入陳述式。
```

Recommended expected:

```text
模型輸出的程式碼片段應該包含必要的匯入陳述式。
```

Reason:

程式語境 import statement 譯為「匯入陳述式」較精確。

Maintainer decision:

```text

```

### blind-llm-0013：recommend `third_value`

- Domain: `llm`
- Risk: `candidate_gap`

Input:

```text
这条系统消息限制助理不能泄露内部规则。
```

Codex expected:

```text
這則系統訊息限制助理不能洩露內部規則。
```

Gemini expected:

```text
這條系統訊息限制助理不能洩漏內部規則。
```

Recommended expected:

```text
這則系統訊息限制助理不能洩漏內部規則。
```

Reason:

建議第三版：「這則系統訊息限制助理不能洩漏內部規則。」；Codex 的「這則」較自然，Gemini 的「洩漏」較自然。

Maintainer decision:

```text

```

### blind-formal-0012：recommend `codex`

- Domain: `formal`
- Risk: `over_conversion_guard`

Input:

```text
合同签署前，双方应确认付款条件。
```

Codex expected:

```text
契約簽署前，雙方應確認付款條件。
```

Gemini expected:

```text
合約簽署前，雙方應確認付款條件。
```

Recommended expected:

```text
契約簽署前，雙方應確認付款條件。
```

Reason:

正式/法律語境「契約」較適合；也與高風險 legal 用語一致。

Maintainer decision:

```text

```

### blind-social-0015：recommend `codex`

- Domain: `social`
- Risk: `candidate_gap`

Input:

```text
今天的直播回放什么时候会上架？
```

Codex expected:

```text
今天的直播重播什麼時候會上架？
```

Gemini expected:

```text
今天的直播回放什麼時候會上架？
```

Recommended expected:

```text
今天的直播重播什麼時候會上架？
```

Reason:

台灣日常/影音語境「直播重播」比「直播回放」自然。

Maintainer decision:

```text

```


## Exact But Policy Review

### blind-it-0002：quick confirm

- Domain: `it`
- Risk: `candidate_gap`

Recommended expected:

```text
使用者登入後，伺服器會回傳存取權杖和重新整理權杖。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-it-0004：quick confirm

- Domain: `it`
- Risk: `candidate_gap`

Recommended expected:

```text
部署指令碼需要讀取環境變數裡的資料庫憑證。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-it-0005：quick confirm

- Domain: `it`
- Risk: `candidate_gap`

Recommended expected:

```text
這個介面會分頁回傳訂單清單，每頁最多五十筆。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-it-0006：quick confirm

- Domain: `it`
- Risk: `over_conversion_guard`

Recommended expected:

```text
當連線逾時發生時，請不要重複送出表單。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-it-0007：quick confirm

- Domain: `it`
- Risk: `candidate_gap`

Recommended expected:

```text
我們在背景工作裡記錄每一次重試的原因。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-it-0010：quick confirm

- Domain: `it`
- Risk: `candidate_gap`

Recommended expected:

```text
管理員可以在主控台停用異常的 API 金鑰。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-ui-0012：quick confirm

- Domain: `ui`
- Risk: `candidate_gap`

Recommended expected:

```text
你可以把常用頁面加入我的最愛。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-ui-0017：quick confirm

- Domain: `ui`
- Risk: `over_conversion_guard`

Recommended expected:

```text
請在刪除帳號前再次輸入你的電子郵件。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-ui-0020：quick confirm

- Domain: `ui`
- Risk: `candidate_gap`

Recommended expected:

```text
系統會在工作階段即將過期時彈出提示。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-llm-0005：quick confirm

- Domain: `llm`
- Risk: `over_conversion_guard`

Recommended expected:

```text
如果回答涉及醫療建議，請提醒使用者諮詢專業人員。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-llm-0006：quick confirm

- Domain: `llm`
- Risk: `over_conversion_guard`

Recommended expected:

```text
產生測試資料時，不要使用真實的個人資訊。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-llm-0011：quick confirm

- Domain: `llm`
- Risk: `over_conversion_guard`

Recommended expected:

```text
自動回覆需要避免承諾無法保證的處理時間。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-formal-0004：quick confirm

- Domain: `formal`
- Risk: `over_conversion_guard`

Recommended expected:

```text
主管機關提醒業者不得誤導消費者。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-formal-0007：quick confirm

- Domain: `formal`
- Risk: `over_conversion_guard`

Recommended expected:

```text
申請人須在期限內補交相關證明文件。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-formal-0010：quick confirm

- Domain: `formal`
- Risk: `candidate_gap`

Recommended expected:

```text
新聞稿指出，合作專案不會影響現有使用者權益。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-formal-0015：quick confirm

- Domain: `formal`
- Risk: `over_conversion_guard`

Recommended expected:

```text
本聲明不構成任何投資建議。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-social-0007：quick confirm

- Domain: `social`
- Risk: `candidate_gap`

Recommended expected:

```text
我剛剛在便利商店看到同款充電線。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-social-0009：quick confirm

- Domain: `social`
- Risk: `over_conversion_guard`

Recommended expected:

```text
這首歌的副歌很洗腦，大家都在哼。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-social-0011：quick confirm

- Domain: `social`
- Risk: `over_conversion_guard`

Recommended expected:

```text
我們先在捷運站出口集合。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-high-risk-0001：quick confirm

- Domain: `high_risk`
- Risk: `over_conversion_guard`

Recommended expected:

```text
不得以定型化契約條款排除責任。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-high-risk-0002：quick confirm

- Domain: `high_risk`
- Risk: `over_conversion_guard`

Recommended expected:

```text
跨行匯款手續費由使用者負擔。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-high-risk-0003：quick confirm

- Domain: `high_risk`
- Risk: `over_conversion_guard`

Recommended expected:

```text
請依醫師指示服用本藥，並留意過敏反應。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-high-risk-0004：quick confirm

- Domain: `high_risk`
- Risk: `over_conversion_guard`

Recommended expected:

```text
投保前應詳閱保單條款和除外責任。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-high-risk-0005：quick confirm

- Domain: `high_risk`
- Risk: `candidate_gap`

Recommended expected:

```text
申請補助時，必須提供有效的身分證明文件。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-high-risk-0006：quick confirm

- Domain: `high_risk`
- Risk: `over_conversion_guard`

Recommended expected:

```text
病人出現胸痛或呼吸困難時，應立即就醫。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-high-risk-0007：quick confirm

- Domain: `high_risk`
- Risk: `candidate_gap`

Recommended expected:

```text
貸款利率可能隨市場條件調整。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-high-risk-0008：quick confirm

- Domain: `high_risk`
- Risk: `over_conversion_guard`

Recommended expected:

```text
個人資料不得用於原申請目的以外的用途。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-high-risk-0009：quick confirm

- Domain: `high_risk`
- Risk: `over_conversion_guard`

Recommended expected:

```text
本合約爭議適用中華民國法律。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```

### blind-high-risk-0010：quick confirm

- Domain: `high_risk`
- Risk: `over_conversion_guard`

Recommended expected:

```text
醫療紀錄應依法保存，不得任意刪除。
```

Reason:

Codex/Gemini 一致，但屬 high_risk、over_conversion_guard 或前序 medium confidence，仍建議 maintainer 快速確認。

Maintainer decision:

```text

```


## No Immediate Question

- `blind-it-0001`
- `blind-it-0013`
- `blind-it-0024`
- `blind-ui-0002`
- `blind-ui-0003`
- `blind-ui-0005`
- `blind-ui-0007`
- `blind-ui-0009`
- `blind-ui-0013`
- `blind-ui-0014`
- `blind-ui-0015`
- `blind-ui-0016`
- `blind-ui-0019`
- `blind-llm-0003`
- `blind-llm-0004`
- `blind-llm-0007`
- `blind-llm-0008`
- `blind-llm-0009`
- `blind-llm-0014`
- `blind-llm-0015`
- `blind-formal-0001`
- `blind-formal-0002`
- `blind-formal-0003`
- `blind-formal-0005`
- `blind-formal-0006`
- `blind-formal-0008`
- `blind-formal-0009`
- `blind-formal-0011`
- `blind-formal-0013`
- `blind-formal-0014`
- `blind-social-0001`
- `blind-social-0002`
- `blind-social-0003`
- `blind-social-0004`
- `blind-social-0005`
- `blind-social-0006`
- `blind-social-0008`
- `blind-social-0010`
- `blind-social-0012`
- `blind-social-0013`
- `blind-social-0014`
