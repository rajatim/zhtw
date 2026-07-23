#!/usr/bin/env python3
"""Build a deterministic Codex synthesis from two input-only advisories."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_synthesis(
    codex: dict[str, Any],
    gemini: dict[str, Any],
    *,
    gemini_case_ids: set[str],
    generated_date: str,
    overrides: dict[str, dict[str, Any]] | None = None,
    override_basis: str = "maintainer_feedback",
) -> dict[str, Any]:
    if codex["packet_sha256"] != gemini["packet_sha256"]:
        raise ValueError("advisory packet hashes do not match")

    gemini_by_id = {case["id"]: case for case in gemini["cases"]}
    if set(gemini_by_id) != {case["id"] for case in codex["cases"]}:
        raise ValueError("advisories do not cover the same case IDs")
    unknown = gemini_case_ids - set(gemini_by_id)
    if unknown:
        raise ValueError(f"unknown Gemini override IDs: {sorted(unknown)}")
    overrides = overrides or {}
    if override_basis not in {"codex_synthesis", "maintainer_feedback"}:
        raise ValueError(f"invalid override basis: {override_basis}")
    unknown = set(overrides) - set(gemini_by_id)
    if unknown:
        raise ValueError(f"unknown maintainer override IDs: {sorted(unknown)}")

    cases: list[dict[str, Any]] = []
    bases: Counter[str] = Counter()
    classification_fields = ("eligible", "script", "domain", "risk")
    output_fields = (*classification_fields, "quality_flags", "confidence")
    for case_id, override in overrides.items():
        if set(override) != set(output_fields):
            raise ValueError(f"invalid maintainer override fields for {case_id}")
        if override["eligible"] != (
            override["domain"] is not None and override["risk"] is not None
        ):
            raise ValueError(f"invalid eligibility labels for {case_id}")
    for codex_case in codex["cases"]:
        gemini_case = gemini_by_id[codex_case["id"]]
        exact = all(codex_case[field] == gemini_case[field] for field in classification_fields)
        if codex_case["id"] in overrides:
            selected = overrides[codex_case["id"]]
            basis = override_basis
        elif exact:
            selected = codex_case
            basis = "agreement"
        elif codex_case["id"] in gemini_case_ids:
            selected = gemini_case
            basis = "gemini"
        else:
            selected = codex_case
            basis = "codex"

        case = {"id": codex_case["id"]}
        case.update({field: selected[field] for field in output_fields})
        case["notes"] = (
            "Codex 依 input-only 獨立可裁決性、來源品質、臺灣領域語境與 "
            "Gemini 獨立意見完成第二輪綜合判斷。"
        )
        case["selection_basis"] = basis
        cases.append(case)
        bases[basis] += 1

    return {
        "version": 1,
        "dataset": "blind-v2",
        "reviewer": "Codex synthesis after independent Gemini review",
        "stage": "codex_synthesis_advisory",
        "status": "advisory_only",
        "generated_date": generated_date,
        "packet_path": codex["packet_path"],
        "packet_sha256": codex["packet_sha256"],
        "policy": "input_only_no_converter_output",
        "stats": {
            "total": len(cases),
            "eligible": sum(case["eligible"] for case in cases),
            "excluded": sum(not case["eligible"] for case in cases),
            "by_selection_basis": dict(sorted(bases.items())),
        },
        "cases": cases,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--codex", type=Path, required=True)
    parser.add_argument("--gemini", type=Path, required=True)
    parser.add_argument("--gemini-case-id", action="append", default=[])
    parser.add_argument("--overrides", type=Path)
    parser.add_argument("--synthesis-overrides", type=Path)
    parser.add_argument("--generated-date", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    codex = load(args.codex)
    if args.overrides and args.synthesis_overrides:
        raise ValueError("maintainer and Codex synthesis overrides are mutually exclusive")
    overrides: dict[str, dict[str, Any]] = {}
    override_path = args.overrides or args.synthesis_overrides
    override_basis = "codex_synthesis" if args.synthesis_overrides else "maintainer_feedback"
    if override_path:
        override_report = load(override_path)
        if override_report.get("packet_sha256") != codex.get("packet_sha256"):
            raise ValueError("override packet hash does not match")
        if len({case["id"] for case in override_report["cases"]}) != len(override_report["cases"]):
            raise ValueError("duplicate override IDs")
        overrides = {case["id"]: case["classification"] for case in override_report["cases"]}
    result = build_synthesis(
        codex,
        load(args.gemini),
        gemini_case_ids=set(args.gemini_case_id),
        generated_date=args.generated_date,
        overrides=overrides,
        override_basis=override_basis,
    )
    content = (json.dumps(result, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    if args.check:
        if not args.output.exists() or args.output.read_bytes() != content:
            raise SystemExit(f"stale synthesis: {args.output}")
        return 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(content)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
