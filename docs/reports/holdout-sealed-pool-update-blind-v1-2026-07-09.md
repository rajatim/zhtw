<!-- zhtw:disable -->
# Holdout Sealed Pool Update - blind-v1

Generated: `2026-07-09`

This report records the removal of public regression candidates from the sealed holdout pool. It does not include expected values, input text, or converter outputs.

## Summary

- Original input cases: 100
- Removed to public regression candidates: 22
- Remaining sealed input cases: 78
- Public candidates: `benchmarks/accuracy/holdout-regression-candidates-v1.json`
- Private expected updated: `True`
- Source inputs sha256: `f3572ff591046f6890baa1cd9cfe5732ac44fa3a4bb9707ffea102a392cf81c9`
- Private expected sha256: `4700b294de9a9fdac211f53b471ad9de765620bcdc5452d04f8f766156a3741a`

## Removed Case IDs

- `blind-it-0002`
- `blind-it-0005`
- `blind-it-0006`
- `blind-it-0008`
- `blind-it-0009`
- `blind-it-0010`
- `blind-it-0015`
- `blind-it-0021`
- `blind-it-0023`
- `blind-it-0024`
- `blind-it-0025`
- `blind-ui-0001`
- `blind-ui-0004`
- `blind-ui-0006`
- `blind-ui-0009`
- `blind-ui-0019`
- `blind-ui-0020`
- `blind-llm-0010`
- `blind-llm-0013`
- `blind-formal-0003`
- `blind-social-0005`
- `blind-social-0007`

## Remaining Sealed Distribution

| Domain | Cases |
|--------|-------|
| formal | 14 |
| high_risk | 10 |
| it | 14 |
| llm | 13 |
| social | 13 |
| ui | 14 |

| Risk | Cases |
|------|-------|
| baseline_guard | 13 |
| candidate_gap | 46 |
| over_conversion_guard | 19 |
