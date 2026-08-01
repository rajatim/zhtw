# zhtw:disable
# ruff: noqa: F403,F405
"""Blind-v1 collection and annotation history tests."""

from tests._accuracy_holdout_support import *  # noqa: F403


def test_batch13_miss_final_decision_promotion_and_sanity_are_auditable() -> None:
    final = load_json(MAINTAINER_BATCH13_MISS_FINAL_DECISION)
    pool = load_json(SEALED_POOL_UPDATE_BATCH13_MISS_REVIEW)
    gate = load_json(HOLDOUT_PROMOTION_GATE_BATCH13_MISS_REVIEW)
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH13_MISS_REVIEW)
    inputs = load_json(INPUTS)
    expected = load_json(EXPECTED)
    candidates = load_json(ROOT / "benchmarks/accuracy/holdout-regression-candidates-v1.json")
    regression = load_json(ROOT / "benchmarks/accuracy/regression-v1.json")

    assert final["decision"] == "review_ok"
    assert final["summary"]["reviewed_batch13_misses"] == 34
    assert len(final["confirmed_acceptable_variant_case_ids"]) == 5
    assert len(final["removed_to_public_regression_candidate_case_ids"]) == 22
    assert len(final["strict_private_holdout_signal_case_ids"]) == 7
    assert pool["summary"] == {
        "original_sealed_cases": 1030,
        "removed_cases": 22,
        "remaining_sealed_cases": 1008,
        "confirmed_acceptable_variants": 5,
        "strict_private_holdout_signals": 7,
    }
    assert not (set(pool["removed_case_ids"]) & {case["id"] for case in inputs["cases"]})
    assert len(inputs["cases"]) == len(expected["cases"]) == 1008
    assert expected["source_inputs_sha256"] == hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert gate["summary"] == {
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
    assert candidates["stats"]["total_cases"] == 219
    assert regression["stats"]["by_classification"]["holdout_regression_promoted"] == 219
    assert sanity["summary"]["case_count"] == 1008
    assert sanity["summary"]["accepted"] == 955
    assert sanity["summary"]["misses"] == 53
    assert sanity["summary"]["accepted_accuracy"] == 0.9474206349206349
    assert sanity["interpretation_policy"]["denominator_changed"] is True
    assert sanity["interpretation_policy"]["pure_capability_gain_claim_allowed"] is False
    for report in (final, pool, gate, sanity):
        assert report.get("expected_values_included", False) is False
        assert report.get("inputs_included", False) is False
        assert "cases" not in report


def original_seed_ids_from_report(report_ids: list[str], input_ids: list[str]) -> list[str]:
    report_id_set = set(report_ids)
    return [case_id for case_id in input_ids if case_id in report_id_set]


def test_blind_v1_schema_files_exist() -> None:
    inputs_schema = load_json(INPUTS_SCHEMA)
    expected_schema = load_json(EXPECTED_SCHEMA)
    candidates_schema = load_json(HOLDOUT_CANDIDATES_SCHEMA)

    assert inputs_schema["title"] == "zhtw published evaluation input dataset"
    assert expected_schema["title"] == "zhtw published evaluation expected dataset"
    assert candidates_schema["title"] == "zhtw holdout regression candidates"
    assert inputs_schema["properties"]["target_total"]["const"] == 2000
    assert (
        expected_schema["properties"]["expected_policy"]["properties"]["expected_source"]["const"]
        == "human_review_only"
    )
    expected_policy = expected_schema["properties"]["expected_policy"]["properties"]
    assert expected_policy["approval_policy"]["enum"] == [
        "two_human_reviewers",
        "single_human_with_ai_advisory",
    ]
    assert expected_policy["minimum_human_reviewers"]["minimum"] == 1

    annotation = expected_schema["properties"]["cases"]["items"]["properties"]["annotation"]
    assert "approval_policy" in annotation["required"]
    assert "ai_advisory_reviewers" in annotation["required"]
    assert "source_reports" in annotation["required"]
    assert annotation["properties"]["ai_advisory_reviewers"]["items"]["enum"] == [
        "codex",
        "gemini_vertex",
        "gemini_cli",
    ]


def test_blind_v1_is_classified_as_published_evaluation() -> None:
    metadata = load_json(BLIND_V1_METADATA)

    assert metadata["benchmark_classification"] == "published_evaluation"
    assert metadata["fresh_holdout"] is False
    assert metadata["sealed"] is False
    assert metadata["inputs_sha256"] == hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert metadata["expected_sha256"] == private_expected_sha256()
    assert metadata["superseding_plan"] == ("docs/plans/2026-07-19-external-benchmark-v2-plan.md")


def test_blind_v1_inputs_are_input_only_seed_pool() -> None:
    data = load_json(INPUTS)
    cases = data["cases"]

    assert data["name"] == "blind-v1.inputs"
    assert data["dataset"] == "blind-v1"
    assert data["status"] == "collecting_inputs"
    assert data["publish_state"] == "public_inputs_only"
    assert data["target_total"] == 2000
    assert data["source_policy"]["expected_not_in_inputs"] is True
    assert len(cases) == data["stats"]["total_collected"] == 1008

    case_ids = [case["id"] for case in cases]
    assert len(case_ids) == len(set(case_ids))
    assert not (load_all_removed_case_ids() & set(case_ids))
    assert not (
        {
            "blind-it-0002",
            "blind-ui-0020",
            "blind-formal-0003",
            "blind-it-0026",
            "blind-high-risk-0016",
            "blind-it-0080",
            "blind-it-0082",
            "blind-it-0084",
            "blind-high-risk-0028",
            "blind-high-risk-0030",
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
        }
        & set(case_ids)
    )
    forbidden_case_fields = {"expected", "acceptable", "review", "annotation"}
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["input"]
        assert case["source"]["license"] == "MIT-compatible project original text"
        assert case["notes"] == "Input only; expected must be human reviewed separately."

    by_domain = Counter(case["domain"] for case in cases)
    by_risk = Counter(case["risk"] for case in cases)
    assert dict(sorted(by_domain.items())) == data["stats"]["by_domain"]
    assert dict(sorted(by_risk.items())) == data["stats"]["by_risk"]
    assert by_domain == {
        "formal": 164,
        "high_risk": 128,
        "it": 189,
        "llm": 159,
        "social": 180,
        "ui": 188,
    }
    assert by_risk == {
        "baseline_guard": 161,
        "candidate_gap": 564,
        "over_conversion_guard": 283,
    }

    targets = {batch["id"]: batch["target_cases"] for batch in data["batches"]}
    assert sum(targets.values()) == data["target_total"]
    assert targets == {
        "blind-it-api-cli": 500,
        "blind-ui-i18n": 400,
        "blind-llm-content": 300,
        "blind-formal-news": 300,
        "blind-social-daily": 300,
        "blind-high-risk": 200,
    }


def test_holdout_input_pool_expansion_omits_expected_and_input_text() -> None:
    inputs = load_json(INPUTS)
    report = load_json(INPUT_POOL_EXPANSION)
    input_ids = {case["id"] for case in inputs["cases"]}

    assert report["report_type"] == "holdout_input_pool_expansion"
    assert report["dataset"] == "blind-v1"
    assert report["expected_values_included"] is False
    assert report["inputs_included"] is False
    assert report["new_cases_include_only_ids_and_metadata"] is True
    assert "cases" not in report
    assert "inputs" not in report
    assert report["summary"] == {
        "previous_input_cases": 73,
        "added_input_cases": 127,
        "current_input_cases": 200,
        "target_total": 2000,
        "added_by_domain": {
            "formal": 18,
            "high_risk": 10,
            "it": 37,
            "llm": 17,
            "social": 18,
            "ui": 27,
        },
        "current_by_domain": {
            "formal": 30,
            "high_risk": 20,
            "it": 50,
            "llm": 30,
            "social": 30,
            "ui": 40,
        },
        "added_by_risk": {
            "baseline_guard": 17,
            "candidate_gap": 79,
            "over_conversion_guard": 31,
        },
        "current_by_risk": {
            "baseline_guard": 30,
            "candidate_gap": 120,
            "over_conversion_guard": 50,
        },
    }
    assert len(report["new_case_ids"]) == 127
    assert set(report["new_case_ids"]) <= input_ids | load_all_removed_case_ids()
    assert report["policy"]["expected_not_generated"] is True
    assert report["policy"]["converter_outputs_not_used"] is True


def test_holdout_expansion_advisory_reports_are_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expansion = load_json(INPUT_POOL_EXPANSION)
    codex = load_json(CODEX_EXPANSION_FIRST_PASS)
    gemini = load_json(GEMINI_EXPANSION_ADVISORY)
    diff = load_json(CODEX_GEMINI_EXPANSION_DIFF_REVIEW)

    input_ids = {case["id"] for case in inputs["cases"]}
    expansion_ids = set(expansion["new_case_ids"])

    assert codex["review_stage"] == "first_pass_advisory"
    assert codex["reviewer"] == "codex"
    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["summary"] == {
        "total_cases": 127,
        "by_domain": {
            "formal": 18,
            "high_risk": 10,
            "it": 37,
            "llm": 17,
            "social": 18,
            "ui": 27,
        },
        "by_confidence": {"high": 87, "medium": 40},
        "review_needed": 71,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in codex["cases"]} == expansion_ids
    assert expansion_ids <= input_ids | load_all_removed_case_ids()
    assert all(case["codex_expected"] for case in codex["cases"])
    assert not any(case["promotion_allowed"] for case in codex["cases"])

    assert gemini["review_stage"] == "independent_holdout_expected_review_aggregate"
    assert gemini["reviewer"] == "gemini_vertex"
    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert len(gemini["source_reports"]) == 8
    assert gemini["summary"] == {
        "total_cases": 127,
        "exact_matches_with_codex": 79,
        "differences_from_codex": 48,
        "needs_maintainer_review": 81,
        "by_domain": {
            "formal": 18,
            "high_risk": 10,
            "it": 37,
            "llm": 17,
            "social": 18,
            "ui": 27,
        },
        "by_gemini_confidence": {"high": 127},
        "promotion_allowed": False,
    }
    assert {case["id"] for case in gemini["review"]["cases"]} == expansion_ids
    assert {row["id"] for row in gemini["comparisons"]} == expansion_ids

    assert diff["review_stage"] == "codex_gemini_difference_review"
    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["summary"] == {
        "total_cases": 127,
        "exact_matches": 79,
        "differences": 48,
        "exact_but_policy_review": 33,
        "no_immediate_question": 46,
        "maintainer_queue_total": 81,
        "difference_recommendations": {
            "codex": 39,
            "gemini": 7,
            "third_value": 2,
        },
        "promotion_allowed": False,
    }
    difference_ids = {case["id"] for case in diff["differences"]}
    policy_ids = {case["id"] for case in diff["exact_but_policy_review"]}
    no_question_ids = {case["id"] for case in diff["no_immediate_question"]}
    assert difference_ids | policy_ids | no_question_ids == expansion_ids
    assert not (difference_ids & policy_ids)
    assert not (difference_ids & no_question_ids)
    assert not (policy_ids & no_question_ids)


def test_holdout_batch4_input_pool_expansion_omits_expected_and_input_text() -> None:
    inputs = load_json(INPUTS)
    report = load_json(INPUT_POOL_EXPANSION_BATCH4)
    input_ids = {case["id"] for case in inputs["cases"]}

    assert report["report_type"] == "holdout_input_pool_expansion"
    assert report["dataset"] == "blind-v1"
    assert report["batch"] == "batch4_100_cases"
    assert report["expected_values_included"] is False
    assert report["inputs_included"] is False
    assert report["new_cases_include_only_ids_and_metadata"] is True
    assert "cases" not in report
    assert "inputs" not in report
    assert report["summary"] == {
        "previous_input_cases": 161,
        "added_input_cases": 100,
        "current_input_cases": 261,
        "target_total": 2000,
        "added_by_domain": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "current_by_domain": {
            "formal": 41,
            "high_risk": 28,
            "it": 53,
            "llm": 43,
            "social": 44,
            "ui": 52,
        },
        "added_by_risk": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
        "current_by_risk": {
            "baseline_guard": 40,
            "candidate_gap": 154,
            "over_conversion_guard": 67,
        },
    }
    assert len(report["new_case_ids"]) == 100
    assert set(report["new_case_ids"]) <= input_ids | load_all_removed_case_ids()
    assert report["new_case_ids"][0] == "blind-it-0063"
    assert report["new_case_ids"][-1] == "blind-high-risk-0030"
    assert report["policy"]["expected_not_generated"] is True
    assert report["policy"]["converter_outputs_not_used"] is True


def test_holdout_batch5_input_pool_expansion_omits_expected_and_input_text() -> None:
    inputs = load_json(INPUTS)
    report = load_json(INPUT_POOL_EXPANSION_BATCH5)
    input_ids = {case["id"] for case in inputs["cases"]}

    assert report["report_type"] == "holdout_input_pool_expansion"
    assert report["dataset"] == "blind-v1"
    assert report["batch"] == "batch5_100_cases"
    assert report["expected_values_included"] is False
    assert report["inputs_included"] is False
    assert report["new_cases_include_only_ids_and_metadata"] is True
    assert "cases" not in report
    assert "inputs" not in report
    assert report["summary"] == {
        "previous_input_cases": 238,
        "added_input_cases": 100,
        "current_input_cases": 338,
        "target_total": 2000,
        "added_by_domain": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "current_by_domain": {
            "formal": 54,
            "high_risk": 36,
            "it": 68,
            "llm": 57,
            "social": 55,
            "ui": 68,
        },
        "added_by_risk": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
        "current_by_risk": {
            "baseline_guard": 53,
            "candidate_gap": 197,
            "over_conversion_guard": 88,
        },
    }
    assert len(report["new_case_ids"]) == 100
    assert set(report["new_case_ids"]) <= input_ids | load_all_removed_case_ids()
    assert report["new_case_ids"][0] == "blind-it-0088"
    assert report["new_case_ids"][-1] == "blind-high-risk-0040"
    assert report["policy"]["expected_not_generated"] is True
    assert report["policy"]["converter_outputs_not_used"] is True


def test_holdout_batch6_input_pool_expansion_omits_expected_and_input_text() -> None:
    inputs = load_json(INPUTS)
    report = load_json(INPUT_POOL_EXPANSION_BATCH6)
    input_ids = {case["id"] for case in inputs["cases"]}

    assert report["report_type"] == "holdout_input_pool_expansion"
    assert report["dataset"] == "blind-v1"
    assert report["batch"] == "batch6_100_cases"
    assert report["expected_values_included"] is False
    assert report["inputs_included"] is False
    assert report["new_cases_include_only_ids_and_metadata"] is True
    assert "cases" not in report
    assert "inputs" not in report
    assert report["source_inputs_sha256"] == (
        "be3ab808d2f2bb71b1c86e66cd95eb182446693412c1ebbecdf5aa632f35d35e"
    )
    assert report["summary"] == {
        "previous_input_cases": 326,
        "added_input_cases": 100,
        "current_input_cases": 426,
        "target_total": 2000,
        "added_by_domain": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "current_by_domain": {
            "formal": 69,
            "high_risk": 46,
            "it": 86,
            "llm": 71,
            "social": 70,
            "ui": 84,
        },
        "added_by_risk": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
        "current_by_risk": {
            "baseline_guard": 67,
            "candidate_gap": 246,
            "over_conversion_guard": 113,
        },
        "private_expected_cases_currently_reviewed": 326,
        "new_cases_pending_expected_review": 100,
    }
    assert len(report["new_case_ids"]) == 100
    assert set(report["new_case_ids"]) <= input_ids | load_all_removed_case_ids()
    assert set(report["new_case_ids"]) & load_all_removed_case_ids() == set(
        load_json(SEALED_POOL_UPDATE_BATCH6_MISS_REVIEW)["removed_case_ids"]
    )
    assert report["new_case_ids"][0] == "blind-it-0113"
    assert report["new_case_ids"][-1] == "blind-high-risk-0050"
    assert report["policy"]["expected_not_generated"] is True
    assert report["policy"]["converter_outputs_not_used"] is True


def test_holdout_batch7_input_pool_expansion_omits_expected_and_input_text() -> None:
    inputs = load_json(INPUTS)
    report = load_json(INPUT_POOL_EXPANSION_BATCH7)
    input_ids = {case["id"] for case in inputs["cases"]}

    assert report["report_type"] == "holdout_input_pool_expansion"
    assert report["dataset"] == "blind-v1"
    assert report["batch"] == "batch7_100_cases"
    assert report["expected_values_included"] is False
    assert report["inputs_included"] is False
    assert report["new_cases_include_only_ids_and_metadata"] is True
    assert "cases" not in report
    assert "inputs" not in report
    assert report["source_inputs_sha256"] == (
        "27a3ec40cf4f5df586524d3ec307f3fcbf164a1e1ece097cc8637cd484cb5dc1"
    )
    assert report["summary"] == {
        "previous_input_cases": 415,
        "added_input_cases": 100,
        "current_input_cases": 515,
        "target_total": 2000,
        "added_by_domain": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "current_by_domain": {
            "formal": 84,
            "high_risk": 56,
            "it": 101,
            "llm": 86,
            "social": 85,
            "ui": 103,
        },
        "added_by_risk": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
        "current_by_risk": {
            "baseline_guard": 81,
            "candidate_gap": 296,
            "over_conversion_guard": 138,
        },
        "private_expected_cases_currently_reviewed": 415,
        "new_cases_pending_expected_review": 100,
    }
    assert len(report["new_case_ids"]) == 100
    assert set(report["new_case_ids"]) <= input_ids | load_all_removed_case_ids()
    assert report["new_case_ids"][0] == "blind-it-0138"
    assert report["new_case_ids"][-1] == "blind-high-risk-0060"
    assert report["policy"]["expected_not_generated"] is True
    assert report["policy"]["converter_outputs_not_used"] is True


def test_holdout_batch8_input_pool_expansion_omits_expected_and_input_text() -> None:
    inputs = load_json(INPUTS)
    report = load_json(INPUT_POOL_EXPANSION_BATCH8)
    input_ids = {case["id"] for case in inputs["cases"]}

    assert report["report_type"] == "holdout_input_pool_expansion"
    assert report["dataset"] == "blind-v1"
    assert report["batch"] == "batch8_100_cases"
    assert report["expected_values_included"] is False
    assert report["inputs_included"] is False
    assert report["new_cases_include_only_ids_and_metadata"] is True
    assert "cases" not in report
    assert "inputs" not in report
    assert report["source_inputs_sha256"] == (
        "287b30b7d08ac7761fc78624e8db5f9f9d2664a214feef6b06dfe401cdd719cb"
    )
    assert report["summary"] == {
        "previous_input_cases": 498,
        "added_input_cases": 100,
        "current_input_cases": 598,
        "target_total": 2000,
        "added_by_domain": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "current_by_domain": {
            "formal": 98,
            "high_risk": 66,
            "it": 115,
            "llm": 99,
            "social": 99,
            "ui": 121,
        },
        "added_by_risk": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
        "current_by_risk": {
            "baseline_guard": 94,
            "candidate_gap": 341,
            "over_conversion_guard": 163,
        },
        "private_expected_cases_currently_reviewed": 498,
        "new_cases_pending_expected_review": 100,
    }
    assert len(report["new_case_ids"]) == 100
    assert set(report["new_case_ids"]) <= input_ids | load_all_removed_case_ids()
    assert set(report["new_case_ids"]) & load_all_removed_case_ids() == set(
        load_json(SEALED_POOL_UPDATE_BATCH8_MISS_REVIEW)["removed_case_ids"]
    )
    assert report["new_case_ids"][0] == "blind-it-0163"
    assert report["new_case_ids"][-1] == "blind-high-risk-0070"
    assert report["policy"]["expected_not_generated"] is True
    assert report["policy"]["converter_outputs_not_used"] is True
    assert report["policy"]["private_expected_not_modified"] is True


def test_holdout_batch9_input_pool_expansion_omits_expected_and_input_text() -> None:
    inputs = load_json(INPUTS)
    report = load_json(INPUT_POOL_EXPANSION_BATCH9)
    input_ids = {case["id"] for case in inputs["cases"]}

    assert report["report_type"] == "holdout_input_pool_expansion"
    assert report["dataset"] == "blind-v1"
    assert report["batch"] == "batch9_100_cases"
    assert report["expected_values_included"] is False
    assert report["inputs_included"] is False
    assert report["new_cases_include_only_ids_and_metadata"] is True
    assert "cases" not in report
    assert "inputs" not in report
    assert report["source_inputs_sha256"] == (
        "0ac742ac9885cdae198bed6fc376c2fb5c3e991573ae4cb4ac2072cfef3e937d"
    )
    assert report["source_inputs_sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert report["summary"] == {
        "previous_input_cases": 583,
        "added_input_cases": 100,
        "current_input_cases": 683,
        "target_total": 2000,
        "added_by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "current_by_domain": {
            "formal": 112,
            "high_risk": 76,
            "it": 132,
            "llm": 113,
            "social": 114,
            "ui": 136,
        },
        "added_by_risk": {
            "candidate_gap": 60,
            "baseline_guard": 15,
            "over_conversion_guard": 25,
        },
        "current_by_risk": {
            "baseline_guard": 109,
            "candidate_gap": 386,
            "over_conversion_guard": 188,
        },
        "private_expected_cases_currently_reviewed": 583,
        "new_cases_pending_expected_review": 100,
    }
    assert len(report["new_case_ids"]) == 100
    assert set(report["new_case_ids"]) <= input_ids | load_all_removed_case_ids()
    assert report["new_case_ids"][0] == "blind-it-0188"
    assert report["new_case_ids"][-1] == "blind-high-risk-0080"
    assert report["policy"]["expected_not_generated"] is True
    assert report["policy"]["converter_outputs_not_used"] is True
    assert report["policy"]["private_expected_not_modified"] is True


