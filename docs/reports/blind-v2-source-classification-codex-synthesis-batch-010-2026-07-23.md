<!-- zhtw:disable -->
# Blind-v2 Source Classification Synthesis 010

Status: synthesis confirmed by maintainer on 2026-07-24

Sources: seven OSHA Simplified Chinese occupational-safety publications

## Summary

- Total extracted inputs: 100
- Exact Codex/Gemini matches: 41
- Review queue: 59
- Recommended eligible: 85
- Recommended excluded: 15
- Recommended eligible domains: 60 high-stakes, 22 formal/news, 3 social/daily
- Recommended eligible risks: 48 candidate-gap, 25 baseline, 12 over-conversion guard
- Selection basis: 41 agreement, 56 Codex, 3 Gemini

Gemini CLI 0.52.0 (`gemini-2.5-pro`) covered 100/100 IDs in an independent
session with zero tool calls and zero API errors. It received only the input
packet and classification policy, without Codex conclusions, converter output,
or expected output.

## Recommended Exclusions

- `cleanup/sentence-008`, `sentence-009`, and `sentence-026`: noun or hazard-list
  fragments without a complete independent statement.
- `cleanup/sentence-024` and `sentence-043`: PDF headings are joined directly to
  body text.
- `cleanup/sentence-036`, `sentence-062`, and `sentence-075`: the instruction or
  referent depends materially on omitted context.
- `falls/sentence-005` and `sentence-006`: list extraction produced malformed or
  concatenated text.
- `fallen-workers/sentence-007` and `sentence-014`: PDF headings or list items are
  incorrectly joined to body text.
- `small-business/sentence-010` and `sentence-019`: headings or separate clauses
  are joined without the source layout boundary.
- `work-zone/sentence-002`: duplicated `筒` indicates malformed source text.

## Boundary Decisions

- Keep `分享/创建纪念物品或活动。`; it is a complete imperative despite its
  compact list-item style. Gemini's `social_daily` classification is preferred.
- Keep work-zone statements beginning with `作业区防护：`, `信号：`, `照明：`,
  `培训：`, and `行驶：`. The label and following clause form a complete,
  independently understandable statement rather than an accidental PDF join.
- Keep occupational safety requirements as `high_stakes`, including planning and
  traffic-control duties that could otherwise look like administrative prose.
- Prefer Gemini for `反冲` as a candidate terminology gap and for the U.S. state
  names as an over-conversion guard. Other source-quality boundaries retain the
  stricter Codex recommendation.

## Human Gate

Maintainer `tim` confirmed all 100 synthesis classifications on 2026-07-24 using
`batch_human_confirmation`. All 85 eligible inputs passed exact/reference and
character 5-gram Jaccard 0.85 deduplication and entered the collecting pool. No
expected or converter output was used.
