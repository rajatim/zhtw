# Unicode Detection and Mixed-Term Import Plan

> Status: Approved
> Date: 2026-08-26
> Target: 4.5.0

## Goal

Complete the first additive 4.5.0 roadmap slice without changing established
conversion output:

1. detect Han ideographs across the Unicode 17.0 blocks already pinned by the
   project, instead of checking only `U+4E00–U+9FFF`;
2. allow reviewed term-import candidates such as `USB接口` → `USB介面`,
   `IPv6地址` → `IPv6位址`, and `3D打印` → `3D列印`;
3. keep import validation conservative so a mixed rule cannot silently rewrite
   an identifier, punctuation, or formatting.

This work does not add vocabulary, change matcher selection, change dictionary
profiles, or change the normal result for existing inputs. Imported terms still
go to the pending review area and do not become runtime rules automatically.

## Blast radius (files & repos)

Expected files in this repository:

- `src/zhtw/unicode_ranges.py` — one shared definition for supported Han
  ranges and helper functions.
- `src/zhtw/converter.py` — use the shared helper for file-content detection.
- `src/zhtw/import_terms.py` — accept safe mixed terms and keep existing
  conflict, length, and pending-review checks.
- `tests/test_converter.py` — cover BMP, supplementary-plane, compatibility,
  and non-Han detection.
- `tests/test_import_terms.py` — cover accepted mixed terms and rejected unsafe
  or malformed terms.
- `tests/test_cli.py` — prove the import command reports mixed candidates and
  failures correctly.
- `docs/guides/CLI-ADVANCED.md` — document the mixed-term policy and examples.
- `CHANGELOG.md` — record the additive behavior under `[Unreleased]`.

Release-preparation files, changed together only through
`make bump VERSION=4.5.0` after separate release approval:

- `pyproject.toml` and `src/zhtw/__init__.py`;
- `sdk/java/pom.xml`;
- `sdk/typescript/package.json`;
- `sdk/rust/Cargo.toml` and `sdk/rust/zhtw-wasm/package.json`;
- `sdk/dotnet/Zhtw.csproj`;
- `sdk/data/zhtw-data.json` and `sdk/data/golden-test.json`.

No other repository is expected to change. Feature implementation should not
change SDK source or exported data because this slice changes Python-side
scanning and candidate import only. The later mono-version bump will update the
listed package metadata and generated version fields. If implementation shows
that an SDK or shared-data contract must otherwise change, stop and revise this
plan before editing those files.

## Steps

1. Add a Unicode 17.0 Han-range module that includes:
   - CJK Unified Ideographs;
   - Extensions A through I;
   - CJK Compatibility Ideographs and their supplementary block.
2. Replace the narrow converter regular expression with the shared helper.
   Keep the public `contains_chinese(text)` behavior and signature stable.
3. Refactor term validation to require at least one Han ideograph in both the
   source and target.
4. Allow only Han ideographs plus a small technical ASCII set: letters,
   digits, ordinary spaces, `.`, `+`, `#`, `-`, `_`, `/`, `:`, and `@`.
5. Require the non-Han character sequence, including spaces and punctuation,
   to be identical after Han code points are removed from source and target.
   For example, `IPv6地址` → `IPv6位址` is valid, while `HTTP接口` →
   `HTTPS介面` is rejected.
6. Continue rejecting empty values, identity pairs, terms over 20 Unicode code
   points, control characters, line breaks, leading or trailing whitespace,
   unsupported symbols, duplicates, and conflicts.
7. Add focused unit and CLI tests for accepted and rejected cases, including
   supplementary-plane Han characters.
8. Update the advanced CLI guide and changelog. Do not add example terms to the
   production dictionary.
9. Run:
   - `pytest tests/test_converter.py tests/test_import_terms.py tests/test_cli.py`;
   - `zhtw validate`;
   - `make version-check`;
   - `make export-check`;
   - the complete `pytest` suite;
   - `make release-gate` before release preparation.
10. Keep project metadata at the current version during feature development.
    When 4.5.0 release preparation is approved, use `make bump VERSION=4.5.0`
    so every SDK and generated artifact moves together, then follow the Jenkins
    release checklist.

## Risks & rollback

- A too-wide Unicode definition could make a file enter conversion even when
  it contains only a rare compatibility character. This changes scan work, not
  conversion rules. Tests will lock the intended block list.
- A too-wide mixed-character policy could accept unsafe rules. The fixed ASCII
  allowlist, Han requirement, identical non-Han-part rule, and pending-review
  workflow limit that risk.
- A too-narrow policy may reject useful terms containing parentheses or other
  symbols. The safe response is to keep rejecting them until a reviewed use
  case supports expanding the allowlist.
- Supplementary-plane characters use one Python code point but may use two code
  units in other runtimes. This slice does not change SDK parsing or index
  contracts.
- Rollback is a normal revert of the implementation commit. No database,
  external service, published package, or production dictionary migration is
  involved.

## Open questions

1. Should this focused slice define the full 4.5.0 feature scope, with larger
   items such as rule schema v2 and structured adapters moved to later releases?
2. Is the proposed technical ASCII allowlist enough for the first release, or
   is there one required mixed-term format that needs another character?
