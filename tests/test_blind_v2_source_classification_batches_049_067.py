"""Blind-v2 source-classification tests for batches 049 through 067."""
# ruff: noqa: F403,F405

from tests._blind_v2_source_classification_support import *  # noqa: F403


def test_forty_ninth_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-049.json"
    codex_path = (
        prefix / "blind-v2-source-classification-codex-first-pass-batch-049-2026-07-29.json"
    )
    gemini_path = (
        prefix / "blind-v2-source-classification-gemini-independent-batch-049-2026-07-29.json"
    )
    adjustments_path = (
        prefix
        / "blind-v2-source-classification-codex-synthesis-adjustments-batch-049-2026-07-29.json"
    )
    synthesis_path = (
        prefix / "blind-v2-source-classification-codex-synthesis-batch-049-2026-07-29.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-049-2026-07-29.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-049-2026-07-29.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 49)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == "balanced-source-class-remaining-deterministic-sha256-v1"
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "kubernetes-docs-zh-cn-v1": 32,
            "ready-gov-cybersecurity-zh-hans-v1": 14,
            "ready-gov-evacuation-zh-hans-v1": 14,
            "ready-gov-kids-tornadoes-zh-hans-v1": 4,
            "zhtw-project-formal-llm-context-guard-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert codex["stats"] == {
        "total": 96,
        "eligible": 88,
        "excluded": 8,
        "high": 8,
        "medium": 88,
        "low": 0,
    }
    assert gemini["stats"] == {
        "total": 96,
        "eligible": 95,
        "excluded": 1,
        "high": 94,
        "medium": 2,
        "low": 0,
        "policy_violations": 0,
    }
    session_ids = gemini["execution"]["session_id"].split(",")
    assert len(session_ids) == len(set(session_ids)) == 12
    assert gemini["execution"]["tool_calls"] == 0
    assert gemini["execution"]["total_errors"] == 0
    stats, _ = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 34,
        "review_queue": 62,
        "by_field": {"eligible": 7, "script": 16, "domain": 33, "risk": 33},
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert adjustments["stats"] == {"total": 15}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-29",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 88,
        "excluded": 8,
        "by_selection_basis": {"agreement": 34, "codex": 47, "codex_synthesis": 15},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-29",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 62,
        "confirmed_exact_matches": 34,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-29",
        maintainer_decisions=decision,
    )


