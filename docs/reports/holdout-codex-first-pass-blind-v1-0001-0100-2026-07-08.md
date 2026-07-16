<!-- zhtw:disable -->
# Holdout Codex First-Pass Advisory (2026-07-08)

Dataset: `blind-v1`
Inputs: `benchmarks/accuracy/blind-v1.inputs.json`
Raw JSON: `docs/reports/holdout-codex-first-pass-blind-v1-0001-0100-2026-07-08.json`
Reviewer: `codex`
Stage: `first_pass_advisory`
Cases: 100

## Policy

- This report is advisory only.
- It is not ground truth and must not populate `blind-v1.expected.json` without maintainer confirmation.
- No zhtw, OpenCC, zhconv, or Gemini output was used as a source of expected values.
- Next step: run Gemini independent advisory from the input-only packet, then compare differences.

## Summary

- Total cases: 100
- High confidence: 83
- Medium confidence: 17
- Review needed: 36

Domain distribution:

- `formal`: 15
- `high_risk`: 10
- `it`: 25
- `llm`: 15
- `social`: 15
- `ui`: 20

## Review-Needed Cases

- `blind-it-0002` (it, medium): OAuth/身分驗證術語有「重新整理權杖」與「更新權杖」兩種常見譯法，需後續確認產品慣例。
- `blind-it-0004` (it, medium): 台灣技術文件常用「指令碼」，但口語與開發者文件也常見「腳本」。
- `blind-it-0005` (it, medium): 「接口」在 API 語境可譯「介面」或直接寫 API；主句未明確寫 API，先採「介面」。
- `blind-it-0006` (it, high): 「连接超时」轉「連線逾時」，UI 動作用「送出表單」較自然。
- `blind-it-0007` (it, medium): 「后台任务」可為「背景工作」或「背景任務」，需依系統用語確認。
- `blind-it-0010` (it, medium): 「控制台」採台灣常見「主控台」；「異常的 API 金鑰」語氣可再順修。
- `blind-it-0012` (it, medium): 訊息佇列/消費者為技術術語；「阻塞」在程式語境可保留。
- `blind-it-0017` (it, medium): API 安全語境「signature」多譯「簽章」，但也可能依產品用「簽名」。
- `blind-it-0018` (it, medium): 「回调」轉「回呼」；付款/支付需依產品金融用語確認。
- `blind-it-0019` (it, medium): 資料庫 record 可用「記錄」；一般語境也可見「紀錄」。
- `blind-ui-0008` (ui, medium): 台灣消費者 UI 常見「大頭貼」，但部分產品仍用「頭像」。
- `blind-ui-0012` (ui, medium): 「收藏夹」在台灣 UI 常見「我的最愛」，但也有產品用「收藏」。
- `blind-ui-0017` (ui, high): 「账号」轉台灣常用「帳號」。
- `blind-ui-0020` (ui, medium): 「会话」在軟體語境常譯「工作階段」，但產品也可能用「作業階段」。
- `blind-llm-0005` (llm, high): 醫療語境「咨询」轉「諮詢」，「用户」轉「使用者」。
- `blind-llm-0006` (llm, high): 台灣多用「資料」「資訊」。
- `blind-llm-0011` (llm, high): 正式客服語境自然轉換。
- `blind-formal-0004` (formal, high): 「业者」轉「業者」，「主管機關」已是台灣正式用語。
- `blind-formal-0007` (formal, high): 正式文件直轉，保留「須」。
- `blind-formal-0010` (formal, medium): 「项目」可依語境譯「專案」或「計畫」，需確認合作性質。
- `blind-formal-0012` (formal, medium): 法律/正式文件中「合同」可譯「契約」或「合約」，需依文件性質確認。
- `blind-formal-0015` (formal, high): 投資免責文字直轉。
- `blind-social-0007` (social, medium): 「便利店」在台灣可轉「便利商店」，口語也常用「超商」。
- `blind-social-0009` (social, high): 「洗腦」可保留，符合台灣口語。
- `blind-social-0011` (social, high): 「捷運站」為台灣交通用語。
- `blind-social-0015` (social, medium): 「直播回放」在台灣較常改為「直播重播」，但產品用語可能保留「回放」。
- `blind-high-risk-0001` (high_risk, high): 法律語境使用「定型化契約條款」。
- `blind-high-risk-0002` (high_risk, high): 金融語境「跨行匯款」「手續費」直轉。
- `blind-high-risk-0003` (high_risk, high): 醫療用語使用「醫師」「過敏反應」。
- `blind-high-risk-0004` (high_risk, high): 保險正式用語「保單條款」「除外責任」。
- `blind-high-risk-0005` (high_risk, high): 台灣正式文件用「身分證明文件」。
- `blind-high-risk-0006` (high_risk, high): 醫療安全語境直轉。
- `blind-high-risk-0007` (high_risk, high): 金融語境直轉。
- `blind-high-risk-0008` (high_risk, high): 個資法語境用「個人資料」。
- `blind-high-risk-0009` (high_risk, medium): 「合約」與「契約」都常見；正式法務文件可能需依上下文決定。
- `blind-high-risk-0010` (high_risk, high): 醫療語境使用「醫療紀錄」。

