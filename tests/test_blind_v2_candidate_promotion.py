"""Tests for maintainer-confirmed Blind-v2 candidate promotion."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from scripts.blind_v2_governance import validate_pool

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
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-014-2026-07-24.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-015-2026-07-24.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-016-2026-07-24.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-017-2026-07-25.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-018-2026-07-26.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-019-2026-07-26.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-020-2026-07-26.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-021-2026-07-27.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-022-2026-07-27.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-023-2026-07-27.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-024-2026-07-27.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-025-2026-07-27.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-026-2026-07-27.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-027-2026-07-27.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-028-2026-07-27.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-029-2026-07-27.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-030-2026-07-27.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-031-2026-07-27.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-032-2026-07-27.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-033-2026-07-27.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-034-2026-07-27.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-035-2026-07-27.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-036-2026-07-28.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-037-2026-07-28.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-038-2026-07-28.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-039-2026-07-28.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-040-2026-07-28.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-041-2026-07-28.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-042-2026-07-28.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-043-2026-07-28.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-044-2026-07-28.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-045-2026-07-28.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-046-2026-07-28.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-047-2026-07-28.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-048-2026-07-29.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-049-2026-07-29.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-050-2026-07-29.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-051-2026-07-29.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-052-2026-07-29.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-053-2026-07-30.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-054-2026-07-30.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-055-2026-07-30.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-056-2026-07-30.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-057-2026-07-30.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-058-2026-07-30.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-059-2026-07-30.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-060-2026-07-30.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-061-2026-07-30.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-062-2026-07-30.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-063-2026-07-30.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-064-2026-07-30.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-065-2026-07-30.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-066-2026-07-30.json",
    ROOT
    / "docs/reports/blind-v2-source-classification-maintainer-decision-batch-067-2026-07-30.json",
)
REPORT = ROOT / "docs/reports/blind-v2-candidate-promotion-batches-001-067-2026-07-30.md"
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


def test_committed_frozen_candidates_are_input_only_and_internally_valid() -> None:
    committed = json.loads(POOL.read_text(encoding="utf-8"))

    assert validate_pool(POOL, check_references=False) == []
    assert committed["status"] == "frozen"
    assert committed["stats"] == {
        "total": 5896,
        "by_domain": {
            "formal_news": 806,
            "high_stakes": 1564,
            "it_api_cli": 939,
            "llm_generated": 632,
            "social_daily": 796,
            "ui_i18n": 1159,
        },
        "by_risk": {
            "baseline_guard": 1716,
            "candidate_gap": 2452,
            "over_conversion_guard": 1728,
        },
        "by_source_class": {
            "permissive_license": 2003,
            "project_original": 2006,
            "public_domain": 1887,
        },
        "by_source": {
            "aosp-framework-zh-rcn-v1": 559,
            "chromium-strings-zh-cn-v1": 295,
            "cisa-cyber-hygiene-zh-hans-v1": 21,
            "cisa-personal-security-zh-hans-v1": 123,
            "cdc-stacks-111808-v1": 18,
            "cdc-stacks-116683-v1": 21,
            "cdc-stacks-120024-v1": 22,
            "census-newsroom-zh-hans-v1": 214,
            "flores-200-zho-hans-v1": 114,
            "ftc-heads-up-simplified-v1": 115,
            "ftc-how-to-avoid-scam-simplified-v1": 33,
            "ftc-identity-theft-simplified-v1": 18,
            "ftc-small-business-simplified-v1": 55,
            "kubernetes-docs-zh-cn-v1": 507,
            "massive-1-0-zh-cn-v1": 344,
            "nps-essential-acadia-simplified-v1": 30,
            "osha-chainsaw-safety-simplified-v1": 20,
            "osha-disaster-cleanup-simplified-v1": 56,
            "osha-disaster-falls-simplified-v1": 12,
            "osha-electrical-safety-simplified-v1": 14,
            "osha-fallen-workers-family-simplified-v1": 20,
            "osha-small-business-consultation-simplified-v1": 20,
            "osha-work-zone-traffic-simplified-v1": 15,
            "ready-gov-drought-zh-hans-v1": 70,
            "ready-gov-earthquakes-zh-hans-v1": 44,
            "ready-gov-evacuation-zh-hans-v1": 46,
            "ready-gov-floods-zh-hans-v1": 47,
            "ready-gov-home-fires-zh-hans-v1": 81,
            "ready-gov-hurricanes-zh-hans-v1": 42,
            "ready-gov-campus-zh-hans-v1": 4,
            "ready-gov-cybersecurity-zh-hans-v1": 46,
            "ready-gov-kids-tornadoes-zh-hans-v1": 34,
            "ready-gov-landslides-debris-flow-zh-hans-v1": 53,
            "ready-gov-radiation-zh-hans-v1": 59,
            "ready-gov-are-you-ready-guide-simplified-v1": 461,
            "ready-gov-tornadoes-zh-hans-v1": 32,
            "ready-gov-winter-weather-zh-hans-v1": 41,
            "ud-chinese-cfl-v1": 69,
            "vscode-loc-zh-hans-v1": 115,
            "zhtw-project-balanced-baseline-guard-v1": 100,
            "zhtw-project-competitor-risk-taxonomy-v1": 80,
            "zhtw-project-formal-entity-guard-v1": 100,
            "zhtw-project-formal-llm-balance-v1": 100,
            "zhtw-project-formal-llm-context-guard-v1": 98,
            "zhtw-project-formal-llm-evidence-guard-v1": 96,
            "zhtw-project-formal-llm-overconversion-guard-v1": 79,
            "zhtw-project-formal-llm-semantic-v1": 100,
            "zhtw-project-it-api-cli-v1": 100,
            "zhtw-project-it-llm-social-guard-v1": 100,
            "zhtw-project-it-llm-ui-guard-v1": 100,
            "zhtw-project-it-ui-llm-formal-guard-v1": 100,
            "zhtw-project-llm-domain-balance-v1": 98,
            "zhtw-project-llm-formal-operations-guard-v1": 96,
            "zhtw-project-llm-formal-reasoning-guard-v1": 96,
            "zhtw-project-llm-it-ui-baseline-v1": 100,
            "zhtw-project-llm-product-v1": 50,
            "zhtw-project-llm-social-baseline-v1": 100,
            "zhtw-project-social-formal-context-guard-v1": 96,
            "zhtw-project-social-formal-ambiguity-guard-v1": 72,
            "zhtw-project-ui-i18n-v1": 50,
            "zhtw-project-ui-social-baseline-guard-v1": 95,
        },
    }
    assert find_forbidden_keys(committed) == set()
    assert {case["source"]["class"] for case in committed["cases"]} == {
        "permissive_license",
        "project_original",
        "public_domain",
    }
    report_text = REPORT.read_text(encoding="utf-8")
    assert "Maintainer-confirmed eligible inputs: 5912" in report_text
    assert "Promoted after exact/near dedupe: 5896" in report_text
    assert "Excluded by dedupe: 16" in report_text
    assert "Status: collecting; freeze-readiness gates passed" in report_text


def test_frozen_pool_meets_formal_sampling_gates() -> None:
    errors = validate_pool(POOL, require_ready=True, check_references=False)

    assert errors == []
