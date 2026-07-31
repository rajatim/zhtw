"""Tests for the public benchmark reproduction attestation."""

from __future__ import annotations

from scripts.reproduce_public_benchmarks import build_attestation, compare_track
from scripts.validate_public_benchmark_attestation import validate_attestation


def report(score: int) -> dict[str, object]:
    return {
        "dataset": "track-1",
        "manifest_sha256": "a" * 64,
        "normalized_sha256": "b" * 64,
        "scores": {"exact": score},
    }


def test_compare_track_requires_identical_metadata_and_scores() -> None:
    result = compare_track("track-1", report(10), report(10))

    assert result["passed"] is True
    assert result["scores_match"] is True
    assert result["baseline_scores_sha256"] == result["reproduced_scores_sha256"]


def test_compare_track_rejects_score_difference() -> None:
    result = compare_track("track-1", report(10), report(9))

    assert result["passed"] is False
    assert result["scores_match"] is False


def test_attestation_requires_clean_worktree_and_passing_tracks() -> None:
    passed_track = compare_track("track-1", report(10), report(10))

    passed = build_attestation(
        operator="outside-reviewer",
        organization=None,
        relationship="independent_third_party",
        repository_url="https://example.com/fork.git",
        tool_git_sha="c" * 40,
        source_git_sha="d" * 40,
        clean_worktree=True,
        tracks=[passed_track],
    )
    dirty = build_attestation(
        operator="outside-reviewer",
        organization=None,
        relationship="independent_third_party",
        repository_url="https://example.com/fork.git",
        tool_git_sha="c" * 40,
        source_git_sha="d" * 40,
        clean_worktree=False,
        tracks=[passed_track],
    )

    assert passed["status"] == "passed"
    assert passed["scope"] == "public_secondary_tracks_only"
    assert dirty["status"] == "failed"


def test_validator_rejects_local_smoke_test_as_independent_evidence() -> None:
    track = compare_track("ud-gsd-v1", report(10), report(10))
    track["track"] = "ud-gsd-v1"
    track["baseline_report_sha256"] = "e" * 64
    track["reproduced_report_sha256"] = "f" * 64
    second_track = {**track, "track": "naer-terms-v1"}
    attestation = build_attestation(
        operator="maintainer",
        organization=None,
        relationship="project_local_smoke_test",
        repository_url="https://example.com/fork.git",
        tool_git_sha="c" * 40,
        source_git_sha="4b7f0e66fa0262021d0ec8e37acfae881b06bc4b",
        clean_worktree=True,
        tracks=[track, second_track],
    )

    assert validate_attestation(attestation, require_independent=False) == []
    assert validate_attestation(attestation, require_independent=True) == [
        "relationship must be independent_third_party"
    ]
