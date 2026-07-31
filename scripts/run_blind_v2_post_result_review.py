#!/usr/bin/env python3
"""Run independent private Codex or Agy review for Blind-v2 post-result packets."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import subprocess
import tempfile
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PRIVATE_ROOT = PROJECT_ROOT / "benchmarks/accuracy/private/post-result-audit-v1"
CATEGORIES = (
    "over_conversion",
    "under_conversion",
    "regional_wording",
    "wrong_character",
    "entity_or_identifier",
    "punctuation_or_format",
    "expected_problem",
    "acceptable_variant",
    "other",
)
SEVERITIES = ("P0", "P1", "P2", "P3", "none")
DECISION_FIELDS = ("severity", "category", "expected_valid", "actual_acceptable")


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON must be an object")
    return value


def response_schema(case_count: int) -> dict[str, Any]:
    return {
        "type": "object",
        "required": ["cases"],
        "additionalProperties": False,
        "properties": {
            "cases": {
                "type": "array",
                "minItems": case_count,
                "maxItems": case_count,
                "items": {
                    "type": "object",
                    "required": [
                        "id",
                        "severity",
                        "category",
                        "expected_valid",
                        "actual_acceptable",
                        "confidence",
                        "rationale",
                    ],
                    "additionalProperties": False,
                    "properties": {
                        "id": {"type": "string"},
                        "severity": {"type": "string", "enum": list(SEVERITIES)},
                        "category": {"type": "string", "enum": list(CATEGORIES)},
                        "expected_valid": {"type": "boolean"},
                        "actual_acceptable": {"type": "boolean"},
                        "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
                        "rationale": {"type": "string"},
                    },
                },
            }
        },
    }


def synthesis_schema(case_count: int) -> dict[str, Any]:
    schema = response_schema(case_count)
    properties = schema["properties"]["cases"]["items"]["properties"]
    required = schema["properties"]["cases"]["items"]["required"]
    properties["decision_source"] = {
        "type": "string",
        "enum": ["codex", "agy", "hybrid"],
    }
    properties["needs_maintainer"] = {"type": "boolean"}
    required.extend(["decision_source", "needs_maintainer"])
    return schema


def review_prompt(packet: dict[str, Any]) -> str:
    cases = json.dumps(packet["cases"], ensure_ascii=False, separators=(",", ":"))
    return f"""You are reviewing misses from a consumed Simplified Chinese to Taiwan
Traditional Chinese benchmark. Review every case independently. Do not use tools, files,
web search, converters, or another review. The published score is immutable.

Classify the actual output against the input and expected output:
- P0: materially dangerous meaning error in safety, medical, legal, financial, security,
  or identifier content.
- P1: clear semantic damage or seriously misleading wording without immediate P0 harm.
- P2: clear Taiwan localization, orthography, or terminology error, but understandable.
- P3: style, strict-reference, punctuation, or minor wording difference with no material
  meaning change.
- none: actual is acceptable, or expected needs correction.

Set expected_valid=false only when the expected output is genuinely wrong. Set
actual_acceptable=true when actual is a valid Taiwan Traditional Chinese rendering even if it
does not exactly match expected. Keep each rationale to one short sentence. Preserve the case
order and IDs. Return structured JSON only.

Cases:
{cases}
"""


def synthesis_prompt(packet: dict[str, Any]) -> str:
    cases = json.dumps(packet["cases"], ensure_ascii=False, separators=(",", ":"))
    return f"""You are the synthesis reviewer for a consumed Simplified Chinese to Taiwan
Traditional Chinese benchmark. Each case includes the source, expected, actual, Codex first
pass, and independent Agy review. Resolve the disagreement using the fixed severity meanings.
The published score is immutable. Do not use tools, files, web search, or converters.

Choose codex or agy when that review is fully correct; choose hybrid when you combine or correct
them. Set needs_maintainer=true only for a final P0/P1, an invalid expected value, an acceptable
actual that would change scoring, or genuinely unresolved low-confidence judgment. Keep the
rationale to one short sentence. Preserve IDs and return structured JSON only.

