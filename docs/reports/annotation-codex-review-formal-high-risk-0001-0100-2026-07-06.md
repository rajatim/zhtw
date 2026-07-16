<!-- zhtw:disable -->
# Codex Review：formal-high-risk 0001-0100（2026-07-06）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`
Codex draft：`docs/reports/annotation-first-pass-ai-draft-formal-high-risk-0001-0100-2026-07-06.md`
Gemini advisory：

- `docs/reports/annotation-gemini-vertex-advisory-formal-high-risk-0001-0050-2026-07-06.md`
- `docs/reports/annotation-gemini-vertex-advisory-formal-high-risk-0051-0100-2026-07-06.md`

## Boundary

- This is Codex advisory review only, not maintainer approval.
- Do not copy recommendations into `review.expected` without maintainer final review.
- Gemini remains an AI advisory, not a human `blind_reviewer`.

## Summary

- Cases reviewed: 100
- Codex/Gemini exact matches: 91
- Codex/Gemini differences: 9
- Recommendation on differences: Codex 5, Gemini 4
- Maintainer final decision on differences: Codex 2, Gemini 7
- Current backlog status: `approved`

## Maintainer Final Decision

Maintainer `tim` reviewed the 9 differing cases on 2026-07-07:

- Codex accepted: `formal-high-risk-0040`, `formal-high-risk-0043`
- Gemini accepted: `formal-high-risk-0002`, `formal-high-risk-0008`,
  `formal-high-risk-0019`, `formal-high-risk-0035`,
  `formal-high-risk-0038`, `formal-high-risk-0051`,
  `formal-high-risk-0098`

The 91 exact-match cases use the shared Codex/Gemini expected output as
`human_first_pass`. The 9 differing cases are recorded as
`human_adjudication`.

## Difference Recommendations

| ID | Input | Codex draft | Gemini advisory | Recommendation | Reason |
|----|-------|-------------|-----------------|----------------|--------|
| formal-high-risk-0002 | 气象局发出海上台风警报。 | 氣象局發出海上颱風警報。 | 氣象局發布海上颱風警報。 | Codex | 原文是「发出」，不是「发布」；高風險 formal case 應避免把動作改成另一個動詞。 |
| formal-high-risk-0008 | 会议纪要将上传至机关网站。 | 會議紀要將上傳至機關網站。 | 會議紀錄將上傳至機關網站。 | Gemini | 台灣正式會議文件常用「會議紀錄」；此處比逐字「會議紀要」更像台灣用語。 |
| formal-high-risk-0019 | 隐私声明已更新。 | 隱私聲明已更新。 | 隱私權聲明已更新。 | Gemini | 台灣網站與正式文件常見「隱私權聲明」，比「隱私聲明」更自然。 |
| formal-high-risk-0035 | 罚款应于期限内缴清。 | 罰鍰應於期限內繳清。 | 罰款應於期限內繳清。 | Codex | 行政處分/期限內繳清語境下，台灣法政用語通常是「罰鍰」。 |
| formal-high-risk-0038 | 营业执照副本需附印章。 | 營業執照副本需附印章。 | 營業執照影本需附印章。 | Gemini | 「副本需附印章」在送件文件語境可理解為影本；「影本」較符合台灣申辦文件用語。 |
| formal-high-risk-0040 | 不得以格式条款排除责任。 | 不得以定型化契約條款排除責任。 | 不得以格式條款排除責任。 | Codex | 台灣消保與契約語境常用「定型化契約條款」，比「格式條款」更在地。 |
| formal-high-risk-0043 | 跨行汇款手续费由用户承担。 | 跨行匯款手續費由使用者負擔。 | 跨行匯款手續費由使用者承擔。 | Codex | 費用語境中「手續費由使用者負擔」比「承擔」更自然且常見。 |
| formal-high-risk-0051 | 请勿泄露信用卡安全码。 | 請勿洩露信用卡安全碼。 | 請勿洩漏信用卡安全碼。 | Gemini | 信用卡安全碼屬資訊外流語境，「洩漏」比「洩露」更常見。 |
| formal-high-risk-0098 | 项目经费不得挪用于私人用途。 | 計畫經費不得挪用於私人用途。 | 專案經費不得挪用於私人用途。 | Codex | 公共/補助經費語境中「計畫經費」比「專案經費」更像政府正式用語。 |

## Maintainer Apply Rules

- If accepting an exact-match case, copy the shared expected value to `review.expected`, set `review.expected_source = "human_first_pass"`, `review.first_reviewer = "tim"`, and record Gemini advisory as accepted.
- If accepting a differing Codex recommendation, set `review.expected_source = "human_adjudication"`, `review.adjudicator = "tim"`, `review.disagreement = true`, and record Gemini advisory as rejected.
- If accepting a differing Gemini recommendation, set `review.expected_source = "human_adjudication"`, `review.adjudicator = "tim"`, `review.disagreement = true`, and record Gemini advisory as accepted with `exact_match_with_first_pass = false`.
