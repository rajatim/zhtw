#!/usr/bin/env python3
"""Audit dictionary target idempotency.

For each effective dictionary entry, checks whether converting the target again
would change it. A changed target means the first conversion can be damaged by a
second zhtw pass, e.g. ``權限 -> 許可權``.

Usage:
    uv run python scripts/audit_idempotency.py
    uv run python scripts/audit_idempotency.py --sources cn --curated-only
    uv run python scripts/audit_idempotency.py --curated-only --fail-on-issues
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from zhtw import convert  # noqa: E402
from zhtw.converter import VALID_SOURCES  # noqa: E402
from zhtw.dictionary import BULK_FILES, DATA_DIR, iter_directory_files, load_json_file  # noqa: E402


@dataclass(frozen=True)
class Issue:
    source_group: tuple[str, ...]
    source: str
    target: str
    converted_target: str
    term_source: str
    file_name: str


def parse_sources(raw: str) -> list[str]:
    sources = [s.strip() for s in raw.split(",") if s.strip()]
    invalid = sorted(set(sources) - set(VALID_SOURCES))
    if not sources or invalid:
        valid = ",".join(sorted(VALID_SOURCES))
        raise argparse.ArgumentTypeError(f"sources must be comma-separated from {valid}")
    return sources


def effective_terms(sources: list[str]) -> dict[str, tuple[str, str, str]]:
    """Return effective source -> (target, source namespace, file name)."""
    merged: dict[str, tuple[str, str, str]] = {}
    for term_source in sources:
        src_dir = DATA_DIR / term_source
        for json_file in iter_directory_files(src_dir):
            terms = load_json_file(json_file)
            for source, target in terms.items():
                if source.startswith("_"):
                    continue
                merged[source] = (target, term_source, json_file.name)
    return merged


def audit(sources: list[str], curated_only: bool) -> list[Issue]:
    terms = effective_terms(sources)
    converted_cache: dict[str, str] = {}
    issues: list[Issue] = []

    for source, (target, term_source, file_name) in terms.items():
        if curated_only and file_name in BULK_FILES:
            continue
        converted = converted_cache.get(target)
        if converted is None:
            converted = convert(target, sources=sources)
            converted_cache[target] = converted
        if converted != target:
            issues.append(
                Issue(
                    source_group=tuple(sources),
                    source=source,
                    target=target,
                    converted_target=converted,
                    term_source=term_source,
                    file_name=file_name,
                )
            )

    issues.sort(key=lambda i: (i.term_source, i.file_name, i.source))
    return issues


def print_report(issues: list[Issue], limit: int) -> None:
    if not issues:
        print("✅ target idempotency OK")
        return

    by_file = Counter(f"{i.term_source}/{i.file_name}" for i in issues)
    print(f"⚠️  found {len(issues)} non-idempotent targets")
    print()
    print("By file:")
    for file_name, count in by_file.most_common():
        print(f"  {file_name}: {count}")

    print()
    print("Issues:")
    for issue in issues[:limit]:
        sources = ",".join(issue.source_group)
        print(
            f"  [{sources}] {issue.term_source}/{issue.file_name}: "
            f"{issue.source} -> {issue.target} -> {issue.converted_target}"
        )
    if len(issues) > limit:
        print(f"  ... {len(issues) - limit} more")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--sources",
        type=parse_sources,
        default=parse_sources("cn,hk"),
        help="Comma-separated sources to audit: cn, hk, or cn,hk. Default: cn,hk",
    )
    parser.add_argument(
        "--curated-only",
        action="store_true",
        help="Exclude bulk imported dictionaries such as opencc.json.",
    )
    parser.add_argument(
        "--fail-on-issues",
        action="store_true",
        help="Exit 1 when any issue is found.",
    )
    parser.add_argument("--limit", type=int, default=100, help="Maximum issues to print.")
    args = parser.parse_args()

    issues = audit(args.sources, args.curated_only)
    print_report(issues, max(args.limit, 0))
    return 1 if issues and args.fail_on_issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
