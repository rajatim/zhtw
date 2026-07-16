# Public Reproduction Codex First Pass After Batch10 Remaining Signal

- Generated date: `2026-07-13`
- Dataset: `public-reproduction-seeds-v1`
- Source inputs: `benchmarks/accuracy/public-reproduction-seeds-v1.json`
- Reviewer: `codex`
- Stage: `first_pass_advisory`
- Ground truth: `false`
- Promotion allowed: `false`

Codex produced first-pass expected recommendations for all 32 independent
public reproduction inputs. These are advisory only. They must not be written
to regression data or used for tuning until Gemini independent advisory and
maintainer confirmation are complete.

Summary:

| Metric | Count |
| --- | ---: |
| Total cases | 32 |
| High confidence | 19 |
| Medium confidence | 13 |
| Review-needed | 13 |

Domain distribution:

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

Next step: run Gemini independent advisory from the public input-only seed set,
without showing Gemini this Codex first-pass report.
