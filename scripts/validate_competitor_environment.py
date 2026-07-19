#!/usr/bin/env python3
"""Validate the locked benchmark competitor environment and optional runtime image."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.benchmark_metrics import canonical_json_bytes  # noqa: E402
from scripts.competitor_benchmark import load_engines  # noqa: E402

DEFAULT_LOCK = PROJECT_ROOT / "benchmarks" / "accuracy" / "competitors.lock.json"
SCHEMA = PROJECT_ROOT / "benchmarks" / "accuracy" / "competitors-lock.schema.json"


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON must be an object")
    return value


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def project_path(raw: str) -> Path:
    path = (PROJECT_ROOT / raw).resolve()
    try:
        path.relative_to(PROJECT_ROOT)
    except ValueError as exc:
        raise ValueError(f"path escapes project root: {raw}") from exc
    return path


def computed_environment_hash(files: dict[str, str]) -> str:
    return hashlib.sha256(canonical_json_bytes(files)).hexdigest()


def validate_lock(path: Path) -> list[str]:
    lock = load_json(path)
    schema = load_json(SCHEMA)
    errors = [
        f"{error.json_path}: {error.message}"
        for error in sorted(
            Draft202012Validator(
                schema,
                format_checker=FormatChecker(),
            ).iter_errors(lock),
            key=lambda item: list(item.path),
        )
    ]
    if errors:
        return errors

    environment = lock["environment"]
    for raw_path, expected_hash in environment["files"].items():
        try:
            path_in_project = project_path(raw_path)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if not path_in_project.is_file():
            errors.append(f"environment file does not exist: {raw_path}")
        elif sha256_file(path_in_project) != expected_hash:
            errors.append(f"environment file hash mismatch: {raw_path}")
    actual_environment = computed_environment_hash(environment["files"])
    if actual_environment != environment["environment_sha256"]:
        errors.append(
            "environment_sha256 mismatch: "
            f"expected={environment['environment_sha256']} actual={actual_environment}"
        )

    dockerfile_path = project_path(environment["dockerfile"])
    if not dockerfile_path.is_file():
        errors.append(f"Dockerfile does not exist: {environment['dockerfile']}")
    else:
        dockerfile = dockerfile_path.read_text(encoding="utf-8")
        if "latest" in dockerfile.lower() or "@sha256:" not in dockerfile:
            errors.append("Dockerfile must use digest-pinned base images and no latest tag")
        for image in environment["base_images"].values():
            pinned = f"{image['reference']}@{image['index_digest']}"
            if pinned not in dockerfile:
                errors.append(f"Dockerfile does not contain pinned base image: {pinned}")

    competitors = lock["competitors"]
    ids = [item["id"] for item in competitors]
    if len(ids) != len(set(ids)):
        errors.append("competitor ids must be unique")
    formal_ids = set(lock["formal_engine_ids"])
    if formal_ids != {item["id"] for item in competitors if item["included_in_formal_runner"]}:
        errors.append("formal_engine_ids do not match included_in_formal_runner competitors")

    python_artifacts = load_json(
        project_path("benchmarks/accuracy/competitor-env/python-artifacts.lock.json")
    )
    competitors_by_package = {item["package"]: item for item in competitors}
    for artifact in python_artifacts.get("artifacts", []):
        package = artifact.get("package")
        competitor = competitors_by_package.get(package)
        if competitor is None or competitor["version"] != artifact.get("version"):
            errors.append(f"Python artifact does not match competitor lock: {package}")
            continue
        artifact_hashes = (
            {artifact["sha256"]}
            if "sha256" in artifact
            else {item["sha256"] for item in artifact.get("platforms", {}).values()}
        )
        if artifact_hashes != set(competitor["artifact_sha256"].values()):
            errors.append(f"Python artifact hashes do not match competitor lock: {package}")

    package_lock = load_json(project_path("benchmarks/accuracy/competitor-env/package-lock.json"))
    opencc_js = competitors_by_package.get("opencc-js", {})
    npm_entry = package_lock.get("packages", {}).get("node_modules/opencc-js", {})
    if npm_entry.get("version") != opencc_js.get("version") or not npm_entry.get("integrity"):
        errors.append("opencc-js npm lock does not match competitor lock")

    represented: set[str] = set()
    for family in lock["ranking_families"]:
        family_ids = set(family["engine_ids"])
        if family["ranking_representative"] not in family_ids:
            errors.append(f"ranking representative is outside family: {family['id']}")
        if represented & family_ids:
            errors.append(f"engines appear in multiple ranking families: {family['id']}")
        represented.update(family_ids)
        for engine_id in family_ids:
            match = next((item for item in competitors if item["id"] == engine_id), None)
            if match is None or match["family"] != family["id"]:
                errors.append(f"ranking family metadata mismatch: {family['id']}/{engine_id}")
    if represented != formal_ids:
        errors.append("ranking families must cover every formal engine exactly once")
    return errors


def validate_runtime(lock: dict[str, Any], image: str) -> list[str]:
    engine_ids = [engine_id for engine_id in lock["formal_engine_ids"] if engine_id != "zhtw"]
    engines = load_engines(engine_ids, lock=lock, container_image=image)
    errors = [f"{engine.name}: {engine.error}" for engine in engines if not engine.available]
    smoke_input = "API 1.0\n開發軟體"
    for engine in engines:
        if not engine.available or engine.convert is None:
            continue
        try:
            first = engine.convert(smoke_input)
            second = engine.convert(smoke_input)
        except Exception as exc:
            errors.append(f"{engine.name}: smoke conversion failed: {exc}")
            continue
        if first != second:
            errors.append(f"{engine.name}: smoke conversion is not deterministic")
        if not first.startswith("API 1.0\n開發"):
            errors.append(f"{engine.name}: smoke output failed preservation/conversion checks")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lock", type=Path, default=DEFAULT_LOCK)
    parser.add_argument("--image")
    args = parser.parse_args()
    errors = validate_lock(args.lock.resolve())
    lock = load_json(args.lock.resolve())
    if not errors and args.image:
        errors.extend(validate_runtime(lock, args.image))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    suffix = f"; runtime image={args.image}" if args.image else ""
    print(f"competitor environment valid{suffix}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
