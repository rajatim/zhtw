#!/usr/bin/env python3
"""Validate benchmark manifests, licenses, hashes, and preregistrations."""

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

from scripts.benchmark_metrics import paired_power_analysis  # noqa: E402
from scripts.validate_competitor_environment import validate_lock  # noqa: E402

ACCURACY_ROOT = PROJECT_ROOT / "benchmarks" / "accuracy"
MANIFEST_SCHEMA = ACCURACY_ROOT / "manifest.schema.json"
PREREGISTRATION_SCHEMA = ACCURACY_ROOT / "preregistration.schema.json"
LICENSES = ACCURACY_ROOT / "LICENSES.md"
RANKING_POLICY = ACCURACY_ROOT / "ranking-policy-v1.json"
COMPETITORS_LOCK = ACCURACY_ROOT / "competitors.lock.json"
BLIND_V2_SCHEMAS = (
    ACCURACY_ROOT / "blind-v2.source-pilot.schema.json",
    ACCURACY_ROOT / "blind-v2.source-classification-packet.schema.json",
    ACCURACY_ROOT / "blind-v2.candidate-pool.schema.json",
    ACCURACY_ROOT / "blind-v2.inputs.schema.json",
    ACCURACY_ROOT / "blind-v2.expected.schema.json",
    ACCURACY_ROOT / "blind-v2.final-decisions.schema.json",
    ACCURACY_ROOT / "blind-v2.replacements.schema.json",
    ACCURACY_ROOT / "blind-v2.evaluation-ledger-event.schema.json",
)


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON must be an object")
    return value


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_schema(instance: dict[str, Any], schema_path: Path) -> list[str]:
    schema = load_json(schema_path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [
        f"{error.json_path}: {error.message}"
        for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.path))
    ]


def project_path(raw: str, *, label: str) -> Path:
    path = (PROJECT_ROOT / raw).resolve()
    try:
        path.relative_to(PROJECT_ROOT)
    except ValueError as exc:
        raise ValueError(f"{label} escapes project root") from exc
    return path


def validate_manifest(path: Path, licenses: str | None = None) -> list[str]:
    manifest = load_json(path)
    errors = validate_schema(manifest, MANIFEST_SCHEMA)
    if errors:
        return [f"{path}: {error}" for error in errors]

    placeholder_fields = (
        "upstream_revision",
        "license",
        "output_license",
        "attribution",
        "modification_notice",
    )
    for field in placeholder_fields:
        normalized = manifest[field].strip().lower()
        if any(marker in normalized for marker in ("pending", "unknown", "tbd", "not locked")):
            errors.append(f"{path}: {field} contains placeholder metadata")

    notice_text = LICENSES.read_text(encoding="utf-8") if licenses is None else licenses
    notice_heading = f"## {manifest['notice_id']}"
    if notice_heading not in notice_text:
        errors.append(f"{path}: missing license notice {notice_heading}")
    else:
        notice = notice_text.split(notice_heading, 1)[1].split("\n## ", 1)[0]
        for field in ("license", "output_license", "attribution", "modification_notice"):
            if manifest[field] not in notice:
                errors.append(f"{path}: license notice does not contain {field}")

    try:
        importer = project_path(manifest["importer"], label="importer")
        if not importer.is_file():
            errors.append(f"{path}: importer does not exist: {manifest['importer']}")
    except ValueError as exc:
        errors.append(f"{path}: {exc}")

    try:
        normalized = project_path(manifest["normalized_path"], label="normalized_path")
        if not normalized.is_file():
            errors.append(
                f"{path}: normalized dataset does not exist: {manifest['normalized_path']}"
            )
        elif sha256_file(normalized) != manifest["normalized_sha256"]:
            errors.append(f"{path}: normalized_sha256 does not match {manifest['normalized_path']}")
    except ValueError as exc:
        errors.append(f"{path}: {exc}")

    for raw_path, expected_hash in manifest["raw_sha256"].items():
        if "://" in raw_path:
            continue
        try:
            source = project_path(raw_path, label="raw_sha256 path")
            if not source.is_file():
                errors.append(f"{path}: raw source does not exist: {raw_path}")
            elif sha256_file(source) != expected_hash:
                errors.append(f"{path}: raw sha256 does not match {raw_path}")
        except ValueError as exc:
            errors.append(f"{path}: {exc}")
    return errors


