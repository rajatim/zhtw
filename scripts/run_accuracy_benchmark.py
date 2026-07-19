#!/usr/bin/env python3
"""Run an accuracy benchmark against locked converters."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import platform
import random
import subprocess
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from scripts.benchmark_metrics import changed_span_metrics, paired_comparison  # noqa: E402
from scripts.competitor_benchmark import ENGINE_LOADERS, Engine, load_engines  # noqa: E402
from scripts.validate_benchmark_assets import (  # noqa: E402
    validate_manifest,
    validate_preregistration,
)
from scripts.validate_competitor_environment import validate_lock  # noqa: E402

DEFAULT_INPUTS = PROJECT_ROOT / "benchmarks" / "accuracy" / "blind-v1.inputs.json"
DEFAULT_EXPECTED = PROJECT_ROOT / "benchmarks" / "accuracy" / "blind-v1.expected.json"
DEFAULT_LOCK = PROJECT_ROOT / "benchmarks" / "accuracy" / "competitors.lock.json"
DEFAULT_OUTPUT_PREFIX = PROJECT_ROOT / "docs" / "reports" / "accuracy-benchmark"
DEFAULT_COMPETITORS = "zhtw"
REPORT_MODES = {"aggregate", "detailed"}
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


def git_output(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=PROJECT_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise ValueError("git provenance unavailable")
    return result.stdout.strip()


def optional_tool_version(*command: str) -> str | None:
    try:
        result = subprocess.run(
            list(command),
            cwd=PROJECT_ROOT,
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if result.returncode != 0:
        return None
    return (result.stdout or result.stderr).strip().splitlines()[0]


def build_provenance(engines: list[Engine]) -> dict[str, Any]:
    from zhtw import __version__

    project = tomllib.loads((PROJECT_ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    declared_version = str(project["project"]["version"])
    zhtw_engine = next((engine for engine in engines if engine.name == "zhtw"), None)
    versions = {
        "package": __version__,
        "pyproject": declared_version,
        "engine": zhtw_engine.version if zhtw_engine else None,
    }
    if len({version for version in versions.values() if version is not None}) != 1:
        raise ValueError(f"zhtw version mismatch: {versions}")

    status = git_output("status", "--porcelain")
    return {
        "zhtw_version": __version__,
        "git_sha": git_output("rev-parse", "HEAD"),
        "git_dirty": bool(status),
        "python_version": platform.python_version(),
        "node_version": optional_tool_version("node", "--version"),
        "rust_version": optional_tool_version("rustc", "--version"),
        "os": platform.platform(),
        "architecture": platform.machine(),
        "runner_sha256": sha256_file(Path(__file__)),
    }


def is_git_tracked(path: Path) -> bool:
    try:
        relative = path.resolve().relative_to(PROJECT_ROOT)
    except ValueError:
        return False
    result = subprocess.run(
        ["git", "ls-files", "--error-unmatch", "--", str(relative)],
        cwd=PROJECT_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    return result.returncode == 0


def is_git_ignored(path: Path) -> bool:
    try:
        relative = path.resolve().relative_to(PROJECT_ROOT)
    except ValueError:
        return True
    result = subprocess.run(
        ["git", "check-ignore", "--no-index", "--quiet", "--", str(relative)],
        cwd=PROJECT_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    return result.returncode == 0


def assert_output_policy(output_prefix: Path, formats: list[str], report_mode: str) -> None:
    if report_mode == "aggregate":
        return
    for output_format in formats:
        path = output_prefix.with_suffix(f".{output_format}")
        if is_git_tracked(path):
            raise ValueError(f"detailed report output is tracked by git: {relative_path(path)}")
        if not is_git_ignored(path):
            raise ValueError(
                "detailed report output inside the repository must be gitignored: "
                f"{relative_path(path)}"
            )


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


def assert_formal_engines_locked(
    requested: list[str],
    engines: list[Engine],
    lock: dict[str, Any],
) -> None:
    if lock.get("status") != "locked":
        raise ValueError("formal benchmark requires a locked competitor environment")
    required = set(lock.get("formal_engine_ids", []))
    if set(requested) != required:
        raise ValueError(
            "formal market benchmark must run every locked engine: "
            f"required={sorted(required)} requested={sorted(requested)}"
        )
    locked = {item["id"]: item for item in lock["competitors"]}
    environment_hash = lock["environment"]["environment_sha256"]
    mismatches: list[str] = []
    for engine in engines:
        expected = locked[engine.name]
        checks = {
            "version": expected["version"],
            "family": expected["family"],
            "adapter": expected["adapter"],
            "config_sha256": expected["config_sha256"],
        }
        if engine.name != "zhtw":
            checks["environment_sha256"] = environment_hash
        for field, expected_value in checks.items():
            actual_value = getattr(engine, field)
            if actual_value != expected_value:
                mismatches.append(
                    f"{engine.name}.{field}: expected={expected_value} actual={actual_value}"
                )
    if mismatches:
        raise ValueError("formal competitor lock mismatch: " + "; ".join(mismatches))


def assert_formal_engines_available(engines: list[Engine]) -> None:
    unavailable = [engine.name for engine in engines if not engine.available]
    if unavailable:
        raise ValueError(
            "formal benchmark requires every requested engine to be available: "
            + ", ".join(unavailable)
        )


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
            "error_category": "engine_unavailable",
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
            "error_category": "exception",
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
        "error": "empty output" if not normalized_output else "",
        "error_category": "empty_output" if not normalized_output else "",
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
    error_counts: Counter[str] = Counter()
    risk_totals: Counter[str] = Counter()
    risk_accepted: Counter[str] = Counter()
    severe_errors: Counter[str] = Counter()
    changed_required = 0
    changed_produced = 0
    changed_correct = 0
    for row in rows:
        evaluation = row["evaluations"][engine_name]
        if not evaluation["available"]:
            continue
        domain_totals[row["domain"]] += 1
        risk_totals[row["risk"]] += 1
        if evaluation["error_category"]:
            error_counts[evaluation["error_category"]] += 1
        if evaluation["accepted"]:
            domain_accepted[row["domain"]] += 1
            risk_accepted[row["risk"]] += 1
        else:
            risk_miss_counts[row["risk"]] += 1
            issue_miss_counts.update(row["issue_tags"] or ["other"])
            if row["severity"] in {"P0", "P1"}:
                severe_errors[row["severity"]] += 1
        span_metrics = changed_span_metrics(
            row["input"], row["expected"], evaluation["normalized_output"]
        )
        changed_required += int(span_metrics["required_edits"])
        changed_produced += int(span_metrics["produced_edits"])
        changed_correct += int(span_metrics["correct_edits"])

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
    risk_accuracy = {
        risk: {
            "total": count,
            "accepted": risk_accepted[risk],
            "accuracy": risk_accepted[risk] / count,
        }
        for risk, count in sorted(risk_totals.items())
    }
    changed_precision = changed_correct / changed_produced if changed_produced else 1.0
    changed_recall = changed_correct / changed_required if changed_required else 1.0
    changed_f1 = (
        2 * changed_precision * changed_recall / (changed_precision + changed_recall)
        if changed_precision + changed_recall
        else 0.0
    )
    macro_domain_accuracy = (
        sum(item["accepted_accuracy"] for item in by_domain.values()) / len(by_domain)
        if by_domain
        else 0.0
    )
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
        "micro_accuracy": accepted / available_count if available_count else 0.0,
        "macro_domain_accuracy": macro_domain_accuracy,
        "primary_exact_accuracy": primary_exact / available_count if available_count else 0.0,
        "idempotency_rate": idempotent / available_count if available_count else 0.0,
        "accepted_accuracy_ci_95": bootstrap_ci(accepted_values),
        "by_domain": by_domain,
        "by_risk": risk_accuracy,
        "conversion_recall": risk_accuracy.get("candidate_gap", {}).get("accuracy", 0.0),
        "over_conversion_guard_accuracy": risk_accuracy.get("over_conversion_guard", {}).get(
            "accuracy", 0.0
        ),
        "baseline_guard_accuracy": risk_accuracy.get("baseline_guard", {}).get("accuracy", 0.0),
        "p0_error_count": severe_errors["P0"],
        "p1_error_count": severe_errors["P1"],
        "severe_error_rate": sum(severe_errors.values()) / available_count
        if available_count
        else 0.0,
        "errors_by_category": dict(sorted(error_counts.items())),
        "changed_span": {
            "required_edits": changed_required,
            "produced_edits": changed_produced,
            "correct_edits": changed_correct,
            "precision": changed_precision,
            "recall": changed_recall,
            "f1": changed_f1,
        },
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
                "severity": str(expected_case.annotation.get("severity", "")),
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
    report_mode: str,
    manifest_path: Path | None = None,
    preregistration_path: Path | None = None,
    provenance: dict[str, Any] | None = None,
) -> dict[str, Any]:
    by_domain = Counter(case.domain for case in inputs)
    by_risk = Counter(case.risk for case in inputs)
    engine_meta = {
        engine.name: {
            "available": engine.available,
            "version": engine.version,
            "error": engine.error,
            "family": engine.family,
            "adapter": engine.adapter,
            "environment_sha256": engine.environment_sha256,
            "image_id": engine.image_id,
            "config_sha256": engine.config_sha256,
            "scores": summarize_engine(rows, engine.name),
        }
        for engine in engines
    }
    report = {
        "generated_date": generated_date,
        "report_mode": report_mode,
        "dataset": input_data.get("dataset", ""),
        "dataset_classification": (
            "published_evaluation"
            if input_data.get("dataset") == "blind-v1"
            else input_data.get("publish_state", "")
        ),
        "provenance": provenance or build_provenance(engines),
        "inputs": {
            "path": relative_path(inputs_path),
            "sha256": sha256_file(inputs_path),
            "name": input_data.get("name", ""),
            "status": input_data.get("status", ""),
            "publish_state": input_data.get("publish_state", ""),
        },
        "expected_sha256": sha256_file(expected_path),
        "competitors_lock": {
            "path": relative_path(lock_path),
            "sha256": sha256_file(lock_path),
            "status": lock.get("status", ""),
            "environment_sha256": lock.get("environment", {}).get("environment_sha256"),
            "ranking_families": lock.get("ranking_families", []),
            "competitors": lock.get("competitors", []),
        },
        "normalization": NORMALIZATION_RULES,
        "dataset_manifest_sha256": sha256_file(manifest_path) if manifest_path else None,
        "preregistration_sha256": (
            sha256_file(preregistration_path) if preregistration_path else None
        ),
        "summary": {
            "case_count": len(inputs),
            "by_domain": dict(sorted(by_domain.items())),
            "by_risk": dict(sorted(by_risk.items())),
        },
        "engines": engine_meta,
    }
    if len(engines) > 1:
        zhtw_values = [bool(row["evaluations"]["zhtw"]["accepted"]) for row in rows]
        report["paired_comparisons"] = {
            engine.name: paired_comparison(
                zhtw_values,
                [bool(row["evaluations"][engine.name]["accepted"]) for row in rows],
            )
            for engine in engines
            if engine.name != "zhtw" and engine.available
        }
    if report_mode == "detailed":
        report["private_expected"] = {
            "path": relative_path(expected_path),
            "name": expected_data.get("name", ""),
            "status": expected_data.get("status", ""),
            "source_inputs": expected_data.get("source_inputs", ""),
            "source_inputs_sha256": expected_data.get("source_inputs_sha256", ""),
        }
        report["rows"] = rows
    return report


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "<!-- zhtw:disable -->",
        f"# Accuracy Benchmark ({report['generated_date']})",
        "",
        f"Report mode: `{report['report_mode']}`",
        f"Dataset classification: `{report['dataset_classification']}`",
        f"Dataset: `{report['dataset']}`",
        f"Inputs: `{report['inputs']['path']}`",
        f"Competitors lock: `{report['competitors_lock']['path']}`",
        "",
        "## Hashes",
        "",
        f"- Inputs sha256: `{report['inputs']['sha256']}`",
        f"- Expected sha256: `{report['expected_sha256']}`",
        f"- Lock sha256: `{report['competitors_lock']['sha256']}`",
        f"- Competitor environment: `{report['competitors_lock']['environment_sha256'] or ''}`",
        f"- zhtw version: `{report['provenance']['zhtw_version']}`",
        f"- Git SHA: `{report['provenance']['git_sha']}`",
        f"- Git dirty: `{str(report['provenance']['git_dirty']).lower()}`",
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
                f"- Family: `{engine['family'] or ''}`",
                f"- Adapter: `{engine['adapter'] or ''}`",
                f"- Environment: `{engine['environment_sha256'] or ''}`",
                f"- Image ID: `{engine['image_id'] or ''}`",
                f"- Config sha256: `{engine['config_sha256'] or ''}`",
                f"- Accepted accuracy: {scores['accepted_accuracy']:.4f}",
                f"- Macro-domain accuracy: {scores['macro_domain_accuracy']:.4f}",
                f"- Primary exact accuracy: {scores['primary_exact_accuracy']:.4f}",
                f"- Idempotency rate: {scores['idempotency_rate']:.4f}",
                f"- Accepted: {scores['accepted']} / {scores['available_cases']}",
                f"- Misses: {scores['misses']}",
                "",
            ]
        )

    if report["report_mode"] != "detailed":
        lines.append("")
        return "\n".join(lines)

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


def parse_report_mode(raw: str) -> str:
    if raw not in REPORT_MODES:
        raise argparse.ArgumentTypeError("report mode must be aggregate or detailed")
    return raw


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path, default=DEFAULT_INPUTS)
    parser.add_argument("--expected", type=Path, default=DEFAULT_EXPECTED)
    parser.add_argument("--competitors-lock", type=Path, default=DEFAULT_LOCK)
    parser.add_argument(
        "--competitor-image",
        help="Locked Docker image used for all non-zhtw competitors.",
    )
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
    parser.add_argument(
        "--report-mode",
        type=parse_report_mode,
        default="aggregate",
        help="aggregate is safe for publication; detailed requires a private output path.",
    )
    parser.add_argument("--generated-date", default=dt.date.today().isoformat())
    parser.add_argument("--formal", action="store_true")
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--preregistration", type=Path)
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
    assert_output_policy(args.output_prefix, args.formats, args.report_mode)

    if args.formal and (args.manifest is None or args.preregistration is None):
        parser.error("--formal requires --manifest and --preregistration")
    if args.formal:
        validation_errors = validate_manifest(args.manifest.resolve())
        validation_errors.extend(
            validate_preregistration(
                args.preregistration.resolve(),
                manifest_path=args.manifest.resolve(),
                inputs_path=args.inputs.resolve(),
                expected_path=args.expected.resolve(),
                lock_path=args.competitors_lock.resolve(),
            )
        )
        if validation_errors:
            raise ValueError("formal benchmark assets invalid: " + "; ".join(validation_errors))

    input_data, inputs = load_input_cases(args.inputs)
    expected_data, expected = load_expected_cases(args.expected)
    assert_expected_matches_inputs(inputs, expected)
    assert_expected_source_hash(args.inputs, expected_data)
    lock = load_lockfile(args.competitors_lock)
    assert_competitors_locked(args.competitors, lock)
    if args.formal:
        lock_errors = validate_lock(args.competitors_lock.resolve())
        if lock_errors:
            raise ValueError("formal competitor lock invalid: " + "; ".join(lock_errors))

    if args.formal and not args.competitor_image:
        parser.error("--formal requires --competitor-image")
    engines = load_engines(
        args.competitors,
        lock=lock,
        container_image=args.competitor_image,
    )
    if args.formal:
        assert_formal_engines_available(engines)
        assert_formal_engines_locked(args.competitors, engines, lock)
    provenance = build_provenance(engines)
    if args.formal:
        preregistration = load_json(args.preregistration)
        if provenance["git_dirty"]:
            raise ValueError("formal benchmark requires a clean Git worktree")
        if preregistration["zhtw_git_sha"] != provenance["git_sha"]:
            raise ValueError("formal benchmark zhtw_git_sha does not match HEAD")
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
        report_mode=args.report_mode,
        manifest_path=args.manifest,
        preregistration_path=args.preregistration,
        provenance=provenance,
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
