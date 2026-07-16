# Public Reproduction Codex/Gemini Diff After Batch10 Remaining Signal

- Generated date: `2026-07-13`
- Dataset: `public-reproduction-seeds-v1`
- Codex first pass: `docs/reports/public-reproduction-codex-first-pass-after-batch10-remaining-signal-2026-07-13.json`
- Gemini advisory: `docs/reports/public-reproduction-gemini-advisory-after-batch10-remaining-signal-2026-07-13.json`
- Ground truth: `false`
- Promotion allowed: `false`

Summary:

| Metric | Count |
| --- | ---: |
| Total cases | 32 |
| Primary exact matches | 26 |
| Primary differences | 6 |
| Review-needed | 17 |
| No immediate question | 15 |

Primary differences:

- `public-repro-20260713-formal-0002` (formal): recommended `codex`.
  - Codex: 請將會議紀錄歸檔，並通知各部門負責人確認版本。
  - Gemini: 請將會議記錄歸檔，並通知各部門負責人確認版本。
  - Reason: 會議紀錄作正式文件名詞較符合台灣用法。
- `public-repro-20260713-llm-0001` (llm): recommended `codex`.
  - Codex: 提示範本會插入使用者問題、系統規則與輸出格式。
  - Gemini: 提示模板會插入使用者問題、系統規則與輸出格式。
  - Reason: 提示範本比提示模板更符合本專案既有台灣用語傾向。
- `public-repro-20260713-social-0003` (social): recommended `codex_with_gemini_acceptable`.
  - Codex: 短影片下方的留言很快增加，創作者決定關閉通知。
  - Gemini: 短影片下方的評論很快增加，創作者決定關閉通知。
  - Reason: 短影片社群語境建議以留言為 primary，評論可作 acceptable variant。
- `public-repro-20260713-ui-0002` (ui): recommended `gemini_with_codex_acceptable`.
  - Codex: 下拉選單展開時，目前選項會以藍色邊框標示。
  - Gemini: 下拉式選單展開時，目前選項會以藍色邊框標示。
  - Reason: 下拉式選單是台灣 UI 文件常見 primary，下拉選單可作 acceptable variant。
- `public-repro-20260713-ui-0004` (ui): recommended `codex_with_gemini_acceptable`.
  - Codex: 確認對話框關閉後，焦點應回到原本的輸入框。
  - Gemini: 確認對話方塊關閉後，焦點應回到原本的輸入框。
  - Reason: Web/UI 語境建議以對話框為 primary，對話方塊可作 acceptable variant。
- `public-repro-20260713-ui-0005` (ui): recommended `codex_with_gemini_acceptable`.
  - Codex: 側邊欄篩選條件重設後，表格資料應立即重新整理。
  - Gemini: 側邊欄篩選條件重置後，表格資料應立即重新整理。
  - Reason: 台灣 UI 動作文字建議以重設為 primary，重置可作 acceptable variant。
