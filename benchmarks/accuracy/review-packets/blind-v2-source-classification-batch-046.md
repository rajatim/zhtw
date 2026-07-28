<!-- zhtw:disable -->
# Blind-v2 Source Classification 046

Packet: `benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-046.json`
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

### kubernetes-docs-zh-cn-v1/page-01-sentence-0012

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-01-sentence-0012`
- Split: `documentation_01`

Input:

```text
从 Kubernetes v1.31 及更高版本开始，这种情况发生的概率大大降低，因为服务器会尝试最多 8 次生成唯一名称，然后才返回 HTTP 409 响应。
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

### kubernetes-docs-zh-cn-v1/page-02-sentence-0011

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-02-sentence-0011`
- Split: `documentation_02`

Input:

```text
命令不与变更审查流程集成。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0032

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0032`
- Split: `documentation_03`

Input:

```text
除了本文档中列举的内容外，不应该再假定 Pod 有其他的 `phase` 值。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0049

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0049`
- Split: `documentation_03`

Input:

```text
如果某节点死掉或者与集群中其他节点失联，Kubernetes 会实施一种策略，将失去的节点上运行的所有 Pod 的 `phase` 设置为 `Failed`。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0056

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0056`
- Split: `documentation_03`

Input:

```text
如果容器并不处在 `Running` 或 `Terminated` 状态之一，它就处在 `Waiting` 状态。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0060

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0060`
- Split: `documentation_03`

Input:

```text
如果配置了 `postStart` 回调，那么该回调已经执行且已完成。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0063

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0063`
- Split: `documentation_03`

Input:

```text
如果你使用 `kubectl` 来查询包含 `Terminated` 状态的容器的 Pod 时，你会看到容器进入此状态的原因、退出代码以及容器执行期间的起止时间。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0064

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0064`
- Split: `documentation_03`

Input:

```text
如果容器配置了 `preStop` 回调，则该回调会在容器进入 `Terminated` 状态之前执行。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0078

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0078`
- Split: `documentation_03`

Input:

```text
如果应用程序没有在预期时间内启动服务，健康检查就会失败。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0081

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0081`
- Split: `documentation_03`

Input:

```text
这通常是诊断导致崩溃的问题的最直接方法。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0082

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0082`
- Split: `documentation_03`

Input:

```text
检查事件：使用 `kubectl describe pod ` 查看 Pod 的事件，这可以提供有关配置或资源问题的提示。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0098

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0098`
- Split: `documentation_03`

Input:

```text
`Always`：只要容器终止就自动重启容器。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0106

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0106`
- Split: `documentation_03`

Input:

```text
当 Pod 中的容器退出时，`kubelet` 会以指数级回退延迟机制（10 秒、20 秒、40 秒......）重启容器，上限为 300 秒（5 分钟）。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0120

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0120`
- Split: `documentation_03`

Input:

```text
支持的条件是 `exitCodes`，用于将容器的退出码与给定值列表进行比较。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0149

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0149`
- Split: `documentation_03`

Input:

```text
整个 Pod（包括 `setup-environment` init 容器和 `main-application` 容器）随后就地重启。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0174

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0174`
- Split: `documentation_03`

Input:

```text
你可以使用 Kubernetes 客户端库之一来编写代码，针对 Pod 就绪态设置定制的 Pod 状况。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0180

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0180`
- Split: `documentation_03`

Input:

```text
如果启用了 `PodReadyToStartContainersCondition` 特性门控（Kubernetes 版本中默认启用）， `PodReadyToStartContainers` 状况会被添加到 Pod 的 `status.conditions` 字段中。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0184

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0184`
- Split: `documentation_03`

Input:

```text
在运行时插件成功完成 Pod 的沙箱创建和网络配置后， kubelet 会将 `PodReadyToStartContainers` 状况设置为 `True`。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0202

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0202`
- Split: `documentation_03`

Input:

```text
这种方法：适用于任何 Kubernetes 版本。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0213

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0213`
- Split: `documentation_03`

Input:

```text
`grpc` : 使用 gRPC 执行一个远程过程调用。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0214

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0214`
- Split: `documentation_03`

Input:

```text
目标应该实现 gRPC 健康检查。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0220

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0220`
- Split: `documentation_03`

Input:

```text
如果端口打开，则诊断被认为是成功的。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0224

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0224`
- Split: `documentation_03`

Input:

```text
这种场景下，请考虑使用其他探针机制以避免额外的开销。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0225

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0225`
- Split: `documentation_03`

Input:

```text
`Success`（成功） : 容器通过了诊断。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0233

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0233`
- Split: `documentation_03`

Input:

```text
初始延迟之前的就绪态的状态值默认为 `Failure`。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0258

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0258`
- Split: `documentation_03`

Input:

```text
由于 Pod 所代表的是在集群中节点上运行的进程，当不再需要这些进程时允许其体面地终止是很重要的。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0263

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0263`
- Split: `documentation_03`

Input:

```text
通常 Pod 体面终止的过程为：kubelet 先发送一个带有体面超时限期的 TERM（又名 SIGTERM）信号到每个容器中的主进程，将请求发送到容器运行时来尝试停止 Pod 中的容器。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0272

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0272`
- Split: `documentation_03`

Input:

```text
在容器生命周期中定义终止信号时，Pod 的 `spec.os.name` 字段必须存在。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0280

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0280`
- Split: `documentation_03`

Input:

```text
在 Pod 运行所在的节点上：`kubelet` 一旦看到 Pod 被标记为正在终止（已经设置了体面终止限期），`kubelet` 即开始本地的 Pod 关闭过程。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0287

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0287`
- Split: `documentation_03`

Input:

```text
如果关闭顺序很重要，考虑使用 `preStop` 钩子进行同步（或者切换为使用 Sidecar 容器）。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0289

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0289`
- Split: `documentation_03`

Input:

```text
和其他工作负载资源不再将关闭进程中的 Pod 视为合法的、能够提供服务的副本。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0292

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0292`
- Split: `documentation_03`

Input:

```text
任何正在终止的 Pod 所对应的端点都不会立即从 EndpointSlice 中被删除，EndpointSlice API 会公开一个状态来指示其处于终止状态。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0301

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0301`
- Split: `documentation_03`

Input:

```text
API 服务器删除 Pod 的 API 对象，从任何客户端都无法再看到该对象。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0306

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0306`
- Split: `documentation_03`

Input:

```text
如果 Pod 仍然运行于某节点上，强制删除操作会触发 `kubelet` 立即执行清理操作。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0016

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0016`
- Split: `documentation_04`

Input:

```text
Service 抽象使这种解耦成为可能。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0017

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0017`
- Split: `documentation_04`

Input:

```text
Service 所对应的 Pod 集合通常由你定义的来确定。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0033

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0033`
- Split: `documentation_04`

Input:

```text
你可以定义一个 Service 来发布该 TCP 侦听器。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0055

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0055`
- Split: `documentation_04`

Input:

```text
在评估所采用的方法时，你仅在 Kubernetes 中运行一部分后端。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0068

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0068`
- Split: `documentation_04`

Input:

```text
访问没有选择算符的 Service 与有选择算符的 Service 的原理相同。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0101

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0101`
- Split: `documentation_04`

Input:

```text
与一般的 Kubernetes 名称一样，端口名称只能包含小写字母、数字和 `-`。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0125

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0125`
- Split: `documentation_04`

Input:

```text
你所选择的 IP 地址必须是合法的 IPv4 或者 IPv6 地址，并且这个 IP 地址在 API 服务器上所配置的 `service-cluster-ip-range` CIDR 范围内。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0130

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0130`
- Split: `documentation_04`

Input:

```text
你的 Service 在其 `.spec.ports[*].nodePort` 字段中报告已分配的端口。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0142

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0142`
- Split: `documentation_04`

Input:

```text
动态端口分配默认使用较高的端口段，并且在较高的端口段耗尽时也可以使用较低的端口段。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0145

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0145`
- Split: `documentation_04`

Input:

```text
你可以配置集群中的节点使用特定 IP 地址来支持 NodePort Service。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0151

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0151`
- Split: `documentation_04`

Input:

```text
`--nodeport-addresses` 的默认值是一个空的列表。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0153

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0153`
- Split: `documentation_04`

Input:

```text
此 Service 的可见形式为 `:spec.ports[].nodePort` 以及 `.spec.clusterIP:spec.ports[].port`。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0165

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0165`
- Split: `documentation_04`

Input:

```text
针对 Service 的 `.spec.loadBalancerIP` 字段已在 Kubernetes v1.24 中被弃用。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0178

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0178`
- Split: `documentation_04`

Input:

```text
通过设置 Service 的 `spec.allocateLoadBalancerNodePorts` 为 `false`，你可以对 LoadBalancer 类型的 Service 禁用节点端口分配操作。
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

