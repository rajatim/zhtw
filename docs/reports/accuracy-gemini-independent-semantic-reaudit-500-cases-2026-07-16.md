# Gemini Independent Semantic Re-audit（2026-07-16）

Gemini CLI `gemini-2.5-pro` 獨立審查 annotation backlog 目前 500 筆
input/expected，只標記明確語意錯誤、實體／角色混淆、技術名詞直譯錯誤或臺灣幾乎
不用的詞。未提供 Codex findings，tool calls 為 0。

## 結果

- Reviewed：500
- Flagged：10
- 現行 expected 已符合 Gemini 建議：10
- 新增 ground-truth correction：0

Flagged IDs：`it-api-cli-0121`、`ui-i18n-0091`、
`formal-high-risk-0040`、`formal-high-risk-0085`、`social-daily-0001`、
`social-daily-0002`、`social-daily-0009`、`social-daily-0013`、
`social-daily-0033`、`mixed-ambiguity-0001`。

本報告只記錄當前 re-audit 結果；三筆先前發現並已修正的案例另見
`accuracy-ground-truth-corrections-2026-07-16.md`。
