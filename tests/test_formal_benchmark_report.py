"""Tests for the formal aggregate market report."""

from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from scripts.build_formal_benchmark_report import build_report

ROOT = Path(__file__).resolve().parents[1]


def load(name: str) -> dict[str, object]:
    return json.loads((ROOT / "docs/reports" / name).read_text(encoding="utf-8"))


def inputs() -> tuple[dict[str, object], ...]:
    return (
        load("blind-v2-benchmark-2026-07-31.json"),
        load("ud-gsd-benchmark-2026-07-31.json"),
        load("naer-terms-benchmark-2026-07-31.json"),
        load("aosp-framework-paired-ui-v1-benchmark-2026-07-31.json"),
        load("vscode-paired-ui-v1-benchmark-2026-07-31.json"),
        load("firefox-paired-ui-v1-benchmark-2026-07-31.json"),
    )


def test_formal_report_uses_blind_v2_as_the_only_primary_endpoint() -> None:
    report = build_report(*inputs())

    assert report["decision"] == "scoped_winner"
    assert report["primary_endpoint"]["dataset"] == "blind-v2"
    assert len(report["secondary_tracks"]) == 5
    assert report["cross_track_assessment"]["status"] == (
        "mixed_secondary_evidence_no_primary_conflict"
    )
    assert report["governance"]["maintainer_claim_confirmation"]["status"] == "confirmed"
    assert report["governance"]["detailed_rows_read"] is False
    assert report["governance"]["private_detailed_audit"]["status"] == "completed"
    assert report["governance"]["external_hosted_public_reproduction"]["status"] == "passed"
    assert (
        report["governance"]["independent_third_party_reproduction"]["status"]
        == "optional_not_required"
    )
    expansion = report["governance"]["project_run_public_external_expansion"]
    assert expansion["case_count"] == 20365
    assert expansion["independent_third_party_validation"] is False

    paired = {track["dataset"]: track for track in report["secondary_tracks"]}
    assert (
        paired["aosp-framework-paired-ui-v1"]["paired_comparisons"]["opencc-s2twp"]["result"]
        == "loser"
    )
    assert (
        paired["firefox-paired-ui-v1"]["paired_comparisons"]["opencc-s2twp"]["result"]
        == "statistical_tie"
    )


def test_formal_report_rejects_nonpositive_paired_delta_ci() -> None:
    blind, ud, naer, *paired = inputs()
    invalid = copy.deepcopy(blind)
    invalid["paired_comparisons"]["opencc-s2twp"]["delta_ci_95"]["low"] = 0

    with pytest.raises(ValueError, match="not fully above zero"):
        build_report(invalid, ud, naer, *paired)


def test_formal_report_rejects_dirty_public_track() -> None:
    blind, ud, naer, *paired = inputs()
    invalid = copy.deepcopy(ud)
    invalid["provenance"]["git_dirty"] = True

    with pytest.raises(ValueError, match="dirty provenance"):
        build_report(blind, invalid, naer, *paired)
