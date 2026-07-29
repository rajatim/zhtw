<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 054 (2026-07-30)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `84e73beacddbe8d8fa030b4a7989f8222a643b223ac9bb04ccead41ab5e694fe`
Cases: 96
Exact Codex/Gemini classifications: 41
Maintainer review queue: 55

Field differences:

- Eligibility: 4
- Script: 8
- Domain: 29
- Risk: 40

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

The maintainer resolved all 55 advisory disagreements and batch-confirmed the 41 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. kubernetes-docs-zh-cn-v1/page-01-sentence-0005

Changed: `eligible, domain, risk`

Input:

```text
**名称在同一资源的所有 API 版本中必须是唯一的。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_markdown_fragment |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: The input starts with an unmatched Markdown marker, so the extracted sentence is malformed.

Gemini reason: A standard technical documentation sentence requiring basic character conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 02. kubernetes-docs-zh-cn-v1/page-01-sentence-0023

Changed: `risk`

Input:

```text
某些资源类型可能具有额外的命名约束。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A straightforward technical sentence requiring only standard character conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 03. kubernetes-docs-zh-cn-v1/page-03-sentence-0034

Changed: `risk`

Input:

```text
此阶段包括等待 Pod 被调度的时间和通过网络下载镜像的时间。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains key technical terms like '调度' and '镜像' which require specific phrase-level translation for Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 04. kubernetes-docs-zh-cn-v1/page-03-sentence-0039

Changed: `script, risk`

Input:

```text
也就是说，容器以非 0 状态退出或者被系统终止，且未被设置为自动重启。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A technical sentence where the digit '0' in '非 0 状态' must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 05. kubernetes-docs-zh-cn-v1/page-03-sentence-0156

Changed: `script, risk`

Input:

```text
如上文容器重启策略所述，该节点上的延迟仍将从 10 秒开始，并在每次重启后以指数方式增加 2 倍，但现在其上限将被限制为你所配置的最大值。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The sentence contains numbers that must be preserved as digits.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 06. kubernetes-docs-zh-cn-v1/page-03-sentence-0247

Changed: `risk`

Input:

```text
这可以帮助你避免将流量导向只能返回错误信息的 Pod。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The terms '流量' and '导向' may require specific idiomatic translations in a networking context for Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 07. kubernetes-docs-zh-cn-v1/page-03-sentence-0252

Changed: `risk`

Input:

```text
对于所包含的容器需要较长时间才能启动就绪的 Pod 而言，启动探针是有用的。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The technical concepts '启动就绪' and '启动探针' require correct terminological mapping for Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 08. kubernetes-docs-zh-cn-v1/page-03-sentence-0261

Changed: `eligible, domain, risk`

Input:

```text
当你请求删除某个 Pod 时，集群会记录并跟踪 Pod 的体面终止周期，而不是直接强制地杀死 Pod。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | unsafe_source_translation |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: The phrase 体面终止周期 is an unsafe mistranslation of the Kubernetes graceful termination concept.

Gemini reason: Technical Kubernetes terminology like 'graceful termination period' and 'kill' requires phrase-level conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 09. kubernetes-docs-zh-cn-v1/page-03-sentence-0265

Changed: `risk`

Input:

```text
这些请求的处理顺序无法被保证。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This is a straightforward technical statement where basic character conversion should be sufficient.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 10. kubernetes-docs-zh-cn-v1/page-03-sentence-0290

Changed: `risk`

Input:

```text
关闭动作很慢的 Pod 不应继续处理常规服务请求，而应开始终止并完成对打开的连接的处理。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This sentence involves technical concepts like service requests and connections, with phrasing that may differ in Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 11. kubernetes-docs-zh-cn-v1/page-04-sentence-0057

Changed: `risk`

Input:

```text
由于此 Service 没有选择算符，因此不会自动创建对应的 EndpointSlice 对象。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The term 'selector' ('选择算符') needs a standard Taiwan IT translation, while 'Service' and 'EndpointSlice' must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 12. kubernetes-docs-zh-cn-v1/page-04-sentence-0115

Changed: `risk`

Input:

```text
集群不会为之创建任何类型代理。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A straightforward technical sentence where character conversion is sufficient.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 13. kubernetes-docs-zh-cn-v1/page-04-sentence-0116

Changed: `risk`

Input:

