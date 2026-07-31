"""Tests for the private paired-localization disagreement audit tool."""

from __future__ import annotations

import json

import scripts.audit_paired_localization_disagreements as audit


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_build_packets_uses_short_stable_review_ids(tmp_path, monkeypatch) -> None:
    selected = [
        {
            "id": f"source/very-long-resource-key-{index:03d}",
            "source_track": "aosp-framework-paired-ui-v1" if index < 60 else "firefox-paired-ui-v1",
            "resource_key": f"key-{index:03d}",
            "input": "输入",
            "expected": "輸入",
            "actual": "輸入值",
        }
        for index in range(100)
    ]
    monkeypatch.setattr(
        audit,
        "select_cases",
        lambda **_: (
            selected,
            {"aosp-framework-paired-ui-v1": 61, "firefox-paired-ui-v1": 63},
        ),
    )

    audit.build_packets(root=tmp_path, lock_path=tmp_path / "lock.json", container_image="image")

    packets = [read(path) for path in sorted(tmp_path.glob("packet-*.json"))]
    cases = [case for packet in packets for case in packet["cases"]]
    assert [len(packet["cases"]) for packet in packets] == [25, 25, 25, 25]
    assert cases[0]["id"] == "paired-audit-0001"
    assert cases[-1]["id"] == "paired-audit-0100"
    assert cases[0]["source_case_id"] == "source/very-long-resource-key-000"


def test_synthesis_packet_contains_only_core_decision_disagreements(tmp_path) -> None:
    for batch in range(1, 5):
        case_id = f"paired-audit-{batch:04d}"
        audit.write_json(
            tmp_path / f"packet-{batch:03d}.json",
            {
                "version": 1,
                "audit_id": "fixture",
                "batch": batch,
                "cases": [{"id": case_id, "input": "输入", "expected": "輸入", "actual": "輸入"}],
            },
        )
        common = {
            "id": case_id,
            "severity": "none",
            "category": "acceptable_variant",
            "expected_valid": True,
            "actual_acceptable": True,
            "confidence": "high",
            "rationale": "fixture",
        }
        codex = dict(common)
        agy = dict(common)
        if batch == 3:
            agy.update(severity="P2", category="regional_wording", actual_acceptable=False)
        for stage, value in (("codex", codex), ("agy", agy)):
            audit.write_json(
                tmp_path / stage / f"review-{batch:03d}.json",
                {"version": 1, "cases": [value]},
            )

    paths = audit.build_synthesis_packets(tmp_path)

    assert len(paths) == 1
    cases = read(paths[0])["cases"]
    assert [case["id"] for case in cases] == ["paired-audit-0003"]
    assert cases[0]["codex_review"]["actual_acceptable"] is True
    assert cases[0]["agy_review"]["actual_acceptable"] is False
