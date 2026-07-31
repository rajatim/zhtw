#!/usr/bin/env python3
"""Build private final advice and a public aggregate Blind-v2 audit report."""

from __future__ import annotations

import argparse
import datetime as dt
import json
from collections import Counter
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PRIVATE_ROOT = PROJECT_ROOT / "benchmarks/accuracy/private/post-result-audit-v1"
DEFAULT_OUTPUT_PREFIX = PROJECT_ROOT / "docs/reports/blind-v2-post-result-audit-2026-07-31"
DECISION_FIELDS = ("severity", "category", "expected_valid", "actual_acceptable")
MAINTAINER_DECISION = PRIVATE_ROOT / "maintainer-decision.json"


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON must be an object")
    return value


def load_cases(directory: Path) -> dict[str, dict[str, Any]]:
    cases: dict[str, dict[str, Any]] = {}
    for path in sorted(directory.glob("*.json")):
        if not path.name.startswith(("packet-", "review-")):
            continue
        for case in load_json(path)["cases"]:
            case_id = case["id"]
            if case_id in cases:
                raise ValueError(f"duplicate case ID in {directory}: {case_id}")
            cases[case_id] = case
    return cases


def count(values: list[str]) -> dict[str, int]:
    return dict(sorted(Counter(values).items()))


def load_maintainer_decision(private_root: Path, queue_size: int) -> dict[str, Any] | None:
    path = private_root / "maintainer-decision.json"
    if not path.exists():
        return None
    decision = load_json(path)
    required = {
        "version": 1,
        "audit_id": "blind-v2-post-result-audit-1",
        "decision": "approve_all_synthesis_decisions",
        "confirmed_cases": queue_size,
        "confirmed_by": "tim",
    }
    for key, expected in required.items():
        if decision.get(key) != expected:
            raise ValueError(f"invalid maintainer decision field: {key}")
    if not decision.get("confirmed_at") or not decision.get("confirmation"):
        raise ValueError("maintainer decision requires time and confirmation text")
    return decision


