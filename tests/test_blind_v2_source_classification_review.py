"""Tests for Blind-v2 Codex/Gemini source classification comparison."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from scripts.build_blind_v2_codex_synthesis import build_synthesis
from scripts.compare_blind_v2_source_classifications import build_comparison, render_markdown
from scripts.record_blind_v2_source_classification_decision import (
    build_decision,
    validate_decision,
)

ROOT = Path(__file__).resolve().parents[1]
ACCURACY_ROOT = ROOT / "benchmarks" / "accuracy"
PACKET_PATH = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-001.json"
CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-001-2026-07-20.json"
)
GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-001-2026-07-20.json"
)
DIFF_PATH = ROOT / "docs/reports/blind-v2-source-classification-diff-batch-001-2026-07-20.md"
DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-001-2026-07-21.json"
)
SECOND_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-002.json"
)
SECOND_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-002-2026-07-21.json"
)
SECOND_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-002-2026-07-21.json"
)
SECOND_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-002-2026-07-21.md"
)
SECOND_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-002-2026-07-21.json"
)
THIRD_PACKET_PATH = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-003.json")
THIRD_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-003-2026-07-22.json"
)
THIRD_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-003-2026-07-22.json"
)
THIRD_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-003-2026-07-22.md"
)
THIRD_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-003-2026-07-22.json"
)
FOURTH_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-004.json"
)
FOURTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-004-2026-07-23.json"
)
FOURTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-004-2026-07-23.json"
)
FOURTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-004-2026-07-23.json"
)
FOURTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-004-2026-07-23.md"
)
FOURTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-004-2026-07-23.json"
)
FIFTH_PACKET_PATH = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-005.json")
FIFTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-005-2026-07-23.json"
)
FIFTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-005-2026-07-23.json"
)
FIFTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-005-2026-07-23.json"
)
FIFTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-005-2026-07-23.md"
)
FIFTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-005-2026-07-23.json"
)
SIXTH_PACKET_PATH = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-006.json")
SIXTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-006-2026-07-23.json"
)
SIXTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-006-2026-07-23.json"
)
SIXTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-006-2026-07-23.json"
)
SIXTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-006-2026-07-23.md"
)
SIXTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-006-2026-07-23.json"
)
SEVENTH_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-007.json"
)
SEVENTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-007-2026-07-23.json"
)
SEVENTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-007-2026-07-23.json"
)
SEVENTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-007-2026-07-23.json"
)
SEVENTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-007-2026-07-23.md"
)
SEVENTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-007-2026-07-23.json"
)
EIGHTH_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-008.json"
)
EIGHTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-008-2026-07-23.json"
)
EIGHTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-008-2026-07-23.json"
)
EIGHTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-008-2026-07-23.json"
)
EIGHTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-008-2026-07-23.md"
)
EIGHTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-008-2026-07-23.json"
)
TENTH_PACKET_PATH = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-010.json")
TENTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-010-2026-07-23.json"
)
TENTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-010-2026-07-23.json"
)
TENTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-010-2026-07-23.json"
)
TENTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-010-2026-07-23.md"
)
TENTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-010-2026-07-24.json"
)
ELEVENTH_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-011.json"
)
ELEVENTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-011-2026-07-24.json"
)
ELEVENTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-011-2026-07-24.json"
)
ELEVENTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-011-2026-07-24.json"
)
ELEVENTH_ADJUSTMENTS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-adjustments-batch-011-2026-07-24.json"
)
ELEVENTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-011-2026-07-24.md"
)
ELEVENTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-011-2026-07-24.json"
)
ELEVENTH_GEMINI_CASE_IDS = {
    "vscode-loc-zh-hans-v1/entry-0e09bd6f9c17b08d",
    "vscode-loc-zh-hans-v1/entry-28115d85b27abca4",
    "vscode-loc-zh-hans-v1/entry-3bc2558a39853869",
    "vscode-loc-zh-hans-v1/entry-695847b5a35b3aea",
}
TWELFTH_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-012.json"
)
TWELFTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-012-2026-07-24.json"
)
TWELFTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-012-2026-07-24.json"
)
TWELFTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-012-2026-07-24.json"
)
TWELFTH_ADJUSTMENTS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-adjustments-batch-012-2026-07-24.json"
)
TWELFTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-012-2026-07-24.md"
)
TWELFTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-012-2026-07-24.json"
)
THIRTEENTH_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-013.json"
)
THIRTEENTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-013-2026-07-24.json"
)
THIRTEENTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-013-2026-07-24.json"
)
THIRTEENTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-013-2026-07-24.json"
)
THIRTEENTH_ADJUSTMENTS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-adjustments-batch-013-2026-07-24.json"
)
THIRTEENTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-013-2026-07-24.md"
)
THIRTEENTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-013-2026-07-24.json"
)
THIRTEENTH_GEMINI_CASE_IDS = {
    f"zhtw-project-formal-llm-semantic-v1/{case_id}"
    for case_id in (
        "formal-036",
        "llm-009",
        "llm-011",
        "llm-012",
        "llm-015",
        "llm-016",
        "llm-021",
        "llm-024",
        "llm-025",
        "llm-026",
        "llm-027",
        "llm-028",
        "llm-032",
        "llm-033",
        "llm-034",
        "llm-035",
        "llm-036",
        "llm-037",
        "llm-041",
        "llm-042",
        "llm-044",
        "llm-045",
        "llm-046",
        "llm-049",
    )
}
FOURTEENTH_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-014.json"
)
FOURTEENTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-014-2026-07-24.json"
)
FOURTEENTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-014-2026-07-24.json"
)
FOURTEENTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-014-2026-07-24.json"
)
FOURTEENTH_ADJUSTMENTS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-adjustments-batch-014-2026-07-24.json"
)
FOURTEENTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-014-2026-07-24.md"
)
FOURTEENTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-014-2026-07-24.json"
)
FOURTEENTH_GEMINI_CASE_IDS = {
    f"aosp-framework-zh-rcn-v1/{case_id}"
    for case_id in (
        "string-04e490f612fcaa02",
        "string-114f2dd20598dd3d",
        "string-6b65b8fa97b1b2c5",
        "string-7179b94f61589660",
        "string-cd5eacc89701c0a9",
    )
}
FIFTEENTH_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-015.json"
)
FIFTEENTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-015-2026-07-24.json"
)
FIFTEENTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-015-2026-07-24.json"
)
FIFTEENTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-015-2026-07-24.json"
)
FIFTEENTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-015-2026-07-24.md"
)
FIFTEENTH_GEMINI_CASE_IDS = {
    f"zhtw-project-formal-entity-guard-v1/{case_id}"
    for case_id in (
        "baseline-001",
        "baseline-002",
        "baseline-007",
        "baseline-008",
        "baseline-019",
        "code-012",
        "code-016",
        "code-018",
        "entity-015",
        "quote-001",
        "quote-003",
        "quote-005",
        "title-009",
        "title-015",
        "title-016",
    )
}


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_synthesis_distinguishes_codex_and_maintainer_overrides() -> None:
    codex = {
        "packet_path": "packet.json",
        "packet_sha256": "a" * 64,
        "cases": [
            {
                "id": "case-1",
                "eligible": True,
                "script": "simplified",
                "domain": "formal_news",
                "risk": "baseline_guard",
                "quality_flags": [],
                "confidence": "high",
            }
        ],
    }
    gemini = json.loads(json.dumps(codex))
    override = {
        "case-1": {
            **codex["cases"][0],
            "risk": "candidate_gap",
        }
    }
    override["case-1"].pop("id")

    synthesis = build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-24",
        overrides=override,
        override_basis="codex_synthesis",
    )

    assert synthesis["cases"][0]["selection_basis"] == "codex_synthesis"
    assert synthesis["stats"]["by_selection_basis"] == {"codex_synthesis": 1}


def test_committed_advisories_cover_packet_and_diff_is_reproducible() -> None:
    packet = load(PACKET_PATH)
    codex = load(CODEX_PATH)
    gemini = load(GEMINI_PATH)
    decision = load(DECISION_PATH)
    packet_hash = hashlib.sha256(PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in gemini["cases"]] == [case["id"] for case in packet["cases"]]
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 60,
        "review_queue": 40,
        "by_field": {"eligible": 21, "script": 0, "domain": 28, "risk": 35},
    }
    assert len(differences) == 40
    assert gemini["stats"]["policy_violations"] == 16
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 100,
        "confirmed_cases": 100,
        "resolved_disagreements": 40,
        "confirmed_exact_matches": 60,
        "remaining_cases": 0,
    }
    assert {case["id"] for case in decision["cases"]} == {case["id"] for case in packet["cases"]}
    assert sum(case["advisory_relation"] == "disagreement" for case in decision["cases"]) == 40
    assert sum(case["advisory_relation"] == "exact_match" for case in decision["cases"]) == 60
    assert all(case["selected_advisory"] == "codex" for case in decision["cases"])
    allowed_domains = {
        "it_api_cli",
        "ui_i18n",
        "llm_generated",
        "formal_news",
        "social_daily",
        "high_stakes",
        None,
    }
    allowed_risks = {"candidate_gap", "over_conversion_guard", "baseline_guard", None}
    for report in (codex, gemini):
        for case in report["cases"]:
            assert case["domain"] in allowed_domains
            assert case["risk"] in allowed_risks
            if not case["eligible"]:
                assert case["domain"] is case["risk"] is None
    assert DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-20",
        maintainer_decisions=decision,
    )


def test_committed_maintainer_decision_is_reproducible() -> None:
    assert load(DECISION_PATH) == build_decision(
        PACKET_PATH,
        CODEX_PATH,
        GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-21",
        selected_advisory="codex",
    )


def test_second_committed_advisories_cover_packet_and_diff_is_reproducible() -> None:
    packet = load(SECOND_PACKET_PATH)
    codex = load(SECOND_CODEX_PATH)
    gemini = load(SECOND_GEMINI_PATH)
    decision = load(SECOND_DECISION_PATH)
    packet_hash = hashlib.sha256(SECOND_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in gemini["cases"]] == [case["id"] for case in packet["cases"]]
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 55,
        "review_queue": 45,
        "by_field": {"eligible": 9, "script": 0, "domain": 27, "risk": 31},
    }
    assert len(differences) == 45
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert gemini["stats"]["policy_violations"] == 0
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 100,
        "confirmed_cases": 100,
        "resolved_disagreements": 45,
        "confirmed_exact_matches": 55,
        "remaining_cases": 0,
    }
    assert all(case["selected_advisory"] == "codex" for case in decision["cases"])
    assert SECOND_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-21",
        maintainer_decisions=decision,
    )


def test_second_committed_maintainer_decision_is_reproducible() -> None:
    assert load(SECOND_DECISION_PATH) == build_decision(
        SECOND_PACKET_PATH,
        SECOND_CODEX_PATH,
        SECOND_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-21",
        selected_advisory="codex",
    )


def test_third_committed_advisories_and_decision_cover_cdc_packet() -> None:
    packet = load(THIRD_PACKET_PATH)
    codex = load(THIRD_CODEX_PATH)
    gemini = load(THIRD_GEMINI_PATH)
    decision = load(THIRD_DECISION_PATH)
    packet_hash = hashlib.sha256(THIRD_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in gemini["cases"]] == [case["id"] for case in packet["cases"]]
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 62,
        "exact": 33,
        "review_queue": 29,
        "by_field": {"eligible": 1, "script": 0, "domain": 20, "risk": 21},
    }
    assert len(differences) == 29
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 62,
        "confirmed_cases": 62,
        "resolved_disagreements": 29,
        "confirmed_exact_matches": 33,
        "remaining_cases": 0,
    }
    assert sum(case["classification"]["eligible"] for case in decision["cases"]) == 61
    assert all(case["selected_advisory"] == "codex" for case in decision["cases"])
    assert THIRD_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-22",
        maintainer_decisions=decision,
    )


def test_third_committed_maintainer_decision_is_reproducible() -> None:
    assert load(THIRD_DECISION_PATH) == build_decision(
        THIRD_PACKET_PATH,
        THIRD_CODEX_PATH,
        THIRD_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-22",
        selected_advisory="codex",
    )


def test_fourth_advisories_cover_project_original_packet() -> None:
    packet = load(FOURTH_PACKET_PATH)
    codex = load(FOURTH_CODEX_PATH)
    gemini = load(FOURTH_GEMINI_PATH)
    decision = load(FOURTH_DECISION_PATH)
    packet_hash = hashlib.sha256(FOURTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in gemini["cases"]] == [case["id"] for case in packet["cases"]]
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 69,
        "review_queue": 31,
        "by_field": {"eligible": 0, "script": 0, "domain": 5, "risk": 27},
    }
    assert len(differences) == 31
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert gemini["stats"]["policy_violations"] == 0
    assert validate_decision(decision) == []
    assert all(case["selected_advisory"] == "synthesis" for case in decision["cases"])
    assert FOURTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-23",
        maintainer_decisions=decision,
    )


def test_fourth_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(FOURTH_DECISION_PATH) == build_decision(
        FOURTH_PACKET_PATH,
        FOURTH_CODEX_PATH,
        FOURTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-23",
        selected_advisory="synthesis",
        synthesis_path=FOURTH_SYNTHESIS_PATH,
    )


def test_fifth_advisories_synthesis_and_decision_cover_massive_packet() -> None:
    packet = load(FIFTH_PACKET_PATH)
    codex = load(FIFTH_CODEX_PATH)
    gemini = load(FIFTH_GEMINI_PATH)
    synthesis = load(FIFTH_SYNTHESIS_PATH)
    decision = load(FIFTH_DECISION_PATH)
    packet_hash = hashlib.sha256(FIFTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in gemini["cases"]] == [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in synthesis["cases"]] == [case["id"] for case in packet["cases"]]
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 35,
        "review_queue": 65,
        "by_field": {"eligible": 4, "script": 3, "domain": 48, "risk": 33},
    }
    assert len(differences) == 65
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert len(gemini["validation"]["rejected_attempts"]) == 2
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 98,
        "excluded": 2,
        "by_selection_basis": {
            "agreement": 35,
            "codex": 16,
            "gemini": 45,
            "hybrid": 4,
        },
    }
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 100,
        "confirmed_cases": 100,
        "resolved_disagreements": 65,
        "confirmed_exact_matches": 35,
        "remaining_cases": 0,
    }
    assert sum(case["classification"]["eligible"] for case in decision["cases"]) == 98
    assert all(case["selected_advisory"] == "synthesis" for case in decision["cases"])
    assert FIFTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-23",
        maintainer_decisions=decision,
    )


def test_fifth_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(FIFTH_DECISION_PATH) == build_decision(
        FIFTH_PACKET_PATH,
        FIFTH_CODEX_PATH,
        FIFTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-23",
        selected_advisory="synthesis",
        synthesis_path=FIFTH_SYNTHESIS_PATH,
    )


def test_sixth_advisories_and_synthesis_cover_project_it_packet() -> None:
    packet = load(SIXTH_PACKET_PATH)
    codex = load(SIXTH_CODEX_PATH)
    gemini = load(SIXTH_GEMINI_PATH)
    synthesis = load(SIXTH_SYNTHESIS_PATH)
    decision = load(SIXTH_DECISION_PATH)
    packet_hash = hashlib.sha256(SIXTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in gemini["cases"]] == [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in synthesis["cases"]] == [case["id"] for case in packet["cases"]]
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 58,
        "review_queue": 42,
        "by_field": {"eligible": 0, "script": 8, "domain": 0, "risk": 35},
    }
    assert len(differences) == 42
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 100,
        "excluded": 0,
        "by_selection_basis": {
            "agreement": 58,
            "codex": 13,
            "gemini": 28,
            "hybrid": 1,
        },
    }
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 100,
        "confirmed_cases": 100,
        "resolved_disagreements": 42,
        "confirmed_exact_matches": 58,
        "remaining_cases": 0,
    }
    assert sum(case["classification"]["eligible"] for case in decision["cases"]) == 100
    assert all(case["selected_advisory"] == "synthesis" for case in decision["cases"])
    assert SIXTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-23",
        maintainer_decisions=decision,
    )


def test_sixth_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(SIXTH_DECISION_PATH) == build_decision(
        SIXTH_PACKET_PATH,
        SIXTH_CODEX_PATH,
        SIXTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-23",
        selected_advisory="synthesis",
        synthesis_path=SIXTH_SYNTHESIS_PATH,
    )


def test_seventh_advisories_and_synthesis_cover_ftc_packet() -> None:
    packet = load(SEVENTH_PACKET_PATH)
    codex = load(SEVENTH_CODEX_PATH)
    gemini = load(SEVENTH_GEMINI_PATH)
    synthesis = load(SEVENTH_SYNTHESIS_PATH)
    decision = load(SEVENTH_DECISION_PATH)
    packet_hash = hashlib.sha256(SEVENTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 81,
        "exact": 53,
        "review_queue": 28,
        "by_field": {"eligible": 22, "script": 0, "domain": 25, "risk": 26},
    }
    assert len(differences) == 28
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert "73 eligible" in gemini["validation"]["raw_summary_mismatch"]
    assert synthesis["stats"] == {
        "total": 81,
        "eligible": 55,
        "excluded": 26,
        "by_selection_basis": {
            "agreement": 53,
            "codex": 19,
            "gemini": 8,
            "hybrid": 1,
        },
    }
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 81,
        "confirmed_cases": 81,
        "resolved_disagreements": 28,
        "confirmed_exact_matches": 53,
        "remaining_cases": 0,
    }
    assert sum(case["classification"]["eligible"] for case in decision["cases"]) == 55
    assert all(case["selected_advisory"] == "synthesis" for case in decision["cases"])
    assert SEVENTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-23",
        maintainer_decisions=decision,
    )


def test_seventh_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(SEVENTH_DECISION_PATH) == build_decision(
        SEVENTH_PACKET_PATH,
        SEVENTH_CODEX_PATH,
        SEVENTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-23",
        selected_advisory="synthesis",
        synthesis_path=SEVENTH_SYNTHESIS_PATH,
    )


def test_eighth_advisories_and_synthesis_cover_nps_acadia_packet() -> None:
    packet = load(EIGHTH_PACKET_PATH)
    codex = load(EIGHTH_CODEX_PATH)
    gemini = load(EIGHTH_GEMINI_PATH)
    synthesis = load(EIGHTH_SYNTHESIS_PATH)
    decision = load(EIGHTH_DECISION_PATH)
    packet_hash = hashlib.sha256(EIGHTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 32,
        "exact": 7,
        "review_queue": 25,
        "by_field": {"eligible": 2, "script": 0, "domain": 22, "risk": 15},
    }
    assert len(differences) == 25
    assert gemini["validation"]["exact_id_coverage"] == "32/32"
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert synthesis["stats"] == {
        "total": 32,
        "eligible": 30,
        "excluded": 2,
        "by_selection_basis": {
            "agreement": 7,
            "codex": 21,
            "gemini": 1,
            "hybrid": 3,
        },
    }
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 32,
        "confirmed_cases": 32,
        "resolved_disagreements": 25,
        "confirmed_exact_matches": 7,
        "remaining_cases": 0,
    }
    assert sum(case["classification"]["eligible"] for case in decision["cases"]) == 30
    assert all(case["selected_advisory"] == "synthesis" for case in decision["cases"])
    assert EIGHTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-23",
        maintainer_decisions=decision,
    )


def test_eighth_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(EIGHTH_DECISION_PATH) == build_decision(
        EIGHTH_PACKET_PATH,
        EIGHTH_CODEX_PATH,
        EIGHTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-23",
        selected_advisory="synthesis",
        synthesis_path=EIGHTH_SYNTHESIS_PATH,
    )


def test_tenth_advisories_synthesis_and_decision_cover_osha_packet() -> None:
    packet = load(TENTH_PACKET_PATH)
    codex = load(TENTH_CODEX_PATH)
    gemini = load(TENTH_GEMINI_PATH)
    synthesis = load(TENTH_SYNTHESIS_PATH)
    decision = load(TENTH_DECISION_PATH)
    packet_hash = hashlib.sha256(TENTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    packet_ids = [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert [case["id"] for case in synthesis["cases"]] == packet_ids
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 41,
        "review_queue": 59,
        "by_field": {"eligible": 17, "script": 0, "domain": 20, "risk": 59},
    }
    assert len(differences) == 59
    assert gemini["validation"]["exact_id_coverage"] == "100/100"
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 85,
        "excluded": 15,
        "by_selection_basis": {"agreement": 41, "codex": 56, "gemini": 3},
    }
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 100,
        "confirmed_cases": 100,
        "resolved_disagreements": 59,
        "confirmed_exact_matches": 41,
        "remaining_cases": 0,
    }
    assert sum(case["classification"]["eligible"] for case in decision["cases"]) == 85
    assert all(case["selected_advisory"] == "synthesis" for case in decision["cases"])
    assert TENTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-23",
        maintainer_decisions=decision,
    )


def test_tenth_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(TENTH_DECISION_PATH) == build_decision(
        TENTH_PACKET_PATH,
        TENTH_CODEX_PATH,
        TENTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-24",
        selected_advisory="synthesis",
        synthesis_path=TENTH_SYNTHESIS_PATH,
    )


def test_eleventh_advisories_and_pending_synthesis_cover_vscode_packet() -> None:
    packet = load(ELEVENTH_PACKET_PATH)
    codex = load(ELEVENTH_CODEX_PATH)
    gemini = load(ELEVENTH_GEMINI_PATH)
    synthesis = load(ELEVENTH_SYNTHESIS_PATH)
    adjustments = load(ELEVENTH_ADJUSTMENTS_PATH)
    decision = load(ELEVENTH_DECISION_PATH)
    packet_hash = hashlib.sha256(ELEVENTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    packet_ids = [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert [case["id"] for case in synthesis["cases"]] == packet_ids
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 35,
        "review_queue": 65,
        "by_field": {"eligible": 4, "script": 0, "domain": 31, "risk": 50},
    }
    assert len(differences) == 65
    assert gemini["validation"]["exact_id_coverage"] == "100/100"
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 100,
        "excluded": 0,
        "by_selection_basis": {
            "agreement": 35,
            "codex": 57,
            "gemini": 4,
            "maintainer_feedback": 4,
        },
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=ELEVENTH_GEMINI_CASE_IDS,
        generated_date="2026-07-24",
        overrides=overrides,
    )
    assert validate_decision(decision) == []
    assert sum(case["classification"]["eligible"] for case in decision["cases"]) == 100
    rendered_diff = render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-24",
        maintainer_decisions=decision,
    )
    assert ELEVENTH_DIFF_PATH.read_text(encoding="utf-8") == rendered_diff
    assert all(line == line.rstrip() for line in rendered_diff.splitlines())


def test_eleventh_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(ELEVENTH_DECISION_PATH) == build_decision(
        ELEVENTH_PACKET_PATH,
        ELEVENTH_CODEX_PATH,
        ELEVENTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-24",
        selected_advisory="synthesis",
        synthesis_path=ELEVENTH_SYNTHESIS_PATH,
    )


def test_twelfth_advisories_and_pending_synthesis_cover_ftc_heads_up_packet() -> None:
    packet = load(TWELFTH_PACKET_PATH)
    codex = load(TWELFTH_CODEX_PATH)
    gemini = load(TWELFTH_GEMINI_PATH)
    synthesis = load(TWELFTH_SYNTHESIS_PATH)
    adjustments = load(TWELFTH_ADJUSTMENTS_PATH)
    decision = load(TWELFTH_DECISION_PATH)
    packet_hash = hashlib.sha256(TWELFTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    packet_ids = [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert [case["id"] for case in synthesis["cases"]] == packet_ids
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 49,
        "review_queue": 51,
        "by_field": {"eligible": 1, "script": 0, "domain": 25, "risk": 34},
    }
    assert len(differences) == 51
    assert gemini["validation"]["exact_id_coverage"] == "100/100"
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert gemini["validation"]["response_json_extracted_from_markdown_fence"] is True
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 100,
        "excluded": 0,
        "by_selection_basis": {
            "agreement": 49,
            "codex": 50,
            "maintainer_feedback": 1,
        },
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-24",
        overrides=overrides,
    )
    assert validate_decision(decision) == []
    assert sum(case["classification"]["eligible"] for case in decision["cases"]) == 100
    assert TWELFTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-24",
        maintainer_decisions=decision,
    )


def test_twelfth_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(TWELFTH_DECISION_PATH) == build_decision(
        TWELFTH_PACKET_PATH,
        TWELFTH_CODEX_PATH,
        TWELFTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-24",
        selected_advisory="synthesis",
        synthesis_path=TWELFTH_SYNTHESIS_PATH,
    )


def test_thirteenth_advisories_and_codex_synthesis_are_reproducible() -> None:
    packet = load(THIRTEENTH_PACKET_PATH)
    codex = load(THIRTEENTH_CODEX_PATH)
    gemini = load(THIRTEENTH_GEMINI_PATH)
    synthesis = load(THIRTEENTH_SYNTHESIS_PATH)
    decision = load(THIRTEENTH_DECISION_PATH)
    adjustments = load(THIRTEENTH_ADJUSTMENTS_PATH)
    packet_hash = hashlib.sha256(THIRTEENTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    packet_ids = [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert [case["id"] for case in synthesis["cases"]] == packet_ids
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 57,
        "review_queue": 43,
        "by_field": {"eligible": 0, "script": 0, "domain": 11, "risk": 35},
    }
    assert len(differences) == 43
    assert gemini["reviewer"] == "Gemini via Antigravity CLI"
    assert gemini["model"] == "gemini-3.1-pro-high"
    assert gemini["validation"]["exact_id_coverage"] == "100/100"
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 100,
        "excluded": 0,
        "by_selection_basis": {
            "agreement": 57,
            "codex": 16,
            "codex_synthesis": 3,
            "gemini": 24,
        },
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=THIRTEENTH_GEMINI_CASE_IDS,
        generated_date="2026-07-24",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert THIRTEENTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-24",
        maintainer_decisions=decision,
    )


def test_thirteenth_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(THIRTEENTH_DECISION_PATH) == build_decision(
        THIRTEENTH_PACKET_PATH,
        THIRTEENTH_CODEX_PATH,
        THIRTEENTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-24",
        selected_advisory="synthesis",
        synthesis_path=THIRTEENTH_SYNTHESIS_PATH,
    )


def test_fourteenth_advisories_and_codex_synthesis_are_reproducible() -> None:
    packet = load(FOURTEENTH_PACKET_PATH)
    codex = load(FOURTEENTH_CODEX_PATH)
    gemini = load(FOURTEENTH_GEMINI_PATH)
    synthesis = load(FOURTEENTH_SYNTHESIS_PATH)
    decision = load(FOURTEENTH_DECISION_PATH)
    adjustments = load(FOURTEENTH_ADJUSTMENTS_PATH)
    packet_hash = hashlib.sha256(FOURTEENTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    packet_ids = [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert [case["id"] for case in synthesis["cases"]] == packet_ids
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 75,
        "review_queue": 25,
        "by_field": {"eligible": 0, "script": 0, "domain": 1, "risk": 25},
    }
    assert len(differences) == 25
    assert gemini["reviewer"] == "Gemini via Antigravity CLI"
    assert gemini["model"] == "gemini-3.1-pro-high"
    assert gemini["validation"]["exact_id_coverage"] == "100/100"
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 100,
        "excluded": 0,
        "by_selection_basis": {
            "agreement": 75,
            "codex": 19,
            "codex_synthesis": 1,
            "gemini": 5,
        },
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=FOURTEENTH_GEMINI_CASE_IDS,
        generated_date="2026-07-24",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert FOURTEENTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-24",
        maintainer_decisions=decision,
    )


def test_fourteenth_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(FOURTEENTH_DECISION_PATH) == build_decision(
        FOURTEENTH_PACKET_PATH,
        FOURTEENTH_CODEX_PATH,
        FOURTEENTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-24",
        selected_advisory="synthesis",
        synthesis_path=FOURTEENTH_SYNTHESIS_PATH,
    )


def test_fifteenth_pending_advisories_and_codex_synthesis_are_reproducible() -> None:
    packet = load(FIFTEENTH_PACKET_PATH)
    codex = load(FIFTEENTH_CODEX_PATH)
    gemini = load(FIFTEENTH_GEMINI_PATH)
    synthesis = load(FIFTEENTH_SYNTHESIS_PATH)
    packet_hash = hashlib.sha256(FIFTEENTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    packet_ids = [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert [case["id"] for case in synthesis["cases"]] == packet_ids
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 73,
        "review_queue": 27,
        "by_field": {"eligible": 0, "script": 0, "domain": 24, "risk": 3},
    }
    assert len(differences) == 27
    assert gemini["reviewer"] == "Gemini via Antigravity CLI"
    assert gemini["model"] == "gemini-3.1-pro-high"
    assert gemini["validation"]["exact_id_coverage"] == "100/100"
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 100,
        "excluded": 0,
        "by_selection_basis": {"agreement": 73, "codex": 12, "gemini": 15},
    }
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=FIFTEENTH_GEMINI_CASE_IDS,
        generated_date="2026-07-24",
    )
    assert FIFTEENTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-24",
    )
