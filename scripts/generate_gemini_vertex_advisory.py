#!/usr/bin/env python3
"""Generate a Gemini Vertex advisory review for annotation backlog cases."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_BACKLOG = PROJECT_ROOT / "benchmarks" / "accuracy" / "annotation-backlog-v1.json"
DEFAULT_PROJECT = "tw-el-gemini"
DEFAULT_LOCATION = "us-central1"
DEFAULT_MODEL = "gemini-2.5-flash"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def relative_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path)


def selected_cases(
    backlog: dict[str, Any],
    *,
    batch: str | None,
    status: str | None,
    id_from: str | None,
    id_to: str | None,
) -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    for case in backlog["cases"]:
        case_id = str(case["id"])
        review = case.get("review", {})
        if batch is not None and case.get("batch") != batch:
            continue
        if status is not None and review.get("status") != status:
            continue
        if id_from is not None and case_id < id_from:
            continue
        if id_to is not None and case_id > id_to:
            continue
        cases.append(case)
    return cases


def review_context(case: dict[str, Any]) -> str:
    batch = str(case.get("batch", ""))
    domain = str(case.get("domain", ""))
    contexts = {
        "it-api-cli": "IT/API/CLI 簡體轉台灣繁體 expected output 標註",
        "ui-i18n": "UI/i18n 產品介面文案簡體轉台灣繁體 expected output 標註",
        "formal-high-risk": "正式文件與高風險領域簡體轉台灣繁體 expected output 標註",
        "social-daily": "社群與日常短句簡體轉台灣繁體 expected output 標註",
        "mixed-ambiguity": "混合語境與歧義詞簡體轉台灣繁體 expected output 標註",
    }
    return contexts.get(batch, f"{domain or 'general'} 簡體轉台灣繁體 expected output 標註")


def reviewer_role(cases: list[dict[str, Any]]) -> str:
    batches = {str(case.get("batch", "")) for case in cases}
    if batches == {"ui-i18n"}:
        return "你是台灣繁體中文與 UI/i18n 產品介面文案審稿者。"
    if batches == {"formal-high-risk"}:
        return "你是台灣繁體中文正式文件與高風險領域文案審稿者。"
    if batches == {"social-daily"}:
        return "你是台灣繁體中文社群與日常短句審稿者。"
    if batches == {"mixed-ambiguity"}:
        return "你是台灣繁體中文歧義詞與混合語境審稿者。"
    return "你是台灣繁體中文與 IT/API/CLI 文件審稿者。"


def build_prompt(cases: list[dict[str, Any]]) -> str:
    payload = [
        {
            "id": case["id"],
            "domain": case["domain"],
            "input": case["input"],
            "context": review_context(case),
        }
        for case in cases
    ]
    return "\n".join(
        [
            reviewer_role(cases),
            "請為每筆簡體中文 input 產生台灣繁體中文 expected output。",
            "規則：",
            "- 使用台灣常見技術用語；寧可少轉，不要錯轉。",
            "- 不要使用 OpenCC 或競品輸出作為依據。",
            "- 保留英文字母、數字、符號與原句標點。",
            "- 只輸出 JSON，不要 Markdown。",
            "",
            "JSON 格式必須是：",
            '{"review":{"reviewer":"gemini_vertex","review_type":"independent_expected_review","cases":[{"id":"...","expected":"...","notes":"..."}]}}',
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
            "maxOutputTokens": 16384,
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
        with urllib.request.urlopen(request, timeout=180) as response:
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


def comparison_rows(cases: list[dict[str, Any]], review: dict[str, Any]) -> list[dict[str, Any]]:
    gemini_by_id = {str(case["id"]): case for case in review["cases"]}
    expected_ids = [case["id"] for case in cases]
    actual_ids = sorted(gemini_by_id)
    missing = [case_id for case_id in expected_ids if case_id not in gemini_by_id]
    extra = [case_id for case_id in actual_ids if case_id not in expected_ids]
    if missing or extra:
        raise ValueError(f"Gemini case id mismatch: missing={missing} extra={extra}")

    rows: list[dict[str, Any]] = []
    for case in cases:
        gemini_case = gemini_by_id[case["id"]]
        codex_expected = str(case.get("ai_draft", {}).get("expected", ""))
        gemini_expected = str(gemini_case.get("expected", ""))
        if not gemini_expected.strip():
            raise ValueError(f"Gemini case {case['id']} has empty expected")
        rows.append(
            {
                "id": case["id"],
                "input": case["input"],
                "codex_expected": codex_expected,
                "gemini_expected": gemini_expected,
                "gemini_notes": str(gemini_case.get("notes", "")),
                "exact_match_with_codex_draft": codex_expected == gemini_expected,
            }
        )
    return rows


def code_block(text: str) -> str:
    fence = "```"
    while fence in text:
        fence += "`"
    return f"{fence}text\n{text}\n{fence}"


def render_markdown(report: dict[str, Any]) -> str:
    summary = report["comparison_summary"]
    lines = [
        "<!-- zhtw:disable -->",
        f"# Gemini Vertex Advisory Review：{report['case_range']}（{report['generated_date']}）",
        "",
        f"Backlog：`{report['source_backlog']}`",
        f"Raw JSON：`{report['raw_report']}`",
        "",
        "## Boundary",
        "",
        "- This is Gemini Vertex AI advisory output, not a human review.",
        (
            "- It must not be recorded as `human_first_pass`, "
            "`human_adjudication`, or `blind_reviewer`."
        ),
        (
            "- Maintainer review is required before any `review.expected` "
            "value becomes promotion-ready."
        ),
        "",
        "## Summary",
        "",
        f"- Model: `{report['model']}`",
        f"- Project: `{report['project']}`",
        f"- Location: `{report['location']}`",
        f"- Cases: {summary['cases']}",
        f"- Exact matches with Codex draft: {summary['exact_matches_with_codex_draft']}",
        f"- Differences from Codex draft: {summary['differences_from_codex_draft']}",
        "",
        "## Maintainer Action",
        "",
        (
            "For each case, choose the final Taiwan Traditional expected output. "
            "After maintainer approval:"
        ),
        "",
        "- write the final value to `review.expected`",
        (
            '- set `review.expected_source = "human_first_pass"` when accepting '
            "one advisory version unchanged"
        ),
        (
            '- set `review.expected_source = "human_adjudication"` and '
            '`review.adjudicator = "tim"` when resolving a difference'
        ),
        "- keep Gemini under `review.ai_advisory`; do not set it as `blind_reviewer`",
        "",
        "## Comparison",
        "",
    ]

    for row in report["comparisons"]:
        status = "match" if row["exact_match_with_codex_draft"] else "different"
        lines.extend(
            [
                f"### {row['id']}：{status}",
                "",
                "Input:",
                "",
                code_block(row["input"]),
                "",
                "Codex draft expected:",
                "",
                code_block(row["codex_expected"]),
                "",
                "Gemini advisory expected:",
                "",
                code_block(row["gemini_expected"]),
                "",
                "Gemini notes:",
                "",
                code_block(row["gemini_notes"]),
                "",
            ]
        )

    return "\n".join(lines)


def build_report(
    *,
    backlog_path: Path,
    raw_report_path: Path,
    cases: list[dict[str, Any]],
    response: dict[str, Any],
    review: dict[str, Any],
    generated_date: str,
    project: str,
    location: str,
    model: str,
) -> dict[str, Any]:
    rows = comparison_rows(cases, review)
    exact_matches = sum(row["exact_match_with_codex_draft"] for row in rows)
    case_range = f"{cases[0]['id']}-{cases[-1]['id']}"
    return {
        "generated_date": generated_date,
        "model": model,
        "project": project,
        "location": location,
        "source_backlog": relative_path(backlog_path),
        "raw_report": relative_path(raw_report_path),
        "case_range": case_range,
        "usage_metadata": response.get("usageMetadata", {}),
        "review": review,
        "comparison_summary": {
            "cases": len(rows),
            "exact_matches_with_codex_draft": exact_matches,
            "differences_from_codex_draft": len(rows) - exact_matches,
        },
        "comparisons": rows,
    }


def update_backlog(
    backlog: dict[str, Any],
    report: dict[str, Any],
    *,
    source_report: Path,
    raw_report: Path,
) -> None:
    comparison_by_id = {row["id"]: row for row in report["comparisons"]}
    for case in backlog["cases"]:
        row = comparison_by_id.get(case["id"])
        if row is None:
            continue
        review = case["review"]
        review["status"] = "needs_maintainer_review"
        review["ai_advisory_draft"] = {
            "reviewer": "gemini_vertex",
            "source_report": relative_path(source_report),
            "raw_report": relative_path(raw_report),
            "exact_match_with_ai_draft": row["exact_match_with_codex_draft"],
        }


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backlog", type=Path, default=DEFAULT_BACKLOG)
    parser.add_argument("--batch", default=None)
    parser.add_argument("--status", default=None)
    parser.add_argument("--id-from", default=None)
    parser.add_argument("--id-to", default=None)
    parser.add_argument("--project", default=DEFAULT_PROJECT)
    parser.add_argument("--location", default=DEFAULT_LOCATION)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--generated-date", default=dt.date.today().isoformat())
    parser.add_argument("--output-json", type=Path, required=True)
    parser.add_argument("--output-md", type=Path, required=True)
    parser.add_argument("--update-backlog", action="store_true")
    args = parser.parse_args()

    backlog = load_json(args.backlog)
    cases = selected_cases(
        backlog,
        batch=args.batch,
        status=args.status,
        id_from=args.id_from,
        id_to=args.id_to,
    )
    if not cases:
        print("No cases selected for Gemini advisory review", file=sys.stderr)
        return 1

    response = call_vertex(
        build_prompt(cases),
        project=args.project,
        location=args.location,
        model=args.model,
    )
    review = extract_review(response)
    report = build_report(
        backlog_path=args.backlog,
        raw_report_path=args.output_json,
        cases=cases,
        response=response,
        review=review,
        generated_date=args.generated_date,
        project=args.project,
        location=args.location,
        model=args.model,
    )

    write_json(args.output_json, report)
    args.output_md.parent.mkdir(parents=True, exist_ok=True)
    args.output_md.write_text(render_markdown(report), encoding="utf-8")

    if args.update_backlog:
        update_backlog(backlog, report, source_report=args.output_md, raw_report=args.output_json)
        args.backlog.write_text(
            json.dumps(backlog, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    summary = report["comparison_summary"]
    print(
        "cases={cases} exact_matches={exact_matches_with_codex_draft} "
        "differences={differences_from_codex_draft}".format(**summary)
    )
    print(f"wrote {relative_path(args.output_json)}")
    print(f"wrote {relative_path(args.output_md)}")
    if args.update_backlog:
        print(f"updated {relative_path(args.backlog)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
