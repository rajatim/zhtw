# zhtw:disable
# ruff: noqa: F403,F405
"""Blind-v1 governance and sealed-data safety tests."""

from tests._accuracy_holdout_support import *  # noqa: F403


def test_private_expected_covers_current_pool_after_batch13_review() -> None:
    inputs = load_json(INPUTS)
    expected = load_json(EXPECTED)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH5)
    batch6 = load_json(INPUT_POOL_EXPANSION_BATCH6)
    batch7 = load_json(INPUT_POOL_EXPANSION_BATCH7)
    batch8 = load_json(INPUT_POOL_EXPANSION_BATCH8)
    batch9 = load_json(INPUT_POOL_EXPANSION_BATCH9)
    batch10 = load_json(INPUT_POOL_EXPANSION_BATCH10)
    batch11 = load_json(INPUT_POOL_EXPANSION_BATCH11)
    batch12 = load_json(INPUT_POOL_EXPANSION_BATCH12)
    batch13 = load_json(INPUT_POOL_EXPANSION_BATCH13)
    batch7_miss_review = load_json(SEALED_POOL_UPDATE_BATCH7_MISS_REVIEW)
    batch8_miss_review = load_json(SEALED_POOL_UPDATE_BATCH8_MISS_REVIEW)
    batch9_miss_review = load_json(SEALED_POOL_UPDATE_BATCH9_MISS_REVIEW)
    batch10_miss_review = load_json(SEALED_POOL_UPDATE_BATCH10_MISS_REVIEW)
    batch5_ids = set(expansion["new_case_ids"])
    batch6_ids = set(batch6["new_case_ids"])
    batch7_ids = set(batch7["new_case_ids"])
    batch8_ids = set(batch8["new_case_ids"])
    batch9_ids = set(batch9["new_case_ids"])
    batch10_ids = set(batch10["new_case_ids"])
    batch11_ids = set(batch11["new_case_ids"])
    batch12_ids = set(batch12["new_case_ids"])
    batch13_ids = set(batch13["new_case_ids"])
    input_ids = [case["id"] for case in inputs["cases"]]
    expected_ids = [case["id"] for case in expected["cases"]]
    batch7_removed_ids = set(batch7_miss_review["removed_case_ids"])
    batch8_removed_ids = set(batch8_miss_review["removed_case_ids"])
    batch9_removed_ids = set(batch9_miss_review["removed_case_ids"])
    batch10_removed_ids = set(batch10_miss_review["removed_case_ids"])

    semantic_removed_ids = set(
        load_json(SEALED_POOL_UPDATE_BATCH11_SEMANTIC_REAUDIT)["removed_case_ids"]
    )
    batch12_removed_ids = set(load_json(SEALED_POOL_UPDATE_BATCH12_MISS_REVIEW)["removed_case_ids"])
    batch13_removed_ids = set(load_json(SEALED_POOL_UPDATE_BATCH13_MISS_REVIEW)["removed_case_ids"])
    assert len(input_ids) == 1008
    assert len(expected_ids) == 1008
    assert set(expected_ids) == set(input_ids)
    assert batch13_ids - batch13_removed_ids <= set(input_ids)
    assert batch13_ids - batch13_removed_ids <= set(expected_ids)
    assert not (batch13_removed_ids & set(input_ids))
    assert not (batch13_removed_ids & set(expected_ids))
    assert batch12_ids - batch12_removed_ids <= set(expected_ids)
    assert batch12_ids - batch12_removed_ids <= set(input_ids)
    assert not (batch12_removed_ids & set(input_ids))
    assert not (batch12_removed_ids & set(expected_ids))
    assert batch11_ids - semantic_removed_ids <= set(input_ids)
    assert batch11_ids - semantic_removed_ids <= set(expected_ids)
    assert not (semantic_removed_ids & set(input_ids))
    assert not (semantic_removed_ids & set(expected_ids))
    assert batch10_ids - batch10_removed_ids <= set(expected_ids)
    assert batch10_ids - batch10_removed_ids <= set(input_ids)
    assert batch9_ids - batch9_removed_ids <= set(expected_ids)
    assert batch9_ids - batch9_removed_ids <= set(input_ids)
    assert not (set(input_ids) & batch8_removed_ids)
    assert not (set(expected_ids) & batch8_removed_ids)
    assert not (set(input_ids) & batch9_removed_ids)
    assert not (set(expected_ids) & batch9_removed_ids)
    assert not (set(input_ids) & batch10_removed_ids)
    assert not (set(expected_ids) & batch10_removed_ids)
    assert expected["status"] == "sealed_private"
    assert expected["source_inputs"] == "benchmarks/accuracy/blind-v1.inputs.json"
    assert expected["source_inputs_sha256"] == hashlib.sha256(INPUTS.read_bytes()).hexdigest()

    batch5_cases = [case for case in expected["cases"] if case["id"] in batch5_ids]
    assert len(batch5_cases) == 88
    assert Counter(case["annotation"]["expected_source"] for case in batch5_cases) == {
        "human_first_pass": 81,
        "human_adjudication": 7,
    }
    assert Counter(str(case["annotation"]["disagreement"]).lower() for case in batch5_cases) == {
        "false": 81,
        "true": 7,
    }
    assert all(
        case["annotation"]["ai_advisory_reviewers"] == ["codex", "gemini_cli"]
        for case in batch5_cases
    )
    assert all(
        "docs/reports/holdout-maintainer-final-decision-blind-v1-batch5-100-cases-2026-07-09.json"
        in case["annotation"]["source_reports"]
        for case in batch5_cases
    )

    batch6_cases = [case for case in expected["cases"] if case["id"] in batch6_ids]
    assert len(batch6_cases) == 89
    assert Counter(case["annotation"]["expected_source"] for case in batch6_cases) == {
        "human_first_pass": 76,
        "human_adjudication": 13,
    }
    assert Counter(str(case["annotation"]["disagreement"]).lower() for case in batch6_cases) == {
        "false": 76,
        "true": 13,
    }
    assert all(
        case["annotation"]["ai_advisory_reviewers"] == ["codex", "gemini_cli"]
        for case in batch6_cases
    )
    assert all(
        "docs/reports/holdout-maintainer-final-decision-blind-v1-batch6-100-cases-2026-07-10.json"
        in case["annotation"]["source_reports"]
        for case in batch6_cases
    )

    batch7_cases = [case for case in expected["cases"] if case["id"] in batch7_ids]
    assert len(batch7_cases) == 83
    assert not (set(expected_ids) & batch7_removed_ids)
    assert Counter(case["annotation"]["expected_source"] for case in batch7_cases) == {
        "human_first_pass": 64,
        "human_adjudication": 19,
    }
    assert Counter(str(case["annotation"]["disagreement"]).lower() for case in batch7_cases) == {
        "false": 64,
        "true": 19,
    }
    assert all(
        case["annotation"]["ai_advisory_reviewers"] == ["codex", "gemini_cli"]
        for case in batch7_cases
    )
    acceptable_variant_ids = {
        "blind-it-0146",
        "blind-it-0147",
        "blind-it-0148",
        "blind-it-0157",
        "blind-ui-0108",
        "blind-ui-0110",
        "blind-ui-0118",
    }
    acceptable_variant_cases = [
        case for case in batch7_cases if case["id"] in acceptable_variant_ids
    ]
    assert len(acceptable_variant_cases) == 7
    assert all(
        "docs/reports/holdout-maintainer-final-decision-batch7-miss-classification-blind-v1-2026-07-10.json"
        in case["annotation"]["source_reports"]
        for case in acceptable_variant_cases
    )
    assert all(
        "docs/reports/holdout-maintainer-final-decision-blind-v1-batch7-100-cases-2026-07-10.json"
        in case["annotation"]["source_reports"]
        for case in batch7_cases
    )

    batch8_cases = [case for case in expected["cases"] if case["id"] in batch8_ids]
    assert len(batch8_cases) == 85
    assert Counter(case["annotation"]["expected_source"] for case in batch8_cases) == {
        "human_first_pass": 71,
        "human_adjudication": 14,
    }
    assert Counter(str(case["annotation"]["disagreement"]).lower() for case in batch8_cases) == {
        "false": 71,
        "true": 14,
    }
    assert all(
        case["annotation"]["first_reviewer"] == "tim"
        and case["annotation"]["second_reviewer"] == ""
        and case["annotation"]["ai_advisory_reviewers"] == ["codex", "gemini_cli"]
        for case in batch8_cases
    )
    assert all(
        "docs/reports/holdout-maintainer-final-decision-blind-v1-batch8-100-cases-2026-07-10.json"
        in case["annotation"]["source_reports"]
        for case in batch8_cases
    )
    batch8_acceptable_variant_ids = {
        "blind-it-0167",
        "blind-it-0175",
        "blind-llm-0097",
        "blind-social-0095",
    }
    batch8_acceptable_variant_cases = [
        case for case in batch8_cases if case["id"] in batch8_acceptable_variant_ids
    ]
    assert len(batch8_acceptable_variant_cases) == 4
    assert all(
        "docs/reports/holdout-maintainer-final-decision-batch8-miss-classification-blind-v1-2026-07-11.json"
        in case["annotation"]["source_reports"]
        for case in batch8_acceptable_variant_cases
    )
    assert all("regional_term" in case["issue_tags"] for case in batch8_cases)
    social_0099 = next(case for case in batch8_cases if case["id"] == "blind-social-0099")
    assert social_0099["expected"] == "可以幫我確認外送到了沒？"
    assert social_0099["acceptable"] == []

    batch9_cases = [case for case in expected["cases"] if case["id"] in batch9_ids]
    assert len(batch9_cases) == 84
    assert Counter(case["annotation"]["expected_source"] for case in batch9_cases) == {
        "human_first_pass": 60,
        "human_adjudication": 24,
    }
    assert Counter(str(case["annotation"]["disagreement"]).lower() for case in batch9_cases) == {
        "false": 60,
        "true": 24,
    }
    assert all(
        case["annotation"]["first_reviewer"] == "tim"
        and case["annotation"]["second_reviewer"] == ""
        and case["annotation"]["ai_advisory_reviewers"] == ["codex", "gemini_cli"]
        for case in batch9_cases
    )
    assert all(
        "docs/reports/holdout-maintainer-final-decision-blind-v1-batch9-100-cases-2026-07-12.json"
        in case["annotation"]["source_reports"]
        for case in batch9_cases
    )
    batch9_acceptable_variant_ids = {
        "blind-it-0189",
        "blind-it-0197",
        "blind-it-0202",
        "blind-it-0206",
        "blind-ui-0148",
        "blind-ui-0166",
    }
    batch9_acceptable_variant_cases = [
        case for case in batch9_cases if case["id"] in batch9_acceptable_variant_ids
    ]
    assert len(batch9_acceptable_variant_cases) == 6
    assert all(
        "docs/reports/holdout-maintainer-final-decision-batch9-miss-classification-blind-v1-2026-07-12.json"
        in case["annotation"]["source_reports"]
        for case in batch9_acceptable_variant_cases
    )
    assert all("regional_term" in case["issue_tags"] for case in batch9_cases)

    batch10_cases = [case for case in expected["cases"] if case["id"] in batch10_ids]
    assert len(batch10_cases) == 84
    assert Counter(case["annotation"]["expected_source"] for case in batch10_cases) == {
        "human_first_pass": 70,
        "human_adjudication": 14,
    }
    assert Counter(str(case["annotation"]["disagreement"]).lower() for case in batch10_cases) == {
        "false": 70,
        "true": 14,
    }
    assert all(
        case["annotation"]["first_reviewer"] == "tim"
        and case["annotation"]["second_reviewer"] == ""
        and case["annotation"]["ai_advisory_reviewers"] == ["codex", "gemini_cli"]
        for case in batch10_cases
    )
    assert all(
        "docs/reports/holdout-maintainer-final-decision-blind-v1-batch10-100-cases-2026-07-12.json"
        in case["annotation"]["source_reports"]
        for case in batch10_cases
    )
    batch10_acceptable_variant_ids = {
        "blind-it-0222",
        "blind-it-0232",
        "blind-llm-0123",
        "blind-llm-0137",
    }
    batch10_acceptable_variant_cases = [
        case for case in batch10_cases if case["id"] in batch10_acceptable_variant_ids
    ]
    assert len(batch10_acceptable_variant_cases) == 4
    assert all(
        "docs/reports/holdout-maintainer-final-decision-batch10-miss-classification-blind-v1-2026-07-13.json"
        in case["annotation"]["source_reports"]
        for case in batch10_acceptable_variant_cases
    )
    assert all("regional_term" in case["issue_tags"] for case in batch10_cases)


def test_holdout_expansion_differences_confirmation_packet_is_not_ground_truth() -> None:
    diff = load_json(CODEX_GEMINI_EXPANSION_DIFF_REVIEW)
    packet = load_json(MAINTAINER_EXPANSION_DIFFERENCES_CONFIRMATION)

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "expansion_differences_only"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["source_diff_review"] == (
        "docs/reports/holdout-codex-gemini-diff-review-blind-v1-expansion-127-cases-2026-07-09.json"
    )
    assert packet["summary"] == {
        "total_review_cases": 48,
        "difference_cases": 48,
        "policy_review_cases": 0,
        "deferred_policy_review_cases": 33,
        "no_immediate_question": 46,
        "difference_recommendations": {
            "codex": 39,
            "gemini": 7,
            "third_value": 2,
        },
        "promotion_allowed": False,
    }
    assert len(packet["cases"]) == 48
    assert {case["id"] for case in packet["cases"]} == {case["id"] for case in diff["differences"]}
    assert packet["deferred_policy_review_case_ids"] == [
        case["id"] for case in diff["exact_but_policy_review"]
    ]
    assert packet["no_immediate_question_case_ids"] == [
        case["id"] for case in diff["no_immediate_question"]
    ]
    assert {case["kind"] for case in packet["cases"]} == {"difference"}
    assert {case["maintainer_action"] for case in packet["cases"]} == {"confirm_or_edit"}
    assert all(case["recommended_expected"] for case in packet["cases"])


def test_holdout_expansion_differences_final_decision_omits_expected_values() -> None:
    packet = load_json(MAINTAINER_EXPANSION_DIFFERENCES_CONFIRMATION)
    decision = load_json(MAINTAINER_EXPANSION_DIFFERENCES_FINAL_DECISION)

    assert decision["review_stage"] == "maintainer_partial_final_decision_summary"
    assert decision["scope"] == "expansion_differences_only"
    assert decision["expected_values_included"] is False
    assert decision["private_expected_updated"] is False
    assert "cases" not in decision
    assert decision["source_confirmation_packet"] == (
        "docs/reports/"
        "holdout-maintainer-confirmation-blind-v1-expansion-differences-2026-07-09.json"
    )
    assert decision["summary"] == {
        "total_confirmed_cases": 48,
        "accepted_recommended_expected": 48,
        "edited_cases": 0,
        "dropped_cases": 0,
        "deferred_policy_review_cases": 33,
        "no_immediate_question_cases": 46,
        "private_expected_updated": False,
        "private_expected_update_blocker": (
            "Partial expansion decision only; current blind-v1.inputs.json has 200 cases "
            "and run_accuracy_benchmark requires expected ids and source_inputs_sha256 "
            "to match the full input file."
        ),
        "would_be_expected_source": {"human_adjudication": 48},
        "by_recommendation": {
            "codex": 39,
            "gemini": 7,
            "third_value": 2,
        },
        "by_domain": {
            "formal": 2,
            "high_risk": 2,
            "it": 27,
            "llm": 8,
            "social": 5,
            "ui": 4,
        },
        "by_risk": {
            "baseline_guard": 2,
            "candidate_gap": 31,
            "over_conversion_guard": 15,
        },
    }
    assert decision["confirmed_case_ids"] == [case["id"] for case in packet["cases"]]


