<!-- zhtw:disable -->
# Holdout Maintainer Final Decision Summary (2026-07-08)

Dataset: `blind-v1`
Private expected path: `benchmarks/accuracy/blind-v1.expected.json`
Private expected sha256: `efb8ee42152eacede683dbfa357ace86b3b649ce611eef0d3362646ae8ba7e65`
Source inputs: `benchmarks/accuracy/blind-v1.inputs.json`
Source inputs sha256: `6ed7102cb31128c6f9bdbaa0be65e5c6ea6278733b329d5e32967116079cd4fd`

## Boundary

- This report records maintainer final decision metadata only.
- It intentionally does not include expected values.
- `blind-v1.expected.json` remains private and gitignored.
- Approval policy is `single_human_with_ai_advisory`; this is not a strict two-human sealed benchmark.
- Any public claim must disclose the approval policy or obtain a second human review first.

## Summary

- Cases: 100
- Status: `sealed_private`
- Approval policy: `single_human_with_ai_advisory`
- Minimum human reviewers: 1
- AI advisory allowed: `true`

Expected source:

- `human_adjudication`: 30
- `human_first_pass`: 70

Disagreement:

- `false`: 70
- `true`: 30

Source reports:

- `docs/reports/holdout-codex-first-pass-blind-v1-0001-0100-2026-07-08.json`
- `docs/reports/holdout-gemini-vertex-advisory-blind-v1-0001-0100-2026-07-08.json`
- `docs/reports/holdout-codex-gemini-diff-review-blind-v1-0001-0100-2026-07-08.json`
- `docs/reports/holdout-maintainer-confirmation-blind-v1-0001-0100-2026-07-08.json`
