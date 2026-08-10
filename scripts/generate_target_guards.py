#!/usr/bin/env python3
"""Generate identity guards for dictionary targets that change on another pass."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from zhtw.charconv import get_translate_table  # noqa: E402
from zhtw.converter import convert_text, inject_protect_terms  # noqa: E402
from zhtw.dictionary import (  # noqa: E402
    DATA_DIR,
    TARGET_GUARD_FILES,
    iter_directory_files,
    load_json_file,
)
from zhtw.matcher import Matcher  # noqa: E402

DEFAULT_OUTPUT = DATA_DIR / "cn" / "target-guards.json"
SOURCES = ["cn", "hk"]


def load_effective_terms() -> dict[str, tuple[str, str, str]]:
    """Load effective terms without the generated guard file."""
    merged: dict[str, tuple[str, str, str]] = {}
    for source_group in SOURCES:
        for path in iter_directory_files(DATA_DIR / source_group):
            if path.name in TARGET_GUARD_FILES:
                continue
            for source, target in load_json_file(path).items():
                merged[source] = (target, source_group, path.name)
    return merged


def generate_guard_terms() -> dict[str, str]:
    """Return target identity mappings required for one-pass target stability."""
    effective = load_effective_terms()
    terms = {source: target for source, (target, _group, _file) in effective.items()}
    inject_protect_terms(terms, SOURCES)
    matcher = Matcher(terms)
    char_table = get_translate_table()

    converted_cache: dict[str, str] = {}
    guards: dict[str, str] = {}
    for target, _group, _file in effective.values():
        converted = converted_cache.get(target)
        if converted is None:
            converted = convert_text(
                target,
                matcher,
                fix=True,
                char_table=char_table,
            )[0]
            converted_cache[target] = converted
        if converted == target:
            continue

        existing = effective.get(target)
        if existing is not None and existing[0] != target:
            raise ValueError(f"cannot guard target {target!r}; it is also a conversion source")
        guards[target] = target

    return dict(sorted(guards.items()))


def build_payload() -> dict[str, object]:
    """Build the deterministic guard-file payload."""
    return {
        "version": "1.0",
        "description": (
            "Generated identity guards that keep declared dictionary targets "
            "stable on another conversion pass"
        ),
        "source": "scripts/generate_target_guards.py",
        "terms": generate_guard_terms(),
    }


def render_payload() -> str:
    """Render the committed JSON form."""
    return json.dumps(build_payload(), ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    rendered = render_payload()
    if args.check:
        if not args.output.exists() or args.output.read_text(encoding="utf-8") != rendered:
            print(f"target guards are stale: {args.output}", file=sys.stderr)
            return 1
        print(f"target guards are current: {args.output}")
        return 0

    payload = json.loads(rendered)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding="utf-8")
    print(f"wrote {len(payload['terms'])} target guards to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
