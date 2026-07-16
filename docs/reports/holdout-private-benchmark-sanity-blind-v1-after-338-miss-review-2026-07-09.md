<!-- zhtw:disable -->
# Private Benchmark Sanity Summary - After 338 Miss Review

Generated: `2026-07-09`

This report is aggregate-only. Sealed inputs, expected values, acceptable variants, actual outputs, and benchmark rows are omitted.

## Source

- Full private benchmark: `/tmp/zhtw-blind-v1-private-benchmark-after-338-miss-review-2026-07-09.json`
- Inputs sha256: `2d69cf2ceb90dff8b41e9806cfe7c642d8e3e64947ea83045a8fd41be705a5a2`
- Expected sha256: `899b3d87ef8dc551f2ac517646d76c990ca9ae9a303599ea7d5e11a7e399fd3c`

## Summary

- case_count: 326
- accepted: 304
- misses: 22
- primary_exact: 242
- acceptable_exact: 62
- accepted_accuracy: 0.932515337423
- primary_exact_accuracy: 0.742331288344
- idempotency_rate: 0.990797546012

## Domain Accuracy

- `formal`: 49/54 (0.907407407407)
- `high_risk`: 33/36 (0.916666666667)
- `it`: 59/61 (0.967213114754)
- `llm`: 52/56 (0.928571428571)
- `social`: 50/55 (0.909090909091)
- `ui`: 61/64 (0.953125000000)

## Misses By Risk

- `over_conversion_guard`: 22

## Misses By Issue Tag

- `formal_term`: 8
- `high_risk_term`: 3
- `it_term`: 4
- `over_conversion`: 22
- `regional_term`: 22
- `ui_term`: 3
