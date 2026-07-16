#!/usr/bin/env python3
"""Run a sealed-holdout accuracy benchmark against locked converters."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import random
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from scripts.competitor_benchmark import ENGINE_LOADERS, Engine, load_engines  # noqa: E402

DEFAULT_INPUTS = PROJECT_ROOT / "benchmarks" / "accuracy" / "blind-v1.inputs.json"
DEFAULT_EXPECTED = PROJECT_ROOT / "benchmarks" / "accuracy" / "blind-v1.expected.json"
DEFAULT_LOCK = PROJECT_ROOT / "benchmarks" / "accuracy" / "competitors.lock.json"
DEFAULT_OUTPUT_PREFIX = PROJECT_ROOT / "docs" / "reports" / "accuracy-benchmark"
DEFAULT_COMPETITORS = "zhtw"
NORMALIZATION_RULES = [
    "Unicode NFC",
    "CRLF and CR become LF",
    "remove one CLI trailing newline only",
    "do not normalize punctuation, internal spaces, or regional synonyms",
]


@dataclass(frozen=True)
class InputCase:
    id: str
    batch: str
    domain: str
    input: str
    risk: str
    tags: list[str]
    notes: str


@dataclass(frozen=True)
class ExpectedCase:
    id: str
    expected: str
    acceptable: list[str]
    issue_tags: list[str]
    annotation: dict[str, Any]


def relative_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_input_cases(path: Path) -> tuple[dict[str, Any], list[InputCase]]:
    data = load_json(path)
    cases: list[InputCase] = []
    forbidden = {"expected", "acceptable", "review", "annotation"}
    for index, raw in enumerate(data.get("cases", []), start=1):
        leaked = sorted(forbidden & set(raw))
        if leaked:
            raise ValueError(f"input case #{index} leaks expected fields: {', '.join(leaked)}")
        missing = sorted({"id", "batch", "domain", "input", "risk", "tags", "notes"} - set(raw))
        if missing:
            raise ValueError(f"input case #{index} missing required fields: {', '.join(missing)}")
        cases.append(
            InputCase(
                id=str(raw["id"]),
                batch=str(raw["batch"]),
                domain=str(raw["domain"]),
                input=str(raw["input"]),
                risk=str(raw["risk"]),
                tags=[str(tag) for tag in raw.get("tags", [])],
                notes=str(raw.get("notes", "")),
            )
        )
    if not cases:
        raise ValueError(f"no input cases found in {path}")
    assert_unique_ids(cases, "input")
    return data, cases


def load_expected_cases(path: Path) -> tuple[dict[str, Any], list[ExpectedCase]]:
    data = load_json(path)
    cases: list[ExpectedCase] = []
    for index, raw in enumerate(data.get("cases", []), start=1):
        missing = sorted({"id", "expected", "acceptable", "annotation", "issue_tags"} - set(raw))
        if missing:
            missing_fields = ", ".join(missing)
            raise ValueError(f"expected case #{index} missing required fields: {missing_fields}")
        cases.append(
            ExpectedCase(
                id=str(raw["id"]),
                expected=str(raw["expected"]),
                acceptable=[str(item) for item in raw.get("acceptable", [])],
                issue_tags=[str(item) for item in raw.get("issue_tags", [])],
                annotation=dict(raw.get("annotation", {})),
            )
        )
    if not cases:
        raise ValueError(f"no expected cases found in {path}")
    assert_unique_ids(cases, "expected")
    return data, cases


def assert_unique_ids(cases: list[InputCase] | list[ExpectedCase], label: str) -> None:
    counts = Counter(case.id for case in cases)
    duplicates = sorted(case_id for case_id, count in counts.items() if count > 1)
    if duplicates:
        raise ValueError(f"duplicate {label} case ids: {duplicates}")


def assert_expected_matches_inputs(inputs: list[InputCase], expected: list[ExpectedCase]) -> None:
    input_ids = {case.id for case in inputs}
    expected_ids = {case.id for case in expected}
    missing = sorted(input_ids - expected_ids)
    extra = sorted(expected_ids - input_ids)
    if missing or extra:
        parts = []
        if missing:
            parts.append(f"missing expected ids: {missing[:20]}")
        if extra:
            parts.append(f"extra expected ids: {extra[:20]}")
        raise ValueError("; ".join(parts))


def assert_expected_source_hash(input_path: Path, expected_data: dict[str, Any]) -> None:
    expected_hash = str(expected_data.get("source_inputs_sha256", ""))
    actual_hash = sha256_file(input_path)
    if expected_hash != actual_hash:
        raise ValueError(
            "expected source_inputs_sha256 does not match inputs file: "
            f"expected={expected_hash} actual={actual_hash}"
        )


def load_lockfile(path: Path) -> dict[str, Any]:
    lock = load_json(path)
    ids = [item["id"] for item in lock.get("competitors", [])]
    duplicates = sorted(name for name, count in Counter(ids).items() if count > 1)
    if duplicates:
        raise ValueError(f"duplicate competitors in lockfile: {duplicates}")
    return lock


def parse_competitors(raw: str) -> list[str]:
    competitors = [name.strip() for name in raw.split(",") if name.strip()]
    invalid = sorted(set(competitors) - set(ENGINE_LOADERS))
    if not competitors or invalid:
        valid = ",".join(sorted(ENGINE_LOADERS))
        raise argparse.ArgumentTypeError(f"competitors must be comma-separated from {valid}")
    if "zhtw" not in competitors:
        raise argparse.ArgumentTypeError("competitors must include zhtw")
    return competitors


def assert_competitors_locked(competitors: list[str], lock: dict[str, Any]) -> None:
    locked = {item["id"] for item in lock.get("competitors", [])}
    missing = sorted(set(competitors) - locked)
    if missing:
        raise ValueError(f"requested competitors missing from lockfile: {missing}")


def normalize_output(text: str) -> str:
    normalized = unicodedata.normalize("NFC", text).replace("\r\n", "\n").replace("\r", "\n")
    if normalized.endswith("\n"):
        normalized = normalized[:-1]
    return normalized


def evaluate_output(
    engine: Engine,
    case: InputCase,
    expected: ExpectedCase,
) -> dict[str, Any]:
    if not engine.available or engine.convert is None:
        return {
            "available": False,
            "error": engine.error or "engine unavailable",
            "output": "",
            "normalized_output": "",
            "primary_exact": False,
            "acceptable_exact": False,
            "accepted": False,
            "idempotent": False,
        }

    try:
        output = engine.convert(case.input)
        output_after_convert = engine.convert(output)
    except Exception as exc:
        return {
            "available": True,
            "error": str(exc),
            "output": "",
            "normalized_output": "",
            "primary_exact": False,
            "acceptable_exact": False,
            "accepted": False,
            "idempotent": False,
        }

    normalized_output = normalize_output(output)
    normalized_expected = normalize_output(expected.expected)
    normalized_acceptable = {normalize_output(item) for item in expected.acceptable}
    primary_exact = normalized_output == normalized_expected
    acceptable_exact = normalized_output in normalized_acceptable

    return {
        "available": True,
        "error": "",
        "output": output,
        "normalized_output": normalized_output,
        "primary_exact": primary_exact,
        "acceptable_exact": acceptable_exact and not primary_exact,
        "accepted": primary_exact or acceptable_exact,
        "idempotent": normalize_output(output_after_convert) == normalized_output,
    }


def bootstrap_ci(
    values: list[bool],
    *,
    rounds: int = 1000,
    seed: int = 20260707,
) -> dict[str, float]:
    if not values:
        return {"low": 0.0, "high": 0.0}
    rng = random.Random(seed)
    size = len(values)
    means = []
    for _ in range(rounds):
        sample = [values[rng.randrange(size)] for _ in range(size)]
        means.append(sum(sample) / size)
    means.sort()
    low_index = int(0.025 * (rounds - 1))
    high_index = int(0.975 * (rounds - 1))
    return {"low": means[low_index], "high": means[high_index]}


def summarize_engine(rows: list[dict[str, Any]], engine_name: str) -> dict[str, Any]:
    evaluations = [row["evaluations"][engine_name] for row in rows]
    available = [item for item in evaluations if item["available"]]
    total = len(evaluations)
    accepted_values = [bool(item["accepted"]) for item in available]
    primary_values = [bool(item["primary_exact"]) for item in available]
    idempotent_values = [bool(item["idempotent"]) for item in available]

    by_domain: dict[str, dict[str, Any]] = {}
    domain_totals: defaultdict[str, int] = defaultdict(int)
    domain_accepted: defaultdict[str, int] = defaultdict(int)
    issue_miss_counts: Counter[str] = Counter()
    risk_miss_counts: Counter[str] = Counter()
    for row in rows:
        evaluation = row["evaluations"][engine_name]
        if not evaluation["available"]:
            continue
        domain_totals[row["domain"]] += 1
        if evaluation["accepted"]:
            domain_accepted[row["domain"]] += 1
        else:
            risk_miss_counts[row["risk"]] += 1
            issue_miss_counts.update(row["issue_tags"] or ["other"])

    for domain, count in sorted(domain_totals.items()):
        accepted = domain_accepted[domain]
        by_domain[domain] = {
            "total": count,
            "accepted": accepted,
            "accepted_accuracy": accepted / count if count else 0.0,
        }

    accepted = sum(accepted_values)
    primary_exact = sum(primary_values)
    idempotent = sum(idempotent_values)
    available_count = len(available)
    return {
        "total_cases": total,
        "available_cases": available_count,
        "unavailable_cases": total - available_count,
        "accepted": accepted,
        "misses": available_count - accepted,
        "primary_exact": primary_exact,
        "acceptable_exact": sum(item["acceptable_exact"] for item in available),
        "idempotent": idempotent,
        "accepted_accuracy": accepted / available_count if available_count else 0.0,
        "primary_exact_accuracy": primary_exact / available_count if available_count else 0.0,
        "idempotency_rate": idempotent / available_count if available_count else 0.0,
        "accepted_accuracy_ci_95": bootstrap_ci(accepted_values),
        "by_domain": by_domain,
        "misses_by_risk": dict(sorted(risk_miss_counts.items())),
        "misses_by_issue_tag": dict(sorted(issue_miss_counts.items())),
    }


def build_rows(
    inputs: list[InputCase],
    expected: list[ExpectedCase],
    engines: list[Engine],
) -> list[dict[str, Any]]:
    expected_by_id = {case.id: case for case in expected}
    rows: list[dict[str, Any]] = []
    for case in inputs:
        expected_case = expected_by_id[case.id]
        evaluations = {
            engine.name: evaluate_output(engine, case, expected_case) for engine in engines
        }
        rows.append(
            {
                "id": case.id,
                "batch": case.batch,
                "domain": case.domain,
                "risk": case.risk,
                "tags": case.tags,
                "input": case.input,
                "expected": expected_case.expected,
                "acceptable": expected_case.acceptable,
                "issue_tags": expected_case.issue_tags,
                "annotation": expected_case.annotation,
                "evaluations": evaluations,
            }
        )
    return rows


def build_report(
    *,
    generated_date: str,
    inputs_path: Path,
    expected_path: Path,
    lock_path: Path,
    input_data: dict[str, Any],
    expected_data: dict[str, Any],
    lock: dict[str, Any],
    inputs: list[InputCase],
    engines: list[Engine],
    rows: list[dict[str, Any]],
) -> dict[str, Any]:
    by_domain = Counter(case.domain for case in inputs)
    by_risk = Counter(case.risk for case in inputs)
    engine_meta = {
        engine.name: {
            "available": engine.available,
            "version": engine.version,
            "error": engine.error,
            "scores": summarize_engine(rows, engine.name),
        }
        for engine in engines
    }
    return {
        "generated_date": generated_date,
        "dataset": input_data.get("dataset", ""),
        "inputs": {
            "path": relative_path(inputs_path),
            "sha256": sha256_file(inputs_path),
            "name": input_data.get("name", ""),
            "status": input_data.get("status", ""),
            "publish_state": input_data.get("publish_state", ""),
        },
        "expected": {
            "path": relative_path(expected_path),
            "sha256": sha256_file(expected_path),
            "name": expected_data.get("name", ""),
            "status": expected_data.get("status", ""),
            "source_inputs": expected_data.get("source_inputs", ""),
            "source_inputs_sha256": expected_data.get("source_inputs_sha256", ""),
        },
        "competitors_lock": {
            "path": relative_path(lock_path),
            "sha256": sha256_file(lock_path),
            "status": lock.get("status", ""),
            "competitors": lock.get("competitors", []),
        },
        "normalization": NORMALIZATION_RULES,
        "summary": {
            "case_count": len(inputs),
            "by_domain": dict(sorted(by_domain.items())),
            "by_risk": dict(sorted(by_risk.items())),
        },
        "engines": engine_meta,
        "rows": rows,
    }


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "<!-- zhtw:disable -->",
        f"# Accuracy Benchmark ({report['generated_date']})",
        "",
        f"Dataset: `{report['dataset']}`",
        f"Inputs: `{report['inputs']['path']}`",
        f"Expected: `{report['expected']['path']}`",
        f"Competitors lock: `{report['competitors_lock']['path']}`",
        "",
        "## Hashes",
        "",
        f"- Inputs sha256: `{report['inputs']['sha256']}`",
        f"- Expected sha256: `{report['expected']['sha256']}`",
        f"- Lock sha256: `{report['competitors_lock']['sha256']}`",
        "",
        "## Summary",
        "",
        f"- Cases: {report['summary']['case_count']}",
        "",
        "Domain distribution:",
        "",
    ]
    for domain, count in report["summary"]["by_domain"].items():
        lines.append(f"- `{domain}`: {count}")

    lines.extend(["", "Risk distribution:", ""])
    for risk, count in report["summary"]["by_risk"].items():
        lines.append(f"- `{risk}`: {count}")

    lines.extend(["", "## Engine Scores", ""])
    for engine_name, engine in report["engines"].items():
        scores = engine["scores"]
        availability = "available" if engine["available"] else f"skipped: {engine['error']}"
        lines.extend(
            [
                f"### {engine_name}",
                "",
                f"- Availability: {availability}",
                f"- Version: `{engine['version'] or ''}`",
                f"- Accepted accuracy: {scores['accepted_accuracy']:.4f}",
                f"- Primary exact accuracy: {scores['primary_exact_accuracy']:.4f}",
                f"- Idempotency rate: {scores['idempotency_rate']:.4f}",
                f"- Accepted: {scores['accepted']} / {scores['available_cases']}",
                f"- Misses: {scores['misses']}",
                "",
            ]
        )

    misses = [
        (row, engine_name, evaluation)
        for row in report["rows"]
        for engine_name, evaluation in row["evaluations"].items()
        if evaluation["available"] and not evaluation["accepted"]
    ]
    lines.extend(["## Misses", ""])
    if not misses:
        lines.append("None.")
    for row, engine_name, evaluation in misses:
        lines.extend(
            [
                f"### {row['id']} / {engine_name}",
                "",
                f"- Domain: `{row['domain']}`",
                f"- Risk: `{row['risk']}`",
                f"- Issue tags: `{', '.join(row['issue_tags'])}`",
                "",
                "Input:",
                "",
                code_block(row["input"]),
                "",
                "Expected:",
                "",
                code_block(row["expected"]),
                "",
                "Actual:",
                "",
                code_block(evaluation["output"]),
                "",
            ]
        )

    lines.append("")
    return "\n".join(lines)


def code_block(text: str) -> str:
    fence = "```"
    while fence in text:
        fence += "`"
    return f"{fence}text\n{text}\n{fence}"


def write_reports(report: dict[str, Any], output_prefix: Path, formats: list[str]) -> None:
    output_prefix.parent.mkdir(parents=True, exist_ok=True)
    if "json" in formats:
        output_prefix.with_suffix(".json").write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    if "md" in formats:
        output_prefix.with_suffix(".md").write_text(render_markdown(report), encoding="utf-8")


def parse_formats(raw: str) -> list[str]:
    formats = [item.strip() for item in raw.split(",") if item.strip()]
    invalid = sorted(set(formats) - {"json", "md"})
    if not formats or invalid:
        raise argparse.ArgumentTypeError("formats must be comma-separated from json,md")
    return formats


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path, default=DEFAULT_INPUTS)
    parser.add_argument("--expected", type=Path, default=DEFAULT_EXPECTED)
    parser.add_argument("--competitors-lock", type=Path, default=DEFAULT_LOCK)
    parser.add_argument(
        "--competitors",
        type=parse_competitors,
        default=parse_competitors(DEFAULT_COMPETITORS),
        help=f"Comma-separated competitors. Default: {DEFAULT_COMPETITORS}",
    )
    parser.add_argument(
        "--engines",
        dest="competitors",
        type=parse_competitors,
        help="Alias for --competitors.",
    )
    parser.add_argument(
        "--formats",
        type=parse_formats,
        default=parse_formats("json,md"),
        help="Comma-separated output formats. Default: json,md",
    )
    parser.add_argument("--output-prefix", type=Path, default=DEFAULT_OUTPUT_PREFIX)
    parser.add_argument("--generated-date", default=dt.date.today().isoformat())
    parser.add_argument(
        "--fail-on-zhtw-miss",
        action="store_true",
        help="Exit 1 if zhtw misses any expected output.",
    )
    parser.add_argument(
        "--fail-on-unavailable",
        action="store_true",
        help="Exit 1 if any requested competitor is unavailable.",
    )
    args = parser.parse_args()

    input_data, inputs = load_input_cases(args.inputs)
    expected_data, expected = load_expected_cases(args.expected)
    assert_expected_matches_inputs(inputs, expected)
    assert_expected_source_hash(args.inputs, expected_data)
    lock = load_lockfile(args.competitors_lock)
    assert_competitors_locked(args.competitors, lock)

    engines = load_engines(args.competitors)
    rows = build_rows(inputs, expected, engines)
    report = build_report(
        generated_date=args.generated_date,
        inputs_path=args.inputs,
        expected_path=args.expected,
        lock_path=args.competitors_lock,
        input_data=input_data,
        expected_data=expected_data,
        lock=lock,
        inputs=inputs,
        engines=engines,
        rows=rows,
    )
    write_reports(report, args.output_prefix, args.formats)

    summary = report["engines"]["zhtw"]["scores"]
    print(
        "cases={case_count} zhtw_accepted={accepted} zhtw_misses={misses}".format(
            case_count=report["summary"]["case_count"],
            accepted=summary["accepted"],
            misses=summary["misses"],
        )
    )
    for output_format in args.formats:
        print(f"wrote {relative_path(args.output_prefix.with_suffix('.' + output_format))}")

    if args.fail_on_unavailable and any(not engine.available for engine in engines):
        return 1
    if args.fail_on_zhtw_miss and summary["misses"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
