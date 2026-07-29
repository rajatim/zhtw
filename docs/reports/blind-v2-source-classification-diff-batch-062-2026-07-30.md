<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 062 (2026-07-30)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `e5fd5063fb14f5466f7f15f70fec2fab1f7e9b06eb00710ae8f194abab9b497b`
Cases: 96
Exact Codex/Gemini classifications: 94
Maintainer review queue: 2

Field differences:

- Eligibility: 2
- Script: 0
- Domain: 2
- Risk: 2

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

The maintainer resolved all 2 advisory disagreements and batch-confirmed the 94 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. ready-gov-are-you-ready-guide-simplified-v1/sentence-364

Changed: `eligible, domain, risk`

Input:

```text
开罐器等食物的准备工具。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | no | null | null | high | sentence_fragment |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Noun phrase checklist item lacking a main verb or sentence context.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 02. ready-gov-are-you-ready-guide-simplified-v1/sentence-368

Changed: `eligible, domain, risk`

Input:

```text
紧急参考材料（例如急救书或来自 Ready.gov的资料)。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | no | null | null | high | sentence_fragment |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: List item fragment containing protected Latin domain name Ready.gov.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`
