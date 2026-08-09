# zhtw:disable
# ruff: noqa: F403,F405
"""Blind-v1 post-review and public promotion tests."""

from tests._accuracy_holdout_support import *  # noqa: F403
from zhtw import __version__ as ZHTW_VERSION


def test_batch7_miss_final_decision_omits_sealed_values() -> None:
    decision = load_json(MAINTAINER_BATCH7_MISS_FINAL_DECISION)

    assert decision["report_type"] == (
        "holdout_maintainer_final_decision_batch7_miss_classification"
    )
    assert decision["review_stage"] == ("maintainer_final_decision_batch7_miss_classification")
    assert decision["maintainer"] == "tim"
    assert decision["decision"] == "review_ok"
    assert decision["private_expected_updated"] is True
    assert decision["expected_values_included"] is False
    assert decision["acceptable_values_included"] is False
    assert decision["inputs_included"] is False
    assert decision["outputs_included"] is False
    assert decision["benchmark_rows_included"] is False
    assert decision["source_inputs_sha256_after"] == (
        "d331a1a2d6c58774089ca723677ec77ca4abe05e1eb11298ca8a5700b6a1cbcd"
    )
    assert decision["private_expected_sha256_after"] != private_expected_sha256()
    assert decision["summary"]["reviewed_maintainer_cases"] == 24
    assert decision["summary"]["maintainer_confirmed_acceptable_variants"] == 7
    assert decision["summary"]["removed_from_sealed_to_public_regression_candidates"] == 17
    assert decision["summary"]["remaining_private_expected_cases"] == 498
    assert decision["summary"]["remaining_sealed_input_cases"] == 498
    assert decision["summary"]["public_candidates_promoted_to_regression"] == 17
    assert decision["summary"]["projected_remaining_private_benchmark"] == {
        "case_count": 498,
        "accepted": 472,
        "misses": 26,
        "accepted_accuracy": 0.9477911646586346,
    }
    assert decision["confirmed_acceptable_variant_case_ids"] == [
        "blind-it-0146",
        "blind-it-0147",
        "blind-it-0148",
        "blind-it-0157",
        "blind-ui-0108",
        "blind-ui-0110",
        "blind-ui-0118",
    ]
    assert decision["removed_to_public_regression_candidate_case_ids"] == [
        "blind-it-0138",
        "blind-it-0140",
        "blind-it-0142",
        "blind-it-0145",
        "blind-it-0150",
        "blind-it-0151",
        "blind-it-0152",
        "blind-it-0153",
        "blind-it-0155",
        "blind-it-0156",
        "blind-it-0158",
        "blind-ui-0119",
        "blind-ui-0123",
        "blind-llm-0083",
        "blind-llm-0085",
        "blind-formal-0084",
        "blind-social-0079",
    ]
    assert len(decision["kept_sealed_holdout_signal_case_ids"]) == 26
    assert "cases" not in decision
    assert "rows" not in decision
    assert "inputs" not in decision


def test_batch8_miss_final_decision_omits_sealed_values() -> None:
    decision = load_json(MAINTAINER_BATCH8_MISS_FINAL_DECISION)

    assert decision["report_type"] == (
        "holdout_maintainer_final_decision_batch8_miss_classification"
    )
    assert decision["review_stage"] == ("maintainer_final_decision_batch8_miss_classification")
    assert decision["maintainer"] == "tim"
    assert decision["decision"] == "review_ok"
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_updated"] is True
    assert decision["expected_values_included"] is False
    assert decision["acceptable_values_included"] is False
    assert decision["inputs_included"] is False
    assert decision["outputs_included"] is False
    assert decision["benchmark_rows_included"] is False
    assert decision["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "case_ids_and_metadata_only": True,
    }
    assert decision["source_inputs_sha256_after"] == (
        "96226f1fc747cc1d6ae9eb40793077a3a8bc8dc36b194491dc63c7cb26bd4450"
    )
    assert decision["source_inputs_sha256_after"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert decision["private_expected_sha256_after"] != private_expected_sha256()
    assert decision["summary"]["reviewed_maintainer_cases"] == 19
    assert decision["summary"]["maintainer_confirmed_acceptable_variants"] == 4
    assert decision["summary"]["removed_from_sealed_to_public_regression_candidates"] == 15
    assert decision["summary"]["remaining_private_expected_cases"] == 583
    assert decision["summary"]["remaining_sealed_input_cases"] == 583
    assert decision["summary"]["public_candidates_promoted_to_regression"] == 15
    assert decision["summary"]["projected_remaining_private_benchmark"] == {
        "case_count": 583,
        "accepted": 553,
        "misses": 30,
        "accepted_accuracy": 0.9485420240137221,
    }
    assert decision["confirmed_acceptable_variant_case_ids"] == [
        "blind-it-0167",
        "blind-it-0175",
        "blind-llm-0097",
        "blind-social-0095",
    ]
    assert decision["removed_to_public_regression_candidate_case_ids"] == [
        "blind-it-0165",
        "blind-it-0166",
        "blind-it-0168",
        "blind-it-0169",
        "blind-it-0171",
        "blind-it-0173",
        "blind-it-0174",
        "blind-it-0177",
        "blind-ui-0130",
        "blind-ui-0131",
        "blind-ui-0136",
        "blind-ui-0138",
        "blind-ui-0139",
        "blind-llm-0098",
        "blind-formal-0101",
    ]
    assert len(decision["kept_sealed_holdout_signal_case_ids"]) == 30
    assert decision["source_gemini_public_promotion_policy_review"] == (
        "docs/reports/holdout-gemini-policy-review-batch8-miss-public-promotion-2026-07-11.json"
    )
    assert "cases" not in decision
    assert "rows" not in decision
    assert "inputs" not in decision


def test_batch9_miss_final_decision_omits_sealed_values() -> None:
    decision = load_json(MAINTAINER_BATCH9_MISS_FINAL_DECISION)

    assert decision["report_type"] == (
        "holdout_maintainer_final_decision_batch9_miss_classification"
    )
    assert decision["review_stage"] == ("maintainer_final_decision_batch9_miss_classification")
    assert decision["maintainer"] == "tim"
    assert decision["decision"] == "review_ok"
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_updated"] is True
    assert decision["expected_values_included"] is False
    assert decision["acceptable_values_included"] is False
    assert decision["inputs_included"] is False
    assert decision["outputs_included"] is False
    assert decision["benchmark_rows_included"] is False
    assert decision["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "case_ids_and_metadata_only": True,
    }
    assert decision["source_inputs_sha256_before"] == (
        "0ac742ac9885cdae198bed6fc376c2fb5c3e991573ae4cb4ac2072cfef3e937d"
    )
    assert decision["source_inputs_sha256_after"] == (
        "8f54d6e8185cf94f73805aeea27a23859e691cfd8ae04f3956023ec8ec9606d4"
    )
    assert decision["source_inputs_sha256_after"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert decision["private_expected_sha256_after"] != private_expected_sha256()
    assert decision["summary"]["reviewed_maintainer_cases"] == 22
    assert decision["summary"]["maintainer_confirmed_acceptable_variants"] == 6
    assert decision["summary"]["removed_from_sealed_to_public_regression_candidates"] == 16
    assert decision["summary"]["remaining_private_expected_cases"] == 667
    assert decision["summary"]["remaining_sealed_input_cases"] == 667
    assert decision["summary"]["public_candidates_promoted_to_regression"] == 16
    assert decision["summary"]["projected_remaining_private_benchmark"] == {
        "case_count": 667,
        "accepted": 636,
        "misses": 31,
        "accepted_accuracy": 0.9535232383808095,
    }
    assert decision["confirmed_acceptable_variant_case_ids"] == [
        "blind-it-0189",
        "blind-it-0197",
        "blind-it-0202",
        "blind-it-0206",
        "blind-ui-0148",
        "blind-ui-0166",
    ]
    assert decision["removed_to_public_regression_candidate_case_ids"] == [
        "blind-it-0190",
        "blind-it-0195",
        "blind-it-0200",
        "blind-it-0201",
        "blind-it-0203",
        "blind-it-0208",
        "blind-it-0209",
        "blind-it-0210",
        "blind-ui-0150",
        "blind-ui-0157",
        "blind-ui-0160",
        "blind-ui-0164",
        "blind-llm-0116",
        "blind-llm-0122",
        "blind-formal-0115",
        "blind-formal-0116",
    ]
    assert len(decision["kept_sealed_holdout_signal_case_ids"]) == 31
    assert decision["source_gemini_public_promotion_policy_review"] == (
        "docs/reports/holdout-gemini-policy-review-batch9-miss-public-promotion-2026-07-12.json"
    )
    assert "cases" not in decision
    assert "rows" not in decision
    assert "inputs" not in decision


def test_batch6_miss_final_decision_omits_sealed_values() -> None:
    decision = load_json(MAINTAINER_BATCH6_MISS_FINAL_DECISION)

    assert decision["report_type"] == (
        "holdout_maintainer_final_decision_batch6_miss_classification"
    )
    assert decision["review_stage"] == ("maintainer_final_decision_batch6_miss_classification")
    assert decision["maintainer"] == "tim"
    assert decision["decision"] == "review_ok"
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_updated"] is True
    assert decision["expected_values_included"] is False
    assert decision["acceptable_values_included"] is False
    assert decision["inputs_included"] is False
    assert decision["outputs_included"] is False
    assert decision["benchmark_rows_included"] is False
    assert decision["sealed_content_policy"] == {
        "case_ids_and_aggregate_counts_only": True,
        "expected_values_omitted": True,
        "acceptable_values_omitted": True,
        "input_values_omitted": True,
        "actual_values_omitted": True,
        "remaining_sealed_rows_omitted": True,
        "removed_cases_are_public_candidates_after_decision": True,
    }
    assert decision["summary"]["reviewed_maintainer_cases"] == 13
    assert decision["summary"]["maintainer_confirmed_acceptable_variants"] == 2
    assert decision["summary"]["removed_from_sealed_to_public_regression_candidates"] == 11
    assert decision["summary"]["remaining_private_expected_cases"] == 415
    assert decision["summary"]["remaining_sealed_input_cases"] == 415
    assert decision["summary"]["public_candidates_promoted_to_regression"] == 11
    assert decision["summary"]["projected_remaining_private_benchmark"] == {
        "case_count": 415,
        "accepted": 391,
        "misses": 24,
        "accepted_accuracy": 0.9421686746987952,
    }
    assert decision["confirmed_acceptable_variant_case_ids"] == [
        "blind-ui-0096",
        "blind-llm-0071",
    ]
    assert decision["removed_to_public_regression_candidate_case_ids"] == [
        "blind-it-0113",
        "blind-it-0115",
        "blind-it-0117",
        "blind-it-0119",
        "blind-it-0121",
        "blind-it-0123",
        "blind-it-0124",
        "blind-it-0125",
        "blind-it-0126",
        "blind-it-0136",
        "blind-ui-0089",
    ]
    assert len(decision["kept_sealed_holdout_signal_case_ids"]) == 24
    assert "cases" not in decision
    assert "rows" not in decision
    assert "inputs" not in decision


def test_gemini_batch6_miss_public_promotion_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_BATCH6_MISS_PUBLIC_PROMOTION_POLICY_REVIEW)

    assert review["report_type"] == ("holdout_gemini_policy_review_batch6_miss_public_promotion")
    assert review["reviewer"] == "gemini_cli"
    assert review["review_stage"] == "public_regression_promotion_policy_review"
    assert review["source_promotion_gate"] == (
        "docs/reports/holdout-regression-promotion-gate-blind-v1-batch6-miss-review-2026-07-10.json"
    )
    assert review["sealed_values_seen"] is False
    assert review["public_values_seen"] is True
    assert review["sealed_content_policy"] == {
        "reviewed_cases_removed_from_sealed_before_tuning": True,
        "remaining_sealed_holdout_signal_cases_used_for_tuning": False,
        "opencc_or_competitor_outputs_used_for_expected": False,
        "gemini_received_public_candidate_values_only": True,
    }
    assert review["summary"] == {
        "checked": 11,
        "promotion_ready": 11,
        "policy_consistent": True,
        "risk_level": "low",
        "blocking_findings": 0,
        "info_findings": 3,
    }
    assert "GOOGLE_GENERATIVE_AI_API_KEY unset" in " ".join(review["tool_notes"])
    assert "cases" not in review
    assert "rows" not in review
    assert "inputs" not in review


def test_gemini_batch7_miss_public_promotion_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_BATCH7_MISS_PUBLIC_PROMOTION_POLICY_REVIEW)

    assert review["report_type"] == ("holdout_gemini_policy_review_batch7_miss_public_promotion")
    assert review["reviewer"] == "gemini_cli"
    assert review["model_requested"] == "gemini-2.5-flash"
    assert review["review_stage"] == "public_regression_promotion_policy_review"
    assert review["source_promotion_gate"] == (
        "docs/reports/holdout-regression-promotion-gate-blind-v1-batch7-miss-review-2026-07-10.json"
    )
    assert review["sealed_values_seen"] is False
    assert review["public_values_seen"] is True
    assert review["sealed_content_policy"] == {
        "reviewed_cases_removed_from_sealed_before_tuning": True,
        "remaining_sealed_holdout_signal_cases_used_for_tuning": False,
        "opencc_or_competitor_outputs_used_for_expected": False,
        "gemini_received_public_candidate_values_only": True,
    }
    assert review["summary"] == {
        "checked": 17,
        "promotion_ready": 17,
        "policy_consistent": True,
        "risk_level": "low",
        "blocking_findings": 0,
        "info_findings": 0,
    }
    assert "cases" not in review
    assert "rows" not in review
    assert "inputs" not in review


