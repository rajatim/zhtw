"""Validate optional zhtw-test-corpus samples.

The corpus lives in a separate repository so Simplified Chinese inputs are not
rewritten by this repository's hooks. These tests run when the corpus has been
cloned to ``tests/data/corpus`` and otherwise skip cleanly.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from zhtw.converter import convert

CORPUS_DIR = Path(__file__).parent / "data" / "corpus"
CURATED_CATEGORIES = ("news", "regressions", "social", "tech", "wiki")


def _sample_files() -> list[Path]:
    if not CORPUS_DIR.exists():
        return []
    files: list[Path] = []
    for category in CURATED_CATEGORIES:
        files.extend((CORPUS_DIR / category).glob("*.json"))
    return sorted(files)


def _load_cases() -> list[Any]:
    cases: list[Any] = []
    for path in _sample_files():
        data: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
        for case in data.get("corpus", []):
            case_id = case.get("id", path.stem)
            cases.append(
                pytest.param(
                    case["input"],
                    case["expected"],
                    id=f"{path.parent.name}/{case_id}",
                )
            )
    return cases


CORPUS_CASES = _load_cases()


@pytest.mark.skipif(
    not CORPUS_CASES,
    reason="zhtw-test-corpus 未下載（git clone 到 tests/data/corpus）",
)
@pytest.mark.parametrize("source,expected", CORPUS_CASES)
def test_corpus_samples_match_expected(source: str, expected: str) -> None:
    assert convert(source) == expected


@pytest.mark.skipif(
    not CORPUS_CASES,
    reason="zhtw-test-corpus 未下載（git clone 到 tests/data/corpus）",
)
@pytest.mark.parametrize("source,expected", CORPUS_CASES)
def test_corpus_samples_are_idempotent(source: str, expected: str) -> None:
    assert convert(convert(source)) == expected
