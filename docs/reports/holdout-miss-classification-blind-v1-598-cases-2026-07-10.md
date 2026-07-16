<!-- zhtw:disable -->
# Holdout Miss Classification - blind-v1 598 cases

Generated: `2026-07-10`

This report is sanitized. It contains case ids and metadata only; sealed inputs, expected values, acceptable variants, converter outputs, and benchmark rows are omitted.

## Summary

- Current sealed cases: 598
- Current accepted: 549
- Current misses: 49
- Accepted accuracy: 0.918060200669
- Classified misses: 49
- By action: {"keep_as_holdout_signal": 30, "move_to_public_regression_candidate": 15, "requires_expected_recheck": 4}
- By priority: {"P1": 5, "P2": 44}
- Idempotency follow-up cases: 2

## Review Required

- `blind-it-0165`: move_to_public_regression_candidate / P2 / `cli_support_config_terminology_gap` / it, candidate_gap
- `blind-it-0166`: move_to_public_regression_candidate / P2 / `tenant_identifier_terminology_gap` / it, candidate_gap
- `blind-it-0167`: requires_expected_recheck / P1 / `log_sampling_style_variant_recheck` / it, candidate_gap
- `blind-it-0168`: move_to_public_regression_candidate / P2 / `audit_event_terminology_gap` / it, candidate_gap
- `blind-it-0169`: move_to_public_regression_candidate / P2 / `migration_script_support_terminology_gap` / it, candidate_gap
- `blind-it-0171`: move_to_public_regression_candidate / P2 / `webhook_signature_generation_terminology_gap` / it, candidate_gap
- `blind-it-0173`: move_to_public_regression_candidate / P2 / `package_manager_dependency_terminology_gap` / it, candidate_gap
- `blind-it-0174`: move_to_public_regression_candidate / P2 / `dev_server_file_reload_terminology_gap` / it, candidate_gap
- `blind-it-0175`: requires_expected_recheck / P1 / `observability_platform_variant_recheck` / it, candidate_gap
- `blind-it-0177`: move_to_public_regression_candidate / P2 / `object_storage_access_policy_terminology_gap` / it, candidate_gap
- `blind-ui-0130`: move_to_public_regression_candidate / P2 / `avatar_crop_terminology_gap` / ui, candidate_gap
- `blind-ui-0131`: move_to_public_regression_candidate / P2 / `saved_filter_current_view_terminology_gap` / ui, candidate_gap
- `blind-ui-0136`: move_to_public_regression_candidate / P2 / `dialog_save_draft_terminology_gap` / ui, candidate_gap
- `blind-ui-0138`: move_to_public_regression_candidate / P2 / `pin_sidebar_item_terminology_gap` / ui, candidate_gap
- `blind-ui-0139`: move_to_public_regression_candidate / P2 / `search_highlight_match_terminology_gap` / ui, candidate_gap
- `blind-llm-0097`: requires_expected_recheck / P1 / `placeholder_term_variant_recheck` / llm, candidate_gap
- `blind-llm-0098`: move_to_public_regression_candidate / P2 / `vector_database_document_chunk_terminology_gap` / llm, candidate_gap
- `blind-formal-0101`: move_to_public_regression_candidate / P1 / `identity_document_formal_term_gap` / formal, candidate_gap
- `blind-social-0095`: requires_expected_recheck / P1 / `group_message_send_variant_recheck` / social, candidate_gap

## No Immediate Question

- `blind-llm-0026`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / llm, over_conversion_guard
- `blind-llm-0028`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / llm, over_conversion_guard
- `blind-formal-0029`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / formal, over_conversion_guard
- `blind-social-0025`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / social, over_conversion_guard
- `blind-social-0026`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / social, over_conversion_guard
- `blind-it-0083`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / it, over_conversion_guard
- `blind-ui-0060`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / ui, over_conversion_guard
- `blind-ui-0061`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / ui, over_conversion_guard
- `blind-llm-0043`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / llm, over_conversion_guard
- `blind-llm-0044`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / llm, over_conversion_guard
- `blind-formal-0043`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / formal, over_conversion_guard
- `blind-formal-0044`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / formal, over_conversion_guard
- `blind-formal-0045`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / formal, over_conversion_guard
- `blind-formal-0046`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / formal, over_conversion_guard
- `blind-social-0042`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / social, over_conversion_guard
- `blind-social-0043`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / social, over_conversion_guard
- `blind-social-0044`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / social, over_conversion_guard
- `blind-high-risk-0026`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / high_risk, over_conversion_guard
- `blind-high-risk-0027`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / high_risk, over_conversion_guard
- `blind-it-0108`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / it, over_conversion_guard
- `blind-ui-0081`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / ui, over_conversion_guard
- `blind-high-risk-0039`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / high_risk, over_conversion_guard
- `blind-it-0131`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / it, over_conversion_guard
- `blind-ui-0102`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / ui, over_conversion_guard
- `blind-high-risk-0053`: keep_as_holdout_signal / `high_risk_private_holdout_signal` / high_risk, candidate_gap
- `blind-high-risk-0058`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / high_risk, over_conversion_guard
- `blind-ui-0147`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / ui, over_conversion_guard
- `blind-formal-0105`: keep_as_holdout_signal / `preserve_existing_taiwan_term_over_conversion_guard` / formal, over_conversion_guard
- `blind-high-risk-0064`: keep_as_holdout_signal / `high_risk_private_holdout_signal` / high_risk, candidate_gap
- `blind-high-risk-0068`: keep_as_holdout_signal / `high_risk_baseline_guard_private_signal` / high_risk, baseline_guard