### zhtw-project-formal-llm-overconversion-guard-v1/formal-002

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-002`
- Split: `project_original`

Input:

```text
委员会文件编号 COM(2026) 318 final 应保持完整。
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

### zhtw-project-formal-llm-overconversion-guard-v1/formal-005

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-005`
- Split: `project_original`

Input:

```text
公报附件沿用标题 Annex IV，不改写罗马数字。
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

### zhtw-project-formal-llm-overconversion-guard-v1/formal-006

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-006`
- Split: `project_original`

Input:

```text
声明引用原文“without prejudice”，引号内文字不得意译。
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

### zhtw-project-formal-llm-overconversion-guard-v1/formal-011

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-011`
- Split: `project_original`

Input:

```text
预算附件以 FY2028-Q1 标示财政期间。
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

### zhtw-project-formal-llm-overconversion-guard-v1/formal-015

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-015`
- Split: `project_original`

Input:

```text
医学论文将试验编号 NCT01234567 列在摘要末尾。
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

### zhtw-project-formal-llm-overconversion-guard-v1/formal-017

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-017`
- Split: `project_original`

Input:

```text
技术规范引用完整版本 ISO 8601-1:2019。
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

### zhtw-project-formal-llm-overconversion-guard-v1/formal-019

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-019`
- Split: `project_original`

Input:

```text
决议正文提及 Paris Agreement 时沿用官方英文名称。
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

