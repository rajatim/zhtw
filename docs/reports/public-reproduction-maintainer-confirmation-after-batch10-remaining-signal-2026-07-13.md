# Public Reproduction Maintainer Confirmation After Batch10 Remaining Signal

- Generated date: `2026-07-13`
- Dataset: `public-reproduction-seeds-v1`
- Source diff report: `docs/reports/public-reproduction-codex-gemini-diff-after-batch10-remaining-signal-2026-07-13.json`
- Ground truth: `false`
- Promotion allowed: `false`

Review summary:

| Metric | Count |
| --- | ---: |
| Review cases | 17 |
| No immediate question cases | 15 |
| Primary differences | 6 |
| High-risk review cases | 8 |

Maintainer review cases:

## public-repro-20260713-formal-0002

- Domain/risk: `formal` / `over_conversion_guard`
- Input: 请将会议记录归档，并通知各部门负责人确认版本。
- Codex: 請將會議紀錄歸檔，並通知各部門負責人確認版本。
- Gemini: 請將會議記錄歸檔，並通知各部門負責人確認版本。
- Recommendation: `codex`
- Recommended expected: 請將會議紀錄歸檔，並通知各部門負責人確認版本。
- Recommended acceptable: []
- Reason: 會議紀錄作正式文件名詞較符合台灣用法。

## public-repro-20260713-formal-0004

- Domain/risk: `formal` / `over_conversion_guard`
- Input: 采购公告应列明交货地点、验收标准与联系窗口。
- Codex: 採購公告應列明交貨地點、驗收標準與聯絡窗口。
- Gemini: 採購公告應列明交貨地點、驗收標準與聯絡窗口。
- Recommendation: `shared_expected`
- Recommended expected: 採購公告應列明交貨地點、驗收標準與聯絡窗口。
- Recommended acceptable: []
- Reason: Codex and Gemini primary expected match.

## public-repro-20260713-high-risk-0001

- Domain/risk: `high_risk` / `over_conversion_guard`
- Input: 医师评估后建议病人持续监测血压并记录用药时间。
- Codex: 醫師評估後建議病人持續監測血壓並記錄用藥時間。
- Gemini: 醫師評估後建議病人持續監測血壓並記錄用藥時間。
- Recommendation: `shared_expected`
- Recommended expected: 醫師評估後建議病人持續監測血壓並記錄用藥時間。
- Recommended acceptable: []
- Reason: Codex and Gemini primary expected match.

## public-repro-20260713-high-risk-0002

- Domain/risk: `high_risk` / `over_conversion_guard`
- Input: 药袋上应标示每日剂量、服用方式与注意事项。
- Codex: 藥袋上應標示每日劑量、服用方式與注意事項。
- Gemini: 藥袋上應標示每日劑量、服用方式與注意事項。
- Recommendation: `shared_expected`
- Recommended expected: 藥袋上應標示每日劑量、服用方式與注意事項。
- Recommended acceptable: []
- Reason: Codex and Gemini primary expected match.

## public-repro-20260713-high-risk-0003

- Domain/risk: `high_risk` / `candidate_gap`
- Input: 保险理赔文件需要附上诊断证明与收据正本。
- Codex: 保險理賠文件需要附上診斷證明與收據正本。
- Gemini: 保險理賠文件需要附上診斷證明與收據正本。
- Recommendation: `shared_expected`
- Recommended expected: 保險理賠文件需要附上診斷證明與收據正本。
- Recommended acceptable: []
- Reason: Codex and Gemini primary expected match.

## public-repro-20260713-high-risk-0004

- Domain/risk: `high_risk` / `candidate_gap`
- Input: 银行审核大额转账时，会要求客户补充资金来源说明。
- Codex: 銀行審核大額轉帳時，會要求客戶補充資金來源說明。
- Gemini: 銀行審核大額轉帳時，會要求客戶補充資金來源說明。
- Recommendation: `shared_expected`
- Recommended expected: 銀行審核大額轉帳時，會要求客戶補充資金來源說明。
- Recommended acceptable: []
- Reason: Codex and Gemini primary expected match.

## public-repro-20260713-high-risk-0005

- Domain/risk: `high_risk` / `over_conversion_guard`
- Input: 法院通知当事人携带身份证明文件出庭说明。
- Codex: 法院通知當事人攜帶身分證明文件出庭說明。
- Gemini: 法院通知當事人攜帶身分證明文件出庭說明。
- Recommendation: `shared_expected`
- Recommended expected: 法院通知當事人攜帶身分證明文件出庭說明。
- Recommended acceptable: ['法院通知當事人攜帶身份證明文件出庭說明。']
- Reason: Codex and Gemini primary expected match.

## public-repro-20260713-high-risk-0006

- Domain/risk: `high_risk` / `over_conversion_guard`
- Input: 税务资料若有遗漏，应在期限内补正并保存凭证。
- Codex: 稅務資料若有遺漏，應在期限內補正並保存憑證。
- Gemini: 稅務資料若有遺漏，應在期限內補正並保存憑證。
- Recommendation: `shared_expected`
- Recommended expected: 稅務資料若有遺漏，應在期限內補正並保存憑證。
- Recommended acceptable: []
- Reason: Codex and Gemini primary expected match.

## public-repro-20260713-high-risk-0007

