<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 051 (2026-07-29)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `cb1057be72b2ded934108d76d8c4518f132845e41c3f99a3d991863e2019d2b4`
Cases: 96
Exact Codex/Gemini classifications: 29
Maintainer review queue: 67

Field differences:

- Eligibility: 1
- Script: 17
- Domain: 12
- Risk: 53

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

The maintainer resolved all 67 advisory disagreements and batch-confirmed the 29 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. kubernetes-docs-zh-cn-v1/page-01-sentence-0011

Changed: `script`

Input:

```text
即使名称是自动生成的，它仍可能与现有名称冲突，从而导致 HTTP 409 响应。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clean, complete sentence from technical documentation. Contains a technical token (HTTP 409) that needs to be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 02. kubernetes-docs-zh-cn-v1/page-02-sentence-0037

Changed: `risk`

Input:

```text
声明性对象配置更好地支持对目录进行操作并自动检测每个文件的操作类型（创建，修补，删除）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete technical sentence. Key terms like 'declarative object configuration' and 'patch' are good candidates for checking Taiwan-specific terminology.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 03. kubernetes-docs-zh-cn-v1/page-03-sentence-0133

Changed: `risk`

Input:

```text
当容器的退出符合包含此动作的某个规则时，整个 Pod 被终止并就地重启。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete technical sentence. Contains terms like 'in-place restart' that could have specific TW translations, and a token 'Pod' to preserve.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 04. kubernetes-docs-zh-cn-v1/page-03-sentence-0178

Changed: `risk`

Input:

```text
在 Pod 被调度到某节点后，它需要被 kubelet 接受并且挂载所需的存储卷。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Good technical sentence for testing terminology gaps (schedule, node, mount, storage volume). Also contains English tokens (Pod, kubelet) to preserve.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 05. kubernetes-docs-zh-cn-v1/page-03-sentence-0305

Changed: `risk`

Input:

```text
将宽限期限强制设置为 `0` 意味着立即从 API 服务器删除 Pod。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Good test case for a specific technical concept ('grace period') and preservation of English tokens (API, Pod).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 06. kubernetes-docs-zh-cn-v1/page-03-sentence-0311

Changed: `risk`

Input:

```text
马上删除时不等待确认正在运行的资源已被终止。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A standard technical sentence with common terms (resource, terminate), good for baseline conversion quality check.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 07. kubernetes-docs-zh-cn-v1/page-03-sentence-0334

Changed: `eligible, script, domain, risk`

Input:

```text
（也可能通过其他方式重启 kubelet，例如为修复某个节点缺陷而重启；在这些情况下， Kubernetes 会选择更安全的处理方式，例如先停止再启动 kubelet。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_terms, complete_sentence, documentation |

Codex reason: The PDF or Markdown extraction joined layout fragments, so this is not a clean standalone input.

Gemini reason: Complete sentence from Kubernetes documentation. Contains technical terms like 'kubelet' and 'Kubernetes' that need protection from over-conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 08. kubernetes-docs-zh-cn-v1/page-03-sentence-0340

Changed: `script`

Input:

```text
在 Kubernetes 中，你可以选择启用一种传统的行为：在 kubelet 重启后，总是将容器的 `ready` 状态修改为 false。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_terms, code_like, complete_sentence, documentation |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Technical sentence with code-like terms ('ready', 'false') and proper nouns ('Kubernetes', 'kubelet') that should not be converted.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 09. kubernetes-docs-zh-cn-v1/page-03-sentence-0342

Changed: `script, risk`

Input:

```text
虽然此特性门控允许暂时回退到这种传统行为，但 Kubernetes 项目建议如果你遇到相关问题，应提交 Bug 报告。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | technical_terms, complete_sentence, documentation |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Good test for terminology conversion (e.g., '特性门控') and preserving the English word 'Bug'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 10. kubernetes-docs-zh-cn-v1/page-04-sentence-0009

Changed: `script`

Input:

```text
对于集群中给定的某个 Deployment，这一刻运行的 Pod 集合可能不同于下一刻运行该应用的 Pod 集合。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_terms, complete_sentence, documentation |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Tests preservation of technical English terms ('Deployment', 'Pod') alongside standard conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 11. kubernetes-docs-zh-cn-v1/page-04-sentence-0011

