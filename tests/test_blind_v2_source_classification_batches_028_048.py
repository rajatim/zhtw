"""Blind-v2 source-classification tests for batches 028 through 048."""
# ruff: noqa: F403,F405

from tests._blind_v2_source_classification_support import *  # noqa: F403


def test_twenty_eighth_synthesis_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-028.json")
    prior_packet_path = ACCURACY_ROOT / (
        "review-packets/blind-v2-source-classification-batch-027.json"
    )
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-028-2026-07-27.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-028-2026-07-27.json"
    )
    adjustments_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-adjustments-batch-028-2026-07-27.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-028-2026-07-27.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-028-2026-07-27.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-028-2026-07-27.md"
    packet = load(packet_path)
    prior_packet = load(prior_packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()
    packet_ids = [case["id"] for case in packet["cases"]]

    assert packet["selection_policy"] == "balanced-remaining-deterministic-sha256-v1"
    assert packet["stats"] == {"total": 90, "by_source": {"kubernetes-docs-zh-cn-v1": 90}}
    assert set(packet_ids).isdisjoint(case["id"] for case in prior_packet["cases"])
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert gemini["execution"] == {
        "cli": "@google/gemini-cli",
        "cli_version": "0.52.0",
        "session_id": "0341974b-d3bf-4c6b-b1eb-e1cac1d01f56",
        "tool_calls": 0,
        "total_errors": 0,
    }
    assert gemini["stats"]["policy_violations"] == 0
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 90,
        "exact": 3,
        "review_queue": 87,
        "by_field": {"eligible": 10, "script": 74, "domain": 10, "risk": 40},
    }
    assert len(differences) == 87
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-27",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 90,
        "eligible": 80,
        "excluded": 10,
        "by_selection_basis": {"codex_synthesis": 90},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-27",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 90,
        "confirmed_cases": 90,
        "resolved_disagreements": 87,
        "confirmed_exact_matches": 3,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-27",
        maintainer_decisions=decision,
    )


def test_twenty_ninth_synthesis_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-029.json")
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-029-2026-07-27.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-029-2026-07-27.json"
    )
    adjustments_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-adjustments-batch-029-2026-07-27.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-029-2026-07-27.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-029-2026-07-27.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-029-2026-07-27.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 29)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }

    assert packet["selection_policy"] == "balanced-remaining-deterministic-sha256-v1"
    assert packet["stats"]["total"] == 70
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert gemini["execution"] == {
        "cli": "@google/gemini-cli",
        "cli_version": "0.52.0",
        "session_id": "ce278b43-730a-4bc6-bf11-257bc6fd6c3b",
        "tool_calls": 0,
        "total_errors": 0,
    }
    assert gemini["stats"]["policy_violations"] == 0
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 70,
        "exact": 18,
        "review_queue": 52,
        "by_field": {"eligible": 5, "script": 6, "domain": 15, "risk": 50},
    }
    assert len(differences) == 52
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-27",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 70,
        "eligible": 65,
        "excluded": 5,
        "by_selection_basis": {"codex_synthesis": 70},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-27",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 70,
        "confirmed_cases": 70,
        "resolved_disagreements": 52,
        "confirmed_exact_matches": 18,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-27",
        maintainer_decisions=decision,
    )


def test_thirtieth_synthesis_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-030.json")
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-030-2026-07-27.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-030-2026-07-27.json"
    )
    adjustments_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-adjustments-batch-030-2026-07-27.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-030-2026-07-27.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-030-2026-07-27.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-030-2026-07-27.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 30)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }

    assert packet["selection_policy"] == "balanced-remaining-deterministic-sha256-v1"
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "aosp-framework-zh-rcn-v1": 16,
            "census-newsroom-zh-hans-v1": 16,
            "chromium-strings-zh-cn-v1": 16,
            "kubernetes-docs-zh-cn-v1": 16,
            "massive-1-0-zh-cn-v1": 16,
            "ready-gov-radiation-zh-hans-v1": 16,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert gemini["execution"] == {
        "cli": "@google/gemini-cli",
        "cli_version": "0.52.0",
        "session_id": "e627b12b-9f5c-47ba-a178-8360b9424634",
        "tool_calls": 0,
        "total_errors": 0,
    }
    assert gemini["stats"]["policy_violations"] == 0
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 33,
        "review_queue": 63,
        "by_field": {"eligible": 8, "script": 11, "domain": 23, "risk": 54},
    }
    assert len(differences) == 63
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-27",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 88,
        "excluded": 8,
        "by_selection_basis": {"codex_synthesis": 96},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-27",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 63,
        "confirmed_exact_matches": 33,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-27",
        maintainer_decisions=decision,
    )


