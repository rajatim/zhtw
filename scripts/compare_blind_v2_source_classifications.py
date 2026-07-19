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
) -> str:
    stats, differences = build_comparison(packet, codex, gemini)
    lines = [
        "<!-- zhtw:disable -->",
        f"# Blind-v2 Source Classification Diff 001 ({generated_date})",
        "",
        "Status: advisory only; maintainer decisions pending",
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
        ),
        "",
        "Codex is the current conservative recommendation. Neither AI review is a human decision, "
        "and no classification in this report has been written into the candidate pool.",
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
                "Maintainer decision: `pending`",
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
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    content = render_markdown(
        load_json(args.packet),
        load_json(args.codex),
        load_json(args.gemini),
        generated_date=args.generated_date,
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
