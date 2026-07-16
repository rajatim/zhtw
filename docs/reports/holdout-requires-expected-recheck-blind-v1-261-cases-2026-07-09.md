<!-- zhtw:disable -->
# Holdout Requires-Expected Recheck - blind-v1 261-case Sanity

Generated: `2026-07-09`

This report summarizes Codex first-pass recommendations for 16 sealed recheck cases. It intentionally omits expected values, acceptable variants, input text, converter outputs, and benchmark rows.

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

- Current sealed cases: 261
- Current accepted: 207
- Current misses: 54
- Recheck cases: 16
- Recommended acceptable variant candidates: 9
- Recommended move to public regression candidate: 5
- Recommended keep strict primary expected: 2
- Hypothetical accepted after acceptable confirmations only: 216 / 261 (0.8276)

The hypothetical number is not an updated benchmark result. Private expected remains unchanged until maintainer confirmation.

## Recommendations

| Case | Domain | Risk | Recommendation | Priority | Reason | Flags |
|------|--------|------|----------------|----------|--------|-------|
| `blind-it-0080` | `it` | `over_conversion_guard` | `maintainer_confirm_move_to_public_regression_candidate` | `P2` | `clear_example_term_and_graph_variant_gap_after_recheck` | `over_conversion_guard`, `graph_variant`, `multi_term_gap`, `gemini_policy_followup` |
| `blind-it-0081` | `it` | `over_conversion_guard` | `maintainer_confirm_add_acceptable_variant` | `P2` | `valid_variable_name_term_variant` | `over_conversion_guard`, `it_term_variant`, `gemini_policy_followup` |
| `blind-it-0082` | `it` | `over_conversion_guard` | `maintainer_confirm_move_to_public_regression_candidate` | `P2` | `clear_project_term_gap_after_recheck` | `over_conversion_guard`, `it_term_gap`, `gemini_policy_followup` |
| `blind-it-0084` | `it` | `over_conversion_guard` | `maintainer_confirm_move_to_public_regression_candidate` | `P1` | `clear_localization_term_gap_after_recheck` | `over_conversion_guard`, `it_term_gap`, `ui_term_gap`, `gemini_policy_followup` |
| `blind-it-0085` | `it` | `baseline_guard` | `maintainer_confirm_add_acceptable_variant` | `P2` | `valid_cli_command_term_variant` | `style_variant`, `it_term_variant` |
| `blind-ui-0048` | `ui` | `candidate_gap` | `maintainer_confirm_keep_strict_primary_expected` | `P2` | `preserve_strict_ui_click_action_wording_signal` | `style_variant`, `strict_ui_wording` |
| `blind-ui-0059` | `ui` | `candidate_gap` | `maintainer_confirm_add_acceptable_variant` | `P3` | `valid_breadcrumb_navigation_term_variant` | `style_variant`, `ui_term_variant` |
| `blind-llm-0035` | `llm` | `candidate_gap` | `maintainer_confirm_add_acceptable_variant` | `P2` | `valid_ai_generation_term_variant` | `style_variant`, `llm_term_variant` |
| `blind-llm-0042` | `llm` | `over_conversion_guard` | `maintainer_confirm_add_acceptable_variant` | `P2` | `valid_variable_name_term_variant` | `over_conversion_guard`, `it_term_variant`, `gemini_policy_followup` |
| `blind-formal-0035` | `formal` | `candidate_gap` | `maintainer_confirm_keep_strict_primary_expected` | `P2` | `preserve_formal_identity_term_signal` | `formal_term_recheck`, `strict_formal_wording` |
| `blind-formal-0036` | `formal` | `candidate_gap` | `maintainer_confirm_add_acceptable_variant` | `P2` | `valid_record_graph_variant` | `formal_term_variant`, `style_variant` |
| `blind-formal-0041` | `formal` | `candidate_gap` | `maintainer_confirm_add_acceptable_variant` | `P2` | `valid_send_term_variant` | `formal_term_variant`, `style_variant` |
| `blind-high-risk-0022` | `high_risk` | `candidate_gap` | `maintainer_confirm_add_acceptable_variant` | `P1` | `valid_high_risk_finance_send_term_variant_needs_confirmation` | `high_risk`, `finance_term_variant` |
| `blind-high-risk-0024` | `high_risk` | `candidate_gap` | `maintainer_confirm_add_acceptable_variant` | `P1` | `valid_high_risk_medical_patient_term_variant_needs_confirmation` | `high_risk`, `medical_term_variant` |
| `blind-high-risk-0028` | `high_risk` | `over_conversion_guard` | `maintainer_confirm_move_to_public_regression_candidate` | `P1` | `clear_high_risk_finance_note_term_gap_after_recheck` | `high_risk`, `formal_term_gap`, `over_conversion_guard`, `gemini_policy_followup` |
| `blind-high-risk-0030` | `high_risk` | `baseline_guard` | `maintainer_confirm_move_to_public_regression_candidate` | `P1` | `clear_high_risk_medical_audit_record_term_gap_after_recheck` | `high_risk`, `formal_term_gap`, `it_term_gap`, `gemini_policy_followup` |

## Notes

- `maintainer_confirm_add_acceptable_variant` is a recommendation only; it does not update private expected.
- `maintainer_confirm_move_to_public_regression_candidate` still requires removing the case from sealed holdout before any converter or dictionary tuning.
- `maintainer_confirm_keep_strict_primary_expected` remains sealed and must not be used for converter or dictionary tuning.
- The private maintainer packet is stored in `/tmp` and intentionally not committed.
