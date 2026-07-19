#!/usr/bin/env python3
"""Report-only precision benchmark against optional competitor converters.

This script compares zhtw with optional third-party converters on manually
curated Taiwan Traditional expected outputs. Competitor outputs are discovery
signals only; they are not a source of truth and should not be used to bulk
import vocabulary.

Usage:
    uv run python scripts/competitor_benchmark.py
    uv run python scripts/competitor_benchmark.py --format json
    uv run python scripts/competitor_benchmark.py --engines zhtw
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import sys
from collections import Counter
from contextlib import redirect_stdout
from dataclasses import dataclass
from io import StringIO
from pathlib import Path
from typing import Any, Callable

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from scripts.container_competitors import (  # noqa: E402
    JsonlProcessClient,
    docker_adapter_command,
    inspect_image_environment,
)

DEFAULT_CASES = PROJECT_ROOT / "benchmarks" / "precision_cases.json"
DEFAULT_LOCK = PROJECT_ROOT / "benchmarks" / "accuracy" / "competitors.lock.json"

Converter = Callable[[str], str]


@dataclass(frozen=True)
class Engine:
    name: str
    available: bool
    convert: Converter | None = None
    version: str | None = None
    error: str | None = None
    family: str | None = None
    adapter: str | None = None
    environment_sha256: str | None = None
    image_id: str | None = None
    config_sha256: str | None = None


@dataclass(frozen=True)
class Case:
    id: str
    domain: str
    input: str
    expected: str
    risk: str
    notes: str


def load_zhtw() -> Engine:
    from zhtw import __version__, convert

    data_path = PROJECT_ROOT / "sdk" / "data" / "zhtw-data.json"
    return Engine(
        name="zhtw",
        available=True,
        convert=convert,
        version=__version__,
        family="zhtw",
        adapter="local_python",
        config_sha256=hashlib.sha256(data_path.read_bytes()).hexdigest(),
    )


def package_version(*names: str) -> str | None:
    for name in names:
        try:
            return importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            continue
    return None


def load_opencc_s2twp() -> Engine:
    try:
        import opencc  # type: ignore[import-not-found]
    except Exception as exc:
        return Engine(name="opencc-s2twp", available=False, error=str(exc))

    errors: list[str] = []
    for config in ("s2twp", "s2twp.json"):
        try:
            converter = opencc.OpenCC(config)
            converter.convert("test")
            return Engine(
                name="opencc-s2twp",
                available=True,
                convert=converter.convert,
                version=package_version("opencc-python-reimplemented", "opencc"),
                family="opencc",
                adapter="local_python_optional",
            )
        except Exception as exc:
            errors.append(f"{config}: {exc}")

    return Engine(name="opencc-s2twp", available=False, error="; ".join(errors))


def load_zhconv_zh_tw() -> Engine:
    try:
        import zhconv  # type: ignore[import-not-found]
    except Exception as exc:
        return Engine(name="zhconv-zh-tw", available=False, error=str(exc))

    try:
        zhconv.convert("test", "zh-tw")
    except Exception as exc:
        return Engine(name="zhconv-zh-tw", available=False, error=str(exc))

    return Engine(
        name="zhconv-zh-tw",
        available=True,
        convert=lambda text: zhconv.convert(text, "zh-tw"),
        version=package_version("zhconv"),
        family="mediawiki-zhconv",
        adapter="local_python_optional",
    )


def unavailable_container_engine(name: str) -> Engine:
    return Engine(
        name=name,
        available=False,
        error="locked container image is required",
        adapter="container_jsonl",
    )


ENGINE_LOADERS: dict[str, Callable[[], Engine]] = {
    "zhtw": load_zhtw,
    "opencc-s2twp": load_opencc_s2twp,
    "zhconv-zh-tw": load_zhconv_zh_tw,
    "opencc-js-cn-twp": lambda: unavailable_container_engine("opencc-js-cn-twp"),
    "zhconv-rs-zh-tw": lambda: unavailable_container_engine("zhconv-rs-zh-tw"),
}


def parse_engines(raw: str) -> list[str]:
    engines = [name.strip() for name in raw.split(",") if name.strip()]
    invalid = sorted(set(engines) - set(ENGINE_LOADERS))
    if not engines or invalid:
        valid = ",".join(ENGINE_LOADERS)
        raise argparse.ArgumentTypeError(f"engines must be comma-separated from {valid}")
    if "zhtw" not in engines:
        raise argparse.ArgumentTypeError("engines must include zhtw")
    return engines


def load_cases(path: Path) -> list[Case]:
    data = json.loads(path.read_text(encoding="utf-8"))
    cases: list[Case] = []
    for index, raw in enumerate(data.get("cases", []), start=1):
        missing = sorted({"id", "domain", "input", "expected"} - set(raw))
        if missing:
            raise ValueError(f"case #{index} missing required fields: {', '.join(missing)}")
        cases.append(
            Case(
                id=str(raw["id"]),
                domain=str(raw["domain"]),
                input=str(raw["input"]),
                expected=str(raw["expected"]),
                risk=str(raw.get("risk", "")),
                notes=str(raw.get("notes", "")),
            )
        )
    if not cases:
        raise ValueError(f"no cases found in {path}")
    return cases


def load_container_engine(
    name: str,
    *,
    lock: dict[str, Any],
    image: str,
) -> Engine:
    competitors = {item["id"]: item for item in lock.get("competitors", [])}
    expected = competitors[name]
    expected_environment = lock["environment"]["environment_sha256"]
    client: JsonlProcessClient | None = None
    try:
        actual_environment, image_id = inspect_image_environment(image)
        if actual_environment != expected_environment:
            raise ValueError(
                "competitor image environment hash mismatch: "
                f"expected={expected_environment} actual={actual_environment}"
            )
        client = JsonlProcessClient(
            docker_adapter_command(image_id, name),
            timeout_seconds=float(lock["environment"]["timeout_seconds"]),
        )
        probe = client.request("probe")
        checks = {
            "engine": name,
            "family": expected["family"],
            "version": expected["version"],
            "config_sha256": expected["config_sha256"],
        }
        mismatches = {
            key: {"expected": value, "actual": probe.get(key)}
            for key, value in checks.items()
            if probe.get(key) != value
        }
        if mismatches:
            client.close()
            raise ValueError(f"competitor probe mismatch: {mismatches}")

        def convert(text: str) -> str:
            response = client.request("convert", text=text)
            output = response.get("output")
            if not isinstance(output, str):
                raise RuntimeError("adapter output must be a string")
            return output

        return Engine(
            name=name,
            available=True,
            convert=convert,
            version=probe["version"],
            family=probe["family"],
            adapter="container_jsonl",
            environment_sha256=actual_environment,
            image_id=image_id,
            config_sha256=probe["config_sha256"],
        )
    except Exception as exc:
        if client is not None:
            client.close()
        return Engine(
            name=name,
            available=False,
            error=str(exc),
            family=expected.get("family"),
            adapter="container_jsonl",
            environment_sha256=expected_environment,
        )


def load_engines(
    names: list[str],
    *,
    lock: dict[str, Any] | None = None,
    container_image: str | None = None,
) -> list[Engine]:
    engines: list[Engine] = []
    for name in names:
        if name == "zhtw" or container_image is None:
            engines.append(ENGINE_LOADERS[name]())
        elif lock is None:
            engines.append(Engine(name=name, available=False, error="competitor lock is required"))
        else:
            engines.append(load_container_engine(name, lock=lock, image=container_image))
    return engines


def run_cases(cases: list[Case], engines: list[Engine]) -> list[dict[str, Any]]:
    available = [engine for engine in engines if engine.available and engine.convert is not None]
    rows: list[dict[str, Any]] = []

    for case in cases:
        outputs: dict[str, str] = {}
        engine_errors: dict[str, str] = {}
        for engine in available:
            try:
                outputs[engine.name] = engine.convert(case.input)  # type: ignore[misc]
            except Exception as exc:
                engine_errors[engine.name] = str(exc)

        rows.append(
            {
                "id": case.id,
                "domain": case.domain,
                "risk": case.risk,
                "notes": case.notes,
                "input": case.input,
                "expected": case.expected,
                "outputs": outputs,
                "errors": engine_errors,
                "classification": classify(case.expected, outputs),
            }
        )

    return rows


def classify(expected: str, outputs: dict[str, str]) -> str:
    zhtw_output = outputs.get("zhtw")
    competitor_outputs = {name: output for name, output in outputs.items() if name != "zhtw"}

    if zhtw_output != expected:
        if any(output == expected for output in competitor_outputs.values()):
            return "candidate_gap"
        return "zhtw_miss"

    if not competitor_outputs:
        return "zhtw_only"

    if all(output == expected for output in competitor_outputs.values()):
        return "all_match"

    return "zhtw_advantage"


def summarize(rows: list[dict[str, Any]]) -> Counter[str]:
    return Counter(row["classification"] for row in rows)


def result_payload(
    case_file: Path,
    engines: list[Engine],
    rows: list[dict[str, Any]],
) -> dict[str, Any]:
    return {
        "case_file": str(case_file),
        "engines": {
            engine.name: {
                "available": engine.available,
                "version": engine.version,
                "error": engine.error,
                "family": engine.family,
                "adapter": engine.adapter,
                "environment_sha256": engine.environment_sha256,
                "image_id": engine.image_id,
                "config_sha256": engine.config_sha256,
            }
            for engine in engines
        },
        "summary": dict(sorted(summarize(rows).items())),
        "rows": rows,
    }


def print_text_report(payload: dict[str, Any], limit: int) -> None:
    rows = payload["rows"]
    summary = Counter(payload["summary"])

    print("zhtw precision competitor benchmark")
    print(f"Case file: {payload['case_file']}")
    print(f"Cases: {len(rows)}")
    print()

    print("Engines:")
    for name, engine in payload["engines"].items():
        if engine["available"]:
            version = f" {engine['version']}" if engine["version"] else ""
            print(f"  {name}: available{version}")
        else:
            print(f"  {name}: skipped ({engine['error']})")
    print()

    print("Summary:")
    for key in ("candidate_gap", "zhtw_miss", "zhtw_advantage", "all_match", "zhtw_only"):
        print(f"  {key}: {summary.get(key, 0)}")

    selected = [
        row
        for category in ("candidate_gap", "zhtw_miss", "zhtw_advantage")
        for row in rows
        if row["classification"] == category
    ]
    if limit >= 0:
        selected = selected[:limit]

    if not selected:
        return

    print()
    print("Rows:")
    for row in selected:
        print(f"  [{row['classification']}] {row['id']} ({row['domain']})")
        print(f"    input: {row['input']}")
        print(f"    expected: {row['expected']}")
        for engine, output in row["outputs"].items():
            print(f"    {engine}: {output}")
        if row["notes"]:
            print(f"    notes: {row['notes']}")


def write_output(payload: dict[str, Any], output: Path | None, as_json: bool, limit: int) -> None:
    if as_json:
        text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    else:
        buffer = StringIO()
        with redirect_stdout(buffer):
            print_text_report(payload, limit)
        text = buffer.getvalue()

    if output is None:
        print(text, end="")
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--cases",
        type=Path,
        default=DEFAULT_CASES,
        help=f"Case fixture path. Default: {DEFAULT_CASES}",
    )
    parser.add_argument(
        "--engines",
        type=parse_engines,
        default=parse_engines("zhtw,opencc-s2twp,zhconv-zh-tw"),
        help="Comma-separated engines. Default: zhtw,opencc-s2twp,zhconv-zh-tw",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Output format. Default: text",
    )
    parser.add_argument("--output", type=Path, help="Write report to a file instead of stdout.")
    parser.add_argument("--competitors-lock", type=Path, default=DEFAULT_LOCK)
    parser.add_argument(
        "--competitor-image",
        help="Use the locked Docker image for every non-zhtw engine.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=50,
        help="Maximum detailed rows in text output. Use -1 for all. Default: 50",
    )
    parser.add_argument(
        "--fail-on-zhtw-mismatch",
        action="store_true",
        help="Exit 1 if zhtw output differs from the manually curated expected output.",
    )
    args = parser.parse_args()

    cases = load_cases(args.cases)
    lock = json.loads(args.competitors_lock.read_text(encoding="utf-8"))
    engines = load_engines(
        args.engines,
        lock=lock,
        container_image=args.competitor_image,
    )
    rows = run_cases(cases, engines)
    payload = result_payload(args.cases, engines, rows)
    write_output(payload, args.output, args.format == "json", args.limit)

    if args.fail_on_zhtw_mismatch:
        if any(row["outputs"].get("zhtw") != row["expected"] for row in rows):
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
