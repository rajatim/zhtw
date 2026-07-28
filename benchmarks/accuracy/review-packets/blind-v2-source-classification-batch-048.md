<!-- zhtw:disable -->
# Blind-v2 Source Classification 048

Packet: `benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-048.json`
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

### kubernetes-docs-zh-cn-v1/page-01-sentence-0025

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-01-sentence-0025`
- Split: `documentation_01`

Input:

```text
UUID 是标准化的，见 ISO/IEC 9834-8 和 ITU-T X.667。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-01-sentence-0027

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-01-sentence-0027`
- Split: `documentation_01`

Input:

```text
参阅 Kubernetes 标识符和名称的设计文档。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-02-sentence-0031

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-02-sentence-0031`
- Split: `documentation_02`

Input:

```text
`kubectl` 会自动检测每个文件的创建、更新和删除操作。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0002

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0002`
- Split: `documentation_03`

Input:

```text
Pod 遵循预定义的生命周期，起始于 `Pending` 阶段，如果至少其中有一个主要容器正常启动，则进入 `Running`，之后取决于 Pod 中是否有容器以失败状态结束而进入 `Succeeded` 或者 `Failed` 阶段。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0020

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0020`
- Split: `documentation_03`

Input:

```text
如果 Pod 被调度到某个而该节点之后失效， Pod 会被视为不健康，最终 Kubernetes 会删除 Pod。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0030

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0030`
- Split: `documentation_03`

Input:

```text
该阶段并不是对容器或 Pod 状态的综合汇总，也不是为了成为完整的状态机。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0104

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0104`
- Split: `documentation_03`

Input:

```text
虽然主应用程序容器遵循 Pod 的 `restartPolicy: OnFailure`，但边车容器无论其退出代码如何都会重新启动，因为边车容器在容器级别会始终设置 `restartPolicy: Always`。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0122

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0122`
- Split: `documentation_03`

Input:

```text
这些规则会按顺序进行评估。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0123

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0123`
- Split: `documentation_03`

Input:

```text
一旦匹配成功，立即执行相应动作。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0140

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0140`
- Split: `documentation_03`

Input:

```text
Init 容器按顺序重新运行。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0141

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0141`
- Split: `documentation_03`

Input:

```text
此特性的一个关键点是所有容器都会被重启，包括之前已成功完成或失败的容器。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0146

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0146`
- Split: `documentation_03`

Input:

```text
watcher 可以以特定代码退出，从而触发 worker Pod 的就地完整重启。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0243

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0243`
- Split: `documentation_03`

Input:

```text
在这种情况下，就绪态探针可能与存活态探针相同，但是规约中的就绪态探针的存在意味着 Pod 将在启动阶段不接收任何数据，并且只有在探针探测成功后才开始接收数据。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0273

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0273`
- Split: `documentation_03`

Input:

```text
可用的信号列表取决于 Pod 调度到的操作系统。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0274

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0274`
- Split: `documentation_03`

Input:

```text
对于调度到 Windows 节点的 Pod，仅支持 SIGTERM 和 SIGKILL 信号。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0291

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0291`
- Split: `documentation_03`

Input:

```text
一些应用程序不仅需要完成对打开的连接的处理，还需要更进一步的体面终止逻辑 - 比如：排空和完成会话。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0293

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0293`
- Split: `documentation_03`

Input:

```text
正在终止的端点始终将其 `ready` 状态设置为 `false`（为了向后兼容 1.26 之前的版本），因此负载均衡器不会将其用于常规流量。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0309

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0309`
- Split: `documentation_03`

Input:

```text
API 服务器直接删除 Pod 对象，这样新的与之同名的 Pod 即可以被创建。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0322

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0322`
- Split: `documentation_03`

Input:

```text
对于已失败的 Pod 而言，对应的 API 对象仍然会保留在集群的 API 服务器上，直到用户或者进程显式地将其删除。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0324

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0324`
- Split: `documentation_03`

Input:

```text
这一行为会避免随着时间演进不断创建和终止 Pod 而引起的资源泄露问题。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0013

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0013`
- Split: `documentation_04`

Input:

```text
例如，考虑一个无状态的图像处理后端，其中运行 3 个副本（Replicas）。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0051

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0051`
- Split: `documentation_04`

Input:

```text
由于选择算符的存在，Service 的最常见用法是为 Kubernetes Pod 集合提供访问抽象，但是当与相应的对象一起使用且没有设置选择算符时，Service 也可以为其他类型的后端提供抽象，包括在集群外运行的后端。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0063

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0063`
- Split: `documentation_04`

Input:

```text
对于你自己或在你自己代码中创建的 EndpointSlice，你还应该为 `endpointslice.kubernetes.io/managed-by` 标签设置一个值。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0095

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0095`
- Split: `documentation_04`

Input:

```text
此字段遵循标准的 Kubernetes 标签语法。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0097

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0097`
- Split: `documentation_04`

Input:

```text
由具体实现所定义的、带有 `mycompany.com/my-custom-protocol` 这类前缀的名称。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0141

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0141`
- Split: `documentation_04`

Input:

```text
为了避免这个问题，用于 NodePort Service 的端口范围被分为两段。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0147

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0147`
- Split: `documentation_04`

Input:

```text
如果你要指定特定的 IP 地址来为端口提供代理，可以将 kube-proxy 的 `--nodeport-addresses` 标志或 kube-proxy 配置文件中的等效字段 `nodePortAddresses` 设置为特定的 IP 段。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0148

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0148`
- Split: `documentation_04`

Input:

```text
此标志接受逗号分隔的 IP 段列表（例如 `10.0.0.0/8`、`192.0.2.0/25`），用来设置 IP 地址范围。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0171

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0171`
- Split: `documentation_04`

Input:

```text
你可以与 Gateway 而不是 Service 集成，或者你可以在 Service 上定义自己的（特定于提供商的）注解，以指定等效的细节。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0207

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0207`
- Split: `documentation_04`

Input:

```text
针对 ExternalName Service 使用一些常见的协议，包括 HTTP 和 HTTPS，可能会有问题。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0214

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0214`
- Split: `documentation_04`

Input:

```text
无头 Service 不会获得集群 IP，kube-proxy 不会处理这类 Service，而且平台也不会为它们提供负载均衡或路由支持。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0215

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0215`
- Split: `documentation_04`

Input:

```text
无头 Service 允许客户端直接连接到它所偏好的任一 Pod。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-001

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-001`
- Split: `article`

Input:

```text
网络攻击是指访问或损坏电脑或网络系统的恶意企图，可能导致金钱损失或个人、财务和医疗信息被盗。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-002

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-002`
- Split: `article`

Input:

```text
这些攻击可能会损害受害者的声誉和安全。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-003

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-003`
- Split: `article`

Input:

```text
网络安全涉及预防、检测和应对可能对个人、组织、社区和国家产生广泛影响的网络攻击。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-004

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-004`
- Split: `article`

Input:

```text
访问个人电脑、手机、游戏系统和其他连接互联网和蓝牙的设备。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-006

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-006`
- Split: `article`

Input:

```text
阻止访问或删除个人信息和帐户。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-007

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-007`
- Split: `article`

Input:

```text
使就业或商业服务更加复杂。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-008

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-008`
- Split: `article`

Input:

```text
影响交通和电网。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-009

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-009`
- Split: `article`

Input:

```text
限制在线共享的个人信息。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-010

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-010`
- Split: `article`

Input:

```text
更改隐私设置，不要使用位置功能。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-012

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-012`
- Split: `article`

Input:

```text
使用大小写字母、数字和特殊字符创建强密码。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-015

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-015`
- Split: `article`

Input:

```text
点击之前应深思。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-016

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-016`
- Split: `article`

Input:

```text
有疑问时不要点击。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-017

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-017`
- Split: `article`

Input:

```text
使用安全的互联网连接和 Wi-Fi 网络保护好家庭和/或企业，定期更改密码。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-023

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-023`
- Split: `article`

Input:

```text
使用能创建更安全连接的虚拟专用网络 (VPN)。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-024

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-024`
- Split: `article`

Input:

```text
使用防病毒和反恶意软件解决方案及防火墙来阻止威胁。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-025

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-025`
- Split: `article`

Input:

```text
定期在加密文件或加密文件储存设备中备份文件。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-026

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-026`
- Split: `article`

Input:

```text
不要点击陌生人发来短信或电子邮件中的链接。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-027

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-027`
- Split: `article`

Input:

```text
诈骗者可能会创建指向网站的虚假链接。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-029

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-029`
- Split: `article`

Input:

```text
还要记住，诈骗者可能会试图利用在家工作的机会、债务合并优惠和学生贷款还款计划来利用财务恐惧。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-031

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-031`
- Split: `article`

Input:

```text
检查信用报告中是否有任何自己未开设的新账户或贷款。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-034

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-034`
- Split: `article`

Input:

```text
考虑关闭受影响的设备，交给专业人员扫描潜在病毒，并删除发现的任何病毒。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-035

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-035`
- Split: `article`

Input:

```text
切记：公司不会打电话来要求控制电脑以修复。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-036

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-036`
- Split: `article`

Input:

```text
这是一种常见的骗局。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-039

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-039`
- Split: `article`

Input:

```text
如果发现问题，应断开设备的互联网连接，并执行完整的系统还原。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-042

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-042`
- Split: `article`

Input:

```text
可能需要暂停受到攻击的帐户。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-044

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-044`
- Split: `article`

Input:

```text
报告有人可能在使用您的身份。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-045

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-045`
- Split: `article`

Input:

```text
如果认为有人在非法使用您的社会保障号，请向监察长办公室 (OIG) 举报。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-047

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-047`
- Split: `article`

Input:

```text
他们会审查投诉并交给适当的机构。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-048

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-048`
- Split: `article`

Input:

```text
向当地警方报案，以便有事件的正式记录。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-049

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-049`
- Split: `article`

Input:

```text
向联邦贸易委员会报告身份盗窃。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-054

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-054`
- Split: `article`

Input:

```text
iKeepSafe 为儿童、学校和家庭提供安全的数字环境。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-cybersecurity-zh-hans-v1/sentence-055

