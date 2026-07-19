#!/usr/bin/env python3
"""Import a pinned Simplified Chinese source as a Blind-v2 input-only pilot."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import sys
import tarfile
import unicodedata
import urllib.request
from collections import Counter
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.benchmark_metrics import canonical_json_bytes  # noqa: E402
from scripts.import_ud_gsd_benchmark import parse_conllu  # noqa: E402

ACCURACY_ROOT = PROJECT_ROOT / "benchmarks" / "accuracy"
PILOT_SCHEMA = ACCURACY_ROOT / "blind-v2.source-pilot.schema.json"
SUPPORTED_SOURCES = {
    "flores-200-zho-hans-v1": "flores",
    "ud-chinese-cfl-v1": "ud_cfl",
}


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON must be an object")
    return value


def normalize_input(text: str) -> str:
    return " ".join(unicodedata.normalize("NFC", text).split())


def read_raw_source(manifest: dict[str, Any], source_file: Path | None = None) -> tuple[str, bytes]:
    raw_sha256 = manifest["raw_sha256"]
    markers = {
        "flores-200-zho-hans-v1": "flores200_dataset.tar.gz",
        "ud-chinese-cfl-v1": "zh_cfl-ud-test.conllu",
    }
    marker = markers.get(manifest["id"])
    data_urls = [url for url in raw_sha256 if marker and url.endswith(marker)]
    if not data_urls and len(raw_sha256) == 1:
        data_urls = list(raw_sha256)
    if len(data_urls) != 1:
        raise ValueError("source pilot manifest must identify exactly one source data file")
    data_url = data_urls[0]
    data_content: bytes | None = None
    for url, expected_hash in raw_sha256.items():
        if source_file is not None:
            if url != data_url:
                continue
            content = source_file.read_bytes()
        else:
            with urllib.request.urlopen(url, timeout=120) as response:
                content = response.read()
        actual_hash = sha256_bytes(content)
        if actual_hash != expected_hash:
            raise ValueError(f"raw sha256 mismatch for {url}: {actual_hash}")
        if url == data_url:
            data_content = content
    if data_content is None:
        raise ValueError("source data file was not read")
    return data_url, data_content


def parse_flores(content: bytes) -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = []
    members = (
        ("dev", "./flores200_dataset/dev/zho_Hans.dev"),
        ("devtest", "./flores200_dataset/devtest/zho_Hans.devtest"),
    )
    with tarfile.open(fileobj=io.BytesIO(content), mode="r:gz") as archive:
        for split, member_name in members:
            member = archive.getmember(member_name)
            extracted = archive.extractfile(member)
            if extracted is None:
                raise ValueError(f"FLORES archive member is not a file: {member_name}")
            lines = extracted.read().decode("utf-8").splitlines()
            rows.extend(
                (split, f"{split}-{index:04d}", text) for index, text in enumerate(lines, 1)
            )
    return rows


def parse_ud_cfl(content: bytes) -> list[tuple[str, str, str]]:
    sentences = parse_conllu(content.decode("utf-8"), source="UD Chinese-CFL")
    return [("test", sent_id, sentence.text) for sent_id, sentence in sorted(sentences.items())]


def build_dataset(manifest: dict[str, Any], *, source_file: Path | None = None) -> dict[str, Any]:
    source_kind = SUPPORTED_SOURCES.get(manifest["id"])
    if source_kind is None:
        raise ValueError(f"unsupported Blind-v2 source pilot: {manifest['id']}")
    raw_url, content = read_raw_source(manifest, source_file)
    raw_rows = parse_flores(content) if source_kind == "flores" else parse_ud_cfl(content)

    cases: list[dict[str, Any]] = []
    exclusions = Counter()
    seen_inputs: set[str] = set()
    by_split = Counter()
    for split, source_case_id, raw_text in raw_rows:
        text = normalize_input(raw_text)
        if not text:
            exclusions["empty_after_normalization"] += 1
            continue
        if text in seen_inputs:
            exclusions["exact_duplicate_within_source"] += 1
            continue
        seen_inputs.add(text)
        by_split[split] += 1
        cases.append(
            {
                "id": f"{manifest['id']}/{source_case_id}",
                "input": text,
                "provenance": {
                    "raw_url": raw_url,
                    "source_case_id": source_case_id,
                    "split": split,
                },
                "classification": {
                    "domain": None,
                    "risk": None,
                    "status": "needs_input_only_review",
                },
            }
        )

    return {
        "version": 1,
        "id": manifest["id"],
        "dataset": "blind-v2",
        "purpose": "candidate_source_pilot",
        "input_only": True,
        "converter_output_used": False,
        "source_class": "permissive_license",
        "license": manifest["output_license"],
        "attribution": manifest["attribution"],
        "modification_notice": manifest["modification_notice"],
        "upstream_revision": manifest["upstream_revision"],
        "review_policy": "domain_and_risk_must_be_assigned_from_input_only",
        "stats": {
            "raw_cases": len(raw_rows),
            "eligible_pending_review": len(cases),
            "by_split": dict(sorted(by_split.items())),
            "exclusions": dict(sorted(exclusions.items())),
        },
        "cases": cases,
    }


def validate_dataset(dataset: dict[str, Any]) -> list[str]:
    schema = load_json(PILOT_SCHEMA)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [
        f"{error.json_path}: {error.message}"
        for error in sorted(validator.iter_errors(dataset), key=lambda item: list(item.path))
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--source-file", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    manifest = load_json(args.manifest)
    output = args.output or PROJECT_ROOT / manifest["normalized_path"]
    dataset = build_dataset(manifest, source_file=args.source_file)
    errors = validate_dataset(dataset)
    if errors:
        raise ValueError("invalid source pilot: " + "; ".join(errors))
    content = canonical_json_bytes(dataset)
    if args.check:
        if not output.is_file() or output.read_bytes() != content:
            print(f"normalized source pilot is stale: {output}", file=sys.stderr)
            return 1
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(content)
    print(
        f"{manifest['id']}: {dataset['stats']['eligible_pending_review']} input-only cases; "
        f"sha256={sha256_bytes(content)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