def test_thirty_first_synthesis_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-031.json")
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-031-2026-07-27.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-031-2026-07-27.json"
    )
    adjustments_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-adjustments-batch-031-2026-07-27.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-031-2026-07-27.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-031-2026-07-27.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-031-2026-07-27.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 31)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }

    assert packet["selection_policy"] == "all-source-cases-sorted-v1"
    assert packet["stats"] == {
        "total": 100,
        "by_source": {"zhtw-project-llm-domain-balance-v1": 100},
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert gemini["execution"] == {
        "cli": "@google/gemini-cli",
        "cli_version": "0.52.0",
        "session_id": "26231404-30c8-424a-bf1a-d4195510450c",
        "tool_calls": 0,
        "total_errors": 0,
    }
    assert gemini["stats"]["policy_violations"] == 0
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 43,
        "review_queue": 57,
        "by_field": {"eligible": 0, "script": 1, "domain": 25, "risk": 39},
    }
    assert len(differences) == 57
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-27",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 100,
        "excluded": 0,
        "by_selection_basis": {"codex_synthesis": 100},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-27",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 100,
        "confirmed_cases": 100,
        "resolved_disagreements": 57,
        "confirmed_exact_matches": 43,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-27",
        maintainer_decisions=decision,
    )


def test_thirty_second_synthesis_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-032.json")
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-032-2026-07-27.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-032-2026-07-27.json"
    )
    adjustments_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-adjustments-batch-032-2026-07-27.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-032-2026-07-27.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-032-2026-07-27.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-032-2026-07-27.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 32)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == "balanced-remaining-deterministic-sha256-v1"
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "aosp-framework-zh-rcn-v1": 16,
            "census-newsroom-zh-hans-v1": 16,
            "chromium-strings-zh-cn-v1": 16,
            "kubernetes-docs-zh-cn-v1": 16,
            "osha-disaster-cleanup-simplified-v1": 16,
            "ready-gov-home-fires-zh-hans-v1": 16,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert all(isinstance(case["quality_flags"], list) for case in gemini["cases"])
    assert gemini["execution"] == {
        "cli": "@google/gemini-cli",
        "cli_version": "0.52.0",
        "session_id": (
            "40f6f6d0-5cba-4883-ac5b-73b69978ccaf,"
            "e3429365-fd9a-4426-a6f0-4d7e2428e3af,"
            "3891fd21-c2c0-48d1-a25f-d41ca8852042,"
            "a28b5e81-c9f6-494e-bf0a-375e17366c74,"
            "8ad29bbf-3d74-4848-8667-13d7d3f83273,"
            "ad1d42fe-5800-4369-8caa-aec7f2eebebb"
        ),
        "tool_calls": 6,
        "total_errors": 0,
        "structural_normalization": "quality_flags_null_to_empty_array",
        "structural_normalization_cases": 62,
    }
    assert gemini["stats"]["policy_violations"] == 0
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 48,
        "review_queue": 48,
        "by_field": {"eligible": 2, "script": 4, "domain": 6, "risk": 43},
    }
    assert len(differences) == 48
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert set(overrides) == {
        "osha-disaster-cleanup-simplified-v1/sentence-029",
        "osha-disaster-cleanup-simplified-v1/sentence-066",
        "ready-gov-home-fires-zh-hans-v1/sentence-069",
        "ready-gov-home-fires-zh-hans-v1/sentence-074",
    }
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-27",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 92,
        "excluded": 4,
        "by_selection_basis": {"agreement": 48, "codex": 44, "codex_synthesis": 4},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-27",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 48,
        "confirmed_exact_matches": 48,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-27",
        maintainer_decisions=decision,
    )


def test_thirty_third_synthesis_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-033.json")
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-033-2026-07-27.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-033-2026-07-27.json"
    )
    adjustments_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-adjustments-batch-033-2026-07-27.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-033-2026-07-27.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-033-2026-07-27.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-033-2026-07-27.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 33)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == "balanced-remaining-deterministic-sha256-v1"
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "aosp-framework-zh-rcn-v1": 16,
            "census-newsroom-zh-hans-v1": 16,
            "chromium-strings-zh-cn-v1": 16,
            "kubernetes-docs-zh-cn-v1": 16,
            "osha-disaster-cleanup-simplified-v1": 16,
            "ready-gov-home-fires-zh-hans-v1": 16,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert all(isinstance(case["quality_flags"], list) for case in gemini["cases"])
    assert gemini["execution"] == {
        "cli": "@google/gemini-cli",
        "cli_version": "0.52.0",
        "session_id": (
            "90ce21bc-00a5-43de-b0c1-8860f92d8756,"
            "54758c1f-4ae8-4182-be7e-18aa57450797,"
            "faaffe2d-007d-4d49-9c5c-0e80b5359a4c,"
            "5a6dfbad-1c4b-41f3-8ee4-3ce5a1f8e648,"
            "fa573059-57b5-4e4d-8370-2135e9eedb33,"
            "7603fd73-f780-4835-8f73-8dd7eb2208d0"
        ),
        "tool_calls": 6,
        "total_errors": 0,
    }
    assert gemini["stats"]["policy_violations"] == 0
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 47,
        "review_queue": 49,
        "by_field": {"eligible": 5, "script": 1, "domain": 7, "risk": 48},
    }
    assert len(differences) == 49
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert set(overrides) == {"census-newsroom-zh-hans-v1/page-02-sentence-006"}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-27",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 91,
        "excluded": 5,
        "by_selection_basis": {"agreement": 47, "codex": 48, "codex_synthesis": 1},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-27",
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
        generated_date="2026-07-27",
        maintainer_decisions=decision,
    )


