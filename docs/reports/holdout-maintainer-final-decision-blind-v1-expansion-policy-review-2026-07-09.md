<!-- zhtw:disable -->
# Holdout Maintainer Final Decision Summary - blind-v1 Expansion Policy Review

Dataset: `blind-v1`
Scope: `expansion_policy_review_only`
Maintainer: `tim`
Source confirmation packet: `docs/reports/holdout-maintainer-confirmation-blind-v1-expansion-policy-review-2026-07-09.json`
Source diff review: `docs/reports/holdout-codex-gemini-diff-review-blind-v1-expansion-127-cases-2026-07-09.json`
Private expected path: `benchmarks/accuracy/blind-v1.expected.json`

## Boundary

- This report records maintainer decision metadata only.
- It intentionally does not include expected values.
- It covers only the 33 Codex/Gemini exact-match policy-review cases from the 127-case expansion.
- The full 127-case expansion decision summary records the private expected rebuild.

## Summary

- Confirmed cases: 33
- Accepted recommended expected: 33
- Edited cases: 0
- Dropped cases: 0
- No immediate-question cases: 46
- Private expected updated in this summary: `false`

Recommendation source:

- `codex_gemini_match`: 33

Domain:

- `formal`: 4
- `high_risk`: 8
- `it`: 3
- `llm`: 4
- `social`: 5
- `ui`: 9

Risk:

- `baseline_guard`: 3
- `candidate_gap`: 14
- `over_conversion_guard`: 16

Policy reason:

- `Codex confidence medium`: 11
- `high-risk domain`: 4
- `high-risk domain, Codex confidence medium`: 2
- `high-risk domain, over-conversion guard`: 2
- `over-conversion guard`: 14

Confirmed case ids:

- `blind-it-0040`
- `blind-it-0053`
- `blind-it-0062`
- `blind-ui-0021`
- `blind-ui-0025`
- `blind-ui-0028`
- `blind-ui-0035`
- `blind-ui-0038`
- `blind-ui-0041`
- `blind-ui-0042`
- `blind-ui-0043`
- `blind-ui-0044`
- `blind-llm-0019`
- `blind-llm-0023`
- `blind-llm-0027`
- `blind-llm-0030`
- `blind-formal-0023`
- `blind-formal-0026`
- `blind-formal-0028`
- `blind-formal-0030`
- `blind-social-0019`
- `blind-social-0027`
- `blind-social-0028`
- `blind-social-0030`
- `blind-social-0031`
- `blind-high-risk-0011`
- `blind-high-risk-0013`
- `blind-high-risk-0014`
- `blind-high-risk-0015`
- `blind-high-risk-0017`
- `blind-high-risk-0018`
- `blind-high-risk-0019`
- `blind-high-risk-0020`
