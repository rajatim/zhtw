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
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-009-2026-07-23.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-010-2026-07-24.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-011-2026-07-24.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-012-2026-07-24.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-013-2026-07-24.json",
)
REPORT = ROOT / "docs/reports/blind-v2-candidate-promotion-batches-001-013-2026-07-24.md"
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
        created_at="2026-07-24T00:00:00+08:00",
    )

    assert generated == committed
    assert validate_pool(POOL) == []
    assert committed["status"] == "collecting"
    assert committed["stats"] == {
        "total": 1081,
        "by_domain": {
            "formal_news": 139,
            "high_stakes": 271,
            "it_api_cli": 219,
            "llm_generated": 107,
            "social_daily": 223,
            "ui_i18n": 122,
        },
        "by_risk": {
            "baseline_guard": 300,
            "candidate_gap": 546,
            "over_conversion_guard": 235,
        },
        "by_source_class": {
            "permissive_license": 365,
            "project_original": 300,
            "public_domain": 416,
        },
        "by_source": {
            "cdc-stacks-111808-v1": 18,
            "cdc-stacks-116683-v1": 21,
            "cdc-stacks-120024-v1": 22,
            "flores-200-zho-hans-v1": 98,
            "ftc-heads-up-simplified-v1": 100,
            "ftc-small-business-simplified-v1": 55,
            "massive-1-0-zh-cn-v1": 98,
            "nps-essential-acadia-simplified-v1": 30,
            "osha-chainsaw-safety-simplified-v1": 15,
            "osha-disaster-cleanup-simplified-v1": 7,
            "osha-disaster-falls-simplified-v1": 12,
            "osha-electrical-safety-simplified-v1": 14,
            "osha-fallen-workers-family-simplified-v1": 12,
            "osha-small-business-consultation-simplified-v1": 12,
            "osha-work-zone-traffic-simplified-v1": 13,
            "ready-gov-earthquakes-zh-hans-v1": 31,
            "ready-gov-floods-zh-hans-v1": 28,
            "ready-gov-hurricanes-zh-hans-v1": 26,
            "ud-chinese-cfl-v1": 69,
            "vscode-loc-zh-hans-v1": 100,
            "zhtw-project-formal-llm-semantic-v1": 100,
            "zhtw-project-it-api-cli-v1": 100,
            "zhtw-project-llm-product-v1": 50,
            "zhtw-project-ui-i18n-v1": 50,
        },
    }
    assert report["confirmed_eligible"] == 1082
    assert report["promoted"] == 1081
    assert report["excluded_by_dedupe"] == 1
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
    assert not any("source class permissive_license exceeds 35%" in error for error in errors)
    assert any("source class public_domain exceeds 35%" in error for error in errors)
    assert not any("source class project_original exceeds 35%" in error for error in errors)
    assert not any("source flores-200-zho-hans-v1 exceeds 10%" in error for error in errors)
    assert not any("source ftc-heads-up-simplified-v1 exceeds 10%" in error for error in errors)
    assert not any("source massive-1-0-zh-cn-v1 exceeds 10%" in error for error in errors)
    assert not any("source vscode-loc-zh-hans-v1 exceeds 10%" in error for error in errors)
    assert not any("source zhtw-project-it-api-cli-v1 exceeds 10%" in error for error in errors)
    assert not any("source ud-chinese-cfl-v1 exceeds 10%" in error for error in errors)
