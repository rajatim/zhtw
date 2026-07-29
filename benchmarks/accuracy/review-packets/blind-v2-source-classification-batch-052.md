<!-- zhtw:disable -->
# Blind-v2 Source Classification 052

Packet: `benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-052.json`
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

### kubernetes-docs-zh-cn-v1/page-01-sentence-0006

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-01-sentence-0006`
- Split: `documentation_01`

Input:

```text
虽然你可以通过不同的 API 版本（如 `v1` 或 `v1beta1`）访问资源，但版本只是同一底层对象的不同表示。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-02-sentence-0008

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-02-sentence-0008`
- Split: `documentation_02`

Input:

```text
这是开始或者在集群中运行一次性任务的推荐方法。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-02-sentence-0014

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-02-sentence-0014`
- Split: `documentation_02`

Input:

```text
命令不提供用于创建新对象的模板。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-02-sentence-0019

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-02-sentence-0019`
- Split: `documentation_02`

Input:

```text
此方法不应与对象规约被独立于配置文件进行更新的资源类型一起使用。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0028

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0028`
- Split: `documentation_03`

Input:

```text
Pod 的 `status` 字段是一个 PodStatus 对象，其中包含一个 `phase` 字段。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0041

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0041`
- Split: `documentation_03`

Input:

```text
这种情况通常是因为与 Pod 所在主机通信失败。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0074

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0074`
- Split: `documentation_03`

Input:

```text
这种机制可以防止有问题的容器因不断进行启动失败尝试而导致系统不堪重负。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0090

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0090`
- Split: `documentation_03`

Input:

```text
你可以将重启配置为适用于所有 Pod 的策略，或者使用容器级别的配置（例如：在你定义或定义容器级别重载时）。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0094

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0094`
- Split: `documentation_03`

Input:

```text
Pod 的 `spec` 中包含一个 `restartPolicy` 字段，其可能取值包括 Always、OnFailure 和 Never。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0111

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0111`
- Split: `documentation_03`

Input:

```text
Kubernetes 原生的边车容器将其容器级别的 `restartPolicy` 设置为 `Always`。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0170

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0170`
- Split: `documentation_03`

Input:

```text
如果 Kubernetes 无法在 `status.conditions` 字段中找到某状况，则该状况的状态值默认为 "`False`"。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0189

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0189`
- Split: `documentation_03`

Input:

```text
你可以调整 Pod 的容器级别 CPU 和内存资源，而无需重建 Pod。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0203

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0203`
- Split: `documentation_03`

Input:

```text
可以更改任何 Pod 规约，而不仅仅是资源。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0218

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0218`
- Split: `documentation_03`

Input:

```text
有关 kubelet 如何跟踪重定向的更多信息，请参阅配置探测。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0240

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0240`
- Split: `documentation_03`

Input:

```text
如果容器中的进程能够在遇到问题或不健康的情况下自行崩溃，则不一定需要存活态探针； `kubelet` 将根据 Pod 的 `restartPolicy` 自动执行修复操作。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0244

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0244`
- Split: `documentation_03`

Input:

```text
如果你希望容器能够自行进入维护状态，也可以指定一个就绪态探针，检查某个特定于就绪态的因此不同于存活态探测的端点。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-03-sentence-0268

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-03-sentence-0268`
- Split: `documentation_03`

Input:

```text
如果 `kubelet` 或者容器运行时的管理服务在等待进程终止期间被重启，集群会从头开始重试，赋予 Pod 完整的体面终止限期。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0005

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0005`
- Split: `documentation_04`

Input:

```text
在任何时刻，你都不知道有多少个这样的 Pod 正在工作以及它们健康与否；你可能甚至不知道如何辨别健康的 Pod。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0014

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0014`
- Split: `documentation_04`

Input:

```text
这些副本是可互换的 —— 前端不需要关心它们调用的是哪个后端。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0015

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0015`
- Split: `documentation_04`

Input:

```text
即便构成后端集合的实际 Pod 可能会发生变化，前端客户端不应该也没必要知道这些，而且它们也不必亲自跟踪后端的状态变化。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0023

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0023`
- Split: `documentation_04`

Input:

```text
Gateway 是使用实现的一系列扩展 API。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0029

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0029`
- Split: `documentation_04`

Input:

```text
Kubernetes 中的 Service 是一个（与 Pod 或 ConfigMap 类似）。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0030

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0030`
- Split: `documentation_04`

Input:

```text
你可以使用 Kubernetes API 创建、查看或修改 Service 定义。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0054

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0054`
- Split: `documentation_04`

Input:

```text
你正在将工作负载迁移到 Kubernetes 上来。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0061

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0061`
- Split: `documentation_04`

Input:

```text
端点 IP 地址必须不是：本地回路地址（IPv4 的 127.0.0.0/8、IPv6 的 ::1/128）或链路本地地址（IPv4 的 169.254.0.0/16 和 224.0.0.0/24、IPv6 的 fe80::/64）。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0166

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0166`
- Split: `documentation_04`

Input:

```text
此字段的定义模糊，其含义因实现而异。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0175

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0175`
- Split: `documentation_04`

Input:

```text
默认情况下，对于 LoadBalancer 类型的 Service，当其中定义了多个端口时，所有端口必须使用相同的协议，并且该协议必须是被云平台支持的。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0184

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0184`
- Split: `documentation_04`

Input:

```text
默认情况下，`.spec.loadBalancerClass` 是未设置的，如果集群使用 `--cloud-provider` 件标志配置了云平台，`LoadBalancer` 类型 Service 会使用云平台的默认负载均衡器实现。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0199

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0199`
- Split: `documentation_04`

Input:

```text
类型为 ExternalName 的 Service 将 Service 映射到 DNS 名称，而不是典型的选择算符，例如 `my-service` 或者 `cassandra`。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0208

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0208`
- Split: `documentation_04`

Input:

```text
如果你使用 ExternalName Service，那么集群内客户端使用的主机名与 ExternalName 引用的名称不同。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0224

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0224`
- Split: `documentation_04`

Input:

```text
对于在集群内运行的客户端，Kubernetes 支持两种主要的服务发现模式：环境变量和 DNS。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### kubernetes-docs-zh-cn-v1/page-04-sentence-0259

