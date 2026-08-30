# Quality and evidence

Every ZHTW quality claim must state the version, data set, sample size, scoring method, and limits. Public reports are reproducible. Internal release job numbers are not accuracy evidence.

## Formal Blind-v2 historical result

Blind-v2 is a frozen one-shot benchmark of **zhtw 4.4.2** with **1,960 cases**. It preserves the formal comparison before tuning. It is not a live 4.5.0 score, and later improvements do not rewrite it.

See these sources for full scores, competitor versions, container digests, data hashes, and limits:

- [Formal market comparison report](https://github.com/rajatim/zhtw/blob/main/docs/reports/formal-market-benchmark-2026-07-31.md)
- [Public third-party reproduction](https://github.com/rajatim/zhtw/blob/main/docs/testing/public-benchmark-third-party-reproduction.md)
- [Public paired localization benchmarks](https://github.com/rajatim/zhtw/blob/main/docs/testing/public-paired-localization-benchmarks.md)

## Continuous quality gates

Every release candidate checks:

- Shared golden fixtures in Python and every SDK.
- Dictionary structure, schema, versions, and exported-data consistency.
- Incorrect-conversion regressions, identity protection, and idempotency.
- Exact-byte JSON adapter cases and the `explain` event contract.
- Bilingual public pages, versions, examples, and a strict site build.

## Reading the results

- Exact match requires the whole sentence to match. It is sensitive to punctuation and reasonable variants.
- Accepted score may include variants approved before evaluation. Answers must not be added after seeing converter output.
- Idempotency only proves that a second run does not change the result. It does not prove that the first result is correct.
- Public paired data is useful for diagnosis, but it cannot replace a sealed holdout that the project has not seen.

Blind-v3 has not run. It is not a 4.5.0 release condition. Any future claim will publish its version, freeze process, and limits separately.
