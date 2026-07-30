<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 067 (2026-07-30)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `7de987c3d4236d290424f0b522e86679c465121ec6ae2901883dddb77b45231a`
Cases: 120
Exact Codex/Gemini classifications: 118
Maintainer review queue: 2

Field differences:

- Eligibility: 2
- Script: 0
- Domain: 2
- Risk: 2

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

The maintainer resolved all 2 advisory disagreements and batch-confirmed the 118 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. ready-gov-are-you-ready-guide-simplified-v1/sentence-316

Changed: `eligible, domain, risk`

Input:

```text
鼓励全家注册社交媒体应用程序，例如脸书安全检查或美国红十字会安全和健康。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | unsafe_source_translation |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex excluded this input-only case because the source text is not reliable enough for an independently judgeable conversion benchmark.

Gemini reason: This is a complete recommendation sentence regarding safety registration.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 02. ready-gov-are-you-ready-guide-simplified-v1/sentence-349

Changed: `eligible, domain, risk`

Input:

```text
在灾难来袭前，研究好便利宠物的庇护所或寄养宠物的地方。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | unsafe_source_translation |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex excluded this input-only case because the source text is not reliable enough for an independently judgeable conversion benchmark.

Gemini reason: This is a complete preparedness instruction for pet owners.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`
