<!-- zhtw:disable -->
# Blind-v2 Source Classification 050

Packet: `benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-050.json`
Cases: 80
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

### kubernetes-docs-zh-cn-v1/page-01-sentence-0016

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-01-sentence-0016`
- Split: `documentation_01`

Input:

```text
当启用 `RelaxedServiceNameValidation` 特性门控时， Service 对象名称可以以数字开头。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-01-sentence-0020

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-01-sentence-0020`
- Split: `documentation_01`

Input:

```text
例外情况是当为 Service 对象启用了 `RelaxedServiceNameValidation` 特性门控时，这允许 Service 名称以数字开头。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-02-sentence-0015

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-02-sentence-0015`
- Split: `documentation_02`

Input:

```text
在指令式对象配置中，kubectl 命令指定操作（创建，替换等），可选标志和至少一个文件名。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-02-sentence-0025

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-02-sentence-0025`
- Split: `documentation_02`

Input:

```text
对象配置需要额外的步骤来编写 YAML 文件。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0019

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0019`
- Split: `documentation_03`

Input:

```text
然而，Pod 也可能以集群无法恢复的方式失败，在这种情况下，Kubernetes 不会进一步尝试修复 Pod；相反，Kubernetes 会删除 Pod 并依赖其他组件提供自动修复。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0055

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0055`
- Split: `documentation_03`

Input:

```text
其输出中包含 Pod 中每个容器的状态。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0072

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0072`
- Split: `documentation_03`

Input:

```text
当 Pod 中的容器无法正常启动，并反复进入尝试与失败的循环时就会出现。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0181

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0181`
- Split: `documentation_03`

Input:

```text
当 kubelet 检测到 Pod 不具备配置了网络的运行时沙箱时，`PodReadyToStartContainers` 状况将被设置为 `False`。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0183

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0183`
- Split: `documentation_03`

Input:

```text
在 Pod 生命周期的末期阶段，Pod 的沙箱由于以下原因被销毁时：节点重启时 Pod 没有被驱逐对于使用虚拟机进行隔离的容器运行时，Pod 沙箱虚拟机重启时，需要创建一个新的沙箱和全新的容器网络配置。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0227

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0227`
- Split: `documentation_03`

Input:

```text
`Unknown`（未知） : 诊断失败，因此不会采取任何行动。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0234

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0234`
- Split: `documentation_03`

Input:

```text
如果容器不提供就绪态探针，则默认状态为 `Success`。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0248

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0248`
- Split: `documentation_03`

Input:

```text
如果你的容器需要在启动期间加载大型数据、配置文件或执行迁移，你可以使用启动探针。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0251

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0251`
- Split: `documentation_03`

Input:

```text
关于 kubelet 如何处理 Pod 删除的更多信息，请参见 Pod 终止。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0266

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0266`
- Split: `documentation_03`

Input:

```text
许多容器运行时遵循容器镜像内定义的 `STOPSIGNAL` 值，如果不同，则发送容器镜像中配置的 STOPSIGNAL，而不是 TERM 信号。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0281

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0281`
- Split: `documentation_03`

Input:

```text
如果 Pod 中的容器之一定义了 `preStop` 回调且 Pod 规约中的 `terminationGracePeriodSeconds` 未设为 0， `kubelet` 开始在容器内运行该回调逻辑。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0282

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0282`
- Split: `documentation_03`

Input:

```text
如果 `preStop` 回调在体面期结束后仍在运行，kubelet 将请求短暂的、一次性的体面期延长 2 秒。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0341

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0341`
- Split: `documentation_03`

Input:

```text
这种传统行为在很长一段时间内都是默认设置的，但给 Kubernetes 用户带来了一些问题，尤其是在大规模部署场景中。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0002

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0002`
- Split: `documentation_04`

Input:

```text
你可以在 Pod 集合中运行代码，无论该代码是为云原生环境设计的，还是被容器化的老应用。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0004

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0004`
- Split: `documentation_04`

Input:

```text
如果你使用来运行你的应用， Deployment 可以动态地创建和销毁 Pod。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0020

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0020`
- Split: `documentation_04`

Input:

```text
Ingress 不是一种 Service，但它可用作集群的入口点。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0046

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0046`
- Split: `documentation_04`

Input:

```text
这一机制为 Service 的部署和演化提供了较高的灵活性。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0078

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0078`
- Split: `documentation_04`

Input:

```text
默认情况下，一旦现有 EndpointSlice 都包含至少 100 个端点，Kubernetes 就会创建一个新的 EndpointSlice。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0122

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0122`
- Split: `documentation_04`

Input:

```text
有关详细信息，请参阅无头服务。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0129

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0129`
- Split: `documentation_04`

Input:

```text
每个节点将该端口（每个节点上的相同端口号）上的流量代理到你的 Service。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0137

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0137`
- Split: `documentation_04`

Input:

```text
这意味着你需要自行注意可能发生的端口冲突。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0150

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0150`
- Split: `documentation_04`

Input:

```text
例如，如果你使用 `--nodeport-addresses=127.0.0.0/8` 标志启动 kube-proxy，则 kube-proxy 仅选择 NodePort Service 的本地回路接口。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0176

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0176`
- Split: `documentation_04`

Input:

```text
当 Service 中定义了多个端口时，特性门控 `MixedProtocolLBService`（从 kube-apiserver 1.24 版本起默认为启用）允许 LoadBalancer 类型的 Service 使用不同的协议。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0193

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0193`
- Split: `documentation_04`

Input:

```text
`.status.loadBalancer.ingress.ipMode` 有两个可能的值："VIP" 和 "Proxy"。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0206

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0206`
- Split: `documentation_04`

Input:

```text
如果后来你决定将数据库移到集群中，则可以启动其 Pod，添加适当的选择算符或端点并更改 Service 的 `type`。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0229

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0229`
- Split: `documentation_04`

Input:

```text
否则，这些客户端 Pod 中将不会出现对应的环境变量。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0231

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0231`
- Split: `documentation_04`

Input:

```text
Kubernetes 还支持并提供与 Docker Engine 的 "legacy container links" 兼容的变量。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0250

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0250`
- Split: `documentation_04`

Input:

```text
`PreferSameZone` : 表示优先将流量路由到与客户端处于同一区域中的端点。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0251

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0251`
- Split: `documentation_04`

Input:

```text
`PreferSameNode` : 表示优先将流量路由到与客户端处于同一节点上的端点。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0255

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0255`
- Split: `documentation_04`

Input:

```text
可阅读会话亲和性来进一步学习。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-014

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-014`
- Split: `article`

Input:

```text
注意那些要求立即做某事、提供听起来好得令人难以置信的东西或需要个人信息的可疑活动。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-019

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-019`
- Split: `article`

Input:

```text
尽可能利用能使用生物特征扫描的设备（例如，指纹扫描仪或面部识别）。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-020

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-020`
- Split: `article`

Input:

```text
定期检查账户结单和信用报告。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-021

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-021`
- Split: `article`

Input:

```text
共享个人财务信息时要谨慎，例如，银行帐号、社会保险号或信用卡号。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-028

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-028`
- Split: `article`

Input:

```text
切记：政府不会就欠款打电话、发短信或通过社交媒体联系您。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-030

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-030`
- Split: `article`

Input:

```text
检查信用卡和银行结单是否有无法识别的费用。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-038

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-038`
- Split: `article`

Input:

```text
在设备上运行安全扫描，确保系统没有受到感染或运行缓慢或效率低下。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-040

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-040`
- Split: `article`

Input:

```text
如果认为自己是网络攻击的受害者，应向适当的联邦、州和地方当局报告。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-051

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-051`
- Split: `article`

Input:

```text
如果驾照或汽车登记被盗，应联系机动车辆管理局。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-005

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-005`
- Split: `article`

Input:

```text
如果建议疏散，请计划好如何离开，以及将去往何处。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-022

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-022`
- Split: `article`

Input:

```text
下载FEMA app，以获得在当地发生灾害时开放的避难所清单。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-041

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-041`
- Split: `article`

Input:

```text
如果你因风暴而疏散，在旅行前向所在的地方和家乡的地方官员核实。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-006

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-006`
- Split: `project_original`

Input:

```text
审计报告指出采购程序缺少书面记录。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-008

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-008`
- Split: `project_original`

Input:

```text
研究团队发布人口变化的初步分析。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-010

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-010`
- Split: `project_original`

Input:

```text
市议会通过旧城区更新计划。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-011

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-011`
- Split: `project_original`

Input:

```text
执行单位须按季度提交进度报告。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-012

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-012`
- Split: `project_original`

Input:

```text
公报列出新规定的施行日期与适用范围。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-017

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-017`
- Split: `project_original`

Input:

```text
报告建议加强偏远地区的交通服务。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-019

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-019`
- Split: `project_original`

Input:

```text
委员会要求业者改善收费资讯的揭露方式。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-020

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-020`
- Split: `project_original`

Input:

```text
会议纪要记录各单位提出的保留意见。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-026

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-026`
- Split: `project_original`

Input:

```text
能源报告比较不同月份的用电需求。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-027

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-027`
- Split: `project_original`

Input:

```text
监管机关依法受理消费者提出的申诉。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-028

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-028`
- Split: `project_original`

Input:

```text
委员会确认本次表决达到法定人数。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-036

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-036`
- Split: `project_original`

Input:

```text
机关核定名称后才会制作正式标牌。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-038

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-038`
- Split: `project_original`

Input:

```text
调查人员查核支出凭证与付款纪录。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-042

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-042`
- Split: `project_original`

Input:

```text
预算审查将优先处理法定支出项目。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-043

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-043`
- Split: `project_original`

Input:

```text
主管单位请各机构指定联络窗口。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-046

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-046`
- Split: `project_original`

Input:

```text
委员会将在下次会议确认修正文字。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-047

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-047`
- Split: `project_original`

Input:

```text
新闻稿并未评论尚在审理中的案件。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-050

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-050`
- Split: `project_original`

Input:

```text
决议要求相关单位提出具体执行方案。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-001

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-001`
- Split: `project_original`

Input:

```text
模型先判断问题是否需要检索外部资料。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-004

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-004`
- Split: `project_original`

Input:

```text
助理应区分已知事实与合理推测。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-015

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-015`
- Split: `project_original`

Input:

```text
系统记录每次工具调用的开始与结束时间。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-016

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-016`
- Split: `project_original`

Input:

```text
模型会根据对话内容补充必要的上下文。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-018

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-018`
- Split: `project_original`

Input:

```text
检索器应排除已经失效的文件版本。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-020

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-020`
- Split: `project_original`

Input:

```text
助理应先确认高风险建议的适用范围。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-028

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-028`
- Split: `project_original`

Input:

```text
系统会合并重复出现的检索结果。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-031

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-031`
- Split: `project_original`

Input:

```text
评测集不得用于调整待测系统的规则。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-032

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-032`
- Split: `project_original`

Input:

```text
助理应避免扩大原始声明的适用对象。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-034

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-034`
- Split: `project_original`

Input:

```text
模型可以引用多个来源支持同一项结论。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-037

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-037`
- Split: `project_original`

Input:

```text
模型不应根据姓名推测个人的背景。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-038

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-038`
- Split: `project_original`

Input:

```text
工具失败时系统会保留可诊断的错误讯息。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-044

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-044`
- Split: `project_original`

Input:

```text
系统会限制一次能够处理的附件数量。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-045

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-045`
- Split: `project_original`

Input:

```text
模型必须区分原文陈述与后续评论。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-046

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-046`
- Split: `project_original`

Input:

```text
使用者可以选择是否保留对话纪录。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-050

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-050`
- Split: `project_original`

Input:

```text
模型需要依照请求决定回答的详细程度。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```
