<!-- zhtw:disable -->
# Blind-v2 Source Classification 049

Packet: `benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-049.json`
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

### kubernetes-docs-zh-cn-v1/page-01-sentence-0010

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-01-sentence-0010`
- Split: `documentation_01`

Input:

```text
使用 `generateName` 时，所提供的值将作为名称前缀，服务器会在其后附加一个生成的后缀。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-02-sentence-0001

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-02-sentence-0001`
- Split: `documentation_02`

Input:

```text
`kubectl` 命令行工具支持多种不同的方式来创建和管理 Kubernetes。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-02-sentence-0016

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-02-sentence-0016`
- Split: `documentation_02`

Input:

```text
指定的文件必须包含 YAML 或 JSON 格式的对象的完整定义。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0016

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0016`
- Split: `documentation_03`

Input:

```text
例如，你可能想要定义一组 Pod，但只有在所有 Pod 都被创建完成后才会触发调度。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0023

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0023`
- Split: `documentation_03`

Input:

```text
任何给定的 Pod （由 UID 定义）从不会被“重新调度（rescheduled）”到不同的节点；相反，这一 Pod 可以被一个新的、几乎完全相同的 Pod 替换掉。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0027

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0027`
- Split: `documentation_03`

Input:

```text
如果 Pod 因为任何原因被删除，甚至某完全相同的替代 Pod 被创建时，这个相关的对象（例如这里的卷）也会被删除并重建。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0038

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0038`
- Split: `documentation_03`

Input:

```text
`Failed`（失败） | Pod 中的所有容器都已终止，并且至少有一个容器是因为失败终止。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0052

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0052`
- Split: `documentation_03`

Input:

```text
一旦将 Pod 分派给某个节点，`kubelet` 就通过开始为 Pod 创建容器。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0103

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0103`
- Split: `documentation_03`

Input:

```text
边车容器是初始化容器，无论 Pod 的 `restartPolicy` 设置如何，它们都会始终重启，因为它们拥有自己的容器级 `restartPolicy: Always` 设置。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0105

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0105`
- Split: `documentation_03`

Input:

```text
当 kubelet 根据配置的重启策略处理容器重启时，仅适用于同一 Pod 内替换容器并在同一节点上运行的重启。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0128

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0128`
- Split: `documentation_03`

Input:

```text
下面是一个重启策略为 Never 的 Pod，其中包含的容器会在遇到特定的退出码时忽略之并重启。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0163

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0163`
- Split: `documentation_03`

Input:

```text
`DisruptionTarget`：由于干扰（例如抢占、驱逐或垃圾回收），Pod 即将被终止。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0176

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0176`
- Split: `documentation_03`

Input:

```text
当 Pod 的容器都已就绪，但至少一个定制状况没有取值或者取值为 `False`， `kubelet` 将 Pod 的状况设置为 `ContainersReady`。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0188

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0188`
- Split: `documentation_03`

Input:

```text
（对于其他基础设施资源，你需要使用特定于这些资源的不同技术。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0210

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0210`
- Split: `documentation_03`

Input:

```text
使用探针来检查容器有四种不同的方法。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0256

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0256`
- Split: `documentation_03`

Input:

```text
你应该将其 `failureThreshold` 设置得足够高，以便容器有充足的时间完成启动，并且避免更改存活态探针所使用的默认值。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0294

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0294`
- Split: `documentation_03`

Input:

```text
如果需要排空正被终止的 Pod 上的流量，可以将 `serving` 状况作为实际的就绪状态。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0316

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0316`
- Split: `documentation_03`

Input:

```text
这样确保了 Sidecar 容器继续为 Pod 中的其他容器提供服务，直到完全不再需要为止。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0012

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0012`
- Split: `documentation_04`

Input:

```text
每个 Service 对象定义端点的一个逻辑集合（通常这些端点就是 Pod）以及如何访问到这些 Pod 的策略。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0066

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0066`
- Split: `documentation_04`

Input:

```text
如果直接使用 `kubectl` 之类的工具来管理 EndpointSlice 对象，请使用用来描述这种手动管理的名称，例如 `"staff"` 或 `"cluster-admins"`。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0087

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0087`
- Split: `documentation_04`

Input:

```text
由于一个 Service 可以链接到多个 EndpointSlice 之上，所以 1000 个支撑端点的限制仅影响旧版的 Endpoints API。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0092

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0092`
- Split: `documentation_04`

Input:

```text
`appProtocol` 字段提供了一种为每个 Service 端口设置应用协议的方式。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0100

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0100`
- Split: `documentation_04`

Input:

```text
为 Service 使用多个端口时，必须为所有端口提供名称，以使它们无歧义。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0117

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0117`
- Split: `documentation_04`

Input:

```text
但是，这种层层递进的形式有一个例外。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0120

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0120`
- Split: `documentation_04`

Input:

```text
其他几种 Service 类型在 `ClusterIP` 类型的基础上进行构建。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0121

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0121`
- Split: `documentation_04`

Input:

```text
如果你定义的 Service 将 `.spec.clusterIP` 设置为 `"None"`，则 Kubernetes 不会为其分配 IP 地址。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0134

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0134`
- Split: `documentation_04`

Input:

```text
通过使用合适的协议（例如 TCP）和适当的端口（分配给该 Service）连接到任何一个节点，你就能够从集群外部访问 `type: NodePort` Service。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0136

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0136`
- Split: `documentation_04`

Input:

```text
控制平面将或者为你分配该端口，或者报告 API 事务失败。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0149

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0149`
- Split: `documentation_04`

Input:

```text
kube-proxy 应视将其视为所在节点的本机地址。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0181

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0181`
- Split: `documentation_04`

Input:

```text
如果某已有 Service 已被分配节点端口，如果将其属性 `spec.allocateLoadBalancerNodePorts` 设置为 `false`，这些节点端口不会被自动释放。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0217

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0217`
- Split: `documentation_04`

Input:

```text
这些 DNS 记录是由集群内部 DNS 服务所提供的要定义无头 Service，你需要将 `.spec.type` 设置为 ClusterIP（这也是 `type` 的默认值），并进一步将 `.spec.clusterIP` 设置为 `None`。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0253

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0253`
- Split: `documentation_04`

Input:

```text
如果未设置该字段，实现将应用其默认路由策略，详见流量分发。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-005

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-005`
- Split: `article`

Input:

```text
损害财务安全，包括身份盗用。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-011

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-011`
- Split: `article`

Input:

```text
使软件应用程序和操作系统保持最新。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-013

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-013`
- Split: `article`

Input:

```text
使用密码管理器和两种验证方法。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-018

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-018`
- Split: `article`

Input:

```text
不要共享个人识别号码或密码。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-022

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-022`
- Split: `article`

Input:

```text
不要使用证书无效的网站。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-032

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-032`
- Split: `article`

Input:

```text
警惕要求提供私人信息的电子邮件和社交媒体用户。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-033

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-033`
- Split: `article`

Input:

```text
如果发现奇怪的活动，应立即更改所有互联网帐户密码，以减少损失。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-037

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-037`
- Split: `article`

Input:

```text
告诉工作单位、学校或其他系统所有者发生了什么。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-041

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-041`
- Split: `article`

Input:

```text
联系持有账户的银行、信用卡公司和其他金融服务公司。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-043

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-043`
- Split: `article`

Input:

```text
关闭任何未经授权的信用或收费账户。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-046

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-046`
- Split: `article`

Input:

```text
向联邦调查局 (FBI) 互联网犯罪投诉中心 (IC3) 提出投诉。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-050

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-050`
- Split: `article`

Input:

```text
视被盗信息情况，应联系其他适当机构。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-052

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-052`
- Split: `article`

Input:

```text
向当地的美国特勤局 (USSS) 电子犯罪特别工作组或互联网犯罪投诉中心报告在线犯罪或欺诈行为。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-053

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-053`
- Split: `article`

Input:

```text
国家网络安全联盟，一个非营利组织，致力于打造更安全的互联世界。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-002

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-002`
- Split: `article`

Input:

```text
在某些情况下，各位可能有一两天的时间准备，而其他情况可能需要立即疏散。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-006

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-006`
- Split: `article`

Input:

```text
向当地官员了解今年有哪些避难所的名额。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-010

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-010`
- Split: `article`

Input:

```text
大多数公共庇护所只允许服务性动物。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-015

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-015`
- Split: `article`

Input:

```text
准备一个“行囊”，当步行或乘坐公共交通工具撤离时可以携带，如果你有车，则准备好长距离旅行的用品。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-023

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-023`
- Split: `article`

Input:

```text
收听电池供电的收音机，遵守当地的疏散指示。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-024

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-024`
- Split: `article`

Input:

```text
带上应急用品包。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-027

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-027`
- Split: `article`

Input:

```text
现在就计划在紧急情况下如何照顾自己的宠物。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-028

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-028`
- Split: `article`

Input:

```text
如果时间允许：依照家庭通讯计划中的州外联系人打电话或发电子邮件。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-031

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-031`
- Split: `article`

Input:

```text
拔掉收音机、电视和小家电等电器设备的插头。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-036

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-036`
- Split: `article`

Input:

```text
向可能需要搭车的邻居查询。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-042

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-042`
- Split: `article`

Input:

```text
如果要返回受灾地区，在重大事件发生后，要为日常活动的中断做好准备，并记住在风暴废墟被清理之前返回家园是很危险的。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-044

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-044`
- Split: `article`

Input:

```text
为设备充电，并考虑购买备用电池，以防继续停电。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-045

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-045`
- Split: `article`

Input:

```text
加满油箱，并考虑下载一个燃料应用程序，以检查沿途的停电情况。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-049

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-049`
- Split: `article`

Input:

```text
只在室外使用发电机，并远离家，千万不要在家里或车库里运行发电机或将其连接到家庭电气系统。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-kids-tornadoes-zh-hans-v1/sentence-006

