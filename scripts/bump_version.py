#!/usr/bin/env python3
"""Update every zhtw mono-versioned file without OS-specific sed flags."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

SEMVER = re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$")


def replace_required(
    path: Path,
    pattern: str,
    replacement: str,
    *,
    count: int = 0,
    minimum: int = 1,
) -> None:
    text = path.read_text(encoding="utf-8")
    updated, replacements = re.subn(pattern, replacement, text, count=count, flags=re.MULTILINE)
    if replacements < minimum:
        raise SystemExit(f"Expected version pattern was not found in {path}")
    path.write_text(updated, encoding="utf-8")


def update_readme(path: Path, version: str) -> None:
    substitutions = (
        (r"<version>[0-9][0-9.]*</version>", f"<version>{version}</version>"),
        (r"com\.rajatim:zhtw:[0-9][0-9.]*", f"com.rajatim:zhtw:{version}"),
        (r"rev: v[0-9][0-9.]*", f"rev: v{version}"),
        (r'zhtw = "[0-9][0-9.]*"', f'zhtw = "{version}"'),
        (r"sdk%2Fgo%2Fv[0-9][0-9.]*", f"sdk%2Fgo%2Fv{version}"),
    )
    for pattern, replacement in substitutions:
        replace_required(path, pattern, replacement, minimum=0)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("version")
    args = parser.parse_args()
    version = args.version
    if not SEMVER.fullmatch(version):
        raise SystemExit(f"Version must be stable SemVer X.Y.Z, got: {version}")

    replace_required(Path("pyproject.toml"), r"^version = .*", f'version = "{version}"', count=1)
    replace_required(
        Path("src/zhtw/__init__.py"),
        r"^__version__ = .*",
        f'__version__ = "{version}"',
        count=1,
    )
    replace_required(
        Path("sdk/java/pom.xml"),
        r"^    <version>[^<]*</version>",
        f"    <version>{version}</version>",
        count=1,
    )
    replace_required(
        Path("sdk/typescript/package.json"),
        r'^  "version": "[^"]*"',
        f'  "version": "{version}"',
        count=1,
    )
    replace_required(
        Path("sdk/rust/Cargo.toml"),
        r'(?ms)(^\[workspace\.package\].*?^version = ")[0-9][0-9.]*(")',
        rf"\g<1>{version}\g<2>",
        count=1,
    )
    replace_required(
        Path("sdk/rust/zhtw-wasm/package.json"),
        r'^  "version": "[^"]*"',
        f'  "version": "{version}"',
        count=1,
    )
    replace_required(
        Path("sdk/dotnet/Zhtw.csproj"),
        r"<Version>[^<]*</Version>",
        f"<Version>{version}</Version>",
        count=1,
    )
    replace_required(
        Path("AGENTS.md"),
        r"^> \*\*v[0-9][0-9.]*\*\*",
        f"> **v{version}**",
        count=1,
    )

    for readme in (
        Path("README.md"),
        Path("README.en.md"),
        Path("sdk/java/README.md"),
        Path("sdk/go/README.md"),
        Path("sdk/dotnet/README.md"),
        Path("sdk/rust/zhtw/README.md"),
    ):
        if readme.exists():
            update_readme(readme, version)

    replace_required(
        Path("sdk/java/BENCHMARK.md"),
        r"\| SDK Version \| [0-9][0-9.]* \|",
        f"| SDK Version | {version} |",
        count=1,
    )


if __name__ == "__main__":
    main()
