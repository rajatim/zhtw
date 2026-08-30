#!/usr/bin/env python3
"""Check the curated public documentation contract."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10
    import tomli as tomllib


ROOT = Path(__file__).resolve().parents[1]
PAIRS = (
    "index",
    "guides/getting-started",
    "guides/cli-and-files",
    "guides/sdk-and-browser",
    "guides/contributing",
    "reference/conversion-behavior",
    "reference/explain-api",
    "reference/json-adapter",
    "reference/rule-schema-v2",
    "reference/roadmap",
    "testing/quality-and-evidence",
    "releases/current",
)
FORBIDDEN_PUBLIC_TEXT = (
    "4.5.0 開發中",
    "4.5.0 in development",
    "build #31",
    "verify #13",
    "release #26",
    "CREDENTIAL_PREFLIGHT",
    "APPROVAL_REFERENCE",
    "1Password",
    "credential ID",
)


def fail(message: str) -> None:
    raise SystemExit(f"public docs check failed: {message}")


def run_cli(*args: str) -> str:
    completed = subprocess.run(
        [sys.executable, "-m", "zhtw", *args],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout


def main() -> None:
    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]
    version = project["version"]
    config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")

    contents: list[tuple[Path, str]] = []
    for stem in PAIRS:
        for suffix in (".md", ".en.md"):
            path = ROOT / "docs" / f"{stem}{suffix}"
            if not path.is_file():
                fail(f"missing bilingual page: {path.relative_to(ROOT)}")
            text = path.read_text(encoding="utf-8")
            contents.append((path, text))
        if f"{stem}.md" not in config:
            fail(f"curated page is absent from mkdocs nav: {stem}.md")

    for path, text in contents:
        for forbidden in FORBIDDEN_PUBLIC_TEXT:
            if forbidden.casefold() in text.casefold():
                fail(f"internal or stale text {forbidden!r} found in {path.relative_to(ROOT)}")

    current_zh = (ROOT / "docs/releases/current.md").read_text(encoding="utf-8")
    current_en = (ROOT / "docs/releases/current.en.md").read_text(encoding="utf-8")
    if f"目前版本：**{version}**" not in current_zh:
        fail("Traditional Chinese current-version page does not match pyproject.toml")
    if f"Current version: **{version}**" not in current_en:
        fail("English current-version page does not match pyproject.toml")

    cli_version = run_cli("--version").strip()
    if version not in cli_version:
        fail(f"CLI version differs from pyproject.toml: {cli_version}")

    explained = json.loads(run_cli("explain", "软件", "--source", "cn", "--json"))
    if explained["output"] != "軟體":
        fail("documented explain example no longer returns 軟體")
    if not any(event["outcome"] == "applied" for event in explained["events"]):
        fail("documented explain example has no applied event")

    print(f"public docs check passed: {len(PAIRS)} bilingual pairs, zhtw {version}")


if __name__ == "__main__":
    main()