def test_holdout_expansion_policy_review_confirmation_packet_is_not_ground_truth() -> None:
    diff = load_json(CODEX_GEMINI_EXPANSION_DIFF_REVIEW)
    packet = load_json(MAINTAINER_EXPANSION_POLICY_REVIEW_CONFIRMATION)

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "expansion_policy_review_only"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["source_diff_review"] == (
        "docs/reports/holdout-codex-gemini-diff-review-blind-v1-expansion-127-cases-2026-07-09.json"
    )
    assert packet["summary"] == {
        "total_review_cases": 33,
        "difference_cases": 0,
        "policy_review_cases": 33,
        "no_immediate_question": 46,
        "recommendation": {"codex_gemini_match": 33},
        "by_domain": {
            "formal": 4,
            "high_risk": 8,
            "it": 3,
            "llm": 4,
            "social": 5,
            "ui": 9,
        },
        "by_risk": {
            "baseline_guard": 3,
            "candidate_gap": 14,
            "over_conversion_guard": 16,
        },
        "by_policy_reason": {
            "Codex confidence medium": 11,
            "high-risk domain": 4,
            "high-risk domain, Codex confidence medium": 2,
            "high-risk domain, over-conversion guard": 2,
            "over-conversion guard": 14,
        },
        "promotion_allowed": False,
    }
    assert len(packet["cases"]) == 33
    assert {case["id"] for case in packet["cases"]} == {
        case["id"] for case in diff["exact_but_policy_review"]
    }
    assert packet["no_immediate_question_case_ids"] == [
        case["id"] for case in diff["no_immediate_question"]
    ]
    assert {case["kind"] for case in packet["cases"]} == {"exact_but_policy_review"}
    assert {case["recommendation"] for case in packet["cases"]} == {"codex_gemini_match"}
    assert {case["maintainer_action"] for case in packet["cases"]} == {"confirm_or_edit"}
    assert all(case["recommended_expected"] for case in packet["cases"])


def test_holdout_expansion_policy_review_final_decision_omits_expected_values() -> None:
    packet = load_json(MAINTAINER_EXPANSION_POLICY_REVIEW_CONFIRMATION)
    decision = load_json(MAINTAINER_EXPANSION_POLICY_REVIEW_FINAL_DECISION)

    assert decision["review_stage"] == "maintainer_partial_final_decision_summary"
    assert decision["scope"] == "expansion_policy_review_only"
    assert decision["expected_values_included"] is False
    assert decision["private_expected_updated"] is False
    assert "cases" not in decision
    assert decision["source_confirmation_packet"] == (
        "docs/reports/"
        "holdout-maintainer-confirmation-blind-v1-expansion-policy-review-2026-07-09.json"
    )
    assert decision["summary"] == {
        "total_confirmed_cases": 33,
        "accepted_recommended_expected": 33,
        "edited_cases": 0,
        "dropped_cases": 0,
        "no_immediate_question_cases": 46,
        "private_expected_updated": False,
        "private_expected_update_note": (
            "This policy-review summary records maintainer approval only; the private "
            "expected file is rebuilt by the full 127-case expansion decision summary."
        ),
        "would_be_expected_source": {"human_first_pass": 33},
        "by_recommendation": {"codex_gemini_match": 33},
        "by_domain": {
            "formal": 4,
            "high_risk": 8,
            "it": 3,
            "llm": 4,
            "social": 5,
            "ui": 9,
        },
        "by_risk": {
            "baseline_guard": 3,
            "candidate_gap": 14,
            "over_conversion_guard": 16,
        },
        "by_policy_reason": {
            "Codex confidence medium": 11,
            "high-risk domain": 4,
            "high-risk domain, Codex confidence medium": 2,
            "high-risk domain, over-conversion guard": 2,
            "over-conversion guard": 14,
        },
    }
    assert decision["confirmed_case_ids"] == [case["id"] for case in packet["cases"]]


def test_holdout_expansion_final_decision_omits_expected_values() -> None:
    diff_decision = load_json(MAINTAINER_EXPANSION_DIFFERENCES_FINAL_DECISION)
    policy_decision = load_json(MAINTAINER_EXPANSION_POLICY_REVIEW_FINAL_DECISION)
    diff = load_json(CODEX_GEMINI_EXPANSION_DIFF_REVIEW)
    decision = load_json(MAINTAINER_EXPANSION_FINAL_DECISION)

    assert decision["review_stage"] == "maintainer_final_decision_summary"
    assert decision["scope"] == "expansion_127_cases"
    assert decision["expected_values_included"] is False
    assert decision["private_expected_updated"] is True
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert len(decision["private_expected_sha256"]) == 64
    assert "cases" not in decision
    assert (
        "docs/reports/"
        "holdout-maintainer-final-decision-blind-v1-expansion-policy-review-2026-07-09.json"
    ) in decision["source_reports"]
    assert decision["summary"] == {
        "expansion_cases": 127,
        "total_private_expected_cases": 200,
        "status": "sealed_private",
        "approval_policy": "single_human_with_ai_advisory",
        "minimum_human_reviewers": 1,
        "ai_advisory_review_allowed": True,
        "private_expected_updated": True,
        "accepted_recommended_expected": 81,
        "accepted_exact_no_immediate_question": 46,
        "edited_cases": 0,
        "dropped_cases": 0,
        "by_expected_source_for_expansion": {
            "human_adjudication": 48,
            "human_first_pass": 79,
        },
        "by_disagreement_for_expansion": {
            "false": 79,
            "true": 48,
        },
        "by_expected_source_total": {
            "human_adjudication": 65,
            "human_first_pass": 135,
        },
        "by_disagreement_total": {
            "false": 135,
            "true": 65,
        },
        "by_domain_for_expansion": {
            "formal": 18,
            "high_risk": 10,
            "it": 37,
            "llm": 17,
            "social": 18,
            "ui": 27,
        },
        "by_risk_for_expansion": {
            "baseline_guard": 17,
            "candidate_gap": 79,
            "over_conversion_guard": 31,
        },
    }
    assert decision["confirmed_case_ids"] == {
        "differences": diff_decision["confirmed_case_ids"],
        "policy_review": policy_decision["confirmed_case_ids"],
        "no_immediate_question": [case["id"] for case in diff["no_immediate_question"]],
    }


def test_competitors_lock_records_reproducible_adapters() -> None:
    lock = load_json(COMPETITORS_LOCK)
    competitors = {item["id"]: item for item in lock["competitors"]}

    assert lock["status"] == "locked"
    assert {
        "zhtw",
        "opencc-s2twp",
        "zhconv-zh-tw",
        "opencc-js-cn-twp",
        "zhconv-rs-zh-tw",
    } == set(competitors)
    assert competitors["zhtw"]["included_in_formal_runner"] is True
    assert competitors["opencc-s2twp"]["locale_or_config"] == "s2twp.json"
    assert competitors["zhconv-zh-tw"]["locale_or_config"] == "zh-tw"
    assert competitors["opencc-js-cn-twp"]["included_in_formal_runner"] is True
    assert competitors["zhconv-rs-zh-tw"]["included_in_formal_runner"] is True
    assert competitors["opencc-s2twp"]["family"] == "opencc"
    assert competitors["opencc-js-cn-twp"]["family"] == "opencc"
    assert competitors["zhconv-zh-tw"]["family"] == "mediawiki-zhconv"
    assert competitors["zhconv-rs-zh-tw"]["family"] == "mediawiki-zhconv"

    for competitor in competitors.values():
        assert competitor["command"]
        assert competitor["version"]
        assert competitor["version_probe"]
        assert len(competitor["config_sha256"]) == 64
        assert (
            "expected output" not in competitor["notes"].lower()
            or "never" in competitor["notes"].lower()
        )


