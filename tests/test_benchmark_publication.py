"""Publication-safety tests for accuracy benchmark reports."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

import scripts.run_accuracy_benchmark as benchmark_runner
from scripts.audit_benchmark_publication import audit_paths, find_sensitive_values
from scripts.competitor_benchmark import Engine
from scripts.run_accuracy_benchmark import assert_output_policy

ROOT = Path(__file__).resolve().parents[1]
AUDITOR = ROOT / "scripts" / "audit_benchmark_publication.py"


def test_publication_audit_allows_top_level_expected_hash() -> None:
    payload = {
        "report_mode": "aggregate",
        "expected_sha256": "a" * 64,
        "engines": {"zhtw": {"scores": {"misses": 2}}},
    }

    assert find_sensitive_values(payload) == []


@pytest.mark.parametrize(
    ("payload", "finding"),
    [
        ({"rows": []}, "$.rows"),
        ({"case": {"expected": "value"}}, "$.case.expected"),
        ({"case": {"output": "value"}}, "$.case.output"),
        ({"summary": {"miss_case_ids": ["case-1"]}}, "$.summary.miss_case_ids"),
        ({"source": "benchmarks/accuracy/blind-v2.expected.json"}, "$.source"),
    ],
)
def test_publication_audit_detects_sensitive_fields(
    payload: dict[str, object], finding: str
) -> None:
    assert finding in find_sensitive_values(payload)


def test_publication_audit_rejects_sensitive_aggregate_file(tmp_path: Path) -> None:
    report = tmp_path / "report.json"
    report.write_text(
        json.dumps({"report_mode": "aggregate", "rows": [{"expected": "secret"}]}),
        encoding="utf-8",
    )

    errors = audit_paths([report])

    assert errors
    assert "forbidden $.rows" in errors[0]


def test_publication_audit_rejects_detailed_markdown(tmp_path: Path) -> None:
    report = tmp_path / "report.md"
    report.write_text(
        "# Accuracy Benchmark\n\n## Misses\n\nExpected:\n\nsecret\n",
        encoding="utf-8",
    )

    errors = audit_paths([report])

    assert any("## Misses" in error for error in errors)
    assert any("Expected:" in error for error in errors)


def test_detailed_report_rejects_unignored_repository_path(tmp_path: Path) -> None:
    output_prefix = ROOT / "docs" / "reports" / "private-benchmark-test"

    with pytest.raises(ValueError, match="must be gitignored"):
        assert_output_policy(output_prefix, ["json"], "detailed")

    assert_output_policy(tmp_path / "private-benchmark-test", ["json", "md"], "detailed")


def test_detailed_report_rejects_tracked_path() -> None:
    output_prefix = ROOT / "docs" / "reports" / "accuracy-benchmark-2026-07-19"

    with pytest.raises(ValueError, match="tracked by git"):
        assert_output_policy(output_prefix, ["json"], "detailed")


def test_provenance_rejects_zhtw_version_mismatch(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    (tmp_path / "pyproject.toml").write_text('[project]\nversion = "9.9.9"\n', encoding="utf-8")
    monkeypatch.setattr(benchmark_runner, "PROJECT_ROOT", tmp_path)

    with pytest.raises(ValueError, match="zhtw version mismatch"):
        benchmark_runner.build_provenance([Engine(name="zhtw", available=True, version="4.4.2")])


def test_tracked_benchmark_reports_pass_publication_audit() -> None:
    result = subprocess.run(
        [sys.executable, str(AUDITOR)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr
