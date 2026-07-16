#!/usr/bin/env python3
"""Generate a Gemini Vertex advisory review for sealed holdout inputs."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INPUTS = PROJECT_ROOT / "benchmarks" / "accuracy" / "blind-v1.inputs.json"
DEFAULT_CODEX = (
    PROJECT_ROOT
    / "docs"
    / "reports"
    / "holdout-codex-first-pass-blind-v1-0001-0100-2026-07-08.json"
)
DEFAULT_PROJECT = "tw-el-gemini"
DEFAULT_LOCATION = "us-central1"
DEFAULT_MODEL = "gemini-2.5-flash"
VALID_ISSUE_TAGS = {
    "over_conversion",
    "under_conversion",
    "regional_term",
    "it_term",
    "ui_term",
    "formal_term",
    "high_risk_term",
    "punctuation",
    "ambiguous_context",
    "other",
}
VALID_CONFIDENCE = {"high", "medium", "low"}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def relative_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path)


def selected_cases(
    inputs: dict[str, Any],
    *,
    batch: str | None,
    id_from: str | None,
    id_to: str | None,
) -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    for case in inputs["cases"]:
        case_id = str(case["id"])
        if batch is not None and case.get("batch") != batch:
            continue
        if id_from is not None and case_id < id_from:
            continue
        if id_to is not None and case_id > id_to:
            continue
        cases.append(case)
    return cases


def build_prompt(cases: list[dict[str, Any]]) -> str:
    payload = [
        {
            "id": case["id"],
            "batch": case["batch"],
            "domain": case["domain"],
            "risk": case["risk"],
            "tags": case.get("tags", []),
            "input": case["input"],
        }
        for case in cases
    ]
    return "\n".join(
        [
            "你是台灣繁體中文、IT/UI/i18n、正式文件、社群日常與高風險文字審稿者。",
            (
                "請只根據下方 input-only cases，為每筆簡體中文 input "
                "產生台灣繁體中文 expected output。"
            ),
            "",
            "重要邊界：",
            "- 這是獨立 advisory review，不是 human ground truth。",
            "- 不要使用 zhtw、OpenCC、zhconv、Codex 結論或任何競品輸出。",
            "- 不要新增原文沒有的意思，不要改寫成不同句型。",
            "- 保留英文字母、數字、符號與原句標點。",
            "- 使用台灣常見用語；寧可少轉，不要錯轉。",
            "- high_risk 領域要偏保守，法律/金融/醫療用語不要口語化。",
            "",
            "issue_tags 只能使用：",
            json.dumps(sorted(VALID_ISSUE_TAGS), ensure_ascii=False),
            "",
            "confidence 只能是 high、medium、low。",
            "",
            "只輸出 JSON，不要 Markdown，不要 code fence。JSON 格式必須是：",
            (
                '{"review":{"reviewer":"gemini_vertex",'
                '"review_type":"independent_holdout_expected_review",'
                '"cases":[{"id":"...","expected":"...",'
                '"acceptable":["..."],"issue_tags":["regional_term"],'
                '"confidence":"high","notes":"..."}]}}'
            ),
            "",
            "Cases:",
            json.dumps(payload, ensure_ascii=False, indent=2),
        ]
    )


def access_token() -> str:
    result = subprocess.run(
        ["gcloud", "auth", "print-access-token"],
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "failed to obtain gcloud access token")
    return result.stdout.strip()


def call_vertex(
    prompt: str,
    *,
    project: str,
    location: str,
    model: str,
) -> dict[str, Any]:
    endpoint = (
        f"https://{location}-aiplatform.googleapis.com/v1/projects/{project}"
        f"/locations/{location}/publishers/google/models/{model}:generateContent"
    )
    payload = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0,
            "maxOutputTokens": 32768,
            "responseMimeType": "application/json",
        },
    }
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {access_token()}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=240) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Vertex HTTP {error.code}: {body}") from error


def extract_review(response: dict[str, Any]) -> dict[str, Any]:
    try:
        text = response["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError) as error:
        raise ValueError("Vertex response did not contain text output") from error
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as error:
        raise ValueError(f"Gemini output was not JSON: {text[:500]}") from error
    review = payload.get("review")
    if not isinstance(review, dict):
        raise ValueError("Gemini JSON missing review object")
    cases = review.get("cases")
    if not isinstance(cases, list):
        raise ValueError("Gemini JSON missing review.cases array")
    return review


def validate_review_cases(cases: list[dict[str, Any]], review: dict[str, Any]) -> None:
    expected_ids = [str(case["id"]) for case in cases]
    review_cases = review["cases"]
    actual_ids = [str(case.get("id", "")) for case in review_cases]
    missing = [case_id for case_id in expected_ids if case_id not in actual_ids]
    extra = [case_id for case_id in actual_ids if case_id not in expected_ids]
    duplicates = sorted(case_id for case_id, count in Counter(actual_ids).items() if count > 1)
    if missing or extra or duplicates:
        raise ValueError(
            f"Gemini case id mismatch: missing={missing} extra={extra} duplicates={duplicates}"
        )

    for item in review_cases:
        case_id = str(item.get("id", ""))
        expected = str(item.get("expected", "")).strip()
        confidence = str(item.get("confidence", ""))
        issue_tags = item.get("issue_tags", [])
        acceptable = item.get("acceptable", [])
        if not expected:
            raise ValueError(f"Gemini case {case_id} has empty expected")
        if confidence not in VALID_CONFIDENCE:
            raise ValueError(f"Gemini case {case_id} has invalid confidence {confidence!r}")
        if not isinstance(issue_tags, list) or not issue_tags:
            raise ValueError(f"Gemini case {case_id} has empty issue_tags")
        invalid_tags = sorted(set(map(str, issue_tags)) - VALID_ISSUE_TAGS)
        if invalid_tags:
            raise ValueError(f"Gemini case {case_id} has invalid issue tags: {invalid_tags}")
        if not isinstance(acceptable, list):
            raise ValueError(f"Gemini case {case_id} acceptable must be a list")


def comparison_rows(
    input_cases: list[dict[str, Any]],
    gemini_review: dict[str, Any],
    codex_report: dict[str, Any],
) -> list[dict[str, Any]]:
    gemini_by_id = {str(case["id"]): case for case in gemini_review["cases"]}
    codex_by_id = {str(case["id"]): case for case in codex_report["cases"]}
    rows: list[dict[str, Any]] = []
    for case in input_cases:
        case_id = str(case["id"])
        gemini_case = gemini_by_id[case_id]
        codex_case = codex_by_id[case_id]
        codex_expected = str(codex_case["codex_expected"])
        gemini_expected = str(gemini_case["expected"])
        exact_match = codex_expected == gemini_expected
        needs_maintainer_review = (
            not exact_match
            or str(codex_case.get("confidence", "")) != "high"
            or str(gemini_case.get("confidence", "")) != "high"
            or case.get("domain") == "high_risk"
            or case.get("risk") == "over_conversion_guard"
        )
        rows.append(
            {
                "id": case_id,
                "batch": case["batch"],
                "domain": case["domain"],
                "risk": case["risk"],
                "input": case["input"],
                "codex_expected": codex_expected,
                "codex_acceptable": codex_case.get("acceptable", []),
                "codex_confidence": codex_case.get("confidence", ""),
                "codex_review_needed": codex_case.get("review_needed", False),
                "codex_rationale": codex_case.get("rationale", ""),
                "gemini_expected": gemini_expected,
                "gemini_acceptable": gemini_case.get("acceptable", []),
                "gemini_confidence": gemini_case.get("confidence", ""),
                "gemini_issue_tags": gemini_case.get("issue_tags", []),
                "gemini_notes": str(gemini_case.get("notes", "")),
                "exact_match": exact_match,
                "needs_maintainer_review": needs_maintainer_review,
            }
        )
    return rows


def code_block(text: str) -> str:
    fence = "```"
    while fence in text:
        fence += "`"
    return f"{fence}text\n{text}\n{fence}"


def build_report(
    *,
    inputs_path: Path,
    codex_path: Path,
    raw_report_path: Path,
    input_cases: list[dict[str, Any]],
    response: dict[str, Any],
    gemini_review: dict[str, Any],
    codex_report: dict[str, Any],
    generated_date: str,
    project: str,
    location: str,
    model: str,
) -> dict[str, Any]:
    rows = comparison_rows(input_cases, gemini_review, codex_report)
    exact_matches = sum(row["exact_match"] for row in rows)
    needs_review = sum(row["needs_maintainer_review"] for row in rows)
    by_domain = Counter(row["domain"] for row in rows)
    by_gemini_confidence = Counter(row["gemini_confidence"] for row in rows)
    return {
        "generated_date": generated_date,
        "dataset": "blind-v1",
        "reviewer": "gemini_vertex",
        "review_stage": "independent_holdout_expected_review",
        "ground_truth": False,
        "promotion_allowed": False,
        "model": model,
        "project": project,
        "location": location,
        "source_inputs": relative_path(inputs_path),
        "source_codex_report": relative_path(codex_path),
        "raw_report": relative_path(raw_report_path),
        "usage_metadata": response.get("usageMetadata", {}),
        "review": gemini_review,
        "summary": {
            "total_cases": len(rows),
            "exact_matches_with_codex": exact_matches,
            "differences_from_codex": len(rows) - exact_matches,
            "needs_maintainer_review": needs_review,
            "by_domain": dict(sorted(by_domain.items())),
            "by_gemini_confidence": dict(sorted(by_gemini_confidence.items())),
            "promotion_allowed": False,
        },
        "comparisons": rows,
    }


def render_markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines = [
        "<!-- zhtw:disable -->",
        f"# Holdout Gemini Vertex Advisory ({report['generated_date']})",
        "",
        f"Dataset: `{report['dataset']}`",
        f"Inputs: `{report['source_inputs']}`",
        f"Codex advisory: `{report['source_codex_report']}`",
        f"Raw JSON: `{report['raw_report']}`",
        f"Reviewer: `{report['reviewer']}`",
        f"Model: `{report['model']}`",
        "",
        "## Policy",
        "",
        "- Gemini saw only the input cases, not Codex recommendations.",
        "- This report is advisory only.",
        "- It is not ground truth and must not populate `blind-v1.expected.json` directly.",
        "- Maintainer confirmation is required before any expected value becomes human decision.",
        "",
        "## Summary",
        "",
        f"- Cases: {summary['total_cases']}",
        f"- Exact matches with Codex: {summary['exact_matches_with_codex']}",
        f"- Differences from Codex: {summary['differences_from_codex']}",
        f"- Needs maintainer review: {summary['needs_maintainer_review']}",
        "",
        "Gemini confidence:",
        "",
    ]
    for confidence, count in summary["by_gemini_confidence"].items():
        lines.append(f"- `{confidence}`: {count}")

    lines.extend(["", "Domain distribution:", ""])
    for domain, count in summary["by_domain"].items():
        lines.append(f"- `{domain}`: {count}")

    lines.extend(["", "## Maintainer Review Queue", ""])
    for row in report["comparisons"]:
        if row["needs_maintainer_review"]:
            status = "match" if row["exact_match"] else "different"
            lines.append(
                f"- `{row['id']}` ({row['domain']}, {status}, "
                f"Codex {row['codex_confidence']}, Gemini {row['gemini_confidence']})"
            )

    lines.extend(["", "## Comparisons", ""])
    for row in report["comparisons"]:
        status = "match" if row["exact_match"] else "different"
        lines.extend(
            [
                f"### {row['id']}：{status}",
                "",
                f"- Domain: `{row['domain']}`",
                f"- Risk: `{row['risk']}`",
                f"- Codex confidence: `{row['codex_confidence']}`",
                f"- Gemini confidence: `{row['gemini_confidence']}`",
                f"- Needs maintainer review: `{str(row['needs_maintainer_review']).lower()}`",
                "",
                "Input:",
                "",
                code_block(row["input"]),
                "",
                "Codex expected:",
                "",
                code_block(row["codex_expected"]),
                "",
                "Gemini expected:",
                "",
                code_block(row["gemini_expected"]),
                "",
                "Gemini acceptable variants:",
                "",
                code_block(
                    "\n".join(row["gemini_acceptable"]) if row["gemini_acceptable"] else "(none)"
                ),
                "",
                "Gemini notes:",
                "",
                code_block(row["gemini_notes"]),
                "",
            ]
        )
    return "\n".join(lines)


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path, default=DEFAULT_INPUTS)
    parser.add_argument("--codex-report", type=Path, default=DEFAULT_CODEX)
    parser.add_argument("--batch", default=None)
    parser.add_argument("--id-from", default=None)
    parser.add_argument("--id-to", default=None)
    parser.add_argument("--project", default=DEFAULT_PROJECT)
    parser.add_argument("--location", default=DEFAULT_LOCATION)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--generated-date", default=dt.date.today().isoformat())
    parser.add_argument("--output-json", type=Path, required=True)
    parser.add_argument("--output-md", type=Path, required=True)
    args = parser.parse_args()

    inputs = load_json(args.inputs)
    codex_report = load_json(args.codex_report)
    cases = selected_cases(inputs, batch=args.batch, id_from=args.id_from, id_to=args.id_to)
    if not cases:
        print("No cases selected for Gemini holdout advisory review", file=sys.stderr)
        return 1

    response = call_vertex(
        build_prompt(cases),
        project=args.project,
        location=args.location,
        model=args.model,
    )
    review = extract_review(response)
    validate_review_cases(cases, review)
    report = build_report(
        inputs_path=args.inputs,
        codex_path=args.codex_report,
        raw_report_path=args.output_json,
        input_cases=cases,
        response=response,
        gemini_review=review,
        codex_report=codex_report,
        generated_date=args.generated_date,
        project=args.project,
        location=args.location,
        model=args.model,
    )

    write_json(args.output_json, report)
    args.output_md.parent.mkdir(parents=True, exist_ok=True)
    args.output_md.write_text(render_markdown(report), encoding="utf-8")

    summary = report["summary"]
    print(
        "cases={total_cases} exact_matches={exact_matches_with_codex} "
        "differences={differences_from_codex} "
        "needs_review={needs_maintainer_review}".format(**summary)
    )
    print(f"wrote {relative_path(args.output_json)}")
    print(f"wrote {relative_path(args.output_md)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