```text
Service API 中的 `type` 字段被设计为层层递进的形式 - 每层都建立在前一层的基础上。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The descriptive phrase 'progressive layers' may require idiomatic rephrasing for technical documentation in Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 14. kubernetes-docs-zh-cn-v1/page-04-sentence-0157

Changed: `risk`

Input:

```text
来自外部负载均衡器的流量将被直接重定向到后端各个 Pod 上，云平台决定如何进行负载平衡。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This sentence contains multiple standard IT terms like 'load balancer' and 'cloud platform' that require correct idiomatic conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 15. kubernetes-docs-zh-cn-v1/page-04-sentence-0197

Changed: `risk`

Input:

```text
在混合环境中，有时有必要在同一（虚拟）网络地址段内路由来自 Service 的流量。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Technical terms like 'hybrid environment' and 'network address segment' may require specific Taiwan IT phrasing.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 16. kubernetes-docs-zh-cn-v1/page-04-sentence-0219

Changed: `risk`

Input:

```text
对定义了选择算符的无头 Service，Kubernetes 控制平面在 Kubernetes API 中创建 EndpointSlice 对象，并且修改 DNS 配置返回 A 或 AAAA 记录（IPv4 或 IPv6 地址），这些记录直接指向 Service 的后端 Pod 集合。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This dense sentence contains multiple technical phrases like 'selector' and 'control plane' that need accurate Taiwan-specific translation, alongside many identifiers to preserve.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 17. kubernetes-docs-zh-cn-v1/page-04-sentence-0233

Changed: `risk`

Input:

```text
你可以（并且几乎总是应该）使用插件（add-on）来为 Kubernetes 集群安装 DNS 服务。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The term 'plugin' ('插件') and its English equivalent 'add-on' require a standard idiomatic translation for the Taiwan context.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 18. ready-gov-are-you-ready-guide-simplified-v1/sentence-036

Changed: `domain`

Input:

```text
作为国民，我们越了解这些措施，我们就可以保护和挽救更多生命。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | awkward_source_translation |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A standard formal sentence about public preparedness.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 19. ready-gov-are-you-ready-guide-simplified-v1/sentence-115

Changed: `domain, risk`

Input:

```text
避免过度劳累和体力吃重的活动，特别是在一天中温度最高的时段。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A clear instruction, a good candidate for evaluating subtle vocabulary choices.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 20. ready-gov-are-you-ready-guide-simplified-v1/sentence-130

Changed: `script, risk`

Input:

```text
可以使用此储备金来支付租金、房屋和/或洪水保险，并在紧急情况下购买诸如食品、庇护所和饮水之类的救生物品。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A good candidate for financial and emergency-related vocabulary, including a mixed-script element.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 21. ready-gov-are-you-ready-guide-simplified-v1/sentence-140

Changed: `domain, risk`

Input:

```text
洪水的深度很难确定，并且可能包含隐藏的危险杂物碎片。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | awkward_source_translation |
| Gemini | yes | formal_news | candidate_gap | high | slightly_awkward_phrasing |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The sentence is a warning about floodwater hazards; the phrasing for 'debris' is a potential conversion point.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 22. ready-gov-are-you-ready-guide-simplified-v1/sentence-178

Changed: `domain`

Input:

```text
注册获取有关当前状况信息的紧急通知，或下载紧急手机应用程序，例如联邦应急管理署（FEMA）的应用程序。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Excellent candidate testing IT vocabulary ('app'), and requires protecting a Latin acronym (FEMA) from conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 23. ready-gov-are-you-ready-guide-simplified-v1/sentence-187

Changed: `domain`

Input:

```text
有时洪水会接踵而至，因为它们可能由同一事件引发。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A formal sentence using a common idiom to describe recurring floods.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 24. ready-gov-are-you-ready-guide-simplified-v1/sentence-191

Changed: `script, domain, risk`

Input:

```text
除非当地当局另有指示，否则在室内呆24小时。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A clear directive involving a number and a key vocabulary term for 'authorities'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 25. ready-gov-are-you-ready-guide-simplified-v1/sentence-192

Changed: `risk`

Input:

