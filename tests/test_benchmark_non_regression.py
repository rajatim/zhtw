"""Tests for current-candidate benchmark floors."""

from __future__ import annotations

import copy

import pytest

from scripts.validate_benchmark_non_regression import ValidationError, validate_reports


def single_report(exact: int = 8, idempotent: int = 9, f1: float = 0.8) -> dict:
    return {
        "dataset": "fixture",
        "manifest_sha256": "a" * 64,
        "normalized_sha256": "b" * 64,
        "upstream_revision": "c" * 40,
        "scores": {
            "total_cases": 10,
            "exact": exact,
            "idempotent": idempotent,
            "changed_span": {"f1": f1},
        },
    }


def paired_report(zhtw_exact: int = 8, competitor_exact: int = 7) -> dict:
    report = single_report()
    report.pop("scores")
    report["engines"] = {
        "zhtw": {
            "version": "4.4.3",
            "total_cases": 10,
            "exact": zhtw_exact,
            "idempotent": 9,
            "changed_span": {"f1": 0.8},
        },
        "locked": {
            "version": "1.0.0",
            "total_cases": 10,
            "exact": competitor_exact,
            "idempotent": 10,
        },
    }
    return report


def test_single_report_allows_improvement() -> None:
    validate_reports(single_report(), single_report(exact=9, idempotent=10, f1=0.9))


@pytest.mark.parametrize(
    ("current", "message"),
    [
        (single_report(exact=7), "scores.exact regressed"),
        (single_report(idempotent=8), "scores.idempotent regressed"),
        (single_report(f1=0.7), "changed_span.f1 regressed"),
    ],
)
def test_single_report_rejects_regression(current: dict, message: str) -> None:
    with pytest.raises(ValidationError, match=message):
        validate_reports(single_report(), current)


def test_report_rejects_dataset_drift() -> None:
    current = single_report()
    current["manifest_sha256"] = "d" * 64

    with pytest.raises(ValidationError, match="Report identity changed"):
        validate_reports(single_report(), current)


def test_paired_report_allows_zhtw_version_and_score_improvement() -> None:
    current = paired_report(zhtw_exact=9)
    current["engines"]["zhtw"]["version"] = "4.4.4"

    validate_reports(paired_report(), current)


def test_paired_report_rejects_competitor_drift() -> None:
    current = copy.deepcopy(paired_report())
    current["engines"]["locked"]["exact"] = 6

    with pytest.raises(ValidationError, match="Locked competitor output changed"):
        validate_reports(paired_report(), current)
