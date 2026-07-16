<!-- zhtw:disable -->
# Holdout Maintainer Confirmation - Batch10 Miss Classification

Generated: `2026-07-12`

This packet is sanitized. It contains case ids and metadata only; sealed inputs, expected values, acceptable variants, converter outputs, and benchmark rows are omitted.

## Summary

- Total review cases: 20
- Public regression candidates: 16
- Expected recheck cases: 4
- No immediate question: 32
- Gemini policy passed: `true`
- Gemini classification changes recommended: 0

## Review Cases

| id | domain | risk | recommended action | reason |
|---|---|---|---|---|
| `blind-it-0217` | it | candidate_gap | `move_to_public_regression_candidate` | `it_term_public_regression` |
| `blind-it-0220` | it | candidate_gap | `move_to_public_regression_candidate` | `it_term_public_regression` |
| `blind-it-0222` | it | candidate_gap | `requires_expected_recheck` | `possible_acceptable_variant` |
| `blind-it-0223` | it | candidate_gap | `move_to_public_regression_candidate` | `it_term_public_regression` |
| `blind-it-0230` | it | candidate_gap | `move_to_public_regression_candidate` | `it_term_public_regression` |
| `blind-it-0232` | it | candidate_gap | `requires_expected_recheck` | `combined_acceptable_variant_recheck` |
| `blind-it-0235` | it | candidate_gap | `move_to_public_regression_candidate` | `it_term_public_regression` |
| `blind-it-0236` | it | candidate_gap | `move_to_public_regression_candidate` | `it_term_public_regression` |
| `blind-it-0237` | it | candidate_gap | `move_to_public_regression_candidate` | `it_term_public_regression` |
| `blind-ui-0169` | ui | candidate_gap | `move_to_public_regression_candidate` | `ui_term_public_regression` |
| `blind-ui-0170` | ui | candidate_gap | `move_to_public_regression_candidate` | `ui_term_public_regression` |
| `blind-ui-0175` | ui | candidate_gap | `move_to_public_regression_candidate` | `ui_term_public_regression` |
| `blind-ui-0181` | ui | candidate_gap | `move_to_public_regression_candidate` | `ui_term_public_regression` |
| `blind-ui-0183` | ui | candidate_gap | `move_to_public_regression_candidate` | `ui_term_public_regression` |
| `blind-ui-0184` | ui | candidate_gap | `move_to_public_regression_candidate` | `ui_term_public_regression` |
| `blind-llm-0123` | llm | candidate_gap | `requires_expected_recheck` | `semantic_term_variant_recheck` |
| `blind-llm-0137` | llm | candidate_gap | `requires_expected_recheck` | `file_message_overwrite_variant_recheck` |
| `blind-formal-0129` | formal | baseline_guard | `move_to_public_regression_candidate` | `baseline_guard_public_regression` |
| `blind-formal-0131` | formal | baseline_guard | `move_to_public_regression_candidate` | `baseline_guard_public_regression` |
| `blind-formal-0134` | formal | baseline_guard | `move_to_public_regression_candidate` | `baseline_guard_public_regression` |

## Gemini Findings

- `INFO` / `blind-ui-0147`: Case blind-ui-0147 is flagged with non-idempotent converter output. Since the recommended action is 'keep_as_holdout_signal', debugging must be conducted using independent public inputs rather than the sealed text to comply with the no-tuning policy.
- `INFO` / `blind-it-0230`: Case blind-it-0230 is non-idempotent and recommended for transition to public regression candidates. This will be safe to debug publicly only after maintainer confirmation and complete removal of the case from the sealed holdout dataset.
- `INFO` / `expected-rechecks`: Four cases (blind-it-0222, blind-it-0232, blind-llm-0123, and blind-llm-0137) properly trigger Rule 5, requiring expected value validation prior to any updates.