def test_create_holdout_annotation_packet(tmp_path: Path) -> None:
    output = tmp_path / "holdout-packet.md"

    result = subprocess.run(
        [
            sys.executable,
            str(PACKET_SCRIPT),
            "--inputs",
            str(INPUTS),
            "--batch",
            "blind-high-risk",
            "--generated-date",
            "2026-07-07",
            "--reviewer-stage",
            "first_human_review",
            "--output",
            str(output),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert "Wrote" in result.stdout
    assert "(128 cases)" in result.stdout

    content = output.read_text(encoding="utf-8")
    assert content.startswith("<!-- zhtw:disable -->")
    assert "Reviewer stage: `first_human_review`" in content
    assert "Cases: 128" in content
    assert "### blind-high-risk-0001" in content
    assert "不得以定型化契约条款排除责任。" in content
    assert "Do not run zhtw, OpenCC, zhconv, Gemini, or any converter" in content
    assert "Expected:" in content
    assert "Acceptable:" in content
    assert "Reviewer notes:" in content
    assert "跨行匯款手續費由使用者負擔。" not in content


def test_codex_first_pass_report_is_advisory_only() -> None:
    inputs = load_json(INPUTS)
    report = load_json(CODEX_FIRST_PASS)

    input_ids = [case["id"] for case in inputs["cases"]]
    report_ids = [case["id"] for case in report["cases"]]
    original_seed_input_ids = original_seed_ids_from_report(report_ids, input_ids)
    removed_ids = load_all_removed_case_ids()
    removed_report_ids = set(report_ids) & removed_ids

    assert report["review_stage"] == "first_pass_advisory"
    assert report["reviewer"] == "codex"
    assert report["ground_truth"] is False
    assert report["promotion_allowed"] is False
    assert report["summary"]["total_cases"] == len(report["cases"]) == 100
    assert report["summary"]["promotion_allowed"] is False
    assert report["summary"]["by_confidence"] == {"high": 83, "medium": 17}
    assert report["summary"]["review_needed"] == 36
    assert [case_id for case_id in report_ids if case_id not in removed_ids] == (
        original_seed_input_ids
    )
    assert len(report_ids) - len(original_seed_input_ids) == len(removed_report_ids)
    assert len(removed_report_ids) == 28

    for case in report["cases"]:
        assert case["codex_expected"]
        assert case["promotion_allowed"] is False
        assert case["confidence"] in {"high", "medium"}
        assert case["issue_tags"]
        assert case["rationale"]


def test_gemini_holdout_advisory_is_independent_and_advisory_only() -> None:
    inputs = load_json(INPUTS)
    report = load_json(GEMINI_ADVISORY)

    input_ids = [case["id"] for case in inputs["cases"]]
    comparison_ids = [case["id"] for case in report["comparisons"]]
    review_ids = [case["id"] for case in report["review"]["cases"]]
    original_seed_input_ids = original_seed_ids_from_report(comparison_ids, input_ids)
    removed_ids = load_all_removed_case_ids()
    removed_comparison_ids = set(comparison_ids) & removed_ids
    removed_review_ids = set(review_ids) & removed_ids

    assert report["reviewer"] == "gemini_vertex"
    assert report["review_stage"] == "independent_holdout_expected_review"
    assert report["ground_truth"] is False
    assert report["promotion_allowed"] is False
    assert report["summary"]["total_cases"] == 100
    assert report["summary"]["exact_matches_with_codex"] == 70
    assert report["summary"]["differences_from_codex"] == 30
    assert report["summary"]["needs_maintainer_review"] == 59
    assert report["summary"]["by_gemini_confidence"] == {"high": 100}
    assert [case_id for case_id in comparison_ids if case_id not in removed_ids] == (
        original_seed_input_ids
    )
    assert [case_id for case_id in review_ids if case_id not in removed_ids] == (
        original_seed_input_ids
    )
    assert len(comparison_ids) - len(original_seed_input_ids) == len(removed_comparison_ids)
    assert len(review_ids) - len(original_seed_input_ids) == len(removed_review_ids)
    assert len(removed_comparison_ids) == 28
    assert len(removed_review_ids) == 28

    for case in report["review"]["cases"]:
        assert case["expected"]
        assert case["confidence"] == "high"
        assert case["issue_tags"]
        assert case["notes"]


def test_codex_gemini_diff_review_lists_maintainer_queue() -> None:
    review = load_json(CODEX_GEMINI_DIFF_REVIEW)

    assert review["review_stage"] == "codex_gemini_difference_review"
    assert review["ground_truth"] is False
    assert review["promotion_allowed"] is False
    assert review["summary"] == {
        "total_cases": 100,
        "exact_matches": 70,
        "differences": 30,
        "exact_but_policy_review": 29,
        "no_immediate_question": 41,
        "maintainer_queue_total": 59,
        "difference_recommendations": {
            "codex": 24,
            "gemini": 5,
            "third_value": 1,
        },
        "promotion_allowed": False,
    }
    assert len(review["differences"]) == 30
    assert len(review["exact_but_policy_review"]) == 29
    assert len(review["no_immediate_question"]) == 41

    recommendations = {case["id"]: case["codex_recommendation"] for case in review["differences"]}
    assert recommendations["blind-it-0009"] == "gemini"
    assert recommendations["blind-llm-0013"] == "third_value"
    assert recommendations["blind-formal-0012"] == "codex"


def test_maintainer_confirmation_packet_is_not_ground_truth() -> None:
    packet = load_json(MAINTAINER_CONFIRMATION)

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["summary"] == {
        "total_review_cases": 59,
        "difference_cases": 30,
        "policy_review_cases": 29,
        "no_immediate_question": 41,
        "difference_recommendations": {
            "codex": 24,
            "gemini": 5,
            "third_value": 1,
        },
        "promotion_allowed": False,
    }
    assert len(packet["cases"]) == 59
    assert len(packet["no_immediate_question"]) == 41

    difference_cases = [case for case in packet["cases"] if case["kind"] == "difference"]
    policy_cases = [case for case in packet["cases"] if case["kind"] == "policy_review"]
    assert len(difference_cases) == 30
    assert len(policy_cases) == 29
    assert {case["maintainer_action"] for case in difference_cases} == {"confirm_or_edit"}
    assert {case["maintainer_action"] for case in policy_cases} == {"quick_confirm_or_edit"}
    assert all(case["recommended_expected"] for case in packet["cases"])


def test_maintainer_final_decision_summary_does_not_publish_expected_values() -> None:
    decision = load_json(FINAL_DECISION)

    assert decision["review_stage"] == "maintainer_final_decision_summary"
    assert decision["expected_values_included"] is False
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["summary"]["cases"] == 100
    assert decision["summary"]["status"] == "sealed_private"
    assert decision["summary"]["approval_policy"] == "single_human_with_ai_advisory"
    assert decision["summary"]["minimum_human_reviewers"] == 1
    assert decision["summary"]["ai_advisory_review_allowed"] is True
    assert decision["summary"]["by_expected_source"] == {
        "human_adjudication": 30,
        "human_first_pass": 70,
    }
    assert decision["summary"]["by_disagreement"] == {
        "false": 70,
        "true": 30,
    }
    assert "cases" not in decision


def test_private_benchmark_sanity_summary_omits_rows_and_expected_values() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["expected_values_included"] is False
    assert sanity["rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert sanity["summary"]["case_count"] == 256
    assert sanity["summary"]["accepted"] == 216
    assert sanity["summary"]["misses"] == 40
    assert sanity["summary"]["primary_exact"] == 184
    assert sanity["summary"]["acceptable_exact"] == 32
    assert sanity["summary"]["accepted_accuracy"] == 0.84375
    assert sanity["summary"]["primary_exact_accuracy"] == 0.71875
    assert sanity["summary"]["idempotency_rate"] == 0.98828125
    assert sanity["summary"]["accepted_accuracy_ci_95"] == {
        "low": 0.796875,
        "high": 0.88671875,
    }
    assert sanity["summary"]["by_domain"]["formal"]["accepted_accuracy"] == 0.8292682926829268
    assert sanity["summary"]["by_domain"]["high_risk"]["accepted_accuracy"] == 0.9230769230769231
    assert sanity["summary"]["by_domain"]["it"]["accepted_accuracy"] == 0.82
    assert sanity["summary"]["by_domain"]["llm"]["accepted_accuracy"] == 0.8837209302325582
    assert sanity["summary"]["by_domain"]["social"]["accepted_accuracy"] == 0.7954545454545454
    assert sanity["summary"]["by_domain"]["ui"]["accepted_accuracy"] == 0.8461538461538461
    assert sanity["summary"]["misses_by_risk"] == {
        "baseline_guard": 2,
        "candidate_gap": 19,
        "over_conversion_guard": 19,
    }
    assert sanity["summary"]["misses_by_issue_tag"] == {
        "formal_term": 10,
        "high_risk_term": 2,
        "it_term": 12,
        "over_conversion": 19,
        "regional_term": 40,
        "ui_term": 8,
    }


def test_private_benchmark_sanity_after_remaining_40_final_review_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_REMAINING_40_FINAL_REVIEW)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_remaining_40_final_review"
    assert sanity["expected_values_included"] is False
    assert sanity["rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert sanity["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "aggregate_statistics_only": True,
    }
    assert sanity["summary"]["case_count"] == 238
    assert sanity["summary"]["accepted"] == 219
    assert sanity["summary"]["misses"] == 19
    assert sanity["summary"]["primary_exact"] == 184
    assert sanity["summary"]["acceptable_exact"] == 35
    assert sanity["summary"]["accepted_accuracy"] == 0.9201680672268907
    assert sanity["summary"]["primary_exact_accuracy"] == 0.773109243697479
    assert sanity["summary"]["idempotency_rate"] == 0.9957983193277311
    assert sanity["summary"]["accepted_accuracy_ci_95"] == {
        "low": 0.8823529411764706,
        "high": 0.9537815126050421,
    }
    assert sanity["summary"]["by_domain"]["formal"]["accepted_accuracy"] == (0.8717948717948718)
    assert sanity["summary"]["by_domain"]["high_risk"]["accepted_accuracy"] == (0.9230769230769231)
    assert sanity["summary"]["by_domain"]["it"]["accepted_accuracy"] == (0.9767441860465116)
    assert sanity["summary"]["by_domain"]["llm"]["accepted_accuracy"] == (0.9047619047619048)
    assert sanity["summary"]["by_domain"]["social"]["accepted_accuracy"] == 0.875
    assert sanity["summary"]["by_domain"]["ui"]["accepted_accuracy"] == (0.9583333333333334)
    assert sanity["summary"]["misses_by_risk"] == {"over_conversion_guard": 19}
    assert sanity["summary"]["misses_by_issue_tag"] == {
        "formal_term": 7,
        "high_risk_term": 2,
        "it_term": 3,
        "over_conversion": 19,
        "regional_term": 19,
        "ui_term": 2,
    }


def test_holdout_miss_classification_omits_sealed_rows_and_values() -> None:
    report = load_json(MISS_CLASSIFICATION)

    assert report["report_type"] == "holdout_miss_classification"
    assert report["dataset"] == "blind-v1"
    assert report["source_benchmark"]["in_repo"] is False
    assert report["sealed_content_policy"] == {
        "expected_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "case_classifications_include_only_ids_and_metadata": True,
    }
    assert "rows" not in report
    assert "inputs" not in report

    summary = report["summary"]
    assert summary["case_count"] == 100
    assert summary["accepted"] == 57
    assert summary["misses"] == 43
    assert summary["by_action"] == {
        "move_to_public_regression_candidate": 22,
        "keep_as_holdout_signal": 7,
        "requires_expected_recheck": 14,
    }
    assert summary["by_domain_action"]["it"] == {
        "move_to_public_regression_candidate": 11,
        "keep_as_holdout_signal": 1,
        "requires_expected_recheck": 5,
    }
    assert summary["by_domain_action"]["ui"] == {
        "move_to_public_regression_candidate": 6,
        "keep_as_holdout_signal": 3,
        "requires_expected_recheck": 3,
    }
    assert summary["idempotency_followup_misses"] == 5
    assert summary["accepted_non_idempotent"] == 1

    forbidden_case_fields = {
        "acceptable",
        "annotation",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    cases = report["case_classifications"]
    assert len(cases) == 43
    assert len({case["id"] for case in cases}) == len(cases)
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["id"].startswith("blind-")
        assert case["action"] in summary["by_action"]
        assert case["reason_category"]
        assert case["next_step"]

    move_ids = {
        case["id"] for case in cases if case["action"] == "move_to_public_regression_candidate"
    }
    recheck_ids = {case["id"] for case in cases if case["action"] == "requires_expected_recheck"}
    holdout_ids = {case["id"] for case in cases if case["action"] == "keep_as_holdout_signal"}
    assert {"blind-it-0002", "blind-ui-0020", "blind-formal-0003"} <= move_ids
    assert {"blind-llm-0002", "blind-formal-0012"} <= recheck_ids
    assert {"blind-ui-0011", "blind-social-0015"} <= holdout_ids
    assert report["idempotency_notes"]["non_idempotent_miss_ids"] == [
        "blind-it-0023",
        "blind-ui-0002",
        "blind-ui-0019",
        "blind-formal-0003",
        "blind-social-0005",
    ]
    assert report["idempotency_notes"]["accepted_non_idempotent_ids"] == ["blind-formal-0015"]


def test_holdout_expected_recheck_summary_omits_sealed_values() -> None:
    report = load_json(EXPECTED_RECHECK)

    assert report["report_type"] == "holdout_expected_recheck_summary"
    assert report["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "case_decisions_include_only_ids_and_metadata": True,
    }
    assert report["private_expected_update"]["updated"] is True
    assert report["private_expected_update"]["acceptable_variants_added"] == 12
    assert report["summary"] == {
        "recheck_cases": 14,
        "add_acceptable_variant": 12,
        "keep_strict_primary_expected": 2,
        "move_to_public_regression_candidate": 0,
        "accepted_before_recheck": 57,
        "accepted_after_recheck": 69,
        "misses_before_recheck": 21,
        "misses_after_recheck": 9,
        "accepted_accuracy_after_recheck": 0.8846153846153846,
        "idempotency_rate_after_recheck": 0.9743589743589743,
        "by_domain_decision": {
            "formal": {
                "add_acceptable_variant": 1,
                "keep_strict_primary_expected": 1,
            },
            "it": {"add_acceptable_variant": 5},
            "llm": {"add_acceptable_variant": 4},
            "ui": {
                "add_acceptable_variant": 2,
                "keep_strict_primary_expected": 1,
            },
        },
    }
    assert "rows" not in report
    assert "inputs" not in report

    forbidden_case_fields = {
        "acceptable",
        "actual",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    decisions = report["case_decisions"]
    assert len(decisions) == 14
    assert len({case["id"] for case in decisions}) == len(decisions)
    for case in decisions:
        assert not (forbidden_case_fields & set(case))
        assert case["expected_values_included"] is False
        assert case["acceptable_values_included"] is False
        assert case["actual_outputs_included"] is False

    decision_by_id = {case["id"]: case["decision"] for case in decisions}
    assert decision_by_id["blind-it-0003"] == "add_acceptable_variant"
    assert decision_by_id["blind-llm-0012"] == "add_acceptable_variant"
    assert decision_by_id["blind-formal-0012"] == "add_acceptable_variant"
    assert decision_by_id["blind-ui-0002"] == "keep_strict_primary_expected"
    assert decision_by_id["blind-formal-0010"] == "keep_strict_primary_expected"


def test_holdout_remaining_miss_classification_omits_sealed_values() -> None:
    report = load_json(REMAINING_MISS_CLASSIFICATION)
    inputs = load_json(INPUTS)
    input_ids = {case["id"] for case in inputs["cases"]}
    batch2_removed_ids = set(load_json(SEALED_POOL_UPDATE_BATCH2)["removed_case_ids"])
    batch3_removed_ids = set(load_json(SEALED_POOL_UPDATE_BATCH3)["removed_case_ids"])

    assert report["report_type"] == "holdout_remaining_miss_classification"
    assert report["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "case_classifications_include_only_ids_and_metadata": True,
    }
    assert report["summary"] == {
        "current_sealed_cases": 78,
        "current_accepted": 69,
        "current_misses": 9,
        "classified_misses": 9,
        "by_action": {
            "move_to_public_regression_candidate": 5,
            "keep_as_holdout_signal": 4,
        },
        "by_priority": {"P1": 3, "P2": 6},
        "by_domain_action": {
            "formal": {
                "move_to_public_regression_candidate": 2,
                "keep_as_holdout_signal": 1,
            },
            "it": {
                "move_to_public_regression_candidate": 1,
                "keep_as_holdout_signal": 0,
            },
            "social": {
                "move_to_public_regression_candidate": 1,
                "keep_as_holdout_signal": 0,
            },
            "ui": {
                "move_to_public_regression_candidate": 1,
                "keep_as_holdout_signal": 3,
            },
        },
        "by_risk_action": {
            "baseline_guard": {
                "move_to_public_regression_candidate": 0,
                "keep_as_holdout_signal": 2,
            },
            "candidate_gap": {
                "move_to_public_regression_candidate": 5,
                "keep_as_holdout_signal": 2,
            },
        },
        "idempotency_followup_cases": 1,
        "strict_after_expected_recheck_cases": 2,
    }
    assert "rows" not in report
    assert "inputs" not in report

    forbidden_case_fields = {
        "acceptable",
        "actual",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    cases = report["case_classifications"]
    assert len(cases) == 9
    assert len({case["id"] for case in cases}) == len(cases)
    assert {case["id"] for case in cases} <= input_ids | batch2_removed_ids | batch3_removed_ids
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["action"] in report["summary"]["by_action"]
        assert case["next_step"]

    action_by_id = {case["id"]: case["action"] for case in cases}
    assert {
        case_id
        for case_id, action in action_by_id.items()
        if action == "move_to_public_regression_candidate"
    } == batch2_removed_ids
    assert action_by_id == {
        "blind-it-0014": "move_to_public_regression_candidate",
        "blind-ui-0002": "move_to_public_regression_candidate",
        "blind-ui-0011": "keep_as_holdout_signal",
        "blind-ui-0014": "keep_as_holdout_signal",
        "blind-ui-0016": "keep_as_holdout_signal",
        "blind-formal-0005": "keep_as_holdout_signal",
        "blind-formal-0006": "move_to_public_regression_candidate",
        "blind-formal-0010": "move_to_public_regression_candidate",
        "blind-social-0015": "move_to_public_regression_candidate",
    }

    flags_by_id = {case["id"]: set(case["flags"]) for case in cases}
    assert flags_by_id["blind-ui-0002"] == {
        "idempotency_followup",
        "strict_after_expected_recheck",
    }
    assert flags_by_id["blind-formal-0010"] == {"strict_after_expected_recheck"}


def test_holdout_200_case_miss_classification_omits_sealed_values() -> None:
    report = load_json(MISS_CLASSIFICATION_200_CASE)

    assert report["report_type"] == "holdout_miss_classification_200_case_sanity"
    assert report["review_stage"] == "private_miss_classification_first_pass"
    assert report["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "case_classifications_include_only_ids_and_metadata": True,
    }
    assert report["gemini_review_policy"] == {
        "status": "completed_on_sanitized_metadata",
        "review_report": (
            "docs/reports/"
            "holdout-gemini-policy-review-miss-classification-blind-v1-200-cases-2026-07-09.json"
        ),
        "sealed_values_seen_by_gemini": False,
        "policy_consistent": True,
        "needs_codex_followup": 0,
        "reason": (
            "Gemini reviewed case ids and classification metadata only; private expected, "
            "inputs, and converter outputs were not sent."
        ),
    }
    assert report["summary"] == {
        "current_sealed_cases": 200,
        "current_accepted": 144,
        "current_misses": 56,
        "classified_misses": 56,
        "by_action": {
            "keep_as_holdout_signal": 6,
            "move_to_public_regression_candidate": 39,
            "requires_expected_recheck": 11,
        },
        "by_priority": {"P1": 28, "P2": 27, "P3": 1},
        "by_domain_action": {
            "formal": {
                "keep_as_holdout_signal": 1,
                "move_to_public_regression_candidate": 4,
                "requires_expected_recheck": 1,
            },
            "high_risk": {
                "move_to_public_regression_candidate": 2,
                "requires_expected_recheck": 2,
            },
            "it": {
                "move_to_public_regression_candidate": 22,
                "requires_expected_recheck": 2,
            },
            "llm": {
                "keep_as_holdout_signal": 2,
                "move_to_public_regression_candidate": 2,
                "requires_expected_recheck": 2,
            },
            "social": {
                "keep_as_holdout_signal": 2,
                "move_to_public_regression_candidate": 1,
                "requires_expected_recheck": 1,
            },
            "ui": {
                "keep_as_holdout_signal": 1,
                "move_to_public_regression_candidate": 8,
                "requires_expected_recheck": 3,
            },
        },
        "by_risk_action": {
            "baseline_guard": {
                "keep_as_holdout_signal": 1,
                "move_to_public_regression_candidate": 5,
            },
            "candidate_gap": {
                "move_to_public_regression_candidate": 26,
                "requires_expected_recheck": 9,
            },
            "over_conversion_guard": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 8,
                "requires_expected_recheck": 2,
            },
        },
        "idempotency_followup_cases": 4,
        "expected_recheck_cases": 11,
        "safe_public_candidate_cases": 39,
        "holdout_signal_cases": 6,
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
    cases = report["case_classifications"]
    assert len(cases) == 56
    assert len({case["id"] for case in cases}) == len(cases)
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["id"].startswith("blind-")
        assert case["action"] in report["summary"]["by_action"]
        assert case["reason_category"]
        assert case["next_step"]

    action_by_id = {case["id"]: case["action"] for case in cases}
    assert action_by_id["blind-it-0026"] == "move_to_public_regression_candidate"
    assert action_by_id["blind-it-0055"] == "requires_expected_recheck"
    assert action_by_id["blind-llm-0026"] == "keep_as_holdout_signal"
    assert action_by_id["blind-high-risk-0016"] == "move_to_public_regression_candidate"
    assert report["idempotency_notes"]["non_idempotent_miss_ids"] == [
        "blind-it-0034",
        "blind-ui-0040",
        "blind-formal-0025",
        "blind-social-0019",
    ]


def test_gemini_200_case_miss_classification_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_MISS_CLASSIFICATION_POLICY_REVIEW)

    assert review["reviewer"] == "gemini_vertex"
    assert review["model"] == "gemini-2.5-flash"
    assert review["review_stage"] == "sanitized_miss_classification_policy_review"
    assert review["sealed_values_seen"] is False
    assert review["source_classification_report"] == (
        "docs/reports/holdout-miss-classification-blind-v1-200-cases-2026-07-09.json"
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
        "total_cases": 56,
        "policy_consistent": True,
        "needs_codex_followup": 0,
    }
    assert review["findings"] == []
    assert "cases" not in review


def test_holdout_261_case_miss_classification_omits_sealed_values() -> None:
    report = load_json(MISS_CLASSIFICATION_261_CASE)

    assert report["report_type"] == "holdout_miss_classification_261_case_sanity"
    assert report["review_stage"] == "private_miss_classification_first_pass"
    assert report["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "case_classifications_include_only_ids_and_metadata": True,
    }
    assert report["gemini_review_policy"] == {
        "status": "completed_on_sanitized_metadata",
        "review_report": (
            "docs/reports/"
            "holdout-gemini-policy-review-miss-classification-blind-v1-261-cases-2026-07-09.json"
        ),
        "sealed_values_seen_by_gemini": False,
        "policy_consistent": True,
        "needs_codex_followup": 0,
        "reason": (
            "Gemini reviewed case ids and classification metadata only; private expected, "
            "inputs, and converter outputs were not sent."
        ),
    }
    assert report["codex_followup"] == {
        "status": "revised_after_gemini_policy_findings",
        "revised_case_ids": [
            "blind-high-risk-0028",
            "blind-high-risk-0030",
            "blind-it-0080",
            "blind-it-0081",
            "blind-it-0082",
            "blind-it-0084",
            "blind-llm-0042",
        ],
        "reason": (
            "Gemini policy review flagged over-conversion guard and high-risk cases as "
            "insufficiently conservative for direct move-to-public classification; Codex "
            "changed them to requires_expected_recheck."
        ),
    }
    assert report["summary"] == {
        "current_sealed_cases": 261,
        "current_accepted": 207,
        "current_misses": 54,
        "classified_misses": 54,
        "by_action": {
            "keep_as_holdout_signal": 20,
            "move_to_public_regression_candidate": 18,
            "requires_expected_recheck": 16,
        },
        "by_priority": {"P1": 19, "P2": 34, "P3": 1},
        "by_domain_action": {
            "formal": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 1,
                "requires_expected_recheck": 3,
            },
            "high_risk": {
                "keep_as_holdout_signal": 2,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 4,
            },
            "it": {
                "keep_as_holdout_signal": 1,
                "move_to_public_regression_candidate": 8,
                "requires_expected_recheck": 5,
            },
            "llm": {
                "keep_as_holdout_signal": 4,
                "move_to_public_regression_candidate": 1,
                "requires_expected_recheck": 2,
            },
            "social": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 4,
                "requires_expected_recheck": 0,
            },
            "ui": {
                "keep_as_holdout_signal": 3,
                "move_to_public_regression_candidate": 4,
                "requires_expected_recheck": 2,
            },
        },
        "by_risk_action": {
            "baseline_guard": {
                "keep_as_holdout_signal": 1,
                "move_to_public_regression_candidate": 1,
                "requires_expected_recheck": 2,
            },
            "candidate_gap": {
                "keep_as_holdout_signal": 0,
                "move_to_public_regression_candidate": 17,
                "requires_expected_recheck": 8,
            },
            "over_conversion_guard": {
                "keep_as_holdout_signal": 19,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 6,
            },
        },
        "idempotency_followup_cases": 2,
        "expected_recheck_cases": 16,
        "safe_public_candidate_cases": 18,
        "holdout_signal_cases": 20,
        "high_risk_cases": 6,
        "over_conversion_guard_cases": 25,
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
    cases = report["case_classifications"]
    assert len(cases) == 54
    assert len({case["id"] for case in cases}) == len(cases)
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["id"].startswith("blind-")
        assert case["action"] in report["summary"]["by_action"]
        assert case["reason_category"]
        assert case["next_step"]

    action_by_id = {case["id"]: case["action"] for case in cases}
    assert action_by_id["blind-it-0063"] == "move_to_public_regression_candidate"
    assert action_by_id["blind-it-0080"] == "requires_expected_recheck"
    assert action_by_id["blind-high-risk-0030"] == "requires_expected_recheck"
    assert action_by_id["blind-social-0042"] == "keep_as_holdout_signal"

    assert report["idempotency_notes"]["non_idempotent_miss_ids"] == [
        "blind-it-0070",
        "blind-social-0034",
    ]


def test_gemini_261_case_miss_classification_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_MISS_CLASSIFICATION_261_POLICY_REVIEW)

    assert review["reviewer"] == "gemini_vertex"
    assert review["model"] == "gemini-2.5-flash"
    assert review["review_stage"] == "sanitized_miss_classification_policy_review"
    assert review["sealed_values_seen"] is False
    assert review["source_classification_report"] == (
        "docs/reports/holdout-miss-classification-blind-v1-261-cases-2026-07-09.json"
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
        "total_cases": 54,
        "policy_consistent": True,
        "needs_codex_followup": 0,
    }
    assert review["findings"] == []
    assert "cases" not in review


def test_private_benchmark_sanity_after_batch5_covers_338_cases() -> None:
    report = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH5)
    final_decision = load_json(MAINTAINER_BATCH5_FINAL_DECISION)

    assert report["dataset"] == "blind-v1"
    assert report["summary"]["case_count"] == 338
    assert report["report_mode"] == "aggregate"
    assert report["dataset_classification"] == "published_evaluation"
    assert report["expected_sha256"] == final_decision["private_expected_sha256"]
    assert report["engines"]["zhtw"]["scores"]["total_cases"] == 338
    assert report["engines"]["zhtw"]["scores"]["accepted"] == 301
    assert report["engines"]["zhtw"]["scores"]["misses"] == 37
    assert round(report["engines"]["zhtw"]["scores"]["accepted_accuracy"], 4) == 0.8905
    assert "rows" not in report
    assert "expected" not in report


def test_private_benchmark_sanity_after_338_miss_review_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_338_MISS_REVIEW)
    final_decision = load_json(MAINTAINER_338_MISS_FINAL_DECISION)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_338_miss_review"
    assert sanity["expected_values_included"] is False
    assert sanity["rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert sanity["source_benchmark"] == {
        "path": "/tmp/zhtw-blind-v1-private-benchmark-after-338-miss-review-2026-07-09.json",
        "in_repo": False,
        "rows_used_for_aggregate_only": True,
    }
    assert sanity["inputs"]["path"] == "benchmarks/accuracy/blind-v1.inputs.json"
    assert sanity["inputs"]["sha256"] == (
        "2d69cf2ceb90dff8b41e9806cfe7c642d8e3e64947ea83045a8fd41be705a5a2"
    )
    assert sanity["expected"]["path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert sanity["expected"]["sha256"] == final_decision["private_expected_sha256_after"]
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "aggregate_statistics_only": True,
    }
    assert sanity["summary"]["case_count"] == 326
    assert sanity["summary"]["accepted"] == 304
    assert sanity["summary"]["misses"] == 22
    assert sanity["summary"]["primary_exact"] == 242
    assert sanity["summary"]["acceptable_exact"] == 62
    assert sanity["summary"]["accepted_accuracy"] == 0.9325153374233128
    assert sanity["summary"]["primary_exact_accuracy"] == 0.7423312883435583
    assert sanity["summary"]["idempotency_rate"] == 0.99079754601227
    assert sanity["summary"]["accepted_accuracy_ci_95"] == {
        "low": 0.9079754601226994,
        "high": 0.9601226993865031,
    }
    assert sanity["summary"]["by_domain"] == {
        "formal": {
            "total": 54,
            "accepted": 49,
            "accepted_accuracy": 0.9074074074074074,
        },
        "high_risk": {
            "total": 36,
            "accepted": 33,
            "accepted_accuracy": 0.9166666666666666,
        },
        "it": {
            "total": 61,
            "accepted": 59,
            "accepted_accuracy": 0.9672131147540983,
        },
        "llm": {
            "total": 56,
            "accepted": 52,
            "accepted_accuracy": 0.9285714285714286,
        },
        "social": {
            "total": 55,
            "accepted": 50,
            "accepted_accuracy": 0.9090909090909091,
        },
        "ui": {
            "total": 64,
            "accepted": 61,
            "accepted_accuracy": 0.953125,
        },
    }
    assert sanity["summary"]["by_risk"] == {
        "baseline_guard": 52,
        "candidate_gap": 186,
        "over_conversion_guard": 88,
    }
    assert sanity["summary"]["misses_by_risk"] == {"over_conversion_guard": 22}
    assert sanity["summary"]["misses_by_issue_tag"] == {
        "formal_term": 8,
        "high_risk_term": 3,
        "it_term": 4,
        "over_conversion": 22,
        "regional_term": 22,
        "ui_term": 3,
    }


