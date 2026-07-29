<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 053 (2026-07-29)

Status: advisory only; maintainer decisions pending

Packet SHA-256: `e87770108af867ece6a3b345b29db1dac8e05c37bf702f3f211e4bca5fb3d2b3`
Cases: 96
Exact Codex/Gemini classifications: 40
Maintainer review queue: 56

Field differences:

- Eligibility: 7
- Script: 5
- Domain: 16
- Risk: 53

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

Neither advisory is auto-preferred. Codex must synthesize the differences before maintainer confirmation; no classification in this report has been written into the candidate pool.

## Review Queue

### 01. kubernetes-docs-zh-cn-v1/page-01-sentence-0014

Changed: `script, risk`

Input:

```text
很多资源类型需要可以用作 DNS 子域名的名称。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This sentence uses technical terms that may have different idiomatic equivalents in Taiwan Mandarin.

Maintainer decision: `pending`

### 02. kubernetes-docs-zh-cn-v1/page-03-sentence-0007

Changed: `risk`

Input:

```text
在 Pod 内部，Kubernetes 跟踪不同容器的状态并确定使 Pod 重新变得健康所需要采取的动作。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The sentence describes a technical process where idiomatic phrasing for state changes may differ.

Maintainer decision: `pending`

### 03. kubernetes-docs-zh-cn-v1/page-03-sentence-0011

Changed: `risk`

Input:

```text
Pod 在其生命周期中只会被调度一次。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A simple sentence with key technical terms that could have idiomatic variants.

Maintainer decision: `pending`

### 04. kubernetes-docs-zh-cn-v1/page-03-sentence-0083

Changed: `risk`

Input:

```text
审查配置：确保 Pod 配置正确无误，包括环境变量和挂载卷，并且所有必需的外部资源都可用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This sentence contains a list of technical terms that require idiomatic validation.

Maintainer decision: `pending`

### 05. kubernetes-docs-zh-cn-v1/page-03-sentence-0199

Changed: `script, risk`

Input:

```text
有关执行原地调整大小的详细说明，请参见调整分配给容器的 CPU 和内存资源。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The sentence uses a key technical phrase, 'in-place resizing', that needs idiomatic verification.

Maintainer decision: `pending`

### 06. kubernetes-docs-zh-cn-v1/page-03-sentence-0229

Changed: `eligible, script, domain, risk`

Input:

```text
如果存活态探测失败，则 kubelet 会杀死容器，并且容器将根据其重启策略决定未来。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex excluded this input-only case because its source text is malformed, incomplete, duplicated, context-dependent, or unsafe as a standalone conversion target.

Gemini reason: A standard technical documentation sentence about liveness probes and container restart policies.

Maintainer decision: `pending`

### 07. kubernetes-docs-zh-cn-v1/page-03-sentence-0328

Changed: `risk`

Input:

```text
参阅 Pod 干扰状况了解更多详情。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Sentence references Pod disruption, which may have different terminology in Taiwan.

Maintainer decision: `pending`

### 08. kubernetes-docs-zh-cn-v1/page-04-sentence-0062

Changed: `script, risk`

Input:

```text
端点 IP 地址不能是其他 Kubernetes 服务的集群 IP，因为不支持将虚拟 IP 作为目标地址。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A good baseline test for standard networking and Kubernetes terminology.

Maintainer decision: `pending`

### 09. kubernetes-docs-zh-cn-v1/page-04-sentence-0099

Changed: `risk`

Input:

```text
Kubernetes 允许你为 Service 对象配置多个端口定义。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A straightforward sentence about configuring Service ports.

Maintainer decision: `pending`

### 10. kubernetes-docs-zh-cn-v1/page-04-sentence-0177

Changed: `risk`

Input:

```text
可用于负载均衡 Service 的协议集合由你的云平台决定，他们可能在 Kubernetes API 强制执行的限制之外另加一些约束。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Sentence about load balancing and cloud platforms where phrasing may differ.

Maintainer decision: `pending`

### 11. kubernetes-docs-zh-cn-v1/page-04-sentence-0213

Changed: `risk`

Input:

```text
你可以使用无头 Service 与其他服务发现机制交互，而不必绑定到 Kubernetes 的实现。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Features the specific technical term "headless Service" which requires correct handling.

Maintainer decision: `pending`

### 12. kubernetes-docs-zh-cn-v1/page-04-sentence-0230

Changed: `risk`

Input:

```text
如果仅使用 DNS 来发现 Service 的集群 IP，则无需担心此顺序问题。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A straightforward technical sentence about DNS and cluster IPs.

