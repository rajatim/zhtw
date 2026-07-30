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


def inputs() -> tuple[dict[str, object], dict[str, object], dict[str, object]]:
    return (
        load("blind-v2-benchmark-2026-07-31.json"),
        load("ud-gsd-benchmark-2026-07-31.json"),
        load("naer-terms-benchmark-2026-07-31.json"),
    )


def test_formal_report_uses_blind_v2_as_the_only_primary_endpoint() -> None:
    report = build_report(*inputs())

    assert report["decision"] == "scoped_winner"
    assert report["primary_endpoint"]["dataset"] == "blind-v2"
    assert all(track["role"] == "secondary_evidence" for track in report["secondary_tracks"])
    assert report["governance"]["maintainer_claim_confirmation"] == "pending"
    assert report["governance"]["detailed_rows_read"] is False
    assert report["governance"]["external_hosted_public_reproduction"]["status"] == "passed"


def test_formal_report_rejects_nonpositive_paired_delta_ci() -> None:
    blind, ud, naer = inputs()
    invalid = copy.deepcopy(blind)
    invalid["paired_comparisons"]["opencc-s2twp"]["delta_ci_95"]["low"] = 0

    with pytest.raises(ValueError, match="not fully above zero"):
        build_report(invalid, ud, naer)


def test_formal_report_rejects_dirty_public_track() -> None:
    blind, ud, naer = inputs()
    invalid = copy.deepcopy(ud)
    invalid["provenance"]["git_dirty"] = True

    with pytest.raises(ValueError, match="dirty provenance"):
        build_report(blind, invalid, naer)
