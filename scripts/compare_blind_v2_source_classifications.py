#!/usr/bin/env python3
"""Compare Codex/Gemini input-only source classifications and render review queue."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
FIELDS = ("eligible", "script", "domain", "risk")


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON must be an object")
    return value


def case_map(report: dict[str, Any], *, label: str) -> dict[str, dict[str, Any]]:
    cases = report.get("cases")
    if not isinstance(cases, list):
        raise ValueError(f"{label}: cases must be an array")
    mapped = {case["id"]: case for case in cases}
    if len(mapped) != len(cases):
        raise ValueError(f"{label}: duplicate case ids")
    return mapped


def code_block(text: str) -> str:
    fence = "```"
    while fence in text:
        fence += "`"
    return f"{fence}text\n{text}\n{fence}"


def format_value(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "yes" if value else "no"
    return str(value)


def build_comparison(
    packet: dict[str, Any], codex: dict[str, Any], gemini: dict[str, Any]
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    packet_cases = case_map(packet, label="packet")
    codex_cases = case_map(codex, label="codex")
    gemini_cases = case_map(gemini, label="gemini")
    expected_ids = list(packet_cases)
    for label, mapped in (("codex", codex_cases), ("gemini", gemini_cases)):
        if set(mapped) != set(expected_ids):
            raise ValueError(f"{label}: ids do not exactly cover packet")

    differences: list[dict[str, Any]] = []
    by_field = {field: 0 for field in FIELDS}
    for case_id in expected_ids:
        changed = [
            field for field in FIELDS if codex_cases[case_id][field] != gemini_cases[case_id][field]
        ]
        for field in changed:
            by_field[field] += 1
        if changed:
            differences.append(
                {
                    "id": case_id,
                    "input": packet_cases[case_id]["input"],
                    "changed_fields": changed,
                    "codex": codex_cases[case_id],
                    "gemini": gemini_cases[case_id],
                }
            )
    stats = {
        "total": len(expected_ids),
        "exact": len(expected_ids) - len(differences),
        "review_queue": len(differences),
        "by_field": by_field,
    }
    return stats, differences


def render_markdown(
    packet: dict[str, Any],
    codex: dict[str, Any],
    gemini: dict[str, Any],
    *,
    generated_date: str,
    maintainer_decisions: dict[str, Any] | None = None,
) -> str:
    stats, differences = build_comparison(packet, codex, gemini)
    decision_cases = (
        case_map(maintainer_decisions, label="maintainer decisions")
        if maintainer_decisions is not None
        else {}
    )
    difference_ids = {item["id"] for item in differences}
    if decision_cases and not difference_ids.issubset(decision_cases):
        raise ValueError("maintainer decisions must cover the complete review queue")
    resolved = bool(decision_cases) and difference_ids.issubset(decision_cases)
    lines = [
        "<!-- zhtw:disable -->",
        (f"# Blind-v2 Source Classification Diff {packet['batch_number']:03d} ({generated_date})"),
        "",
        (
            "Status: all advisory disagreements resolved by maintainer"
            if resolved
            else "Status: advisory only; maintainer decisions pending"
        ),
        "",
        f"Packet SHA-256: `{codex['packet_sha256']}`",
        f"Cases: {stats['total']}",
        f"Exact Codex/Gemini classifications: {stats['exact']}",
        f"Maintainer review queue: {stats['review_queue']}",
        "",
        "Field differences:",
        "",
        f"- Eligibility: {stats['by_field']['eligible']}",
        f"- Script: {stats['by_field']['script']}",
        f"- Domain: {stats['by_field']['domain']}",
        f"- Risk: {stats['by_field']['risk']}",
        "",
        "## Policy Finding",
        "",
        (
            f"Gemini marked {gemini['stats']['policy_violations']} cases as eligible even though "
            "its own quality flags identified malformed or fragmentary input. These suggestions "
            "fail the declared source-quality rule and are not auto-adopted."
            if gemini["stats"]["policy_violations"]
            else "Gemini reported no eligibility/quality-policy conflicts; its validation also "
            "recorded zero tool calls and zero API errors."
        ),
        "",
        (
            f"The maintainer resolved all {stats['review_queue']} advisory disagreements and "
            f"batch-confirmed the {stats['exact']} exact AI matches after reviewing the Codex "
            "synthesis. No classification in this report has been written into the candidate pool."
            if resolved
            else "Neither advisory is auto-preferred. Codex must synthesize the differences before "
            "maintainer confirmation; no classification in this report has been written into the "
            "candidate pool."
        ),
        "",
        "## Review Queue",
        "",
    ]
    for number, item in enumerate(differences, 1):
        codex_case = item["codex"]
        gemini_case = item["gemini"]
        lines.extend(
            [
                f"### {number:02d}. {item['id']}",
                "",
                f"Changed: `{', '.join(item['changed_fields'])}`",
                "",
                "Input:",
                "",
                code_block(item["input"]),
                "",
                "| Reviewer | Eligible | Domain | Risk | Confidence | Quality |",
                "|----------|----------|--------|------|------------|---------|",
                (
                    f"| Codex | {format_value(codex_case['eligible'])} | "
                    f"{format_value(codex_case['domain'])} | {format_value(codex_case['risk'])} | "
                    f"{codex_case['confidence']} | "
                    f"{', '.join(codex_case['quality_flags']) or '-'} |"
                ),
                (
                    f"| Gemini | {format_value(gemini_case['eligible'])} | "
                    f"{format_value(gemini_case['domain'])} | "
                    f"{format_value(gemini_case['risk'])} | {gemini_case['confidence']} | "
                    f"{', '.join(gemini_case['quality_flags']) or '-'} |"
                ),
                "",
                f"Codex reason: {codex_case['notes']}",
                "",
                f"Gemini reason: {gemini_case['notes']}",
                "",
                (
                    f"Maintainer decision: `{decision_cases[item['id']]['selected_advisory']}` "
                    f"accepted by `{maintainer_decisions['maintainer']}` on "
                    f"`{maintainer_decisions['decision_date']}`"
                    if resolved
                    else "Maintainer decision: `pending`"
                ),
                "",
            ]
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packet", type=Path, required=True)
    parser.add_argument("--codex", type=Path, required=True)
    parser.add_argument("--gemini", type=Path, required=True)
    parser.add_argument("--generated-date", required=True)
    parser.add_argument("--maintainer-decisions", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    decisions = load_json(args.maintainer_decisions) if args.maintainer_decisions else None
    content = render_markdown(
        load_json(args.packet),
        load_json(args.codex),
        load_json(args.gemini),
        generated_date=args.generated_date,
        maintainer_decisions=decisions,
    )
    if args.check:
        if not args.output.is_file() or args.output.read_text(encoding="utf-8") != content:
            print("Blind-v2 source classification diff is stale", file=sys.stderr)
            return 1
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content, encoding="utf-8")
    print("Blind-v2 source classification diff generated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
