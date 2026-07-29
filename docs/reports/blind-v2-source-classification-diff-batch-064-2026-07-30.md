<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 064 (2026-07-30)

Status: advisory only; maintainer decisions pending

Packet SHA-256: `a089a7102f29f0f12f9d6cb6d1da34bcad6d604871b0796a38afb96f3d398f3a`
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

Neither advisory is auto-preferred. Codex must synthesize the differences before maintainer confirmation; no classification in this report has been written into the candidate pool.

## Review Queue

### 01. ready-gov-are-you-ready-guide-simplified-v1/sentence-102

Changed: `eligible, domain, risk`

Input:

```text
如果是在车辆中，请停在远离建筑物、树木立交桥地下通道或公用电线的空旷区域。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | no | null | null | high | missing_punctuation, extraction_artifact |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The input is damaged due to missing enumeration punctuation between concatenated words.

Maintainer decision: `pending`

### 02. ready-gov-are-you-ready-guide-simplified-v1/sentence-186

Changed: `eligible, domain, risk`

Input:

```text
山体滑坡、泥石流或碎石流后的洪水。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | no | null | null | high | sentence_fragment |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The input is an incomplete sentence fragment lacking a main predicate.

Maintainer decision: `pending`