Changed: `script`

Input:

```text
Service API 是 Kubernetes 的组成部分，它是一种抽象，帮助你将 Pod 集合在网络上公开出去。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_terms, complete_sentence, documentation |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains multiple technical terms ('Service API', 'Kubernetes', 'Pod') that should remain unchanged.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 12. kubernetes-docs-zh-cn-v1/page-04-sentence-0056

Changed: `script, risk`

Input:

```text
在所有这些场景中，你都可以定义不指定用来匹配 Pod 的选择算符的 Service。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | technical_terms, complete_sentence, documentation |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Excellent case for terminology. '选择算符' (selector) is a key term needing correct localization, not just character conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 13. kubernetes-docs-zh-cn-v1/page-04-sentence-0059

Changed: `script, risk`

Input:

```text
一个名字空间中的各个 EndpointSlice 都必须具有一个唯一的名称。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | technical_terms, complete_sentence, documentation |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Tests both terminology ('名字空间' -> '命名空間') and preservation of a technical term ('EndpointSlice').

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 14. kubernetes-docs-zh-cn-v1/page-04-sentence-0077

Changed: `script`

Input:

```text
如果 Service 的端点太多以至于达到阈值，Kubernetes 会添加另一个空的 EndpointSlice 并在其中存储新的端点信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_terms, complete_sentence, documentation |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Good mix of standard conversion, terminology ('阈值'), and protected terms ('Service', 'EndpointSlice').

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 15. kubernetes-docs-zh-cn-v1/page-04-sentence-0123

Changed: `script`

Input:

```text
在创建 `Service` 的请求中，你可以通过设置 `spec.clusterIP` 字段来指定自己的集群 IP 地址。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_terms, code_like, complete_sentence, documentation |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains code-like strings ('Service', 'spec.clusterIP') that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 16. kubernetes-docs-zh-cn-v1/page-04-sentence-0127

Changed: `script`

Input:

```text
请阅读避免冲突节，以了解 Kubernetes 如何协助降低两个不同的 Service 试图使用相同 IP 地址的风险和影响。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_terms, complete_sentence, documentation |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Standard technical sentence with proper nouns ('Kubernetes', 'Service') to protect.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 17. kubernetes-docs-zh-cn-v1/page-04-sentence-0155

Changed: `script`

Input:

```text
在使用支持外部负载均衡器的云平台时，如果将 `type` 设置为 `"LoadBalancer"`，则平台会为 Service 提供负载均衡器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_terms, code_like, complete_sentence, documentation |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Excellent test case with code values ('type', '"LoadBalancer"') and important technical terms ('负载均衡器') needing correct localization.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 18. kubernetes-docs-zh-cn-v1/page-04-sentence-0234

Changed: `script, risk`

Input:

```text
能够感知集群的 DNS 服务器（例如 CoreDNS）会监视 Kubernetes API 中的新 Service，并为每个 Service 创建一组 DNS 记录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | technical_terms, complete_sentence, documentation |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Prime example for candidate gap with '服务器' (-> '伺服器'). Also contains several proper nouns to protect.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 19. kubernetes-docs-zh-cn-v1/page-04-sentence-0248

Changed: `risk`

Input:

```text
虽然流量策略侧重于严格的语义保证，但流量分发允许你表达一定的偏好（例如路由到拓扑上更接近的端点）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | technical_terms, complete_sentence, documentation |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Sentence rich with networking terms ('流量策略', '拓扑', '路由') that require correct idiomatic translation beyond simple character mapping.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 20. kubernetes-docs-zh-cn-v1/page-04-sentence-0254

Changed: `script, risk`

Input:

```text
如果你想确保来自特定客户端的连接每次都传递到同一个 Pod，你可以配置基于客户端 IP 地址的会话亲和性。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | technical_terms, complete_sentence, documentation |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Key terminology test for '客户端' (client) and '会话亲和性' (session affinity).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 21. kubernetes-docs-zh-cn-v1/page-04-sentence-0257

