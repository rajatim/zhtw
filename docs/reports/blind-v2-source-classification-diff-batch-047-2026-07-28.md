<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 047 (2026-07-28)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `eb6b92f9a541be69ab7ec6c22cb922aadf224b7be29fe3d07acfbbc436f97853`
Cases: 96
Exact Codex/Gemini classifications: 29
Maintainer review queue: 67

Field differences:

- Eligibility: 4
- Script: 47
- Domain: 32
- Risk: 17

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

The maintainer resolved all 67 advisory disagreements and batch-confirmed the 29 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. kubernetes-docs-zh-cn-v1/page-03-sentence-0187

Changed: `risk`

Input:

```text
Kubernetes 支持在 Pod 创建后更改分配给 Pod 的 CPU 和内存资源。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Key risk is the mainland term '内存' (memory), which should be '記憶體' in Taiwan. Also contains identifiers 'Kubernetes', 'Pod', 'CPU' which need an over_conversion_guard.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 02. kubernetes-docs-zh-cn-v1/page-03-sentence-0196

Changed: `script`

Input:

```text
就地调整大小的关键考量：仅 CPU 和内存资源可以原地调整大小。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Key risk is the mainland term '内存' (memory), which should be '記憶體' in Taiwan. '资源' (resources) is also a term that can differ in usage between mainland and Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 03. kubernetes-docs-zh-cn-v1/page-03-sentence-0200

Changed: `script`

Input:

```text
更改 Pod 资源更云原生的方法是通过管理它的工作负载资源（如 Deployment 或 StatefulSet）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: The terms '云原生' (cloud-native) and '工作负载' (workload) are common Mainland IT terms. Identifiers 'Deployment' and 'StatefulSet' must be preserved, which also adds an over_conversion_guard risk.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 04. kubernetes-docs-zh-cn-v1/page-03-sentence-0238

Changed: `script`

Input:

```text
如果容器没有提供启动探测，则默认状态为 `Success`。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: The keyword 'Success' is an API status and must be preserved. The term '启动探测' (startup probe) is a technical term that could be a candidate_gap.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 05. kubernetes-docs-zh-cn-v1/page-03-sentence-0295

Changed: `script`

Input:

```text
你可以在教程探索 Pod 及其端点的终止行为中找到有关如何实现连接排空的更多详细信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Technical terms like '端点' (endpoint) and '连接排空' (connection draining) may require localization. The identifier 'Pod' must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 06. kubernetes-docs-zh-cn-v1/page-03-sentence-0304

Changed: `script`

Input:

```text
`kubectl delete` 命令支持 `--grace-period=` 选项，允许你重载默认值，设定自己希望的期限值。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: The CLI command 'kubectl delete' and the flag '--grace-period=' must be preserved and not converted. The term '重载' (overload/override) could also be a candidate_gap.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 07. kubernetes-docs-zh-cn-v1/page-03-sentence-0314

Changed: `script`

Input:

```text
如果你的 Pod 包含一个或多个 Sidecar 容器（重启策略为 `Always` 的 Init 容器），kubelet 将延迟向这些 Sidecar 容器发送 TERM 信号，直到最后一个主容器已完全终止。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Contains multiple English identifiers ('Pod', 'Sidecar', 'Always', 'Init', 'kubelet', 'TERM') that must be preserved. Terms like '重启策略' (restart policy) and '主容器' (main container) are also candidate_gaps.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 08. kubernetes-docs-zh-cn-v1/page-03-sentence-0315

Changed: `script, risk`

Input:

```text
Sidecar 容器将按照它们在 Pod 规约中被定义的相反顺序被终止。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: The term '规约' for 'specification' is a common Mainlandism that needs localization. The identifiers 'Sidecar' and 'Pod' must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 09. kubernetes-docs-zh-cn-v1/page-03-sentence-0318

Changed: `script, risk`

Input:

```text
如果在终止过程完成之前宽限期已到，Pod 可能会进入强制终止阶段。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: The terms '宽限期' (grace period) and '强制终止' (force termination) are technical concepts that may require localization. The identifier 'Pod' must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 10. kubernetes-docs-zh-cn-v1/page-03-sentence-0331

Changed: `script`

Input:

```text
如果需要停止节点上的 Pod，可以使用 `kubectl drain`。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: The input contains a command `kubectl drain` which must be preserved without character conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 11. kubernetes-docs-zh-cn-v1/page-03-sentence-0338

