<!-- zhtw:disable -->
# Holdout Sealed Pool Update - blind-v1 batch2

Generated: `2026-07-09`

This report records the second removal of public regression candidates from the sealed holdout pool. It does not include expected values, input text, or converter outputs.

## Summary

- Original input cases: 78
- Removed to public regression candidates: 5
- Remaining sealed input cases: 73
- Public candidates: `benchmarks/accuracy/holdout-regression-candidates-v1.json`
- Private expected updated: `True`
- Source inputs sha256: `38c74d7219657a137c7fe93ff50d5f1c4ee22d02e9ff97fe805d5b72bd297f60`
- Private expected sha256: `d107756144b3f23d1cb5e00724767d6fe33fe5886ddbea2053e3414c82e73866`

## Removed Case IDs

- `blind-it-0014`
- `blind-ui-0002`
- `blind-formal-0006`
- `blind-formal-0010`
- `blind-social-0015`

## Remaining Sealed Distribution

| Domain | Cases |
|--------|-------|
| formal | 12 |
| high_risk | 10 |
| it | 13 |
| llm | 13 |
| social | 12 |
| ui | 13 |

| Risk | Cases |
|------|-------|
| baseline_guard | 13 |
| candidate_gap | 41 |
| over_conversion_guard | 19 |
