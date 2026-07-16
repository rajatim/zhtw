<!-- zhtw:disable -->
# Holdout Miss Classification - blind-v1 683 cases

Generated: `2026-07-12`

This report is sanitized. It contains case ids and metadata only, not sealed inputs, expected values, acceptable variants, converter outputs, or benchmark rows.

## Summary

- current_sealed_cases: 683
- current_accepted: 630
- current_misses: 53
- accepted_accuracy: 0.922401171303
- classified_misses: 53
- idempotency_followup_cases: 3
- expected_recheck_cases: 6
- safe_public_candidate_cases: 16
- holdout_signal_cases: 31

## By Action

{"keep_as_holdout_signal": 31, "move_to_public_regression_candidate": 16, "requires_expected_recheck": 6}

## Review Queue

Cases below require maintainer confirmation before any private expected update or sealed-to-public move.

### blind-it-0189

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `requires_expected_recheck`
- Priority: `P1`
- Reason code: `mapping_term_variant_recheck`
- Flags: `possible_acceptable_variant`

### blind-it-0190

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P1`
- Reason code: `queue_priority_message_terminology_gap`
- Flags: `non_idempotent_output`

### blind-it-0195

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `repository_terminology_gap`
- Flags: ``

### blind-it-0197

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `requires_expected_recheck`
- Priority: `P1`
- Reason code: `service_discovery_return_instance_variant_recheck`
- Flags: `possible_acceptable_variant`

### blind-it-0200

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P1`
- Reason code: `event_bus_terminology_gap`
- Flags: `non_idempotent_output`

### blind-it-0201

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `background_job_terminology_gap`
- Flags: ``

### blind-it-0202

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `requires_expected_recheck`
- Priority: `P1`
- Reason code: `timestamp_term_variant_recheck`
- Flags: `possible_acceptable_variant`

### blind-it-0203

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `shared_config_template_terminology_gap`
- Flags: ``

### blind-it-0206

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `requires_expected_recheck`
- Priority: `P1`
- Reason code: `load_balancer_node_orthography_variant_recheck`
- Flags: `possible_acceptable_variant`

### blind-it-0208

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `queue_message_terminology_gap`
- Flags: ``

### blind-it-0209

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `monitoring_backend_terminology_gap`
- Flags: ``

### blind-it-0210

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `runtime_config_source_terminology_gap`
- Flags: ``

### blind-ui-0148

- Domain: `ui`
- Risk: `candidate_gap`
- Recommended action: `requires_expected_recheck`
- Priority: `P1`
- Reason code: `refresh_button_punctuation_style_variant_recheck`
- Flags: `possible_acceptable_variant`

### blind-ui-0150

- Domain: `ui`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `save_draft_status_label_terminology_gap`
- Flags: ``

### blind-ui-0157

- Domain: `ui`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `sidebar_collapse_icon_terminology_gap`
- Flags: ``

### blind-ui-0160

- Domain: `ui`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `table_column_drag_terminology_gap`
- Flags: ``

### blind-ui-0164

- Domain: `ui`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `current_view_navigation_terminology_gap`
- Flags: ``

### blind-ui-0166

- Domain: `ui`
- Risk: `candidate_gap`
- Recommended action: `requires_expected_recheck`
- Priority: `P1`
- Reason code: `archived_item_tab_variant_recheck`
- Flags: `possible_acceptable_variant`

### blind-llm-0116

- Domain: `llm`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `merge_document_chunk_character_gap`
- Flags: ``

### blind-llm-0122

- Domain: `llm`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `system_message_terminology_gap`
- Flags: ``

### blind-formal-0115

- Domain: `formal`
- Risk: `baseline_guard`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P1`
- Reason code: `formal_standard_character_gap`
- Flags: `baseline_guard_miss`

### blind-formal-0116

- Domain: `formal`
- Risk: `baseline_guard`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P1`
- Reason code: `formal_contact_window_overconversion_gap`
- Flags: `baseline_guard_miss`

## No Immediate Maintainer Queue

The remaining keep-as-holdout-signal cases are retained as private pressure signal and must not be used for tuning while sealed.