def test_holdout_batch10_input_pool_expansion_omits_expected_and_input_text() -> None:
    inputs = load_json(INPUTS)
    expected = load_json(EXPECTED)
    report = load_json(INPUT_POOL_EXPANSION_BATCH10)
    input_ids = {case["id"] for case in inputs["cases"]}
    expected_ids = {case["id"] for case in expected["cases"]}

    assert report["report_type"] == "holdout_input_pool_expansion"
    assert report["dataset"] == "blind-v1"
    assert report["batch"] == "batch10_100_cases"
    assert report["expected_values_included"] is False
    assert report["inputs_included"] is False
    assert report["new_cases_include_only_ids_and_metadata"] is True
    assert "cases" not in report
    assert "inputs" not in report
    assert report["source_inputs_sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert report["summary"] == {
        "previous_input_cases": 667,
        "added_input_cases": 100,
        "current_input_cases": 767,
        "target_total": 2000,
        "added_by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "current_by_domain": {
            "formal": 125,
            "high_risk": 86,
            "it": 149,
            "llm": 126,
            "social": 129,
            "ui": 152,
        },
        "added_by_risk": {
            "candidate_gap": 60,
            "baseline_guard": 15,
            "over_conversion_guard": 25,
        },
        "current_by_risk": {
            "baseline_guard": 122,
            "candidate_gap": 432,
            "over_conversion_guard": 213,
        },
        "private_expected_cases_currently_reviewed": 667,
        "new_cases_pending_expected_review": 100,
    }
    assert len(report["new_case_ids"]) == 100
    removed_ids = load_all_removed_case_ids()
    assert set(report["new_case_ids"]) <= input_ids | removed_ids
    assert set(report["new_case_ids"]) <= expected_ids | removed_ids
    assert report["new_case_ids"][0] == "blind-it-0213"
    assert report["new_case_ids"][-1] == "blind-high-risk-0090"
    assert report["policy"]["expected_not_generated"] is True
    assert report["policy"]["converter_outputs_not_used"] is True
    assert report["policy"]["private_expected_not_modified"] is True


def test_holdout_batch11_input_pool_expansion_omits_expected_and_input_text() -> None:
    inputs = load_json(INPUTS)
    expected = load_json(EXPECTED)
    report = load_json(INPUT_POOL_EXPANSION_BATCH11)
    input_ids = {case["id"] for case in inputs["cases"]}
    expected_ids = {case["id"] for case in expected["cases"]}
    batch11_ids = set(report["new_case_ids"])

    assert report["report_type"] == "holdout_input_pool_expansion"
    assert report["dataset"] == "blind-v1"
    assert report["batch"] == "batch11_100_cases"
    assert report["expected_values_included"] is False
    assert report["inputs_included"] is False
    assert report["new_cases_include_only_ids_and_metadata"] is True
    assert "cases" not in report
    assert "inputs" not in report
    assert report["source_inputs_sha256"] == (
        "e7018d35e078a53ff1c59e4a8281b787151fd11c158859ad882defc82b93aff9"
    )
    assert report["source_inputs_sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert report["summary"] == {
        "previous_input_cases": 751,
        "added_input_cases": 100,
        "current_input_cases": 851,
        "target_total": 2000,
        "added_by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "current_by_domain": {
            "formal": 137,
            "high_risk": 96,
            "it": 167,
            "llm": 141,
            "social": 144,
            "ui": 166,
        },
        "added_by_risk": {
            "candidate_gap": 60,
            "baseline_guard": 15,
            "over_conversion_guard": 25,
        },
        "current_by_risk": {
            "baseline_guard": 134,
            "candidate_gap": 479,
            "over_conversion_guard": 238,
        },
        "private_expected_cases_currently_reviewed": 751,
        "new_cases_pending_expected_review": 100,
    }
    assert len(batch11_ids) == 100
    removed_ids = load_all_removed_case_ids()
    assert batch11_ids <= input_ids | removed_ids
    assert batch11_ids <= expected_ids | removed_ids
    assert report["new_case_ids"][0] == "blind-it-0238"
    assert report["new_case_ids"][-1] == "blind-high-risk-0100"
    assert report["policy"]["expected_not_generated"] is True
    assert report["policy"]["converter_outputs_not_used"] is True
    assert report["policy"]["private_expected_not_modified"] is True


def test_holdout_batch12_input_pool_expansion_is_fresh_and_input_only() -> None:
    inputs = load_json(INPUTS)
    expected = load_json(EXPECTED)
    report = load_json(INPUT_POOL_EXPANSION_BATCH12)
    input_ids = {case["id"] for case in inputs["cases"]}
    expected_ids = {case["id"] for case in expected["cases"]}
    batch12_ids = set(report["new_case_ids"])

    assert report["report_type"] == "holdout_input_pool_expansion"
    assert report["batch"] == "batch12_100_cases"
    assert report["expected_values_included"] is False
    assert report["inputs_included"] is False
    assert report["new_cases_include_only_ids_and_metadata"] is True
    assert "cases" not in report
    assert "inputs" not in report
    assert report["source_inputs_sha256"] == (
        "c1082299113239bfe88590425ccd6c4b4b0f0d769ddea18ce457a11050863deb"
    )
    assert report["source_inputs_sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert report["summary"] == {
        "previous_input_cases": 841,
        "added_input_cases": 100,
        "current_input_cases": 941,
        "target_total": 2000,
        "added_by_domain": {
            "formal": 20,
            "high_risk": 20,
            "it": 15,
            "llm": 10,
            "social": 20,
            "ui": 15,
        },
        "current_by_domain": {
            "formal": 153,
            "high_risk": 116,
            "it": 178,
            "llm": 149,
            "social": 164,
            "ui": 181,
        },
        "added_by_risk": {
            "baseline_guard": 16,
            "candidate_gap": 47,
            "over_conversion_guard": 37,
        },
        "current_by_risk": {
            "baseline_guard": 149,
            "candidate_gap": 521,
            "over_conversion_guard": 271,
        },
        "private_expected_cases_currently_reviewed": 841,
        "new_cases_pending_expected_review": 100,
    }
    assert len(batch12_ids) == 100
    batch12_removed_ids = set(load_json(SEALED_POOL_UPDATE_BATCH12_MISS_REVIEW)["removed_case_ids"])
    assert batch12_ids <= input_ids | batch12_removed_ids
    assert batch12_ids <= expected_ids | batch12_removed_ids
    assert batch12_ids & batch12_removed_ids == batch12_removed_ids
    assert report["new_case_ids"][0] == "blind-formal-0154"
    assert report["new_case_ids"][-1] == "blind-llm-0162"
    assert report["policy"]["input_only_before_expected_review"] is True
    assert report["policy"]["converter_outputs_used"] is False
    assert report["policy"]["competitor_outputs_used"] is False
    assert report["policy"]["private_expected_not_modified"] is True