def validate_preregistration(
    path: Path,
    *,
    manifest_path: Path | None = None,
    inputs_path: Path | None = None,
    expected_path: Path | None = None,
    lock_path: Path | None = None,
) -> list[str]:
    preregistration = load_json(path)
    errors = validate_schema(preregistration, PREREGISTRATION_SCHEMA)
    if errors:
        return [f"{path}: {error}" for error in errors]

    hash_checks = (
        ("dataset_manifest_sha256", manifest_path),
        ("inputs_sha256", inputs_path),
        ("expected_sha256", expected_path),
        ("competitor_lock_sha256", lock_path),
        ("ranking_policy_sha256", RANKING_POLICY),
    )
    for field, artifact in hash_checks:
        if artifact is not None and sha256_file(artifact) != preregistration[field]:
            errors.append(f"{path}: {field} does not match {artifact}")

    if manifest_path is not None:
        manifest = load_json(manifest_path)
        if preregistration["dataset_id"] != manifest.get("id"):
            errors.append(f"{path}: dataset_id does not match manifest id")

    ranking_policy = load_json(RANKING_POLICY)
    if preregistration["ranking_policy_id"] != ranking_policy.get("id"):
        errors.append(f"{path}: ranking_policy_id does not match ranking policy")

    declared_power = preregistration["power_analysis"]
    computed_power = paired_power_analysis(
        discordant_rate=declared_power["discordant_rate"],
        minimum_detectable_effect=declared_power["minimum_detectable_effect"],
        alpha=declared_power["alpha"],
        target_power=declared_power["target_power"],
    )
    if declared_power["required_cases"] != computed_power["required_cases"]:
        errors.append(f"{path}: required_cases does not match power analysis")

    if (
        preregistration["power_analysis"]["selected_cases"]
        < preregistration["power_analysis"]["required_cases"]
    ):
        errors.append(f"{path}: selected_cases is below required_cases")
    return errors


def discover(directory: Path) -> list[Path]:
    return sorted(directory.glob("*.json")) if directory.is_dir() else []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", action="append", type=Path, default=[])
    parser.add_argument("--preregistration", action="append", type=Path, default=[])
    parser.add_argument("--require-assets", action="store_true")
    args = parser.parse_args()

    errors: list[str] = []
    for schema_path in (
        MANIFEST_SCHEMA,
        PREREGISTRATION_SCHEMA,
        ACCURACY_ROOT / "competitors-lock.schema.json",
        *BLIND_V2_SCHEMAS,
    ):
        try:
            Draft202012Validator.check_schema(load_json(schema_path))
        except Exception as exc:
            errors.append(f"{schema_path}: invalid schema: {exc}")
    for required_path in (LICENSES, RANKING_POLICY, COMPETITORS_LOCK):
        if not required_path.is_file():
            errors.append(f"required benchmark governance file missing: {required_path}")

    if COMPETITORS_LOCK.is_file():
        errors.extend(f"{COMPETITORS_LOCK}: {error}" for error in validate_lock(COMPETITORS_LOCK))

    manifests = args.manifest or discover(ACCURACY_ROOT / "manifests")
    preregistrations = args.preregistration or discover(ACCURACY_ROOT / "preregistrations")
    if args.require_assets and (not manifests or not preregistrations):
        print("formal validation requires a manifest and preregistration", file=sys.stderr)
        return 1

    for manifest in manifests:
        errors.extend(validate_manifest(manifest.resolve()))
    for preregistration in preregistrations:
        errors.extend(validate_preregistration(preregistration.resolve()))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(
        f"benchmark assets valid (manifests={len(manifests)}, "
        f"preregistrations={len(preregistrations)})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