def test_gemini_batch8_miss_public_promotion_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_BATCH8_MISS_PUBLIC_PROMOTION_POLICY_REVIEW)

    assert review["report_type"] == ("holdout_gemini_policy_review_batch8_miss_public_promotion")
    assert review["reviewer"] == "gemini_cli"
    assert review["model_requested"] == "gemini-2.5-flash"
    assert review["review_stage"] == "public_regression_promotion_policy_review"
    assert review["source_promotion_gate"] == (
        "docs/reports/holdout-regression-promotion-gate-blind-v1-batch8-miss-review-2026-07-11.json"
    )
    assert review["sealed_values_seen"] is False
    assert review["public_values_seen"] is True
    assert review["sealed_content_policy"] == {
        "reviewed_cases_removed_from_sealed_before_tuning": True,
        "remaining_sealed_holdout_signal_cases_used_for_tuning": False,
        "opencc_or_competitor_outputs_used_for_expected": False,
        "gemini_received_public_candidate_values_only": True,
    }
    assert review["summary"] == {
        "checked": 15,
        "promotion_ready": 15,
        "policy_consistent": True,
        "risk_level": "low",
        "blocking_findings": 0,
        "info_findings": 0,
    }
    assert "cases" not in review
    assert "rows" not in review
    assert "inputs" not in review


def test_gemini_batch9_miss_public_promotion_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_BATCH9_MISS_PUBLIC_PROMOTION_POLICY_REVIEW)

    assert review["report_type"] == ("holdout_gemini_policy_review_batch9_miss_public_promotion")
    assert review["reviewer"] == "gemini_cli"
    assert review["model_requested"] == "gemini-2.5-flash"
    assert review["review_stage"] == "public_regression_promotion_policy_review"
    assert review["source_promotion_gate"] == (
        "docs/reports/holdout-regression-promotion-gate-blind-v1-batch9-miss-review-2026-07-12.json"
    )
    assert review["sealed_values_seen"] is False
    assert review["public_values_seen"] is True
    assert review["sealed_content_policy"] == {
        "reviewed_cases_removed_from_sealed_before_tuning": True,
        "remaining_sealed_holdout_signal_cases_used_for_tuning": False,
        "opencc_or_competitor_outputs_used_for_expected": False,
        "gemini_received_public_candidate_values_only": True,
    }
    assert review["summary"] == {
        "checked": 16,
        "promotion_ready": 16,
        "policy_consistent": True,
        "risk_level": "low",
        "blocking_findings": 0,
        "info_findings": 3,
    }
    assert all(finding["severity"] == "info" for finding in review["findings"])
    assert "cases" not in review
    assert "rows" not in review
    assert "inputs" not in review


