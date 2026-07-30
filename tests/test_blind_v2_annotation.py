"""Tests for private Blind-v2 annotation packet governance."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

import scripts.blind_v2_annotation as annotation
from scripts.blind_v2_annotation import (
    agy_prompt,
    agy_response_schema,
    build_confirmation_artifacts,
    build_packet,
    build_synthesis,
    compare_advisories,
    json_text,
    sha256_file,
    sha256_value,
    validate_advisory,
    validate_confirmation,
)

ROOT = Path(__file__).resolve().parents[1]
INPUTS = ROOT / "benchmarks/accuracy/blind-v2.inputs.json"


def advisory(packet_path: Path, *, stage: str, suffix: str = "") -> dict[str, object]:
    packet = json.loads(packet_path.read_text(encoding="utf-8"))
    return {
        "version": 1,
        "dataset": "blind-v2",
        "batch_id": packet["batch_id"],
        "stage": stage,
        "reviewer": "fixture",
        "model": "fixture-model",
        "review_date": "2026-07-30",
        "packet_sha256": sha256_file(packet_path),
        "policy": {
            "input_only": True,
            "converter_output_not_used": True,
            "other_advisory_not_seen": True,
        },
        "cases": [
            {
                "id": case["id"],
                "expected": f"預期文字{suffix}",
                "acceptable": [],
                "confidence": "high",
                "notes": "",
            }
            for case in packet["cases"]
        ],
    }


def test_build_packet_selects_exact_frozen_input_slice() -> None:
    packet = build_packet(INPUTS, batch_number=1, offset=0, limit=100)
    inputs = json.loads(INPUTS.read_text(encoding="utf-8"))

    assert packet["inputs_sha256"] == sha256_file(INPUTS)
    assert packet["selection"] == {"offset": 0, "limit": 100, "total_inputs": 1960}
    assert [case["id"] for case in packet["cases"]] == [
        case["id"] for case in inputs["cases"][:100]
    ]
    assert all(set(case) == {"id", "input", "domain", "risk"} for case in packet["cases"])


def test_validate_advisory_requires_exact_packet_order(tmp_path: Path) -> None:
    packet = build_packet(INPUTS, batch_number=1, offset=0, limit=3)
    packet_path = tmp_path / "packet.json"
    packet_path.write_text(json_text(packet), encoding="utf-8")
    value = advisory(packet_path, stage="codex_first_pass")
    value["cases"] = list(reversed(value["cases"]))
    advisory_path = tmp_path / "advisory.json"
    advisory_path.write_text(json_text(value), encoding="utf-8")

    errors = validate_advisory(packet_path, advisory_path)

    assert errors == ["advisory case IDs or ordering do not exactly match packet"]


def test_compare_advisories_reports_only_expected_differences(tmp_path: Path) -> None:
    packet = build_packet(INPUTS, batch_number=1, offset=0, limit=3)
    packet_path = tmp_path / "packet.json"
    packet_path.write_text(json_text(packet), encoding="utf-8")
    codex = advisory(packet_path, stage="codex_first_pass")
    agy = advisory(packet_path, stage="agy_independent")
    agy["cases"][1]["expected"] = "不同預期"
    codex_path = tmp_path / "codex.json"
    agy_path = tmp_path / "agy.json"
    codex_path.write_text(json_text(codex), encoding="utf-8")
    agy_path.write_text(json_text(agy), encoding="utf-8")

    result = compare_advisories(packet_path, codex_path, agy_path)

    assert result["stats"] == {"total": 3, "agreement": 2, "differences": 1}
    assert result["differences"][0]["id"] == packet["cases"][1]["id"]


def test_agy_prompt_contains_only_packet_cases_and_blind_rules() -> None:
    packet = build_packet(INPUTS, batch_number=1, offset=0, limit=2)
    prompt = agy_prompt(packet["cases"])
    schema = agy_response_schema(minimum_cases=2, maximum_cases=2)

    assert packet["cases"][0]["input"] in prompt
    assert "Do not use tools, converters, repository files" in prompt
    assert "Codex" not in prompt
    assert "expected" not in packet["cases"][0]
    assert schema["properties"]["cases"]["minItems"] == 2
    assert schema["properties"]["cases"]["maxItems"] == 2


def test_synthesis_requires_choices_for_primary_output_differences(tmp_path: Path) -> None:
    packet = build_packet(INPUTS, batch_number=1, offset=0, limit=2)
    packet_path = tmp_path / "packet.json"
    packet_path.write_text(json_text(packet), encoding="utf-8")
    codex = advisory(packet_path, stage="codex_first_pass")
    agy = advisory(packet_path, stage="agy_independent")
    agy["cases"][1]["expected"] = "Agy 預期"
    codex_path = tmp_path / "codex.json"
    agy_path = tmp_path / "agy.json"
    choices_path = tmp_path / "choices.json"
    codex_path.write_text(json_text(codex), encoding="utf-8")
    agy_path.write_text(json_text(agy), encoding="utf-8")
    choices_path.write_text(
        json_text(
            {
                "choices": [
                    {
                        "id": packet["cases"][1]["id"],
                        "decision": "agy",
                        "confidence": "high",
                        "needs_maintainer_review": True,
                        "rationale": "Agy is more natural.",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )

    result = build_synthesis(packet_path, codex_path, agy_path, choices_path)

    assert result["stats"] == {
        "total": 2,
        "agreement": 1,
        "codex": 0,
        "agy": 1,
        "hybrid": 0,
        "needs_maintainer_review": 1,
    }
    assert result["cases"][1]["expected"] == "Agy 預期"


def test_synthesis_allows_hybrid_audit_override_for_agreement(tmp_path: Path) -> None:
    packet = build_packet(INPUTS, batch_number=1, offset=0, limit=1)
    packet_path = tmp_path / "packet.json"
    packet_path.write_text(json_text(packet), encoding="utf-8")
    codex = advisory(packet_path, stage="codex_first_pass")
    agy = advisory(packet_path, stage="agy_independent")
    codex_path = tmp_path / "codex.json"
    agy_path = tmp_path / "agy.json"
    choices_path = tmp_path / "choices.json"
    codex_path.write_text(json_text(codex), encoding="utf-8")
    agy_path.write_text(json_text(agy), encoding="utf-8")
    choices_path.write_text(
        json_text(
            {
                "choices": [
                    {
                        "id": packet["cases"][0]["id"],
                        "decision": "hybrid",
                        "expected": "Codex audit correction",
                        "confidence": "high",
                        "needs_maintainer_review": False,
                        "rationale": "Both independent reviews made the same clear error.",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )

    result = build_synthesis(packet_path, codex_path, agy_path, choices_path)

    assert result["stats"] == {
        "total": 1,
        "agreement": 0,
        "codex": 0,
        "agy": 0,
        "hybrid": 1,
        "needs_maintainer_review": 0,
    }
    assert result["cases"][0]["expected"] == "Codex audit correction"


def test_synthesis_rejects_non_hybrid_override_for_agreement(tmp_path: Path) -> None:
    packet = build_packet(INPUTS, batch_number=1, offset=0, limit=1)
    packet_path = tmp_path / "packet.json"
    packet_path.write_text(json_text(packet), encoding="utf-8")
    codex = advisory(packet_path, stage="codex_first_pass")
    agy = advisory(packet_path, stage="agy_independent")
    codex_path = tmp_path / "codex.json"
    agy_path = tmp_path / "agy.json"
    choices_path = tmp_path / "choices.json"
    codex_path.write_text(json_text(codex), encoding="utf-8")
    agy_path.write_text(json_text(agy), encoding="utf-8")
    choices_path.write_text(
        json_text(
            {
                "choices": [
                    {
                        "id": packet["cases"][0]["id"],
                        "decision": "codex",
                        "confidence": "high",
                        "needs_maintainer_review": False,
                        "rationale": "Invalid override provenance.",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="audit override requires hybrid decision"):
        build_synthesis(packet_path, codex_path, agy_path, choices_path)


def test_confirmation_keeps_expected_private_and_tracks_public_coverage(
    tmp_path: Path,
) -> None:
    packet = build_packet(INPUTS, batch_number=1, offset=0, limit=2)
    packet_path = tmp_path / "packet.json"
    packet_path.write_text(json_text(packet), encoding="utf-8")
    codex = advisory(packet_path, stage="codex_first_pass")
    agy = advisory(packet_path, stage="agy_independent")
    codex_path = tmp_path / "codex.json"
    agy_path = tmp_path / "agy.json"
    choices_path = tmp_path / "choices.json"
    synthesis_path = tmp_path / "synthesis.json"
    codex_path.write_text(json_text(codex), encoding="utf-8")
    agy_path.write_text(json_text(agy), encoding="utf-8")
    choices_path.write_text(json_text({"choices": []}), encoding="utf-8")
    synthesis = build_synthesis(packet_path, codex_path, agy_path, choices_path)
    synthesis_path.write_text(json_text(synthesis), encoding="utf-8")

    decision, progress, expected = build_confirmation_artifacts(
        INPUTS,
        packet_path,
        synthesis_path,
        progress_path=tmp_path / "progress.json",
        expected_path=tmp_path / "expected.json",
        batch_decision_path=ROOT / "docs/reports/blind-v2-annotation-decision-test.json",
        maintainer="tim",
        decision_date="2026-07-30",
    )

    assert decision["case_ids"] == [case["id"] for case in packet["cases"]]
    assert progress["total_reviewed"] == 2
    assert progress["batches"][0]["decision_artifact_sha256"] == sha256_value(decision)
    assert expected["status"] == "annotating"
    assert len(expected["cases"]) == 2
    assert expected["decision_summary_sha256"] == sha256_value(progress)
    assert all("expected" not in batch for batch in progress["batches"])

    local_decision_path = tmp_path / "docs/reports/blind-v2-annotation-decision-test.json"
    local_decision_path.parent.mkdir(parents=True)
    progress["batches"][0]["decision_artifact"] = str(local_decision_path.relative_to(tmp_path))
    progress["batches"][0]["decision_artifact_sha256"] = sha256_value(decision)
    expected["cases"][0]["decision_artifact_sha256"] = sha256_value(decision)
    expected["cases"][1]["decision_artifact_sha256"] = sha256_value(decision)
    progress_path = tmp_path / "progress.json"
    expected_path = tmp_path / "expected.json"
    local_decision_path.write_text(json_text(decision), encoding="utf-8")
    progress_path.write_text(json_text(progress), encoding="utf-8")
    expected["decision_summary_sha256"] = sha256_file(progress_path)
    expected_path.write_text(json_text(expected), encoding="utf-8")

    original_root = annotation.PROJECT_ROOT
    annotation.PROJECT_ROOT = tmp_path
    try:
        assert validate_confirmation(INPUTS, progress_path, expected_path) == []
    finally:
        annotation.PROJECT_ROOT = original_root
