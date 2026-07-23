<!-- zhtw:disable -->
# Blind-v2 Source Classification Synthesis 008

Status: advisory only; maintainer confirmation pending

Source: NPS *Essential Acadia: Simplified Chinese*

## Summary

- Total extracted inputs: 32
- Exact Codex/Gemini matches: 7
- Review queue: 25
- Recommended eligible: 30
- Recommended excluded: 2
- Recommended eligible domains: 11 social/daily, 10 formal/news, 9 high-stakes
- Recommended eligible risks: 13 candidate-gap, 7 over-conversion guard, 10 baseline
- Selection basis: 7 agreement, 21 Codex, 1 Gemini, 3 field-level hybrid

Gemini CLI 0.52.0 (`gemini-2.5-pro`) covered 32/32 IDs in one API request
with zero tool calls and zero API errors. Gemini recommended all 32 as eligible.

## Eligibility Decisions

Recommended exclusions:

- `sentence-005`: `go.nps.gov/ AcadiaPass` is a malformed URL/link-label
  artifact used as a sentence subject, including an invalid embedded space.
- `sentence-010`: `附近的城镇` lacks the location that “nearby” refers to and
  cannot be independently adjudicated under the fixed context rule.

The other 30 cases are complete propositions with enough sentence-internal
context for later expected annotation.

## Classification Review

- Ordinary trip planning, accommodation, pets, and visitor services remain
  `social_daily`; official prohibitions and park rules are `formal_news`.
- `high_stakes` is limited to legal or outdoor-safety instructions. A rule is
  not high-stakes merely because it is important to a visitor.
- Simple character changes such as `瑰宝` or `判断` do not by themselves create
  a lexical `candidate_gap`.
- `sentence-003` and `sentence-009` are baseline guards after second review.
- `sentence-023` adopts Gemini's baseline risk because `让路` is ordinary
  Taiwan usage after script conversion.
- `sentence-029` is a candidate gap because Taiwan wording normally describes
  pet excrement rather than literal “pet garbage.”
- Names and literals such as Acadia, Recreation.gov, and Island Explorer are
  over-conversion guards.

## Human Gate

These classifications remain AI advisory. Batch 008 cannot enter the candidate
pool until the maintainer confirms all 32 synthesis decisions.
