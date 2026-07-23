#!/usr/bin/env python3
"""Promote confirmed input-only classifications into a collecting Blind-v2 pool."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.benchmark_metrics import canonical_json_bytes, paired_power_analysis  # noqa: E402
from scripts.blind_v2_governance import (  # noqa: E402
    NEAR_DUPLICATE_THRESHOLD,
    _expected_stats,
    _near_duplicate_pairs,
    _near_duplicates_against_references,
    normalize_for_dedupe,
    reference_texts,
    validate_pool,
    validate_schema,
)
from scripts.record_blind_v2_source_classification_decision import (  # noqa: E402
    validate_decision,
)

ACCURACY_ROOT = PROJECT_ROOT / "benchmarks" / "accuracy"
POOL_SCHEMA = ACCURACY_ROOT / "blind-v2.candidate-pool.schema.json"


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON must be an object")
    return value


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def project_path(raw: str) -> Path:
    path = (PROJECT_ROOT / raw).resolve()
    try:
        path.relative_to(PROJECT_ROOT)
    except ValueError as exc:
        raise ValueError(f"path escapes project root: {raw}") from exc
    return path


def verified_decision_cases(
    decision_path: Path,
) -> tuple[dict[str, Any], list[tuple[dict[str, Any], dict[str, Any], dict[str, Any]]]]:
    decision = load_json(decision_path)
    decision_errors = validate_decision(decision)
    if decision_errors:
        raise ValueError(f"{decision_path}: " + "; ".join(decision_errors))
    if decision.get("status") != "all_classifications_confirmed":
        raise ValueError(f"{decision_path}: classifications are not fully confirmed")
    for path_field, hash_field in (
        ("codex_path", "codex_sha256"),
        ("gemini_path", "gemini_sha256"),
    ):
        advisory_path = project_path(decision[path_field])
        if sha256_file(advisory_path) != decision[hash_field]:
            raise ValueError(f"{decision_path}: {path_field} sha256 mismatch")
    if "synthesis_path" in decision:
        synthesis_path = project_path(decision["synthesis_path"])
        if sha256_file(synthesis_path) != decision["synthesis_sha256"]:
            raise ValueError(f"{decision_path}: synthesis_path sha256 mismatch")
    packet_path = project_path(decision["packet_path"])
    if sha256_file(packet_path) != decision["packet_sha256"]:
        raise ValueError(f"{decision_path}: packet sha256 mismatch")
    packet = load_json(packet_path)
    if packet.get("input_only") is not True or packet.get("converter_output_used") is not False:
        raise ValueError(f"{packet_path}: packet is not input-only")

    packet_cases = {case["id"]: case for case in packet["cases"]}
    decision_cases = {case["id"]: case for case in decision["cases"]}
    if set(packet_cases) != set(decision_cases):
        raise ValueError(f"{decision_path}: decision IDs do not exactly cover packet")

    manifests: dict[str, dict[str, Any]] = {}
    for snapshot in packet["source_snapshots"]:
        source_path = project_path(snapshot["path"])
        if sha256_file(source_path) != snapshot["sha256"]:
            raise ValueError(f"{source_path}: source snapshot sha256 mismatch")
        source = load_json(source_path)
        manifest_path = ACCURACY_ROOT / "manifests" / f"{source['id']}.json"
        manifest = load_json(manifest_path)
        if project_path(manifest["normalized_path"]) != source_path:
            raise ValueError(f"{manifest_path}: normalized_path does not match packet source")
        if manifest["normalized_sha256"] != snapshot["sha256"]:
            raise ValueError(f"{manifest_path}: normalized_sha256 does not match packet source")
        manifests[source["id"]] = manifest

    confirmed = []
    for case in packet["cases"]:
        classification = decision_cases[case["id"]]["classification"]
        if classification["eligible"]:
            confirmed.append((case, classification, manifests[case["source_id"]]))
    return decision, confirmed


def pool_template(*, created_at: str) -> dict[str, Any]:
    power = paired_power_analysis(
        discordant_rate=0.1,
        minimum_detectable_effect=0.02,
        alpha=0.05,
        target_power=0.8,
    )
    return {
        "version": 1,
        "id": "blind-v2-candidate-pool-v1",
        "status": "collecting",
        "created_at": created_at,
        "formal_n": power["required_cases"],
        "power_analysis": {
            key: power[key]
            for key in (
                "method",
                "discordant_rate",
                "minimum_detectable_effect",
                "alpha",
                "target_power",
                "required_cases",
            )
        },
        "seed": 20260719,
        "source_policy": {
            "maximum_source_fraction": 0.1,
            "maximum_source_class_fraction": 0.35,
        },
        "deduplication": {
            "normalization": "unicode-nfc-collapse-whitespace-v1",
            "ngram_size": 5,
            "near_duplicate_threshold": NEAR_DUPLICATE_THRESHOLD,
            "reference_globs": [
                "benchmarks/accuracy/*.json",
                "docs/reports/*.json",
                "src/zhtw/data/terms/**/*.json",
            ],
            "reference_snapshot_sha256": "0" * 64,
        },
        "stats": _expected_stats([]),
        "cases": [],
    }


def build_pool(
    decision_paths: list[Path], *, output: Path, created_at: str
) -> tuple[dict[str, Any], dict[str, Any]]:
    promoted: list[tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]] = []
    decisions: list[dict[str, str]] = []
    seen_ids: set[str] = set()
    for decision_path in decision_paths:
        decision, cases = verified_decision_cases(decision_path)
        decisions.append(
            {
                "path": str(decision_path.relative_to(PROJECT_ROOT)),
                "sha256": sha256_file(decision_path),
            }
        )
        for case, classification, manifest in cases:
            if case["id"] in seen_ids:
                raise ValueError(f"duplicate promoted source case: {case['id']}")
            seen_ids.add(case["id"])
            promoted.append((case, classification, manifest, decision["decision_date"]))

    pool = pool_template(created_at=created_at)
    references, reference_errors, snapshot_hash = reference_texts(pool, output)
    if reference_errors:
        raise ValueError("; ".join(reference_errors))
    pool["deduplication"]["reference_snapshot_sha256"] = snapshot_hash

    exclusions: dict[str, dict[str, Any]] = {}
    normalized_to_id: dict[str, str] = {}
    eligible_for_near: list[tuple[str, str]] = []
    reference_exact = {normalize_for_dedupe(text) for text in references if text.strip()}
    for case, _, _, _ in promoted:
        normalized = normalize_for_dedupe(case["input"])
        if normalized in normalized_to_id:
            exclusions[case["id"]] = {
                "reason": "exact_duplicate_within_promotions",
                "other_id": normalized_to_id[normalized],
            }
        elif normalized in reference_exact:
            exclusions[case["id"]] = {"reason": "exact_duplicate_with_reference"}
        else:
            normalized_to_id[normalized] = case["id"]
            eligible_for_near.append((case["id"], normalized))

    for left, right, score in _near_duplicate_pairs(eligible_for_near, NEAR_DUPLICATE_THRESHOLD):
        if left not in exclusions and right not in exclusions:
            exclusions[right] = {
                "reason": "near_duplicate_within_promotions",
                "other_id": left,
                "score": round(score, 6),
            }
    remaining = [item for item in eligible_for_near if item[0] not in exclusions]
    for case_id, score in _near_duplicates_against_references(
        remaining, references, NEAR_DUPLICATE_THRESHOLD
    ):
        exclusions[case_id] = {
            "reason": "near_duplicate_with_reference",
            "score": round(score, 6),
        }

    candidates = []
    for case, classification, manifest, decision_date in promoted:
        if case["id"] in exclusions:
            continue
        source_class = manifest.get("source_class", "permissive_license")
        candidates.append(
            {
                "id": f"blind-v2-candidate-{len(candidates) + 1:06d}",
                "domain": classification["domain"],
                "risk": classification["risk"],
                "input": normalize_for_dedupe(case["input"]),
                "source": {
                    "class": source_class,
                    "id": manifest["id"],
                    "citation": f"{manifest['attribution']} {manifest['source_urls'][0]}",
                    "license": manifest["output_license"],
                    "license_url": manifest["license_url"],
                    "created_at": decision_date,
                },
                "tags": sorted(
                    set(classification["quality_flags"]) | {"input_only", "maintainer_confirmed"}
                ),
                "notes": classification["notes"],
            }
        )
    pool["cases"] = candidates
    pool["stats"] = _expected_stats(candidates)
    schema_errors = validate_schema(pool, POOL_SCHEMA)
    if schema_errors:
        raise ValueError("invalid generated pool: " + "; ".join(schema_errors))

    report = {
        "decisions": decisions,
        "confirmed_eligible": len(promoted),
        "promoted": len(candidates),
        "excluded_by_dedupe": len(exclusions),
        "exclusions": dict(sorted(exclusions.items())),
        "by_source": dict(sorted(Counter(case["source"]["id"] for case in candidates).items())),
        "reference_snapshot_sha256": snapshot_hash,
    }
    return pool, report


def render_report(report: dict[str, Any], pool: dict[str, Any]) -> str:
    required_domains = {
        "it_api_cli",
        "ui_i18n",
        "llm_generated",
        "formal_news",
        "social_daily",
        "high_stakes",
    }
    missing_domains = sorted(required_domains - set(pool["stats"]["by_domain"]))
    total = pool["stats"]["total"]
    source_limit = pool["source_policy"]["maximum_source_fraction"]
    class_limit = pool["source_policy"]["maximum_source_class_fraction"]
    over_limit_sources = sorted(
        source_id
        for source_id, count in pool["stats"]["by_source"].items()
        if count / total > source_limit
    )
    over_limit_classes = sorted(
        source_class
        for source_class, count in pool["stats"]["by_source_class"].items()
        if count / total > class_limit
    )
    lines = [
        "<!-- zhtw:disable -->",
        f"# Blind-v2 Candidate Promotion ({pool['created_at'][:10]})",
        "",
        "Status: collecting; not ready to freeze or sample",
        "",
        f"- Maintainer-confirmed eligible inputs: {report['confirmed_eligible']}",
        f"- Promoted after exact/near dedupe: {report['promoted']}",
        f"- Excluded by dedupe: {report['excluded_by_dedupe']}",
        f"- Candidate pool total: {pool['stats']['total']}",
        f"- Reference snapshot SHA-256: {report['reference_snapshot_sha256']}",
        "- Converter output and expected text used: no",
        "",
        "## Decisions",
        "",
    ]
    for decision in report["decisions"]:
        lines.append(f"- {decision['path']}: {decision['sha256']}")
    lines.extend(
        [
            "",
            "## Sources",
            "",
        ]
    )
    for source_id, count in report["by_source"].items():
        lines.append(f"- {source_id}: {count}")
    lines.extend(["", "## Dedupe Exclusions", ""])
    if not report["exclusions"]:
        lines.append("None.")
    else:
        for case_id, exclusion in report["exclusions"].items():
            detail = ", ".join(f"{key}={value}" for key, value in exclusion.items())
            lines.append(f"- {case_id}: {detail}")
    lines.extend(
        [
            "",
            "## Collection Gaps",
            "",
            "Final 10% per-source and 35% per-source-class caps are evaluated only when",
            "the pool is frozen or validated with --require-ready. This partial pool is",
            "expected to exceed those final ratios while additional source classes are collected.",
            "It must not be sampled or annotated for expected output yet.",
            f"Minimum-pool gap: {max(0, 3 * pool['formal_n'] - total)}.",
            f"Missing domains: {', '.join(missing_domains) if missing_domains else 'none'}.",
            (
                "Sources currently over the final 10% cap: "
                f"{', '.join(over_limit_sources) if over_limit_sources else 'none'}."
            ),
            (
                "Source classes currently over the final 35% cap: "
                f"{', '.join(over_limit_classes) if over_limit_classes else 'none'}."
            ),
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--decision", action="append", type=Path, required=True)
    parser.add_argument("--created-at", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    pool, report = build_pool(
        [path.resolve() for path in args.decision],
        output=args.output.resolve(),
        created_at=args.created_at,
    )
    content = canonical_json_bytes(pool)
    report_content = render_report(report, pool)
    if args.check:
        stale = not args.output.is_file() or args.output.read_bytes() != content
        stale = stale or not args.report.is_file()
        stale = stale or args.report.read_text(encoding="utf-8") != report_content
        if stale:
            print("Blind-v2 candidate pool or promotion report is stale", file=sys.stderr)
            return 1
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(content)
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(report_content, encoding="utf-8")

    validation_errors = validate_pool(args.output.resolve())
    if validation_errors:
        print("\n".join(validation_errors), file=sys.stderr)
        return 1
    print(
        f"Blind-v2 candidate promotion: {report['promoted']} promoted, "
        f"{report['excluded_by_dedupe']} dedupe exclusions"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
