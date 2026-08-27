# Unicode Detection and Mixed-Term Import Plan

> Status: Integrated into the Approved 4.5.0 master plan
> Date: 2026-08-26
> Integrated: 2026-08-27
> Implementation approved: 2026-08-27
> Target: 4.5.0 Phase A supporting work

## Goal

Support the rule-foundation phase of 4.5.0 without changing established
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
   - Extensions A through J;
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

## Integration decisions

1. This work is supporting scope inside the 4.5.0 rule-schema phase. It does
   not define the full 4.5.0 release by itself.
2. Mixed-term import must write schema v2 review candidates, so it starts only
   after the v2 rule model and compatibility contract are approved.
3. The technical ASCII allowlist in this plan is the approved first-release
   baseline. Expanding it requires a reviewed use case and a plan update.
4. Implementation follows the separately approved 4.5.0 master plan and its
   fixed compatibility baseline.