Changed: `script`

Input:

```text
但是，即使开始发生 Pod 驱逐，Kubernetes 也不会将这些 Pod 中的单个容器标记为 `ready: false`。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: The input contains proper nouns (Pod, Kubernetes) and a code snippet (`ready: false`) that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 12. kubernetes-docs-zh-cn-v1/page-04-sentence-0006

Changed: `eligible, script, domain, risk`

Input:

```text
Kubernetes 的创建和销毁是为了匹配集群的预期状态。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 句子把建立與銷毀的主體寫成 Kubernetes，疑似 Markdown 連結文字遺失，語意不完整。

Gemini reason: The term '销毁' (destroy) is Mainland terminology that may require localization to a more appropriate term like '移除' (remove) or '刪除' (delete) for a Taiwan context.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 13. kubernetes-docs-zh-cn-v1/page-04-sentence-0008

Changed: `script, risk`

Input:

```text
每个 Pod 会获得属于自己的 IP 地址（Kubernetes 期待网络插件来保证这一点）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: The term '网络插件' (network plugin) is Mainland terminology. Taiwan context would likely use '網路外掛' (network plugin) or a similar variant.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 14. kubernetes-docs-zh-cn-v1/page-04-sentence-0019

Changed: `script, risk`

Input:

```text
如果你的工作负载使用 HTTP 通信，你可能会选择使用 Ingress 来控制 Web 流量如何到达该工作负载。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: The term '工作负载' (workload) is common in Mainland technical documents and may require localization review. '通信' (communication) is also a candidate for localization to '通訊'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 15. kubernetes-docs-zh-cn-v1/page-04-sentence-0084

Changed: `script`

Input:

```text
因此，推荐所有客户端使用 EndpointSlice API 来替换 Endpoints。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Contains API names 'EndpointSlice' and 'Endpoints' that must be preserved. The term '客户端' (client) is also a potential localization candidate ('用戶端').

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 16. kubernetes-docs-zh-cn-v1/page-04-sentence-0106

Changed: `script`

Input:

```text
`ClusterIP` : 通过集群的内部 IP 公开 Service，选择该值时 Service 只能够在集群内部访问。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Contains technical identifiers 'ClusterIP' and 'Service' that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 17. kubernetes-docs-zh-cn-v1/page-04-sentence-0139

Changed: `script`

Input:

```text
为 NodePort Service 分配端口的策略既适用于自动分配的情况，也适用于手动分配的场景。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Contains technical identifiers 'NodePort' and 'Service' that must be preserved. The term '场景' (scenario) is also a potential candidate for localization.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 18. kubernetes-docs-zh-cn-v1/page-04-sentence-0152

Changed: `eligible, script, domain, risk`

Input:

```text
这意味着 kube-proxy 将认为所有可用网络接口都可用于 NodePort Service （这也与早期的 Kubernetes 版本兼容。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 句尾括號未閉合，來源句在抽取前即不完整。

Gemini reason: Contains multiple English proper nouns (kube-proxy, NodePort, Service) that must be preserved. Also contains Mainland technical term '网络接口' (network interface).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 19. kubernetes-docs-zh-cn-v1/page-04-sentence-0161

Changed: `script`

Input:

```text
某些云平台允许你设置 `loadBalancerIP`。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Contains a code identifier 'loadBalancerIP' that must be preserved. '云平台' (cloud platform) is a potential candidate gap.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 20. kubernetes-docs-zh-cn-v1/page-04-sentence-0164

Changed: `script`

Input:

```text
如果设置了 `loadBalancerIP`，但云平台并不支持这一特性，所设置的 `loadBalancerIP` 值将会被忽略。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Contains a code identifier 'loadBalancerIP' that must be preserved. '云平台' (cloud platform) and '特性' (feature) are potential candidate gaps.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 21. kubernetes-docs-zh-cn-v1/page-04-sentence-0169

Changed: `script, risk`

Input:

```text
如果你正在集成某云平台，该平台通过（特定于平台的）注解为 Service 指定负载均衡器 IP 地址，你应该切换到这种做法。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Contains multiple Mainland technical terms requiring localization ('集成', '云平台', '注解', '负载均衡器'). Also contains an English proper noun 'Service' to preserve.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 22. kubernetes-docs-zh-cn-v1/page-04-sentence-0196

Changed: `script`

Input:

```text
Service 实现可以使用此信息来调整流量路由。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Contains an English proper noun 'Service' that must be preserved. '实现' (implementation) and '信息' (information) are candidate gaps.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 23. kubernetes-docs-zh-cn-v1/page-04-sentence-0223

Changed: `script`

Input:

```text
当你定义无选择算符的无头 Service 时，`port` 必须与 `targetPort` 匹配。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Contains multiple English terms/identifiers ('Service', 'port', 'targetPort') that must be preserved. '选择算符' (selector) and '无头' (headless) are candidate gaps.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 24. kubernetes-docs-zh-cn-v1/page-04-sentence-0225

Changed: `script`

Input:

```text
当 Pod 运行在某 Node 上时，kubelet 会在其中为每个活跃的 Service 添加一组环境变量。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Contains multiple English proper nouns (Pod, Node, kubelet, Service) that must be preserved. '活跃' (active) is a candidate gap.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 25. kubernetes-docs-zh-cn-v1/page-04-sentence-0249

Changed: `risk`

Input:

```text
这一机制有助于优化性能、成本或可靠性。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Contains multiple common Mainland technical terms ('机制', '优化', '性能') that have different idiomatic equivalents in Taiwan ('機制', '優化', '效能').

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 26. ready-gov-evacuation-zh-hans-v1/sentence-001

Changed: `domain`

Input:

```text
许多类型的紧急情况可能会导致你不得不进行疏散。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的 FEMA 疏散指引完整句；依高風險安全語境與臺灣用語需求分類。

Gemini reason: Standard simplified Chinese sentence from official guidance.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 27. ready-gov-evacuation-zh-hans-v1/sentence-003

Changed: `domain`

Input:

```text
无论在什么情况下，计划对于确保各位能快速安全地撤离至关重要。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的 FEMA 疏散指引完整句；依高風險安全語境與臺灣用語需求分類。

Gemini reason: Standard simplified Chinese sentence, formal tone.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 28. ready-gov-evacuation-zh-hans-v1/sentence-004

Changed: `domain, risk`

Input:

```text
了解各自所在社区可能发生的灾害类型，以及当地针对每种具体灾害的应急、疏散和避难计划。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的 FEMA 疏散指引完整句；依高風險安全語境與臺灣用語需求分類。

Gemini reason: Standard simplified Chinese sentence, formal tone.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 29. ready-gov-evacuation-zh-hans-v1/sentence-007

Changed: `domain, risk`

Input:

```text
冠状病毒可能改变了所在社区的计划。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 可獨立判讀的 FEMA 疏散指引完整句；依高風險安全語境與臺灣用語需求分類。

Gemini reason: The term '冠状病毒' (Coronavirus) might require localization to '新冠肺炎' (COVID-19) for Taiwan public health context, representing a potential terminology gap.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 30. ready-gov-evacuation-zh-hans-v1/sentence-008

Changed: `domain`

Input:

```text
确定几个你在紧急情况下可以去的地方，如另一个城市的朋友家或汽车旅馆。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的 FEMA 疏散指引完整句；依高風險安全語境與臺灣用語需求分類。

Gemini reason: Standard simplified Chinese sentence.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 31. ready-gov-evacuation-zh-hans-v1/sentence-009

Changed: `domain`

Input:

```text
选择不同方向的目的地，以便在紧急情况下可以有选择。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的 FEMA 疏散指引完整句；依高風險安全語境與臺灣用語需求分類。

Gemini reason: Standard simplified Chinese sentence.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 32. ready-gov-evacuation-zh-hans-v1/sentence-011

Changed: `domain`

Input:

```text
熟悉离开所在地区的备用路线和其他交通方式。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的 FEMA 疏散指引完整句；依高風險安全語境與臺灣用語需求分類。

Gemini reason: Standard simplified Chinese sentence.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 33. ready-gov-evacuation-zh-hans-v1/sentence-012

Changed: `domain`

Input:

```text
始终遵循当地官员的指示，并记住疏散路线可能是步行，这取决于灾害的类型。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的 FEMA 疏散指引完整句；依高風險安全語境與臺灣用語需求分類。

Gemini reason: Standard simplified Chinese sentence.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 34. ready-gov-evacuation-zh-hans-v1/sentence-014

Changed: `eligible, domain, risk`

Input:

```text
集合准备好撤离用的物资。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 「集合準備好撤離用的物資」語法與動作關係不完整，無法穩定裁決。

Gemini reason: A simple, direct instruction. The term '物资' (supplies/materials) is standard and neutral, requiring straightforward character conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 35. ready-gov-evacuation-zh-hans-v1/sentence-016

Changed: `risk`

Input:

```text
如果有车的话：如果有可能进行疏散，请保持满箱汽油。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 可獨立判讀的 FEMA 疏散指引完整句；依高風險安全語境與臺灣用語需求分類。

Gemini reason: This is evacuation advice. The phrasing '保持满箱汽油' (keep a full tank of gas) is understandable but slightly unnatural; a more idiomatic expression in Taiwan might be '把油箱加滿' (fill up the gas tank). This represents a gap in natural phrasing.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 36. ready-gov-evacuation-zh-hans-v1/sentence-020

Changed: `risk`

Input:

```text
如果你没有车，计划好在需要时如何离开。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 可獨立判讀的 FEMA 疏散指引完整句；依高風險安全語境與臺灣用語需求分類。

Gemini reason: Similar to the previous sentence, the use of '计划好' (plan well) points to a potential localization gap. A more formal or common phrasing in Taiwan for official guidance might be '預先規劃' (plan in advance).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 37. ready-gov-evacuation-zh-hans-v1/sentence-032

Changed: `eligible, domain, risk`

Input:

```text
除非有水淹的危险，否则不要把冰箱和冰柜的插头插上。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 冰箱插頭指令出現疑似否定方向錯譯，不適合作為可靠 benchmark 輸入。

Gemini reason: Candidate gap: '冰柜' (freezer) is more common in Mainland China. Taiwan tends to use '冷凍櫃' for a standalone freezer.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 38. ready-gov-evacuation-zh-hans-v1/sentence-047

Changed: `risk`

Input:

```text
避开停电或公用事业线，它们可能带有致命的电压。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的 FEMA 疏散指引完整句；依高風險安全語境與臺灣用語需求分類。

Gemini reason: Standard safety warning. '公用事业' is a formal term but not a regionalism gap.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 39. ready-gov-evacuation-zh-hans-v1/sentence-048

Changed: `risk`

Input:

```text
远离它们，并立即向电力或公用事业公司报告。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的 FEMA 疏散指引完整句；依高風險安全語境與臺灣用語需求分類。

Gemini reason: Standard safety instruction referring to a power or utility company.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 40. zhtw-project-formal-llm-overconversion-guard-v1/formal-001

Changed: `script, domain`

Input:

```text
采购公告将产品名称 Microsoft Entra ID 原样列入需求表。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 正式文件中的專名、編號或識別碼保留案例，可獨立裁決。

Gemini reason: Contains a product name 'Microsoft Entra ID' that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 41. zhtw-project-formal-llm-overconversion-guard-v1/formal-003

Changed: `script`

Input:

```text
判决书引用案件名称 Brown v. Board of Education。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 正式文件中的專名、編號或識別碼保留案例，可獨立裁決。

Gemini reason: Contains a proper name 'Brown v. Board of Education' that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 42. zhtw-project-formal-llm-overconversion-guard-v1/formal-004

Changed: `script`

Input:

```text
审计报告以 Finding No. 2026-04 标示缺失事项。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 正式文件中的專名、編號或識別碼保留案例，可獨立裁決。

Gemini reason: Contains an identifier 'Finding No. 2026-04' that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 43. zhtw-project-formal-llm-overconversion-guard-v1/formal-007

Changed: `script`

Input:

```text
法院卷宗以 Case No. 24-CV-0187 识别案件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 正式文件中的專名、編號或識別碼保留案例，可獨立裁決。

Gemini reason: Contains an identifier 'Case No. 24-CV-0187' that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 44. zhtw-project-formal-llm-overconversion-guard-v1/formal-008

Changed: `script`

Input:

```text
会议记录保留议程代码 Item 3(c)(ii)。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 正式文件中的專名、編號或識別碼保留案例，可獨立裁決。

