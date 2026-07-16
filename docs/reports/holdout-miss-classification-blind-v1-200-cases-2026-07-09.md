<!-- zhtw:disable -->
# Holdout Miss Classification - blind-v1 200-case Sanity

Generated: `2026-07-09`

This report classifies private benchmark misses using local sealed rows, but it intentionally omits expected values, acceptable variants, inputs, converter outputs, and benchmark rows.

## Summary

- Current sealed cases: 200
- Current accepted: 144
- Current misses: 56
- Classified misses: 56
- Move to public regression candidate: 39
- Requires expected/acceptable recheck: 11
- Keep as holdout signal: 6
- Non-idempotent misses: 4

## Policy

- Do not tune from sealed cases directly.
- Cases marked `move_to_public_regression_candidate` must be removed from sealed holdout before any converter or dictionary change.
- Cases marked `requires_expected_recheck` do not update private expected in this report.
- Cases marked `keep_as_holdout_signal` remain sealed and must not be used for tuning.
- Gemini reviewed sanitized classification metadata only and reported policy consistent with 0 follow-up findings; sealed values were not sent.

## Action Counts

- `keep_as_holdout_signal`: 6
- `move_to_public_regression_candidate`: 39
- `requires_expected_recheck`: 11

## Case Classifications

| Case | Domain | Risk | Action | Priority | Reason | Flags |
|------|--------|------|--------|----------|--------|-------|
| `blind-ui-0011` | `ui` | `baseline_guard` | `keep_as_holdout_signal` | `P2` | `preserve_ui_click_wording_signal` | `previous_holdout_signal`, `style_variant` |
| `blind-ui-0014` | `ui` | `candidate_gap` | `requires_expected_recheck` | `P2` | `possible_current_term_acceptable_variant` | `style_variant` |
| `blind-ui-0016` | `ui` | `candidate_gap` | `requires_expected_recheck` | `P3` | `possible_page_position_acceptable_variant` | `style_variant` |
| `blind-formal-0005` | `formal` | `baseline_guard` | `move_to_public_regression_candidate` | `P2` | `clear_taiwan_formal_time_term_gap` |  |
| `blind-it-0026` | `it` | `candidate_gap` | `move_to_public_regression_candidate` | `P1` | `clear_taiwan_it_api_config_gap` | `multi_term_gap` |
| `blind-it-0027` | `it` | `candidate_gap` | `move_to_public_regression_candidate` | `P2` | `clear_taiwan_it_storage_term_gap` |  |
| `blind-it-0028` | `it` | `candidate_gap` | `move_to_public_regression_candidate` | `P1` | `clear_taiwan_cli_log_file_gap` | `multi_term_gap` |
| `blind-it-0029` | `it` | `candidate_gap` | `move_to_public_regression_candidate` | `P2` | `clear_taiwan_dependency_term_gap` |  |
| `blind-it-0033` | `it` | `candidate_gap` | `move_to_public_regression_candidate` | `P1` | `clear_taiwan_project_localization_gap` | `multi_term_gap` |
| `blind-it-0034` | `it` | `candidate_gap` | `move_to_public_regression_candidate` | `P2` | `clear_taiwan_delivery_verb_gap` | `non_idempotent_output` |
| `blind-it-0035` | `it` | `candidate_gap` | `move_to_public_regression_candidate` | `P1` | `clear_taiwan_queue_term_gap` |  |
| `blind-it-0036` | `it` | `candidate_gap` | `requires_expected_recheck` | `P2` | `possible_debug_mode_acceptable_variant` | `style_variant` |
| `blind-it-0037` | `it` | `candidate_gap` | `move_to_public_regression_candidate` | `P1` | `clear_taiwan_background_session_gap` | `multi_term_gap` |
| `blind-it-0038` | `it` | `candidate_gap` | `move_to_public_regression_candidate` | `P1` | `clear_over_conversion_only_character_gap` | `single_character_error` |
| `blind-it-0041` | `it` | `candidate_gap` | `move_to_public_regression_candidate` | `P2` | `clear_taiwan_api_term_gap` |  |
| `blind-it-0042` | `it` | `candidate_gap` | `move_to_public_regression_candidate` | `P1` | `clear_database_table_term_gap` | `over_conversion` |
| `blind-it-0044` | `it` | `candidate_gap` | `move_to_public_regression_candidate` | `P2` | `clear_code_hook_term_gap` |  |
| `blind-it-0047` | `it` | `candidate_gap` | `move_to_public_regression_candidate` | `P1` | `clear_callback_signature_term_gap` | `multi_term_gap` |
| `blind-it-0049` | `it` | `candidate_gap` | `move_to_public_regression_candidate` | `P1` | `clear_certificate_alert_term_gap` | `multi_term_gap` |
| `blind-it-0050` | `it` | `candidate_gap` | `move_to_public_regression_candidate` | `P2` | `clear_request_body_term_gap` |  |
| `blind-it-0053` | `it` | `over_conversion_guard` | `move_to_public_regression_candidate` | `P2` | `clear_program_term_gap` |  |
| `blind-it-0054` | `it` | `over_conversion_guard` | `move_to_public_regression_candidate` | `P2` | `clear_project_name_term_gap` |  |
| `blind-it-0055` | `it` | `over_conversion_guard` | `requires_expected_recheck` | `P1` | `taipei_variant_and_field_name_mix_needs_recheck` | `over_conversion_guard`, `possible_expected_variant` |
| `blind-it-0056` | `it` | `over_conversion_guard` | `move_to_public_regression_candidate` | `P1` | `clear_localization_term_gap` | `over_conversion_guard` |
| `blind-it-0057` | `it` | `over_conversion_guard` | `move_to_public_regression_candidate` | `P1` | `clear_repository_term_gap_with_preserve_variant` | `over_conversion_guard`, `multi_term_gap` |
| `blind-it-0058` | `it` | `baseline_guard` | `move_to_public_regression_candidate` | `P1` | `clear_build_checksum_term_gap` | `multi_term_gap` |
| `blind-it-0059` | `it` | `baseline_guard` | `move_to_public_regression_candidate` | `P1` | `clear_cache_storage_term_gap` | `multi_term_gap` |
| `blind-it-0060` | `it` | `baseline_guard` | `move_to_public_regression_candidate` | `P1` | `clear_access_permission_term_gap` |  |
| `blind-ui-0028` | `ui` | `candidate_gap` | `move_to_public_regression_candidate` | `P2` | `clear_ui_save_term_gap` |  |
| `blind-ui-0029` | `ui` | `candidate_gap` | `move_to_public_regression_candidate` | `P1` | `clear_ui_file_term_gap` |  |
| `blind-ui-0030` | `ui` | `candidate_gap` | `move_to_public_regression_candidate` | `P1` | `clear_ui_email_term_gap` |  |
| `blind-ui-0034` | `ui` | `candidate_gap` | `move_to_public_regression_candidate` | `P1` | `clear_ui_submit_term_gap` |  |
| `blind-ui-0035` | `ui` | `candidate_gap` | `move_to_public_regression_candidate` | `P2` | `clear_application_term_gap` |  |
| `blind-ui-0036` | `ui` | `candidate_gap` | `move_to_public_regression_candidate` | `P2` | `clear_ui_drag_term_gap` |  |
| `blind-ui-0038` | `ui` | `candidate_gap` | `move_to_public_regression_candidate` | `P1` | `clear_identity_character_gap` |  |
| `blind-ui-0039` | `ui` | `over_conversion_guard` | `requires_expected_recheck` | `P2` | `possible_replace_verb_acceptable_variant` | `style_variant`, `over_conversion_guard` |
| `blind-ui-0040` | `ui` | `over_conversion_guard` | `move_to_public_regression_candidate` | `P1` | `clear_simplified_character_leak_with_preserve_variant` | `non_idempotent_output`, `over_conversion_guard` |
| `blind-llm-0017` | `llm` | `candidate_gap` | `requires_expected_recheck` | `P2` | `possible_generation_term_acceptable_variant` | `ai_domain_variant` |
| `blind-llm-0023` | `llm` | `candidate_gap` | `requires_expected_recheck` | `P2` | `possible_generation_term_acceptable_variant` | `ai_domain_variant` |
| `blind-llm-0024` | `llm` | `candidate_gap` | `move_to_public_regression_candidate` | `P2` | `clear_meeting_minutes_term_gap` |  |
| `blind-llm-0026` | `llm` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `preserve_taiwan_variant_over_conversion_signal` | `over_conversion_guard` |
| `blind-llm-0027` | `llm` | `over_conversion_guard` | `move_to_public_regression_candidate` | `P2` | `clear_variable_name_term_gap` |  |
| `blind-llm-0028` | `llm` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `preserve_taipei_variant_over_conversion_signal` | `over_conversion_guard` |
| `blind-formal-0023` | `formal` | `candidate_gap` | `requires_expected_recheck` | `P2` | `possible_record_term_acceptable_variant` | `style_variant` |
| `blind-formal-0024` | `formal` | `candidate_gap` | `move_to_public_regression_candidate` | `P1` | `clear_data_quality_term_gap` |  |
| `blind-formal-0025` | `formal` | `candidate_gap` | `move_to_public_regression_candidate` | `P1` | `clear_formal_preposition_character_gap` | `non_idempotent_output` |
| `blind-formal-0028` | `formal` | `over_conversion_guard` | `move_to_public_regression_candidate` | `P1` | `clear_over_conversion_variant_character_gap` | `over_conversion_guard` |
| `blind-formal-0029` | `formal` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `preserve_taipei_variant_over_conversion_signal` | `over_conversion_guard` |
| `blind-social-0019` | `social` | `candidate_gap` | `move_to_public_regression_candidate` | `P1` | `clear_photo_album_term_gap` | `non_idempotent_output` |
| `blind-social-0024` | `social` | `candidate_gap` | `requires_expected_recheck` | `P2` | `possible_send_verb_acceptable_variant` | `style_variant` |
| `blind-social-0025` | `social` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `preserve_taiwan_variant_over_conversion_signal` | `over_conversion_guard` |
| `blind-social-0026` | `social` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `preserve_taiwan_variant_over_conversion_signal` | `over_conversion_guard` |
| `blind-high-risk-0011` | `high_risk` | `candidate_gap` | `requires_expected_recheck` | `P1` | `possible_medical_patient_term_acceptable_variant` | `high_risk`, `possible_expected_variant` |
| `blind-high-risk-0012` | `high_risk` | `candidate_gap` | `requires_expected_recheck` | `P1` | `possible_finance_delivery_verb_acceptable_variant` | `high_risk`, `style_variant` |
| `blind-high-risk-0016` | `high_risk` | `over_conversion_guard` | `move_to_public_regression_candidate` | `P1` | `clear_high_risk_legal_contract_term_gap` | `high_risk`, `over_conversion_guard` |
| `blind-high-risk-0019` | `high_risk` | `baseline_guard` | `move_to_public_regression_candidate` | `P1` | `clear_high_risk_identity_character_gap` | `high_risk` |