- Source: `kubernetes-docs-zh-cn-v1`
- Source case: `page-04-sentence-0259`
- Split: `documentation_04`

Input:

```text
在下面的例子中，名为 `my-service` 的 Service 可以在 "`198.51.100.32:80`" （根据 `.spec.externalIPs[]` 和 `.spec.ports[].port` 得出）上被客户端使用 TCP 协议访问。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-015

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-015`
- Split: `guide`

Input:

```text
大多数社区面临多种类型的危险。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-016

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-016`
- Split: `guide`

Input:

```text
重要的是要了解您的住房的具体风险以及如果离家时，则应如何评估风险。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-035

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-035`
- Split: `guide`

Input:

```text
所有灾难的基本保护措施在灾难发生之前、期间和之后灾难发生之前、期间和之后，您可以采取可靠的措施或“保护措施”“保护措施”来保护家庭和财产安全。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-040

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-040`
- Split: `guide`

Input:

```text
制定一个家庭灾难计划个家庭灾难计划并演习该计划。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-069

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-069`
- Split: `guide`

Input:

```text
参加培训课程以学习急救技能，包括如何止血和进行 C P R（心肺复苏术）。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-078

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-078`
- Split: `guide`

Input:

```text
参加培训课程，学习如何识别危险情况，要避免的地方以及正确使用安全和救援设备的方法。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-081

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-081`
- Split: `guide`

Input:

```text
避免高风险区域，例如坡度大于30度的山坡或陡峭的下坡区域。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-083

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-083`
- Split: `guide`

