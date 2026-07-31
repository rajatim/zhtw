<!-- zhtw:disable -->
# Blind-v2 Post-result Audit (2026-07-31)

Report mode: `aggregate`

## Status

The controlled audit has reviewed every zhtw miss and is pending maintainer
confirmation. The published Blind-v2 score is immutable.

## Coverage

- Benchmark cases: 1,960
- Audited zhtw misses: 1,299
- Codex first pass: 1,299
- Independent Agy review: 1,299
- Codex synthesis: 501

## Agreement

- Severity: 981 / 1,299 (75.52%)
- Category: 861 / 1,299 (66.28%)
- All decision fields: 810 / 1,299 (62.36%)

## Final Advisory

| Severity | Cases |
|---|---:|
| P0 | 0 |
| P1 | 45 |
| P2 | 656 |
| P3 | 82 |
| none | 516 |

The private maintainer queue contains 152 cases: 45 P1 semantic-error decisions and 107 acceptable-variant decisions. It includes 2 reference-correction candidates.

## Governance

- Case-level material remains private and gitignored.
- This report contains aggregate counts only.
- Findings cannot change the consumed Blind-v2 score.
- Findings cannot be used to tune against sealed rows.
- The audit is complete only after maintainer confirmation.
