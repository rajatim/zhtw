<!-- zhtw:disable -->
# Private Benchmark Sanity Summary - After Batch6 Final Decision

Generated: `2026-07-10`

This report is aggregate-only. Sealed inputs, expected values, acceptable variants, actual outputs, and benchmark rows are omitted.

## Source

- Full private benchmark: `/tmp/zhtw-blind-v1-private-benchmark-after-batch6-2026-07-10.json`
- Inputs sha256: `be3ab808d2f2bb71b1c86e66cd95eb182446693412c1ebbecdf5aa632f35d35e`
- Expected sha256: `ac7200fde2a7a304a311704bf0da90fb526181b73f9c402c87736c6369eee91e`

## Summary

- case_count: 426
- accepted: 389
- misses: 37
- primary_exact: 308
- acceptable_exact: 81
- accepted_accuracy: 0.913145539906
- primary_exact_accuracy: 0.723004694836
- idempotency_rate: 0.985915492958

## Domain Accuracy

- `formal`: 64/69 (0.927536231884)
- `high_risk`: 43/46 (0.934782608696)
- `it`: 73/86 (0.848837209302)
- `llm`: 66/71 (0.929577464789)
- `social`: 65/70 (0.928571428571)
- `ui`: 78/84 (0.928571428571)

## Misses By Risk

- `baseline_guard`: 1
- `candidate_gap`: 12
- `over_conversion_guard`: 24

## Misses By Issue Tag

- `formal_term`: 8
- `high_risk_term`: 3
- `it_term`: 16
- `over_conversion`: 24
- `regional_term`: 37
- `ui_term`: 6
