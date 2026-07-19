"""Tests for the pinned UD Chinese GSD/GSDSimp benchmark track."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from scripts.benchmark_metrics import canonical_json_bytes
from scripts.import_ud_gsd_benchmark import build_dataset, parse_conllu
from scripts.run_ud_gsd_benchmark import build_report
from scripts.validate_benchmark_assets import validate_manifest

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "benchmarks" / "accuracy" / "manifests" / "ud-gsd-v1.json"
DATASET = ROOT / "benchmarks" / "accuracy" / "external" / "ud-gsd-v1.json"


def conllu(*sentences: tuple[str, str]) -> str:
    blocks = []
    for sent_id, text in sentences:
        blocks.append(
            f"# sent_id = {sent_id}\n# text = {text}\n1\t{text}\t_\tX\t_\t_\t0\troot\t_\t_"
        )
    return "\n\n".join(blocks) + "\n\n"


def fixture_sources(tmp_path: Path) -> tuple[dict[str, object], Path, Path]:
    gsd = tmp_path / "gsd"
    gsdsimp = tmp_path / "gsdsimp"
    gsd.mkdir()
    gsdsimp.mkdir()
    raw_sha256: dict[str, str] = {}
    for directory, repository, prefix, texts in (
        (gsd, "UD_Chinese-GSD", "zh_gsd", ("開發", "軟體")),
        (gsdsimp, "UD_Chinese-GSDSimp", "zh_gsdsimp", ("开发", "软件")),
    ):
        license_path = directory / "LICENSE.txt"
        license_path.write_text("CC BY-SA 4.0\n", encoding="utf-8")
        license_url = f"https://raw.example/{repository}/rev/LICENSE.txt"
        raw_sha256[license_url] = hashlib.sha256(license_path.read_bytes()).hexdigest()
        for split in ("train", "dev", "test"):
            path = directory / f"{prefix}-ud-{split}.conllu"
            path.write_text(
                conllu((f"{split}-s1", texts[0]), (f"{split}-s2", texts[1])),
                encoding="utf-8",
            )
            url = f"https://raw.example/{repository}/rev/{path.name}"
            raw_sha256[url] = hashlib.sha256(path.read_bytes()).hexdigest()
    manifest: dict[str, object] = {
        "id": "fixture-v1",
        "track": "external_context",
        "output_license": "CC BY-SA 4.0",
        "attribution": "Fixture",
        "modification_notice": "Fixture extraction",
        "upstream_revision": "fixture-revision",
        "raw_sha256": raw_sha256,
    }
    return manifest, gsd, gsdsimp


def test_importer_pairs_unique_sent_ids_offline(tmp_path: Path) -> None:
    manifest, gsd, gsdsimp = fixture_sources(tmp_path)

    first = build_dataset(manifest, gsd_dir=gsd, gsdsimp_dir=gsdsimp)
    second = build_dataset(manifest, gsd_dir=gsd, gsdsimp_dir=gsdsimp)

    assert first["stats"] == {
        "total_cases": 6,
        "by_split": {"train": 2, "dev": 2, "test": 2},
        "by_genre": {"wiki": 6},
    }
    assert first["cases"][0] == {
        "id": "fixture-v1/train-s1",
        "sent_id": "train-s1",
        "split": "train",
        "genre": "wiki",
        "input": "开发",
        "expected": "開發",
    }
    assert canonical_json_bytes(first) == canonical_json_bytes(second)


def test_importer_rejects_duplicate_sent_id() -> None:
    content = conllu(("dup", "第一句"), ("dup", "第二句"))

    with pytest.raises(ValueError, match="duplicate sent_id"):
        parse_conllu(content, source="fixture")


def test_importer_rejects_missing_text() -> None:
    content = "# sent_id = missing-text\n1\t文字\t_\tX\t_\t_\t0\troot\t_\t_\n\n"

    with pytest.raises(ValueError, match="missing sent_id or text"):
        parse_conllu(content, source="fixture")


def test_importer_rejects_mismatched_sent_ids(tmp_path: Path) -> None:
    manifest, gsd, gsdsimp = fixture_sources(tmp_path)
    path = gsdsimp / "zh_gsdsimp-ud-test.conllu"
    path.write_text(conllu(("test-other", "其他")), encoding="utf-8")
    raw_sha256 = manifest["raw_sha256"]
    assert isinstance(raw_sha256, dict)
    url = next(key for key in raw_sha256 if key.endswith("zh_gsdsimp-ud-test.conllu"))
    raw_sha256[url] = hashlib.sha256(path.read_bytes()).hexdigest()

    with pytest.raises(ValueError, match="sent_id mismatch"):
        build_dataset(manifest, gsd_dir=gsd, gsdsimp_dir=gsdsimp)


def test_committed_ud_dataset_is_pinned_and_complete() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    dataset = json.loads(DATASET.read_text(encoding="utf-8"))

    assert validate_manifest(MANIFEST) == []
    assert hashlib.sha256(DATASET.read_bytes()).hexdigest() == manifest["normalized_sha256"]
    assert manifest["license"] == manifest["output_license"] == "CC BY-SA 4.0"
    assert dataset["stats"]["total_cases"] == len(dataset["cases"]) == 4997
    assert dataset["stats"]["by_split"] == {"train": 3997, "dev": 500, "test": 500}
    assert dataset["source_bias"] == "opencc_derived_source_bias"
    assert dataset["evidence_role"] == "secondary_evidence"
    assert dataset["primary_market_endpoint"] is False
    case_ids = [case["id"] for case in dataset["cases"]]
    sent_ids = [case["sent_id"] for case in dataset["cases"]]
    assert len(case_ids) == len(set(case_ids))
    assert len(sent_ids) == len(set(sent_ids))


def test_ud_report_contains_required_secondary_metrics() -> None:
    report = build_report(
        manifest_path=MANIFEST,
        dataset_path=DATASET,
        generated_date="2026-07-19",
    )
    scores = report["scores"]

    assert report["report_mode"] == "aggregate"
    assert report["evidence_role"] == "secondary_evidence"
    assert report["primary_market_endpoint"] is False
    assert report["source_bias"] == "opencc_derived_source_bias"
    assert scores["total_cases"] == 4997
    assert scores["exact"] == 3517
    assert scores["misses"] == 1480
    assert scores["errors_by_category"] == {}
    assert scores["changed_span"]["f1"] == pytest.approx(0.9421875211798354)
    assert scores["idempotency_rate"] == pytest.approx(0.9789873924354613)
    assert scores["by_genre"]["wiki"]["total"] == 4997