def test_holdout_batch12_advisories_and_confirmation_are_not_ground_truth() -> None:
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH12)
    codex = load_json(CODEX_BATCH12_FIRST_PASS)
    gemini = load_json(GEMINI_BATCH12_ADVISORY)
    diff = load_json(CODEX_GEMINI_BATCH12_DIFF_REVIEW)
    packet = load_json(MAINTAINER_BATCH12_CONFIRMATION)
    batch12_ids = set(expansion["new_case_ids"])

    assert codex["review_stage"] == "first_pass_advisory"
    assert codex["reviewer"] == "codex"
    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "formal": 20,
            "high_risk": 20,
            "it": 15,
            "llm": 10,
            "social": 20,
            "ui": 15,
        },
        "by_risk": {
            "baseline_guard": 16,
            "candidate_gap": 47,
            "over_conversion_guard": 37,
        },
        "by_confidence": {"high": 79, "medium": 21},
        "review_needed": 21,
        "acceptable_variants_proposed": 11,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in codex["cases"]} == batch12_ids

    assert gemini["review_stage"] == "independent_holdout_expected_review"
    assert gemini["model_requested"] == "gemini-2.5-pro"
    assert gemini["model_observed"] == ["gemini-2.5-pro"]
    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["independence_policy"] == {
        "codex_values_seen": False,
        "current_expected_seen": False,
        "zhtw_output_seen": False,
        "competitor_output_seen": False,
        "workspace_files_seen": False,
        "input_only_cases_seen": True,
        "tool_calls": 0,
    }
    assert gemini["summary"]["total_cases"] == 100
    assert gemini["summary"]["quality_flags"] == 1
    assert {case["id"] for case in gemini["cases"]} == batch12_ids

    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["summary"] == {
        "total_cases": 100,
        "exact_matches": 87,
        "differences": 13,
        "exact_but_policy_review": 31,
        "no_immediate_question": 56,
        "maintainer_queue_total": 44,
        "difference_recommendations": {"codex": 7, "gemini": 6},
        "gemini_quality_flags": 1,
        "promotion_allowed": False,
    }
    difference_ids = {case["id"] for case in diff["differences"]}
    policy_ids = {case["id"] for case in diff["exact_but_policy_review"]}
    no_question_ids = {case["id"] for case in diff["no_immediate_question"]}
    assert difference_ids | policy_ids | no_question_ids == batch12_ids
    assert not (difference_ids & policy_ids)
    assert not (difference_ids & no_question_ids)
    assert not (policy_ids & no_question_ids)

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert {case["id"] for case in packet["cases"]} == difference_ids | policy_ids
    assert set(packet["no_immediate_question_case_ids"]) == no_question_ids
    assert packet["policy"]["private_expected_not_modified"] is True


def test_holdout_batch12_final_decision_updates_private_expected() -> None:
    expected = load_json(EXPECTED)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH12)
    packet = load_json(MAINTAINER_BATCH12_CONFIRMATION)
    decision = load_json(MAINTAINER_BATCH12_FINAL_DECISION)
    batch12_ids = set(expansion["new_case_ids"])
    batch12_cases = [case for case in expected["cases"] if case["id"] in batch12_ids]

    assert decision["review_stage"] == "maintainer_final_decision_summary"
    assert decision["scope"] == "batch12_100_cases"
    assert decision["maintainer"] == "tim"
    assert decision["decision"] == "review_ok"
    assert decision["expected_values_included"] is False
    assert decision["acceptable_values_included"] is False
    assert decision["inputs_included"] is False
    assert decision["outputs_included"] is False
    assert "cases" not in decision
    assert decision["private_expected_sha256"] == (
        "617f048425d75605e1997b8952432792f417444b3c4facec89bc5bd7a160dd22"
    )
    assert decision["private_expected_sha256"] != private_expected_sha256()
    assert decision["source_inputs_sha256"] == (
        "c1082299113239bfe88590425ccd6c4b4b0f0d769ddea18ce457a11050863deb"
    )
    assert decision["source_inputs_sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert decision["summary"] == {
        "batch12_cases": 100,
        "total_private_expected_cases": 941,
        "status": "sealed_private",
        "approval_policy": "single_human_with_ai_advisory",
        "minimum_human_reviewers": 1,
        "ai_advisory_review_allowed": True,
        "private_expected_updated": True,
        "accepted_recommended_expected": 44,
        "accepted_exact_no_immediate_question": 56,
        "primary_differences_adjudicated": 13,
        "acceptable_variant_cases": 23,
        "acceptable_variant_values": 32,
        "by_expected_source_for_batch12": {
            "human_adjudication": 13,
            "human_first_pass": 87,
        },
        "by_disagreement_for_batch12": {"false": 87, "true": 13},
        "by_expected_source_total": {
            "human_adjudication": 181,
            "human_first_pass": 760,
        },
        "by_disagreement_total": {"false": 763, "true": 178},
        "by_domain_for_batch12": {
            "formal": 20,
            "high_risk": 20,
            "it": 15,
            "llm": 10,
            "social": 20,
            "ui": 15,
        },
        "by_risk_for_batch12": {
            "baseline_guard": 16,
            "candidate_gap": 47,
            "over_conversion_guard": 37,
        },
    }
    removed_ids = set(load_json(SEALED_POOL_UPDATE_BATCH12_MISS_REVIEW)["removed_case_ids"])
    assert {case["id"] for case in batch12_cases} == batch12_ids - removed_ids
    assert decision["confirmed_case_ids"] == {
        "review_packet": [case["id"] for case in packet["cases"]],
        "no_immediate_question": packet["no_immediate_question_case_ids"],
    }


def test_holdout_batch12_miss_semantic_review_is_advisory_and_sanitized() -> None:
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH12)
    codex = load_json(BATCH12_MISS_CLASSIFICATION)
    gemini = load_json(GEMINI_BATCH12_MISS_SEMANTIC_REVIEW)
    diff = load_json(CODEX_GEMINI_BATCH12_MISS_DIFF)
    packet = load_json(MAINTAINER_BATCH12_MISS_CONFIRMATION)
    partial_decision = load_json(MAINTAINER_BATCH12_MISS_PARTIAL_DECISION)
    batch12_ids = set(expansion["new_case_ids"])
    codex_ids = {case["id"] for case in codex["cases"]}
    gemini_ids = {case["id"] for case in gemini["cases"]}
    difference_ids = {case["id"] for case in diff["differences"]}
    no_question_ids = {case["id"] for case in diff["no_immediate_question"]}
    resolved_ids = {case["id"] for case in diff["maintainer_resolved"]}
    forbidden_fields = {"input", "expected", "acceptable", "output", "zhtw_output"}

    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "acceptable_values_included": False,
        "zhtw_outputs_included": False,
        "classification_metadata_only": True,
    }
    assert codex["summary"] == {
        "total_misses": 15,
        "by_action": {
            "add_zhtw_output_as_acceptable_variant": 7,
            "move_to_public_regression_candidate": 8,
        },
        "by_domain": {
            "formal": 2,
            "high_risk": 3,
            "it": 4,
            "llm": 3,
            "social": 2,
            "ui": 1,
        },
        "by_risk": {
            "baseline_guard": 2,
            "candidate_gap": 8,
            "over_conversion_guard": 5,
        },
        "promotion_allowed": False,
    }
    assert len(codex_ids) == 15
    assert codex_ids <= batch12_ids
    assert all(not (forbidden_fields & set(case)) for case in codex["cases"])

    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["model_observed"] == ["gemini-2.5-pro"]
    assert gemini["independence_policy"] == {
        "codex_classification_seen": False,
        "current_expected_seen": False,
        "zhtw_output_seen": False,
        "competitor_output_seen": False,
        "workspace_files_seen": False,
        "input_only_cases_seen": True,
        "tool_calls": 0,
    }
    assert gemini_ids == codex_ids

    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["summary"] == {
        "total_cases": 15,
        "classification_agreements": 7,
        "classification_differences": 8,
        "recommended_acceptable_variants": 7,
        "recommended_public_regression_candidates": 8,
        "recommended_strict_private_signals": 0,
        "maintainer_queue": 6,
        "no_immediate_question": 7,
        "promotion_allowed": False,
        "maintainer_resolved": 2,
    }
    assert difference_ids | no_question_ids | resolved_ids == codex_ids
    assert not (difference_ids & no_question_ids)
    assert not (difference_ids & resolved_ids)
    assert not (no_question_ids & resolved_ids)
    assert all(not (forbidden_fields & set(case)) for case in diff["differences"])
    assert all(not (forbidden_fields & set(case)) for case in diff["no_immediate_question"])

    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["summary"]["review_cases"] == 6
    assert {case["id"] for case in packet["cases"]} == difference_ids
    assert set(packet["no_immediate_question_case_ids"]) == no_question_ids
    assert set(packet["maintainer_resolved_case_ids"]) == resolved_ids
    assert packet["policy"] == {
        "private_expected_not_modified": True,
        "sealed_pool_not_modified": True,
        "dictionary_not_modified": True,
        "maintainer_confirmation_required": True,
        "codex_and_gemini_are_advisory_only": True,
    }
    assert partial_decision["maintainer"] == "tim"
    assert partial_decision["resolved_case_ids"] == sorted(resolved_ids)
    assert partial_decision["resolved_action"] == "move_to_public_regression_candidate"
    assert partial_decision["remaining_maintainer_queue"] == 6
    assert partial_decision["private_expected_updated"] is False
    assert partial_decision["sealed_pool_updated"] is False
    assert partial_decision["dictionary_updated"] is False


