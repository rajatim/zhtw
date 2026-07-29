<!-- zhtw:disable -->
# Blind-v2 Source Classification 051

Packet: `benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-051.json`
Cases: 96
Seed: `20260719`
Selection: `balanced-source-class-remaining-deterministic-sha256-v1`

## Rules

- Read only the input and provenance shown in this packet.
- Do not run zhtw, OpenCC, zhconv, Gemini, or another converter.
- Mark `eligible = no` for malformed, unclear, non-Mandarin, or unsuitable text.
- Script: `simplified`, `mixed`, `traditional`, or `uncertain`.
- Domain: `it_api_cli`, `ui_i18n`, `llm_generated`, `formal_news`, `social_daily`, or `high_stakes`.
- Risk: `candidate_gap`, `over_conversion_guard`, or `baseline_guard`.
- Confidence: `high`, `medium`, or `low`; do not guess when context is insufficient.
- This packet is advisory input classification, not expected-output annotation.

## Cases

### kubernetes-docs-zh-cn-v1/page-01-sentence-0011

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-01-sentence-0011`
- Split: `documentation_01`

Input:

```text
即使名称是自动生成的，它仍可能与现有名称冲突，从而导致 HTTP 409 响应。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-02-sentence-0037

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-02-sentence-0037`
- Split: `documentation_02`

Input:

```text
声明性对象配置更好地支持对目录进行操作并自动检测每个文件的操作类型（创建，修补，删除）。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0014

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0014`
- Split: `documentation_03`

Input:

```text
Pod 会在该节点上运行，直到 Pod 停止或者被终止；如果 Kubernetes 无法在选定的节点上启动 Pod（例如，如果节点在 Pod 启动前崩溃），那么特定的 Pod 将永远不会启动。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0040

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0040`
- Split: `documentation_03`

Input:

```text
`Unknown`（未知） | 因为某些原因无法取得 Pod 的状态。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0042

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0042`
- Split: `documentation_03`

Input:

```text
当 Pod 反复启动失败时，某些 kubectl 命令的 `Status` 字段中可能会出现 `CrashLoopBackOff`。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0048

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0048`
- Split: `documentation_03`

Input:

```text
从 Kubernetes 1.27 开始，除了静态 Pod 和没有 Finalizer 的强制终止 Pod 之外，`kubelet` 会将已删除的 Pod 转换到终止阶段（`Failed` 或 `Succeeded` 具体取决于 Pod 容器的退出状态），然后再从 API 服务器中删除。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0053

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0053`
- Split: `documentation_03`

Input:

```text
容器的状态有三种：`Waiting`（等待）、`Running`（运行中）和 `Terminated`（已终止）。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0113

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0113`
- Split: `documentation_03`

Input:

```text
`Always`：在任何原因的容器终止后都会自动重启容器。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0125

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0125`
- Split: `documentation_03`

Input:

```text
例如，重启策略为 OnFailure 的某个 Pod 包含一个 `try-once` 容器。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0133

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0133`
- Split: `documentation_03`

Input:

```text
当容器的退出符合包含此动作的某个规则时，整个 Pod 被终止并就地重启。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0159

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0159`
- Split: `documentation_03`

Input:

```text
每个节点上的配置优先于 `ReduceDefaultCrashLoopBackOffDecay` 所设置的默认值，即使这会导致某些节点的最大退避时间比集群中的其他节点更长。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0173

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0173`
- Split: `documentation_03`

Input:

```text
需要使用 `PATCH` 操作。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0178

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0178`
- Split: `documentation_03`

Input:

```text
在 Pod 被调度到某节点后，它需要被 kubelet 接受并且挂载所需的存储卷。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0219

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0219`
- Split: `documentation_03`

Input:

```text
`tcpSocket` : 对容器的 IP 地址上的指定端口执行 TCP 检查。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0305

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0305`
- Split: `documentation_03`

Input:

```text
将宽限期限强制设置为 `0` 意味着立即从 API 服务器删除 Pod。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0311

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0311`
- Split: `documentation_03`

Input:

```text
马上删除时不等待确认正在运行的资源已被终止。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0334

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0334`
- Split: `documentation_03`

Input:

```text
（也可能通过其他方式重启 kubelet，例如为修复某个节点缺陷而重启；在这些情况下， Kubernetes 会选择更安全的处理方式，例如先停止再启动 kubelet。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0340

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0340`
- Split: `documentation_03`

Input:

```text
在 Kubernetes 中，你可以选择启用一种传统的行为：在 kubelet 重启后，总是将容器的 `ready` 状态修改为 false。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0342

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0342`
- Split: `documentation_03`

Input:

```text
虽然此特性门控允许暂时回退到这种传统行为，但 Kubernetes 项目建议如果你遇到相关问题，应提交 Bug 报告。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0009

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0009`
- Split: `documentation_04`

Input:

```text
对于集群中给定的某个 Deployment，这一刻运行的 Pod 集合可能不同于下一刻运行该应用的 Pod 集合。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0011

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0011`
- Split: `documentation_04`

Input:

```text
Service API 是 Kubernetes 的组成部分，它是一种抽象，帮助你将 Pod 集合在网络上公开出去。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0056

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0056`
- Split: `documentation_04`

Input:

```text
在所有这些场景中，你都可以定义不指定用来匹配 Pod 的选择算符的 Service。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0059

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0059`
- Split: `documentation_04`

Input:

```text
一个名字空间中的各个 EndpointSlice 都必须具有一个唯一的名称。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0077

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0077`
- Split: `documentation_04`

Input:

```text
如果 Service 的端点太多以至于达到阈值，Kubernetes 会添加另一个空的 EndpointSlice 并在其中存储新的端点信息。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0123

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0123`
- Split: `documentation_04`

Input:

```text
在创建 `Service` 的请求中，你可以通过设置 `spec.clusterIP` 字段来指定自己的集群 IP 地址。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0127

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0127`
- Split: `documentation_04`

Input:

```text
请阅读避免冲突节，以了解 Kubernetes 如何协助降低两个不同的 Service 试图使用相同 IP 地址的风险和影响。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0155

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0155`
- Split: `documentation_04`

Input:

```text
在使用支持外部负载均衡器的云平台时，如果将 `type` 设置为 `"LoadBalancer"`，则平台会为 Service 提供负载均衡器。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0234

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0234`
- Split: `documentation_04`

Input:

```text
能够感知集群的 DNS 服务器（例如 CoreDNS）会监视 Kubernetes API 中的新 Service，并为每个 Service 创建一组 DNS 记录。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0248

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0248`
- Split: `documentation_04`

Input:

```text
虽然流量策略侧重于严格的语义保证，但流量分发允许你表达一定的偏好（例如路由到拓扑上更接近的端点）。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0254

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0254`
- Split: `documentation_04`

Input:

```text
如果你想确保来自特定客户端的连接每次都传递到同一个 Pod，你可以配置基于客户端 IP 地址的会话亲和性。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0257

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0257`
- Split: `documentation_04`

Input:

```text
当网络流量进入集群时，如果外部 IP（作为目的 IP 地址）和端口都与该 Service 匹配， Kubernetes 所配置的规则和路由会确保流量被路由到该 Service 的端点之一。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0258

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0258`
- Split: `documentation_04`

Input:

```text
定义 Service 时，你可以为任何 Service 类型指定 `externalIPs`。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-001

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-001`
- Split: `guide`

Input:

```text
不是假设，而是何时：美国各州和领地都有遭受灾难的风险。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-058

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-058`
- Split: `guide`

Input:

```text
枪手行凶 • 如果您看见一些事情或某人形迹可疑，请向当地执法部门报告。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-071

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-071`
- Split: `guide`

Input:

```text
每次到访建筑物时，请找出在附近的两个出口。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-088

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-088`
- Split: `guide`

Input:

```text
这可能是任何要求您立即完成任务的信息，提供一些好得令人难以置信的事物，或要求提供个人的信息。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-103

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-103`
- Split: `guide`

Input:

```text
如果在斜坡、悬崖或山区附近，请警惕掉落的岩石和山体滑坡。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-116

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-116`
- Split: `guide`

Input:

```text
在天热时段，切勿将儿童、成人或动物单独留在车内。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-129

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-129`
- Split: `guide`

Input:

```text
每月或每次发薪水时留下一定数量的金钱，存入紧急储备金。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-134

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-134`
- Split: `guide`

Input:

```text
为您的房屋，公寓或企业购买保险可以帮助您修复，重建或替换灾难期间发生的损坏。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-141

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-141`
- Split: `guide`

Input:

```text
找出所在地区可能发生的洪水风险类型。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-150

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-150`
- Split: `guide`

Input:

```text
如果被困在建筑物中，请前往建筑物的最高层。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-155

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-155`
- Split: `guide`

Input:

```text
洪水后进行清理时，请使用护目镜、安全镜、工作手套、安全帽和防水靴。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-189

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-189`
- Split: `guide`

Input:

```text
最佳位置是地下，或在由砖石或混凝土的大型建筑物的中间。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-217

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-217`
- Split: `guide`

Input:

```text
带有备用电池的电子探测器也可接受。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-244

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-244`
- Split: `guide`

Input:

```text
在雷电风暴期间，请注意官方的警报。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-247

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-247`
- Split: `guide`

Input:

```text
了解龙卷风的迹象，包括旋转的漏斗状云、接近的碎片云或仿佛货运火车一般的巨大轰鸣。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-273

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-273`
- Split: `guide`

Input:

```text
风和重力将携带碎石和火山灰。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-298

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-298`
- Split: `guide`

Input:

```text
为汽车准备一个应急补给包，包括跳线、沙子、手电筒、瓶装水和不易腐烂的点心。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-307

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-307`
- Split: `guide`

Input:

```text
老年人和幼儿在极寒的天气更为危险。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-309

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-309`
- Split: `guide`

Input:

```text
考虑制定撤离、通信计划，保护重要文件和财产安全。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-314

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-314`
- Split: `guide`

Input:

```text
确保该人至少有两种联系方式。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-315

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-315`
- Split: `guide`

Input:

```text
您也可以使用社交媒体作为与家人沟通的重要方法。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-319

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-319`
- Split: `guide`

Input:

```text
计划一旦制定了，家人就必须演练该计划，就像进行消防演练一样。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-342

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-342`
- Split: `guide`

Input:

```text
请遵循建议的撤离路线，不要走捷径，因为它们可能受阻。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-358

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-358`
- Split: `guide`

Input:

```text
应该将应急用品存储在不同地方，例如家里、办公室和车上。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-359

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-359`
- Split: `guide`

Input:

```text
基本应急用品包应包括以下内容： • 水：水：在包中为每个人每天准备一加仑的饮水。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-367

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-367`
- Split: `guide`

Input:

```text
宠物食品和为宠物准备的额外用水。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-405

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-405`
- Split: `guide`

Input:

```text
工作场所、学校以及社区或信仰团体可能有自己类似的选择加入通知系统。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-408

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-408`
- Split: `guide`

Input:

```text
重复检查您的移动设备是否可以收到无线紧急警报（WEA）。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-414

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-414`
- Split: `guide`

Input:

```text
现在立即采取以下措施，找到并保护适当的保单，以保护家庭的财务健康。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-451

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-451`
- Split: `guide`

Input:

```text
保护财产您现在就可采用一些措施，以缓解（即减轻）潜在灾害对您的房屋或财产可能造成的影响。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-510

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-510`
- Split: `guide`

Input:

```text
如果房屋已损坏，请由合格的检查员检查以确保可以安全进入和居住。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-527

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-527`
- Split: `guide`

Input:

```text
请记住，灾难和威胁生命的情况将增加野生动物的不可预测性。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-011

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-011`
- Split: `project_original`

Input:

```text
公报注明法规条文开始生效的具体日期。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-015

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-015`
- Split: `project_original`

Input:

```text
统计报告揭露估计值的误差范围和限制。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-017

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-017`
- Split: `project_original`

Input:

```text
委员会尚未核定草案中涉及费用的条款。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-018

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-018`
- Split: `project_original`

Input:

```text
承办单位确认附件版本与签核纪录相符。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-019

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-019`
- Split: `project_original`

Input:

```text
新闻资料区分已确认事实与初步研判。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-020

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-020`
- Split: `project_original`

Input:

```text
审查意见指出引用资料缺少公开取得路径。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-022

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-022`
- Split: `project_original`

Input:

```text
主管机关保留现场检查的照片与时间戳记。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-030

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-030`
- Split: `project_original`

Input:

```text
调查结果必须经过资料检核才能对外发布。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-031

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-031`
- Split: `project_original`

Input:

```text
主管单位要求说明指标定义变更造成的影响。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-033

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-033`
- Split: `project_original`

Input:

```text
会议主席确认表决人数符合程序规定。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-039

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-039`
- Split: `project_original`

Input:

```text
机关将错误讯息的更正说明置于原文旁边。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-041

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-041`
- Split: `project_original`

Input:

```text
预算书注明各项估算采用的价格基准。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-042

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-042`
- Split: `project_original`

Input:

```text
委员会请专家确认技术用语是否准确。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-043

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-043`
- Split: `project_original`

Input:

```text
政策说明列出不适用这项措施的对象。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-045

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-045`
- Split: `project_original`

Input:

```text
新闻稿不得省略调查结果的重要限制条件。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-047

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-047`
- Split: `project_original`

Input:

```text
审议结果须待主席签署后才正式生效。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-048

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-048`
- Split: `project_original`

Input:

```text
报告附录说明无法完成验证的资料项目。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-003

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-003`
- Split: `project_original`

Input:

```text
助理无法验证引用时应说明资料不足。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-004

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-004`
- Split: `project_original`

Input:

```text
摘要不能删除会改变结论的限制条件。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-009

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-009`
- Split: `project_original`

Input:

```text
检索结果为空时不得假设文件已经删除。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-011

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-011`
- Split: `project_original`

Input:

```text
系统会显示每项结论对应的证据片段。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-018

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-018`
- Split: `project_original`

Input:

```text
模型产生的表格必须对应工具回传的数据。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-019

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-019`
- Split: `project_original`

Input:

```text
分类器只依据输入内容判断资料所属领域。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-020

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-020`
- Split: `project_original`

Input:

```text
低信心的事实陈述会进入待确认清单。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-022

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-022`
- Split: `project_original`

Input:

```text
回答采用推算数字时必须清楚标示假设。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-029

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-029`
- Split: `project_original`

Input:

```text
助理引用法规时需要确认条文仍然有效。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-033

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-033`
- Split: `project_original`

Input:

```text
助理只可使用目前对话中提供的账号资料。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-035

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-035`
- Split: `project_original`

Input:

```text
模型应指出哪些步骤尚未实际执行。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-041

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-041`
- Split: `project_original`

Input:

```text
评测人员会复查自动判分出现分歧的案例。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-043

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-043`
- Split: `project_original`

Input:

```text
系统会记录使用者接受或拒绝建议的决定。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-049

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-049`
- Split: `project_original`

Input:

```text
模型应把使用者提供的事实与外部资料分开。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-050

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-050`
- Split: `project_original`

Input:

```text
评测结果必须能够追溯到固定版本的输入。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```