def test_thirty_fourth_synthesis_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-034.json")
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-034-2026-07-27.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-034-2026-07-27.json"
    )
    adjustments_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-adjustments-batch-034-2026-07-27.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-034-2026-07-27.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-034-2026-07-27.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-034-2026-07-27.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 34)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == "balanced-remaining-deterministic-sha256-v1"
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "massive-1-0-zh-cn-v1": 32,
            "ready-gov-drought-zh-hans-v1": 32,
            "zhtw-project-llm-social-baseline-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert gemini["execution"] == {
        "cli": "@google/gemini-cli",
        "cli_version": "0.52.0",
        "session_id": (
            "44090521-6f26-4960-9fa0-43f4cb968102,"
            "1103f74f-ca15-4f67-b86d-c715b2fd200e,"
            "ede77efb-1128-4891-a7d0-54d297ac2825"
        ),
        "tool_calls": 3,
        "total_errors": 0,
    }
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 39,
        "review_queue": 57,
        "by_field": {"eligible": 2, "script": 0, "domain": 45, "risk": 31},
    }
    assert len(differences) == 57
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert set(overrides) == {
        "ready-gov-drought-zh-hans-v1/sentence-008",
        "ready-gov-drought-zh-hans-v1/sentence-023",
        "ready-gov-drought-zh-hans-v1/sentence-026",
        "ready-gov-drought-zh-hans-v1/sentence-048",
        "ready-gov-drought-zh-hans-v1/sentence-063",
        "zhtw-project-llm-social-baseline-v1/llm-028",
    }
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids={"zhtw-project-llm-social-baseline-v1/llm-046"},
        generated_date="2026-07-27",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 92,
        "excluded": 4,
        "by_selection_basis": {
            "agreement": 39,
            "codex": 50,
            "codex_synthesis": 6,
            "gemini": 1,
        },
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-27",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 57,
        "confirmed_exact_matches": 39,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-27",
        maintainer_decisions=decision,
    )


def test_thirty_fifth_synthesis_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-035.json")
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-035-2026-07-27.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-035-2026-07-27.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-035-2026-07-27.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-035-2026-07-27.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-035-2026-07-27.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 35)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == "balanced-remaining-deterministic-sha256-v1"
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "census-newsroom-zh-hans-v1": 32,
            "massive-1-0-zh-cn-v1": 32,
            "zhtw-project-llm-social-baseline-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert gemini["execution"] == {
        "cli": "@google/gemini-cli",
        "cli_version": "0.52.0",
        "session_id": (
            "d7cc5f57-52a8-4596-ac63-cf7803e4b17b,"
            "92e0e4b1-d217-4ac7-ad81-c6b573543933,"
            "f3621105-3b2c-47a6-93ad-8128af43217f"
        ),
        "tool_calls": 0,
        "total_errors": 0,
    }
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 61,
        "review_queue": 35,
        "by_field": {"eligible": 6, "script": 1, "domain": 15, "risk": 29},
    }
    assert len(differences) == 35
    gemini_case_ids = {
        "census-newsroom-zh-hans-v1/page-02-sentence-002",
        "census-newsroom-zh-hans-v1/page-04-sentence-010",
        "census-newsroom-zh-hans-v1/page-05-sentence-010",
        "zhtw-project-llm-social-baseline-v1/llm-003",
        "zhtw-project-llm-social-baseline-v1/llm-009",
    }
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=gemini_case_ids,
        generated_date="2026-07-27",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 90,
        "excluded": 6,
        "by_selection_basis": {"agreement": 61, "codex": 30, "gemini": 5},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-27",
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
        generated_date="2026-07-27",
        maintainer_decisions=decision,
    )


