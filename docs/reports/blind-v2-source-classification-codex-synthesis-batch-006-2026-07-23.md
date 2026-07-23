<!-- zhtw:disable -->
# Blind-v2 Source Classification Synthesis 006

Status: confirmed by maintainer `tim` on 2026-07-23

Source: zhtw project-original IT/API/CLI v1

## Summary

- Total: 100
- Exact Codex/Gemini matches: 58
- Review queue: 42
- Recommended eligible: 100
- Recommended excluded: 0
- Recommended domain: 100 IT/API/CLI
- Recommended script: 100 simplified
- Recommended risks: 82 candidate-gap, 8 over-conversion guard, 10 baseline
- Selection basis: 58 agreement, 13 Codex, 28 Gemini, 1 field-level hybrid

Gemini CLI 0.52.0 (`gemini-2.5-pro`) covered 100/100 IDs with zero tool
calls and zero API errors. It received only packet IDs, inputs, and the fixed
classification rules; it did not receive the Codex advisory.

## Policy Decisions

- Embedded API names, protocol names, and CLI literals do not by themselves
  make a predominantly Simplified Chinese sentence `mixed`. This follows the
  policy already applied to JSON, API, Markdown, and Escape in batch 004.
- `it-002` remains `candidate_gap`: `请求体` is a meaningful engineering term,
  not only a glyph-level baseline case.
- `it-010` is the only field-level hybrid: keep Codex `simplified` script and
  Gemini `over_conversion_guard` risk because the literal `API` must remain
  intact.
- A second Codex case-level review corrected five initial synthesis choices:
  `it-022`, `it-088`, and `it-089` are baseline guards because their terms are
  standard Taiwan engineering usage after ordinary glyph conversion;
  `it-071` and `it-080` are candidate gaps because `用户` and `身份` require
  contextual Taiwan wording.
- The remaining risk disagreements adopt Gemini. Its candidate-gap findings
  identify concrete engineering terms such as `管道`, `拉取请求`, `进程`,
  `实例`, `软件包`, `模块`, `日志`, `缓存`, and `配置中心`.

## Over-Conversion Guards

`it-007, it-009, it-010, it-012, it-038, it-043, it-078, it-097`

These contain literal Webhook, GraphQL, API, `--dry-run`, UTC, `root`, TLS, or
DNS boundaries that must be preserved while surrounding Chinese text converts.

## Baseline Guards

`it-005, it-019, it-022, it-052, it-054, it-083, it-088, it-089, it-090,
it-098`

## Advisory Selection

Adopt Codex (13):

`it-002, it-007, it-009, it-012, it-022, it-038, it-043, it-071, it-078,
it-080, it-088, it-089, it-097`

Adopt Gemini (28):

`it-005, it-013, it-014, it-017, it-024, it-025, it-035, it-037, it-044,
it-047, it-050, it-053, it-057, it-058, it-065, it-066, it-068, it-070,
it-076, it-081, it-082, it-085, it-086, it-087, it-092, it-096, it-099,
it-100`

Field-level hybrid (1): `it-010`.

The other 58 cases are exact Codex/Gemini matches.

## Human Gate

These classifications began as AI advisory. Maintainer `tim` confirmed the
complete second-review synthesis on 2026-07-23 using
`batch_human_confirmation`; all 100 eligible cases entered the promotion gate.
