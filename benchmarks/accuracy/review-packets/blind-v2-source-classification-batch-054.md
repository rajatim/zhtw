<!-- zhtw:disable -->
# Blind-v2 Source Classification 054

Packet: `benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-054.json`
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

### kubernetes-docs-zh-cn-v1/page-01-sentence-0005

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-01-sentence-0005`
- Split: `documentation_01`

Input:

```text
**名称在同一资源的所有 API 版本中必须是唯一的。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-01-sentence-0018

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-01-sentence-0018`
- Split: `documentation_01`

Input:

```text
某些资源类型需要其名称遵循 RFC 1035 所定义的 DNS 标签标准。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-01-sentence-0023

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-01-sentence-0023`
- Split: `documentation_01`

Input:

```text
某些资源类型可能具有额外的命名约束。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-02-sentence-0009

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-02-sentence-0009`
- Split: `documentation_02`

Input:

```text
因为这个技术直接在活跃对象上操作，所以它不提供以前配置的历史记录。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-02-sentence-0029

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-02-sentence-0029`
- Split: `documentation_02`

Input:

```text
对活动对象的更新必须反映在配置文件中，否则会在下一次替换时丢失。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0026

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0026`
- Split: `documentation_03`

Input:

```text
如果某物声称其生命期与某 Pod 相同，例如存储，这就意味着该对象在此 Pod （UID 亦相同）存在期间也一直存在。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0034

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0034`
- Split: `documentation_03`

Input:

```text
此阶段包括等待 Pod 被调度的时间和通过网络下载镜像的时间。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0039

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0039`
- Split: `documentation_03`

Input:

```text
也就是说，容器以非 0 状态退出或者被系统终止，且未被设置为自动重启。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0047

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0047`
- Split: `documentation_03`

Input:

```text
你可以使用 `--force` 参数来强制终止 Pod。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0088

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0088`
- Split: `documentation_03`

Input:

```text
当 Pod 中的某个容器停止或发生故障时，Kubernetes 可以重新启动此容器。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0155

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0155`
- Split: `documentation_03`

Input:

```text
在你的 kubelet 配置中，在 `crashLoopBackOff` 下设置 `maxContainerRestartPeriod` 字段，取值范围在 `"1s"` 到 `"300s"` 之间。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0156

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0156`
- Split: `documentation_03`

Input:

```text
如上文容器重启策略所述，该节点上的延迟仍将从 10 秒开始，并在每次重启后以指数方式增加 2 倍，但现在其上限将被限制为你所配置的最大值。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0185

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0185`
- Split: `documentation_03`

Input:

```text
当 `PodReadyToStartContainers` 状况设置为 `True` 后， Kubelet 可以开始拉取容器镜像和创建容器。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0241

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0241`
- Split: `documentation_03`

Input:

```text
如果你希望容器在探测失败时被杀死并重新启动，那么请指定一个存活态探针，并指定 `restartPolicy` 为 "`Always`" 或 "`OnFailure`"。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0247

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0247`
- Split: `documentation_03`

Input:

```text
这可以帮助你避免将流量导向只能返回错误信息的 Pod。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0252

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0252`
- Split: `documentation_03`

Input:

```text
对于所包含的容器需要较长时间才能启动就绪的 Pod 而言，启动探针是有用的。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0261

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0261`
- Split: `documentation_03`

Input:

```text
当你请求删除某个 Pod 时，集群会记录并跟踪 Pod 的体面终止周期，而不是直接强制地杀死 Pod。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0265

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0265`
- Split: `documentation_03`

Input:

```text
这些请求的处理顺序无法被保证。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0284

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0284`
- Split: `documentation_03`

Input:

```text
`kubelet` 接下来触发容器运行时发送 TERM 信号给每个容器中的进程 1。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0290

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0290`
- Split: `documentation_03`

Input:

```text
关闭动作很慢的 Pod 不应继续处理常规服务请求，而应开始终止并完成对打开的连接的处理。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0333

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0333`
- Split: `documentation_03`

Input:

```text
如果该 Node 的 `Ready` 状况保持不变，也就是说该状况没有从 true 变为 false，Kubernetes 就会将其检测为一次 kubelet 重启。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0346

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0346`
- Split: `documentation_03`

Input:

```text
进一步了解容器生命周期回调。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0057

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0057`
- Split: `documentation_04`

Input:

```text
由于此 Service 没有选择算符，因此不会自动创建对应的 EndpointSlice 对象。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0093

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0093`
- Split: `documentation_04`

Input:

```text
此字段被实现代码用作一种提示信息，以便针对实现能够理解的协议提供更为丰富的行为。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0113

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0113`
- Split: `documentation_04`

Input:

```text
`ExternalName` : 将服务映射到 `externalName` 字段的内容（例如，映射到主机名 `api.foo.bar.example`）。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0115

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0115`
- Split: `documentation_04`

Input:

```text
集群不会为之创建任何类型代理。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0116

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0116`
- Split: `documentation_04`

Input:

```text
Service API 中的 `type` 字段被设计为层层递进的形式 - 每层都建立在前一层的基础上。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0157

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0157`
- Split: `documentation_04`

Input:

```text
来自外部负载均衡器的流量将被直接重定向到后端各个 Pod 上，云平台决定如何进行负载平衡。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0197

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0197`
- Split: `documentation_04`

Input:

```text
在混合环境中，有时有必要在同一（虚拟）网络地址段内路由来自 Service 的流量。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0210

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0210`
- Split: `documentation_04`

Input:

```text
HTTP 请求将具有源服务器无法识别的 `Host:` 标头； TLS 服务器将无法提供与客户端连接的主机名匹配的证书。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0219

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0219`
- Split: `documentation_04`

Input:

```text
对定义了选择算符的无头 Service，Kubernetes 控制平面在 Kubernetes API 中创建 EndpointSlice 对象，并且修改 DNS 配置返回 A 或 AAAA 记录（IPv4 或 IPv6 地址），这些记录直接指向 Service 的后端 Pod 集合。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0233

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0233`
- Split: `documentation_04`

Input:

```text
你可以（并且几乎总是应该）使用插件（add-on）来为 Kubernetes 集群安装 DNS 服务。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-036

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-036`
- Split: `guide`

Input:

```text
作为国民，我们越了解这些措施，我们就可以保护和挽救更多生命。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-055

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-055`
- Split: `guide`

Input:

```text
相反，在遇到枪手行凶的情况下，您可以尝试转移到其他到枪手行凶的情况下，您可以尝试转移到其他地方。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-115

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-115`
- Split: `guide`

Input:

```text
避免过度劳累和体力吃重的活动，特别是在一天中温度最高的时段。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-123

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-123`
- Split: `guide`

Input:

```text
尝试洗凉水澡，用海绵擦拭身体，用冰袋或用湿冷的床单包裹起来。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-125

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-125`
- Split: `guide`

Input:

```text
注意呼吸，直到急救人员到达。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-130

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-130`
- Split: `guide`

Input:

```text
可以使用此储备金来支付租金、房屋和/或洪水保险，并在紧急情况下购买诸如食品、庇护所和饮水之类的救生物品。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-140

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-140`
- Split: `guide`

Input:

```text
洪水的深度很难确定，并且可能包含隐藏的危险杂物碎片。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-164

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-164`
- Split: `guide`

Input:

```text
请记住每个人的特定需求，包括药物。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-178

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-178`
- Split: `guide`

Input:

```text
注册获取有关当前状况信息的紧急通知，或下载紧急手机应用程序，例如联邦应急管理署（FEMA）的应用程序。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-187

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-187`
- Split: `guide`

Input:

```text
有时洪水会接踵而至，因为它们可能由同一事件引发。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-191

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-191`
- Split: `guide`

Input:

```text
除非当地当局另有指示，否则在室内呆24小时。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-192

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-192`
- Split: `guide`

Input:

```text
落尘之后，如果您在室外，请脱去被污染的衣服，擦去或清洗没有保护措施的皮肤。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-204

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-204`
- Split: `guide`

Input:

```text
当出现新型疾病，则表明它在人类中从未见过，通常没有疫苗可以预防它的传播。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-246

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-246`
- Split: `guide`

Input:

```text
龙卷风 • 如果是龙卷风警戒，请靠近安全的房间、庇护所或坚固的建筑物。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-251

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-251`
- Split: `guide`

Input:

```text
躲避龙卷风的最好方法是按照FEMA P-361标准建造的安全室，或按照ICC 500标准建造的防风洞。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-253

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-253`
- Split: `guide`

Input:

```text
在龙卷风警戒期间，请寻找庇护所。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-260

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-260`
- Split: `guide`

Input:

```text
海啸 • 如果您住在靠近或到访沿海地区，请了解海啸风险。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-263

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-263`
- Split: `guide`

Input:

```text
了解潜在的海啸征兆，如地震、海洋的巨大轰鸣，或海洋异常，例如突然水位上升，出现水墙，突然倒流露出海底的现象。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-286

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-286`
- Split: `guide`

Input:

```text
装修或建造新房屋时，请使用耐火的建筑材料。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-332

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-332`
- Split: `guide`

Input:

```text
如果听到了龙卷风的警报响起，您知道要去哪里吗？
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-373

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-373`
- Split: `guide`

Input:

```text
酒精含量至少为 60％的清洁用品，肥皂和免洗洗手液。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-391

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-391`
- Split: `guide`

Input:

```text
收集这些文件，并列出家里财产和贵重物品清单。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-423

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-423`
- Split: `guide`

Input:

```text
保险只适用于您的保单承保造成损失的危险。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-441

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-441`
- Split: `guide`

Input:

```text
从购买洪水保障到保险开始生效日之间，通常需要 30 天的等待期，因此请勿延迟购买保险。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-442

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-442`
- Split: `guide`

Input:

```text
帮助您购车、房屋或人寿保险的保险经纪人可以帮助购买洪水保险。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-478

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-478`
- Split: `guide`

Input:

```text
CERT项目教您基本的灾难响应技能，例如消防安全和紧急医疗作业。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-487

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-487`
- Split: `guide`

Input:

```text
民航巡逻队发现失踪人员；在灾难发生时给予安慰；并促进科学、技术、工程和数学（S T E M）等学科方面的教育。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-501

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-501`
- Split: `guide`

Input:

```text
在杂物碎片中工作时，请穿戴坚固的工作靴和手套，并经常用肥皂和清水彻底洗手。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-552

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-552`
- Split: `guide`

Input:

```text
确保您和您的家人在事件之后获得完全康复所需的支持。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-554

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-554`
- Split: `guide`

Input:

```text
有些人可能获得灾后经济援助计划。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-574

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-574`
- Split: `guide`

Input:

```text
如果可以的话，请帮助邻居来恢复社区。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-576

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-576`
- Split: `guide`

Input:

```text
在灾后，儿童、老年人、母语非英语人士、残障人士以及其他有障碍和功能需求的人们会受到严重影响，可能需要特殊关照。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/social-009

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `social-009`
- Split: `project_original`

