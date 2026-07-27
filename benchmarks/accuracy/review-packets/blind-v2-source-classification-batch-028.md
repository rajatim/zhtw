<!-- zhtw:disable -->
# Blind-v2 Source Classification 028

Packet: `benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-028.json`
Cases: 90
Seed: `20260719`
Selection: `balanced-remaining-deterministic-sha256-v1`

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

### kubernetes-docs-zh-cn-v1/page-01-sentence-0001

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-01-sentence-0001`
- Split: `documentation_01`

Input:

```text
集群中的每一个都有一个名称来标识在同类资源中的唯一性。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-01-sentence-0017

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-01-sentence-0017`
- Split: `documentation_01`

Input:

```text
某些资源类型需要其名称遵循 RFC 1123 所定义的 DNS 标签标准。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-01-sentence-0019

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-01-sentence-0019`
- Split: `documentation_01`

Input:

```text
尽管 RFC 1123 在技术上允许标签以数字开头，当前的 Kubernetes 实现要求 RFC 1035 和 RFC 1123 标签都以字母字符开头。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-01-sentence-0022

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-01-sentence-0022`
- Split: `documentation_01`

Input:

```text
换句话说，其名称不能是 `.`、`..`，也不可以包含 `/` 或 `%` 这些字符。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-02-sentence-0023

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-02-sentence-0023`
- Split: `documentation_02`

Input:

```text
对象配置提供了用于创建新对象的模板。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-02-sentence-0030

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-02-sentence-0030`
- Split: `documentation_02`

Input:

```text
使用声明式对象配置时，用户对本地存储的对象配置文件进行操作，但是用户未定义要对该文件执行的操作。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-02-sentence-0034

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-02-sentence-0034`
- Split: `documentation_02`

Input:

```text
可以通过使用 `patch` API 操作仅写入观察到的差异，而不是使用 `replace` API 操作来替换整个对象配置来实现。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-02-sentence-0039

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-02-sentence-0039`
- Split: `documentation_02`

Input:

```text
使用 diff 产生的部分更新会创建复杂的合并和补丁操作。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0001

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0001`
- Split: `documentation_03`

Input:

```text
本页面讲述 Pod 的生命周期。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0015

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0015`
- Split: `documentation_03`

Input:

```text
你可以使用 Pod 调度就绪态来延迟 Pod 的调度，直到所有的调度门控都被移除。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0037

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0037`
- Split: `documentation_03`

Input:

```text
`Succeeded`（成功） | Pod 中的所有容器都已成功结束，并且不会再重启。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0044

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0044`
- Split: `documentation_03`

Input:

```text
确保不要将 Status（kubectl 用于用户直觉的显示字段）与 Pod 的 `phase` 混淆。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0045

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0045`
- Split: `documentation_03`

Input:

```text
Pod 阶段（phase）是 Kubernetes 数据模型和 Pod API 的一个明确的部分。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0054

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0054`
- Split: `documentation_03`

Input:

```text
要检查 Pod 中容器的状态，你可以使用 `kubectl describe pod `。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0061

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0061`
- Split: `documentation_03`

Input:

```text
如果你使用 `kubectl` 来查询包含 `Running` 状态的容器的 Pod 时，你也会看到关于容器进入 `Running` 状态的信息。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0065

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0065`
- Split: `documentation_03`

Input:

```text
Kubernetes 通过在 Pod `spec` 中定义的 `restartPolicy` 管理 Pod 内容器出现的失效。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0079

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0079`
- Split: `documentation_03`

Input:

```text
容器的存活探针或者启动探针返回 `失败` 结果，如探针部分所述。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0084

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0084`
- Split: `documentation_03`

Input:

```text
检查资源限制：确保容器被分配了足够的 CPU 和内存。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0085

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0085`
- Split: `documentation_03`

Input:

```text
有时，增加 Pod 定义中的资源可以解决问题。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0086

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0086`
- Split: `documentation_03`

Input:

```text
调试应用程序：应用程序代码中可能存在错误或配置不当。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0087

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0087`
- Split: `documentation_03`

Input:

```text
在本地或开发环境中运行此容器镜像有助于诊断应用程序的特定问题。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0091

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0091`
- Split: `documentation_03`

Input:

```text
Kubernetes 项目建议遵循云原生原则，包括能够应对未预告或随意重启的弹性设计。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0093

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0093`
- Split: `documentation_03`

Input:

```text
无论哪种方式，都有助于确保即使在部分故障的情况下，你的整体工作负载依然保持可用。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0099

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0099`
- Split: `documentation_03`

Input:

```text
`OnFailure`：只有在容器错误退出（退出状态非零）时才重新启动容器。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0109

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0109`
- Split: `documentation_03`

Input:

```text
如果你的集群启用了 `ContainerRestartRules` 特性门控，你可以针对单个容器指定 `restartPolicy` 和 `restartPolicyRules` 来覆盖 Pod 重启策略。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0116

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0116`
- Split: `documentation_03`

Input:

```text
此外，单个容器可以指定 `restartPolicyRules`。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0118

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0118`
- Split: `documentation_03`

Input:

```text
`restartPolicyRules` 定义了一系列在容器退出时应用的规则。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0127

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0127`
- Split: `documentation_03`

Input:

```text
如果 Init 容器失败，则 Pod 也会失败。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0129

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0129`
- Split: `documentation_03`

Input:

```text
重启规则可用于许多其他高级的生命周期管理场景。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0144

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0144`
- Split: `documentation_03`

Input:

```text
边车容器可以监控主应用的健康状态，如果该应用进入不可恢复的状态，则触发整个 Pod 重启。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0145

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0145`
- Split: `documentation_03`

Input:

```text
考虑一种工作负载，其中 watcher 边车负责在主应用出错时从已知良好状态重启主应用。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0147

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0147`
- Split: `documentation_03`

Input:

```text
`watcher-sidecar` 执行命令后以退出码 `88` 退出。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0150

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0150`
- Split: `documentation_03`

Input:

```text
Pod 保留其 UID、沙箱、IP 和卷。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0177

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0177`
- Split: `documentation_03`

Input:

```text
在其早期开发过程中，这种状况被命名为 `PodHasNetwork`。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0205

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0205`
- Split: `documentation_03`

Input:

```text
考虑使用 PodDisruptionBudget 来控制可用性。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0215

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0215`
- Split: `documentation_03`

Input:

```text
如果响应的状态是 "SERVING"，则认为诊断成功。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0217

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0217`
- Split: `documentation_03`

Input:

```text
如果响应的状态码大于等于 200 且小于 400，则诊断被认为是成功的。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0221

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0221`
- Split: `documentation_03`

Input:

```text
如果远程系统（容器）在打开连接后立即将其关闭，这算作是健康的。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0222

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0222`
- Split: `documentation_03`

Input:

```text
和其他机制不同，`exec` 探针的实现涉及每次执行时创建/复制多个进程。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0232

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0232`
- Split: `documentation_03`

Input:

```text
控制器将从与该 Pod 匹配的所有 Service 的 EndpointSlice 中删除该 Pod 的 IP 地址。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0235

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0235`
- Split: `documentation_03`

Input:

```text
`startupProbe` : 指示容器中的应用是否已经启动。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0242

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0242`
- Split: `documentation_03`

Input:

```text
如果要仅在探测成功时才开始向 Pod 发送请求流量，请指定就绪态探针。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0257

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0257`
- Split: `documentation_03`

Input:

```text
这一设置有助于减少死锁状况的发生。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0271

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0271`
- Split: `documentation_03`

Input:

```text
如果启用了 `ContainerStopSignals` 特性门控（feature gate），你可以通过容器的生命周期（Lifecycle）配置自定义的终止信号。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0303

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0303`
- Split: `documentation_03`

Input:

```text
默认情况下，所有的删除操作都会附有 30 秒钟的宽限期限。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0310

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0310`
- Split: `documentation_03`

Input:

```text
在节点侧，被设置为立即终止的 Pod 仍然会在被强行杀死之前获得一点点的宽限时间。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0320

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0320`
- Split: `documentation_03`

Input:

```text
同样地，如果 Pod 有一个 `preStop` 钩子超过了终止宽限期，可能会发生紧急终止。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0325

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0325`
- Split: `documentation_03`

Input:

```text
孤儿 Pod - 绑定到不再存在的节点，计划外终止的 Pod 终止过程中的 Pod，绑定到有 `node.kubernetes.io/out-of-service` 污点的未就绪节点。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0327

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0327`
- Split: `documentation_03`

Input:

```text
此外，PodGC 在清理孤儿 Pod 时会添加 Pod 干扰状况。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0347

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0347`
- Split: `documentation_03`

Input:

```text
进一步了解 Sidecar 容器。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0026

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0026`
- Split: `documentation_04`

Input:

```text
只要 Service 中的 Pod 集合发生变化，Kubernetes 就会为其更新 EndpointSlice。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0036

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0036`
- Split: `documentation_04`

Input:

```text
Kubernetes 为该 Service 分配一个 IP 地址（称为“集群 IP”），供虚拟 IP 地址机制使用。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0043

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0043`
- Split: `documentation_04`

Input:

```text
启用该特性后，Service 对象的名称必须符合 RFC 1123 标签名称的规范。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0048

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0048`
- Split: `documentation_04`

Input:

```text
Service 的默认协议是 TCP；你还可以使用其他受支持的任何协议。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0049

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0049`
- Split: `documentation_04`

Input:

```text
由于许多 Service 需要公开多个端口，所以 Kubernetes 为同一 Service 定义多个端口。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0053

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0053`
- Split: `documentation_04`

Input:

```text
你希望让你的 Service 指向另一个中或其它集群中的 Service。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0069

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0069`
- Split: `documentation_04`

Input:

```text
在没有选择算符的 Service 示例中，流量被路由到 EndpointSlice 清单中定义的两个端点之一：通过 TCP 协议连接到 10.1.2.3 或 10.4.5.6 的端口 9376。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0070

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0070`
- Split: `documentation_04`

Input:

```text
Kubernetes API 服务器不允许将流量代理到未被映射至 Pod 上的端点。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0071

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0071`
- Split: `documentation_04`

Input:

```text
由于此约束，当 Service 没有选择算符时，诸如 `kubectl port-forward service/ forwardedPort:servicePort` 之类的操作将会失败。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0072

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0072`
- Split: `documentation_04`

Input:

```text
这可以防止 Kubernetes API 服务器被用作调用者可能无权访问的端点的代理。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0074

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0074`
- Split: `documentation_04`

Input:

```text
更多的相关信息，请参阅 ExternalName 一节。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0075

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0075`
- Split: `documentation_04`

Input:

```text
EndpointSlice 对象表示某个 Service 的后端网络端点的子集（切片）。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0076

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0076`
- Split: `documentation_04`

Input:

```text
你的 Kubernetes 集群会跟踪每个 EndpointSlice 所表示的端点数量。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0085

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0085`
- Split: `documentation_04`

Input:

```text
Kubernetes 限制单个 Endpoints 对象中可以容纳的端点数量。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0086

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0086`
- Split: `documentation_04`

Input:

```text
当一个 Service 拥有 1000 个以上支撑端点时，Kubernetes 会截断 Endpoints 对象中的数据。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0091

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0091`
- Split: `documentation_04`

Input:

```text
这一 API 限制也意味着你不能手动将 Endpoints 更新为拥有超过 1000 个端点。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0096

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0096`
- Split: `documentation_04`

Input:

```text
IANA 标准服务名称。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0112

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0112`
- Split: `documentation_04`

Input:

```text
Kubernetes 不直接提供负载均衡组件；你必须提供一个，或者将你的 Kubernetes 集群与某个云平台集成。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0119

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0119`
- Split: `documentation_04`

Input:

```text
此默认 Service 类型从你的集群中为此预留的 IP 地址池中分配一个 IP 地址。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0126

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0126`
- Split: `documentation_04`

Input:

```text
如果你尝试创建一个带有非法 `clusterIP` 地址值的 Service，API 服务器会返回 HTTP 状态码 422，表示值不合法。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0135

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0135`
- Split: `documentation_04`

Input:

```text
如果需要特定的端口号，你可以在 `nodePort` 字段中指定一个值。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0146

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0146`
- Split: `documentation_04`

Input:

```text
如果每个节点都连接到多个网络（例如：一个网络用于应用流量，另一网络用于节点和控制平面之间的流量），你可能想要这样做。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0158

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0158`
- Split: `documentation_04`

Input:

```text
要实现 `type: LoadBalancer` 的服务，Kubernetes 通常首先进行与请求 `type: NodePort` 服务类似的更改。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0160

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0160`
- Split: `documentation_04`

Input:

```text
你可以将负载均衡 Service 配置为忽略分配节点端口，前提是云平台实现支持这点。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0162

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0162`
- Split: `documentation_04`

Input:

```text
这时，平台将使用用户指定的 `loadBalancerIP` 来创建负载均衡器。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0167

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0167`
- Split: `documentation_04`

Input:

```text
它也不支持双协议栈联网。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0172

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0172`
- Split: `documentation_04`

Input:

```text
负载均衡器运行状态检查对于现代应用程序至关重要，它们用于确定负载均衡器应将流量分派到哪个服务器（虚拟机或 IP 地址）。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0174

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0174`
- Split: `documentation_04`

Input:

```text
负载均衡器运行状态检查广泛用于支持 Service 的 `externalTrafficPolicy` 字段。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0179

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0179`
- Split: `documentation_04`

Input:

```text
这仅适用于负载均衡器的实现能够直接将流量路由到 Pod 而不是使用节点端口的情况。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0186

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0186`
- Split: `documentation_04`

Input:

```text
所有默认的负载均衡器实现（例如，由云平台所提供的）都会忽略设置了此字段的 Service。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0187

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0187`
- Split: `documentation_04`

Input:

```text
`.spec.loadBalancerClass` 只能设置到类型为 `LoadBalancer` 的 Service 之上，而且一旦设置之后不可变更。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0188

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0188`
- Split: `documentation_04`

Input:

```text
`.spec.loadBalancerClass` 的值必须是一个标签风格的标识符，可以有选择地带有类似 "`internal-vip`" 或 "`example.com/internal-vip`" 这类前缀。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0189

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0189`
- Split: `documentation_04`

Input:

```text
没有前缀的名字是保留给最终用户的。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0211

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0211`
- Split: `documentation_04`

Input:

```text
有时你并不需要负载均衡，也不需要单独的 Service IP。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0232

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0232`
- Split: `documentation_04`

Input:

```text
你可以阅读 makeLinkVariables 来了解这是如何在 Kubernetes 中实现的。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0236

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0236`
- Split: `documentation_04`

Input:

```text
例如，如果你在 Kubernetes 命名空间 `my-ns` 中有一个名为 `my-service` 的 Service，则控制平面和 DNS 服务共同为 `my-service.my-ns` 生成 DNS 记录。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0239

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0239`
- Split: `documentation_04`

Input:

```text
这些名称将解析为分配给 Service 的集群 IP。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0240

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0240`
- Split: `documentation_04`

Input:

```text
Kubernetes 还支持命名端口的 DNS SRV（Service）记录。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0256

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0256`
- Split: `documentation_04`

Input:

```text
如果有外部 IP 能够路由到一个或多个集群节点上，则 Kubernetes Service 可以在这些 `externalIPs` 上公开出去。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0264

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0264`
- Split: `documentation_04`

Input:

```text
Ingress 负责将来自集群外部的 HTTP 和 HTTPS 请求路由给集群内的 Service。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```
