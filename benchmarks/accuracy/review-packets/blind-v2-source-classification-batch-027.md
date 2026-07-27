<!-- zhtw:disable -->
# Blind-v2 Source Classification 027

Packet: `benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-027.json`
Cases: 100
Seed: `20260719`
Selection: `equal-source-deterministic-sha256-v1`
Selection round: 1

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

### kubernetes-docs-zh-cn-v1/page-01-sentence-0008

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-01-sentence-0008`
- Split: `documentation_01`

Input:

```text
当对象所代表的是一个物理实体（例如代表一台物理主机的 Node）时，如果在 Node 对象未被删除并重建的条件下，重新创建了同名的物理主机，则 Kubernetes 会将新的主机看作是老的主机，这可能会带来某种不一致性。
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

### kubernetes-docs-zh-cn-v1/page-01-sentence-0009

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-01-sentence-0009`
- Split: `documentation_01`

Input:

```text
当在资源创建请求中提供 `generateName` 而不是 `name` 时，服务器可能会生成一个名称。
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

### kubernetes-docs-zh-cn-v1/page-01-sentence-0024

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-01-sentence-0024`
- Split: `documentation_01`

Input:

```text
Kubernetes UID 是全局唯一标识符（也叫 UUID）。
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

### kubernetes-docs-zh-cn-v1/page-02-sentence-0004

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-02-sentence-0004`
- Split: `documentation_02`

Input:

```text
应该只使用一种技术来管理 Kubernetes 对象。
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

### kubernetes-docs-zh-cn-v1/page-02-sentence-0005

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-02-sentence-0005`
- Split: `documentation_02`

Input:

```text
混合和匹配技术作用在同一对象上将导致未定义行为。
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

### kubernetes-docs-zh-cn-v1/page-02-sentence-0013

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-02-sentence-0013`
- Split: `documentation_02`

Input:

```text
除了实时内容外，命令不提供记录源。
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

### kubernetes-docs-zh-cn-v1/page-02-sentence-0020

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-02-sentence-0020`
- Split: `documentation_02`

Input:

```text
比如类型为 `LoadBalancer` 的服务，它的 `externalIPs` 字段就是独立于集群配置进行更新。
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

### kubernetes-docs-zh-cn-v1/page-02-sentence-0026

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-02-sentence-0026`
- Split: `documentation_02`

Input:

```text
指令式对象配置行为更加简单易懂。
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

### kubernetes-docs-zh-cn-v1/page-02-sentence-0035

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-02-sentence-0035`
- Split: `documentation_02`

Input:

```text
处理 `configs` 目录中的所有对象配置文件，创建并更新活跃对象。
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

