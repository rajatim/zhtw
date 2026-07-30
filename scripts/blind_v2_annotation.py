#!/usr/bin/env python3
"""Build and validate private Blind-v2 expected-annotation artifacts."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ACCURACY_ROOT = PROJECT_ROOT / "benchmarks" / "accuracy"
PACKET_SCHEMA = ACCURACY_ROOT / "blind-v2.annotation-packet.schema.json"
ADVISORY_SCHEMA = ACCURACY_ROOT / "blind-v2.annotation-advisory.schema.json"
SYNTHESIS_SCHEMA = ACCURACY_ROOT / "blind-v2.annotation-synthesis.schema.json"
BATCH_DECISION_SCHEMA = ACCURACY_ROOT / "blind-v2.annotation-batch-decision.schema.json"
ANNOTATION_DECISIONS_SCHEMA = ACCURACY_ROOT / "blind-v2.annotation-decisions.schema.json"
EXPECTED_SCHEMA = ACCURACY_ROOT / "blind-v2.expected.schema.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def json_text(value: dict[str, Any]) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha256_value(value: dict[str, Any]) -> str:
    return hashlib.sha256(json_text(value).encode()).hexdigest()


def relative_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path.resolve())


def validate_schema(value: dict[str, Any], schema_path: Path) -> list[str]:
    schema = load_json(schema_path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [error.message for error in sorted(validator.iter_errors(value), key=str)]


def build_packet(
    inputs_path: Path,
    *,
    batch_number: int,
    offset: int,
    limit: int,
) -> dict[str, Any]:
    inputs = load_json(inputs_path)
    cases = inputs["cases"][offset : offset + limit]
    if len(cases) != limit:
        raise ValueError(f"requested {limit} cases at offset {offset}, found {len(cases)}")
    packet = {
        "version": 1,
        "dataset": "blind-v2",
        "batch_id": f"blind-v2-annotation-batch-{batch_number:03d}",
        "inputs_sha256": sha256_file(inputs_path),
        "selection": {
            "offset": offset,
            "limit": limit,
            "total_inputs": len(inputs["cases"]),
        },
        "policy": {
            "input_only": True,
            "converter_output_forbidden": True,
            "expected_text_private": True,
        },
        "cases": [
            {
                "id": case["id"],
                "input": case["input"],
                "domain": case["domain"],
                "risk": case["risk"],
            }
            for case in cases
        ],
    }
    errors = validate_schema(packet, PACKET_SCHEMA)
    if errors:
        raise ValueError("; ".join(errors))
    return packet


def validate_advisory(packet_path: Path, advisory_path: Path) -> list[str]:
    packet = load_json(packet_path)
    advisory = load_json(advisory_path)
    errors = validate_schema(advisory, ADVISORY_SCHEMA)
    if errors:
        return errors
    if advisory["batch_id"] != packet["batch_id"]:
        errors.append("advisory batch_id does not match packet")
    if advisory["packet_sha256"] != sha256_file(packet_path):
        errors.append("advisory packet_sha256 does not match packet")
    packet_ids = [case["id"] for case in packet["cases"]]
    advisory_ids = [case["id"] for case in advisory["cases"]]
    if len(advisory_ids) != len(set(advisory_ids)):
        errors.append("advisory contains duplicate case IDs")
    if advisory_ids != packet_ids:
        errors.append("advisory case IDs or ordering do not exactly match packet")
    return errors


def compare_advisories(
    packet_path: Path,
    codex_path: Path,
    agy_path: Path,
) -> dict[str, Any]:
    errors = validate_advisory(packet_path, codex_path)
    errors.extend(validate_advisory(packet_path, agy_path))
    if errors:
        raise ValueError("; ".join(errors))
    packet = load_json(packet_path)
    codex = load_json(codex_path)
    agy = load_json(agy_path)
    if codex["stage"] != "codex_first_pass":
        raise ValueError("Codex advisory has the wrong stage")
    if agy["stage"] != "agy_independent":
        raise ValueError("Agy advisory has the wrong stage")

    differences = []
    agreement = 0
    for source, codex_case, agy_case in zip(
        packet["cases"], codex["cases"], agy["cases"], strict=True
    ):
        same = (
            codex_case["expected"] == agy_case["expected"]
            and codex_case["acceptable"] == agy_case["acceptable"]
        )
        if same:
            agreement += 1
            continue
        differences.append(
            {
                "id": source["id"],
                "input": source["input"],
                "domain": source["domain"],
                "risk": source["risk"],
                "codex": codex_case,
                "agy": agy_case,
            }
        )
    return {
        "version": 1,
        "dataset": "blind-v2",
        "batch_id": packet["batch_id"],
        "packet_sha256": sha256_file(packet_path),
        "codex_advisory_sha256": sha256_file(codex_path),
        "agy_advisory_sha256": sha256_file(agy_path),
        "stats": {
            "total": len(packet["cases"]),
            "agreement": agreement,
            "differences": len(differences),
        },
        "differences": differences,
    }


def agy_response_schema(*, minimum_cases: int, maximum_cases: int) -> dict[str, Any]:
    return {
        "type": "object",
        "required": ["cases"],
        "additionalProperties": False,
        "properties": {
            "cases": {
                "type": "array",
                "minItems": minimum_cases,
                "maxItems": maximum_cases,
                "items": {
                    "type": "object",
                    "required": ["id", "expected", "acceptable", "confidence", "notes"],
                    "additionalProperties": False,
                    "properties": {
                        "id": {"type": "string"},
                        "expected": {"type": "string", "minLength": 1},
                        "acceptable": {
                            "type": "array",
                            "uniqueItems": True,
                            "items": {"type": "string", "minLength": 1},
                        },
                        "confidence": {
                            "type": "string",
                            "enum": ["high", "medium", "low"],
                        },
                        "notes": {"type": "string"},
                    },
                },
            }
        },
    }


def agy_prompt(cases: list[dict[str, Any]]) -> str:
    payload = json.dumps(cases, ensure_ascii=False, indent=2)
    return f"""You are the independent language reviewer for a sealed benchmark.