- Domain/risk: `high_risk` / `over_conversion_guard`
- Input: 工地主管应确认安全帽、护目镜与警示标志齐备。
- Codex: 工地主管應確認安全帽、護目鏡與警示標誌齊備。
- Gemini: 工地主管應確認安全帽、護目鏡與警示標誌齊備。
- Recommendation: `shared_expected`
- Recommended expected: 工地主管應確認安全帽、護目鏡與警示標誌齊備。
- Recommended acceptable: []
- Reason: Codex and Gemini primary expected match.

## public-repro-20260713-high-risk-0008

- Domain/risk: `high_risk` / `baseline_guard`
- Input: 个人资料同意书应说明使用目的、保存期间与撤回方式。
- Codex: 個人資料同意書應說明使用目的、保存期間與撤回方式。
- Gemini: 個人資料同意書應說明使用目的、保存期間與撤回方式。
- Recommendation: `shared_expected`
- Recommended expected: 個人資料同意書應說明使用目的、保存期間與撤回方式。
- Recommended acceptable: []
- Reason: Codex and Gemini primary expected match.

## public-repro-20260713-it-0001

- Domain/risk: `it` / `over_conversion_guard`
- Input: API 回应包含分页资讯、错误代码与请求识别码。
- Codex: API 回應包含分頁資訊、錯誤代碼與請求識別碼。
- Gemini: API 回應包含分頁資訊、錯誤代碼與請求識別碼。
- Recommendation: `shared_expected`
- Recommended expected: API 回應包含分頁資訊、錯誤代碼與請求識別碼。
- Recommended acceptable: ['API 回應包含分頁資訊、錯誤碼與請求 ID。']
- Reason: Codex and Gemini primary expected match.

## public-repro-20260713-llm-0001

- Domain/risk: `llm` / `over_conversion_guard`
- Input: 提示模板会插入使用者问题、系统规则与输出格式。
- Codex: 提示範本會插入使用者問題、系統規則與輸出格式。
- Gemini: 提示模板會插入使用者問題、系統規則與輸出格式。
- Recommendation: `codex`
- Recommended expected: 提示範本會插入使用者問題、系統規則與輸出格式。
- Recommended acceptable: []
- Reason: 提示範本比提示模板更符合本專案既有台灣用語傾向。

## public-repro-20260713-llm-0002

- Domain/risk: `llm` / `over_conversion_guard`
- Input: 模型回覆前会先读取上下文、工具结果与安全规则。
- Codex: 模型回覆前會先讀取上下文、工具結果與安全規則。
- Gemini: 模型回覆前會先讀取上下文、工具結果與安全規則。
- Recommendation: `shared_expected`
- Recommended expected: 模型回覆前會先讀取上下文、工具結果與安全規則。
- Recommended acceptable: ['模型回覆前會先讀取脈絡、工具結果與安全規則。']
- Reason: Codex and Gemini primary expected match.

## public-repro-20260713-social-0003

- Domain/risk: `social` / `over_conversion_guard`
- Input: 短影片下方的评论很快增加，创作者决定关闭通知。
- Codex: 短影片下方的留言很快增加，創作者決定關閉通知。
- Gemini: 短影片下方的評論很快增加，創作者決定關閉通知。
- Recommendation: `codex_with_gemini_acceptable`
- Recommended expected: 短影片下方的留言很快增加，創作者決定關閉通知。
- Recommended acceptable: ['短影片下方的評論很快增加，創作者決定關閉通知。', '短影音下方的留言很快增加，創作者決定關閉通知。']
- Reason: 短影片社群語境建議以留言為 primary，評論可作 acceptable variant。

## public-repro-20260713-ui-0002

- Domain/risk: `ui` / `over_conversion_guard`
- Input: 下拉选单展开时，当前选项会以蓝色边框标示。
- Codex: 下拉選單展開時，目前選項會以藍色邊框標示。
- Gemini: 下拉式選單展開時，目前選項會以藍色邊框標示。
- Recommendation: `gemini_with_codex_acceptable`
- Recommended expected: 下拉式選單展開時，目前選項會以藍色邊框標示。
- Recommended acceptable: ['下拉選單展開時，當前選項會以藍色邊框標示。', '下拉選單展開時，目前選項會以藍色邊框標示。']
- Reason: 下拉式選單是台灣 UI 文件常見 primary，下拉選單可作 acceptable variant。

## public-repro-20260713-ui-0004

- Domain/risk: `ui` / `over_conversion_guard`
- Input: 确认对话框关闭后，焦点应回到原本的输入框。
- Codex: 確認對話框關閉後，焦點應回到原本的輸入框。
- Gemini: 確認對話方塊關閉後，焦點應回到原本的輸入框。
- Recommendation: `codex_with_gemini_acceptable`
- Recommended expected: 確認對話框關閉後，焦點應回到原本的輸入框。
- Recommended acceptable: ['確認對話方塊關閉後，焦點應回到原本的輸入框。']
- Reason: Web/UI 語境建議以對話框為 primary，對話方塊可作 acceptable variant。

## public-repro-20260713-ui-0005

- Domain/risk: `ui` / `over_conversion_guard`
- Input: 侧边栏筛选条件重置后，表格资料应立即重新整理。
- Codex: 側邊欄篩選條件重設後，表格資料應立即重新整理。
- Gemini: 側邊欄篩選條件重置後，表格資料應立即重新整理。
- Recommendation: `codex_with_gemini_acceptable`
- Recommended expected: 側邊欄篩選條件重設後，表格資料應立即重新整理。
- Recommended acceptable: ['側邊欄篩選條件重置後，表格資料應立即重新整理。']
- Reason: 台灣 UI 動作文字建議以重設為 primary，重置可作 acceptable variant。
