"""Tests for checksum-pinned paired vendor localization benchmarks."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from scripts.benchmark_metrics import canonical_json_bytes
from scripts.competitor_benchmark import load_zhtw
from scripts.import_paired_localization_benchmark import (
    build_dataset,
    parse_android_xml,
    parse_fluent,
    parse_vscode_json,
    placeholder_signature,
)
from scripts.run_paired_localization_benchmark import score_engine
from scripts.validate_benchmark_assets import validate_manifest

ROOT = Path(__file__).resolve().parent.parent
TRACKS = {
    "aosp-framework-paired-ui-v1": (1968, "blind_v2_source_pool"),
    "vscode-paired-ui-v1": (17133, "blind_v2_source_pool"),
    "firefox-paired-ui-v1": (1264, "none_known"),
}


def test_android_parser_supports_product_variants_and_rejects_markup() -> None:
    values, excluded = parse_android_xml(
        """<resources xmlns:x='urn:test'>
        <string name='plain'>"软件"</string>
        <string name='device' product='tablet'>"平板电脑"</string>
        <string name='format'>"%1$s 文件"</string>
        <string name='markup'><b>text</b></string>
        </resources>""".encode(),
        source="fixture.xml",
    )
    assert values == {
        "device[product=tablet]": "平板电脑",
        "format": "%1$s 文件",
        "plain": "软件",
    }
    assert excluded == {"rich_markup": 1}


def test_vscode_parser_flattens_structured_message_keys() -> None:
    content = json.dumps(
        {"version": "1", "contents": {"module": {"title": "打开 {0}"}}},
        ensure_ascii=False,
    ).encode()
    values, excluded = parse_vscode_json(content, source="fixture.json")
    assert values == {"module/title": "打开 {0}"}
    assert not excluded


def test_fluent_parser_keeps_plain_text_and_rejects_expressions() -> None:
    values, excluded = parse_fluent(
        "plain = 打开文件\nvariable = 打开 { $name }\n    .label = 关闭\n".encode(),
        source="fixture.ftl",
    )
    assert values == {"plain": "打开文件", "variable.label": "关闭"}
    assert excluded == {"fluent_expression": 1}


def test_pair_builder_rejects_placeholder_mismatches_and_duplicate_pairs() -> None:
    simplified_url = "https://example.test/zh-hans/messages.json"
    traditional_url = "https://example.test/zh-hant/messages.json"
    simplified = json.dumps(
        {
            "contents": {
                "one": "打开 {0}",
                "two": "打开 {0}",
                "bad": "删除 {0}",
                "guard": "API",
            }
        },
        ensure_ascii=False,
    ).encode()
    traditional = json.dumps(
        {
            "contents": {
                "one": "開啟 {0}",
                "two": "開啟 {0}",
                "bad": "刪除 {1}",
                "guard": "API",
            }
        },
        ensure_ascii=False,
    ).encode()
    manifest = {
        "id": "vscode-paired-ui-v1",
        "track": "external_regional",
        "output_license": "MIT License",
        "attribution": "fixture",
        "modification_notice": "fixture",
        "upstream_revision": "fixture",
    }
    dataset = build_dataset(
        manifest,
        {simplified_url: simplified, traditional_url: traditional},
    )
    assert [(case["input"], case["expected"]) for case in dataset["cases"]] == [
        ("打开 {0}", "開啟 {0}")
    ]
    assert dataset["stats"]["excluded"] == {
        "duplicate_pair": 1,
        "no_han_input": 1,
        "placeholder_mismatch": 1,
    }


def test_committed_paired_datasets_are_pinned_and_conservative() -> None:
    for track_id, (expected_cases, overlap) in TRACKS.items():
        manifest_path = ROOT / "benchmarks/accuracy/manifests" / f"{track_id}.json"
        dataset_path = ROOT / "benchmarks/accuracy/external" / f"{track_id}.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        dataset = json.loads(dataset_path.read_text(encoding="utf-8"))
        assert not validate_manifest(manifest_path)
        actual_hash = hashlib.sha256(dataset_path.read_bytes()).hexdigest()
        assert actual_hash == manifest["normalized_sha256"]
        assert dataset["stats"]["total_cases"] == expected_cases
        assert dataset["source_overlap"] == overlap
        assert dataset["reference_is_ground_truth"] is False
        assert dataset_path.read_bytes() == canonical_json_bytes(dataset)
        assert len({case["id"] for case in dataset["cases"]}) == expected_cases
        for case in dataset["cases"]:
            assert "\n" not in case["input"]
            assert placeholder_signature(case["input"]) == placeholder_signature(case["expected"])


def test_aggregate_scorer_does_not_return_case_rows() -> None:
    dataset = {
        "cases": [
            {
                "file": "fixture",
                "input": "软件设置",
                "expected": "軟體設定",
            }
        ]
    }
    score, exact = score_engine(dataset, load_zhtw())
    assert exact == [True]
    assert score["exact"] == 1
    assert "cases" not in score
