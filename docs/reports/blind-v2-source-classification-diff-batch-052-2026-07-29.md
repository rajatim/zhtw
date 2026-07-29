<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 052 (2026-07-29)

Status: advisory only; maintainer decisions pending

Packet SHA-256: `e7f94c66809755cec12b6f3f84de79253dd9839e4ff4d5143c5d68bc1e25d2e1`
Cases: 96
Exact Codex/Gemini classifications: 51
Maintainer review queue: 45

Field differences:

- Eligibility: 8
- Script: 3
- Domain: 24
- Risk: 35

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

Neither advisory is auto-preferred. Codex must synthesize the differences before maintainer confirmation; no classification in this report has been written into the candidate pool.

## Review Queue

### 01. kubernetes-docs-zh-cn-v1/page-02-sentence-0008

Changed: `risk`

Input:

```text
这是开始或者在集群中运行一次性任务的推荐方法。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains the technical term "集群" (cluster) which has a different preferred translation in Taiwan.

Maintainer decision: `pending`

### 02. kubernetes-docs-zh-cn-v1/page-02-sentence-0014

Changed: `risk`

Input:

```text
命令不提供用于创建新对象的模板。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A straightforward sentence about technical concepts.

Maintainer decision: `pending`

### 03. kubernetes-docs-zh-cn-v1/page-02-sentence-0019

Changed: `risk`

Input:

```text
此方法不应与对象规约被独立于配置文件进行更新的资源类型一起使用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The terms "规约" (spec) and "配置文件" (config file) require idiomatic translation.

Maintainer decision: `pending`

### 04. kubernetes-docs-zh-cn-v1/page-03-sentence-0074

Changed: `risk`

Input:

```text
这种机制可以防止有问题的容器因不断进行启动失败尝试而导致系统不堪重负。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A standard technical sentence where basic conversion should suffice.

Maintainer decision: `pending`

### 05. kubernetes-docs-zh-cn-v1/page-03-sentence-0090

Changed: `eligible, domain, risk`

Input:

```text
你可以将重启配置为适用于所有 Pod 的策略，或者使用容器级别的配置（例如：在你定义或定义容器级别重载时）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | it_api_cli | over_conversion_guard | high | source_translation_error |

Codex reason: Codex excluded this input-only case because its source text is malformed, incomplete, duplicated, context-dependent, or unsafe as a standalone conversion target.

Gemini reason: The parenthetical phrase seems redundant or poorly translated ("在你定义或定义...").

Maintainer decision: `pending`

### 06. kubernetes-docs-zh-cn-v1/page-03-sentence-0244

Changed: `eligible, domain, risk`

Input:

```text
如果你希望容器能够自行进入维护状态，也可以指定一个就绪态探针，检查某个特定于就绪态的因此不同于存活态探测的端点。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Codex excluded this input-only case because its source text is malformed, incomplete, duplicated, context-dependent, or unsafe as a standalone conversion target.

Gemini reason: A complex sentence describing technical probes with somewhat awkward phrasing.

Maintainer decision: `pending`

### 07. kubernetes-docs-zh-cn-v1/page-04-sentence-0014

Changed: `risk`

Input:

```text
这些副本是可互换的 —— 前端不需要关心它们调用的是哪个后端。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Common IT terms like '副本' (replicas), '前端' (front-end) and '后端' (back-end) may require locale-specific wording.

Maintainer decision: `pending`

### 08. kubernetes-docs-zh-cn-v1/page-04-sentence-0166

Changed: `risk`

Input:

```text
此字段的定义模糊，其含义因实现而异。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Technical terms '字段' (field) and '实现' (implementation) require locale-specific vocabulary ('欄位', '實作').

Maintainer decision: `pending`

### 09. kubernetes-docs-zh-cn-v1/page-04-sentence-0184

Changed: `eligible, domain, risk`

Input:

```text
默认情况下，`.spec.loadBalancerClass` 是未设置的，如果集群使用 `--cloud-provider` 件标志配置了云平台，`LoadBalancer` 类型 Service 会使用云平台的默认负载均衡器实现。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | it_api_cli | over_conversion_guard | high | source_error |

Codex reason: Codex excluded this input-only case because its source text is malformed, incomplete, duplicated, context-dependent, or unsafe as a standalone conversion target.

Gemini reason: Contains a likely source error ('件标志'), but is otherwise a good test case for preserving multiple code identifiers.

Maintainer decision: `pending`

### 10. ready-gov-are-you-ready-guide-simplified-v1/sentence-015

Changed: `domain, risk`

Input:

```text
大多数社区面临多种类型的危险。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A standard informational sentence about community risks.

Maintainer decision: `pending`

### 11. ready-gov-are-you-ready-guide-simplified-v1/sentence-016

Changed: `eligible, domain, risk`

Input:

```text
重要的是要了解您的住房的具体风险以及如果离家时，则应如何评估风险。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex excluded this input-only case because its source text is malformed, incomplete, duplicated, context-dependent, or unsafe as a standalone conversion target.

Gemini reason: Sentence structure and vocabulary like '住房' (housing) may require adaptation.

Maintainer decision: `pending`

### 12. ready-gov-are-you-ready-guide-simplified-v1/sentence-069

Changed: `risk`

Input:

```text
参加培训课程以学习急救技能，包括如何止血和进行 C P R（心肺复苏术）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | odd_spacing |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Medical term 'C P R' must be protected from over-conversion.

Maintainer decision: `pending`

### 13. ready-gov-are-you-ready-guide-simplified-v1/sentence-078

Changed: `domain, risk`

Input:

```text
参加培训课程，学习如何识别危险情况，要避免的地方以及正确使用安全和救援设备的方法。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A standard instructional sentence about safety training.

Maintainer decision: `pending`

### 14. ready-gov-are-you-ready-guide-simplified-v1/sentence-081

Changed: `script, risk`

Input:

```text
避免高风险区域，例如坡度大于30度的山坡或陡峭的下坡区域。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The numerical value '30' is a technical token requiring protection.

Maintainer decision: `pending`

### 15. ready-gov-are-you-ready-guide-simplified-v1/sentence-151

Changed: `risk`

Input:

```text
避开地下室和较低楼层，但不要爬进封闭的阁楼，因为如果洪水涨高，您可能会被困其中。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Standard safety warning with common vocabulary.

Maintainer decision: `pending`

### 16. ready-gov-are-you-ready-guide-simplified-v1/sentence-215

Changed: `domain, risk`

Input:

```text
停电时规划用电池和其他替代产品，来满足停电时的需求。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | medium | repetitive |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Slightly repetitive phrasing but still a valid candidate.

Maintainer decision: `pending`

### 17. ready-gov-are-you-ready-guide-simplified-v1/sentence-229

Changed: `eligible, script, domain, risk`

Input:

```text
扔掉所有暴露于40度或更高温度下两个小时以上，或有异味、变色或变质的食物。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Codex excluded this input-only case because its source text is malformed, incomplete, duplicated, context-dependent, or unsafe as a standalone conversion target.

Gemini reason: Food safety instruction where the number '40' must be protected.

Maintainer decision: `pending`

### 18. ready-gov-are-you-ready-guide-simplified-v1/sentence-254

Changed: `domain, risk`

Input:

```text
国家气象局对特定危害的“警戒”和“警告”定义有所不同，如在 Weather.gov所述。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The URL 'Weather.gov' must be protected from conversion.

Maintainer decision: `pending`

### 19. ready-gov-are-you-ready-guide-simplified-v1/sentence-256

Changed: `domain, risk`

Input:

```text
认真遵守警戒和警告，以了解接下来要采取的措施。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Standard sentence using official meteorological terminology.

Maintainer decision: `pending`

### 20. ready-gov-are-you-ready-guide-simplified-v1/sentence-296

Changed: `eligible, domain, risk`

Input:

```text
冬季风暴 • 使用绝缘材料、填缝剂和挡风雨条为房屋做好防寒准备。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex excluded this input-only case because its source text is malformed, incomplete, duplicated, context-dependent, or unsafe as a standalone conversion target.

Gemini reason: Home winterization advice using several technical terms that may require specific regional equivalents.

Maintainer decision: `pending`

### 21. ready-gov-are-you-ready-guide-simplified-v1/sentence-343

Changed: `risk`

Input:

```text
警惕道路危险，例如被冲毁的道路或桥梁以及掉落的电线。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A warning about common road hazards post-disaster, using standard vocabulary.

Maintainer decision: `pending`

### 22. ready-gov-are-you-ready-guide-simplified-v1/sentence-377

Changed: `script`

Input:

```text
如果您需要留在原处，则为车辆和工作场所准备单独小套的应急用品，至少可以维持 24 小时。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Recommends preparing separate 24-hour emergency kits for vehicles and workplaces.

Maintainer decision: `pending`

### 23. ready-gov-are-you-ready-guide-simplified-v1/sentence-404

Changed: `eligible, domain, risk`

Input:

```text
有些可能有移动应用程序，以确保灾难发生时您可以接收信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_reference |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex excluded this input-only case because its source text is malformed, incomplete, duplicated, context-dependent, or unsafe as a standalone conversion target.

Gemini reason: Suggests using mobile apps to receive information during a disaster.

Maintainer decision: `pending`

### 24. ready-gov-are-you-ready-guide-simplified-v1/sentence-432

Changed: `eligible, domain, risk`

Input:

```text
只有洪水保险才能防止洪水造成的情感和经济毁坏。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex excluded this input-only case because its source text is malformed, incomplete, duplicated, context-dependent, or unsafe as a standalone conversion target.

Gemini reason: A statement on the importance of flood insurance for preventing financial and emotional damage.

Maintainer decision: `pending`

### 25. ready-gov-are-you-ready-guide-simplified-v1/sentence-472

Changed: `risk`

Input:

```text
购买洪水保险或其他有关的保险。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A simple, direct recommendation to purchase flood insurance or other related policies.

Maintainer decision: `pending`

### 26. ready-gov-are-you-ready-guide-simplified-v1/sentence-562

Changed: `risk`

Input:

```text
FEMA的衬衫或联邦小企业管理局（SBA）工作外套不是绝对的身份证明。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Fraud warning specifying that FEMA/SBA apparel is not absolute proof of identity.

Maintainer decision: `pending`

### 27. ready-gov-are-you-ready-guide-simplified-v1/sentence-570

Changed: `risk`

Input:

```text
FEMA 和 SBA的工作人员从不为灾难帮助、检查或填写申请表向申请人收费。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: States clearly that official FEMA and SBA staff do not charge fees for help.

Maintainer decision: `pending`

### 28. zhtw-project-formal-llm-evidence-guard-v1/formal-003

Changed: `domain`

Input:

```text
审计单位将抽查原始凭证与付款授权记录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This is a standard formal sentence from an audit or financial context.

Maintainer decision: `pending`

### 29. zhtw-project-formal-llm-evidence-guard-v1/formal-005

Changed: `domain`

Input:

```text
法院公告载明裁定主文与救济期限。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This sentence contains formal legal terminology specific to a jurisdiction.

Maintainer decision: `pending`

### 30. zhtw-project-formal-llm-evidence-guard-v1/formal-006

Changed: `risk`

Input:

```text
研究人员公开问卷设计及样本筛选条件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This is a formal sentence from a research or academic context.

Maintainer decision: `pending`

### 31. zhtw-project-formal-llm-evidence-guard-v1/formal-008