Cases:
{cases}
"""


def normalize_cases(packet: dict[str, Any], result: dict[str, Any]) -> list[dict[str, Any]]:
    expected_ids = [case["id"] for case in packet["cases"]]
    cases = result.get("cases", [])
    by_id = {case.get("id"): case for case in cases}
    if len(by_id) != len(cases) or set(by_id) != set(expected_ids):
        raise ValueError("review returned missing, extra, or duplicate IDs")
    return [by_id[case_id] for case_id in expected_ids]


def run_codex(packet_path: Path, output_path: Path, workdir: Path) -> None:
    packet = load_json(packet_path)
    schema_path = workdir / f"schema-{packet['batch']:03d}.json"
    raw_path = workdir / f"codex-{packet['batch']:03d}.json"
    schema_path.write_text(json.dumps(response_schema(len(packet["cases"]))), encoding="utf-8")
    subprocess.run(
        [
            "codex",
            "exec",
            "--ephemeral",
            "--ignore-rules",
            "--skip-git-repo-check",
            "--sandbox",
            "read-only",
            "--output-schema",
            str(schema_path),
            "--output-last-message",
            str(raw_path),
            review_prompt(packet),
        ],
        cwd=workdir,
        check=True,
        capture_output=True,
        text=True,
        timeout=1200,
    )
    result = load_json(raw_path)
    cases = normalize_cases(packet, result)
    output_path.write_text(
        json.dumps(
            {
                "version": 1,
                "audit_id": packet["audit_id"],
                "batch": packet["batch"],
                "stage": "codex_first_pass",
                "packet": packet_path.name,
                "cases": cases,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def run_agy(packet_path: Path, output_path: Path, workdir: Path, model: str) -> None:
    packet = load_json(packet_path)
    schema = response_schema(len(packet["cases"]))
    completed = subprocess.run(
        [
            "agy",
            "--model",
            model,
            "--effort",
            "high",
            "--sandbox",
            "--output-format",
            "json",
            "--json-schema",
            json.dumps(schema, separators=(",", ":")),
            "--print-timeout",
            "20m",
            "-p",
            review_prompt(packet),
        ],
        cwd=workdir,
        check=True,
        capture_output=True,
        text=True,
        timeout=1260,
    )
    envelope = json.loads(completed.stdout)
    if envelope.get("status") != "SUCCESS":
        raise ValueError(f"Agy failed: {envelope.get('status')}")
    result = envelope["structured_output"]
    cases = normalize_cases(packet, result)
    output_path.write_text(
        json.dumps(
            {
                "version": 1,
                "audit_id": packet["audit_id"],
                "batch": packet["batch"],
                "stage": "agy_independent",
                "model": model,
                "packet": packet_path.name,
                "conversation_id": envelope.get("conversation_id"),
                "cases": cases,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def build_synthesis_packets(batch_size: int = 50) -> list[Path]:
    packet_by_id: dict[str, dict[str, Any]] = {}
    codex_by_id: dict[str, dict[str, Any]] = {}
    agy_by_id: dict[str, dict[str, Any]] = {}
    for path in sorted(PRIVATE_ROOT.glob("packet-*.json")):
        for case in load_json(path)["cases"]:
            packet_by_id[case["id"]] = case
    for path in sorted((PRIVATE_ROOT / "codex").glob("review-*.json")):
        for case in load_json(path)["cases"]:
            codex_by_id[case["id"]] = case
    for path in sorted((PRIVATE_ROOT / "agy").glob("review-*.json")):
        for case in load_json(path)["cases"]:
            agy_by_id[case["id"]] = case
    if not (len(packet_by_id) == len(codex_by_id) == len(agy_by_id) == 1299):
        raise ValueError("synthesis requires complete packet, Codex, and Agy coverage")
    selected = []
    for case_id, case in packet_by_id.items():
        codex = codex_by_id[case_id]
        agy = agy_by_id[case_id]
        disagrees = any(codex[field] != agy[field] for field in DECISION_FIELDS)
        severe = bool({"P0", "P1"} & {codex["severity"], agy["severity"]})
        if disagrees or severe or not codex["expected_valid"] or not agy["expected_valid"]:
            selected.append({**case, "codex_review": codex, "agy_review": agy})
    output_dir = PRIVATE_ROOT / "synthesis-packets"
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    for index, start in enumerate(range(0, len(selected), batch_size), start=1):
        path = output_dir / f"packet-{index:03d}.json"
        path.write_text(
            json.dumps(
                {
                    "version": 1,
                    "audit_id": "blind-v2-post-result-audit-1",
                    "batch": index,
                    "cases": selected[start : start + batch_size],
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        paths.append(path)
    print(f"synthesis packets: {len(selected)} cases in {len(paths)} batches")
    return paths


def run_synthesis(packet_path: Path, output_path: Path, workdir: Path) -> None:
    packet = load_json(packet_path)
    schema_path = workdir / f"synthesis-schema-{packet['batch']:03d}.json"
    raw_path = workdir / f"synthesis-{packet['batch']:03d}.json"
    schema_path.write_text(json.dumps(synthesis_schema(len(packet["cases"]))), encoding="utf-8")
    subprocess.run(
        [
            "codex",
            "exec",
            "--ephemeral",
            "--ignore-rules",
            "--skip-git-repo-check",
            "--sandbox",
            "read-only",
            "--output-schema",
            str(schema_path),
            "--output-last-message",
            str(raw_path),
            synthesis_prompt(packet),
        ],
        cwd=workdir,
        check=True,
        capture_output=True,
        text=True,
        timeout=1200,
    )
    result = load_json(raw_path)
    cases = normalize_cases(packet, result)
    output_path.write_text(
        json.dumps(
            {
                "version": 1,
                "audit_id": packet["audit_id"],
                "batch": packet["batch"],
                "stage": "codex_synthesis",
                "packet": packet_path.name,
                "cases": cases,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reviewer", choices=("codex", "agy", "synthesis"), required=True)
    parser.add_argument("--batch-from", type=int, default=1)
    parser.add_argument("--batch-to", type=int, default=26)
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--agy-model", default="gemini-3.1-pro-high")
    args = parser.parse_args()
    if args.reviewer == "synthesis":
        all_paths = build_synthesis_packets()
        packet_paths = all_paths[args.batch_from - 1 : args.batch_to]
    else:
        packet_paths = [
            PRIVATE_ROOT / f"packet-{number:03d}.json"
            for number in range(args.batch_from, args.batch_to + 1)
        ]
    output_dir = PRIVATE_ROOT / args.reviewer
    output_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=f"blind-v2-{args.reviewer}-") as temp_dir:
        workdir = Path(temp_dir)

        def run(packet_path: Path) -> int:
            batch = int(packet_path.stem.split("-")[-1])
            output_path = output_dir / f"review-{batch:03d}.json"
            if output_path.exists():
                return batch
            if args.reviewer == "codex":
                run_codex(packet_path, output_path, workdir)
            elif args.reviewer == "agy":
                run_agy(packet_path, output_path, workdir, args.agy_model)
            else:
                run_synthesis(packet_path, output_path, workdir)
            return batch

        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {executor.submit(run, path): path for path in packet_paths}
            for future in concurrent.futures.as_completed(futures):
                batch = future.result()
                print(f"{args.reviewer} review complete: batch {batch:03d}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
