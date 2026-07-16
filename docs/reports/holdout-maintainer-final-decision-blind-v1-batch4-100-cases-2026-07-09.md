<!-- zhtw:disable -->
# Holdout Maintainer Final Decision Summary - blind-v1 Batch4 100 Cases

Dataset: `blind-v1`
Scope: `batch4_100_cases`
Maintainer: `tim`
Private expected path: `benchmarks/accuracy/blind-v1.expected.json`
Private expected sha256: `1f82eed5f2cf530f5e1e55d326cb09384fff1942f0084764833b0ca54fc5c828`

## Boundary

- This report records aggregate maintainer decision metadata only.
- It intentionally does not include expected values.
- The private expected file was rebuilt to align with all 261 current input cases.

## Summary

- Batch4 cases: 100
- Total private expected cases: 261
- Private expected updated: `true`
- Approval policy: `single_human_with_ai_advisory`
- Accepted recommendation-confirmed cases: 64
- Accepted exact no-immediate-question cases: 36
- Edited cases: 0
- Dropped cases: 0

Expected source for batch4:

- `human_adjudication`: 26
- `human_first_pass`: 74

Disagreement for batch4:

- `false`: 74
- `true`: 26

Expected source total:

- `human_adjudication`: 68
- `human_first_pass`: 193

Domain for batch4:

- `formal`: 15
- `high_risk`: 10
- `it`: 25
- `llm`: 15
- `social`: 15
- `ui`: 20

Risk for batch4:

- `baseline_guard`: 15
- `candidate_gap`: 60
- `over_conversion_guard`: 25

Source reports:

- `docs/reports/holdout-codex-first-pass-blind-v1-batch4-100-cases-2026-07-09.json`
- `docs/reports/holdout-gemini-vertex-advisory-blind-v1-batch4-100-cases-2026-07-09.json`
- `docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch4-100-cases-2026-07-09.json`
- `docs/reports/holdout-maintainer-confirmation-blind-v1-batch4-100-cases-2026-07-09.json`
