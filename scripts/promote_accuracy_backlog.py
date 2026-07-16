#!/usr/bin/env python3
"""Promote checked annotation backlog cases into regression-v1."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.accuracy_annotation_status import approved_case_errors  # noqa: E402

DEFAULT_BACKLOG = PROJECT_ROOT / "benchmarks" / "accuracy" / "annotation-backlog-v1.json"
DEFAULT_GATE = PROJECT_ROOT / "docs" / "reports" / "annotation-promotion-gate-2026-07-05.json"
DEFAULT_DATASET = PROJECT_ROOT / "benchmarks" / "accuracy" / "regression-v1.json"
ANNOTATION_CLASSIFICATION = "annotation_promoted"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def relative_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path)


def assert_gate_ready(gate: dict[str, Any]) -> None:
    summary = gate["summary"]
    if summary["needs_zhtw_fix"] != 0:
        raise ValueError(f"promotion gate has {summary['needs_zhtw_fix']} cases needing zhtw fix")
    if summary["convert_mismatches"] != 0:
        raise ValueError(f"promotion gate has {summary['convert_mismatches']} convert mismatches")
    if summary["expected_not_idempotent"] != 0:
        raise ValueError(
            f"promotion gate has {summary['expected_not_idempotent']} non-idempotent expected cases"
        )


def promotion_ready_gate_cases(gate: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        case["id"]: case
        for case in gate["cases"]
        if case.get("status") == "promotion_ready"
        and case.get("convert_matches") is True
        and case.get("expected_idempotent") is True
    }


def approved_backlog_cases(backlog: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        case
        for case in backlog["cases"]
        if case.get("review", {}).get("status") == "approved" and not approved_case_errors(case)
    ]


def promoted_case(
    case: dict[str, Any],
    gate_case: dict[str, Any],
    *,
    backlog_path: Path,
    gate_path: Path,
) -> dict[str, Any]:
    review = case["review"]
    advisory = review.get("ai_advisory", {})
    notes = [
        "promoted from annotation backlog",
        f"expected_source={review['expected_source']}",
    ]
    if advisory:
        notes.append(f"ai_advisory={advisory.get('reviewer', '')}")
        notes.append(f"decision_by={advisory.get('decision_by', '')}")
    if review.get("adjudicator"):
        notes.append(f"adjudicator={review['adjudicator']}")

    return {
        "id": f"annotation/{case['id']}",
        "domain": case["domain"],
        "input": case["input"],
        "expected": gate_case["expected"],
        "risk": case["risk"],
        "source": {
            "report": relative_path(gate_path),
            "source_file": relative_path(backlog_path),
            "case_id": case["id"],
            "sample_seed": None,
            "classification": ANNOTATION_CLASSIFICATION,
        },
        "tags": ["annotation", case["batch"], case["domain"], case["risk"]],
        "notes": "; ".join(part for part in notes if part),
        "competitor_misses": [],
    }


def recalculate_stats(dataset: dict[str, Any]) -> None:
    cases = dataset["cases"]
    by_domain = Counter(case["domain"] for case in cases)
    by_risk = Counter(case["risk"] for case in cases)
    by_classification = Counter(case["source"]["classification"] for case in cases)
    by_miss_count = Counter(str(len(case["competitor_misses"])) for case in cases)

    dataset["stats"] = {
        "total_cases": len(cases),
        "by_domain": dict(sorted(by_domain.items())),
        "by_risk": dict(sorted(by_risk.items())),
        "by_classification": dict(sorted(by_classification.items())),
        "by_competitor_miss_count": dict(sorted(by_miss_count.items())),
    }
    dataset["selection"]["total_cases"] = len(cases)
    domains = list(dataset["selection"].get("categories", []))
    for domain in sorted(by_domain):
        if domain not in domains:
            domains.append(domain)
    dataset["selection"]["categories"] = domains
    dataset["selection"]["per_category"] = None
    dataset["selection"]["classification"] = (
        "curated corpus cases plus approved annotation backlog promotions"
    )
    dataset["selection"]["sort"] = "curated corpus order, then annotation case id"
    dataset["source_report"] = "case-level source.report"
    dataset["description"] = (
        "Public regression dataset from the curated zhtw-test-corpus plus approved "
        "accuracy annotation backlog promotions. Inputs stay Simplified Chinese; "
        "expected values are manually reviewed Taiwan Traditional Chinese."
    )


def promote(
    dataset: dict[str, Any],
    backlog: dict[str, Any],
    gate: dict[str, Any],
    *,
    backlog_path: Path,
    gate_path: Path,
) -> int:
    assert_gate_ready(gate)
    gate_cases = promotion_ready_gate_cases(gate)
    backlog_cases = approved_backlog_cases(backlog)

    missing = sorted(case["id"] for case in backlog_cases if case["id"] not in gate_cases)
    if missing:
        raise ValueError(f"approved backlog cases missing from gate report: {missing}")

    promoted = [
        promoted_case(case, gate_cases[case["id"]], backlog_path=backlog_path, gate_path=gate_path)
        for case in sorted(backlog_cases, key=lambda item: item["id"])
    ]
    promoted_ids = {case["id"] for case in promoted}
    existing_cases = [case for case in dataset["cases"] if case["id"] not in promoted_ids]
    dataset["cases"] = existing_cases + promoted
    recalculate_stats(dataset)
    return len(promoted)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", type=Path, default=DEFAULT_DATASET)
    parser.add_argument("--backlog", type=Path, default=DEFAULT_BACKLOG)
    parser.add_argument("--gate", type=Path, default=DEFAULT_GATE)
    args = parser.parse_args()

    dataset = load_json(args.dataset)
    backlog = load_json(args.backlog)
    gate = load_json(args.gate)
    promoted_count = promote(
        dataset,
        backlog,
        gate,
        backlog_path=args.backlog,
        gate_path=args.gate,
    )
    args.dataset.write_text(
        json.dumps(dataset, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"promoted={promoted_count} dataset_total={dataset['stats']['total_cases']}")
    print(f"updated {relative_path(args.dataset)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
