# zhtw:disable
"""Tests for public accuracy regression datasets."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

import pytest

from zhtw.converter import convert

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "benchmarks" / "accuracy" / "regression-v1.json"
SCHEMA = ROOT / "benchmarks" / "accuracy" / "regression-v1.schema.json"
EXPECTED_DOMAINS = {"news", "regressions", "social", "tech", "wiki"}
EXPECTED_PROMOTED_DOMAINS = {"formal", "high_risk", "it", "llm", "mixed", "social", "ui"}
EXPECTED_COMPETITORS = {"opencc-s2twp", "zhconv-zh-tw"}
EXPECTED_CLASSIFICATIONS = {
    "all_match",
    "annotation_promoted",
    "holdout_regression_promoted",
    "public_reproduction_promoted",
    "zhtw_advantage",
}
EXPECTED_RISKS = {"baseline_guard", "over_conversion_guard", "candidate_gap"}
ORIGINAL_CORPUS_DOMAINS = {"news", "regressions", "social", "tech", "wiki"}
ANNOTATION_REPORT = "docs/reports/annotation-promotion-gate-2026-07-07.json"
HISTORICAL_GROUND_TRUTH_CORRECTION_REPORT = (
    "docs/reports/accuracy-ground-truth-corrections-2026-07-16.json"
)
CURRENT_GROUND_TRUTH_CORRECTION_REPORT = (
    "docs/reports/accuracy-ground-truth-corrections-2026-07-18.json"
)
LATEST_GROUND_TRUTH_CORRECTION_REPORT = (
    "docs/reports/accuracy-ground-truth-corrections-2026-07-19.json"
)
FINAL_TRANSLATION_CORRECTION_REPORT = (
    "docs/reports/accuracy-final-translation-corrections-2026-07-19.json"
)
HISTORICAL_GROUND_TRUTH_CORRECTION_IDS = {
    "annotation/it-api-cli-0043",
    "annotation/it-api-cli-0170",
    "annotation/social-daily-0038",
}
CURRENT_GROUND_TRUTH_CORRECTION_IDS = {
    "annotation/it-api-cli-0009",
    "annotation/it-api-cli-0018",
    "annotation/it-api-cli-0020",
    "annotation/it-api-cli-0030",
    "annotation/it-api-cli-0079",
    "annotation/it-api-cli-0129",
    "annotation/it-api-cli-0154",
    "annotation/it-api-cli-0156",
    "annotation/it-api-cli-0167",
    "holdout/blind-it-0070",
    "holdout/blind-it-0073",
    "holdout/blind-it-0138",
    "holdout/blind-it-0169",
    "holdout/blind-it-0223",
}
LATEST_GROUND_TRUTH_CORRECTION_IDS = {
    "annotation/formal-high-risk-0094",
    "annotation/it-api-cli-0062",
    "annotation/it-api-cli-0069",
    "annotation/ui-i18n-0004",
    "annotation/ui-i18n-0087",
    "annotation/ui-i18n-0125",
    "holdout/blind-it-0042",
    "holdout/blind-it-0044",
    "holdout/blind-ui-0034",
    "holdout/blind-ui-0079",
    "holdout/blind-llm-0085",
    "holdout/blind-it-0177",
    "holdout/blind-ui-0169",
    "public-reproduction/public-repro-20260713-ui-0001",
    "holdout/blind-it-0291",
    "holdout/blind-ui-0229",
}
FINAL_TRANSLATION_CORRECTION_IDS = {
    "regressions/regression_020",
    "social/social_033",
    "social/social_034",
    "social/social_036",
    "social/social_053",
    "tech/tech_066",
    "tech/tech_034",
    "tech/tech_037",
    "tech/tech_048",
    "tech/tech_010",
    "tech/tech_017",
    "annotation/it-api-cli-0038",
    "holdout/blind-it-0057",
}
GROUND_TRUTH_CORRECTION_REPORT_BY_ID = {
    **{
        case_id: HISTORICAL_GROUND_TRUTH_CORRECTION_REPORT
        for case_id in HISTORICAL_GROUND_TRUTH_CORRECTION_IDS
    },
    **{
        case_id: CURRENT_GROUND_TRUTH_CORRECTION_REPORT
        for case_id in CURRENT_GROUND_TRUTH_CORRECTION_IDS
    },
    **{
        case_id: LATEST_GROUND_TRUTH_CORRECTION_REPORT
        for case_id in LATEST_GROUND_TRUTH_CORRECTION_IDS
    },
    **{
        case_id: FINAL_TRANSLATION_CORRECTION_REPORT for case_id in FINAL_TRANSLATION_CORRECTION_IDS
    },
}
ANNOTATION_BACKLOG = "benchmarks/accuracy/annotation-backlog-v1.json"
HOLDOUT_PROMOTION_REPORT = "docs/reports/holdout-regression-promotion-gate-blind-v1-2026-07-09.json"
HOLDOUT_PROMOTION_REPORT_BATCH2 = (
    "docs/reports/holdout-regression-promotion-gate-blind-v1-batch2-2026-07-09.json"
)
HOLDOUT_PROMOTION_REPORT_BATCH3 = (
    "docs/reports/holdout-regression-promotion-gate-blind-v1-batch3-2026-07-09.json"
)
HOLDOUT_PROMOTION_REPORT_BATCH4_RECHECK = (
    "docs/reports/holdout-regression-promotion-gate-blind-v1-batch4-recheck-2026-07-09.json"
)
HOLDOUT_PROMOTION_REPORT_REMAINING_40_FINAL_REVIEW = (
    "docs/reports/holdout-regression-promotion-gate-blind-v1-"
    "remaining-40-final-review-2026-07-09.json"
)
HOLDOUT_PROMOTION_REPORT_338_MISS_REVIEW = (
    "docs/reports/holdout-regression-promotion-gate-blind-v1-338-miss-review-2026-07-09.json"
)
HOLDOUT_PROMOTION_REPORT_BATCH6_MISS_REVIEW = (
    "docs/reports/holdout-regression-promotion-gate-blind-v1-batch6-miss-review-2026-07-10.json"
)
HOLDOUT_PROMOTION_REPORT_BATCH7_MISS_REVIEW = (
    "docs/reports/holdout-regression-promotion-gate-blind-v1-batch7-miss-review-2026-07-10.json"
)
HOLDOUT_PROMOTION_REPORT_BATCH8_MISS_REVIEW = (
    "docs/reports/holdout-regression-promotion-gate-blind-v1-batch8-miss-review-2026-07-11.json"
)
HOLDOUT_PROMOTION_REPORT_BATCH9_MISS_REVIEW = (
    "docs/reports/holdout-regression-promotion-gate-blind-v1-batch9-miss-review-2026-07-12.json"
)
HOLDOUT_PROMOTION_REPORT_BATCH10_MISS_REVIEW = (
    "docs/reports/holdout-regression-promotion-gate-blind-v1-batch10-miss-review-2026-07-13.json"
)
HOLDOUT_PROMOTION_REPORT_BATCH11_SEMANTIC_REAUDIT = (
    "docs/reports/holdout-regression-promotion-gate-blind-v1-"
    "batch11-semantic-reaudit-2026-07-14.json"
)
HOLDOUT_PROMOTION_REPORT_BATCH12_MISS_REVIEW = (
    "docs/reports/holdout-regression-promotion-gate-blind-v1-batch12-miss-review-2026-07-14.json"
)
HOLDOUT_PROMOTION_REPORT_BATCH13_MISS_REVIEW = (
    "docs/reports/holdout-regression-promotion-gate-blind-v1-batch13-miss-review-2026-07-14.json"
)
PUBLIC_REPRODUCTION_PROMOTION_REPORT = (
    "docs/reports/public-reproduction-promotion-gate-after-batch10-remaining-signal-2026-07-13.json"
)
HOLDOUT_PROMOTION_REPORTS = {
    HOLDOUT_PROMOTION_REPORT,
    HOLDOUT_PROMOTION_REPORT_BATCH2,
    HOLDOUT_PROMOTION_REPORT_BATCH3,
    HOLDOUT_PROMOTION_REPORT_BATCH4_RECHECK,
    HOLDOUT_PROMOTION_REPORT_REMAINING_40_FINAL_REVIEW,
    HOLDOUT_PROMOTION_REPORT_338_MISS_REVIEW,
    HOLDOUT_PROMOTION_REPORT_BATCH6_MISS_REVIEW,
    HOLDOUT_PROMOTION_REPORT_BATCH7_MISS_REVIEW,
    HOLDOUT_PROMOTION_REPORT_BATCH8_MISS_REVIEW,
    HOLDOUT_PROMOTION_REPORT_BATCH9_MISS_REVIEW,
    HOLDOUT_PROMOTION_REPORT_BATCH10_MISS_REVIEW,
    HOLDOUT_PROMOTION_REPORT_BATCH11_SEMANTIC_REAUDIT,
    HOLDOUT_PROMOTION_REPORT_BATCH12_MISS_REVIEW,
    HOLDOUT_PROMOTION_REPORT_BATCH13_MISS_REVIEW,
}
HOLDOUT_CANDIDATES = "benchmarks/accuracy/holdout-regression-candidates-v1.json"
PUBLIC_REPRODUCTION_FINAL_DECISION = (
    "docs/reports/public-reproduction-maintainer-final-decision-"
    "after-batch10-remaining-signal-2026-07-13.json"
)


def _load_dataset() -> dict[str, Any]:
    return json.loads(DATASET.read_text(encoding="utf-8"))


REGRESSION_DATA = _load_dataset()
REGRESSION_CASES = REGRESSION_DATA["cases"]


def test_regression_v1_schema_file_exists() -> None:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))

    assert schema["title"] == "zhtw accuracy regression dataset"
    assert "cases" in schema["properties"]


def test_regression_v1_metadata_and_stats_are_consistent() -> None:
    data = REGRESSION_DATA
    cases = REGRESSION_CASES

    assert data["version"] == 1
    assert data["name"] == "regression-v1"
    assert (
        data["selection"]["classification"]
        == "curated corpus cases plus approved annotation backlog, "
        "holdout regression promotions, and public reproduction promotions"
    )
    assert data["selection"]["required_zhtw_match"] is True
    assert data["selection"]["total_cases"] == len(cases) == 1251
    assert set(data["selection"]["categories"]) == EXPECTED_DOMAINS | EXPECTED_PROMOTED_DOMAINS

    by_domain = Counter(case["domain"] for case in cases)
    by_risk = Counter(case["risk"] for case in cases)
    by_classification = Counter(case["source"]["classification"] for case in cases)
    by_miss_count = Counter(str(len(case["competitor_misses"])) for case in cases)

    assert dict(sorted(by_domain.items())) == data["stats"]["by_domain"]
    assert dict(sorted(by_risk.items())) == data["stats"]["by_risk"]
    assert dict(sorted(by_classification.items())) == data["stats"]["by_classification"]
    assert dict(sorted(by_miss_count.items())) == data["stats"]["by_competitor_miss_count"]
    assert by_domain["news"] == 100
    assert by_domain["regressions"] == 100
    assert by_domain["social"] == 194
    assert by_domain["tech"] == 100
    assert by_domain["wiki"] == 100
    assert by_domain["formal"] == 130
    assert by_domain["high_risk"] == 15
    assert by_domain["it"] == 286
    assert by_domain["llm"] == 22
    assert by_domain["mixed"] == 25
    assert by_domain["ui"] == 179
    assert by_classification["annotation_promoted"] == 500
    assert by_classification["holdout_regression_promoted"] == 219
    assert by_classification["public_reproduction_promoted"] == 32


def test_regression_v1_cases_have_required_shape() -> None:
    seen_ids: set[str] = set()

    for case in REGRESSION_CASES:
        assert case["id"] not in seen_ids
        seen_ids.add(case["id"])

        assert case["domain"] in EXPECTED_DOMAINS | EXPECTED_PROMOTED_DOMAINS
        assert case["input"]
        assert case["expected"]
        assert case["risk"] in EXPECTED_RISKS
        assert set(case["competitor_misses"]).issubset(EXPECTED_COMPETITORS)

        source = case["source"]
        assert source["case_id"]
        assert source["classification"] in EXPECTED_CLASSIFICATIONS

        if source["classification"] == "annotation_promoted":
            assert case["id"].startswith("annotation/")
            expected_report = GROUND_TRUTH_CORRECTION_REPORT_BY_ID.get(
                case["id"], ANNOTATION_REPORT
            )
            assert source["report"] == expected_report
            assert source["source_file"] == ANNOTATION_BACKLOG
            assert source["sample_seed"] is None
            assert case["domain"] in EXPECTED_PROMOTED_DOMAINS
            assert case["competitor_misses"] == []
        elif source["classification"] == "holdout_regression_promoted":
            assert case["id"].startswith("holdout/blind-")
            expected_report = GROUND_TRUTH_CORRECTION_REPORT_BY_ID.get(case["id"])
            if expected_report is None:
                assert source["report"] in HOLDOUT_PROMOTION_REPORTS
            else:
                assert source["report"] == expected_report
            assert source["source_file"] == HOLDOUT_CANDIDATES
            assert source["sample_seed"] is None
            assert case["domain"] in EXPECTED_PROMOTED_DOMAINS
            assert case["competitor_misses"] == []
            assert "promoted from blind-v1 after removal from sealed holdout" in case["notes"]
        elif source["classification"] == "public_reproduction_promoted":
            assert case["id"].startswith("public-reproduction/public-repro-")
            expected_report = GROUND_TRUTH_CORRECTION_REPORT_BY_ID.get(
                case["id"], PUBLIC_REPRODUCTION_PROMOTION_REPORT
            )
            assert source["report"] == expected_report
            assert source["source_file"] == PUBLIC_REPRODUCTION_FINAL_DECISION
            assert source["sample_seed"] is None
            assert case["domain"] in EXPECTED_PROMOTED_DOMAINS
            assert case["competitor_misses"] == []
            assert (
                "promoted from public reproduction after maintainer final decision" in case["notes"]
            )
        elif source["classification"] == "zhtw_advantage":
            assert source["report"] == data_report_path()
            assert source["source_file"].startswith("tests/data/corpus/")
            assert case["risk"] == "over_conversion_guard"
            assert case["competitor_misses"]
        else:
            assert source["classification"] == "all_match"
            assert source["report"] == data_report_path()
            assert source["source_file"].startswith("tests/data/corpus/")
            assert case["risk"] == "baseline_guard"
            assert case["competitor_misses"] == []


def data_report_path() -> str:
    return "docs/reports/competitor-diffs-full-2026-07-03.json"


@pytest.mark.parametrize(
    ("source", "expected"),
    [(case["input"], case["expected"]) for case in REGRESSION_CASES],
    ids=[case["id"] for case in REGRESSION_CASES],
)
def test_regression_v1_matches_zhtw_expected(source: str, expected: str) -> None:
    assert convert(source) == expected


@pytest.mark.parametrize(
    ("source", "expected"),
    [(case["input"], case["expected"]) for case in REGRESSION_CASES],
    ids=[case["id"] for case in REGRESSION_CASES],
)
def test_regression_v1_is_idempotent(source: str, expected: str) -> None:
    assert convert(convert(source)) == expected


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("租用戶", "租用戶"),
        ("多租用戶架構使用命名空間。", "多租用戶架構使用命名空間。"),
        ("命名空間", "命名空間"),
        ("熱重載", "熱重新載入"),
        ("開發伺服器支援熱重載。", "開發伺服器支援熱重新載入。"),
    ],
)
def test_final_translation_audit_term_guards(source: str, expected: str) -> None:
    assert convert(source) == expected
    assert convert(expected) == expected