def test_holdout_batch12_miss_final_decision_updates_pool_and_promotion_gate() -> None:
    decision = load_json(MAINTAINER_BATCH12_MISS_FINAL_DECISION)
    pool_update = load_json(SEALED_POOL_UPDATE_BATCH12_MISS_REVIEW)
    gate = load_json(HOLDOUT_PROMOTION_GATE_BATCH12_MISS_REVIEW)
    inputs = load_json(INPUTS)
    expected = load_json(EXPECTED)
    candidates = load_json(HOLDOUT_CANDIDATES)
    regression = load_json(REGRESSION)

    acceptable_ids = set(decision["confirmed_acceptable_variant_case_ids"])
    removed_ids = set(decision["removed_to_public_regression_candidate_case_ids"])
    strict_ids = set(decision["strict_private_holdout_signal_case_ids"])
    input_ids = {case["id"] for case in inputs["cases"]}
    expected_ids = {case["id"] for case in expected["cases"]}

    assert decision["decision"] == "review_ok"
    assert decision["promotion_allowed"] is True
    assert decision["private_expected_updated"] is True
    assert decision["sealed_pool_updated"] is True
    assert decision["dictionary_updated"] is True
    assert len(acceptable_ids) == 4
    assert len(removed_ids) == 11
    assert strict_ids == set()
    assert acceptable_ids <= input_ids
    assert acceptable_ids <= expected_ids
    assert not (removed_ids & input_ids)
    assert not (removed_ids & expected_ids)
    assert decision["source_inputs_sha256_after"] == (
        "9297eaf5688b87b0d89d83dceb04f9ce3fa62944f6cbde83b485bc0524e7f780"
    )
    assert decision["source_inputs_sha256_after"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert decision["private_expected_sha256_after"] == (
        "81246822bffc1423b1460b0bfe7f1ed2539060f31880f8b49424e85c25b6052e"
    )
    assert decision["private_expected_sha256_after"] != private_expected_sha256()
    assert decision["candidate_dataset_sha256_after_promotion"] == (
        "74461c47e7dcc1c1f6296bbc82eeabb4eb13f9dafe821eaefa478776296fc1a7"
    )
    assert decision["regression_sha256_after_promotion"] == (
        "e3313f2dc54c0e0f5d7adfb7688528913f3a3118655457bfa0567f121fb6754c"
    )
    assert (
        decision["candidate_dataset_sha256_after_promotion"]
        != hashlib.sha256(HOLDOUT_CANDIDATES.read_bytes()).hexdigest()
    )
    assert (
        decision["regression_sha256_after_promotion"]
        != hashlib.sha256(REGRESSION.read_bytes()).hexdigest()
    )
    assert decision["summary"] == {
        "reviewed_batch12_misses": 15,
        "confirmed_acceptable_variants": 4,
        "removed_to_public_regression_candidates": 11,
        "strict_private_holdout_signals": 0,
        "remaining_sealed_input_cases": 930,
        "remaining_private_expected_cases": 930,
        "candidate_dataset_total_cases": 197,
        "dictionary_updated": True,
        "promotion_gate_pending": False,
        "promotion_gate_passed": True,
        "promoted_to_regression": 11,
        "full_sentence_mappings_added": 11,
        "identity_mappings_added": 11,
        "regression_total_cases": 1229,
    }
    assert (
        pool_update["removed_case_ids"]
        == decision["removed_to_public_regression_candidate_case_ids"]
    )
    assert pool_update["remaining_inputs_sha256"] == (
        "9297eaf5688b87b0d89d83dceb04f9ce3fa62944f6cbde83b485bc0524e7f780"
    )
    assert pool_update["remaining_inputs_sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert pool_update["remaining_expected_sha256"] == (
        "81246822bffc1423b1460b0bfe7f1ed2539060f31880f8b49424e85c25b6052e"
    )
    assert pool_update["remaining_expected_sha256"] != private_expected_sha256()
    assert gate["promoted_case_ids"] == pool_update["removed_case_ids"]
    assert gate["source_candidates_sha256"] == (
        "74461c47e7dcc1c1f6296bbc82eeabb4eb13f9dafe821eaefa478776296fc1a7"
    )
    assert gate["regression_sha256"] == (
        "e3313f2dc54c0e0f5d7adfb7688528913f3a3118655457bfa0567f121fb6754c"
    )
    assert candidates["stats"]["total_cases"] == 219
    assert regression["stats"]["by_classification"]["holdout_regression_promoted"] == 219
    for report in (decision, pool_update, gate):
        assert report["expected_values_included"] is False
        assert report["inputs_included"] is False
        assert "cases" not in report


def test_holdout_batch13_review_and_first_benchmark_are_auditable() -> None:
    inputs = load_json(INPUTS)
    expected = load_json(EXPECTED)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH13)
    codex = load_json(CODEX_BATCH13_FIRST_PASS)
    gemini = load_json(GEMINI_BATCH13_ADVISORY)
    diff = load_json(CODEX_GEMINI_BATCH13_DIFF_REVIEW)
    packet = load_json(MAINTAINER_BATCH13_CONFIRMATION)
    final = load_json(MAINTAINER_BATCH13_FINAL_DECISION)
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH13)

    batch13_ids = set(expansion["new_case_ids"])
    input_ids = {case["id"] for case in inputs["cases"]}
    expected_ids = {case["id"] for case in expected["cases"]}
    removed_ids = set(load_json(SEALED_POOL_UPDATE_BATCH13_MISS_REVIEW)["removed_case_ids"])

    assert expansion["batch"] == "batch13_100_cases"
    assert expansion["source_inputs_sha256"] == final["source_inputs_sha256"]
    assert expansion["expected_values_included"] is False
    assert expansion["inputs_included"] is False
    assert "cases" not in expansion
    assert expansion["summary"] == {
        "previous_input_cases": 930,
        "added_input_cases": 100,
        "current_input_cases": 1030,
        "target_total": 2000,
        "added_by_domain": {
            "formal": 15,
            "high_risk": 15,
            "it": 20,
            "llm": 15,
            "social": 20,
            "ui": 15,
        },
        "current_by_domain": {
            "formal": 166,
            "high_risk": 130,
            "it": 195,
            "llm": 162,
            "social": 182,
            "ui": 195,
        },
        "added_by_risk": {
            "baseline_guard": 18,
            "candidate_gap": 64,
            "over_conversion_guard": 18,
        },
        "current_by_risk": {
            "baseline_guard": 165,
            "candidate_gap": 581,
            "over_conversion_guard": 284,
        },
        "private_expected_cases_currently_reviewed": 930,
        "new_cases_pending_expected_review": 100,
    }
    assert len(batch13_ids) == 100
    assert batch13_ids <= input_ids | removed_ids
    assert batch13_ids <= expected_ids | removed_ids
    assert len(expected_ids) == 1008

    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["summary"]["by_confidence"] == {"high": 78, "medium": 22}
    assert codex["summary"]["review_needed"] == 22
    assert {case["id"] for case in codex["cases"]} == batch13_ids

    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["model_requested"] == "gemini-2.5-pro"
    assert gemini["model_observed"] == ["gemini-2.5-pro"]
    assert gemini["quality_flags"] == []
    assert gemini["independence_policy"] == {
        "codex_values_seen": False,
        "current_expected_seen": False,
        "zhtw_output_seen": False,
        "competitor_output_seen": False,
        "workspace_files_seen": False,
        "input_only_cases_seen": True,
        "tool_calls": 0,
    }
    assert {case["id"] for case in gemini["cases"]} == batch13_ids
    for raw_path in gemini["raw_reports"]:
        raw = load_json(ROOT / raw_path)
        assert raw["stats"]["tools"]["totalCalls"] == 0
        assert raw["stats"]["files"] == {"totalLinesAdded": 0, "totalLinesRemoved": 0}

    assert diff["summary"] == {
        "total_cases": 100,
        "exact_matches": 66,
        "differences": 34,
        "exact_but_policy_review": 19,
        "no_immediate_question": 47,
        "maintainer_queue_total": 53,
        "difference_recommendations": {"codex": 29, "gemini": 5},
        "gemini_quality_flags": 0,
        "promotion_allowed": False,
    }
    difference_ids = {case["id"] for case in diff["differences"]}
    policy_ids = {case["id"] for case in diff["exact_but_policy_review"]}
    no_question_ids = {case["id"] for case in diff["no_immediate_question"]}
    assert difference_ids | policy_ids | no_question_ids == batch13_ids
    assert not (difference_ids & policy_ids)
    assert not (difference_ids & no_question_ids)
    assert not (policy_ids & no_question_ids)

    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["summary"] == {
        "review_cases": 53,
        "difference_cases": 34,
        "exact_policy_review_cases": 19,
        "no_immediate_question_cases": 47,
    }
    assert {case["id"] for case in packet["cases"]} == difference_ids | policy_ids
    assert set(packet["no_immediate_question_case_ids"]) == no_question_ids
    assert packet["policy"]["private_expected_not_modified"] is True
    assert all(case["maintainer_decision"] is None for case in packet["cases"])

    assert final["decision"] == "review_ok"
    assert final["private_expected_updated"] is True
    assert final["source_inputs_sha256"] == expansion["source_inputs_sha256"]
    assert final["private_expected_sha256"] == sanity["expected"]["sha256"]
    assert set(final["confirmed_case_ids"]) == batch13_ids
    assert final["summary"]["human_adjudication"] == 35
    assert final["summary"]["human_first_pass"] == 65
    assert final["summary"]["benchmark_pending"] is False
    assert final["summary"]["batch13_accepted"] == 66
    assert final["summary"]["batch13_misses"] == 34

    assert sanity["review_stage"] == "after_batch13_final_decision"
    assert sanity["inputs"]["sha256"] == final["source_inputs_sha256"]
    assert sanity["expected"]["sha256"] == final["private_expected_sha256"]
    assert sanity["interpretation_policy"] == {
        "fresh_batch_before_tuning": True,
        "batch13_capability_claim_allowed": True,
        "approval_policy": "single_human_with_ai_advisory",
        "market_best_claim_allowed": False,
    }
    assert sanity["summary"]["case_count"] == 1030
    assert sanity["summary"]["accepted"] == 950
    assert sanity["summary"]["misses"] == 80
    assert sanity["summary"]["accepted_accuracy"] == 0.9223300970873787
    assert sanity["batch13_summary"] == {
        "case_count": 100,
        "accepted": 66,
        "misses": 34,
        "primary_exact": 57,
        "acceptable_exact": 9,
        "idempotent": 100,
        "accepted_accuracy": 0.66,
        "by_domain": {
            "formal": {"total": 15, "accepted": 13, "misses": 2},
            "high_risk": {"total": 15, "accepted": 10, "misses": 5},
            "it": {"total": 20, "accepted": 10, "misses": 10},
            "llm": {"total": 15, "accepted": 9, "misses": 6},
            "social": {"total": 20, "accepted": 17, "misses": 3},
            "ui": {"total": 15, "accepted": 7, "misses": 8},
        },
        "misses_by_risk": {
            "baseline_guard": 4,
            "candidate_gap": 28,
            "over_conversion_guard": 2,
        },
    }
    for key in (
        "expected_values_included",
        "acceptable_values_included",
        "rows_included",
        "inputs_included",
        "outputs_included",
        "benchmark_rows_included",
    ):
        assert sanity[key] is False
    assert "rows" not in sanity


def test_holdout_batch13_miss_review_is_independent_and_sanitized() -> None:
    codex = load_json(BATCH13_MISS_CLASSIFICATION)
    gemini = load_json(GEMINI_BATCH13_MISS_SEMANTIC_REVIEW)
    diff = load_json(CODEX_GEMINI_BATCH13_MISS_DIFF)
    packet = load_json(MAINTAINER_BATCH13_MISS_CONFIRMATION)
    raw = load_json(ROOT / gemini["source_raw"])
    forbidden_fields = {"input", "expected", "acceptable", "output", "zhtw_output"}

    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["summary"] == {
        "total_misses": 34,
        "by_action": {
            "add_zhtw_output_as_acceptable_variant": 5,
            "keep_strict_private_signal": 9,
            "move_to_public_regression_candidate": 20,
        },
        "by_domain": {
            "formal": 2,
            "high_risk": 5,
            "it": 10,
            "llm": 6,
            "social": 3,
            "ui": 8,
        },
        "by_risk": {
            "baseline_guard": 4,
            "candidate_gap": 28,
            "over_conversion_guard": 2,
        },
        "by_confidence": {"high": 20, "medium": 14},
        "promotion_allowed": False,
    }
    assert all(not (forbidden_fields & set(case)) for case in codex["cases"])

    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["model_observed"] == ["gemini-2.5-pro"]
    assert gemini["independence_policy"] == {
        "codex_classification_seen": False,
        "current_expected_seen": False,
        "zhtw_output_seen": False,
        "competitor_output_seen": False,
        "workspace_files_seen": False,
        "input_only_cases_seen": True,
        "tool_calls": 0,
    }
    assert gemini["summary"] == {
        "total_cases": 34,
        "by_action": {
            "add_zhtw_output_as_acceptable_variant": 3,
            "keep_strict_private_signal": 3,
            "move_to_public_regression_candidate": 28,
        },
        "by_confidence": {"high": 34},
        "review_needed": 0,
        "promotion_allowed": False,
    }
    assert all(not (forbidden_fields & set(case)) for case in gemini["cases"])
    assert raw["stats"]["tools"]["totalCalls"] == 0
    assert raw["stats"]["files"] == {"totalLinesAdded": 0, "totalLinesRemoved": 0}

    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["summary"] == {
        "total_cases": 34,
        "classification_agreements": 19,
        "classification_differences": 15,
        "recommended_by_action": {
            "add_zhtw_output_as_acceptable_variant": 5,
            "keep_strict_private_signal": 7,
            "move_to_public_regression_candidate": 22,
        },
        "maintainer_queue": 19,
        "no_immediate_question": 15,
        "promotion_allowed": False,
    }
    difference_ids = {case["id"] for case in diff["differences"]}
    agreement_ids = {case["id"] for case in diff["agreements"]}
    queue_ids = set(diff["maintainer_queue_case_ids"])
    no_question_ids = set(diff["no_immediate_question_case_ids"])
    assert len(difference_ids) == 15
    assert len(agreement_ids) == 19
    assert len(queue_ids) == 19
    assert len(no_question_ids) == 15
    assert difference_ids | agreement_ids == queue_ids | no_question_ids
    assert not (difference_ids & agreement_ids)
    assert not (queue_ids & no_question_ids)
    assert all(not (forbidden_fields & set(case)) for case in diff["differences"])

    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["summary"] == {
        "review_cases": 19,
        "classification_difference_cases": 15,
        "high_risk_or_medium_agreement_cases": 4,
        "no_immediate_question_cases": 15,
    }
    assert {case["id"] for case in packet["cases"]} == queue_ids
    assert set(packet["no_immediate_question_case_ids"]) == no_question_ids
    assert all(not (forbidden_fields & set(case)) for case in packet["cases"])
    assert all(case["maintainer_decision"] is None for case in packet["cases"])
    assert packet["policy"] == {
        "private_expected_not_modified": True,
        "sealed_pool_not_modified": True,
        "dictionary_not_modified": True,
        "maintainer_confirmation_required": True,
        "codex_and_gemini_are_advisory_only": True,
    }


def test_holdout_batch4_advisory_reports_are_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH4)
    codex = load_json(CODEX_BATCH4_FIRST_PASS)
    gemini = load_json(GEMINI_BATCH4_ADVISORY)
    diff = load_json(CODEX_GEMINI_BATCH4_DIFF_REVIEW)
    packet = load_json(MAINTAINER_BATCH4_CONFIRMATION)

    input_ids = {case["id"] for case in inputs["cases"]}
    batch4_ids = set(expansion["new_case_ids"])

    assert batch4_ids <= input_ids | load_all_removed_case_ids()
    assert codex["review_stage"] == "first_pass_advisory"
    assert codex["reviewer"] == "codex"
    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "by_confidence": {"high": 75, "medium": 25},
        "review_needed": 53,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in codex["cases"]} == batch4_ids
    assert all(case["codex_expected"] for case in codex["cases"])
    assert not any(case["promotion_allowed"] for case in codex["cases"])

    assert gemini["review_stage"] == "independent_holdout_expected_review"
    assert gemini["reviewer"] == "gemini_vertex"
    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["summary"] == {
        "total_cases": 100,
        "exact_matches_with_codex": 74,
        "differences_from_codex": 26,
        "needs_maintainer_review": 64,
        "by_domain": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "by_gemini_confidence": {"high": 100},
        "promotion_allowed": False,
    }
    assert len(gemini["postprocess"]["issue_tags_repaired_from_case_metadata"]) == 17
    assert {case["id"] for case in gemini["review"]["cases"]} == batch4_ids
    assert {row["id"] for row in gemini["comparisons"]} == batch4_ids

    assert diff["review_stage"] == "codex_gemini_difference_review"
    assert diff["scope"] == "batch4_100_cases"
    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["summary"] == {
        "total_cases": 100,
        "exact_matches": 74,
        "differences": 26,
        "exact_but_policy_review": 38,
        "no_immediate_question": 36,
        "maintainer_queue_total": 64,
        "difference_recommendations": {
            "codex": 21,
            "gemini": 4,
            "third_value": 1,
        },
        "promotion_allowed": False,
    }
    assert len(diff["differences"]) == 26
    assert len(diff["exact_but_policy_review"]) == 38
    assert len(diff["no_immediate_question"]) == 36
    assert (
        {case["id"] for case in diff["differences"]}
        | {case["id"] for case in diff["exact_but_policy_review"]}
        | {case["id"] for case in diff["no_immediate_question"]}
    ) == batch4_ids

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch4_100_cases"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["summary"] == {
        "total_review_cases": 64,
        "difference_cases": 26,
        "policy_review_cases": 38,
        "no_immediate_question": 36,
        "difference_recommendations": {
            "codex": 21,
            "gemini": 4,
            "third_value": 1,
        },
        "by_domain": {
            "formal": 8,
            "high_risk": 10,
            "it": 19,
            "llm": 7,
            "social": 9,
            "ui": 11,
        },
        "by_risk": {
            "baseline_guard": 6,
            "candidate_gap": 33,
            "over_conversion_guard": 25,
        },
        "by_policy_reason": {
            "Codex confidence medium": 11,
            "Codex confidence medium, over-conversion guard": 1,
            "high-risk domain": 4,
            "high-risk domain, over-conversion guard": 3,
            "over-conversion guard": 19,
        },
        "promotion_allowed": False,
    }
    assert len(packet["cases"]) == 64
    assert len(packet["no_immediate_question_case_ids"]) == 36
    assert {case["kind"] for case in packet["cases"]} == {
        "difference",
        "exact_but_policy_review",
    }
    assert all(case["recommended_expected"] for case in packet["cases"])