def test_fiftieth_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-050.json"
    codex_path = (
        prefix / "blind-v2-source-classification-codex-first-pass-batch-050-2026-07-29.json"
    )
    gemini_path = (
        prefix / "blind-v2-source-classification-gemini-independent-batch-050-2026-07-29.json"
    )
    adjustments_path = (
        prefix
        / "blind-v2-source-classification-codex-synthesis-adjustments-batch-050-2026-07-29.json"
    )
    synthesis_path = (
        prefix / "blind-v2-source-classification-codex-synthesis-batch-050-2026-07-29.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-050-2026-07-29.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-050-2026-07-29.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 50)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == "balanced-remaining-deterministic-sha256-v1"
    assert packet["stats"] == {
        "total": 80,
        "by_source": {
            "kubernetes-docs-zh-cn-v1": 34,
            "ready-gov-cybersecurity-zh-hans-v1": 9,
            "ready-gov-evacuation-zh-hans-v1": 3,
            "zhtw-project-formal-llm-context-guard-v1": 34,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert codex["stats"] == {
        "total": 80,
        "eligible": 77,
        "excluded": 3,
        "high": 3,
        "medium": 77,
        "low": 0,
    }
    assert gemini["stats"] == {
        "total": 80,
        "eligible": 76,
        "excluded": 4,
        "high": 79,
        "medium": 1,
        "low": 0,
        "policy_violations": 0,
    }
    session_ids = gemini["execution"]["session_id"].split(",")
    assert len(session_ids) == len(set(session_ids)) == 10
    assert gemini["execution"]["tool_calls"] == 0
    assert gemini["execution"]["total_errors"] == 0
    stats, _ = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 80,
        "exact": 28,
        "review_queue": 52,
        "by_field": {"eligible": 1, "script": 28, "domain": 11, "risk": 26},
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert adjustments["stats"] == {"total": 9}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-29",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 80,
        "eligible": 76,
        "excluded": 4,
        "by_selection_basis": {"agreement": 28, "codex": 43, "codex_synthesis": 9},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-29",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 80,
        "confirmed_cases": 80,
        "resolved_disagreements": 52,
        "confirmed_exact_matches": 28,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-29",
        maintainer_decisions=decision,
    )


def test_fifty_first_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-051.json"
    codex_path = (
        prefix / "blind-v2-source-classification-codex-first-pass-batch-051-2026-07-29.json"
    )
    gemini_path = (
        prefix / "blind-v2-source-classification-gemini-independent-batch-051-2026-07-29.json"
    )
    adjustments_path = (
        prefix
        / "blind-v2-source-classification-codex-synthesis-adjustments-batch-051-2026-07-29.json"
    )
    synthesis_path = (
        prefix / "blind-v2-source-classification-codex-synthesis-batch-051-2026-07-29.json"
    )
    decision_path = (
        prefix / "blind-v2-source-classification-maintainer-decision-batch-051-2026-07-29.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-051-2026-07-29.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 51)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == ("balanced-source-class-remaining-deterministic-sha256-v1")
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "kubernetes-docs-zh-cn-v1": 32,
            "ready-gov-are-you-ready-guide-simplified-v1": 32,
            "zhtw-project-formal-llm-evidence-guard-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert codex["stats"] == {
        "total": 96,
        "eligible": 90,
        "excluded": 6,
        "high": 6,
        "medium": 90,
        "low": 0,
    }
    assert gemini["stats"] == {
        "total": 96,
        "eligible": 91,
        "excluded": 5,
        "high": 96,
        "medium": 0,
        "low": 0,
        "policy_violations": 0,
    }
    session_ids = gemini["execution"]["session_id"].split(",")
    assert len(session_ids) == len(set(session_ids)) == 6
    assert gemini["execution"]["tool_calls"] == 0
    assert gemini["execution"]["total_errors"] == 0
    stats, _ = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 29,
        "review_queue": 67,
        "by_field": {"eligible": 1, "script": 17, "domain": 12, "risk": 53},
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert adjustments["stats"] == {"total": 67}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-29",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 90,
        "excluded": 6,
        "by_selection_basis": {"agreement": 29, "codex_synthesis": 67},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-29",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 67,
        "confirmed_exact_matches": 29,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-29",
        maintainer_decisions=decision,
    )


def test_fifty_second_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-052.json"
    codex_path = (
        prefix / "blind-v2-source-classification-codex-first-pass-batch-052-2026-07-29.json"
    )
    gemini_path = (
        prefix / "blind-v2-source-classification-gemini-independent-batch-052-2026-07-29.json"
    )
    adjustments_path = (
        prefix
        / "blind-v2-source-classification-codex-synthesis-adjustments-batch-052-2026-07-29.json"
    )
    synthesis_path = (
        prefix / "blind-v2-source-classification-codex-synthesis-batch-052-2026-07-29.json"
    )
    decision_path = (
        prefix / "blind-v2-source-classification-maintainer-decision-batch-052-2026-07-29.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-052-2026-07-29.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 52)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == ("balanced-source-class-remaining-deterministic-sha256-v1")
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "kubernetes-docs-zh-cn-v1": 32,
            "ready-gov-are-you-ready-guide-simplified-v1": 32,
            "zhtw-project-formal-llm-evidence-guard-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert codex["stats"] == {
        "total": 96,
        "eligible": 81,
        "excluded": 15,
        "high": 15,
        "medium": 81,
        "low": 0,
    }
    assert gemini["stats"] == {
        "total": 96,
        "eligible": 89,
        "excluded": 7,
        "high": 95,
        "medium": 1,
        "low": 0,
        "policy_violations": 0,
    }
    session_ids = gemini["execution"]["session_id"].split(",")
    assert len(session_ids) == len(set(session_ids)) == 6
    assert gemini["execution"]["tool_calls"] == 0
    assert gemini["execution"]["total_errors"] == 0
    stats, _ = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 51,
        "review_queue": 45,
        "by_field": {"eligible": 8, "script": 3, "domain": 24, "risk": 35},
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert adjustments["stats"] == {"total": 45}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-29",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 81,
        "excluded": 15,
        "by_selection_basis": {"agreement": 51, "codex_synthesis": 45},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-29",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 45,
        "confirmed_exact_matches": 51,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-29",
        maintainer_decisions=decision,
    )


def test_fifty_third_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-053.json"
    codex_path = (
        prefix / "blind-v2-source-classification-codex-first-pass-batch-053-2026-07-29.json"
    )
    gemini_path = (
        prefix / "blind-v2-source-classification-gemini-independent-batch-053-2026-07-29.json"
    )
    adjustments_path = (
        prefix
        / "blind-v2-source-classification-codex-synthesis-adjustments-batch-053-2026-07-29.json"
    )
    synthesis_path = (
        prefix / "blind-v2-source-classification-codex-synthesis-batch-053-2026-07-29.json"
    )
    decision_path = (
        prefix / "blind-v2-source-classification-maintainer-decision-batch-053-2026-07-30.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-053-2026-07-29.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 53)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == ("balanced-source-class-remaining-deterministic-sha256-v1")
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "kubernetes-docs-zh-cn-v1": 32,
            "ready-gov-are-you-ready-guide-simplified-v1": 32,
            "zhtw-project-formal-llm-evidence-guard-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert codex["stats"] == {
        "total": 96,
        "eligible": 87,
        "excluded": 9,
        "high": 9,
        "medium": 87,
        "low": 0,
    }
    assert gemini["stats"] == {
        "total": 96,
        "eligible": 92,
        "excluded": 4,
        "high": 95,
        "medium": 1,
        "low": 0,
        "policy_violations": 0,
    }
    session_ids = gemini["execution"]["session_id"].split(",")
    assert len(session_ids) == len(set(session_ids)) == 6
    assert gemini["execution"]["tool_calls"] == 0
    assert gemini["execution"]["total_errors"] == 0
    stats, _ = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 40,
        "review_queue": 56,
        "by_field": {"eligible": 7, "script": 5, "domain": 16, "risk": 53},
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert adjustments["stats"] == {"total": 56}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-29",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 86,
        "excluded": 10,
        "by_selection_basis": {"agreement": 40, "codex_synthesis": 56},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-30",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 56,
        "confirmed_exact_matches": 40,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-29",
        maintainer_decisions=decision,
    )


