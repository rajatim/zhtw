#!/usr/bin/env python3
"""Advance the idempotency baseline version only when every result is unchanged."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict
from pathlib import Path

from scripts.audit_corpus_idempotency import build_summary

SEMVER = re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$")
DEFAULT_INPUTS = Path("benchmarks/accuracy/blind-v2.inputs.json")
DEFAULT_BASELINE = Path("benchmarks/accuracy/blind-v2.idempotency-baseline.json")


def update_baseline(version: str, inputs_path: Path, baseline_path: Path) -> None:
    if not SEMVER.fullmatch(version):
        raise ValueError(f"Version must be stable SemVer X.Y.Z, got: {version}")
    summary = asdict(build_summary(inputs_path))
    if summary["converter_version"] != version:
        raise ValueError(
            f"loaded converter is {summary['converter_version']!r}, expected {version!r}"
        )

    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    expected = {key: value for key, value in baseline.items() if key != "converter_version"}
    actual = {key: value for key, value in summary.items() if key != "converter_version"}
    if expected != actual:
        changed = sorted(
            key for key in set(expected) | set(actual) if expected.get(key) != actual.get(key)
        )
        raise ValueError(
            "idempotency results changed; review before advancing the baseline: "
            + ", ".join(changed)
        )

    baseline["converter_version"] = version
    baseline_path.write_text(
        json.dumps(baseline, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("version")
    parser.add_argument("--inputs", type=Path, default=DEFAULT_INPUTS)
    parser.add_argument("--baseline", type=Path, default=DEFAULT_BASELINE)
    args = parser.parse_args()
    try:
        update_baseline(args.version, args.inputs, args.baseline)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(str(exc)) from exc


if __name__ == "__main__":
    main()
