"""Freeze the effective 4.4.5 behavior before the schema-v2 migration."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from zhtw.charconv import (
    get_ambiguous_chars,
    get_balanced_defaults,
    get_protect_terms,
    load_charmap,
)
from zhtw.dictionary import DATA_DIR, load_dictionary, load_directory
from zhtw.export import export_data

ROOT = Path(__file__).resolve().parent.parent
BASELINE_PATH = ROOT / "tests/data/compatibility/v4.4.5-baseline.json"
SHARED_DATA_PATH = ROOT / "sdk/data/zhtw-data.json"
GOLDEN_DATA_PATH = ROOT / "sdk/data/golden-test.json"


def _canonical_sha256(value: Any) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _assert_count_and_digest(value: Any, expected: dict[str, Any]) -> None:
    assert len(value) == expected["count"]
    assert _canonical_sha256(value) == expected["sha256"]


def test_effective_term_maps_match_v445() -> None:
    baseline = _load_json(BASELINE_PATH)["effective_terms"]

    _assert_count_and_digest(load_directory(DATA_DIR / "cn"), baseline["cn"])
    _assert_count_and_digest(load_directory(DATA_DIR / "hk"), baseline["hk"])
    _assert_count_and_digest(load_dictionary(), baseline["cn_then_hk"])


def test_charmap_layers_match_v445() -> None:
    baseline = _load_json(BASELINE_PATH)["charmap"]

    _assert_count_and_digest(load_charmap(), baseline["chars"])
    _assert_count_and_digest(sorted(get_ambiguous_chars()), baseline["ambiguous"])
    _assert_count_and_digest(get_balanced_defaults(), baseline["balanced_defaults"])

    protect_terms = get_protect_terms()
    assert (
        sum(len(values) for values in protect_terms.values())
        == baseline["balanced_protect_terms"]["count"]
    )
    assert _canonical_sha256(protect_terms) == baseline["balanced_protect_terms"]["sha256"]


def test_exported_effective_data_matches_v445() -> None:
    baseline = _load_json(BASELINE_PATH)["shared_data"]
    exported = export_data()

    assert sum(len(values) for values in exported["terms"].values()) == baseline["terms_count"]
    assert _canonical_sha256(exported["terms"]) == baseline["terms_sha256"]
    assert _canonical_sha256(exported["charmap"]) == baseline["charmap_sha256"]


def test_tracked_shared_data_preserves_v445_effective_content() -> None:
    baseline = _load_json(BASELINE_PATH)["shared_data"]
    shared = _load_json(SHARED_DATA_PATH)

    assert _canonical_sha256(shared["terms"]) == baseline["terms_sha256"]
    assert _canonical_sha256(shared["charmap"]) == baseline["charmap_sha256"]
    if shared["schema_version"] == baseline["schema_version"]:
        assert (
            hashlib.sha256(SHARED_DATA_PATH.read_bytes()).hexdigest() == baseline["artifact_sha256"]
        )


def test_golden_behavior_matches_v445() -> None:
    baseline = _load_json(BASELINE_PATH)["golden_data"]
    golden = _load_json(GOLDEN_DATA_PATH)

    for section in ("convert", "check", "lookup"):
        assert _canonical_sha256(golden[section]) == baseline[f"{section}_sha256"]
    if golden["schema_version"] == baseline["schema_version"]:
        assert (
            hashlib.sha256(GOLDEN_DATA_PATH.read_bytes()).hexdigest() == baseline["artifact_sha256"]
        )
