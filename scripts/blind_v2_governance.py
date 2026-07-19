#!/usr/bin/env python3
"""Validate and deterministically sample Blind-v2 input-only candidates."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.benchmark_metrics import paired_power_analysis  # noqa: E402

ACCURACY_ROOT = PROJECT_ROOT / "benchmarks" / "accuracy"
POOL_SCHEMA = ACCURACY_ROOT / "blind-v2.candidate-pool.schema.json"
INPUTS_SCHEMA = ACCURACY_ROOT / "blind-v2.inputs.schema.json"
DECISIONS_SCHEMA = ACCURACY_ROOT / "blind-v2.final-decisions.schema.json"
REPLACEMENTS_SCHEMA = ACCURACY_ROOT / "blind-v2.replacements.schema.json"
LEDGER_EVENT_SCHEMA = ACCURACY_ROOT / "blind-v2.evaluation-ledger-event.schema.json"
SEED = 20260719
NGRAM_SIZE = 5
NEAR_DUPLICATE_THRESHOLD = 0.85
MINIMUM_CANDIDATES = 1800

DOMAIN_WEIGHTS = (
    ("it_api_cli", 25),
    ("ui_i18n", 20),
    ("llm_generated", 15),
    ("formal_news", 15),
    ("social_daily", 15),
    ("high_stakes", 10),
)
RISK_WEIGHTS = (
    ("candidate_gap", 40),
    ("over_conversion_guard", 40),
    ("baseline_guard", 20),
)
FORBIDDEN_CASE_KEYS = {
    "expected",
    "acceptable",
    "annotation",
    "output",
    "normalized_output",
    "review",
}
REFERENCE_TEXT_KEYS = {"input", "source", "target", "expected", "acceptable"}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON must be an object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_schema(value: dict[str, Any], schema_path: Path) -> list[str]:
    schema = load_json(schema_path)
    pool_schema = load_json(POOL_SCHEMA)
    registry = Registry().with_resource(pool_schema["$id"], Resource.from_contents(pool_schema))
    validator = Draft202012Validator(
        schema,
        format_checker=FormatChecker(),
        registry=registry,
    )
    return [
        f"{error.json_path}: {error.message}"
        for error in sorted(validator.iter_errors(value), key=lambda item: list(item.path))
    ]


def normalize_for_dedupe(text: str) -> str:
    """Apply the preregistered dedupe normalization, without script conversion."""
    return " ".join(unicodedata.normalize("NFC", text).split())


def character_ngrams(text: str, size: int = NGRAM_SIZE) -> frozenset[str]:
    normalized = normalize_for_dedupe(text)
    if len(normalized) <= size:
        return frozenset({normalized}) if normalized else frozenset()
    return frozenset(
        normalized[index : index + size] for index in range(len(normalized) - size + 1)
    )


def jaccard(left: frozenset[str], right: frozenset[str]) -> float:
    if not left and not right:
        return 1.0
    union = left | right
    return len(left & right) / len(union) if union else 0.0


def apportion(total: int, weights: tuple[tuple[str, int], ...]) -> dict[str, int]:
    """Largest-remainder apportionment with declared order as the tie-break."""
    weight_total = sum(weight for _, weight in weights)
    floors: dict[str, int] = {}
    remainders: list[tuple[int, int, str]] = []
    for order, (name, weight) in enumerate(weights):
        numerator = total * weight
        floors[name] = numerator // weight_total
        remainders.append((numerator % weight_total, -order, name))
    for _, _, name in sorted(remainders, reverse=True)[: total - sum(floors.values())]:
        floors[name] += 1
    return floors


def stratum_quotas(total: int) -> dict[str, dict[str, int]]:
    domains = apportion(total, DOMAIN_WEIGHTS)
    return {domain: apportion(count, RISK_WEIGHTS) for domain, count in domains.items()}


def _rank(seed: int, case_id: str) -> str:
    return hashlib.sha256(f"{seed}\0{case_id}".encode()).hexdigest()


def deterministic_sample(
    pool: dict[str, Any],
    *,
    selected_n: int,
    excluded_ids: set[str] | None = None,
) -> tuple[list[dict[str, Any]], dict[str, dict[str, int]]]:
    if selected_n < 600:
        raise ValueError("selected_n must be at least 600")
    excluded_ids = excluded_ids or set()
    quotas = stratum_quotas(selected_n)
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for case in pool["cases"]:
        if case["id"] not in excluded_ids:
            grouped[(case["domain"], case["risk"])].append(case)

    selected: list[dict[str, Any]] = []
    for domain, risks in quotas.items():
        for risk, required in risks.items():
            candidates = sorted(
                grouped[(domain, risk)],
                key=lambda item: (_rank(pool["seed"], item["id"]), item["id"]),
            )
            if len(candidates) < required:
                raise ValueError(
                    f"stratum {domain}/{risk} requires {required}, has {len(candidates)}"
                )
            selected.extend(candidates[:required])
    selected.sort(key=lambda item: item["id"])
    return selected, quotas


def build_inputs(
    pool_path: Path,
    pool: dict[str, Any],
    selected_n: int,
    *,
    replacement_ledger_sha256: str = "0" * 64,
    excluded_ids: set[str] | None = None,
) -> dict[str, Any]:
    selected, quotas = deterministic_sample(
        pool,
        selected_n=selected_n,
        excluded_ids=excluded_ids,
    )
    by_domain = Counter(case["domain"] for case in selected)
    by_risk = Counter(case["risk"] for case in selected)
    return {
        "version": 1,
        "name": "blind-v2.inputs",
        "dataset": "blind-v2",
        "status": "selected",
        "source_pool_id": pool["id"],
        "source_pool_sha256": sha256_file(pool_path),
        "seed": pool["seed"],
        "selected_n": selected_n,
        "replacement_ledger_sha256": replacement_ledger_sha256,
        "quotas": quotas,
        "stats": {
            "by_domain": dict(sorted(by_domain.items())),
            "by_risk": dict(sorted(by_risk.items())),
        },
        "cases": selected,
    }


def _iter_strings(value: Any, *, parent_key: str | None = None) -> Iterable[str]:
    if isinstance(value, dict):
        for key, child in value.items():
            if key in REFERENCE_TEXT_KEYS:
                if isinstance(child, str):
                    yield child
                elif isinstance(child, list):
                    yield from (item for item in child if isinstance(item, str))
            yield from _iter_strings(child, parent_key=key)
    elif isinstance(value, list):
        for child in value:
            yield from _iter_strings(child, parent_key=parent_key)
    elif isinstance(value, str) and parent_key is None:
        yield value


def _mapping_strings(value: Any) -> Iterable[str]:
    if isinstance(value, dict):
        for key, child in value.items():
            yield str(key)
            yield from _mapping_strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from _mapping_strings(child)
    elif isinstance(value, str):
        yield value


def _is_tracked(path: Path) -> bool:
    result = subprocess.run(
        ["git", "ls-files", "--error-unmatch", "--", str(path.relative_to(PROJECT_ROOT))],
        cwd=PROJECT_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    return result.returncode == 0


def reference_texts(pool: dict[str, Any], pool_path: Path) -> tuple[list[str], list[str], str]:
    texts: list[str] = []
    errors: list[str] = []
    seen_paths: set[Path] = set()
    snapshot: list[dict[str, str]] = []
    for pattern in pool["deduplication"]["reference_globs"]:
        matches = sorted(PROJECT_ROOT.glob(pattern))
        if not matches:
            errors.append(f"dedupe reference glob matched no files: {pattern}")
        for path in matches:
            path = path.resolve()
            is_blind_v2_artifact = path.parent == ACCURACY_ROOT and path.name.startswith(
                "blind-v2."
            )
            if (
                path == pool_path.resolve()
                or is_blind_v2_artifact
                or path in seen_paths
                or not path.is_file()
            ):
                continue
            seen_paths.add(path)
            if not _is_tracked(path):
                continue
            try:
                value = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                errors.append(
                    f"cannot read dedupe reference {path.relative_to(PROJECT_ROOT)}: {exc}"
                )
                continue
            extractor = _mapping_strings if "src/zhtw/data/terms/" in str(path) else _iter_strings
            texts.extend(extractor(value))
            snapshot.append(
                {
                    "path": str(path.relative_to(PROJECT_ROOT)),
                    "sha256": sha256_file(path),
                }
            )
    snapshot_bytes = (
        json.dumps(snapshot, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode()
    return texts, errors, hashlib.sha256(snapshot_bytes).hexdigest()


def _near_duplicate_pairs(
    labelled_texts: list[tuple[str, str]], threshold: float
) -> Iterable[tuple[str, str, float]]:
    grams_by_label: dict[str, frozenset[str]] = {}
    inverted: dict[str, set[str]] = defaultdict(set)
    normalized_by_label: dict[str, str] = {}
    for label, text in labelled_texts:
        normalized = normalize_for_dedupe(text)
        grams = character_ngrams(normalized)
        possible: set[str] = set()
        for gram in grams:
            possible.update(inverted[gram])
        for other in sorted(possible):
            if normalized == normalized_by_label[other]:
                continue
            score = jaccard(grams, grams_by_label[other])
            if score >= threshold:
                yield other, label, score
        grams_by_label[label] = grams
        normalized_by_label[label] = normalized
        for gram in grams:
            inverted[gram].add(label)


def _near_duplicates_against_references(
    candidates: list[tuple[str, str]], references: list[str], threshold: float
) -> Iterable[tuple[str, float]]:
    reference_grams: dict[int, frozenset[str]] = {}
    inverted: dict[str, set[int]] = defaultdict(set)
    for index, text in enumerate(references):
        grams = character_ngrams(text)
        reference_grams[index] = grams
        for gram in grams:
            inverted[gram].add(index)

    for case_id, text in candidates:
        grams = character_ngrams(text)
        possible: set[int] = set()
        for gram in grams:
            possible.update(inverted[gram])
        best = max((jaccard(grams, reference_grams[index]) for index in possible), default=0.0)
        if best >= threshold:
            yield case_id, best


def _expected_stats(cases: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "total": len(cases),
        "by_domain": dict(sorted(Counter(case["domain"] for case in cases).items())),
        "by_risk": dict(sorted(Counter(case["risk"] for case in cases).items())),
        "by_source_class": dict(sorted(Counter(case["source"]["class"] for case in cases).items())),
        "by_source": dict(sorted(Counter(case["source"]["id"] for case in cases).items())),
    }


def validate_pool(
    pool_path: Path,
    *,
    require_ready: bool = False,
    check_references: bool = True,
) -> list[str]:
    pool = load_json(pool_path)
    errors = [f"{pool_path}: {error}" for error in validate_schema(pool, POOL_SCHEMA)]
    if errors:
        return errors

    cases = pool["cases"]
    ids = [case["id"] for case in cases]
    duplicate_ids = sorted(case_id for case_id, count in Counter(ids).items() if count > 1)
    if duplicate_ids:
        errors.append(f"duplicate case ids: {', '.join(duplicate_ids[:10])}")
    for case in cases:
        leaked = sorted(FORBIDDEN_CASE_KEYS & set(case))
        if leaked:
            errors.append(f"{case['id']} leaks forbidden fields: {', '.join(leaked)}")
        if normalize_for_dedupe(case["input"]) != case["input"]:
            errors.append(f"{case['id']} input is not dedupe-normalized")

    expected_stats = _expected_stats(cases)
    if pool["stats"] != expected_stats:
        errors.append("stats do not match candidate cases")

    total = len(cases)
    power = pool["power_analysis"]
    computed_power = paired_power_analysis(
        discordant_rate=power["discordant_rate"],
        minimum_detectable_effect=power["minimum_detectable_effect"],
        alpha=power["alpha"],
        target_power=power["target_power"],
    )
    if power["required_cases"] != computed_power["required_cases"]:
        errors.append("power_analysis.required_cases does not match recomputed power")
    if pool["formal_n"] < max(600, computed_power["required_cases"]):
        errors.append("formal_n is below the power-analysis requirement")
    minimum = max(MINIMUM_CANDIDATES, 3 * pool["formal_n"])
    if (require_ready or pool["status"] == "frozen") and total < minimum:
        errors.append(f"candidate pool requires at least {minimum} cases for N={pool['formal_n']}")
    if total:
        class_limit = pool["source_policy"]["maximum_source_class_fraction"]
        source_limit = pool["source_policy"]["maximum_source_fraction"]
        for source_class, count in expected_stats["by_source_class"].items():
            if count / total > class_limit + 1e-12:
                errors.append(
                    f"source class {source_class} exceeds {class_limit:.0%}: {count}/{total}"
                )
        for source_id, count in expected_stats["by_source"].items():
            if count / total > source_limit + 1e-12:
                errors.append(f"source {source_id} exceeds {source_limit:.0%}: {count}/{total}")

    normalized_to_ids: dict[str, list[str]] = defaultdict(list)
    for case in cases:
        normalized_to_ids[normalize_for_dedupe(case["input"])].append(case["id"])
    for case_ids in normalized_to_ids.values():
        if len(case_ids) > 1:
            errors.append(f"exact duplicate candidates: {', '.join(sorted(case_ids))}")

    labelled_candidates = [(case["id"], case["input"]) for case in cases]
    for left, right, score in _near_duplicate_pairs(
        labelled_candidates, pool["deduplication"]["near_duplicate_threshold"]
    ):
        errors.append(f"near duplicate candidates: {left}, {right} ({score:.4f})")

    if check_references:
        references, reference_errors, reference_snapshot_sha256 = reference_texts(pool, pool_path)
        errors.extend(reference_errors)
        if pool["deduplication"]["reference_snapshot_sha256"] != reference_snapshot_sha256:
            errors.append("dedupe reference_snapshot_sha256 does not match tracked references")
        reference_exact = {normalize_for_dedupe(text) for text in references if text.strip()}
        for case in cases:
            if normalize_for_dedupe(case["input"]) in reference_exact:
                errors.append(f"{case['id']} exactly duplicates an existing benchmark or mapping")

        for case_id, score in _near_duplicates_against_references(
            labelled_candidates,
            references,
            pool["deduplication"]["near_duplicate_threshold"],
        ):
            errors.append(
                f"{case_id} near-duplicates an existing benchmark or mapping ({score:.4f})"
            )
    return errors


def validate_decisions(inputs_path: Path, decisions_path: Path) -> list[str]:
    inputs = load_json(inputs_path)
    decisions = load_json(decisions_path)
    errors = [
        f"{decisions_path}: {error}" for error in validate_schema(decisions, DECISIONS_SCHEMA)
    ]
    if errors:
        return errors
    if decisions["inputs_sha256"] != sha256_file(inputs_path):
        errors.append("final decisions inputs_sha256 does not match inputs")
    input_ids = [case["id"] for case in inputs["cases"]]
    decision_ids = [case_id for batch in decisions["batches"] for case_id in batch["case_ids"]]
    duplicates = sorted(case_id for case_id, count in Counter(decision_ids).items() if count > 1)
    if duplicates:
        errors.append(f"cases covered by multiple decision batches: {', '.join(duplicates[:10])}")
    if set(decision_ids) != set(input_ids) or len(decision_ids) != len(input_ids):
        missing = sorted(set(input_ids) - set(decision_ids))
        extra = sorted(set(decision_ids) - set(input_ids))
        errors.append(
            f"final decisions do not cover N/N cases; missing={missing[:10]} extra={extra[:10]}"
        )
    if decisions["total_cases"] != len(input_ids):
        errors.append("final decisions total_cases does not match inputs")
    return errors


def validate_replacements(pool_path: Path, ledger_path: Path) -> tuple[list[str], set[str]]:
    pool = load_json(pool_path)
    ledger = load_json(ledger_path)
    errors = [f"{ledger_path}: {error}" for error in validate_schema(ledger, REPLACEMENTS_SCHEMA)]
    if errors:
        return errors, set()
    if ledger["source_pool_sha256"] != sha256_file(pool_path):
        errors.append("replacement ledger source_pool_sha256 does not match pool")
    if ledger["seed"] != pool["seed"]:
        errors.append("replacement ledger seed does not match pool")
    if ledger["formal_n"] != pool["formal_n"]:
        errors.append("replacement ledger formal_n does not match pool")

    excluded: set[str] = set()
    try:
        current, _ = deterministic_sample(pool, selected_n=pool["formal_n"])
    except ValueError as exc:
        return errors + [f"cannot build initial sample: {exc}"], excluded
    current_ids = {case["id"] for case in current}
    for index, event in enumerate(ledger["events"], start=1):
        excluded_id = event["excluded_id"]
        if excluded_id in excluded:
            errors.append(f"replacement event #{index} excludes {excluded_id} more than once")
            continue
        if excluded_id not in current_ids:
            errors.append(f"replacement event #{index} excludes a case outside the current sample")
            continue
        excluded.add(excluded_id)
        try:
            updated, _ = deterministic_sample(
                pool,
                selected_n=pool["formal_n"],
                excluded_ids=excluded,
            )
        except ValueError as exc:
            errors.append(f"replacement event #{index} cannot refill its stratum: {exc}")
            continue
        updated_ids = {case["id"] for case in updated}
        removed = current_ids - updated_ids
        added = updated_ids - current_ids
        if removed != {excluded_id} or added != {event["replacement_id"]}:
            errors.append(
                f"replacement event #{index} is not the next deterministic reserve; "
                f"removed={sorted(removed)} added={sorted(added)}"
            )
        current_ids = updated_ids
    return errors, excluded


def load_ledger(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    if not path.exists():
        return [], []
    events: list[dict[str, Any]] = []
    errors: list[str] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"ledger line {line_number}: invalid JSON: {exc}")
            continue
        if not isinstance(event, dict):
            errors.append(f"ledger line {line_number}: event must be an object")
            continue
        events.append(event)
        errors.extend(
            f"ledger line {line_number}: {error}"
            for error in validate_schema(event, LEDGER_EVENT_SCHEMA)
        )
    return events, errors


def validate_ledger(path: Path) -> list[str]:
    events, errors = load_ledger(path)
    exposed: set[str] = set()
    active_runs: dict[str, dict[str, Any]] = {}
    immutable_fields = (
        "preregistration_sha256",
        "inputs_sha256",
        "expected_sha256",
        "zhtw_git_sha",
        "competitor_lock_sha256",
    )
    fingerprints: dict[str, tuple[Any, ...]] = {}
    for event in events:
        preregistration = event["preregistration_sha256"]
        fingerprint = tuple(event[field] for field in immutable_fields)
        previous = fingerprints.setdefault(preregistration, fingerprint)
        if previous != fingerprint:
            errors.append("ledger changes immutable hashes for one preregistration")
        if preregistration in exposed and event["event"] == "run_started":
            errors.append("one-shot evaluation already exposed a score")
        run_id = event["run_id"]
        if event["event"] == "run_started":
            if run_id in active_runs:
                errors.append(f"run {run_id} starts more than once")
            active_runs[run_id] = event
        elif run_id not in active_runs:
            errors.append(f"run {run_id} ends without run_started")
        else:
            active_runs.pop(run_id)
            if event["event"] == "score_exposed":
                if preregistration in exposed:
                    errors.append("one preregistration exposes more than one score")
                exposed.add(preregistration)
    if active_runs:
        errors.append(f"ledger has unfinished runs: {', '.join(sorted(active_runs))}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_pool_parser = subparsers.add_parser("validate-pool")
    validate_pool_parser.add_argument("pool", type=Path)
    validate_pool_parser.add_argument("--require-ready", action="store_true")
    validate_pool_parser.add_argument("--skip-references", action="store_true")

    sample_parser = subparsers.add_parser("sample")
    sample_parser.add_argument("pool", type=Path)
    sample_parser.add_argument("--selected-n", type=int, required=True)
    sample_parser.add_argument("--replacements", type=Path, required=True)
    sample_parser.add_argument("--output", type=Path, required=True)

    replacements_parser = subparsers.add_parser("validate-replacements")
    replacements_parser.add_argument("pool", type=Path)
    replacements_parser.add_argument("replacements", type=Path)

    decisions_parser = subparsers.add_parser("validate-decisions")
    decisions_parser.add_argument("inputs", type=Path)
    decisions_parser.add_argument("decisions", type=Path)

    ledger_parser = subparsers.add_parser("validate-ledger")
    ledger_parser.add_argument("ledger", type=Path)

    args = parser.parse_args()
    errors: list[str]
    if args.command == "validate-pool":
        errors = validate_pool(
            args.pool.resolve(),
            require_ready=args.require_ready,
            check_references=not args.skip_references,
        )
    elif args.command == "sample":
        errors = validate_pool(args.pool.resolve(), require_ready=True)
        replacement_errors, excluded_ids = validate_replacements(
            args.pool.resolve(), args.replacements.resolve()
        )
        errors.extend(replacement_errors)
        if not errors:
            pool = load_json(args.pool)
            if pool["status"] != "frozen":
                errors.append("candidate pool must be frozen before sampling")
            elif args.selected_n != pool["formal_n"]:
                errors.append("selected_n must equal the pool's preregistered formal_n")
            else:
                inputs = build_inputs(
                    args.pool.resolve(),
                    pool,
                    args.selected_n,
                    replacement_ledger_sha256=sha256_file(args.replacements.resolve()),
                    excluded_ids=excluded_ids,
                )
                schema_errors = validate_schema(inputs, INPUTS_SCHEMA)
                errors.extend(f"generated inputs: {error}" for error in schema_errors)
                if not errors:
                    write_json(args.output, inputs)
                    print(f"wrote {args.output} ({args.selected_n} cases)")
    elif args.command == "validate-replacements":
        errors, _ = validate_replacements(args.pool.resolve(), args.replacements.resolve())
    elif args.command == "validate-decisions":
        errors = validate_decisions(args.inputs.resolve(), args.decisions.resolve())
    else:
        errors = validate_ledger(args.ledger.resolve())

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Blind-v2 {args.command} validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