Input:

```text
记得在出门前关闭客厅的电灯。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/social-010

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `social-010`
- Split: `project_original`

Input:

```text
这家餐厅可以提前预约靠窗座位。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/social-011

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `social-011`
- Split: `project_original`

Input:

```text
孩子的学校明天会提早放学。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/social-012

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `social-012`
- Split: `project_original`

Input:

```text
维修人员下午会来检查热水器。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/social-017

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `social-017`
- Split: `project_original`

Input:

```text
公车到站前，应用程序会发送提醒。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/social-018

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `social-018`
- Split: `project_original`

Input:

```text
这条道路施工期间只能单向通行。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/social-028

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `social-028`
- Split: `project_original`

Input:

```text
会议结束后大家一起去吃午餐。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/social-029

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `social-029`
- Split: `project_original`

Input:

```text
请先把药袋上的用法看清楚。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/social-031

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `social-031`
- Split: `project_original`

Input:

```text
跨行汇款手续费由转账人负担。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/social-032

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `social-032`
- Split: `project_original`

Input:

```text
租车费用不包含高速公路通行费。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/social-034

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `social-034`
- Split: `project_original`

Input:

```text
客服人员已经帮我更正收货地址。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/social-036

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `social-036`
- Split: `project_original`

Input:

```text
雨伞放在入口旁边的置物柜里。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/social-037

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `social-037`
- Split: `project_original`

