#!/usr/bin/env python3
"""Audit sentence-level idempotency without publishing case-level results."""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from zhtw import __version__, convert


@dataclass(frozen=True)
class Summary:
    schema_version: int
    dataset: str
    converter_version: str
    inputs_sha256: str
    total_cases: int
    idempotent_cases: int
    non_idempotent_cases: int
    idempotency_rate: float
    non_idempotent_ids_sha256: str


def load_cases(path: Path) -> tuple[str, list[dict[str, Any]]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or not isinstance(payload.get("cases"), list):
        raise ValueError("input file must be an object with a cases array")
    dataset = payload.get("dataset")
    if not isinstance(dataset, str) or not dataset:
        raise ValueError("input file must contain a non-empty dataset")

    cases = payload["cases"]
    seen: set[str] = set()
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            raise ValueError(f"case {index} must be an object")
        case_id = case.get("id")
        text = case.get("input")
        if not isinstance(case_id, str) or not case_id:
            raise ValueError(f"case {index} must contain a non-empty id")
        if case_id in seen:
            raise ValueError(f"duplicate case id: {case_id}")
        if not isinstance(text, str):
            raise ValueError(f"case {case_id} must contain a string input")
        seen.add(case_id)
    return dataset, cases


def build_summary(path: Path) -> Summary:
    dataset, cases = load_cases(path)
    non_idempotent_ids: list[str] = []
    for case in cases:
        converted = convert(case["input"])
        if convert(converted) != converted:
            non_idempotent_ids.append(case["id"])

    digest_input = "".join(f"{case_id}\n" for case_id in sorted(non_idempotent_ids))
    total = len(cases)
    idempotent = total - len(non_idempotent_ids)
    return Summary(
        schema_version=1,
        dataset=dataset,
        converter_version=__version__,
        inputs_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
        total_cases=total,
        idempotent_cases=idempotent,
        non_idempotent_cases=len(non_idempotent_ids),
        idempotency_rate=idempotent / total if total else 1.0,
        non_idempotent_ids_sha256=hashlib.sha256(digest_input.encode("utf-8")).hexdigest(),
    )


def compare_baseline(summary: Summary, baseline_path: Path) -> list[str]:
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    current = asdict(summary)
    errors: list[str] = []
    for field in (
        "schema_version",
        "dataset",
        "converter_version",
        "inputs_sha256",
        "total_cases",
        "idempotent_cases",
        "non_idempotent_cases",
        "non_idempotent_ids_sha256",
    ):
        if baseline.get(field) != current[field]:
            errors.append(f"{field}: expected {baseline.get(field)!r}, got {current[field]!r}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", type=Path)
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--json", action="store_true", dest="json_output")
    args = parser.parse_args()

    try:
        summary = build_summary(args.inputs)
        errors = compare_baseline(summary, args.baseline) if args.baseline else []
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    if args.json_output:
        print(json.dumps(asdict(summary), ensure_ascii=False, indent=2))
    else:
        print(
            f"{summary.dataset}: {summary.idempotent_cases}/{summary.total_cases} "
            f"idempotent ({summary.idempotency_rate:.2%}); "
            f"{summary.non_idempotent_cases} non-idempotent"
        )
    if errors:
        for error in errors:
            print(f"baseline mismatch: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