Changed: `domain`

Input:

```text
评审小组将利益冲突声明纳入会议档案。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This is a formal procedural sentence regarding conflict of interest.

Maintainer decision: `pending`

### 32. zhtw-project-formal-llm-evidence-guard-v1/formal-010

Changed: `domain`

Input:

```text
申请人须说明资料缺漏的原因及补正方式。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This sentence describes a requirement in a formal application process.

Maintainer decision: `pending`

### 33. zhtw-project-formal-llm-evidence-guard-v1/formal-012

Changed: `domain`

Input:

```text
调查人员分别记录目击者陈述与客观证据。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This sentence is from a formal investigative or legal context.

Maintainer decision: `pending`

### 34. zhtw-project-formal-llm-evidence-guard-v1/formal-014

Changed: `domain, risk`

Input:

```text
听证纪录应标示发言者身份及发言顺序。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This sentence describes a procedural requirement for official hearing records.

Maintainer decision: `pending`

### 35. zhtw-project-formal-llm-evidence-guard-v1/formal-016

Changed: `domain`

Input:

```text
采购文件要求厂商保存材料来源证明。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This is a formal sentence from a business or procurement context.

Maintainer decision: `pending`

### 36. zhtw-project-formal-llm-evidence-guard-v1/formal-023

Changed: `risk`

Input:

```text
决议附件列明各单位负责的工作项目。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This is a standard sentence from a formal administrative or corporate document.

Maintainer decision: `pending`

### 37. zhtw-project-formal-llm-evidence-guard-v1/formal-028

Changed: `domain`

Input:

```text
公告同时提供修正理由和条文对照表。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This sentence describes the contents of a formal legal or administrative announcement.

Maintainer decision: `pending`

### 38. zhtw-project-formal-llm-evidence-guard-v1/formal-029

Changed: `domain`

Input:

```text
财政报告将一次性收入与经常性收入分开计算。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This sentence contains specific financial reporting terminology.

Maintainer decision: `pending`

### 39. zhtw-project-formal-llm-evidence-guard-v1/formal-038

Changed: `domain, risk`

Input:

```text
申请资料中的名称应以核定文件为准。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This sentence specifies a rule for names in official application materials.

Maintainer decision: `pending`

### 40. zhtw-project-formal-llm-evidence-guard-v1/formal-040

Changed: `domain`

Input:

```text
调查小组未取得授权前不得公开个人资料。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This is a formal sentence concerning legal requirements for handling personal data.

Maintainer decision: `pending`

### 41. zhtw-project-formal-llm-evidence-guard-v1/llm-008

Changed: `risk`

Input:

```text
模型应保留引文中的产品名称和版本编号。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The instruction to preserve product names and version numbers makes this a guard against over-conversion.

Maintainer decision: `pending`

### 42. zhtw-project-formal-llm-evidence-guard-v1/llm-015

Changed: `risk`

Input:

```text
引用网页时应保留原始发布时间与更新日期。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This is a straightforward instruction where a conservative character conversion should be sufficient.

Maintainer decision: `pending`

### 43. zhtw-project-formal-llm-evidence-guard-v1/llm-030

Changed: `risk`

Input:

```text
系统会比较多个来源对同一事件的描述。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This describes a general system function with common vocabulary, suitable for a baseline conversion check.

Maintainer decision: `pending`

### 44. zhtw-project-formal-llm-evidence-guard-v1/llm-036

Changed: `risk`

Input:

```text
回答中的日期必须对应来源所在的时区。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This is a simple rule with standard vocabulary where basic conversion should be effective.

Maintainer decision: `pending`

### 45. zhtw-project-formal-llm-evidence-guard-v1/llm-040

Changed: `risk`

Input:

```text
模型需要保留命令范例中的引号和选项顺序。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This is a rule about preserving syntax, making it a test for preventing unwanted conversion of code-related elements.

Maintainer decision: `pending`
