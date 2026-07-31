<!-- zhtw:disable -->
# Formal Market Benchmark (2026-07-31)

Report mode: `aggregate`

## Decision

zhtw is the scoped winner on the preregistered Blind-v2 primary endpoint.
This is not an unrestricted market-best claim.

## Primary Result

| Engine | Accepted | Accuracy | 95% CI | Idempotency |
|---|---:|---:|---:|---:|
| zhtw 4.4.2 | 661 / 1960 | 33.72% | 31.73%-35.87% | 97.70% |
| opencc-s2twp 1.4.1 | 604 / 1960 | 30.82% | 28.88%-32.91% | 98.42% |
| zhconv-zh-tw 1.4.3 | 560 / 1960 | 28.57% | 26.63%-30.46% | 99.95% |

| Comparison | Delta | Delta 95% CI | McNemar p | Result |
|---|---:|---:|---:|---|
| zhtw vs opencc-s2twp | +2.91 pp | +1.48 to +4.34 pp | 9.04e-05 | winner |
| zhtw vs zhconv-zh-tw | +5.15 pp | +3.67 to +6.63 pp | 1.18e-11 | winner |

Both paired confidence intervals are fully above zero, and the aggregate report
records zero tagged P0 errors. The P0 value is not a separate human review of all
misses because detailed rows remained sealed.

## Secondary Evidence

- `ud-gsd-v1`: 4,997 cases, 70.52% accuracy, 97.94% idempotency; clean commit `a11d1f4eba49648fabc3fee019c37fb633996cbe`.
- `naer-terms-v1`: 775 cases, 40.13% accuracy, 96.65% idempotency; clean commit `a11d1f4eba49648fabc3fee019c37fb633996cbe`.
- `aosp-framework-paired-ui-v1`: 1,968 cases, 20.48% accuracy, 97.41% idempotency; clean commit `4d26060cbfd7d07b3e80c6a740fc4a069a038c23`.
- `vscode-paired-ui-v1`: 17,133 cases, 12.21% accuracy, 97.51% idempotency; clean commit `4d26060cbfd7d07b3e80c6a740fc4a069a038c23`.
- `firefox-paired-ui-v1`: 1,264 cases, 23.18% accuracy, 99.21% idempotency; clean commit `4d26060cbfd7d07b3e80c6a740fc4a069a038c23`.

The public evidence is mixed. On exact vendor-localization agreement, OpenCC
led zhtw on AOSP and VS Code, while Firefox was a statistical tie. zhtw led
zhconv on all three. Vendor translation is not universal Taiwan Traditional
ground truth, and these results do not change the frozen Blind-v2 decision.

## Limits

- The result covers Simplified Chinese to Taiwan Traditional Chinese only.
- It covers the frozen Blind-v2 cases and listed locked versions only.
- Strict sentence-level accepted accuracy is not normal-traffic accuracy.
- zhtw did not lead every domain and had lower Blind-v2 idempotency than both ranking representatives.
- Expected values used one maintainer with Codex and independent Agy advice.
- Detailed rows were not read during the formal run. A later controlled audit reviewed all 1,299 zhtw misses, and the maintainer confirmed all 152 queued synthesis decisions.
- Independent third-party reproduction remains optional stronger evidence in GitHub issue #51; it is not recorded as completed.

## Proposed Claim

On the frozen 1,960-case Blind-v2 benchmark for Simplified Chinese to Taiwan Traditional Chinese, zhtw 4.4.2 achieved 33.72% accepted accuracy, above OpenCC 1.4.1 at 30.82% and zhconv 1.4.3 at 28.57%. Both paired 95% confidence intervals were above zero. This result applies only to this dataset, direction, metric, and the listed versions; it does not prove that zhtw is best for every domain or real-world workload.

Status: `confirmed_by_maintainer` on 2026-07-31.

## Governance

- Blind-v2 commit: `19626cf119e0ef7c8c04faa81960ee735eb9ac5a`
- Public-track commits: `ud-gsd-v1`=`a11d1f4eba49648fabc3fee019c37fb633996cbe`, `naer-terms-v1`=`a11d1f4eba49648fabc3fee019c37fb633996cbe`, `aosp-framework-paired-ui-v1`=`4d26060cbfd7d07b3e80c6a740fc4a069a038c23`, `vscode-paired-ui-v1`=`4d26060cbfd7d07b3e80c6a740fc4a069a038c23`, `firefox-paired-ui-v1`=`4d26060cbfd7d07b3e80c6a740fc4a069a038c23`
- Preregistration SHA-256: `f9931673a781acd9b3c68d5805b801161dbeb982fb66d07c336c1b68731a5f5c`
- Inputs SHA-256: `ddef836456ee29decf019dae981c1017b9728524c42808ae2d7c2c894299820a`
- Expected SHA-256: `511b2845969a60c6c5b53e7de17b85fbe00b11521648dac10e77fe6ec6ace9c5`
- Competitor lock SHA-256: `f72ed6d38c1fe1336a61c267baab518b48cd4d3046d4ca3bd525f94eb7ca8765`
- Public-track score reproduction: GitHub Actions run `30591590536` passed.
- Optional independent public-track reproduction request: GitHub issue `#51`.