Maintainer decision: `pending`

### 13. ready-gov-are-you-ready-guide-simplified-v1/sentence-008

Changed: `eligible, domain, risk`

Input:

```text
在本文件中，您将学习有关灾难发生之前，期间和之后的一般备灾技巧，以及关于针对特定灾难特定灾难（例如飓风、地震和行凶的枪手）的备灾决策方面的最佳做法。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex excluded this input-only case because its source text is malformed, incomplete, duplicated, context-dependent, or unsafe as a standalone conversion target.

Gemini reason: Formal instructional text about disaster preparedness, where terms like "active shooter" may have regional variants.

Maintainer decision: `pending`

### 14. ready-gov-are-you-ready-guide-simplified-v1/sentence-029

Changed: `eligible, domain, risk`

Input:

```text
确定您的风险有很多不同类型的灾难和危害。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | high_stakes | baseline_guard | high | awkward_phrasing |

Codex reason: Codex excluded this input-only case because its source text is malformed, incomplete, duplicated, context-dependent, or unsafe as a standalone conversion target.

Gemini reason: The sentence structure is slightly awkward, likely a translation artifact, but remains understandable.

Maintainer decision: `pending`

### 15. ready-gov-are-you-ready-guide-simplified-v1/sentence-056

Changed: `eligible, domain, risk`

Input:

```text
特定危害的关键防护措施根据危险情况，应采取的保护措施有所不同。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | high_stakes | baseline_guard | medium | possible_heading |

Codex reason: Codex excluded this input-only case because its source text is malformed, incomplete, duplicated, context-dependent, or unsafe as a standalone conversion target.

Gemini reason: This appears to be a heading concatenated with a full sentence, making it awkward as a single item.

Maintainer decision: `pending`

### 16. ready-gov-are-you-ready-guide-simplified-v1/sentence-064

Changed: `risk`

Input:

```text
将电子设备静音，锁上或堵住门，关闭百叶窗，然后关灯。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A clear, direct, and list-like instruction for an emergency situation.

Maintainer decision: `pending`

### 17. ready-gov-are-you-ready-guide-simplified-v1/sentence-065

Changed: `risk`

Input:

```text
不要成群结队地躲在一起，沿墙壁散开或单独躲藏。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clear and direct safety instruction for hiding during an emergency.

Maintainer decision: `pending`

### 18. ready-gov-are-you-ready-guide-simplified-v1/sentence-072

Changed: `risk`

Input:

```text
良好的藏身之处包括：无窗房间，带锁的实心门后面、书桌下或重型家具后面。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A clear, list-like sentence providing examples of good hiding places.

Maintainer decision: `pending`

### 19. ready-gov-are-you-ready-guide-simplified-v1/sentence-073

Changed: `risk`

Input:

```text
保持双手可见，并保持空手。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A direct, high-stakes instruction, likely for interacting with law enforcement.

Maintainer decision: `pending`

### 20. ready-gov-are-you-ready-guide-simplified-v1/sentence-089

Changed: `risk`

Input:

```text
使用加密的（安全）互联网通信。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: An instruction about secure internet use with a parenthetical clarification.

Maintainer decision: `pending`

### 21. ready-gov-are-you-ready-guide-simplified-v1/sentence-113

Changed: `risk`

Input:

```text
如果在户外，寻找阴凉的地方。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Simple and clear health and safety advice for being outdoors.

Maintainer decision: `pending`

### 22. ready-gov-are-you-ready-guide-simplified-v1/sentence-163

Changed: `eligible, domain, risk`

Input:

```text
次好的保护措施是在坚固建筑物不会受到洪水侵袭的最底层小型室内无窗房间。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex excluded this input-only case because its source text is malformed, incomplete, duplicated, context-dependent, or unsafe as a standalone conversion target.

Gemini reason: A complex but grammatically correct sentence providing a specific safety instruction.

Maintainer decision: `pending`

### 23. ready-gov-are-you-ready-guide-simplified-v1/sentence-199

Changed: `script, risk`

Input:

```text
在您的家里和办公室中保留一个24小时应急用品箱。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A straightforward instruction involving a number that must be preserved.

Maintainer decision: `pending`

### 24. ready-gov-are-you-ready-guide-simplified-v1/sentence-211

Changed: `risk`

Input:

```text
当外出到公共场合时，请穿戴口罩以遮住口鼻。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clear public health instruction relevant to a pandemic.

Maintainer decision: `pending`

### 25. ready-gov-are-you-ready-guide-simplified-v1/sentence-219

