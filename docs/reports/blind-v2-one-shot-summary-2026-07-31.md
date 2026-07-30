<!-- zhtw:disable -->
# Blind-v2 One-Shot Summary (2026-07-31)

## Result

Blind-v2 completed as an aggregate-only one-shot evaluation on 1,960 frozen
cases. zhtw 4.4.2 ranked first by the preregistered accepted-accuracy endpoint
among the locked OpenCC and MediaWiki/zhconv families.

| Engine | Family role | Accepted | Accuracy | 95% CI | Idempotency |
|---|---|---:|---:|---:|---:|
| zhtw 4.4.2 | candidate | 661 / 1,960 | 33.72% | 31.73%-35.87% | 97.70% |
| OpenCC s2twp 1.4.1 | OpenCC representative | 604 / 1,960 | 30.82% | 28.88%-32.91% | 98.42% |
| zhconv zh-tw 1.4.3 | MediaWiki representative | 560 / 1,960 | 28.57% | 26.63%-30.46% | 99.95% |

The two family conformance implementations matched their ranking representatives
on accepted count: opencc-js had 604 accepted cases, and zhconv-rs had 560.

## Paired Comparison

| Representative | zhtw delta | Delta 95% CI | McNemar exact p | Result |
|---|---:|---:|---:|---|
| OpenCC s2twp | +2.91 pp | +1.48 to +4.34 pp | 0.0000904 | zhtw winner |
| zhconv zh-tw | +5.15 pp | +3.67 to +6.63 pp | 1.18e-11 | zhtw winner |

Both confidence intervals are above zero, so the preregistered winner rule is
met for both independent ranking families.

## Scope And Limits

- The valid claim is limited to Simplified Chinese to Taiwan Traditional Chinese,
  this frozen 1,960-case design, and the listed locked engines and versions.
- The 33.72% value is strict sentence-level accepted accuracy on a difficult,
  quota-balanced benchmark. It is not an estimate that zhtw is correct only
  33.72% of the time in normal use.
- zhtw did not lead every domain. OpenCC led social/daily and UI cases; zhconv
  led formal/news and high-stakes cases. zhtw led the aggregate endpoint, IT/API/CLI,
  and LLM-generated cases.
- zhtw idempotency was lower than both ranking representatives. This remains a
  product-quality target even though zhtw won the primary endpoint.
- Expected values were confirmed by one maintainer with Codex and independent
  Agy advice. This is `single_human_with_ai_advisory`, not a two-human review.
- No detailed rows were read. Error-taxonomy review and case-level tuning are
  outside this one-shot result and would require moving reviewed cases out of
  sealed status.

## Governance

- Candidate commit: `19626cf119e0ef7c8c04faa81960ee735eb9ac5a`
- Preregistration SHA-256: `f9931673a781acd9b3c68d5805b801161dbeb982fb66d07c336c1b68731a5f5c`
- Inputs SHA-256: `ddef836456ee29decf019dae981c1017b9728524c42808ae2d7c2c894299820a`
- Expected SHA-256: `511b2845969a60c6c5b53e7de17b85fbe00b11521648dac10e77fe6ec6ace9c5`
- Competitor lock SHA-256: `f72ed6d38c1fe1336a61c267baab518b48cd4d3046d4ca3bd525f94eb7ca8765`
- Aggregate JSON SHA-256: `4e63fb66bb74d12bd46176e17e6235334da48d1460c5fef7a30cb44b5906c34c`
- Ledger snapshot SHA-256: `62fcea244da64b4f4b0886bdf5e412301b7009a8e01ad7c05f46cd6d47720ef4`
- Ledger events: one interrupted preflight attempt and one completed
  `score_exposed` attempt; `detailed_rows_read` remained false for every event.

The raw aggregate reports are `blind-v2-benchmark-2026-07-31.json` and
`blind-v2-benchmark-2026-07-31.md` in this directory.
