"""Reproducibility tests for the generated character map."""

from __future__ import annotations

import io
import json
from pathlib import Path

import pytest

import scripts.generate_charmap as generator

ROOT = Path(__file__).resolve().parents[1]


class _Response(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *_args):
        self.close()


def test_unihan_source_is_pinned() -> None:
    """The generator must not follow a moving Unicode alias."""
    assert "/latest/" not in generator.UNIHAN_URL
    assert generator.UNIHAN_VERSION in generator.UNIHAN_URL
    assert len(generator.UNIHAN_SHA256) == 64


def test_download_unihan_rejects_checksum_mismatch(monkeypatch) -> None:
    """Unexpected upstream bytes must fail before generation."""
    monkeypatch.setattr(generator, "urlopen", lambda _url: _Response(b"changed"))

    with pytest.raises(RuntimeError, match="checksum mismatch"):
        generator.download_unihan()


def test_committed_charmap_records_pinned_source() -> None:
    """Generated output records enough source data for an exact rebuild."""
    path = ROOT / "src/zhtw/data/charmap/safe_chars.json"
    data = json.loads(path.read_text(encoding="utf-8"))

    assert data["source_metadata"] == {
        "unicode_version": generator.UNIHAN_VERSION,
        "url": generator.UNIHAN_URL,
        "sha256": generator.UNIHAN_SHA256,
    }
    reviewed_ambiguity_regressions = set("伙佣吁姜旋沈症范蔑")
    assert reviewed_ambiguity_regressions <= set(data["ambiguous_excluded"])
    assert reviewed_ambiguity_regressions.isdisjoint(data["chars"])
