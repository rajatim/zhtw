#!/usr/bin/env python3
"""Run a public paired vendor-localization benchmark with aggregate output."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from scripts.benchmark_metrics import changed_span_metrics, paired_comparison  # noqa: E402
from scripts.competitor_benchmark import Engine, load_engines, parse_engines  # noqa: E402
from scripts.run_accuracy_benchmark import (  # noqa: E402
    bootstrap_ci,
    build_provenance,
    normalize_output,
    sha256_file,
)
from scripts.validate_benchmark_assets import validate_manifest  # noqa: E402

DEFAULT_LOCK = PROJECT_ROOT / "benchmarks" / "accuracy" / "competitors.lock.json"


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON must be an object")
    return value


def score_engine(dataset: dict[str, Any], engine: Engine) -> tuple[dict[str, Any], list[bool]]:
    if not engine.available or engine.convert is None:
        return {"available": False, "error": engine.error}, []

    exact_values: list[bool] = []
    idempotent_values: list[bool] = []
    by_file_total: Counter[str] = Counter()
    by_file_exact: Counter[str] = Counter()
    errors: Counter[str] = Counter()
    changed_totals: defaultdict[str, int] = defaultdict(int)
    for case in dataset["cases"]:
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
        idempotent = bool(output) and second == output
        exact_values.append(exact)
        idempotent_values.append(idempotent)
        by_file_total[case["file"]] += 1
        if exact:
            by_file_exact[case["file"]] += 1
        changed = changed_span_metrics(case["input"], expected, output)
        for field in ("required_edits", "produced_edits", "correct_edits"):
            changed_totals[field] += int(changed[field])

    total = len(exact_values)
    exact_count = sum(exact_values)
    idempotent_count = sum(idempotent_values)
    precision = (
        changed_totals["correct_edits"] / changed_totals["produced_edits"]
        if changed_totals["produced_edits"]
        else 1.0
    )
    recall = (
        changed_totals["correct_edits"] / changed_totals["required_edits"]
        if changed_totals["required_edits"]
        else 1.0
    )
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return (
        {
            "available": True,
            "version": engine.version,
            "family": engine.family,
            "adapter": engine.adapter,
            "total_cases": total,
            "exact": exact_count,
            "misses": total - exact_count,
            "exact_accuracy": exact_count / total,
            "exact_accuracy_ci_95": bootstrap_ci(exact_values),
            "idempotent": idempotent_count,
            "idempotency_rate": idempotent_count / total,
            "changed_span": {
                **dict(changed_totals),
                "precision": precision,
                "recall": recall,
                "f1": f1,
            },
            "by_file": {
                key: {
                    "total": count,
                    "exact": by_file_exact[key],
                    "exact_accuracy": by_file_exact[key] / count,
                }
                for key, count in sorted(by_file_total.items())
            },
            "errors_by_category": dict(sorted(errors.items())),
        },
        exact_values,
    )


def build_report(
    *,
    manifest_path: Path,
    dataset_path: Path,
    generated_date: str,
    engines: list[Engine],
) -> dict[str, Any]:
    manifest_errors = validate_manifest(manifest_path)
    if manifest_errors:
        raise ValueError("invalid manifest: " + "; ".join(manifest_errors))
    manifest = load_json(manifest_path)
    dataset = load_json(dataset_path)
    if dataset.get("id") != manifest["id"]:
        raise ValueError("dataset id does not match manifest")
    if sha256_file(dataset_path) != manifest["normalized_sha256"]:
        raise ValueError("normalized dataset hash does not match manifest")

    scores: dict[str, Any] = {}
    exact_by_engine: dict[str, list[bool]] = {}
    for engine in engines:
        score, exact = score_engine(dataset, engine)
        scores[engine.name] = score
        if exact:
            exact_by_engine[engine.name] = exact
    if "zhtw" not in exact_by_engine:
        raise ValueError("zhtw engine is unavailable")
    comparisons = {
        name: paired_comparison(exact_by_engine["zhtw"], values)
        for name, values in exact_by_engine.items()
        if name != "zhtw"
    }
    provenance = build_provenance(engines)
    provenance["scorer_sha256"] = sha256_file(Path(__file__))
    return {
        "generated_date": generated_date,
        "report_mode": "aggregate",
        "dataset": manifest["id"],
        "track": manifest["track"],
        "evidence_role": dataset["evidence_role"],
        "primary_market_endpoint": False,
        "reference_kind": dataset["reference_kind"],
        "reference_is_ground_truth": False,
        "source_overlap": dataset["source_overlap"],
        "manifest_sha256": sha256_file(manifest_path),
        "normalized_sha256": sha256_file(dataset_path),
        "upstream_revision": manifest["upstream_revision"],
        "license": manifest["output_license"],
        "provenance": provenance,
        "engines": scores,
        "paired_comparisons": comparisons,
    }


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "<!-- zhtw:disable -->",
        f"# Paired Localization Benchmark: {report['dataset']} ({report['generated_date']})",
        "",
        "Report mode: `aggregate`",
        "",
        "This project-run public track compares converter output with a vendor's paired",
        "Traditional localization. The vendor translation is a useful reference, not",
        "universal Taiwan Traditional ground truth. This track cannot replace Blind-v2.",
        "",
    ]
    if report["source_overlap"] == "blind_v2_source_pool":
        lines.extend(
            [
                "The Simplified source overlaps the Blind-v2 source pool. Treat this as a",
                "diagnostic track, not fresh independent evidence for the primary claim.",
                "",
            ]
        )
    lines.extend(
        [
            "| Engine | Exact | Accuracy | Idempotency | Changed-span F1 |",
            "|---|---:|---:|---:|---:|",
        ]
    )
    for name, score in report["engines"].items():
        if not score["available"]:
            lines.append(f"| {name} | unavailable | - | - | - |")
            continue
        lines.append(
            f"| {name} {score['version'] or ''} | {score['exact']} / {score['total_cases']} "
            f"| {score['exact_accuracy']:.6f} | {score['idempotency_rate']:.6f} "
            f"| {score['changed_span']['f1']:.6f} |"
        )
    if report["paired_comparisons"]:
        lines.extend(["", "## Paired Comparisons", ""])
        for name, comparison in report["paired_comparisons"].items():
            ci = comparison["delta_ci_95"]
            lines.append(
                f"- zhtw vs `{name}`: {comparison['absolute_delta']:+.6f}; 95% CI "
                f"{ci['low']:+.6f} to {ci['high']:+.6f}; {comparison['result']}."
            )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--dataset", type=Path)
    parser.add_argument("--output-prefix", type=Path, required=True)
    parser.add_argument("--generated-date", default=dt.date.today().isoformat())
    parser.add_argument("--engines", type=parse_engines, default=["zhtw"])
    parser.add_argument("--lock", type=Path, default=DEFAULT_LOCK)
    parser.add_argument("--container-image")
    args = parser.parse_args()

    manifest = load_json(args.manifest)
    dataset_path = args.dataset or PROJECT_ROOT / manifest["normalized_path"]
    lock = load_json(args.lock) if args.container_image else None
    engines = load_engines(args.engines, lock=lock, container_image=args.container_image)
    report = build_report(
        manifest_path=args.manifest,
        dataset_path=dataset_path,
        generated_date=args.generated_date,
        engines=engines,
    )
    args.output_prefix.parent.mkdir(parents=True, exist_ok=True)
    args.output_prefix.with_suffix(".json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    args.output_prefix.with_suffix(".md").write_text(render_markdown(report), encoding="utf-8")
    print(f"{report['dataset']}: {report['engines']['zhtw']['exact']} exact")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
