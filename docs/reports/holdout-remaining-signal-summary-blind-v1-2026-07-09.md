<!-- zhtw:disable -->
# Holdout Remaining Signal Summary - blind-v1

Generated: `2026-07-09`

This report summarizes the six remaining sealed holdout signals after post-batch3 maintainer recheck. It intentionally omits expected values, acceptable variants, input text, converter outputs, and benchmark rows.

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

- Current sealed cases: 161
- Current accepted: 155
- Current misses: 6
- Remaining signal cases: 6
- Converter or dictionary updated: `false`
- Private expected updated in this step: `false`
- Non-idempotent signal cases: 0

## Signal Cases

| Case | Domain | Risk | Signal category | Reason | Flags |
|------|--------|------|-----------------|--------|-------|
| `blind-formal-0029` | `formal` | `over_conversion_guard` | `graph_variant_over_conversion_signal` | `preserve_taipei_formal_over_conversion_signal` | `over_conversion_guard`, `graph_variant` |
| `blind-llm-0026` | `llm` | `over_conversion_guard` | `graph_variant_over_conversion_signal` | `preserve_taiwan_graph_variant_over_conversion_signal` | `over_conversion_guard`, `graph_variant` |
| `blind-llm-0028` | `llm` | `over_conversion_guard` | `graph_variant_over_conversion_signal` | `preserve_taipei_graph_variant_over_conversion_signal` | `over_conversion_guard`, `graph_variant` |
| `blind-social-0025` | `social` | `over_conversion_guard` | `graph_variant_over_conversion_signal` | `preserve_taiwan_place_name_over_conversion_signal` | `over_conversion_guard`, `graph_variant` |
| `blind-social-0026` | `social` | `over_conversion_guard` | `graph_variant_over_conversion_signal` | `preserve_taiwan_traditional_text_over_conversion_signal` | `over_conversion_guard`, `graph_variant` |
| `blind-ui-0011` | `ui` | `baseline_guard` | `strict_ui_wording_signal` | `preserve_strict_ui_click_action_wording_signal` | `style_variant`, `strict_ui_wording` |

## Policy Notes

- These cases remain sealed and must not be used for converter or dictionary tuning.
- Future tuning requires first removing the case from sealed holdout and creating a public regression candidate artifact.
- The current role of these cases is to preserve a real holdout signal around strict UI wording and graph-variant over-conversion behavior.
