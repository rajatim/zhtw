#!/usr/bin/env python3
"""Import checksum-pinned Simplified/Traditional vendor localization pairs."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from typing import Any

from fluent.syntax import FluentParser, ast

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.benchmark_metrics import canonical_json_bytes  # noqa: E402

HAN_RE = re.compile(r"[\u3400-\u9fff]")
PLACEHOLDER_RE = re.compile(
    r"%(?:\d+\$)?[-+#0 ,]*(?:\d+|\*)?(?:\.\d+)?[A-Za-z]" r"|\{\d+\}|\$\{[^{}]+\}"
)


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def load_manifest(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("manifest must be a JSON object")
    return value


def read_raw_sources(manifest: dict[str, Any]) -> dict[str, bytes]:
    sources: dict[str, bytes] = {}
    for url, expected_hash in manifest["raw_sha256"].items():
        with urllib.request.urlopen(url, timeout=60) as response:
            content = response.read()
        actual_hash = sha256_bytes(content)
        if actual_hash != expected_hash:
            raise ValueError(f"raw sha256 mismatch for {url}: {actual_hash}")
        sources[url] = content
    return sources


def normalize_text(value: str) -> str:
    return unicodedata.normalize("NFC", value.strip())


def normalize_android_text(value: str) -> str:
    normalized = normalize_text(value)
    if len(normalized) >= 2 and normalized[0] == normalized[-1] == '"':
        normalized = normalized[1:-1]
    return (
        normalized.replace(r"\n", "\n")
        .replace(r"\t", "\t")
        .replace(r"\'", "'")
        .replace(r"\"", '"')
        .replace(r"\\", "\\")
    )


def placeholder_signature(value: str) -> tuple[str, ...]:
    return tuple(PLACEHOLDER_RE.findall(value))


def pair_urls(
    sources: dict[str, bytes], *, simplified_locale: str, traditional_locale: str
) -> list[tuple[str, str, str]]:
    pairs: list[tuple[str, str, str]] = []
    for simplified_url in sorted(sources):
        if simplified_locale not in simplified_url:
            continue
        traditional_url = simplified_url.replace(simplified_locale, traditional_locale, 1)
        if traditional_url not in sources:
            raise ValueError(f"missing paired source: {traditional_url}")
        relative = simplified_url.split(simplified_locale, 1)[1].lstrip("/-_") or "root"
        pairs.append((relative, simplified_url, traditional_url))
    if not pairs:
        raise ValueError("no Simplified/Traditional source pairs found")
    return pairs


def _xml_tag_name(element: ET.Element) -> str:
    return element.tag.rsplit("}", 1)[-1]


def parse_android_xml(content: bytes, *, source: str) -> tuple[dict[str, str], Counter[str]]:
    root = ET.fromstring(content)
    values: dict[str, str] = {}
    excluded: Counter[str] = Counter()
    for element in root:
        if _xml_tag_name(element) != "string":
            excluded["unsupported_resource_type"] += 1
            continue
        name = element.attrib.get("name")
        if not name or element.attrib.get("translatable") == "false":
            excluded["missing_key_or_nontranslatable"] += 1
            continue
        if any(_xml_tag_name(child) != "g" for child in element):
            excluded["rich_markup"] += 1
            continue
        product = element.attrib.get("product")
        key = f"{name}[product={product}]" if product else name
        value = normalize_android_text("".join(element.itertext()))
        if key in values:
            raise ValueError(f"{source}: duplicate Android string key: {key}")
        values[key] = value
    return values, excluded


def _flatten_json(value: Any, prefix: str = "") -> dict[str, str]:
    values: dict[str, str] = {}
    if isinstance(value, str):
        values[prefix] = normalize_text(value)
    elif isinstance(value, dict):
        for key in sorted(value):
            child = f"{prefix}/{key}" if prefix else str(key)
            values.update(_flatten_json(value[key], child))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            child = f"{prefix}/{index}" if prefix else str(index)
            values.update(_flatten_json(item, child))
    return values


def parse_vscode_json(content: bytes, *, source: str) -> tuple[dict[str, str], Counter[str]]:
    value = json.loads(content.decode("utf-8"))
    if not isinstance(value, dict) or not isinstance(value.get("contents"), dict):
        raise ValueError(f"{source}: VS Code localization JSON is missing contents")
    return _flatten_json(value["contents"]), Counter()


def parse_fluent(content: bytes, *, source: str) -> tuple[dict[str, str], Counter[str]]:
    text = content.decode("utf-8")
    resource = FluentParser(with_spans=True).parse(text)
    values: dict[str, str] = {}
    excluded: Counter[str] = Counter()
    for entry in resource.body:
        if isinstance(entry, ast.Junk):
            raise ValueError(f"{source}: Fluent parser found invalid syntax")
        if not isinstance(entry, ast.Message):
            continue
        patterns: list[tuple[str, ast.Pattern]] = []
        if entry.value is not None:
            patterns.append((entry.id.name, entry.value))
        patterns.extend(
            (f"{entry.id.name}.{item.id.name}", item.value) for item in entry.attributes
        )
        for key, pattern in patterns:
            if len(pattern.elements) != 1 or not isinstance(pattern.elements[0], ast.TextElement):
                excluded["fluent_expression"] += 1
                continue
            value = normalize_text(pattern.elements[0].value)
            if key in values:
                raise ValueError(f"{source}: duplicate Fluent message key: {key}")
            values[key] = value
    return values, excluded


PARSERS = {
    "android_xml": parse_android_xml,
    "vscode_json": parse_vscode_json,
    "fluent": parse_fluent,
}

TRACK_CONFIGS = {
    "aosp-framework-paired-ui-v1": {
        "format": "android_xml",
        "simplified_locale": "zh-rCN",
        "traditional_locale": "zh-rTW",
        "source_overlap": "blind_v2_source_pool",
    },
    "vscode-paired-ui-v1": {
        "format": "vscode_json",
        "simplified_locale": "zh-hans",
        "traditional_locale": "zh-hant",
        "source_overlap": "blind_v2_source_pool",
    },
    "firefox-paired-ui-v1": {
        "format": "fluent",
        "simplified_locale": "zh-CN",
        "traditional_locale": "zh-TW",
        "source_overlap": "none_known",
    },
}


def build_dataset(manifest: dict[str, Any], raw_sources: dict[str, bytes]) -> dict[str, Any]:
    try:
        config = TRACK_CONFIGS[manifest["id"]]
    except KeyError as exc:
        raise ValueError(f"unsupported paired localization track: {manifest['id']}") from exc
    parser = PARSERS[config["format"]]
    cases: list[dict[str, str]] = []
    excluded: Counter[str] = Counter()
    by_file: Counter[str] = Counter()
    seen_pairs: set[tuple[str, str]] = set()

    for relative, simplified_url, traditional_url in pair_urls(
        raw_sources,
        simplified_locale=config["simplified_locale"],
        traditional_locale=config["traditional_locale"],
    ):
        simplified, simplified_excluded = parser(raw_sources[simplified_url], source=simplified_url)
        traditional, traditional_excluded = parser(
            raw_sources[traditional_url], source=traditional_url
        )
        excluded.update({f"simplified_{key}": count for key, count in simplified_excluded.items()})
        excluded.update(
            {f"traditional_{key}": count for key, count in traditional_excluded.items()}
        )
        for key in sorted(set(simplified) | set(traditional)):
            if key not in simplified or key not in traditional:
                excluded["unpaired_key"] += 1
                continue
            source_text = simplified[key]
            expected = traditional[key]
            if not source_text or not expected:
                excluded["empty_value"] += 1
                continue
            if "\n" in source_text or "\n" in expected:
                excluded["multiline"] += 1
                continue
            if not HAN_RE.search(source_text):
                excluded["no_han_input"] += 1
                continue
            if placeholder_signature(source_text) != placeholder_signature(expected):
                excluded["placeholder_mismatch"] += 1
                continue
            pair = (source_text, expected)
            if pair in seen_pairs:
                excluded["duplicate_pair"] += 1
                continue
            seen_pairs.add(pair)
            cases.append(
                {
                    "id": f"{manifest['id']}/{relative}/{key}",
                    "file": relative,
                    "resource_key": key,
                    "domain": "ui",
                    "input": source_text,
                    "expected": expected,
                }
            )
            by_file[relative] += 1

    if not cases:
        raise ValueError("paired localization dataset has no eligible cases")
    return {
        "version": 1,
        "id": manifest["id"],
        "track": manifest["track"],
        "evidence_role": "public_external_secondary_evidence",
        "primary_market_endpoint": False,
        "reference_kind": "vendor_paired_localization",
        "reference_is_ground_truth": False,
        "license": manifest["output_license"],
        "attribution": manifest["attribution"],
        "modification_notice": manifest["modification_notice"],
        "upstream_revision": manifest["upstream_revision"],
        "source_overlap": config["source_overlap"],
        "locales": {
            "input": config["simplified_locale"],
            "reference": config["traditional_locale"],
        },
        "stats": {
            "total_cases": len(cases),
            "by_file": dict(sorted(by_file.items())),
            "excluded": dict(sorted(excluded.items())),
        },
        "cases": cases,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    manifest = load_manifest(args.manifest)
    output = args.output or PROJECT_ROOT / manifest["normalized_path"]
    dataset = build_dataset(manifest, read_raw_sources(manifest))
    content = canonical_json_bytes(dataset)
    if args.check:
        if not output.is_file() or output.read_bytes() != content:
            print(f"normalized paired dataset is stale: {output}", file=sys.stderr)
            return 1
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(content)
    print(
        f"{manifest['id']}: {dataset['stats']['total_cases']} pairs; "
        f"sha256={sha256_bytes(content)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
