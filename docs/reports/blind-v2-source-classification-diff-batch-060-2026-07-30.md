<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 060 (2026-07-30)

Status: advisory only; maintainer decisions pending

Packet SHA-256: `03c46a873a5548bfacb3dd9400155f697a34cc4335b4acfa6035ef7032e1a284`
Cases: 96
Exact Codex/Gemini classifications: 47
Maintainer review queue: 49

Field differences:

- Eligibility: 1
- Script: 21
- Domain: 24
- Risk: 36

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

Neither advisory is auto-preferred. Codex must synthesize the differences before maintainer confirmation; no classification in this report has been written into the candidate pool.

## Review Queue

### 01. aosp-framework-zh-rcn-v1/string-199a1d51e698a9a0

Changed: `script, risk`

Input:

```text
已更改为新的 SS 请求
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete status message containing Latin abbreviation.

Maintainer decision: `pending`

### 02. aosp-framework-zh-rcn-v1/string-20d987272ce62f00

Changed: `script, risk`

Input:

```text
{count,plural, =1{# 天}other{# 天}}
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete ICU message format string with plural placeholder.

Maintainer decision: `pending`

### 03. aosp-framework-zh-rcn-v1/string-4c1a4c022c7f24aa

Changed: `script, risk`

Input:

```text
PIN码有误
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete UI error message with Latin acronym PIN.

Maintainer decision: `pending`

### 04. aosp-framework-zh-rcn-v1/string-62e4f1bd0e6620f3

Changed: `script, risk`

Input:

```text
勿扰 (%1$s)
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete UI status label with string placeholder.

Maintainer decision: `pending`

### 05. aosp-framework-zh-rcn-v1/string-79ada3ba8e6f9435

Changed: `script, risk`

Input:

```text
运行“camera”类型的前台服务
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete Android UI string containing technical terms like 前台服务 and 运行.

Maintainer decision: `pending`

### 06. aosp-framework-zh-rcn-v1/string-92669ea213e118d9

Changed: `script, risk`

Input:

```text
账号 %3$s 在进行“%2$s”同步时删除了 %1$d 项内容。您要如何处理这些删除的内容？
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete user prompt dialog message with multiple string format placeholders.

Maintainer decision: `pending`

### 07. aosp-framework-zh-rcn-v1/string-9901024cc0a8149b

Changed: `script, risk`

Input:

```text
允许该应用使用“remoteMessaging”类型的前台服务
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete permission string including mixed Latin service type identifiers.

Maintainer decision: `pending`

### 08. aosp-framework-zh-rcn-v1/string-a4ba01c4b7aea276

Changed: `risk`

Input:

```text
所有语言
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Standard short UI menu option label.

Maintainer decision: `pending`

### 09. aosp-framework-zh-rcn-v1/string-d7683137df575bf2

Changed: `script`

Input:

```text
工作 2
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Short workspace profile identifier containing shared Hanzi and ASCII digit.

Maintainer decision: `pending`

### 10. aosp-framework-zh-rcn-v1/string-f51f5fe3a3626b34

Changed: `script, risk`

Input:

```text
%1$s的自动填充功能
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete UI feature title string starting with a placeholder.

Maintainer decision: `pending`

### 11. ready-gov-are-you-ready-guide-simplified-v1/sentence-087

Changed: `domain, risk`

Input:

```text
使用强密码和双因素身份验证。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete IT security instruction containing standard terminology (strong passwords, 2FA).

Maintainer decision: `pending`

### 12. ready-gov-are-you-ready-guide-simplified-v1/sentence-090

Changed: `domain, risk`

Input:

```text
拥有防病毒和防火墙的解决方案来阻止恶意软件和其他威胁。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete IT cybersecurity advice covering antivirus, firewall, and malware solutions.

Maintainer decision: `pending`

### 13. ready-gov-are-you-ready-guide-simplified-v1/sentence-161

Changed: `risk`

Input:

```text
熟悉撤离区，撤离路线和庇护所的位置。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete emergency guidance sentence with location terms.

Maintainer decision: `pending`

### 14. ready-gov-are-you-ready-guide-simplified-v1/sentence-282

Changed: `script`

Input:

```text
从房产30英尺范围内清除天然气、石油、煤油和其他燃料，以及可能着火的物品，例如垃圾和院子废弃物。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete fire safety instruction sentence.

Maintainer decision: `pending`

### 15. ready-gov-are-you-ready-guide-simplified-v1/sentence-304

Changed: `risk`

Input:

```text
仅在户外且远离窗户的地方使用发电机和烤炉。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete generator safety sentence containing vocabulary terms like 窗户.

Maintainer decision: `pending`

### 16. ready-gov-are-you-ready-guide-simplified-v1/sentence-434

Changed: `risk`

Input:

```text
如果您的房产有遭受洪水或泥石流（包括飓风或地震造成的洪水）的风险，请与您的保险经纪人联系。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete advisory sentence containing terms like 泥石流 and 联系.

Maintainer decision: `pending`

### 17. ready-gov-are-you-ready-guide-simplified-v1/sentence-446

Changed: `risk`

Input:

```text
对于您家里的财物清单，请拍照或录像以记录您的财产并记下年份、品牌和型号等说明。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete guidance sentence containing vocabulary like 录像 and 型号.

Maintainer decision: `pending`

### 18. ready-gov-are-you-ready-guide-simplified-v1/sentence-479

Changed: `risk`

Input:

```text
许多社区都有地方应急准备委员会，为突发事件提供备灾资源和计划。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete sentence on community emergency committees containing terms like 应急 and 计划.

Maintainer decision: `pending`

### 19. ready-gov-are-you-ready-guide-simplified-v1/sentence-482

Changed: `eligible, domain, risk`

Input:

```text
两个项目都授权公众通过自愿预防犯罪来保护社区。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | insufficient_context |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex excluded this input-only case because the source text is not reliable enough for an independently judgeable conversion benchmark.

Gemini reason: Complete descriptive sentence containing terms like 项目 and 通过.

Maintainer decision: `pending`

### 20. ready-gov-are-you-ready-guide-simplified-v1/sentence-507

Changed: `risk`

Input:

```text
拍摄损坏的图片和视频，并对维修和清洁的花费做准确的记录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete instruction sentence containing terms like 视频 and 记录.

Maintainer decision: `pending`

### 21. ready-gov-are-you-ready-guide-simplified-v1/sentence-563

Changed: `risk`

Input:

```text
除非您确定安全，否则请勿泄露个人信息，例如社会保障号码或银行帐号。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete privacy warning sentence containing terms like 个人信息, 确定, and 帐号.

Maintainer decision: `pending`

### 22. zhtw-project-llm-formal-operations-guard-v1/formal-002

Changed: `domain, risk`

Input:

```text
核定结果将以书面通知申请人。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete administrative notification sentence testing standard baseline conversion.

Maintainer decision: `pending`

### 23. zhtw-project-llm-formal-operations-guard-v1/formal-007

Changed: `domain, risk`

Input:

```text
业者应在改善期限届满前提交佐证资料。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete regulatory compliance statement testing formal business terminology.

Maintainer decision: `pending`

### 24. zhtw-project-llm-formal-operations-guard-v1/formal-011

Changed: `domain, risk`

Input:

```text
主管机关要求各单位统一资料格式。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete government authority requirement statement.

Maintainer decision: `pending`

### 25. zhtw-project-llm-formal-operations-guard-v1/formal-012

Changed: `domain, risk`

Input:

```text
公开说明会将同步提供会议资料。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete formal public presentation notice sentence.

Maintainer decision: `pending`

### 26. zhtw-project-llm-formal-operations-guard-v1/formal-020

Changed: `domain, risk`

Input:

```text
核定名单将依类别名称分别公布。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete official announcement sentence.

Maintainer decision: `pending`

### 27. zhtw-project-llm-formal-operations-guard-v1/formal-021

Changed: `script, domain`

Input:

```text
采购公告保留案件编号 PROC-2026-118。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains alphanumeric procurement identifier PROC-2026-118 requiring non-alteration.

Maintainer decision: `pending`

### 28. zhtw-project-llm-formal-operations-guard-v1/formal-022

Changed: `script, domain`

Input:

```text
审计附件引用凭证编号 INV-TW-0842。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains Latin audit invoice code INV-TW-0842 requiring non-alteration.

Maintainer decision: `pending`

### 29. zhtw-project-llm-formal-operations-guard-v1/formal-023

Changed: `script, domain`

Input:

```text
法院卷宗以 Case No. 26-CV-104 标示案件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains legal case identifier Case No. 26-CV-104 requiring non-alteration.

Maintainer decision: `pending`

### 30. zhtw-project-llm-formal-operations-guard-v1/formal-024

Changed: `script, domain`

Input:

```text
公报附件沿用 Appendix IV 的标题。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains English appendix designation Appendix IV requiring non-alteration.

Maintainer decision: `pending`

### 31. zhtw-project-llm-formal-operations-guard-v1/formal-025

Changed: `script, domain`

Input:

```text
技术报告引用 DOI 10.1000/xyz123。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains standard DOI string DOI 10.1000/xyz123 requiring non-alteration.

Maintainer decision: `pending`

### 32. zhtw-project-llm-formal-operations-guard-v1/formal-034

Changed: `domain, risk`

Input:

```text
主管机关得要求补充风险评估资料。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete formal legal/regulatory provision sentence.

Maintainer decision: `pending`

### 33. zhtw-project-llm-formal-operations-guard-v1/formal-044

Changed: `domain, risk`

Input:

```text
资料检核完成后才会产生缴费通知。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete administrative workflow and payment process sentence.

Maintainer decision: `pending`

### 34. zhtw-project-llm-formal-operations-guard-v1/formal-047

Changed: `domain, risk`

Input:

```text
公开资料应遮蔽帐号与联络资讯。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Privacy data protection rule sentence testing exact terminology handling.

Maintainer decision: `pending`

### 35. zhtw-project-llm-formal-operations-guard-v1/formal-048

Changed: `domain, risk`

Input:

```text
复审结果不会影响已经核定的给付。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Administrative review and benefits policy sentence testing disambiguation for 复/給付.

Maintainer decision: `pending`

### 36. zhtw-project-llm-formal-operations-guard-v1/formal-049

Changed: `domain, risk`

Input:

```text
报告结论仅适用于本次调查范围。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Formal investigation report disclaimer sentence.

Maintainer decision: `pending`

### 37. zhtw-project-llm-formal-operations-guard-v1/llm-003

Changed: `risk`

Input:

```text
模型不得把空白状态误写成系统错误。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Instruction spec clause targeting model error states.

Maintainer decision: `pending`

### 38. zhtw-project-llm-formal-operations-guard-v1/llm-010

Changed: `risk`

Input:

```text
回答应分别列出本机设定和远端设定。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete Simplified Chinese sentence specifying model output requirements with TW terminology.

Maintainer decision: `pending`

### 39. zhtw-project-llm-formal-operations-guard-v1/llm-013

Changed: `risk`

Input:

```text
请勿把联络窗口自动替换成联络人姓名。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete Simplified Chinese input for AI behavior guard.

Maintainer decision: `pending`

### 40. zhtw-project-llm-formal-operations-guard-v1/llm-016

Changed: `risk`

Input:

```text
模型应把资料库迁移和资料汇入视为不同操作。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete Simplified Chinese prompt containing TW domain terms in Simplified script.

Maintainer decision: `pending`

### 41. zhtw-project-llm-formal-operations-guard-v1/llm-021

Changed: `script, domain`

Input:

```text
请保留追踪编号 TRACE-2026-0730-A。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains Latin identifier TRACE-2026-0730-A requiring exact preservation.

Maintainer decision: `pending`

### 42. zhtw-project-llm-formal-operations-guard-v1/llm-023

Changed: `script, domain`

Input:

```text
请勿调整命令 kubectl rollout status 的参数顺序。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains CLI command kubectl rollout status which must be preserved.

Maintainer decision: `pending`

### 43. zhtw-project-llm-formal-operations-guard-v1/llm-026

Changed: `script, domain`

Input:

```text
回答应保留 HTTP 409 与错误代码 RECORD_IN_USE。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains HTTP status code and error string identifier.

Maintainer decision: `pending`

### 44. zhtw-project-llm-formal-operations-guard-v1/llm-027

Changed: `script, domain`

Input:

```text
请勿把分支名称 release/2026.07 转换成日期。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains Git branch name release/2026.07 requiring strict preservation.

Maintainer decision: `pending`

### 45. zhtw-project-llm-formal-operations-guard-v1/llm-028

Changed: `script, domain`

Input:

```text
模型必须维持 SHA-256 值的大小写与长度。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains technical algorithm name SHA-256 requiring non-alteration.

Maintainer decision: `pending`

### 46. zhtw-project-llm-formal-operations-guard-v1/llm-039

Changed: `risk`

Input:

```text
模型需要保留引文中的原始标点。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete Simplified Chinese requirement for LLM output.

Maintainer decision: `pending`

### 47. zhtw-project-llm-formal-operations-guard-v1/llm-041

Changed: `risk`

Input:

```text
如果使用者只要求检视，请勿执行写入操作。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains TW terminology in Simplified script requiring faithful conversion.

Maintainer decision: `pending`

### 48. zhtw-project-llm-formal-operations-guard-v1/llm-048

Changed: `script, domain`

Input:

```text
模型应保留引用中的 RFC 9110 章节编号。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains RFC specification identifier RFC 9110.

Maintainer decision: `pending`

### 49. zhtw-project-llm-formal-operations-guard-v1/llm-050

Changed: `risk`

Input:

```text
回答完成前应再次核对数量、单位和时区。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete Simplified Chinese validation requirement.

Maintainer decision: `pending`