def test_holdout_batch5_advisory_reports_are_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH5)
    codex = load_json(CODEX_BATCH5_FIRST_PASS)
    gemini = load_json(GEMINI_BATCH5_ADVISORY)
    diff = load_json(CODEX_GEMINI_BATCH5_DIFF_REVIEW)
    packet = load_json(MAINTAINER_BATCH5_CONFIRMATION)

    input_ids = {case["id"] for case in inputs["cases"]}
    batch5_ids = set(expansion["new_case_ids"])

    assert batch5_ids <= input_ids | load_all_removed_case_ids()
    assert codex["review_stage"] == "first_pass_advisory"
    assert codex["reviewer"] == "codex"
    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "by_risk": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
        "by_confidence": {"high": 80, "medium": 20},
        "review_needed": 46,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in codex["cases"]} == batch5_ids
    assert all(case["codex_expected"] for case in codex["cases"])
    assert not any(case["promotion_allowed"] for case in codex["cases"])

    assert gemini["review_stage"] == "independent_holdout_expected_review"
    assert gemini["reviewer"] == "gemini_cli"
    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["model_requested"] == "gemini-2.5-flash"
    assert gemini["chunking"] == {
        "strategy": "by_domain",
        "domain_order": ["it", "ui", "llm", "formal", "social", "high_risk"],
    }
    assert gemini["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "by_risk": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
        "by_confidence": {"high": 95, "medium": 5},
        "review_needed": 39,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in gemini["cases"]} == batch5_ids
    assert all(case["gemini_expected"] for case in gemini["cases"])
    assert not any(case["promotion_allowed"] for case in gemini["cases"])

    assert diff["review_stage"] == "codex_gemini_difference_review"
    assert diff["scope"] == "batch5_100_cases"
    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["summary"] == {
        "total_cases": 100,
        "exact_matches": 92,
        "differences": 8,
        "exact_but_policy_review": 42,
        "no_immediate_question": 50,
        "maintainer_queue_total": 50,
        "difference_recommendations": {
            "codex": 5,
            "gemini": 3,
        },
        "zhtw_current_status_for_differences": {
            "in_recommended_acceptable": 5,
            "matches_recommended": 1,
            "needs_followup_if_confirmed": 2,
        },
        "promotion_allowed": False,
    }
    difference_ids = {case["id"] for case in diff["differences"]}
    policy_ids = {case["id"] for case in diff["exact_but_policy_review"]}
    no_question_ids = {case["id"] for case in diff["no_immediate_question"]}
    assert difference_ids == {
        "blind-high-risk-0031",
        "blind-it-0094",
        "blind-llm-0055",
        "blind-social-0052",
        "blind-ui-0068",
        "blind-ui-0069",
        "blind-ui-0074",
        "blind-ui-0077",
    }
    assert difference_ids | policy_ids | no_question_ids == batch5_ids
    assert not (difference_ids & policy_ids)
    assert not (difference_ids & no_question_ids)
    assert not (policy_ids & no_question_ids)
    assert all("zhtw_current" in case for case in diff["differences"])

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch5_100_cases"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["source_diff_review"] == (
        "docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch5-100-cases-2026-07-09.json"
    )
    assert packet["summary"] == {
        "total_review_cases": 50,
        "difference_cases": 8,
        "policy_review_cases": 42,
        "no_immediate_question": 50,
        "difference_recommendations": {
            "codex": 5,
            "gemini": 3,
        },
        "by_domain": {
            "formal": 6,
            "high_risk": 10,
            "it": 9,
            "llm": 7,
            "social": 7,
            "ui": 11,
        },
        "by_risk": {
            "baseline_guard": 2,
            "candidate_gap": 23,
            "over_conversion_guard": 25,
        },
        "by_policy_reason": {
            "Codex confidence medium": 16,
            "Gemini confidence medium": 4,
            "high-risk domain": 9,
            "over-conversion guard": 25,
        },
        "zhtw_current_status_for_differences": {
            "in_recommended_acceptable": 5,
            "matches_recommended": 1,
            "needs_followup_if_confirmed": 2,
        },
        "promotion_allowed": False,
    }
    assert len(packet["cases"]) == 50
    assert len(packet["no_immediate_question_case_ids"]) == 50
    assert {case["kind"] for case in packet["cases"]} == {
        "difference",
        "exact_but_policy_review",
    }
    assert {case["id"] for case in packet["cases"]} == difference_ids | policy_ids
    assert all(case["recommended_expected"] for case in packet["cases"])
    assert all("zhtw_current" in case for case in packet["cases"])


def test_holdout_batch6_codex_first_pass_is_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH6)
    codex = load_json(CODEX_BATCH6_FIRST_PASS)

    input_ids = {case["id"] for case in inputs["cases"]}
    batch6_ids = set(expansion["new_case_ids"])

    assert batch6_ids <= input_ids | load_all_removed_case_ids()
    assert batch6_ids & load_all_removed_case_ids() == set(
        load_json(SEALED_POOL_UPDATE_BATCH6_MISS_REVIEW)["removed_case_ids"]
    )
    assert codex["review_stage"] == "first_pass_advisory"
    assert codex["reviewer"] == "codex"
    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["source_expansion_report"] == (
        "docs/reports/holdout-input-pool-expansion-blind-v1-batch6-100-cases-2026-07-09.json"
    )
    assert codex["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 60,
            "over_conversion_guard": 25,
            "baseline_guard": 15,
        },
        "by_confidence": {"high": 80, "medium": 20},
        "review_needed": 50,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in codex["cases"]} == batch6_ids
    assert all(case["codex_expected"] for case in codex["cases"])
    assert not any(case["promotion_allowed"] for case in codex["cases"])
    assert sum(1 for case in codex["cases"] if case["review_needed"]) == 50
    assert all(
        case["review_needed"]
        for case in codex["cases"]
        if case["risk"] == "over_conversion_guard"
        or case["domain"] == "high_risk"
        or case["confidence"] == "medium"
    )
    assert not any(
        case["review_needed"]
        for case in codex["cases"]
        if case["risk"] != "over_conversion_guard"
        and case["domain"] != "high_risk"
        and case["confidence"] == "high"
    )


def test_holdout_batch7_codex_first_pass_is_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH7)
    codex = load_json(CODEX_BATCH7_FIRST_PASS)

    input_ids = {case["id"] for case in inputs["cases"]}
    batch7_ids = set(expansion["new_case_ids"])

    assert batch7_ids <= input_ids | load_all_removed_case_ids()
    assert codex["review_stage"] == "first_pass_advisory"
    assert codex["reviewer"] == "codex"
    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["source_expansion_report"] == (
        "docs/reports/holdout-input-pool-expansion-blind-v1-batch7-100-cases-2026-07-10.json"
    )
    assert codex["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 60,
            "baseline_guard": 15,
            "over_conversion_guard": 25,
        },
        "by_confidence": {"medium": 20, "high": 80},
        "review_needed": 50,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in codex["cases"]} == batch7_ids
    assert all(case["codex_expected"] for case in codex["cases"])
    assert not any(case["promotion_allowed"] for case in codex["cases"])
    assert sum(1 for case in codex["cases"] if case["review_needed"]) == 50
    assert all(
        case["review_needed"]
        for case in codex["cases"]
        if case["risk"] == "over_conversion_guard"
        or case["domain"] == "high_risk"
        or case["confidence"] == "medium"
    )
    assert not any(
        case["review_needed"]
        for case in codex["cases"]
        if case["risk"] != "over_conversion_guard"
        and case["domain"] != "high_risk"
        and case["confidence"] == "high"
    )


def test_holdout_batch8_codex_first_pass_is_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH8)
    codex = load_json(CODEX_BATCH8_FIRST_PASS)

    input_ids = {case["id"] for case in inputs["cases"]}
    batch8_ids = set(expansion["new_case_ids"])

    assert batch8_ids <= input_ids | load_all_removed_case_ids()
    assert codex["review_stage"] == "first_pass_advisory"
    assert codex["reviewer"] == "codex"
    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["source_expansion_report"] == (
        "docs/reports/holdout-input-pool-expansion-blind-v1-batch8-100-cases-2026-07-10.json"
    )
    assert codex["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 60,
            "baseline_guard": 15,
            "over_conversion_guard": 25,
        },
        "by_confidence": {"medium": 20, "high": 80},
        "review_needed": 50,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in codex["cases"]} == batch8_ids
    assert all(case["codex_expected"] for case in codex["cases"])
    assert not any(case["promotion_allowed"] for case in codex["cases"])
    assert sum(1 for case in codex["cases"] if case["review_needed"]) == 50
    assert all(
        case["review_needed"]
        for case in codex["cases"]
        if case["risk"] == "over_conversion_guard"
        or case["domain"] == "high_risk"
        or case["confidence"] == "medium"
    )
    assert not any(
        case["review_needed"]
        for case in codex["cases"]
        if case["risk"] != "over_conversion_guard"
        and case["domain"] != "high_risk"
        and case["confidence"] == "high"
    )


def test_holdout_batch6_gemini_cli_advisory_is_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH6)
    gemini = load_json(GEMINI_BATCH6_ADVISORY)

    input_ids = {case["id"] for case in inputs["cases"]}
    batch6_ids = set(expansion["new_case_ids"])

    assert batch6_ids <= input_ids | load_all_removed_case_ids()
    assert batch6_ids & load_all_removed_case_ids() == set(
        load_json(SEALED_POOL_UPDATE_BATCH6_MISS_REVIEW)["removed_case_ids"]
    )
    assert gemini["review_stage"] == "independent_holdout_expected_review"
    assert gemini["reviewer"] == "gemini_cli"
    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["model_requested"] == "gemini-2.5-flash"
    assert gemini["chunking"] == {
        "strategy": "by_domain",
        "domain_order": ["it", "ui", "llm", "formal", "social", "high_risk"],
    }
    assert gemini["source_expansion_report"] == (
        "docs/reports/holdout-input-pool-expansion-blind-v1-batch6-100-cases-2026-07-09.json"
    )
    assert "GEMINI_API_KEY" in gemini["policy"]
    assert gemini["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 60,
            "over_conversion_guard": 25,
            "baseline_guard": 15,
        },
        "by_confidence": {"high": 100},
        "review_needed": 70,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in gemini["cases"]} == batch6_ids
    assert all(case["gemini_expected"] for case in gemini["cases"])
    assert not any(case["promotion_allowed"] for case in gemini["cases"])
    assert sum(1 for case in gemini["cases"] if case["review_needed"]) == 70
    assert all(
        case["review_needed"]
        for case in gemini["cases"]
        if case["risk"] == "over_conversion_guard"
        or case["domain"] == "high_risk"
        or case["confidence"] in {"medium", "low"}
    )


def test_holdout_batch6_diff_review_and_confirmation_are_not_ground_truth() -> None:
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH6)
    diff = load_json(CODEX_GEMINI_BATCH6_DIFF_REVIEW)
    packet = load_json(MAINTAINER_BATCH6_CONFIRMATION)

    batch6_ids = set(expansion["new_case_ids"])

    assert diff["review_stage"] == "codex_gemini_difference_review"
    assert diff["scope"] == "batch6_100_cases"
    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["source_codex_report"] == (
        "docs/reports/holdout-codex-first-pass-blind-v1-batch6-100-cases-2026-07-10.json"
    )
    assert diff["source_gemini_report"] == (
        "docs/reports/holdout-gemini-cli-advisory-blind-v1-batch6-100-cases-2026-07-10.json"
    )
    assert diff["summary"] == {
        "total_cases": 100,
        "exact_matches": 80,
        "differences": 20,
        "exact_but_policy_review": 56,
        "no_immediate_question": 24,
        "maintainer_queue_total": 76,
        "difference_recommendations": {
            "codex": 13,
            "gemini": 4,
            "third": 3,
        },
        "zhtw_current_status_for_differences": {
            "needs_followup_if_confirmed": 9,
            "in_recommended_acceptable": 8,
            "matches_recommended": 3,
        },
        "promotion_allowed": False,
    }
    difference_ids = {case["id"] for case in diff["differences"]}
    policy_ids = {case["id"] for case in diff["exact_but_policy_review"]}
    no_question_ids = {case["id"] for case in diff["no_immediate_question"]}
    assert difference_ids == {
        "blind-it-0113",
        "blind-it-0115",
        "blind-it-0117",
        "blind-it-0123",
        "blind-it-0124",
        "blind-it-0130",
        "blind-it-0133",
        "blind-it-0136",
        "blind-ui-0089",
        "blind-ui-0090",
        "blind-ui-0091",
        "blind-ui-0094",
        "blind-ui-0096",
        "blind-ui-0097",
        "blind-ui-0102",
        "blind-ui-0106",
        "blind-ui-0107",
        "blind-llm-0069",
        "blind-llm-0070",
        "blind-formal-0065",
    }
    assert difference_ids | policy_ids | no_question_ids == batch6_ids
    assert len(policy_ids) == 56
    assert len(no_question_ids) == 24
    assert all(case["recommended_expected"] for case in diff["differences"])
    assert all("zhtw_current" in case for case in diff["differences"])

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch6_100_cases"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["source_diff_review"] == (
        "docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch6-100-cases-2026-07-10.json"
    )
    assert packet["summary"] == {
        "total_review_cases": 76,
        "difference_cases": 20,
        "policy_review_cases": 56,
        "no_immediate_question": 24,
        "difference_recommendations": {
            "codex": 13,
            "gemini": 4,
            "third": 3,
        },
        "by_domain": {
            "it": 17,
            "ui": 18,
            "llm": 12,
            "formal": 12,
            "social": 7,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 45,
            "over_conversion_guard": 25,
            "baseline_guard": 6,
        },
        "by_policy_reason": {
            "Codex confidence medium": 20,
            "Gemini review-needed variant": 37,
            "over-conversion guard": 25,
            "high-risk domain": 10,
        },
        "zhtw_current_status_for_differences": {
            "needs_followup_if_confirmed": 9,
            "in_recommended_acceptable": 8,
            "matches_recommended": 3,
        },
        "promotion_allowed": False,
    }
    assert len(packet["cases"]) == 76
    assert len(packet["no_immediate_question_case_ids"]) == 24
    assert {case["kind"] for case in packet["cases"]} == {
        "difference",
        "exact_but_policy_review",
    }
    assert {case["id"] for case in packet["cases"]} == difference_ids | policy_ids
    assert set(packet["no_immediate_question_case_ids"]) == no_question_ids
    assert all(case["recommended_expected"] for case in packet["cases"])
    assert all("zhtw_current" in case for case in packet["cases"])


