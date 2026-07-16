<!-- zhtw:disable -->
# Holdout Expected Recheck - blind-v1

Generated: `2026-07-09`

This report summarizes the 14 expected/acceptable rechecks without publishing sealed expected values, acceptable variants, input text, converter outputs, or benchmark rows.

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

- Recheck cases: 14
- Acceptable variants added privately: 12
- Strict misses kept: 2
- Moved to public regression in this step: 0
- Accepted before recheck: 57 / 78
- Accepted after recheck: 69 / 78
- Misses after recheck: 9
- Accepted accuracy after recheck: 0.8846
- Idempotency rate after recheck: 0.9744
- Private expected sha256: `6b34d7167fc0ba16c51cb6fa8e12ab51b7bb5860783a2c0a6d0897e96afd1ff2`

## Decisions

| Case | Domain | Risk | Decision | Reason category |
|------|--------|------|----------|-----------------|
| `blind-it-0003` | it | candidate_gap | `add_acceptable_variant` | `valid_client_term_variant` |
| `blind-it-0007` | it | candidate_gap | `add_acceptable_variant` | `valid_background_task_variant` |
| `blind-it-0017` | it | candidate_gap | `add_acceptable_variant` | `valid_signature_term_variant` |
| `blind-it-0020` | it | candidate_gap | `add_acceptable_variant` | `valid_environment_term_variant` |
| `blind-it-0022` | it | candidate_gap | `add_acceptable_variant` | `valid_plugin_term_variant` |
| `blind-ui-0002` | ui | candidate_gap | `keep_strict_primary_expected` | `strict_ui_delivery_term_kept` |
| `blind-ui-0008` | ui | candidate_gap | `add_acceptable_variant` | `valid_profile_image_term_variant` |
| `blind-ui-0018` | ui | baseline_guard | `add_acceptable_variant` | `valid_collapse_term_variant` |
| `blind-llm-0002` | llm | candidate_gap | `add_acceptable_variant` | `valid_orthography_variant` |
| `blind-llm-0003` | llm | candidate_gap | `add_acceptable_variant` | `valid_ai_generation_term_variant` |
| `blind-llm-0006` | llm | over_conversion_guard | `add_acceptable_variant` | `valid_generation_term_variant` |
| `blind-llm-0012` | llm | candidate_gap | `add_acceptable_variant` | `valid_programming_statement_term_variant` |
| `blind-formal-0010` | formal | candidate_gap | `keep_strict_primary_expected` | `strict_project_term_kept` |
| `blind-formal-0012` | formal | over_conversion_guard | `add_acceptable_variant` | `valid_legal_contract_term_variant` |

## Notes

- `add_acceptable_variant` updates only the private expected file; it is not a converter or dictionary change.
- `keep_strict_primary_expected` remains a sealed holdout miss and must not be tuned unless moved out of sealed holdout first.
- Existing Codex/Gemini advisory reports were used as advisory evidence; the maintainer remains the human decision maker.