Changed: `script, risk`

Input:

```text
当网络流量进入集群时，如果外部 IP（作为目的 IP 地址）和端口都与该 Service 匹配， Kubernetes 所配置的规则和路由会确保流量被路由到该 Service 的端点之一。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | technical_terms, complete_sentence, documentation |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Good test for common networking terms ('集群', '端口') and protecting proper nouns ('Kubernetes', 'Service').

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 22. kubernetes-docs-zh-cn-v1/page-04-sentence-0258

Changed: `script`

Input:

```text
定义 Service 时，你可以为任何 Service 类型指定 `externalIPs`。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_terms, code_like, complete_sentence, documentation |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Simple sentence testing the preservation of a code-like property name 'externalIPs'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 23. ready-gov-are-you-ready-guide-simplified-v1/sentence-001

Changed: `risk`

Input:

```text
不是假设，而是何时：美国各州和领地都有遭受灾难的风险。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clean, complete sentence. Good baseline for high-stakes official guidance.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 24. ready-gov-are-you-ready-guide-simplified-v1/sentence-071

Changed: `risk`

Input:

```text
每次到访建筑物时，请找出在附近的两个出口。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clear, standalone emergency instruction. Good baseline case.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 25. ready-gov-are-you-ready-guide-simplified-v1/sentence-116

Changed: `risk`

Input:

```text
在天热时段，切勿将儿童、成人或动物单独留在车内。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clear and universal safety warning. Serves as a good baseline test for high-stakes content.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 26. ready-gov-are-you-ready-guide-simplified-v1/sentence-129

Changed: `risk`

Input:

```text
每月或每次发薪水时留下一定数量的金钱，存入紧急储备金。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Financial advice sentence, good baseline for the high-stakes category.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 27. ready-gov-are-you-ready-guide-simplified-v1/sentence-141

Changed: `risk`

Input:

```text
找出所在地区可能发生的洪水风险类型。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clear disaster-risk sentence. Good baseline test.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 28. ready-gov-are-you-ready-guide-simplified-v1/sentence-150

Changed: `risk`

Input:

```text
如果被困在建筑物中，请前往建筑物的最高层。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Straightforward emergency instruction, good baseline test.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 29. ready-gov-are-you-ready-guide-simplified-v1/sentence-189

Changed: `risk`

Input:

```text
最佳位置是地下，或在由砖石或混凝土的大型建筑物的中间。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Sentence about shelter construction. Good baseline test for architectural/material terms.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 30. ready-gov-are-you-ready-guide-simplified-v1/sentence-217

Changed: `risk`

Input:

```text
带有备用电池的电子探测器也可接受。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A sentence about electronic safety equipment. Good baseline test.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 31. ready-gov-are-you-ready-guide-simplified-v1/sentence-273

Changed: `risk`

Input:

```text
风和重力将携带碎石和火山灰。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A simple, scientific sentence about volcanic effects. Good baseline test.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 32. ready-gov-are-you-ready-guide-simplified-v1/sentence-307

Changed: `risk`

Input:

```text
老年人和幼儿在极寒的天气更为危险。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clear safety-related sentence, suitable as a baseline test.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 33. ready-gov-are-you-ready-guide-simplified-v1/sentence-314

Changed: `risk`

Input:

```text
确保该人至少有两种联系方式。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Good baseline test for common character conversion (e.g., '联系' to '聯繫').

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 34. ready-gov-are-you-ready-guide-simplified-v1/sentence-319

Changed: `risk`

Input:

```text
计划一旦制定了，家人就必须演练该计划，就像进行消防演练一样。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clear, complete sentence for a baseline conversion test, using common words like '计划' and '演练'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 35. ready-gov-are-you-ready-guide-simplified-v1/sentence-342

Changed: `risk`

Input:

```text
请遵循建议的撤离路线，不要走捷径，因为它们可能受阻。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Good high-stakes baseline test for common verbs and nouns like '遵循' and '建议'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 36. ready-gov-are-you-ready-guide-simplified-v1/sentence-358

Changed: `risk`

Input:

```text
应该将应急用品存储在不同地方，例如家里、办公室和车上。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Tests common character conversions like '存储' (儲存) and '办公室' (辦公室).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 37. ready-gov-are-you-ready-guide-simplified-v1/sentence-408

