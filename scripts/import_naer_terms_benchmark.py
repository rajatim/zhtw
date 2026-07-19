#!/usr/bin/env python3
"""Import the pinned NAER cross-strait computer terminology dataset."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import sys
import unicodedata
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.benchmark_metrics import canonical_json_bytes  # noqa: E402

DEFAULT_MANIFEST = PROJECT_ROOT / "benchmarks" / "accuracy" / "manifests" / "naer-terms-v1.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "benchmarks" / "accuracy" / "external" / "naer-terms-v1.json"
EXPECTED_HEADERS = ("序號", "英文名稱", "中文名稱", "中國大陸譯名", "來源網站")

MARKER_PATTERNS = (
    ("multi_value_delimiter", re.compile(r"[;；、/／|｜,，]")),
    ("annotation", re.compile(r"[()（）\[\]【】{}]")),
    ("sentence_punctuation", re.compile(r"[。！？!?]")),
)


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def normalize_text(value: str) -> str:
    return unicodedata.normalize("NFC", value.strip())


def comparison_key(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value).casefold()
    return " ".join(normalized.split())


def structure_cell(value: str) -> dict[str, Any]:
    raw = normalize_text(value)
    markers = [name for name, pattern in MARKER_PATTERNS if pattern.search(raw)]
    if markers:
        return {
            "raw": raw,
            "status": "unresolved_compound",
            "values": [],
            "markers": markers,
        }
    return {"raw": raw, "status": "atomic", "values": [raw], "markers": []}


def parse_csv(content: bytes, *, source: str) -> list[dict[str, str]]:
    try:
        text = content.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValueError(f"{source}: CSV must be UTF-8") from exc
    reader = csv.DictReader(io.StringIO(text, newline=""))
    if tuple(reader.fieldnames or ()) != EXPECTED_HEADERS:
        raise ValueError(f"{source}: unexpected CSV headers: {reader.fieldnames}")

    rows: list[dict[str, str]] = []
    seen_sequences: set[str] = set()
    for line_number, raw_row in enumerate(reader, start=2):
        if None in raw_row:
            raise ValueError(f"{source}:{line_number}: extra CSV columns")
        row = {field: normalize_text(raw_row[field] or "") for field in EXPECTED_HEADERS}
        if any(not row[field] for field in EXPECTED_HEADERS):
            raise ValueError(f"{source}:{line_number}: required field is empty")
        sequence = row["序號"]
        if not sequence.isdecimal():
            raise ValueError(f"{source}:{line_number}: sequence must be numeric")
        if sequence in seen_sequences:
            raise ValueError(f"{source}:{line_number}: duplicate sequence {sequence}")
        seen_sequences.add(sequence)
        rows.append(row)
    if not rows:
        raise ValueError(f"{source}: no terminology rows found")
    return rows


def read_raw_source(url: str, expected_hash: str, *, source_file: Path | None) -> bytes:
    if source_file is None:
        with urllib.request.urlopen(url, timeout=60) as response:
            content = response.read()
    else:
        content = source_file.read_bytes()
    actual_hash = sha256_bytes(content)
    if actual_hash != expected_hash:
        raise ValueError(f"raw sha256 mismatch for {url}: {actual_hash}")
    return content


def load_manifest(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("manifest must be a JSON object")
    return value


def _initial_record(row: dict[str, str], dataset_id: str) -> dict[str, Any]:
    english = structure_cell(row["英文名稱"])
    taiwan = structure_cell(row["中文名稱"])
    mainland = structure_cell(row["中國大陸譯名"])
    reasons: list[str] = []
    for name, cell in (("english", english), ("taiwan", taiwan), ("mainland", mainland)):
        if cell["status"] != "atomic":
            reasons.append(f"{name}_field_requires_structure_review")
    if len(mainland["raw"]) <= 1 or len(taiwan["raw"]) <= 1:
        reasons.append("single_character_bare_term")

    candidate_kind: str | None = None
    if not reasons:
        candidate_kind = "identity_guard" if mainland["raw"] == taiwan["raw"] else "conversion"
    return {
        "id": f"{dataset_id}/source/{int(row['序號']):04d}",
        "source_sequence": int(row["序號"]),
        "english": english,
        "taiwan": taiwan,
        "mainland": mainland,
        "source_website": row["來源網站"],
        "candidate_kind": candidate_kind,
        "ambiguity_reasons": reasons,
    }


def build_dataset(manifest: dict[str, Any], *, source_file: Path | None = None) -> dict[str, Any]:
    if len(manifest["raw_sha256"]) != 1:
        raise ValueError("NAER manifest must contain exactly one raw CSV source")
    source_url, expected_hash = next(iter(manifest["raw_sha256"].items()))
    rows = parse_csv(
        read_raw_source(source_url, expected_hash, source_file=source_file),
        source=source_url,
    )
    records = [_initial_record(row, manifest["id"]) for row in rows]

    proposed: defaultdict[str, defaultdict[str, list[dict[str, Any]]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for record in records:
        if record["candidate_kind"] is None:
            continue
        input_text = (
            record["taiwan"]["raw"]
            if record["candidate_kind"] == "identity_guard"
            else record["mainland"]["raw"]
        )
        proposed[comparison_key(input_text)][comparison_key(record["taiwan"]["raw"])].append(record)

    for expected_groups in proposed.values():
        if len(expected_groups) <= 1:
            continue
        for grouped_records in expected_groups.values():
            for record in grouped_records:
                record["candidate_kind"] = None
                record["ambiguity_reasons"].append("input_maps_to_multiple_expected_values")

    merged: defaultdict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        kind = record["candidate_kind"]
        if kind is None:
            continue
        input_text = (
            record["taiwan"]["raw"] if kind == "identity_guard" else record["mainland"]["raw"]
        )
        expected = record["taiwan"]["raw"]
        merged[(kind, comparison_key(input_text), comparison_key(expected))].append(record)

    evaluation_cases: list[dict[str, Any]] = []
    by_kind: defaultdict[str, int] = defaultdict(int)
    for (kind, _, _), grouped_records in sorted(merged.items()):
        representative = min(grouped_records, key=lambda item: item["source_sequence"])
        input_text = (
            representative["taiwan"]["raw"]
            if kind == "identity_guard"
            else representative["mainland"]["raw"]
        )
        by_kind[kind] += 1
        case_id = f"{manifest['id']}/{kind}/{by_kind[kind]:04d}"
        case = {
            "id": case_id,
            "kind": kind,
            "domain": "computer_terminology",
            "input": input_text,
            "expected": representative["taiwan"]["raw"],
            "english_concepts": sorted({item["english"]["raw"] for item in grouped_records}),
            "source_record_ids": sorted(item["id"] for item in grouped_records),
        }
        evaluation_cases.append(case)
        for record in grouped_records:
            record["evaluation_case_id"] = case_id

    context_candidates = []
    for record in records:
        if record["candidate_kind"] is not None:
            continue
        context_candidates.append(
            {
                "id": record["id"].replace("/source/", "/context/"),
                "source_record_id": record["id"],
                "english_raw": record["english"]["raw"],
                "taiwan_raw": record["taiwan"]["raw"],
                "mainland_raw": record["mainland"]["raw"],
                "reasons": sorted(set(record["ambiguity_reasons"])),
                "review_status": "needs_context_sentence",
            }
        )

    kind_counts = {
        kind: sum(case["kind"] == kind for case in evaluation_cases)
        for kind in ("conversion", "identity_guard")
    }
    return {
        "version": 1,
        "id": manifest["id"],
        "track": manifest["track"],
        "evidence_role": "secondary_evidence",
        "primary_market_endpoint": False,
        "license": manifest["output_license"],
        "attribution": manifest["attribution"],
        "modification_notice": manifest["modification_notice"],
        "upstream_revision": manifest["upstream_revision"],
        "classification_policy": {
            "multi_value_parsing": (
                "No delimiter splitting; compound source cells remain unresolved."
            ),
            "deduplication": (
                "NFKC, casefold, and whitespace comparison keys; source text remains NFC."
            ),
            "ambiguity": (
                "Conflicting expected values and unresolved fields receive no expected output."
            ),
            "product_import": "prohibited",
        },
        "context_review_protocol": {
            "status": "candidate_packet_only",
            "required_stages": [
                "codex_first_pass",
                "gemini_independent_advisory",
                "maintainer_confirmation",
            ],
            "expected_policy": (
                "No context candidate receives an expected output before maintainer confirmation."
            ),
        },
        "stats": {
            "source_records": len(records),
            "evaluation_cases": len(evaluation_cases),
            "conversion_cases": kind_counts["conversion"],
            "identity_guard_cases": kind_counts["identity_guard"],
            "context_candidates": len(context_candidates),
        },
        "evaluation_cases": evaluation_cases,
        "context_candidates": context_candidates,
        "source_records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--source-file", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    manifest = load_manifest(args.manifest)
    dataset = build_dataset(manifest, source_file=args.source_file)
    content = canonical_json_bytes(dataset)
    if args.check:
        if not args.output.is_file() or args.output.read_bytes() != content:
            print("normalized NAER dataset is stale", file=sys.stderr)
            return 1
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(content)
    stats = dataset["stats"]
    print(
        f"NAER cases: conversion={stats['conversion_cases']}, "
        f"identity={stats['identity_guard_cases']}, context={stats['context_candidates']}; "
        f"sha256={sha256_bytes(content)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
