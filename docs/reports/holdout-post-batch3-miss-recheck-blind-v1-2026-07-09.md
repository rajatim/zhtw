<!-- zhtw:disable -->
# Holdout Post-Batch3 Miss Recheck - blind-v1

Generated: `2026-07-09`

This report summarizes Codex first-pass recommendations for the 17 post-batch3 sealed misses. It intentionally omits expected values, acceptable variants, input text, converter outputs, and benchmark rows.

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
- Current accepted: 144
- Current misses: 17
- Maintainer review required: 11
- Recommended acceptable variant candidates: 11
- Keep as sealed holdout signal: 6
- Non-idempotent misses: 0
- Hypothetical accepted after maintainer confirmation: 155 / 161 (0.9627)

The hypothetical number is not an updated benchmark result. Private expected remains unchanged until maintainer confirmation.

## Recommendations

| Case | Domain | Risk | Recommendation | Priority | Reason | Flags |
|------|--------|------|----------------|----------|--------|-------|
| `blind-formal-0023` | `formal` | `candidate_gap` | `maintainer_confirm_add_acceptable_variant` | `P2` | `valid_record_graph_variant` | `style_variant` |
| `blind-formal-0029` | `formal` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `preserve_taipei_formal_over_conversion_signal` | `over_conversion_guard`, `graph_variant` |
| `blind-high-risk-0011` | `high_risk` | `candidate_gap` | `maintainer_confirm_add_acceptable_variant` | `P1` | `valid_medical_patient_term_variant_needs_confirmation` | `high_risk`, `medical_term_variant` |
| `blind-high-risk-0012` | `high_risk` | `candidate_gap` | `maintainer_confirm_add_acceptable_variant` | `P1` | `valid_finance_delivery_verb_variant_needs_confirmation` | `high_risk`, `finance_term_variant` |
| `blind-it-0036` | `it` | `candidate_gap` | `maintainer_confirm_add_acceptable_variant` | `P2` | `valid_debug_mode_term_variant` | `it_term_variant` |
| `blind-it-0055` | `it` | `over_conversion_guard` | `maintainer_confirm_add_acceptable_variant` | `P1` | `valid_taipei_and_field_name_variant_needs_confirmation` | `over_conversion_guard`, `multi_term_variant` |
| `blind-llm-0017` | `llm` | `candidate_gap` | `maintainer_confirm_add_acceptable_variant` | `P2` | `valid_ai_generation_term_variant` | `ai_domain_variant` |
| `blind-llm-0023` | `llm` | `candidate_gap` | `maintainer_confirm_add_acceptable_variant` | `P2` | `valid_ai_generation_term_variant` | `ai_domain_variant` |
| `blind-llm-0026` | `llm` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `preserve_taiwan_graph_variant_over_conversion_signal` | `over_conversion_guard`, `graph_variant` |
| `blind-llm-0028` | `llm` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `preserve_taipei_graph_variant_over_conversion_signal` | `over_conversion_guard`, `graph_variant` |
| `blind-social-0024` | `social` | `candidate_gap` | `maintainer_confirm_add_acceptable_variant` | `P2` | `valid_send_to_chat_variant_needs_confirmation` | `style_variant`, `daily_usage_variant` |
| `blind-social-0025` | `social` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `preserve_taiwan_place_name_over_conversion_signal` | `over_conversion_guard`, `graph_variant` |
| `blind-social-0026` | `social` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `preserve_taiwan_traditional_text_over_conversion_signal` | `over_conversion_guard`, `graph_variant` |
| `blind-ui-0011` | `ui` | `baseline_guard` | `keep_as_holdout_signal` | `P2` | `preserve_strict_ui_click_action_wording_signal` | `style_variant`, `strict_ui_wording` |
| `blind-ui-0014` | `ui` | `candidate_gap` | `maintainer_confirm_add_acceptable_variant` | `P2` | `valid_current_state_term_variant` | `style_variant` |
| `blind-ui-0016` | `ui` | `candidate_gap` | `maintainer_confirm_add_acceptable_variant` | `P2` | `valid_page_position_term_variant` | `style_variant` |
| `blind-ui-0039` | `ui` | `over_conversion_guard` | `maintainer_confirm_add_acceptable_variant` | `P2` | `valid_replace_verb_variant` | `style_variant`, `over_conversion_guard` |

## Notes

- `maintainer_confirm_add_acceptable_variant` is a recommendation only; it does not update private expected.
- `keep_as_holdout_signal` remains sealed and must not be used for converter or dictionary tuning.
- The private maintainer packet is stored in `/tmp` and intentionally not committed.
