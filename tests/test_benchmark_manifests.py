"""Tests for benchmark manifests, licenses, and preregistration validation."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

import scripts.validate_benchmark_assets as validator
from scripts.benchmark_metrics import paired_power_analysis

ROOT = Path(__file__).resolve().parents[1]
ACCURACY_ROOT = ROOT / "benchmarks" / "accuracy"


def write_json(path: Path, value: dict[str, object]) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def fixture_manifest(root: Path) -> tuple[Path, dict[str, object]]:
    normalized = root / "normalized.json"
    raw = root / "raw.txt"
    importer = root / "scripts" / "import_fixture.py"
    importer.parent.mkdir()
    normalized.write_text('{"cases":[]}\n', encoding="utf-8")
    raw.write_text("source\n", encoding="utf-8")
    importer.write_text("# fixture\n", encoding="utf-8")
    manifest = {
        "version": 1,
        "id": "fixture-v1",
        "track": "external_context",
        "source_urls": ["https://example.test/source"],
        "upstream_revision": "revision-1",
        "retrieved_at": "2026-07-19T00:00:00Z",
        "license": "CC BY 4.0",
        "license_url": "https://creativecommons.org/licenses/by/4.0/",
        "output_license": "CC BY 4.0",
        "attribution": "Fixture authors",
        "modification_notice": "Normalized for tests.",
        "notice_id": "fixture-v1",
        "raw_sha256": {"raw.txt": hashlib.sha256(raw.read_bytes()).hexdigest()},
        "normalized_path": "normalized.json",
        "normalized_sha256": hashlib.sha256(normalized.read_bytes()).hexdigest(),
        "importer": "scripts/import_fixture.py",
        "known_biases": ["Test-only fixture."],
        "allowed_uses": ["evaluation", "public_reporting"],
        "tuning_policy": "public_track_only",
    }
    path = root / "manifest.json"
    write_json(path, manifest)
    return path, manifest


def fixture_notice() -> str:
    return """## fixture-v1
CC BY 4.0
Fixture authors
Normalized for tests.
"""


def test_manifest_schema_requires_license_revision_and_hashes(tmp_path: Path) -> None:
    path, manifest = fixture_manifest(tmp_path)
    for field in ("license", "upstream_revision", "normalized_sha256"):
        invalid = dict(manifest)
        invalid.pop(field)
        write_json(path, invalid)
        errors = validator.validate_manifest(path, licenses=fixture_notice())
        assert any(field in error for error in errors)


def test_manifest_validates_notice_and_artifact_hashes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    path, _ = fixture_manifest(tmp_path)
    monkeypatch.setattr(validator, "PROJECT_ROOT", tmp_path)

    assert validator.validate_manifest(path, licenses=fixture_notice()) == []
    assert any(
        "missing license notice" in error
        for error in validator.validate_manifest(path, licenses="# no notice\n")
    )

    (tmp_path / "normalized.json").write_text("changed\n", encoding="utf-8")
    assert any(
        "normalized_sha256" in error
        for error in validator.validate_manifest(path, licenses=fixture_notice())
    )


def test_manifest_rejects_paths_outside_project(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    path, manifest = fixture_manifest(tmp_path)
    manifest["normalized_path"] = "../outside.json"
    write_json(path, manifest)
    monkeypatch.setattr(validator, "PROJECT_ROOT", tmp_path)

    errors = validator.validate_manifest(path, licenses=fixture_notice())

    assert any("escapes project root" in error for error in errors)


def test_manifest_rejects_pending_license_metadata(tmp_path: Path) -> None:
    path, manifest = fixture_manifest(tmp_path)
    manifest["license"] = "Pending verification"
    write_json(path, manifest)

    errors = validator.validate_manifest(path, licenses=fixture_notice())

    assert any("placeholder metadata" in error for error in errors)


def test_preregistration_locks_ranking_and_artifact_hashes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    manifest_path, manifest = fixture_manifest(tmp_path)
    inputs = tmp_path / "inputs.json"
    expected = tmp_path / "expected.json"
    lock = tmp_path / "lock.json"
    ranking = tmp_path / "ranking.json"
    for path in (inputs, expected, lock):
        path.write_text("{}\n", encoding="utf-8")
    write_json(ranking, {"id": "market-ranking-v1"})
    power = paired_power_analysis(discordant_rate=0.03)
    preregistration = {
        "version": 1,
        "id": "blind-v2-run-1",
        "status": "frozen",
        "created_at": "2026-07-19T00:00:00Z",
        "dataset_id": manifest["id"],
        "dataset_manifest_sha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
        "inputs_sha256": hashlib.sha256(inputs.read_bytes()).hexdigest(),
        "expected_sha256": hashlib.sha256(expected.read_bytes()).hexdigest(),
        "zhtw_git_sha": "a" * 40,
        "competitor_lock_sha256": hashlib.sha256(lock.read_bytes()).hexdigest(),
        "normalization_id": "zhtw-exact-v1",
        "primary_endpoint": "blind-v2.accepted_accuracy",
        "ranking_policy_id": "market-ranking-v1",
        "ranking_policy_sha256": hashlib.sha256(ranking.read_bytes()).hexdigest(),
        "power_analysis": {
            "method": "paired_mcnemar_normal_approximation",
            "discordant_rate": 0.03,
            "minimum_detectable_effect": 0.02,
            "alpha": 0.05,
            "target_power": 0.8,
            "required_cases": power["required_cases"],
            "selected_cases": 600,
        },
    }
    preregistration_path = tmp_path / "preregistration.json"
    write_json(preregistration_path, preregistration)
    monkeypatch.setattr(validator, "RANKING_POLICY", ranking)

    assert (
        validator.validate_preregistration(
            preregistration_path,
            manifest_path=manifest_path,
            inputs_path=inputs,
            expected_path=expected,
            lock_path=lock,
        )
        == []
    )

    preregistration["power_analysis"]["selected_cases"] = 599  # type: ignore[index]
    write_json(preregistration_path, preregistration)
    errors = validator.validate_preregistration(preregistration_path)
    assert any("selected_cases" in error for error in errors)


def test_ranking_policy_is_fixed() -> None:
    policy = json.loads((ACCURACY_ROOT / "ranking-policy-v1.json").read_text(encoding="utf-8"))

    assert policy["primary_track"] == "blind-v2"
    assert policy["primary_endpoint"] == "accepted_accuracy"
    assert policy["cross_track_total_allowed"] is False
    assert policy["p0_disqualifies"] is True
    assert policy["winner_rule"] == "paired_delta_ci_95_low_gt_zero"
    assert policy["tie_rule"] == "paired_delta_ci_95_includes_zero"


def test_license_notices_cover_planned_external_tracks() -> None:
    licenses = (ACCURACY_ROOT / "LICENSES.md").read_text(encoding="utf-8")

    for notice_id in ("ud-gsd-v1", "naer-terms-v1", "sc-tc-regional-v1"):
        assert f"## {notice_id}" in licenses
