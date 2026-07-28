<!-- zhtw:disable -->
# Blind-v2 Source Classification 047

Packet: `benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-047.json`
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

### kubernetes-docs-zh-cn-v1/page-03-sentence-0009

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0009`
- Split: `documentation_03`

Input:

```text
Pod 对象的状态包含了一组 Pod 状况（Conditions）。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0062

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0062`
- Split: `documentation_03`

Input:

```text
处于 `Terminated` 状态的容器开始执行后，或者运行至正常结束或者因为某些原因失败。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0067

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0067`
- Split: `documentation_03`

Input:

```text
反复的崩溃：在最初的崩溃之后，Kubernetes 对于后续重新启动的容器采用指数级回退延迟机制，如 `restartPolicy` 中所述。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0117

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0117`
- Split: `documentation_03`

Input:

```text
如果指定了 `restartPolicyRules` 字段，则必须同时指定容器的 `restartPolicy`。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0138

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0138`
- Split: `documentation_03`

Input:

```text
这样可以确保快速关闭容器。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0142

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0142`
- Split: `documentation_03`

Input:

```text
`RestartAllContainers` 动作会重载所有已配置的容器级或 Pod 级别的 `restartPolicy`。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0187

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0187`
- Split: `documentation_03`

Input:

```text
Kubernetes 支持在 Pod 创建后更改分配给 Pod 的 CPU 和内存资源。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0196

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0196`
- Split: `documentation_03`

Input:

```text
就地调整大小的关键考量：仅 CPU 和内存资源可以原地调整大小。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0200

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0200`
- Split: `documentation_03`

Input:

```text
更改 Pod 资源更云原生的方法是通过管理它的工作负载资源（如 Deployment 或 StatefulSet）。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0238

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0238`
- Split: `documentation_03`

Input:

```text
如果容器没有提供启动探测，则默认状态为 `Success`。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0246

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0246`
- Split: `documentation_03`

Input:

```text
当应用程序本身是健康的，存活态探针检测通过后，就绪态探针会额外检查每个所需的后端服务是否可用。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0295

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0295`
- Split: `documentation_03`

Input:

```text
你可以在教程探索 Pod 及其端点的终止行为中找到有关如何实现连接排空的更多详细信息。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0304

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0304`
- Split: `documentation_03`

Input:

```text
`kubectl delete` 命令支持 `--grace-period=` 选项，允许你重载默认值，设定自己希望的期限值。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0314

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0314`
- Split: `documentation_03`

Input:

```text
如果你的 Pod 包含一个或多个 Sidecar 容器（重启策略为 `Always` 的 Init 容器），kubelet 将延迟向这些 Sidecar 容器发送 TERM 信号，直到最后一个主容器已完全终止。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0315

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0315`
- Split: `documentation_03`

Input:

```text
Sidecar 容器将按照它们在 Pod 规约中被定义的相反顺序被终止。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0318

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0318`
- Split: `documentation_03`

Input:

```text
如果在终止过程完成之前宽限期已到，Pod 可能会进入强制终止阶段。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0331

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0331`
- Split: `documentation_03`

Input:

```text
如果需要停止节点上的 Pod，可以使用 `kubectl drain`。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0338

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0338`
- Split: `documentation_03`

Input:

```text
但是，即使开始发生 Pod 驱逐，Kubernetes 也不会将这些 Pod 中的单个容器标记为 `ready: false`。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0006

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0006`
- Split: `documentation_04`

Input:

```text
Kubernetes 的创建和销毁是为了匹配集群的预期状态。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0008

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0008`
- Split: `documentation_04`

Input:

```text
每个 Pod 会获得属于自己的 IP 地址（Kubernetes 期待网络插件来保证这一点）。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0019

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0019`
- Split: `documentation_04`

Input:

```text
如果你的工作负载使用 HTTP 通信，你可能会选择使用 Ingress 来控制 Web 流量如何到达该工作负载。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0084

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0084`
- Split: `documentation_04`

Input:

```text
因此，推荐所有客户端使用 EndpointSlice API 来替换 Endpoints。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0106

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0106`
- Split: `documentation_04`

Input:

```text
`ClusterIP` : 通过集群的内部 IP 公开 Service，选择该值时 Service 只能够在集群内部访问。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0139

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0139`
- Split: `documentation_04`

Input:

```text
为 NodePort Service 分配端口的策略既适用于自动分配的情况，也适用于手动分配的场景。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0152

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0152`
- Split: `documentation_04`

Input:

```text
这意味着 kube-proxy 将认为所有可用网络接口都可用于 NodePort Service （这也与早期的 Kubernetes 版本兼容。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0161

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0161`
- Split: `documentation_04`

Input:

```text
某些云平台允许你设置 `loadBalancerIP`。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0164

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0164`
- Split: `documentation_04`

Input:

```text
如果设置了 `loadBalancerIP`，但云平台并不支持这一特性，所设置的 `loadBalancerIP` 值将会被忽略。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0169

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0169`
- Split: `documentation_04`

Input:

```text
如果你正在集成某云平台，该平台通过（特定于平台的）注解为 Service 指定负载均衡器 IP 地址，你应该切换到这种做法。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0196

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0196`
- Split: `documentation_04`

Input:

```text
Service 实现可以使用此信息来调整流量路由。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0223

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0223`
- Split: `documentation_04`

Input:

```text
当你定义无选择算符的无头 Service 时，`port` 必须与 `targetPort` 匹配。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0225

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0225`
- Split: `documentation_04`

Input:

```text
当 Pod 运行在某 Node 上时，kubelet 会在其中为每个活跃的 Service 添加一组环境变量。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0249

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0249`
- Split: `documentation_04`

Input:

```text
这一机制有助于优化性能、成本或可靠性。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-001

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-001`
- Split: `article`

Input:

```text
许多类型的紧急情况可能会导致你不得不进行疏散。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-003

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-003`
- Split: `article`

Input:

```text
无论在什么情况下，计划对于确保各位能快速安全地撤离至关重要。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-004

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-004`
- Split: `article`

Input:

```text
了解各自所在社区可能发生的灾害类型，以及当地针对每种具体灾害的应急、疏散和避难计划。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-007

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-007`
- Split: `article`

Input:

```text
冠状病毒可能改变了所在社区的计划。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-008

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-008`
- Split: `article`

Input:

```text
确定几个你在紧急情况下可以去的地方，如另一个城市的朋友家或汽车旅馆。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-009

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-009`
- Split: `article`

Input:

```text
选择不同方向的目的地，以便在紧急情况下可以有选择。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-011

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-011`
- Split: `article`

Input:

```text
熟悉离开所在地区的备用路线和其他交通方式。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-012

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-012`
- Split: `article`

Input:

```text
始终遵循当地官员的指示，并记住疏散路线可能是步行，这取决于灾害的类型。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-013

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-013`
- Split: `article`

Input:

```text
制定家庭/家族计划，以便在失散的情况下保持联系；包含会面地点，并根据情况更新。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-014

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-014`
- Split: `article`

Input:

```text
集合准备好撤离用的物资。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-016

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-016`
- Split: `article`

Input:

```text
如果有车的话：如果有可能进行疏散，请保持满箱汽油。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-017

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-017`
- Split: `article`

Input:

```text
始终保持半箱汽油，以防意外需要撤离。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-018

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-018`
- Split: `article`

Input:

```text
加油站在紧急情况下可能会关闭，在停电期间也无法抽油。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-019

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-019`
- Split: `article`

Input:

```text
计划每个家庭带一辆车，以减少拥挤和延误。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-020

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-020`
- Split: `article`

Input:

```text
如果你没有车，计划好在需要时如何离开。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-021

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-021`
- Split: `article`

Input:

```text
与家人、朋友或当地应急管理办公室一起决定，看看有哪些资源可以利用。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-025

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-025`
- Split: `article`

Input:

```text
提前离开，以免被恶劣天气所困。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-026

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-026`
- Split: `article`

Input:

```text
带上宠物，但要明白只有服务性动物才可以进入公共庇护所。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-029

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-029`
- Split: `article`

Input:

```text
告知他们你的去处。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-030

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-030`
- Split: `article`

Input:

```text
关闭并锁好门窗，保护你的家。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-032

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-032`
- Split: `article`

Input:

```text
除非有水淹的危险，否则不要把冰箱和冰柜的插头插上。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-033

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-033`
- Split: `article`

Input:

```text
如果你的家受到损害，并且要求你这样做，在离开之前关闭水、煤气和电。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-034

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-034`
- Split: `article`

Input:

```text
留下一张纸条，告诉他人你什么时候离开以及要去哪里。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-035

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-035`
- Split: `article`

Input:

```text
穿上结实的鞋子和能提供一些保护的衣服，如长裤、长袖衬衫和帽子。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-037

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-037`
- Split: `article`

Input:

```text
遵循建议的疏散路线。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-038

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-038`
- Split: `article`

Input:

```text
不要走捷径，道路可能被封锁。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-039

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-039`
- Split: `article`

Input:

```text
对道路上的危险保持警惕，如被冲毁的道路或桥梁以及被压断的电线。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-040

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-040`
- Split: `article`

Input:

```text
不要开车进入洪水区。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-043

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-043`
- Split: `article`

Input:

```text
在离开之前和到达之后，让朋友和家人知道。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-046

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-046`
- Split: `article`

Input:

```text
带上水和不易腐烂的食物等用品，以便乘车时使用。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-047

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-047`
- Split: `article`

Input:

```text
避开停电或公用事业线，它们可能带有致命的电压。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-evacuation-zh-hans-v1/sentence-048

- Source: `ready-gov-evacuation-zh-hans-v1`
- Source case: `sentence-048`
- Split: `article`

Input:

```text
远离它们，并立即向电力或公用事业公司报告。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/formal-001

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-001`
- Split: `project_original`

Input:

```text
采购公告将产品名称 Microsoft Entra ID 原样列入需求表。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/formal-003

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-003`
- Split: `project_original`

Input:

```text
判决书引用案件名称 Brown v. Board of Education。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/formal-004

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-004`
- Split: `project_original`

Input:

```text
审计报告以 Finding No. 2026-04 标示缺失事项。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/formal-007

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-007`
- Split: `project_original`

Input:

```text
法院卷宗以 Case No. 24-CV-0187 识别案件。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/formal-008

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-008`
- Split: `project_original`

Input:

```text
会议记录保留议程代码 Item 3(c)(ii)。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/formal-009

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-009`
- Split: `project_original`

Input:

```text
合约将服务级别标记写为 SLO-99.95。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/formal-010

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-010`
- Split: `project_original`

Input:

```text
研究报告引用 DOI 10.5281/zenodo.1234567。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/formal-012

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-012`
- Split: `project_original`

Input:

```text
证券文件中的 ISIN US5949181045 不得改写。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/formal-013

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-013`
- Split: `project_original`

Input:

```text
危险品申报单保留运输编号 UN 3091。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/formal-014

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-014`
- Split: `project_original`

Input:

```text
专利公报使用申请号 PCT/US2026/012345。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/formal-016

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-016`
- Split: `project_original`

Input:

```text
国际文件的正式代号为 A/RES/81/12。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/formal-018

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-018`
- Split: `project_original`

Input:

```text
财务附注保留科目代码 AR-1200-07。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/formal-024

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-024`
- Split: `project_original`

Input:

```text
公告中的电子邮件地址 service-desk@example.org 必须保持不变。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/formal-027

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-027`
- Split: `project_original`

Input:

```text
采购清单中的料号 MX-2048-B 不得本地化。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/formal-028

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-028`
- Split: `project_original`

Input:

```text
法规附件引用 Article 6(1)(f) 的原始编号。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/formal-030

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-030`
- Split: `project_original`

Input:

```text
新闻稿将品牌名称 Cloudflare Workers 原样呈现。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/formal-033

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-033`
- Split: `project_original`

Input:

```text
药品批号 LOT 26A07 应与包装记录一致。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/formal-037

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `formal-037`
- Split: `project_original`

Input:

```text
招标文件使用项目代号 Project Lighthouse。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/llm-001

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-001`
- Split: `project_original`

Input:

```text
请求中的模型名称 gemini-example-pro-002 必须保持不变。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/llm-002

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-002`
- Split: `project_original`

Input:

```text
系统消息以 policy_version=2026-07 标记规则版本。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/llm-003

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-003`
- Split: `project_original`

Input:

```text
工具调用使用 call_id=call_01JQ8M7Y 对应结果。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/llm-005

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-005`
- Split: `project_original`

Input:

```text
评测器把 pass、fail 与 abstain 设为固定标签。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/llm-010

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-010`
- Split: `project_original`

Input:

```text
系统边界标记 BEGIN_EXTERNAL_CONTEXT 不属于回答内容。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/llm-011

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-011`
- Split: `project_original`

Input:

```text
批次任务以 batch_01JQ9A2Z7H 作为不可变识别码。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/llm-013

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-013`
- Split: `project_original`

Input:

```text
多模态输入通过 image_url.high_detail 指定解析模式。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/llm-020

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-020`
- Split: `project_original`

Input:

```text
语音转录保留说话者标签 SPEAKER_02。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/llm-022

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-022`
- Split: `project_original`

Input:

```text
对话汇出档保留 message_id、parent_id 与thread_id。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/llm-025

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-025`
- Split: `project_original`

Input:

```text
解码器遇到停止序列 </final_answer> 时结束生成。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/llm-029

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-029`
- Split: `project_original`

Input:

```text
知识库文件以 kb://legal/policy-17 作为来源位置。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/llm-030

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-030`
- Split: `project_original`

Input:

```text
评测资料保留 locale=zh-TW 的大小写。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/llm-038

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-038`
- Split: `project_original`

Input:

```text
资料切片的识别码为 chunk_000184。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-overconversion-guard-v1/llm-039

- Source: `zhtw-project-formal-llm-overconversion-guard-v1`
- Source case: `llm-039`
- Split: `project_original`

Input:

```text
系统提示引用产品名称 Vertex AI Search。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```