def test_private_benchmark_sanity_after_batch6_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH6)
    final_decision = load_json(MAINTAINER_BATCH6_FINAL_DECISION)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch6_final_decision"
    assert sanity["expected_values_included"] is False
    assert sanity["rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert sanity["source_benchmark"] == {
        "path": "/tmp/zhtw-blind-v1-private-benchmark-after-batch6-2026-07-10.json",
        "in_repo": False,
        "rows_used_for_aggregate_only": True,
    }
    assert sanity["inputs"]["path"] == "benchmarks/accuracy/blind-v1.inputs.json"
    assert sanity["inputs"]["sha256"] == (
        "be3ab808d2f2bb71b1c86e66cd95eb182446693412c1ebbecdf5aa632f35d35e"
    )
    assert sanity["expected"]["path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert sanity["expected"]["sha256"] == final_decision["private_expected_sha256"]
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "aggregate_statistics_only": True,
    }
    assert sanity["summary"]["case_count"] == 426
    assert sanity["summary"]["accepted"] == 389
    assert sanity["summary"]["misses"] == 37
    assert sanity["summary"]["primary_exact"] == 308
    assert sanity["summary"]["acceptable_exact"] == 81
    assert sanity["summary"]["accepted_accuracy"] == 0.9131455399061033
    assert sanity["summary"]["primary_exact_accuracy"] == 0.7230046948356808
    assert sanity["summary"]["idempotency_rate"] == 0.9859154929577465
    assert sanity["summary"]["accepted_accuracy_ci_95"] == {
        "low": 0.8873239436619719,
        "high": 0.9413145539906104,
    }
    assert sanity["summary"]["by_domain"] == {
        "formal": {
            "total": 69,
            "accepted": 64,
            "accepted_accuracy": 0.927536231884058,
        },
        "high_risk": {
            "total": 46,
            "accepted": 43,
            "accepted_accuracy": 0.9347826086956522,
        },
        "it": {
            "total": 86,
            "accepted": 73,
            "accepted_accuracy": 0.8488372093023255,
        },
        "llm": {
            "total": 71,
            "accepted": 66,
            "accepted_accuracy": 0.9295774647887324,
        },
        "social": {
            "total": 70,
            "accepted": 65,
            "accepted_accuracy": 0.9285714285714286,
        },
        "ui": {
            "total": 84,
            "accepted": 78,
            "accepted_accuracy": 0.9285714285714286,
        },
    }
    assert sanity["summary"]["by_risk"] == {
        "baseline_guard": 67,
        "candidate_gap": 246,
        "over_conversion_guard": 113,
    }
    assert sanity["summary"]["misses_by_risk"] == {
        "baseline_guard": 1,
        "candidate_gap": 12,
        "over_conversion_guard": 24,
    }
    assert sanity["summary"]["misses_by_issue_tag"] == {
        "formal_term": 8,
        "high_risk_term": 3,
        "it_term": 16,
        "over_conversion": 24,
        "regional_term": 37,
        "ui_term": 6,
    }


def test_private_benchmark_sanity_after_batch6_miss_review_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH6_MISS_REVIEW)
    final_decision = load_json(MAINTAINER_BATCH6_MISS_FINAL_DECISION)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch6_miss_review"
    assert sanity["expected_values_included"] is False
    assert sanity["rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert sanity["source_benchmark"] == {
        "path": "/tmp/zhtw-blind-v1-private-benchmark-after-batch6-miss-review-2026-07-10.json",
        "in_repo": False,
        "rows_used_for_aggregate_only": True,
    }
    assert sanity["inputs"]["path"] == "benchmarks/accuracy/blind-v1.inputs.json"
    assert sanity["inputs"]["sha256"] == (
        "18153aa5d4bafad940734bf19754d1948f4a9562979e7c668ecf855c1c683a20"
    )
    assert sanity["inputs"]["sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert sanity["expected"]["path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert sanity["expected"]["sha256"] == final_decision["private_expected_sha256_after"]
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "aggregate_statistics_only": True,
    }
    assert sanity["summary"]["case_count"] == 415
    assert sanity["summary"]["accepted"] == 391
    assert sanity["summary"]["misses"] == 24
    assert sanity["summary"]["primary_exact"] == 308
    assert sanity["summary"]["acceptable_exact"] == 83
    assert sanity["summary"]["accepted_accuracy"] == 0.9421686746987952
    assert sanity["summary"]["primary_exact_accuracy"] == 0.7421686746987952
    assert sanity["summary"]["idempotency_rate"] == 0.9879518072289156
    assert sanity["summary"]["accepted_accuracy_ci_95"] == {
        "low": 0.9180722891566265,
        "high": 0.963855421686747,
    }
    assert sanity["summary"]["by_domain"] == {
        "formal": {
            "total": 69,
            "accepted": 64,
            "accepted_accuracy": 0.927536231884058,
        },
        "high_risk": {
            "total": 46,
            "accepted": 43,
            "accepted_accuracy": 0.9347826086956522,
        },
        "it": {
            "total": 76,
            "accepted": 73,
            "accepted_accuracy": 0.9605263157894737,
        },
        "llm": {
            "total": 71,
            "accepted": 67,
            "accepted_accuracy": 0.9436619718309859,
        },
        "social": {
            "total": 70,
            "accepted": 65,
            "accepted_accuracy": 0.9285714285714286,
        },
        "ui": {
            "total": 83,
            "accepted": 79,
            "accepted_accuracy": 0.9518072289156626,
        },
    }
    assert sanity["summary"]["by_risk"] == {
        "baseline_guard": 66,
        "candidate_gap": 236,
        "over_conversion_guard": 113,
    }
    assert sanity["summary"]["misses_by_risk"] == {"over_conversion_guard": 24}
    assert sanity["summary"]["misses_by_issue_tag"] == {
        "formal_term": 8,
        "high_risk_term": 3,
        "it_term": 5,
        "over_conversion": 24,
        "regional_term": 24,
        "ui_term": 4,
    }


def test_private_benchmark_sanity_after_batch7_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH7)
    final_decision = load_json(MAINTAINER_BATCH7_FINAL_DECISION)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch7_final_decision"
    assert sanity["expected_values_included"] is False
    assert sanity["rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert sanity["source_benchmark"] == {
        "path": "/tmp/zhtw-blind-v1-private-benchmark-after-batch7-2026-07-10.json",
        "in_repo": False,
        "rows_used_for_aggregate_only": True,
    }
    assert sanity["inputs"]["path"] == "benchmarks/accuracy/blind-v1.inputs.json"
    assert sanity["inputs"]["sha256"] == (
        "27a3ec40cf4f5df586524d3ec307f3fcbf164a1e1ece097cc8637cd484cb5dc1"
    )
    assert sanity["inputs"]["sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert sanity["expected"]["path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert sanity["expected"]["sha256"] == final_decision["private_expected_sha256"]
    assert sanity["expected"]["sha256"] != private_expected_sha256()
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "aggregate_statistics_only": True,
    }
    assert sanity["summary"]["case_count"] == 515
    assert sanity["summary"]["accepted"] == 465
    assert sanity["summary"]["misses"] == 50
    assert sanity["summary"]["primary_exact"] == 370
    assert sanity["summary"]["acceptable_exact"] == 95
    assert sanity["summary"]["accepted_accuracy"] == 0.9029126213592233
    assert sanity["summary"]["primary_exact_accuracy"] == 0.7184466019417476
    assert sanity["summary"]["idempotency_rate"] == 0.9786407766990292
    assert sanity["summary"]["accepted_accuracy_ci_95"] == {
        "low": 0.8776699029126214,
        "high": 0.9281553398058252,
    }
    assert sanity["summary"]["by_domain"] == {
        "formal": {
            "total": 84,
            "accepted": 78,
            "accepted_accuracy": 0.9285714285714286,
        },
        "high_risk": {
            "total": 56,
            "accepted": 51,
            "accepted_accuracy": 0.9107142857142857,
        },
        "it": {
            "total": 101,
            "accepted": 83,
            "accepted_accuracy": 0.8217821782178217,
        },
        "llm": {
            "total": 86,
            "accepted": 80,
            "accepted_accuracy": 0.9302325581395349,
        },
        "social": {
            "total": 85,
            "accepted": 79,
            "accepted_accuracy": 0.9294117647058824,
        },
        "ui": {
            "total": 103,
            "accepted": 94,
            "accepted_accuracy": 0.912621359223301,
        },
    }
    assert sanity["summary"]["by_risk"] == {
        "baseline_guard": 81,
        "candidate_gap": 296,
        "over_conversion_guard": 138,
    }
    assert sanity["summary"]["misses_by_risk"] == {
        "baseline_guard": 2,
        "candidate_gap": 23,
        "over_conversion_guard": 25,
    }
    assert sanity["summary"]["misses_by_issue_tag"] == {
        "formal_term": 9,
        "high_risk_term": 5,
        "it_term": 20,
        "over_conversion": 25,
        "regional_term": 50,
        "ui_term": 9,
    }


