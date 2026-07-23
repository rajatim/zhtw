#!/usr/bin/env python3
# zhtw:disable  # GitHub 表單標題與提交內容含簡體 input
"""Preview or import permissioned user-report GitHub issues into Blind-v2."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.validate_permissioned_user_reports import (  # noqa: E402
    detect_sensitive_data,
    load_json,
    normalize_input,
    validate_collection,
)

DEFAULT_COLLECTION = (
    PROJECT_ROOT / "benchmarks/accuracy/sources/permissioned-user-report-batch-001.json"
)
DEFAULT_REPOSITORY = "rajatim/zhtw"
INPUT_HEADING = "簡體中文原句"
CONTEXT_HEADING = "非敏感情境說明"
CONSENT_HEADING = "權利、公開與資料安全確認"
ALLOWED_HEADINGS = {INPUT_HEADING, CONTEXT_HEADING, CONSENT_HEADING}
CONSENT_MARKERS = {
    "rights_confirmed": "文字原作者或有權提供",
    "cc0_applied": "CC0 1.0 Universal",
    "public_redistribution_confirmed": "文字、GitHub 帳號、issue",
    "no_sensitive_data_confirmed": "內容不含個資",
    "input_only_confirmed": "只提交 input",
}
ISSUE_URL_PATTERN = re.compile(
    r"^https://github\.com/(?P<repository>[^/]+/[^/]+)/issues/(?P<number>[0-9]+)$"
)
CHECKBOX_PATTERN = re.compile(r"^- \[(?P<checked>[ xX])\] (?P<label>.+)$")


class IntakeError(ValueError):
    """Raised when a user-report issue fails a fail-closed intake gate."""


def fetch_issue(repository: str, number: int) -> dict[str, Any]:
    result = subprocess.run(
        ["gh", "api", f"repos/{repository}/issues/{number}"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        detail = result.stderr.strip() or "unknown gh api error"
        raise IntakeError(f"issue #{number}: GitHub fetch failed: {detail}")
    value = json.loads(result.stdout)
    if not isinstance(value, dict):
        raise IntakeError(f"issue #{number}: GitHub response must be an object")
    return value


def load_issue(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise IntakeError(f"{path}: issue JSON must be an object")
    return value


def parse_sections(body: str) -> dict[str, str]:
    matches = list(re.finditer(r"^###\s+(.+?)\s*$", body, re.MULTILINE))
    if not matches:
        raise IntakeError("issue body does not contain GitHub issue-form sections")

    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        heading = match.group(1)
        if heading in sections:
            raise IntakeError(f"duplicate issue section: {heading}")
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        sections[heading] = body[start:end].strip()

    unexpected = set(sections) - ALLOWED_HEADINGS
    missing = {INPUT_HEADING, CONSENT_HEADING} - set(sections)
    if unexpected:
        raise IntakeError(f"unexpected issue sections: {', '.join(sorted(unexpected))}")
    if missing:
        raise IntakeError(f"missing issue sections: {', '.join(sorted(missing))}")
    return sections


def parse_consent(section: str) -> None:
    checkboxes = []
    for line in section.splitlines():
        match = CHECKBOX_PATTERN.fullmatch(line.strip())
        if match:
            checkboxes.append((match.group("checked").lower() == "x", match.group("label")))

    for marker in CONSENT_MARKERS.values():
        matching = [checked for checked, label in checkboxes if marker in label]
        if len(matching) != 1:
            raise IntakeError(f"consent item missing or duplicated: {marker}")
        if not matching[0]:
            raise IntakeError(f"consent item is not checked: {marker}")

    if len(checkboxes) != len(CONSENT_MARKERS):
        raise IntakeError("consent section contains an unexpected checkbox")


def parse_inputs(section: str) -> list[str]:
    inputs = [line.strip() for line in section.splitlines() if line.strip()]
    if not 1 <= len(inputs) <= 10:
        raise IntakeError(
            f"each issue must contain 1-10 non-empty input lines, found {len(inputs)}"
        )
    for index, text in enumerate(inputs, 1):
        if text.startswith(("#", "- ", "* ", ">", "```")):
            raise IntakeError(f"input line {index} contains Markdown structure")
        findings = detect_sensitive_data(text)
        if findings:
            raise IntakeError(
                f"input line {index} contains sensitive patterns: {', '.join(findings)}"
            )
    return inputs


def parse_issue(issue: dict[str, Any], *, repository: str) -> dict[str, Any]:
    required = ("number", "title", "body", "created_at", "html_url")
    missing = [field for field in required if not issue.get(field)]
    if missing:
        raise IntakeError(f"issue is missing fields: {', '.join(missing)}")
    if "pull_request" in issue:
        raise IntakeError("pull requests cannot be imported as user reports")
    if not str(issue["title"]).startswith("[語料回報]"):
        raise IntakeError("issue title does not identify the permissioned report form")

    url_match = ISSUE_URL_PATTERN.fullmatch(str(issue["html_url"]))
    if not url_match:
        raise IntakeError("issue html_url is not a canonical public GitHub issue URL")
    if url_match.group("repository").lower() != repository.lower():
        raise IntakeError("issue repository does not match the requested repository")
    if int(url_match.group("number")) != int(issue["number"]):
        raise IntakeError("issue number does not match html_url")

    body = str(issue["body"])
    sections = parse_sections(body)
    parse_consent(sections[CONSENT_HEADING])
    return {
        "number": int(issue["number"]),
        "issue_url": str(issue["html_url"]),
        "submitted_at": str(issue["created_at"]),
        "issue_body_sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
        "inputs": parse_inputs(sections[INPUT_HEADING]),
    }


def prepare_imports(
    collection: dict[str, Any], issues: list[dict[str, Any]], *, repository: str
) -> list[dict[str, Any]]:
    current_errors = validate_collection(collection)
    if current_errors:
        raise IntakeError("collection is invalid: " + "; ".join(current_errors))
    if collection["status"] != "collecting":
        raise IntakeError("collection must remain collecting while issues are appended")

    parsed = sorted(
        (parse_issue(issue, repository=repository) for issue in issues),
        key=lambda item: item["number"],
    )
    numbers = [item["number"] for item in parsed]
    if len(numbers) != len(set(numbers)):
        raise IntakeError("the same issue was supplied more than once")

    existing_inputs = {normalize_input(case["input"]): case["id"] for case in collection["cases"]}
    proposed_inputs: dict[str, str] = {}
    proposals: list[dict[str, Any]] = []
    for item in parsed:
        for text in item["inputs"]:
            normalized = normalize_input(text)
            if normalized in existing_inputs:
                raise IntakeError(
                    f"duplicate normalized input already stored as {existing_inputs[normalized]}"
                )
            if normalized in proposed_inputs:
                raise IntakeError(
                    f"duplicate normalized input proposed by {proposed_inputs[normalized]}"
                )
            proposed_inputs[normalized] = item["issue_url"]
            proposals.append({**item, "input": text})

    available = collection["target_count"] - len(collection["cases"])
    if len(proposals) > available:
        raise IntakeError(
            f"proposed {len(proposals)} inputs but collection has only {available} slots"
        )
    return proposals


def append_confirmed(
    collection: dict[str, Any],
    proposals: list[dict[str, Any]],
    *,
    maintainer: str,
    reviewed_at: str,
) -> dict[str, Any]:
    if not proposals:
        raise IntakeError("at least one proposed input is required")
    try:
        parsed_time = datetime.fromisoformat(reviewed_at.replace("Z", "+00:00"))
    except ValueError as exc:
        raise IntakeError("reviewed_at must be an ISO 8601 date-time") from exc
    if parsed_time.tzinfo is None:
        raise IntakeError("reviewed_at must include a UTC offset")
    if not maintainer.strip():
        raise IntakeError("maintainer must not be empty")

    updated = copy.deepcopy(collection)
    next_index = len(updated["cases"]) + 1
    for offset, proposal in enumerate(proposals):
        updated["cases"].append(
            {
                "id": f"report-{next_index + offset:04d}",
                "input": proposal["input"],
                "submitted_at": proposal["submitted_at"],
                "issue_url": proposal["issue_url"],
                "consent": {
                    "policy_version": collection["consent_policy_version"],
                    "cc0_applied": True,
                    "rights_confirmed": True,
                    "public_redistribution_confirmed": True,
                    "no_sensitive_data_confirmed": True,
                },
                "intake_review": {
                    "reviewer": maintainer.strip(),
                    "reviewed_at": reviewed_at,
                    "decision": "accepted",
                    "issue_body_sha256": proposal["issue_body_sha256"],
                },
            }
        )

    errors = validate_collection(updated)
    if errors:
        raise IntakeError("updated collection is invalid: " + "; ".join(errors))
    return updated


def write_collection(path: Path, collection: dict[str, Any]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(collection, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def render_preview(collection: dict[str, Any], proposals: list[dict[str, Any]]) -> str:
    first_index = len(collection["cases"]) + 1
    lines = [
        "permissioned user-report import preview",
        f"current={len(collection['cases'])}/{collection['target_count']}",
        f"proposed={len(proposals)}",
        f"result={len(collection['cases']) + len(proposals)}/{collection['target_count']}",
    ]
    for offset, proposal in enumerate(proposals):
        lines.append(
            f"report-{first_index + offset:04d}\t{proposal['issue_url']}\t{proposal['input']}"
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--collection", type=Path, default=DEFAULT_COLLECTION)
    parser.add_argument("--repo", default=DEFAULT_REPOSITORY)
    parser.add_argument("--issue", type=int, action="append", default=[])
    parser.add_argument("--issue-json", type=Path, action="append", default=[])
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--maintainer")
    parser.add_argument("--reviewed-at")
    args = parser.parse_args()

    if not args.issue and not args.issue_json:
        parser.error("at least one --issue or --issue-json is required")
    if args.write and (not args.maintainer or not args.reviewed_at):
        parser.error("--write requires --maintainer and --reviewed-at")

    try:
        collection = load_json(args.collection)
        issues = [fetch_issue(args.repo, number) for number in args.issue]
        issues.extend(load_issue(path) for path in args.issue_json)
        proposals = prepare_imports(collection, issues, repository=args.repo)
        print(render_preview(collection, proposals))
        if args.write:
            updated = append_confirmed(
                collection,
                proposals,
                maintainer=args.maintainer,
                reviewed_at=args.reviewed_at,
            )
            write_collection(args.collection, updated)
            print(f"wrote {args.collection}")
    except (IntakeError, OSError, json.JSONDecodeError) as exc:
        print(f"permissioned intake failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
