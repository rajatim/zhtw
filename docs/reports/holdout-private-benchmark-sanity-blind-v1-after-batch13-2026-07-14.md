<!-- zhtw:disable -->
# Holdout Private Benchmark Sanity - After Batch13

Generated: `2026-07-14`

## Aggregate

- Cases: 1030
- Accepted: 950
- Misses: 80
- Accepted accuracy: 92.23%

## Fresh Batch13

- Cases: 100
- Accepted: 66
- Misses: 34
- Accepted accuracy: 66.00%
- By domain: {"formal": {"total": 15, "accepted": 13, "misses": 2}, "high_risk": {"total": 15, "accepted": 10, "misses": 5}, "it": {"total": 20, "accepted": 10, "misses": 10}, "llm": {"total": 15, "accepted": 9, "misses": 6}, "social": {"total": 20, "accepted": 17, "misses": 3}, "ui": {"total": 15, "accepted": 7, "misses": 8}}
- Misses by risk: {"baseline_guard": 4, "candidate_gap": 28, "over_conversion_guard": 2}

## Interpretation

Batch13 was fresh and benchmarked before tuning, so its 66% result is a valid generalization signal under single-human-with-AI-advisory expected review. It does not support a market-best claim. This report contains aggregate statistics only and no input, expected, acceptable, output, or row data.