def test_private_benchmark_sanity_after_batch7_miss_review_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH7_MISS_REVIEW)
    final_decision = load_json(MAINTAINER_BATCH7_MISS_FINAL_DECISION)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch7_miss_review"
    assert sanity["expected_values_included"] is False
    assert sanity["rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert sanity["source_benchmark"] == {
        "path": "/tmp/zhtw-blind-v1-private-benchmark-after-batch7-miss-review-2026-07-10.json",
        "in_repo": False,
        "rows_used_for_aggregate_only": True,
    }
    assert sanity["inputs"]["sha256"] == (
        "d331a1a2d6c58774089ca723677ec77ca4abe05e1eb11298ca8a5700b6a1cbcd"
    )
    assert sanity["inputs"]["sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert sanity["expected"]["sha256"] == final_decision["private_expected_sha256_after"]
    assert sanity["expected"]["sha256"] != private_expected_sha256()
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "aggregate_statistics_only": True,
    }
    assert sanity["summary"]["case_count"] == 498
    assert sanity["summary"]["accepted"] == 472
    assert sanity["summary"]["misses"] == 26
    assert sanity["summary"]["primary_exact"] == 370
    assert sanity["summary"]["acceptable_exact"] == 102
    assert sanity["summary"]["accepted_accuracy"] == 0.9477911646586346
    assert sanity["summary"]["primary_exact_accuracy"] == 0.7429718875502008
    assert sanity["summary"]["idempotency_rate"] == 0.9879518072289156
    assert sanity["summary"]["accepted_accuracy_ci_95"] == {
        "low": 0.927710843373494,
        "high": 0.9658634538152611,
    }
    assert sanity["summary"]["by_risk"] == {
        "baseline_guard": 79,
        "candidate_gap": 281,
        "over_conversion_guard": 138,
    }
    assert sanity["summary"]["misses_by_risk"] == {
        "candidate_gap": 1,
        "over_conversion_guard": 25,
    }


def test_private_benchmark_sanity_after_batch8_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH8)
    final_decision = load_json(MAINTAINER_BATCH8_FINAL_DECISION)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch8"
    assert sanity["expected_values_included"] is False
    assert sanity["rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert sanity["source_benchmark"] == {
        "path": "/tmp/zhtw-blind-v1-private-benchmark-after-batch8-2026-07-10.json",
        "in_repo": False,
        "rows_used_for_aggregate_only": True,
    }
    assert sanity["inputs"]["sha256"] == (
        "287b30b7d08ac7761fc78624e8db5f9f9d2664a214feef6b06dfe401cdd719cb"
    )
    assert sanity["inputs"]["sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert sanity["expected"]["sha256"] == final_decision["private_expected_sha256"]
    assert sanity["expected"]["sha256"] != private_expected_sha256()
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "aggregate_statistics_only": True,
    }
    assert sanity["summary"]["case_count"] == 598
    assert sanity["summary"]["accepted"] == 549
    assert sanity["summary"]["misses"] == 49
    assert sanity["summary"]["primary_exact"] == 434
    assert sanity["summary"]["acceptable_exact"] == 115
    assert sanity["summary"]["accepted_accuracy"] == 0.9180602006688964
    assert sanity["summary"]["primary_exact_accuracy"] == 0.725752508361204
    assert sanity["summary"]["idempotency_rate"] == 0.9832775919732442
    assert sanity["summary"]["accepted_accuracy_ci_95"] == {
        "low": 0.8946488294314381,
        "high": 0.939799331103679,
    }
    assert sanity["summary"]["by_domain"] == {
        "formal": {
            "total": 98,
            "accepted": 91,
            "accepted_accuracy": 0.9285714285714286,
        },
        "high_risk": {
            "total": 66,
            "accepted": 59,
            "accepted_accuracy": 0.8939393939393939,
        },
        "it": {
            "total": 115,
            "accepted": 102,
            "accepted_accuracy": 0.8869565217391304,
        },
        "llm": {
            "total": 99,
            "accepted": 93,
            "accepted_accuracy": 0.9393939393939394,
        },
        "social": {
            "total": 99,
            "accepted": 93,
            "accepted_accuracy": 0.9393939393939394,
        },
        "ui": {
            "total": 121,
            "accepted": 111,
            "accepted_accuracy": 0.9173553719008265,
        },
    }
    assert sanity["summary"]["by_risk"] == {
        "baseline_guard": 94,
        "candidate_gap": 341,
        "over_conversion_guard": 163,
    }
    assert sanity["summary"]["misses_by_risk"] == {
        "baseline_guard": 1,
        "candidate_gap": 21,
        "over_conversion_guard": 27,
    }
    assert sanity["summary"]["misses_by_issue_tag"] == {
        "baseline_guard": 1,
        "candidate_gap": 20,
        "formal_term": 10,
        "high_risk_term": 7,
        "it_term": 15,
        "llm_term": 2,
        "over_conversion": 27,
        "regional_term": 49,
        "social_term": 1,
        "ui_term": 10,
    }


def test_private_benchmark_sanity_after_batch8_miss_review_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH8_MISS_REVIEW)
    final_decision = load_json(MAINTAINER_BATCH8_MISS_FINAL_DECISION)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch8_miss_review"
    assert sanity["expected_values_included"] is False
    assert sanity["rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert sanity["source_benchmark"] == {
        "path": "/tmp/zhtw-blind-v1-private-benchmark-after-batch8-miss-review-2026-07-11.json",
        "in_repo": False,
        "rows_used_for_aggregate_only": True,
    }
    assert sanity["inputs"]["sha256"] == (
        "96226f1fc747cc1d6ae9eb40793077a3a8bc8dc36b194491dc63c7cb26bd4450"
    )
    assert sanity["inputs"]["sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert sanity["expected"]["sha256"] == final_decision["private_expected_sha256_after"]
    assert sanity["expected"]["sha256"] != private_expected_sha256()
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "aggregate_statistics_only": True,
    }
    assert sanity["summary"]["case_count"] == 583
    assert sanity["summary"]["accepted"] == 553
    assert sanity["summary"]["misses"] == 30
    assert sanity["summary"]["primary_exact"] == 434
    assert sanity["summary"]["acceptable_exact"] == 119
    assert sanity["summary"]["accepted_accuracy"] == 0.9485420240137221
    assert sanity["summary"]["primary_exact_accuracy"] == 0.7444253859348199
    assert sanity["summary"]["idempotency_rate"] == 0.9845626072041166
    assert sanity["summary"]["accepted_accuracy_ci_95"] == {
        "low": 0.9296740994854202,
        "high": 0.9656946826758147,
    }
    assert sanity["summary"]["by_domain"] == {
        "formal": {
            "total": 97,
            "accepted": 91,
            "accepted_accuracy": 0.9381443298969072,
        },
        "high_risk": {
            "total": 66,
            "accepted": 59,
            "accepted_accuracy": 0.8939393939393939,
        },
        "it": {
            "total": 107,
            "accepted": 104,
            "accepted_accuracy": 0.9719626168224299,
        },
        "llm": {
            "total": 98,
            "accepted": 94,
            "accepted_accuracy": 0.9591836734693877,
        },
        "social": {
            "total": 99,
            "accepted": 94,
            "accepted_accuracy": 0.9494949494949495,
        },
        "ui": {
            "total": 116,
            "accepted": 111,
            "accepted_accuracy": 0.9568965517241379,
        },
    }
    assert sanity["summary"]["by_risk"] == {
        "baseline_guard": 94,
        "candidate_gap": 326,
        "over_conversion_guard": 163,
    }
    assert sanity["summary"]["misses_by_risk"] == {
        "baseline_guard": 1,
        "candidate_gap": 2,
        "over_conversion_guard": 27,
    }
    assert sanity["summary"]["misses_by_issue_tag"] == {
        "baseline_guard": 1,
        "candidate_gap": 1,
        "formal_term": 9,
        "high_risk_term": 7,
        "it_term": 5,
        "over_conversion": 27,
        "regional_term": 30,
        "ui_term": 5,
    }


def test_private_benchmark_sanity_after_batch9_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH9)
    final_decision = load_json(MAINTAINER_BATCH9_FINAL_DECISION)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch9_final_decision"
    assert sanity["expected_values_included"] is False
    assert sanity["rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert sanity["source_benchmark"] == {
        "path": "/tmp/zhtw-blind-v1-private-benchmark-after-batch9-2026-07-12.json",
        "in_repo": False,
        "rows_used_for_aggregate_only": True,
    }
    assert sanity["inputs"]["sha256"] == (
        "0ac742ac9885cdae198bed6fc376c2fb5c3e991573ae4cb4ac2072cfef3e937d"
    )
    assert sanity["inputs"]["sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert sanity["expected"]["sha256"] == final_decision["private_expected_sha256"]
    assert sanity["expected"]["sha256"] != private_expected_sha256()
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "aggregate_statistics_only": True,
    }
    assert sanity["summary"]["case_count"] == 683
    assert sanity["summary"]["accepted"] == 630
    assert sanity["summary"]["misses"] == 53
    assert sanity["summary"]["primary_exact"] == 491
    assert sanity["summary"]["acceptable_exact"] == 139
    assert sanity["summary"]["accepted_accuracy"] == 0.9224011713030746
    assert sanity["summary"]["primary_exact_accuracy"] == 0.718887262079063
    assert sanity["summary"]["idempotency_rate"] == 0.9809663250366032
    assert sanity["summary"]["accepted_accuracy_ci_95"] == {
        "low": 0.9019033674963397,
        "high": 0.9399707174231332,
    }
    assert sanity["summary"]["by_domain"] == {
        "formal": {
            "total": 112,
            "accepted": 104,
            "accepted_accuracy": 0.9285714285714286,
        },
        "high_risk": {
            "total": 76,
            "accepted": 69,
            "accepted_accuracy": 0.9078947368421053,
        },
        "it": {
            "total": 132,
            "accepted": 117,
            "accepted_accuracy": 0.8863636363636364,
        },
        "llm": {
            "total": 113,
            "accepted": 107,
            "accepted_accuracy": 0.9469026548672567,
        },
        "social": {
            "total": 114,
            "accepted": 108,
            "accepted_accuracy": 0.9473684210526315,
        },
        "ui": {
            "total": 136,
            "accepted": 125,
            "accepted_accuracy": 0.9191176470588235,
        },
    }
    assert sanity["summary"]["by_risk"] == {
        "baseline_guard": 109,
        "candidate_gap": 386,
        "over_conversion_guard": 188,
    }
    assert sanity["summary"]["misses_by_risk"] == {
        "baseline_guard": 3,
        "candidate_gap": 22,
        "over_conversion_guard": 28,
    }
    assert sanity["summary"]["misses_by_issue_tag"] == {
        "baseline_guard": 3,
        "candidate_gap": 21,
        "formal_term": 11,
        "high_risk_term": 7,
        "it_term": 17,
        "llm_term": 2,
        "over_conversion": 28,
        "regional_term": 53,
        "social_term": 1,
        "ui_term": 11,
    }


def test_private_benchmark_sanity_after_batch9_miss_review_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH9_MISS_REVIEW)
    final_decision = load_json(MAINTAINER_BATCH9_MISS_FINAL_DECISION)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch9_miss_review"
    assert sanity["expected_values_included"] is False
    assert sanity["rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert sanity["source_benchmark"] == {
        "path": "/tmp/zhtw-blind-v1-private-benchmark-after-batch9-miss-review-2026-07-12.json",
        "in_repo": False,
        "rows_used_for_aggregate_only": True,
    }
    assert sanity["inputs"]["sha256"] == (
        "8f54d6e8185cf94f73805aeea27a23859e691cfd8ae04f3956023ec8ec9606d4"
    )
    assert sanity["inputs"]["sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert sanity["expected"]["sha256"] == final_decision["private_expected_sha256_after"]
    assert sanity["expected"]["sha256"] != private_expected_sha256()
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_values_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "aggregate_statistics_only": True,
    }
    assert sanity["summary"]["case_count"] == 667
    assert sanity["summary"]["accepted"] == 636
    assert sanity["summary"]["misses"] == 31
    assert sanity["summary"]["primary_exact"] == 491
    assert sanity["summary"]["acceptable_exact"] == 145
    assert sanity["summary"]["accepted_accuracy"] == 0.9535232383808095
    assert sanity["summary"]["primary_exact_accuracy"] == 0.7361319340329835
    assert sanity["summary"]["idempotency_rate"] == 0.9835082458770614
    assert sanity["summary"]["accepted_accuracy_ci_95"] == {
        "low": 0.9355322338830585,
        "high": 0.9685157421289355,
    }
    assert sanity["summary"]["by_domain"] == {
        "formal": {
            "total": 110,
            "accepted": 104,
            "accepted_accuracy": 0.9454545454545454,
        },
        "high_risk": {
            "total": 76,
            "accepted": 69,
            "accepted_accuracy": 0.9078947368421053,
        },
        "it": {
            "total": 124,
            "accepted": 121,
            "accepted_accuracy": 0.9758064516129032,
        },
        "llm": {
            "total": 111,
            "accepted": 107,
            "accepted_accuracy": 0.963963963963964,
        },
        "social": {
            "total": 114,
            "accepted": 108,
            "accepted_accuracy": 0.9473684210526315,
        },
        "ui": {
            "total": 132,
            "accepted": 127,
            "accepted_accuracy": 0.9621212121212122,
        },
    }
    assert sanity["summary"]["by_risk"] == {
        "baseline_guard": 107,
        "candidate_gap": 372,
        "over_conversion_guard": 188,
    }
    assert sanity["summary"]["misses_by_risk"] == {
        "baseline_guard": 1,
        "candidate_gap": 2,
        "over_conversion_guard": 28,
    }
    assert sanity["summary"]["misses_by_issue_tag"] == {
        "baseline_guard": 1,
        "candidate_gap": 1,
        "formal_term": 9,
        "high_risk_term": 7,
        "it_term": 5,
        "over_conversion": 28,
        "regional_term": 31,
        "social_term": 1,
        "ui_term": 5,
    }


