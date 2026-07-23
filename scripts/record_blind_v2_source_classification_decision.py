#!/usr/bin/env python3
"""Record maintainer decisions for a Blind-v2 source-classification packet."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ACCURACY_ROOT = PROJECT_ROOT / "benchmarks" / "accuracy"
SCHEMA = ACCURACY_ROOT / "blind-v2.source-classification-decision.schema.json"
CLASSIFICATION_FIELDS = (
    "eligible",
    "script",
    "domain",
    "risk",
    "quality_flags",
    "confidence",
    "notes",
)
COMPARISON_FIELDS = ("eligible", "script", "domain", "risk")


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON must be an object")
    return value


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative_path(path: Path) -> str:
    return str(path.resolve().relative_to(PROJECT_ROOT))


def case_map(report: dict[str, Any], *, label: str) -> dict[str, dict[str, Any]]:
    cases = report.get("cases")
    if not isinstance(cases, list):
        raise ValueError(f"{label}: cases must be an array")
    mapped = {case["id"]: case for case in cases}
    if len(mapped) != len(cases):
        raise ValueError(f"{label}: duplicate case ids")
    return mapped


def build_decision(
    packet_path: Path,
    codex_path: Path,
    gemini_path: Path,
    *,
    maintainer: str,
    decision_date: str,
    selected_advisory: str,
    synthesis_path: Path | None = None,
) -> dict[str, Any]:
    packet = load_json(packet_path)
    codex = load_json(codex_path)
    gemini = load_json(gemini_path)
    packet_hash = sha256_file(packet_path)
    if codex.get("packet_sha256") != packet_hash or gemini.get("packet_sha256") != packet_hash:
        raise ValueError("advisory packet hashes do not match the classification packet")

    packet_cases = case_map(packet, label="packet")
    codex_cases = case_map(codex, label="codex")
    gemini_cases = case_map(gemini, label="gemini")
    if set(packet_cases) != set(codex_cases) or set(packet_cases) != set(gemini_cases):
        raise ValueError("advisories must exactly cover the classification packet")

    if selected_advisory == "codex":
        selected = codex_cases
    elif selected_advisory == "gemini":
        selected = gemini_cases
    else:
        if synthesis_path is None:
            raise ValueError("synthesis advisory path is required")
        synthesis = load_json(synthesis_path)
        if synthesis.get("packet_sha256") != packet_hash:
            raise ValueError("synthesis packet hash does not match the classification packet")
        selected = case_map(synthesis, label="synthesis")
        if set(packet_cases) != set(selected):
            raise ValueError("synthesis must exactly cover the classification packet")
    disagreements = {
        case_id
        for case_id in packet_cases
        if any(
            codex_cases[case_id][field] != gemini_cases[case_id][field]
            for field in COMPARISON_FIELDS
        )
    }
    cases = []
    for case_id in packet_cases:
        cases.append(
            {
                "id": case_id,
                "advisory_relation": (
                    "disagreement" if case_id in disagreements else "exact_match"
                ),
                "selected_advisory": selected_advisory,
                "classification": {
                    field: selected[case_id][field] for field in CLASSIFICATION_FIELDS
                },
            }
        )
    decision = {
        "version": 1,
        "dataset": "blind-v2",
        "stage": "source_classification_maintainer_decision",
        "status": "all_classifications_confirmed",
        "decision_date": decision_date,
        "maintainer": maintainer,
        "decision_method": "batch_human_confirmation",
        "packet_path": relative_path(packet_path),
        "packet_sha256": packet_hash,
        "codex_path": relative_path(codex_path),
        "codex_sha256": sha256_file(codex_path),
        "gemini_path": relative_path(gemini_path),
        "gemini_sha256": sha256_file(gemini_path),
        "stats": {
            "packet_cases": len(packet_cases),
            "confirmed_cases": len(packet_cases),
            "resolved_disagreements": len(disagreements),
            "confirmed_exact_matches": len(packet_cases) - len(disagreements),
            "remaining_cases": 0,
        },
        "cases": cases,
    }
    if selected_advisory == "synthesis" and synthesis_path is not None:
        decision["synthesis_path"] = relative_path(synthesis_path)
        decision["synthesis_sha256"] = sha256_file(synthesis_path)
    return decision


def validate_decision(decision: dict[str, Any]) -> list[str]:
    validator = Draft202012Validator(load_json(SCHEMA), format_checker=FormatChecker())
    return [
        f"{error.json_path}: {error.message}"
        for error in sorted(validator.iter_errors(decision), key=lambda item: list(item.path))
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packet", type=Path, required=True)
    parser.add_argument("--codex", type=Path, required=True)
    parser.add_argument("--gemini", type=Path, required=True)
    parser.add_argument("--synthesis", type=Path)
    parser.add_argument("--maintainer", required=True)
    parser.add_argument("--decision-date", required=True)
    parser.add_argument(
        "--selected-advisory", choices=("codex", "gemini", "synthesis"), required=True
    )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    decision = build_decision(
        args.packet,
        args.codex,
        args.gemini,
        maintainer=args.maintainer,
        decision_date=args.decision_date,
        selected_advisory=args.selected_advisory,
        synthesis_path=args.synthesis,
    )
    errors = validate_decision(decision)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    content = json.dumps(decision, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.check:
        if not args.output.is_file() or args.output.read_text(encoding="utf-8") != content:
            print("Blind-v2 source classification decision is stale", file=sys.stderr)
            return 1
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content, encoding="utf-8")
    print(f"Blind-v2 source classification decision recorded: {len(decision['cases'])} cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