def test_thirty_sixth_synthesis_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-036.json")
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-036-2026-07-28.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-036-2026-07-28.json"
    )
    adjustments_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-adjustments-batch-036-2026-07-28.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-036-2026-07-28.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-036-2026-07-28.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-036-2026-07-28.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 36)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == "balanced-remaining-deterministic-sha256-v1"
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "census-newsroom-zh-hans-v1": 32,
            "massive-1-0-zh-cn-v1": 32,
            "zhtw-project-llm-social-baseline-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert gemini["execution"] == {
        "cli": "@google/gemini-cli",
        "cli_version": "0.52.0",
        "session_id": (
            "f204a058-b67b-4f62-8105-21b0d8933681,"
            "8a70a65a-15b0-43bb-abd0-08f1d0ff116d,"
            "e34be403-1a07-4a5a-b284-63f8534a8c98"
        ),
        "tool_calls": 0,
        "total_errors": 0,
    }
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 45,
        "review_queue": 51,
        "by_field": {"eligible": 2, "script": 1, "domain": 20, "risk": 38},
    }
    assert len(differences) == 51
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert set(overrides) == {
        "census-newsroom-zh-hans-v1/page-07-sentence-013",
        "massive-1-0-zh-cn-v1/14279",
        "zhtw-project-llm-social-baseline-v1/llm-012",
        "zhtw-project-llm-social-baseline-v1/llm-025",
        "zhtw-project-llm-social-baseline-v1/llm-032",
        "zhtw-project-llm-social-baseline-v1/llm-035",
    }
    gemini_case_ids = {
        "census-newsroom-zh-hans-v1/page-01-sentence-011",
        "census-newsroom-zh-hans-v1/page-02-sentence-011",
        "census-newsroom-zh-hans-v1/page-06-sentence-003",
        "census-newsroom-zh-hans-v1/page-06-sentence-035",
        "census-newsroom-zh-hans-v1/page-08-sentence-028",
        "massive-1-0-zh-cn-v1/11605",
        "massive-1-0-zh-cn-v1/14294",
        "massive-1-0-zh-cn-v1/14674",
        "massive-1-0-zh-cn-v1/14717",
        "massive-1-0-zh-cn-v1/3006",
        "massive-1-0-zh-cn-v1/3820",
        "zhtw-project-llm-social-baseline-v1/llm-011",
        "zhtw-project-llm-social-baseline-v1/llm-015",
        "zhtw-project-llm-social-baseline-v1/social-022",
        "zhtw-project-llm-social-baseline-v1/social-023",
        "zhtw-project-llm-social-baseline-v1/social-034",
        "zhtw-project-llm-social-baseline-v1/social-040",
        "zhtw-project-llm-social-baseline-v1/social-043",
        "zhtw-project-llm-social-baseline-v1/social-047",
    }
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=gemini_case_ids,
        generated_date="2026-07-28",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 92,
        "excluded": 4,
        "by_selection_basis": {
            "agreement": 45,
            "codex": 26,
            "codex_synthesis": 6,
            "gemini": 19,
        },
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-28",
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
        generated_date="2026-07-28",
        maintainer_decisions=decision,
    )


def test_thirty_seventh_advisory_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-037.json")
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-037-2026-07-28.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-037-2026-07-28.json"
    )
    adjustments_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-adjustments-batch-037-2026-07-28.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-037-2026-07-28.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-037-2026-07-28.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-037-2026-07-28.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 37)
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
            "census-newsroom-zh-hans-v1": 11,
            "massive-1-0-zh-cn-v1": 32,
            "ready-gov-home-fires-zh-hans-v1": 11,
            "ready-gov-landslides-debris-flow-zh-hans-v1": 10,
            "zhtw-project-it-llm-social-guard-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert gemini["execution"] == {
        "cli": "@google/gemini-cli",
        "cli_version": "0.52.0",
        "session_id": (
            "8e82bc3b-7739-4be2-baf6-a919b41f91d3,"
            "8fbce307-ef37-40ed-aa3c-ee2f3dd8a193,"
            "4385ad30-198f-475b-a3d9-22fbcb2d4741,"
            "fbefefed-6dca-446e-abd2-15b498096b27,"
            "4f7dd6f0-0cf1-4428-bc63-4b6f3651fc84"
        ),
        "tool_calls": 0,
        "total_errors": 0,
    }
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 31,
        "review_queue": 65,
        "by_field": {"eligible": 6, "script": 6, "domain": 23, "risk": 53},
    }
    assert len(differences) == 65
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert set(overrides) == {"ready-gov-landslides-debris-flow-zh-hans-v1/sentence-030"}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-28",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 89,
        "excluded": 7,
        "by_selection_basis": {
            "agreement": 31,
            "codex": 64,
            "codex_synthesis": 1,
        },
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-28",
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
        generated_date="2026-07-28",
        maintainer_decisions=decision,
    )


