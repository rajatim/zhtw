"""Tests for maintainer-confirmed Blind-v2 candidate promotion."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from scripts.blind_v2_governance import validate_pool
from scripts.promote_blind_v2_candidates import build_pool, render_report

ROOT = Path(__file__).resolve().parents[1]
POOL = ROOT / "benchmarks/accuracy/blind-v2.candidate-pool.json"
DECISIONS = (
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-001-2026-07-21.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-002-2026-07-21.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-003-2026-07-22.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-004-2026-07-23.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-005-2026-07-23.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-006-2026-07-23.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-007-2026-07-23.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-008-2026-07-23.json",
)
REPORT = ROOT / "docs/reports/blind-v2-candidate-promotion-batches-001-008-2026-07-23.md"
FORBIDDEN_KEYS = {"expected", "acceptable", "annotation", "output", "normalized_output"}


def find_forbidden_keys(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            if key in FORBIDDEN_KEYS:
                found.add(key)
            found.update(find_forbidden_keys(child))
    elif isinstance(value, list):
        for child in value:
            found.update(find_forbidden_keys(child))
    return found


def test_committed_candidates_are_reproducible_input_only_and_deduplicated() -> None:
    committed = json.loads(POOL.read_text(encoding="utf-8"))
    generated, report = build_pool(
        list(DECISIONS),
        output=POOL,
        created_at="2026-07-23T00:00:00+08:00",
    )

    assert generated == committed
    assert validate_pool(POOL) == []
    assert committed["status"] == "collecting"
    assert committed["stats"] == {
        "total": 611,
        "by_domain": {
            "formal_news": 84,
            "high_stakes": 108,
            "it_api_cli": 121,
            "llm_generated": 48,
            "social_daily": 167,
            "ui_i18n": 83,
        },
        "by_risk": {
            "baseline_guard": 185,
            "candidate_gap": 309,
            "over_conversion_guard": 117,
        },
        "by_source_class": {
            "permissive_license": 265,
            "project_original": 200,
            "public_domain": 146,
        },
        "by_source": {
            "cdc-stacks-111808-v1": 18,
            "cdc-stacks-116683-v1": 21,
            "cdc-stacks-120024-v1": 22,
            "flores-200-zho-hans-v1": 98,
            "ftc-small-business-simplified-v1": 55,
            "massive-1-0-zh-cn-v1": 98,
            "nps-essential-acadia-simplified-v1": 30,
            "ud-chinese-cfl-v1": 69,
            "zhtw-project-it-api-cli-v1": 100,
            "zhtw-project-llm-product-v1": 50,
            "zhtw-project-ui-i18n-v1": 50,
        },
    }
    assert report["confirmed_eligible"] == report["promoted"] == 611
    assert report["excluded_by_dedupe"] == 0
    assert find_forbidden_keys(committed) == set()
    assert {case["source"]["class"] for case in committed["cases"]} == {
        "permissive_license",
        "project_original",
        "public_domain",
    }
    assert REPORT.read_text(encoding="utf-8") == render_report(report, generated)


def test_collecting_pool_is_not_ready_for_formal_sampling() -> None:
    errors = validate_pool(POOL, require_ready=True)

    assert any("requires at least 5880 cases" in error for error in errors)
    assert any("source class permissive_license exceeds 35%" in error for error in errors)
    assert not any("source class project_original exceeds 35%" in error for error in errors)
    assert any("source flores-200-zho-hans-v1 exceeds 10%" in error for error in errors)
    assert any("source ud-chinese-cfl-v1 exceeds 10%" in error for error in errors)