## Cases

### blind-it-0001

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
这个函数会抛出异常，请在调用前检查返回值。
```

Codex expected:

```text
這個函式會拋出例外，請在呼叫前檢查回傳值。
```

Acceptable variants:

```text
(none)
```

Rationale:

IT 語境使用「函式」「例外」「呼叫」「回傳值」。

### blind-it-0002

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
用户登录后，服务器会返回访问令牌和刷新令牌。
```

Codex expected:

```text
使用者登入後，伺服器會回傳存取權杖和重新整理權杖。
```

Acceptable variants:

```text
使用者登入後，伺服器會回傳存取權杖和更新權杖。
```

Rationale:

OAuth/身分驗證術語有「重新整理權杖」與「更新權杖」兩種常見譯法，需後續確認產品慣例。

### blind-it-0003

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
如果缓存过期，客户端应该重新请求配置文件。
```

Codex expected:

```text
如果快取過期，客戶端應該重新請求設定檔。
```

Acceptable variants:

```text
(none)
```

Rationale:

「缓存」轉「快取」，「配置文件」轉「設定檔」。

### blind-it-0004

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
部署脚本需要读取环境变量里的数据库凭证。
```

Codex expected:

```text
部署指令碼需要讀取環境變數裡的資料庫憑證。
```

Acceptable variants:

```text
部署腳本需要讀取環境變數裡的資料庫憑證。
```

Rationale:

台灣技術文件常用「指令碼」，但口語與開發者文件也常見「腳本」。

### blind-it-0005

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
这个接口会分页返回订单列表，每页最多五十条。
```

Codex expected:

```text
這個介面會分頁回傳訂單清單，每頁最多五十筆。
```

Acceptable variants:

```text
這個 API 會分頁回傳訂單清單，每頁最多五十筆。
```

Rationale:

「接口」在 API 語境可譯「介面」或直接寫 API；主句未明確寫 API，先採「介面」。

### blind-it-0006

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `it_term, ui_term`

Input:

```text
当连接超时发生时，请不要重复提交表单。
```

Codex expected:

```text
當連線逾時發生時，請不要重複送出表單。
```

Acceptable variants:

```text
(none)
```

Rationale:

「连接超时」轉「連線逾時」，UI 動作用「送出表單」較自然。

### blind-it-0007

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
我们在后台任务里记录每一次重试的原因。
```

Codex expected:

```text
我們在背景工作裡記錄每一次重試的原因。
```

Acceptable variants:

```text
我們在背景任務裡記錄每一次重試的原因。
```

Rationale:

「后台任务」可為「背景工作」或「背景任務」，需依系統用語確認。

### blind-it-0008

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
新版 SDK 支持批量上传文件和取消请求。
```

Codex expected:

```text
新版 SDK 支援批次上傳檔案和取消請求。
```

Acceptable variants:

```text
(none)
```

Rationale:

「支持」轉「支援」，「批量」轉「批次」，「文件」轉「檔案」。

### blind-it-0009

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
这个命令会覆盖本地设置，请先备份原始文件。
```

Codex expected:

```text
這個命令會覆蓋本機設定，請先備份原始檔案。
```

Acceptable variants:

```text
(none)
```

Rationale:

「本地设置」轉「本機設定」。

### blind-it-0010

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
管理员可以在控制台停用异常的 API 密钥。
```

Codex expected:

```text
管理員可以在主控台停用異常的 API 金鑰。
```

Acceptable variants:

```text
管理員可以在主控台停用有異常的 API 金鑰。
```

Rationale:

「控制台」採台灣常見「主控台」；「異常的 API 金鑰」語氣可再順修。

### blind-it-0011

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
日志里显示用户权限不足，无法删除这个资源。
```

Codex expected:

```text
日誌裡顯示使用者權限不足，無法刪除這個資源。
```

Acceptable variants:

```text
(none)
```

Rationale:

