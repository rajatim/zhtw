# zhtw:disable  # 測試會處理簡體 corpus input
"""Tests for competitor difference discovery."""

from __future__ import annotations

import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import discover_competitor_diffs as discover  # noqa: E402
from competitor_benchmark import Engine  # noqa: E402


def engine(name: str, mapping: dict[str, str]) -> Engine:
    return Engine(name=name, available=True, version="test", convert=lambda text: mapping[text])


def case(expected: str | None = "正確") -> discover.CorpusCase:
    return discover.CorpusCase(
        id="case_001",
        category="tech",
        source_file=ROOT / "tests" / "data" / "corpus" / "tech" / "samples.json",
        input="输入",
        expected=expected,
        tags=("unit",),
        notes="note",
    )


@pytest.mark.parametrize(
    ("expected", "outputs", "classification"),
    [
        ("正確", {"zhtw": "錯", "opencc-s2twp": "正確", "zhconv-zh-tw": "錯"}, "candidate_gap"),
        ("正確", {"zhtw": "正確", "opencc-s2twp": "錯", "zhconv-zh-tw": "正確"}, "zhtw_advantage"),
        ("正確", {"zhtw": "錯", "opencc-s2twp": "錯", "zhconv-zh-tw": "也錯"}, "all_wrong"),
        ("正確", {"zhtw": "正確", "opencc-s2twp": "正確", "zhconv-zh-tw": "正確"}, "all_match"),
    ],
)
def test_classify_with_expected(
    expected: str,
    outputs: dict[str, str],
    classification: str,
) -> None:
    assert discover.classify_with_expected(expected, outputs) == classification


@pytest.mark.parametrize(
    ("outputs", "classification"),
    [
        ({"zhtw": "A", "opencc-s2twp": "B", "zhconv-zh-tw": "B"}, "competitors_agree"),
        ({"zhtw": "A", "opencc-s2twp": "B", "zhconv-zh-tw": "C"}, "all_different"),
        ({"zhtw": "A", "opencc-s2twp": "A", "zhconv-zh-tw": "B"}, "zhconv_unique"),
    ],
)
def test_classify_without_expected(outputs: dict[str, str], classification: str) -> None:
    assert discover.classify_without_expected(outputs) == classification


def test_run_cases_includes_provenance_and_versions() -> None:
    corpus_case = case()
    engines = [
        engine("zhtw", {"输入": "錯"}),
        engine("opencc-s2twp", {"输入": "正確"}),
        engine("zhconv-zh-tw", {"输入": "錯"}),
    ]

    rows = discover.run_cases([corpus_case], engines, sample_seed=7)

    assert len(rows) == 1
    row = rows[0]
    assert row["classification"] == "candidate_gap"
    assert row["source_file"] == "tests/data/corpus/tech/samples.json"
    assert row["case_id"] == "case_001"
    assert row["sample_seed"] == 7
    assert row["corpus_expected"] == "正確"
    assert row["engine_versions"] == {
        "zhtw": "test",
        "opencc-s2twp": "test",
        "zhconv-zh-tw": "test",
    }


def test_markdown_report_is_protected() -> None:
    payload = discover.build_payload(
        corpus_dir=ROOT / "tests" / "data" / "corpus",
        categories=["tech"],
        total_cases=1,
        selected_cases=[case()],
        engines=[engine("zhtw", {"输入": "正確"})],
        rows=[],
        scanned_summary=Counter({"all_match": 1}),
        limit=1,
        seed=42,
    )

    assert discover.format_markdown(payload).startswith("<!-- zhtw:disable -->\n")


def test_cli_writes_json_with_zhtw_only(tmp_path: Path) -> None:
    corpus_dir = tmp_path / "corpus"
    category_dir = corpus_dir / "tech"
    category_dir.mkdir(parents=True)
    (category_dir / "samples.json").write_text(
        json.dumps(
            {
                "corpus": [
                    {
                        "id": "sample_001",
                        "input": "软件",
                        "expected": "軟體",
                    }
                ]
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    output = tmp_path / "report.json"

    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "discover_competitor_diffs.py"),
            "--corpus-dir",
            str(corpus_dir),
            "--category",
            "tech",
            "--engines",
            "zhtw",
            "--format",
            "json",
            "--output",
            str(output),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert payload["scanned_cases"] == 1
    assert payload["diff_rows"] == 0
    assert payload["engines"]["zhtw"]["available"] is True