Changed: `risk`

Input:

```text
如果用汽车给设备充电，请不要让汽车在车库，半封闭的空间或靠近家中运行，以免一氧化碳中毒。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A critical safety warning about carbon monoxide poisoning from a vehicle.

Maintainer decision: `pending`

### 26. ready-gov-are-you-ready-guide-simplified-v1/sentence-268

Changed: `risk`

Input:

```text
海啸过后，只有在当局告知安全时，才可以返回家园或进入遭受淹水破坏的建筑物。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A clear and critical instruction for returning to an area after a tsunami.

Maintainer decision: `pending`

### 27. ready-gov-are-you-ready-guide-simplified-v1/sentence-284

Changed: `risk`

Input:

```text
与邻居一起清除灌木丛和灌木树冠。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A simple instruction for yard maintenance as a preparedness measure using standard vocabulary.

Maintainer decision: `pending`

### 28. ready-gov-are-you-ready-guide-simplified-v1/sentence-335

Changed: `risk`

Input:

```text
确保家中的每个人都知道在不同类型的灾难中应该去哪里。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A straightforward instruction about ensuring family members know emergency locations.

Maintainer decision: `pending`

### 29. ready-gov-are-you-ready-guide-simplified-v1/sentence-412

Changed: `eligible, domain, risk`

Input:

```text
了解您的保险选择并记录财产了解您的保险需求是为自己和家人为灾难做好准备的重要步骤。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | high_stakes | candidate_gap | high | awkward_phrasing, possible_translation_error |

Codex reason: Codex excluded this input-only case because its source text is malformed, incomplete, duplicated, context-dependent, or unsafe as a standalone conversion target.

Gemini reason: The sentence is grammatically flawed with a likely concatenation error, but the topic is high-stakes.

Maintainer decision: `pending`

### 30. ready-gov-are-you-ready-guide-simplified-v1/sentence-485

Changed: `risk`

Input:

```text
VOAD是一个团体组织，这些团体将与灾难相关的工作列为优先事项，并志愿在灾后帮助社区。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This sentence defines the acronym VOAD and must protect it from conversion.

Maintainer decision: `pending`

### 31. ready-gov-are-you-ready-guide-simplified-v1/sentence-490

Changed: `eligible, domain, risk`

Input:

```text
F E M A 的青年备灾项目为年轻人提供了参与社区备灾的步骤。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | no | null | null | high | malformed, spacing_error |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Ineligible because the acronym 'FEMA' is incorrectly spaced, making it malformed.

Maintainer decision: `pending`

### 32. zhtw-project-formal-llm-evidence-guard-v1/formal-001

Changed: `risk`

Input:

```text
调查报告逐项列出证据来源及查证日期。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A formal sentence about an investigation report's contents.

Maintainer decision: `pending`

### 33. zhtw-project-formal-llm-evidence-guard-v1/formal-002

Changed: `risk`

Input:

```text
委员会要求会议记录保留不同意见的完整理由。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A formal sentence about committee meeting minutes and dissenting opinions.

Maintainer decision: `pending`

### 34. zhtw-project-formal-llm-evidence-guard-v1/formal-007

Changed: `risk`

Input:

```text
新闻稿引用的数字应与附件表格保持一致。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A formal instruction about data consistency between a press release and its attachments.

Maintainer decision: `pending`

### 35. zhtw-project-formal-llm-evidence-guard-v1/formal-009

Changed: `risk`

Input:

```text
地方政府公布预算调整前后的项目差异。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A formal statement about a local government publishing budget differences.

Maintainer decision: `pending`

### 36. zhtw-project-formal-llm-evidence-guard-v1/formal-013

Changed: `risk`

Input:

```text
机关复核后更正先前公告中的计算错误。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A formal sentence about an agency correcting a calculation error in a prior notice.

Maintainer decision: `pending`

### 37. zhtw-project-formal-llm-evidence-guard-v1/formal-021

Changed: `risk`

Input:

```text
年度报告比较计划目标与实际执行结果。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A standard sentence describing the content of an annual report.

Maintainer decision: `pending`

### 38. zhtw-project-formal-llm-evidence-guard-v1/formal-024

Changed: `domain, risk`

Input:

```text
研究结论不得超出样本资料能够支持的范围。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A formal principle of research methodology regarding conclusions and data.

Maintainer decision: `pending`

### 39. zhtw-project-formal-llm-evidence-guard-v1/formal-025

Changed: `risk`

Input:

