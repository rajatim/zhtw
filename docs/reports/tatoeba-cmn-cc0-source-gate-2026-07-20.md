<!-- zhtw:disable -->
# Tatoeba Mandarin CC0 Source Gate (2026-07-20)

Status: rejected for Blind-v2 pilot capacity

Issue: #43

This source gate inspected the official CC0 export only. It did not run zhtw,
OpenCC, zhconv, Gemini, or another converter, and it did not inspect expected or
engine output.

## Pinned Snapshot

- Official download page: <https://tatoeba.org/en/downloads>
- Export URL:
  <https://downloads.tatoeba.org/exports/per_language/cmn/cmn_sentences_CC0.tsv.bz2>
- Weekly snapshot date: 2026-07-18
- Last-Modified: `Sat, 18 Jul 2026 06:36:35 GMT`
- ETag: `"6a5b1ef3-66"`
- Compressed size: 102 bytes
- SHA-256: `72c6ac699497cbc9b75f6c021ef16dfaa91ab760fbb407217902b6b5388401c0`
- License: CC0 1.0
- Rows: 1

The official download documentation defines the CC0 row format as sentence ID,
language, text, and last-modified date. Tatoeba's CC0 contribution policy limits
CC0 to contributor-authored original sentences; translations are not eligible.

## Input-Only Quality Decision

The sole Mandarin row is sentence `10597783`, last modified
`2021-12-31 15:06:47`. Its text starts with the malformed year expression
`2022/2972`, so it fails the source-quality gate. No row is eligible for the
Blind-v2 candidate pool.

The mutable weekly URL has no discovered official date-addressed archive. The
snapshot metadata and hash are retained as audit evidence, but no normalized
dataset or manifest is committed because it would add zero eligible cases and a
future online import check could not reproduce the overwritten weekly object.

## Decision

- Do not substitute the general CC BY export for the CC0 export.
- Do not use translations, transcriptions, or converter-generated script
  variants to increase capacity.
- Recheck only if a future CC0 weekly export contains materially more Mandarin
  originals; any future snapshot needs a new date and SHA-256.
- Continue with individually verified CDC public-domain items and
  project-original/permissioned sources.
