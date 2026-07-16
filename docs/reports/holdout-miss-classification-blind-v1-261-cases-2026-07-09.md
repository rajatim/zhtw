<!-- zhtw:disable -->
# Holdout Miss Classification - blind-v1 261-case Sanity

Generated: `2026-07-09`

This report contains sanitized classification metadata only. It omits inputs, expected values, acceptable variants, zhtw outputs, and benchmark rows.

## Summary

- Current sealed cases: 261
- Current accepted: 207
- Current misses: 54
- Classified misses: 54
- Move to public regression candidate: 18
- Requires expected/acceptable recheck: 16
- Keep as holdout signal: 20
- Idempotency follow-up cases: 2

## Codex Follow-Up

- Revised 7 cases from `move_to_public_regression_candidate` to `requires_expected_recheck` after Gemini policy findings.

## By Domain

- `formal`: keep_as_holdout_signal=5, move_to_public_regression_candidate=1, requires_expected_recheck=3
- `high_risk`: keep_as_holdout_signal=2, requires_expected_recheck=4
- `it`: keep_as_holdout_signal=1, move_to_public_regression_candidate=8, requires_expected_recheck=5
- `llm`: keep_as_holdout_signal=4, move_to_public_regression_candidate=1, requires_expected_recheck=2
- `social`: keep_as_holdout_signal=5, move_to_public_regression_candidate=4
- `ui`: keep_as_holdout_signal=3, move_to_public_regression_candidate=4, requires_expected_recheck=2

## By Risk

- `baseline_guard`: keep_as_holdout_signal=1, move_to_public_regression_candidate=1, requires_expected_recheck=2
- `candidate_gap`: move_to_public_regression_candidate=17, requires_expected_recheck=8
- `over_conversion_guard`: keep_as_holdout_signal=19, requires_expected_recheck=6

## Cases

### blind-ui-0011

- Domain: `ui`
- Risk: `baseline_guard`
- Issue tags: `regional_term, ui_term`
- Action: `keep_as_holdout_signal`
- Reason category: `preserve_ui_click_wording_signal`
- Priority: `P2`
- Flags: `previous_holdout_signal, style_variant`
- Expected source: `human_adjudication`
- Expected disagreement: `true`
- Idempotent: `true`
- Next step: `keep_in_sealed_holdout_and_do_not_tune_from_this_case`

### blind-llm-0026

- Domain: `llm`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, over_conversion`
- Action: `keep_as_holdout_signal`
- Reason category: `preserve_taiwan_graph_variant_over_conversion_signal`
- Priority: `P2`
- Flags: `previous_holdout_signal, over_conversion_guard, graph_variant`
- Expected source: `human_adjudication`
- Expected disagreement: `true`
- Idempotent: `true`
- Next step: `keep_in_sealed_holdout_and_do_not_tune_from_this_case`

### blind-llm-0028

- Domain: `llm`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, over_conversion`
- Action: `keep_as_holdout_signal`
- Reason category: `preserve_taipei_graph_variant_over_conversion_signal`
- Priority: `P2`
- Flags: `previous_holdout_signal, over_conversion_guard, graph_variant`
- Expected source: `human_adjudication`
- Expected disagreement: `true`
- Idempotent: `true`
- Next step: `keep_in_sealed_holdout_and_do_not_tune_from_this_case`

### blind-formal-0029

- Domain: `formal`
- Risk: `over_conversion_guard`
- Issue tags: `formal_term, regional_term, over_conversion`
- Action: `keep_as_holdout_signal`
- Reason category: `preserve_taipei_legal_name_graph_variant_signal`
- Priority: `P2`
- Flags: `previous_holdout_signal, over_conversion_guard, graph_variant`
- Expected source: `human_adjudication`
- Expected disagreement: `true`
- Idempotent: `true`
- Next step: `keep_in_sealed_holdout_and_do_not_tune_from_this_case`

### blind-social-0025

