#!/usr/bin/env python3
"""Reject sensitive case-level data in publishable benchmark reports."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REPORTS_DIR = PROJECT_ROOT / "docs" / "reports"
FORBIDDEN_KEYS = {
    "rows",
    "private_expected",
    "expected",
    "acceptable",
    "output",
    "normalized_output",
    "annotation",
    "miss_ids",
    "miss_case_ids",
    "missed_case_ids",
}
PRIVATE_EXPECTED_MARKER = ".expected.json"
FORBIDDEN_MARKDOWN_MARKERS = (
    "\n## Misses\n",
    "\nExpected: `",
    "\nExpected:\n",
    "\nActual:\n",
    PRIVATE_EXPECTED_MARKER,
)


def find_sensitive_values(value: Any, path: str = "$") -> list[str]:
    findings: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if key in FORBIDDEN_KEYS:
                findings.append(child_path)
                continue
            findings.extend(find_sensitive_values(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            findings.extend(find_sensitive_values(child, f"{path}[{index}]"))
    elif isinstance(value, str) and PRIVATE_EXPECTED_MARKER in value:
        findings.append(path)
    return findings


def is_publishable_benchmark(path: Path, payload: dict[str, Any]) -> bool:
    return payload.get("report_mode") == "aggregate" or path.name.startswith("accuracy-benchmark-")


def tracked_reports() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "docs/reports/*.json", "docs/reports/*.md"],
        cwd=PROJECT_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [PROJECT_ROOT / line for line in result.stdout.splitlines() if line]


def audit_paths(paths: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in paths:
        if path.suffix == ".md":
            try:
                content = path.read_text(encoding="utf-8")
            except OSError as exc:
                errors.append(f"{path}: cannot read Markdown: {exc}")
                continue
            if "# Accuracy Benchmark" not in content and "Report mode: `aggregate`" not in content:
                continue
            for marker in FORBIDDEN_MARKDOWN_MARKERS:
                if marker in content:
                    errors.append(f"{path}: forbidden Markdown marker {marker!r}")
            continue
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path}: cannot read JSON: {exc}")
            continue
        if not isinstance(payload, dict) or not is_publishable_benchmark(path, payload):
            continue
        try:
            display_path = path.relative_to(PROJECT_ROOT)
        except ValueError:
            display_path = path
        for finding in find_sensitive_values(payload):
            errors.append(f"{display_path}: forbidden {finding}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path)
    args = parser.parse_args()
    paths = args.paths or tracked_reports()
    errors = audit_paths([path.resolve() for path in paths])
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"publication audit passed ({len(paths)} report files checked)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