```text
落尘之后，如果您在室外，请脱去被污染的衣服，擦去或清洗没有保护措施的皮肤。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: High-stakes instruction where the specific term for 'fallout' is a key conversion point.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 26. ready-gov-are-you-ready-guide-simplified-v1/sentence-204

Changed: `risk`

Input:

```text
当出现新型疾病，则表明它在人类中从未见过，通常没有疫苗可以预防它的传播。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | awkward_source_translation |
| Gemini | yes | high_stakes | candidate_gap | high | formal_structure |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A formal, high-stakes sentence about novel diseases and vaccines.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 27. ready-gov-are-you-ready-guide-simplified-v1/sentence-246

Changed: `script, domain, risk`

Input:

```text
龙卷风 • 如果是龙卷风警戒，请靠近安全的房间、庇护所或坚固的建筑物。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Instruction for a tornado watch, testing weather alert terminology.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 28. ready-gov-are-you-ready-guide-simplified-v1/sentence-253

Changed: `domain, risk`

Input:

```text
在龙卷风警戒期间，请寻找庇护所。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A concise directive testing vocabulary for 'watch period' and 'shelter'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 29. ready-gov-are-you-ready-guide-simplified-v1/sentence-260

Changed: `domain`

Input:

```text
海啸 • 如果您住在靠近或到访沿海地区，请了解海啸风险。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Standard instructional text about tsunami risk suitable for baseline conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 30. ready-gov-are-you-ready-guide-simplified-v1/sentence-263

Changed: `domain`

Input:

```text
了解潜在的海啸征兆，如地震、海洋的巨大轰鸣，或海洋异常，例如突然水位上升，出现水墙，突然倒流露出海底的现象。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A descriptive list of tsunami signs suitable for baseline character conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 31. ready-gov-are-you-ready-guide-simplified-v1/sentence-286

Changed: `domain, risk`

Input:

```text
装修或建造新房屋时，请使用耐火的建筑材料。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The term '装修' (renovate) may require a specific vocabulary mapping for Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 32. ready-gov-are-you-ready-guide-simplified-v1/sentence-332

Changed: `domain`

Input:

```text
如果听到了龙卷风的警报响起，您知道要去哪里吗？
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A standard question about emergency preparedness suitable for baseline conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 33. ready-gov-are-you-ready-guide-simplified-v1/sentence-373

Changed: `eligible, script, domain, risk`

Input:

```text
酒精含量至少为 60％的清洁用品，肥皂和免洗洗手液。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: This is a noun-list fragment without enough standalone context for fair evaluation.

Gemini reason: The term '免洗洗手液' (hand sanitizer) may require a specific vocabulary mapping for Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 34. ready-gov-are-you-ready-guide-simplified-v1/sentence-391

Changed: `domain`

Input:

```text
收集这些文件，并列出家里财产和贵重物品清单。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A standard instruction for preparing an inventory of valuables.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 35. ready-gov-are-you-ready-guide-simplified-v1/sentence-423

Changed: `eligible, domain, risk`

Input:

```text
保险只适用于您的保单承保造成损失的危险。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | unsafe_source_translation |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: The insurance sentence has broken source semantics and is unsafe as a conversion benchmark.

Gemini reason: The use of '危险' for an insurance peril might require specific terminology mapping for a high-stakes domain.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 36. ready-gov-are-you-ready-guide-simplified-v1/sentence-441

Changed: `script, risk`

Input:

```text
从购买洪水保障到保险开始生效日之间，通常需要 30 天的等待期，因此请勿延迟购买保险。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Insurance-specific terminology like '洪水保障' may require mapping.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 37. ready-gov-are-you-ready-guide-simplified-v1/sentence-442

Changed: `risk`

Input:

```text
帮助您购车、房屋或人寿保险的保险经纪人可以帮助购买洪水保险。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The professional title '保险经纪人' could require a locale-specific vocabulary mapping.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 38. ready-gov-are-you-ready-guide-simplified-v1/sentence-478

Changed: `domain, risk`

Input:

```text
CERT项目教您基本的灾难响应技能，例如消防安全和紧急医疗作业。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The proper noun 'CERT' must be preserved, and terms like '项目' and '作业' might need mapping.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 39. ready-gov-are-you-ready-guide-simplified-v1/sentence-487

Changed: `domain`

Input:

```text
民航巡逻队发现失踪人员；在灾难发生时给予安慰；并促进科学、技术、工程和数学（S T E M）等学科方面的教育。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | awkward_source_translation |
| Gemini | yes | formal_news | over_conversion_guard | high | odd_spacing |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The spaced acronym 'S T E M' must be preserved, and '民航巡逻队' (Civil Air Patrol) is a proper noun translation.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 40. ready-gov-are-you-ready-guide-simplified-v1/sentence-501

Changed: `domain, risk`

Input:

```text
在杂物碎片中工作时，请穿戴坚固的工作靴和手套，并经常用肥皂和清水彻底洗手。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The term '杂物碎片' for debris may require a specific vocabulary mapping for Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 41. ready-gov-are-you-ready-guide-simplified-v1/sentence-552

Changed: `domain`

Input:

```text
确保您和您的家人在事件之后获得完全康复所需的支持。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A standard sentence about post-event recovery, likely suitable for baseline conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 42. ready-gov-are-you-ready-guide-simplified-v1/sentence-554

Changed: `domain, risk`

Input:

```text
有些人可能获得灾后经济援助计划。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The term '援助计划' (assistance program) is likely to have a different common phrasing in Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 43. ready-gov-are-you-ready-guide-simplified-v1/sentence-574

Changed: `domain`

Input:

```text
如果可以的话，请帮助邻居来恢复社区。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A simple, common phrase about helping neighbors that serves as a good baseline case.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 44. ready-gov-are-you-ready-guide-simplified-v1/sentence-576

Changed: `domain, risk`

Input:

```text
在灾后，儿童、老年人、母语非英语人士、残障人士以及其他有障碍和功能需求的人们会受到严重影响，可能需要特殊关照。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | awkward_source_translation |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Multiple terms for vulnerable groups, like '残障人士', are likely to require specific vocabulary mapping.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 45. zhtw-project-ui-social-baseline-guard-v1/social-017

Changed: `domain`

Input:

```text
公车到站前，应用程序会发送提醒。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Involves UI terminology like '应用程序' (application) which requires correct regional mapping.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 46. zhtw-project-ui-social-baseline-guard-v1/social-029

Changed: `domain`

Input:

```text
请先把药袋上的用法看清楚。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A high-stakes medical instruction, although the vocabulary is simple.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 47. zhtw-project-ui-social-baseline-guard-v1/social-031

Changed: `domain`

Input:

```text
跨行汇款手续费由转账人负担。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Financial transaction terms require careful mapping to Taiwanese usage.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 48. zhtw-project-ui-social-baseline-guard-v1/social-032

Changed: `risk`

Input:

```text
租车费用不包含高速公路通行费。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The term for highway tolls might differ in Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 49. zhtw-project-ui-social-baseline-guard-v1/social-036

Changed: `risk`

Input:

```text
雨伞放在入口旁边的置物柜里。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | medium | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The term for 'locker' can vary, making this a good test for regional vocabulary.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 50. zhtw-project-ui-social-baseline-guard-v1/social-037

Changed: `risk`

Input:

```text
我们约在捷运站第二个出口见面。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | taiwan_specific_term_in_sc |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Uses the Taiwan-specific term '捷运' (MRT) in simplified characters, a good test case.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 51. zhtw-project-ui-social-baseline-guard-v1/social-038

Changed: `domain`

Input:

```text
这段视频只会保留到月底。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains '视频' (video), which should ideally be converted to the more common Taiwanese term '影片'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 52. zhtw-project-ui-social-baseline-guard-v1/social-046

Changed: `script, risk`

Input:

```text
房间号码 1208 不需要加上楼层。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Includes a number that must be preserved, testing over-conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 53. zhtw-project-ui-social-baseline-guard-v1/ui-009

Changed: `risk`

Input:

```text
密码输入错误三次后，账号会暂时锁定。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A standard account security message with common terms suitable for a baseline test.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 54. zhtw-project-ui-social-baseline-guard-v1/ui-018

Changed: `domain`

Input:

```text
消息消费者停止后，待处理数量不会继续减少。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A technical IT phrase ('message consumer') that tests for correct vocabulary in a software context.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 55. zhtw-project-ui-social-baseline-guard-v1/ui-034

Changed: `risk`

Input:

```text
表格栏位过多时可以水平滚动。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | source_uses_target_term |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Source text uses '栏位', a Taiwan-preferred term, and also tests '滚动' ('scroll') vs. '捲動'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`
