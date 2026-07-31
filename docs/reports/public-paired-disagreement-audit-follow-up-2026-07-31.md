<!-- zhtw:disable -->
# Public Paired Disagreement Audit Follow-up (2026-07-31)

## Scope

This project-run audit reviewed a deterministic 100-case sample where locked
OpenCC matched an AOSP or Firefox Traditional localization and zhtw did not.
The sample contained 60 AOSP cases and 40 Firefox cases.

The review order was Codex first pass, independent Agy review, Codex synthesis,
and maintainer confirmation. The maintainer confirmed 57 real zhtw gaps and 43
acceptable Taiwan variants.

## Implementation

- 51 of the 57 confirmed gaps now produce a maintainer-accepted output.
- Both P1 semantic errors were fixed: `日常` is no longer changed to `每日`, and
  `私密` is no longer changed to `私人`.
- Six context-free labels remain conservative: two `保存` cases, plus `不支持`,
  `壁纸`, `文件`, and `默认`.
- Broad mappings were not added for those labels because each has a valid
  non-UI meaning that would be damaged by a forced Taiwan UI term.
- Accepted forms such as `打開`, `查看`, and `字體` remain accepted and were not
  forced to `開啟`, `檢視`, or `字型`.

## Post-audit Diagnostics

The post-audit implementation is versioned as zhtw 4.4.3. The original formal
benchmark remains a historical zhtw 4.4.2 result.

| Track | Before | After | Exact accuracy before | Exact accuracy after | Idempotency before | Idempotency after |
|---|---:|---:|---:|---:|---:|---:|
| AOSP framework UI | 380 / 1,968 | 403 / 1,968 | 19.31% | 20.48% | 97.21% | 97.41% |
| VS Code UI | 2,089 / 17,133 | 2,092 / 17,133 | 12.19% | 12.21% | 97.50% | 97.51% |
| Firefox browser UI | 270 / 1,264 | 293 / 1,264 | 21.36% | 23.18% | 98.97% | 99.21% |

The UD GSD secondary diagnostic also moved from 3,522 to 3,524 exact matches
out of 4,997 cases.

## Interpretation

These are tuned regression diagnostics, not fresh benchmark evidence. The
audited AOSP and Firefox cases directly informed the fixes, so their improved
scores must not be used as independent support for a market-best claim. The
frozen Blind-v2 result and the original public-track reports remain unchanged.