def test_holdout_batch7_gemini_cli_advisory_is_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH7)
    gemini = load_json(GEMINI_BATCH7_ADVISORY)

    input_ids = {case["id"] for case in inputs["cases"]}
    batch7_ids = set(expansion["new_case_ids"])

    assert batch7_ids <= input_ids | load_all_removed_case_ids()
    assert gemini["review_stage"] == "independent_holdout_expected_review"
    assert gemini["reviewer"] == "gemini_cli"
    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["model_requested"] == "gemini-2.5-flash"
    assert gemini["chunking"] == {
        "strategy": "by_domain",
        "domain_order": ["it", "ui", "llm", "formal", "social", "high_risk"],
    }
    assert gemini["source_expansion_report"] == (
        "docs/reports/holdout-input-pool-expansion-blind-v1-batch7-100-cases-2026-07-10.json"
    )
    assert "GEMINI_API_KEY" in gemini["policy"]
    assert gemini["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 60,
            "baseline_guard": 15,
            "over_conversion_guard": 25,
        },
        "by_confidence": {"high": 100},
        "review_needed": 32,
        "promotion_allowed": False,
    }
    assert gemini["postprocess"] == {
        "malformed_acceptable_removed": [
            {
                "id": "blind-social-0080",
                "removed_acceptable": "禮這家店的排隊系統會傳送簡訊提醒。",
            }
        ]
    }
    assert {case["id"] for case in gemini["cases"]} == batch7_ids
    assert all(case["gemini_expected"] for case in gemini["cases"])
    assert not any(case["promotion_allowed"] for case in gemini["cases"])
    assert sum(1 for case in gemini["cases"] if case["review_needed"]) == 32
    assert all(
        case["review_needed"]
        for case in gemini["cases"]
        if case["risk"] == "over_conversion_guard"
        or case["domain"] == "high_risk"
        or case["confidence"] in {"medium", "low"}
    )


def test_holdout_batch8_gemini_cli_advisory_is_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH8)
    gemini = load_json(GEMINI_BATCH8_ADVISORY)

    input_ids = {case["id"] for case in inputs["cases"]}
    batch8_ids = set(expansion["new_case_ids"])

    assert batch8_ids <= input_ids | load_all_removed_case_ids()
    assert gemini["review_stage"] == "independent_holdout_expected_review"
    assert gemini["reviewer"] == "gemini_cli"
    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["model_requested"] == "gemini-2.5-flash"
    assert gemini["model_observed"] == ["gemini-3.5-flash"]
    assert gemini["chunking"] == {
        "strategy": "single_batch",
        "domain_order": ["it", "ui", "llm", "formal", "social", "high_risk"],
    }
    assert gemini["source_expansion_report"] == (
        "docs/reports/holdout-input-pool-expansion-blind-v1-batch8-100-cases-2026-07-10.json"
    )
    assert "GEMINI_API_KEY" in gemini["policy"]
    assert gemini["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 60,
            "baseline_guard": 15,
            "over_conversion_guard": 25,
        },
        "by_confidence": {"high": 100},
        "review_needed": 0,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in gemini["cases"]} == batch8_ids
    assert all(case["gemini_expected"] for case in gemini["cases"])
    assert not any(case["promotion_allowed"] for case in gemini["cases"])


def test_holdout_batch7_diff_review_and_confirmation_are_not_ground_truth() -> None:
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH7)
    diff = load_json(CODEX_GEMINI_BATCH7_DIFF_REVIEW)
    packet = load_json(MAINTAINER_BATCH7_CONFIRMATION)

    batch7_ids = set(expansion["new_case_ids"])

    assert diff["review_stage"] == "codex_gemini_difference_review"
    assert diff["scope"] == "batch7_100_cases"
    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["source_codex_report"] == (
        "docs/reports/holdout-codex-first-pass-blind-v1-batch7-100-cases-2026-07-10.json"
    )
    assert diff["source_gemini_report"] == (
        "docs/reports/holdout-gemini-cli-advisory-blind-v1-batch7-100-cases-2026-07-10.json"
    )
    assert diff["summary"] == {
        "total_cases": 100,
        "exact_matches": 72,
        "differences": 28,
        "exact_but_policy_review": 37,
        "no_immediate_question": 35,
        "maintainer_queue_total": 65,
        "difference_recommendations": {
            "codex": 19,
            "gemini": 6,
            "third": 3,
        },
        "zhtw_current_status_for_differences": {
            "in_recommended_acceptable": 5,
            "matches_recommended": 8,
            "needs_followup_if_confirmed": 15,
        },
        "promotion_allowed": False,
    }
    difference_ids = {case["id"] for case in diff["differences"]}
    policy_ids = {case["id"] for case in diff["exact_but_policy_review"]}
    no_question_ids = {case["id"] for case in diff["no_immediate_question"]}
    assert difference_ids == {
        "blind-it-0139",
        "blind-it-0141",
        "blind-it-0142",
        "blind-it-0143",
        "blind-it-0145",
        "blind-it-0146",
        "blind-it-0147",
        "blind-it-0149",
        "blind-it-0150",
        "blind-it-0151",
        "blind-it-0152",
        "blind-it-0153",
        "blind-it-0154",
        "blind-it-0155",
        "blind-it-0156",
        "blind-it-0157",
        "blind-ui-0108",
        "blind-ui-0111",
        "blind-ui-0117",
        "blind-ui-0118",
        "blind-ui-0124",
        "blind-llm-0080",
        "blind-llm-0084",
        "blind-llm-0085",
        "blind-llm-0087",
        "blind-social-0080",
        "blind-high-risk-0053",
        "blind-high-risk-0057",
    }
    assert difference_ids | policy_ids | no_question_ids == batch7_ids
    assert len(policy_ids) == 37
    assert len(no_question_ids) == 35
    assert all(case["recommended_expected"] for case in diff["differences"])
    assert all("zhtw_current" in case for case in diff["differences"])

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch7_100_cases"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["source_diff_review"] == (
        "docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch7-100-cases-2026-07-10.json"
    )
    assert packet["summary"] == {
        "total_review_cases": 65,
        "difference_cases": 28,
        "policy_review_cases": 37,
        "no_immediate_question": 35,
        "difference_recommendations": {
            "codex": 19,
            "gemini": 6,
            "third": 3,
        },
        "by_domain": {
            "it": 19,
            "ui": 10,
            "llm": 10,
            "social": 9,
            "high_risk": 10,
            "formal": 7,
        },
        "by_risk": {
            "candidate_gap": 36,
            "baseline_guard": 4,
            "over_conversion_guard": 25,
        },
        "by_policy_reason": {
            "high-risk domain": 10,
            "over-conversion guard": 25,
            "Codex confidence medium": 20,
            "Gemini review-needed policy guard": 32,
        },
        "zhtw_current_status_for_differences": {
            "in_recommended_acceptable": 5,
            "matches_recommended": 8,
            "needs_followup_if_confirmed": 15,
        },
        "promotion_allowed": False,
    }
    assert len(packet["cases"]) == 65
    assert len(packet["no_immediate_question_case_ids"]) == 35
    assert {case["kind"] for case in packet["cases"]} == {
        "difference",
        "exact_but_policy_review",
    }
    assert {case["id"] for case in packet["cases"]} == difference_ids | policy_ids
    assert set(packet["no_immediate_question_case_ids"]) == no_question_ids
    assert all(case["recommended_expected"] for case in packet["cases"])
    assert all("zhtw_current" in case for case in packet["cases"])


def test_holdout_batch8_diff_review_and_confirmation_are_not_ground_truth() -> None:
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH8)
    diff = load_json(CODEX_GEMINI_BATCH8_DIFF_REVIEW)
    packet = load_json(MAINTAINER_BATCH8_CONFIRMATION)

    batch8_ids = set(expansion["new_case_ids"])

    assert diff["review_stage"] == "codex_gemini_difference_review"
    assert diff["scope"] == "batch8_100_cases"
    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["converter_outputs_used"] is False
    assert diff["source_codex_report"] == (
        "docs/reports/holdout-codex-first-pass-blind-v1-batch8-100-cases-2026-07-10.json"
    )
    assert diff["source_gemini_report"] == (
        "docs/reports/holdout-gemini-cli-advisory-blind-v1-batch8-100-cases-2026-07-10.json"
    )
    assert diff["summary"] == {
        "total_cases": 100,
        "exact_matches": 76,
        "differences": 24,
        "exact_but_policy_review": 42,
        "no_immediate_question": 34,
        "maintainer_queue_total": 66,
        "difference_recommendations": {
            "codex": 17,
            "gemini": 7,
        },
        "by_policy_reason": {
            "Codex confidence medium": 20,
            "Codex review-needed policy guard": 50,
            "high-risk domain": 10,
            "over-conversion guard": 25,
        },
        "promotion_allowed": False,
    }
    difference_ids = {case["id"] for case in diff["differences"]}
    policy_ids = {case["id"] for case in diff["exact_but_policy_review"]}
    no_question_ids = set(diff["no_immediate_question"])
    assert difference_ids | policy_ids | no_question_ids == batch8_ids
    assert len(difference_ids) == 24
    assert len(policy_ids) == 42
    assert len(no_question_ids) == 34
    assert "blind-social-0099" in difference_ids
    assert all(case["recommended_expected"] for case in diff["differences"])

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch8_100_cases"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["converter_outputs_used"] is False
    assert packet["source_diff_review"] == (
        "docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch8-100-cases-2026-07-10.json"
    )
    assert packet["summary"] == {
        "total_review_cases": 66,
        "difference_cases": 24,
        "policy_review_cases": 42,
        "no_immediate_question": 34,
        "difference_recommendations": {
            "codex": 17,
            "gemini": 7,
        },
        "by_domain": {
            "it": 18,
            "ui": 13,
            "llm": 11,
            "formal": 7,
            "social": 7,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 38,
            "baseline_guard": 3,
            "over_conversion_guard": 25,
        },
        "by_kind": {
            "difference": 24,
            "policy_review": 42,
        },
        "by_policy_reason": {
            "Codex confidence medium": 20,
            "Codex review-needed policy guard": 50,
            "high-risk domain": 10,
            "over-conversion guard": 25,
        },
        "promotion_allowed": False,
    }
    assert len(packet["cases"]) == 66
    assert len(packet["no_immediate_question_case_ids"]) == 34
    assert {case["kind"] for case in packet["cases"]} == {
        "difference",
        "policy_review",
    }
    assert {case["id"] for case in packet["cases"]} == difference_ids | policy_ids
    assert set(packet["no_immediate_question_case_ids"]) == no_question_ids
    assert all(case["recommended_expected"] for case in packet["cases"])
    social_0099 = next(case for case in packet["cases"] if case["id"] == "blind-social-0099")
    assert social_0099["recommendation"] == "codex"
    assert social_0099["recommended_acceptable"] == []


def test_holdout_batch9_codex_first_pass_is_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH9)
    codex = load_json(CODEX_BATCH9_FIRST_PASS)

    input_ids = {case["id"] for case in inputs["cases"]}
    batch9_ids = set(expansion["new_case_ids"])

    assert batch9_ids <= input_ids | load_all_removed_case_ids()
    assert codex["review_stage"] == "first_pass_advisory"
    assert codex["reviewer"] == "codex"
    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["source_expansion_report"] == (
        "docs/reports/holdout-input-pool-expansion-blind-v1-batch9-100-cases-2026-07-12.json"
    )
    assert codex["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 60,
            "baseline_guard": 15,
            "over_conversion_guard": 25,
        },
        "by_confidence": {"medium": 20, "high": 80},
        "review_needed": 50,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in codex["cases"]} == batch9_ids
    assert all(case["codex_expected"] for case in codex["cases"])
    assert not any(case["promotion_allowed"] for case in codex["cases"])
    assert sum(1 for case in codex["cases"] if case["review_needed"]) == 50


def test_holdout_batch9_gemini_cli_advisory_is_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH9)
    gemini = load_json(GEMINI_BATCH9_ADVISORY)

    input_ids = {case["id"] for case in inputs["cases"]}
    batch9_ids = set(expansion["new_case_ids"])

    assert batch9_ids <= input_ids | load_all_removed_case_ids()
    assert gemini["review_stage"] == "independent_holdout_expected_review"
    assert gemini["reviewer"] == "gemini_cli"
    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["model_requested"] == "gemini-2.5-flash"
    assert gemini["model_observed"] == ["gemini-3.5-flash"]
    assert gemini["chunking"] == {
        "strategy": "by_domain",
        "domain_order": ["it", "ui", "llm", "formal", "social", "high_risk"],
    }
    assert gemini["source_expansion_report"] == (
        "docs/reports/holdout-input-pool-expansion-blind-v1-batch9-100-cases-2026-07-12.json"
    )
    assert "GEMINI_API_KEY" in gemini["policy"]
    assert gemini["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 60,
            "baseline_guard": 15,
            "over_conversion_guard": 25,
        },
        "by_confidence": {"high": 100},
        "review_needed": 0,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in gemini["cases"]} == batch9_ids
    assert all(case["gemini_expected"] for case in gemini["cases"])
    assert not any(case["promotion_allowed"] for case in gemini["cases"])