def test_fifty_fourth_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-054.json"
    codex_path = (
        prefix / "blind-v2-source-classification-codex-first-pass-batch-054-2026-07-30.json"
    )
    gemini_path = (
        prefix / "blind-v2-source-classification-gemini-independent-batch-054-2026-07-30.json"
    )
    adjustments_path = (
        prefix
        / "blind-v2-source-classification-codex-synthesis-adjustments-batch-054-2026-07-30.json"
    )
    synthesis_path = (
        prefix / "blind-v2-source-classification-codex-synthesis-batch-054-2026-07-30.json"
    )
    decision_path = (
        prefix / "blind-v2-source-classification-maintainer-decision-batch-054-2026-07-30.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-054-2026-07-30.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 54)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == ("balanced-source-class-remaining-deterministic-sha256-v1")
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "kubernetes-docs-zh-cn-v1": 32,
            "ready-gov-are-you-ready-guide-simplified-v1": 32,
            "zhtw-project-ui-social-baseline-guard-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert codex["stats"] == {
        "total": 96,
        "eligible": 91,
        "excluded": 5,
        "high": 5,
        "medium": 91,
        "low": 0,
    }
    assert gemini["stats"] == {
        "total": 96,
        "eligible": 95,
        "excluded": 1,
        "high": 94,
        "medium": 2,
        "low": 0,
        "policy_violations": 0,
    }
    session_ids = gemini["execution"]["session_id"].split(",")
    assert len(session_ids) == len(set(session_ids)) == 6
    assert gemini["execution"]["tool_calls"] == 0
    assert gemini["execution"]["total_errors"] == 0
    stats, _ = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 41,
        "review_queue": 55,
        "by_field": {"eligible": 4, "script": 8, "domain": 29, "risk": 40},
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert adjustments["stats"] == {"total": 55}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-30",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 91,
        "excluded": 5,
        "by_selection_basis": {"agreement": 41, "codex_synthesis": 55},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-30",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 55,
        "confirmed_exact_matches": 41,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-30",
        maintainer_decisions=decision,
    )


def test_fifty_fifth_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-055.json"
    codex_path = (
        prefix / "blind-v2-source-classification-codex-first-pass-batch-055-2026-07-30.json"
    )
    gemini_path = (
        prefix / "blind-v2-source-classification-gemini-independent-batch-055-2026-07-30.json"
    )
    adjustments_path = (
        prefix
        / "blind-v2-source-classification-codex-synthesis-adjustments-batch-055-2026-07-30.json"
    )
    synthesis_path = (
        prefix / "blind-v2-source-classification-codex-synthesis-batch-055-2026-07-30.json"
    )
    decision_path = (
        prefix / "blind-v2-source-classification-maintainer-decision-batch-055-2026-07-30.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-055-2026-07-30.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 55)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == ("balanced-source-class-remaining-deterministic-sha256-v1")
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "aosp-framework-zh-rcn-v1": 32,
            "ready-gov-are-you-ready-guide-simplified-v1": 32,
            "zhtw-project-ui-social-baseline-guard-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert codex["stats"] == {
        "total": 96,
        "eligible": 89,
        "excluded": 7,
        "high": 7,
        "medium": 89,
        "low": 0,
    }
    assert gemini["stats"] == {
        "total": 96,
        "eligible": 94,
        "excluded": 2,
        "high": 95,
        "medium": 1,
        "low": 0,
        "policy_violations": 0,
    }
    session_ids = gemini["execution"]["session_id"].split(",")
    assert len(session_ids) == len(set(session_ids)) == 6
    assert gemini["execution"]["tool_calls"] == 0
    assert gemini["execution"]["total_errors"] == 0
    stats, _ = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 61,
        "review_queue": 35,
        "by_field": {"eligible": 5, "script": 0, "domain": 19, "risk": 25},
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert adjustments["stats"] == {"total": 35}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-30",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 90,
        "excluded": 6,
        "by_selection_basis": {"agreement": 61, "codex_synthesis": 35},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-30",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 35,
        "confirmed_exact_matches": 61,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-30",
        maintainer_decisions=decision,
    )


def test_fifty_sixth_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-056.json"
    codex_path = (
        prefix / "blind-v2-source-classification-codex-first-pass-batch-056-2026-07-30.json"
    )
    gemini_path = (
        prefix / "blind-v2-source-classification-gemini-independent-batch-056-2026-07-30.json"
    )
    adjustments_path = (
        prefix
        / "blind-v2-source-classification-codex-synthesis-adjustments-batch-056-2026-07-30.json"
    )
    synthesis_path = (
        prefix / "blind-v2-source-classification-codex-synthesis-batch-056-2026-07-30.json"
    )
    decision_path = (
        prefix / "blind-v2-source-classification-maintainer-decision-batch-056-2026-07-30.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-056-2026-07-30.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 56)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == ("balanced-source-class-remaining-deterministic-sha256-v1")
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "aosp-framework-zh-rcn-v1": 32,
            "ready-gov-are-you-ready-guide-simplified-v1": 32,
            "zhtw-project-ui-social-baseline-guard-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert codex["stats"] == {
        "total": 96,
        "eligible": 90,
        "excluded": 6,
        "high": 6,
        "medium": 90,
        "low": 0,
    }
    assert gemini["stats"] == {
        "total": 96,
        "eligible": 94,
        "excluded": 2,
        "high": 95,
        "medium": 1,
        "low": 0,
        "policy_violations": 0,
    }
    session_ids = gemini["execution"]["session_id"].split(",")
    assert len(session_ids) == len(set(session_ids)) == 6
    assert gemini["execution"]["tool_calls"] == 0
    assert gemini["execution"]["total_errors"] == 0
    stats, _ = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 63,
        "review_queue": 33,
        "by_field": {"eligible": 4, "script": 2, "domain": 13, "risk": 27},
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert adjustments["stats"] == {"total": 33}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-30",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 91,
        "excluded": 5,
        "by_selection_basis": {"agreement": 63, "codex_synthesis": 33},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-30",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 33,
        "confirmed_exact_matches": 63,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-30",
        maintainer_decisions=decision,
    )


def test_fifty_seventh_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-057.json"
    codex_path = (
        prefix / "blind-v2-source-classification-codex-first-pass-batch-057-2026-07-30.json"
    )
    gemini_path = (
        prefix / "blind-v2-source-classification-gemini-independent-batch-057-2026-07-30.json"
    )
    adjustments_path = (
        prefix
        / "blind-v2-source-classification-codex-synthesis-adjustments-batch-057-2026-07-30.json"
    )
    synthesis_path = (
        prefix / "blind-v2-source-classification-codex-synthesis-batch-057-2026-07-30.json"
    )
    decision_path = (
        prefix / "blind-v2-source-classification-maintainer-decision-batch-057-2026-07-30.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-057-2026-07-30.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 57)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == ("balanced-source-class-remaining-deterministic-sha256-v1")
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "aosp-framework-zh-rcn-v1": 32,
            "ready-gov-are-you-ready-guide-simplified-v1": 32,
            "zhtw-project-llm-formal-reasoning-guard-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert codex["stats"] == {
        "total": 96,
        "eligible": 92,
        "excluded": 4,
        "high": 4,
        "medium": 92,
        "low": 0,
    }
    assert gemini["stats"] == {
        "total": 96,
        "eligible": 94,
        "excluded": 2,
        "high": 93,
        "medium": 3,
        "low": 0,
        "policy_violations": 0,
    }
    session_ids = gemini["execution"]["session_id"].split(",")
    assert len(session_ids) == len(set(session_ids)) == 6
    assert gemini["execution"]["tool_calls"] == 0
    assert gemini["execution"]["total_errors"] == 0
    assert gemini["execution"]["discarded_session_id"] not in session_ids
    stats, _ = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 31,
        "review_queue": 65,
        "by_field": {"eligible": 2, "script": 0, "domain": 33, "risk": 45},
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert adjustments["stats"] == {"total": 65}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-30",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 93,
        "excluded": 3,
        "by_selection_basis": {"agreement": 31, "codex_synthesis": 65},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-30",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 65,
        "confirmed_exact_matches": 31,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-30",
        maintainer_decisions=decision,
    )


def test_fifty_eighth_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-058.json"
    codex_path = (
        prefix / "blind-v2-source-classification-codex-first-pass-batch-058-2026-07-30.json"
    )
    gemini_path = (
        prefix / "blind-v2-source-classification-gemini-independent-batch-058-2026-07-30.json"
    )
    adjustments_path = (
        prefix
        / "blind-v2-source-classification-codex-synthesis-adjustments-batch-058-2026-07-30.json"
    )
    synthesis_path = (
        prefix / "blind-v2-source-classification-codex-synthesis-batch-058-2026-07-30.json"
    )
    decision_path = (
        prefix / "blind-v2-source-classification-maintainer-decision-batch-058-2026-07-30.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-058-2026-07-30.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 58)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == ("balanced-source-class-remaining-deterministic-sha256-v1")
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "aosp-framework-zh-rcn-v1": 32,
            "ready-gov-are-you-ready-guide-simplified-v1": 32,
            "zhtw-project-llm-formal-reasoning-guard-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert codex["stats"] == {
        "total": 96,
        "eligible": 91,
        "excluded": 5,
        "high": 5,
        "medium": 91,
        "low": 0,
    }
    assert gemini["stats"] == {
        "total": 96,
        "eligible": 93,
        "excluded": 3,
        "high": 96,
        "medium": 0,
        "low": 0,
        "policy_violations": 0,
    }
    execution = gemini["execution"]
    conversation_ids = execution["conversation_id"].split(",")
    assert execution["cli"] == "agy"
    assert execution["cli_version"] == "1.1.8"
    assert execution["mode"] == "plan"
    assert len(conversation_ids) == len(set(conversation_ids)) == 6
    assert execution["accepted_conversations"] == 6
    assert execution["turns_per_conversation"] == [1] * 6
    assert execution["tool_calls"] == 0
    assert execution["total_errors"] == 0
    assert "none of their output was used" in execution["discarded_execution"]
    stats, _ = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 45,
        "review_queue": 51,
        "by_field": {"eligible": 2, "script": 21, "domain": 2, "risk": 47},
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert adjustments["stats"] == {"total": 51}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-30",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 93,
        "excluded": 3,
        "by_selection_basis": {"agreement": 45, "codex_synthesis": 51},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-30",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 51,
        "confirmed_exact_matches": 45,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-30",
        maintainer_decisions=decision,
    )