### kubernetes-docs-zh-cn-v1/page-02-sentence-0036

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-02-sentence-0036`
- Split: `documentation_02`

Input:

```text
对活动对象所做的更改即使未合并到配置文件中，也会被保留下来。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0004

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0004`
- Split: `documentation_03`

Input:

```text
Pod 会被创建、赋予一个唯一的 ID（UID），并被调度到节点，并在终止（根据重启策略）或删除之前一直运行在该节点。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0013

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0013`
- Split: `documentation_03`

Input:

```text
一旦 Pod 被调度并绑定到某个节点，Kubernetes 会尝试在该节点上运行 Pod。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0022

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0022`
- Split: `documentation_03`

Input:

```text
Kubernetes 使用一种高级抽象来管理这些相对而言可随时丢弃的 Pod 实例，称作。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0031

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0031`
- Split: `documentation_03`

Input:

```text
Pod 阶段的数量和含义是严格定义的。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0035

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0035`
- Split: `documentation_03`

Input:

```text
`Running`（运行中） | Pod 已经绑定到了某个节点，Pod 中所有的容器都已被创建。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0036

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0036`
- Split: `documentation_03`

Input:

```text
至少有一个容器仍在运行，或者正处于启动或重启状态。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0046

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0046`
- Split: `documentation_03`

Input:

```text
Pod 被赋予一个可以体面终止的期限，默认为 30 秒。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0050

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0050`
- Split: `documentation_03`

Input:

```text
Kubernetes 会跟踪 Pod 中每个容器的状态，就像它跟踪 Pod 总体上的阶段一样。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0057

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0057`
- Split: `documentation_03`

Input:

```text
处于 `Waiting` 状态的容器仍在运行它完成启动所需要的操作：例如，从某个容器镜像仓库拉取容器镜像，或者向容器应用数据等等。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0069

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0069`
- Split: `documentation_03`

Input:

```text
CrashLoopBackOff 状态：这一状态表明，对于一个给定的、处于崩溃循环、反复失效并重启的容器，回退延迟机制目前正在生效。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0075

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0075`
- Split: `documentation_03`

Input:

```text
应用程序错误导致的容器退出。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0076

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0076`
- Split: `documentation_03`

Input:

```text
配置错误，如环境变量不正确或配置文件丢失。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0077

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0077`
- Split: `documentation_03`

Input:

```text
资源限制，容器可能没有足够的内存或 CPU 正常启动。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0097

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0097`
- Split: `documentation_03`

Input:

```text
对于因错误而退出的 Init 容器，如果 Pod 级别 `restartPolicy` 为 `OnFailure` 或 `Always`，则 kubelet 会重新启动 Init 容器。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0100

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0100`
- Split: `documentation_03`

Input:

```text
`Never`：不会自动重启已终止的容器。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0110

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0110`
- Split: `documentation_03`

Input:

```text
容器重启策略和规则适用于 Pod 中的以及常规的 Init 容器。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0137

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0137`
- Split: `documentation_03`

Input:

```text
配置的 `terminationGracePeriodSeconds` 不会生效，配置的所有 `preStop` 回调也不会被执行。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0151

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0151`
- Split: `documentation_03`

Input:

```text
启用 Alpha 特性开关 `ReduceDefaultCrashLoopBackOffDecay` 后，集群中容器启动重试的初始延迟将从 10 秒减少到 1 秒，之后每次重启延迟时间按 2 倍指数增长，直到达到最大延迟 60 秒（之前为 300 秒，即 5 分钟）。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0158

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0158`
- Split: `documentation_03`

Input:

```text
如果你将此特性与上文提到的 Alpha 特性 `ReduceDefaultCrashLoopBackOffDecay` 一起使用，那么集群的初始退避时间和最大退避时间默认值将不再是 10 秒和 300 秒，而是 1 秒和 60 秒。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0166

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0166`
- Split: `documentation_03`

Input:

```text
`PodResizeInProgress`：Pod 正在调整大小中。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0167

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0167`
- Split: `documentation_03`

Input:

```text
你的应用可以向 PodStatus 中注入额外的反馈或者信号：Pod Readiness（Pod 就绪态）。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0179

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0179`
- Split: `documentation_03`

Input:

```text
一旦这些阶段完成，Kubelet 将与容器运行时（使用）一起为 Pod 生成运行时沙箱并配置网络。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0186

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0186`
- Split: `documentation_03`

Input:

```text
对于带有 Init 容器的 Pod，kubelet 会在 Init 容器成功完成后将 `Initialized` 状况设置为 `True` （这发生在运行时成功创建沙箱和配置网络之后），对于没有 Init 容器的 Pod，kubelet 会在创建沙箱和网络配置开始之前将 `Initialized` 状况设置为 `True`。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0190

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0190`
- Split: `documentation_03`

Input:

```text
这亦被称为原地 Pod 垂直扩缩。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0191

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0191`
- Split: `documentation_03`

Input:

```text
这允许你在可能避免应用程序中断的同时，调整运行容器的资源配置。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0193

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0193`
- Split: `documentation_03`

Input:

```text
然后，kubelet 会尝试将新的资源值应用到运行中的容器。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0195

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0195`
- Split: `documentation_03`

Input:

```text
有关调整大小状态的更多详情，请参见容器调整大小状态。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0198

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0198`
- Split: `documentation_03`

Input:

```text
你可以使用容器规约中的 `resizePolicy` 配置是否需要重启容器以进行调整大小。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0208

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0208`
- Split: `documentation_03`

Input:

```text
probe 是由 kubelet 对容器执行的定期诊断。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0212

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0212`
- Split: `documentation_03`

Input:

```text
如果命令退出时返回码为 0 则认为诊断成功。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0216

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0216`
- Split: `documentation_03`

Input:

```text
`httpGet` : 对容器的 IP 地址上指定端口和路径执行 HTTP `GET` 请求。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0228

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0228`
- Split: `documentation_03`

Input:

```text
`livenessProbe` : 指示容器是否正在运行。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0231

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0231`
- Split: `documentation_03`

Input:

```text
`readinessProbe` : 指示容器是否准备好为请求提供服务。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0239

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0239`
- Split: `documentation_03`

Input:

```text
如欲了解如何设置存活态、就绪态和启动探针的进一步细节，可以参阅配置存活态、就绪态和启动探针。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0249

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0249`
- Split: `documentation_03`

Input:

```text
然而，如果你想区分已经失败的应用和仍在处理其启动数据的应用，你可能更倾向于使用就绪探针。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0250

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0250`
- Split: `documentation_03`

Input:

```text
请注意，如果你只是想在 Pod 被删除时能够排空请求，则不一定需要使用就绪态探针；当 Pod 被删除时，`EndpointSlice` 中对应的端点会更新其状况：该端点的 `ready` 状况将被设置为 `false`，因此负载均衡器不会再将该 Pod 用于常规流量。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0253

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0253`
- Split: `documentation_03`

Input:

```text
你不再需要配置一个较长的存活态探测时间间隔，只需要设置另一个独立的配置选定，对启动期间的容器执行探测，从而允许使用远远超出存活态时间间隔所允许的时长。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0254

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0254`
- Split: `documentation_03`

Input:

```text
如果你的容器启动时间通常超出 \\( initialDelaySeconds + failureThreshold \times periodSeconds \\) 总值，你应该设置一个启动探测，对存活态探针所使用的同一端点执行检查。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0264

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0264`
- Split: `documentation_03`

Input:

```text
停止容器的这些请求由容器运行时以异步方式处理。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0275

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0275`
- Split: `documentation_03`

Input:

```text
如果在生命周期中定义了终止信号，则会覆盖容器镜像中定义的信号。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0276

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0276`
- Split: `documentation_03`

Input:

```text
如果容器规约中未定义终止信号，则容器将回退到默认行为。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0277

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0277`
- Split: `documentation_03`

Input:

```text
你使用 `kubectl` 工具手动删除某个特定的 Pod，而该 Pod 的体面终止限期是默认值（30 秒）。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0279

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0279`
- Split: `documentation_03`

Input:

```text
如果你使用 `kubectl describe` 来查验你正在删除的 Pod，该 Pod 会显示为 "Terminating" （正在终止）。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0283

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0283`
- Split: `documentation_03`

Input:

```text
如果 `preStop` 回调所需要的时间长于默认的体面终止限期，你必须修改 `terminationGracePeriodSeconds` 属性值来使其正常工作。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0286

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0286`
- Split: `documentation_03`

Input:

```text
否则，Pod 中的容器会在不同的时间和任意的顺序接收 TERM 信号。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0299

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0299`
- Split: `documentation_03`

Input:

```text
`kubelet` 将 Pod 转换到终止阶段（`Failed` 或 `Succeeded`，具体取决于其容器的结束状态）。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0308

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0308`
- Split: `documentation_03`

Input:

```text
执行强制删除操作时，API 服务器不再等待来自 `kubelet` 的、关于 Pod 已经在原来运行的节点上终止执行的确认消息。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0319

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0319`
- Split: `documentation_03`

Input:

```text
在这种情况下，Pod 中所有剩余的容器将在某个短宽限期内被同时终止。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0326

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0326`
- Split: `documentation_03`

Input:

```text
在清理 Pod 的同时，如果它们处于非终止状态阶段，PodGC 也会将它们标记为失败。
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0336

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0336`
- Split: `documentation_03`

Input:

```text
之前设置为 `ready: true` 状态的容器仍然保持就绪。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0001

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0001`
- Split: `documentation_04`

Input:

```text
Kubernetes 中 Service 的一个关键目标是让你无需修改现有应用以使用某种不熟悉的服务发现机制。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0025

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0025`
- Split: `documentation_04`

Input:

```text
如果你想要在自己的应用中使用 Kubernetes API 进行服务发现，可以查询，寻找匹配的 EndpointSlice 对象。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0027

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0027`
- Split: `documentation_04`

Input:

```text
对于非本地应用，Kubernetes 提供了在应用和后端 Pod 之间放置网络端口或负载均衡器的方法。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0028

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0028`
- Split: `documentation_04`

Input:

```text
无论采用那种方式，你的负载都可以使用这里的服务发现机制找到希望连接的目标。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0032

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0032`
- Split: `documentation_04`

Input:

```text
例如，假定有一组 Pod，每个 Pod 都在侦听 TCP 端口 9376，并且它们还被打上 `app.kubernetes.io/name=MyApp` 标签。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0039

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0039`
- Split: `documentation_04`

Input:

```text
Service 对象的名称必须是有效的 RFC 1035 标签名称。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0040

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0040`
- Split: `documentation_04`

Input:

```text
Service 能够将任意入站 `port` 映射到某个 `targetPort`。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0041

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0041`
- Split: `documentation_04`

Input:

```text
默认情况下，出于方便考虑，`targetPort` 会被设置为与 `port` 字段相同的值。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0047

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0047`
- Split: `documentation_04`

Input:

```text
例如，你可以在后端软件的新版本中更改 Pod 公开的端口号，但不会影响到客户端。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0052

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0052`
- Split: `documentation_04`

Input:

```text
你希望在生产环境中使用外部数据库集群，但在测试环境中使用自己的数据库。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0065

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0065`
- Split: `documentation_04`

Input:

```text
如果你使用的是第三方工具，请使用全小写的工具名称，并将空格和其他标点符号更改为短划线（`-`）。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0079

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0079`
- Split: `documentation_04`

Input:

```text
在需要添加额外的端点之前，Kubernetes 不会创建新的 EndpointSlice。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0081

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0081`
- Split: `documentation_04`

Input:

```text
EndpointSlice API 是旧版 Endpoints API 的演进版本。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0088

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0088`
- Split: `documentation_04`

Input:

```text
如出现端点过多的情况，Kubernetes 选择最多 1000 个可能的后端端点存储到 Endpoints 对象中，并在 Endpoints 上设置 `endpoints.kubernetes.io/over-capacity: truncated`。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0090

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0090`
- Split: `documentation_04`

Input:

```text
请求流量仍会被发送到后端，但任何依赖旧版 Endpoints API 的负载均衡机制最多只能将流量发送到 1000 个可用的支撑端点。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0094

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0094`
- Split: `documentation_04`

Input:

```text
此字段的取值会被映射到对应的 Endpoints 和 EndpointSlice 对象中。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0110

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0110`
- Split: `documentation_04`

Input:

```text
为了让 Service 可通过节点端口访问，Kubernetes 会为 Service 配置集群 IP 地址，相当于你请求了 `type: ClusterIP` 的 Service。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0133

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0133`
- Split: `documentation_04`

Input:

```text
集群中的每个节点都将自己配置为监听所分配的端口，并将流量转发到与该 Service 关联的某个就绪端点。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0138

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0138`
- Split: `documentation_04`

Input:

```text
你还必须使用有效的端口号，该端口号在配置用于 NodePort 的范围内。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0140

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0140`
- Split: `documentation_04`

Input:

```text
当某个用于希望创建一个使用特定端口的 NodePort Service 时，该目标端口可能与另一个已经被分配的端口冲突。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0163

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0163`
- Split: `documentation_04`

Input:

```text
如果没有设置 `loadBalancerIP` 字段，平台将会给负载均衡器分配一个临时 IP。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0173

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0173`
- Split: `documentation_04`

Input:

```text
Kubernetes API 没有定义如何为 Kubernetes 托管负载均衡器实施运行状况检查，而是由云提供商（以及集成代码的实现人员）决定其行为。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0194

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0194`
- Split: `documentation_04`

Input:

```text
默认值是 "VIP"，意味着流量被传递到目的地设置为负载均衡器 IP 和端口的节点上。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0195

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0195`
- Split: `documentation_04`

Input:

```text
如果流量被传递到节点，然后 DNAT 到 Pod，则目的地将被设置为节点的 IP 和节点端口；如果流量被直接传递到 Pod，则目的地将被设置为 Pod 的 IP 和端口。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0198

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0198`
- Split: `documentation_04`

Input:

```text
在水平分割（Split-Horizon）DNS 环境中，你需要两个 Service 才能将内部和外部流量都路由到你的端点。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0200

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0200`
- Split: `documentation_04`

Input:

```text
你可以使用 `spec.externalName` 参数指定这些 Service。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0202

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0202`
- Split: `documentation_04`

Input:

```text
类似于 IPv4 地址的外部名称无法被 DNS 服务器解析。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0209

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0209`
- Split: `documentation_04`

Input:

```text
对于使用主机名的协议，这一差异可能会导致错误或意外响应。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0216

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0216`
- Split: `documentation_04`

Input:

```text
无头 Service 不使用虚拟 IP 地址和代理配置路由和数据包转发；相反，无头 Service 通过内部 DNS 记录报告各个 Pod 的端点 IP 地址，这些 DNS 记录是由集群的 DNS 服务所提供的。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0220

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0220`
- Split: `documentation_04`

Input:

```text
对没有定义选择算符的无头 Service，控制平面不会创建 EndpointSlice 对象。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0221

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0221`
- Split: `documentation_04`

Input:

```text
对于 `type: ExternalName` Service，查找和配置其 CNAME 记录；对所有其他类型的 Service，针对 Service 的就绪端点的所有 IP 地址，查找和配置 DNS A / AAAA 记录：对于 IPv4 端点，DNS 系统创建 A 记录。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0222

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0222`
- Split: `documentation_04`

Input:

```text
对于 IPv6 端点，DNS 系统创建 AAAA 记录。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0227

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0227`
- Split: `documentation_04`

Input:

```text
这里 Service 的名称被转为大写字母，横线被转换成下划线。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0237

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0237`
- Split: `documentation_04`

Input:

```text
名字空间 `my-ns` 中的 Pod 应该能够通过按名检索 `my-service` 来找到 Service （`my-service.my-ns` 也可以）。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0244

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0244`
- Split: `documentation_04`

Input:

```text
阅读虚拟 IP 和 Service 代理以了解 Kubernetes 提供的使用虚拟 IP 地址公开 Service 的机制。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0247

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0247`
- Split: `documentation_04`

Input:

```text
`.spec.trafficDistribution` 字段提供了另一种影响 Kubernetes Service 内流量路由的方法。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0260

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0260`
- Split: `documentation_04`

Input:

```text
Kubernetes 不负责管理 `externalIPs` 的分配，这一工作是集群管理员的职责。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0261

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0261`
- Split: `documentation_04`

Input:

```text
Service 是 Kubernetes REST API 中的顶级资源。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0262

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0262`
- Split: `documentation_04`

Input:

```text
你可以找到有关 Service 对象 API 的更多详细信息。
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

### kubernetes-docs-zh-cn-v1/page-04-sentence-0265

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0265`
- Split: `documentation_04`

Input:

```text
Gateway 作为 Kubernetes 的扩展提供比 Ingress 更高的灵活性。
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
