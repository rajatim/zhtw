#!/usr/bin/env python3
"""Discover report-only differences between zhtw and optional competitors.

The input is the curated corpus under tests/data/corpus. When a corpus case has
an expected output, classification is correctness-aware. Competitor agreement is
only a structural signal for cases without an expected output.

Usage:
    uv run python scripts/discover_competitor_diffs.py --limit 300
    uv run --with opencc-python-reimplemented --with zhconv \
        python scripts/discover_competitor_diffs.py --limit 300
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from competitor_benchmark import Engine, load_engines, parse_engines  # noqa: E402

CORPUS_DIR = PROJECT_ROOT / "tests" / "data" / "corpus"
REPORTS_DIR = PROJECT_ROOT / "docs" / "reports"
CURATED_CATEGORIES = ("news", "regressions", "social", "tech", "wiki")


@dataclass(frozen=True)
class CorpusCase:
    id: str
    category: str
    source_file: Path
    input: str
    expected: str | None
    tags: tuple[str, ...]
    notes: str


def parse_categories(raw: str) -> list[str]:
    if raw == "all":
        return list(CURATED_CATEGORIES)
    categories = [category.strip() for category in raw.split(",") if category.strip()]
    invalid = sorted(set(categories) - set(CURATED_CATEGORIES))
    if not categories or invalid:
        valid = ",".join(("all", *CURATED_CATEGORIES))
        raise argparse.ArgumentTypeError(f"category must be comma-separated from {valid}")
    return categories


def rel_path(path: Path) -> str:
    try:
        return str(path.relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path)


def corpus_files(corpus_dir: Path, categories: list[str]) -> list[Path]:
    files: list[Path] = []
    for category in categories:
        files.extend((corpus_dir / category).glob("*.json"))
    return sorted(files)


def load_corpus_cases(corpus_dir: Path, categories: list[str]) -> list[CorpusCase]:
    cases: list[CorpusCase] = []
    for path in corpus_files(corpus_dir, categories):
        data = json.loads(path.read_text(encoding="utf-8"))
        category = path.parent.name
        for index, raw in enumerate(data.get("corpus", []), start=1):
            text = raw.get("input")
            if not isinstance(text, str) or not text:
                continue
            raw_tags = raw.get("tags", [])
            tags = tuple(str(tag) for tag in raw_tags) if isinstance(raw_tags, list) else ()
            case_id = str(raw.get("id") or f"{path.stem}-{index:04d}")
            expected = raw.get("expected")
            cases.append(
                CorpusCase(
                    id=case_id,
                    category=category,
                    source_file=path,
                    input=text,
                    expected=expected if isinstance(expected, str) else None,
                    tags=tags,
                    notes=str(raw.get("notes", "")),
                )
            )
    return cases


def select_cases(cases: list[CorpusCase], limit: int, seed: int | None) -> list[CorpusCase]:
    selected = list(cases)
    if seed is not None:
        random.Random(seed).shuffle(selected)
    if limit >= 0:
        selected = selected[:limit]
    return selected


def engine_metadata(engines: list[Engine]) -> dict[str, dict[str, Any]]:
    return {
        engine.name: {
            "available": engine.available,
            "version": engine.version,
            "error": engine.error,
        }
        for engine in engines
    }


def available_engine_versions(engines: list[Engine]) -> dict[str, str | None]:
    return {engine.name: engine.version for engine in engines if engine.available}


def collect_outputs(
    case: CorpusCase,
    engines: list[Engine],
) -> tuple[dict[str, str], dict[str, str]]:
    outputs: dict[str, str] = {}
    errors: dict[str, str] = {}
    for engine in engines:
        if not engine.available or engine.convert is None:
            continue
        try:
            outputs[engine.name] = engine.convert(case.input)
        except Exception as exc:
            errors[engine.name] = str(exc)
    return outputs, errors


def classify_with_expected(expected: str, outputs: dict[str, str]) -> str:
    zhtw_output = outputs.get("zhtw")
    competitor_outputs = {name: output for name, output in outputs.items() if name != "zhtw"}

    if zhtw_output == expected:
        if not competitor_outputs:
            return "zhtw_only"
        if all(output == expected for output in competitor_outputs.values()):
            return "all_match"
        return "zhtw_advantage"

    if any(output == expected for output in competitor_outputs.values()):
        return "candidate_gap"
    return "all_wrong"


def classify_without_expected(outputs: dict[str, str]) -> str:
    if len(outputs) < 2:
        return "zhtw_only"

    output_groups: dict[str, list[str]] = defaultdict(list)
    for engine, output in outputs.items():
        output_groups[output].append(engine)

    if len(output_groups) == 1:
        return "no_difference"

    if len(outputs) >= 3 and all(len(engines) == 1 for engines in output_groups.values()):
        return "all_different"

    zhtw_output = outputs.get("zhtw")
    opencc_output = outputs.get("opencc-s2twp")
    zhconv_output = outputs.get("zhconv-zh-tw")
    if (
        opencc_output is not None
        and opencc_output == zhconv_output
        and zhtw_output != opencc_output
    ):
        return "competitors_agree"

    for engine, output in outputs.items():
        if len(output_groups[output]) == 1:
            if engine == "zhtw":
                return "zhtw_unique"
            if engine == "opencc-s2twp":
                return "opencc_unique"
            if engine == "zhconv-zh-tw":
                return "zhconv_unique"

    return "partial_difference"


def classify_case(case: CorpusCase, outputs: dict[str, str]) -> str:
    if case.expected is not None:
        return classify_with_expected(case.expected, outputs)
    return classify_without_expected(outputs)


def should_emit(case: CorpusCase, outputs: dict[str, str], classification: str) -> bool:
    if len(set(outputs.values())) > 1:
        return True
    if case.expected is not None and outputs.get("zhtw") != case.expected:
        return True
    return classification in {"candidate_gap", "all_wrong"}


def run_cases(
    cases: list[CorpusCase],
    engines: list[Engine],
    sample_seed: int | None,
) -> list[dict[str, Any]]:
    rows, _scanned_summary = scan_cases(cases, engines, sample_seed)
    return rows


def scan_cases(
    cases: list[CorpusCase],
    engines: list[Engine],
    sample_seed: int | None,
) -> tuple[list[dict[str, Any]], Counter[str]]:
    rows: list[dict[str, Any]] = []
    scanned_summary: Counter[str] = Counter()
    versions = available_engine_versions(engines)

    for case in cases:
        outputs, errors = collect_outputs(case, engines)
        classification = classify_case(case, outputs)
        scanned_summary[classification] += 1
        if not should_emit(case, outputs, classification):
            continue

        rows.append(
            {
                "id": f"{case.category}/{case.id}",
                "category": case.category,
                "source_file": rel_path(case.source_file),
                "case_id": case.id,
                "sample_seed": sample_seed,
                "input": case.input,
                "corpus_expected": case.expected,
                "outputs": outputs,
                "errors": errors,
                "engine_versions": versions,
                "classification": classification,
                "review": "pending",
                "expected": None,
                "decision": None,
                "tags": list(case.tags),
                "notes": case.notes,
            }
        )

    return rows, scanned_summary


def summarize(rows: list[dict[str, Any]]) -> Counter[str]:
    return Counter(row["classification"] for row in rows)


def build_payload(
    corpus_dir: Path,
    categories: list[str],
    total_cases: int,
    selected_cases: list[CorpusCase],
    engines: list[Engine],
    rows: list[dict[str, Any]],
    scanned_summary: Counter[str],
    limit: int,
    seed: int | None,
) -> dict[str, Any]:
    with_expected = sum(1 for case in selected_cases if case.expected is not None)
    return {
        "generated_date": date.today().isoformat(),
        "corpus_dir": rel_path(corpus_dir),
        "categories": categories,
        "limit": limit,
        "sample_seed": seed,
        "total_cases": total_cases,
        "scanned_cases": len(selected_cases),
        "cases_with_expected": with_expected,
        "diff_rows": len(rows),
        "engines": engine_metadata(engines),
        "scanned_summary": dict(sorted(scanned_summary.items())),
        "diff_summary": dict(sorted(summarize(rows).items())),
        "summary": dict(sorted(summarize(rows).items())),
        "rows": rows,
    }


def format_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "<!-- zhtw:disable -->",
        f"# 競品差異探索報告（{payload['generated_date']}）",
        "",
        "## 摘要",
        "",
        f"- Corpus：`{payload['corpus_dir']}`",
        f"- Categories：{', '.join(payload['categories'])}",
        f"- 掃描 case：{payload['scanned_cases']} / {payload['total_cases']}",
        f"- 含 expected：{payload['cases_with_expected']}",
        f"- 輸出差異 rows：{payload['diff_rows']}",
        f"- Seed：{payload['sample_seed']}",
        "",
        "## Engines",
        "",
        "| Engine | Version | Status |",
        "|--------|---------|--------|",
    ]

    for name, engine in payload["engines"].items():
        status = "available" if engine["available"] else f"skipped: {engine['error']}"
        lines.append(f"| `{name}` | {engine['version'] or ''} | {status} |")

    lines.extend(
        ["", "## Scanned Summary", "", "| Classification | Count |", "|----------------|-------|"]
    )
    for key, count in payload["scanned_summary"].items():
        lines.append(f"| `{key}` | {count} |")

    lines.extend(
        ["", "## Diff Row Summary", "", "| Classification | Count |", "|----------------|-------|"]
    )
    for key, count in payload["diff_summary"].items():
        lines.append(f"| `{key}` | {count} |")

    lines.extend(["", "## Rows", ""])
    if not payload["rows"]:
        lines.append("沒有輸出差異 rows。")
        return "\n".join(lines) + "\n"

    for row in payload["rows"]:
        lines.extend(
            [
                f"### {row['id']} — `{row['classification']}`",
                "",
                f"- Source：`{row['source_file']}`",
                f"- Corpus expected：{row['corpus_expected']}",
                f"- Review：{row['review']}",
                f"- Notes：{row['notes']}",
                "",
                "| Engine | Output |",
                "|--------|--------|",
            ]
        )
        for engine, output in row["outputs"].items():
            lines.append(f"| `{engine}` | {output} |")
        if row["errors"]:
            lines.extend(["", "Errors:"])
            for engine, error in row["errors"].items():
                lines.append(f"- `{engine}`: {error}")
        lines.append("")

    return "\n".join(lines)


def output_path(fmt: str, explicit: Path | None) -> Path:
    if explicit is not None:
        return explicit
    suffix = "json" if fmt == "json" else "md"
    return REPORTS_DIR / f"competitor-diffs-{date.today().isoformat()}.{suffix}"


def write_report(payload: dict[str, Any], fmt: str, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fmt == "json":
        text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    else:
        text = format_markdown(payload)
    path.write_text(text, encoding="utf-8")


def print_summary(payload: dict[str, Any], path: Path) -> None:
    print(f"wrote {path}")
    print(f"scanned_cases: {payload['scanned_cases']}")
    print(f"cases_with_expected: {payload['cases_with_expected']}")
    print(f"diff_rows: {payload['diff_rows']}")
    print("scanned_summary:")
    for key, count in payload["scanned_summary"].items():
        print(f"  {key}: {count}")
    print("diff_summary:")
    for key, count in payload["diff_summary"].items():
        print(f"  {key}: {count}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus-dir", type=Path, default=CORPUS_DIR)
    parser.add_argument(
        "--category",
        type=parse_categories,
        default=parse_categories("all"),
        help="Comma-separated corpus categories or all. Default: all",
    )
    parser.add_argument("--limit", type=int, default=300, help="Cases to scan. Use -1 for all.")
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Sample seed. Use -1 to disable shuffle.",
    )
    parser.add_argument(
        "--engines",
        type=parse_engines,
        default=parse_engines("zhtw,opencc-s2twp,zhconv-zh-tw"),
        help="Comma-separated engines. Default: zhtw,opencc-s2twp,zhconv-zh-tw",
    )
    parser.add_argument("--format", choices=("json", "md"), default="md")
    parser.add_argument("--output", type=Path, help="Report output path.")
    args = parser.parse_args()

    seed = None if args.seed < 0 else args.seed
    cases = load_corpus_cases(args.corpus_dir, args.category)
    selected_cases = select_cases(cases, args.limit, seed)
    engines = load_engines(args.engines)
    rows, scanned_summary = scan_cases(selected_cases, engines, sample_seed=seed)
    payload = build_payload(
        corpus_dir=args.corpus_dir,
        categories=args.category,
        total_cases=len(cases),
        selected_cases=selected_cases,
        engines=engines,
        rows=rows,
        scanned_summary=scanned_summary,
        limit=args.limit,
        seed=seed,
    )

    path = output_path(args.format, args.output)
    write_report(payload, args.format, path)
    print_summary(payload, path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