def test_fifty_ninth_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-059.json"
    codex_path = (
        prefix / "blind-v2-source-classification-codex-first-pass-batch-059-2026-07-30.json"
    )
    gemini_path = (
        prefix / "blind-v2-source-classification-gemini-independent-batch-059-2026-07-30.json"
    )
    adjustments_path = (
        prefix
        / "blind-v2-source-classification-codex-synthesis-adjustments-batch-059-2026-07-30.json"
    )
    synthesis_path = (
        prefix / "blind-v2-source-classification-codex-synthesis-batch-059-2026-07-30.json"
    )
    decision_path = (
        prefix / "blind-v2-source-classification-maintainer-decision-batch-059-2026-07-30.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-059-2026-07-30.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 59)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == ("balanced-source-class-remaining-deterministic-sha256-v1")
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "aosp-framework-zh-rcn-v1": 32,
            "ready-gov-are-you-ready-guide-simplified-v1": 32,
            "zhtw-project-llm-formal-reasoning-guard-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert codex["stats"] == {
        "total": 96,
        "eligible": 90,
        "excluded": 6,
        "high": 6,
        "medium": 90,
        "low": 0,
    }
    assert gemini["stats"] == {
        "total": 96,
        "eligible": 92,
        "excluded": 4,
        "high": 96,
        "medium": 0,
        "low": 0,
        "policy_violations": 0,
    }
    execution = gemini["execution"]
    conversation_ids = execution["conversation_id"].split(",")
    assert execution["cli"] == "agy"
    assert execution["cli_version"] == "1.1.8"
    assert execution["mode"] == "plan"
    assert len(conversation_ids) == len(set(conversation_ids)) == 6
    assert execution["accepted_conversations"] == 6
    assert execution["turns_per_conversation"] == [1] * 6
    assert execution["tool_calls"] == 0
    assert execution["total_errors"] == 0
    stats, _ = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 30,
        "review_queue": 66,
        "by_field": {"eligible": 4, "script": 22, "domain": 14, "risk": 58},
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert adjustments["stats"] == {"total": 66}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-30",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 90,
        "excluded": 6,
        "by_selection_basis": {"agreement": 30, "codex_synthesis": 66},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-30",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 66,
        "confirmed_exact_matches": 30,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-30",
        maintainer_decisions=decision,
    )


def test_sixtieth_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-060.json"
    codex_path = (
        prefix / "blind-v2-source-classification-codex-first-pass-batch-060-2026-07-30.json"
    )
    gemini_path = (
        prefix / "blind-v2-source-classification-gemini-independent-batch-060-2026-07-30.json"
    )
    adjustments_path = (
        prefix
        / "blind-v2-source-classification-codex-synthesis-adjustments-batch-060-2026-07-30.json"
    )
    synthesis_path = (
        prefix / "blind-v2-source-classification-codex-synthesis-batch-060-2026-07-30.json"
    )
    decision_path = (
        prefix / "blind-v2-source-classification-maintainer-decision-batch-060-2026-07-30.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-060-2026-07-30.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 60)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == ("balanced-source-class-remaining-deterministic-sha256-v1")
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "aosp-framework-zh-rcn-v1": 32,
            "ready-gov-are-you-ready-guide-simplified-v1": 32,
            "zhtw-project-llm-formal-operations-guard-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert codex["stats"] == {
        "total": 96,
        "eligible": 88,
        "excluded": 8,
        "high": 8,
        "medium": 88,
        "low": 0,
    }
    assert gemini["stats"] == {
        "total": 96,
        "eligible": 89,
        "excluded": 7,
        "high": 96,
        "medium": 0,
        "low": 0,
        "policy_violations": 0,
    }
    execution = gemini["execution"]
    conversation_ids = execution["conversation_id"].split(",")
    assert execution["cli"] == "agy"
    assert execution["cli_version"] == "1.1.8"
    assert execution["mode"] == "plan"
    assert len(conversation_ids) == len(set(conversation_ids)) == 6
    assert execution["accepted_conversations"] == 6
    assert execution["turns_per_conversation"] == [1] * 6
    assert execution["tool_calls"] == 0
    assert execution["total_errors"] == 0
    stats, _ = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 47,
        "review_queue": 49,
        "by_field": {"eligible": 1, "script": 21, "domain": 24, "risk": 36},
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert adjustments["stats"] == {"total": 49}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-30",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 88,
        "excluded": 8,
        "by_selection_basis": {"agreement": 47, "codex_synthesis": 49},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-30",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 49,
        "confirmed_exact_matches": 47,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-30",
        maintainer_decisions=decision,
    )


