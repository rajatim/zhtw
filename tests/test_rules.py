"""Contract tests for schema-v2 rule records."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from zhtw.rules import (
    ReviewStatus,
    RuleCatalogError,
    RuleClass,
    RuleRecord,
    SourceLocale,
    TrustLevel,
    legacy_rule_id,
    legacy_rule_record,
    validate_rule_catalog,
)

SCHEMA = Path("src/zhtw/data/schemas/rule-v2.schema.json")


def _pending_mapping() -> dict[str, object]:
    return {
        "id": "rule:cn:it:software",
        "source_locale": "cn",
        "source": "\u8f6f\u4ef6",
        "target": "\u8edf\u9ad4",
        "rule_class": "custom",
        "domain": "it",
        "trust_level": "custom",
        "priority": 0,
        "context": ["developer-tools"],
        "evidence_source": None,
        "review_status": "pending",
    }


def test_legacy_rule_id_is_deterministic_and_path_independent() -> None:
    source = "\u8f6f\u4ef6"
    target = "\u8edf\u9ad4"

    first = legacy_rule_id(SourceLocale.CN, source, target, RuleClass.CURATED)
    rebuilt = legacy_rule_id("cn", source, target, "curated")

    assert first == rebuilt
    assert first.startswith("legacy:cn:curated:")


def test_legacy_rule_id_changes_with_target_or_rule_class() -> None:
    source = "\u8f6f\u4ef6"
    original = legacy_rule_id("cn", source, "\u8edf\u9ad4", "curated")

    assert legacy_rule_id("cn", source, "\u8edf\u4ef6", "curated") != original
    assert legacy_rule_id("cn", source, "\u8edf\u9ad4", "custom") != original


def test_legacy_record_is_approved_descriptive_metadata() -> None:
    record = legacy_rule_record(
        source_locale="cn",
        source="\u8f6f\u4ef6",
        target="\u8edf\u9ad4",
        rule_class="curated",
        domain="it",
        evidence_source="src/zhtw/data/terms/cn/it.json",
    )

    assert record.review_status is ReviewStatus.APPROVED
    assert record.trust_level is TrustLevel.CURATED
    assert record.to_mapping()["context"] == []


def test_rule_record_round_trip() -> None:
    value = _pending_mapping()

    record = RuleRecord.from_mapping(value)

    assert record.to_mapping() == value


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("source_locale", "sg"),
        ("rule_class", "automatic"),
        ("domain", "unknown"),
        ("trust_level", "unverified"),
        ("review_status", "released"),
    ],
)
def test_rule_record_rejects_unknown_enum_values(field: str, value: str) -> None:
    payload = _pending_mapping()
    payload[field] = value

    with pytest.raises(RuleCatalogError):
        RuleRecord.from_mapping(payload)


def test_rule_record_rejects_unknown_fields() -> None:
    payload = _pending_mapping()
    payload["path"] = "must-not-affect-id.json"

    with pytest.raises(RuleCatalogError, match="unknown rule fields"):
        RuleRecord.from_mapping(payload)


def test_approved_rule_requires_evidence() -> None:
    payload = _pending_mapping()
    payload["review_status"] = "approved"

    with pytest.raises(RuleCatalogError, match="require evidence_source"):
        RuleRecord.from_mapping(payload)


def test_catalog_rejects_same_id_with_different_content() -> None:
    first = RuleRecord.from_mapping(_pending_mapping())
    changed_payload = _pending_mapping()
    changed_payload["target"] = "\u8edf\u4ef6"
    second = RuleRecord.from_mapping(changed_payload)

    with pytest.raises(RuleCatalogError, match="different content"):
        validate_rule_catalog([first, second])


def test_catalog_collapses_exact_duplicate() -> None:
    record = RuleRecord.from_mapping(_pending_mapping())

    assert validate_rule_catalog([record, record]) == (record,)


def test_json_schema_accepts_pending_rule() -> None:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)

    errors = list(
        Draft202012Validator(schema).iter_errors(
            {"schema_version": 2, "rules": [_pending_mapping()]}
        )
    )

    assert errors == []


def test_json_schema_rejects_unknown_field_and_approved_rule_without_evidence() -> None:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    payload = _pending_mapping()
    payload["review_status"] = "approved"
    payload["unexpected"] = True

    errors = list(
        Draft202012Validator(schema).iter_errors({"schema_version": 2, "rules": [payload]})
    )

    assert len(errors) == 2
