#!/usr/bin/env python3
"""Install hash-pinned competitor artifacts without unresolved build dependencies."""

from __future__ import annotations

import hashlib
import json
import platform
import shutil
import subprocess
import sys
import sysconfig
import tarfile
import tempfile
import urllib.request
from pathlib import Path, PurePosixPath
from typing import Any

LOCK_PATH = Path("/opt/competitors/python-artifacts.lock.json")
PLATFORM_NAMES = {"aarch64": "linux/arm64", "x86_64": "linux/amd64"}


def download(url: str, expected_hash: str, destination: Path) -> None:
    with urllib.request.urlopen(url, timeout=120) as response:
        content = response.read()
    actual_hash = hashlib.sha256(content).hexdigest()
    if actual_hash != expected_hash:
        raise ValueError(f"artifact sha256 mismatch: expected={expected_hash} actual={actual_hash}")
    destination.write_bytes(content)


def install_wheel(artifact: dict[str, Any], directory: Path) -> None:
    platform_name = PLATFORM_NAMES.get(platform.machine())
    if platform_name is None or platform_name not in artifact["platforms"]:
        raise ValueError(f"unsupported wheel platform: {platform.machine()}")
    source = artifact["platforms"][platform_name]
    wheel = directory / source["url"].rsplit("/", 1)[-1]
    download(source["url"], source["sha256"], wheel)
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "--no-deps", "--no-index", str(wheel)],
        check=True,
    )


def validated_members(archive: tarfile.TarFile, prefix: PurePosixPath) -> list[tarfile.TarInfo]:
    selected: list[tarfile.TarInfo] = []
    for member in archive.getmembers():
        path = PurePosixPath(member.name)
        if path.is_absolute() or ".." in path.parts or member.issym() or member.islnk():
            raise ValueError(f"unsafe sdist member: {member.name}")
        relative = PurePosixPath(*path.parts[1:])
        if relative == prefix or prefix in relative.parents:
            selected.append(member)
    return selected


def install_pure_python_sdist(artifact: dict[str, Any], directory: Path) -> None:
    source = directory / "source.tar.gz"
    download(artifact["url"], artifact["sha256"], source)
    site_packages = Path(sysconfig.get_paths()["purelib"])
    with tarfile.open(source, "r:gz") as archive:
        for target_name in ("zhconv", "zhconv.egg-info"):
            members = validated_members(archive, PurePosixPath(target_name))
            if not members:
                raise ValueError(f"sdist is missing {target_name}")
            for member in members:
                relative = Path(*PurePosixPath(member.name).parts[1:])
                destination = site_packages / relative
                if member.isdir():
                    destination.mkdir(parents=True, exist_ok=True)
                elif member.isfile():
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    extracted = archive.extractfile(member)
                    if extracted is None:
                        raise ValueError(f"cannot extract {member.name}")
                    with extracted, destination.open("wb") as output:
                        shutil.copyfileobj(extracted, output)


def main() -> int:
    lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory() as raw_directory:
        directory = Path(raw_directory)
        for artifact in lock["artifacts"]:
            mode = artifact["install_mode"]
            if mode == "wheel":
                install_wheel(artifact, directory)
            elif mode == "pure_python_sdist":
                install_pure_python_sdist(artifact, directory)
            else:
                raise ValueError(f"unsupported install mode: {mode}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