Gemini reason: Contains an identifier 'Item 3(c)(ii)' that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 45. zhtw-project-formal-llm-overconversion-guard-v1/formal-009

Changed: `script, domain`

Input:

```text
合约将服务级别标记写为 SLO-99.95。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 正式文件中的專名、編號或識別碼保留案例，可獨立裁決。

Gemini reason: Contains an identifier 'SLO-99.95' that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 46. zhtw-project-formal-llm-overconversion-guard-v1/formal-010

Changed: `script`

Input:

```text
研究报告引用 DOI 10.5281/zenodo.1234567。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 正式文件中的專名、編號或識別碼保留案例，可獨立裁決。

Gemini reason: Contains an identifier 'DOI 10.5281/zenodo.1234567' that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 47. zhtw-project-formal-llm-overconversion-guard-v1/formal-012

Changed: `script`

Input:

```text
证券文件中的 ISIN US5949181045 不得改写。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 正式文件中的專名、編號或識別碼保留案例，可獨立裁決。

Gemini reason: Contains an identifier 'ISIN US5949181045' that must be preserved, as explicitly stated in the source.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 48. zhtw-project-formal-llm-overconversion-guard-v1/formal-013

Changed: `domain`

Input:

```text
危险品申报单保留运输编号 UN 3091。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 正式文件中的專名、編號或識別碼保留案例，可獨立裁決。

Gemini reason: Contains a standard UN transportation number that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 49. zhtw-project-formal-llm-overconversion-guard-v1/formal-014

Changed: `domain`

Input:

```text
专利公报使用申请号 PCT/US2026/012345。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 正式文件中的專名、編號或識別碼保留案例，可獨立裁決。

Gemini reason: Contains a standard international patent application number that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 50. zhtw-project-formal-llm-overconversion-guard-v1/formal-024

Changed: `domain`

Input:

```text
公告中的电子邮件地址 service-desk@example.org 必须保持不变。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 正式文件中的專名、編號或識別碼保留案例，可獨立裁決。

Gemini reason: Contains an email address which must be preserved exactly.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 51. zhtw-project-formal-llm-overconversion-guard-v1/formal-030

Changed: `domain`

Input:

```text
新闻稿将品牌名称 Cloudflare Workers 原样呈现。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 正式文件中的專名、編號或識別碼保留案例，可獨立裁決。

Gemini reason: Contains a proper brand name that must be preserved. The sentence itself is a meta-instruction.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 52. zhtw-project-formal-llm-overconversion-guard-v1/formal-033

Changed: `script, domain`

Input:

```text
药品批号 LOT 26A07 应与包装记录一致。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 正式文件中的專名、編號或識別碼保留案例，可獨立裁決。

Gemini reason: Input contains a product lot number 'LOT 26A07' which must be preserved and not converted.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 53. zhtw-project-formal-llm-overconversion-guard-v1/formal-037

Changed: `script`

Input:

```text
招标文件使用项目代号 Project Lighthouse。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 正式文件中的專名、編號或識別碼保留案例，可獨立裁決。

Gemini reason: Input contains a proper name 'Project Lighthouse' which must be preserved and not converted.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 54. zhtw-project-formal-llm-overconversion-guard-v1/llm-001

Changed: `script, domain`

Input:

```text
请求中的模型名称 gemini-example-pro-002 必须保持不变。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: LLM 系統語境中的識別碼、標籤或字面值保留案例，可獨立裁決。

Gemini reason: Input contains a technical model identifier 'gemini-example-pro-002' which must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 55. zhtw-project-formal-llm-overconversion-guard-v1/llm-002

Changed: `script, domain`

Input:

```text
系统消息以 policy_version=2026-07 标记规则版本。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: LLM 系統語境中的識別碼、標籤或字面值保留案例，可獨立裁決。

Gemini reason: Input contains a technical parameter 'policy_version=2026-07' which must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 56. zhtw-project-formal-llm-overconversion-guard-v1/llm-003

Changed: `script, domain`

Input:

```text
工具调用使用 call_id=call_01JQ8M7Y 对应结果。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: LLM 系統語境中的識別碼、標籤或字面值保留案例，可獨立裁決。