For every input below, write the expected output in natural Taiwan Traditional Chinese.
Work from the input only. Do not use tools, converters, repository files, web search, or any
other review. Preserve meaning, entities, numbers, punctuation, spacing, placeholders, code,
and identifiers unless Taiwan wording requires a direct change. Prefer conservative conversion
when context is unclear. Add an acceptable variant only when it is genuinely equally correct.
Use high, medium, or low confidence. Keep notes short. Return structured JSON only, in the same
case order, with exactly these IDs.

Cases:
{payload}
"""


def run_agy_review(
    packet_path: Path,
    *,
    output_path: Path,
    review_date: str,
    model: str,
    chunk_size: int,
) -> dict[str, Any]:
    if not 1 <= chunk_size <= 25:
        raise ValueError("Agy chunk size must be between 1 and 25")
    packet = load_json(packet_path)
    version_result = subprocess.run(
        ["agy", "--version"],
        check=True,
        capture_output=True,
        text=True,
    )
    cli_version = version_result.stdout.strip()
    reviewed_cases: list[dict[str, Any]] = []
    conversation_ids: list[str] = []
    statuses: list[str] = []
    turns: list[int] = []

    with tempfile.TemporaryDirectory(prefix="blind-v2-agy-") as temp_dir:
        for start in range(0, len(packet["cases"]), chunk_size):
            chunk = packet["cases"][start : start + chunk_size]
            schema = agy_response_schema(
                minimum_cases=len(chunk),
                maximum_cases=len(chunk),
            )
            result = subprocess.run(
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
                    "10m",
                    "-p",
                    agy_prompt(chunk),
                ],
                cwd=temp_dir,
                check=True,
                capture_output=True,
                text=True,
                timeout=660,
            )
            envelope = json.loads(result.stdout)
            if envelope.get("status") != "SUCCESS":
                raise ValueError(f"Agy chunk at offset {start} failed: {envelope.get('status')}")
            structured = envelope.get("structured_output")
            if not isinstance(structured, dict) or not isinstance(structured.get("cases"), list):
                raise ValueError(f"Agy chunk at offset {start} has no structured cases")
            expected_ids = [case["id"] for case in chunk]
            actual_ids = [case.get("id") for case in structured["cases"]]
            if actual_ids != expected_ids:
                raise ValueError(f"Agy chunk at offset {start} returned wrong IDs or ordering")
            reviewed_cases.extend(structured["cases"])
            conversation_ids.append(str(envelope["conversation_id"]))
            statuses.append(str(envelope["status"]))
            turns.append(int(envelope["num_turns"]))

    advisory = {
        "version": 1,
        "dataset": "blind-v2",
        "batch_id": packet["batch_id"],
        "stage": "agy_independent",
        "reviewer": "Agy",
        "model": model,
        "review_date": review_date,
        "packet_sha256": sha256_file(packet_path),
        "execution": {
            "cli": "agy",
            "cli_version": cli_version,
            "conversation_ids": conversation_ids,
            "chunk_size": chunk_size,
            "statuses": statuses,
            "turns": turns,
        },
        "policy": {
            "input_only": True,
            "converter_output_not_used": True,
            "other_advisory_not_seen": True,
        },
        "cases": reviewed_cases,
    }
    errors = validate_schema(advisory, ADVISORY_SCHEMA)
    if errors:
        raise ValueError("; ".join(errors))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json_text(advisory), encoding="utf-8")
    return advisory


def build_synthesis(
    packet_path: Path,
    codex_path: Path,
    agy_path: Path,
    choices_path: Path,
) -> dict[str, Any]:
    errors = validate_advisory(packet_path, codex_path)
    errors.extend(validate_advisory(packet_path, agy_path))
    if errors:
        raise ValueError("; ".join(errors))
    packet = load_json(packet_path)
    codex = load_json(codex_path)
    agy = load_json(agy_path)
    choices = load_json(choices_path)
    choice_by_id = {choice["id"]: choice for choice in choices["choices"]}
    if len(choice_by_id) != len(choices["choices"]):
        raise ValueError("synthesis choices contain duplicate IDs")

    cases: list[dict[str, Any]] = []
    counts = {"agreement": 0, "codex": 0, "agy": 0, "hybrid": 0}
    for packet_case, codex_case, agy_case in zip(
        packet["cases"], codex["cases"], agy["cases"], strict=True
    ):
        case_id = packet_case["id"]
        if codex_case["expected"] == agy_case["expected"]:
            choice = choice_by_id.pop(case_id, None)
            if choice is None:
                common_acceptable = [
                    value for value in codex_case["acceptable"] if value in agy_case["acceptable"]
                ]
                value = {
                    "id": case_id,
                    "expected": codex_case["expected"],
                    "acceptable": common_acceptable,
                    "decision": "agreement",
                    "confidence": min(
                        codex_case["confidence"],
                        agy_case["confidence"],
                        key=("low", "medium", "high").index,
                    ),
                    "needs_maintainer_review": False,
                    "rationale": "Codex and Agy primary outputs agree.",
                }
            else:
                if choice["decision"] != "hybrid":
                    raise ValueError(
                        f"agreeing case {case_id} audit override requires hybrid decision"
                    )
                expected = choice.get("expected", "")
                if not expected or expected == codex_case["expected"]:
                    raise ValueError(
                        f"agreeing case {case_id} audit override requires a corrected expected"
                    )
                value = {
                    "id": case_id,
                    "expected": expected,
                    "acceptable": choice.get("acceptable", []),
                    "decision": "hybrid",
                    "confidence": choice["confidence"],
                    "needs_maintainer_review": choice["needs_maintainer_review"],
                    "rationale": choice["rationale"],
                }
        else:
            if case_id not in choice_by_id:
                raise ValueError(f"missing synthesis choice for differing case {case_id}")
            choice = choice_by_id.pop(case_id)
            decision = choice["decision"]
            if decision == "codex":
                expected = codex_case["expected"]
            elif decision == "agy":
                expected = agy_case["expected"]
            elif decision == "hybrid":
                expected = choice.get("expected", "")
                if not expected:
                    raise ValueError(f"hybrid choice for {case_id} requires expected")
            else:
                raise ValueError(f"invalid synthesis decision for {case_id}: {decision}")
            value = {
                "id": case_id,
                "expected": expected,
                "acceptable": choice.get("acceptable", []),
                "decision": decision,
                "confidence": choice["confidence"],
                "needs_maintainer_review": choice["needs_maintainer_review"],
                "rationale": choice["rationale"],
            }
        counts[value["decision"]] += 1
        cases.append(value)
    if choice_by_id:
        raise ValueError(f"unknown synthesis choice IDs: {sorted(choice_by_id)}")

    synthesis = {
        "version": 1,
        "dataset": "blind-v2",
        "batch_id": packet["batch_id"],
        "stage": "codex_synthesis",
        "packet_sha256": sha256_file(packet_path),
        "codex_advisory_sha256": sha256_file(codex_path),
        "agy_advisory_sha256": sha256_file(agy_path),
        "stats": {
            "total": len(cases),
            **counts,
            "needs_maintainer_review": sum(case["needs_maintainer_review"] for case in cases),
        },
        "cases": cases,
    }
    errors = validate_schema(synthesis, SYNTHESIS_SCHEMA)
    if errors:
        raise ValueError("; ".join(errors))
    return synthesis


def build_confirmation_artifacts(
    inputs_path: Path,
    packet_path: Path,
    synthesis_path: Path,
    *,
    progress_path: Path,
    expected_path: Path,
    batch_decision_path: Path,
    maintainer: str,
    decision_date: str,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    inputs = load_json(inputs_path)
    packet = load_json(packet_path)
    synthesis = load_json(synthesis_path)
    synthesis_errors = validate_schema(synthesis, SYNTHESIS_SCHEMA)
    if synthesis_errors:
        raise ValueError("; ".join(synthesis_errors))
    if packet["inputs_sha256"] != sha256_file(inputs_path):
        raise ValueError("packet inputs_sha256 does not match inputs")
    if synthesis["packet_sha256"] != sha256_file(packet_path):
        raise ValueError("synthesis packet_sha256 does not match packet")
    packet_ids = [case["id"] for case in packet["cases"]]
    synthesis_ids = [case["id"] for case in synthesis["cases"]]
    if synthesis_ids != packet_ids:
        raise ValueError("synthesis IDs or ordering do not match packet")

    batch_decision = {
        "version": 1,
        "dataset": "blind-v2",
        "batch_id": packet["batch_id"],
        "status": "human_confirmed",
        "inputs_sha256": sha256_file(inputs_path),
        "packet_sha256": sha256_file(packet_path),
        "synthesis_sha256": sha256_file(synthesis_path),
        "approval_policy": "single_human_with_ai_advisory",
        "decision_method": "batch_human_confirmation",
        "maintainer": maintainer,
        "decision_date": decision_date,
        "case_ids": packet_ids,
        "summary": (
            f"Maintainer confirmed the complete {len(packet_ids)}-case Codex synthesis "
            "after independent Agy advisory review."
        ),
    }
    errors = validate_schema(batch_decision, BATCH_DECISION_SCHEMA)
    if errors:
        raise ValueError("; ".join(errors))
    batch_decision_sha256 = sha256_value(batch_decision)

    if progress_path.is_file():
        progress = load_json(progress_path)
        errors = validate_schema(progress, ANNOTATION_DECISIONS_SCHEMA)
        if errors:
            raise ValueError("; ".join(errors))
        if progress["inputs_sha256"] != sha256_file(inputs_path):
            raise ValueError("annotation progress inputs_sha256 does not match inputs")
    else:
        progress = {
            "version": 1,
            "dataset": "blind-v2",
            "inputs_sha256": sha256_file(inputs_path),
            "approval_policy": "single_human_with_ai_advisory",
            "total_reviewed": 0,
            "batches": [],
        }
    reviewed_ids = {case_id for batch in progress["batches"] for case_id in batch["case_ids"]}
    if any(batch["id"] == packet["batch_id"] for batch in progress["batches"]):
        raise ValueError(f"annotation batch already confirmed: {packet['batch_id']}")
    overlap = reviewed_ids.intersection(packet_ids)
    if overlap:
        raise ValueError(f"annotation cases already confirmed: {sorted(overlap)}")
    progress["batches"].append(
        {
            "id": packet["batch_id"],
            "decision_artifact": relative_path(batch_decision_path),
            "decision_artifact_sha256": batch_decision_sha256,
            "case_count": len(packet_ids),
            "case_ids": packet_ids,
        }
    )
    progress["total_reviewed"] = sum(batch["case_count"] for batch in progress["batches"])
    errors = validate_schema(progress, ANNOTATION_DECISIONS_SCHEMA)
    if errors:
        raise ValueError("; ".join(errors))
    progress_sha256 = sha256_value(progress)

    if expected_path.is_file():
        expected = load_json(expected_path)
        errors = validate_schema(expected, EXPECTED_SCHEMA)
        if errors:
            raise ValueError("; ".join(errors))
        if expected["source_inputs_sha256"] != sha256_file(inputs_path):
            raise ValueError("private expected source_inputs_sha256 does not match inputs")
    else:
        expected = {
            "version": 1,
            "name": "blind-v2.expected",
            "dataset": "blind-v2",
            "status": "annotating",
            "source_inputs_sha256": sha256_file(inputs_path),
            "decision_summary_sha256": progress_sha256,
            "approval_policy": "single_human_with_ai_advisory",
            "cases": [],
        }
    expected_ids = {case["id"] for case in expected["cases"]}
    overlap = expected_ids.intersection(packet_ids)
    if overlap:
        raise ValueError(f"private expected cases already exist: {sorted(overlap)}")
    expected["cases"].extend(
        {
            "id": case["id"],
            "expected": case["expected"],
            "acceptable": case["acceptable"],
            "decision_method": "batch_human_confirmation",
            "decision_artifact_sha256": batch_decision_sha256,
        }
        for case in synthesis["cases"]
    )
    input_order = {case["id"]: index for index, case in enumerate(inputs["cases"])}
    expected["cases"].sort(key=lambda case: input_order[case["id"]])
    expected["decision_summary_sha256"] = progress_sha256
    expected["status"] = (
        "sealed_private" if len(expected["cases"]) == len(inputs["cases"]) else "annotating"
    )
    errors = validate_schema(expected, EXPECTED_SCHEMA)
    if errors:
        raise ValueError("; ".join(errors))
    return batch_decision, progress, expected


def validate_confirmation(
    inputs_path: Path,
    progress_path: Path,
    expected_path: Path,
) -> list[str]:
    inputs = load_json(inputs_path)
    progress = load_json(progress_path)
    expected = load_json(expected_path)
    errors = validate_schema(progress, ANNOTATION_DECISIONS_SCHEMA)
    errors.extend(validate_schema(expected, EXPECTED_SCHEMA))
    if errors:
        return errors
    inputs_sha256 = sha256_file(inputs_path)
    if progress["inputs_sha256"] != inputs_sha256:
        errors.append("annotation progress inputs_sha256 does not match inputs")
    if expected["source_inputs_sha256"] != inputs_sha256:
        errors.append("private expected source_inputs_sha256 does not match inputs")
    if expected["decision_summary_sha256"] != sha256_file(progress_path):
        errors.append("private expected decision_summary_sha256 does not match progress")

    input_ids = [case["id"] for case in inputs["cases"]]
    input_id_set = set(input_ids)
    reviewed_ids: list[str] = []
    artifact_by_id: dict[str, str] = {}
    for batch in progress["batches"]:
        artifact_path = PROJECT_ROOT / batch["decision_artifact"]
        if not artifact_path.is_file():
            errors.append(f"missing annotation decision artifact: {batch['decision_artifact']}")
            continue
        if sha256_file(artifact_path) != batch["decision_artifact_sha256"]:
            errors.append(f"annotation decision artifact hash mismatch: {batch['id']}")
            continue
        decision = load_json(artifact_path)
        errors.extend(
            f"{batch['id']}: {error}" for error in validate_schema(decision, BATCH_DECISION_SCHEMA)
        )
        if decision.get("case_ids") != batch["case_ids"]:
            errors.append(f"annotation decision case IDs do not match progress: {batch['id']}")
        if decision.get("batch_id") != batch["id"]:
            errors.append(f"annotation decision batch ID does not match progress: {batch['id']}")
        reviewed_ids.extend(batch["case_ids"])
        artifact_by_id.update(dict.fromkeys(batch["case_ids"], batch["decision_artifact_sha256"]))
    if len(reviewed_ids) != len(set(reviewed_ids)):
        errors.append("annotation progress contains duplicate case IDs")
    if not set(reviewed_ids).issubset(input_id_set):
        errors.append("annotation progress contains IDs outside frozen inputs")
    if progress["total_reviewed"] != len(reviewed_ids):
        errors.append("annotation progress total_reviewed does not match case coverage")

    expected_ids = [case["id"] for case in expected["cases"]]
    if expected_ids != [case_id for case_id in input_ids if case_id in set(reviewed_ids)]:
        errors.append("private expected IDs do not match reviewed inputs in frozen order")
    for case in expected["cases"]:
        if case["decision_artifact_sha256"] != artifact_by_id.get(case["id"]):
            errors.append(f"private expected decision link mismatch: {case['id']}")
    required_status = "sealed_private" if len(expected_ids) == len(input_ids) else "annotating"
    if expected["status"] != required_status:
        errors.append(f"private expected status must be {required_status}")
    return errors


def write_or_check(path: Path, value: dict[str, Any], *, check: bool) -> list[str]:
    content = json_text(value)
    if check:
        if not path.is_file() or path.read_text(encoding="utf-8") != content:
            return [f"{path} is stale"]
        return []
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    packet_parser = subparsers.add_parser("packet")
    packet_parser.add_argument("--inputs", type=Path, required=True)
    packet_parser.add_argument("--batch-number", type=int, required=True)
    packet_parser.add_argument("--offset", type=int, required=True)
    packet_parser.add_argument("--limit", type=int, default=100)
    packet_parser.add_argument("--output", type=Path, required=True)
    packet_parser.add_argument("--check", action="store_true")

    validate_parser = subparsers.add_parser("validate-advisory")
    validate_parser.add_argument("--packet", type=Path, required=True)
    validate_parser.add_argument("--advisory", type=Path, required=True)

    compare_parser = subparsers.add_parser("compare")
    compare_parser.add_argument("--packet", type=Path, required=True)
    compare_parser.add_argument("--codex", type=Path, required=True)
    compare_parser.add_argument("--agy", type=Path, required=True)
    compare_parser.add_argument("--output", type=Path, required=True)
    compare_parser.add_argument("--check", action="store_true")

    agy_parser = subparsers.add_parser("run-agy")
    agy_parser.add_argument("--packet", type=Path, required=True)
    agy_parser.add_argument("--output", type=Path, required=True)
    agy_parser.add_argument("--review-date", required=True)
    agy_parser.add_argument("--model", default="gemini-3.1-pro-high")
    agy_parser.add_argument("--chunk-size", type=int, default=20)

    synthesis_parser = subparsers.add_parser("synthesize")
    synthesis_parser.add_argument("--packet", type=Path, required=True)
    synthesis_parser.add_argument("--codex", type=Path, required=True)
    synthesis_parser.add_argument("--agy", type=Path, required=True)
    synthesis_parser.add_argument("--choices", type=Path, required=True)
    synthesis_parser.add_argument("--output", type=Path, required=True)
    synthesis_parser.add_argument("--check", action="store_true")

    confirm_parser = subparsers.add_parser("confirm-batch")
    confirm_parser.add_argument("--inputs", type=Path, required=True)
    confirm_parser.add_argument("--packet", type=Path, required=True)
    confirm_parser.add_argument("--synthesis", type=Path, required=True)
    confirm_parser.add_argument("--progress", type=Path, required=True)
    confirm_parser.add_argument("--expected", type=Path, required=True)
    confirm_parser.add_argument("--batch-decision", type=Path, required=True)
    confirm_parser.add_argument("--maintainer", required=True)
    confirm_parser.add_argument("--decision-date", required=True)

    confirmation_parser = subparsers.add_parser("validate-confirmation")
    confirmation_parser.add_argument("--inputs", type=Path, required=True)
    confirmation_parser.add_argument("--progress", type=Path, required=True)
    confirmation_parser.add_argument("--expected", type=Path, required=True)

    args = parser.parse_args()
    errors: list[str] = []
    try:
        if args.command == "packet":
            value = build_packet(
                args.inputs.resolve(),
                batch_number=args.batch_number,
                offset=args.offset,
                limit=args.limit,
            )
            errors = write_or_check(args.output, value, check=args.check)
        elif args.command == "validate-advisory":
            errors = validate_advisory(args.packet.resolve(), args.advisory.resolve())
        elif args.command == "compare":
            value = compare_advisories(
                args.packet.resolve(), args.codex.resolve(), args.agy.resolve()
            )
            errors = write_or_check(args.output, value, check=args.check)
        elif args.command == "run-agy":
            run_agy_review(
                args.packet.resolve(),
                output_path=args.output,
                review_date=args.review_date,
                model=args.model,
                chunk_size=args.chunk_size,
            )
        elif args.command == "synthesize":
            value = build_synthesis(
                args.packet.resolve(),
                args.codex.resolve(),
                args.agy.resolve(),
                args.choices.resolve(),
            )
            errors = write_or_check(args.output, value, check=args.check)
        elif args.command == "confirm-batch":
            batch_decision, progress, expected = build_confirmation_artifacts(
                args.inputs.resolve(),
                args.packet.resolve(),
                args.synthesis.resolve(),
                progress_path=args.progress.resolve(),
                expected_path=args.expected.resolve(),
                batch_decision_path=args.batch_decision.resolve(),
                maintainer=args.maintainer,
                decision_date=args.decision_date,
            )
            args.batch_decision.parent.mkdir(parents=True, exist_ok=True)
            args.batch_decision.write_text(json_text(batch_decision), encoding="utf-8")
            args.progress.parent.mkdir(parents=True, exist_ok=True)
            args.progress.write_text(json_text(progress), encoding="utf-8")
            args.expected.parent.mkdir(parents=True, exist_ok=True)
            args.expected.write_text(json_text(expected), encoding="utf-8")
        else:
            errors = validate_confirmation(
                args.inputs.resolve(),
                args.progress.resolve(),
                args.expected.resolve(),
            )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        errors = [str(exc)]

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Blind-v2 annotation {args.command} passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