def test_private_benchmark_sanity_after_batch10_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH10)
    final_decision = load_json(MAINTAINER_BATCH10_FINAL_DECISION)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch10_final_decision"
    assert sanity["expected_values_included"] is False
    assert sanity["rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert sanity["source_benchmark"] == {
        "path": "/tmp/zhtw-blind-v1-private-benchmark-after-batch10-2026-07-12.json",
        "in_repo": False,
        "rows_used_for_aggregate_only": True,
    }
    assert sanity["inputs"]["sha256"] == (
        "eff19da4ff198981bdb0018bceabb128b1aa5a33e9199ea5421f69561da340d0"
    )
    assert sanity["inputs"]["sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert sanity["expected"]["sha256"] == final_decision["private_expected_sha256"]
    assert sanity["expected"]["sha256"] != private_expected_sha256()
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "aggregate_statistics_only": True,
    }
    assert sanity["summary"]["case_count"] == 767
    assert sanity["summary"]["accepted"] == 715
    assert sanity["summary"]["misses"] == 52
    assert sanity["summary"]["primary_exact"] == 552
    assert sanity["summary"]["acceptable_exact"] == 163
    assert sanity["summary"]["accepted_accuracy"] == 0.9322033898305084
    assert sanity["summary"]["primary_exact_accuracy"] == 0.7196870925684485
    assert sanity["summary"]["idempotency_rate"] == 0.9830508474576272
    assert sanity["summary"]["accepted_accuracy_ci_95"] == {
        "low": 0.9139504563233377,
        "high": 0.9491525423728814,
    }
    assert sanity["summary"]["by_domain"] == {
        "formal": {
            "total": 125,
            "accepted": 116,
            "accepted_accuracy": 0.928,
        },
        "high_risk": {
            "total": 86,
            "accepted": 78,
            "accepted_accuracy": 0.9069767441860465,
        },
        "it": {
            "total": 149,
            "accepted": 137,
            "accepted_accuracy": 0.9194630872483222,
        },
        "llm": {
            "total": 126,
            "accepted": 120,
            "accepted_accuracy": 0.9523809523809523,
        },
        "social": {
            "total": 129,
            "accepted": 123,
            "accepted_accuracy": 0.9534883720930233,
        },
        "ui": {
            "total": 152,
            "accepted": 141,
            "accepted_accuracy": 0.9276315789473685,
        },
    }
    assert sanity["summary"]["by_risk"] == {
        "baseline_guard": 122,
        "candidate_gap": 432,
        "over_conversion_guard": 213,
    }
    assert sanity["summary"]["misses_by_risk"] == {
        "baseline_guard": 4,
        "candidate_gap": 19,
        "over_conversion_guard": 29,
    }
    assert sanity["summary"]["misses_by_issue_tag"] == {
        "baseline_guard": 4,
        "candidate_gap": 18,
        "formal_term": 13,
        "high_risk_term": 8,
        "it_term": 14,
        "llm_term": 2,
        "over_conversion": 29,
        "regional_term": 52,
        "social_term": 1,
        "ui_term": 11,
    }


def test_private_benchmark_sanity_after_batch11_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH11)
    final_decision = load_json(MAINTAINER_BATCH11_FINAL_DECISION)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch11_final_decision"
    assert sanity["expected_values_included"] is False
    assert sanity["acceptable_values_included"] is False
    assert sanity["rows_included"] is False
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert "rows" not in sanity
    assert sanity["source_final_decision"] == str(
        MAINTAINER_BATCH11_FINAL_DECISION.relative_to(ROOT)
    )
    assert sanity["source_benchmark"] == {
        "path": "/tmp/zhtw-blind-v1-private-benchmark-after-batch11-2026-07-14.json",
        "in_repo": False,
        "rows_used_for_aggregate_only": True,
    }
    assert sanity["inputs"]["sha256"] == (
        "e7018d35e078a53ff1c59e4a8281b787151fd11c158859ad882defc82b93aff9"
    )
    assert sanity["inputs"]["sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert sanity["expected"]["sha256"] == (
        "bbf89dfa8db7774fdd9b8c078f97d18b9b3749f164d5f4e7cc109bb8ac0ab096"
    )
    assert sanity["expected"]["sha256"] != private_expected_sha256()
    assert sanity["expected"]["sha256"] == final_decision["private_expected_sha256"]
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"]["aggregate_statistics_only"] is True
    assert sanity["summary"]["case_count"] == 851
    assert sanity["summary"]["accepted"] == 791
    assert sanity["summary"]["misses"] == 60
    assert sanity["summary"]["primary_exact"] == 624
    assert sanity["summary"]["acceptable_exact"] == 167
    assert sanity["summary"]["accepted_accuracy"] == 0.9294947121034077
    assert sanity["summary"]["primary_exact_accuracy"] == 0.7332549941245593
    assert sanity["summary"]["idempotency_rate"] == 0.9835487661574618
    assert sanity["summary"]["misses_by_risk"] == {
        "baseline_guard": 4,
        "candidate_gap": 20,
        "over_conversion_guard": 36,
    }


def test_private_benchmark_sanity_after_batch11_semantic_reaudit_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH11_SEMANTIC_REAUDIT)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch11_semantic_reaudit"
    assert sanity["expected_values_included"] is False
    assert sanity["acceptable_values_included"] is False
    assert sanity["rows_included"] is False
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs"]["sha256"] == (
        "3c35b332959c7a87410a0ba7c08d46aa98857b1c080155d275a8892d0f507fef"
    )
    assert sanity["inputs"]["sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert sanity["expected"]["sha256"] == (
        "066bcd60d16760a10eb8cdd54de61e8ff438fe4a7ffe971e8f814fc45563db2d"
    )
    assert sanity["expected"]["sha256"] != private_expected_sha256()
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"]["aggregate_statistics_only"] is True
    assert sanity["summary"]["case_count"] == 841
    assert sanity["summary"]["accepted"] == 795
    assert sanity["summary"]["misses"] == 46
    assert sanity["summary"]["primary_exact"] == 624
    assert sanity["summary"]["acceptable_exact"] == 171
    assert sanity["summary"]["accepted_accuracy"] == 0.9453032104637337
    assert sanity["summary"]["misses_by_risk"] == {
        "baseline_guard": 3,
        "candidate_gap": 11,
        "over_conversion_guard": 32,
    }


def test_private_benchmark_sanity_after_batch12_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH12)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch12_final_decision"
    assert sanity["expected_values_included"] is False
    assert sanity["acceptable_values_included"] is False
    assert sanity["rows_included"] is False
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs"]["sha256"] == (
        "c1082299113239bfe88590425ccd6c4b4b0f0d769ddea18ce457a11050863deb"
    )
    assert sanity["inputs"]["sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert sanity["expected"]["sha256"] == (
        "617f048425d75605e1997b8952432792f417444b3c4facec89bc5bd7a160dd22"
    )
    assert sanity["expected"]["sha256"] != private_expected_sha256()
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"]["aggregate_statistics_only"] is True
    assert sanity["summary"]["case_count"] == 941
    assert sanity["summary"]["accepted"] == 880
    assert sanity["summary"]["misses"] == 61
    assert sanity["summary"]["accepted_accuracy"] == 0.9351753453772582
    assert sanity["batch12_summary"]["case_count"] == 100
    assert sanity["batch12_summary"]["accepted"] == 85
    assert sanity["batch12_summary"]["misses"] == 15
    assert sanity["batch12_summary"]["accepted_accuracy"] == 0.85


def test_private_benchmark_sanity_after_batch12_miss_review_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH12_MISS_REVIEW)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch12_miss_review"
    assert sanity["inputs"]["sha256"] == (
        "9297eaf5688b87b0d89d83dceb04f9ce3fa62944f6cbde83b485bc0524e7f780"
    )
    assert sanity["inputs"]["sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert sanity["expected"]["sha256"] == (
        "81246822bffc1423b1460b0bfe7f1ed2539060f31880f8b49424e85c25b6052e"
    )
    assert sanity["expected"]["sha256"] != private_expected_sha256()
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"]["aggregate_statistics_only"] is True
    assert sanity["interpretation_policy"] == {
        "pure_capability_gain_claimed": False,
        "acceptable_variants_added": 4,
        "cases_removed_before_tuning": 11,
        "denominator_changed": True,
    }
    assert sanity["summary"]["case_count"] == 930
    assert sanity["summary"]["accepted"] == 884
    assert sanity["summary"]["misses"] == 46
    assert sanity["summary"]["accepted_accuracy"] == 0.9505376344086022
    assert sanity["summary"]["misses_by_risk"] == {
        "baseline_guard": 3,
        "candidate_gap": 11,
        "over_conversion_guard": 32,
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


def test_private_benchmark_sanity_after_batch10_miss_review_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH10_MISS_REVIEW)
    final_decision = load_json(MAINTAINER_BATCH10_MISS_FINAL_DECISION)

    assert sanity["report_type"] == "holdout_private_benchmark_sanity"
    assert sanity["review_stage"] == "after_batch10_miss_review"
    assert sanity["expected_values_included"] is False
    assert sanity["acceptable_values_included"] is False
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert "rows" not in sanity
    assert sanity["source_final_decision"] == str(
        MAINTAINER_BATCH10_MISS_FINAL_DECISION.relative_to(ROOT)
    )
    assert sanity["summary"]["source_inputs_sha256"] == (
        "e6d6e8a2d0b5f9fdffaee7cc7c467cab74210eed62db0202d287bceceb2d02bf"
    )
    assert (
        sanity["summary"]["source_inputs_sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    )
    assert sanity["summary"]["private_expected_sha256"] == (
        "5c89d5037efcbc33c80dd86f35ccfd12102a709fe701820b9d318fa1f8fe49dc"
    )
    assert sanity["summary"]["private_expected_sha256"] != private_expected_sha256()
    assert (
        sanity["summary"]["private_expected_sha256"]
        == (final_decision["private_expected_sha256_after"])
    )
    assert sanity["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "case_ids_and_metadata_only": False,
        "aggregate_statistics_only": True,
    }
    assert sanity["summary"]["case_count"] == 751
    assert sanity["summary"]["accepted"] == 719
    assert sanity["summary"]["misses"] == 32
    assert sanity["summary"]["accepted_accuracy"] == 0.9573901464713716
    assert sanity["summary"]["primary_exact"] == 552
    assert sanity["summary"]["acceptable_exact"] == 167
    assert sanity["summary"]["miss_by_risk"] == {
        "baseline_guard": 1,
        "candidate_gap": 2,
        "over_conversion_guard": 29,
    }
    assert sanity["summary"]["miss_by_domain"] == {
        "formal": 6,
        "high_risk": 8,
        "it": 3,
        "llm": 4,
        "social": 6,
        "ui": 5,
    }


def test_holdout_426_case_miss_classification_omits_sealed_values() -> None:
    report = load_json(MISS_CLASSIFICATION_426_CASE)

    assert report["report_type"] == "holdout_miss_classification_426_case_sanity"
    assert report["review_stage"] == "private_miss_classification_first_pass_after_batch6"
    assert report["reviewer"] == "codex"
    assert report["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "case_ids_and_metadata_only": True,
    }
    assert report["gemini_review_policy"] == {
        "status": "completed_on_sanitized_metadata",
        "review_report": (
            "docs/reports/"
            "holdout-gemini-policy-review-miss-classification-blind-v1-426-cases-2026-07-10.json"
        ),
        "sealed_values_seen_by_gemini": False,
        "policy_passed": True,
        "classification_changes_recommended": 0,
        "reason": (
            "Gemini reviewed case ids and classification metadata only; private expected, "
            "inputs, and converter outputs were not sent."
        ),
    }
    assert report["summary"] == {
        "current_sealed_cases": 426,
        "current_accepted": 389,
        "current_misses": 37,
        "accepted_accuracy": 0.9131455399061033,
        "classified_misses": 37,
        "by_action": {
            "keep_as_holdout_signal": 24,
            "move_to_public_regression_candidate": 11,
            "requires_expected_recheck": 2,
        },
        "by_priority": {"P1": 2, "P2": 35},
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
                "keep_as_holdout_signal": 3,
                "move_to_public_regression_candidate": 10,
                "requires_expected_recheck": 0,
            },
            "llm": {
                "keep_as_holdout_signal": 4,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 1,
            },
            "social": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
            "ui": {
                "keep_as_holdout_signal": 4,
                "move_to_public_regression_candidate": 1,
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
                "move_to_public_regression_candidate": 10,
                "requires_expected_recheck": 2,
            },
            "over_conversion_guard": {
                "keep_as_holdout_signal": 24,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
        },
        "idempotency_followup_cases": 1,
        "expected_recheck_cases": 2,
        "safe_public_candidate_cases": 11,
        "holdout_signal_cases": 24,
        "high_risk_cases": 3,
        "over_conversion_guard_cases": 24,
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
        assert case["id"].startswith("blind-")
        assert case["action"] in report["summary"]["by_action"]
        assert case["reason_code"]
        assert case["next_step"]

    action_by_id = {case["id"]: case["action"] for case in cases}
    assert action_by_id["blind-it-0124"] == "move_to_public_regression_candidate"
    assert action_by_id["blind-ui-0096"] == "requires_expected_recheck"
    assert action_by_id["blind-llm-0071"] == "requires_expected_recheck"
    assert action_by_id["blind-high-risk-0039"] == "keep_as_holdout_signal"
    assert report["idempotency_notes"]["non_idempotent_miss_ids"] == ["blind-it-0124"]


def test_gemini_426_case_miss_classification_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_MISS_CLASSIFICATION_426_POLICY_REVIEW)

    assert review["reviewer"] == "gemini_cli"
    assert review["model_requested"] == "gemini-2.5-flash"
    assert review["review_stage"] == "sanitized_miss_classification_policy_review_after_batch6"
    assert review["source_classification_report"] == (
        "docs/reports/holdout-miss-classification-blind-v1-426-cases-2026-07-10.json"
    )
    assert review["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "gemini_received_sanitized_metadata_only": True,
    }
    assert review["policy_passed"] is True
    assert review["classification_changes_recommended"] == []
    assert len(review["findings"]) == 3
    assert {finding["case_id"] for finding in review["findings"]} == {
        "blind-it-0124",
        "blind-ui-0096",
        "blind-llm-0071",
    }


def test_holdout_batch6_miss_classification_confirmation_packet_is_sanitized() -> None:
    classification = load_json(MISS_CLASSIFICATION_426_CASE)
    packet = load_json(MAINTAINER_BATCH6_MISS_CLASSIFICATION_CONFIRMATION)

    review_ids = {
        case["id"]
        for case in classification["case_classifications"]
        if case["action"] in {"move_to_public_regression_candidate", "requires_expected_recheck"}
    }
    holdout_signal_ids = {
        case["id"]
        for case in classification["case_classifications"]
        if case["action"] == "keep_as_holdout_signal"
    }

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch6_miss_classification_after_426_case_sanity"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["sealed_content_policy"] == classification["sealed_content_policy"]
    assert packet["summary"] == {
        "total_review_cases": 13,
        "public_regression_candidate_cases": 11,
        "expected_recheck_cases": 2,
        "no_immediate_question": 24,
        "gemini_policy_passed": True,
        "classification_changes_recommended_by_gemini": 0,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in packet["cases"]} == review_ids
    assert set(packet["no_immediate_question_case_ids"]) == holdout_signal_ids
    assert len(packet["cases"]) == 13
    assert len(packet["no_immediate_question_case_ids"]) == 24
    assert all(case["sealed_values_omitted"] is True for case in packet["cases"])


def test_holdout_515_case_miss_classification_omits_sealed_values() -> None:
    report = load_json(MISS_CLASSIFICATION_515_CASE)

    assert report["report_type"] == "holdout_miss_classification_515_case_sanity"
    assert report["review_stage"] == "private_miss_classification_first_pass_after_batch7"
    assert report["reviewer"] == "codex"
    assert report["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "case_ids_and_metadata_only": True,
    }
    assert report["gemini_review_policy"] == {
        "status": "completed_on_sanitized_metadata",
        "review_report": (
            "docs/reports/"
            "holdout-gemini-policy-review-miss-classification-blind-v1-515-cases-2026-07-10.json"
        ),
        "sealed_values_seen_by_gemini": False,
        "policy_passed": True,
        "classification_changes_recommended": 0,
        "reason": (
            "Gemini reviewed case ids and classification metadata only; private expected, "
            "inputs, and converter outputs were not sent. GEMINI_API_KEY was unset for "
            "this CLI run to avoid invalid API-key mode."
        ),
    }
    assert report["summary"] == {
        "current_sealed_cases": 515,
        "current_accepted": 465,
        "current_misses": 50,
        "accepted_accuracy": 0.9029126213592233,
        "classified_misses": 50,
        "by_action": {
            "keep_as_holdout_signal": 26,
            "move_to_public_regression_candidate": 17,
            "requires_expected_recheck": 7,
        },
        "by_priority": {"P1": 7, "P2": 43},
        "by_domain_action": {
            "formal": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 1,
                "requires_expected_recheck": 0,
            },
            "high_risk": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
            "it": {
                "keep_as_holdout_signal": 3,
                "move_to_public_regression_candidate": 11,
                "requires_expected_recheck": 4,
            },
            "llm": {
                "keep_as_holdout_signal": 4,
                "move_to_public_regression_candidate": 2,
                "requires_expected_recheck": 0,
            },
            "social": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 1,
                "requires_expected_recheck": 0,
            },
            "ui": {
                "keep_as_holdout_signal": 4,
                "move_to_public_regression_candidate": 2,
                "requires_expected_recheck": 3,
            },
        },
        "by_risk_action": {
            "baseline_guard": {
                "keep_as_holdout_signal": 0,
                "move_to_public_regression_candidate": 2,
                "requires_expected_recheck": 0,
            },
            "candidate_gap": {
                "keep_as_holdout_signal": 1,
                "move_to_public_regression_candidate": 15,
                "requires_expected_recheck": 7,
            },
            "over_conversion_guard": {
                "keep_as_holdout_signal": 25,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
        },
        "idempotency_followup_cases": 5,
        "expected_recheck_cases": 7,
        "safe_public_candidate_cases": 17,
        "holdout_signal_cases": 26,
        "high_risk_cases": 5,
        "over_conversion_guard_cases": 25,
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
    assert len(cases) == 50
    assert len({case["id"] for case in cases}) == len(cases)
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["id"].startswith("blind-")
        assert case["action"] in report["summary"]["by_action"]
        assert case["reason_code"]
        assert case["next_step"]

    action_by_id = {case["id"]: case["action"] for case in cases}
    assert action_by_id["blind-it-0142"] == "move_to_public_regression_candidate"
    assert action_by_id["blind-it-0148"] == "requires_expected_recheck"
    assert action_by_id["blind-ui-0108"] == "requires_expected_recheck"
    assert action_by_id["blind-high-risk-0053"] == "keep_as_holdout_signal"
    assert report["idempotency_notes"]["non_idempotent_miss_ids"] == [
        "blind-it-0142",
        "blind-it-0152",
        "blind-it-0155",
        "blind-ui-0123",
        "blind-social-0079",
    ]


def test_gemini_515_case_miss_classification_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_MISS_CLASSIFICATION_515_POLICY_REVIEW)

    assert review["reviewer"] == "gemini_cli"
    assert review["model_requested"] == "gemini-2.5-flash"
    assert review["review_stage"] == "sanitized_miss_classification_policy_review_after_batch7"
    assert review["source_classification_report"] == (
        "docs/reports/holdout-miss-classification-blind-v1-515-cases-2026-07-10.json"
    )
    assert review["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "gemini_received_sanitized_metadata_only": True,
    }
    assert review["policy_passed"] is True
    assert review["classification_changes_recommended"] == []
    assert len(review["findings"]) == 5
    assert {finding["case_id"] for finding in review["findings"]} == {
        "over_conversion_guard_cases",
        "high_risk_cases",
        "public_regression_candidate_cases",
        "expected_recheck_cases",
        "non_idempotent_miss_ids",
    }


