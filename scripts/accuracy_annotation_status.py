#!/usr/bin/env python3
"""Report progress for the accuracy annotation backlog."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_BACKLOG = PROJECT_ROOT / "benchmarks" / "accuracy" / "annotation-backlog-v1.json"
HUMAN_EXPECTED_SOURCES = {"human_first_pass", "human_adjudication"}
AI_ADVISORY_REVIEWERS = {"gemini_cli", "gemini_vertex"}


def ai_advisory_errors(review: dict[str, Any]) -> list[str]:
    advisory = review.get("ai_advisory")
    if not isinstance(advisory, dict):
        return ["approved case missing blind_reviewer or ai_advisory"]

    errors: list[str] = []
    reviewer = str(advisory.get("reviewer", ""))
    decision = str(advisory.get("decision", ""))
    decision_by = str(advisory.get("decision_by", ""))
    decision_date = str(advisory.get("decision_date", ""))
    source_report = str(advisory.get("source_report", ""))
    raw_report = str(advisory.get("raw_report", ""))
    expected_source = str(review.get("expected_source", ""))
    adjudicator = str(review.get("adjudicator", ""))
    disagreement = bool(review.get("disagreement", False))

    if reviewer not in AI_ADVISORY_REVIEWERS:
        errors.append("approved case ai_advisory reviewer is not recognized")
    if decision not in {"accepted", "rejected"}:
        errors.append("approved case ai_advisory decision is not recognized")
    if decision == "rejected":
        if expected_source != "human_adjudication":
            errors.append("approved case rejected ai_advisory requires human_adjudication")
        if not adjudicator.strip():
            errors.append("approved case rejected ai_advisory missing adjudicator")
        if not disagreement:
            errors.append("approved case rejected ai_advisory requires disagreement")
    if not decision_by.strip():
        errors.append("approved case ai_advisory missing decision_by")
    if not decision_date.strip():
        errors.append("approved case ai_advisory missing decision_date")
    if not source_report.strip():
        errors.append("approved case ai_advisory missing source_report")
    if not raw_report.strip():
        errors.append("approved case ai_advisory missing raw_report")

    return errors


def load_backlog(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def approved_case_errors(case: dict[str, Any]) -> list[str]:
    review = case.get("review", {})
    if review.get("status") != "approved":
        return []

    errors: list[str] = []
    expected = str(review.get("expected", ""))
    first_reviewer = str(review.get("first_reviewer", ""))
    blind_reviewer = str(review.get("blind_reviewer", ""))
    adjudicator = str(review.get("adjudicator", ""))
    expected_source = str(review.get("expected_source", ""))
    disagreement = bool(review.get("disagreement", False))

    if not expected.strip():
        errors.append("approved case has empty expected")
    if expected_source not in HUMAN_EXPECTED_SOURCES:
        errors.append("approved case expected_source is not human-reviewed")
    if not first_reviewer.strip():
        errors.append("approved case missing first_reviewer")
    if blind_reviewer.strip() and first_reviewer.strip() and first_reviewer == blind_reviewer:
        errors.append("approved case first_reviewer and blind_reviewer must differ")
    if not blind_reviewer.strip():
        errors.extend(ai_advisory_errors(review))
    if expected_source == "human_adjudication" and not adjudicator.strip():
        errors.append("approved human_adjudication case missing adjudicator")
    if disagreement and not adjudicator.strip():
        errors.append("approved disagreement case missing adjudicator")

    return errors


def is_promotion_ready(case: dict[str, Any]) -> bool:
    return case.get("review", {}).get("status") == "approved" and not approved_case_errors(case)


def summarize(backlog: dict[str, Any]) -> dict[str, Any]:
    batches = backlog["batches"]
    cases = backlog["cases"]
    target_by_batch = {batch["id"]: int(batch["target_cases"]) for batch in batches}
    case_count_by_batch = Counter(str(case["batch"]) for case in cases)
    approved_by_batch = Counter(str(case["batch"]) for case in cases if is_promotion_ready(case))
    raw_approved_total = sum(
        1 for case in cases if case.get("review", {}).get("status") == "approved"
    )
    review_status = Counter(str(case.get("review", {}).get("status", "missing")) for case in cases)
    target_total = int(backlog["target_total"])
    collected_total = len(cases)
    approved_total = sum(approved_by_batch.values())

    return {
        "name": backlog["name"],
        "status": backlog["status"],
        "target_total": target_total,
        "collected_total": collected_total,
        "raw_approved_total": raw_approved_total,
        "approved_total": approved_total,
        "remaining_to_collect": max(target_total - collected_total, 0),
        "remaining_to_approve": max(target_total - approved_total, 0),
        "review_status": dict(sorted(review_status.items())),
        "batches": [
            {
                "id": batch["id"],
                "domain": batch["domain"],
                "target_cases": target_by_batch[batch["id"]],
                "collected_cases": case_count_by_batch[batch["id"]],
                "approved_cases": approved_by_batch[batch["id"]],
                "remaining_to_collect": max(
                    target_by_batch[batch["id"]] - case_count_by_batch[batch["id"]],
                    0,
                ),
            }
            for batch in batches
        ],
    }


def validate_summary(backlog: dict[str, Any], summary: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    target_sum = sum(int(batch["target_cases"]) for batch in backlog["batches"])
    if target_sum != int(backlog["target_total"]):
        errors.append(f"batch targets sum to {target_sum}, not {backlog['target_total']}")

    known_batches = {batch["id"] for batch in backlog["batches"]}
    seen_ids: set[str] = set()
    for case in backlog["cases"]:
        case_id = str(case.get("id", "<missing>"))
        if case_id in seen_ids:
            errors.append(f"duplicate case id {case_id}")
        seen_ids.add(case_id)
        if case["batch"] not in known_batches:
            errors.append(f"case {case_id} uses unknown batch {case['batch']}")
        for error in approved_case_errors(case):
            errors.append(f"case {case_id}: {error}")

    for batch in summary["batches"]:
        if batch["collected_cases"] > batch["target_cases"]:
            errors.append(f"batch {batch['id']} exceeds target")

    if summary["collected_total"] > summary["target_total"]:
        errors.append("collected cases exceed target total")

    return errors


def print_text(summary: dict[str, Any]) -> None:
    print(f"{summary['name']}: {summary['status']}")
    print(f"Target: {summary['target_total']}")
    print(f"Collected: {summary['collected_total']}")
    print(f"Approved: {summary['approved_total']} promotion-ready")
    if summary["raw_approved_total"] != summary["approved_total"]:
        print(f"Raw approved: {summary['raw_approved_total']}")
    print(f"Remaining to collect: {summary['remaining_to_collect']}")
    print(f"Remaining to approve: {summary['remaining_to_approve']}")
    print()
    print("Batches:")
    for batch in summary["batches"]:
        print(
            "  "
            f"{batch['id']}: {batch['approved_cases']} approved / "
            f"{batch['collected_cases']} collected / {batch['target_cases']} target"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backlog", type=Path, default=DEFAULT_BACKLOG)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument(
        "--fail-under-target",
        action="store_true",
        help="Exit 1 unless approved cases reach the target total.",
    )
    args = parser.parse_args()

    backlog = load_backlog(args.backlog)
    summary = summarize(backlog)
    errors = validate_summary(backlog, summary)

    if args.format == "json":
        print(json.dumps({"summary": summary, "errors": errors}, ensure_ascii=False, indent=2))
    else:
        print_text(summary)
        if errors:
            print()
            print("Errors:", file=sys.stderr)
            for error in errors:
                print(f"  {error}", file=sys.stderr)

    if errors:
        return 1
    if args.fail_under_target and summary["approved_total"] < summary["target_total"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
