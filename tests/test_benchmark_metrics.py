"""Tests for deterministic benchmark metrics and statistics."""

from __future__ import annotations

from scripts.benchmark_metrics import (
    align_edits,
    canonical_json_bytes,
    canonical_sha256,
    changed_span_metrics,
    edit_span_payload,
    paired_comparison,
    paired_power_analysis,
)
from scripts.run_accuracy_benchmark import summarize_engine


def test_canonical_json_is_byte_identical_across_key_order() -> None:
    left = {"b": [2, 1], "a": "臺灣"}
    right = {"a": "臺灣", "b": [2, 1]}

    assert canonical_json_bytes(left) == canonical_json_bytes(right)
    assert canonical_sha256(left) == canonical_sha256(right)
    assert canonical_json_bytes(left) == b'{"a":"\xe8\x87\xba\xe7\x81\xa3","b":[2,1]}\n'


def test_alignment_covers_insert_delete_substitute() -> None:
    assert edit_span_payload("ab", "acb") == [
        {
            "operation": "insert",
            "source_start": 1,
            "source_end": 1,
            "target_start": 1,
            "target_end": 2,
            "source_text": "",
            "target_text": "c",
        }
    ]
    assert edit_span_payload("abc", "ac") == [
        {
            "operation": "delete",
            "source_start": 1,
            "source_end": 2,
            "target_start": 1,
            "target_end": 1,
            "source_text": "b",
            "target_text": "",
        }
    ]
    assert edit_span_payload("后", "後") == [
        {
            "operation": "substitute",
            "source_start": 0,
            "source_end": 1,
            "target_start": 0,
            "target_end": 1,
            "source_text": "后",
            "target_text": "後",
        }
    ]


def test_repeated_character_alignment_has_one_deterministic_result() -> None:
    expected = [
        {
            "operation": "delete",
            "source_start": 0,
            "source_end": 1,
            "target_start": 0,
            "target_end": 0,
            "source_text": "a",
            "target_text": "",
        }
    ]

    assert edit_span_payload("aaaa", "aaa") == expected
    assert all(edit_span_payload("aaaa", "aaa") == expected for _ in range(20))


def test_changed_span_metrics_penalize_extra_edits() -> None:
    exact = changed_span_metrics("开发软件", "開發軟體", "開發軟體")
    extra = changed_span_metrics("开发软件", "開發軟體", "開發軟件")

    assert exact["precision"] == exact["recall"] == exact["f1"] == 1.0
    assert extra["recall"] < 1.0
    assert extra["f1"] < 1.0


def test_paired_comparison_reports_tie_and_winner() -> None:
    tie = paired_comparison([True, True, False, False], [True, False, True, False], rounds=1000)
    winner = paired_comparison([True] * 100, [True] * 50 + [False] * 50, rounds=2000)

    assert tie["absolute_delta"] == 0
    assert tie["mcnemar_exact_p"] == 1.0
    assert tie["result"] == "statistical_tie"
    assert winner["delta_ci_95"]["low"] > 0
    assert winner["result"] == "winner"


def test_power_analysis_is_deterministic_and_requires_selected_size() -> None:
    first = paired_power_analysis(discordant_rate=0.10)
    second = paired_power_analysis(discordant_rate=0.10)

    assert first == second
    assert first["required_cases"] > 600
    assert first["power_at_1200"] > first["power_at_600"]
    assert first["target_power"] == 0.80


def test_alignment_result_is_immutable_value_object() -> None:
    edit = align_edits("里", "裡")[0]

    assert edit.operation == "substitute"


def test_summary_counts_case_errors_as_misses_and_reports_risk_metrics() -> None:
    def row(
        *,
        domain: str,
        risk: str,
        accepted: bool,
        error_category: str = "",
        severity: str = "",
    ) -> dict[str, object]:
        return {
            "domain": domain,
            "risk": risk,
            "input": "开发",
            "expected": "開發",
            "issue_tags": ["regional_term"],
            "severity": severity,
            "evaluations": {
                "zhtw": {
                    "available": True,
                    "error": "failure" if error_category else "",
                    "error_category": error_category,
                    "output": "開發" if accepted else "",
                    "normalized_output": "開發" if accepted else "",
                    "primary_exact": accepted,
                    "acceptable_exact": False,
                    "accepted": accepted,
                    "idempotent": accepted,
                }
            },
        }

    rows = [
        row(domain="it", risk="candidate_gap", accepted=True),
        row(
            domain="it",
            risk="over_conversion_guard",
            accepted=False,
            error_category="exception",
            severity="P0",
        ),
        row(domain="formal", risk="baseline_guard", accepted=True),
    ]

    summary = summarize_engine(rows, "zhtw")  # type: ignore[arg-type]

    assert summary["available_cases"] == 3
    assert summary["accepted"] == 2
    assert summary["misses"] == 1
    assert summary["errors_by_category"] == {"exception": 1}
    assert summary["p0_error_count"] == 1
    assert summary["severe_error_rate"] == 1 / 3
    assert summary["conversion_recall"] == 1.0
    assert summary["over_conversion_guard_accuracy"] == 0.0
    assert summary["baseline_guard_accuracy"] == 1.0
    assert summary["macro_domain_accuracy"] == 0.75