- Domain: `social`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, over_conversion`
- Action: `keep_as_holdout_signal`
- Reason category: `preserve_taiwan_place_name_graph_variant_signal`
- Priority: `P2`
- Flags: `previous_holdout_signal, over_conversion_guard, graph_variant`
- Expected source: `human_adjudication`
- Expected disagreement: `true`
- Idempotent: `true`
- Next step: `keep_in_sealed_holdout_and_do_not_tune_from_this_case`

### blind-social-0026

- Domain: `social`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, over_conversion`
- Action: `keep_as_holdout_signal`
- Reason category: `preserve_existing_traditional_taiwan_graph_variant_signal`
- Priority: `P2`
- Flags: `previous_holdout_signal, over_conversion_guard, graph_variant`
- Expected source: `human_adjudication`
- Expected disagreement: `true`
- Idempotent: `true`
- Next step: `keep_in_sealed_holdout_and_do_not_tune_from_this_case`

### blind-it-0063

- Domain: `it`
- Risk: `candidate_gap`
- Issue tags: `it_term, formal_term, regional_term`
- Action: `move_to_public_regression_candidate`
- Reason category: `clear_api_return_and_audit_log_term_gap`
- Priority: `P1`
- Flags: `multi_term_gap`
- Expected source: `human_adjudication`
- Expected disagreement: `true`
- Idempotent: `true`
- Next step: `remove_from_sealed_holdout_before_any_converter_or_dictionary_tuning`

### blind-it-0064

- Domain: `it`
- Risk: `candidate_gap`
- Issue tags: `it_term, regional_term`
- Action: `move_to_public_regression_candidate`
- Reason category: `clear_request_body_term_gap`
- Priority: `P1`
- Flags: `it_term_gap`
- Expected source: `human_adjudication`
- Expected disagreement: `true`
- Idempotent: `true`
- Next step: `remove_from_sealed_holdout_before_any_converter_or_dictionary_tuning`

### blind-it-0067

- Domain: `it`
- Risk: `candidate_gap`
- Issue tags: `it_term, regional_term`
- Action: `move_to_public_regression_candidate`
- Reason category: `clear_api_return_term_gap`
- Priority: `P1`
- Flags: `it_term_gap`
- Expected source: `human_adjudication`
- Expected disagreement: `true`
- Idempotent: `true`
- Next step: `remove_from_sealed_holdout_before_any_converter_or_dictionary_tuning`

### blind-it-0069

- Domain: `it`
- Risk: `candidate_gap`
- Issue tags: `it_term, regional_term`
- Action: `move_to_public_regression_candidate`
- Reason category: `clear_hook_term_gap`
- Priority: `P2`
- Flags: `it_term_gap`
- Expected source: `human_adjudication`
- Expected disagreement: `true`
- Idempotent: `true`
- Next step: `remove_from_sealed_holdout_before_any_converter_or_dictionary_tuning`

### blind-it-0070

- Domain: `it`
- Risk: `candidate_gap`
- Issue tags: `it_term, regional_term`
- Action: `move_to_public_regression_candidate`
- Reason category: `clear_configuration_mapping_term_gap`
- Priority: `P1`
- Flags: `it_term_gap, idempotency_followup`
- Expected source: `human_adjudication`
- Expected disagreement: `true`
- Idempotent: `false`
- Next step: `remove_from_sealed_holdout_before_any_converter_or_dictionary_tuning`

### blind-it-0073

- Domain: `it`
- Risk: `candidate_gap`
- Issue tags: `it_term, regional_term`
- Action: `move_to_public_regression_candidate`
- Reason category: `clear_file_checksum_term_gap`
- Priority: `P1`
- Flags: `it_term_gap`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `remove_from_sealed_holdout_before_any_converter_or_dictionary_tuning`

### blind-it-0076

- Domain: `it`
- Risk: `candidate_gap`
- Issue tags: `it_term, regional_term`
- Action: `move_to_public_regression_candidate`
- Reason category: `clear_access_key_and_generate_term_gap`
- Priority: `P1`
- Flags: `multi_term_gap`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `remove_from_sealed_holdout_before_any_converter_or_dictionary_tuning`

### blind-it-0080