def test_thirty_eighth_advisory_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-038.json")
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-038-2026-07-28.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-038-2026-07-28.json"
    )
    adjustments_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-adjustments-batch-038-2026-07-28.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-038-2026-07-28.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-038-2026-07-28.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-038-2026-07-28.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 38)
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
            "cisa-personal-security-zh-hans-v1": 8,
            "massive-1-0-zh-cn-v1": 32,
            "ready-gov-home-fires-zh-hans-v1": 8,
            "ready-gov-landslides-debris-flow-zh-hans-v1": 8,
            "ready-gov-radiation-zh-hans-v1": 8,
            "zhtw-project-it-llm-social-guard-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert gemini["execution"] == {
        "cli": "@google/gemini-cli",
        "cli_version": "0.52.0",
        "session_id": (
            "29fa94e8-66dd-4ec5-af7a-5ab5c61701c2,"
            "809634dc-5c37-4c4c-99a2-8500ab5654b4,"
            "2bd6232b-75f3-4dbd-9e66-d46bffa0e293,"
            "2e4f6ef9-f00a-4013-a37b-23f0d7bfc3a1,"
            "83468906-11b1-4f54-ba60-1839780ba7f5,"
            "0db6b8ef-58e5-416e-8c66-955dd081f2f8"
        ),
        "tool_calls": 0,
        "total_errors": 0,
    }
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 45,
        "review_queue": 51,
        "by_field": {"eligible": 4, "script": 6, "domain": 16, "risk": 47},
    }
    assert len(differences) == 51
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert set(overrides) == {"massive-1-0-zh-cn-v1/11496"}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-28",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 91,
        "excluded": 5,
        "by_selection_basis": {
            "agreement": 45,
            "codex": 50,
            "codex_synthesis": 1,
        },
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-28",
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
        generated_date="2026-07-28",
        maintainer_decisions=decision,
    )


def test_thirty_ninth_advisory_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-039.json")
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-039-2026-07-28.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-039-2026-07-28.json"
    )
    adjustments_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-adjustments-batch-039-2026-07-28.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-039-2026-07-28.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-039-2026-07-28.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-039-2026-07-28.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 39)
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
            "massive-1-0-zh-cn-v1": 32,
            "osha-disaster-cleanup-simplified-v1": 6,
            "ready-gov-drought-zh-hans-v1": 6,
            "ready-gov-floods-zh-hans-v1": 7,
            "ready-gov-hurricanes-zh-hans-v1": 7,
            "ready-gov-landslides-debris-flow-zh-hans-v1": 6,
            "zhtw-project-llm-it-ui-baseline-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert gemini["execution"] == {
        "cli": "@google/gemini-cli",
        "cli_version": "0.52.0",
        "session_id": (
            "c98ddae8-db7f-4887-9c1d-c72115e636f0,"
            "2f3d2624-ce59-49e5-b499-44e0048c9407,"
            "750ecf14-db47-4297-80f5-292304986571,"
            "27f15d2d-0e01-4974-be39-49f73c4b926f,"
            "1dc2a2bd-955b-4088-8a6d-fb0cdae5b278,"
            "1596dc30-e04c-43dd-92cb-f8ef6b169c11,"
            "3d3761db-a599-4053-8e65-9ebb774e89f2"
        ),
        "tool_calls": 0,
        "total_errors": 0,
    }
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 49,
        "review_queue": 47,
        "by_field": {"eligible": 5, "script": 3, "domain": 18, "risk": 40},
    }
    assert len(differences) == 47
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert set(overrides) == {"massive-1-0-zh-cn-v1/16462"}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-28",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 90,
        "excluded": 6,
        "by_selection_basis": {
            "agreement": 49,
            "codex": 46,
            "codex_synthesis": 1,
        },
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-28",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 47,
        "confirmed_exact_matches": 49,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-28",
        maintainer_decisions=decision,
    )


def test_fortieth_advisory_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-040.json"
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-040-2026-07-28.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-040-2026-07-28.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-040-2026-07-28.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-040-2026-07-28.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-040-2026-07-28.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 40)
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
            "massive-1-0-zh-cn-v1": 32,
            "ready-gov-winter-weather-zh-hans-v1": 32,
            "zhtw-project-llm-it-ui-baseline-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert gemini["execution"] == {
        "cli": "@google/gemini-cli",
        "cli_version": "0.52.0",
        "session_id": (
            "f7658e6a-21ce-4d3f-995d-1d1e7abb4541,"
            "c41186d4-ad2c-4661-9627-4856a35f78f7,"
            "65f3310c-c05f-4dd2-96eb-55995368681c"
        ),
        "tool_calls": 0,
        "total_errors": 0,
    }
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 43,
        "review_queue": 53,
        "by_field": {"eligible": 9, "script": 0, "domain": 13, "risk": 52},
    }
    assert len(differences) == 53
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-28",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 84,
        "excluded": 12,
        "by_selection_basis": {"agreement": 43, "codex": 53},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-28",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 53,
        "confirmed_exact_matches": 43,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-28",
        maintainer_decisions=decision,
    )


