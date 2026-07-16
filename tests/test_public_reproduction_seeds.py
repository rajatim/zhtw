# zhtw:disable
"""Tests for independent public reproduction seed datasets."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SEEDS = ROOT / "benchmarks" / "accuracy" / "public-reproduction-seeds-v1.json"
BLIND_INPUTS = ROOT / "benchmarks" / "accuracy" / "blind-v1.inputs.json"
SOURCE_SIGNAL_REPORT = (
    "docs/reports/"
    "holdout-remaining-signal-summary-blind-v1-after-batch10-miss-review-2026-07-13.json"
)
GEMINI_POLICY_REVIEW = (
    "docs/reports/"
    "holdout-gemini-policy-review-remaining-signal-blind-v1-after-batch10-miss-review-2026-07-13.json"
)
CODEX_FIRST_PASS = (
    ROOT
    / "docs"
    / "reports"
    / "public-reproduction-codex-first-pass-after-batch10-remaining-signal-2026-07-13.json"
)
GEMINI_ADVISORY = (
    ROOT
    / "docs"
    / "reports"
    / "public-reproduction-gemini-advisory-after-batch10-remaining-signal-2026-07-13.json"
)
CODEX_GEMINI_DIFF = (
    ROOT
    / "docs"
    / "reports"
    / "public-reproduction-codex-gemini-diff-after-batch10-remaining-signal-2026-07-13.json"
)
MAINTAINER_PACKET = (
    ROOT
    / "docs"
    / "reports"
    / "public-reproduction-maintainer-confirmation-after-batch10-remaining-signal-2026-07-13.json"
)
FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "public-reproduction-maintainer-final-decision-after-batch10-remaining-signal-2026-07-13.json"
)
PROMOTION_GATE = (
    ROOT
    / "docs"
    / "reports"
    / "public-reproduction-promotion-gate-after-batch10-remaining-signal-2026-07-13.json"
)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_public_reproduction_seeds_are_input_only_and_metadata_derived() -> None:
    data = load_json(SEEDS)

    assert data["version"] == 1
    assert data["name"] == "public-reproduction-seeds-v1"
    assert data["status"] == "input_only_needs_review"
    assert data["source_policy"] == {
        "source_signal_report": SOURCE_SIGNAL_REPORT,
        "gemini_policy_review": GEMINI_POLICY_REVIEW,
        "sealed_values_used": False,
        "sealed_case_ids_used_as_case_inputs": False,
        "derived_from_metadata_only": [
            "domain",
            "risk",
            "issue_tags",
            "signal_category",
            "zhtw_output_idempotent",
        ],
        "forbidden_source_fields": [
            "input",
            "expected",
            "acceptable",
            "actual",
            "output",
            "normalized_output",
            "benchmark_rows",
        ],
    }
    assert data["review_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "converter_outputs_included": False,
        "codex_first_pass_required": True,
        "gemini_advisory_required": True,
        "maintainer_confirmation_required": True,
        "may_tune_converter_or_dictionary_now": False,
        "eligible_for_public_regression_only_after_human_expected_review": True,
    }

    cases = data["cases"]
    assert len(cases) == 32
    assert len({case["id"] for case in cases}) == len(cases)
    assert all(case["id"].startswith("public-repro-20260713-") for case in cases)
    assert data["stats"] == {
        "total_cases": 32,
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
        "by_signal_theme": {
            "formal_regional_over_conversion": 6,
            "high_risk_baseline_guard": 1,
            "high_risk_candidate_gap": 2,
            "high_risk_over_conversion": 5,
            "it_term_over_conversion": 3,
            "llm_term_over_conversion": 4,
            "social_regional_over_conversion": 6,
            "ui_term_over_conversion": 4,
            "ui_idempotency_followup": 1,
        },
    }
    assert Counter(case["domain"] for case in cases) == data["stats"]["by_domain"]
    assert Counter(case["risk"] for case in cases) == data["stats"]["by_risk"]
    assert Counter(case["signal_theme"] for case in cases) == data["stats"]["by_signal_theme"]


def test_public_reproduction_seed_cases_do_not_include_ground_truth_or_sealed_values() -> None:
    data = load_json(SEEDS)
    blind_inputs = load_json(BLIND_INPUTS)
    sealed_input_texts = {case["input"] for case in blind_inputs["cases"]}
    forbidden_case_fields = {
        "acceptable",
        "actual",
        "evaluations",
        "expected",
        "normalized_output",
        "output",
        "zhtw_output",
    }
    forbidden_text_fragments = {
        "請保留原文",
        "范例输出",
        "本案涉及",
        "留言裡",
        "不得以定型化契約條款排除責任",
        "跨行匯款手續費由使用者負擔",
    }

    for case in data["cases"]:
        assert not (forbidden_case_fields & set(case))
        assert case["input"]
        assert case["input"] not in sealed_input_texts
        assert "blind-" not in case["id"]
        assert "blind-" not in case["input"]
        assert not any(fragment in case["input"] for fragment in forbidden_text_fragments)
        assert case["source"] == {
            "type": "independent_public_reproduction_seed",
            "license": "MIT-compatible project original text",
            "sealed_text_used": False,
        }
        assert case["review"] == {"status": "needs_codex_first_pass"}
        assert case["notes"].startswith("Original public ")


def test_public_reproduction_codex_and_gemini_reports_are_advisory_only() -> None:
    seeds = load_json(SEEDS)
    seed_ids = {case["id"] for case in seeds["cases"]}
    codex = load_json(CODEX_FIRST_PASS)
    gemini = load_json(GEMINI_ADVISORY)

    assert codex["dataset"] == "public-reproduction-seeds-v1"
    assert codex["source_inputs"] == "benchmarks/accuracy/public-reproduction-seeds-v1.json"
    assert codex["reviewer"] == "codex"
    assert codex["review_stage"] == "first_pass_advisory"
    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["summary"] == {
        "total_cases": 32,
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
        "by_confidence": {"high": 19, "medium": 13},
        "review_needed": 13,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in codex["cases"]} == seed_ids
    assert all(case["codex_expected"] for case in codex["cases"])
    assert all(case["promotion_allowed"] is False for case in codex["cases"])

    assert gemini["dataset"] == "public-reproduction-seeds-v1"
    assert gemini["source_inputs"] == "benchmarks/accuracy/public-reproduction-seeds-v1.json"
    assert gemini["reviewer"] == "gemini_cli"
    assert gemini["model_requested"] == "gemini-2.5-pro"
    assert gemini["auth_type"] == "vertex-ai"
    assert gemini["review_stage"] == "independent_advisory"
    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert "did not see Codex first-pass expected values" in gemini["policy"]
    assert gemini["summary"] == {
        "total_cases": 32,
        "high_confidence": 32,
        "medium_confidence": 0,
        "low_confidence": 0,
        "review_needed": 0,
    }
    assert {case["id"] for case in gemini["cases"]} == seed_ids
    assert all(case["gemini_expected"] for case in gemini["cases"])


def test_public_reproduction_diff_and_maintainer_packet_are_not_ground_truth() -> None:
    diff = load_json(CODEX_GEMINI_DIFF)
    packet = load_json(MAINTAINER_PACKET)
    expected_diff_ids = {
        "public-repro-20260713-formal-0002",
        "public-repro-20260713-llm-0001",
        "public-repro-20260713-social-0003",
        "public-repro-20260713-ui-0002",
        "public-repro-20260713-ui-0004",
        "public-repro-20260713-ui-0005",
    }

    assert diff["review_stage"] == "codex_gemini_diff_review"
    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["summary"] == {
        "total_cases": 32,
        "primary_exact_matches": 26,
        "primary_differences": 6,
        "review_needed": 17,
        "no_immediate_question": 15,
        "by_recommendation": {
            "codex": 2,
            "codex_with_gemini_acceptable": 3,
            "gemini_with_codex_acceptable": 1,
            "shared_expected": 26,
        },
        "by_review_domain": {
            "formal": 2,
            "high_risk": 8,
            "it": 1,
            "llm": 2,
            "social": 1,
            "ui": 3,
        },
    }
    assert {
        case["id"] for case in diff["cases"] if not case["primary_exact_match"]
    } == expected_diff_ids
    assert all(case["promotion_allowed"] is False for case in diff["cases"])

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["summary"] == {
        "review_cases": 17,
        "no_immediate_question_cases": 15,
        "primary_differences": 6,
        "high_risk_review_cases": 8,
    }
    assert len(packet["review_cases"]) == 17
    assert expected_diff_ids <= {case["id"] for case in packet["review_cases"]}
    assert len(packet["no_immediate_question_case_ids"]) == 15


def test_public_reproduction_final_decision_is_human_confirmed_but_not_promoted() -> None:
    seeds = load_json(SEEDS)
    decision = load_json(FINAL_DECISION)
    seed_ids = {case["id"] for case in seeds["cases"]}

    assert decision["review_stage"] == "maintainer_final_decision"
    assert decision["maintainer"] == "tim"
    assert decision["decision"] == "review_ok"
    assert decision["approval_policy"] == "single_human_with_ai_advisory"
    assert decision["ground_truth"] is True
    assert decision["expected_values_included"] is True
    assert decision["acceptable_values_included"] is True
    assert decision["public_seed_inputs_updated"] is False
    assert decision["public_expected_dataset_updated"] is False
    assert decision["regression_updated"] is False
    assert decision["converter_or_dictionary_changed"] is False
    assert decision["promotion_status"] == "not_promoted_requires_gate"
    assert decision["promotion_allowed_now"] is False
    assert decision["eligible_for_public_regression_gate"] is True
    assert decision["may_tune_converter_or_dictionary_now"] is False
    assert decision["summary"] == {
        "total_cases": 32,
        "maintainer_confirmed_cases": 32,
        "confirmed_review_cases": 17,
        "accepted_no_immediate_question_cases": 15,
        "primary_differences_confirmed": 6,
        "primary_exact_matches_confirmed": 26,
        "high_risk_confirmed_cases": 8,
        "by_decision_source": {
            "accepted_no_immediate_question": 15,
            "maintainer_review_ok": 17,
        },
        "by_expected_source": {
            "human_adjudication": 17,
            "human_confirmed_no_immediate_question": 15,
        },
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
    }

    cases = decision["cases"]
    by_id = {case["id"]: case for case in cases}
    assert set(by_id) == seed_ids
    assert len(decision["confirmed_case_ids"]["review_packet"]) == 17
    assert len(decision["confirmed_case_ids"]["no_immediate_question"]) == 15
    assert all(case["expected"] for case in cases)
    assert all(case["approval_policy"] == "single_human_with_ai_advisory" for case in cases)
    assert all(case["promotion_status"] == "not_promoted_requires_gate" for case in cases)

    assert (
        by_id["public-repro-20260713-formal-0002"]["expected"]
        == "請將會議紀錄歸檔，並通知各部門負責人確認版本。"
    )
    assert (
        by_id["public-repro-20260713-llm-0001"]["expected"]
        == "提示範本會插入使用者問題、系統規則與輸出格式。"
    )
    assert (
        by_id["public-repro-20260713-ui-0002"]["expected"]
        == "下拉式選單展開時，目前選項會以藍色邊框標示。"
    )
    assert (
        "下拉選單展開時，目前選項會以藍色邊框標示。"
        in by_id["public-repro-20260713-ui-0002"]["acceptable"]
    )


def test_public_reproduction_promotion_gate_promotes_exact_matches_only() -> None:
    gate = load_json(PROMOTION_GATE)

    assert gate["decision"] == "promote_exact_matches_only"
    assert gate["promotion_policy"] == {
        "required_zhtw_match": True,
        "primary_expected_exact_match_required": True,
        "acceptable_variant_match_promoted": False,
        "acceptable_variant_reason": (
            "regression-v1 currently stores a single expected value per case"
        ),
        "converter_or_dictionary_changes_allowed": True,
    }
    assert gate["summary"] == {
        "total_cases": 32,
        "exact_match": 32,
        "acceptable_match_not_promoted": 0,
        "miss_not_promoted": 0,
        "promoted_to_regression": 32,
        "withheld_from_regression": 0,
        "regression_total_before": 1176,
        "regression_total_after": 1208,
        "converter_or_dictionary_changed": True,
        "regression_updated": True,
        "promotion_rule": "primary expected must match zhtw output exactly",
        "by_status": {
            "exact_match": 32,
        },
        "by_domain_promoted": {
            "formal": 6,
            "high_risk": 8,
            "it": 3,
            "llm": 4,
            "social": 6,
            "ui": 5,
        },
        "by_risk_promoted": {
            "baseline_guard": 1,
            "candidate_gap": 2,
            "over_conversion_guard": 29,
        },
    }
    assert len(gate["promoted_case_ids"]) == 32
    assert gate["acceptable_match_not_promoted_case_ids"] == []
    assert gate["miss_not_promoted_case_ids"] == []
