#!/usr/bin/env python3
"""Create a deterministic input-only classification packet from Blind-v2 pilots."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.benchmark_metrics import canonical_json_bytes  # noqa: E402
from scripts.blind_v2_governance import apportion  # noqa: E402

ACCURACY_ROOT = PROJECT_ROOT / "benchmarks" / "accuracy"
PACKET_SCHEMA = ACCURACY_ROOT / "blind-v2.source-classification-packet.schema.json"
DEFAULT_SOURCES = (
    ACCURACY_ROOT / "external" / "flores-200-zho-hans-v1.json",
    ACCURACY_ROOT / "external" / "ud-chinese-cfl-v1.json",
)
DEFAULT_SEED = 20260719


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON must be an object")
    return value


def relative_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path.resolve())


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rank(seed: int, case_id: str) -> str:
    return hashlib.sha256(f"{seed}\0{case_id}".encode()).hexdigest()


def build_packet(
    source_paths: list[Path],
    *,
    batch_size: int,
    batch_number: int,
    seed: int,
    generated_date: str,
    all_source_cases: bool = False,
    selection_round: int | None = None,
) -> dict[str, Any]:
    if not all_source_cases and batch_size < len(source_paths):
        raise ValueError("batch size must be at least the number of sources")
    if batch_number < 1:
        raise ValueError("batch number must be at least 1")
    if selection_round is not None and selection_round < 1:
        raise ValueError("selection round must be at least 1")

    sources: list[tuple[Path, dict[str, Any]]] = []
    for path in source_paths:
        source = load_json(path)
        if source.get("input_only") is not True or source.get("converter_output_used") is not False:
            raise ValueError(f"{path}: source must be input-only with no converter output")
        sources.append((path, source))
    sources.sort(key=lambda item: item[1]["id"])

    if all_source_cases:
        quotas = {source["id"]: len(source["cases"]) for _, source in sources}
        selection_policy = "all-source-cases-sorted-v1"
    else:
        weights = tuple((source["id"], 1) for _, source in sources)
        quotas = apportion(batch_size, weights)
        selection_policy = "equal-source-deterministic-sha256-v1"
    selected: list[dict[str, Any]] = []
    source_snapshots: list[dict[str, str]] = []
    for path, source in sources:
        source_id = source["id"]
        required = quotas[source_id]
        if all_source_cases:
            source_cases = sorted(source["cases"], key=lambda case: case["id"])
            start = 0
        else:
            start = ((selection_round or batch_number) - 1) * required
            ranked = sorted(source["cases"], key=lambda case: (rank(seed, case["id"]), case["id"]))
            source_cases = ranked[start : start + required]
        if len(source_cases) != required:
            raise ValueError(
                f"{source_id}: batch {batch_number} requires {required} cases at offset "
                f"{start}, has {len(source_cases)}"
            )
        source_snapshots.append(
            {
                "id": source_id,
                "path": relative_path(path),
                "sha256": sha256_file(path),
            }
        )
        for case in source_cases:
            selected.append(
                {
                    "id": case["id"],
                    "input": case["input"],
                    "source_id": source_id,
                    "provenance": case["provenance"],
                    "classification": {
                        "eligible": None,
                        "script": None,
                        "domain": None,
                        "risk": None,
                        "quality_flags": [],
                        "confidence": None,
                        "notes": "",
                    },
                }
            )
    selected.sort(key=lambda case: case["id"])

    packet = {
        "version": 1,
        "name": f"blind-v2-source-classification-batch-{batch_number:03d}",
        "dataset": "blind-v2",
        "status": "needs_codex_first_pass",
        "generated_date": generated_date,
        "seed": seed,
        "batch_number": batch_number,
        "batch_size": len(selected),
        "selection_policy": selection_policy,
        "input_only": True,
        "converter_output_used": False,
        "source_snapshots": source_snapshots,
        "stats": {
            "total": len(selected),
            "by_source": quotas,
        },
        "cases": selected,
    }
    if selection_round is not None:
        packet["selection_round"] = selection_round
    return packet


def validate_packet(packet: dict[str, Any]) -> list[str]:
    schema = load_json(PACKET_SCHEMA)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [
        f"{error.json_path}: {error.message}"
        for error in sorted(validator.iter_errors(packet), key=lambda item: list(item.path))
    ]


def code_block(text: str) -> str:
    fence = "```"
    while fence in text:
        fence += "`"
    return f"{fence}text\n{text}\n{fence}"


def render_markdown(packet_path: Path, packet: dict[str, Any]) -> str:
    lines = [
        "<!-- zhtw:disable -->",
        f"# Blind-v2 Source Classification {packet['batch_number']:03d}",
        "",
        f"Packet: `{relative_path(packet_path)}`",
        f"Cases: {packet['stats']['total']}",
        f"Seed: `{packet['seed']}`",
        f"Selection: `{packet['selection_policy']}`",
        *([f"Selection round: {packet['selection_round']}"] if "selection_round" in packet else []),
        "",
        "## Rules",
        "",
        "- Read only the input and provenance shown in this packet.",
        "- Do not run zhtw, OpenCC, zhconv, Gemini, or another converter.",
        "- Mark `eligible = no` for malformed, unclear, non-Mandarin, or unsuitable text.",
        "- Script: `simplified`, `mixed`, `traditional`, or `uncertain`.",
        (
            "- Domain: `it_api_cli`, `ui_i18n`, `llm_generated`, `formal_news`, "
            "`social_daily`, or `high_stakes`."
        ),
        "- Risk: `candidate_gap`, `over_conversion_guard`, or `baseline_guard`.",
        "- Confidence: `high`, `medium`, or `low`; do not guess when context is insufficient.",
        "- This packet is advisory input classification, not expected-output annotation.",
        "",
        "## Cases",
        "",
    ]
    for case in packet["cases"]:
        lines.extend(
            [
                f"### {case['id']}",
                "",
                f"- Source: `{case['source_id']}`",
                f"- Source case: `{case['provenance']['source_case_id']}`",
                f"- Split: `{case['provenance']['split']}`",
                "",
                "Input:",
                "",
                code_block(case["input"]),
                "",
                "Classification:",
                "",
                "```text",
                "eligible:",
                "script:",
                "domain:",
                "risk:",
                "quality_flags:",
                "confidence:",
                "notes:",
                "```",
                "",
            ]
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", action="append", type=Path, default=[])
    parser.add_argument("--batch-size", type=int, default=100)
    parser.add_argument("--batch-number", type=int, default=1)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--all-source-cases", action="store_true")
    parser.add_argument("--selection-round", type=int)
    parser.add_argument("--generated-date", default=dt.date.today().isoformat())
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--markdown-output", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    source_paths = args.source or list(DEFAULT_SOURCES)
    packet = build_packet(
        source_paths,
        batch_size=args.batch_size,
        batch_number=args.batch_number,
        seed=args.seed,
        generated_date=args.generated_date,
        all_source_cases=args.all_source_cases,
        selection_round=args.selection_round,
    )
    errors = validate_packet(packet)
    if errors:
        raise ValueError("invalid classification packet: " + "; ".join(errors))
    content = canonical_json_bytes(packet)
    markdown = render_markdown(args.output, packet) if args.markdown_output else None
    if args.check:
        stale = not args.output.is_file() or args.output.read_bytes() != content
        if args.markdown_output and markdown is not None:
            stale = stale or not args.markdown_output.is_file()
            stale = stale or args.markdown_output.read_text(encoding="utf-8") != markdown
        if stale:
            print("Blind-v2 source classification packet is stale", file=sys.stderr)
            return 1
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(content)
        if args.markdown_output and markdown is not None:
            args.markdown_output.parent.mkdir(parents=True, exist_ok=True)
            args.markdown_output.write_text(markdown, encoding="utf-8")
    print(f"classification packet: {packet['stats']['total']} input-only cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