「日志」轉「日誌」，「用户」轉「使用者」。

### blind-it-0012

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
如果消息队列阻塞，消费者会延迟处理通知。
```

Codex expected:

```text
如果訊息佇列阻塞，消費者會延遲處理通知。
```

Acceptable variants:

```text
(none)
```

Rationale:

訊息佇列/消費者為技術術語；「阻塞」在程式語境可保留。

### blind-it-0013

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
这个字段只接受小写字母和数字。
```

Codex expected:

```text
這個欄位只接受小寫字母和數字。
```

Acceptable variants:

```text
(none)
```

Rationale:

「字段」轉「欄位」。

### blind-it-0014

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
合并请求通过检查后，机器人会自动发布预览版本。
```

Codex expected:

```text
合併請求通過檢查後，機器人會自動發布預覽版本。
```

Acceptable variants:

```text
(none)
```

Rationale:

Git/CI 語境使用「合併請求」「檢查」「發布」。

### blind-it-0015

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
你可以用配置文件指定默认语言和时区。
```

Codex expected:

```text
你可以用設定檔指定預設語言和時區。
```

Acceptable variants:

```text
(none)
```

Rationale:

「配置文件」轉「設定檔」，「默认」轉「預設」。

### blind-it-0016

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
数据迁移完成后，请验证索引是否已经重建。
```

Codex expected:

```text
資料遷移完成後，請驗證索引是否已經重建。
```

Acceptable variants:

```text
(none)
```

Rationale:

「数据迁移」轉「資料遷移」。

### blind-it-0017

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
这个端点需要签名，否则网关会拒绝请求。
```

Codex expected:

```text
這個端點需要簽章，否則閘道會拒絕請求。
```

Acceptable variants:

```text
這個端點需要簽名，否則閘道會拒絕請求。
```

Rationale:

API 安全語境「signature」多譯「簽章」，但也可能依產品用「簽名」。

### blind-it-0018

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
我们把支付回调放进独立的工作线程处理。
```

Codex expected:

```text
我們把付款回呼放進獨立的工作執行緒處理。
```

Acceptable variants:

```text
我們把支付回呼放進獨立的工作執行緒處理。
```

Rationale:

「回调」轉「回呼」；付款/支付需依產品金融用語確認。

### blind-it-0019

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `over_conversion_guard`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `it_term`

Input:

```text
发生冲突时，客户端应该重新下载最新记录。
```

Codex expected:

```text
發生衝突時，客戶端應該重新下載最新記錄。
```

Acceptable variants:

```text
發生衝突時，客戶端應該重新下載最新紀錄。
```

Rationale:

資料庫 record 可用「記錄」；一般語境也可見「紀錄」。

### blind-it-0020

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
请在测试环境启用详细日志，线上环境保持关闭。
```

Codex expected:

```text
請在測試環境啟用詳細日誌，正式環境保持關閉。
```

Acceptable variants:

```text
(none)
```

Rationale:

「线上环境」在部署語境轉「正式環境」。

### blind-it-0021

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
压缩包解开后，把二进制文件移动到系统路径。
```

Codex expected:

```text
壓縮檔解開後，把二進位檔案移動到系統路徑。
```

Acceptable variants:

```text
(none)
```

Rationale:

「压缩包」轉「壓縮檔」，「二进制文件」轉「二進位檔案」。

### blind-it-0022

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
这个插件会在保存文件时格式化代码。
```

Codex expected:

```text
這個外掛會在儲存檔案時格式化程式碼。
```

Acceptable variants:

```text
(none)
```

Rationale:

「插件」轉「外掛」，「代码」轉「程式碼」。

### blind-it-0023

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
任务失败后，调度器会在五分钟后再次尝试。
```

Codex expected:

```text
任務失敗後，排程器會在五分鐘後再次嘗試。
```

Acceptable variants:

```text
(none)
```

Rationale:

「调度器」轉「排程器」。

### blind-it-0024

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
请确认防火墙允许代理服务器访问内部服务。
```

Codex expected:

```text
請確認防火牆允許代理伺服器存取內部服務。
```

Acceptable variants:

```text
(none)
```

Rationale:

「代理服务器」轉「代理伺服器」，「访问」轉「存取」。

### blind-it-0025

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
如果版本号不匹配，安装程序会停止更新。
```

Codex expected:

```text
如果版本號不相符，安裝程式會停止更新。
```

Acceptable variants:

```text
(none)
```

Rationale:

「不匹配」轉自然台灣用語「不相符」。

### blind-ui-0001

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
点击保存后，页面会显示上次更新时间。
```