Input:

```text
携带可折叠的雪崩探针和小铲，以帮助营救他人。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-108

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-108`
- Split: `guide`

Input:

```text
如果您被困，则发送短信或在水管或墙壁上敲打。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-151

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-151`
- Split: `guide`

Input:

```text
避开地下室和较低楼层，但不要爬进封闭的阁楼，因为如果洪水涨高，您可能会被困其中。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-183

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-183`
- Split: `guide`

Input:

```text
一旦泥流发生或泥石流，您可能无法逃脱，因此请远离泥石流外围。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-215

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-215`
- Split: `guide`

Input:

```text
停电时规划用电池和其他替代产品，来满足停电时的需求。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-229

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-229`
- Split: `guide`

Input:

```text
扔掉所有暴露于40度或更高温度下两个小时以上，或有异味、变色或变质的食物。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-230

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-230`
- Split: `guide`

Input:

```text
如果停电超过一天，请丢弃所有应冷藏的药品，除非药品标签上另有说明。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-254

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-254`
- Split: `guide`

Input:

```text
国家气象局对特定危害的“警戒”和“警告”定义有所不同，如在 Weather.gov所述。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-256

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-256`
- Split: `guide`

Input:

```text
认真遵守警戒和警告，以了解接下来要采取的措施。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-280

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-280`
- Split: `guide`

Input:

```text
测试每个口罩以确保能够紧密贴合面部。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-296

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-296`
- Split: `guide`

Input:

```text
冬季风暴 • 使用绝缘材料、填缝剂和挡风雨条为房屋做好防寒准备。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-313

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-313`
- Split: `guide`

Input:

```text
还应该设置一个州外联络点，如果本地通讯无法使用，家人可以通过该人分享最新情况。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-343

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-343`
- Split: `guide`

Input:

```text
警惕道路危险，例如被冲毁的道路或桥梁以及掉落的电线。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-346

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-346`
- Split: `guide`

Input:

```text
在撤离期间，请随身携带应急用品包。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-377

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-377`
- Split: `guide`

Input:

```text
如果您需要留在原处，则为车辆和工作场所准备单独小套的应急用品，至少可以维持 24 小时。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-404

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-404`
- Split: `guide`

Input:

```text
有些可能有移动应用程序，以确保灾难发生时您可以接收信息。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-432

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-432`
- Split: `guide`

Input:

```text
只有洪水保险才能防止洪水造成的情感和经济毁坏。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-467

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-467`
- Split: `guide`

Input:

```text
换新应急物资用品（至少每六个月一次）。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-470

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-470`
- Split: `guide`

Input:

```text
进行保险检查. 以下是为实施防灾计划而建议的一年时间表: 以下是为实施防灾计划而建议的一年时间表: 第1个月：第1个月：登记参加心肺复苏术（CPR）和急救培训，以及所在地区或在线提供的其他特定危害的培训。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-472

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-472`
- Split: `guide`

Input:

```text
购买洪水保险或其他有关的保险。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-496

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-496`
- Split: `guide`

Input:

```text
应该尽快提出保险索赔，了解预期，减少不确定性。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-505

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-505`
- Split: `guide`

Input:

```text
为安全起见，请等到地方当局表示可以返回时方可返乡。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-545

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-545`
- Split: `guide`

Input:

```text
应对灾难灾难可能会对您和家人的心理健康产生重大影响，尤其是如果您的房屋、生意或个人财产遭到损毁时。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-562

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-562`
- Split: `guide`

Input:

```text
FEMA的衬衫或联邦小企业管理局（SBA）工作外套不是绝对的身份证明。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### ready-gov-are-you-ready-guide-simplified-v1/sentence-570

- Source: `ready-gov-are-you-ready-guide-simplified-v1`
- Source case: `sentence-570`
- Split: `guide`

Input:

```text
FEMA 和 SBA的工作人员从不为灾难帮助、检查或填写申请表向申请人收费。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-003

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-003`
- Split: `project_original`

Input:

```text
审计单位将抽查原始凭证与付款授权记录。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-004

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-004`
- Split: `project_original`

Input:

```text
主管机关说明这项统计不包含尚未结案的申请。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-005

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-005`
- Split: `project_original`

Input:

```text
法院公告载明裁定主文与救济期限。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-006

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-006`
- Split: `project_original`

Input:

```text
研究人员公开问卷设计及样本筛选条件。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-008

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-008`
- Split: `project_original`

Input:

```text
评审小组将利益冲突声明纳入会议档案。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-010

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-010`
- Split: `project_original`

Input:

```text
申请人须说明资料缺漏的原因及补正方式。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-012

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-012`
- Split: `project_original`

Input:

```text
调查人员分别记录目击者陈述与客观证据。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-014

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-014`
- Split: `project_original`

Input:

```text
听证纪录应标示发言者身份及发言顺序。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-016

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-016`
- Split: `project_original`

Input:

```text
采购文件要求厂商保存材料来源证明。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-023

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-023`
- Split: `project_original`

Input:

```text
决议附件列明各单位负责的工作项目。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-027

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-027`
- Split: `project_original`

Input:

```text
委员会决定补充征询受影响团体的意见。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-028

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-028`
- Split: `project_original`

Input:

```text
公告同时提供修正理由和条文对照表。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-029

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-029`
- Split: `project_original`

Input:

```text
财政报告将一次性收入与经常性收入分开计算。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-038

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-038`
- Split: `project_original`

Input:

```text
申请资料中的名称应以核定文件为准。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/formal-040

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `formal-040`
- Split: `project_original`

Input:

```text
调查小组未取得授权前不得公开个人资料。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-005

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-005`
- Split: `project_original`

Input:

```text
评测器会检查回答是否误用过期版本。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-006

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-006`
- Split: `project_original`

Input:

```text
系统将工具结果与模型推论分开记录。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-007

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-007`
- Split: `project_original`

Input:

```text
提示词中的示例不代表使用者的真实资料。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-008

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-008`
- Split: `project_original`

Input:

```text
模型应保留引文中的产品名称和版本编号。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-012

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-012`
- Split: `project_original`

Input:

```text
助理应先确认来源是否真的讨论同一对象。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-014

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-014`
- Split: `project_original`

Input:

```text
模型不得把搜索结果标题当成完整证据。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-015

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-015`
- Split: `project_original`

Input:

```text
引用网页时应保留原始发布时间与更新日期。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-024

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-024`
- Split: `project_original`

Input:

```text
助理不能根据档名猜测文件的实际内容。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-027

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-027`
- Split: `project_original`

Input:

```text
评测报告分别统计有依据和无依据的回答。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-030

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-030`
- Split: `project_original`

Input:

```text
系统会比较多个来源对同一事件的描述。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-032

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-032`
- Split: `project_original`

Input:

```text
工具输出被截断时回答必须说明这个限制。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-036

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-036`
- Split: `project_original`

Input:

```text
回答中的日期必须对应来源所在的时区。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-037

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-037`
- Split: `project_original`

Input:

```text
检索摘要不能取代原始文件的正式内容。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-038

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-038`
- Split: `project_original`

Input:

```text
助理会把未经证实的说法标成待查资料。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-040

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-040`
- Split: `project_original`

Input:

```text
模型需要保留命令范例中的引号和选项顺序。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-044

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-044`
- Split: `project_original`

Input:

```text
模型不得将假设情境描述成已经发生的事件。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-formal-llm-evidence-guard-v1/llm-046

- Source: `zhtw-project-formal-llm-evidence-guard-v1`
- Source case: `llm-046`
- Split: `project_original`

Input:

```text
检索器应优先返回能够追溯来源的文件。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```
