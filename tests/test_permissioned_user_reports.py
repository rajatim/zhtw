"""Tests for permissioned Blind-v2 user-report intake."""
# zhtw:disable  # 測試 input 必須保持簡體

from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any

import pytest

from scripts.import_blind_v2_source_pilot import parse_permissioned_user_reports
from scripts.validate_permissioned_user_reports import (
    detect_sensitive_data,
    validate_collection,
)

ROOT = Path(__file__).resolve().parents[1]
COLLECTION = (
    ROOT / "benchmarks" / "accuracy" / "sources" / "permissioned-user-report-batch-001.json"
)
ISSUE_FORM = ROOT / ".github" / "ISSUE_TEMPLATE" / "permissioned-user-report.yml"
CONSENT_VERSION = "permissioned-user-report-v1"


def report_case(index: int) -> dict[str, Any]:
    return {
        "id": f"report-{index:04d}",
        "input": f"请检查第 {index} 个设置项目。",
        "submitted_at": "2026-07-23T12:00:00+08:00",
        "issue_url": f"https://github.com/rajatim/zhtw/issues/{1000 + index}",
        "consent": {
            "policy_version": CONSENT_VERSION,
            "cc0_applied": True,
            "rights_confirmed": True,
            "public_redistribution_confirmed": True,
            "no_sensitive_data_confirmed": True,
        },
        "intake_review": {
            "reviewer": "tim",
            "reviewed_at": "2026-07-23T13:00:00+08:00",
            "decision": "accepted",
            "issue_body_sha256": "a" * 64,
        },
    }


def collection(*, status: str = "ready_for_import", count: int = 100) -> dict[str, Any]:
    return {
        "version": 1,
        "id": "permissioned-user-report-batch-001",
        "batch_number": 1,
        "created_date": "2026-07-23",
        "status": status,
        "source_class": "permissioned",
        "target_count": 100,
        "input_only": True,
        "converter_output_used": False,
        "consent_policy_version": CONSENT_VERSION,
        "redaction_policy": "reject_and_resubmit_no_automatic_mutation",
        "cases": [report_case(index) for index in range(1, count + 1)],
    }


def test_committed_collection_is_valid_empty_input_only_template() -> None:
    source = json.loads(COLLECTION.read_text(encoding="utf-8"))

    assert validate_collection(source) == []
    assert source["status"] == "collecting"
    assert source["target_count"] == 100
    assert source["cases"] == []
    assert source["input_only"] is True
    assert source["converter_output_used"] is False


def test_collection_must_be_ready_before_import() -> None:
    source = collection(status="collecting", count=0)

    assert validate_collection(source, require_ready=True) == [
        "$.status: collection is not ready_for_import"
    ]
    with pytest.raises(ValueError, match="not ready_for_import"):
        parse_permissioned_user_reports(source["id"], json.dumps(source).encode())


def test_ready_collection_requires_exactly_100_cases() -> None:
    source = collection(count=99)

    errors = validate_collection(source)

    assert any("too short" in error for error in errors)


def test_ready_collection_imports_100_input_only_rows() -> None:
    source = collection()

    rows = parse_permissioned_user_reports(source["id"], json.dumps(source).encode())

    assert len(rows) == 100
    assert rows[0] == ("permissioned_user_report", "report-0001", "请检查第 1 个设置项目。")
    assert validate_collection(source, require_ready=True) == []


def test_duplicate_normalized_input_is_rejected() -> None:
    source = collection()
    source["cases"][1]["input"] = "  请检查第 1 个设置项目。\n"

    errors = validate_collection(source)

    assert any("duplicate normalized input with report-0001" in error for error in errors)


def test_forbidden_expected_field_is_rejected() -> None:
    source = collection()
    source["cases"][0]["expected"] = "請檢查第一個設定項目。"

    errors = validate_collection(source)

    assert any("expected" in error for error in errors)


@pytest.mark.parametrize(
    ("text", "finding"),
    [
        ("联络邮箱：alice@example.com", "email"),
        ("电话：0912-345-678", "labelled_phone_number"),
        ("服务器是 192.168.1.2", "ipv4_address"),
        ("api_key=abcd1234", "secret_assignment"),
        ("https://example.com/path?token=abc", "url_query_or_fragment"),
        ("账号：A123456", "labelled_personal_identifier"),
        ("-----BEGIN PRIVATE KEY-----", "private_key"),
    ],
)
def test_sensitive_data_patterns_are_rejected(text: str, finding: str) -> None:
    assert finding in detect_sensitive_data(text)

    source = collection()
    source["cases"][0]["input"] = text
    assert any(
        f"sensitive pattern detected: {finding}" in error for error in validate_collection(source)
    )


@pytest.mark.parametrize(
    "text",
    [
        "请勿把密码写在配置文件中。",
        "版本为 2026.07.23。",
        "请访问 https://example.com/docs。",
    ],
)
def test_benign_security_and_technical_text_is_not_overblocked(text: str) -> None:
    assert detect_sensitive_data(text) == []


def test_source_id_must_match_manifest_id() -> None:
    source = collection()

    with pytest.raises(ValueError, match="does not match manifest"):
        parse_permissioned_user_reports(
            "permissioned-user-report-batch-002", json.dumps(source).encode()
        )


def test_source_id_must_match_batch_number() -> None:
    source = collection()
    source["batch_number"] = 2

    assert any("does not match batch_number 2" in error for error in validate_collection(source))


def test_case_ids_must_be_contiguous() -> None:
    source = collection()
    source["cases"][1]["id"] = "report-0101"

    assert any(
        "expected contiguous id report-0002" in error for error in validate_collection(source)
    )


def test_issue_form_requires_all_consent_confirmations() -> None:
    form = ISSUE_FORM.read_text(encoding="utf-8")

    assert form.count("required: true") == 6
    assert "https://github.com/rajatim/zhtw/blob/main/docs/benchmark/" in form
    assert "CC0 1.0 Universal" in form
    assert "不得附上繁體答案或任何轉換器輸出" in form


def test_false_consent_cannot_pass_schema() -> None:
    source = collection()
    changed = copy.deepcopy(source)
    changed["cases"][0]["consent"]["rights_confirmed"] = False

    assert any("True was expected" in error for error in validate_collection(changed))