def test_holdout_batch7_miss_classification_confirmation_packet_is_sanitized() -> None:
    classification = load_json(MISS_CLASSIFICATION_515_CASE)
    packet = load_json(MAINTAINER_BATCH7_MISS_CLASSIFICATION_CONFIRMATION)

    review_ids = {
        case["id"]
        for case in classification["case_classifications"]
        if case["action"] in {"move_to_public_regression_candidate", "requires_expected_recheck"}
    }
    holdout_signal_ids = {
        case["id"]
        for case in classification["case_classifications"]
        if case["action"] == "keep_as_holdout_signal"
    }

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch7_miss_classification_after_515_case_sanity"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["sealed_content_policy"] == classification["sealed_content_policy"]
    assert packet["summary"] == {
        "total_review_cases": 24,
        "public_regression_candidate_cases": 17,
        "expected_recheck_cases": 7,
        "no_immediate_question": 26,
        "gemini_policy_passed": True,
        "classification_changes_recommended_by_gemini": 0,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in packet["cases"]} == review_ids
    assert set(packet["no_immediate_question_case_ids"]) == holdout_signal_ids
    assert len(packet["cases"]) == 24
    assert len(packet["no_immediate_question_case_ids"]) == 26
    assert all(case["sealed_values_omitted"] is True for case in packet["cases"])