def test_forty_first_advisory_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-041.json"
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-041-2026-07-28.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-041-2026-07-28.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-041-2026-07-28.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-041-2026-07-28.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-041-2026-07-28.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 41)
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
            "massive-1-0-zh-cn-v1": 32,
            "ready-gov-tornadoes-zh-hans-v1": 16,
            "ready-gov-winter-weather-zh-hans-v1": 16,
            "zhtw-project-llm-it-ui-baseline-v1": 32,
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
        "eligible": 95,
        "excluded": 1,
        "high": 96,
        "medium": 0,
        "low": 0,
        "policy_violations": 0,
    }
    assert gemini["execution"] == {
        "cli": "@google/gemini-cli",
        "cli_version": "0.52.0",
        "session_id": (
            "452a8991-6132-4963-a371-02c61c3132bb,"
            "952e395d-e551-4171-9b18-c411b99cbbe7,"
            "2fbe8c09-bded-4689-95cd-941a38819534,"
            "10631792-ea0c-43cf-acb7-8c276b99aee5"
        ),
        "tool_calls": 0,
        "total_errors": 0,
    }
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 21,
        "review_queue": 75,
        "by_field": {"eligible": 8, "script": 0, "domain": 12, "risk": 73},
    }
    assert len(differences) == 75
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-28",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 87,
        "excluded": 9,
        "by_selection_basis": {"agreement": 21, "codex": 75},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-28",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 75,
        "confirmed_exact_matches": 21,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-28",
        maintainer_decisions=decision,
    )


def test_forty_second_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-042.json"
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-042-2026-07-28.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-042-2026-07-28.json"
    )
    adjustments_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-adjustments-batch-042-2026-07-28.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-042-2026-07-28.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-042-2026-07-28.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-042-2026-07-28.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 42)
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
            "aosp-framework-zh-rcn-v1": 32,
            "ftc-how-to-avoid-scam-simplified-v1": 16,
            "ftc-identity-theft-simplified-v1": 16,
            "zhtw-project-it-ui-llm-formal-guard-v1": 32,
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
        "eligible": 96,
        "excluded": 0,
        "high": 96,
        "medium": 0,
        "low": 0,
        "policy_violations": 0,
    }
    session_ids = gemini["execution"]["session_id"].split(",")
    assert len(session_ids) == len(set(session_ids)) == 25
    assert gemini["execution"]["tool_calls"] == 0
    assert gemini["execution"]["total_errors"] == 0
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 50,
        "review_queue": 46,
        "by_field": {"eligible": 8, "script": 13, "domain": 15, "risk": 32},
    }
    assert len(differences) == 46
    gemini_ids = {
        "ftc-how-to-avoid-scam-simplified-v1/sentence-010",
        "ftc-how-to-avoid-scam-simplified-v1/sentence-014",
        "ftc-identity-theft-simplified-v1/sentence-002",
        "ftc-identity-theft-simplified-v1/sentence-004",
        "ftc-identity-theft-simplified-v1/sentence-005",
        "ftc-identity-theft-simplified-v1/sentence-006",
        "ftc-identity-theft-simplified-v1/sentence-007",
        "ftc-identity-theft-simplified-v1/sentence-012",
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=gemini_ids,
        generated_date="2026-07-28",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 91,
        "excluded": 5,
        "by_selection_basis": {
            "agreement": 50,
            "codex": 35,
            "codex_synthesis": 3,
            "gemini": 8,
        },
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-28",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 46,
        "confirmed_exact_matches": 50,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-28",
        maintainer_decisions=decision,
    )


def test_forty_third_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-043.json"
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-043-2026-07-28.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-043-2026-07-28.json"
    )
    adjustments_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-adjustments-batch-043-2026-07-28.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-043-2026-07-28.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-043-2026-07-28.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-043-2026-07-28.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 43)
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
            "chromium-strings-zh-cn-v1": 16,
            "ftc-how-to-avoid-scam-simplified-v1": 16,
            "kubernetes-docs-zh-cn-v1": 16,
            "ready-gov-tornadoes-zh-hans-v1": 16,
            "zhtw-project-it-ui-llm-formal-guard-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert codex["stats"] == {
        "total": 96,
        "eligible": 94,
        "excluded": 2,
        "high": 2,
        "medium": 94,
        "low": 0,
    }
    assert gemini["stats"] == {
        "total": 96,
        "eligible": 95,
        "excluded": 1,
        "high": 96,
        "medium": 0,
        "low": 0,
        "policy_violations": 0,
    }
    session_ids = gemini["execution"]["session_id"].split(",")
    assert len(session_ids) == len(set(session_ids)) == 13
    assert gemini["execution"]["tool_calls"] == 0
    assert gemini["execution"]["total_errors"] == 0
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 26,
        "review_queue": 70,
        "by_field": {"eligible": 1, "script": 47, "domain": 20, "risk": 26},
    }
    assert len(differences) == 70
    gemini_ids = {
        "chromium-strings-zh-cn-v1/translation-5596627076506792578",
        "chromium-strings-zh-cn-v1/translation-6248988683584659830",
        "chromium-strings-zh-cn-v1/translation-6388799252195623474",
        "kubernetes-docs-zh-cn-v1/page-01-sentence-0021",
        "kubernetes-docs-zh-cn-v1/page-02-sentence-0033",
        "zhtw-project-it-ui-llm-formal-guard-v1/ui-006",
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=gemini_ids,
        generated_date="2026-07-28",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 94,
        "excluded": 2,
        "by_selection_basis": {
            "agreement": 26,
            "codex": 63,
            "codex_synthesis": 1,
            "gemini": 6,
        },
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-28",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 70,
        "confirmed_exact_matches": 26,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-28",
        maintainer_decisions=decision,
    )


