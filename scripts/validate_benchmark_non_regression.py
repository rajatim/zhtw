#!/usr/bin/env python3
"""Compare a current benchmark report with a locked historical floor."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


class ValidationError(ValueError):
    """Raised when a benchmark report is invalid or regresses."""


def load_report(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationError(f"Cannot read JSON report {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValidationError(f"Report must be a JSON object: {path}")
    return payload


def require_mapping(value: Any, path: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValidationError(f"{path} must be an object")
    return value


def require_count(metrics: dict[str, Any], key: str, path: str) -> int:
    value = metrics.get(key)
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValidationError(f"{path}.{key} must be a non-negative integer")
    return value


def require_number(metrics: dict[str, Any], key: str, path: str) -> float:
    value = metrics.get(key)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValidationError(f"{path}.{key} must be a number")
    return float(value)


def validate_report_identity(baseline: dict[str, Any], current: dict[str, Any]) -> None:
    for key in ("dataset", "manifest_sha256", "normalized_sha256", "upstream_revision"):
        if key in baseline and baseline[key] != current.get(key):
            raise ValidationError(f"Report identity changed at {key}")


def validate_score_floor(baseline: dict[str, Any], current: dict[str, Any], path: str) -> None:
    baseline_total = require_count(baseline, "total_cases", f"baseline.{path}")
    current_total = require_count(current, "total_cases", f"current.{path}")
    if current_total != baseline_total:
        raise ValidationError(f"{path}.total_cases changed: {baseline_total} -> {current_total}")

    for key in ("exact", "idempotent"):
        baseline_value = require_count(baseline, key, f"baseline.{path}")
        current_value = require_count(current, key, f"current.{path}")
        if baseline_value > baseline_total or current_value > current_total:
            raise ValidationError(f"{path}.{key} cannot exceed total_cases")
        if current_value < baseline_value:
            raise ValidationError(f"{path}.{key} regressed: {baseline_value} -> {current_value}")

    baseline_span = baseline.get("changed_span")
    if baseline_span is not None:
        current_span = current.get("changed_span")
        baseline_span = require_mapping(baseline_span, f"baseline.{path}.changed_span")
        current_span = require_mapping(current_span, f"current.{path}.changed_span")
        baseline_f1 = require_number(baseline_span, "f1", f"baseline.{path}.changed_span")
        current_f1 = require_number(current_span, "f1", f"current.{path}.changed_span")
        if current_f1 < baseline_f1:
            raise ValidationError(
                f"{path}.changed_span.f1 regressed: {baseline_f1} -> {current_f1}"
            )


def validate_reports(baseline: dict[str, Any], current: dict[str, Any]) -> None:
    validate_report_identity(baseline, current)
    if "scores" in baseline:
        validate_score_floor(
            require_mapping(baseline.get("scores"), "baseline.scores"),
            require_mapping(current.get("scores"), "current.scores"),
            "scores",
        )
        return

    baseline_engines = require_mapping(baseline.get("engines"), "baseline.engines")
    current_engines = require_mapping(current.get("engines"), "current.engines")
    if set(current_engines) != set(baseline_engines):
        raise ValidationError("Benchmark engine set changed")
    if "zhtw" not in baseline_engines:
        raise ValidationError("Paired benchmark is missing the zhtw engine")

    validate_score_floor(
        require_mapping(baseline_engines["zhtw"], "baseline.engines.zhtw"),
        require_mapping(current_engines["zhtw"], "current.engines.zhtw"),
        "engines.zhtw",
    )
    for engine_id in sorted(set(baseline_engines) - {"zhtw"}):
        if current_engines[engine_id] != baseline_engines[engine_id]:
            raise ValidationError(f"Locked competitor output changed: {engine_id}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("baseline", type=Path)
    parser.add_argument("current", type=Path)
    args = parser.parse_args()

    try:
        validate_reports(load_report(args.baseline), load_report(args.current))
    except ValidationError as exc:
        raise SystemExit(f"Benchmark non-regression check failed: {exc}") from exc
    print(f"Benchmark non-regression check passed: {args.current}")


if __name__ == "__main__":
    main()
