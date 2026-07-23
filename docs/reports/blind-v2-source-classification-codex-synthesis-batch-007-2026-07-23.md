<!-- zhtw:disable -->
# Blind-v2 Source Classification Synthesis 007

Status: advisory only; maintainer confirmation pending

Source: FTC *Scams and Your Small Business*, Simplified Chinese, July 2023

## Summary

- Total extracted inputs: 81
- Exact Codex/Gemini matches: 53
- Review queue: 28
- Recommended eligible: 55
- Recommended excluded: 26
- Recommended eligible domains: 36 high-stakes, 12 IT/API/CLI, 7 formal/news
- Recommended eligible risks: 43 candidate-gap, 5 over-conversion guard, 7 baseline
- Selection basis: 53 agreement, 19 Codex, 8 Gemini, 1 field-level hybrid

Gemini CLI 0.52.0 (`gemini-2.5-pro`) covered 81/81 IDs with zero tool calls
and zero API errors. Its free-form summary claimed 73 eligible, but its 81
case records contain 72 eligible; the advisory records this mismatch and uses
the complete case records rather than the inconsistent summary count.

## Eligibility Rule

Every promoted sentence must be independently adjudicable outside the source
booklet. The synthesis excludes unresolved anaphora or transitions such as
`他們`, `其`, `上述要求`, `這時`, and `之後` when the referent is absent.

Recommended exclusions (26):

`sentence-002, sentence-004, sentence-006, sentence-007, sentence-009,
sentence-012, sentence-013, sentence-025, sentence-028, sentence-029,
sentence-031, sentence-032, sentence-036, sentence-040, sentence-044,
sentence-048, sentence-049, sentence-051, sentence-055, sentence-056,
sentence-064, sentence-067, sentence-069, sentence-075, sentence-079,
sentence-081`

Two Codex first-pass exclusions are retained after re-review:

- `sentence-057` explicitly names both the scammers and novice entrepreneurs,
  so the sentence is independently understandable despite its opening phrase.
- `sentence-065` is a complete proposition about changing contract terms; the
  word “other” does not hide the proposition being evaluated.

## Other Decisions

- `sentence-015`: IT/API/CLI because it concerns email, passwords, and sensitive
  information handling.
- `sentence-019`: high-stakes because it concerns wire transfer,
  cryptocurrency, and gift-card payment fraud.
- `sentence-076`: high-stakes domain with candidate-gap risk; the legal-office
  terminology requires contextual Taiwan treatment.
- `sentence-011`, `sentence-059`, and `sentence-077` are baseline guards after
  case-level review.
- The five over-conversion guards preserve official agency names, abbreviations,
  or literal identifiers: `sentence-041, sentence-043, sentence-045,
  sentence-060, sentence-080`.

## Human Gate

These classifications remain AI advisory. Batch 007 cannot enter the candidate
pool until the maintainer confirms all 81 synthesis decisions.
