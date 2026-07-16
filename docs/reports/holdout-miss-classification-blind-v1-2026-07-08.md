<!-- zhtw:disable -->
# Holdout Miss Classification - blind-v1

Generated: `2026-07-08`

This report classifies the 43 local private benchmark misses without publishing sealed expected values, converter outputs, or benchmark rows.

## Sealed Content Policy

| Field | Included |
|-------|----------|
| Expected values | No |
| Actual converter outputs | No |
| Input text | No |
| Full benchmark rows | No |
| Case IDs and metadata | Yes |

## Summary

| Metric | Value |
|--------|-------|
| Total cases | 100 |
| Accepted | 57 |
| Misses | 43 |
| Accepted accuracy | 0.5700 |
| Idempotency rate | 0.9400 |
| Non-idempotent misses | 5 |
| Accepted but non-idempotent | 1 |

## Action Counts

| Action | Cases | Next step |
|--------|-------|-----------|
| `move_to_public_regression_candidate` | 22 | `remove_from_sealed_holdout_before_any_converter_or_dictionary_tuning` |
| `keep_as_holdout_signal` | 7 | `keep_sealed_and_do_not_tune_against_this_case` |
| `requires_expected_recheck` | 14 | `maintainer_recheck_expected_or_add_acceptable_variant_before_tuning` |

## Domain Breakdown

| Domain | Move to public candidate | Keep holdout | Recheck expected |
|--------|--------------------------|--------------|------------------|
| formal | 1 | 2 | 2 |
| it | 11 | 1 | 5 |
| llm | 2 | 0 | 4 |
| social | 2 | 1 | 0 |
| ui | 6 | 3 | 3 |

## Risk Breakdown

| Risk | Move to public candidate | Keep holdout | Recheck expected |
|------|--------------------------|--------------|------------------|
| baseline_guard | 2 | 2 | 1 |
| candidate_gap | 19 | 5 | 11 |
| over_conversion_guard | 1 | 0 | 2 |

## Case Classifications

