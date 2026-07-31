"""Tests for the aggregate Blind-v2 post-result audit report."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts.audit_benchmark_publication import find_sensitive_values
from scripts.build_blind_v2_post_result_audit_report import build_outputs


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")


def review(
    case_id: str,
    *,
    severity: str,
    category: str,
    actual_acceptable: bool,
) -> dict[str, object]:
    return {
        "id": case_id,
        "severity": severity,
        "category": category,
        "expected_valid": True,
        "actual_acceptable": actual_acceptable,
        "confidence": "high",
        "rationale": "Synthetic test decision.",
    }


@pytest.fixture
def private_audit(tmp_path: Path) -> Path:
    cases = [
        {
            "id": "case-1",
            "domain": "ui_i18n",
            "risk": "candidate_gap",
            "input": "input-1",
            "expected": "reference-1",
            "acceptable": [],
            "actual": "actual-1",
        },
        {
            "id": "case-2",
            "domain": "formal_news",
            "risk": "baseline_guard",
            "input": "input-2",
            "expected": "reference-2",
            "acceptable": [],
            "actual": "actual-2",
        },
    ]
    write_json(tmp_path / "manifest.json", {"total_cases": 3, "misses": 2})
    write_json(tmp_path / "packet-001.json", {"cases": cases})
    codex = [
        review(
            "case-1",
            severity="P2",
            category="regional_wording",
            actual_acceptable=False,
        ),
        review(
            "case-2",
            severity="none",
            category="acceptable_variant",
            actual_acceptable=True,
        ),
    ]
    agy = [
        codex[0],
        review(
            "case-2",
            severity="P2",
            category="regional_wording",
            actual_acceptable=False,
        ),
    ]
    synthesis = {
        **codex[1],
        "decision_source": "codex",
        "needs_maintainer": True,
    }
    write_json(tmp_path / "codex/review-001.json", {"cases": codex})
    write_json(tmp_path / "agy/review-001.json", {"cases": agy})
    write_json(tmp_path / "synthesis/review-001.json", {"cases": [synthesis]})
    return tmp_path


def test_audit_report_has_complete_private_review_coverage(private_audit: Path) -> None:
    private, public = build_outputs(private_audit)

    assert len(private["cases"]) == 2
    assert public["scope"]["audited_zhtw_misses"] == 2
    assert public["review"]["codex_first_pass_cases"] == 2
    assert public["review"]["agy_independent_cases"] == 2
    assert public["review"]["synthesis_cases"] == 1


def test_audit_report_stays_pending_until_maintainer_confirmation(
    private_audit: Path,
) -> None:
    private, public = build_outputs(private_audit)

    assert private["status"] == "pending_maintainer_confirmation"
    assert public["status"] == "pending_maintainer_confirmation"
    assert public["maintainer_queue"]["cases"] == 1
    assert public["governance"]["published_score"] == "immutable"


def test_public_audit_report_contains_no_case_level_material(private_audit: Path) -> None:
    _, public = build_outputs(private_audit)

    assert find_sensitive_values(public) == []
    assert "cases" not in public


def test_valid_maintainer_decision_completes_audit(private_audit: Path) -> None:
    write_json(
        private_audit / "maintainer-decision.json",
        {
            "version": 1,
            "audit_id": "blind-v2-post-result-audit-1",
            "decision": "approve_all_synthesis_decisions",
            "confirmed_cases": 1,
            "confirmed_by": "tim",
            "confirmed_at": "2026-07-31T01:00:00Z",
            "confirmation": "Follow the recommendation",
        },
    )

    private, public = build_outputs(private_audit)

    assert private["status"] == "completed"
    assert private["maintainer_queue"][0]["maintainer_decision"] == "approved_synthesis"
    assert public["status"] == "completed"
    assert public["maintainer_queue"]["status"] == "confirmed"
    assert public["governance"]["audit_completion"] == "maintainer_confirmed"