- Source: `ready-gov-kids-tornadoes-zh-hans-v1`
- Source case: `sentence-006`
- Split: `article`

Input:

```text
龙卷风警告：龙卷风警告意味着已经发现龙卷风，或者多普勒雷达显示可能引发龙卷风的雷暴环流。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-kids-tornadoes-zh-hans-v1/sentence-008

- Source: `ready-gov-kids-tornadoes-zh-hans-v1`
- Source case: `sentence-008`
- Split: `article`

Input:

```text
漏斗云：一种长云形状，顶部较宽，底部较细，像冰淇淋甜筒。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-kids-tornadoes-zh-hans-v1/sentence-013

- Source: `ready-gov-kids-tornadoes-zh-hans-v1`
- Source case: `sentence-013`
- Split: `article`

Input:

```text
春季，该地区转移到德克萨斯州中北部和俄克拉荷马州。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-kids-tornadoes-zh-hans-v1/sentence-037

- Source: `ready-gov-kids-tornadoes-zh-hans-v1`
- Source case: `sentence-037`
- Split: `article`

Input:

```text
如果已经损坏，请远离并听从成人的指示。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-001

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-001`
- Split: `project_original`

Input:

```text
委员会将在公开会议中审议这项修正草案。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-003

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-003`
- Split: `project_original`

Input:

```text
地方政府公布下一年度公共建设预算。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-004

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-004`
- Split: `project_original`

Input:

```text
调查小组核对访谈记录与现场照片。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-005

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-005`
- Split: `project_original`

Input:

```text
法院裁定原处分应由原机关重新审查。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-007

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-007`
- Split: `project_original`

Input:

```text
新闻稿说明补助申请期限延长两周。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-015

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-015`
- Split: `project_original`

Input:

```text
评选结果将在异议处理完成后公告。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-018

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-018`
- Split: `project_original`

Input:

```text
财政部门说明税收估算采用的基准。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-021

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-021`
- Split: `project_original`

Input:

```text
农业部门评估连续降雨造成的损失。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-022

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-022`
- Split: `project_original`

Input:

```text
公告提醒投标厂商检查资格文件。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-023

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-023`
- Split: `project_original`

Input:

```text
调查结果显示通勤时间较去年增加。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-024

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-024`
- Split: `project_original`

Input:

```text
文化机构将修复工程分成三个阶段。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-033

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-033`
- Split: `project_original`

Input:

```text
审查意见要求统一图表的计算口径。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-039

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-039`
- Split: `project_original`

Input:

```text
公听会资料已上传至机关网站。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-044

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-044`
- Split: `project_original`

Input:

```text
调查报告区分事实认定与改进建议。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-045

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-045`
- Split: `project_original`

Input:

```text
申请资料缺少签章时应通知限期补正。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-048

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-048`
- Split: `project_original`

Input:

```text
机关将定期检核公开资料是否完整。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-002

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-002`
- Split: `project_original`

Input:

```text
系统会在回答前检查引用来源是否存在。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-003

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-003`
- Split: `project_original`

Input:

```text
使用者可以要求重新生成较精简的版本。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-007

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-007`
- Split: `project_original`

Input:

```text
模型无法确认时应明确表达不确定性。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-012

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-012`
- Split: `project_original`

Input:

```text
分类器将低信心案例交由人工复核。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-014

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-014`
- Split: `project_original`

Input:

```text
回应需要符合使用者指定的语言与地区。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-017

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-017`
- Split: `project_original`

Input:

```text
评测人员只会看到去除产品名称的输出。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-019

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-019`
- Split: `project_original`

Input:

```text
对话太长时系统会压缩较早的消息。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-023

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-023`
- Split: `project_original`

Input:

```text
系统会检查结构化输出是否符合格式。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-026

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-026`
- Split: `project_original`

Input:

```text
安全过滤器可能要求提供额外说明。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-027

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-027`
- Split: `project_original`

Input:

```text
助理可以先提出一个必要的澄清问题。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-029

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-029`
- Split: `project_original`

Input:

```text
标注人员按照统一准则判断回答品质。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-036

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-036`
- Split: `project_original`

Input:

```text
评测器会检查答案是否遗漏否定语意。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-039

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-039`
- Split: `project_original`

Input:

```text
助理必须遵守对话中较高优先级的规则。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-041

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-041`
- Split: `project_original`

Input:

```text
模型应确认表格中的单位与栏位名称。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-042

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-042`
- Split: `project_original`

Input:

```text
评测人员会记录错误发生的主要原因。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-049

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-049`
- Split: `project_original`

Input:

```text
系统会在发布前移除内部审查备注。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```