Codex expected:

```text
點選儲存後，頁面會顯示上次更新時間。
```

Acceptable variants:

```text
(none)
```

Rationale:

UI 動作用「點選」「儲存」。

### blind-ui-0002

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
请输入验证码，系统会发送简讯到你的手机。
```

Codex expected:

```text
請輸入驗證碼，系統會傳送簡訊到你的手機。
```

Acceptable variants:

```text
(none)
```

Rationale:

「发送简讯」轉「傳送簡訊」。

### blind-ui-0003

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
你可以在设置页面关闭桌面通知。
```

Codex expected:

```text
你可以在設定頁面關閉桌面通知。
```

Acceptable variants:

```text
(none)
```

Rationale:

「设置」轉「設定」。

### blind-ui-0004

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
拖动滑块调整音量，然后点击应用。
```

Codex expected:

```text
拖曳滑桿調整音量，然後點選套用。
```

Acceptable variants:

```text
(none)
```

Rationale:

UI 元件用「拖曳滑桿」「套用」。

### blind-ui-0005

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
搜索结果为空时，显示重置筛选按钮。
```

Codex expected:

```text
搜尋結果為空時，顯示重設篩選按鈕。
```

Acceptable variants:

```text
(none)
```

Rationale:

「搜索」轉「搜尋」，「重置」轉「重設」。

### blind-ui-0006

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
这个对话框会在离开页面前提醒尚未保存的更改。
```

Codex expected:

```text
這個對話框會在離開頁面前提醒尚未儲存的變更。
```

Acceptable variants:

```text
(none)
```

Rationale:

「更改」在 UI 文字轉「變更」。

### blind-ui-0007

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
下载完成后，通知中心会显示打开文件的按钮。
```

Codex expected:

```text
下載完成後，通知中心會顯示開啟檔案的按鈕。
```

Acceptable variants:

```text
(none)
```

Rationale:

「打开文件」轉 UI 常用「開啟檔案」。

### blind-ui-0008

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `ui_term, regional_term`

Input:

```text
会员可以在个人资料里修改头像。
```

Codex expected:

```text
會員可以在個人資料裡修改大頭貼。
```

Acceptable variants:

```text
會員可以在個人資料裡修改頭像。
```

Rationale:

台灣消費者 UI 常見「大頭貼」，但部分產品仍用「頭像」。

### blind-ui-0009

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
表格支持按创建时间排序和按状态筛选。
```

Codex expected:

```text
表格支援依建立時間排序和依狀態篩選。
```

Acceptable variants:

```text
(none)
```

Rationale:

「创建时间」轉「建立時間」。

### blind-ui-0010

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
如果密码太短，输入框下方会显示错误消息。
```

Codex expected:

```text
如果密碼太短，輸入框下方會顯示錯誤訊息。
```

Acceptable variants:

```text
(none)
```

Rationale:

「错误消息」轉「錯誤訊息」。

### blind-ui-0011

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
点击返回箭头会回到上一层目录。
```

Codex expected:

```text
點選返回箭頭會回到上一層目錄。
```

Acceptable variants:

```text
(none)
```

Rationale:

UI 動作用「點選」。

### blind-ui-0012

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `ui_term, regional_term`

Input:

```text
你可以把常用页面加入收藏夹。
```

Codex expected:

```text
你可以把常用頁面加入我的最愛。
```

Acceptable variants:

```text
你可以把常用頁面加入收藏。
```

Rationale:

「收藏夹」在台灣 UI 常見「我的最愛」，但也有產品用「收藏」。

### blind-ui-0013

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
开启深色模式后，图表颜色会自动调整。
```

Codex expected:

```text
開啟深色模式後，圖表顏色會自動調整。
```

Acceptable variants:

```text
(none)
```

Rationale:

「开启」轉「開啟」。

### blind-ui-0014

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
语言切换后，当前草稿不会被清除。
```

Codex expected:

```text
語言切換後，目前草稿不會被清除。
```

Acceptable variants:

```text
(none)
```

Rationale:

「当前」轉「目前」。

### blind-ui-0015

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
订单取消成功后，按钮会变成灰色。
```

Codex expected:

```text
訂單取消成功後，按鈕會變成灰色。
```

Acceptable variants:

```text
(none)
```

Rationale:

直轉即可，保留 UI 狀態語氣。