- Domain: `it`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, it_term, over_conversion`
- Action: `requires_expected_recheck`
- Reason category: `over_conversion_guard_with_example_term_requires_recheck`
- Priority: `P2`
- Flags: `over_conversion_guard, graph_variant, multi_term_gap, gemini_policy_followup`
- Expected source: `human_adjudication`
- Expected disagreement: `true`
- Idempotent: `true`
- Next step: `perform_private_expected_or_acceptable_recheck_before_changing_dataset`

### blind-it-0081

- Domain: `it`
- Risk: `over_conversion_guard`
- Issue tags: `it_term, over_conversion, regional_term`
- Action: `requires_expected_recheck`
- Reason category: `over_conversion_guard_with_variable_name_term_requires_recheck`
- Priority: `P2`
- Flags: `over_conversion_guard, it_term_gap, gemini_policy_followup`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `perform_private_expected_or_acceptable_recheck_before_changing_dataset`

### blind-it-0082

- Domain: `it`
- Risk: `over_conversion_guard`
- Issue tags: `it_term, over_conversion, regional_term`
- Action: `requires_expected_recheck`
- Reason category: `over_conversion_guard_with_project_code_term_requires_recheck`
- Priority: `P2`
- Flags: `over_conversion_guard, it_term_gap, gemini_policy_followup`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `perform_private_expected_or_acceptable_recheck_before_changing_dataset`

### blind-it-0083

- Domain: `it`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, over_conversion, it_term`
- Action: `keep_as_holdout_signal`
- Reason category: `preserve_taichung_graph_variant_over_conversion_signal`
- Priority: `P2`
- Flags: `over_conversion_guard, graph_variant`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `keep_in_sealed_holdout_and_do_not_tune_from_this_case`

### blind-it-0084

- Domain: `it`
- Risk: `over_conversion_guard`
- Issue tags: `ui_term, it_term, regional_term, over_conversion`
- Action: `requires_expected_recheck`
- Reason category: `over_conversion_guard_with_localization_term_requires_recheck`
- Priority: `P1`
- Flags: `over_conversion_guard, it_term_gap, ui_term_gap, gemini_policy_followup`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `perform_private_expected_or_acceptable_recheck_before_changing_dataset`

### blind-it-0085

- Domain: `it`
- Risk: `baseline_guard`
- Issue tags: `it_term, regional_term`
- Action: `requires_expected_recheck`
- Reason category: `possible_cli_command_acceptable_variant`
- Priority: `P2`
- Flags: `style_variant, it_term_recheck`
- Expected source: `human_adjudication`
- Expected disagreement: `true`
- Idempotent: `true`
- Next step: `perform_private_expected_or_acceptable_recheck_before_changing_dataset`

### blind-it-0087

- Domain: `it`
- Risk: `baseline_guard`
- Issue tags: `it_term, regional_term`
- Action: `move_to_public_regression_candidate`
- Reason category: `clear_ci_pipeline_term_gap`
- Priority: `P1`
- Flags: `it_term_gap`
- Expected source: `human_adjudication`
- Expected disagreement: `true`
- Idempotent: `true`
- Next step: `remove_from_sealed_holdout_before_any_converter_or_dictionary_tuning`

### blind-ui-0048

- Domain: `ui`
- Risk: `candidate_gap`
- Issue tags: `ui_term, regional_term`
- Action: `requires_expected_recheck`
- Reason category: `possible_click_wording_acceptable_variant`
- Priority: `P2`
- Flags: `style_variant, ui_term_recheck`
- Expected source: `human_adjudication`
- Expected disagreement: `true`
- Idempotent: `true`
- Next step: `perform_private_expected_or_acceptable_recheck_before_changing_dataset`

### blind-ui-0049

- Domain: `ui`
- Risk: `candidate_gap`
- Issue tags: `ui_term, regional_term`
- Action: `move_to_public_regression_candidate`
- Reason category: `clear_current_page_and_save_term_gap`
- Priority: `P1`
- Flags: `ui_term_gap, multi_term_gap`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `remove_from_sealed_holdout_before_any_converter_or_dictionary_tuning`

### blind-ui-0051

- Domain: `ui`
- Risk: `candidate_gap`
- Issue tags: `ui_term, regional_term`
- Action: `move_to_public_regression_candidate`
- Reason category: `clear_drag_term_gap`
- Priority: `P1`
- Flags: `ui_term_gap`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `remove_from_sealed_holdout_before_any_converter_or_dictionary_tuning`

### blind-ui-0052

- Domain: `ui`
- Risk: `candidate_gap`
- Issue tags: `ui_term, regional_term`
- Action: `move_to_public_regression_candidate`
- Reason category: `clear_table_column_width_term_gap`
- Priority: `P1`
- Flags: `ui_term_gap`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `remove_from_sealed_holdout_before_any_converter_or_dictionary_tuning`

### blind-ui-0054