def test_sixty_first_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-061.json"
    codex_path = (
        prefix / "blind-v2-source-classification-codex-first-pass-batch-061-2026-07-30.json"
    )
    gemini_path = (
        prefix / "blind-v2-source-classification-gemini-independent-batch-061-2026-07-30.json"
    )
    synthesis_path = (
        prefix / "blind-v2-source-classification-codex-synthesis-batch-061-2026-07-30.json"
    )
    decision_path = (
        prefix / "blind-v2-source-classification-maintainer-decision-batch-061-2026-07-30.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-061-2026-07-30.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 61)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == ("balanced-source-class-remaining-deterministic-sha256-v1")
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "aosp-framework-zh-rcn-v1": 32,
            "ready-gov-are-you-ready-guide-simplified-v1": 32,
            "zhtw-project-llm-formal-operations-guard-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert codex["stats"] == {
        "total": 96,
        "eligible": 93,
        "excluded": 3,
        "high": 3,
        "medium": 93,
        "low": 0,
    }
    assert gemini["stats"] == {
        "total": 96,
        "eligible": 93,
        "excluded": 3,
        "high": 96,
        "medium": 0,
        "low": 0,
        "policy_violations": 0,
    }
    execution = gemini["execution"]
    conversation_ids = execution["conversation_id"].split(",")
    assert execution["cli"] == "agy"
    assert execution["cli_version"] == "1.1.8"
    assert execution["mode"] == "plan"
    assert len(conversation_ids) == len(set(conversation_ids)) == 6
    assert execution["accepted_conversations"] == 6
    assert execution["attempted_review_conversations"] == 8
    assert execution["turns_per_conversation"] == [1] * 6
    assert execution["tool_calls"] == 0
    assert execution["total_errors"] == 1
    assert execution["discarded_conversations"] == [
        {
            "conversation_id": "a0a3a8ad-8d8a-4c2b-b6d8-6e7a986aad34",
            "reason": "structured_output_schema_error_before_token_submission",
        },
        {
            "conversation_id": "50b49118-8b5f-4322-a49a-e640a845ab7e",
            "reason": "incomplete_case_coverage_15_of_16",
        },
    ]
    stats, _ = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 96,
        "review_queue": 0,
        "by_field": {"eligible": 0, "script": 0, "domain": 0, "risk": 0},
    }
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-30",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 93,
        "excluded": 3,
        "by_selection_basis": {"agreement": 96},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-30",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 0,
        "confirmed_exact_matches": 96,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-30",
        maintainer_decisions=decision,
    )


def test_sixty_second_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-062.json"
    codex_path = (
        prefix / "blind-v2-source-classification-codex-first-pass-batch-062-2026-07-30.json"
    )
    gemini_path = (
        prefix / "blind-v2-source-classification-gemini-independent-batch-062-2026-07-30.json"
    )
    adjustments_path = (
        prefix
        / "blind-v2-source-classification-codex-synthesis-adjustments-batch-062-2026-07-30.json"
    )
    synthesis_path = (
        prefix / "blind-v2-source-classification-codex-synthesis-batch-062-2026-07-30.json"
    )
    decision_path = (
        prefix / "blind-v2-source-classification-maintainer-decision-batch-062-2026-07-30.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-062-2026-07-30.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 62)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == ("balanced-source-class-remaining-deterministic-sha256-v1")
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "aosp-framework-zh-rcn-v1": 32,
            "ready-gov-are-you-ready-guide-simplified-v1": 32,
            "zhtw-project-llm-formal-operations-guard-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert codex["stats"] == {
        "total": 96,
        "eligible": 95,
        "excluded": 1,
        "high": 1,
        "medium": 95,
        "low": 0,
    }
    assert gemini["stats"] == {
        "total": 96,
        "eligible": 93,
        "excluded": 3,
        "high": 96,
        "medium": 0,
        "low": 0,
        "policy_violations": 0,
    }
    execution = gemini["execution"]
    conversation_ids = execution["conversation_id"].split(",")
    assert execution["cli"] == "agy"
    assert execution["cli_version"] == "1.1.8"
    assert execution["mode"] == "plan"
    assert len(conversation_ids) == len(set(conversation_ids)) == 6
    assert execution["accepted_conversations"] == 6
    assert execution["attempted_review_conversations"] == 6
    assert execution["discarded_conversations"] == []
    assert execution["turns_per_conversation"] == [1] * 6
    assert execution["tool_calls"] == 0
    assert execution["total_errors"] == 0
    stats, _ = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 94,
        "review_queue": 2,
        "by_field": {"eligible": 2, "script": 0, "domain": 2, "risk": 2},
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert adjustments["stats"] == {"total": 2}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-30",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 95,
        "excluded": 1,
        "by_selection_basis": {"agreement": 94, "codex_synthesis": 2},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-30",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 2,
        "confirmed_exact_matches": 94,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-30",
        maintainer_decisions=decision,
    )


def test_sixty_third_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-063.json"
    codex_path = (
        prefix / "blind-v2-source-classification-codex-first-pass-batch-063-2026-07-30.json"
    )
    gemini_path = (
        prefix / "blind-v2-source-classification-gemini-independent-batch-063-2026-07-30.json"
    )
    adjustments_path = (
        prefix
        / "blind-v2-source-classification-codex-synthesis-adjustments-batch-063-2026-07-30.json"
    )
    synthesis_path = (
        prefix / "blind-v2-source-classification-codex-synthesis-batch-063-2026-07-30.json"
    )
    decision_path = (
        prefix / "blind-v2-source-classification-maintainer-decision-batch-063-2026-07-30.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-063-2026-07-30.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 63)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == ("balanced-source-class-remaining-deterministic-sha256-v1")
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "aosp-framework-zh-rcn-v1": 32,
            "ready-gov-are-you-ready-guide-simplified-v1": 32,
            "zhtw-project-social-formal-context-guard-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert codex["stats"] == {
        "total": 96,
        "eligible": 91,
        "excluded": 5,
        "high": 5,
        "medium": 91,
        "low": 0,
    }
    assert gemini["stats"] == {
        "total": 96,
        "eligible": 93,
        "excluded": 3,
        "high": 96,
        "medium": 0,
        "low": 0,
        "policy_violations": 0,
    }
    execution = gemini["execution"]
    conversation_ids = execution["conversation_id"].split(",")
    assert execution["cli"] == "agy"
    assert execution["cli_version"] == "1.1.8"
    assert execution["mode"] == "plan"
    assert len(conversation_ids) == len(set(conversation_ids)) == 6
    assert execution["accepted_conversations"] == 6
    assert execution["attempted_review_conversations"] == 6
    assert execution["discarded_conversations"] == []
    assert execution["turns_per_conversation"] == [1] * 6
    assert execution["tool_calls"] == 0
    assert execution["total_errors"] == 0
    stats, _ = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 94,
        "review_queue": 2,
        "by_field": {"eligible": 2, "script": 0, "domain": 2, "risk": 2},
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert adjustments["stats"] == {"total": 2}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-30",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 92,
        "excluded": 4,
        "by_selection_basis": {"agreement": 94, "codex_synthesis": 2},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-30",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 2,
        "confirmed_exact_matches": 94,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-30",
        maintainer_decisions=decision,
    )


