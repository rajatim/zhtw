#!/usr/bin/env python3
"""Run the public UD GSD/GSDSimp secondary benchmark track."""

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

from scripts.benchmark_metrics import changed_span_metrics  # noqa: E402
from scripts.competitor_benchmark import load_zhtw  # noqa: E402
from scripts.run_accuracy_benchmark import (  # noqa: E402
    bootstrap_ci,
    build_provenance,
    normalize_output,
    sha256_file,
)
from scripts.validate_benchmark_assets import validate_manifest  # noqa: E402

DEFAULT_MANIFEST = PROJECT_ROOT / "benchmarks" / "accuracy" / "manifests" / "ud-gsd-v1.json"
DEFAULT_DATASET = PROJECT_ROOT / "benchmarks" / "accuracy" / "external" / "ud-gsd-v1.json"
DEFAULT_OUTPUT_PREFIX = PROJECT_ROOT / "docs" / "reports" / "ud-gsd-benchmark"


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
    by_split_total: Counter[str] = Counter()
    by_split_exact: Counter[str] = Counter()
    by_genre_total: Counter[str] = Counter()
    by_genre_exact: Counter[str] = Counter()
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
        idempotent = second == output and bool(output)
        exact_values.append(exact)
        idempotent_values.append(idempotent)
        by_split_total[case["split"]] += 1
        by_genre_total[case["genre"]] += 1
        if exact:
            by_split_exact[case["split"]] += 1
            by_genre_exact[case["genre"]] += 1
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

    def grouped(
        totals: Counter[str], exact_counts: Counter[str]
    ) -> dict[str, dict[str, float | int]]:
        return {
            key: {
                "total": count,
                "exact": exact_counts[key],
                "exact_accuracy": exact_counts[key] / count,
            }
            for key, count in sorted(totals.items())
        }

    return {
        "total_cases": total,
        "exact": exact_count,
        "misses": total - exact_count,
        "exact_accuracy": exact_count / total if total else 0.0,
        "exact_accuracy_ci_95": bootstrap_ci(exact_values),
        "idempotent": idempotent_count,
        "idempotency_rate": idempotent_count / total if total else 0.0,
        "changed_span": {
            **dict(changed_totals),
            "precision": precision,
            "recall": recall,
            "f1": f1,
        },
        "by_split": grouped(by_split_total, by_split_exact),
        "by_genre": grouped(by_genre_total, by_genre_exact),
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
        "source_bias": dataset["source_bias"],
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
        f"# UD GSD Accuracy Benchmark ({report['generated_date']})",
        "",
        "Report mode: `aggregate`",
        "",
        "This is public secondary evidence, not the Blind-v2 primary market endpoint.",
        "GSDSimp was initially converted with OpenCC and later manually corrected, so the",
        "track is not independent evidence against OpenCC-family converters.",
        "",
        f"- Cases: {scores['total_cases']}",
        f"- Exact: {scores['exact']} / {scores['total_cases']}",
        f"- Exact accuracy: {scores['exact_accuracy']:.6f}",
        f"- Idempotency rate: {scores['idempotency_rate']:.6f}",
        f"- Changed-span precision: {scores['changed_span']['precision']:.6f}",
        f"- Changed-span recall: {scores['changed_span']['recall']:.6f}",
        f"- Changed-span F1: {scores['changed_span']['f1']:.6f}",
        "",
        "## Split Results",
        "",
    ]
    for split, values in scores["by_split"].items():
        lines.append(
            f"- `{split}`: {values['exact']} / {values['total']} ({values['exact_accuracy']:.6f})"
        )
    lines.extend(["", "## Genre Results", ""])
    for genre, values in scores["by_genre"].items():
        lines.append(
            f"- `{genre}`: {values['exact']} / {values['total']} ({values['exact_accuracy']:.6f})"
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
    print(f"UD exact: {scores['exact']}/{scores['total_cases']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
