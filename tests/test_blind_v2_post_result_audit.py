"""Governance tests for the private Blind-v2 post-result audit."""

from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "benchmarks/accuracy/blind-v2.post-result-audit-ledger-event.schema.json"
PROTOCOL = ROOT / "benchmarks/accuracy/blind-v2.post-result-audit-protocol-v1.json"


def test_post_result_audit_protocol_keeps_score_immutable_and_rows_private() -> None:
    protocol = json.loads(PROTOCOL.read_text(encoding="utf-8"))

    assert protocol["scope"] == "all_zhtw_misses"
    assert protocol["review_order"] == [
        "codex_first_pass",
        "agy_independent",
        "codex_synthesis",
        "maintainer_decision",
    ]
    assert "Aggregate counts only" in protocol["publication"]
    assert "immutable" in protocol["score_policy"]


def test_post_result_audit_ledger_requires_private_rows_and_no_tuning() -> None:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    event = {
        "version": 1,
        "dataset": "blind-v2",
        "audit_id": "audit-1",
        "event": "audit_started",
        "recorded_at": "2026-07-31T00:00:00Z",
        "operator": "tim",
        "reason": "post-result audit",
        "source_run_id": "blind-v2-run-3-attempt-1",
        "source_report_sha256": "a" * 64,
        "inputs_sha256": "b" * 64,
        "expected_sha256": "c" * 64,
        "zhtw_git_sha": "d" * 40,
        "audit_protocol_sha256": "e" * 64,
        "detailed_rows_read": True,
        "case_level_artifacts_private": True,
        "result_tuning_prohibited": True,
        "exit_status": None,
        "findings_summary_sha256": None,
    }

    assert list(Draft202012Validator(schema).iter_errors(event)) == []
    event["case_level_artifacts_private"] = False
    assert list(Draft202012Validator(schema).iter_errors(event))


def test_post_result_audit_private_paths_are_gitignored() -> None:
    paths = (
        ROOT / "benchmarks/accuracy/private/blind-v2.post-result-audit-ledger.jsonl",
        ROOT / "benchmarks/accuracy/private/post-result-audit-v1/packet-001.json",
    )
    for path in paths:
        relative = path.relative_to(ROOT)
        assert relative.parts[:3] == ("benchmarks", "accuracy", "private")
