<!-- zhtw:disable -->
# Accuracy Benchmark (2026-07-09)

Report mode: `aggregate`
Dataset classification: `published_evaluation`

Dataset: `blind-v1`
Inputs: `benchmarks/accuracy/blind-v1.inputs.json`
Competitors lock: `benchmarks/accuracy/competitors.lock.json`

## Hashes

- Inputs sha256: `29200c136659fecd27e8efb59390d18f53a33508962848845c4eb78de6cd0f41`
- Expected sha256: `8682ef7b0a2cf1bc61a75628eadc16d196d7d64b6ebc3f28fc0ae447ae913fdf`
- Lock sha256: `d9bf3f57e280287e1cc1699d82d62bcbe28c1b1665b82ab1db60ef8520bdad18`

## Summary

- Cases: 338

Domain distribution:

- `formal`: 54
- `high_risk`: 36
- `it`: 68
- `llm`: 57
- `social`: 55
- `ui`: 68

Risk distribution:

- `baseline_guard`: 53
- `candidate_gap`: 197
- `over_conversion_guard`: 88

## Engine Scores

### zhtw

- Availability: available
- Version: `4.4.1`
- Accepted accuracy: 0.8905
- Primary exact accuracy: 0.7160
- Idempotency rate: 0.9911
- Accepted: 301 / 338
- Misses: 37
