<!-- zhtw:disable -->
# Holdout Maintainer Confirmation Packet - batch7 miss classification

Generated: `2026-07-10`

This packet is sanitized. It lists only case IDs and metadata requiring maintainer confirmation; sealed values are omitted.

## Summary

- Total review cases: 24
- Public regression candidate cases: 17
- Expected recheck cases: 7
- No immediate question: 26
- Gemini policy passed: True

## Review Cases

### blind-it-0138

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `request_identifier_terminology_gap`
- Flags: []

### blind-it-0140

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `api_return_terminology_gap`
- Flags: []

### blind-it-0142

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `config_mapping_namespace_terminology_gap`
- Flags: ["non_idempotent_output"]

### blind-it-0145

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `message_subscriber_event_terminology_gap`
- Flags: []

### blind-it-0146

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `requires_expected_recheck`
- Priority: `P1`
- Reason code: `dependency_version_style_variant_recheck`
- Flags: ["possible_acceptable_variant"]

### blind-it-0147

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `requires_expected_recheck`
- Priority: `P1`
- Reason code: `log_aggregation_preposition_variant_recheck`
- Flags: ["possible_acceptable_variant"]

### blind-it-0148

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `requires_expected_recheck`
- Priority: `P1`
- Reason code: `object_storage_bucket_variant_recheck`
- Flags: ["possible_acceptable_variant"]

### blind-it-0150

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `adapter_field_naming_terminology_gap`
- Flags: []

### blind-it-0151

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `build_dependency_pipeline_terminology_gap`
- Flags: []

### blind-it-0152

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `failover_notification_terminology_gap`
- Flags: ["non_idempotent_output"]

### blind-it-0153

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `container_image_vulnerability_terminology_gap`
- Flags: []

### blind-it-0155

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `scheduler_instance_terminology_gap`
- Flags: ["non_idempotent_output"]

### blind-it-0156

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `migration_schema_export_terminology_gap`
- Flags: []

### blind-it-0157

- Domain: `it`
- Risk: `candidate_gap`
- Recommended action: `requires_expected_recheck`
- Priority: `P1`
- Reason code: `cli_extension_module_variant_recheck`
- Flags: ["possible_acceptable_variant"]

### blind-it-0158

- Domain: `it`
- Risk: `baseline_guard`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `readme_example_path_terminology_gap`
- Flags: []

### blind-ui-0108

- Domain: `ui`
- Risk: `candidate_gap`
- Recommended action: `requires_expected_recheck`
- Priority: `P1`
- Reason code: `filter_collapse_style_variant_recheck`
- Flags: ["possible_acceptable_variant"]

### blind-ui-0110

- Domain: `ui`
- Risk: `candidate_gap`
- Recommended action: `requires_expected_recheck`
- Priority: `P1`
- Reason code: `pagination_control_component_variant_recheck`
- Flags: ["possible_acceptable_variant"]

### blind-ui-0118

- Domain: `ui`
- Risk: `candidate_gap`
- Recommended action: `requires_expected_recheck`
- Priority: `P1`
- Reason code: `search_focus_record_variant_recheck`
- Flags: ["possible_acceptable_variant"]

### blind-ui-0119

- Domain: `ui`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `notification_card_support_terminology_gap`
- Flags: []

### blind-ui-0123

- Domain: `ui`
- Risk: `baseline_guard`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `reviewed_traditional_button_guard_gap`
- Flags: ["non_idempotent_output"]

### blind-llm-0083

- Domain: `llm`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `code_block_terminology_gap`
- Flags: []

### blind-llm-0085

- Domain: `llm`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `conversation_history_message_terminology_gap`
- Flags: []

### blind-formal-0084

- Domain: `formal`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `board_resolution_pass_wording_gap`
- Flags: []

### blind-social-0079

- Domain: `social`
- Risk: `candidate_gap`
- Recommended action: `move_to_public_regression_candidate`
- Priority: `P2`
- Reason code: `shared_album_terminology_gap`
- Flags: ["non_idempotent_output"]

## No Immediate Question

blind-llm-0026, blind-llm-0028, blind-formal-0029, blind-social-0025, blind-social-0026, blind-it-0083, blind-ui-0060, blind-ui-0061, blind-llm-0043, blind-llm-0044, blind-formal-0043, blind-formal-0044, blind-formal-0045, blind-formal-0046, blind-social-0042, blind-social-0043, blind-social-0044, blind-high-risk-0026, blind-high-risk-0027, blind-it-0108, blind-ui-0081, blind-high-risk-0039, blind-it-0131, blind-ui-0102, blind-high-risk-0053, blind-high-risk-0058