- Source: `ready-gov-cybersecurity-zh-hans-v1`
- Source case: `sentence-055`
- Split: `article`

Input:

```text
iSafe 证明数字产品符合处理受保护个人信息的州和联邦要求。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-002

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-002`
- Split: `project_original`

Input:

```text
主管机关要求申请人补充资金来源说明。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-009

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-009`
- Split: `project_original`

Input:

```text
听证会将邀请居民陈述实际影响。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-013

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-013`
- Split: `project_original`

Input:

```text
学校委员会决定调整校车服务路线。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-014

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-014`
- Split: `project_original`

Input:

```text
卫生部门提醒民众留意最新检验结果。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-016

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-016`
- Split: `project_original`

Input:

```text
承办人员确认附件均已完成用印。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-025

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-025`
- Split: `project_original`

Input:

```text
管理单位说明场地租借的优先顺序。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-029

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-029`
- Split: `project_original`

Input:

```text
新闻资料引用专家对市场趋势的观察。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-030

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-030`
- Split: `project_original`

Input:

```text
计划书应说明风险评估与应对措施。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-031

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-031`
- Split: `project_original`

Input:

```text
主管机关公布获准设置的服务据点。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-032

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-032`
- Split: `project_original`

Input:

```text
统计资料依年龄与居住地区分别汇整。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-034

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-034`
- Split: `project_original`