Gemini reason: Input contains a technical identifier 'call_id=call_01JQ8M7Y' which must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 57. zhtw-project-formal-llm-overconversion-guard-v1/llm-005

Changed: `script`

Input:

```text
评测器把 pass、fail 与 abstain 设为固定标签。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: LLM 系統語境中的識別碼、標籤或字面值保留案例，可獨立裁決。

Gemini reason: Input contains English keywords 'pass', 'fail', 'abstain' used as technical labels that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 58. zhtw-project-formal-llm-overconversion-guard-v1/llm-010

Changed: `script, domain`

Input:

```text
系统边界标记 BEGIN_EXTERNAL_CONTEXT 不属于回答内容。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: LLM 系統語境中的識別碼、標籤或字面值保留案例，可獨立裁決。

Gemini reason: Input contains a system marker 'BEGIN_EXTERNAL_CONTEXT' which must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 59. zhtw-project-formal-llm-overconversion-guard-v1/llm-011

Changed: `script, domain`

Input:

```text
批次任务以 batch_01JQ9A2Z7H 作为不可变识别码。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: LLM 系統語境中的識別碼、標籤或字面值保留案例，可獨立裁決。

Gemini reason: Input contains a technical identifier 'batch_01JQ9A2Z7H' which must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 60. zhtw-project-formal-llm-overconversion-guard-v1/llm-013

Changed: `script, domain`

Input:

```text
多模态输入通过 image_url.high_detail 指定解析模式。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: LLM 系統語境中的識別碼、標籤或字面值保留案例，可獨立裁決。

Gemini reason: Contains a technical parameter 'image_url.high_detail' that must be preserved and not converted.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 61. zhtw-project-formal-llm-overconversion-guard-v1/llm-020

Changed: `script, domain`

Input:

```text
语音转录保留说话者标签 SPEAKER_02。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: LLM 系統語境中的識別碼、標籤或字面值保留案例，可獨立裁決。

Gemini reason: Contains a speaker label identifier 'SPEAKER_02' which must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 62. zhtw-project-formal-llm-overconversion-guard-v1/llm-022

Changed: `script, domain`

Input:

```text
对话汇出档保留 message_id、parent_id 与thread_id。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: LLM 系統語境中的識別碼、標籤或字面值保留案例，可獨立裁決。

Gemini reason: Contains technical identifiers 'message_id', 'parent_id', and 'thread_id' that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 63. zhtw-project-formal-llm-overconversion-guard-v1/llm-025

Changed: `script, domain`

Input:

```text
解码器遇到停止序列 </final_answer> 时结束生成。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: LLM 系統語境中的識別碼、標籤或字面值保留案例，可獨立裁決。

Gemini reason: Contains a code sequence '</final_answer>' that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 64. zhtw-project-formal-llm-overconversion-guard-v1/llm-029

Changed: `script, domain`

Input:

```text
知识库文件以 kb://legal/policy-17 作为来源位置。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: LLM 系統語境中的識別碼、標籤或字面值保留案例，可獨立裁決。

Gemini reason: Contains a URI 'kb://legal/policy-17' that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 65. zhtw-project-formal-llm-overconversion-guard-v1/llm-030

Changed: `script, domain`

Input:

```text
评测资料保留 locale=zh-TW 的大小写。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: LLM 系統語境中的識別碼、標籤或字面值保留案例，可獨立裁決。

Gemini reason: Contains a technical parameter 'locale=zh-TW' whose case and content must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 66. zhtw-project-formal-llm-overconversion-guard-v1/llm-038

Changed: `script, domain`

Input:

```text
资料切片的识别码为 chunk_000184。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: LLM 系統語境中的識別碼、標籤或字面值保留案例，可獨立裁決。

Gemini reason: Contains a technical identifier 'chunk_000184' that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 67. zhtw-project-formal-llm-overconversion-guard-v1/llm-039

Changed: `script, domain`

Input:

```text
系统提示引用产品名称 Vertex AI Search。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: LLM 系統語境中的識別碼、標籤或字面值保留案例，可獨立裁決。

Gemini reason: Contains a proper product name 'Vertex AI Search' that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`
