<!-- zhtw:disable -->
# Holdout Maintainer Final Decision - Batch10

Generated: `2026-07-12`

## Summary

- Dataset: `blind-v1`
- Scope: `batch10_100_cases`
- Expected values included: `false`
- Private expected updated: `true`
- Private expected sha256: `b8150c2e41e2bc574de54a730fe1a0c1c1edf39a9efce344ef1bbbd267179250`
- Source inputs sha256: `eff19da4ff198981bdb0018bceabb128b1aa5a33e9199ea5421f69561da340d0`
- Batch10 cases: 100
- Review packet cases accepted: 44
- No-immediate-question cases accepted: 56
- Edited cases: 0
- Dropped cases: 0

## Policy

- Approval policy: `single_human_with_ai_advisory`
- Minimum human reviewers: 1
- AI advisory reviewers: `codex`, `gemini_cli`
- This public summary does not include expected values, acceptable variants, inputs, or converter outputs.

## Source Reports

- `docs/reports/holdout-codex-first-pass-blind-v1-batch10-100-cases-2026-07-12.json`
- `docs/reports/holdout-gemini-cli-advisory-blind-v1-batch10-100-cases-2026-07-12.json`
- `docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch10-100-cases-2026-07-12.json`
- `docs/reports/holdout-maintainer-confirmation-blind-v1-batch10-100-cases-2026-07-12.json`

## Counts

- `by_expected_source_for_batch10`: `{"human_adjudication": 17, "human_first_pass": 83}`
- `by_disagreement_for_batch10`: `{"false": 83, "true": 17}`
- `by_expected_source_total`: `{"human_adjudication": 151, "human_first_pass": 616}`
- `by_disagreement_total`: `{"false": 616, "true": 151}`
- `by_domain_for_batch10`: `{"formal": 15, "high_risk": 10, "it": 25, "llm": 15, "social": 15, "ui": 20}`
- `by_risk_for_batch10`: `{"baseline_guard": 15, "candidate_gap": 60, "over_conversion_guard": 25}`