- Domain: `ui`
- Risk: `candidate_gap`
- Issue tags: `ui_term, regional_term`
- Action: `move_to_public_regression_candidate`
- Reason category: `clear_error_message_term_gap`
- Priority: `P1`
- Flags: `ui_term_gap`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `remove_from_sealed_holdout_before_any_converter_or_dictionary_tuning`

### blind-ui-0059

- Domain: `ui`
- Risk: `candidate_gap`
- Issue tags: `ui_term, regional_term`
- Action: `requires_expected_recheck`
- Reason category: `possible_breadcrumb_navigation_acceptable_variant`
- Priority: `P3`
- Flags: `style_variant, ui_term_recheck`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `perform_private_expected_or_acceptable_recheck_before_changing_dataset`

### blind-ui-0060

- Domain: `ui`
- Risk: `over_conversion_guard`
- Issue tags: `ui_term, regional_term, over_conversion`
- Action: `keep_as_holdout_signal`
- Reason category: `preserve_taipei_brand_name_graph_variant_signal`
- Priority: `P2`
- Flags: `over_conversion_guard, graph_variant`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `keep_in_sealed_holdout_and_do_not_tune_from_this_case`

### blind-ui-0061

- Domain: `ui`
- Risk: `over_conversion_guard`
- Issue tags: `ui_term, regional_term, over_conversion`
- Action: `keep_as_holdout_signal`
- Reason category: `preserve_user_label_graph_variant_and_punctuation_signal`
- Priority: `P2`
- Flags: `over_conversion_guard, graph_variant, punctuation_signal`
- Expected source: `human_adjudication`
- Expected disagreement: `true`
- Idempotent: `true`
- Next step: `keep_in_sealed_holdout_and_do_not_tune_from_this_case`

### blind-llm-0035

- Domain: `llm`
- Risk: `candidate_gap`
- Issue tags: `it_term, regional_term`
- Action: `requires_expected_recheck`
- Reason category: `possible_generate_term_acceptable_variant`
- Priority: `P2`
- Flags: `style_variant, llm_term_recheck`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `perform_private_expected_or_acceptable_recheck_before_changing_dataset`

### blind-llm-0039

- Domain: `llm`
- Risk: `candidate_gap`
- Issue tags: `it_term, regional_term`
- Action: `move_to_public_regression_candidate`
- Reason category: `clear_file_list_term_gap`
- Priority: `P1`
- Flags: `it_term_gap`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `remove_from_sealed_holdout_before_any_converter_or_dictionary_tuning`

### blind-llm-0042

- Domain: `llm`
- Risk: `over_conversion_guard`
- Issue tags: `it_term, over_conversion, regional_term`
- Action: `requires_expected_recheck`
- Reason category: `over_conversion_guard_with_variable_name_term_requires_recheck`
- Priority: `P2`
- Flags: `over_conversion_guard, it_term_gap, gemini_policy_followup`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `perform_private_expected_or_acceptable_recheck_before_changing_dataset`

### blind-llm-0043

- Domain: `llm`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, over_conversion, it_term`
- Action: `keep_as_holdout_signal`
- Reason category: `preserve_taiwan_postal_code_graph_variant_signal`
- Priority: `P2`
- Flags: `over_conversion_guard, graph_variant`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `keep_in_sealed_holdout_and_do_not_tune_from_this_case`

### blind-llm-0044

- Domain: `llm`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, over_conversion, it_term`
- Action: `keep_as_holdout_signal`
- Reason category: `preserve_taipei_user_address_graph_variant_signal`
- Priority: `P2`
- Flags: `over_conversion_guard, graph_variant`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `keep_in_sealed_holdout_and_do_not_tune_from_this_case`

### blind-formal-0034

- Domain: `formal`
- Risk: `candidate_gap`
- Issue tags: `formal_term, regional_term`
- Action: `move_to_public_regression_candidate`
- Reason category: `clear_taiwan_formal_quarter_term_gap`
- Priority: `P2`
- Flags: `formal_term_gap`
- Expected source: `human_adjudication`
- Expected disagreement: `true`
- Idempotent: `true`
- Next step: `remove_from_sealed_holdout_before_any_converter_or_dictionary_tuning`

### blind-formal-0035

