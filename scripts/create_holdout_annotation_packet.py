#!/usr/bin/env python3
"""Create a human annotation packet for sealed holdout inputs."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INPUTS = PROJECT_ROOT / "benchmarks" / "accuracy" / "blind-v1.inputs.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "docs" / "reports" / "holdout-annotation-packet-blind-v1.md"


def load_inputs(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def relative_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path)


def selected_cases(
    inputs: dict[str, Any],
    *,
    batch: str | None,
    id_from: str | None,
    id_to: str | None,
) -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    for case in inputs["cases"]:
        case_id = str(case["id"])
        if batch is not None and case.get("batch") != batch:
            continue
        if id_from is not None and case_id < id_from:
            continue
        if id_to is not None and case_id > id_to:
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
    inputs_path: Path,
    inputs: dict[str, Any],
    cases: list[dict[str, Any]],
    *,
    generated_date: str,
    reviewer_stage: str,
    batch: str | None,
    id_from: str | None,
    id_to: str | None,
) -> str:
    batch_label = batch or "all"
    id_range = f"{id_from or 'first'}..{id_to or 'last'}"
    lines = [
        "<!-- zhtw:disable -->",
        f"# Holdout Annotation Packet ({generated_date})",
        "",
        f"Inputs: `{relative_path(inputs_path)}`",
        f"Dataset: `{inputs['dataset']}`",
        f"Reviewer stage: `{reviewer_stage}`",
        f"Batch filter: `{batch_label}`",
        f"ID range: `{id_range}`",
        f"Cases: {len(cases)}",
        "",
        "## Reviewer Rules",
        "",
        "- Write Taiwan Traditional Chinese expected output from the Simplified input only.",
        "- Do not run zhtw, OpenCC, zhconv, Gemini, or any converter while filling this packet.",
        "- Do not open any generated converter output or benchmark report.",
        "- Keep the input text unchanged.",
        (
            "- Preserve punctuation and spacing unless a Taiwan Traditional output "
            "requires a direct change."
        ),
        "- Put optional variants in `Acceptable`, one per line.",
        "- Mark issue tags only from the provided list.",
        "- If unsure, write a short note instead of guessing.",
        "",
        "Allowed issue tags:",
        "",
        "- `over_conversion`",
        "- `under_conversion`",
        "- `regional_term`",
        "- `it_term`",
        "- `ui_term`",
        "- `formal_term`",
        "- `high_risk_term`",
        "- `punctuation`",
        "- `ambiguous_context`",
        "- `other`",
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
                f"- Risk: `{case['risk']}`",
                f"- Tags: `{', '.join(case.get('tags', []))}`",
                f"- Source: {source_line(case.get('source', {}))}",
                "",
                "Input:",
                "",
                code_block(str(case["input"])),
                "",
                "Reviewer:",
                "",
                "```text",
                "",
                "```",
                "",
                "Expected:",
                "",
                "```text",
                "",
                "```",
                "",
                "Acceptable:",
                "",
                "```text",
                "",
                "```",
                "",
                "Issue tags:",
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
            "## Coordinator Rules",
            "",
            "- This packet is an annotation aid, not ground truth by itself.",
            (
                "- Import completed values into `benchmarks/accuracy/blind-v1.expected.json` "
                "only after review."
            ),
            "- The expected file must stay private until benchmark publication.",
            "- The expected file must keep `source_inputs_sha256` matching the input file hash.",
            "- First and second reviewers must be different people.",
            "- Disagreements require `human_adjudication` and a non-empty adjudicator.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path, default=DEFAULT_INPUTS)
    parser.add_argument("--batch", default=None)
    parser.add_argument("--id-from", default=None)
    parser.add_argument("--id-to", default=None)
    parser.add_argument("--reviewer-stage", default="first_human_review")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--generated-date", default=dt.date.today().isoformat())
    args = parser.parse_args()

    inputs = load_inputs(args.inputs)
    cases = selected_cases(
        inputs,
        batch=args.batch,
        id_from=args.id_from,
        id_to=args.id_to,
    )
    if not cases:
        print(
            "No cases matched "
            f"batch={args.batch!r} id_from={args.id_from!r} id_to={args.id_to!r}",
            file=sys.stderr,
        )
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        render_markdown(
            args.inputs,
            inputs,
            cases,
            generated_date=args.generated_date,
            reviewer_stage=args.reviewer_stage,
            batch=args.batch,
            id_from=args.id_from,
            id_to=args.id_to,
        ),
        encoding="utf-8",
    )
    print(f"Wrote {relative_path(args.output)} ({len(cases)} cases)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
