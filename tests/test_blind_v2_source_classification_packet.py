"""Tests for Blind-v2 deterministic input-only source classification packets."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from scripts.create_blind_v2_source_classification_packet import (
    build_packet,
    render_markdown,
    validate_packet,
)

ROOT = Path(__file__).resolve().parents[1]
ACCURACY_ROOT = ROOT / "benchmarks" / "accuracy"
PACKET = ACCURACY_ROOT / "review-packets" / "blind-v2-source-classification-batch-001.json"
MARKDOWN = ACCURACY_ROOT / "review-packets" / "blind-v2-source-classification-batch-001.md"
SECOND_PACKET = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-002.json"
SECOND_MARKDOWN = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-002.md"
THIRD_PACKET = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-003.json"
THIRD_MARKDOWN = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-003.md"
FIFTH_PACKET = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-005.json"
FIFTH_MARKDOWN = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-005.md"
SIXTH_PACKET = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-006.json"
SIXTH_MARKDOWN = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-006.md"
SEVENTH_PACKET = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-007.json"
SEVENTH_MARKDOWN = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-007.md"
EIGHTH_PACKET = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-008.json"
EIGHTH_MARKDOWN = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-008.md"
FORBIDDEN_KEYS = {"expected", "acceptable", "annotation", "output", "normalized_output"}


def write_source(path: Path, source_id: str, count: int) -> None:
    cases = []
    for number in range(1, count + 1):
        cases.append(
            {
                "id": f"{source_id}/case-{number:03d}",
                "input": f"输入句子 {source_id} {number}",
                "provenance": {
                    "raw_url": f"https://example.test/{source_id}",
                    "source_case_id": f"case-{number:03d}",
                    "split": "test",
                },
                "classification": {
                    "domain": None,
                    "risk": None,
                    "status": "needs_input_only_review",
                },
            }
        )
    path.write_text(
        json.dumps(
            {
                "id": source_id,
                "input_only": True,
                "converter_output_used": False,
                "cases": cases,
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )


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


def test_packet_is_balanced_deterministic_and_nonoverlapping(tmp_path: Path) -> None:
    first_source = tmp_path / "first.json"
    second_source = tmp_path / "second.json"
    write_source(first_source, "first-source", 120)
    write_source(second_source, "second-source", 120)

    first = build_packet(
        [second_source, first_source],
        batch_size=100,
        batch_number=1,
        seed=20260719,
        generated_date="2026-07-20",
    )
    reordered = build_packet(
        [first_source, second_source],
        batch_size=100,
        batch_number=1,
        seed=20260719,
        generated_date="2026-07-20",
    )
    second = build_packet(
        [first_source, second_source],
        batch_size=100,
        batch_number=2,
        seed=20260719,
        generated_date="2026-07-20",
    )

    assert first == reordered
    assert first["stats"] == {
        "total": 100,
        "by_source": {"first-source": 50, "second-source": 50},
    }
    assert {case["id"] for case in first["cases"]}.isdisjoint(
        case["id"] for case in second["cases"]
    )
    assert find_forbidden_keys(first) == set()
    assert validate_packet(first) == []


def test_packet_rejects_source_that_used_converter_output(tmp_path: Path) -> None:
    source = tmp_path / "source.json"
    write_source(source, "source", 10)
    value = json.loads(source.read_text(encoding="utf-8"))
    value["converter_output_used"] = True
    source.write_text(json.dumps(value), encoding="utf-8")

    try:
        build_packet(
            [source],
            batch_size=2,
            batch_number=1,
            seed=20260719,
            generated_date="2026-07-20",
        )
    except ValueError as exc:
        assert "no converter output" in str(exc)
    else:
        raise AssertionError("converter-derived source must be rejected")


def test_selection_round_is_independent_from_global_batch_number(tmp_path: Path) -> None:
    source = tmp_path / "source.json"
    write_source(source, "source", 220)

    first_round = build_packet(
        [source],
        batch_size=100,
        batch_number=5,
        selection_round=1,
        seed=20260719,
        generated_date="2026-07-23",
    )
    second_round = build_packet(
        [source],
        batch_size=100,
        batch_number=6,
        selection_round=2,
        seed=20260719,
        generated_date="2026-07-23",
    )

    assert first_round["batch_number"] == 5
    assert first_round["selection_round"] == 1
    assert {case["id"] for case in first_round["cases"]}.isdisjoint(
        case["id"] for case in second_round["cases"]
    )
    assert validate_packet(first_round) == []


def test_all_source_cases_mode_keeps_uneven_sources_complete(tmp_path: Path) -> None:
    first_source = tmp_path / "first.json"
    second_source = tmp_path / "second.json"
    write_source(first_source, "first-source", 2)
    write_source(second_source, "second-source", 3)

    packet = build_packet(
        [second_source, first_source],
        batch_size=100,
        batch_number=3,
        seed=20260719,
        generated_date="2026-07-22",
        all_source_cases=True,
    )

    assert packet["batch_size"] == 5
    assert packet["selection_policy"] == "all-source-cases-sorted-v1"
    assert packet["stats"] == {
        "total": 5,
        "by_source": {"first-source": 2, "second-source": 3},
    }
    assert validate_packet(packet) == []


def test_committed_packet_is_valid_input_only_and_reproducible() -> None:
    packet = json.loads(PACKET.read_text(encoding="utf-8"))

    assert validate_packet(packet) == []
    assert packet["stats"] == {
        "total": 100,
        "by_source": {
            "flores-200-zho-hans-v1": 50,
            "ud-chinese-cfl-v1": 50,
        },
    }
    assert packet["input_only"] is True
    assert packet["converter_output_used"] is False
    assert find_forbidden_keys(packet) == set()
    for snapshot in packet["source_snapshots"]:
        source_path = ROOT / snapshot["path"]
        assert hashlib.sha256(source_path.read_bytes()).hexdigest() == snapshot["sha256"]
    assert MARKDOWN.read_text(encoding="utf-8") == render_markdown(PACKET, packet)


def test_second_committed_packet_is_valid_nonoverlapping_and_reproducible() -> None:
    first = json.loads(PACKET.read_text(encoding="utf-8"))
    second = json.loads(SECOND_PACKET.read_text(encoding="utf-8"))

    assert validate_packet(second) == []
    assert second["batch_number"] == 2
    assert second["stats"] == first["stats"]
    assert {case["id"] for case in first["cases"]}.isdisjoint(
        case["id"] for case in second["cases"]
    )
    assert find_forbidden_keys(second) == set()
    assert SECOND_MARKDOWN.read_text(encoding="utf-8") == render_markdown(SECOND_PACKET, second)


def test_third_committed_packet_covers_all_cdc_pilots_and_is_reproducible() -> None:
    packet = json.loads(THIRD_PACKET.read_text(encoding="utf-8"))

    assert validate_packet(packet) == []
    assert packet["batch_number"] == 3
    assert packet["selection_policy"] == "all-source-cases-sorted-v1"
    assert packet["stats"] == {
        "total": 62,
        "by_source": {
            "cdc-stacks-111808-v1": 18,
            "cdc-stacks-116683-v1": 22,
            "cdc-stacks-120024-v1": 22,
        },
    }
    assert find_forbidden_keys(packet) == set()
    for snapshot in packet["source_snapshots"]:
        source_path = ROOT / snapshot["path"]
        assert hashlib.sha256(source_path.read_bytes()).hexdigest() == snapshot["sha256"]
    assert THIRD_MARKDOWN.read_text(encoding="utf-8") == render_markdown(THIRD_PACKET, packet)


def test_fifth_packet_uses_first_massive_selection_round_and_is_reproducible() -> None:
    packet = json.loads(FIFTH_PACKET.read_text(encoding="utf-8"))

    assert validate_packet(packet) == []
    assert packet["batch_number"] == 5
    assert packet["selection_round"] == 1
    assert packet["stats"] == {
        "total": 100,
        "by_source": {"massive-1-0-zh-cn-v1": 100},
    }
    assert find_forbidden_keys(packet) == set()
    assert FIFTH_MARKDOWN.read_text(encoding="utf-8") == render_markdown(FIFTH_PACKET, packet)


def test_sixth_packet_covers_project_it_source_and_is_reproducible() -> None:
    packet = json.loads(SIXTH_PACKET.read_text(encoding="utf-8"))

    assert validate_packet(packet) == []
    assert packet["batch_number"] == 6
    assert packet["selection_policy"] == "all-source-cases-sorted-v1"
    assert packet["stats"] == {
        "total": 100,
        "by_source": {"zhtw-project-it-api-cli-v1": 100},
    }
    assert find_forbidden_keys(packet) == set()
    assert SIXTH_MARKDOWN.read_text(encoding="utf-8") == render_markdown(SIXTH_PACKET, packet)


def test_seventh_packet_covers_ftc_source_and_is_reproducible() -> None:
    packet = json.loads(SEVENTH_PACKET.read_text(encoding="utf-8"))

    assert validate_packet(packet) == []
    assert packet["batch_number"] == 7
    assert packet["stats"] == {
        "total": 81,
        "by_source": {"ftc-small-business-simplified-v1": 81},
    }
    assert find_forbidden_keys(packet) == set()
    assert SEVENTH_MARKDOWN.read_text(encoding="utf-8") == render_markdown(SEVENTH_PACKET, packet)


def test_eighth_packet_covers_nps_acadia_source_and_is_reproducible() -> None:
    packet = json.loads(EIGHTH_PACKET.read_text(encoding="utf-8"))

    assert validate_packet(packet) == []
    assert packet["batch_number"] == 8
    assert packet["stats"] == {
        "total": 32,
        "by_source": {"nps-essential-acadia-simplified-v1": 32},
    }
    assert find_forbidden_keys(packet) == set()
    assert EIGHTH_MARKDOWN.read_text(encoding="utf-8") == render_markdown(EIGHTH_PACKET, packet)
