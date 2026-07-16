<!-- zhtw:disable -->
# Holdout Private Benchmark Sanity Summary (2026-07-08)

Dataset: `blind-v1`
Engine: `zhtw`
Private expected status: `sealed_private`
Private expected sha256: `efb8ee42152eacede683dbfa357ace86b3b649ce611eef0d3362646ae8ba7e65`

## Boundary

- Aggregate-only sanity summary.
- Expected values and per-case rows are intentionally omitted.
- Full benchmark report is kept outside the repo because it contains private expected values.
- Do not use this holdout to tune zhtw without first removing affected cases from sealed holdout.

## Summary

- Cases: 100
- Accepted: 57
- Misses: 43
- Accepted accuracy: 0.5700
- Primary exact accuracy: 0.5700
- Idempotency rate: 0.9400

## Domain Accuracy

- `formal`: 10 / 15 (0.6667)
- `high_risk`: 10 / 10 (1.0000)
- `it`: 8 / 25 (0.3200)
- `llm`: 9 / 15 (0.6000)
- `social`: 12 / 15 (0.8000)
- `ui`: 8 / 20 (0.4000)

## Misses By Risk

- `baseline_guard`: 5
- `candidate_gap`: 35
- `over_conversion_guard`: 3

## Misses By Issue Tag

- `formal_term`: 9
- `high_risk_term`: 1
- `it_term`: 26
- `regional_term`: 43
- `ui_term`: 17
