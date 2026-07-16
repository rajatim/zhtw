<!-- zhtw:disable -->
# Codex Review：ui-i18n 0101-0125（2026-07-06）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`

## Boundary

- This is Codex review of Codex-vs-Gemini advisory differences only.
- It is not maintainer final review.
- Do not promote these recommendations directly.
- Maintainer must choose the final expected value before `review.expected` is populated.

## Summary

- Cases reviewed: 25
- Codex/Gemini exact matches: 18
- Differences needing maintainer decision: 7
- Codex recommendation: 6
- Gemini recommendation: 1

## Maintainer Decision

Maintainer `tim` accepted this Codex review recommendation on 2026-07-06.
The backlog was updated as follows:

- 18 exact-match cases use the shared Codex/Gemini expected output with
  `expected_source = "human_first_pass"`.
- 1 differing case uses the Gemini advisory expected output with
  `expected_source = "human_adjudication"` and `adjudicator = "tim"`.
- 6 differing cases use the Codex expected output with
  `expected_source = "human_adjudication"`, `adjudicator = "tim"`, and Gemini
  advisory recorded as `decision = "rejected"`.
- All 25 cases are now `approved`, promotion-ready, and promoted into
  `regression-v1.json`.

## Recommended Decisions

| ID | Input | Codex | Gemini | Codex recommendation | Reason |
|----|-------|-------|--------|----------------------|--------|
| ui-i18n-0101 | 语言包下载完成。 | 語言套件下載完成。 | 語言包下載完成。 | Codex | 台灣軟體語境中 package 較常用 `套件`。 |
| ui-i18n-0105 | 数字分组符号可以自定义。 | 數字分組符號可以自訂。 | 數字分位符號可自訂。 | Codex | Source 是 grouping separator，保留 `分組符號` 較直準。 |
| ui-i18n-0107 | 翻译缺失时会回退到默认语言。 | 翻譯缺漏時會改用預設語言。 | 翻譯遺失時會回復為預設語言。 | Codex | i18n fallback 用 `改用預設語言` 較自然，`遺失` 較像檔案遺失。 |
| ui-i18n-0108 | 字符串键不能重复。 | 字串鍵不能重複。 | 字串鍵不可重複。 | Gemini | UI 驗證錯誤訊息中 `不可重複` 較簡潔自然。 |
| ui-i18n-0109 | 请为每个语言添加说明。 | 請為每種語言新增說明。 | 請為每個語言新增說明。 | Codex | `語言` 的量詞用 `種` 較自然。 |
| ui-i18n-0110 | 导入翻译文件前请预览差异。 | 匯入翻譯檔前請預覽差異。 | 匯入翻譯檔案前請預覽差異。 | Codex | UI 文案中 `翻譯檔` 精簡且自然。 |
| ui-i18n-0125 | 请在发布前锁定语言版本。 | 請在發佈前鎖定語言版本。 | 請在發布前鎖定語言版本。 | Codex | 軟體 release 語境沿用專案已核准的 `發佈`。 |
