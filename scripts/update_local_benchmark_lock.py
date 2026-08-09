#!/usr/bin/env python3
"""Bind the local zhtw benchmark entry to the mono-versioned SDK data."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

SEMVER = re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$")
LOCK_PATH = Path("benchmarks/accuracy/competitors.lock.json")
DATA_PATH = Path("sdk/data/zhtw-data.json")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("version")
    args = parser.parse_args()
    if not SEMVER.fullmatch(args.version):
        raise SystemExit(f"Version must be stable SemVer X.Y.Z, got: {args.version}")

    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    if data.get("version") != args.version:
        raise SystemExit(
            f"{DATA_PATH} version is {data.get('version')!r}, expected {args.version!r}"
        )
    digest = hashlib.sha256(DATA_PATH.read_bytes()).hexdigest()

    lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    matches = [item for item in lock.get("competitors", []) if item.get("id") == "zhtw"]
    if len(matches) != 1:
        raise SystemExit("competitors lock must contain exactly one zhtw entry")
    local = matches[0]
    artifact_hashes = local.get("artifact_sha256")
    if local.get("adapter") != "local_python" or set(artifact_hashes or {}) != {str(DATA_PATH)}:
        raise SystemExit("zhtw benchmark entry does not match the reviewed local adapter contract")

    local["version"] = args.version
    artifact_hashes[str(DATA_PATH)] = digest
    local["config_sha256"] = digest
    LOCK_PATH.write_text(
        json.dumps(lock, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
