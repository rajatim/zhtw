"""Tests for the legacy novel quality-audit entry point."""

# zhtw:disable  # Simplified inputs are required by these regressions.

from scripts.quality_audit import convert, load_converter
from zhtw import convert as public_convert


def test_quality_audit_uses_canonical_converter() -> None:
    """Audit output must match identity protection in the public pipeline."""
    converter = load_converter()
    source = "党太尉吃匾食"

    assert convert(source, converter) == public_convert(source, sources=["cn"])
    assert convert(source, converter) == "党太尉吃匾食"
