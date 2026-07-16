<!-- zhtw:disable -->
# Holdout Remaining 40 Miss Classification - blind-v1

Generated: `2026-07-09`

This report is sanitized. Expected values, acceptable variants, input text, converter output, and full benchmark rows are intentionally omitted.

## Summary

- current_sealed_cases: 256
- current_accepted: 216
- current_misses: 40
- classified_misses: 40
- maintainer_review_required: 21
- recommended_move_to_public_regression_candidate: 17
- recommended_acceptable_variant_candidates: 2
- requires_expected_recheck: 2
- keep_as_holdout_signal: 19

## Recommendations By Case

- `blind-ui-0011`: `maintainer_confirm_add_acceptable_variant` (valid_click_verb_variant)
- `blind-llm-0026`: `keep_as_holdout_signal` (taiwan_graph_preservation_signal)
- `blind-llm-0028`: `keep_as_holdout_signal` (taipei_graph_preservation_signal)
- `blind-formal-0029`: `keep_as_holdout_signal` (taipei_legal_name_preservation_signal)
- `blind-social-0025`: `keep_as_holdout_signal` (taiwan_graph_preservation_signal)
- `blind-social-0026`: `keep_as_holdout_signal` (taiwan_graph_preservation_signal)
- `blind-it-0063`: `maintainer_confirm_move_to_public_regression_candidate` (clear_it_audit_log_term_gap)
- `blind-it-0064`: `maintainer_confirm_move_to_public_regression_candidate` (clear_it_request_body_term_gap)
- `blind-it-0067`: `maintainer_confirm_move_to_public_regression_candidate` (clear_it_return_verb_gap)
- `blind-it-0069`: `requires_expected_recheck` (hook_term_variant_requires_maintainer_confirmation)
- `blind-it-0070`: `requires_expected_recheck` (config_mapping_term_variant_requires_maintainer_confirmation)
- `blind-it-0073`: `maintainer_confirm_move_to_public_regression_candidate` (clear_it_file_term_gap)
- `blind-it-0076`: `maintainer_confirm_move_to_public_regression_candidate` (clear_it_access_key_and_generate_terms_gap)
- `blind-it-0083`: `keep_as_holdout_signal` (taichung_address_preservation_signal)
- `blind-it-0087`: `maintainer_confirm_move_to_public_regression_candidate` (clear_it_pipeline_term_gap)
- `blind-ui-0048`: `maintainer_confirm_add_acceptable_variant` (valid_click_verb_variant)
- `blind-ui-0049`: `maintainer_confirm_move_to_public_regression_candidate` (clear_ui_current_save_terms_gap)
- `blind-ui-0051`: `maintainer_confirm_move_to_public_regression_candidate` (clear_ui_drag_term_gap)
- `blind-ui-0052`: `maintainer_confirm_move_to_public_regression_candidate` (clear_ui_table_column_width_term_gap)
- `blind-ui-0054`: `maintainer_confirm_move_to_public_regression_candidate` (clear_ui_error_message_term_gap)
- `blind-ui-0060`: `keep_as_holdout_signal` (taipei_store_name_preservation_signal)
- `blind-ui-0061`: `keep_as_holdout_signal` (custom_label_preservation_signal)
- `blind-llm-0039`: `maintainer_confirm_move_to_public_regression_candidate` (clear_llm_file_list_term_gap)
- `blind-llm-0043`: `keep_as_holdout_signal` (taiwan_postal_code_preservation_signal)
- `blind-llm-0044`: `keep_as_holdout_signal` (taipei_address_preservation_signal)
- `blind-formal-0034`: `maintainer_confirm_move_to_public_regression_candidate` (clear_formal_quarter_term_gap)
- `blind-formal-0035`: `maintainer_confirm_move_to_public_regression_candidate` (clear_formal_identity_term_gap)
- `blind-formal-0043`: `keep_as_holdout_signal` (taipei_regulation_name_preservation_signal)
- `blind-formal-0044`: `keep_as_holdout_signal` (university_name_preservation_signal)
- `blind-formal-0045`: `keep_as_holdout_signal` (taichung_address_preservation_signal)
- `blind-formal-0046`: `keep_as_holdout_signal` (contract_code_preservation_signal)
- `blind-social-0034`: `maintainer_confirm_move_to_public_regression_candidate` (clear_social_album_term_gap)
- `blind-social-0036`: `maintainer_confirm_move_to_public_regression_candidate` (clear_social_send_to_group_term_gap)
- `blind-social-0040`: `maintainer_confirm_move_to_public_regression_candidate` (clear_social_replay_term_gap)
- `blind-social-0041`: `maintainer_confirm_move_to_public_regression_candidate` (clear_social_send_to_person_term_gap)
- `blind-social-0042`: `keep_as_holdout_signal` (nickname_preservation_signal)
- `blind-social-0043`: `keep_as_holdout_signal` (caption_trip_name_preservation_signal)
- `blind-social-0044`: `keep_as_holdout_signal` (hashtag_preservation_signal)
- `blind-high-risk-0026`: `keep_as_holdout_signal` (medical_facility_name_preservation_signal)
- `blind-high-risk-0027`: `keep_as_holdout_signal` (contract_branch_name_preservation_signal)

## Gemini Policy Review

- Status: `completed`
- Reviewer: `gemini_vertex`
- Model: `gemini-2.5-flash`
- Report: `docs/reports/holdout-gemini-policy-review-remaining-40-miss-classification-blind-v1-2026-07-09.json`
- Policy consistent: `true`
- Needs Codex follow-up: 0
- Sealed values seen by Gemini: `false`
