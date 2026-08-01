<!-- zhtw:disable -->
# Blind-v2 Idempotency Audit for zhtw 4.4.3

Report mode: `aggregate`

## Result

| Version | Idempotent | Rate | Non-idempotent |
|---|---:|---:|---:|
| zhtw 4.4.3 | 1,915 / 1,960 | 97.70% | 45 |

The result matches the formal zhtw 4.4.2 Blind-v2 idempotency rate. Version 4.4.3
did not add a new sentence-level idempotency regression on this frozen input set,
but it also did not reduce the existing 45 cases.

## Safety Decision

The audit does not publish case IDs, intermediate output, or second-pass output.
The regression baseline stores only the input hash, aggregate counts, and a SHA-256
hash of the non-idempotent ID set.

The second pass is not accepted as an automatic correction. Some second-pass
changes are over-conversions, so each candidate must follow the normal Codex,
independent Agy, and maintainer review process before a dictionary change.

## Reproduction

```bash
uv run python scripts/audit_corpus_idempotency.py \
  benchmarks/accuracy/blind-v2.inputs.json \
  --baseline benchmarks/accuracy/blind-v2.idempotency-baseline.json
```

Status: `baseline_locked` on 2026-08-01.

Follow-up: [GitHub issue #54](https://github.com/rajatim/zhtw/issues/54).
