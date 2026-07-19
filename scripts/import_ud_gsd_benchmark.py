#!/usr/bin/env python3
"""Import pinned UD Chinese GSD/GSDSimp sentence pairs."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.benchmark_metrics import canonical_json_bytes  # noqa: E402

DEFAULT_MANIFEST = PROJECT_ROOT / "benchmarks" / "accuracy" / "manifests" / "ud-gsd-v1.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "benchmarks" / "accuracy" / "external" / "ud-gsd-v1.json"
SPLITS = ("train", "dev", "test")


@dataclass(frozen=True)
class Sentence:
    sent_id: str
    text: str


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def parse_conllu(content: str, *, source: str) -> dict[str, Sentence]:
    sentences: dict[str, Sentence] = {}
    current_id: str | None = None
    current_text: str | None = None

    def finish() -> None:
        nonlocal current_id, current_text
        if current_id is None and current_text is None:
            return
        if current_id is None or current_text is None:
            raise ValueError(f"{source}: sentence block is missing sent_id or text")
        if current_id in sentences:
            raise ValueError(f"{source}: duplicate sent_id: {current_id}")
        sentences[current_id] = Sentence(sent_id=current_id, text=current_text)
        current_id = None
        current_text = None

    for raw_line in content.splitlines():
        line = raw_line.rstrip("\r")
        if not line:
            finish()
        elif line.startswith("# sent_id = "):
            if current_id is not None:
                raise ValueError(f"{source}: duplicate sent_id field in one block")
            current_id = line.removeprefix("# sent_id = ").strip()
        elif line.startswith("# text = "):
            if current_text is not None:
                raise ValueError(f"{source}: duplicate text field in one block")
            current_text = line.removeprefix("# text = ")
    finish()
    if not sentences:
        raise ValueError(f"{source}: no sentences found")
    return sentences


def load_manifest(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("manifest must be a JSON object")
    return value


def local_source_path(url: str, *, gsd_dir: Path, gsdsimp_dir: Path) -> Path:
    root = gsdsimp_dir if "UD_Chinese-GSDSimp" in url else gsd_dir
    return root / url.rsplit("/", 1)[-1]


def read_raw_source(
    url: str,
    expected_hash: str,
    *,
    gsd_dir: Path | None,
    gsdsimp_dir: Path | None,
) -> bytes:
    if (gsd_dir is None) != (gsdsimp_dir is None):
        raise ValueError("--gsd-dir and --gsdsimp-dir must be provided together")
    if gsd_dir is not None and gsdsimp_dir is not None:
        path = local_source_path(url, gsd_dir=gsd_dir, gsdsimp_dir=gsdsimp_dir)
        content = path.read_bytes()
    else:
        with urllib.request.urlopen(url, timeout=60) as response:
            content = response.read()
    actual_hash = sha256_bytes(content)
    if actual_hash != expected_hash:
        raise ValueError(f"raw sha256 mismatch for {url}: {actual_hash}")
    return content


def source_url(manifest: dict[str, Any], *, simplified: bool, split: str) -> str:
    marker = f"zh_{'gsdsimp' if simplified else 'gsd'}-ud-{split}.conllu"
    matches = [url for url in manifest["raw_sha256"] if url.endswith(marker)]
    if len(matches) != 1:
        raise ValueError(f"manifest must contain exactly one raw source ending with {marker}")
    return matches[0]


def build_dataset(
    manifest: dict[str, Any],
    *,
    gsd_dir: Path | None = None,
    gsdsimp_dir: Path | None = None,
) -> dict[str, Any]:
    cases: list[dict[str, Any]] = []
    by_split: dict[str, int] = {}
    seen_ids: set[str] = set()
    raw_content = {
        url: read_raw_source(
            url,
            expected_hash,
            gsd_dir=gsd_dir,
            gsdsimp_dir=gsdsimp_dir,
        )
        for url, expected_hash in manifest["raw_sha256"].items()
    }

    for split in SPLITS:
        traditional_url = source_url(manifest, simplified=False, split=split)
        simplified_url = source_url(manifest, simplified=True, split=split)
        traditional = parse_conllu(
            raw_content[traditional_url].decode("utf-8"),
            source=traditional_url,
        )
        simplified = parse_conllu(
            raw_content[simplified_url].decode("utf-8"),
            source=simplified_url,
        )
        if set(traditional) != set(simplified):
            missing_traditional = sorted(set(simplified) - set(traditional))
            missing_simplified = sorted(set(traditional) - set(simplified))
            raise ValueError(
                f"{split}: sent_id mismatch; missing traditional={missing_traditional[:5]} "
                f"missing simplified={missing_simplified[:5]}"
            )
        duplicate_across_splits = seen_ids & set(traditional)
        if duplicate_across_splits:
            raise ValueError(
                f"duplicate sent_id across splits: {sorted(duplicate_across_splits)[:5]}"
            )
        seen_ids.update(traditional)
        by_split[split] = len(traditional)
        for sent_id in sorted(traditional):
            cases.append(
                {
                    "id": f"{manifest['id']}/{sent_id}",
                    "sent_id": sent_id,
                    "split": split,
                    "genre": "wiki",
                    "input": simplified[sent_id].text,
                    "expected": traditional[sent_id].text,
                }
            )

    return {
        "version": 1,
        "id": manifest["id"],
        "track": manifest["track"],
        "evidence_role": "secondary_evidence",
        "primary_market_endpoint": False,
        "license": manifest["output_license"],
        "attribution": manifest["attribution"],
        "modification_notice": manifest["modification_notice"],
        "upstream_revision": manifest["upstream_revision"],
        "source_bias": "opencc_derived_source_bias",
        "stats": {
            "total_cases": len(cases),
            "by_split": by_split,
            "by_genre": {"wiki": len(cases)},
        },
        "cases": cases,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--gsd-dir", type=Path)
    parser.add_argument("--gsdsimp-dir", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    manifest = load_manifest(args.manifest)
    dataset = build_dataset(
        manifest,
        gsd_dir=args.gsd_dir,
        gsdsimp_dir=args.gsdsimp_dir,
    )
    content = canonical_json_bytes(dataset)
    if args.check:
        if not args.output.is_file() or args.output.read_bytes() != content:
            print("normalized UD dataset is stale", file=sys.stderr)
            return 1
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(content)
    print(f"UD pairs: {dataset['stats']['total_cases']}; sha256={sha256_bytes(content)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
