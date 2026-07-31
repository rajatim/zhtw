<!-- zhtw:disable -->
# Paired Localization Benchmark: aosp-framework-paired-ui-v1 (2026-07-31)

Report mode: `aggregate`

This project-run public track compares converter output with a vendor's paired
Traditional localization. The vendor translation is a useful reference, not
universal Taiwan Traditional ground truth. This track cannot replace Blind-v2.

The Simplified source overlaps the Blind-v2 source pool. Treat this as a
diagnostic track, not fresh independent evidence for the primary claim.

| Engine | Exact | Accuracy | Idempotency | Changed-span F1 |
|---|---:|---:|---:|---:|
| zhtw 4.4.2 | 380 / 1968 | 0.193089 | 0.972053 | 0.328510 |
| opencc-s2twp 1.4.1 | 418 / 1968 | 0.212398 | 0.986280 | 0.348770 |
| zhconv-zh-tw 1.4.3 | 309 / 1968 | 0.157012 | 0.999492 | 0.287426 |

## Paired Comparisons

- zhtw vs `opencc-s2twp`: -0.019309; 95% CI -0.028963 to -0.010671; loser.
- zhtw vs `zhconv-zh-tw`: +0.036077; 95% CI +0.024898 to +0.047256; winner.
