# zhtw:disable
"""Tests for the accuracy annotation backlog."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BACKLOG = ROOT / "benchmarks" / "accuracy" / "annotation-backlog-v1.json"
SCHEMA = ROOT / "benchmarks" / "accuracy" / "annotation-backlog-v1.schema.json"
STATUS_SCRIPT = ROOT / "scripts" / "accuracy_annotation_status.py"
PACKET_SCRIPT = ROOT / "scripts" / "create_blind_review_packet.py"
CHECK_SCRIPT = ROOT / "scripts" / "check_accuracy_backlog.py"
GEMINI_ADVISORY = ROOT / "docs" / "reports" / "annotation-gemini-vertex-advisory-2026-07-05.json"
SECOND_GEMINI_ADVISORY = (
    ROOT
    / "docs"
    / "reports"
    / "annotation-gemini-vertex-advisory-it-api-cli-0026-0075-2026-07-05.json"
)
THIRD_GEMINI_ADVISORY = (
    ROOT
    / "docs"
    / "reports"
    / "annotation-gemini-vertex-advisory-it-api-cli-0076-0125-2026-07-06.json"
)
FOURTH_GEMINI_ADVISORY = (
    ROOT
    / "docs"
    / "reports"
    / "annotation-gemini-vertex-advisory-it-api-cli-0126-0175-2026-07-06.json"
)
UI_GEMINI_ADVISORY_FIRST = (
    ROOT
    / "docs"
    / "reports"
    / "annotation-gemini-vertex-advisory-ui-i18n-0001-0050-2026-07-06.json"
)
UI_GEMINI_ADVISORY_SECOND = (
    ROOT
    / "docs"
    / "reports"
    / "annotation-gemini-vertex-advisory-ui-i18n-0051-0100-2026-07-06.json"
)
UI_GEMINI_ADVISORY_THIRD = (
    ROOT
    / "docs"
    / "reports"
    / "annotation-gemini-vertex-advisory-ui-i18n-0101-0125-2026-07-06.json"
)
FORMAL_GEMINI_ADVISORY_FIRST = (
    ROOT
    / "docs"
    / "reports"
    / "annotation-gemini-vertex-advisory-formal-high-risk-0001-0050-2026-07-06.json"
)
FORMAL_GEMINI_ADVISORY_SECOND = (
    ROOT
    / "docs"
    / "reports"
    / "annotation-gemini-vertex-advisory-formal-high-risk-0051-0100-2026-07-06.json"
)
SOCIAL_GEMINI_ADVISORY_FIRST = (
    ROOT
    / "docs"
    / "reports"
    / "annotation-gemini-vertex-advisory-social-daily-0001-0050-2026-07-07.json"
)
SOCIAL_GEMINI_ADVISORY_SECOND = (
    ROOT
    / "docs"
    / "reports"
    / "annotation-gemini-vertex-advisory-social-daily-0051-0075-2026-07-07.json"
)
MIXED_GEMINI_ADVISORY = (
    ROOT
    / "docs"
    / "reports"
    / "annotation-gemini-vertex-advisory-mixed-ambiguity-0001-0025-2026-07-07.json"
)
GROUND_TRUTH_CORRECTIONS = (
    ROOT / "docs" / "reports" / "accuracy-ground-truth-corrections-2026-07-16.json"
)
GROUND_TRUTH_CORRECTION_IDS = {
    "it-api-cli-0043",
    "it-api-cli-0170",
    "social-daily-0038",
}
FIRST_DRAFT_REPORT = "docs/reports/annotation-first-pass-ai-draft-2026-07-05.md"
SECOND_DRAFT_REPORT = (
    "docs/reports/annotation-first-pass-ai-draft-it-api-cli-0026-0075-2026-07-05.md"
)
THIRD_DRAFT_REPORT = (
    "docs/reports/annotation-first-pass-ai-draft-it-api-cli-0076-0125-2026-07-06.md"
)
FOURTH_DRAFT_REPORT = (
    "docs/reports/annotation-first-pass-ai-draft-it-api-cli-0126-0175-2026-07-06.md"
)
UI_DRAFT_REPORT = "docs/reports/annotation-first-pass-ai-draft-ui-i18n-0001-0100-2026-07-06.md"
UI_DRAFT_REPORT_SECOND = (
    "docs/reports/annotation-first-pass-ai-draft-ui-i18n-0101-0125-2026-07-06.md"
)
FORMAL_DRAFT_REPORT = (
    "docs/reports/annotation-first-pass-ai-draft-formal-high-risk-0001-0100-2026-07-06.md"
)
SOCIAL_DRAFT_REPORT = (
    "docs/reports/annotation-first-pass-ai-draft-social-daily-0001-0075-2026-07-07.md"
)
MIXED_DRAFT_REPORT = (
    "docs/reports/annotation-first-pass-ai-draft-mixed-ambiguity-0001-0025-2026-07-07.md"
)
SECOND_GEMINI_ADVISORY_REPORT = (
    "docs/reports/annotation-gemini-vertex-advisory-it-api-cli-0026-0075-2026-07-05.md"
)
SECOND_GEMINI_ADVISORY_RAW = (
    "docs/reports/annotation-gemini-vertex-advisory-it-api-cli-0026-0075-2026-07-05.json"
)
THIRD_GEMINI_ADVISORY_REPORT = (
    "docs/reports/annotation-gemini-vertex-advisory-it-api-cli-0076-0125-2026-07-06.md"
)
THIRD_GEMINI_ADVISORY_RAW = (
    "docs/reports/annotation-gemini-vertex-advisory-it-api-cli-0076-0125-2026-07-06.json"
)
FOURTH_GEMINI_ADVISORY_REPORT = (
    "docs/reports/annotation-gemini-vertex-advisory-it-api-cli-0126-0175-2026-07-06.md"
)
FOURTH_GEMINI_ADVISORY_RAW = (
    "docs/reports/annotation-gemini-vertex-advisory-it-api-cli-0126-0175-2026-07-06.json"
)
UI_GEMINI_ADVISORY_FIRST_REPORT = (
    "docs/reports/annotation-gemini-vertex-advisory-ui-i18n-0001-0050-2026-07-06.md"
)
UI_GEMINI_ADVISORY_FIRST_RAW = (
    "docs/reports/annotation-gemini-vertex-advisory-ui-i18n-0001-0050-2026-07-06.json"
)
UI_GEMINI_ADVISORY_SECOND_REPORT = (
    "docs/reports/annotation-gemini-vertex-advisory-ui-i18n-0051-0100-2026-07-06.md"
)
UI_GEMINI_ADVISORY_SECOND_RAW = (
    "docs/reports/annotation-gemini-vertex-advisory-ui-i18n-0051-0100-2026-07-06.json"
)
UI_GEMINI_ADVISORY_THIRD_REPORT = (
    "docs/reports/annotation-gemini-vertex-advisory-ui-i18n-0101-0125-2026-07-06.md"
)
UI_GEMINI_ADVISORY_THIRD_RAW = (
    "docs/reports/annotation-gemini-vertex-advisory-ui-i18n-0101-0125-2026-07-06.json"
)
FORMAL_GEMINI_ADVISORY_FIRST_REPORT = (
    "docs/reports/annotation-gemini-vertex-advisory-formal-high-risk-0001-0050-2026-07-06.md"
)
FORMAL_GEMINI_ADVISORY_FIRST_RAW = (
    "docs/reports/annotation-gemini-vertex-advisory-formal-high-risk-0001-0050-2026-07-06.json"
)
FORMAL_GEMINI_ADVISORY_SECOND_REPORT = (
    "docs/reports/annotation-gemini-vertex-advisory-formal-high-risk-0051-0100-2026-07-06.md"
)
FORMAL_GEMINI_ADVISORY_SECOND_RAW = (
    "docs/reports/annotation-gemini-vertex-advisory-formal-high-risk-0051-0100-2026-07-06.json"
)
SOCIAL_GEMINI_ADVISORY_FIRST_REPORT = (
    "docs/reports/annotation-gemini-vertex-advisory-social-daily-0001-0050-2026-07-07.md"
)
SOCIAL_GEMINI_ADVISORY_FIRST_RAW = (
    "docs/reports/annotation-gemini-vertex-advisory-social-daily-0001-0050-2026-07-07.json"
)
SOCIAL_GEMINI_ADVISORY_SECOND_REPORT = (
    "docs/reports/annotation-gemini-vertex-advisory-social-daily-0051-0075-2026-07-07.md"
)
SOCIAL_GEMINI_ADVISORY_SECOND_RAW = (
    "docs/reports/annotation-gemini-vertex-advisory-social-daily-0051-0075-2026-07-07.json"
)
MIXED_GEMINI_ADVISORY_REPORT = (
    "docs/reports/annotation-gemini-vertex-advisory-mixed-ambiguity-0001-0025-2026-07-07.md"
)
MIXED_GEMINI_ADVISORY_RAW = (
    "docs/reports/annotation-gemini-vertex-advisory-mixed-ambiguity-0001-0025-2026-07-07.json"
)
UI_GEMINI_DECISION_IDS = {
    "ui-i18n-0022",
    "ui-i18n-0059",
    "ui-i18n-0066",
    "ui-i18n-0083",
    "ui-i18n-0108",
}
UI_CODEX_DECISION_IDS = {
    "ui-i18n-0005",
    "ui-i18n-0006",
    "ui-i18n-0008",
    "ui-i18n-0028",
    "ui-i18n-0030",
    "ui-i18n-0031",
    "ui-i18n-0052",
    "ui-i18n-0061",
    "ui-i18n-0062",
    "ui-i18n-0064",
    "ui-i18n-0067",
    "ui-i18n-0068",
    "ui-i18n-0071",
    "ui-i18n-0072",
    "ui-i18n-0075",
    "ui-i18n-0076",
    "ui-i18n-0079",
    "ui-i18n-0084",
    "ui-i18n-0085",
    "ui-i18n-0086",
    "ui-i18n-0087",
    "ui-i18n-0094",
    "ui-i18n-0095",
    "ui-i18n-0096",
    "ui-i18n-0101",
    "ui-i18n-0105",
    "ui-i18n-0107",
    "ui-i18n-0109",
    "ui-i18n-0110",
    "ui-i18n-0125",
}
FORMAL_GEMINI_DECISION_IDS = {
    "formal-high-risk-0002",
    "formal-high-risk-0008",
    "formal-high-risk-0019",
    "formal-high-risk-0035",
    "formal-high-risk-0038",
    "formal-high-risk-0051",
    "formal-high-risk-0098",
}
FORMAL_CODEX_DECISION_IDS = {
    "formal-high-risk-0040",
    "formal-high-risk-0043",
}
SOCIAL_MIXED_GEMINI_DECISION_IDS = {
    "social-daily-0008",
    "social-daily-0026",
    "mixed-ambiguity-0007",
}
SOCIAL_MIXED_CODEX_DECISION_IDS = {
    "social-daily-0005",
    "social-daily-0009",
    "social-daily-0013",
    "social-daily-0015",
    "social-daily-0022",
    "social-daily-0031",
    "social-daily-0032",
    "social-daily-0033",
    "social-daily-0042",
    "social-daily-0052",
    "social-daily-0053",
    "social-daily-0065",
    "social-daily-0068",
    "mixed-ambiguity-0002",
    "mixed-ambiguity-0009",
    "mixed-ambiguity-0011",
    "mixed-ambiguity-0018",
    "mixed-ambiguity-0020",
    "mixed-ambiguity-0021",
}


def load_backlog() -> dict:
    return json.loads(BACKLOG.read_text(encoding="utf-8"))


def test_annotation_backlog_schema_file_exists() -> None:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))

    assert schema["title"] == "zhtw accuracy annotation backlog"
    assert schema["properties"]["target_total"]["const"] == 500
    statuses = schema["properties"]["cases"]["items"]["properties"]["review"]["properties"][
        "status"
    ]["enum"]
    assert "needs_ai_advisory" in statuses
    assert "needs_maintainer_review" in statuses


def test_annotation_backlog_targets_match_m1_gap() -> None:
    backlog = load_backlog()

    assert backlog["name"] == "annotation-backlog-v1"
    assert backlog["status"] == "collecting_inputs"
    assert backlog["target_total"] == 500
    assert backlog["source_policy"]["expected_source"] == "human_review_only"
    assert (
        backlog["promotion_requirements"]["approval_policy"]
        == "single_human_with_ai_advisory_or_independent_blind_review"
    )
    assert backlog["promotion_requirements"]["blind_review_required"] is False
    assert backlog["promotion_requirements"]["ai_advisory_review_allowed"] is True
    assert backlog["promotion_requirements"]["default_review_order"] == [
        "codex_ai_draft",
        "gemini_vertex_independent_advisory",
        "maintainer_final_review",
    ]

    targets = {batch["id"]: batch["target_cases"] for batch in backlog["batches"]}
    assert targets == {
        "it-api-cli": 175,
        "ui-i18n": 125,
        "formal-high-risk": 100,
        "social-daily": 75,
        "mixed-ambiguity": 25,
    }
    assert sum(targets.values()) == backlog["target_total"]


def test_annotation_backlog_has_first_it_api_cli_input_batch() -> None:
    backlog = load_backlog()
    advisory = json.loads(GEMINI_ADVISORY.read_text(encoding="utf-8"))
    second_advisory = json.loads(SECOND_GEMINI_ADVISORY.read_text(encoding="utf-8"))
    third_advisory = json.loads(THIRD_GEMINI_ADVISORY.read_text(encoding="utf-8"))
    fourth_advisory = json.loads(FOURTH_GEMINI_ADVISORY.read_text(encoding="utf-8"))
    ui_first_advisory = json.loads(UI_GEMINI_ADVISORY_FIRST.read_text(encoding="utf-8"))
    ui_second_advisory = json.loads(UI_GEMINI_ADVISORY_SECOND.read_text(encoding="utf-8"))
    ui_third_advisory = json.loads(UI_GEMINI_ADVISORY_THIRD.read_text(encoding="utf-8"))
    formal_first_advisory = json.loads(FORMAL_GEMINI_ADVISORY_FIRST.read_text(encoding="utf-8"))
    formal_second_advisory = json.loads(FORMAL_GEMINI_ADVISORY_SECOND.read_text(encoding="utf-8"))
    social_first_advisory = json.loads(SOCIAL_GEMINI_ADVISORY_FIRST.read_text(encoding="utf-8"))
    social_second_advisory = json.loads(SOCIAL_GEMINI_ADVISORY_SECOND.read_text(encoding="utf-8"))
    mixed_advisory = json.loads(MIXED_GEMINI_ADVISORY.read_text(encoding="utf-8"))
    advisory_by_id = {case["id"]: case for case in advisory["review"]["cases"]}
    second_advisory_by_id = {case["id"]: case for case in second_advisory["review"]["cases"]}
    fourth_advisory_by_id = {case["id"]: case for case in fourth_advisory["review"]["cases"]}
    third_comparison_by_id = {case["id"]: case for case in third_advisory["comparisons"]}
    ui_comparison_by_id = {
        case["id"]: case
        for case in (
            ui_first_advisory["comparisons"]
            + ui_second_advisory["comparisons"]
            + ui_third_advisory["comparisons"]
        )
    }
    formal_comparison_by_id = {
        case["id"]: case
        for case in formal_first_advisory["comparisons"] + formal_second_advisory["comparisons"]
    }
    social_comparison_by_id = {
        case["id"]: case
        for case in social_first_advisory["comparisons"] + social_second_advisory["comparisons"]
    }
    mixed_comparison_by_id = {case["id"]: case for case in mixed_advisory["comparisons"]}
    cases = backlog["cases"]
    it_cases = [case for case in cases if case["batch"] == "it-api-cli"]
    ui_batch = [case for case in cases if case["batch"] == "ui-i18n"]
    formal_batch = [case for case in cases if case["batch"] == "formal-high-risk"]
    social_batch = [case for case in cases if case["batch"] == "social-daily"]
    mixed_batch = [case for case in cases if case["batch"] == "mixed-ambiguity"]
    approved_ui_batch = ui_batch
    ui_third_batch = [case for case in cases if "ui-i18n-0101" <= case["id"] <= "ui-i18n-0125"]
    first_batch = [
        case for case in it_cases if "it-api-cli-0001" <= case["id"] <= "it-api-cli-0025"
    ]
    second_batch = [
        case for case in it_cases if "it-api-cli-0026" <= case["id"] <= "it-api-cli-0075"
    ]
    third_batch = [
        case for case in it_cases if "it-api-cli-0076" <= case["id"] <= "it-api-cli-0125"
    ]
    fourth_batch = [
        case for case in it_cases if "it-api-cli-0126" <= case["id"] <= "it-api-cli-0175"
    ]
    ui_first_batch = [case for case in cases if "ui-i18n-0001" <= case["id"] <= "ui-i18n-0050"]
    ui_second_batch = [case for case in cases if "ui-i18n-0051" <= case["id"] <= "ui-i18n-0100"]
    formal_first_batch = [
        case for case in cases if "formal-high-risk-0001" <= case["id"] <= "formal-high-risk-0050"
    ]
    formal_second_batch = [
        case for case in cases if "formal-high-risk-0051" <= case["id"] <= "formal-high-risk-0100"
    ]
    social_first_batch = [
        case for case in cases if "social-daily-0001" <= case["id"] <= "social-daily-0050"
    ]
    social_second_batch = [
        case for case in cases if "social-daily-0051" <= case["id"] <= "social-daily-0075"
    ]
    approved_social_mixed_batch = social_batch + mixed_batch

    assert len(cases) == 500
    assert len(it_cases) == 175
    assert len(ui_batch) == 125
    assert len(formal_batch) == 100
    assert len(social_batch) == 75
    assert len(mixed_batch) == 25
    assert len(approved_ui_batch) == 125
    assert len(ui_third_batch) == 25
    assert len(first_batch) == 25
    assert len(second_batch) == 50
    assert len(third_batch) == 50
    assert len(fourth_batch) == 50
    assert len(ui_first_batch) == 50
    assert len(ui_second_batch) == 50
    assert len(formal_first_batch) == 50
    assert len(formal_second_batch) == 50
    assert len(social_first_batch) == 50
    assert len(social_second_batch) == 25
    assert {case["batch"] for case in cases} == {
        "formal-high-risk",
        "it-api-cli",
        "mixed-ambiguity",
        "social-daily",
        "ui-i18n",
    }
    assert {case["domain"] for case in cases} == {"formal", "it", "mixed", "social", "ui"}
    assert {case["review"]["status"] for case in it_cases} == {
        "approved",
    }
    assert {case["review"]["status"] for case in approved_ui_batch} == {"approved"}
    assert all(
        case["review"]["expected"] == advisory_by_id[case["id"]]["expected"] for case in first_batch
    )
    assert (
        sum(case["review"]["expected_source"] == "human_first_pass" for case in first_batch) == 11
    )
    assert (
        sum(case["review"]["expected_source"] == "human_adjudication" for case in first_batch) == 14
    )
    assert all(case["review"]["first_reviewer"] == "tim" for case in first_batch)
    assert all(case["review"]["blind_reviewer"] == "" for case in first_batch)
    assert sum(case["review"]["adjudicator"] == "tim" for case in first_batch) == 14
    assert sum(case["review"]["adjudicator"] == "" for case in first_batch) == 11
    assert all(case["review"]["ai_advisory"]["reviewer"] == "gemini_vertex" for case in first_batch)
    assert all(case["review"]["ai_advisory"]["decision"] == "accepted" for case in first_batch)
    assert all(case["review"]["ai_advisory"]["decision_by"] == "tim" for case in first_batch)
    assert all(
        case["review"]["ai_advisory"]["decision_date"] == "2026-07-05" for case in first_batch
    )
    assert all(case["review"]["status"] == "approved" for case in second_batch)
    assert all(
        case["review"]["expected"] == second_advisory_by_id[case["id"]]["expected"]
        for case in second_batch
        if case["id"] not in GROUND_TRUTH_CORRECTION_IDS
    )
    assert (
        sum(case["review"]["expected_source"] == "human_first_pass" for case in second_batch) == 25
    )
    assert (
        sum(case["review"]["expected_source"] == "human_adjudication" for case in second_batch)
        == 25
    )
    assert all(case["review"]["first_reviewer"] == "tim" for case in second_batch)
    assert all(case["review"]["blind_reviewer"] == "" for case in second_batch)
    assert sum(case["review"]["adjudicator"] == "tim" for case in second_batch) == 25
    assert sum(case["review"]["adjudicator"] == "" for case in second_batch) == 25
    assert all(
        case["review"]["ai_advisory"]["reviewer"] == "gemini_vertex" for case in second_batch
    )
    assert (
        sum(case["review"]["ai_advisory"]["decision"] == "accepted" for case in second_batch) == 49
    )
    assert (
        sum(case["review"]["ai_advisory"]["decision"] == "rejected" for case in second_batch) == 1
    )
    assert all(case["review"]["ai_advisory"]["decision_by"] == "tim" for case in second_batch)
    assert all(
        case["review"]["ai_advisory"]["decision_date"] in {"2026-07-05", "2026-07-16"}
        for case in second_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["reviewer"] == "gemini_vertex" for case in second_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["source_report"] == SECOND_GEMINI_ADVISORY_REPORT
        for case in second_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["raw_report"] == SECOND_GEMINI_ADVISORY_RAW
        for case in second_batch
    )
    assert (
        sum(
            case["review"]["ai_advisory_draft"]["exact_match_with_ai_draft"]
            for case in second_batch
        )
        == 25
    )
    assert second_advisory["comparison_summary"] == {
        "cases": 50,
        "exact_matches_with_codex_draft": 25,
        "differences_from_codex_draft": 25,
    }
    assert all(case["review"]["status"] == "approved" for case in third_batch)
    assert all(
        case["review"]["expected"] == third_comparison_by_id[case["id"]]["codex_expected"]
        for case in third_batch
    )
    assert (
        sum(case["review"]["expected_source"] == "human_first_pass" for case in third_batch) == 24
    )
    assert (
        sum(case["review"]["expected_source"] == "human_adjudication" for case in third_batch) == 26
    )
    assert all(case["review"]["first_reviewer"] == "tim" for case in third_batch)
    assert all(case["review"]["blind_reviewer"] == "" for case in third_batch)
    assert sum(case["review"]["adjudicator"] == "tim" for case in third_batch) == 26
    assert sum(case["review"]["adjudicator"] == "" for case in third_batch) == 24
    assert sum(case["review"]["disagreement"] for case in third_batch) == 26
    assert all(case["review"]["ai_advisory"]["reviewer"] == "gemini_vertex" for case in third_batch)
    assert (
        sum(case["review"]["ai_advisory"]["decision"] == "accepted" for case in third_batch) == 24
    )
    assert (
        sum(case["review"]["ai_advisory"]["decision"] == "rejected" for case in third_batch) == 26
    )
    assert all(case["review"]["ai_advisory"]["decision_by"] == "tim" for case in third_batch)
    assert all(
        case["review"]["ai_advisory"]["decision_date"] == "2026-07-06" for case in third_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["reviewer"] == "gemini_vertex" for case in third_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["source_report"] == THIRD_GEMINI_ADVISORY_REPORT
        for case in third_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["raw_report"] == THIRD_GEMINI_ADVISORY_RAW
        for case in third_batch
    )
    assert (
        sum(
            case["review"]["ai_advisory_draft"]["exact_match_with_ai_draft"] for case in third_batch
        )
        == 24
    )
    assert third_advisory["comparison_summary"] == {
        "cases": 50,
        "exact_matches_with_codex_draft": 24,
        "differences_from_codex_draft": 26,
    }
    assert all(case["review"]["status"] == "approved" for case in fourth_batch)
    assert all(
        case["review"]["expected"] == fourth_advisory_by_id[case["id"]]["expected"]
        for case in fourth_batch
        if case["id"] not in GROUND_TRUTH_CORRECTION_IDS
    )
    assert (
        sum(case["review"]["expected_source"] == "human_first_pass" for case in fourth_batch) == 33
    )
    assert (
        sum(case["review"]["expected_source"] == "human_adjudication" for case in fourth_batch)
        == 17
    )
    assert all(case["review"]["first_reviewer"] == "tim" for case in fourth_batch)
    assert all(case["review"]["blind_reviewer"] == "" for case in fourth_batch)
    assert sum(case["review"]["adjudicator"] == "tim" for case in fourth_batch) == 17
    assert sum(case["review"]["adjudicator"] == "" for case in fourth_batch) == 33
    assert sum(case["review"]["disagreement"] for case in fourth_batch) == 17
    assert all(
        case["review"]["ai_advisory"]["reviewer"] == "gemini_vertex" for case in fourth_batch
    )
    assert (
        sum(case["review"]["ai_advisory"]["decision"] == "accepted" for case in fourth_batch) == 49
    )
    assert (
        sum(case["review"]["ai_advisory"]["decision"] == "rejected" for case in fourth_batch) == 1
    )
    assert all(case["review"]["ai_advisory"]["decision_by"] == "tim" for case in fourth_batch)
    assert all(
        case["review"]["ai_advisory"]["decision_date"] in {"2026-07-06", "2026-07-16"}
        for case in fourth_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["reviewer"] == "gemini_vertex" for case in fourth_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["source_report"] == FOURTH_GEMINI_ADVISORY_REPORT
        for case in fourth_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["raw_report"] == FOURTH_GEMINI_ADVISORY_RAW
        for case in fourth_batch
    )
    assert (
        sum(
            case["review"]["ai_advisory_draft"]["exact_match_with_ai_draft"]
            for case in fourth_batch
        )
        == 34
    )
    assert fourth_advisory["comparison_summary"] == {
        "cases": 50,
        "exact_matches_with_codex_draft": 34,
        "differences_from_codex_draft": 16,
    }
    assert all(case["review"]["first_reviewer"] == "tim" for case in approved_ui_batch)
    assert all(case["review"]["blind_reviewer"] == "" for case in approved_ui_batch)
    assert (
        sum(case["review"]["expected_source"] == "human_first_pass" for case in approved_ui_batch)
        == 90
    )
    assert (
        sum(case["review"]["expected_source"] == "human_adjudication" for case in approved_ui_batch)
        == 35
    )
    assert sum(case["review"]["adjudicator"] == "tim" for case in approved_ui_batch) == 35
    assert sum(case["review"]["adjudicator"] == "" for case in approved_ui_batch) == 90
    assert sum(case["review"]["disagreement"] for case in approved_ui_batch) == 35
    assert all(
        case["review"]["ai_advisory"]["reviewer"] == "gemini_vertex" for case in approved_ui_batch
    )
    assert (
        sum(case["review"]["ai_advisory"]["decision"] == "accepted" for case in approved_ui_batch)
        == 95
    )
    assert (
        sum(case["review"]["ai_advisory"]["decision"] == "rejected" for case in approved_ui_batch)
        == 30
    )
    assert all(case["review"]["ai_advisory"]["decision_by"] == "tim" for case in approved_ui_batch)
    assert all(
        case["review"]["ai_advisory"]["decision_date"] == "2026-07-06" for case in approved_ui_batch
    )
    rejected_ui_ids = {
        case["id"]
        for case in approved_ui_batch
        if case["review"]["ai_advisory"]["decision"] == "rejected"
    }
    accepted_disagreement_ui_ids = {
        case["id"]
        for case in approved_ui_batch
        if case["review"]["ai_advisory"]["decision"] == "accepted"
        and case["review"]["disagreement"]
    }
    assert rejected_ui_ids == UI_CODEX_DECISION_IDS
    assert accepted_disagreement_ui_ids == UI_GEMINI_DECISION_IDS
    for case in approved_ui_batch:
        row = ui_comparison_by_id[case["id"]]
        review = case["review"]
        if row["exact_match_with_codex_draft"]:
            assert review["expected"] == row["codex_expected"]
            assert review["expected_source"] == "human_first_pass"
            assert review["ai_advisory"]["decision"] == "accepted"
            assert review["ai_advisory"]["exact_match_with_first_pass"] is True
        elif case["id"] in UI_GEMINI_DECISION_IDS:
            assert review["expected"] == row["gemini_expected"]
            assert review["expected_source"] == "human_adjudication"
            assert review["ai_advisory"]["decision"] == "accepted"
            assert review["ai_advisory"]["exact_match_with_first_pass"] is False
        else:
            assert case["id"] in UI_CODEX_DECISION_IDS
            assert review["expected"] == row["codex_expected"]
            assert review["expected_source"] == "human_adjudication"
            assert review["ai_advisory"]["decision"] == "rejected"
            assert review["ai_advisory"]["exact_match_with_first_pass"] is False
    assert all(
        case["review"]["ai_advisory_draft"]["reviewer"] == "gemini_vertex" for case in ui_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["source_report"] == UI_GEMINI_ADVISORY_FIRST_REPORT
        for case in ui_first_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["raw_report"] == UI_GEMINI_ADVISORY_FIRST_RAW
        for case in ui_first_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["source_report"] == UI_GEMINI_ADVISORY_SECOND_REPORT
        for case in ui_second_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["raw_report"] == UI_GEMINI_ADVISORY_SECOND_RAW
        for case in ui_second_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["source_report"] == UI_GEMINI_ADVISORY_THIRD_REPORT
        for case in ui_third_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["raw_report"] == UI_GEMINI_ADVISORY_THIRD_RAW
        for case in ui_third_batch
    )
    assert (
        sum(
            case["review"]["ai_advisory_draft"]["exact_match_with_ai_draft"]
            for case in ui_first_batch
        )
        == 43
    )
    assert (
        sum(
            case["review"]["ai_advisory_draft"]["exact_match_with_ai_draft"]
            for case in ui_second_batch
        )
        == 29
    )
    assert ui_first_advisory["comparison_summary"] == {
        "cases": 50,
        "exact_matches_with_codex_draft": 43,
        "differences_from_codex_draft": 7,
    }
    assert ui_second_advisory["comparison_summary"] == {
        "cases": 50,
        "exact_matches_with_codex_draft": 29,
        "differences_from_codex_draft": 21,
    }
    assert (
        sum(
            case["review"]["ai_advisory_draft"]["exact_match_with_ai_draft"]
            for case in ui_third_batch
        )
        == 18
    )
    assert ui_third_advisory["comparison_summary"] == {
        "cases": 25,
        "exact_matches_with_codex_draft": 18,
        "differences_from_codex_draft": 7,
    }
    assert {case["review"]["status"] for case in formal_batch} == {"approved"}
    assert all(case["review"]["expected"] for case in formal_batch)
    assert all(case["review"]["acceptable"] == [] for case in formal_batch)
    assert (
        sum(case["review"]["expected_source"] == "human_first_pass" for case in formal_batch) == 91
    )
    assert (
        sum(case["review"]["expected_source"] == "human_adjudication" for case in formal_batch) == 9
    )
    assert all(case["review"]["first_reviewer"] == "tim" for case in formal_batch)
    assert all(case["review"]["blind_reviewer"] == "" for case in formal_batch)
    assert sum(case["review"]["adjudicator"] == "tim" for case in formal_batch) == 9
    assert sum(case["review"]["adjudicator"] == "" for case in formal_batch) == 91
    assert sum(case["review"]["disagreement"] for case in formal_batch) == 9
    assert all(
        case["review"]["ai_advisory"]["reviewer"] == "gemini_vertex" for case in formal_batch
    )
    assert (
        sum(case["review"]["ai_advisory"]["decision"] == "accepted" for case in formal_batch) == 98
    )
    assert (
        sum(case["review"]["ai_advisory"]["decision"] == "rejected" for case in formal_batch) == 2
    )
    assert all(case["review"]["ai_advisory"]["decision_by"] == "tim" for case in formal_batch)
    assert all(
        case["review"]["ai_advisory"]["decision_date"] == "2026-07-07" for case in formal_batch
    )
    rejected_formal_ids = {
        case["id"]
        for case in formal_batch
        if case["review"]["ai_advisory"]["decision"] == "rejected"
    }
    accepted_disagreement_formal_ids = {
        case["id"]
        for case in formal_batch
        if case["review"]["ai_advisory"]["decision"] == "accepted"
        and case["review"]["disagreement"]
    }
    assert rejected_formal_ids == FORMAL_CODEX_DECISION_IDS
    assert accepted_disagreement_formal_ids == FORMAL_GEMINI_DECISION_IDS
    for case in formal_batch:
        row = formal_comparison_by_id[case["id"]]
        review = case["review"]
        if row["exact_match_with_codex_draft"]:
            assert review["expected"] == row["codex_expected"]
            assert review["expected_source"] == "human_first_pass"
            assert review["ai_advisory"]["decision"] == "accepted"
            assert review["ai_advisory"]["exact_match_with_first_pass"] is True
        elif case["id"] in FORMAL_GEMINI_DECISION_IDS:
            assert review["expected"] == row["gemini_expected"]
            assert review["expected_source"] == "human_adjudication"
            assert review["ai_advisory"]["decision"] == "accepted"
            assert review["ai_advisory"]["exact_match_with_first_pass"] is False
        else:
            assert case["id"] in FORMAL_CODEX_DECISION_IDS
            assert review["expected"] == row["codex_expected"]
            assert review["expected_source"] == "human_adjudication"
            assert review["ai_advisory"]["decision"] == "rejected"
            assert review["ai_advisory"]["exact_match_with_first_pass"] is False
    assert all(
        case["review"]["ai_advisory_draft"]["reviewer"] == "gemini_vertex" for case in formal_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["source_report"] == FORMAL_GEMINI_ADVISORY_FIRST_REPORT
        for case in formal_first_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["raw_report"] == FORMAL_GEMINI_ADVISORY_FIRST_RAW
        for case in formal_first_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["source_report"] == FORMAL_GEMINI_ADVISORY_SECOND_REPORT
        for case in formal_second_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["raw_report"] == FORMAL_GEMINI_ADVISORY_SECOND_RAW
        for case in formal_second_batch
    )
    for case in formal_batch:
        comparison = formal_comparison_by_id[case["id"]]
        assert (
            case["review"]["ai_advisory_draft"]["exact_match_with_ai_draft"]
            is comparison["exact_match_with_codex_draft"]
        )
    assert (
        sum(
            case["review"]["ai_advisory_draft"]["exact_match_with_ai_draft"]
            for case in formal_first_batch
        )
        == 43
    )
    assert (
        sum(
            case["review"]["ai_advisory_draft"]["exact_match_with_ai_draft"]
            for case in formal_second_batch
        )
        == 48
    )
    assert formal_first_advisory["comparison_summary"] == {
        "cases": 50,
        "exact_matches_with_codex_draft": 43,
        "differences_from_codex_draft": 7,
    }
    assert formal_second_advisory["comparison_summary"] == {
        "cases": 50,
        "exact_matches_with_codex_draft": 48,
        "differences_from_codex_draft": 2,
    }
    assert {case["review"]["status"] for case in approved_social_mixed_batch} == {
        "approved",
    }
    assert all(case["review"]["expected"] for case in approved_social_mixed_batch)
    assert all(case["review"]["acceptable"] == [] for case in approved_social_mixed_batch)
    assert (
        sum(case["review"]["expected_source"] == "human_first_pass" for case in social_batch) == 59
    )
    assert (
        sum(case["review"]["expected_source"] == "human_adjudication" for case in social_batch)
        == 16
    )
    assert (
        sum(case["review"]["expected_source"] == "human_first_pass" for case in mixed_batch) == 18
    )
    assert (
        sum(case["review"]["expected_source"] == "human_adjudication" for case in mixed_batch) == 7
    )
    assert all(case["review"]["first_reviewer"] == "tim" for case in approved_social_mixed_batch)
    assert all(case["review"]["blind_reviewer"] == "" for case in approved_social_mixed_batch)
    assert sum(case["review"]["adjudicator"] == "tim" for case in social_batch) == 16
    assert sum(case["review"]["adjudicator"] == "" for case in social_batch) == 59
    assert sum(case["review"]["adjudicator"] == "tim" for case in mixed_batch) == 7
    assert sum(case["review"]["adjudicator"] == "" for case in mixed_batch) == 18
    assert sum(case["review"]["disagreement"] for case in social_batch) == 16
    assert sum(case["review"]["disagreement"] for case in mixed_batch) == 7
    assert all(
        case["review"]["ai_advisory"]["reviewer"] == "gemini_vertex"
        for case in approved_social_mixed_batch
    )
    assert (
        sum(case["review"]["ai_advisory"]["decision"] == "accepted" for case in social_batch) == 61
    )
    assert (
        sum(case["review"]["ai_advisory"]["decision"] == "rejected" for case in social_batch) == 14
    )
    assert (
        sum(case["review"]["ai_advisory"]["decision"] == "accepted" for case in mixed_batch) == 19
    )
    assert sum(case["review"]["ai_advisory"]["decision"] == "rejected" for case in mixed_batch) == 6
    assert all(
        case["review"]["ai_advisory"]["decision_by"] == "tim"
        for case in approved_social_mixed_batch
    )
    assert all(
        case["review"]["ai_advisory"]["decision_date"] in {"2026-07-07", "2026-07-16"}
        for case in approved_social_mixed_batch
    )
    rejected_social_mixed_ids = {
        case["id"]
        for case in approved_social_mixed_batch
        if case["review"]["ai_advisory"]["decision"] == "rejected"
    }
    accepted_disagreement_social_mixed_ids = {
        case["id"]
        for case in approved_social_mixed_batch
        if case["review"]["ai_advisory"]["decision"] == "accepted"
        and case["review"]["disagreement"]
    }
    assert rejected_social_mixed_ids == SOCIAL_MIXED_CODEX_DECISION_IDS | {"social-daily-0038"}
    assert accepted_disagreement_social_mixed_ids == SOCIAL_MIXED_GEMINI_DECISION_IDS
    for case in social_batch:
        row = social_comparison_by_id[case["id"]]
        review = case["review"]
        if case["id"] == "social-daily-0038":
            assert review["expected"] == "物業管理處通知明天停水。"
            assert review["expected_source"] == "human_adjudication"
            assert review["ai_advisory"]["decision"] == "rejected"
            continue
        if row["exact_match_with_codex_draft"]:
            assert review["expected"] == row["codex_expected"]
            assert review["expected_source"] == "human_first_pass"
            assert review["ai_advisory"]["decision"] == "accepted"
            assert review["ai_advisory"]["exact_match_with_first_pass"] is True
        elif case["id"] in SOCIAL_MIXED_GEMINI_DECISION_IDS:
            assert review["expected"] == row["gemini_expected"]
            assert review["expected_source"] == "human_adjudication"
            assert review["ai_advisory"]["decision"] == "accepted"
            assert review["ai_advisory"]["exact_match_with_first_pass"] is False
        else:
            assert case["id"] in SOCIAL_MIXED_CODEX_DECISION_IDS
            assert review["expected"] == row["codex_expected"]
            assert review["expected_source"] == "human_adjudication"
            assert review["ai_advisory"]["decision"] == "rejected"
            assert review["ai_advisory"]["exact_match_with_first_pass"] is False
    for case in mixed_batch:
        row = mixed_comparison_by_id[case["id"]]
        review = case["review"]
        if row["exact_match_with_codex_draft"]:
            assert review["expected"] == row["codex_expected"]
            assert review["expected_source"] == "human_first_pass"
            assert review["ai_advisory"]["decision"] == "accepted"
            assert review["ai_advisory"]["exact_match_with_first_pass"] is True
        elif case["id"] in SOCIAL_MIXED_GEMINI_DECISION_IDS:
            assert review["expected"] == row["gemini_expected"]
            assert review["expected_source"] == "human_adjudication"
            assert review["ai_advisory"]["decision"] == "accepted"
            assert review["ai_advisory"]["exact_match_with_first_pass"] is False
        else:
            assert case["id"] in SOCIAL_MIXED_CODEX_DECISION_IDS
            assert review["expected"] == row["codex_expected"]
            assert review["expected_source"] == "human_adjudication"
            assert review["ai_advisory"]["decision"] == "rejected"
            assert review["ai_advisory"]["exact_match_with_first_pass"] is False
    assert all(
        case["review"]["ai_advisory_draft"]["reviewer"] == "gemini_vertex"
        for case in approved_social_mixed_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["source_report"] == SOCIAL_GEMINI_ADVISORY_FIRST_REPORT
        for case in social_first_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["raw_report"] == SOCIAL_GEMINI_ADVISORY_FIRST_RAW
        for case in social_first_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["source_report"] == SOCIAL_GEMINI_ADVISORY_SECOND_REPORT
        for case in social_second_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["raw_report"] == SOCIAL_GEMINI_ADVISORY_SECOND_RAW
        for case in social_second_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["source_report"] == MIXED_GEMINI_ADVISORY_REPORT
        for case in mixed_batch
    )
    assert all(
        case["review"]["ai_advisory_draft"]["raw_report"] == MIXED_GEMINI_ADVISORY_RAW
        for case in mixed_batch
    )
    for case in social_batch:
        comparison = social_comparison_by_id[case["id"]]
        assert (
            case["review"]["ai_advisory_draft"]["exact_match_with_ai_draft"]
            is comparison["exact_match_with_codex_draft"]
        )
    for case in mixed_batch:
        comparison = mixed_comparison_by_id[case["id"]]
        assert (
            case["review"]["ai_advisory_draft"]["exact_match_with_ai_draft"]
            is comparison["exact_match_with_codex_draft"]
        )
    assert (
        sum(
            case["review"]["ai_advisory_draft"]["exact_match_with_ai_draft"]
            for case in social_first_batch
        )
        == 39
    )
    assert (
        sum(
            case["review"]["ai_advisory_draft"]["exact_match_with_ai_draft"]
            for case in social_second_batch
        )
        == 21
    )
    assert (
        sum(
            case["review"]["ai_advisory_draft"]["exact_match_with_ai_draft"] for case in mixed_batch
        )
        == 18
    )
    assert social_first_advisory["comparison_summary"] == {
        "cases": 50,
        "exact_matches_with_codex_draft": 39,
        "differences_from_codex_draft": 11,
    }
    assert social_second_advisory["comparison_summary"] == {
        "cases": 25,
        "exact_matches_with_codex_draft": 21,
        "differences_from_codex_draft": 4,
    }
    assert mixed_advisory["comparison_summary"] == {
        "cases": 25,
        "exact_matches_with_codex_draft": 18,
        "differences_from_codex_draft": 7,
    }
    assert all(case["source"]["type"] == "maintainer-written short cases" for case in cases)
    assert all(case["ai_draft"]["generated_by"] == "ai_assistant" for case in cases)
    assert all(case["ai_draft"]["promotion_allowed"] is False for case in cases)
    assert all(case["ai_draft"]["expected"] for case in cases)
    assert all(case["ai_draft"]["source_report"] == FIRST_DRAFT_REPORT for case in first_batch)
    assert all(case["ai_draft"]["source_report"] == SECOND_DRAFT_REPORT for case in second_batch)
    assert all(case["ai_draft"]["source_report"] == THIRD_DRAFT_REPORT for case in third_batch)
    assert all(case["ai_draft"]["source_report"] == FOURTH_DRAFT_REPORT for case in fourth_batch)
    assert all(
        case["ai_draft"]["source_report"] == UI_DRAFT_REPORT
        for case in ui_first_batch + ui_second_batch
    )
    assert all(
        case["ai_draft"]["source_report"] == UI_DRAFT_REPORT_SECOND for case in ui_third_batch
    )
    assert all(case["ai_draft"]["source_report"] == FORMAL_DRAFT_REPORT for case in formal_batch)
    assert all(case["ai_draft"]["source_report"] == SOCIAL_DRAFT_REPORT for case in social_batch)

    corrections = json.loads(GROUND_TRUTH_CORRECTIONS.read_text(encoding="utf-8"))
    assert {case["id"] for case in corrections["cases"]} == GROUND_TRUTH_CORRECTION_IDS
    assert corrections["summary"]["corrected_cases"] == 3
    assert all(case["ai_draft"]["source_report"] == MIXED_DRAFT_REPORT for case in mixed_batch)
    assert len({case["id"] for case in cases}) == len(cases)


def test_annotation_status_script_reports_remaining_target() -> None:
    result = subprocess.run(
        [sys.executable, str(STATUS_SCRIPT), "--format", "json"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr

    payload = json.loads(result.stdout)
    assert payload["errors"] == []
    assert payload["summary"]["target_total"] == 500
    assert payload["summary"]["collected_total"] == 500
    assert payload["summary"]["raw_approved_total"] == 500
    assert payload["summary"]["approved_total"] == 500
    assert payload["summary"]["remaining_to_collect"] == 0
    assert payload["summary"]["remaining_to_approve"] == 0
    assert payload["summary"]["review_status"] == {"approved": 500}


def test_blind_review_packet_hides_first_pass_expected(tmp_path: Path) -> None:
    packet_backlog = load_backlog()
    for case in packet_backlog["cases"]:
        case["review"]["status"] = "needs_blind_review"
        case["review"]["expected"] = case["ai_draft"]["expected"]
    backlog_path = tmp_path / "annotation-backlog.json"
    backlog_path.write_text(
        json.dumps(packet_backlog, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    output = tmp_path / "blind-review.md"
    selected_cases = [case for case in packet_backlog["cases"] if case["batch"] == "it-api-cli"]
    result = subprocess.run(
        [
            sys.executable,
            str(PACKET_SCRIPT),
            "--backlog",
            str(backlog_path),
            "--batch",
            "it-api-cli",
            "--generated-date",
            "2026-07-05",
            "--output",
            str(output),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr

    content = output.read_text(encoding="utf-8")
    assert "# Annotation Blind Review Packet (2026-07-05)" in content
    assert "Cases: 175" in content
    assert "Status filter: `needs_blind_review`" in content
    assert "Batch filter: `it-api-cli`" in content
    assert "ai_draft" not in content
    assert "first_reviewer" not in content
    assert "review.expected" not in content
    for case in selected_cases:
        assert f"### {case['id']}" in content
        assert case["input"] in content
        assert case["review"]["expected"] not in content
        assert case["ai_draft"]["notes"] not in content
    assert "ui-i18n-0001" not in content


def test_blind_review_packet_rejects_empty_selection(tmp_path: Path) -> None:
    result = subprocess.run(
        [
            sys.executable,
            str(PACKET_SCRIPT),
            "--batch",
            "missing-batch",
            "--output",
            str(tmp_path / "blind-review.md"),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 1
    assert "No cases matched" in result.stderr


def backlog_with_cases(cases: list[dict[str, Any]]) -> dict[str, Any]:
    backlog = load_backlog()
    backlog["cases"] = cases
    return backlog


def approved_case(**overrides: Any) -> dict[str, Any]:
    case: dict[str, Any] = {
        "id": "it-api-cli-0001",
        "batch": "it-api-cli",
        "domain": "it",
        "input": "这个函数会抛出异常。",
        "risk": "over_conversion_guard",
        "source": {
            "type": "maintainer-written short cases",
            "citation": "",
            "license": "CC-BY-4.0",
        },
        "review": {
            "status": "approved",
            "expected": "這個函式會拋出例外。",
            "acceptable": [],
            "expected_source": "human_first_pass",
            "first_reviewer": "reviewer-a",
            "blind_reviewer": "reviewer-b",
            "adjudicator": "",
            "disagreement": False,
        },
    }
    for key, value in overrides.items():
        if key == "review":
            case["review"].update(value)
        else:
            case[key] = value
    return case


def accepted_ai_advisory() -> dict[str, Any]:
    return {
        "reviewer": "gemini_vertex",
        "source_report": "docs/reports/annotation-gemini-vertex-advisory-2026-07-05.md",
        "raw_report": "docs/reports/annotation-gemini-vertex-advisory-2026-07-05.json",
        "decision": "accepted",
        "decision_by": "reviewer-a",
        "decision_date": "2026-07-05",
        "exact_match_with_first_pass": True,
    }


def run_status_for_backlog(
    tmp_path: Path,
    backlog: dict[str, Any],
) -> subprocess.CompletedProcess[str]:
    path = tmp_path / "annotation-backlog.json"
    path.write_text(json.dumps(backlog, ensure_ascii=False, indent=2), encoding="utf-8")
    return subprocess.run(
        [sys.executable, str(STATUS_SCRIPT), "--backlog", str(path), "--format", "json"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )


def run_check_for_backlog(
    tmp_path: Path,
    backlog: dict[str, Any],
    *extra_args: str,
) -> subprocess.CompletedProcess[str]:
    path = tmp_path / "annotation-backlog.json"
    output_json = tmp_path / "promotion-gate.json"
    output_md = tmp_path / "promotion-gate.md"
    path.write_text(json.dumps(backlog, ensure_ascii=False, indent=2), encoding="utf-8")
    return subprocess.run(
        [
            sys.executable,
            str(CHECK_SCRIPT),
            "--backlog",
            str(path),
            "--output-json",
            str(output_json),
            "--output-md",
            str(output_md),
            "--generated-date",
            "2026-07-05",
            *extra_args,
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )


def test_promotion_gate_reports_ready_mismatch_and_skipped_cases(tmp_path: Path) -> None:
    not_ready = approved_case(id="skip-0001", input="市政府", review={"status": "needs_first_pass"})
    ready = approved_case(id="ready-0001", input="市政府", review={"expected": "市政府"})
    mismatch = approved_case(id="mismatch-0001", input="市政府", review={"expected": "錯誤"})
    result = run_check_for_backlog(
        tmp_path,
        backlog_with_cases([not_ready, ready, mismatch]),
    )

    assert result.returncode == 0, result.stdout + result.stderr

    payload = json.loads((tmp_path / "promotion-gate.json").read_text(encoding="utf-8"))
    assert payload["generated_date"] == "2026-07-05"
    assert payload["summary"]["approved_checked"] == 2
    assert payload["summary"]["skipped_not_promotion_ready"] == 1
    assert payload["summary"]["promotion_ready"] == 1
    assert payload["summary"]["needs_zhtw_fix"] == 1

    by_id = {case["id"]: case for case in payload["cases"]}
    assert by_id["ready-0001"]["status"] == "promotion_ready"
    assert by_id["mismatch-0001"]["status"] == "needs_zhtw_fix"
    assert "mismatch-0001" in (tmp_path / "promotion-gate.md").read_text(encoding="utf-8")


def test_current_approved_backlog_is_promotion_ready(tmp_path: Path) -> None:
    result = run_check_for_backlog(tmp_path, load_backlog())

    assert result.returncode == 0, result.stdout + result.stderr

    payload = json.loads((tmp_path / "promotion-gate.json").read_text(encoding="utf-8"))
    assert payload["summary"]["approved_checked"] == 500
    assert payload["summary"]["promotion_ready"] == 500
    assert payload["summary"]["needs_zhtw_fix"] == 0
    assert payload["summary"]["expected_not_idempotent"] == 0


def test_promotion_gate_can_fail_on_mismatch(tmp_path: Path) -> None:
    result = run_check_for_backlog(
        tmp_path,
        backlog_with_cases(
            [approved_case(id="mismatch-0001", input="市政府", review={"expected": "錯誤"})]
        ),
        "--fail-on-mismatch",
    )

    assert result.returncode == 1
    payload = json.loads((tmp_path / "promotion-gate.json").read_text(encoding="utf-8"))
    assert payload["summary"]["needs_zhtw_fix"] == 1


def test_annotation_status_counts_only_promotion_ready_approved_cases(tmp_path: Path) -> None:
    result = run_status_for_backlog(tmp_path, backlog_with_cases([approved_case()]))

    assert result.returncode == 0, result.stdout + result.stderr

    payload = json.loads(result.stdout)
    assert payload["errors"] == []
    assert payload["summary"]["raw_approved_total"] == 1
    assert payload["summary"]["approved_total"] == 1
    assert payload["summary"]["remaining_to_approve"] == 499


def test_annotation_status_accepts_ai_advisory_approval_path(tmp_path: Path) -> None:
    result = run_status_for_backlog(
        tmp_path,
        backlog_with_cases(
            [
                approved_case(
                    review={
                        "blind_reviewer": "",
                        "ai_advisory": accepted_ai_advisory(),
                    }
                )
            ]
        ),
    )

    assert result.returncode == 0, result.stdout + result.stderr

    payload = json.loads(result.stdout)
    assert payload["errors"] == []
    assert payload["summary"]["raw_approved_total"] == 1
    assert payload["summary"]["approved_total"] == 1


def test_annotation_status_accepts_rejected_ai_advisory_after_adjudication(
    tmp_path: Path,
) -> None:
    advisory = accepted_ai_advisory()
    advisory["decision"] = "rejected"
    advisory["exact_match_with_first_pass"] = False
    result = run_status_for_backlog(
        tmp_path,
        backlog_with_cases(
            [
                approved_case(
                    review={
                        "blind_reviewer": "",
                        "expected_source": "human_adjudication",
                        "adjudicator": "reviewer-a",
                        "disagreement": True,
                        "ai_advisory": advisory,
                    }
                )
            ]
        ),
    )

    assert result.returncode == 0, result.stdout + result.stderr

    payload = json.loads(result.stdout)
    assert payload["errors"] == []
    assert payload["summary"]["raw_approved_total"] == 1
    assert payload["summary"]["approved_total"] == 1


def test_annotation_status_rejects_empty_expected(tmp_path: Path) -> None:
    result = run_status_for_backlog(
        tmp_path,
        backlog_with_cases([approved_case(review={"expected": ""})]),
    )

    assert result.returncode == 1
    payload = json.loads(result.stdout)
    assert payload["summary"]["raw_approved_total"] == 1
    assert payload["summary"]["approved_total"] == 0
    assert any("empty expected" in error for error in payload["errors"])


def test_annotation_status_rejects_non_human_expected_source(tmp_path: Path) -> None:
    result = run_status_for_backlog(
        tmp_path,
        backlog_with_cases([approved_case(review={"expected_source": "zhtw_output"})]),
    )

    assert result.returncode == 1
    payload = json.loads(result.stdout)
    assert payload["summary"]["approved_total"] == 0
    assert any("expected_source is not human-reviewed" in error for error in payload["errors"])


def test_annotation_status_rejects_same_reviewer(tmp_path: Path) -> None:
    result = run_status_for_backlog(
        tmp_path,
        backlog_with_cases([approved_case(review={"blind_reviewer": "reviewer-a"})]),
    )

    assert result.returncode == 1
    payload = json.loads(result.stdout)
    assert payload["summary"]["approved_total"] == 0
    assert any("must differ" in error for error in payload["errors"])


def test_annotation_status_rejects_missing_review_path(tmp_path: Path) -> None:
    result = run_status_for_backlog(
        tmp_path,
        backlog_with_cases([approved_case(review={"blind_reviewer": ""})]),
    )

    assert result.returncode == 1
    payload = json.loads(result.stdout)
    assert payload["summary"]["approved_total"] == 0
    assert any("missing blind_reviewer or ai_advisory" in error for error in payload["errors"])


def test_annotation_status_rejects_rejected_ai_advisory_without_adjudication(
    tmp_path: Path,
) -> None:
    advisory = accepted_ai_advisory()
    advisory["decision"] = "rejected"
    result = run_status_for_backlog(
        tmp_path,
        backlog_with_cases(
            [
                approved_case(
                    review={
                        "blind_reviewer": "",
                        "ai_advisory": advisory,
                    }
                )
            ]
        ),
    )

    assert result.returncode == 1
    payload = json.loads(result.stdout)
    assert payload["summary"]["approved_total"] == 0
    assert any(
        "rejected ai_advisory requires human_adjudication" in error for error in payload["errors"]
    )


def test_annotation_status_rejects_disagreement_without_adjudicator(tmp_path: Path) -> None:
    result = run_status_for_backlog(
        tmp_path,
        backlog_with_cases([approved_case(review={"disagreement": True})]),
    )

    assert result.returncode == 1
    payload = json.loads(result.stdout)
    assert payload["summary"]["approved_total"] == 0
    assert any("missing adjudicator" in error for error in payload["errors"])
