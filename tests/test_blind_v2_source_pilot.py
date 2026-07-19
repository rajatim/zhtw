"""Tests for pinned Blind-v2 input-only source pilots."""

from __future__ import annotations

import hashlib
import io
import json
import tarfile
from pathlib import Path
from typing import Any

import pytest

from scripts.benchmark_metrics import canonical_json_bytes
from scripts.import_blind_v2_source_pilot import build_dataset, normalize_input, validate_dataset
from scripts.validate_benchmark_assets import validate_manifest

ROOT = Path(__file__).resolve().parents[1]
ACCURACY_ROOT = ROOT / "benchmarks" / "accuracy"
MANIFESTS = ACCURACY_ROOT / "manifests"
EXTERNAL = ACCURACY_ROOT / "external"
FORBIDDEN_KEYS = {"expected", "acceptable", "annotation", "output", "normalized_output"}


def flores_archive(dev: list[str], devtest: list[str]) -> bytes:
    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode="w:gz") as archive:
        for name, lines in (
            ("./flores200_dataset/dev/zho_Hans.dev", dev),
            ("./flores200_dataset/devtest/zho_Hans.devtest", devtest),
        ):
            content = ("\n".join(lines) + "\n").encode()
            info = tarfile.TarInfo(name)
            info.size = len(content)
            archive.addfile(info, io.BytesIO(content))
    return buffer.getvalue()


def manifest(source_id: str, source: Path) -> dict[str, Any]:
    return {
        "id": source_id,
        "raw_sha256": {
            "https://example.test/source": hashlib.sha256(source.read_bytes()).hexdigest()
        },
        "normalized_path": "unused.json",
        "output_license": "CC BY-SA 4.0",
        "attribution": "Fixture contributors.",
        "modification_notice": "Input-only fixture extraction.",
        "upstream_revision": "fixture-revision",
    }


def find_forbidden_keys(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            if key in FORBIDDEN_KEYS:
                found.add(key)
            found.update(find_forbidden_keys(child))
    elif isinstance(value, list):
        for child in value:
            found.update(find_forbidden_keys(child))
    return found


def test_flores_import_is_deterministic_input_only_and_deduplicated(tmp_path: Path) -> None:
    source = tmp_path / "flores.tar.gz"
    source.write_bytes(flores_archive(["开发  工具", "重复句"], ["重复句", "用户界面"]))
    fixture = manifest("flores-200-zho-hans-v1", source)

    first = build_dataset(fixture, source_file=source)
    second = build_dataset(fixture, source_file=source)

    assert first["stats"] == {
        "raw_cases": 4,
        "eligible_pending_review": 3,
        "by_split": {"dev": 2, "devtest": 1},
        "exclusions": {"exact_duplicate_within_source": 1},
    }
    assert first["cases"][0]["input"] == "开发 工具"
    assert first["cases"][0]["classification"] == {
        "domain": None,
        "risk": None,
        "status": "needs_input_only_review",
    }
    assert find_forbidden_keys(first) == set()
    assert validate_dataset(first) == []
    assert canonical_json_bytes(first) == canonical_json_bytes(second)


def test_ud_cfl_import_rejects_incomplete_conllu(tmp_path: Path) -> None:
    source = tmp_path / "cfl.conllu"
    source.write_text(
        "# sent_id = missing-text\n1\t文字\t_\tX\t_\t_\t0\troot\t_\t_\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="missing sent_id or text"):
        build_dataset(manifest("ud-chinese-cfl-v1", source), source_file=source)


def test_normalization_does_not_convert_script() -> None:
    assert normalize_input("开发  软件\r\n接口") == "开发 软件 接口"


@pytest.mark.parametrize(
    ("source_id", "expected_cases"),
    (("flores-200-zho-hans-v1", 2009), ("ud-chinese-cfl-v1", 451)),
)
def test_committed_source_pilots_are_pinned_and_input_only(
    source_id: str, expected_cases: int
) -> None:
    manifest_path = MANIFESTS / f"{source_id}.json"
    dataset_path = EXTERNAL / f"{source_id}.json"
    source_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    dataset = json.loads(dataset_path.read_text(encoding="utf-8"))

    assert validate_manifest(manifest_path) == []
    assert (
        hashlib.sha256(dataset_path.read_bytes()).hexdigest()
        == source_manifest["normalized_sha256"]
    )
    assert dataset["input_only"] is True
    assert dataset["converter_output_used"] is False
    assert dataset["stats"]["eligible_pending_review"] == len(dataset["cases"]) == expected_cases
    assert find_forbidden_keys(dataset) == set()
    assert all(case["classification"]["domain"] is None for case in dataset["cases"])
    assert all(case["classification"]["risk"] is None for case in dataset["cases"])