Input:

```text
环境评估将长期监测水质变化。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-035

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-035`
- Split: `project_original`

Input:

```text
公告期间收到的意见将逐项回应。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-037

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-037`
- Split: `project_original`

Input:

```text
承包商必须保存材料检验的原始资料。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/formal-040

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `formal-040`
- Split: `project_original`

Input:

```text
年度报告说明服务量能与人员配置。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-005

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-005`
- Split: `project_original`

Input:

```text
评测资料包含多轮对话与单轮问答。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-006

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-006`
- Split: `project_original`

Input:

```text
检索结果会依相关性重新排序。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-008

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-008`
- Split: `project_original`

Input:

```text
工具回传空结果时不要编造后续内容。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-009

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-009`
- Split: `project_original`

Input:

```text
提示词要求保留输入中的专有名称。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-010

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-010`
- Split: `project_original`

Input:

```text
系统会遮蔽记录中的敏感个人资料。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-011

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-011`
- Split: `project_original`

Input:

```text
摘要必须涵盖原文的主要限制条件。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-013

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-013`
- Split: `project_original`

Input:

```text
助理不应把示例内容当成真实指令。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-021

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-021`
- Split: `project_original`

Input:

```text
模型产生的建议不能取代专业判断。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-022

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-022`
- Split: `project_original`

Input:

```text
评测报告分别统计正确、错误与拒答案例。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-024

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-024`
- Split: `project_original`

Input:

```text
使用者修改问题后会触发新的回答。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-025

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-025`
- Split: `project_original`

Input:

```text
模型应完整保留引用文字的原始语气。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-030

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-030`
- Split: `project_original`

Input:

```text
模型需要辨识问题中隐含的时间范围。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-033

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-033`
- Split: `project_original`

Input:

```text
系统会在传送前验证附件是否可读取。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-035

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-035`
- Split: `project_original`

Input:

```text
回应中的日期必须与来源资料一致。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-040

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-040`
- Split: `project_original`

Input:

```text
系统会把外部内容标记为不受信任的资料。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-043

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-043`
- Split: `project_original`

Input:

```text
助理应说明无法完成请求的具体限制。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-047

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-047`
- Split: `project_original`

Input:

```text
评测器会比较答案与人工建立的参考结果。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-context-guard-v1/llm-048

- Source: `zhtw-project-formal-llm-context-guard-v1`
- Source case: `llm-048`
- Split: `project_original`

Input:

```text
助理应在数字资料不足时避免精确估算。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```