def test_forty_fourth_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-044.json"
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-044-2026-07-28.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-044-2026-07-28.json"
    )
    adjustments_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-adjustments-batch-044-2026-07-28.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-044-2026-07-28.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-044-2026-07-28.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-044-2026-07-28.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 44)
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
            "census-newsroom-zh-hans-v1": 2,
            "cisa-personal-security-zh-hans-v1": 3,
            "flores-200-zho-hans-v1": 16,
            "ftc-heads-up-simplified-v1": 4,
            "ftc-how-to-avoid-scam-simplified-v1": 2,
            "ftc-identity-theft-simplified-v1": 4,
            "ready-gov-earthquakes-zh-hans-v1": 1,
            "ready-gov-floods-zh-hans-v1": 1,
            "ready-gov-hurricanes-zh-hans-v1": 1,
            "ready-gov-landslides-debris-flow-zh-hans-v1": 2,
            "ready-gov-radiation-zh-hans-v1": 5,
            "ready-gov-tornadoes-zh-hans-v1": 2,
            "ready-gov-winter-weather-zh-hans-v1": 5,
            "vscode-loc-zh-hans-v1": 16,
            "zhtw-project-it-llm-social-guard-v1": 16,
            "zhtw-project-it-ui-llm-formal-guard-v1": 16,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert codex["stats"] == {
        "total": 96,
        "eligible": 94,
        "excluded": 2,
        "high": 2,
        "medium": 94,
        "low": 0,
    }
    assert gemini["stats"] == {
        "total": 96,
        "eligible": 95,
        "excluded": 1,
        "high": 93,
        "medium": 3,
        "low": 0,
        "policy_violations": 0,
    }
    session_ids = gemini["execution"]["session_id"].split(",")
    assert len(session_ids) == len(set(session_ids)) == 12
    assert gemini["execution"]["tool_calls"] == 0
    assert gemini["execution"]["total_errors"] == 0
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 41,
        "review_queue": 55,
        "by_field": {"eligible": 1, "script": 10, "domain": 27, "risk": 34},
    }
    assert len(differences) == 55
    gemini_ids = {
        "flores-200-zho-hans-v1/devtest-0179",
        "ready-gov-floods-zh-hans-v1/sentence-027",
        "ready-gov-landslides-debris-flow-zh-hans-v1/sentence-007",
        "ready-gov-radiation-zh-hans-v1/sentence-005",
        "ready-gov-winter-weather-zh-hans-v1/sentence-012",
        "vscode-loc-zh-hans-v1/entry-1bc2d120c0821a7f",
        "vscode-loc-zh-hans-v1/entry-8c957017a839953e",
        "vscode-loc-zh-hans-v1/entry-ec63ec66cb3a69b7",
        "zhtw-project-it-llm-social-guard-v1/it-021",
        "zhtw-project-it-llm-social-guard-v1/llm-017",
        "zhtw-project-it-llm-social-guard-v1/social-020",
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=gemini_ids,
        generated_date="2026-07-28",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 94,
        "excluded": 2,
        "by_selection_basis": {
            "agreement": 41,
            "codex": 40,
            "codex_synthesis": 4,
            "gemini": 11,
        },
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-28",
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
        generated_date="2026-07-28",
        maintainer_decisions=decision,
    )


