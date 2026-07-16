<!-- zhtw:disable -->
# Holdout Remaining Miss Classification - blind-v1

Generated: `2026-07-09`

This report classifies the remaining 9 sealed misses without publishing sealed expected values, acceptable variants, input text, converter outputs, or benchmark rows.

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

- Current sealed cases: 78
- Current accepted: 69
- Current misses: 9
- Move to public regression candidate: 5
- Keep as sealed holdout signal: 4
- Idempotency follow-up cases: 1
- Strict after expected recheck cases: 2

## Domain Breakdown

| Domain | Move to public candidate | Keep holdout |
|--------|--------------------------|--------------|
| formal | 2 | 1 |
| it | 1 | 0 |
| social | 1 | 0 |
| ui | 1 | 3 |

## Case Classifications

| Case | Domain | Risk | Action | Reason category | Priority | Flags |
|------|--------|------|--------|-----------------|----------|-------|
| `blind-it-0014` | it | candidate_gap | `move_to_public_regression_candidate` | `clear_passed_check_phrase_gap` | P2 |  |
| `blind-ui-0002` | ui | candidate_gap | `move_to_public_regression_candidate` | `clear_ui_message_delivery_gap_with_idempotency_followup` | P1 | `idempotency_followup`, `strict_after_expected_recheck` |
| `blind-ui-0011` | ui | baseline_guard | `keep_as_holdout_signal` | `preserve_duplicate_click_action_signal` | P2 |  |
| `blind-ui-0014` | ui | candidate_gap | `keep_as_holdout_signal` | `preserve_current_state_wording_signal` | P2 |  |
| `blind-ui-0016` | ui | candidate_gap | `keep_as_holdout_signal` | `preserve_layout_position_wording_signal` | P2 |  |
| `blind-formal-0005` | formal | baseline_guard | `keep_as_holdout_signal` | `preserve_date_period_style_signal` | P2 |  |
| `blind-formal-0006` | formal | candidate_gap | `move_to_public_regression_candidate` | `clear_formal_record_terminology_gap` | P1 |  |
| `blind-formal-0010` | formal | candidate_gap | `move_to_public_regression_candidate` | `clear_formal_project_terminology_gap_after_strict_recheck` | P1 | `strict_after_expected_recheck` |
| `blind-social-0015` | social | candidate_gap | `move_to_public_regression_candidate` | `clear_social_media_playback_terminology_gap` | P2 |  |

## Notes

- `move_to_public_regression_candidate` is not permission to tune directly. Remove the case from sealed holdout first, create the public candidate artifact, then add conservative regression protection before any converter or dictionary change.
- `keep_as_holdout_signal` cases remain sealed and must not be used for tuning.
- This report uses existing Codex/Gemini advisory artifacts as supporting evidence; it does not call a converter or LLM to generate expected values.