def test_holdout_batch9_diff_review_and_confirmation_are_not_ground_truth() -> None:
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH9)
    diff = load_json(CODEX_GEMINI_BATCH9_DIFF_REVIEW)
    packet = load_json(MAINTAINER_BATCH9_CONFIRMATION)

    batch9_ids = set(expansion["new_case_ids"])

    assert diff["review_stage"] == "codex_gemini_difference_review"
    assert diff["scope"] == "batch9_100_cases"
    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["converter_outputs_used"] is False
    assert diff["source_codex_report"] == (
        "docs/reports/holdout-codex-first-pass-blind-v1-batch9-100-cases-2026-07-12.json"
    )
    assert diff["source_gemini_report"] == (
        "docs/reports/holdout-gemini-cli-advisory-blind-v1-batch9-100-cases-2026-07-12.json"
    )
    assert diff["summary"] == {
        "total_cases": 100,
        "exact_matches": 70,
        "differences": 30,
        "exact_but_policy_review": 39,
        "no_immediate_question": 31,
        "maintainer_queue_total": 69,
        "difference_recommendations": {
            "gemini": 7,
            "codex": 23,
        },
        "by_policy_reason": {
            "Codex confidence medium": 20,
            "Codex review-needed policy guard": 50,
            "over-conversion guard": 25,
            "high-risk domain": 10,
        },
        "promotion_allowed": False,
    }
    difference_ids = {case["id"] for case in diff["differences"]}
    policy_ids = {case["id"] for case in diff["exact_but_policy_review"]}
    no_question_ids = set(diff["no_immediate_question"])
    assert difference_ids | policy_ids | no_question_ids == batch9_ids
    assert len(difference_ids) == 30
    assert len(policy_ids) == 39
    assert len(no_question_ids) == 31
    assert all(case["recommended_expected"] for case in diff["differences"])

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch9_100_cases"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["converter_outputs_used"] is False
    assert packet["source_diff_review"] == (
        "docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch9-100-cases-2026-07-12.json"
    )
    assert packet["summary"] == {
        "total_review_cases": 69,
        "difference_cases": 30,
        "policy_review_cases": 39,
        "no_immediate_question": 31,
        "difference_recommendations": {
            "gemini": 7,
            "codex": 23,
        },
        "by_domain": {
            "it": 17,
            "ui": 12,
            "llm": 10,
            "social": 15,
            "formal": 5,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 39,
            "over_conversion_guard": 25,
            "baseline_guard": 5,
        },
        "by_kind": {
            "difference": 30,
            "policy_review": 39,
        },
        "by_policy_reason": {
            "Codex confidence medium": 20,
            "Codex review-needed policy guard": 50,
            "over-conversion guard": 25,
            "high-risk domain": 10,
        },
        "promotion_allowed": False,
    }
    assert len(packet["cases"]) == 69
    assert len(packet["no_immediate_question_case_ids"]) == 31
    assert {case["kind"] for case in packet["cases"]} == {
        "difference",
        "policy_review",
    }
    assert {case["id"] for case in packet["cases"]} == difference_ids | policy_ids
    assert set(packet["no_immediate_question_case_ids"]) == no_question_ids
    assert all(case["recommended_expected"] for case in packet["cases"])


def test_holdout_batch10_advisory_diff_and_confirmation_are_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expected = load_json(EXPECTED)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH10)
    codex = load_json(CODEX_BATCH10_FIRST_PASS)
    gemini = load_json(GEMINI_BATCH10_ADVISORY)
    diff = load_json(CODEX_GEMINI_BATCH10_DIFF_REVIEW)
    packet = load_json(MAINTAINER_BATCH10_CONFIRMATION)

    input_ids = {case["id"] for case in inputs["cases"]}
    expected_ids = {case["id"] for case in expected["cases"]}
    batch10_ids = set(expansion["new_case_ids"])

    removed_ids = load_all_removed_case_ids()
    assert batch10_ids <= input_ids | removed_ids
    assert batch10_ids <= expected_ids | removed_ids

    assert codex["review_stage"] == "first_pass_advisory"
    assert codex["reviewer"] == "codex"
    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["source_expansion_report"] == (
        "docs/reports/holdout-input-pool-expansion-blind-v1-batch10-100-cases-2026-07-12.json"
    )
    assert codex["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 60,
            "baseline_guard": 15,
            "over_conversion_guard": 25,
        },
        "by_confidence": {"medium": 26, "high": 74},
        "review_needed": 36,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in codex["cases"]} == batch10_ids
    assert all(case["codex_expected"] for case in codex["cases"])
    assert not any(case["promotion_allowed"] for case in codex["cases"])

    assert gemini["review_stage"] == "independent_holdout_expected_review"
    assert gemini["reviewer"] == "gemini_cli"
    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["model_requested"] == "gemini-2.5-flash"
    assert gemini["model_observed"] == ["gemini-3.5-flash"]
    assert gemini["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "by_confidence": {"high": 100},
        "quality_flags": 2,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in gemini["cases"]} == batch10_ids
    assert len(gemini["quality_flags"]) == 2
    assert all(case["gemini_expected"] for case in gemini["cases"])

    assert diff["review_stage"] == "codex_gemini_difference_review"
    assert diff["scope"] == "batch10_100_cases"
    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["summary"] == {
        "total_cases": 100,
        "exact_matches": 83,
        "differences": 17,
        "exact_but_policy_review": 27,
        "no_immediate_question": 56,
        "maintainer_queue_total": 44,
        "difference_recommendations": {
            "codex": 0,
            "gemini": 10,
            "manual": 7,
        },
        "gemini_quality_flags": 2,
        "promotion_allowed": False,
    }
    difference_ids = {case["id"] for case in diff["differences"]}
    policy_ids = {case["id"] for case in diff["exact_but_policy_review"]}
    no_question_ids = {case["id"] for case in diff["no_immediate_question"]}
    assert difference_ids | policy_ids | no_question_ids == batch10_ids

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch10_100_cases"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["summary"] == {
        "total_cases": 100,
        "review_queue_cases": 44,
        "differences": 17,
        "exact_but_policy_review": 27,
        "no_immediate_question": 56,
        "gemini_quality_flags": 2,
        "by_domain": {
            "it": 17,
            "ui": 8,
            "llm": 7,
            "formal": 1,
            "social": 1,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 32,
            "baseline_guard": 1,
            "over_conversion_guard": 11,
        },
        "promotion_allowed": False,
    }
    assert {case["id"] for case in packet["cases"]} == difference_ids | policy_ids
    assert set(packet["no_immediate_question_case_ids"]) == no_question_ids
    assert packet["policy"]["private_expected_not_modified"] is True


def test_holdout_batch11_advisory_diff_and_confirmation_are_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expected = load_json(EXPECTED)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH11)
    codex = load_json(CODEX_BATCH11_FIRST_PASS)
    gemini = load_json(GEMINI_BATCH11_ADVISORY)
    diff = load_json(CODEX_GEMINI_BATCH11_DIFF_REVIEW)
    packet = load_json(MAINTAINER_BATCH11_CONFIRMATION)

    input_ids = {case["id"] for case in inputs["cases"]}
    expected_ids = {case["id"] for case in expected["cases"]}
    batch11_ids = set(expansion["new_case_ids"])
    removed_ids = set(load_json(SEALED_POOL_UPDATE_BATCH11_SEMANTIC_REAUDIT)["removed_case_ids"])
    assert batch11_ids <= input_ids | removed_ids
    assert batch11_ids <= expected_ids | removed_ids

    assert codex["review_stage"] == "first_pass_advisory"
    assert codex["reviewer"] == "codex"
    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["summary"]["total_cases"] == 100
    assert codex["summary"]["by_confidence"] == {"medium": 24, "high": 76}
    assert codex["summary"]["review_needed"] == 34
    assert {case["id"] for case in codex["cases"]} == batch11_ids

    assert gemini["review_stage"] == "independent_holdout_expected_review"
    assert gemini["reviewer"] == "gemini_cli"
    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["model_requested"] == "gemini-2.5-pro"
    assert gemini["model_observed"] == ["gemini-2.5-pro", "gemini-1.5-pro"]
    assert gemini["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "by_confidence": {"high": 94, "medium": 6},
        "review_needed": 12,
        "quality_flags": 1,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in gemini["cases"]} == batch11_ids
    assert gemini["quality_flags"][0]["issue"] == ("self_reported_model_metadata_mismatch")

    assert diff["review_stage"] == "codex_gemini_difference_review"
    assert diff["scope"] == "batch11_100_cases"
    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["summary"] == {
        "total_cases": 100,
        "exact_matches": 79,
        "differences": 21,
        "exact_but_policy_review": 29,
        "no_immediate_question": 50,
        "maintainer_queue_total": 50,
        "difference_recommendations": {
            "codex": 18,
            "gemini": 3,
            "manual": 0,
        },
        "gemini_quality_flags": 1,
        "promotion_allowed": False,
    }
    difference_ids = {case["id"] for case in diff["differences"]}
    policy_ids = {case["id"] for case in diff["exact_but_policy_review"]}
    no_question_ids = {case["id"] for case in diff["no_immediate_question"]}
    assert difference_ids | policy_ids | no_question_ids == batch11_ids
    assert not (difference_ids & policy_ids)
    assert not (difference_ids & no_question_ids)
    assert not (policy_ids & no_question_ids)

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch11_100_cases"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["summary"]["review_queue_cases"] == 50
    assert packet["summary"]["no_immediate_question"] == 50
    assert {case["id"] for case in packet["cases"]} == difference_ids | policy_ids
    assert set(packet["no_immediate_question_case_ids"]) == no_question_ids
    assert all(case["recommended_expected"] for case in packet["cases"])
    assert packet["policy"] == {
        "private_expected_not_modified": True,
        "maintainer_confirmation_required_before_expected_update": True,
        "codex_and_gemini_are_advisory_only": True,
        "approval_policy_after_confirmation": "single_human_with_ai_advisory",
    }


def test_holdout_batch11_final_decision_updates_private_expected() -> None:
    expected = load_json(EXPECTED)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH11)
    packet = load_json(MAINTAINER_BATCH11_CONFIRMATION)
    decision = load_json(MAINTAINER_BATCH11_FINAL_DECISION)
    batch11_ids = set(expansion["new_case_ids"])
    batch11_cases = [case for case in expected["cases"] if case["id"] in batch11_ids]

    assert decision["review_stage"] == "maintainer_final_decision_summary"
    assert decision["scope"] == "batch11_100_cases"
    assert decision["maintainer"] == "tim"
    assert decision["decision"] == "review_ok"
    assert decision["expected_values_included"] is False
    assert decision["private_expected_updated"] is True
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_sha256"] == (
        "bbf89dfa8db7774fdd9b8c078f97d18b9b3749f164d5f4e7cc109bb8ac0ab096"
    )
    assert decision["private_expected_sha256"] != private_expected_sha256()
    assert decision["source_inputs_sha256"] == (
        "e7018d35e078a53ff1c59e4a8281b787151fd11c158859ad882defc82b93aff9"
    )
    assert decision["source_inputs_sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert "cases" not in decision
    assert decision["summary"] == {
        "batch11_cases": 100,
        "total_private_expected_cases": 851,
        "status": "sealed_private",
        "approval_policy": "single_human_with_ai_advisory",
        "minimum_human_reviewers": 1,
        "ai_advisory_review_allowed": True,
        "private_expected_updated": True,
        "accepted_recommended_expected": 50,
        "accepted_exact_no_immediate_question": 50,
        "edited_cases": 2,
        "dropped_cases": 0,
        "acceptable_variants_added": 0,
        "by_expected_source_for_batch11": {
            "human_adjudication": 23,
            "human_first_pass": 77,
        },
        "by_disagreement_for_batch11": {"true": 21, "false": 79},
        "by_expected_source_total": {
            "human_first_pass": 680,
            "human_adjudication": 171,
        },
        "by_disagreement_total": {"false": 682, "true": 169},
        "by_domain_for_batch11": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "by_risk_for_batch11": {
            "candidate_gap": 60,
            "baseline_guard": 15,
            "over_conversion_guard": 25,
        },
    }
    removed_ids = set(load_json(SEALED_POOL_UPDATE_BATCH11_SEMANTIC_REAUDIT)["removed_case_ids"])
    assert len(batch11_cases) == 90
    assert {case["id"] for case in batch11_cases} == batch11_ids - removed_ids
    assert decision["confirmed_case_ids"] == {
        "review_packet": [case["id"] for case in packet["cases"]],
        "no_immediate_question": packet["no_immediate_question_case_ids"],
    }


def test_holdout_batch7_final_decision_omits_expected_values() -> None:
    packet = load_json(MAINTAINER_BATCH7_CONFIRMATION)
    decision = load_json(MAINTAINER_BATCH7_FINAL_DECISION)

    assert decision["review_stage"] == "maintainer_final_decision_summary"
    assert decision["scope"] == "batch7_100_cases"
    assert decision["expected_values_included"] is False
    assert decision["private_expected_updated"] is True
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_sha256"] == (
        "1e4e516efc1685ec9c3158ac3a467df3fa8bc66d988dcd34a43d8a6012d09ff5"
    )
    assert decision["private_expected_sha256"] != private_expected_sha256()
    assert "cases" not in decision
    assert decision["source_confirmation_packet"] == (
        "docs/reports/holdout-maintainer-confirmation-blind-v1-batch7-100-cases-2026-07-10.json"
    )
    assert decision["summary"] == {
        "batch7_cases": 100,
        "total_private_expected_cases": 515,
        "status": "sealed_private",
        "approval_policy": "single_human_with_ai_advisory",
        "minimum_human_reviewers": 1,
        "ai_advisory_review_allowed": True,
        "private_expected_updated": True,
        "accepted_recommended_expected": 65,
        "accepted_exact_no_immediate_question": 35,
        "edited_cases": 0,
        "dropped_cases": 0,
        "by_expected_source_for_batch7": {
            "human_adjudication": 28,
            "human_first_pass": 72,
        },
        "by_disagreement_for_batch7": {
            "false": 72,
            "true": 28,
        },
        "by_expected_source_total": {
            "human_adjudication": 105,
            "human_first_pass": 410,
        },
        "by_disagreement_total": {
            "false": 410,
            "true": 105,
        },
        "by_domain_for_batch7": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "by_risk_for_batch7": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
    }
    assert decision["confirmed_case_ids"] == {
        "review_packet": [case["id"] for case in packet["cases"]],
        "no_immediate_question": packet["no_immediate_question_case_ids"],
    }