### blind-ui-0016

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
当网络中断时，页面顶部显示离线提示。
```

Codex expected:

```text
當網路中斷時，頁面頂端顯示離線提示。
```

Acceptable variants:

```text
(none)
```

Rationale:

「网络」轉「網路」，「顶部」轉「頂端」。

### blind-ui-0017

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `ui_term`

Input:

```text
请在删除账号前再次输入你的电子邮件。
```

Codex expected:

```text
請在刪除帳號前再次輸入你的電子郵件。
```

Acceptable variants:

```text
(none)
```

Rationale:

「账号」轉台灣常用「帳號」。

### blind-ui-0018

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
管理页面左侧菜单可以折叠。
```

Codex expected:

```text
管理頁面左側選單可以收合。
```

Acceptable variants:

```text
(none)
```

Rationale:

「菜单」轉「選單」，「折叠」轉「收合」。

### blind-ui-0019

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `ui_term`

Input:

```text
图片上传失败时，缩略图旁边会显示重试图标。
```

Codex expected:

```text
圖片上傳失敗時，縮圖旁邊會顯示重試圖示。
```

Acceptable variants:

```text
(none)
```

Rationale:

「缩略图」轉「縮圖」，「图标」轉「圖示」。

### blind-ui-0020

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `ui_term, it_term`

Input:

```text
系统会在会话即将过期时弹出提示。
```

Codex expected:

```text
系統會在工作階段即將過期時彈出提示。
```

Acceptable variants:

```text
系統會在作業階段即將過期時彈出提示。
```

Rationale:

「会话」在軟體語境常譯「工作階段」，但產品也可能用「作業階段」。

### blind-llm-0001

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
这段说明可以放在 README 的快速开始章节。
```

Codex expected:

```text
這段說明可以放在 README 的快速開始章節。
```

Acceptable variants:

```text
(none)
```

Rationale:

技術文件語境「快速开始」轉「快速開始」。

### blind-llm-0002

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
请把客服回复改写成更自然的台湾用语。
```

Codex expected:

```text
請把客服回覆改寫成更自然的台灣用語。
```

Acceptable variants:

```text
(none)
```

Rationale:

「台湾用语」轉「台灣用語」。

### blind-llm-0003

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
模型生成的摘要保留了原文的关键限制。
```

Codex expected:

```text
模型產生的摘要保留了原文的關鍵限制。
```

Acceptable variants:

```text
(none)
```

Rationale:

「生成」作動詞轉「產生」。

### blind-llm-0004

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
这份产品文案强调团队协作和权限管理。
```

Codex expected:

```text
這份產品文案強調團隊協作和權限管理。
```

Acceptable variants:

```text
(none)
```

Rationale:

「权限」轉「權限」。

### blind-llm-0005

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term, regional_term`

Input:

```text
如果回答涉及医疗建议，请提醒用户咨询专业人员。
```

Codex expected:

```text
如果回答涉及醫療建議，請提醒使用者諮詢專業人員。
```

Acceptable variants:

```text
(none)
```

Rationale:

醫療語境「咨询」轉「諮詢」，「用户」轉「使用者」。

### blind-llm-0006

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `regional_term`

Input:

```text
生成测试资料时，不要使用真实的个人信息。
```

Codex expected:

```text
產生測試資料時，不要使用真實的個人資訊。
```

Acceptable variants:

```text
(none)
```

Rationale:

台灣多用「資料」「資訊」。

### blind-llm-0007

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
这段提示词要求模型先列出假设再给结论。
```

Codex expected:

```text
這段提示詞要求模型先列出假設再給結論。
```

Acceptable variants:

```text
(none)
```

Rationale:

「提示词」轉「提示詞」。

### blind-llm-0008

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
机器人应该在不知道答案时明确说明限制。
```

Codex expected:

```text
機器人應該在不知道答案時明確說明限制。
```

Acceptable variants:

```text
(none)
```

Rationale:

直轉即可，保留「機器人」。

### blind-llm-0009

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
请把长段落拆成三点，方便使用者快速阅读。
```

Codex expected:

```text
請把長段落拆成三點，方便使用者快速閱讀。
```

Acceptable variants:

```text
(none)
```

Rationale:

「使用者」符合台灣產品語境。

### blind-llm-0010

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term, regional_term`

Input:

```text
这份教程适合第一次部署服务的开发者。
```

Codex expected:

```text
這份教學適合第一次部署服務的開發者。
```

Acceptable variants:

```text
(none)
```

Rationale:

「教程」轉台灣常用「教學」。

### blind-llm-0011

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `formal_term`

Input:

```text
自动回复需要避免承诺无法保证的处理时间。
```

Codex expected:

```text
自動回覆需要避免承諾無法保證的處理時間。
```

Acceptable variants:

```text
(none)
```

Rationale:

正式客服語境自然轉換。

### blind-llm-0012

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
模型输出的代码片段应该包含必要的导入语句。
```

