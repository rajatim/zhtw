#!/usr/bin/env python3
"""Build the scoped formal market report from aggregate benchmark reports."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_BLIND = PROJECT_ROOT / "docs/reports/blind-v2-benchmark-2026-07-31.json"
DEFAULT_UD = PROJECT_ROOT / "docs/reports/ud-gsd-benchmark-2026-07-31.json"
DEFAULT_NAER = PROJECT_ROOT / "docs/reports/naer-terms-benchmark-2026-07-31.json"
DEFAULT_OUTPUT_PREFIX = PROJECT_ROOT / "docs/reports/formal-market-benchmark-2026-07-31"
RANKING_REPRESENTATIVES = ("opencc-s2twp", "zhconv-zh-tw")


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON must be an object")
    return value


def percentage(value: float) -> str:
    return f"{value * 100:.2f}%"


def validate_inputs(blind: dict[str, Any], public_tracks: list[dict[str, Any]]) -> None:
    if blind.get("dataset") != "blind-v2" or blind.get("report_mode") != "aggregate":
        raise ValueError("the primary input must be the aggregate Blind-v2 report")
    if blind.get("summary", {}).get("case_count") != 1960:
        raise ValueError("Blind-v2 case count must be 1,960")
    candidate = blind.get("engines", {}).get("zhtw", {})
    if not candidate.get("available"):
        raise ValueError("zhtw must be available in the formal run")
    if candidate.get("scores", {}).get("p0_error_count") != 0:
        raise ValueError("zhtw has recorded P0 errors")

    for representative in RANKING_REPRESENTATIVES:
        engine = blind.get("engines", {}).get(representative, {})
        comparison = blind.get("paired_comparisons", {}).get(representative, {})
        if not engine.get("available"):
            raise ValueError(f"ranking representative is unavailable: {representative}")
        if comparison.get("result") != "winner":
            raise ValueError(f"zhtw is not the recorded winner against {representative}")
        if comparison.get("delta_ci_95", {}).get("low", 0) <= 0:
            raise ValueError(f"paired delta CI is not fully above zero: {representative}")

    public_sha = public_tracks[0].get("provenance", {}).get("git_sha")
    for track in public_tracks:
        if track.get("report_mode") != "aggregate":
            raise ValueError("public secondary reports must be aggregate-only")
        if track.get("primary_market_endpoint") is not False:
            raise ValueError("public tracks must remain secondary evidence")
        provenance = track.get("provenance", {})
        if provenance.get("git_dirty") is not False:
            raise ValueError(f"public track has dirty provenance: {track.get('dataset')}")
        if provenance.get("git_sha") != public_sha:
            raise ValueError("public tracks must use the same immutable commit")
    if not blind.get("provenance", {}).get("git_sha"):
        raise ValueError("Blind-v2 is missing immutable Git provenance")


def engine_summary(blind: dict[str, Any], engine_id: str) -> dict[str, Any]:
    engine = blind["engines"][engine_id]
    scores = engine["scores"]
    return {
        "id": engine_id,
        "version": engine["version"],
        "family": engine["family"],
        "accepted": scores["accepted"],
        "total_cases": scores["total_cases"],
        "accepted_accuracy": scores["accepted_accuracy"],
        "accepted_accuracy_ci_95": scores["accepted_accuracy_ci_95"],
        "idempotency_rate": scores["idempotency_rate"],
        "p0_error_count": scores["p0_error_count"],
    }


def build_report(blind: dict[str, Any], ud: dict[str, Any], naer: dict[str, Any]) -> dict[str, Any]:
    validate_inputs(blind, [ud, naer])
    zhtw = engine_summary(blind, "zhtw")
    opencc = engine_summary(blind, "opencc-s2twp")
    zhconv = engine_summary(blind, "zhconv-zh-tw")
    return {
        "generated_date": blind["generated_date"],
        "report_mode": "aggregate",
        "name": "formal-market-benchmark-v2",
        "decision": "scoped_winner",
        "primary_endpoint": {
            "dataset": "blind-v2",
            "direction": "Simplified Chinese to Taiwan Traditional Chinese",
            "case_count": blind["summary"]["case_count"],
            "metric": "accepted_accuracy",
            "engines": [zhtw, opencc, zhconv],
            "paired_comparisons": {
                key: blind["paired_comparisons"][key] for key in RANKING_REPRESENTATIVES
            },
        },
        "secondary_tracks": [
            {
                "dataset": ud["dataset"],
                "role": ud["evidence_role"],
                "cases": ud["scores"]["total_cases"],
                "accuracy": ud["scores"]["exact_accuracy"],
                "idempotency_rate": ud["scores"]["idempotency_rate"],
                "source_bias": ud["source_bias"],
                "git_sha": ud["provenance"]["git_sha"],
                "license": ud["license"],
            },
            {
                "dataset": naer["dataset"],
                "role": naer["evidence_role"],
                "cases": naer["scores"]["total_cases"],
                "accuracy": naer["scores"]["accepted_accuracy"],
                "idempotency_rate": naer["scores"]["idempotency_rate"],
                "excluded_context_candidates": naer["scores"]["excluded_context_candidates"],
                "git_sha": naer["provenance"]["git_sha"],
                "license": naer["license"],
            },
        ],
        "cross_track_assessment": {
            "status": "no_primary_conflict",
            "notes": [
                "Public tracks are secondary zhtw-only diagnostics and cannot change "
                "the Blind-v2 ranking.",
                "UD GSD has OpenCC-derived source bias and is not independent competitor evidence.",
                "NAER tests a conservative terminology subset, not sentence-level "
                "general accuracy.",
                "Blind-v2 domain results are mixed; zhtw did not lead every domain.",
                "zhtw idempotency was lower than both independent ranking "
                "representatives on Blind-v2.",
            ],
        },
        "governance": {
            "blind_v2_git_sha": blind["provenance"]["git_sha"],
            "public_tracks_git_sha": ud["provenance"]["git_sha"],
            "preregistration_sha256": blind["preregistration_sha256"],
            "inputs_sha256": blind["inputs"]["sha256"],
            "expected_sha256": blind["expected_sha256"],
            "competitor_lock_sha256": blind["competitors_lock"]["sha256"],
            "annotation_model": "single_human_with_ai_advisory",
            "publication_scope": "aggregate_only",
            "detailed_rows_read": False,
            "private_detailed_audit": "pending_controlled_post_result_audit",
            "external_hosted_public_reproduction": "configured_in_github_actions",
            "independent_third_party_reproduction": "pending",
            "maintainer_claim_confirmation": "pending",
        },
        "claim": {
            "status": "pending_maintainer_confirmation",
            "english": (
                f"On the frozen 1,960-case Blind-v2 benchmark for Simplified Chinese to "
                f"Taiwan Traditional Chinese, zhtw {zhtw['version']} achieved "
                f"{percentage(zhtw['accepted_accuracy'])} accepted accuracy, above OpenCC "
                f"{opencc['version']} at {percentage(opencc['accepted_accuracy'])} and zhconv "
                f"{zhconv['version']} at {percentage(zhconv['accepted_accuracy'])}. Both paired "
                "95% confidence intervals were above zero. This result applies only to this "
                "dataset, direction, metric, and the listed versions; it does not prove that "
                "zhtw is best for every domain or real-world workload."
            ),
            "prohibited": [
                "zhtw is the most accurate converter in every market or domain.",
                "33.72% is zhtw's expected accuracy on normal user traffic.",
                "The result covers untested converters, directions, versions, or datasets.",
            ],
        },
    }


def render_markdown(report: dict[str, Any]) -> str:
    primary = report["primary_endpoint"]
    engines = {engine["id"]: engine for engine in primary["engines"]}
    comparisons = primary["paired_comparisons"]
    lines = [
        "<!-- zhtw:disable -->",
        f"# Formal Market Benchmark ({report['generated_date']})",
        "",
        "Report mode: `aggregate`",
        "",
        "## Decision",
        "",
        "zhtw is the scoped winner on the preregistered Blind-v2 primary endpoint.",
        "This is not an unrestricted market-best claim.",
        "",
        "## Primary Result",
        "",
        "| Engine | Accepted | Accuracy | 95% CI | Idempotency |",
        "|---|---:|---:|---:|---:|",
    ]
    for engine_id in ("zhtw", "opencc-s2twp", "zhconv-zh-tw"):
        engine = engines[engine_id]
        ci = engine["accepted_accuracy_ci_95"]
        lines.append(
            f"| {engine_id} {engine['version']} | {engine['accepted']} / {engine['total_cases']} "
            f"| {percentage(engine['accepted_accuracy'])} | {percentage(ci['low'])}-"
            f"{percentage(ci['high'])} | {percentage(engine['idempotency_rate'])} |"
        )
    lines.extend(
        [
            "",
            "| Comparison | Delta | Delta 95% CI | McNemar p | Result |",
            "|---|---:|---:|---:|---|",
        ]
    )
    for engine_id in RANKING_REPRESENTATIVES:
        comparison = comparisons[engine_id]
        ci = comparison["delta_ci_95"]
        lines.append(
            f"| zhtw vs {engine_id} | +{comparison['absolute_delta'] * 100:.2f} pp | "
            f"+{ci['low'] * 100:.2f} to +{ci['high'] * 100:.2f} pp | "
            f"{comparison['mcnemar_exact_p']:.3g} | {comparison['result']} |"
        )
    lines.extend(
        [
            "",
            "Both paired confidence intervals are fully above zero, and the aggregate report",
            "records zero tagged P0 errors. The P0 value is not a separate human review of all",
            "misses because detailed rows remained sealed.",
            "",
            "## Secondary Evidence",
            "",
        ]
    )
    for track in report["secondary_tracks"]:
        lines.append(
            f"- `{track['dataset']}`: {track['cases']:,} cases, {percentage(track['accuracy'])} "
            f"accuracy, {percentage(track['idempotency_rate'])} idempotency; clean commit "
            f"`{track['git_sha']}`."
        )
    lines.extend(
        [
            "",
            "These tracks are zhtw-only diagnostics. UD GSD has OpenCC-derived source bias,",
            "while NAER is a limited terminology subset. Neither is an independent competitor",
            "ranking, and neither changes the Blind-v2 primary decision.",
            "",
            "## Limits",
            "",
            "- The result covers Simplified Chinese to Taiwan Traditional Chinese only.",
            "- It covers the frozen Blind-v2 cases and listed locked versions only.",
            "- Strict sentence-level accepted accuracy is not normal-traffic accuracy.",
            "- zhtw did not lead every domain and had lower Blind-v2 idempotency than both "
            "ranking representatives.",
            "- Expected values used one maintainer with Codex and independent Agy advice.",
            "- Detailed rows were not read; a controlled post-result audit remains pending.",
            "- Independent third-party reproduction remains pending.",
            "",
            "## Proposed Claim",
            "",
            report["claim"]["english"],
            "",
            "Status: `pending_maintainer_confirmation`.",
            "",
            "## Governance",
            "",
            f"- Blind-v2 commit: `{report['governance']['blind_v2_git_sha']}`",
            f"- Public-track commit: `{report['governance']['public_tracks_git_sha']}`",
            f"- Preregistration SHA-256: `{report['governance']['preregistration_sha256']}`",
            f"- Inputs SHA-256: `{report['governance']['inputs_sha256']}`",
            f"- Expected SHA-256: `{report['governance']['expected_sha256']}`",
            f"- Competitor lock SHA-256: `{report['governance']['competitor_lock_sha256']}`",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--blind", type=Path, default=DEFAULT_BLIND)
    parser.add_argument("--ud", type=Path, default=DEFAULT_UD)
    parser.add_argument("--naer", type=Path, default=DEFAULT_NAER)
    parser.add_argument("--output-prefix", type=Path, default=DEFAULT_OUTPUT_PREFIX)
    args = parser.parse_args()
    report = build_report(load_json(args.blind), load_json(args.ud), load_json(args.naer))
    args.output_prefix.parent.mkdir(parents=True, exist_ok=True)
    args.output_prefix.with_suffix(".json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    args.output_prefix.with_suffix(".md").write_text(render_markdown(report), encoding="utf-8")
    print("formal report: scoped_winner; maintainer confirmation pending")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
