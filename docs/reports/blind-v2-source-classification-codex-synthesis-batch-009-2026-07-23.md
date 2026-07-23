<!-- zhtw:disable -->
# Blind-v2 Source Classification Synthesis 009

Status: synthesis confirmed by maintainer on 2026-07-23

Sources: Ready.gov Simplified Chinese earthquake, flood, and hurricane pages

## Summary

- Total extracted inputs: 100
- Exact Codex/Gemini matches: 68
- Review queue: 32
- Recommended eligible: 86
- Recommended excluded: 14
- Recommended eligible domains: 82 high-stakes, 4 formal/news
- Recommended eligible risks: 49 candidate-gap, 34 baseline, 3 over-conversion guard
- Selection basis: 68 agreement, 24 Codex, 8 Gemini

Gemini CLI 0.52.0 (`gemini-2.5-pro`) covered 100/100 IDs in an independent
session with zero tool calls and zero API errors. Its first response contained
two invalid risk labels; Gemini corrected those labels in the same session
without receiving the Codex advisory.

## Recommended Exclusions

- `earthquakes/sentence-005` and `earthquakes/sentence-011`: section headings
  are joined to body text.
- `earthquakes/sentence-029`: `爬到在地` is malformed source text.
- `floods/sentence-004`, `floods/sentence-006`, and `floods/sentence-031`:
  fragments lack a subject or required sentence context.
- `floods/sentence-012`: a heading fragment is joined to an instruction.
- `hurricanes/sentence-013`, `sentence-017`, `sentence-020`, `sentence-022`,
  `sentence-023`, and `sentence-030`: section headings are joined to body text.
- `hurricanes/sentence-016`: `他们` has no sentence-internal antecedent.

## Boundary Decisions

- Keep `切记：并非每个人...` and `切记：只需 6 英寸...`. Here `切记` is a
  complete discourse marker, not a detached page heading.
- Keep `东太平洋飓风季：5月15日至11月30日。`. The label-value statement is
  independently understandable and has a deterministic Taiwan conversion.
- Keep safety instructions as `high_stakes` even when they mention digital
  copies, an app, or text messages; the subject matter is emergency safety,
  not an IT workflow.

## Human Gate

The maintainer confirmed all 100 synthesis classifications on 2026-07-23 using
`batch_human_confirmation`. Promotion retained 85 of the 86 eligible inputs;
one exact cross-source duplicate was excluded. No expected output or converter
output was used.
