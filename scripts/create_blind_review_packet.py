#!/usr/bin/env python3
"""Create a blind review packet from the accuracy annotation backlog."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_BACKLOG = PROJECT_ROOT / "benchmarks" / "accuracy" / "annotation-backlog-v1.json"
DEFAULT_STATUS = "needs_blind_review"


def load_backlog(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def relative_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path)


def selected_cases(
    backlog: dict[str, Any],
    *,
    batch: str | None,
    status: str,
) -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    for case in backlog["cases"]:
        review = case.get("review", {})
        if review.get("status") != status:
            continue
        if batch is not None and case.get("batch") != batch:
            continue
        cases.append(case)
    return cases


def source_line(source: dict[str, Any]) -> str:
    parts = []
    source_type = str(source.get("type", "")).strip()
    license_name = str(source.get("license", "")).strip()
    citation = str(source.get("citation", "")).strip()
    if source_type:
        parts.append(source_type)
    if license_name:
        parts.append(f"license: {license_name}")
    if citation:
        parts.append(f"citation: {citation}")
    return "; ".join(parts) if parts else "unspecified"


def code_block(text: str) -> str:
    fence = "```"
    while fence in text:
        fence += "`"
    return f"{fence}text\n{text}\n{fence}"


def render_markdown(
    backlog_path: Path,
    backlog: dict[str, Any],
    cases: list[dict[str, Any]],
    *,
    batch: str | None,
    status: str,
    generated_date: str,
) -> str:
    batch_label = batch or "all"
    lines = [
        "<!-- zhtw:disable -->",
        f"# Annotation Blind Review Packet ({generated_date})",
        "",
        f"Backlog: `{relative_path(backlog_path)}`",
        f"Backlog name: `{backlog['name']}`",
        f"Status filter: `{status}`",
        f"Batch filter: `{batch_label}`",
        f"Cases: {len(cases)}",
        "",
        "## Reviewer Rules",
        "",
        "- Use a reviewer who did not complete the first pass.",
        (
            "- Do not open the backlog JSON, AI draft report, or first-pass "
            "expected output while filling this packet."
        ),
        "- Write Taiwan Traditional Chinese expected output from the Simplified input only.",
        "- Keep the input block unchanged.",
        "- Fill reviewer id, blind expected, and notes for each case.",
        "- Return the completed packet to the maintainer for comparison and adjudication.",
        "",
        "## Cases",
        "",
    ]

    for case in cases:
        lines.extend(
            [
                f"### {case['id']}",
                "",
                f"- Batch: `{case['batch']}`",
                f"- Domain: `{case['domain']}`",
                f"- Source: {source_line(case.get('source', {}))}",
                "",
                "Input:",
                "",
                code_block(str(case["input"])),
                "",
                "Blind reviewer:",
                "",
                "```text",
                "",
                "```",
                "",
                "Blind expected:",
                "",
                "```text",
                "",
                "```",
                "",
                "Reviewer notes:",
                "",
                "```text",
                "",
                "```",
                "",
            ]
        )

    lines.extend(
        [
            "## Coordinator Import Rules",
            "",
            (
                "- If blind expected exactly matches the first pass, set "
                '`review.blind_reviewer` and `review.status = "approved"`.'
            ),
            (
                "- If blind expected differs but is an acceptable Taiwan variant, "
                "record it in `review.acceptable` or adjudicate before approval."
            ),
            (
                "- If blind expected conflicts with the first pass, set "
                "`review.disagreement = true` and send the case to adjudication."
            ),
            (
                "- Never mark a case `approved` when first reviewer and blind reviewer "
                "are the same person."
            ),
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backlog", type=Path, default=DEFAULT_BACKLOG)
    parser.add_argument("--batch", default=None)
    parser.add_argument("--status", default=DEFAULT_STATUS)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--generated-date", default=dt.date.today().isoformat())
    args = parser.parse_args()

    backlog = load_backlog(args.backlog)
    cases = selected_cases(backlog, batch=args.batch, status=args.status)
    if not cases:
        print(
            f"No cases matched status={args.status!r} batch={args.batch!r}",
            file=sys.stderr,
        )
        return 1

    output = args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    content = render_markdown(
        args.backlog,
        backlog,
        cases,
        batch=args.batch,
        status=args.status,
        generated_date=args.generated_date,
    )
    output.write_text(content, encoding="utf-8")
    print(f"Wrote {relative_path(output)} ({len(cases)} cases)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
