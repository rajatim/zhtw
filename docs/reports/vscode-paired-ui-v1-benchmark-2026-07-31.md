<!-- zhtw:disable -->
# Paired Localization Benchmark: vscode-paired-ui-v1 (2026-07-31)

Report mode: `aggregate`

This project-run public track compares converter output with a vendor's paired
Traditional localization. The vendor translation is a useful reference, not
universal Taiwan Traditional ground truth. This track cannot replace Blind-v2.

The Simplified source overlaps the Blind-v2 source pool. Treat this as a
diagnostic track, not fresh independent evidence for the primary claim.

| Engine | Exact | Accuracy | Idempotency | Changed-span F1 |
|---|---:|---:|---:|---:|
| zhtw 4.4.3 | 2092 / 17133 | 0.122104 | 0.975077 | 0.300469 |
| opencc-s2twp 1.4.1 | 2190 / 17133 | 0.127823 | 0.978813 | 0.303019 |
| zhconv-zh-tw 1.4.3 | 1288 / 17133 | 0.075177 | 0.994980 | 0.222300 |

## Paired Comparisons

- zhtw vs `opencc-s2twp`: -0.005720; 95% CI -0.008463 to -0.002918; loser.
- zhtw vs `zhconv-zh-tw`: +0.046927; 95% CI +0.043717 to +0.050254; winner.
