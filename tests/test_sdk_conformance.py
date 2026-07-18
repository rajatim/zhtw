"""Independent cross-SDK cases that export must never rewrite."""

import json
from pathlib import Path

import pytest

from zhtw.converter import convert

CONFORMANCE = json.loads(
    (Path(__file__).parents[1] / "sdk" / "data" / "conformance-v1.json").read_text("utf-8")
)


def test_conformance_schema_version():
    assert CONFORMANCE["schema_version"] == 1


@pytest.mark.parametrize("case", CONFORMANCE["convert"], ids=lambda case: case["id"])
def test_approved_sdk_conformance(case):
    assert convert(case["input"], sources=case["sources"]) == case["expected"]
