<!-- zhtw:disable -->
# Paired Localization Benchmark: firefox-paired-ui-v1 (2026-07-31)

Report mode: `aggregate`

This project-run public track compares converter output with a vendor's paired
Traditional localization. The vendor translation is a useful reference, not
universal Taiwan Traditional ground truth. This track cannot replace Blind-v2.

| Engine | Exact | Accuracy | Idempotency | Changed-span F1 |
|---|---:|---:|---:|---:|
| zhtw 4.4.2 | 270 / 1264 | 0.213608 | 0.989715 | 0.334286 |
| opencc-s2twp 1.4.1 | 290 / 1264 | 0.229430 | 0.995253 | 0.344563 |
| zhconv-zh-tw 1.4.3 | 147 / 1264 | 0.116297 | 1.000000 | 0.246812 |

## Paired Comparisons

- zhtw vs `opencc-s2twp`: -0.015823; 95% CI -0.031646 to +0.000000; statistical_tie.
- zhtw vs `zhconv-zh-tw`: +0.097310; 95% CI +0.080696 to +0.113924; winner.