def test_holdout_338_case_miss_classification_omits_sealed_values() -> None:
    report = load_json(MISS_CLASSIFICATION_338_CASE)

    assert report["report_type"] == "holdout_miss_classification_338_case_sanity"
    assert report["review_stage"] == "private_miss_classification_first_pass_after_batch5"
    assert report["reviewer"] == "codex"
    assert report["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "case_ids_and_metadata_only": True,
    }
    assert report["summary"] == {
        "current_sealed_cases": 338,
        "current_accepted": 301,
        "current_misses": 37,
        "accepted_accuracy": 0.8905325443786982,
        "classified_misses": 37,
        "by_action": {
            "keep_as_holdout_signal": 22,
            "move_to_public_regression_candidate": 12,
            "requires_expected_recheck": 3,
        },
        "by_priority": {"P1": 3, "P2": 34},
        "by_domain_action": {
            "formal": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
            "high_risk": {
                "keep_as_holdout_signal": 3,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
            "it": {
                "keep_as_holdout_signal": 2,
                "move_to_public_regression_candidate": 7,
                "requires_expected_recheck": 2,
            },
            "llm": {
                "keep_as_holdout_signal": 4,
                "move_to_public_regression_candidate": 1,
                "requires_expected_recheck": 0,
            },
            "social": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
            "ui": {
                "keep_as_holdout_signal": 3,
                "move_to_public_regression_candidate": 4,
                "requires_expected_recheck": 1,
            },
        },
        "by_risk_action": {
            "baseline_guard": {
                "keep_as_holdout_signal": 0,
                "move_to_public_regression_candidate": 1,
                "requires_expected_recheck": 0,
            },
            "candidate_gap": {
                "keep_as_holdout_signal": 0,
                "move_to_public_regression_candidate": 11,
                "requires_expected_recheck": 3,
            },
            "over_conversion_guard": {
                "keep_as_holdout_signal": 22,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
        },
        "idempotency_followup_cases": 0,
        "expected_recheck_cases": 3,
        "safe_public_candidate_cases": 12,
        "holdout_signal_cases": 22,
        "high_risk_cases": 3,
        "over_conversion_guard_cases": 22,
    }
    forbidden_case_fields = {
        "acceptable",
        "actual",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    cases = report["case_classifications"]
    assert len(cases) == 37
    assert len({case["id"] for case in cases}) == len(cases)
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["sealed_values_omitted"] is True
        assert case["action"] in report["summary"]["by_action"]
        assert case["next_step"]

    action_by_id = {case["id"]: case["action"] for case in cases}
    assert action_by_id["blind-it-0088"] == "move_to_public_regression_candidate"
    assert action_by_id["blind-it-0090"] == "requires_expected_recheck"
    assert action_by_id["blind-ui-0073"] == "requires_expected_recheck"
    assert action_by_id["blind-high-risk-0039"] == "keep_as_holdout_signal"


def test_gemini_338_case_miss_classification_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_MISS_CLASSIFICATION_338_POLICY_REVIEW)

    assert review["reviewer"] == "gemini_cli"
    assert review["review_stage"] == "sanitized_miss_classification_policy_review_after_batch5"
    assert review["source_classification_report"] == (
        "docs/reports/holdout-miss-classification-blind-v1-338-cases-2026-07-09.json"
    )
    assert review["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
    }
    assert review["policy_passed"] is True
    assert len(review["findings"]) == 2
    assert {finding["severity"] for finding in review["findings"]} == {"low"}
    assert review["classification_changes_recommended"] == []
    assert "cases" not in review


def test_338_miss_final_decision_omits_sealed_values() -> None:
    decision = load_json(MAINTAINER_338_MISS_FINAL_DECISION)

    assert decision["report_type"] == ("holdout_maintainer_final_decision_338_miss_classification")
    assert decision["review_stage"] == "maintainer_final_decision_338_miss_classification"
    assert decision["maintainer"] == "tim"
    assert decision["decision"] == "review_ok"
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_updated"] is True
    assert decision["expected_values_included"] is False
    assert decision["acceptable_values_included"] is False
    assert decision["inputs_included"] is False
    assert decision["outputs_included"] is False
    assert decision["benchmark_rows_included"] is False
    assert decision["sealed_content_policy"] == {
        "case_ids_and_aggregate_counts_only": True,
        "expected_values_omitted": True,
        "acceptable_values_omitted": True,
        "input_values_omitted": True,
        "actual_values_omitted": True,
        "remaining_sealed_rows_omitted": True,
        "removed_cases_are_public_candidates_after_decision": True,
    }
    assert decision["summary"]["reviewed_maintainer_cases"] == 15
    assert decision["summary"]["maintainer_confirmed_acceptable_variants"] == 3
    assert decision["summary"]["removed_from_sealed_to_public_regression_candidates"] == 12
    assert decision["summary"]["remaining_private_expected_cases"] == 326
    assert decision["summary"]["remaining_sealed_input_cases"] == 326
    assert decision["summary"]["public_candidates_promoted_to_regression"] == 12
    assert decision["confirmed_acceptable_variant_case_ids"] == [
        "blind-it-0090",
        "blind-it-0094",
        "blind-ui-0073",
    ]
    assert decision["removed_to_public_regression_candidate_case_ids"] == [
        "blind-it-0088",
        "blind-it-0089",
        "blind-it-0092",
        "blind-it-0095",
        "blind-it-0096",
        "blind-it-0097",
        "blind-it-0105",
        "blind-ui-0070",
        "blind-ui-0074",
        "blind-ui-0079",
        "blind-ui-0087",
        "blind-llm-0051",
    ]
    assert len(decision["kept_sealed_holdout_signal_case_ids"]) == 22
    assert "cases" not in decision
    assert "rows" not in decision
    assert "inputs" not in decision


def test_gemini_338_miss_public_promotion_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_338_MISS_PUBLIC_PROMOTION_POLICY_REVIEW)

    assert review["report_type"] == ("holdout_gemini_policy_review_338_miss_public_promotion")
    assert review["reviewer"] == "gemini_cli"
    assert review["review_stage"] == "public_regression_promotion_policy_review"
    assert review["source_promotion_gate"] == (
        "docs/reports/holdout-regression-promotion-gate-blind-v1-338-miss-review-2026-07-09.json"
    )
    assert review["sealed_values_seen"] is False
    assert review["public_values_seen"] is True
    assert review["sealed_content_policy"] == {
        "reviewed_cases_removed_from_sealed_before_tuning": True,
        "remaining_sealed_holdout_signal_cases_used_for_tuning": False,
        "opencc_or_competitor_outputs_used_for_expected": False,
        "gemini_received_public_candidate_values_only": True,
    }
    assert review["summary"] == {
        "checked": 12,
        "promotion_ready": 12,
        "policy_consistent": True,
        "risk_level": "low",
        "blocking_findings": 0,
        "info_findings": 4,
    }
    assert "API_KEY_INVALID" in " ".join(review["tool_notes"])
    assert "cases" not in review
    assert "rows" not in review
    assert "inputs" not in review


def test_holdout_261_case_requires_expected_recheck_omits_sealed_values() -> None:
    report = load_json(REQUIRES_EXPECTED_RECHECK_261_CASE)

    assert report["report_type"] == "holdout_requires_expected_recheck"
    assert report["review_stage"] == "codex_private_recheck_first_pass"
    assert report["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "case_recommendations_include_only_ids_and_metadata": True,
    }
    assert report["policy"] == {
        "codex_is_advisory_only": True,
        "private_expected_updated": False,
        "converter_or_dictionary_updated": False,
        "gemini_review_required_before_maintainer": True,
        "maintainer_confirmation_required_for_acceptable_variants": True,
        "move_to_public_requires_sealed_removal_before_tuning": True,
        "strict_cases_must_not_be_used_for_tuning": True,
    }
    assert report["gemini_review_policy"] == {
        "status": "completed_on_sanitized_metadata",
        "review_report": (
            "docs/reports/"
            "holdout-gemini-policy-review-requires-expected-recheck-blind-v1-261-cases-2026-07-09.json"
        ),
        "sealed_values_seen_by_gemini": False,
        "policy_consistent": True,
        "needs_codex_followup": 0,
        "reason": (
            "Gemini reviewed case ids and recheck recommendation metadata only; private "
            "expected, inputs, and converter outputs were not sent."
        ),
    }
    assert report["summary"] == {
        "current_sealed_cases": 261,
        "current_accepted": 207,
        "current_misses": 54,
        "recheck_cases": 16,
        "maintainer_review_required": 16,
        "recommended_acceptable_variant_candidates": 9,
        "recommended_move_to_public_regression_candidate": 5,
        "recommended_keep_strict_primary_expected": 2,
        "by_recommendation": {
            "maintainer_confirm_add_acceptable_variant": 9,
            "maintainer_confirm_keep_strict_primary_expected": 2,
            "maintainer_confirm_move_to_public_regression_candidate": 5,
        },
        "by_priority": {"P1": 5, "P2": 10, "P3": 1},
        "by_domain_recommendation": {
            "formal": {
                "maintainer_confirm_add_acceptable_variant": 2,
                "maintainer_confirm_keep_strict_primary_expected": 1,
            },
            "high_risk": {
                "maintainer_confirm_add_acceptable_variant": 2,
                "maintainer_confirm_move_to_public_regression_candidate": 2,
            },
            "it": {
                "maintainer_confirm_add_acceptable_variant": 2,
                "maintainer_confirm_move_to_public_regression_candidate": 3,
            },
            "llm": {"maintainer_confirm_add_acceptable_variant": 2},
            "ui": {
                "maintainer_confirm_add_acceptable_variant": 1,
                "maintainer_confirm_keep_strict_primary_expected": 1,
            },
        },
        "by_risk_recommendation": {
            "baseline_guard": {
                "maintainer_confirm_add_acceptable_variant": 1,
                "maintainer_confirm_move_to_public_regression_candidate": 1,
            },
            "candidate_gap": {
                "maintainer_confirm_add_acceptable_variant": 6,
                "maintainer_confirm_keep_strict_primary_expected": 2,
            },
            "over_conversion_guard": {
                "maintainer_confirm_add_acceptable_variant": 2,
                "maintainer_confirm_move_to_public_regression_candidate": 4,
            },
        },
        "hypothetical_if_all_acceptable_recommendations_confirmed": {
            "accepted": 216,
            "misses": 45,
            "accepted_accuracy": 0.8275862068965517,
            "note": (
                "This is not an updated benchmark result; private expected is unchanged "
                "until maintainer confirms acceptable variants."
            ),
        },
    }
    assert "rows" not in report
    assert "inputs" not in report
    assert "cases" not in report

    forbidden_case_fields = {
        "acceptable",
        "actual",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    recommendations = report["case_recommendations"]
    assert len(recommendations) == 16
    assert len({case["id"] for case in recommendations}) == len(recommendations)
    for case in recommendations:
        assert not (forbidden_case_fields & set(case))
        assert case["id"].startswith("blind-")
        assert case["recommendation"] in report["summary"]["by_recommendation"]
        assert case["needs_maintainer_review"] is True
        assert case["next_step"]

    recommendation_by_id = {case["id"]: case["recommendation"] for case in recommendations}
    assert recommendation_by_id["blind-it-0081"] == ("maintainer_confirm_add_acceptable_variant")
    assert recommendation_by_id["blind-it-0080"] == (
        "maintainer_confirm_move_to_public_regression_candidate"
    )
    assert recommendation_by_id["blind-ui-0048"] == (
        "maintainer_confirm_keep_strict_primary_expected"
    )
    assert recommendation_by_id["blind-high-risk-0030"] == (
        "maintainer_confirm_move_to_public_regression_candidate"
    )


def test_gemini_261_case_requires_expected_recheck_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_REQUIRES_EXPECTED_RECHECK_261_POLICY_REVIEW)

    assert review["reviewer"] == "gemini_vertex"
    assert review["model"] == "gemini-2.5-flash"
    assert review["review_stage"] == "sanitized_requires_expected_recheck_policy_review"
    assert review["sealed_values_seen"] is False
    assert review["source_recheck_report"] == (
        "docs/reports/holdout-requires-expected-recheck-blind-v1-261-cases-2026-07-09.json"
    )
    assert review["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "gemini_received_sanitized_metadata_only": True,
    }
    assert review["summary"] == {
        "total_cases": 16,
        "policy_consistent": True,
        "needs_codex_followup": 0,
    }
    assert review["findings"] == []
    assert "cases" not in review


def test_261_case_requires_expected_recheck_final_decision_is_sanitized() -> None:
    decision = load_json(REQUIRES_EXPECTED_RECHECK_261_FINAL_DECISION)

    assert decision["report_type"] == "holdout_maintainer_final_decision_requires_expected_recheck"
    assert decision["review_stage"] == "maintainer_final_decision_requires_expected_recheck"
    assert decision["maintainer"] == "tim"
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_updated"] is True
    assert len(decision["private_expected_sha256"]) == 64
    assert decision["expected_values_included"] is False
    assert decision["acceptable_values_included"] is False
    assert decision["inputs_included"] is False
    assert decision["outputs_included"] is False
    assert decision["benchmark_rows_included"] is False
    assert decision["summary"] == {
        "reviewed_recheck_cases": 16,
        "maintainer_confirmed_acceptable_variants": 9,
        "private_expected_cases_updated": 9,
        "removed_from_sealed_to_public_regression_candidates": 5,
        "kept_strict_primary_expected": 2,
        "primary_expected_changed": 0,
        "converter_or_dictionary_changed_for_public_candidates_after_sealed_removal": True,
        "private_expected_updated": True,
        "previous_private_expected_cases": 261,
        "remaining_private_expected_cases": 256,
        "by_domain_confirmed_acceptable_variant": {
            "formal": 2,
            "high_risk": 2,
            "it": 2,
            "llm": 2,
            "ui": 1,
        },
        "by_domain_removed_to_public_regression_candidate": {
            "high_risk": 2,
            "it": 3,
        },
        "by_domain_kept_strict": {
            "formal": 1,
            "ui": 1,
        },
        "by_risk_confirmed_acceptable_variant": {
            "baseline_guard": 1,
            "candidate_gap": 6,
            "over_conversion_guard": 2,
        },
        "by_risk_removed_to_public_regression_candidate": {
            "baseline_guard": 1,
            "over_conversion_guard": 4,
        },
        "by_risk_kept_strict": {
            "candidate_gap": 2,
        },
    }
    assert decision["confirmed_acceptable_variant_case_ids"] == [
        "blind-formal-0036",
        "blind-formal-0041",
        "blind-high-risk-0022",
        "blind-high-risk-0024",
        "blind-it-0081",
        "blind-it-0085",
        "blind-llm-0035",
        "blind-llm-0042",
        "blind-ui-0059",
    ]
    assert decision["removed_to_public_regression_candidate_case_ids"] == [
        "blind-it-0080",
        "blind-it-0082",
        "blind-it-0084",
        "blind-high-risk-0028",
        "blind-high-risk-0030",
    ]
    assert decision["kept_strict_primary_expected_case_ids"] == [
        "blind-ui-0048",
        "blind-formal-0035",
    ]
    assert "cases" not in decision


def test_post_batch3_recheck_omits_sealed_values() -> None:
    report = load_json(POST_BATCH3_RECHECK)
    inputs = load_json(INPUTS)
    input_ids = {case["id"] for case in inputs["cases"]}

    assert report["report_type"] == "holdout_post_batch3_miss_recheck"
    assert report["review_stage"] == "codex_first_pass_expected_acceptable_recheck"
    assert report["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "case_recommendations_include_only_ids_and_metadata": True,
    }
    assert report["policy"] == {
        "codex_is_advisory_only": True,
        "private_expected_updated": False,
        "converter_or_dictionary_updated": False,
        "gemini_review_required_before_maintainer": True,
        "maintainer_confirmation_required_for_acceptable_variants": True,
        "holdout_signal_cases_must_not_be_used_for_tuning": True,
    }
    assert report["summary"] == {
        "current_sealed_cases": 161,
        "current_accepted": 144,
        "current_misses": 17,
        "classified_misses": 17,
        "maintainer_review_required": 11,
        "recommended_acceptable_variant_candidates": 11,
        "keep_as_holdout_signal": 6,
        "by_recommendation": {
            "keep_as_holdout_signal": 6,
            "maintainer_confirm_add_acceptable_variant": 11,
        },
        "by_priority": {"P1": 3, "P2": 14},
        "by_domain_recommendation": {
            "formal": {
                "keep_as_holdout_signal": 1,
                "maintainer_confirm_add_acceptable_variant": 1,
            },
            "high_risk": {"maintainer_confirm_add_acceptable_variant": 2},
            "it": {"maintainer_confirm_add_acceptable_variant": 2},
            "llm": {
                "keep_as_holdout_signal": 2,
                "maintainer_confirm_add_acceptable_variant": 2,
            },
            "social": {
                "keep_as_holdout_signal": 2,
                "maintainer_confirm_add_acceptable_variant": 1,
            },
            "ui": {
                "keep_as_holdout_signal": 1,
                "maintainer_confirm_add_acceptable_variant": 3,
            },
        },
        "by_risk_recommendation": {
            "baseline_guard": {"keep_as_holdout_signal": 1},
            "candidate_gap": {"maintainer_confirm_add_acceptable_variant": 9},
            "over_conversion_guard": {
                "keep_as_holdout_signal": 5,
                "maintainer_confirm_add_acceptable_variant": 2,
            },
        },
        "idempotent_misses": 17,
        "non_idempotent_misses": 0,
        "hypothetical_if_all_acceptable_recommendations_confirmed": {
            "accepted": 155,
            "misses": 6,
            "accepted_accuracy": 0.9627329192546584,
            "note": (
                "This is not an updated benchmark result; private expected is unchanged "
                "until maintainer confirms acceptable variants."
            ),
        },
    }
    assert report["private_review_packet"]["in_repo"] is False
    assert report["private_review_packet"]["contains_sealed_values"] is True
    assert "rows" not in report
    assert "inputs" not in report

    forbidden_case_fields = {
        "acceptable",
        "actual",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    cases = report["case_recommendations"]
    assert len(cases) == 17
    assert len({case["id"] for case in cases}) == len(cases)
    assert {case["id"] for case in cases} <= input_ids
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["current_benchmark_result"] == {
            "accepted": False,
            "primary_exact": False,
            "acceptable_exact": False,
            "idempotent": True,
        }
        assert case["recommendation"] in report["summary"]["by_recommendation"]
        assert case["reason_category"]
        assert case["next_step"]

    recommendation_by_id = {case["id"]: case["recommendation"] for case in cases}
    assert {
        case_id
        for case_id, recommendation in recommendation_by_id.items()
        if recommendation == "keep_as_holdout_signal"
    } == {
        "blind-ui-0011",
        "blind-llm-0026",
        "blind-llm-0028",
        "blind-formal-0029",
        "blind-social-0025",
        "blind-social-0026",
    }
    assert {
        case_id
        for case_id, recommendation in recommendation_by_id.items()
        if recommendation == "maintainer_confirm_add_acceptable_variant"
    } == {
        "blind-ui-0014",
        "blind-ui-0016",
        "blind-it-0036",
        "blind-it-0055",
        "blind-ui-0039",
        "blind-llm-0017",
        "blind-llm-0023",
        "blind-formal-0023",
        "blind-social-0024",
        "blind-high-risk-0011",
        "blind-high-risk-0012",
    }
    flags_by_id = {case["id"]: set(case["flags"]) for case in cases}
    assert flags_by_id["blind-it-0055"] == {
        "over_conversion_guard",
        "multi_term_variant",
    }
    assert flags_by_id["blind-high-risk-0011"] == {
        "high_risk",
        "medical_term_variant",
    }
    assert flags_by_id["blind-high-risk-0012"] == {
        "high_risk",
        "finance_term_variant",
    }


def test_gemini_post_batch3_recheck_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_POST_BATCH3_RECHECK_POLICY_REVIEW)

    assert review["reviewer"] == "gemini_vertex"
    assert review["model"] == "gemini-2.5-flash"
    assert review["review_stage"] == "sanitized_post_batch3_recheck_policy_review"
    assert review["sealed_values_seen"] is False
    assert review["source_recheck_report"] == (
        "docs/reports/holdout-post-batch3-miss-recheck-blind-v1-2026-07-09.json"
    )
    assert review["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "gemini_received_sanitized_metadata_only": True,
    }
    assert review["summary"] == {
        "total_cases": 17,
        "policy_consistent": True,
        "needs_codex_followup": 0,
    }
    assert review["findings"] == []
    assert "cases" not in review


def test_post_batch3_final_decision_omits_sealed_values() -> None:
    decision = load_json(POST_BATCH3_FINAL_DECISION)

    assert decision["dataset"] == "blind-v1"
    assert decision["review_stage"] == "maintainer_final_decision_post_batch3_recheck"
    assert decision["maintainer"] == "tim"
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_updated"] is True
    assert decision["expected_values_included"] is False
    assert decision["acceptable_values_included"] is False
    assert decision["inputs_included"] is False
    assert decision["outputs_included"] is False
    assert decision["benchmark_rows_included"] is False
    assert decision["summary"] == {
        "reviewed_recheck_cases": 17,
        "maintainer_confirmed_acceptable_variants": 11,
        "private_expected_cases_updated": 11,
        "skipped_existing_variants": 0,
        "kept_as_holdout_signal": 6,
        "primary_expected_changed": 0,
        "converter_or_dictionary_changed": False,
        "private_expected_updated": True,
        "by_domain": {
            "formal": 1,
            "high_risk": 2,
            "it": 2,
            "llm": 2,
            "social": 1,
            "ui": 3,
        },
        "by_risk": {
            "candidate_gap": 9,
            "over_conversion_guard": 2,
        },
        "by_priority": {
            "P1": 3,
            "P2": 8,
        },
        "by_reason_category": {
            "valid_ai_generation_term_variant": 2,
            "valid_current_state_term_variant": 1,
            "valid_debug_mode_term_variant": 1,
            "valid_finance_delivery_verb_variant_needs_confirmation": 1,
            "valid_medical_patient_term_variant_needs_confirmation": 1,
            "valid_page_position_term_variant": 1,
            "valid_record_graph_variant": 1,
            "valid_replace_verb_variant": 1,
            "valid_send_to_chat_variant_needs_confirmation": 1,
            "valid_taipei_and_field_name_variant_needs_confirmation": 1,
        },
    }
    assert decision["confirmed_case_ids"] == [
        "blind-formal-0023",
        "blind-high-risk-0011",
        "blind-high-risk-0012",
        "blind-it-0036",
        "blind-it-0055",
        "blind-llm-0017",
        "blind-llm-0023",
        "blind-social-0024",
        "blind-ui-0014",
        "blind-ui-0016",
        "blind-ui-0039",
    ]
    assert set(decision["kept_as_holdout_signal_case_ids"]) == {
        "blind-ui-0011",
        "blind-llm-0026",
        "blind-llm-0028",
        "blind-formal-0029",
        "blind-social-0025",
        "blind-social-0026",
    }
    assert "cases" not in decision


def test_remaining_signal_summary_omits_sealed_values() -> None:
    report = load_json(REMAINING_SIGNAL_SUMMARY)
    inputs = load_json(INPUTS)
    input_ids = {case["id"] for case in inputs["cases"]}

    assert report["report_type"] == "holdout_remaining_signal_summary"
    assert report["review_stage"] == "post_batch3_remaining_signal_summary"
    assert report["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "case_signals_include_only_ids_and_metadata": True,
    }
    assert report["policy"] == {
        "summary_only": True,
        "private_expected_updated": False,
        "converter_or_dictionary_updated": False,
        "do_not_tune_from_these_cases": True,
        "must_remove_from_sealed_before_any_future_tuning": True,
        "gemini_policy_review_required": True,
    }
    assert report["summary"] == {
        "current_sealed_cases": 161,
        "current_accepted": 155,
        "current_misses": 6,
        "remaining_signal_cases": 6,
        "converter_or_dictionary_updated": False,
        "private_expected_updated": False,
        "all_remaining_misses_are_holdout_signals": True,
        "by_domain": {
            "formal": 1,
            "llm": 2,
            "social": 2,
            "ui": 1,
        },
        "by_risk": {
            "baseline_guard": 1,
            "over_conversion_guard": 5,
        },
        "by_signal_category": {
            "graph_variant_over_conversion_signal": 5,
            "strict_ui_wording_signal": 1,
        },
        "by_issue_tag": {
            "formal_term": 1,
            "over_conversion": 5,
            "regional_term": 6,
            "ui_term": 1,
        },
        "idempotent_signal_cases": 6,
        "non_idempotent_signal_cases": 0,
    }
    assert "rows" not in report
    assert "inputs" not in report

    forbidden_case_fields = {
        "acceptable",
        "actual",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    cases = report["case_signals"]
    assert len(cases) == 6
    assert len({case["id"] for case in cases}) == len(cases)
    assert {case["id"] for case in cases} <= input_ids
    assert {case["id"] for case in cases} == {
        "blind-formal-0029",
        "blind-llm-0026",
        "blind-llm-0028",
        "blind-social-0025",
        "blind-social-0026",
        "blind-ui-0011",
    }
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["decision"] == "remain_sealed_holdout_signal"
        assert case["next_step"] == "keep_sealed_and_do_not_tune_against_this_case"
        assert case["current_benchmark_result"] == {
            "accepted": False,
            "primary_exact": False,
            "acceptable_exact": False,
            "idempotent": True,
        }
        assert "converter_or_dictionary_tuning" in case["prohibited_uses"]
        assert case["reason_category"]


def test_gemini_remaining_signal_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_REMAINING_SIGNAL_POLICY_REVIEW)

    assert review["reviewer"] == "gemini_vertex"
    assert review["model"] == "gemini-2.5-flash"
    assert review["review_stage"] == "sanitized_remaining_signal_policy_review"
    assert review["sealed_values_seen"] is False
    assert review["source_signal_report"] == (
        "docs/reports/holdout-remaining-signal-summary-blind-v1-2026-07-09.json"
    )
    assert review["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "gemini_received_sanitized_metadata_only": True,
    }
    assert review["summary"] == {
        "total_cases": 6,
        "policy_consistent": True,
        "needs_codex_followup": 0,
    }
    assert review["findings"] == []
    assert "cases" not in review


def test_remaining_signal_summary_after_batch6_miss_review_omits_sealed_values() -> None:
    report = load_json(REMAINING_SIGNAL_SUMMARY_AFTER_BATCH6_MISS_REVIEW)
    inputs = load_json(INPUTS)
    input_ids = {case["id"] for case in inputs["cases"]}

    assert report["report_type"] == "holdout_remaining_signal_summary"
    assert report["review_stage"] == ("after_batch6_miss_review_remaining_signal_summary")
    assert report["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "case_signals_include_only_ids_and_metadata": True,
    }
    assert report["policy"] == {
        "summary_only": True,
        "private_expected_updated": False,
        "converter_or_dictionary_updated": False,
        "do_not_tune_from_these_cases": True,
        "must_remove_from_sealed_before_any_future_tuning": True,
        "gemini_policy_review_required": True,
    }
    assert report["summary"] == {
        "current_sealed_cases": 415,
        "current_accepted": 391,
        "current_misses": 24,
        "remaining_signal_cases": 24,
        "converter_or_dictionary_updated": False,
        "private_expected_updated": False,
        "all_remaining_misses_are_holdout_signals": True,
        "by_domain": {
            "formal": 5,
            "high_risk": 3,
            "it": 3,
            "llm": 4,
            "social": 5,
            "ui": 4,
        },
        "by_risk": {"over_conversion_guard": 24},
        "by_signal_category": {
            "existing_taiwan_term_over_conversion_signal": 21,
            "high_risk_existing_term_over_conversion_signal": 3,
        },
        "by_issue_tag": {
            "formal_term": 8,
            "high_risk_term": 3,
            "it_term": 5,
            "over_conversion": 24,
            "regional_term": 24,
            "ui_term": 4,
        },
        "idempotent_signal_cases": 24,
        "non_idempotent_signal_cases": 0,
    }
    assert "rows" not in report
    assert "inputs" not in report

    forbidden_case_fields = {
        "acceptable",
        "actual",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    cases = report["case_signals"]
    assert len(cases) == 24
    assert len({case["id"] for case in cases}) == len(cases)
    assert {case["id"] for case in cases} <= input_ids
    assert {case["id"] for case in cases} == {
        "blind-llm-0026",
        "blind-llm-0028",
        "blind-formal-0029",
        "blind-social-0025",
        "blind-social-0026",
        "blind-it-0083",
        "blind-ui-0060",
        "blind-ui-0061",
        "blind-llm-0043",
        "blind-llm-0044",
        "blind-formal-0043",
        "blind-formal-0044",
        "blind-formal-0045",
        "blind-formal-0046",
        "blind-social-0042",
        "blind-social-0043",
        "blind-social-0044",
        "blind-high-risk-0026",
        "blind-high-risk-0027",
        "blind-it-0108",
        "blind-ui-0081",
        "blind-high-risk-0039",
        "blind-it-0131",
        "blind-ui-0102",
    }
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["decision"] == "remain_sealed_holdout_signal"
        assert case["next_step"] == "keep_sealed_and_do_not_tune_against_this_case"
        assert case["current_benchmark_result"] == {
            "accepted": False,
            "primary_exact": False,
            "acceptable_exact": False,
            "idempotent": True,
        }
        assert case["risk"] == "over_conversion_guard"
        assert "converter_or_dictionary_tuning" in case["prohibited_uses"]
        assert case["sealed_values_omitted"] is True


def test_gemini_remaining_signal_policy_review_after_batch6_is_sanitized() -> None:
    review = load_json(GEMINI_REMAINING_SIGNAL_POLICY_REVIEW_AFTER_BATCH6_MISS_REVIEW)

    assert review["report_type"] == (
        "holdout_gemini_policy_review_remaining_signal_after_batch6_miss_review"
    )
    assert review["reviewer"] == "gemini_cli"
    assert review["model_requested"] == "gemini-2.5-flash"
    assert review["review_stage"] == (
        "sanitized_remaining_signal_policy_review_after_batch6_miss_review"
    )
    assert review["sealed_values_seen"] is False
    assert review["source_signal_report"] == (
        "docs/reports/"
        "holdout-remaining-signal-summary-blind-v1-after-batch6-miss-review-2026-07-10.json"
    )
    assert review["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "gemini_received_sanitized_metadata_only": True,
    }
    assert review["summary"] == {
        "total_cases": 24,
        "policy_passed": True,
        "findings": 0,
        "changes_recommended": 0,
    }
    assert review["findings"] == []
    assert review["changes_recommended"] == []
    assert "cases" not in review
    assert "rows" not in review
    assert "inputs" not in review


def test_remaining_signal_summary_after_batch10_miss_review_omits_sealed_values() -> None:
    report = load_json(REMAINING_SIGNAL_SUMMARY_AFTER_BATCH10_MISS_REVIEW)
    inputs = load_json(INPUTS)
    input_ids = {case["id"] for case in inputs["cases"]}

    assert report["report_type"] == ("holdout_remaining_signal_summary_after_batch10_miss_review")
    assert report["review_stage"] == ("after_batch10_miss_review_remaining_signal_summary")
    assert report["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "benchmark_rows_included": False,
        "case_ids_and_metadata_only": True,
    }
    assert report["policy"] == {
        "converter_or_dictionary_updated_from_remaining_signals": False,
        "private_expected_updated_from_remaining_signals": False,
        "public_promotion_allowed": False,
        "requires_independent_public_reproduction_before_tuning": True,
        "do_not_use_sealed_text_for_dictionary_or_converter_changes": True,
    }
    assert report["summary"] == {
        "current_sealed_cases": 751,
        "current_accepted": 719,
        "current_misses": 32,
        "remaining_signal_cases": 32,
        "all_remaining_misses_are_holdout_signals": True,
        "maintainer_review_cases": 0,
        "public_regression_candidate_cases": 0,
        "expected_recheck_cases": 0,
        "converter_or_dictionary_updated_from_remaining_signals": False,
        "private_expected_updated_from_remaining_signals": False,
        "by_domain": {
            "formal": 6,
            "high_risk": 8,
            "it": 3,
            "llm": 4,
            "social": 6,
            "ui": 5,
        },
        "by_risk": {
            "baseline_guard": 1,
            "candidate_gap": 2,
            "over_conversion_guard": 29,
        },
        "by_signal_category": {
            "high_risk_holdout_signal": 8,
            "over_conversion_guard_holdout_signal": 24,
        },
        "by_issue_tag": {
            "baseline_guard": 1,
            "candidate_gap": 1,
            "formal_term": 10,
            "high_risk_term": 8,
            "it_term": 5,
            "over_conversion": 29,
            "regional_term": 32,
            "social_term": 1,
            "ui_term": 5,
        },
        "idempotent_signal_cases": 31,
        "non_idempotent_signal_cases": 1,
        "non_idempotent_signal_case_ids": ["blind-ui-0147"],
    }
    assert "rows" not in report
    assert "inputs" not in report

    forbidden_case_fields = {
        "acceptable",
        "actual",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    cases = report["case_signals"]
    assert len(cases) == 32
    assert len({case["id"] for case in cases}) == len(cases)
    assert {case["id"] for case in cases} <= input_ids
    assert {case["id"] for case in cases} == {
        "blind-llm-0026",
        "blind-llm-0028",
        "blind-formal-0029",
        "blind-social-0025",
        "blind-social-0026",
        "blind-it-0083",
        "blind-ui-0060",
        "blind-ui-0061",
        "blind-llm-0043",
        "blind-llm-0044",
        "blind-formal-0043",
        "blind-formal-0044",
        "blind-formal-0045",
        "blind-formal-0046",
        "blind-social-0042",
        "blind-social-0043",
        "blind-social-0044",
        "blind-high-risk-0026",
        "blind-high-risk-0027",
        "blind-it-0108",
        "blind-ui-0081",
        "blind-high-risk-0039",
        "blind-it-0131",
        "blind-ui-0102",
        "blind-high-risk-0053",
        "blind-high-risk-0058",
        "blind-ui-0147",
        "blind-formal-0105",
        "blind-high-risk-0064",
        "blind-high-risk-0068",
        "blind-social-0110",
        "blind-high-risk-0084",
    }
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["recommended_action"] == "keep_as_private_holdout_signal"
        assert case["next_step"] == (
            "use_independent_public_inputs_before_any_converter_or_dictionary_change"
        )
        assert case["sealed_values_omitted"] is True
        assert "holdout_signal_do_not_tune" in case["flags"]


def test_gemini_remaining_signal_policy_review_after_batch10_is_sanitized() -> None:
    review = load_json(GEMINI_REMAINING_SIGNAL_POLICY_REVIEW_AFTER_BATCH10_MISS_REVIEW)

    assert review["report_type"] == (
        "holdout_gemini_policy_review_remaining_signal_after_batch10_miss_review"
    )
    assert review["reviewer"] == "gemini_cli"
    assert review["model_requested"] == "gemini-2.5-pro"
    assert review["auth_type"] == "vertex-ai"
    assert review["review_stage"] == ("remaining_signal_policy_review_after_batch10_miss_review")
    assert review["review_status"] == "completed"
    assert review["sealed_values_seen"] is False
    assert review["source_signal_report"] == (
        "docs/reports/"
        "holdout-remaining-signal-summary-blind-v1-after-batch10-miss-review-2026-07-13.json"
    )
    assert review["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "benchmark_rows_included": False,
        "case_ids_and_metadata_only": True,
        "sealed_values_seen_by_gemini": False,
    }
    assert review["summary"] == {
        "total_cases": 32,
        "policy_passed": True,
        "findings": 5,
        "blocking_findings": 0,
        "changes_recommended": 0,
        "blocked": False,
    }
    assert [finding["id"] for finding in review["findings"]] == [
        "sealed_content_policy",
        "case_data_omission",
        "main_tuning_policy",
        "case_recommendations",
        "idempotency_followup",
    ]
    assert [finding["severity"] for finding in review["findings"]] == [
        "INFO",
        "INFO",
        "INFO",
        "INFO",
        "LOW",
    ]
    assert review["changes_recommended"] == []
    assert review["raw_gemini_response_report"] == (
        "docs/reports/"
        "holdout-gemini-policy-review-remaining-signal-blind-v1-after-batch10-miss-review-2026-07-13.raw.json"
    )
    assert "cases" not in review
    assert "rows" not in review
    assert "inputs" not in review


def test_holdout_remaining_40_miss_classification_omits_sealed_values() -> None:
    report = load_json(REMAINING_40_MISS_CLASSIFICATION)

    assert report["report_type"] == "holdout_remaining_40_miss_classification"
    assert report["review_stage"] == (
        "codex_private_miss_classification_first_pass_after_batch4_recheck"
    )
    assert report["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "case_recommendations_include_only_ids_and_metadata": True,
    }
    assert report["policy"] == {
        "codex_is_advisory_only": True,
        "private_expected_updated": False,
        "converter_or_dictionary_updated": False,
        "gemini_review_required_before_maintainer": True,
        "maintainer_confirmation_required_for_acceptable_variants": True,
        "move_to_public_requires_sealed_removal_before_tuning": True,
        "holdout_signal_cases_must_not_be_used_for_tuning": True,
    }
    assert report["gemini_review_policy"] == {
        "status": "completed",
        "reviewer": "gemini_vertex",
        "model": "gemini-2.5-flash",
        "report": (
            "docs/reports/"
            "holdout-gemini-policy-review-remaining-40-miss-classification-blind-v1-2026-07-09.json"
        ),
        "policy_consistent": True,
        "needs_codex_followup": 0,
        "findings": 2,
        "sealed_values_seen_by_gemini": False,
    }
    assert report["summary"] == {
        "current_sealed_cases": 256,
        "current_accepted": 216,
        "current_misses": 40,
        "classified_misses": 40,
        "maintainer_review_required": 21,
        "recommended_move_to_public_regression_candidate": 17,
        "recommended_acceptable_variant_candidates": 2,
        "requires_expected_recheck": 2,
        "keep_as_holdout_signal": 19,
        "by_recommendation": {
            "keep_as_holdout_signal": 19,
            "maintainer_confirm_add_acceptable_variant": 2,
            "maintainer_confirm_move_to_public_regression_candidate": 17,
            "requires_expected_recheck": 2,
        },
        "by_priority": {"P1": 17, "P2": 4, "P3": 19},
        "by_domain_recommendation": {
            "formal": {
                "keep_as_holdout_signal": 5,
                "maintainer_confirm_move_to_public_regression_candidate": 2,
            },
            "high_risk": {"keep_as_holdout_signal": 2},
            "it": {
                "keep_as_holdout_signal": 1,
                "maintainer_confirm_move_to_public_regression_candidate": 6,
                "requires_expected_recheck": 2,
            },
            "llm": {
                "keep_as_holdout_signal": 4,
                "maintainer_confirm_move_to_public_regression_candidate": 1,
            },
            "social": {
                "keep_as_holdout_signal": 5,
                "maintainer_confirm_move_to_public_regression_candidate": 4,
            },
            "ui": {
                "keep_as_holdout_signal": 2,
                "maintainer_confirm_add_acceptable_variant": 2,
                "maintainer_confirm_move_to_public_regression_candidate": 4,
            },
        },
        "by_risk_recommendation": {
            "baseline_guard": {
                "maintainer_confirm_add_acceptable_variant": 1,
                "maintainer_confirm_move_to_public_regression_candidate": 1,
            },
            "candidate_gap": {
                "maintainer_confirm_add_acceptable_variant": 1,
                "maintainer_confirm_move_to_public_regression_candidate": 16,
                "requires_expected_recheck": 2,
            },
            "over_conversion_guard": {"keep_as_holdout_signal": 19},
        },
        "idempotent_misses": 38,
        "non_idempotent_misses": 2,
        "high_risk_cases": 2,
        "over_conversion_guard_cases": 19,
        "hypothetical_if_all_acceptable_recommendations_confirmed": {
            "accepted": 218,
            "misses": 38,
            "accepted_accuracy": 0.8515625,
            "note": (
                "This is not an updated benchmark result; private expected is unchanged "
                "until maintainer confirms acceptable variants."
            ),
        },
        "hypothetical_if_move_candidates_removed_and_acceptable_confirmed": {
            "remaining_sealed_cases": 239,
            "accepted": 218,
            "misses": 21,
            "accepted_accuracy": 0.9121338912133892,
            "note": (
                "This is not an updated benchmark result; move candidates must be removed "
                "from sealed holdout before any tuning."
            ),
        },
    }
    assert "rows" not in report
    assert "inputs" not in report
    assert "cases" not in report

    forbidden_case_fields = {
        "acceptable",
        "actual",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    recommendations = report["case_recommendations"]
    assert len(recommendations) == 40
    assert len({case["id"] for case in recommendations}) == len(recommendations)
    for case in recommendations:
        assert not (forbidden_case_fields & set(case))
        assert case["id"].startswith("blind-")
        assert case["recommendation"] in report["summary"]["by_recommendation"]
        assert case["reason_category"]
        assert case["next_step"]

    recommendation_by_id = {case["id"]: case["recommendation"] for case in recommendations}
    assert {
        case_id
        for case_id, recommendation in recommendation_by_id.items()
        if recommendation == "maintainer_confirm_move_to_public_regression_candidate"
    } == {
        "blind-it-0063",
        "blind-it-0064",
        "blind-it-0067",
        "blind-it-0073",
        "blind-it-0076",
        "blind-it-0087",
        "blind-ui-0049",
        "blind-ui-0051",
        "blind-ui-0052",
        "blind-ui-0054",
        "blind-llm-0039",
        "blind-formal-0034",
        "blind-formal-0035",
        "blind-social-0034",
        "blind-social-0036",
        "blind-social-0040",
        "blind-social-0041",
    }
    assert {
        case_id
        for case_id, recommendation in recommendation_by_id.items()
        if recommendation == "maintainer_confirm_add_acceptable_variant"
    } == {"blind-ui-0011", "blind-ui-0048"}
    assert {
        case_id
        for case_id, recommendation in recommendation_by_id.items()
        if recommendation == "requires_expected_recheck"
    } == {"blind-it-0069", "blind-it-0070"}
    assert {
        case_id
        for case_id, recommendation in recommendation_by_id.items()
        if recommendation == "keep_as_holdout_signal"
    } == {
        "blind-llm-0026",
        "blind-llm-0028",
        "blind-formal-0029",
        "blind-social-0025",
        "blind-social-0026",
        "blind-it-0083",
        "blind-ui-0060",
        "blind-ui-0061",
        "blind-llm-0043",
        "blind-llm-0044",
        "blind-formal-0043",
        "blind-formal-0044",
        "blind-formal-0045",
        "blind-formal-0046",
        "blind-social-0042",
        "blind-social-0043",
        "blind-social-0044",
        "blind-high-risk-0026",
        "blind-high-risk-0027",
    }


def test_gemini_remaining_40_miss_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_REMAINING_40_MISS_POLICY_REVIEW)

    assert review["reviewer"] == "gemini_vertex"
    assert review["model"] == "gemini-2.5-flash"
    assert review["review_stage"] == ("sanitized_remaining_40_miss_classification_policy_review")
    assert review["sealed_values_seen"] is False
    assert review["source_classification_report"] == (
        "docs/reports/holdout-remaining-40-miss-classification-blind-v1-2026-07-09.json"
    )
    assert review["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "gemini_received_sanitized_metadata_only": True,
    }
    assert review["summary"] == {
        "total_cases": 40,
        "policy_consistent": True,
        "needs_codex_followup": 0,
        "findings": 2,
        "info_findings": 2,
        "warning_findings": 0,
        "error_findings": 0,
    }
    assert {finding["id"] for finding in review["findings"]} == {
        "blind-it-0070",
        "blind-social-0034",
    }
    assert all(finding["severity"] == "info" for finding in review["findings"])
    assert review["needs_codex_followup"] == []
    assert "cases" not in review
    assert "rows" not in review
    assert "inputs" not in review


def test_gemini_remaining_40_public_promotion_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_REMAINING_40_PUBLIC_PROMOTION_POLICY_REVIEW)

    assert review["report_type"] == ("holdout_gemini_policy_review_remaining_40_public_promotion")
    assert review["reviewer"] == "gemini_cli"
    assert review["review_stage"] == "public_regression_promotion_policy_review"
    assert review["source_promotion_gate"] == (
        "docs/reports/"
        "holdout-regression-promotion-gate-blind-v1-remaining-40-final-review-2026-07-09.json"
    )
    assert review["sealed_values_seen"] is False
    assert review["public_values_seen"] is True
    assert review["sealed_content_policy"] == {
        "reviewed_cases_removed_from_sealed_before_tuning": True,
        "remaining_sealed_holdout_signal_cases_used_for_tuning": False,
        "opencc_or_competitor_outputs_used_for_expected": False,
        "gemini_received_public_candidate_values_only": True,
    }
    assert review["summary"] == {
        "checked": 18,
        "promotion_ready": 18,
        "policy_consistent": True,
        "risk_level": "low",
        "blocking_findings": 0,
        "info_findings": 2,
    }
    assert "cases" not in review
    assert "rows" not in review
    assert "inputs" not in review


def test_remaining_40_final_decision_omits_sealed_values() -> None:
    decision = load_json(REMAINING_40_FINAL_DECISION)

    assert decision["report_type"] == (
        "holdout_maintainer_final_decision_remaining_40_miss_classification"
    )
    assert decision["review_stage"] == (
        "maintainer_final_decision_remaining_40_miss_classification"
    )
    assert decision["maintainer"] == "tim"
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_updated"] is True
    assert len(decision["private_expected_sha256"]) == 64
    assert decision["expected_values_included"] is False
    assert decision["acceptable_values_included"] is False
    assert decision["inputs_included"] is False
    assert decision["outputs_included"] is False
    assert decision["benchmark_rows_included"] is False
    assert decision["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "case_ids_and_aggregate_counts_only": True,
    }
    assert decision["summary"] == {
        "reviewed_maintainer_cases": 21,
        "maintainer_confirmed_acceptable_variants": 3,
        "private_expected_cases_updated": 3,
        "removed_from_sealed_to_public_regression_candidates": 18,
        "moved_expected_recheck_to_public_regression_candidate": 1,
        "primary_expected_changed": 0,
        "converter_or_dictionary_changed": False,
        "private_expected_updated": True,
        "previous_private_expected_cases": 256,
        "remaining_private_expected_cases": 238,
        "previous_sealed_input_cases": 256,
        "remaining_sealed_input_cases": 238,
        "public_candidates_added": 18,
        "public_candidates_requiring_zhtw_fix": 18,
        "by_domain_confirmed_acceptable_variant": {"it": 1, "ui": 2},
        "by_domain_removed_to_public_regression_candidate": {
            "formal": 2,
            "it": 7,
            "llm": 1,
            "social": 4,
            "ui": 4,
        },
        "by_risk_confirmed_acceptable_variant": {
            "baseline_guard": 1,
            "candidate_gap": 2,
        },
        "by_risk_removed_to_public_regression_candidate": {
            "baseline_guard": 1,
            "candidate_gap": 17,
        },
        "post_decision_private_benchmark_expected": {
            "remaining_sealed_cases": 238,
            "accepted": 219,
            "misses": 19,
            "accepted_accuracy": 0.9201680672268907,
            "note": "Expected benchmark projection before rerunning private benchmark sanity.",
        },
    }
    assert decision["confirmed_acceptable_variant_case_ids"] == [
        "blind-ui-0011",
        "blind-ui-0048",
        "blind-it-0069",
    ]
    assert decision["removed_to_public_regression_candidate_case_ids"] == [
        "blind-it-0063",
        "blind-it-0064",
        "blind-it-0067",
        "blind-it-0070",
        "blind-it-0073",
        "blind-it-0076",
        "blind-it-0087",
        "blind-ui-0049",
        "blind-ui-0051",
        "blind-ui-0052",
        "blind-ui-0054",
        "blind-llm-0039",
        "blind-formal-0034",
        "blind-formal-0035",
        "blind-social-0034",
        "blind-social-0036",
        "blind-social-0040",
        "blind-social-0041",
    ]
    assert len(decision["kept_sealed_holdout_signal_case_ids"]) == 19
    assert "cases" not in decision
    assert "rows" not in decision
    assert "inputs" not in decision


def test_batch10_miss_final_decision_omits_sealed_values() -> None:
    decision = load_json(MAINTAINER_BATCH10_MISS_FINAL_DECISION)

    assert decision["report_type"] == (
        "holdout_maintainer_final_decision_batch10_miss_classification"
    )
    assert decision["review_stage"] == ("maintainer_final_decision_batch10_miss_classification")
    assert decision["maintainer"] == "tim"
    assert decision["decision"] == "review_ok"
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_updated"] is True
    assert decision["expected_values_included"] is False
    assert decision["acceptable_values_included"] is False
    assert decision["inputs_included"] is False
    assert decision["outputs_included"] is False
    assert decision["benchmark_rows_included"] is False
    assert decision["source_inputs_sha256_before"] == (
        "eff19da4ff198981bdb0018bceabb128b1aa5a33e9199ea5421f69561da340d0"
    )
    assert decision["source_inputs_sha256_after"] == (
        "e6d6e8a2d0b5f9fdffaee7cc7c467cab74210eed62db0202d287bceceb2d02bf"
    )
    assert decision["source_inputs_sha256_after"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert decision["private_expected_sha256_after"] == (
        "5c89d5037efcbc33c80dd86f35ccfd12102a709fe701820b9d318fa1f8fe49dc"
    )
    assert decision["private_expected_sha256_after"] != private_expected_sha256()
    assert decision["summary"]["reviewed_maintainer_cases"] == 20
    assert decision["summary"]["maintainer_confirmed_acceptable_variants"] == 4
    assert decision["summary"]["removed_from_sealed_to_public_regression_candidates"] == 16
    assert decision["summary"]["remaining_private_expected_cases"] == 751
    assert decision["summary"]["remaining_sealed_input_cases"] == 751
    assert decision["summary"]["public_candidates_promoted_to_regression"] == 16
    assert decision["removed_to_public_regression_candidate_case_ids"] == [
        "blind-it-0217",
        "blind-it-0220",
        "blind-it-0223",
        "blind-it-0230",
        "blind-it-0235",
        "blind-it-0236",
        "blind-it-0237",
        "blind-ui-0169",
        "blind-ui-0170",
        "blind-ui-0175",
        "blind-ui-0181",
        "blind-ui-0183",
        "blind-ui-0184",
        "blind-formal-0129",
        "blind-formal-0131",
        "blind-formal-0134",
    ]
    assert decision["confirmed_acceptable_variant_case_ids"] == [
        "blind-it-0222",
        "blind-it-0232",
        "blind-llm-0123",
        "blind-llm-0137",
    ]
    assert len(decision["kept_sealed_holdout_signal_case_ids"]) == 32
    assert "cases" not in decision
    assert "rows" not in decision
    assert "inputs" not in decision


def test_holdout_public_regression_candidates_are_promoted_safely() -> None:
    candidates = load_json(HOLDOUT_CANDIDATES)
    gate = load_json(HOLDOUT_PROMOTION_GATE)
    gate_batch2 = load_json(HOLDOUT_PROMOTION_GATE_BATCH2)
    gate_batch3 = load_json(HOLDOUT_PROMOTION_GATE_BATCH3)
    gate_batch4_recheck = load_json(HOLDOUT_PROMOTION_GATE_BATCH4_RECHECK)
    gate_remaining_40 = load_json(HOLDOUT_PROMOTION_GATE_REMAINING_40_FINAL_REVIEW)
    gate_338_miss_review = load_json(HOLDOUT_PROMOTION_GATE_338_MISS_REVIEW)
    gate_batch6_miss_review = load_json(HOLDOUT_PROMOTION_GATE_BATCH6_MISS_REVIEW)
    gate_batch7_miss_review = load_json(HOLDOUT_PROMOTION_GATE_BATCH7_MISS_REVIEW)
    gate_batch8_miss_review = load_json(HOLDOUT_PROMOTION_GATE_BATCH8_MISS_REVIEW)
    gate_batch9_miss_review = load_json(HOLDOUT_PROMOTION_GATE_BATCH9_MISS_REVIEW)
    gate_batch10_miss_review = load_json(HOLDOUT_PROMOTION_GATE_BATCH10_MISS_REVIEW)
    gate_batch11_semantic_reaudit = load_json(HOLDOUT_PROMOTION_GATE_BATCH11_SEMANTIC_REAUDIT)
    gate_batch12_miss_review = load_json(HOLDOUT_PROMOTION_GATE_BATCH12_MISS_REVIEW)
    gate_batch13_miss_review = load_json(HOLDOUT_PROMOTION_GATE_BATCH13_MISS_REVIEW)
    pool_update = load_json(SEALED_POOL_UPDATE)
    pool_update_batch2 = load_json(SEALED_POOL_UPDATE_BATCH2)
    pool_update_batch3 = load_json(SEALED_POOL_UPDATE_BATCH3)
    pool_update_batch4_recheck = load_json(SEALED_POOL_UPDATE_BATCH4_RECHECK)
    pool_update_remaining_40 = load_json(SEALED_POOL_UPDATE_REMAINING_40_FINAL_REVIEW)
    pool_update_338_miss_review = load_json(SEALED_POOL_UPDATE_338_MISS_REVIEW)
    pool_update_batch6_miss_review = load_json(SEALED_POOL_UPDATE_BATCH6_MISS_REVIEW)
    pool_update_batch7_miss_review = load_json(SEALED_POOL_UPDATE_BATCH7_MISS_REVIEW)
    pool_update_batch8_miss_review = load_json(SEALED_POOL_UPDATE_BATCH8_MISS_REVIEW)
    pool_update_batch9_miss_review = load_json(SEALED_POOL_UPDATE_BATCH9_MISS_REVIEW)
    pool_update_batch10_miss_review = load_json(SEALED_POOL_UPDATE_BATCH10_MISS_REVIEW)
    pool_update_batch11_semantic_reaudit = load_json(SEALED_POOL_UPDATE_BATCH11_SEMANTIC_REAUDIT)
    pool_update_batch12_miss_review = load_json(SEALED_POOL_UPDATE_BATCH12_MISS_REVIEW)
    pool_update_batch13_miss_review = load_json(SEALED_POOL_UPDATE_BATCH13_MISS_REVIEW)
    inputs = load_json(INPUTS)

    candidate_cases = candidates["cases"]
    candidate_ids = [case["id"] for case in candidate_cases]
    remaining_input_ids = {case["id"] for case in inputs["cases"]}
    first_removed_ids = pool_update["removed_case_ids"]
    batch2_removed_ids = pool_update_batch2["removed_case_ids"]
    batch3_removed_ids = pool_update_batch3["removed_case_ids"]
    batch4_recheck_removed_ids = pool_update_batch4_recheck["removed_case_ids"]
    remaining_40_removed_ids = pool_update_remaining_40["removed_case_ids"]
    miss_338_removed_ids = pool_update_338_miss_review["removed_case_ids"]
    batch6_miss_removed_ids = pool_update_batch6_miss_review["removed_case_ids"]
    batch7_miss_removed_ids = pool_update_batch7_miss_review["removed_case_ids"]
    batch8_miss_removed_ids = pool_update_batch8_miss_review["removed_case_ids"]
    batch9_miss_removed_ids = pool_update_batch9_miss_review["removed_case_ids"]
    batch10_miss_removed_ids = pool_update_batch10_miss_review["removed_case_ids"]
    batch11_semantic_removed_ids = pool_update_batch11_semantic_reaudit["removed_case_ids"]
    batch12_miss_removed_ids = pool_update_batch12_miss_review["removed_case_ids"]
    batch13_miss_removed_ids = pool_update_batch13_miss_review["removed_case_ids"]

    assert candidates["status"] == "promoted"
    assert candidates["stats"]["total_cases"] == 219
    assert candidates["stats"]["by_domain"] == {
        "formal": 24,
        "high_risk": 7,
        "it": 108,
        "llm": 18,
        "social": 13,
        "ui": 49,
    }
    assert candidates["stats"]["by_risk"] == {
        "baseline_guard": 25,
        "candidate_gap": 171,
        "over_conversion_guard": 23,
    }
    assert candidates["stats"]["by_promotion_status"] == {
        "promoted_to_regression": 219,
    }
    assert candidates["stats"]["by_expected_source"] == {
        "human_adjudication": 126,
        "human_first_pass": 93,
    }
    assert not (set(candidate_ids) & remaining_input_ids)
    assert set(candidate_ids) == (
        set(first_removed_ids)
        | set(batch2_removed_ids)
        | set(batch3_removed_ids)
        | set(batch4_recheck_removed_ids)
        | set(remaining_40_removed_ids)
        | set(miss_338_removed_ids)
        | set(batch6_miss_removed_ids)
        | set(batch7_miss_removed_ids)
        | set(batch8_miss_removed_ids)
        | set(batch9_miss_removed_ids)
        | set(batch10_miss_removed_ids)
        | set(batch11_semantic_removed_ids)
        | set(batch12_miss_removed_ids)
        | set(batch13_miss_removed_ids)
    )

    assert pool_update["expected_values_included"] is False
    assert pool_update["inputs_included"] is False
    assert pool_update["summary"]["original_input_cases"] == 100
    assert pool_update["summary"]["removed_to_public_regression_candidates"] == 22
    assert pool_update["summary"]["remaining_sealed_input_cases"] == 78
    assert pool_update["removed_case_ids"] == candidate_ids[:22]

    assert pool_update_batch2["expected_values_included"] is False
    assert pool_update_batch2["inputs_included"] is False
    assert pool_update_batch2["summary"]["original_input_cases"] == 78
    assert pool_update_batch2["summary"]["removed_to_public_regression_candidates"] == 5
    assert pool_update_batch2["summary"]["remaining_sealed_input_cases"] == 73
    assert pool_update_batch2["removed_case_ids"] == candidate_ids[22:27]

    assert pool_update_batch3["expected_values_included"] is False
    assert pool_update_batch3["inputs_included"] is False
    assert pool_update_batch3["summary"]["original_input_cases"] == 200
    assert pool_update_batch3["summary"]["removed_to_public_regression_candidates"] == 39
    assert pool_update_batch3["summary"]["remaining_sealed_input_cases"] == 161
    assert pool_update_batch3["removed_case_ids"] == candidate_ids[27:66]

    assert pool_update_batch4_recheck["expected_values_included"] is False
    assert pool_update_batch4_recheck["inputs_included"] is False
    assert pool_update_batch4_recheck["summary"]["original_input_cases"] == 261
    assert pool_update_batch4_recheck["summary"]["removed_to_public_regression_candidates"] == 5
    assert pool_update_batch4_recheck["summary"]["remaining_sealed_input_cases"] == 256
    assert pool_update_batch4_recheck["removed_case_ids"] == candidate_ids[66:71]

    assert pool_update_remaining_40["expected_values_included"] is False
    assert pool_update_remaining_40["inputs_included"] is False
    assert pool_update_remaining_40["summary"]["original_input_cases"] == 256
    assert pool_update_remaining_40["summary"]["removed_to_public_regression_candidates"] == 18
    assert pool_update_remaining_40["summary"]["remaining_sealed_input_cases"] == 238
    assert pool_update_remaining_40["removed_case_ids"] == candidate_ids[71:89]

    assert pool_update_338_miss_review["expected_values_included"] is False
    assert pool_update_338_miss_review["inputs_included"] is False
    assert pool_update_338_miss_review["summary"]["original_input_cases"] == 338
    assert pool_update_338_miss_review["summary"]["removed_to_public_regression_candidates"] == 12
    assert pool_update_338_miss_review["summary"]["remaining_sealed_input_cases"] == 326
    assert pool_update_338_miss_review["summary"]["private_expected_acceptable_variants_added"] == 3
    assert pool_update_338_miss_review["removed_case_ids"] == candidate_ids[89:101]

    assert pool_update_batch6_miss_review["expected_values_included"] is False
    assert pool_update_batch6_miss_review["inputs_included"] is False
    assert pool_update_batch6_miss_review["summary"]["original_input_cases"] == 426
    assert (
        pool_update_batch6_miss_review["summary"]["removed_to_public_regression_candidates"] == 11
    )
    assert pool_update_batch6_miss_review["summary"]["remaining_sealed_input_cases"] == 415
    assert (
        pool_update_batch6_miss_review["summary"]["private_expected_acceptable_variants_added"] == 2
    )
    assert pool_update_batch6_miss_review["removed_case_ids"] == candidate_ids[101:112]
    assert pool_update_batch7_miss_review["expected_values_included"] is False
    assert pool_update_batch7_miss_review["inputs_included"] is False
    assert pool_update_batch7_miss_review["summary"]["original_input_cases"] == 515
    assert (
        pool_update_batch7_miss_review["summary"]["removed_to_public_regression_candidates"] == 17
    )
    assert pool_update_batch7_miss_review["summary"]["remaining_sealed_input_cases"] == 498
    assert (
        pool_update_batch7_miss_review["summary"]["private_expected_acceptable_variants_added"] == 7
    )
    assert pool_update_batch7_miss_review["removed_case_ids"] == candidate_ids[112:129]
    assert pool_update_batch8_miss_review["expected_values_included"] is False
    assert pool_update_batch8_miss_review["inputs_included"] is False
    assert pool_update_batch8_miss_review["summary"]["original_input_cases"] == 598
    assert (
        pool_update_batch8_miss_review["summary"]["removed_to_public_regression_candidates"] == 15
    )
    assert pool_update_batch8_miss_review["summary"]["remaining_sealed_input_cases"] == 583
    assert (
        pool_update_batch8_miss_review["summary"]["private_expected_acceptable_variants_added"] == 4
    )
    assert pool_update_batch8_miss_review["removed_case_ids"] == candidate_ids[129:144]
    assert pool_update_batch9_miss_review["expected_values_included"] is False
    assert pool_update_batch9_miss_review["inputs_included"] is False
    assert pool_update_batch9_miss_review["summary"]["original_input_cases"] == 683
    assert (
        pool_update_batch9_miss_review["summary"]["removed_to_public_regression_candidates"] == 16
    )
    assert pool_update_batch9_miss_review["summary"]["remaining_sealed_input_cases"] == 667
    assert (
        pool_update_batch9_miss_review["summary"]["private_expected_acceptable_variants_added"] == 6
    )
    assert pool_update_batch9_miss_review["removed_case_ids"] == candidate_ids[144:160]
    assert pool_update_batch10_miss_review["expected_values_included"] is False
    assert pool_update_batch10_miss_review["inputs_included"] is False
    assert pool_update_batch10_miss_review["summary"]["original_input_cases"] == 767
    assert (
        pool_update_batch10_miss_review["summary"]["removed_to_public_regression_candidates"] == 16
    )
    assert pool_update_batch10_miss_review["summary"]["remaining_sealed_input_cases"] == 751
    assert (
        pool_update_batch10_miss_review["summary"]["private_expected_acceptable_variants_added"]
        == 4
    )
    assert pool_update_batch10_miss_review["removed_case_ids"] == candidate_ids[160:176]
    assert pool_update_batch11_semantic_reaudit["expected_values_included"] is False
    assert pool_update_batch11_semantic_reaudit["inputs_included"] is False
    assert pool_update_batch11_semantic_reaudit["summary"] == {
        "original_sealed_cases": 851,
        "removed_cases": 10,
        "remaining_sealed_cases": 841,
        "confirmed_acceptable_variants": 4,
        "strict_private_holdout_signals": 11,
    }
    assert batch11_semantic_removed_ids == candidate_ids[176:186]
    assert pool_update_batch12_miss_review["expected_values_included"] is False
    assert pool_update_batch12_miss_review["inputs_included"] is False
    assert pool_update_batch12_miss_review["summary"] == {
        "original_sealed_cases": 941,
        "removed_cases": 11,
        "remaining_sealed_cases": 930,
        "confirmed_acceptable_variants": 4,
        "strict_private_holdout_signals": 0,
    }
    assert batch12_miss_removed_ids == candidate_ids[186:197]
    assert pool_update_batch13_miss_review["summary"] == {
        "original_sealed_cases": 1030,
        "removed_cases": 22,
        "remaining_sealed_cases": 1008,
        "confirmed_acceptable_variants": 5,
        "strict_private_holdout_signals": 7,
    }
    assert batch13_miss_removed_ids == candidate_ids[197:219]

    assert gate["summary"] == {
        "checked": 22,
        "promotion_ready": 22,
        "needs_zhtw_fix": 0,
        "convert_matches": 22,
        "convert_mismatches": 0,
        "expected_idempotent": 22,
        "expected_not_idempotent": 0,
        "output_idempotent": 22,
        "output_not_idempotent": 0,
    }
    assert gate_batch2["summary"] == {
        "checked": 5,
        "promotion_ready": 5,
        "needs_zhtw_fix": 0,
        "convert_matches": 5,
        "convert_mismatches": 0,
        "expected_idempotent": 5,
        "expected_not_idempotent": 0,
        "output_idempotent": 5,
        "output_not_idempotent": 0,
    }
    assert gate_batch3["summary"] == {
        "checked": 39,
        "promotion_ready": 39,
        "needs_zhtw_fix": 0,
        "convert_matches": 39,
        "convert_mismatches": 0,
        "expected_idempotent": 39,
        "expected_not_idempotent": 0,
        "output_idempotent": 39,
        "output_not_idempotent": 0,
    }
    assert gate_batch4_recheck["summary"] == {
        "checked": 5,
        "promotion_ready": 5,
        "needs_zhtw_fix": 0,
        "convert_matches": 5,
        "convert_mismatches": 0,
        "expected_idempotent": 5,
        "expected_not_idempotent": 0,
        "output_idempotent": 5,
        "output_not_idempotent": 0,
    }
    assert gate_remaining_40["summary"] == {
        "checked": 18,
        "promotion_ready": 18,
        "needs_zhtw_fix": 0,
        "convert_matches": 18,
        "convert_mismatches": 0,
        "expected_idempotent": 18,
        "expected_not_idempotent": 0,
        "output_idempotent": 18,
        "output_not_idempotent": 0,
    }
    assert gate_338_miss_review["summary"] == {
        "checked": 12,
        "promotion_ready": 12,
        "needs_zhtw_fix": 0,
        "convert_matches": 12,
        "convert_mismatches": 0,
        "expected_idempotent": 12,
        "expected_not_idempotent": 0,
        "output_idempotent": 12,
        "output_not_idempotent": 0,
    }
    assert gate_batch6_miss_review["summary"] == {
        "checked": 11,
        "promotion_ready": 11,
        "needs_zhtw_fix": 0,
        "convert_matches": 11,
        "convert_mismatches": 0,
        "expected_idempotent": 11,
        "expected_not_idempotent": 0,
        "output_idempotent": 11,
        "output_not_idempotent": 0,
    }
    assert gate_batch7_miss_review["summary"] == {
        "checked": 17,
        "promotion_ready": 17,
        "needs_zhtw_fix": 0,
        "convert_matches": 17,
        "convert_mismatches": 0,
        "expected_idempotent": 17,
        "expected_not_idempotent": 0,
        "output_idempotent": 17,
        "output_not_idempotent": 0,
    }
    assert gate_batch8_miss_review["summary"] == {
        "checked": 15,
        "promotion_ready": 15,
        "needs_zhtw_fix": 0,
        "convert_matches": 15,
        "convert_mismatches": 0,
        "expected_idempotent": 15,
        "expected_not_idempotent": 0,
        "output_idempotent": 15,
        "output_not_idempotent": 0,
    }
    assert gate_batch9_miss_review["summary"] == {
        "checked": 16,
        "promotion_ready": 16,
        "needs_zhtw_fix": 0,
        "convert_matches": 16,
        "convert_mismatches": 0,
        "expected_idempotent": 16,
        "expected_not_idempotent": 0,
        "output_idempotent": 16,
        "output_not_idempotent": 0,
    }
    assert gate_batch10_miss_review["summary"] == {
        "checked": 16,
        "promotion_ready": 16,
        "needs_zhtw_fix": 0,
        "convert_matches": 16,
        "convert_mismatches": 0,
        "expected_idempotent": 16,
        "expected_not_idempotent": 0,
        "output_idempotent": 16,
        "output_not_idempotent": 0,
    }
    assert gate_batch11_semantic_reaudit["summary"] == {
        "candidate_cases": 10,
        "zhtw_exact_matches": 10,
        "promotion_ready": 10,
        "promoted_to_regression": 10,
        "full_sentence_mappings_added": 10,
        "identity_mappings_added": 10,
        "regression_total_cases": 1218,
        "gate_passed": True,
    }
    assert gate_batch12_miss_review["summary"] == {
        "candidate_cases": 11,
        "zhtw_exact_matches": 11,
        "expected_idempotent": 11,
        "promotion_ready": 11,
        "promoted_to_regression": 11,
        "full_sentence_mappings_added": 11,
        "identity_mappings_added": 11,
        "candidate_dataset_total_cases": 197,
        "regression_total_cases": 1229,
        "gate_passed": True,
    }
    assert gate_batch13_miss_review["summary"] == {
        "candidate_cases": 22,
        "zhtw_exact_matches": 22,
        "expected_idempotent": 22,
        "promotion_ready": 22,
        "promoted_to_regression": 22,
        "full_sentence_mappings_added": 22,
        "identity_mappings_added": 22,
        "candidate_dataset_total_cases": 219,
        "regression_total_cases": 1251,
        "gate_passed": True,
    }
    gate_by_id = {
        case["id"]: case
        for case in (
            gate["cases"]
            + gate_batch2["cases"]
            + gate_batch3["cases"]
            + gate_batch4_recheck["cases"]
            + gate_remaining_40["cases"]
            + gate_338_miss_review["cases"]
            + gate_batch6_miss_review["cases"]
            + gate_batch7_miss_review["cases"]
            + gate_batch8_miss_review["cases"]
            + gate_batch9_miss_review["cases"]
            + gate_batch10_miss_review["cases"]
        )
    }
    gate_by_id.update(
        {
            case_id: {"status": "promotion_ready"}
            for case_id in gate_batch11_semantic_reaudit["promoted_case_ids"]
        }
    )
    gate_by_id.update(
        {
            case_id: {"status": "promotion_ready"}
            for case_id in gate_batch12_miss_review["promoted_case_ids"]
        }
    )
    gate_by_id.update(
        {
            case_id: {"status": "promotion_ready"}
            for case_id in gate_batch13_miss_review["promoted_case_ids"]
        }
    )
    for case in candidate_cases:
        if case["id"] in batch13_miss_removed_ids:
            expected_gate_report = str(HOLDOUT_PROMOTION_GATE_BATCH13_MISS_REVIEW.relative_to(ROOT))
        elif case["id"] in batch12_miss_removed_ids:
            expected_gate_report = str(HOLDOUT_PROMOTION_GATE_BATCH12_MISS_REVIEW.relative_to(ROOT))
        elif case["id"] in batch11_semantic_removed_ids:
            expected_gate_report = str(
                HOLDOUT_PROMOTION_GATE_BATCH11_SEMANTIC_REAUDIT.relative_to(ROOT)
            )
        elif case["id"] in batch10_miss_removed_ids:
            expected_gate_report = str(HOLDOUT_PROMOTION_GATE_BATCH10_MISS_REVIEW.relative_to(ROOT))
        elif case["id"] in batch9_miss_removed_ids:
            expected_gate_report = str(HOLDOUT_PROMOTION_GATE_BATCH9_MISS_REVIEW.relative_to(ROOT))
        elif case["id"] in batch8_miss_removed_ids:
            expected_gate_report = str(HOLDOUT_PROMOTION_GATE_BATCH8_MISS_REVIEW.relative_to(ROOT))
        elif case["id"] in batch7_miss_removed_ids:
            expected_gate_report = str(HOLDOUT_PROMOTION_GATE_BATCH7_MISS_REVIEW.relative_to(ROOT))
        elif case["id"] in batch6_miss_removed_ids:
            expected_gate_report = str(HOLDOUT_PROMOTION_GATE_BATCH6_MISS_REVIEW.relative_to(ROOT))
        elif case["id"] in miss_338_removed_ids:
            expected_gate_report = str(HOLDOUT_PROMOTION_GATE_338_MISS_REVIEW.relative_to(ROOT))
        elif case["id"] in remaining_40_removed_ids:
            expected_gate_report = str(
                HOLDOUT_PROMOTION_GATE_REMAINING_40_FINAL_REVIEW.relative_to(ROOT)
            )
        elif case["id"] in batch4_recheck_removed_ids:
            expected_gate_report = str(HOLDOUT_PROMOTION_GATE_BATCH4_RECHECK.relative_to(ROOT))
        elif case["id"] in batch3_removed_ids:
            expected_gate_report = str(HOLDOUT_PROMOTION_GATE_BATCH3.relative_to(ROOT))
        elif case["id"] in batch2_removed_ids:
            expected_gate_report = str(HOLDOUT_PROMOTION_GATE_BATCH2.relative_to(ROOT))
        else:
            expected_gate_report = str(HOLDOUT_PROMOTION_GATE.relative_to(ROOT))

        assert case["source"]["type"] == "sealed_holdout_removed_case"
        assert case["review"]["approval_policy"] == "single_human_with_ai_advisory"
        assert case["promotion"]["status"] in {
            "needs_zhtw_fix",
            "promoted_to_regression",
        }
        assert case["promotion"]["gate_report"] == expected_gate_report
        assert case["promotion"]["promoted_id"] == f"holdout/{case['id']}"
        assert gate_by_id[case["id"]]["status"] == case["promotion"]["status"].replace(
            "promoted_to_regression", "promotion_ready"
        )
        if case["promotion"]["status"] == "promoted_to_regression":
            assert convert(case["input"]) == case["expected"]
            assert convert(case["expected"]) == case["expected"]
        else:
            assert case["id"] in remaining_40_removed_ids
            assert convert(case["input"]) != case["expected"]


def test_run_accuracy_benchmark_with_temp_fixture(tmp_path: Path) -> None:
    inputs_path = tmp_path / "blind.inputs.json"
    expected_path = tmp_path / "blind.expected.json"
    output_prefix = tmp_path / "accuracy-benchmark-test"
    input_text = "这个函数会抛出异常。"
    expected_text = convert(input_text)

    inputs_path.write_text(
        json.dumps(
            {
                "version": 1,
                "name": "blind-v1.inputs",
                "dataset": "blind-v1",
                "description": "test fixture",
                "generated_date": "2026-07-07",
                "status": "frozen_inputs",
                "publish_state": "public_inputs_only",
                "target_total": 2000,
                "source_policy": {
                    "expected_not_in_inputs": True,
                    "allowed_input_sources": ["test"],
                    "forbidden_expected_sources": ["zhtw output"],
                    "copyright_policy": "test",
                },
                "annotation_protocol": {
                    "review_order": ["first", "second", "adjudication"],
                    "minimum_human_reviewers": 2,
                    "adjudication_required_on_disagreement": True,
                    "normalization": ["Unicode NFC"],
                },
                "batches": [
                    {
                        "id": "test-batch",
                        "domain": "it",
                        "target_cases": 1,
                        "priority": 1,
                        "focus": ["test"],
                    }
                ],
                "stats": {
                    "total_collected": 1,
                    "by_domain": {"it": 1},
                    "by_risk": {"candidate_gap": 1},
                },
                "cases": [
                    {
                        "id": "fixture-0001",
                        "batch": "test-batch",
                        "domain": "it",
                        "input": input_text,
                        "risk": "candidate_gap",
                        "source": {
                            "type": "test",
                            "citation": "test",
                            "license": "test",
                        },
                        "tags": ["test"],
                        "notes": "test",
                    }
                ],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    inputs_hash = hashlib.sha256(inputs_path.read_bytes()).hexdigest()
    expected_path.write_text(
        json.dumps(
            {
                "version": 1,
                "name": "blind-v1.expected",
                "dataset": "blind-v1",
                "description": "test fixture",
                "generated_date": "2026-07-07",
                "status": "sealed_private",
                "source_inputs": str(inputs_path),
                "source_inputs_sha256": inputs_hash,
                "expected_policy": {
                    "expected_source": "human_review_only",
                    "forbidden_expected_sources": ["zhtw output"],
                    "minimum_human_reviewers": 2,
                    "adjudication_required_on_disagreement": True,
                    "normalization": ["Unicode NFC"],
                },
                "cases": [
                    {
                        "id": "fixture-0001",
                        "expected": expected_text,
                        "acceptable": [],
                        "annotation": {
                            "expected_source": "human_first_pass",
                            "first_reviewer": "fixture",
                            "second_reviewer": "fixture",
                            "adjudicator": "",
                            "disagreement": False,
                            "decision_date": "2026-07-07",
                            "notes": (
                                "fixture expected equals current zhtw output for runner plumbing"
                            ),
                        },
                        "issue_tags": ["it_term"],
                    }
                ],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            str(RUNNER),
            "--inputs",
            str(inputs_path),
            "--expected",
            str(expected_path),
            "--competitors-lock",
            str(COMPETITORS_LOCK),
            "--competitors",
            "zhtw",
            "--formats",
            "json,md",
            "--output-prefix",
            str(output_prefix),
            "--generated-date",
            "2026-07-07",
            "--fail-on-zhtw-miss",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert "cases=1 zhtw_accepted=1 zhtw_misses=0" in result.stdout

    payload = load_json(output_prefix.with_suffix(".json"))
    assert payload["report_mode"] == "aggregate"
    assert payload["dataset_classification"] == "published_evaluation"
    assert payload["summary"]["case_count"] == 1
    assert payload["engines"]["zhtw"]["scores"]["accepted_accuracy"] == 1.0
    assert payload["engines"]["zhtw"]["scores"]["micro_accuracy"] == 1.0
    assert payload["engines"]["zhtw"]["scores"]["macro_domain_accuracy"] == 1.0
    assert payload["engines"]["zhtw"]["scores"]["conversion_recall"] == 1.0
    assert payload["engines"]["zhtw"]["scores"]["p0_error_count"] == 0
    assert payload["engines"]["zhtw"]["scores"]["changed_span"]["f1"] == 1.0
    assert payload["engines"]["zhtw"]["scores"]["primary_exact_accuracy"] == 1.0
    assert "rows" not in payload
    assert "expected" not in payload
    assert payload["expected_sha256"] == hashlib.sha256(expected_path.read_bytes()).hexdigest()
    assert payload["provenance"]["zhtw_version"] == ZHTW_VERSION
    assert len(payload["provenance"]["git_sha"]) == 40
    assert payload["provenance"]["python_version"]
    assert payload["provenance"]["os"]
    assert payload["provenance"]["architecture"]
    assert len(payload["provenance"]["runner_sha256"]) == 64
    assert (
        output_prefix.with_suffix(".md")
        .read_text(encoding="utf-8")
        .startswith("<!-- zhtw:disable -->")
    )

    detailed_prefix = tmp_path / "accuracy-benchmark-detailed"
    detailed_result = subprocess.run(
        [
            sys.executable,
            str(RUNNER),
            "--inputs",
            str(inputs_path),
            "--expected",
            str(expected_path),
            "--competitors-lock",
            str(COMPETITORS_LOCK),
            "--competitors",
            "zhtw",
            "--formats",
            "json",
            "--output-prefix",
            str(detailed_prefix),
            "--report-mode",
            "detailed",
            "--generated-date",
            "2026-07-07",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert detailed_result.returncode == 0, detailed_result.stdout + detailed_result.stderr
    detailed = load_json(detailed_prefix.with_suffix(".json"))
    assert detailed["report_mode"] == "detailed"
    assert detailed["private_expected"]["path"] == str(expected_path)
    assert detailed["rows"][0]["evaluations"]["zhtw"]["accepted"] is True
