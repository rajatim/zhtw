#!/usr/bin/env python3
"""Govern and build private Blind-v2 post-result audit artifacts."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from zhtw import convert  # noqa: E402

ACCURACY = PROJECT_ROOT / "benchmarks/accuracy"
INPUTS = ACCURACY / "blind-v2.inputs.json"
EXPECTED = ACCURACY / "blind-v2.expected.json"
SOURCE_REPORT = PROJECT_ROOT / "docs/reports/blind-v2-benchmark-2026-07-31.json"
PROTOCOL = ACCURACY / "blind-v2.post-result-audit-protocol-v1.json"
SCHEMA = ACCURACY / "blind-v2.post-result-audit-ledger-event.schema.json"
LEDGER = ACCURACY / "private/blind-v2.post-result-audit-ledger.jsonl"
PRIVATE_ROOT = ACCURACY / "private/post-result-audit-v1"
AUDIT_ID = "blind-v2-post-result-audit-1"
SOURCE_RUN_ID = "blind-v2-run-3-attempt-1"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON must be an object")
    return value


def json_text(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def base_event(event: str, *, exit_status: int | None, summary_hash: str | None) -> dict[str, Any]:
    report = load_json(SOURCE_REPORT)
    return {
        "version": 1,
        "dataset": "blind-v2",
        "audit_id": AUDIT_ID,
        "event": event,
        "recorded_at": now(),
        "operator": "tim",
        "reason": "Controlled post-result error taxonomy and severe-error audit",
        "source_run_id": SOURCE_RUN_ID,
        "source_report_sha256": sha256_file(SOURCE_REPORT),
        "inputs_sha256": sha256_file(INPUTS),
        "expected_sha256": sha256_file(EXPECTED),
        "zhtw_git_sha": report["provenance"]["git_sha"],
        "audit_protocol_sha256": sha256_file(PROTOCOL),
        "detailed_rows_read": True,
        "case_level_artifacts_private": True,
        "result_tuning_prohibited": True,
        "exit_status": exit_status,
        "findings_summary_sha256": summary_hash,
    }


def load_ledger() -> list[dict[str, Any]]:
    if not LEDGER.exists():
        return []
    return [json.loads(line) for line in LEDGER.read_text(encoding="utf-8").splitlines() if line]


def validate_event(event: dict[str, Any]) -> None:
    schema = load_json(SCHEMA)
    errors = sorted(
        Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(event),
        key=lambda item: list(item.path),
    )
    if errors:
        raise ValueError("; ".join(f"{error.json_path}: {error.message}" for error in errors))


def append_event(event: dict[str, Any]) -> None:
    validate_event(event)
    events = load_ledger()
    names = [item["event"] for item in events if item["audit_id"] == AUDIT_ID]
    if event["event"] == "audit_started" and names:
        raise ValueError("audit already started")
    if event["event"] != "audit_started":
        if names != ["audit_started"]:
            raise ValueError("audit completion requires one unfinished start event")
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with LEDGER.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")


def start_audit() -> None:
    append_event(base_event("audit_started", exit_status=None, summary_hash=None))
    print(f"audit started: {AUDIT_ID}")


def build_packets(batch_size: int) -> dict[str, Any]:
    if [item["event"] for item in load_ledger() if item["audit_id"] == AUDIT_ID] != [
        "audit_started"
    ]:
        raise ValueError("record audit_started before reading detailed rows")
    inputs = load_json(INPUTS)
    expected = load_json(EXPECTED)
    expected_by_id = {case["id"]: case for case in expected["cases"]}
    misses: list[dict[str, Any]] = []
    for case in inputs["cases"]:
        reference = expected_by_id[case["id"]]
        actual = convert(case["input"])
        accepted = [reference["expected"], *reference.get("acceptable", [])]
        if actual not in accepted:
            misses.append(
                {
                    "id": case["id"],
                    "domain": case["domain"],
                    "risk": case["risk"],
                    "input": case["input"],
                    "expected": reference["expected"],
                    "acceptable": reference.get("acceptable", []),
                    "actual": actual,
                }
            )
    PRIVATE_ROOT.mkdir(parents=True, exist_ok=True)
    batches = []
    for index, start in enumerate(range(0, len(misses), batch_size), start=1):
        path = PRIVATE_ROOT / f"packet-{index:03d}.json"
        packet = {
            "version": 1,
            "dataset": "blind-v2",
            "audit_id": AUDIT_ID,
            "batch": index,
            "cases": misses[start : start + batch_size],
        }
        path.write_text(json_text(packet), encoding="utf-8")
        batches.append({"batch": index, "cases": len(packet["cases"]), "sha256": sha256_file(path)})
    manifest = {
        "version": 1,
        "dataset": "blind-v2",
        "audit_id": AUDIT_ID,
        "total_cases": len(inputs["cases"]),
        "misses": len(misses),
        "batch_size": batch_size,
        "batches": batches,
        "by_domain": dict(sorted(Counter(item["domain"] for item in misses).items())),
        "by_risk": dict(sorted(Counter(item["risk"] for item in misses).items())),
    }
    (PRIVATE_ROOT / "manifest.json").write_text(json_text(manifest), encoding="utf-8")
    print(f"private audit packets: {len(misses)} misses in {len(batches)} batches")
    return manifest


def complete_audit(summary_path: Path) -> None:
    append_event(
        base_event(
            "audit_completed",
            exit_status=0,
            summary_hash=sha256_file(summary_path),
        )
    )
    print(f"audit completed: {AUDIT_ID}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("start")
    build = subparsers.add_parser("build-packets")
    build.add_argument("--batch-size", type=int, default=50)
    complete = subparsers.add_parser("complete")
    complete.add_argument("--summary", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "start":
        start_audit()
    elif args.command == "build-packets":
        build_packets(args.batch_size)
    else:
        complete_audit(args.summary.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
