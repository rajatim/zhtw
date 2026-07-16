<!-- zhtw:disable -->
# Holdout Input Pool Expansion - blind-v1

- Generated date: `2026-07-09`
- Dataset: `blind-v1`
- Source inputs: `benchmarks/accuracy/blind-v1.inputs.json`
- Source inputs SHA256: `6dbe5865463ebc4dc68c191aaa54de7454c6aa3ebb76bbada52fb6a90840c48f`
- Expected values included: `false`
- Input texts included: `false`

## Summary

| Metric | Cases |
|--------|-------|
| Previous input cases | 73 |
| Added input cases | 127 |
| Current input cases | 200 |
| Target total | 2000 |

## Added By Domain

| Domain | Added | Current |
|--------|-------|---------|
| formal | 18 | 30 |
| high_risk | 10 | 20 |
| it | 37 | 50 |
| llm | 17 | 30 |
| social | 18 | 30 |
| ui | 27 | 40 |

## Added By Risk

| Risk | Added | Current |
|------|-------|---------|
| baseline_guard | 17 | 30 |
| candidate_gap | 79 | 120 |
| over_conversion_guard | 31 | 50 |

## Policy

This expansion adds public input-only seed cases. It does not include expected values, acceptable variants, converter outputs, or benchmark rows. These cases require human annotation before they can be used for any benchmark score.
