<!-- zhtw:disable -->
# Holdout Gemini Vertex Advisory (2026-07-09)

Dataset: `blind-v1`
Inputs: `benchmarks/accuracy/blind-v1.inputs.json`
Codex advisory: `docs/reports/holdout-codex-first-pass-blind-v1-expansion-127-cases-2026-07-09.json`
Raw JSON: `docs/reports/holdout-gemini-vertex-advisory-blind-v1-expansion-high-risk-0011-0020-2026-07-09.json`
Reviewer: `gemini_vertex`
Model: `gemini-2.5-flash`

## Policy

- Gemini saw only the input cases, not Codex recommendations.
- This report is advisory only.
- It is not ground truth and must not populate `blind-v1.expected.json` directly.
- Maintainer confirmation is required before any expected value becomes human decision.

## Summary

- Cases: 10
- Exact matches with Codex: 8
- Differences from Codex: 2
- Needs maintainer review: 10

Gemini confidence:

- `high`: 10

Domain distribution:

- `high_risk`: 10

## Maintainer Review Queue

- `blind-high-risk-0011` (high_risk, match, Codex medium, Gemini high)
- `blind-high-risk-0012` (high_risk, different, Codex high, Gemini high)
- `blind-high-risk-0013` (high_risk, match, Codex high, Gemini high)
- `blind-high-risk-0014` (high_risk, match, Codex high, Gemini high)
- `blind-high-risk-0015` (high_risk, match, Codex high, Gemini high)
- `blind-high-risk-0016` (high_risk, different, Codex high, Gemini high)
- `blind-high-risk-0017` (high_risk, match, Codex high, Gemini high)
- `blind-high-risk-0018` (high_risk, match, Codex high, Gemini high)
- `blind-high-risk-0019` (high_risk, match, Codex medium, Gemini high)
- `blind-high-risk-0020` (high_risk, match, Codex high, Gemini high)

## Comparisons

### blind-high-risk-0011：match

- Domain: `high_risk`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
医师建议患者按时回诊并记录症状变化。
```

Codex expected:

```text
醫師建議病患按時回診並記錄症狀變化。
```

Gemini expected:

```text
醫師建議病患按時回診並記錄症狀變化。
```

Gemini acceptable variants:

```text
醫師建議患者按時回診並記錄症狀變化。
```

Gemini notes:

```text
「患者」在台灣醫療語境中也通用，但「病患」更為常見且正式。
```

### blind-high-risk-0012：different

- Domain: `high_risk`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
银行会在交易完成后发送电子对账单。
```

Codex expected:

```text
銀行會在交易完成後傳送電子對帳單。
```

Gemini expected:

```text
銀行會在交易完成後寄送電子對帳單。
```

Gemini acceptable variants:

```text
銀行會在交易完成後發送電子對帳單。
```

Gemini notes:

```text
「寄送」在台灣更常用於發送文件或帳單，比「發送」更自然。
```

### blind-high-risk-0013：match

- Domain: `high_risk`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
申请贷款前，请确认利率和还款期限。
```

Codex expected:

```text
申請貸款前，請確認利率和還款期限。
```

Gemini expected:

```text
申請貸款前，請確認利率和還款期限。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text

```

### blind-high-risk-0014：match

- Domain: `high_risk`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
药品说明应清楚标示使用剂量和禁忌。
```

Codex expected:

```text
藥品說明應清楚標示使用劑量和禁忌。
```

Gemini expected:

```text
藥品說明應清楚標示使用劑量和禁忌。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text

```

### blind-high-risk-0015：match

- Domain: `high_risk`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
保险契约变更需要经双方书面同意。
```

Codex expected:

```text
保險契約變更需要經雙方書面同意。
```

Gemini expected:

```text
保險契約變更需要經雙方書面同意。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text

```

### blind-high-risk-0016：different

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
不得以格式条款免除故意或重大过失责任。
```

Codex expected:

```text
不得以定型化契約條款免除故意或重大過失責任。
```

Gemini expected:

```text
不得以格式條款免除故意或重大過失責任。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text

```

### blind-high-risk-0017：match

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
病历中的专有缩写不得任意改写。
```

Codex expected:

```text
病歷中的專有縮寫不得任意改寫。
```

Gemini expected:

```text
病歷中的專有縮寫不得任意改寫。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text

```

### blind-high-risk-0018：match

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
金融机构应保留客户原始签署文件。
```

Codex expected:

```text
金融機構應保留客戶原始簽署文件。
```

Gemini expected:

```text
金融機構應保留客戶原始簽署文件。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text

```

### blind-high-risk-0019：match

- Domain: `high_risk`
- Risk: `baseline_guard`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
请妥善保管个人身份证件。
```

Codex expected:

```text
請妥善保管個人身分證件。
```

Gemini expected:

```text
請妥善保管個人身分證件。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text

```

### blind-high-risk-0020：match

- Domain: `high_risk`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
未成年人开户需由法定代理人陪同。
```

Codex expected:

```text
未成年人開戶需由法定代理人陪同。
```

Gemini expected:

```text
未成年人開戶需由法定代理人陪同。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text

```
