<!-- zhtw:disable -->
# Holdout Maintainer Final Decision Summary - blind-v1 Expansion Differences

Dataset: `blind-v1`
Scope: `expansion_differences_only`
Maintainer: `tim`
Source confirmation packet: `docs/reports/holdout-maintainer-confirmation-blind-v1-expansion-differences-2026-07-09.json`
Source diff review: `docs/reports/holdout-codex-gemini-diff-review-blind-v1-expansion-127-cases-2026-07-09.json`
Private expected path: `benchmarks/accuracy/blind-v1.expected.json`

## Boundary

- This report records maintainer decision metadata only.
- It intentionally does not include expected values.
- It covers only the 48 Codex/Gemini difference cases from the 127-case expansion.
- `blind-v1.expected.json` was not updated in this step because the current input file has 200 cases and the benchmark runner requires full expected/input alignment.
- The 33 exact-match policy-review cases are still deferred.

## Summary

- Confirmed cases: 48
- Accepted recommended expected: 48
- Edited cases: 0
- Dropped cases: 0
- Deferred policy-review cases: 33
- No immediate-question cases: 46
- Private expected updated: `false`

Recommendation source:

- `codex`: 39
- `gemini`: 7
- `third_value`: 2

Domain:

- `formal`: 2
- `high_risk`: 2
- `it`: 27
- `llm`: 8
- `social`: 5
- `ui`: 4

Risk:

- `baseline_guard`: 2
- `candidate_gap`: 31
- `over_conversion_guard`: 15

Confirmed case ids:

- `blind-it-0026`
- `blind-it-0027`
- `blind-it-0028`
- `blind-it-0029`
- `blind-it-0032`
- `blind-it-0033`
- `blind-it-0034`
- `blind-it-0035`
- `blind-it-0036`
- `blind-it-0037`
- `blind-it-0041`
- `blind-it-0042`
- `blind-it-0043`
- `blind-it-0044`
- `blind-it-0045`
- `blind-it-0046`
- `blind-it-0047`
- `blind-it-0048`
- `blind-it-0050`
- `blind-it-0051`
- `blind-it-0052`
- `blind-it-0054`
- `blind-it-0055`
- `blind-it-0056`
- `blind-it-0057`
- `blind-it-0058`
- `blind-it-0059`
- `blind-ui-0030`
- `blind-ui-0034`
- `blind-ui-0039`
- `blind-ui-0040`
- `blind-llm-0016`
- `blind-llm-0017`
- `blind-llm-0021`
- `blind-llm-0022`
- `blind-llm-0024`
- `blind-llm-0026`
- `blind-llm-0028`
- `blind-llm-0029`
- `blind-formal-0027`
- `blind-formal-0029`
- `blind-social-0016`
- `blind-social-0024`
- `blind-social-0025`
- `blind-social-0026`
- `blind-social-0029`
- `blind-high-risk-0012`
- `blind-high-risk-0016`