def build_outputs(private_root: Path = PRIVATE_ROOT) -> tuple[dict[str, Any], dict[str, Any]]:
    manifest = load_json(private_root / "manifest.json")
    packets = load_cases(private_root)
    codex = load_cases(private_root / "codex")
    agy = load_cases(private_root / "agy")
    synthesis = load_cases(private_root / "synthesis")
    case_ids = set(packets)
    if len(case_ids) != manifest["misses"]:
        raise ValueError("packet coverage does not match the private manifest")
    if set(codex) != case_ids or set(agy) != case_ids:
        raise ValueError("Codex and Agy must both cover every miss")

    selected_ids = {
        case_id
        for case_id in case_ids
        if any(codex[case_id][field] != agy[case_id][field] for field in DECISION_FIELDS)
        or {codex[case_id]["severity"], agy[case_id]["severity"]} & {"P0", "P1"}
        or not codex[case_id]["expected_valid"]
        or not agy[case_id]["expected_valid"]
    }
    if set(synthesis) != selected_ids:
        raise ValueError("synthesis coverage does not match the selected case set")

    final_cases = []
    for case_id, packet in packets.items():
        if case_id in synthesis:
            decision = synthesis[case_id]
            source = f"synthesis_{decision['decision_source']}"
            needs_maintainer = decision["needs_maintainer"]
        else:
            if any(codex[case_id][field] != agy[case_id][field] for field in DECISION_FIELDS):
                raise ValueError(f"unsynthesized disagreement: {case_id}")
            decision = codex[case_id]
            source = "codex_agy_agreement"
            needs_maintainer = False
        final_cases.append(
            {
                **packet,
                "codex_review": codex[case_id],
                "agy_review": agy[case_id],
                "synthesis_review": synthesis.get(case_id),
                "final_advisory": {
                    **{field: decision[field] for field in DECISION_FIELDS},
                    "confidence": decision["confidence"],
                    "rationale": decision["rationale"],
                    "source": source,
                    "needs_maintainer": needs_maintainer,
                },
            }
        )

    queue = [case for case in final_cases if case["final_advisory"]["needs_maintainer"]]
    maintainer_decision = load_maintainer_decision(private_root, len(queue))
    status = "completed" if maintainer_decision else "pending_maintainer_confirmation"
    if maintainer_decision:
        for case in queue:
            case["maintainer_decision"] = "approved_synthesis"
    private = {
        "version": 1,
        "dataset": "blind-v2",
        "audit_id": "blind-v2-post-result-audit-1",
        "status": status,
        "cases": final_cases,
        "maintainer_queue": queue,
        "maintainer_decision": maintainer_decision,
    }

    severity_agreement = sum(codex[key]["severity"] == agy[key]["severity"] for key in case_ids)
    category_agreement = sum(codex[key]["category"] == agy[key]["category"] for key in case_ids)
    full_agreement = sum(
        all(codex[key][field] == agy[key][field] for field in DECISION_FIELDS) for key in case_ids
    )
    decisions = [case["final_advisory"] for case in final_cases]
    queue_decisions = [case["final_advisory"] for case in queue]
    public = {
        "generated_date": "2026-07-31",
        "report_mode": "aggregate",
        "dataset": "blind-v2",
        "audit_id": "blind-v2-post-result-audit-1",
        "status": status,
        "scope": {
            "benchmark_cases": manifest["total_cases"],
            "audited_zhtw_misses": manifest["misses"],
            "coverage": 1.0,
        },
        "review": {
            "order": [
                "codex_first_pass",
                "agy_independent",
                "codex_synthesis",
                "maintainer_decision",
            ],
            "codex_first_pass_cases": len(codex),
            "agy_independent_cases": len(agy),
            "synthesis_cases": len(synthesis),
            "first_pass_agreement": {
                "severity": severity_agreement,
                "category": category_agreement,
                "all_decision_fields": full_agreement,
                "total": len(case_ids),
            },
        },
        "final_advisory": {
            "severity_counts": count([item["severity"] for item in decisions]),
            "category_counts": count([item["category"] for item in decisions]),
            "decision_source_counts": count([item["source"] for item in decisions]),
            "reference_status_counts": {
                "needs_correction": sum(not item["expected_valid"] for item in decisions),
                "valid": sum(item["expected_valid"] for item in decisions),
            },
            "actual_assessment_counts": {
                "accepted_rendering": sum(item["actual_acceptable"] for item in decisions),
                "rejected_rendering": sum(not item["actual_acceptable"] for item in decisions),
            },
            "by_domain": count([case["domain"] for case in final_cases]),
            "by_risk": count([case["risk"] for case in final_cases]),
        },
        "maintainer_queue": {
            "status": "confirmed" if maintainer_decision else "pending",
            "cases": len(queue),
            "severity_counts": count([item["severity"] for item in queue_decisions]),
            "reference_correction_candidates": sum(
                not item["expected_valid"] for item in queue_decisions
            ),
            "acceptable_variant_candidates": sum(
                item["actual_acceptable"] for item in queue_decisions
            ),
        },
        "governance": {
            "case_level_artifacts": "private_gitignored",
            "public_content": "aggregate_counts_only",
            "published_score": "immutable",
            "result_tuning": "prohibited",
            "audit_completion": (
                "maintainer_confirmed"
                if maintainer_decision
                else "requires_maintainer_confirmation"
            ),
        },
    }
    if maintainer_decision:
        public["maintainer_queue"]["confirmed_by"] = maintainer_decision["confirmed_by"]
        public["maintainer_queue"]["confirmed_date"] = maintainer_decision["confirmed_at"][:10]
    return private, public


def percentage(numerator: int, denominator: int) -> str:
    return f"{numerator / denominator * 100:.2f}%"


def render_markdown(report: dict[str, Any]) -> str:
    scope = report["scope"]
    review = report["review"]
    agreement = review["first_pass_agreement"]
    advisory = report["final_advisory"]
    queue = report["maintainer_queue"]
    severity = advisory["severity_counts"]
    if report["status"] == "completed":
        status_lines = [
            "The controlled audit reviewed every zhtw miss. The maintainer approved all",
            f"{queue['cases']:,} queued synthesis decisions, so the audit is complete. The",
            "published Blind-v2 score remains immutable.",
        ]
    else:
        status_lines = [
            "The controlled audit has reviewed every zhtw miss and is pending maintainer",
            "confirmation. The published Blind-v2 score is immutable.",
        ]
    lines = [
        "<!-- zhtw:disable -->",
        "# Blind-v2 Post-result Audit (2026-07-31)",
        "",
        "Report mode: `aggregate`",
        "",
        "## Status",
        "",
        *status_lines,
        "",
        "## Coverage",
        "",
        f"- Benchmark cases: {scope['benchmark_cases']:,}",
        f"- Audited zhtw misses: {scope['audited_zhtw_misses']:,}",
        f"- Codex first pass: {review['codex_first_pass_cases']:,}",
        f"- Independent Agy review: {review['agy_independent_cases']:,}",
        f"- Codex synthesis: {review['synthesis_cases']:,}",
        "",
        "## Agreement",
        "",
        f"- Severity: {agreement['severity']:,} / {agreement['total']:,} "
        f"({percentage(agreement['severity'], agreement['total'])})",
        f"- Category: {agreement['category']:,} / {agreement['total']:,} "
        f"({percentage(agreement['category'], agreement['total'])})",
        f"- All decision fields: {agreement['all_decision_fields']:,} / "
        f"{agreement['total']:,} "
        f"({percentage(agreement['all_decision_fields'], agreement['total'])})",
        "",
        "## Final Advisory",
        "",
        "| Severity | Cases |",
        "|---|---:|",
    ]
    for name in ("P0", "P1", "P2", "P3", "none"):
        lines.append(f"| {name} | {severity.get(name, 0):,} |")
    if report["status"] == "completed":
        queue_summary = (
            f"The maintainer confirmed all {queue['cases']:,} queued cases: "
            f"{queue['severity_counts'].get('P1', 0):,} P1 semantic-error decisions and "
            f"{queue['acceptable_variant_candidates']:,} acceptable-variant decisions. "
            f"The review included {queue['reference_correction_candidates']:,} "
            "reference-correction candidates."
        )
    else:
        queue_summary = (
            f"The private maintainer queue contains {queue['cases']:,} cases: "
            f"{queue['severity_counts'].get('P1', 0):,} P1 semantic-error decisions and "
            f"{queue['acceptable_variant_candidates']:,} acceptable-variant decisions. "
            f"It includes {queue['reference_correction_candidates']:,} "
            "reference-correction candidates."
        )
    lines.extend(
        [
            "",
            queue_summary,
            "",
            "## Governance",
            "",
            "- Case-level material remains private and gitignored.",
            "- This report contains aggregate counts only.",
            "- Findings cannot change the consumed Blind-v2 score.",
            "- Findings cannot be used to tune against sealed rows.",
            (
                "- The maintainer confirmed all queued synthesis decisions."
                if report["status"] == "completed"
                else "- The audit is complete only after maintainer confirmation."
            ),
            "",
        ]
    )
    return "\n".join(lines)


