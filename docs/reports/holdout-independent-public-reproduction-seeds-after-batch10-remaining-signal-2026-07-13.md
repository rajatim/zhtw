# Independent Public Reproduction Seeds After Batch10 Remaining Signal

- Generated date: `2026-07-13`
- Dataset: `benchmarks/accuracy/public-reproduction-seeds-v1.json`
- Source signal report: `docs/reports/holdout-remaining-signal-summary-blind-v1-after-batch10-miss-review-2026-07-13.json`
- Gemini policy review: `docs/reports/holdout-gemini-policy-review-remaining-signal-blind-v1-after-batch10-miss-review-2026-07-13.json`
- Status: `input_only_needs_review`

This seed set is the first public reproduction layer for the 32 remaining
private holdout signals after batch10 miss review. It is intentionally input
only: no expected values, acceptable variants, zhtw outputs, or benchmark rows
are included.

The cases were written as new public project-original sentences from sanitized
metadata themes only: domain, risk, issue tags, signal category, and idempotency
metadata. Sealed holdout text was not used, copied, paraphrased, or inspected
while creating these public inputs.

Distribution:

| Domain | Cases |
| --- | ---: |
| formal | 6 |
| high_risk | 8 |
| it | 3 |
| llm | 4 |
| social | 6 |
| ui | 5 |

Risk distribution:

| Risk | Cases |
| --- | ---: |
| baseline_guard | 1 |
| candidate_gap | 2 |
| over_conversion_guard | 29 |

Policy:

- Do not tune converter or dictionary from this input-only dataset yet.
- Run Codex first-pass expected recommendations next.
- Run Gemini independent advisory after Codex first pass.
- Maintainer confirmation is required before any expected value becomes ground
  truth.
- Only after human expected review may selected public cases become regression
  tests or tuning inputs.

Current next step: create Codex first-pass expected recommendations for these
32 public inputs, then run Gemini advisory independently.