Changed: `script, risk`

Input:

```text
重复检查您的移动设备是否可以收到无线紧急警报（WEA）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | acronym |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Good test case for over-conversion risk, as the English acronym 'WEA' must be preserved. Also includes a terminology gap ('移动设备').

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 38. ready-gov-are-you-ready-guide-simplified-v1/sentence-414

Changed: `risk`

Input:

```text
现在立即采取以下措施，找到并保护适当的保单，以保护家庭的财务健康。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: High-stakes sentence about financial/insurance matters. Good baseline case for converting '保单' and '财务'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 39. ready-gov-are-you-ready-guide-simplified-v1/sentence-510

Changed: `risk`

Input:

```text
如果房屋已损坏，请由合格的检查员检查以确保可以安全进入和居住。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clear, high-stakes instruction, good for baseline conversion ('损坏', '检查员').

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 40. ready-gov-are-you-ready-guide-simplified-v1/sentence-527

Changed: `risk`

Input:

```text
请记住，灾难和威胁生命的情况将增加野生动物的不可预测性。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: High-stakes safety warning, suitable as a baseline test case for words like '灾难' and '威胁'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 41. zhtw-project-formal-llm-evidence-guard-v1/formal-011

Changed: `domain`

Input:

```text
公报注明法规条文开始生效的具体日期。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clean, formal sentence about legal regulations coming into effect. Tests formal vocabulary like '公报' and '法规'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 42. zhtw-project-formal-llm-evidence-guard-v1/formal-017

Changed: `domain`

Input:

```text
委员会尚未核定草案中涉及费用的条款。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clean, formal sentence regarding committee approval of a draft. Tests procedural terms like '核定'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 43. zhtw-project-formal-llm-evidence-guard-v1/formal-018

Changed: `domain`

Input:

```text
承办单位确认附件版本与签核纪录相符。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clean, formal sentence about administrative record verification. Tests office/procedural terms like '承办单位' and '签核纪录'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 44. zhtw-project-formal-llm-evidence-guard-v1/formal-019

Changed: `risk`

Input:

```text
新闻资料区分已确认事实与初步研判。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clean, formal sentence about distinguishing facts in press materials. Tests terms like '研判'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 45. zhtw-project-formal-llm-evidence-guard-v1/formal-022

Changed: `domain`

Input:

```text
主管机关保留现场检查的照片与时间戳记。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clean, formal sentence regarding official inspection evidence. '时间戳记' has common variants in Taiwan ('時間戳', '時戳').

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 46. zhtw-project-formal-llm-evidence-guard-v1/formal-030

Changed: `risk`

Input:

```text
调查结果必须经过资料检核才能对外发布。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clean, formal sentence about the process of releasing investigation results. Tests standard conversion of '资料检核'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 47. zhtw-project-formal-llm-evidence-guard-v1/formal-031

Changed: `risk`

Input:

```text
主管单位要求说明指标定义变更造成的影响。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clean, formal sentence about explaining changes in indicator definitions. Tests standard conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 48. zhtw-project-formal-llm-evidence-guard-v1/formal-033

Changed: `domain, risk`

Input:

```text
会议主席确认表决人数符合程序规定。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clean, formal sentence about meeting procedures. Tests correct conversion of '程序规定'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 49. zhtw-project-formal-llm-evidence-guard-v1/formal-039

Changed: `risk`

Input:

```text
机关将错误讯息的更正说明置于原文旁边。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clean, formal sentence about placing a correction notice. Provides a standard test case for '讯息' to '訊息'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 50. zhtw-project-formal-llm-evidence-guard-v1/formal-041

Changed: `domain, risk`

Input:

```text
预算书注明各项估算采用的价格基准。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clean, formal sentence from a budget document. Tests character mapping like '基准' to '基準'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 51. zhtw-project-formal-llm-evidence-guard-v1/formal-042

