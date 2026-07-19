"""Tests for the pinned NAER computer terminology benchmark track."""

from __future__ import annotations

import csv
import hashlib
import io
import json
from pathlib import Path

import pytest

from scripts.benchmark_metrics import canonical_json_bytes
from scripts.import_naer_terms_benchmark import build_dataset, parse_csv, structure_cell
from scripts.run_naer_terms_benchmark import build_report
from scripts.validate_benchmark_assets import validate_manifest

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "benchmarks" / "accuracy" / "manifests" / "naer-terms-v1.json"
DATASET = ROOT / "benchmarks" / "accuracy" / "external" / "naer-terms-v1.json"
HEADERS = ("序號", "英文名稱", "中文名稱", "中國大陸譯名", "來源網站")


def csv_bytes(*rows: tuple[str, str, str, str, str]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.writer(output)
    writer.writerow(HEADERS)
    writer.writerows(rows)
    return ("\ufeff" + output.getvalue()).encode()


def fixture_manifest(tmp_path: Path, content: bytes) -> tuple[dict[str, object], Path]:
    source = tmp_path / "naer.csv"
    source.write_bytes(content)
    return (
        {
            "id": "naer-fixture-v1",
            "track": "external_terminology",
            "output_license": "Government Data Open License 1.0",
            "attribution": "Fixture",
            "modification_notice": "Fixture extraction",
            "upstream_revision": "fixture-revision",
            "raw_sha256": {"https://example.test/naer.csv": hashlib.sha256(content).hexdigest()},
        },
        source,
    )


def test_structure_cell_does_not_guess_multi_value_segments() -> None:
    cell = structure_cell("位址；地址")

    assert cell == {
        "raw": "位址；地址",
        "status": "unresolved_compound",
        "values": [],
        "markers": ["multi_value_delimiter"],
    }


def test_importer_classifies_and_deduplicates_candidates(tmp_path: Path) -> None:
    content = csv_bytes(
        ("1", "software", "軟體", "软件", "https://terms.naer.edu.tw/"),
        ("2", "software duplicate", "軟體", "软件", "https://terms.naer.edu.tw/"),
        ("3", "accelerator", "加速器", "加速器", "https://terms.naer.edu.tw/"),
        ("4", "address", "位址；地址", "访问", "https://terms.naer.edu.tw/"),
        ("5", "visit", "造訪", "访问", "https://terms.naer.edu.tw/"),
        ("6", "access", "存取", "访问", "https://terms.naer.edu.tw/"),
    )
    manifest, source = fixture_manifest(tmp_path, content)

    first = build_dataset(manifest, source_file=source)
    second = build_dataset(manifest, source_file=source)

    assert canonical_json_bytes(first) == canonical_json_bytes(second)
    assert first["stats"] == {
        "source_records": 6,
        "evaluation_cases": 2,
        "conversion_cases": 1,
        "identity_guard_cases": 1,
        "context_candidates": 3,
    }
    conversion = next(case for case in first["evaluation_cases"] if case["kind"] == "conversion")
    assert conversion["input"] == "软件"
    assert conversion["expected"] == "軟體"
    assert len(conversion["source_record_ids"]) == 2
    assert all("expected" not in case for case in first["context_candidates"])


def test_importer_rejects_schema_drift_and_duplicate_sequences() -> None:
    with pytest.raises(ValueError, match="unexpected CSV headers"):
        parse_csv(b"wrong,header\n1,2\n", source="fixture")

    content = csv_bytes(
        ("1", "software", "軟體", "软件", "https://terms.naer.edu.tw/"),
        ("1", "hardware", "硬體", "硬件", "https://terms.naer.edu.tw/"),
    )
    with pytest.raises(ValueError, match="duplicate sequence"):
        parse_csv(content, source="fixture")


def test_importer_merges_nfkc_near_duplicates(tmp_path: Path) -> None:
    content = csv_bytes(
        ("1", "API", "API介面", "ＡＰＩ", "https://terms.naer.edu.tw/"),
        ("2", "api", "API介面", "API", "https://terms.naer.edu.tw/"),
    )
    manifest, source = fixture_manifest(tmp_path, content)

    dataset = build_dataset(manifest, source_file=source)

    assert dataset["stats"]["evaluation_cases"] == 1
    assert dataset["evaluation_cases"][0]["source_record_ids"] == [
        "naer-fixture-v1/source/0001",
        "naer-fixture-v1/source/0002",
    ]


def test_committed_naer_dataset_is_pinned_and_conservative() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    dataset = json.loads(DATASET.read_text(encoding="utf-8"))

    assert validate_manifest(MANIFEST) == []
    assert hashlib.sha256(DATASET.read_bytes()).hexdigest() == manifest["normalized_sha256"]
    assert dataset["stats"]["source_records"] == len(dataset["source_records"]) == 1532
    assert dataset["stats"]["evaluation_cases"] == len(dataset["evaluation_cases"])
    assert dataset["stats"]["context_candidates"] == len(dataset["context_candidates"])
    assert dataset["classification_policy"]["product_import"] == "prohibited"
    assert dataset["context_review_protocol"]["status"] == "candidate_packet_only"
    assert all("expected" not in case for case in dataset["context_candidates"])
    assert len({case["id"] for case in dataset["evaluation_cases"]}) == len(
        dataset["evaluation_cases"]
    )


def test_naer_report_contains_guard_and_conversion_metrics() -> None:
    report = build_report(
        manifest_path=MANIFEST,
        dataset_path=DATASET,
        generated_date="2026-07-19",
    )
    scores = report["scores"]

    assert report["report_mode"] == "aggregate"
    assert report["evidence_role"] == "secondary_evidence"
    assert report["primary_market_endpoint"] is False
    assert scores["total_cases"] > 0
    assert scores["excluded_context_candidates"] > 0
    assert set(scores["by_candidate_set"]) == {"conversion", "identity_guard"}
    assert scores["accepted_accuracy"] == scores["primary_exact_accuracy"]
    assert scores["identity_guard_accuracy"] == scores["over_conversion_guard_accuracy"]
    assert scores["errors_by_category"] == {}
