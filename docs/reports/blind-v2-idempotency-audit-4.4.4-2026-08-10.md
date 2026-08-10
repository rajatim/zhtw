<!-- zhtw:disable -->
# Blind-v2 Idempotency Audit for zhtw 4.4.4

Report mode: `aggregate`

## Result

| Version | Idempotent | Rate | Non-idempotent |
|---|---:|---:|---:|
| zhtw 4.4.3 | 1,915 / 1,960 | 97.70% | 45 |
| zhtw 4.4.4 | 1,925 / 1,960 | 98.21% | 35 |

Version 4.4.4 removes ten second-pass failures on the frozen Blind-v2 inputs.
The selected-match coverage fix and generated target identity guards caused the
change. The complete effective dictionary target audit also reports zero
unstable targets, including the OpenCC-derived bulk file.

The remaining 35 sentence cases can involve terms formed across converted span
boundaries. This report does not treat a second-pass output as an automatic
correction and does not use sealed case content for tuning.

## Safety Decision

The audit publishes no case IDs, input text, intermediate output, or second-pass
output. The regression baseline stores only the input hash, aggregate counts,
and a SHA-256 hash of the non-idempotent ID set.

Any semantic follow-up must use approved public regression material and the
normal Codex, independent Agy, and maintainer decision process. Blind-v2 remains
sealed historical evidence.

## Reproduction

```bash
uv run python scripts/audit_corpus_idempotency.py \
  benchmarks/accuracy/blind-v2.inputs.json \
  --baseline benchmarks/accuracy/blind-v2.idempotency-baseline.json

uv run python scripts/audit_idempotency.py \
  --sources cn,hk --fail-on-issues
```

Status: `baseline_locked` on 2026-08-10.