Changed: `risk`

Input:

```text
委员会请专家确认技术用语是否准确。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clean, formal sentence about verifying technical terms. Tests '用语' to '用語'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 52. zhtw-project-formal-llm-evidence-guard-v1/formal-043

Changed: `domain, risk`

Input:

```text
政策说明列出不适用这项措施的对象。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clean, formal sentence from a policy document. Tests standard terms like '措施' and '对象'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 53. zhtw-project-formal-llm-evidence-guard-v1/formal-045

Changed: `risk`

Input:

```text
新闻稿不得省略调查结果的重要限制条件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clean, formal sentence stating a rule for press releases. Standard baseline conversion case.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 54. zhtw-project-formal-llm-evidence-guard-v1/formal-047

Changed: `domain, risk`

Input:

```text
审议结果须待主席签署后才正式生效。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clean, formal sentence about the process of formalizing a decision. Tests formal terms like '审议' and '签署'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 55. zhtw-project-formal-llm-evidence-guard-v1/formal-048

Changed: `risk`

Input:

```text
报告附录说明无法完成验证的资料项目。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clean, complete, formal sentence suitable for baseline conversion testing (e.g., '验证', '资料').

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 56. zhtw-project-formal-llm-evidence-guard-v1/llm-003

Changed: `risk`

Input:

```text
助理无法验证引用时应说明资料不足。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A clear instruction for an AI assistant, good for baseline conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 57. zhtw-project-formal-llm-evidence-guard-v1/llm-004

Changed: `risk`

Input:

```text
摘要不能删除会改变结论的限制条件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A rule for text summarization, suitable for baseline conversion testing.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 58. zhtw-project-formal-llm-evidence-guard-v1/llm-011

Changed: `risk`

Input:

```text
系统会显示每项结论对应的证据片段。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Describes system behavior, good for baseline IT term conversion (e.g., '系统', '显示').

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 59. zhtw-project-formal-llm-evidence-guard-v1/llm-019

Changed: `risk`

Input:

```text
分类器只依据输入内容判断资料所属领域。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Standard sentence with multiple technical terms, good for baseline character conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 60. zhtw-project-formal-llm-evidence-guard-v1/llm-020

Changed: `risk`

Input:

```text
低信心的事实陈述会进入待确认清单。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A rule for handling low-confidence outputs in an AI system. Good baseline case.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 61. zhtw-project-formal-llm-evidence-guard-v1/llm-022

Changed: `risk`

Input:

```text
回答采用推算数字时必须清楚标示假设。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: An instruction for AI response generation. Good baseline case.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 62. zhtw-project-formal-llm-evidence-guard-v1/llm-029

Changed: `domain, risk`

Input:

```text
助理引用法规时需要确认条文仍然有效。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: High-stakes instruction for an AI assistant dealing with legal regulations. Good for baseline conversion in a critical domain.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 63. zhtw-project-formal-llm-evidence-guard-v1/llm-033

Changed: `domain, risk`

Input:

```text
助理只可使用目前对话中提供的账号资料。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: High-stakes instruction regarding user data privacy. Good baseline conversion test for common IT terms like '账号'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 64. zhtw-project-formal-llm-evidence-guard-v1/llm-035

Changed: `risk`

Input:

```text
模型应指出哪些步骤尚未实际执行。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clear instruction about model execution state. Good baseline conversion test.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 65. zhtw-project-formal-llm-evidence-guard-v1/llm-043

Changed: `risk`

Input:

```text
系统会记录使用者接受或拒绝建议的决定。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Describes system logging of user actions. Good baseline test for common IT/UI terms.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 66. zhtw-project-formal-llm-evidence-guard-v1/llm-049

Changed: `risk`

Input:

```text
模型应把使用者提供的事实与外部资料分开。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Rule for data handling in a model. Good baseline conversion test.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 67. zhtw-project-formal-llm-evidence-guard-v1/llm-050

Changed: `domain`

Input:

```text
评测结果必须能够追溯到固定版本的输入。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this as an input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A requirement for reproducible evaluations. Good test for IT terminology ('评测', '版本', '输入').

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`