### zhtw-project-formal-llm-overconversion-guard-v1/formal-020

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-020`
- Split: `project_original`

Input:

```text
外交公报将 Côte d’Ivoire 维持为官方拼写。
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

### zhtw-project-formal-llm-overconversion-guard-v1/formal-021

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-021`
- Split: `project_original`

Input:

```text
登记资料中的姓名为 Chen Yu-Hsuan，不应调整拼音。
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

### zhtw-project-formal-llm-overconversion-guard-v1/formal-022

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-022`
- Split: `project_original`

Input:

```text
听证记录把证物标记为 Exhibit C-12。
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

### zhtw-project-formal-llm-overconversion-guard-v1/formal-023

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-023`
- Split: `project_original`

Input:

```text
法学论文引用“stare decisis”时保留拉丁文。
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

### zhtw-project-formal-llm-overconversion-guard-v1/formal-025

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-025`
- Split: `project_original`

Input:

```text
统计表以变量名 adjusted_R2 标示校正决定系数。
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

### zhtw-project-formal-llm-overconversion-guard-v1/formal-026

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-026`
- Split: `project_original`

Input:

```text
报告将坐标参考系统写为 EPSG:3826。
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

### zhtw-project-formal-llm-overconversion-guard-v1/formal-029

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-029`
- Split: `project_original`

Input:

```text
会议决议保留投票结果 17-2-1 的连字符格式。
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

### zhtw-project-formal-llm-overconversion-guard-v1/formal-031

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-031`
- Split: `project_original`

Input:

```text
调查问卷沿用量表名称 PHQ-9。
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

### zhtw-project-formal-llm-overconversion-guard-v1/formal-032

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-032`
- Split: `project_original`

Input:

```text
工程图面以 Drawing No. A-104 标示楼层平面图。
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

### zhtw-project-formal-llm-overconversion-guard-v1/formal-034

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-034`
- Split: `project_original`

Input:

```text
档案目录保留文件路径 /records/2026/final.pdf。
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

### zhtw-project-formal-llm-overconversion-guard-v1/formal-035

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-035`
- Split: `project_original`

Input:

```text
声明中的“status quo ante”属于原文引语。
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