| Case | Domain | Risk | Action | Reason category | Priority | Flags |
|------|--------|------|--------|-----------------|----------|-------|
| `blind-it-0002` | it | candidate_gap | `move_to_public_regression_candidate` | `clear_taiwan_it_terminology_gap` | P1 |  |
| `blind-it-0003` | it | candidate_gap | `requires_expected_recheck` | `variant_client_terminology_recheck` | P2 |  |
| `blind-it-0005` | it | candidate_gap | `move_to_public_regression_candidate` | `clear_taiwan_it_terminology_gap` | P1 |  |
| `blind-it-0006` | it | over_conversion_guard | `move_to_public_regression_candidate` | `clear_ui_action_terminology_gap` | P1 |  |
| `blind-it-0007` | it | candidate_gap | `requires_expected_recheck` | `variant_background_task_terminology_recheck` | P2 |  |
| `blind-it-0008` | it | candidate_gap | `move_to_public_regression_candidate` | `clear_taiwan_it_terminology_gap` | P1 |  |
| `blind-it-0009` | it | candidate_gap | `move_to_public_regression_candidate` | `clear_taiwan_it_terminology_gap` | P1 |  |
| `blind-it-0010` | it | candidate_gap | `move_to_public_regression_candidate` | `clear_taiwan_it_terminology_gap` | P1 |  |
| `blind-it-0014` | it | candidate_gap | `keep_as_holdout_signal` | `preserve_holdout_duplicate_phrase_signal` | P2 |  |
| `blind-it-0015` | it | candidate_gap | `move_to_public_regression_candidate` | `clear_taiwan_it_terminology_gap` | P1 |  |
| `blind-it-0017` | it | candidate_gap | `requires_expected_recheck` | `variant_signature_terminology_recheck` | P2 |  |
| `blind-it-0020` | it | candidate_gap | `requires_expected_recheck` | `variant_environment_terminology_recheck` | P2 |  |
| `blind-it-0021` | it | candidate_gap | `move_to_public_regression_candidate` | `clear_file_archive_terminology_gap` | P1 |  |
| `blind-it-0022` | it | candidate_gap | `requires_expected_recheck` | `variant_plugin_terminology_recheck` | P2 |  |
| `blind-it-0023` | it | candidate_gap | `move_to_public_regression_candidate` | `clear_scheduler_terminology_gap` | P1 | `idempotency_followup` |
| `blind-it-0024` | it | candidate_gap | `move_to_public_regression_candidate` | `clear_taiwan_it_terminology_gap` | P1 |  |
| `blind-it-0025` | it | baseline_guard | `move_to_public_regression_candidate` | `clear_taiwan_software_wording_gap` | P1 |  |
| `blind-ui-0001` | ui | baseline_guard | `move_to_public_regression_candidate` | `clear_ui_localization_gap` | P1 |  |
| `blind-ui-0002` | ui | candidate_gap | `requires_expected_recheck` | `variant_message_delivery_terminology_recheck` | P2 | `idempotency_followup` |
| `blind-ui-0004` | ui | candidate_gap | `move_to_public_regression_candidate` | `clear_ui_localization_gap` | P1 |  |
| `blind-ui-0006` | ui | candidate_gap | `move_to_public_regression_candidate` | `clear_ui_localization_gap` | P1 |  |
| `blind-ui-0008` | ui | candidate_gap | `requires_expected_recheck` | `variant_profile_image_terminology_recheck` | P2 |  |
| `blind-ui-0009` | ui | candidate_gap | `move_to_public_regression_candidate` | `clear_ui_table_terminology_gap` | P1 |  |
| `blind-ui-0011` | ui | baseline_guard | `keep_as_holdout_signal` | `preserve_holdout_duplicate_ui_action_signal` | P2 |  |
| `blind-ui-0014` | ui | candidate_gap | `keep_as_holdout_signal` | `preserve_holdout_current_state_signal` | P2 |  |
| `blind-ui-0016` | ui | candidate_gap | `keep_as_holdout_signal` | `preserve_holdout_layout_position_signal` | P2 |  |
| `blind-ui-0018` | ui | baseline_guard | `requires_expected_recheck` | `variant_collapse_terminology_recheck` | P2 |  |
| `blind-ui-0019` | ui | candidate_gap | `move_to_public_regression_candidate` | `clear_ui_media_terminology_gap` | P1 | `idempotency_followup` |
| `blind-ui-0020` | ui | candidate_gap | `move_to_public_regression_candidate` | `clear_session_terminology_gap` | P1 |  |
| `blind-llm-0002` | llm | candidate_gap | `requires_expected_recheck` | `orthography_variant_recheck` | P3 |  |
| `blind-llm-0003` | llm | candidate_gap | `requires_expected_recheck` | `modern_ai_generation_terminology_recheck` | P2 |  |
| `blind-llm-0006` | llm | over_conversion_guard | `requires_expected_recheck` | `modern_ai_generation_terminology_recheck` | P2 |  |
| `blind-llm-0010` | llm | candidate_gap | `move_to_public_regression_candidate` | `clear_taiwan_learning_content_gap` | P1 |  |
| `blind-llm-0012` | llm | candidate_gap | `requires_expected_recheck` | `variant_programming_statement_terminology_recheck` | P2 |  |
| `blind-llm-0013` | llm | candidate_gap | `move_to_public_regression_candidate` | `clear_ai_message_terminology_gap` | P1 |  |
| `blind-formal-0003` | formal | candidate_gap | `move_to_public_regression_candidate` | `clear_formal_data_terminology_gap` | P1 | `idempotency_followup` |
| `blind-formal-0005` | formal | baseline_guard | `keep_as_holdout_signal` | `preserve_holdout_date_period_signal` | P2 |  |
| `blind-formal-0006` | formal | candidate_gap | `keep_as_holdout_signal` | `preserve_holdout_formal_record_signal` | P2 |  |
| `blind-formal-0010` | formal | candidate_gap | `requires_expected_recheck` | `variant_project_terminology_recheck` | P2 |  |
| `blind-formal-0012` | formal | over_conversion_guard | `requires_expected_recheck` | `high_risk_legal_variant_recheck` | P1 |  |
| `blind-social-0005` | social | candidate_gap | `move_to_public_regression_candidate` | `clear_social_media_terminology_gap` | P1 | `idempotency_followup` |
| `blind-social-0007` | social | candidate_gap | `move_to_public_regression_candidate` | `clear_daily_taiwan_usage_gap` | P1 |  |
| `blind-social-0015` | social | candidate_gap | `keep_as_holdout_signal` | `preserve_holdout_media_playback_signal` | P2 |  |

## Notes

- `move_to_public_regression_candidate` does not mean the converter can be tuned immediately. Remove the case from sealed holdout first, then add it to a public regression/backlog artifact with an audit note.
- `requires_expected_recheck` means the current mismatch may involve a valid Taiwan variant, style choice, or high-risk terminology choice. Do not tune from it until maintainer review updates the expected policy or acceptable variants.
- `keep_as_holdout_signal` preserves duplicate or representative failure patterns so the holdout remains useful after public tuning candidates are removed.
- Idempotency flags are case IDs only; the underlying rows remain private.
