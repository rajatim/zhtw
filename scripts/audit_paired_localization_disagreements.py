#!/usr/bin/env python3
"""Audit cases where OpenCC matches a public vendor reference and zhtw does not."""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import sys
import tempfile
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from scripts.competitor_benchmark import load_engines  # noqa: E402
from scripts.run_accuracy_benchmark import normalize_output  # noqa: E402
from scripts.run_blind_v2_post_result_review import (  # noqa: E402
    run_agy,
    run_codex,
    run_synthesis,
)

DEFAULT_ROOT = (
    PROJECT_ROOT
    / "benchmarks"
    / "accuracy"
    / "private"
    / "paired-localization-disagreement-audit-v1"
)
DEFAULT_LOCK = PROJECT_ROOT / "benchmarks" / "accuracy" / "competitors.lock.json"
TRACKS = {
    "aosp-framework-paired-ui-v1": 60,
    "firefox-paired-ui-v1": 40,
}
SEED = 20260731
DECISION_FIELDS = ("severity", "category", "expected_valid", "actual_acceptable")


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON must be an object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def deterministic_key(case_id: str) -> str:
    return hashlib.sha256(f"{SEED}:{case_id}".encode()).hexdigest()


def select_cases(
    *, lock_path: Path, container_image: str
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    lock = load_json(lock_path)
    engines = load_engines(
        ["zhtw", "opencc-s2twp"],
        lock=lock,
        container_image=container_image,
    )
    by_name = {engine.name: engine for engine in engines}
    if any(not by_name[name].available for name in ("zhtw", "opencc-s2twp")):
        raise ValueError("zhtw and locked OpenCC must both be available")

    selected: list[dict[str, Any]] = []
    candidate_counts: dict[str, int] = {}
    for track_id, quota in TRACKS.items():
        dataset_path = PROJECT_ROOT / "benchmarks" / "accuracy" / "external" / f"{track_id}.json"
        dataset = load_json(dataset_path)
        candidates: list[dict[str, Any]] = []
        for case in dataset["cases"]:
            expected = normalize_output(case["expected"])
            actual = normalize_output(by_name["zhtw"].convert(case["input"]))
            competitor = normalize_output(by_name["opencc-s2twp"].convert(case["input"]))
            if actual != expected and competitor == expected:
                candidates.append(
                    {
                        "id": case["id"],
                        "source_track": track_id,
                        "resource_key": case["resource_key"],
                        "input": case["input"],
                        "expected": expected,
                        "actual": actual,
                    }
                )
        candidate_counts[track_id] = len(candidates)
        if len(candidates) < quota:
            raise ValueError(f"{track_id}: only {len(candidates)} candidates for quota {quota}")
        selected.extend(sorted(candidates, key=lambda case: deterministic_key(case["id"]))[:quota])
    return selected, candidate_counts


def build_packets(*, root: Path, lock_path: Path, container_image: str) -> None:
    selected, candidate_counts = select_cases(lock_path=lock_path, container_image=container_image)
    selected = [
        {
            **case,
            "id": f"paired-audit-{index:04d}",
            "source_case_id": case["id"],
        }
        for index, case in enumerate(selected, start=1)
    ]
    for index, start in enumerate(range(0, len(selected), 25), start=1):
        write_json(
            root / f"packet-{index:03d}.json",
            {
                "version": 1,
                "audit_id": "paired-localization-disagreement-audit-v1",
                "batch": index,
                "selection": {
                    "seed": SEED,
                    "criterion": "opencc_exact_and_zhtw_not_exact",
                    "candidate_counts": candidate_counts,
                    "quotas": TRACKS,
                },
                "cases": selected[start : start + 25],
            },
        )
    print(f"private audit packet: {len(selected)} cases in 4 batches")
    print(f"candidate counts: {candidate_counts}")


def packet_paths(root: Path) -> list[Path]:
    paths = sorted(root.glob("packet-*.json"))
    if len(paths) != 4:
        raise ValueError("expected four private audit packets")
    return paths


def run_reviews(*, root: Path, reviewer: str, model: str, workers: int) -> None:
    output_dir = root / reviewer
    output_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=f"paired-audit-{reviewer}-") as temp:
        workdir = Path(temp)

        def run(path: Path) -> int:
            batch = int(path.stem.rsplit("-", 1)[1])
            output = output_dir / f"review-{batch:03d}.json"
            if output.is_file():
                return batch
            if reviewer == "codex":
                run_codex(path, output, workdir)
            else:
                last_error: ValueError | None = None
                for _ in range(3):
                    try:
                        run_agy(path, output, workdir, model)
                        break
                    except ValueError as exc:
                        last_error = exc
                else:
                    raise ValueError(
                        f"Agy review failed three times for batch {batch}"
                    ) from last_error
            return batch

        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(run, path) for path in packet_paths(root)]
            for future in concurrent.futures.as_completed(futures):
                print(f"{reviewer} review complete: batch {future.result():03d}", flush=True)


def build_synthesis_packets(root: Path) -> list[Path]:
    selected: list[dict[str, Any]] = []
    for packet_path in packet_paths(root):
        batch = int(packet_path.stem.rsplit("-", 1)[1])
        packet = load_json(packet_path)
        codex = load_json(root / "codex" / f"review-{batch:03d}.json")
        agy = load_json(root / "agy" / f"review-{batch:03d}.json")
        codex_by_id = {case["id"]: case for case in codex["cases"]}
        agy_by_id = {case["id"]: case for case in agy["cases"]}
        for case in packet["cases"]:
            first = codex_by_id[case["id"]]
            second = agy_by_id[case["id"]]
            if any(first[field] != second[field] for field in DECISION_FIELDS):
                selected.append({**case, "codex_review": first, "agy_review": second})

    output_dir = root / "synthesis-packets"
    paths: list[Path] = []
    for index, start in enumerate(range(0, len(selected), 25), start=1):
        path = output_dir / f"packet-{index:03d}.json"
        write_json(
            path,
            {
                "version": 1,
                "audit_id": "paired-localization-disagreement-audit-v1",
                "batch": index,
                "cases": selected[start : start + 25],
            },
        )
        paths.append(path)
    print(f"synthesis packets: {len(selected)} disagreements in {len(paths)} batches")
    return paths


def run_syntheses(*, root: Path, workers: int) -> None:
    paths = build_synthesis_packets(root)
    output_dir = root / "synthesis"
    output_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="paired-audit-synthesis-") as temp:
        workdir = Path(temp)

        def run(path: Path) -> int:
            batch = int(path.stem.rsplit("-", 1)[1])
            run_synthesis(path, output_dir / f"review-{batch:03d}.json", workdir)
            return batch

        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(run, path) for path in paths]
            for future in concurrent.futures.as_completed(futures):
                print(f"synthesis complete: batch {future.result():03d}", flush=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("sample", "review-codex", "review-agy", "synthesize"))
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--lock", type=Path, default=DEFAULT_LOCK)
    parser.add_argument("--container-image")
    parser.add_argument("--agy-model", default="gemini-3.1-pro-high")
    parser.add_argument("--workers", type=int, default=2)
    args = parser.parse_args()
    if args.command == "sample":
        if not args.container_image:
            parser.error("sample requires --container-image")
        build_packets(root=args.root, lock_path=args.lock, container_image=args.container_image)
    elif args.command == "review-codex":
        run_reviews(root=args.root, reviewer="codex", model=args.agy_model, workers=args.workers)
    elif args.command == "review-agy":
        run_reviews(root=args.root, reviewer="agy", model=args.agy_model, workers=args.workers)
    else:
        run_syntheses(root=args.root, workers=args.workers)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