def render_private_maintainer_review(private: dict[str, Any], batch_size: int = 50) -> str:
    lines = [
        "<!-- zhtw:disable -->",
        "# Blind-v2 Private Maintainer Review",
        "",
        "This file is private and gitignored. The consumed benchmark score is immutable.",
        (
            "The maintainer approved every queued final advisory."
            if private["status"] == "completed"
            else "Approve or correct each final advisory; AI advice is not human ground truth."
        ),
        "",
    ]
    queue = private["maintainer_queue"]
    for index, case in enumerate(queue, start=1):
        if (index - 1) % batch_size == 0:
            batch = (index - 1) // batch_size + 1
            lines.extend([f"## Batch {batch:03d}", ""])
        decision = case["final_advisory"]
        lines.extend(
            [
                f"### {index}. {case['id']}",
                "",
                f"- Input: {case['input']}",
                f"- Reference: {case['expected']}",
                f"- zhtw: {case['actual']}",
                f"- Recommendation: `{decision['severity']}` / `{decision['category']}`; "
                f"reference valid = `{str(decision['expected_valid']).lower()}`; "
                f"zhtw acceptable = `{str(decision['actual_acceptable']).lower()}`",
                f"- Reason: {decision['rationale']}",
                "",
            ]
        )
    return "\n".join(lines)


def write_outputs(
    private: dict[str, Any],
    public: dict[str, Any],
    output_prefix: Path,
    private_root: Path = PRIVATE_ROOT,
) -> None:
    private_root.mkdir(parents=True, exist_ok=True)
    (private_root / "final-advisory.json").write_text(
        json.dumps(private, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (private_root / "maintainer-review.md").write_text(
        render_private_maintainer_review(private), encoding="utf-8"
    )
    output_prefix.parent.mkdir(parents=True, exist_ok=True)
    output_prefix.with_suffix(".json").write_text(
        json.dumps(public, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    output_prefix.with_suffix(".md").write_text(render_markdown(public), encoding="utf-8")


def record_maintainer_confirmation(private_root: Path, queue_size: int) -> None:
    path = private_root / "maintainer-decision.json"
    if path.exists():
        raise ValueError("maintainer decision is already recorded")
    decision = {
        "version": 1,
        "audit_id": "blind-v2-post-result-audit-1",
        "decision": "approve_all_synthesis_decisions",
        "confirmed_cases": queue_size,
        "confirmed_by": "tim",
        "confirmed_at": dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z"),
        "confirmation": "Follow the recommendation",
    }
    path.write_text(json.dumps(decision, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-prefix", type=Path, default=DEFAULT_OUTPUT_PREFIX)
    parser.add_argument("--confirm-maintainer", action="store_true")
    args = parser.parse_args()
    if args.confirm_maintainer:
        private, _ = build_outputs()
        record_maintainer_confirmation(PRIVATE_ROOT, len(private["maintainer_queue"]))
    private, public = build_outputs()
    write_outputs(private, public, args.output_prefix.resolve())
    print(
        f"audit report built: {public['scope']['audited_zhtw_misses']} misses, "
        f"{public['maintainer_queue']['cases']} maintainer cases; status={public['status']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