Input:

```text
我们约在捷运站第二个出口见面。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/social-038

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `social-038`
- Split: `project_original`

Input:

```text
这段视频只会保留到月底。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/social-039

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `social-039`
- Split: `project_original`

Input:

```text
演唱会现场不能携带外食和饮料。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/social-046

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `social-046`
- Split: `project_original`

Input:

```text
房间号码 1208 不需要加上楼层。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/social-050

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `social-050`
- Split: `project_original`

Input:

```text
请在 RSVP 表单填写饮食需求。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/ui-001

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `ui-001`
- Split: `project_original`

Input:

```text
搜索框的提示文字会在输入内容后自动消失。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/ui-003

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `ui-003`
- Split: `project_original`

Input:

```text
打开通知后，系统会在锁定画面显示摘要。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/ui-009

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `ui-009`
- Split: `project_original`

Input:

```text
密码输入错误三次后，账号会暂时锁定。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/ui-012

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `ui-012`
- Split: `project_original`

Input:

```text
打印设置会记住上次选择的打印机。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/ui-018

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `ui-018`
- Split: `project_original`

Input:

```text
消息消费者停止后，待处理数量不会继续减少。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/ui-021

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `ui-021`
- Split: `project_original`

Input:

```text
切换深色模式后，编辑内容不会重新加载。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/ui-023

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `ui-023`
- Split: `project_original`

Input:

```text
列表排序方式会保存到用户偏好设置。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/ui-026

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `ui-026`
- Split: `project_original`

Input:

```text
下载按钮在文件准备完成前保持停用。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/ui-029

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `ui-029`
- Split: `project_original`

Input:

```text
错误消息应说明哪个字段需要修正。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/ui-034

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `ui-034`
- Split: `project_original`

Input:

```text
表格栏位过多时可以水平滚动。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/ui-036

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `ui-036`
- Split: `project_original`

Input:

```text
步骤指示器会标示尚未完成的项目。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/ui-042

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `ui-042`
- Split: `project_original`

Input:

```text
GitHub 登录失败时不会建立重复账号。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/ui-046

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `ui-046`
- Split: `project_original`

Input:

```text
档案编号 A-1047 会显示在页面标题旁。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/ui-048

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `ui-048`
- Split: `project_original`

Input:

```text
联络窗口变更后会通知所有管理员。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-ui-social-baseline-guard-v1/ui-050

- Source: `zhtw-project-ui-social-baseline-guard-v1`
- Source case: `ui-050`
- Split: `project_original`

Input:

```text
资料检核完成后才能启用发布按钮。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```