def test_sixty_fourth_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-064.json"
    codex_path = (
        prefix / "blind-v2-source-classification-codex-first-pass-batch-064-2026-07-30.json"
    )
    gemini_path = (
        prefix / "blind-v2-source-classification-gemini-independent-batch-064-2026-07-30.json"
    )
    adjustments_path = (
        prefix
        / "blind-v2-source-classification-codex-synthesis-adjustments-batch-064-2026-07-30.json"
    )
    synthesis_path = (
        prefix / "blind-v2-source-classification-codex-synthesis-batch-064-2026-07-30.json"
    )
    decision_path = (
        prefix / "blind-v2-source-classification-maintainer-decision-batch-064-2026-07-30.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-064-2026-07-30.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 64)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == ("balanced-source-class-remaining-deterministic-sha256-v1")
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "chromium-strings-zh-cn-v1": 32,
            "ready-gov-are-you-ready-guide-simplified-v1": 32,
            "zhtw-project-social-formal-context-guard-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert codex["stats"] == {
        "total": 96,
        "eligible": 90,
        "excluded": 6,
        "high": 6,
        "medium": 90,
        "low": 0,
    }
    assert gemini["stats"] == {
        "total": 96,
        "eligible": 88,
        "excluded": 8,
        "high": 96,
        "medium": 0,
        "low": 0,
        "policy_violations": 0,
    }
    execution = gemini["execution"]
    conversation_ids = execution["conversation_id"].split(",")
    assert execution["cli"] == "agy"
    assert execution["cli_version"] == "1.1.8"
    assert execution["mode"] == "plan"
    assert len(conversation_ids) == len(set(conversation_ids)) == 6
    assert execution["accepted_conversations"] == 6
    assert execution["attempted_review_conversations"] == 10
    assert len(execution["discarded_conversations"]) == 4
    assert {item["reason"] for item in execution["discarded_conversations"]} == {
        "markdown_fenced_response_invalid_raw_json"
    }
    assert execution["turns_per_conversation"] == [1] * 6
    assert execution["tool_calls"] == 0
    assert execution["total_errors"] == 0
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 94,
        "review_queue": 2,
        "by_field": {"eligible": 2, "script": 0, "domain": 2, "risk": 2},
    }
    assert len(differences) == 2
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert adjustments["stats"] == {"total": 2}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-30",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 88,
        "excluded": 8,
        "by_selection_basis": {"agreement": 94, "codex_synthesis": 2},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-30",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 2,
        "confirmed_exact_matches": 94,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-30",
        maintainer_decisions=decision,
    )


def test_sixty_fifth_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-065.json"
    codex_path = (
        prefix / "blind-v2-source-classification-codex-first-pass-batch-065-2026-07-30.json"
    )
    gemini_path = (
        prefix / "blind-v2-source-classification-gemini-independent-batch-065-2026-07-30.json"
    )
    synthesis_path = (
        prefix / "blind-v2-source-classification-codex-synthesis-batch-065-2026-07-30.json"
    )
    decision_path = (
        prefix / "blind-v2-source-classification-maintainer-decision-batch-065-2026-07-30.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-065-2026-07-30.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 65)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == ("balanced-source-class-remaining-deterministic-sha256-v1")
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "chromium-strings-zh-cn-v1": 32,
            "ready-gov-are-you-ready-guide-simplified-v1": 32,
            "zhtw-project-social-formal-context-guard-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert codex["stats"] == {
        "total": 96,
        "eligible": 90,
        "excluded": 6,
        "high": 6,
        "medium": 90,
        "low": 0,
    }
    assert gemini["stats"] == {
        "total": 96,
        "eligible": 90,
        "excluded": 6,
        "high": 96,
        "medium": 0,
        "low": 0,
        "policy_violations": 0,
    }
    execution = gemini["execution"]
    conversation_ids = execution["conversation_id"].split(",")
    assert execution["cli"] == "agy"
    assert execution["cli_version"] == "1.1.8"
    assert execution["mode"] == "plan"
    assert len(conversation_ids) == len(set(conversation_ids)) == 6
    assert execution["accepted_conversations"] == 6
    assert execution["attempted_review_conversations"] == 6
    assert execution["discarded_conversations"] == []
    assert execution["turns_per_conversation"] == [1] * 6
    assert execution["tool_calls"] == 0
    assert execution["total_errors"] == 0
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 96,
        "review_queue": 0,
        "by_field": {"eligible": 0, "script": 0, "domain": 0, "risk": 0},
    }
    assert differences == []
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-30",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 90,
        "excluded": 6,
        "by_selection_basis": {"agreement": 96},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-30",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 0,
        "confirmed_exact_matches": 96,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-30",
        maintainer_decisions=decision,
    )


