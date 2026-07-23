#!/usr/bin/env python3
"""Validate permissioned Blind-v2 user-report collections and sensitive-data gates."""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCHEMA = PROJECT_ROOT / "benchmarks/accuracy/blind-v2.permissioned-user-report-source.schema.json"
FORBIDDEN_KEYS = {"expected", "acceptable", "annotation", "output", "normalized_output"}
SENSITIVE_PATTERNS = (
    ("email", re.compile(r"(?<![\w.+-])[\w.+-]+@[\w-]+(?:\.[\w-]+)+", re.I)),
    ("private_key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("jwt", re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b")),
    ("github_token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b")),
    ("aws_access_key", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    (
        "secret_assignment",
        re.compile(
            r"(?i)\b(?:api[_ -]?key|access[_ -]?token|auth[_ -]?token|password|secret)"
            r"\s*[:=]\s*[^\s,;，；]{4,}"
        ),
    ),
    ("url_query_or_fragment", re.compile(r"https?://[^\s?#]+[?#][^\s]+", re.I)),
    (
        "ipv4_address",
        re.compile(
            r"(?<!\d)(?:25[0-5]|2[0-4]\d|1?\d?\d)" r"(?:\.(?:25[0-5]|2[0-4]\d|1?\d?\d)){3}(?!\d)"
        ),
    ),
    (
        "labelled_phone_number",
        re.compile(r"(?:电话|電話|手机|手機|联系电话|聯絡電話)\s*[:：]\s*\+?[\d() .-]{8,}\d"),
    ),
    (
        "labelled_personal_identifier",
        re.compile(
            r"(?:身份证|身分證|身份證|护照|護照|客户编号|客戶編號|账号|帳號)"
            r"\s*[:：]\s*[A-Za-z0-9-]{4,}"
        ),
    ),
    (
        "labelled_address",
        re.compile(r"(?:地址|住址)\s*[:：]\s*[^，。\n]{6,}"),
    ),
)


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON must be an object")
    return value


def normalize_input(text: str) -> str:
    return " ".join(unicodedata.normalize("NFC", text).split())


def forbidden_keys(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            if key in FORBIDDEN_KEYS:
                found.add(key)
            found.update(forbidden_keys(child))
    elif isinstance(value, list):
        for child in value:
            found.update(forbidden_keys(child))
    return found


def detect_sensitive_data(text: str) -> list[str]:
    return [name for name, pattern in SENSITIVE_PATTERNS if pattern.search(text)]


def validate_collection(source: dict[str, Any], *, require_ready: bool = False) -> list[str]:
    schema = load_json(SCHEMA)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = [
        f"{error.json_path}: {error.message}"
        for error in sorted(validator.iter_errors(source), key=lambda item: list(item.path))
    ]
    if errors:
        return errors

    if require_ready and source["status"] != "ready_for_import":
        errors.append("$.status: collection is not ready_for_import")

    expected_source_id = f"permissioned-user-report-batch-{source['batch_number']:03d}"
    if source["id"] != expected_source_id:
        errors.append(
            f"$.id: {source['id']!r} does not match batch_number {source['batch_number']}"
        )

    prohibited = forbidden_keys(source)
    if prohibited:
        errors.append(f"$: forbidden benchmark keys: {', '.join(sorted(prohibited))}")

    seen_ids: set[str] = set()
    seen_inputs: dict[str, str] = {}
    for index, case in enumerate(source["cases"]):
        case_id = case["id"]
        expected_case_id = f"report-{index + 1:04d}"
        if case_id != expected_case_id:
            errors.append(
                f"$.cases[{index}].id: expected contiguous id {expected_case_id}, got {case_id}"
            )
        if case_id in seen_ids:
            errors.append(f"$.cases[{index}].id: duplicate case id {case_id}")
        seen_ids.add(case_id)

        normalized = normalize_input(case["input"])
        if normalized in seen_inputs:
            errors.append(
                f"$.cases[{index}].input: duplicate normalized input with {seen_inputs[normalized]}"
            )
        else:
            seen_inputs[normalized] = case_id

        for finding in detect_sensitive_data(case["input"]):
            errors.append(f"$.cases[{index}].input: sensitive pattern detected: {finding}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--require-ready", action="store_true")
    args = parser.parse_args()

    source = load_json(args.source)
    errors = validate_collection(source, require_ready=args.require_ready)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(
        f"permissioned user reports valid: status={source['status']} "
        f"cases={len(source['cases'])}/{source['target_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