def test_holdout_598_case_miss_classification_omits_sealed_values() -> None:
    report = load_json(MISS_CLASSIFICATION_598_CASE)

    assert report["report_type"] == "holdout_miss_classification_598_case_sanity"
    assert report["review_stage"] == "private_miss_classification_first_pass_after_batch8"
    assert report["reviewer"] == "codex"
    assert report["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "case_ids_and_metadata_only": True,
    }
    assert report["gemini_review_policy"]["status"] == "completed_on_sanitized_metadata"
    assert report["gemini_review_policy"]["review_report"] == (
        "docs/reports/"
        "holdout-gemini-policy-review-miss-classification-blind-v1-598-cases-2026-07-10.json"
    )
    assert report["gemini_review_policy"]["sealed_values_seen_by_gemini"] is False
    assert report["gemini_review_policy"]["policy_passed"] is True
    assert report["gemini_review_policy"]["classification_changes_recommended"] == 0
    assert report["summary"] == {
        "current_sealed_cases": 598,
        "current_accepted": 549,
        "current_misses": 49,
        "accepted_accuracy": 0.9180602006688964,
        "classified_misses": 49,
        "by_action": {
            "keep_as_holdout_signal": 30,
            "move_to_public_regression_candidate": 15,
            "requires_expected_recheck": 4,
        },
        "by_priority": {"P1": 5, "P2": 44},
        "by_domain_action": {
            "formal": {
                "keep_as_holdout_signal": 6,
                "move_to_public_regression_candidate": 1,
                "requires_expected_recheck": 0,
            },
            "high_risk": {
                "keep_as_holdout_signal": 7,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
            "it": {
                "keep_as_holdout_signal": 3,
                "move_to_public_regression_candidate": 8,
                "requires_expected_recheck": 2,
            },
            "llm": {
                "keep_as_holdout_signal": 4,
                "move_to_public_regression_candidate": 1,
                "requires_expected_recheck": 1,
            },
            "social": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 1,
            },
            "ui": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 5,
                "requires_expected_recheck": 0,
            },
        },
        "by_risk_action": {
            "baseline_guard": {
                "keep_as_holdout_signal": 1,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
            "candidate_gap": {
                "keep_as_holdout_signal": 2,
                "move_to_public_regression_candidate": 15,
                "requires_expected_recheck": 4,
            },
            "over_conversion_guard": {
                "keep_as_holdout_signal": 27,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
        },
        "idempotency_followup_cases": 2,
        "expected_recheck_cases": 4,
        "safe_public_candidate_cases": 15,
        "holdout_signal_cases": 30,
        "high_risk_cases": 7,
        "over_conversion_guard_cases": 27,
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
    assert len(cases) == 49
    assert len({case["id"] for case in cases}) == len(cases)
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["id"].startswith("blind-")
        assert case["action"] in report["summary"]["by_action"]
        assert case["reason_code"]
        assert case["next_step"]

    action_by_id = {case["id"]: case["action"] for case in cases}
    assert action_by_id["blind-it-0165"] == "move_to_public_regression_candidate"
    assert action_by_id["blind-formal-0101"] == "move_to_public_regression_candidate"
    assert action_by_id["blind-it-0167"] == "requires_expected_recheck"
    assert action_by_id["blind-social-0095"] == "requires_expected_recheck"
    assert action_by_id["blind-high-risk-0068"] == "keep_as_holdout_signal"
    assert report["idempotency_notes"]["non_idempotent_miss_ids"] == [
        "blind-it-0174",
        "blind-ui-0147",
    ]


def test_gemini_598_case_miss_classification_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_MISS_CLASSIFICATION_598_POLICY_REVIEW)

    assert review["reviewer"] == "gemini_cli"
    assert review["model_requested"] == "gemini-2.5-flash"
    assert review["review_stage"] == "gemini_policy_review_batch8_miss_classification"
    assert review["source_classification_report"] == (
        "docs/reports/holdout-miss-classification-blind-v1-598-cases-2026-07-10.json"
    )
    assert review["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "case_ids_and_metadata_only": True,
        "sealed_values_seen_by_gemini": False,
    }
    assert review["policy_passed"] is True
    assert review["classification_changes_recommended"] == []
    assert {finding["case_id"] for finding in review["findings"]} == {
        "blind-it-0174",
        "blind-ui-0147",
    }


def test_holdout_batch8_miss_classification_confirmation_packet_is_sanitized() -> None:
    classification = load_json(MISS_CLASSIFICATION_598_CASE)
    packet = load_json(MAINTAINER_BATCH8_MISS_CLASSIFICATION_CONFIRMATION)

    review_ids = {
        case["id"]
        for case in classification["case_classifications"]
        if case["action"] in {"move_to_public_regression_candidate", "requires_expected_recheck"}
    }
    holdout_signal_ids = {
        case["id"]
        for case in classification["case_classifications"]
        if case["action"] == "keep_as_holdout_signal"
    }

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch8_miss_classification"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["sealed_content_policy"] == classification["sealed_content_policy"]
    assert packet["summary"] == {
        "total_review_cases": 19,
        "public_regression_candidate_cases": 15,
        "expected_recheck_cases": 4,
        "no_immediate_question": 30,
        "gemini_policy_passed": True,
        "classification_changes_recommended_by_gemini": 0,
        "by_action": {
            "move_to_public_regression_candidate": 15,
            "requires_expected_recheck": 4,
        },
        "by_domain": {
            "formal": 1,
            "it": 10,
            "llm": 2,
            "social": 1,
            "ui": 5,
        },
        "by_risk": {
            "candidate_gap": 19,
        },
        "non_idempotent_review_cases": 1,
    }
    assert {case["id"] for case in packet["cases"]} == review_ids
    assert set(packet["no_immediate_question_case_ids"]) == holdout_signal_ids
    assert len(packet["cases"]) == 19
    assert len(packet["no_immediate_question_case_ids"]) == 30
    assert all(case["sealed_values_omitted"] is True for case in packet["cases"])


def test_holdout_683_case_miss_classification_omits_sealed_values() -> None:
    report = load_json(MISS_CLASSIFICATION_683_CASE)

    assert report["report_type"] == "holdout_miss_classification_683_case_sanity"
    assert report["review_stage"] == "private_miss_classification_first_pass_after_batch9"
    assert report["reviewer"] == "codex"
    assert report["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "case_ids_and_metadata_only": True,
    }
    assert report["gemini_review_policy"]["status"] == "completed_on_sanitized_metadata"
    assert report["gemini_review_policy"]["review_report"] == (
        "docs/reports/"
        "holdout-gemini-policy-review-miss-classification-blind-v1-683-cases-2026-07-12.json"
    )
    assert report["gemini_review_policy"]["sealed_values_seen_by_gemini"] is False
    assert report["gemini_review_policy"]["policy_passed"] is True
    assert report["gemini_review_policy"]["classification_changes_recommended"] == 0
    assert report["summary"] == {
        "current_sealed_cases": 683,
        "current_accepted": 630,
        "current_misses": 53,
        "accepted_accuracy": 0.9224011713030746,
        "classified_misses": 53,
        "by_action": {
            "keep_as_holdout_signal": 31,
            "move_to_public_regression_candidate": 16,
            "requires_expected_recheck": 6,
        },
        "by_priority": {"P1": 10, "P2": 43},
        "by_domain_action": {
            "formal": {
                "keep_as_holdout_signal": 6,
                "move_to_public_regression_candidate": 2,
                "requires_expected_recheck": 0,
            },
            "high_risk": {
                "keep_as_holdout_signal": 7,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
            "it": {
                "keep_as_holdout_signal": 3,
                "move_to_public_regression_candidate": 8,
                "requires_expected_recheck": 4,
            },
            "llm": {
                "keep_as_holdout_signal": 4,
                "move_to_public_regression_candidate": 2,
                "requires_expected_recheck": 0,
            },
            "social": {
                "keep_as_holdout_signal": 6,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
            "ui": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 4,
                "requires_expected_recheck": 2,
            },
        },
        "by_risk_action": {
            "baseline_guard": {
                "keep_as_holdout_signal": 1,
                "move_to_public_regression_candidate": 2,
                "requires_expected_recheck": 0,
            },
            "candidate_gap": {
                "keep_as_holdout_signal": 2,
                "move_to_public_regression_candidate": 14,
                "requires_expected_recheck": 6,
            },
            "over_conversion_guard": {
                "keep_as_holdout_signal": 28,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
        },
        "idempotency_followup_cases": 3,
        "expected_recheck_cases": 6,
        "safe_public_candidate_cases": 16,
        "holdout_signal_cases": 31,
        "high_risk_cases": 7,
        "over_conversion_guard_cases": 28,
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
    assert len(cases) == 53
    assert len({case["id"] for case in cases}) == len(cases)
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["id"].startswith("blind-")
        assert case["action"] in report["summary"]["by_action"]
        assert case["reason_code"]
        assert case["next_step"]

    action_by_id = {case["id"]: case["action"] for case in cases}
    assert action_by_id["blind-it-0190"] == "move_to_public_regression_candidate"
    assert action_by_id["blind-formal-0115"] == "move_to_public_regression_candidate"
    assert action_by_id["blind-it-0189"] == "requires_expected_recheck"
    assert action_by_id["blind-ui-0166"] == "requires_expected_recheck"
    assert action_by_id["blind-social-0110"] == "keep_as_holdout_signal"
    assert report["idempotency_notes"]["non_idempotent_miss_ids"] == [
        "blind-ui-0147",
        "blind-it-0190",
        "blind-it-0200",
    ]


def test_gemini_683_case_miss_classification_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_MISS_CLASSIFICATION_683_POLICY_REVIEW)

    assert review["reviewer"] == "gemini_cli"
    assert review["model_requested"] == "gemini-2.5-flash"
    assert review["review_stage"] == "gemini_policy_review_batch9_miss_classification"
    assert review["source_classification_report"] == (
        "docs/reports/holdout-miss-classification-blind-v1-683-cases-2026-07-12.json"
    )
    assert review["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "case_ids_and_metadata_only": True,
        "sealed_values_seen_by_gemini": False,
    }
    assert review["policy_passed"] is True
    assert review["classification_changes_recommended"] == []
    assert {finding["case_id"] for finding in review["findings"]} == {
        "blind-ui-0147",
        "blind-it-0190",
        "blind-it-0200",
    }


def test_holdout_batch9_miss_classification_confirmation_packet_is_sanitized() -> None:
    classification = load_json(MISS_CLASSIFICATION_683_CASE)
    packet = load_json(MAINTAINER_BATCH9_MISS_CLASSIFICATION_CONFIRMATION)

    review_ids = {
        case["id"]
        for case in classification["case_classifications"]
        if case["action"] in {"move_to_public_regression_candidate", "requires_expected_recheck"}
    }
    holdout_signal_ids = {
        case["id"]
        for case in classification["case_classifications"]
        if case["action"] == "keep_as_holdout_signal"
    }

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch9_miss_classification"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["sealed_content_policy"] == classification["sealed_content_policy"]
    assert packet["summary"] == {
        "total_review_cases": 22,
        "public_regression_candidate_cases": 16,
        "expected_recheck_cases": 6,
        "no_immediate_question": 31,
        "gemini_policy_passed": True,
        "classification_changes_recommended_by_gemini": 0,
        "by_action": {
            "move_to_public_regression_candidate": 16,
            "requires_expected_recheck": 6,
        },
        "by_domain": {
            "formal": 2,
            "it": 12,
            "llm": 2,
            "ui": 6,
        },
        "by_risk": {
            "baseline_guard": 2,
            "candidate_gap": 20,
        },
        "non_idempotent_review_cases": 2,
    }
    assert {case["id"] for case in packet["cases"]} == review_ids
    assert set(packet["no_immediate_question_case_ids"]) == holdout_signal_ids
    assert len(packet["cases"]) == 22
    assert len(packet["no_immediate_question_case_ids"]) == 31
    assert all(case["sealed_values_omitted"] is True for case in packet["cases"])


def test_holdout_767_case_miss_classification_omits_sealed_values() -> None:
    report = load_json(MISS_CLASSIFICATION_767_CASE)

    assert report["report_type"] == "holdout_miss_classification_767_case_sanity"
    assert report["review_stage"] == "private_miss_classification_first_pass_after_batch10"
    assert report["reviewer"] == "codex"
    assert report["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "case_ids_and_metadata_only": True,
    }
    assert report["gemini_review_policy"]["status"] == "completed_on_sanitized_metadata"
    assert report["gemini_review_policy"]["review_report"] == (
        "docs/reports/"
        "holdout-gemini-policy-review-miss-classification-blind-v1-767-cases-2026-07-12.json"
    )
    assert report["gemini_review_policy"]["sealed_values_seen_by_gemini"] is False
    assert report["gemini_review_policy"]["policy_passed"] is True
    assert report["gemini_review_policy"]["classification_changes_recommended"] == 0
    assert report["summary"] == {
        "current_sealed_cases": 767,
        "current_accepted": 715,
        "current_misses": 52,
        "accepted_accuracy": 0.9322033898305084,
        "classified_misses": 52,
        "by_action": {
            "keep_as_holdout_signal": 32,
            "move_to_public_regression_candidate": 16,
            "requires_expected_recheck": 4,
        },
        "by_priority": {"P1": 28, "P2": 24},
        "by_domain_action": {
            "formal": {
                "keep_as_holdout_signal": 6,
                "move_to_public_regression_candidate": 3,
                "requires_expected_recheck": 0,
            },
            "high_risk": {
                "keep_as_holdout_signal": 8,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
            "it": {
                "keep_as_holdout_signal": 3,
                "move_to_public_regression_candidate": 7,
                "requires_expected_recheck": 2,
            },
            "llm": {
                "keep_as_holdout_signal": 4,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 2,
            },
            "social": {
                "keep_as_holdout_signal": 6,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
            "ui": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 6,
                "requires_expected_recheck": 0,
            },
        },
        "by_risk_action": {
            "baseline_guard": {
                "keep_as_holdout_signal": 1,
                "move_to_public_regression_candidate": 3,
                "requires_expected_recheck": 0,
            },
            "candidate_gap": {
                "keep_as_holdout_signal": 2,
                "move_to_public_regression_candidate": 13,
                "requires_expected_recheck": 4,
            },
            "over_conversion_guard": {
                "keep_as_holdout_signal": 29,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
        },
        "idempotency_followup_cases": 2,
        "expected_recheck_cases": 4,
        "safe_public_candidate_cases": 16,
        "holdout_signal_cases": 32,
        "high_risk_cases": 8,
        "over_conversion_guard_cases": 29,
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
    assert len(cases) == 52
    assert len({case["id"] for case in cases}) == len(cases)
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["id"].startswith("blind-")
        action = case.get("action", case.get("recommended_action"))
        assert action in report["summary"]["by_action"]
        assert case["reason_code"]
        assert case["sealed_values_omitted"] is True

    action_by_id = {
        case["id"]: case.get("action", case.get("recommended_action")) for case in cases
    }
    assert action_by_id["blind-it-0217"] == "move_to_public_regression_candidate"
    assert action_by_id["blind-formal-0129"] == "move_to_public_regression_candidate"
    assert action_by_id["blind-it-0222"] == "requires_expected_recheck"
    assert action_by_id["blind-llm-0123"] == "requires_expected_recheck"
    assert action_by_id["blind-llm-0137"] == "requires_expected_recheck"
    assert action_by_id["blind-social-0110"] == "keep_as_holdout_signal"
    assert [case["id"] for case in report["idempotency_notes"]] == [
        "blind-ui-0147",
        "blind-it-0230",
    ]


def test_gemini_767_case_miss_classification_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_MISS_CLASSIFICATION_767_POLICY_REVIEW)

    assert review["reviewer"] == "gemini_cli"
    assert review["model_requested"] == "gemini-2.5-flash"
    assert review["review_stage"] == "sanitized_miss_classification_policy_review_after_batch10"
    assert review["source_classification_report"] == (
        "docs/reports/holdout-miss-classification-blind-v1-767-cases-2026-07-12.json"
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
    assert review["policy_passed"] is True
    assert review["classification_changes_recommended"] == []
    assert {finding.get("case_id", finding.get("id")) for finding in review["findings"]} == {
        "expected-rechecks",
        "blind-ui-0147",
        "blind-it-0230",
    }


def test_holdout_batch10_miss_classification_confirmation_packet_is_sanitized() -> None:
    classification = load_json(MISS_CLASSIFICATION_767_CASE)
    packet = load_json(MAINTAINER_BATCH10_MISS_CLASSIFICATION_CONFIRMATION)

    review_ids = {
        case["id"]
        for case in classification["case_classifications"]
        if case.get("action", case.get("recommended_action"))
        in {"move_to_public_regression_candidate", "requires_expected_recheck"}
    }
    holdout_signal_ids = {
        case["id"]
        for case in classification["case_classifications"]
        if case.get("action", case.get("recommended_action")) == "keep_as_holdout_signal"
    }

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch10_miss_classification_after_767_case_sanity"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["sealed_content_policy"] | {
        "benchmark_rows_included": False,
    } == classification["sealed_content_policy"] | {
        "benchmark_rows_included": False,
    }
    assert packet["summary"] == {
        "total_review_cases": 20,
        "public_regression_candidate_cases": 16,
        "expected_recheck_cases": 4,
        "no_immediate_question": 32,
        "gemini_policy_passed": True,
        "classification_changes_recommended_by_gemini": 0,
        "gemini_info_findings": 3,
        "by_action": {
            "move_to_public_regression_candidate": 16,
            "requires_expected_recheck": 4,
        },
        "by_domain": {
            "formal": 3,
            "it": 9,
            "llm": 2,
            "ui": 6,
        },
        "by_risk": {
            "baseline_guard": 3,
            "candidate_gap": 17,
        },
        "non_idempotent_review_cases": 1,
    }
    assert {case["id"] for case in packet["cases"]} == review_ids
    assert set(packet["no_immediate_question_case_ids"]) == holdout_signal_ids
    assert len(packet["cases"]) == 20
    assert len(packet["no_immediate_question_case_ids"]) == 32
    assert all(case["sealed_values_omitted"] is True for case in packet["cases"])


def test_holdout_batch11_miss_classification_workflow_is_sanitized() -> None:
    classification = load_json(MISS_CLASSIFICATION_851_CASE)
    gemini = load_json(GEMINI_MISS_CLASSIFICATION_851_POLICY_REVIEW)
    packet = load_json(MAINTAINER_BATCH11_MISS_CLASSIFICATION_CONFIRMATION)

    forbidden_case_fields = {
        "acceptable",
        "actual",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    cases = classification["case_classifications"]
    review_ids = {case["id"] for case in cases if case["needs_maintainer_review"]}
    holdout_ids = {case["id"] for case in cases if not case["needs_maintainer_review"]}

    assert classification["report_type"] == "holdout_miss_classification"
    assert classification["review_stage"] == ("codex_first_pass_after_batch11_final_decision")
    assert classification["reviewer"] == "codex"
    assert classification["summary"]["classified_misses"] == 60
    assert classification["summary"]["previously_confirmed_holdout_signals"] == 32
    assert classification["summary"]["new_batch11_misses"] == 28
    assert classification["summary"]["by_action"] == {
        "keep_as_holdout_signal": 35,
        "requires_expected_recheck": 11,
        "move_to_public_regression_candidate": 14,
    }
    assert classification["gemini_review_policy"] == {
        "status": "completed_on_sanitized_metadata",
        "review_report": (
            "docs/reports/holdout-gemini-policy-review-miss-classification-"
            "blind-v1-851-cases-2026-07-14.json"
        ),
        "sealed_values_seen_by_gemini": False,
        "policy_passed": True,
        "classification_changes_recommended": 0,
    }
    assert len(cases) == 60
    assert len({case["id"] for case in cases}) == 60
    assert all(not (forbidden_case_fields & set(case)) for case in cases)
    assert all(case["sealed_values_omitted"] is True for case in cases)

    assert gemini["reviewer"] == "gemini_cli"
    assert gemini["model_requested"] == "gemini-2.5-pro"
    assert gemini["review_stage"] == ("gemini_policy_review_batch11_miss_classification")
    assert gemini["policy_passed"] is True
    assert gemini["classification_changes_recommended"] == []
    assert gemini["sealed_content_policy"]["sealed_values_seen_by_gemini"] is False

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch11_miss_classification_after_851_case_sanity"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["summary"] == {
        "total_review_cases": 25,
        "public_regression_candidate_cases": 14,
        "expected_recheck_cases": 11,
        "no_immediate_question": 35,
        "gemini_policy_passed": True,
        "classification_changes_recommended_by_gemini": 0,
        "by_action": {
            "requires_expected_recheck": 11,
            "move_to_public_regression_candidate": 14,
        },
        "by_domain": {"it": 10, "ui": 4, "llm": 3, "formal": 6, "social": 2},
        "by_risk": {
            "candidate_gap": 17,
            "baseline_guard": 3,
            "over_conversion_guard": 5,
        },
        "non_idempotent_review_cases": 1,
    }
    assert {case["id"] for case in packet["cases"]} == review_ids
    assert set(packet["no_immediate_question_case_ids"]) == holdout_ids
    assert all(case["sealed_values_omitted"] is True for case in packet["cases"])


def test_holdout_batch11_semantic_reaudit_narrows_maintainer_queue() -> None:
    codex = load_json(CODEX_BATCH11_SEMANTIC_REAUDIT)
    gemini = load_json(GEMINI_BATCH11_SEMANTIC_REAUDIT)
    packet = load_json(MAINTAINER_BATCH11_SEMANTIC_REAUDIT_CONFIRMATION)
    forbidden_case_fields = {
        "acceptable",
        "actual",
        "expected",
        "input",
        "output",
        "zhtw_output",
    }

    assert codex["review_stage"] == ("semantic_correctness_reaudit_after_overcorrection_concern")
    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["revised_policy"] == {
        "measure_conversion_correctness_not_house_style": True,
        "valid_taiwan_synonyms_are_acceptable": True,
        "do_not_tune_from_strict_style_preference": True,
        "maintainer_explicit_preferences_override_ai_advisory": True,
    }
    assert codex["summary"] == {
        "total_cases": 25,
        "by_revised_action": {
            "add_zhtw_output_as_acceptable_variant": 4,
            "move_to_public_regression_candidate": 10,
            "keep_as_strict_private_holdout_signal": 11,
        },
        "explicit_maintainer_preferences_recorded": 19,
        "pending_maintainer_confirmation": 6,
        "promotion_allowed": False,
    }
    assert len(codex["cases"]) == 25
    assert all(not (forbidden_case_fields & set(case)) for case in codex["cases"])

    assert gemini["review_stage"] == "independent_input_only_semantic_reaudit"
    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["independence_policy"] == {
        "codex_values_seen": False,
        "current_expected_seen": False,
        "zhtw_output_seen": False,
        "prior_miss_classification_seen": False,
        "input_only_cases_seen": True,
    }
    assert len(gemini["cases"]) == 25

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch11_semantic_reaudit_6_cases"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["summary"] == {
        "review_cases": 6,
        "acceptable_variant_cases": 4,
        "public_regression_candidate_cases": 2,
        "already_resolved_by_maintainer_preference": 19,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in packet["cases"]} == {
        "blind-it-0238",
        "blind-it-0242",
        "blind-it-0244",
        "blind-it-0246",
        "blind-ui-0189",
        "blind-llm-0140",
    }


def test_holdout_batch11_semantic_reaudit_final_decision_is_applied() -> None:
    decision = load_json(MAINTAINER_BATCH11_SEMANTIC_REAUDIT_FINAL_DECISION)
    expected = load_json(EXPECTED)
    pool_update = load_json(SEALED_POOL_UPDATE_BATCH11_SEMANTIC_REAUDIT)
    expected_by_id = {case["id"]: case for case in expected["cases"]}
    acceptable_ids = set(decision["confirmed_acceptable_variant_case_ids"])
    removed_ids = set(decision["removed_to_public_regression_candidate_case_ids"])
    strict_signal_ids = set(decision["strict_private_holdout_signal_case_ids"])

    assert decision["review_stage"] == ("maintainer_final_decision_batch11_semantic_reaudit")
    assert decision["decision"] == "review_ok"
    assert decision["maintainer"] == "tim"
    assert decision["expected_values_included"] is False
    assert decision["inputs_included"] is False
    assert decision["private_expected_sha256_after"] == (
        "066bcd60d16760a10eb8cdd54de61e8ff438fe4a7ffe971e8f814fc45563db2d"
    )
    assert decision["private_expected_sha256_after"] != private_expected_sha256()
    assert decision["source_inputs_sha256_after"] == (
        "3c35b332959c7a87410a0ba7c08d46aa98857b1c080155d275a8892d0f507fef"
    )
    assert decision["source_inputs_sha256_after"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert len(acceptable_ids) == 4
    assert len(removed_ids) == 10
    assert len(strict_signal_ids) == 11
    assert removed_ids == set(pool_update["removed_case_ids"])
    assert not (removed_ids & set(expected_by_id))
    assert strict_signal_ids <= set(expected_by_id)
    assert all(len(expected_by_id[case_id]["acceptable"]) == 1 for case_id in acceptable_ids)
    assert decision["summary"] == {
        "reviewed_semantic_reaudit_cases": 25,
        "maintainer_confirmed_acceptable_variants": 4,
        "removed_from_sealed_to_public_regression_candidates": 10,
        "strict_private_holdout_signals": 11,
        "remaining_private_expected_cases": 841,
        "remaining_sealed_input_cases": 841,
        "public_candidates_promoted_to_regression": 10,
        "regression_total_cases": 1218,
        "converter_or_dictionary_updated": True,
        "promotion_gate_pending": False,
        "candidate_dataset_total_cases": 186,
        "promotion_gate_passed": True,
        "full_sentence_mappings_added": 10,
        "identity_mappings_added": 10,
    }
