<!-- zhtw:disable -->
# Holdout Remaining Signal Summary - blind-v1 After Batch6 Miss Review

Generated: `2026-07-10`

This report summarizes the 24 remaining sealed holdout signals after batch6 miss review. It intentionally omits expected values, acceptable variants, input text, converter outputs, and benchmark rows.

## Sealed Content Policy

| Field | Included |
|-------|----------|
| Expected values | No |
| Acceptable variants | No |
| Actual converter outputs | No |
| Input text | No |
| Full benchmark rows | No |
| Case IDs and metadata | Yes |

## Summary

- Current sealed cases: 415
- Current accepted: 391
- Current misses: 24
- Remaining signal cases: 24
- Converter or dictionary updated: `false`
- Private expected updated in this step: `false`
- Non-idempotent signal cases: 0
- Miss risk: `over_conversion_guard` only

## Signal Cases

| Case | Domain | Risk | Signal category | Reason | Flags |
|------|--------|------|-----------------|--------|-------|
| `blind-llm-0026` | `llm` | `over_conversion_guard` | `existing_taiwan_term_over_conversion_signal` | `preserve_existing_taiwan_term_over_conversion_guard` | `over_conversion_guard` |
| `blind-llm-0028` | `llm` | `over_conversion_guard` | `existing_taiwan_term_over_conversion_signal` | `preserve_existing_taiwan_term_over_conversion_guard` | `over_conversion_guard` |
| `blind-formal-0029` | `formal` | `over_conversion_guard` | `existing_taiwan_term_over_conversion_signal` | `preserve_existing_taiwan_term_over_conversion_guard` | `over_conversion_guard` |
| `blind-social-0025` | `social` | `over_conversion_guard` | `existing_taiwan_term_over_conversion_signal` | `preserve_existing_taiwan_term_over_conversion_guard` | `over_conversion_guard` |
| `blind-social-0026` | `social` | `over_conversion_guard` | `existing_taiwan_term_over_conversion_signal` | `preserve_existing_taiwan_term_over_conversion_guard` | `over_conversion_guard` |
| `blind-it-0083` | `it` | `over_conversion_guard` | `existing_taiwan_term_over_conversion_signal` | `preserve_existing_taiwan_term_over_conversion_guard` | `over_conversion_guard` |
| `blind-ui-0060` | `ui` | `over_conversion_guard` | `existing_taiwan_term_over_conversion_signal` | `preserve_existing_taiwan_term_over_conversion_guard` | `over_conversion_guard` |
| `blind-ui-0061` | `ui` | `over_conversion_guard` | `existing_taiwan_term_over_conversion_signal` | `preserve_existing_taiwan_term_over_conversion_guard` | `over_conversion_guard` |
| `blind-llm-0043` | `llm` | `over_conversion_guard` | `existing_taiwan_term_over_conversion_signal` | `preserve_existing_taiwan_term_over_conversion_guard` | `over_conversion_guard` |
| `blind-llm-0044` | `llm` | `over_conversion_guard` | `existing_taiwan_term_over_conversion_signal` | `preserve_existing_taiwan_term_over_conversion_guard` | `over_conversion_guard` |
| `blind-formal-0043` | `formal` | `over_conversion_guard` | `existing_taiwan_term_over_conversion_signal` | `preserve_existing_taiwan_term_over_conversion_guard` | `over_conversion_guard` |
| `blind-formal-0044` | `formal` | `over_conversion_guard` | `existing_taiwan_term_over_conversion_signal` | `preserve_existing_taiwan_term_over_conversion_guard` | `over_conversion_guard` |
| `blind-formal-0045` | `formal` | `over_conversion_guard` | `existing_taiwan_term_over_conversion_signal` | `preserve_existing_taiwan_term_over_conversion_guard` | `over_conversion_guard` |
| `blind-formal-0046` | `formal` | `over_conversion_guard` | `existing_taiwan_term_over_conversion_signal` | `preserve_existing_taiwan_term_over_conversion_guard` | `over_conversion_guard` |
| `blind-social-0042` | `social` | `over_conversion_guard` | `existing_taiwan_term_over_conversion_signal` | `preserve_existing_taiwan_term_over_conversion_guard` | `over_conversion_guard` |
| `blind-social-0043` | `social` | `over_conversion_guard` | `existing_taiwan_term_over_conversion_signal` | `preserve_existing_taiwan_term_over_conversion_guard` | `over_conversion_guard` |
| `blind-social-0044` | `social` | `over_conversion_guard` | `existing_taiwan_term_over_conversion_signal` | `preserve_existing_taiwan_term_over_conversion_guard` | `over_conversion_guard` |
| `blind-high-risk-0026` | `high_risk` | `over_conversion_guard` | `high_risk_existing_term_over_conversion_signal` | `preserve_existing_taiwan_term_over_conversion_guard` | `over_conversion_guard`, `high_risk` |
| `blind-high-risk-0027` | `high_risk` | `over_conversion_guard` | `high_risk_existing_term_over_conversion_signal` | `preserve_existing_taiwan_term_over_conversion_guard` | `over_conversion_guard`, `high_risk` |
| `blind-it-0108` | `it` | `over_conversion_guard` | `existing_taiwan_term_over_conversion_signal` | `preserve_existing_taiwan_term_over_conversion_guard` | `over_conversion_guard` |
| `blind-ui-0081` | `ui` | `over_conversion_guard` | `existing_taiwan_term_over_conversion_signal` | `preserve_existing_taiwan_term_over_conversion_guard` | `over_conversion_guard` |
| `blind-high-risk-0039` | `high_risk` | `over_conversion_guard` | `high_risk_existing_term_over_conversion_signal` | `preserve_existing_taiwan_term_over_conversion_guard` | `over_conversion_guard`, `high_risk` |
| `blind-it-0131` | `it` | `over_conversion_guard` | `existing_taiwan_term_over_conversion_signal` | `preserve_existing_taiwan_term_over_conversion_guard` | `over_conversion_guard` |
| `blind-ui-0102` | `ui` | `over_conversion_guard` | `existing_taiwan_term_over_conversion_signal` | `preserve_existing_taiwan_term_over_conversion_guard` | `over_conversion_guard` |

## Policy Notes

- These cases remain sealed and must not be used for converter or dictionary tuning.
- Future tuning requires first removing the case from sealed holdout and creating a public regression candidate artifact.
- The current role of these cases is to preserve a real holdout signal around over-conversion guard behavior.