def test_sixty_sixth_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-066.json"
    codex_path = (
        prefix / "blind-v2-source-classification-codex-first-pass-batch-066-2026-07-30.json"
    )
    gemini_path = (
        prefix / "blind-v2-source-classification-gemini-independent-batch-066-2026-07-30.json"
    )
    adjustments_path = (
        prefix
        / "blind-v2-source-classification-codex-synthesis-adjustments-batch-066-2026-07-30.json"
    )
    synthesis_path = (
        prefix / "blind-v2-source-classification-codex-synthesis-batch-066-2026-07-30.json"
    )
    decision_path = (
        prefix / "blind-v2-source-classification-maintainer-decision-batch-066-2026-07-30.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-066-2026-07-30.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 66)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == ("balanced-source-class-remaining-deterministic-sha256-v1")
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "chromium-strings-zh-cn-v1": 32,
            "ready-gov-are-you-ready-guide-simplified-v1": 32,
            "zhtw-project-social-formal-ambiguity-guard-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert codex["stats"] == {
        "total": 96,
        "eligible": 90,
        "excluded": 6,
        "high": 6,
        "medium": 90,
        "low": 0,
    }
    assert gemini["stats"] == {
        "total": 96,
        "eligible": 89,
        "excluded": 7,
        "high": 96,
        "medium": 0,
        "low": 0,
        "policy_violations": 0,
    }
    execution = gemini["execution"]
    conversation_ids = execution["conversation_id"].split(",")
    assert execution["cli"] == "agy"
    assert execution["cli_version"] == "1.1.8"
    assert execution["mode"] == "plan"
    assert len(conversation_ids) == len(set(conversation_ids)) == 6
    assert execution["accepted_conversations"] == 6
    assert execution["attempted_review_conversations"] == 6
    assert execution["discarded_conversations"] == []
    assert execution["turns_per_conversation"] == [1] * 6
    assert execution["tool_calls"] == 0
    assert execution["total_errors"] == 0
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 95,
        "review_queue": 1,
        "by_field": {"eligible": 1, "script": 0, "domain": 1, "risk": 1},
    }
    assert len(differences) == 1
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert adjustments["stats"] == {"total": 1}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-30",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 90,
        "excluded": 6,
        "by_selection_basis": {"agreement": 95, "codex_synthesis": 1},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-30",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 1,
        "confirmed_exact_matches": 95,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-30",
        maintainer_decisions=decision,
    )


def test_sixty_seventh_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-067.json"
    codex_path = (
        prefix / "blind-v2-source-classification-codex-first-pass-batch-067-2026-07-30.json"
    )
    gemini_path = (
        prefix / "blind-v2-source-classification-gemini-independent-batch-067-2026-07-30.json"
    )
    adjustments_path = (
        prefix
        / "blind-v2-source-classification-codex-synthesis-adjustments-batch-067-2026-07-30.json"
    )
    synthesis_path = (
        prefix / "blind-v2-source-classification-codex-synthesis-batch-067-2026-07-30.json"
    )
    decision_path = (
        prefix / "blind-v2-source-classification-maintainer-decision-batch-067-2026-07-30.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-067-2026-07-30.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 67)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == ("balanced-source-class-remaining-deterministic-sha256-v1")
    assert packet["stats"] == {
        "total": 120,
        "by_source": {
            "chromium-strings-zh-cn-v1": 40,
            "ready-gov-are-you-ready-guide-simplified-v1": 40,
            "zhtw-project-social-formal-ambiguity-guard-v1": 40,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert codex["stats"] == {
        "total": 120,
        "eligible": 113,
        "excluded": 7,
        "high": 7,
        "medium": 113,
        "low": 0,
    }
    assert gemini["stats"] == {
        "total": 120,
        "eligible": 115,
        "excluded": 5,
        "high": 120,
        "medium": 0,
        "low": 0,
        "policy_violations": 0,
    }
    execution = gemini["execution"]
    conversation_ids = execution["conversation_id"].split(",")
    assert execution["cli"] == "agy"
    assert execution["cli_version"] == "1.1.8"
    assert execution["mode"] == "plan"
    assert len(conversation_ids) == len(set(conversation_ids)) == 6
    assert execution["accepted_conversations"] == 6
    assert execution["attempted_review_conversations"] == 6
    assert execution["discarded_conversations"] == []
    assert execution["turns_per_conversation"] == [1] * 6
    assert execution["tool_calls"] == 0
    assert execution["total_errors"] == 0
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 120,
        "exact": 118,
        "review_queue": 2,
        "by_field": {"eligible": 2, "script": 0, "domain": 2, "risk": 2},
    }
    assert len(differences) == 2
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert adjustments["stats"] == {"total": 2}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-30",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 120,
        "eligible": 114,
        "excluded": 6,
        "by_selection_basis": {"agreement": 118, "codex_synthesis": 2},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-30",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 120,
        "confirmed_cases": 120,
        "resolved_disagreements": 2,
        "confirmed_exact_matches": 118,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-30",
        maintainer_decisions=decision,
    )