```text
机关收到陈情后建立案件编号并记录处理进度。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A formal description of an agency's petition handling procedure.

Maintainer decision: `pending`

### 40. zhtw-project-formal-llm-evidence-guard-v1/formal-026

Changed: `domain, risk`

Input:

```text
稽核人员检查系统日志是否对应实际操作。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A formal sentence describing an auditor's check on system logs versus actual operations.

Maintainer decision: `pending`

### 41. zhtw-project-formal-llm-evidence-guard-v1/formal-032

Changed: `domain, risk`

Input:

```text
法院文件依卷宗编号排列证物清单。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A formal instruction for organizing court exhibits according to file numbers.

Maintainer decision: `pending`

### 42. zhtw-project-formal-llm-evidence-guard-v1/formal-035

Changed: `domain, risk`

Input:

```text
检验报告注明仪器型号与校正有效期限。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A requirement for an inspection report to include instrument and calibration details.

Maintainer decision: `pending`

### 43. zhtw-project-formal-llm-evidence-guard-v1/formal-036

Changed: `risk`

Input:

```text
记者要求机关提供数字计算的原始依据。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A sentence about a reporter's request for an agency's source data.

Maintainer decision: `pending`

### 44. zhtw-project-formal-llm-evidence-guard-v1/formal-037

Changed: `risk`

Input:

```text
评估报告区分短期效果与长期影响。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A requirement for an evaluation report to distinguish between short-term and long-term effects.

Maintainer decision: `pending`

### 45. zhtw-project-formal-llm-evidence-guard-v1/formal-044

Changed: `risk`

Input:

```text
复查人员发现两份附件使用不同统计期间。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A sentence about a reviewer finding a data discrepancy in statistical periods.

Maintainer decision: `pending`

### 46. zhtw-project-formal-llm-evidence-guard-v1/formal-046

Changed: `risk`

Input:

```text
主管机关将保存每次资料修订的历史版本。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A formal policy statement on a supervisory authority maintaining data revision history.

Maintainer decision: `pending`

### 47. zhtw-project-formal-llm-evidence-guard-v1/formal-049

Changed: `risk`

Input:

```text
承办人员以书面方式确认联络窗口变更。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A formal sentence about confirming a change of contact person in writing.

Maintainer decision: `pending`

### 48. zhtw-project-formal-llm-evidence-guard-v1/llm-001

Changed: `risk`

Input:

```text
模型回答时应附上能够支持结论的来源。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A clear instruction for a language model's response format.

Maintainer decision: `pending`

### 49. zhtw-project-formal-llm-evidence-guard-v1/llm-002

Changed: `domain, risk`

Input:

```text
检索系统必须保留文件标题与发布日期。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A standard requirement for a data retrieval or search system.

Maintainer decision: `pending`

### 50. zhtw-project-formal-llm-evidence-guard-v1/llm-010

Changed: `risk`

Input:

```text
回答需要区分直接证据与间接推测。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A requirement for the logical quality of a model's answer.

Maintainer decision: `pending`

### 51. zhtw-project-formal-llm-evidence-guard-v1/llm-016

Changed: `domain`

Input:

```text
系统发现来源互相冲突时会提示人工复核。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A system behavior for handling data conflicts, using terms like '人工复核'.

Maintainer decision: `pending`

### 52. zhtw-project-formal-llm-evidence-guard-v1/llm-021

Changed: `risk`

Input:

```text
系统不应自动改写引文中的专有名词。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | technical_term |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A direct instruction to prevent incorrect modification of proper nouns.

Maintainer decision: `pending`

### 53. zhtw-project-formal-llm-evidence-guard-v1/llm-023

Changed: `domain`

Input:

```text
检索器会排除没有权限读取的资料片段。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A requirement for a data system, using potentially regional terms like '检索器'.

Maintainer decision: `pending`

### 54. zhtw-project-formal-llm-evidence-guard-v1/llm-025

Changed: `domain`

Input:

```text
系统会检查引用连结是否指向原始来源。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A system requirement for link validation where '连结' might be '連結' in Taiwan.

Maintainer decision: `pending`

### 55. zhtw-project-formal-llm-evidence-guard-v1/llm-026

Changed: `risk`

Input:

```text
模型应保留代码范例中的参数名称与大小写。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | technical_term, code_related |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Explicitly requires preserving code elements like parameter names and case.

Maintainer decision: `pending`

### 56. zhtw-project-formal-llm-evidence-guard-v1/llm-048

Changed: `domain, risk`

Input:

```text
系统会阻止未确认的内容进入正式报告。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A business rule for ensuring the quality of a formal report.

Maintainer decision: `pending`
