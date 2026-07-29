<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 063 (2026-07-30)

Status: advisory only; maintainer decisions pending

Packet SHA-256: `b77ac2a0dbfc0e88baa9b786ed0311cbc1d46f3756ab789996d655c0d594c319`
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

### 01. ready-gov-are-you-ready-guide-simplified-v1/sentence-312

Changed: `eligible, domain, risk`

Input:

```text
还包括其他重要人员或组织的联系信息，例如医疗机构、医生、学校或服务提供商。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | insufficient_context |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex excluded this input-only case because the source text is not reliable enough for an independently judgeable conversion benchmark.

Gemini reason: Complete instructional sentence regarding emergency contact information.

Maintainer decision: `pending`

### 02. ready-gov-are-you-ready-guide-simplified-v1/sentence-430

Changed: `eligible, domain, risk`

Input:

```text
此外，您可以通过访问 FloodSmart.gov来单独购买地震、恐怖主义和污染保险，也可以作为现有保单的附加条款。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | unsafe_source_translation |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex excluded this input-only case because the source text is not reliable enough for an independently judgeable conversion benchmark.

Gemini reason: Complete sentence from Ready.gov containing protected URL FloodSmart.gov.

Maintainer decision: `pending`