- Domain: `formal`
- Risk: `candidate_gap`
- Issue tags: `formal_term, regional_term`
- Action: `requires_expected_recheck`
- Reason category: `possible_identity_term_acceptable_variant`
- Priority: `P2`
- Flags: `formal_term_recheck, style_variant`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `perform_private_expected_or_acceptable_recheck_before_changing_dataset`

### blind-formal-0036

- Domain: `formal`
- Risk: `candidate_gap`
- Issue tags: `formal_term, regional_term`
- Action: `requires_expected_recheck`
- Reason category: `possible_record_term_acceptable_variant`
- Priority: `P2`
- Flags: `formal_term_recheck, style_variant`
- Expected source: `human_adjudication`
- Expected disagreement: `true`
- Idempotent: `true`
- Next step: `perform_private_expected_or_acceptable_recheck_before_changing_dataset`

### blind-formal-0041

- Domain: `formal`
- Risk: `candidate_gap`
- Issue tags: `formal_term, regional_term`
- Action: `requires_expected_recheck`
- Reason category: `possible_send_term_acceptable_variant`
- Priority: `P2`
- Flags: `formal_term_recheck, style_variant`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `perform_private_expected_or_acceptable_recheck_before_changing_dataset`

### blind-formal-0043

- Domain: `formal`
- Risk: `over_conversion_guard`
- Issue tags: `formal_term, regional_term, over_conversion`
- Action: `keep_as_holdout_signal`
- Reason category: `preserve_taipei_law_name_graph_variant_signal`
- Priority: `P2`
- Flags: `over_conversion_guard, graph_variant`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `keep_in_sealed_holdout_and_do_not_tune_from_this_case`

### blind-formal-0044

- Domain: `formal`
- Risk: `over_conversion_guard`
- Issue tags: `formal_term, regional_term, over_conversion`
- Action: `keep_as_holdout_signal`
- Reason category: `preserve_university_name_graph_variant_signal`
- Priority: `P2`
- Flags: `over_conversion_guard, graph_variant`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `keep_in_sealed_holdout_and_do_not_tune_from_this_case`

### blind-formal-0045

- Domain: `formal`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, over_conversion, formal_term`
- Action: `keep_as_holdout_signal`
- Reason category: `preserve_taichung_address_graph_variant_signal`
- Priority: `P2`
- Flags: `over_conversion_guard, graph_variant`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `keep_in_sealed_holdout_and_do_not_tune_from_this_case`

### blind-formal-0046

- Domain: `formal`
- Risk: `over_conversion_guard`
- Issue tags: `formal_term, regional_term, over_conversion`
- Action: `keep_as_holdout_signal`
- Reason category: `preserve_contract_id_tainan_graph_variant_signal`
- Priority: `P2`
- Flags: `over_conversion_guard, graph_variant`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `keep_in_sealed_holdout_and_do_not_tune_from_this_case`

### blind-social-0034

- Domain: `social`
- Risk: `candidate_gap`
- Issue tags: `regional_term`
- Action: `move_to_public_regression_candidate`
- Reason category: `clear_shared_album_term_gap`
- Priority: `P2`
- Flags: `social_term_gap, idempotency_followup`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `false`
- Next step: `remove_from_sealed_holdout_before_any_converter_or_dictionary_tuning`

### blind-social-0036

- Domain: `social`
- Risk: `candidate_gap`
- Issue tags: `regional_term`
- Action: `move_to_public_regression_candidate`
- Reason category: `clear_social_send_to_group_term_gap`
- Priority: `P2`
- Flags: `social_term_gap`
- Expected source: `human_adjudication`
- Expected disagreement: `true`
- Idempotent: `true`
- Next step: `remove_from_sealed_holdout_before_any_converter_or_dictionary_tuning`

### blind-social-0040

- Domain: `social`
- Risk: `candidate_gap`
- Issue tags: `regional_term`
- Action: `move_to_public_regression_candidate`
- Reason category: `clear_livestream_replay_term_gap`
- Priority: `P2`
- Flags: `social_term_gap`
- Expected source: `human_adjudication`
- Expected disagreement: `true`
- Idempotent: `true`
- Next step: `remove_from_sealed_holdout_before_any_converter_or_dictionary_tuning`

### blind-social-0041

- Domain: `social`
- Risk: `candidate_gap`
- Issue tags: `regional_term`
- Action: `move_to_public_regression_candidate`
- Reason category: `clear_social_send_screenshot_term_gap`
- Priority: `P2`
- Flags: `social_term_gap`
- Expected source: `human_adjudication`
- Expected disagreement: `true`
- Idempotent: `true`
- Next step: `remove_from_sealed_holdout_before_any_converter_or_dictionary_tuning`

### blind-social-0042

- Domain: `social`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, over_conversion`
- Action: `keep_as_holdout_signal`
- Reason category: `preserve_nickname_graph_variant_signal`
- Priority: `P2`
- Flags: `over_conversion_guard, graph_variant`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `keep_in_sealed_holdout_and_do_not_tune_from_this_case`

