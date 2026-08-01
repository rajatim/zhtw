"""Tests for the aggregate sentence-level idempotency audit."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

import scripts.audit_corpus_idempotency as audit

ROOT = Path(__file__).resolve().parents[1]


def write_inputs(path: Path, cases: list[dict[str, str]]) -> None:
    path.write_text(
        json.dumps({"dataset": "fixture", "cases": cases}, ensure_ascii=False),
        encoding="utf-8",
    )


def test_summary_hashes_failure_ids_without_exposing_them(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    inputs = tmp_path / "inputs.json"
    write_inputs(inputs, [{"id": "stable", "input": "a"}, {"id": "changes", "input": "b"}])
    conversions = {"a": "a", "b": "c", "c": "d", "d": "d"}
    monkeypatch.setattr(audit, "convert", lambda value: conversions[value])

    summary = audit.build_summary(inputs)

    assert summary.total_cases == 2
    assert summary.idempotent_cases == 1
    assert summary.non_idempotent_cases == 1
    assert "changes" not in json.dumps(audit.asdict(summary))


def test_baseline_comparison_fails_closed(tmp_path: Path) -> None:
    inputs = tmp_path / "inputs.json"
    baseline = tmp_path / "baseline.json"
    write_inputs(inputs, [{"id": "stable", "input": "same"}])
    summary = audit.build_summary(inputs)
    payload = audit.asdict(summary)
    payload["idempotent_cases"] = 0
    baseline.write_text(json.dumps(payload), encoding="utf-8")

    errors = audit.compare_baseline(summary, baseline)

    assert errors == ["idempotent_cases: expected 0, got 1"]


def test_blind_v2_idempotency_matches_frozen_443_baseline() -> None:
    inputs = ROOT / "benchmarks/accuracy/blind-v2.inputs.json"
    baseline = ROOT / "benchmarks/accuracy/blind-v2.idempotency-baseline.json"

    assert audit.compare_baseline(audit.build_summary(inputs), baseline) == []