Codex expected:

```text
模型輸出的程式碼片段應該包含必要的匯入語句。
```

Acceptable variants:

```text
(none)
```

Rationale:

程式語境「代码」轉「程式碼」，「导入」轉「匯入」。

### blind-llm-0013

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `it_term`

Input:

```text
这条系统消息限制助理不能泄露内部规则。
```

Codex expected:

```text
這則系統訊息限制助理不能洩露內部規則。
```

Acceptable variants:

```text
(none)
```

Rationale:

「消息」轉「訊息」，「泄露」轉「洩露」。

### blind-llm-0014

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
使用者要求比较方案时，请先说明评估标准。
```

Codex expected:

```text
使用者要求比較方案時，請先說明評估標準。
```

Acceptable variants:

```text
(none)
```

Rationale:

「用户」轉「使用者」。

### blind-llm-0015

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
这段公告要同时适合网页和电子邮件使用。
```

Codex expected:

```text
這段公告要同時適合網頁和電子郵件使用。
```

Acceptable variants:

```text
(none)
```

Rationale:

「网页」轉「網頁」。

### blind-formal-0001

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
本计划将分阶段公布实施细则和申请流程。
```

Codex expected:

```text
本計畫將分階段公布實施細則和申請流程。
```

Acceptable variants:

```text
(none)
```

Rationale:

正式文件中「计划」轉「計畫」。

### blind-formal-0002

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
公司董事会已经核准年度预算调整案。
```

Codex expected:

```text
公司董事會已經核准年度預算調整案。
```

Acceptable variants:

```text
(none)
```

Rationale:

台灣正式文件常用「核准」。

### blind-formal-0003

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
研究团队发现数据来源存在明显偏差。
```

Codex expected:

```text
研究團隊發現資料來源存在明顯偏差。
```

Acceptable variants:

```text
(none)
```

Rationale:

「数据」轉「資料」。

### blind-formal-0004

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `formal_term`

Input:

```text
主管机关提醒业者不得误导消费者。
```

Codex expected:

```text
主管機關提醒業者不得誤導消費者。
```

Acceptable variants:

```text
(none)
```

Rationale:

「业者」轉「業者」，「主管機關」已是台灣正式用語。

### blind-formal-0005

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
新制度预计明年第一季度开始试办。
```

Codex expected:

```text
新制度預計明年第一季開始試辦。
```

Acceptable variants:

```text
(none)
```

Rationale:

台灣常用「第一季」而非「第一季度」。

### blind-formal-0006

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
会议记录应列明出席人员和决议事项。
```

Codex expected:

```text
會議紀錄應列明出席人員和決議事項。
```

Acceptable variants:

```text
(none)
```

Rationale:

「会议记录」作名詞轉「會議紀錄」。

### blind-formal-0007

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `formal_term`

Input:

```text
申请人须在期限内补交相关证明文件。
```

Codex expected:

```text
申請人須在期限內補交相關證明文件。
```

Acceptable variants:

```text
(none)
```

Rationale:

正式文件直轉，保留「須」。

### blind-formal-0008

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term, it_term`

Input:

```text
该报告建议提高资讯安全审查频率。
```

Codex expected:

```text
該報告建議提高資訊安全審查頻率。
```

Acceptable variants:

```text
(none)
```

Rationale:

台灣語境用「資訊安全」。

### blind-formal-0009

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
政府将持续追踪政策执行效果。
```

Codex expected:

```text
政府將持續追蹤政策執行效果。
```

Acceptable variants:

```text
(none)
```

Rationale:

直轉即可。

### blind-formal-0010

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `formal_term, regional_term`

Input:

```text
新闻稿指出，合作项目不会影响现有用户权益。
```

Codex expected:

```text
新聞稿指出，合作專案不會影響現有使用者權益。
```

Acceptable variants:

```text
新聞稿指出，合作計畫不會影響現有使用者權益。
```

Rationale:

「项目」可依語境譯「專案」或「計畫」，需確認合作性質。

### blind-formal-0011

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
委员会要求承办单位重新评估风险。
```

Codex expected:

```text
委員會要求承辦單位重新評估風險。
```

Acceptable variants:

```text
(none)
```

Rationale:

正式文件直轉。

### blind-formal-0012

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `over_conversion_guard`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `formal_term, high_risk_term`

Input:

```text
合同签署前，双方应确认付款条件。
```