### zhtw-project-formal-llm-overconversion-guard-v1/formal-036

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-036`
- Split: `project_original`

Input:

```text
认证报告列出证书序号 04:7A:9C:11。
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

### zhtw-project-formal-llm-overconversion-guard-v1/formal-038

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-038`
- Split: `project_original`

Input:

```text
资料表将空值记为 N/A，而不是数字零。
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

### zhtw-project-formal-llm-overconversion-guard-v1/formal-039

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-039`
- Split: `project_original`

Input:

```text
研究计划引用资料集版本 v2026.07.1。
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

### zhtw-project-formal-llm-overconversion-guard-v1/formal-040

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-040`
- Split: `project_original`

Input:

```text
裁定书末尾保留签章识别码 SIG-8F21C0。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-004

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-004`
- Split: `project_original`

Input:

```text
结构化输出必须符合 schema 名称 invoice_summary_v2。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-006

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-006`
- Split: `project_original`

Input:

```text
检索器会将 top_k=12 写入追踪记录。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-007

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-007`
- Split: `project_original`

Input:

```text
向量字段 text_embedding_3_large 不得重新命名。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-008

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-008`
- Split: `project_original`

Input:

```text
引用标记 [doc:security#auth-3] 必须完整保留。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-009

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-009`
- Split: `project_original`

Input:

```text
提示模板使用 {{customer_name}} 作为占位符。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-012

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-012`
- Split: `project_original`

Input:

```text
响应事件 response.reasoning_summary.delta 只携带新增内容。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-014

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-014`
- Split: `project_original`

Input:

```text
工具名称 lookup_customer_v3 不应翻译。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-015

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-015`
- Split: `project_original`

Input:

```text
安全分类标签 self_harm_intent 必须使用下划线。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-016

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-016`
- Split: `project_original`

Input:

```text
模型路由规则将 region=asia-east1 传给后端。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-017

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-017`
- Split: `project_original`

Input:

```text
缓存事件 prompt_cache.miss 与 prompt_cache.hit 分开统计。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-018

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-018`
- Split: `project_original`

Input:

```text
函数参数 additionalProperties 固定设为 false。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-019

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-019`
- Split: `project_original`

Input:

```text
测试案例要求输出字面值 null。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-021

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-021`
- Split: `project_original`

Input:

```text
审核状态 needs_human_review 表示必须人工确认。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-023

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-023`
- Split: `project_original`

Input:

```text
评分报告以 macro_f1 与 exact_match 为指标名称。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-024

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-024`
- Split: `project_original`

Input:

```text
提示注入测试包含字串 IGNORE_PREVIOUS_INSTRUCTIONS。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-026

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-026`
- Split: `project_original`

Input:

```text
红队资料中的 DROP TABLE audit_log; 只是测试内容。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-027

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-027`
- Split: `project_original`

Input:

```text
输出档名 evaluation-run-2026-07-28.json 不应改写。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-028

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-028`
- Split: `project_original`

Input:

```text
代理将 handoff_target=human_support 写入事件。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-031

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-031`
- Split: `project_original`

Input:

```text
模型快照名称 assistant-prod@2026-07-28 必须原样记录。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-032

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-032`
- Split: `project_original`

Input:

```text
工具错误代码 TOOL_TIMEOUT_30S 不应意译。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-033

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-033`
- Split: `project_original`

Input:

```text
JSON 字段 finish_reason 的值为 tool_calls。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-034

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-034`
- Split: `project_original`

Input:

```text
检索过滤器使用 tenant_id eq 'tw-001'。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-035

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-035`
- Split: `project_original`

Input:

```text
基准结果以 win_rate_paired 记录成对胜率。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-036

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-036`
- Split: `project_original`

Input:

```text
追踪属性 gen_ai.operation.name 设为 chat。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-037

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-037`
- Split: `project_original`

Input:

```text
模型拒答时返回状态码 safety_refusal。
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

### zhtw-project-formal-llm-overconversion-guard-v1/llm-040

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-040`
- Split: `project_original`

Input:

```text
离线评测使用种子值 seed=20260719。
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