def test_holdout_batch8_final_decision_omits_expected_values() -> None:
    packet = load_json(MAINTAINER_BATCH8_CONFIRMATION)
    decision = load_json(MAINTAINER_BATCH8_FINAL_DECISION)

    assert decision["review_stage"] == "maintainer_final_decision_summary"
    assert decision["scope"] == "batch8_100_cases"
    assert decision["expected_values_included"] is False
    assert decision["private_expected_updated"] is True
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_sha256"] == (
        "7c78a99becbf120ddae840a56e90334cc4df7f36f1d8b62944058b94e66f6025"
    )
    assert decision["private_expected_sha256"] != private_expected_sha256()
    assert "cases" not in decision
    assert decision["source_confirmation_packet"] == (
        "docs/reports/holdout-maintainer-confirmation-blind-v1-batch8-100-cases-2026-07-10.json"
    )
    assert decision["source_reports"] == [
        "docs/reports/holdout-codex-first-pass-blind-v1-batch8-100-cases-2026-07-10.json",
        "docs/reports/holdout-gemini-cli-advisory-blind-v1-batch8-100-cases-2026-07-10.json",
        "docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch8-100-cases-2026-07-10.json",
        "docs/reports/holdout-maintainer-confirmation-blind-v1-batch8-100-cases-2026-07-10.json",
    ]
    assert decision["summary"] == {
        "batch8_cases": 100,
        "total_private_expected_cases": 598,
        "status": "sealed_private",
        "approval_policy": "single_human_with_ai_advisory",
        "minimum_human_reviewers": 1,
        "ai_advisory_review_allowed": True,
        "private_expected_updated": True,
        "accepted_recommended_expected": 66,
        "accepted_exact_no_immediate_question": 34,
        "edited_cases": 0,
        "dropped_cases": 0,
        "by_expected_source_for_batch8": {
            "human_adjudication": 24,
            "human_first_pass": 76,
        },
        "by_disagreement_for_batch8": {
            "false": 76,
            "true": 24,
        },
        "by_expected_source_total": {
            "human_adjudication": 120,
            "human_first_pass": 478,
        },
        "by_disagreement_total": {
            "false": 478,
            "true": 120,
        },
        "by_domain_for_batch8": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "by_risk_for_batch8": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
    }
    assert decision["confirmed_case_ids"] == {
        "review_packet": [case["id"] for case in packet["cases"]],
        "no_immediate_question": packet["no_immediate_question_case_ids"],
    }


def test_holdout_batch9_final_decision_omits_expected_values() -> None:
    packet = load_json(MAINTAINER_BATCH9_CONFIRMATION)
    decision = load_json(MAINTAINER_BATCH9_FINAL_DECISION)

    assert decision["review_stage"] == "maintainer_final_decision_summary"
    assert decision["scope"] == "batch9_100_cases"
    assert decision["expected_values_included"] is False
    assert decision["private_expected_updated"] is True
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_sha256"] == (
        "2c67fe35f756fc406577b042f9c05380bb635426b1c253a3385fa8c3c5224d41"
    )
    assert decision["private_expected_sha256"] != private_expected_sha256()
    assert decision["source_inputs_sha256"] == (
        "0ac742ac9885cdae198bed6fc376c2fb5c3e991573ae4cb4ac2072cfef3e937d"
    )
    assert decision["source_inputs_sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert "cases" not in decision
    assert decision["source_confirmation_packet"] == (
        "docs/reports/holdout-maintainer-confirmation-blind-v1-batch9-100-cases-2026-07-12.json"
    )
    assert decision["source_reports"] == [
        "docs/reports/holdout-codex-first-pass-blind-v1-batch9-100-cases-2026-07-12.json",
        "docs/reports/holdout-gemini-cli-advisory-blind-v1-batch9-100-cases-2026-07-12.json",
        "docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch9-100-cases-2026-07-12.json",
        "docs/reports/holdout-maintainer-confirmation-blind-v1-batch9-100-cases-2026-07-12.json",
    ]
    assert decision["summary"] == {
        "batch9_cases": 100,
        "total_private_expected_cases": 683,
        "status": "sealed_private",
        "approval_policy": "single_human_with_ai_advisory",
        "minimum_human_reviewers": 1,
        "ai_advisory_review_allowed": True,
        "private_expected_updated": True,
        "accepted_recommended_expected": 69,
        "accepted_exact_no_immediate_question": 31,
        "edited_cases": 0,
        "dropped_cases": 0,
        "by_expected_source_for_batch9": {
            "human_adjudication": 30,
            "human_first_pass": 70,
        },
        "by_disagreement_for_batch9": {
            "false": 70,
            "true": 30,
        },
        "by_expected_source_total": {
            "human_adjudication": 140,
            "human_first_pass": 543,
        },
        "by_disagreement_total": {
            "false": 543,
            "true": 140,
        },
        "by_domain_for_batch9": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "by_risk_for_batch9": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
    }
    assert decision["confirmed_case_ids"] == {
        "review_packet": [case["id"] for case in packet["cases"]],
        "no_immediate_question": packet["no_immediate_question_case_ids"],
    }


def test_holdout_batch10_final_decision_omits_expected_values() -> None:
    packet = load_json(MAINTAINER_BATCH10_CONFIRMATION)
    decision = load_json(MAINTAINER_BATCH10_FINAL_DECISION)

    assert decision["review_stage"] == "maintainer_final_decision_summary"
    assert decision["scope"] == "batch10_100_cases"
    assert decision["expected_values_included"] is False
    assert decision["private_expected_updated"] is True
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_sha256"] == (
        "b8150c2e41e2bc574de54a730fe1a0c1c1edf39a9efce344ef1bbbd267179250"
    )
    assert decision["private_expected_sha256"] != private_expected_sha256()
    assert decision["private_expected_sha256_before"] == (
        "0e41c9ac8c130075d66f23daeeb80afd6e69903319ea473e9ac5e7ed38d5f7ab"
    )
    assert decision["source_inputs_sha256"] == (
        "eff19da4ff198981bdb0018bceabb128b1aa5a33e9199ea5421f69561da340d0"
    )
    assert decision["source_inputs_sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert "cases" not in decision
    assert decision["source_confirmation_packet"] == (
        "docs/reports/holdout-maintainer-confirmation-blind-v1-batch10-100-cases-2026-07-12.json"
    )
    assert decision["source_reports"] == [
        "docs/reports/holdout-codex-first-pass-blind-v1-batch10-100-cases-2026-07-12.json",
        "docs/reports/holdout-gemini-cli-advisory-blind-v1-batch10-100-cases-2026-07-12.json",
        "docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch10-100-cases-2026-07-12.json",
        "docs/reports/holdout-maintainer-confirmation-blind-v1-batch10-100-cases-2026-07-12.json",
    ]
    assert decision["summary"] == {
        "batch10_cases": 100,
        "total_private_expected_cases": 767,
        "status": "sealed_private",
        "approval_policy": "single_human_with_ai_advisory",
        "minimum_human_reviewers": 1,
        "ai_advisory_review_allowed": True,
        "private_expected_updated": True,
        "accepted_recommended_expected": 44,
        "accepted_exact_no_immediate_question": 56,
        "edited_cases": 0,
        "dropped_cases": 0,
        "by_expected_source_for_batch10": {
            "human_adjudication": 17,
            "human_first_pass": 83,
        },
        "by_disagreement_for_batch10": {
            "false": 83,
            "true": 17,
        },
        "by_expected_source_total": {
            "human_adjudication": 151,
            "human_first_pass": 616,
        },
        "by_disagreement_total": {
            "false": 616,
            "true": 151,
        },
        "by_domain_for_batch10": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "by_risk_for_batch10": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
    }
    assert decision["confirmed_case_ids"] == {
        "review_packet": [case["id"] for case in packet["cases"]],
        "no_immediate_question": packet["no_immediate_question_case_ids"],
    }


def test_holdout_batch4_final_decision_omits_expected_values() -> None:
    packet = load_json(MAINTAINER_BATCH4_CONFIRMATION)
    decision = load_json(MAINTAINER_BATCH4_FINAL_DECISION)

    assert decision["review_stage"] == "maintainer_final_decision_summary"
    assert decision["scope"] == "batch4_100_cases"
    assert decision["expected_values_included"] is False
    assert decision["private_expected_updated"] is True
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert len(decision["private_expected_sha256"]) == 64
    assert "cases" not in decision
    assert decision["source_confirmation_packet"] == (
        "docs/reports/holdout-maintainer-confirmation-blind-v1-batch4-100-cases-2026-07-09.json"
    )
    assert decision["summary"] == {
        "batch4_cases": 100,
        "total_private_expected_cases": 261,
        "status": "sealed_private",
        "approval_policy": "single_human_with_ai_advisory",
        "minimum_human_reviewers": 1,
        "ai_advisory_review_allowed": True,
        "private_expected_updated": True,
        "accepted_recommended_expected": 64,
        "accepted_exact_no_immediate_question": 36,
        "edited_cases": 0,
        "dropped_cases": 0,
        "by_expected_source_for_batch4": {
            "human_adjudication": 26,
            "human_first_pass": 74,
        },
        "by_disagreement_for_batch4": {
            "false": 74,
            "true": 26,
        },
        "by_expected_source_total": {
            "human_adjudication": 68,
            "human_first_pass": 193,
        },
        "by_disagreement_total": {
            "false": 193,
            "true": 68,
        },
        "by_domain_for_batch4": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "by_risk_for_batch4": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
    }
    assert decision["confirmed_case_ids"] == {
        "review_packet": [case["id"] for case in packet["cases"]],
        "no_immediate_question": packet["no_immediate_question_case_ids"],
    }


def test_holdout_batch5_final_decision_omits_expected_values() -> None:
    packet = load_json(MAINTAINER_BATCH5_CONFIRMATION)
    decision = load_json(MAINTAINER_BATCH5_FINAL_DECISION)

    assert decision["review_stage"] == "maintainer_final_decision_summary"
    assert decision["scope"] == "batch5_100_cases"
    assert decision["expected_values_included"] is False
    assert decision["private_expected_updated"] is True
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert len(decision["private_expected_sha256"]) == 64
    assert "cases" not in decision
    assert decision["source_confirmation_packet"] == (
        "docs/reports/holdout-maintainer-confirmation-blind-v1-batch5-100-cases-2026-07-09.json"
    )
    assert decision["summary"] == {
        "batch5_cases": 100,
        "total_private_expected_cases": 338,
        "status": "sealed_private",
        "approval_policy": "single_human_with_ai_advisory",
        "minimum_human_reviewers": 1,
        "ai_advisory_review_allowed": True,
        "private_expected_updated": True,
        "accepted_recommended_expected": 50,
        "accepted_exact_no_immediate_question": 50,
        "edited_cases": 0,
        "dropped_cases": 0,
        "by_expected_source_for_batch5": {
            "human_adjudication": 8,
            "human_first_pass": 92,
        },
        "by_disagreement_for_batch5": {
            "false": 92,
            "true": 8,
        },
        "by_expected_source_total": {
            "human_adjudication": 65,
            "human_first_pass": 273,
        },
        "by_disagreement_total": {
            "false": 273,
            "true": 65,
        },
        "by_domain_for_batch5": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "by_risk_for_batch5": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
    }
    assert decision["confirmed_case_ids"] == {
        "review_packet": [case["id"] for case in packet["cases"]],
        "no_immediate_question": packet["no_immediate_question_case_ids"],
    }


def test_holdout_batch6_final_decision_omits_expected_values() -> None:
    packet = load_json(MAINTAINER_BATCH6_CONFIRMATION)
    decision = load_json(MAINTAINER_BATCH6_FINAL_DECISION)

    assert decision["review_stage"] == "maintainer_final_decision_summary"
    assert decision["scope"] == "batch6_100_cases"
    assert decision["expected_values_included"] is False
    assert decision["private_expected_updated"] is True
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert len(decision["private_expected_sha256"]) == 64
    assert "cases" not in decision
    assert decision["source_confirmation_packet"] == (
        "docs/reports/holdout-maintainer-confirmation-blind-v1-batch6-100-cases-2026-07-10.json"
    )
    assert decision["summary"] == {
        "batch6_cases": 100,
        "total_private_expected_cases": 426,
        "status": "sealed_private",
        "approval_policy": "single_human_with_ai_advisory",
        "minimum_human_reviewers": 1,
        "ai_advisory_review_allowed": True,
        "private_expected_updated": True,
        "accepted_recommended_expected": 76,
        "accepted_exact_no_immediate_question": 24,
        "edited_cases": 0,
        "dropped_cases": 0,
        "by_expected_source_for_batch6": {
            "human_adjudication": 20,
            "human_first_pass": 80,
        },
        "by_disagreement_for_batch6": {
            "false": 80,
            "true": 20,
        },
        "by_expected_source_total": {
            "human_adjudication": 84,
            "human_first_pass": 342,
        },
        "by_disagreement_total": {
            "false": 342,
            "true": 84,
        },
        "by_domain_for_batch6": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "by_risk_for_batch6": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
    }
    assert decision["confirmed_case_ids"] == {
        "review_packet": [case["id"] for case in packet["cases"]],
        "no_immediate_question": packet["no_immediate_question_case_ids"],
    }
