# Holdout Miss Classification - blind-v1 338-case sanity

Generated: 2026-07-09

This sanitized report omits sealed input, expected, actual, and acceptable values.

## Summary

- Current sealed cases: 338
- Current accepted: 301
- Current misses: 37
- Accepted accuracy: 0.8905
- Classified misses: 37
- By action: {"keep_as_holdout_signal": 22, "move_to_public_regression_candidate": 12, "requires_expected_recheck": 3}
- By priority: {"P1": 3, "P2": 34}
- Safe public candidate cases: 12
- Expected recheck cases: 3
- Holdout signal cases: 22

## Classifications

| ID | Domain | Risk | Action | Priority | Reason |
|---|---|---|---|---|---|
| `blind-llm-0026` | `llm` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `preserve_existing_taiwan_term_over_conversion_guard` |
| `blind-llm-0028` | `llm` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `preserve_existing_taipei_term_over_conversion_guard` |
| `blind-formal-0029` | `formal` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `formal_taipei_name_over_conversion_guard` |
| `blind-social-0025` | `social` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `social_taiwan_place_name_over_conversion_guard` |
| `blind-social-0026` | `social` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `existing_taiwan_friend_phrase_over_conversion_guard` |
| `blind-it-0083` | `it` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `taichung_address_over_conversion_guard` |
| `blind-ui-0060` | `ui` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `brand_store_name_over_conversion_guard` |
| `blind-ui-0061` | `ui` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `user_custom_label_over_conversion_guard` |
| `blind-llm-0043` | `llm` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `example_output_taiwan_postal_term_over_conversion_guard` |
| `blind-llm-0044` | `llm` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `user_provided_taipei_address_over_conversion_guard` |
| `blind-formal-0043` | `formal` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `formal_taipei_legal_name_over_conversion_guard` |
| `blind-formal-0044` | `formal` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `proper_name_taiwan_university_over_conversion_guard` |
| `blind-formal-0045` | `formal` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `raw_taichung_address_over_conversion_guard` |
| `blind-formal-0046` | `formal` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `contract_identifier_tainan_over_conversion_guard` |
| `blind-social-0042` | `social` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `nickname_taiwan_phrase_over_conversion_guard` |
| `blind-social-0043` | `social` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `photo_caption_taipei_phrase_over_conversion_guard` |
| `blind-social-0044` | `social` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `social_hashtag_taichung_over_conversion_guard` |
| `blind-high-risk-0026` | `high_risk` | `over_conversion_guard` | `keep_as_holdout_signal` | `P1` | `medical_facility_name_over_conversion_guard` |
| `blind-high-risk-0027` | `high_risk` | `over_conversion_guard` | `keep_as_holdout_signal` | `P1` | `contract_company_name_over_conversion_guard` |
| `blind-it-0088` | `it` | `candidate_gap` | `move_to_public_regression_candidate` | `P2` | `platform_term_should_remain_platform_not_taiwan_variant` |
| `blind-it-0089` | `it` | `candidate_gap` | `move_to_public_regression_candidate` | `P2` | `identity_token_and_refresh_terms` |
| `blind-it-0090` | `it` | `candidate_gap` | `requires_expected_recheck` | `P2` | `debug_log_term_variant` |
| `blind-it-0092` | `it` | `candidate_gap` | `move_to_public_regression_candidate` | `P2` | `support_and_default_terms` |
| `blind-it-0094` | `it` | `candidate_gap` | `requires_expected_recheck` | `P2` | `rollback_term_variant` |
| `blind-it-0095` | `it` | `candidate_gap` | `move_to_public_regression_candidate` | `P2` | `application_and_readonly_terms` |
| `blind-it-0096` | `it` | `candidate_gap` | `move_to_public_regression_candidate` | `P2` | `api_return_term` |
| `blind-it-0097` | `it` | `candidate_gap` | `move_to_public_regression_candidate` | `P2` | `pipeline_and_skip_terms` |
| `blind-it-0105` | `it` | `candidate_gap` | `move_to_public_regression_candidate` | `P2` | `configuration_volume_terms` |
| `blind-it-0108` | `it` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `node_name_taipei_over_conversion_guard` |
| `blind-ui-0070` | `ui` | `candidate_gap` | `move_to_public_regression_candidate` | `P2` | `ui_support_and_filter_terms` |
| `blind-ui-0073` | `ui` | `candidate_gap` | `requires_expected_recheck` | `P2` | `pagination_control_component_variant` |
| `blind-ui-0074` | `ui` | `candidate_gap` | `move_to_public_regression_candidate` | `P2` | `table_column_header_terms` |
| `blind-ui-0079` | `ui` | `candidate_gap` | `move_to_public_regression_candidate` | `P2` | `message_term_in_notification_center` |
| `blind-ui-0081` | `ui` | `over_conversion_guard` | `keep_as_holdout_signal` | `P2` | `example_account_surrounding_text_with_identifier_guard` |
| `blind-ui-0087` | `ui` | `baseline_guard` | `move_to_public_regression_candidate` | `P2` | `qr_code_spacing_and_term` |
| `blind-llm-0051` | `llm` | `candidate_gap` | `move_to_public_regression_candidate` | `P2` | `llm_tool_return_term` |
| `blind-high-risk-0039` | `high_risk` | `over_conversion_guard` | `keep_as_holdout_signal` | `P1` | `medical_attachment_code_and_taipei_guard` |

## Follow-up

- Run Gemini policy review on this sanitized classification report.
- Ask maintainer to confirm public-regression candidates before removing them from sealed holdout.
- Do not tune dictionary entries from keep_as_holdout_signal or requires_expected_recheck cases.