def test_forty_fifth_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-045.json"
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-045-2026-07-28.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-045-2026-07-28.json"
    )
    adjustments_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-adjustments-batch-045-2026-07-28.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-045-2026-07-28.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-045-2026-07-28.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-045-2026-07-28.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 45)
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
            "ready-gov-campus-zh-hans-v1": 6,
            "ready-gov-kids-tornadoes-zh-hans-v1": 39,
            "ready-gov-winter-weather-zh-hans-v1": 3,
            "zhtw-project-it-llm-social-guard-v1": 20,
            "zhtw-project-it-ui-llm-formal-guard-v1": 20,
            "zhtw-project-llm-it-ui-baseline-v1": 4,
            "zhtw-project-llm-social-baseline-v1": 4,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert codex["stats"] == {
        "total": 96,
        "eligible": 86,
        "excluded": 10,
        "high": 10,
        "medium": 86,
        "low": 0,
    }
    assert gemini["stats"] == {
        "total": 96,
        "eligible": 94,
        "excluded": 2,
        "high": 96,
        "medium": 0,
        "low": 0,
        "policy_violations": 0,
    }
    session_ids = gemini["execution"]["session_id"].split(",")
    assert len(session_ids) == len(set(session_ids)) == 13
    assert gemini["execution"]["tool_calls"] == 0
    assert gemini["execution"]["total_errors"] == 0
    assert gemini["execution"]["transport_retries"] == 2
    stats, _ = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 10,
        "review_queue": 86,
        "by_field": {"eligible": 8, "script": 24, "domain": 41, "risk": 51},
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert adjustments["stats"] == {"total": 18}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids={
            "zhtw-project-it-llm-social-guard-v1/social-007",
            "zhtw-project-it-ui-llm-formal-guard-v1/ui-010",
            "zhtw-project-it-ui-llm-formal-guard-v1/ui-022",
            "zhtw-project-llm-social-baseline-v1/social-002",
        },
        generated_date="2026-07-28",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 85,
        "excluded": 11,
        "by_selection_basis": {
            "agreement": 8,
            "codex": 66,
            "codex_synthesis": 18,
            "gemini": 4,
        },
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-28",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 86,
        "confirmed_exact_matches": 10,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-28",
        maintainer_decisions=decision,
    )


def test_forty_sixth_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-046.json"
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-046-2026-07-28.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-046-2026-07-28.json"
    )
    adjustments_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-adjustments-batch-046-2026-07-28.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-046-2026-07-28.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-046-2026-07-28.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-046-2026-07-28.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 46)
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
            "kubernetes-docs-zh-cn-v1": 48,
            "zhtw-project-formal-llm-overconversion-guard-v1": 48,
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
        "eligible": 96,
        "excluded": 0,
        "high": 96,
        "medium": 0,
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
        "exact": 19,
        "review_queue": 77,
        "by_field": {"eligible": 8, "script": 62, "domain": 37, "risk": 22},
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert adjustments["stats"] == {"total": 10}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-28",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 92,
        "excluded": 4,
        "by_selection_basis": {
            "agreement": 19,
            "codex": 67,
            "codex_synthesis": 10,
        },
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-28",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 77,
        "confirmed_exact_matches": 19,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-28",
        maintainer_decisions=decision,
    )


def test_forty_seventh_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-047.json"
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-047-2026-07-28.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-047-2026-07-28.json"
    )
    adjustments_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-adjustments-batch-047-2026-07-28.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-047-2026-07-28.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-047-2026-07-28.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-047-2026-07-28.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 47)
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
            "ready-gov-evacuation-zh-hans-v1": 32,
            "zhtw-project-formal-llm-overconversion-guard-v1": 32,
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
        "eligible": 96,
        "excluded": 0,
        "high": 96,
        "medium": 0,
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
        "exact": 29,
        "review_queue": 67,
        "by_field": {"eligible": 4, "script": 47, "domain": 32, "risk": 17},
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert adjustments["stats"] == {"total": 21}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-28",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 92,
        "excluded": 4,
        "by_selection_basis": {
            "agreement": 23,
            "codex": 52,
            "codex_synthesis": 21,
        },
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-28",
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
        generated_date="2026-07-28",
        maintainer_decisions=decision,
    )


def test_forty_eighth_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-048.json"
    codex_path = (
        prefix / "blind-v2-source-classification-codex-first-pass-batch-048-2026-07-28.json"
    )
    gemini_path = (
        prefix / "blind-v2-source-classification-gemini-independent-batch-048-2026-07-28.json"
    )
    adjustments_path = (
        prefix
        / "blind-v2-source-classification-codex-synthesis-adjustments-batch-048-2026-07-28.json"
    )
    synthesis_path = (
        prefix / "blind-v2-source-classification-codex-synthesis-batch-048-2026-07-28.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-048-2026-07-29.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-048-2026-07-28.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 48)
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
            "ready-gov-cybersecurity-zh-hans-v1": 32,
            "zhtw-project-formal-llm-context-guard-v1": 32,
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
        "eligible": 91,
        "excluded": 5,
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
        "exact": 35,
        "review_queue": 61,
        "by_field": {"eligible": 8, "script": 3, "domain": 39, "risk": 42},
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert adjustments["stats"] == {"total": 21}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-28",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 86,
        "excluded": 10,
        "by_selection_basis": {"agreement": 35, "codex": 40, "codex_synthesis": 21},
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
        "resolved_disagreements": 61,
        "confirmed_exact_matches": 35,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-28",
        maintainer_decisions=decision,
    )
