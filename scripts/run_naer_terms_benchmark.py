#!/usr/bin/env python3
"""Run the public NAER computer terminology secondary benchmark track."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from scripts.competitor_benchmark import load_zhtw  # noqa: E402
from scripts.run_accuracy_benchmark import (  # noqa: E402
    bootstrap_ci,
    build_provenance,
    normalize_output,
    sha256_file,
)
from scripts.validate_benchmark_assets import validate_manifest  # noqa: E402

DEFAULT_MANIFEST = PROJECT_ROOT / "benchmarks" / "accuracy" / "manifests" / "naer-terms-v1.json"
DEFAULT_DATASET = PROJECT_ROOT / "benchmarks" / "accuracy" / "external" / "naer-terms-v1.json"
DEFAULT_OUTPUT_PREFIX = PROJECT_ROOT / "docs" / "reports" / "naer-terms-benchmark"


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON must be an object")
    return value


def score_dataset(dataset: dict[str, Any]) -> dict[str, Any]:
    engine = load_zhtw()
    if not engine.available or engine.convert is None:
        raise ValueError("zhtw engine is unavailable")

    exact_values: list[bool] = []
    idempotent_values: list[bool] = []
    by_kind_total: Counter[str] = Counter()
    by_kind_exact: Counter[str] = Counter()
    exact_by_kind: dict[str, list[bool]] = {}
    errors: Counter[str] = Counter()
    for case in dataset["evaluation_cases"]:
        try:
            output = normalize_output(engine.convert(case["input"]))
            second = normalize_output(engine.convert(output))
        except Exception:
            output = ""
            second = ""
            errors["exception"] += 1
        if not output:
            errors["empty_output"] += 1
        expected = normalize_output(case["expected"])
        exact = output == expected
        exact_values.append(exact)
        idempotent_values.append(bool(output) and second == output)
        by_kind_total[case["kind"]] += 1
        exact_by_kind.setdefault(case["kind"], []).append(exact)
        if exact:
            by_kind_exact[case["kind"]] += 1

    total = len(exact_values)
    exact_count = sum(exact_values)
    by_kind = {
        kind: {
            "total": count,
            "exact": by_kind_exact[kind],
            "exact_accuracy": by_kind_exact[kind] / count,
            "exact_accuracy_ci_95": bootstrap_ci(exact_by_kind[kind]),
        }
        for kind, count in sorted(by_kind_total.items())
    }
    macro = sum(item["exact_accuracy"] for item in by_kind.values()) / len(by_kind)
    return {
        "total_cases": total,
        "exact": exact_count,
        "misses": total - exact_count,
        "accepted_accuracy": exact_count / total,
        "primary_exact_accuracy": exact_count / total,
        "micro_accuracy": exact_count / total,
        "micro_accuracy_ci_95": bootstrap_ci(exact_values),
        "macro_domain_accuracy": exact_count / total,
        "macro_candidate_set_accuracy": macro,
        "idempotent": sum(idempotent_values),
        "idempotency_rate": sum(idempotent_values) / total,
        "conversion_recall": by_kind["conversion"]["exact_accuracy"],
        "identity_guard_accuracy": by_kind["identity_guard"]["exact_accuracy"],
        "over_conversion_guard_accuracy": by_kind["identity_guard"]["exact_accuracy"],
        "by_candidate_set": by_kind,
        "excluded_context_candidates": dataset["stats"]["context_candidates"],
        "severe_error_assessment": "not_available_without_human_sentence_context",
        "errors_by_category": dict(sorted(errors.items())),
    }


def build_report(*, manifest_path: Path, dataset_path: Path, generated_date: str) -> dict[str, Any]:
    manifest_errors = validate_manifest(manifest_path)
    if manifest_errors:
        raise ValueError("invalid manifest: " + "; ".join(manifest_errors))
    manifest = load_json(manifest_path)
    dataset = load_json(dataset_path)
    if dataset.get("id") != manifest["id"]:
        raise ValueError("dataset id does not match manifest")
    if sha256_file(dataset_path) != manifest["normalized_sha256"]:
        raise ValueError("normalized dataset hash does not match manifest")
    engine = load_zhtw()
    provenance = build_provenance([engine])
    provenance["scorer_sha256"] = sha256_file(Path(__file__))
    return {
        "generated_date": generated_date,
        "report_mode": "aggregate",
        "dataset": manifest["id"],
        "track": manifest["track"],
        "evidence_role": "secondary_evidence",
        "primary_market_endpoint": False,
        "manifest_sha256": sha256_file(manifest_path),
        "normalized_sha256": sha256_file(dataset_path),
        "upstream_revision": manifest["upstream_revision"],
        "license": manifest["output_license"],
        "provenance": provenance,
        "scores": score_dataset(dataset),
    }


def render_markdown(report: dict[str, Any]) -> str:
    scores = report["scores"]
    lines = [
        "<!-- zhtw:disable -->",
        f"# NAER Terminology Benchmark ({report['generated_date']})",
        "",
        "Report mode: `aggregate`",
        "",
        "This public terminology track is secondary evidence, not the Blind-v2 primary",
        "market endpoint. It measures a conservative subset of NAER computer terms;",
        "compound, conflicting, and otherwise ambiguous bare terms are excluded pending",
        "human-confirmed sentence context.",
        "",
        f"- Evaluated cases: {scores['total_cases']}",
        f"- Excluded context candidates: {scores['excluded_context_candidates']}",
        f"- Micro accuracy: {scores['micro_accuracy']:.6f}",
        f"- Macro domain accuracy: {scores['macro_domain_accuracy']:.6f}",
        f"- Macro candidate-set accuracy: {scores['macro_candidate_set_accuracy']:.6f}",
        f"- Conversion recall: {scores['conversion_recall']:.6f}",
        f"- Identity guard accuracy: {scores['identity_guard_accuracy']:.6f}",
        f"- Idempotency rate: {scores['idempotency_rate']:.6f}",
        "",
        "## Candidate Sets",
        "",
    ]
    for kind, values in scores["by_candidate_set"].items():
        lines.append(
            f"- `{kind}`: {values['exact']} / {values['total']} ({values['exact_accuracy']:.6f})"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--dataset", type=Path, default=DEFAULT_DATASET)
    parser.add_argument("--output-prefix", type=Path, default=DEFAULT_OUTPUT_PREFIX)
    parser.add_argument("--generated-date", default=dt.date.today().isoformat())
    args = parser.parse_args()
    report = build_report(
        manifest_path=args.manifest,
        dataset_path=args.dataset,
        generated_date=args.generated_date,
    )
    args.output_prefix.parent.mkdir(parents=True, exist_ok=True)
    args.output_prefix.with_suffix(".json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    args.output_prefix.with_suffix(".md").write_text(render_markdown(report), encoding="utf-8")
    scores = report["scores"]
    print(f"NAER exact: {scores['exact']}/{scores['total_cases']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