### blind-social-0043

- Domain: `social`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, over_conversion`
- Action: `keep_as_holdout_signal`
- Reason category: `preserve_photo_caption_taipei_graph_variant_signal`
- Priority: `P2`
- Flags: `over_conversion_guard, graph_variant`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `keep_in_sealed_holdout_and_do_not_tune_from_this_case`

### blind-social-0044

- Domain: `social`
- Risk: `over_conversion_guard`
- Issue tags: `regional_term, over_conversion`
- Action: `keep_as_holdout_signal`
- Reason category: `preserve_hashtag_taichung_graph_variant_signal`
- Priority: `P2`
- Flags: `over_conversion_guard, graph_variant`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `keep_in_sealed_holdout_and_do_not_tune_from_this_case`

### blind-high-risk-0022

- Domain: `high_risk`
- Risk: `candidate_gap`
- Issue tags: `high_risk_term, formal_term, regional_term`
- Action: `requires_expected_recheck`
- Reason category: `high_risk_send_term_requires_recheck`
- Priority: `P1`
- Flags: `high_risk, formal_term_recheck`
- Expected source: `human_adjudication`
- Expected disagreement: `true`
- Idempotent: `true`
- Next step: `perform_private_expected_or_acceptable_recheck_before_changing_dataset`

### blind-high-risk-0024

- Domain: `high_risk`
- Risk: `candidate_gap`
- Issue tags: `high_risk_term, formal_term, regional_term`
- Action: `requires_expected_recheck`
- Reason category: `high_risk_patient_term_requires_recheck`
- Priority: `P1`
- Flags: `high_risk, formal_term_recheck`
- Expected source: `human_adjudication`
- Expected disagreement: `true`
- Idempotent: `true`
- Next step: `perform_private_expected_or_acceptable_recheck_before_changing_dataset`

### blind-high-risk-0026

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Issue tags: `high_risk_term, formal_term, regional_term, over_conversion`
- Action: `keep_as_holdout_signal`
- Reason category: `preserve_medical_campus_name_graph_variant_signal`
- Priority: `P1`
- Flags: `high_risk, over_conversion_guard, graph_variant`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `keep_in_sealed_holdout_and_do_not_tune_from_this_case`

### blind-high-risk-0027

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Issue tags: `high_risk_term, formal_term, regional_term, over_conversion`
- Action: `keep_as_holdout_signal`
- Reason category: `preserve_legal_branch_name_graph_variant_signal`
- Priority: `P1`
- Flags: `high_risk, over_conversion_guard, graph_variant`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `keep_in_sealed_holdout_and_do_not_tune_from_this_case`

### blind-high-risk-0028

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Issue tags: `high_risk_term, formal_term, over_conversion, regional_term`
- Action: `requires_expected_recheck`
- Reason category: `high_risk_over_conversion_guard_requires_recheck`
- Priority: `P1`
- Flags: `high_risk, formal_term_gap, over_conversion_guard, gemini_policy_followup`
- Expected source: `human_first_pass`
- Expected disagreement: `false`
- Idempotent: `true`
- Next step: `perform_private_expected_or_acceptable_recheck_before_changing_dataset`

### blind-high-risk-0030

- Domain: `high_risk`
- Risk: `baseline_guard`
- Issue tags: `high_risk_term, formal_term, it_term, regional_term`
- Action: `requires_expected_recheck`
- Reason category: `high_risk_medical_audit_record_term_requires_recheck`
- Priority: `P1`
- Flags: `high_risk, formal_term_gap, it_term_gap, gemini_policy_followup`
- Expected source: `human_adjudication`
- Expected disagreement: `true`
- Idempotent: `true`
- Next step: `perform_private_expected_or_acceptable_recheck_before_changing_dataset`
