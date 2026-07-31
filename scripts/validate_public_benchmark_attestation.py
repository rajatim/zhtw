#!/usr/bin/env python3
"""Validate an independent public benchmark reproduction attestation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCHEMA = PROJECT_ROOT / "benchmarks/accuracy/public-benchmark-reproduction-attestation.schema.json"
REQUIRED_TRACKS = {"ud-gsd-v1", "naer-terms-v1"}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON must be an object")
    return value


def validate_attestation(
    attestation: dict[str, Any], *, require_independent: bool = True
) -> list[str]:
    schema = load_json(SCHEMA)
    errors = [
        f"{error.json_path}: {error.message}"
        for error in sorted(
            Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(attestation),
            key=lambda item: list(item.path),
        )
    ]
    if errors:
        return errors
    if attestation["status"] != "passed":
        errors.append("status must be passed")
    if require_independent and attestation["relationship"] != "independent_third_party":
        errors.append("relationship must be independent_third_party")
    if not attestation["source_worktree_clean"]:
        errors.append("source worktree must be clean")
    tracks = attestation["tracks"]
    if {item["track"] for item in tracks} != REQUIRED_TRACKS:
        errors.append("attestation must contain each required track exactly once")
    for track in tracks:
        if not track["passed"] or not track["scores_match"]:
            errors.append(f"{track['track']}: reproduction did not pass")
        if not all(track["metadata_matches"].values()):
            errors.append(f"{track['track']}: metadata did not match")
        if track["baseline_scores_sha256"] != track["reproduced_scores_sha256"]:
            errors.append(f"{track['track']}: score hashes did not match")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("attestation", type=Path)
    parser.add_argument("--allow-local-smoke-test", action="store_true")
    args = parser.parse_args()
    errors = validate_attestation(
        load_json(args.attestation.resolve()),
        require_independent=not args.allow_local_smoke_test,
    )
    if errors:
        print("\n".join(errors))
        return 1
    print("public benchmark reproduction attestation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