Codex expected:

```text
契約簽署前，雙方應確認付款條件。
```

Acceptable variants:

```text
合約簽署前，雙方應確認付款條件。
```

Rationale:

法律/正式文件中「合同」可譯「契約」或「合約」，需依文件性質確認。

### blind-formal-0013

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
统计资料显示，服务使用量持续增加。
```

Codex expected:

```text
統計資料顯示，服務使用量持續增加。
```

Acceptable variants:

```text
(none)
```

Rationale:

「资料」轉「資料」。

### blind-formal-0014

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `formal_term`

Input:

```text
采购案将依公开程序办理。
```

Codex expected:

```text
採購案將依公開程序辦理。
```

Acceptable variants:

```text
(none)
```

Rationale:

台灣正式用語「採購案」。

### blind-formal-0015

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `formal_term, high_risk_term`

Input:

```text
本声明不构成任何投资建议。
```

Codex expected:

```text
本聲明不構成任何投資建議。
```

Acceptable variants:

```text
(none)
```

Rationale:

投資免責文字直轉。

### blind-social-0001

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
我今天下班后想去买一杯珍珠奶茶。
```

Codex expected:

```text
我今天下班後想去買一杯珍珠奶茶。
```

Acceptable variants:

```text
(none)
```

Rationale:

日常語氣直轉。

### blind-social-0002

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
这个视频的字幕有点太快，我来不及看完。
```

Codex expected:

```text
這個影片的字幕有點太快，我來不及看完。
```

Acceptable variants:

```text
(none)
```

Rationale:

台灣常用「影片」。

### blind-social-0003

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
周末如果没下雨，我们就去骑脚踏车。
```

Codex expected:

```text
週末如果沒下雨，我們就去騎腳踏車。
```

Acceptable variants:

```text
(none)
```

Rationale:

「周末」轉「週末」。

### blind-social-0004

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
群组里有人分享了新的餐厅名单。
```

Codex expected:

```text
群組裡有人分享了新的餐廳名單。
```

Acceptable variants:

```text
(none)
```

Rationale:

「群组」轉「群組」。

### blind-social-0005

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
你把照片传给我，我晚点再整理相册。
```

Codex expected:

```text
你把照片傳給我，我晚點再整理相簿。
```

Acceptable variants:

```text
(none)
```

Rationale:

「相册」轉台灣常用「相簿」。

### blind-social-0006

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
这件外套颜色很好看，不过尺寸好像偏小。
```

Codex expected:

```text
這件外套顏色很好看，不過尺寸好像偏小。
```

Acceptable variants:

```text
(none)
```

Rationale:

日常語氣直轉。

### blind-social-0007

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `regional_term`

Input:

```text
我刚刚在便利店看到同款充电线。
```

Codex expected:

```text
我剛剛在便利商店看到同款充電線。
```

Acceptable variants:

```text
我剛剛在超商看到同款充電線。
```

Rationale:

「便利店」在台灣可轉「便利商店」，口語也常用「超商」。

### blind-social-0008

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
明天早上记得带雨伞，天气预报说会下雨。
```

Codex expected:

```text
明天早上記得帶雨傘，天氣預報說會下雨。
```

Acceptable variants:

```text
(none)
```

Rationale:

「天气预报」轉「天氣預報」。

### blind-social-0009

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `regional_term`

Input:

```text
这首歌的副歌很洗脑，大家都在哼。
```

Codex expected:

```text
這首歌的副歌很洗腦，大家都在哼。
```

Acceptable variants:

```text
(none)
```

Rationale:

「洗腦」可保留，符合台灣口語。

### blind-social-0010

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term, it_term`

Input:

```text
他把会议链接贴在留言区了。
```

Codex expected:

```text
他把會議連結貼在留言區了。
```

Acceptable variants:

```text
(none)
```

Rationale:

「链接」轉「連結」。

### blind-social-0011

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `regional_term`

Input:

```text
我们先在捷运站出口集合。
```

Codex expected:

```text
我們先在捷運站出口集合。
```

Acceptable variants:

```text
(none)
```

Rationale:

「捷運站」為台灣交通用語。

### blind-social-0012

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
晚餐想吃面还是便当？
```

Codex expected:

```text
晚餐想吃麵還是便當？
```

Acceptable variants:

```text
(none)
```

Rationale:

「面」轉「麵」。

