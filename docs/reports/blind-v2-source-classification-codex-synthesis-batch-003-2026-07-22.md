<!-- zhtw:disable -->
# Blind-v2 Source Classification Synthesis 003 (2026-07-22)

Status: superseded by maintainer decision; all 62 cases use the Codex first pass

## Summary

- Packet cases: 62
- Exact Codex/Gemini classifications: 33
- Differing classifications: 29
- Eligibility differences requiring explicit attention: 1
- Taxonomy-only differences recommended for Codex batch confirmation: 28
- Gemini CLI: 0 tool calls, 0 API errors, exact 62/62 ID coverage
- Gemini did not receive Codex conclusions, converter output, or expected text.

Maintainer `tim` confirmed the Codex classification for all 62 cases on
2026-07-22: 61 inputs are eligible and one malformed source sentence is
excluded. Gemini remains advisory history. No classification has yet been
promoted into the candidate pool.

## Eligibility Decision

### cdc-stacks-116683-v1/p03-004

Input: `目的：制定和执行全国媒体信息传播活动，以增加 AI/AN 社区中的 COVID-19 免疫而集中。`

- Codex: **exclude**, `malformed_sentence`.
- Gemini: include, `formal_news / baseline_guard`.
- Recommendation: **Codex**. The phrase `免疫而集中` makes the stated purpose
  unreliable and cannot be repaired without reconstructing the upstream text.

## Domain Differences

Recommendation: **Codex** for all IDs in this section.

The following CDC health-equity and public-health program statements describe
medical or public-health risks, interventions, vaccination, mental health, or
health access. Classify them as `high_stakes`, not merely `formal_news`:

- `cdc-stacks-116683-v1/p01-001` through `p01-009`
- `cdc-stacks-116683-v1/p03-001` through `p03-003`
- `cdc-stacks-116683-v1/p04-001`
- `cdc-stacks-116683-v1/p06-002`
- `cdc-stacks-116683-v1/p07-001`
- `cdc-stacks-116683-v1/p08-003`

The malformed `p03-004` is handled by the eligibility decision above.

For the oral-health booklet:

- `cdc-stacks-120024-v1/p01-001`: use Codex `formal_news`; it describes an
  official agency publication rather than an ordinary conversation.
- `cdc-stacks-120024-v1/p06-002` and `p06-003`: use Codex `high_stakes`; both
  are brushing-adherence health advice, not merely daily conversation.

## Risk Differences

Recommendation: **Codex** for all IDs in this section.

Use `candidate_gap` where the input contains a plausible Taiwan lexical or
professional-usage difference, rather than only mechanical character changes:

- `cdc-stacks-111808-v1/p01-005`, `p01-006`
- `cdc-stacks-111808-v1/p02-002`, `p02-003`, `p02-009`
- `cdc-stacks-116683-v1/p01-001`, `p01-004`, `p01-008`, `p01-009`
- `cdc-stacks-116683-v1/p03-002`, `p03-003`
- `cdc-stacks-116683-v1/p04-001`, `p06-001`, `p06-002`
- `cdc-stacks-116683-v1/p08-001`, `p08-002`, `p08-003`
- `cdc-stacks-120024-v1/p01-002`

Examples include `高频触碰`, `呆在`, `呼吸短促`, `医疗保健提供者`,
`接线员`, `健康平等`, `信息`, `药剂师`, `合作伙伴关系`, `信息图`,
`应急`, `艾滋病毒`, and `指导方针`.

Use `over_conversion_guard` for these proper-name-heavy cases:

- `cdc-stacks-116683-v1/p01-003`: preserve `CDC` and `COVID-19`.
- `cdc-stacks-120024-v1/p01-001`: preserve the official agency name.

`cdc-stacks-116683-v1/p01-007` now agrees on `over_conversion_guard` after the
Codex re-audit and remains in the queue only because its domain differs.

## Maintainer Decision

The maintainer selected `codex` for all 62 cases. This confirms the 33 exact
matches and resolves all 29 advisory differences. The decision artifact is
`docs/reports/blind-v2-source-classification-maintainer-decision-batch-003-2026-07-22.json`.
