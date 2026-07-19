<!-- zhtw:disable -->
# Accuracy Benchmark (2026-07-19)

Report mode: `aggregate`
Dataset classification: `published_evaluation`

Dataset: `blind-v1`
Inputs: `benchmarks/accuracy/blind-v1.inputs.json`
Competitors lock: `benchmarks/accuracy/competitors.lock.json`

## Hashes

- Inputs sha256: `4367f25a4bde5a1703163334815e5579788f528bed9401f4197a93bea5ee03e7`
- Expected sha256: `80d27928a962cb03319c09b80f8b0aa22f25be3eb756130e63bfcac1df1c3dcc`
- Lock sha256: `d9bf3f57e280287e1cc1699d82d62bcbe28c1b1665b82ab1db60ef8520bdad18`

## Summary

- Cases: 1008

Domain distribution:

- `formal`: 164
- `high_risk`: 128
- `it`: 189
- `llm`: 159
- `social`: 180
- `ui`: 188

Risk distribution:

- `baseline_guard`: 161
- `candidate_gap`: 564
- `over_conversion_guard`: 283

## Engine Scores

### zhtw

- Availability: available
- Version: `4.4.1`
- Accepted accuracy: 0.9474
- Primary exact accuracy: 0.7520
- Idempotency rate: 0.9851
- Accepted: 955 / 1008
- Misses: 53