### blind-social-0013

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
这家店排队人很多，可能要等半小时。
```

Codex expected:

```text
這家店排隊人很多，可能要等半小時。
```

Acceptable variants:

```text
(none)
```

Rationale:

日常語氣直轉。

### blind-social-0014

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `baseline_guard`
- Confidence: `high`
- Review needed: `false`
- Issue tags: `regional_term`

Input:

```text
我把票放在钱包里，别让我忘记拿。
```

Codex expected:

```text
我把票放在錢包裡，別讓我忘記拿。
```

Acceptable variants:

```text
(none)
```

Rationale:

「钱包」轉「錢包」。

### blind-social-0015

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `candidate_gap`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `regional_term, ui_term`

Input:

```text
今天的直播回放什么时候会上架？
```

Codex expected:

```text
今天的直播重播什麼時候會上架？
```

Acceptable variants:

```text
今天的直播回放什麼時候會上架？
```

Rationale:

「直播回放」在台灣較常改為「直播重播」，但產品用語可能保留「回放」。

### blind-high-risk-0001

- Batch: `blind-high-risk`
- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term, formal_term`

Input:

```text
不得以定型化契约条款排除责任。
```

Codex expected:

```text
不得以定型化契約條款排除責任。
```

Acceptable variants:

```text
(none)
```

Rationale:

法律語境使用「定型化契約條款」。

### blind-high-risk-0002

- Batch: `blind-high-risk`
- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term, formal_term`

Input:

```text
跨行汇款手续费由使用者负担。
```

Codex expected:

```text
跨行匯款手續費由使用者負擔。
```

Acceptable variants:

```text
(none)
```

Rationale:

金融語境「跨行匯款」「手續費」直轉。

### blind-high-risk-0003

- Batch: `blind-high-risk`
- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term`

Input:

```text
请依医师指示服用本药，并留意过敏反应。
```

Codex expected:

```text
請依醫師指示服用本藥，並留意過敏反應。
```

Acceptable variants:

```text
(none)
```

Rationale:

醫療用語使用「醫師」「過敏反應」。

### blind-high-risk-0004

- Batch: `blind-high-risk`
- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term`

Input:

```text
投保前应详阅保单条款和除外责任。
```

Codex expected:

```text
投保前應詳閱保單條款和除外責任。
```

Acceptable variants:

```text
(none)
```

Rationale:

保險正式用語「保單條款」「除外責任」。

### blind-high-risk-0005

- Batch: `blind-high-risk`
- Domain: `high_risk`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term, formal_term`

Input:

```text
申请补助时，必须提供有效的身分证明文件。
```

Codex expected:

```text
申請補助時，必須提供有效的身分證明文件。
```

Acceptable variants:

```text
(none)
```

Rationale:

台灣正式文件用「身分證明文件」。

### blind-high-risk-0006

- Batch: `blind-high-risk`
- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term`

Input:

```text
病人出现胸痛或呼吸困难时，应立即就医。
```

Codex expected:

```text
病人出現胸痛或呼吸困難時，應立即就醫。
```

Acceptable variants:

```text
(none)
```

Rationale:

醫療安全語境直轉。

### blind-high-risk-0007

- Batch: `blind-high-risk`
- Domain: `high_risk`
- Risk: `candidate_gap`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term`

Input:

```text
贷款利率可能随市场条件调整。
```

Codex expected:

```text
貸款利率可能隨市場條件調整。
```

Acceptable variants:

```text
(none)
```

Rationale:

金融語境直轉。

### blind-high-risk-0008

- Batch: `blind-high-risk`
- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term, formal_term`

Input:

```text
个人资料不得用于原申请目的以外的用途。
```

Codex expected:

```text
個人資料不得用於原申請目的以外的用途。
```

Acceptable variants:

```text
(none)
```

Rationale:

個資法語境用「個人資料」。

### blind-high-risk-0009

- Batch: `blind-high-risk`
- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Confidence: `medium`
- Review needed: `true`
- Issue tags: `high_risk_term, formal_term`

Input:

```text
本合约争议适用中华民国法律。
```

Codex expected:

```text
本合約爭議適用中華民國法律。
```

Acceptable variants:

```text
本契約爭議適用中華民國法律。
```

Rationale:

「合約」與「契約」都常見；正式法務文件可能需依上下文決定。

### blind-high-risk-0010

- Batch: `blind-high-risk`
- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Confidence: `high`
- Review needed: `true`
- Issue tags: `high_risk_term`

Input:

```text
医疗纪录应依法保存，不得任意删除。
```

Codex expected:

```text
醫療紀錄應依法保存，不得任意刪除。
```

Acceptable variants:

```text
(none)
```

Rationale:

醫療語境使用「醫療紀錄」。
