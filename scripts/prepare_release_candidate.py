#!/usr/bin/env python3
"""Promote the Unreleased changelog block and write exact release notes."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path

SEMVER = re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True)
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--notes-output", type=Path, required=True)
    args = parser.parse_args()

    if not SEMVER.fullmatch(args.version):
        raise SystemExit(f"Version must be stable SemVer X.Y.Z, got: {args.version}")
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", args.date):
        raise SystemExit(f"Date must be YYYY-MM-DD, got: {args.date}")

    changelog = Path("CHANGELOG.md")
    text = changelog.read_text(encoding="utf-8")
    heading = f"## [{args.version}] - {args.date}"
    if re.search(rf"^## \[{re.escape(args.version)}\](?: - .*)?$", text, re.MULTILINE):
        existing = re.search(
            rf"^## \[{re.escape(args.version)}\](?: - .*)?$",
            text,
            re.MULTILINE,
        )
        assert existing is not None
        if existing.group(0) != heading:
            raise SystemExit(f"CHANGELOG already has {existing.group(0)!r}; expected {heading!r}")
    else:
        marker = "## [Unreleased]\n"
        if text.count(marker) != 1:
            raise SystemExit("CHANGELOG must contain exactly one [Unreleased] heading")
        unreleased_match = re.search(
            r"^## \[Unreleased\]\n(?P<body>.*?)(?=^## \[)",
            text,
            re.MULTILINE | re.DOTALL,
        )
        if not unreleased_match or not unreleased_match.group("body").strip():
            raise SystemExit("CHANGELOG [Unreleased] section is empty")
        text = text.replace(marker, f"{marker}\n{heading}\n", 1)
        changelog.write_text(text, encoding="utf-8")

    notes_match = re.search(
        rf"^## \[{re.escape(args.version)}\](?: - [^\n]*)?\n(?P<body>.*?)(?=^## \[|\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not notes_match or not notes_match.group("body").strip():
        raise SystemExit(f"CHANGELOG section {args.version} is empty")
    args.notes_output.parent.mkdir(parents=True, exist_ok=True)
    args.notes_output.write_text(notes_match.group("body").strip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
