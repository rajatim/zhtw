#!/usr/bin/env python3
"""Reproduce public benchmark scores in a clean worktree and write an attestation."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import platform
import subprocess
import tempfile
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SOURCE_GIT_SHA = "4b7f0e66fa0262021d0ec8e37acfae881b06bc4b"
GENERATED_DATE = "2026-07-31"
TRACKS = {
    "ud-gsd-v1": {
        "report": "docs/reports/ud-gsd-benchmark-2026-07-31.json",
        "runner": "scripts/run_ud_gsd_benchmark.py",
        "output": "ud-gsd",
    },
    "naer-terms-v1": {
        "report": "docs/reports/naer-terms-benchmark-2026-07-31.json",
        "runner": "scripts/run_naer_terms_benchmark.py",
        "output": "naer-terms",
    },
}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON must be an object")
    return value


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def canonical_sha256(value: Any) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return sha256_bytes(encoded.encode())


def compare_track(
    track_id: str, baseline: dict[str, Any], reproduced: dict[str, Any]
) -> dict[str, Any]:
    fields = ("dataset", "manifest_sha256", "normalized_sha256")
    metadata_matches = {field: baseline.get(field) == reproduced.get(field) for field in fields}
    scores_match = baseline.get("scores") == reproduced.get("scores")
    return {
        "track": track_id,
        "metadata_matches": metadata_matches,
        "scores_match": scores_match,
        "baseline_scores_sha256": canonical_sha256(baseline.get("scores")),
        "reproduced_scores_sha256": canonical_sha256(reproduced.get("scores")),
        "passed": scores_match and all(metadata_matches.values()),
    }


def git(*args: str, cwd: Path = PROJECT_ROOT) -> str:
    completed = subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True)
    return completed.stdout.strip()


def run(*args: str, cwd: Path) -> None:
    subprocess.run(args, cwd=cwd, check=True)


def reproduce(worktree: Path, output_dir: Path) -> list[dict[str, Any]]:
    run("uv", "sync", "--frozen", "--extra", "dev", cwd=worktree)
    results = []
    for track_id, config in TRACKS.items():
        output_prefix = output_dir / config["output"]
        run(
            "uv",
            "run",
            "python",
            config["runner"],
            "--generated-date",
            GENERATED_DATE,
            "--output-prefix",
            str(output_prefix),
            cwd=worktree,
        )
        baseline_path = PROJECT_ROOT / config["report"]
        reproduced_path = output_prefix.with_suffix(".json")
        result = compare_track(track_id, load_json(baseline_path), load_json(reproduced_path))
        result["baseline_report_sha256"] = sha256_file(baseline_path)
        result["reproduced_report_sha256"] = sha256_file(reproduced_path)
        results.append(result)
    return results


def build_attestation(
    *,
    operator: str,
    organization: str | None,
    relationship: str,
    repository_url: str,
    tool_git_sha: str,
    source_git_sha: str,
    clean_worktree: bool,
    tracks: list[dict[str, Any]],
) -> dict[str, Any]:
    return {
        "version": 1,
        "kind": "zhtw-public-benchmark-reproduction",
        "status": "passed"
        if clean_worktree and all(item["passed"] for item in tracks)
        else "failed",
        "scope": "public_secondary_tracks_only",
        "operator": operator,
        "organization": organization,
        "relationship": relationship,
        "recorded_at": dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z"),
        "repository_url": repository_url,
        "tool_git_sha": tool_git_sha,
        "source_git_sha": source_git_sha,
        "source_worktree_clean": clean_worktree,
        "environment": {
            "platform": platform.platform(),
            "machine": platform.machine(),
            "python": platform.python_version(),
        },
        "tracks": tracks,
        "limits": [
            "This reproduces only the public UD GSD and NAER secondary tracks.",
            "It does not reproduce the private Blind-v2 primary endpoint.",
            "An attestation counts as independent evidence only when submitted by an "
            "outside person.",
        ],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--operator", required=True)
    parser.add_argument("--organization")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--independent", action="store_true")
    mode.add_argument("--local-smoke-test", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    relationship = "independent_third_party" if args.independent else "project_local_smoke_test"
    tool_git_sha = git("rev-parse", "HEAD")
    source_git_sha = git("rev-parse", SOURCE_GIT_SHA)
    if source_git_sha != SOURCE_GIT_SHA:
        raise ValueError("the frozen public-track source commit is unavailable")
    repository_url = git("remote", "get-url", "origin")

    with tempfile.TemporaryDirectory(prefix="zhtw-public-reproduction-") as temp:
        temp_root = Path(temp)
        worktree = temp_root / "source"
        output_dir = temp_root / "reports"
        output_dir.mkdir()
        git("worktree", "add", "--detach", str(worktree), SOURCE_GIT_SHA)
        try:
            tracks = reproduce(worktree, output_dir)
            clean_worktree = not bool(git("status", "--porcelain", cwd=worktree))
        finally:
            git("worktree", "remove", "--force", str(worktree))

    attestation = build_attestation(
        operator=args.operator,
        organization=args.organization,
        relationship=relationship,
        repository_url=repository_url,
        tool_git_sha=tool_git_sha,
        source_git_sha=source_git_sha,
        clean_worktree=clean_worktree,
        tracks=tracks,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(attestation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"public benchmark reproduction: {attestation['status']}")
    print(f"attestation: {args.output.resolve()}")
    return 0 if attestation["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
