<!-- zhtw:disable -->
# Blind-v2 Source Classification 053

Packet: `benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-053.json`
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

### kubernetes-docs-zh-cn-v1/page-01-sentence-0003

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-01-sentence-0003`
- Split: `documentation_01`

Input:

```text
比如，在同一个名字空间中只能有一个名为 `myapp-1234` 的 Pod，但是可以命名一个 Pod 和一个 Deployment 同为 `myapp-1234`。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-01-sentence-0014

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-01-sentence-0014`
- Split: `documentation_01`

Input:

```text
很多资源类型需要可以用作 DNS 子域名的名称。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-01-sentence-0015

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-01-sentence-0015`
- Split: `documentation_01`

Input:

```text
DNS 子域名的定义可参见 RFC 1123。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-02-sentence-0018

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-02-sentence-0018`
- Split: `documentation_02`

Input:

```text
`replace` 指令式命令将现有规范替换为新提供的规范，并放弃对配置文件中缺少的对象的所有更改。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0007

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0007`
- Split: `documentation_03`

Input:

```text
在 Pod 内部，Kubernetes 跟踪不同容器的状态并确定使 Pod 重新变得健康所需要采取的动作。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0011

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0011`
- Split: `documentation_03`

Input:

```text
Pod 在其生命周期中只会被调度一次。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0021

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0021`
- Split: `documentation_03`

Input:

```text
Pod 无法在因节点资源耗尽或者节点维护而被期间继续存活。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0083

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0083`
- Split: `documentation_03`

Input:

```text
审查配置：确保 Pod 配置正确无误，包括环境变量和挂载卷，并且所有必需的外部资源都可用。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0101

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0101`
- Split: `documentation_03`

Input:

```text
Deployment 通常使用 `restartPolicy: Always`（唯一允许的值）来保持应用程序持续运行。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0102

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0102`
- Split: `documentation_03`

Input:

```text
Job 通常使用 `restartPolicy: OnFailure` 或 `restartPolicy: Never` 来妥善处理批处理作业。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0115

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0115`
- Split: `documentation_03`

Input:

```text
`Never`：不自动重启已终止的容器。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0132

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0132`
- Split: `documentation_03`

Input:

```text
如果你的集群已启用特性门控 `RestartAllContainersOnContainerExits`，你可以在容器级别的 `restartPolicyRules` 中指定 `RestartAllContainers` 作为一个动作。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0162

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0162`
- Split: `documentation_03`

Input:

```text
`PodScheduled`：Pod 已经被调度到某节点； `PodReadyToStartContainers`：Pod 沙箱被成功创建并且配置了网络（Beta 特性，默认启用）； `ContainersReady`：Pod 中所有容器都已就绪； `Initialized`：所有的 Init 容器都已成功完成； `Ready`：Pod 可以为请求提供服务，并且应该被添加到对应服务的负载均衡池中。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0168

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0168`
- Split: `documentation_03`

Input:

```text
要使用这一特性，可以设置 Pod 规约中的 `readinessGates` 列表，为 kubelet 提供一组额外的状况供其评估 Pod 就绪态时使用。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0199

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0199`
- Split: `documentation_03`

Input:

```text
有关执行原地调整大小的详细说明，请参见调整分配给容器的 CPU 和内存资源。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0207

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0207`
- Split: `documentation_03`

Input:

```text
你也可以使用 VerticalPodAutoscaler 来自动管理 Pod 资源建议和更新。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0229

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0229`
- Split: `documentation_03`

Input:

```text
如果存活态探测失败，则 kubelet 会杀死容器，并且容器将根据其重启策略决定未来。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0269

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0269`
- Split: `documentation_03`

Input:

```text
用于终止容器的终止信号可以通过容器镜像中的 `STOPSIGNAL` 指令进行定义。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0270

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0270`
- Split: `documentation_03`

Input:

```text
如果镜像中未定义终止信号，容器运行时（containerd 和 CRI-O 都是 SIGTERM）会使用默认的终止信号来终止容器。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0297

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0297`
- Split: `documentation_03`

Input:

```text
容器运行时会向 Pod 中所有容器内仍在运行的进程发送 `SIGKILL` 信号。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0323

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0323`
- Split: `documentation_03`

Input:

```text
Pod 的垃圾收集器（PodGC）是控制平面的控制器，它会在 Pod 个数超出所配置的阈值（根据 `kube-controller-manager` 的 `terminated-pod-gc-threshold` 设置）时删除已终止的 Pod（阶段值为 `Succeeded` 或 `Failed`）。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0328

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0328`
- Split: `documentation_03`

Input:

```text
参阅 Pod 干扰状况了解更多详情。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0332

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0332`
- Split: `documentation_03`

Input:

```text
当 kubelet 启动时，它会检查是否已经存在一个绑定了 Pod 的 Node。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0339

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0339`
- Split: `documentation_03`

Input:

```text
Pod 级别的驱逐是在控制平面因心跳失败而将节点标记为 `node.kubernetes.io/not-ready` 之后发生的。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0062

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0062`
- Split: `documentation_04`

Input:

```text
端点 IP 地址不能是其他 Kubernetes 服务的集群 IP，因为不支持将虚拟 IP 作为目标地址。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0064

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0064`
- Split: `documentation_04`

Input:

```text
如果你创建自己的控制器代码来管理 EndpointSlice，请考虑使用类似于 `"my-domain.example/name-of-controller"` 的值。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0099

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0099`
- Split: `documentation_04`

Input:

```text
Kubernetes 允许你为 Service 对象配置多个端口定义。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0177

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0177`
- Split: `documentation_04`

Input:

```text
可用于负载均衡 Service 的协议集合由你的云平台决定，他们可能在 Kubernetes API 强制执行的限制之外另加一些约束。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0205

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0205`
- Split: `documentation_04`

Input:

```text
访问 `my-service` 的方式与访问其他 Service 的方式相同，主要区别在于重定向发生在 DNS 级别，而不是通过代理或转发来完成。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0213

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0213`
- Split: `documentation_04`

Input:

```text
你可以使用无头 Service 与其他服务发现机制交互，而不必绑定到 Kubernetes 的实现。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0218

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0218`
- Split: `documentation_04`

Input:

```text
字符串值 None 是一种特殊情况，与未设置 `.spec.clusterIP` 字段不同。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0230

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0230`
- Split: `documentation_04`

Input:

```text
如果仅使用 DNS 来发现 Service 的集群 IP，则无需担心此顺序问题。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-008

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-008`
- Split: `guide`

Input:

```text
在本文件中，您将学习有关灾难发生之前，期间和之后的一般备灾技巧，以及关于针对特定灾难特定灾难（例如飓风、地震和行凶的枪手）的备灾决策方面的最佳做法。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-029

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-029`
- Split: `guide`

Input:

```text
确定您的风险有很多不同类型的灾难和危害。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-056

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-056`
- Split: `guide`

Input:

```text
特定危害的关键防护措施根据危险情况，应采取的保护措施有所不同。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-064

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-064`
- Split: `guide`

Input:

```text
将电子设备静音，锁上或堵住门，关闭百叶窗，然后关灯。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-065

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-065`
- Split: `guide`

Input:

```text
不要成群结队地躲在一起，沿墙壁散开或单独躲藏。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-072

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-072`
- Split: `guide`

Input:

```text
良好的藏身之处包括：无窗房间，带锁的实心门后面、书桌下或重型家具后面。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-073

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-073`
- Split: `guide`

Input:

```text
保持双手可见，并保持空手。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-089

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-089`
- Split: `guide`

Input:

```text
使用加密的（安全）互联网通信。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-113

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-113`
- Split: `guide`

Input:

```text
如果在户外，寻找阴凉的地方。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-163

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-163`
- Split: `guide`

Input:

```text
次好的保护措施是在坚固建筑物不会受到洪水侵袭的最底层小型室内无窗房间。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-199

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-199`
- Split: `guide`

Input:

```text
在您的家里和办公室中保留一个24小时应急用品箱。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-211

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-211`
- Split: `guide`

Input:

```text
当外出到公共场合时，请穿戴口罩以遮住口鼻。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-214

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-214`
- Split: `guide`

Input:

```text
如果您有依赖于电力的医疗设备或辅助技术设备以维持生命，请制定备份计划，包括搬迁计划。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-219

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-219`
- Split: `guide`

Input:

```text
如果用汽车给设备充电，请不要让汽车在车库，半封闭的空间或靠近家中运行，以免一氧化碳中毒。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-242

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-242`
- Split: `guide`

Input:

```text
雷电风暴期间，避免开自来水或使用固定电话。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-268

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-268`
- Split: `guide`

Input:

```text
海啸过后，只有在当局告知安全时，才可以返回家园或进入遭受淹水破坏的建筑物。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-271

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-271`
- Split: `guide`

Input:

```text
如果当局下达疏散令，请立即从火山区撤离，以避免飞扬的碎屑、热气、侧向爆炸和熔岩流。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-284

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-284`
- Split: `guide`

Input:

```text
与邻居一起清除灌木丛和灌木树冠。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-325

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-325`
- Split: `guide`

Input:

```text
此外，了解学校是否做好就地避难的准备，是否有指定的撤离地点，以及是否有计划让家庭团聚。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-335

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-335`
- Split: `guide`

Input:

```text
确保家中的每个人都知道在不同类型的灾难中应该去哪里。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-352

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-352`
- Split: `guide`

Input:

```text
除非有水灾风险，否则不要拔掉冰柜和冰箱的电源插头。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-385

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-385`
- Split: `guide`

Input:

```text
丢掉任何过期或膨胀、凹陷或腐蚀的罐头食品。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-396

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-396`
- Split: `guide`

Input:

```text
一旦收集好了您的财务、法律和联系人信息，重要的是要对其进行保护。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-412

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-412`
- Split: `guide`

Input:

```text
了解您的保险选择并记录财产了解您的保险需求是为自己和家人为灾难做好准备的重要步骤。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-416

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-416`
- Split: `guide`

Input:

```text
房屋保险和租房保险通常为您提供以下方面的保障： • 住宅住宅—承保您的房屋。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-422

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-422`
- Split: `guide`

Input:

```text
保险业将火灾或盗窃等损失的起因称之为“危险”。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-485

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-485`
- Split: `guide`

Input:

```text
VOAD是一个团体组织，这些团体将与灾难相关的工作列为优先事项，并志愿在灾后帮助社区。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-490

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-490`
- Split: `guide`

Input:

```text
F E M A 的青年备灾项目为年轻人提供了参与社区备灾的步骤。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-492

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-492`
- Split: `guide`

Input:

```text
一旦为自己和家人做好准备，就可以作为备灾工作的领导者。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-519

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-519`
- Split: `guide`

Input:

```text
可能需要让电工检查线路。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-542

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-542`
- Split: `guide`

Input:

```text
在您和保险公司同意损失赔偿金额，并且保险公司收到您完整准确和签名的损失证明之后，您将会收到索赔付款。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-555

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-555`
- Split: `guide`

Input:

```text
地志愿组织在内的许多组织都可以直接提供食物、住所、物资用品和清洁工作方面的直接帮助。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-001

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-001`
- Split: `project_original`

Input:

```text
调查报告逐项列出证据来源及查证日期。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-002

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-002`
- Split: `project_original`

Input:

```text
委员会要求会议记录保留不同意见的完整理由。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-007

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-007`
- Split: `project_original`

Input:

```text
新闻稿引用的数字应与附件表格保持一致。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-009

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-009`
- Split: `project_original`

Input:

```text
地方政府公布预算调整前后的项目差异。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-013

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-013`
- Split: `project_original`

Input:

```text
机关复核后更正先前公告中的计算错误。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-021

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-021`
- Split: `project_original`

Input:

```text
年度报告比较计划目标与实际执行结果。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-024

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-024`
- Split: `project_original`

Input:

```text
研究结论不得超出样本资料能够支持的范围。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-025

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-025`
- Split: `project_original`

Input:

```text
机关收到陈情后建立案件编号并记录处理进度。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-026

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-026`
- Split: `project_original`

Input:

```text
稽核人员检查系统日志是否对应实际操作。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-032

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-032`
- Split: `project_original`

Input:

```text
法院文件依卷宗编号排列证物清单。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-035

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-035`
- Split: `project_original`

Input:

```text
检验报告注明仪器型号与校正有效期限。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-036

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-036`
- Split: `project_original`

Input:

```text
记者要求机关提供数字计算的原始依据。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-037

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-037`
- Split: `project_original`

Input:

```text
评估报告区分短期效果与长期影响。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-044

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-044`
- Split: `project_original`

Input:

```text
复查人员发现两份附件使用不同统计期间。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-046

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-046`
- Split: `project_original`

Input:

```text
主管机关将保存每次资料修订的历史版本。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-049

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-049`
- Split: `project_original`

Input:

```text
承办人员以书面方式确认联络窗口变更。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-001

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-001`
- Split: `project_original`

Input:

```text
模型回答时应附上能够支持结论的来源。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-002

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-002`
- Split: `project_original`

Input:

```text
检索系统必须保留文件标题与发布日期。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-010

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-010`
- Split: `project_original`

Input:

```text
回答需要区分直接证据与间接推测。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-013

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-013`
- Split: `project_original`

Input:

```text
评测资料不会包含预先生成的参考答案。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-016

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-016`
- Split: `project_original`

Input:

```text
系统发现来源互相冲突时会提示人工复核。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-017

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-017`
- Split: `project_original`

Input:

```text
助理需要说明计算结果使用了哪些输入值。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-021

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-021`
- Split: `project_original`

Input:

```text
系统不应自动改写引文中的专有名词。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-023

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-023`
- Split: `project_original`

Input:

```text
检索器会排除没有权限读取的资料片段。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-025

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-025`
- Split: `project_original`

Input:

```text
系统会检查引用连结是否指向原始来源。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-026

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-026`
- Split: `project_original`

Input:

```text
模型应保留代码范例中的参数名称与大小写。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-028

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-028`
- Split: `project_original`

Input:

```text
对话记录会保存使用者修正模型的内容。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-039

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-039`
- Split: `project_original`

Input:

```text
系统不得使用隐藏测试资料调整模型输出。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-042

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-042`
- Split: `project_original`

Input:

```text
助理应确认同名文件是否来自不同资料夹。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-045

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-045`
- Split: `project_original`

Input:

```text
回答若省略资料应说明省略的选择标准。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-047

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-047`
- Split: `project_original`

Input:

```text
助理需要核对图表标题与资料栏位是否相符。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-048

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-048`
- Split: `project_original`

Input:

```text
系统会阻止未确认的内容进入正式报告。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```
