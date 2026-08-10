"""Tests for deterministic dictionary-target identity guards."""

from __future__ import annotations

import json

from scripts.generate_target_guards import DEFAULT_OUTPUT, generate_guard_terms


def test_target_guards_are_current() -> None:
    """The committed guard file must match a fresh deterministic calculation."""
    payload = json.loads(DEFAULT_OUTPUT.read_text(encoding="utf-8"))

    assert payload["source"] == "scripts/generate_target_guards.py"
    assert payload["terms"] == generate_guard_terms()
    assert payload["terms"]
    assert all(source == target for source, target in payload["terms"].items())
