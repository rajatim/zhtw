#!/usr/bin/env python3
"""Check approved annotation backlog cases against the current zhtw converter."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.accuracy_annotation_status import approved_case_errors  # noqa: E402
from zhtw.converter import convert  # noqa: E402

DEFAULT_BACKLOG = PROJECT_ROOT / "benchmarks" / "accuracy" / "annotation-backlog-v1.json"
DEFAULT_OUTPUT_JSON = (
    PROJECT_ROOT / "docs" / "reports" / "annotation-promotion-gate-2026-07-05.json"
)
DEFAULT_OUTPUT_MD = PROJECT_ROOT / "docs" / "reports" / "annotation-promotion-gate-2026-07-05.md"


def load_backlog(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def relative_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path)


def approved_cases(backlog: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        case
        for case in backlog["cases"]
        if case.get("review", {}).get("status") == "approved" and not approved_case_errors(case)
    ]


def check_case(case: dict[str, Any]) -> dict[str, Any]:
    review = case["review"]
    output = convert(case["input"])
    expected = review["expected"]
    expected_after_convert = convert(expected)
    output_after_convert = convert(output)
    convert_matches = output == expected
    expected_idempotent = expected_after_convert == expected
    output_idempotent = output_after_convert == output

    return {
        "id": case["id"],
        "batch": case["batch"],
        "domain": case["domain"],
        "input": case["input"],
        "expected": expected,
        "actual": output,
        "convert_matches": convert_matches,
        "expected_idempotent": expected_idempotent,
        "output_idempotent": output_idempotent,
        "expected_after_convert": expected_after_convert,
        "output_after_convert": output_after_convert,
        "status": "promotion_ready"
        if convert_matches and expected_idempotent
        else "needs_zhtw_fix",
        "expected_source": review["expected_source"],
        "adjudicator": review.get("adjudicator", ""),
        "ai_advisory": review.get("ai_advisory", {}),
    }


def build_report(
    backlog_path: Path,
    backlog: dict[str, Any],
    *,
    generated_date: str,
) -> dict[str, Any]:
    skipped_cases = [
        case
        for case in backlog["cases"]
        if case.get("review", {}).get("status") != "approved" or approved_case_errors(case)
    ]
    checked = [check_case(case) for case in approved_cases(backlog)]
    status_counts = Counter(case["status"] for case in checked)
    expected_source_counts = Counter(case["expected_source"] for case in checked)

    return {
        "generated_date": generated_date,
        "source_backlog": relative_path(backlog_path),
        "backlog_name": backlog["name"],
        "summary": {
            "approved_checked": len(checked),
            "skipped_not_promotion_ready": len(skipped_cases),
            "promotion_ready": status_counts["promotion_ready"],
            "needs_zhtw_fix": status_counts["needs_zhtw_fix"],
            "convert_matches": sum(case["convert_matches"] for case in checked),
            "convert_mismatches": sum(not case["convert_matches"] for case in checked),
            "expected_idempotent": sum(case["expected_idempotent"] for case in checked),
            "expected_not_idempotent": sum(not case["expected_idempotent"] for case in checked),
            "by_expected_source": dict(sorted(expected_source_counts.items())),
        },
        "cases": checked,
    }


def code_block(text: str) -> str:
    fence = "```"
    while fence in text:
        fence += "`"
    return f"{fence}text\n{text}\n{fence}"


def render_markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines = [
        "<!-- zhtw:disable -->",
        f"# Annotation Promotion Gate（{report['generated_date']}）",
        "",
        f"Backlog: `{report['source_backlog']}`",
        "",
        "## Summary",
        "",
        f"- Approved checked: {summary['approved_checked']}",
        f"- Promotion ready: {summary['promotion_ready']}",
        f"- Needs zhtw fix: {summary['needs_zhtw_fix']}",
        f"- Convert matches: {summary['convert_matches']}",
        f"- Convert mismatches: {summary['convert_mismatches']}",
        f"- Expected idempotent: {summary['expected_idempotent']}",
        f"- Expected not idempotent: {summary['expected_not_idempotent']}",
        f"- Skipped not promotion-ready: {summary['skipped_not_promotion_ready']}",
        "",
        "Expected source:",
        "",
    ]
    for source, count in summary["by_expected_source"].items():
        lines.append(f"- `{source}`: {count}")

    failures = [case for case in report["cases"] if case["status"] != "promotion_ready"]
    ready = [case for case in report["cases"] if case["status"] == "promotion_ready"]

    lines.extend(["", "## Needs zhtw Fix", ""])
    if not failures:
        lines.append("None.")
    for case in failures:
        lines.extend(
            [
                f"### {case['id']}",
                "",
                f"- Expected source: `{case['expected_source']}`",
                f"- Convert matches: `{case['convert_matches']}`",
                f"- Expected idempotent: `{case['expected_idempotent']}`",
                f"- Output idempotent: `{case['output_idempotent']}`",
                "",
                "Input:",
                "",
                code_block(case["input"]),
                "",
                "Expected:",
                "",
                code_block(case["expected"]),
                "",
                "Actual:",
                "",
                code_block(case["actual"]),
                "",
            ]
        )
        if not case["expected_idempotent"]:
            lines.extend(
                [
                    "Expected after convert:",
                    "",
                    code_block(case["expected_after_convert"]),
                    "",
                ]
            )

    lines.extend(["", "## Promotion Ready", ""])
    if not ready:
        lines.append("None.")
    for case in ready:
        lines.append(f"- `{case['id']}`")

    lines.append("")
    return "\n".join(lines)


def write_report(report: dict[str, Any], output_json: Path, output_md: Path) -> None:
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    output_md.write_text(render_markdown(report), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backlog", type=Path, default=DEFAULT_BACKLOG)
    parser.add_argument("--output-json", type=Path, default=DEFAULT_OUTPUT_JSON)
    parser.add_argument("--output-md", type=Path, default=DEFAULT_OUTPUT_MD)
    parser.add_argument("--generated-date", default=dt.date.today().isoformat())
    parser.add_argument(
        "--fail-on-mismatch",
        action="store_true",
        help="Exit 1 if any approved case is not promotion-ready.",
    )
    args = parser.parse_args()

    backlog = load_backlog(args.backlog)
    report = build_report(args.backlog, backlog, generated_date=args.generated_date)
    write_report(report, args.output_json, args.output_md)

    summary = report["summary"]
    print(
        "checked={approved_checked} promotion_ready={promotion_ready} "
        "needs_zhtw_fix={needs_zhtw_fix}".format(**summary)
    )
    print(f"wrote {relative_path(args.output_json)}")
    print(f"wrote {relative_path(args.output_md)}")

    if args.fail_on_mismatch and summary["needs_zhtw_fix"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
