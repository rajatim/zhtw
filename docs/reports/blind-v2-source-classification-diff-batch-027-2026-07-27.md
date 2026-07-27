<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 027 (2026-07-27)

Status: advisory only; maintainer decisions pending

Packet SHA-256: `ca11a9bd4a724a5e36df6aef1bcddec240ab54fc4dcb012366efcdc8a5ad660c`
Cases: 100
Exact Codex/Gemini classifications: 1
Maintainer review queue: 99

Field differences:

- Eligibility: 7
- Script: 80
- Domain: 7
- Risk: 73

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

Neither advisory is auto-preferred. Codex must synthesize the differences before maintainer confirmation; no classification in this report has been written into the candidate pool.

## Review Queue

### 01. kubernetes-docs-zh-cn-v1/page-01-sentence-0008

Changed: `script, risk`

Input:

```text
当对象所代表的是一个物理实体（例如代表一台物理主机的 Node）时，如果在 Node 对象未被删除并重建的条件下，重新创建了同名的物理主机，则 Kubernetes 会将新的主机看作是老的主机，这可能会带来某种不一致性。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 標準 Kubernetes 技術文件句子，測試「物理實體」、「主機」、「對象」等術語轉換。

Maintainer decision: `pending`

### 02. kubernetes-docs-zh-cn-v1/page-01-sentence-0009

Changed: `script, risk`

Input:

```text
当在资源创建请求中提供 `generateName` 而不是 `name` 时，服务器可能会生成一个名称。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「資源」、「請求」、「伺服器」等常見術語。

Maintainer decision: `pending`

### 03. kubernetes-docs-zh-cn-v1/page-01-sentence-0024

Changed: `script, risk`

Input:

```text
Kubernetes UID 是全局唯一标识符（也叫 UUID）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 簡單術語定義，測試「全局唯一標識符」。

Maintainer decision: `pending`

### 04. kubernetes-docs-zh-cn-v1/page-02-sentence-0004

Changed: `script, risk`

Input:

```text
应该只使用一种技术来管理 Kubernetes 对象。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 基礎句，測試「技術」、「管理」、「對象」。

Maintainer decision: `pending`

### 05. kubernetes-docs-zh-cn-v1/page-02-sentence-0005

Changed: `risk`

Input:

```text
混合和匹配技术作用在同一对象上将导致未定义行为。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「匹配」、「對象」與「行為」，防止過度轉換。

Maintainer decision: `pending`

### 06. kubernetes-docs-zh-cn-v1/page-02-sentence-0013

Changed: `risk`

Input:

```text
除了实时内容外，命令不提供记录源。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「實時」、「內容」、「記錄源」等詞彙。

Maintainer decision: `pending`

### 07. kubernetes-docs-zh-cn-v1/page-02-sentence-0020

Changed: `script`

Input:

```text
比如类型为 `LoadBalancer` 的服务，它的 `externalIPs` 字段就是独立于集群配置进行更新。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 包含 `LoadBalancer`、`externalIPs` 等程式碼，測試術語「類型」、「服務」、「集群」、「配置」且不轉換程式碼。

Maintainer decision: `pending`

### 08. kubernetes-docs-zh-cn-v1/page-02-sentence-0026

Changed: `risk`

Input:

```text
指令式对象配置行为更加简单易懂。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「指令式」、「對象配置」、「行為」的轉換。

Maintainer decision: `pending`

### 09. kubernetes-docs-zh-cn-v1/page-02-sentence-0035

Changed: `script, risk`

Input:

```text
处理 `configs` 目录中的所有对象配置文件，创建并更新活跃对象。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「對象配置文件」、「創建」、「更新」、「活躍對象」等動詞與名詞。

Maintainer decision: `pending`

### 10. kubernetes-docs-zh-cn-v1/page-02-sentence-0036

Changed: `risk`

Input:

```text
对活动对象所做的更改即使未合并到配置文件中，也会被保留下来。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「更改」、「合併」等詞，確保語意正確。

Maintainer decision: `pending`

### 11. kubernetes-docs-zh-cn-v1/page-03-sentence-0004

Changed: `script, risk`

Input:

```text
Pod 会被创建、赋予一个唯一的 ID（UID），并被调度到节点，并在终止（根据重启策略）或删除之前一直运行在该节点。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 包含 Pod 生命週期術語，測試「調度」、「節點」、「終止」、「重啟策略」。

Maintainer decision: `pending`

### 12. kubernetes-docs-zh-cn-v1/page-03-sentence-0013

Changed: `script, risk`

Input:

```text
一旦 Pod 被调度并绑定到某个节点，Kubernetes 会尝试在该节点上运行 Pod。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「調度」、「綁定」、「節點」等術語。

Maintainer decision: `pending`

### 13. kubernetes-docs-zh-cn-v1/page-03-sentence-0022

Changed: `script`

Input:

```text
Kubernetes 使用一种高级抽象来管理这些相对而言可随时丢弃的 Pod 实例，称作。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | no | null | null | high | fragment |

Codex reason: Markdown 结构或链接文字移除后成为残句、列表片段或格式残留，离开上下文后不适合独立裁决。

Gemini reason: 句子以「稱作。」結尾，不完整，屬於片段。

Maintainer decision: `pending`

### 14. kubernetes-docs-zh-cn-v1/page-03-sentence-0031

Changed: `script, risk`

Input:

```text
Pod 阶段的数量和含义是严格定义的。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「階段」、「數量」、「含義」的轉換。

Maintainer decision: `pending`

### 15. kubernetes-docs-zh-cn-v1/page-03-sentence-0035

Changed: `eligible, script, domain, risk`

Input:

```text
`Running`（运行中） | Pod 已经绑定到了某个节点，Pod 中所有的容器都已被创建。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Markdown 结构或链接文字移除后成为残句、列表片段或格式残留，离开上下文后不适合独立裁决。

Gemini reason: 表格內容，測試「綁定」、「節點」、「容器」等基本術語。

Maintainer decision: `pending`

### 16. kubernetes-docs-zh-cn-v1/page-03-sentence-0046

Changed: `script, risk`

Input:

```text
Pod 被赋予一个可以体面终止的期限，默认为 30 秒。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試術語「體面終止」、「期限」，此為 Kubernetes 特定概念。

Maintainer decision: `pending`

### 17. kubernetes-docs-zh-cn-v1/page-03-sentence-0050

Changed: `script, risk`

Input:

```text
Kubernetes 会跟踪 Pod 中每个容器的状态，就像它跟踪 Pod 总体上的阶段一样。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「跟蹤」、「容器」、「狀態」、「階段」。

Maintainer decision: `pending`

### 18. kubernetes-docs-zh-cn-v1/page-03-sentence-0057

Changed: `script`

Input:

```text
处于 `Waiting` 状态的容器仍在运行它完成启动所需要的操作：例如，从某个容器镜像仓库拉取容器镜像，或者向容器应用数据等等。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「容器鏡像倉庫」、「拉取」、「應用Secret」，確保術語轉換準確。

Maintainer decision: `pending`

### 19. kubernetes-docs-zh-cn-v1/page-03-sentence-0069

Changed: `script, risk`

Input:

```text
CrashLoopBackOff 状态：这一状态表明，对于一个给定的、处于崩溃循环、反复失效并重启的容器，回退延迟机制目前正在生效。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 包含特定狀態 `CrashLoopBackOff` 及其中文描述「崩潰循環」、「回退延遲」，可測試新術語覆蓋。

Maintainer decision: `pending`

### 20. kubernetes-docs-zh-cn-v1/page-03-sentence-0075

Changed: `eligible, domain, risk`

Input:

```text
应用程序错误导致的容器退出。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Markdown 结构或链接文字移除后成为残句、列表片段或格式残留，离开上下文后不适合独立裁决。

Gemini reason: 測試「應用程式」、「錯誤」、「退出」。

Maintainer decision: `pending`

### 21. kubernetes-docs-zh-cn-v1/page-03-sentence-0076

Changed: `eligible, domain, risk`

Input:

```text
配置错误，如环境变量不正确或配置文件丢失。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Markdown 结构或链接文字移除后成为残句、列表片段或格式残留，离开上下文后不适合独立裁决。

Gemini reason: 測試「配置錯誤」、「環境變數」、「配置文件」。

Maintainer decision: `pending`

### 22. kubernetes-docs-zh-cn-v1/page-03-sentence-0077

Changed: `script`

Input:

```text
资源限制，容器可能没有足够的内存或 CPU 正常启动。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 主题句结构完整，明确说明资源限制与容器启动的关系，可独立裁决。

Gemini reason: 測試「資源限制」、「內存」、「CPU」。

Maintainer decision: `pending`

### 23. kubernetes-docs-zh-cn-v1/page-03-sentence-0097

Changed: `script, risk`

Input:

```text
对于因错误而退出的 Init 容器，如果 Pod 级别 `restartPolicy` 为 `OnFailure` 或 `Always`，则 kubelet 会重新启动 Init 容器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試 Init 容器與 `restartPolicy` 的相關描述。

Maintainer decision: `pending`

### 24. kubernetes-docs-zh-cn-v1/page-03-sentence-0100

Changed: `script, risk`

Input:

```text
`Never`：不会自动重启已终止的容器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試 `Never` 策略的描述轉換。

Maintainer decision: `pending`

### 25. kubernetes-docs-zh-cn-v1/page-03-sentence-0110

Changed: `eligible, script, domain, risk`

Input:

```text
容器重启策略和规则适用于 Pod 中的以及常规的 Init 容器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Markdown 结构或链接文字移除后成为残句、列表片段或格式残留，离开上下文后不适合独立裁决。

Gemini reason: 測試「常規的」Init 容器的說法，避免過度或錯誤轉換。

Maintainer decision: `pending`

### 26. kubernetes-docs-zh-cn-v1/page-03-sentence-0137

Changed: `script, risk`

Input:

```text
配置的 `terminationGracePeriodSeconds` 不会生效，配置的所有 `preStop` 回调也不会被执行。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 包含 `terminationGracePeriodSeconds` 和 `preStop` 回調，測試 K8s API 欄位名的處理。

Maintainer decision: `pending`

### 27. kubernetes-docs-zh-cn-v1/page-03-sentence-0151

Changed: `script, risk`

Input:

```text
启用 Alpha 特性开关 `ReduceDefaultCrashLoopBackOffDecay` 后，集群中容器启动重试的初始延迟将从 10 秒减少到 1 秒，之后每次重启延迟时间按 2 倍指数增长，直到达到最大延迟 60 秒（之前为 300 秒，即 5 分钟）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 包含 Alpha 特性開關 `ReduceDefaultCrashLoopBackOffDecay`，測試對新功能術語的處理。

Maintainer decision: `pending`

### 28. kubernetes-docs-zh-cn-v1/page-03-sentence-0158

Changed: `script, risk`

Input:

```text
如果你将此特性与上文提到的 Alpha 特性 `ReduceDefaultCrashLoopBackOffDecay` 一起使用，那么集群的初始退避时间和最大退避时间默认值将不再是 10 秒和 300 秒，而是 1 秒和 60 秒。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 再次提及 Alpha 特性，測試「初始退避」、「最大退避」等專有術語。

Maintainer decision: `pending`

### 29. kubernetes-docs-zh-cn-v1/page-03-sentence-0166

Changed: `script, risk`

Input:

```text
`PodResizeInProgress`：Pod 正在调整大小中。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: `PodResizeInProgress` 是特定 Pod 狀況，測試新術語。

Maintainer decision: `pending`

### 30. kubernetes-docs-zh-cn-v1/page-03-sentence-0167

Changed: `script, risk`

Input:

```text
你的应用可以向 PodStatus 中注入额外的反馈或者信号：Pod Readiness（Pod 就绪态）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 提及 `Pod Readiness` (Pod 就緒態)，是很好的術語轉換測試案例。

Maintainer decision: `pending`

### 31. kubernetes-docs-zh-cn-v1/page-03-sentence-0179

Changed: `eligible, script, domain, risk`

Input:

```text
一旦这些阶段完成，Kubelet 将与容器运行时（使用）一起为 Pod 生成运行时沙箱并配置网络。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Markdown 结构或链接文字移除后成为残句、列表片段或格式残留，离开上下文后不适合独立裁决。

Gemini reason: 包含「容器運行時」、「沙箱」、「配置網路」等術語，測試組合詞的轉換。

Maintainer decision: `pending`

### 32. kubernetes-docs-zh-cn-v1/page-03-sentence-0186

Changed: `script`

Input:

```text
对于带有 Init 容器的 Pod，kubelet 会在 Init 容器成功完成后将 `Initialized` 状况设置为 `True` （这发生在运行时成功创建沙箱和配置网络之后），对于没有 Init 容器的 Pod，kubelet 会在创建沙箱和网络配置开始之前将 `Initialized` 状况设置为 `True`。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 複雜長句，包含 Init 容器、`Initialized` 狀況、沙箱、網路配置，測試複雜邏輯描述的準確性。

Maintainer decision: `pending`

### 33. kubernetes-docs-zh-cn-v1/page-03-sentence-0190

Changed: `script, risk`

Input:

```text
这亦被称为原地 Pod 垂直扩缩。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 「原地 Pod 垂直擴縮」是 Kubernetes 的特定術語，適合測試詞庫覆蓋。

Maintainer decision: `pending`

### 34. kubernetes-docs-zh-cn-v1/page-03-sentence-0191

Changed: `risk`

Input:

```text
这允许你在可能避免应用程序中断的同时，调整运行容器的资源配置。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「應用程式中斷」、「調整」、「資源配置」。

Maintainer decision: `pending`

### 35. kubernetes-docs-zh-cn-v1/page-03-sentence-0193

Changed: `script, risk`

Input:

```text
然后，kubelet 会尝试将新的资源值应用到运行中的容器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「應用」、「資源值」、「運行中容器」。

Maintainer decision: `pending`

### 36. kubernetes-docs-zh-cn-v1/page-03-sentence-0195

Changed: `risk`

Input:

```text
有关调整大小状态的更多详情，请参见容器调整大小状态。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「調整大小狀態」的轉換。

Maintainer decision: `pending`

### 37. kubernetes-docs-zh-cn-v1/page-03-sentence-0198

Changed: `script`

Input:

```text
你可以使用容器规约中的 `resizePolicy` 配置是否需要重启容器以进行调整大小。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 包含 API 欄位 `resizePolicy`，測試「容器規約」、「重啟」等術語。

Maintainer decision: `pending`

### 38. kubernetes-docs-zh-cn-v1/page-03-sentence-0208

Changed: `script`

Input:

```text
probe 是由 kubelet 对容器执行的定期诊断。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 「probe」被翻譯為「探針」，是關鍵術語，測試「定期診斷」。

Maintainer decision: `pending`

### 39. kubernetes-docs-zh-cn-v1/page-03-sentence-0212

Changed: `risk`

Input:

```text
如果命令退出时返回码为 0 则认为诊断成功。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「命令」、「退出」、「返回碼」的轉換。

Maintainer decision: `pending`

### 40. kubernetes-docs-zh-cn-v1/page-03-sentence-0216

Changed: `script`

Input:

```text
`httpGet` : 对容器的 IP 地址上指定端口和路径执行 HTTP `GET` 请求。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 包含 `httpGet`，測試「IP 地址」、「端口」、「路徑」、「HTTP GET 請求」。

Maintainer decision: `pending`

### 41. kubernetes-docs-zh-cn-v1/page-03-sentence-0228

Changed: `script, risk`

Input:

```text
`livenessProbe` : 指示容器是否正在运行。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: `livenessProbe` (存活態探針) 是 Kubernetes 的核心概念，測試術語準確性。

Maintainer decision: `pending`

### 42. kubernetes-docs-zh-cn-v1/page-03-sentence-0231

Changed: `script, risk`

Input:

```text
`readinessProbe` : 指示容器是否准备好为请求提供服务。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: `readinessProbe` (就緒態探針) 是 Kubernetes 的核心概念，測試術語準確性。

Maintainer decision: `pending`

### 43. kubernetes-docs-zh-cn-v1/page-03-sentence-0239

Changed: `risk`

Input:

```text
如欲了解如何设置存活态、就绪态和启动探针的进一步细节，可以参阅配置存活态、就绪态和启动探针。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「存活態」、「就緒態」、「啟動探針」等術語的組合。

Maintainer decision: `pending`

### 44. kubernetes-docs-zh-cn-v1/page-03-sentence-0249

Changed: `risk`

Input:

```text
然而，如果你想区分已经失败的应用和仍在处理其启动数据的应用，你可能更倾向于使用就绪探针。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「區分」、「啟動數據」、「就緒探針」等詞的準確性。

Maintainer decision: `pending`

### 45. kubernetes-docs-zh-cn-v1/page-03-sentence-0250

Changed: `script`

Input:

```text
请注意，如果你只是想在 Pod 被删除时能够排空请求，则不一定需要使用就绪态探针；当 Pod 被删除时，`EndpointSlice` 中对应的端点会更新其状况：该端点的 `ready` 状况将被设置为 `false`，因此负载均衡器不会再将该 Pod 用于常规流量。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 長句，包含 `EndpointSlice`、`ready` 狀況、負載均衡器等，是很好的綜合性過度轉換防護案例。

Maintainer decision: `pending`

### 46. kubernetes-docs-zh-cn-v1/page-03-sentence-0253

Changed: `risk`

Input:

```text
你不再需要配置一个较长的存活态探测时间间隔，只需要设置另一个独立的配置选定，对启动期间的容器执行探测，从而允许使用远远超出存活态时间间隔所允许的时长。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「存活態探測時間間隔」、「配置」、「執行探測」。

Maintainer decision: `pending`

### 47. kubernetes-docs-zh-cn-v1/page-03-sentence-0254

Changed: `script`

Input:

```text
如果你的容器启动时间通常超出 \\( initialDelaySeconds + failureThreshold \times periodSeconds \\) 总值，你应该设置一个启动探测，对存活态探针所使用的同一端点执行检查。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 包含公式 `initialDelaySeconds + failureThreshold \times periodSeconds`，測試含 LaTeX 格式的文本處理。

Maintainer decision: `pending`

### 48. kubernetes-docs-zh-cn-v1/page-03-sentence-0264

Changed: `risk`

Input:

```text
停止容器的这些请求由容器运行时以异步方式处理。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「停止容器」、「請求」、「容器運行時」、「異步方式」。

Maintainer decision: `pending`

### 49. kubernetes-docs-zh-cn-v1/page-03-sentence-0275

Changed: `risk`

Input:

```text
如果在生命周期中定义了终止信号，则会覆盖容器镜像中定义的信号。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「生命週期」、「終止信號」、「覆蓋」、「容器鏡像」。

Maintainer decision: `pending`

### 50. kubernetes-docs-zh-cn-v1/page-03-sentence-0276

Changed: `risk`

Input:

```text
如果容器规约中未定义终止信号，则容器将回退到默认行为。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「容器規約」、「回退到」、「默認行為」。

Maintainer decision: `pending`

### 51. kubernetes-docs-zh-cn-v1/page-03-sentence-0277

Changed: `script`

Input:

```text
你使用 `kubectl` 工具手动删除某个特定的 Pod，而该 Pod 的体面终止限期是默认值（30 秒）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「體面終止限期」，確保其作為一個整體術語被正確轉換。

Maintainer decision: `pending`

### 52. kubernetes-docs-zh-cn-v1/page-03-sentence-0279

Changed: `script, risk`

Input:

```text
如果你使用 `kubectl describe` 来查验你正在删除的 Pod，该 Pod 会显示为 "Terminating" （正在终止）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試 `kubectl describe` 和 Pod 狀態 `Terminating`（正在終止）的描述。

Maintainer decision: `pending`

### 53. kubernetes-docs-zh-cn-v1/page-03-sentence-0283

Changed: `script`

Input:

```text
如果 `preStop` 回调所需要的时间长于默认的体面终止限期，你必须修改 `terminationGracePeriodSeconds` 属性值来使其正常工作。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 包含 `preStop` 和 `terminationGracePeriodSeconds`，測試 API 欄位與中文術語的混合。

Maintainer decision: `pending`

### 54. kubernetes-docs-zh-cn-v1/page-03-sentence-0286

Changed: `script, risk`

Input:

```text
否则，Pod 中的容器会在不同的时间和任意的顺序接收 TERM 信号。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「任意的順序」、「接收」、「TERM 信號」。

Maintainer decision: `pending`

### 55. kubernetes-docs-zh-cn-v1/page-03-sentence-0299

Changed: `script, risk`

Input:

```text
`kubelet` 将 Pod 转换到终止阶段（`Failed` 或 `Succeeded`，具体取决于其容器的结束状态）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試 Pod 終止階段 `Failed` 和 `Succeeded` 的描述。

Maintainer decision: `pending`

### 56. kubernetes-docs-zh-cn-v1/page-03-sentence-0308

Changed: `script, risk`

Input:

```text
执行强制删除操作时，API 服务器不再等待来自 `kubelet` 的、关于 Pod 已经在原来运行的节点上终止执行的确认消息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「強制刪除」、「API 伺服器」、「確認消息」。

Maintainer decision: `pending`

### 57. kubernetes-docs-zh-cn-v1/page-03-sentence-0319

Changed: `script`

Input:

```text
在这种情况下，Pod 中所有剩余的容器将在某个短宽限期内被同时终止。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「寬限期」這一術語的轉換。

Maintainer decision: `pending`

### 58. kubernetes-docs-zh-cn-v1/page-03-sentence-0326

Changed: `script, risk`

Input:

```text
在清理 Pod 的同时，如果它们处于非终止状态阶段，PodGC 也会将它们标记为失败。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: PodGC 是 Kubernetes 中的一個控制器，測試對這種縮寫組件名的處理。

Maintainer decision: `pending`

### 59. kubernetes-docs-zh-cn-v1/page-03-sentence-0336

Changed: `script`

Input:

```text
之前设置为 `ready: true` 状态的容器仍然保持就绪。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試 `ready: true` 狀態和「就緒」的表述。

Maintainer decision: `pending`

### 60. kubernetes-docs-zh-cn-v1/page-04-sentence-0001

Changed: `script, risk`

Input:

```text
Kubernetes 中 Service 的一个关键目标是让你无需修改现有应用以使用某种不熟悉的服务发现机制。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: Kubernetes Service 的目標描述，測試「服務發現機制」。

Maintainer decision: `pending`

### 61. kubernetes-docs-zh-cn-v1/page-04-sentence-0025

Changed: `eligible, script, domain, risk`

Input:

```text
如果你想要在自己的应用中使用 Kubernetes API 进行服务发现，可以查询，寻找匹配的 EndpointSlice 对象。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Markdown 结构或链接文字移除后成为残句、列表片段或格式残留，离开上下文后不适合独立裁决。

Gemini reason: 包含 Kubernetes API 和 `EndpointSlice`，測試術語和 API 對象的處理。

Maintainer decision: `pending`

### 62. kubernetes-docs-zh-cn-v1/page-04-sentence-0027

Changed: `script, risk`

Input:

```text
对于非本地应用，Kubernetes 提供了在应用和后端 Pod 之间放置网络端口或负载均衡器的方法。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「非本地應用」、「後端 Pod」、「網絡端口」、「負載均衡器」。

Maintainer decision: `pending`

### 63. kubernetes-docs-zh-cn-v1/page-04-sentence-0028

Changed: `risk`

Input:

```text
无论采用那种方式，你的负载都可以使用这里的服务发现机制找到希望连接的目标。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「負載」、「服務發現機制」、「連接」、「目標」。

Maintainer decision: `pending`

### 64. kubernetes-docs-zh-cn-v1/page-04-sentence-0032

Changed: `script`

Input:

```text
例如，假定有一组 Pod，每个 Pod 都在侦听 TCP 端口 9376，并且它们还被打上 `app.kubernetes.io/name=MyApp` 标签。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 包含標籤 `app.kubernetes.io/name=MyApp`，測試包含標籤的句子。

Maintainer decision: `pending`

### 65. kubernetes-docs-zh-cn-v1/page-04-sentence-0039

Changed: `script, risk`

Input:

```text
Service 对象的名称必须是有效的 RFC 1035 标签名称。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 提及 RFC 1035，測試標準文檔引用。

Maintainer decision: `pending`

### 66. kubernetes-docs-zh-cn-v1/page-04-sentence-0040

Changed: `script`

Input:

```text
Service 能够将任意入站 `port` 映射到某个 `targetPort`。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: `port` 和 `targetPort` 的映射關係，測試對 API 欄位名的處理。

Maintainer decision: `pending`

### 67. kubernetes-docs-zh-cn-v1/page-04-sentence-0041

Changed: `script`

Input:

```text
默认情况下，出于方便考虑，`targetPort` 会被设置为与 `port` 字段相同的值。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 「出於方便考慮」的說法以及 `targetPort` 與 `port` 的關係，防止過度轉換。

Maintainer decision: `pending`

### 68. kubernetes-docs-zh-cn-v1/page-04-sentence-0047

Changed: `script, risk`

Input:

```text
例如，你可以在后端软件的新版本中更改 Pod 公开的端口号，但不会影响到客户端。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「後端軟體」、「新版本」、「端口號」。

Maintainer decision: `pending`

### 69. kubernetes-docs-zh-cn-v1/page-04-sentence-0052

Changed: `risk`

Input:

```text
你希望在生产环境中使用外部数据库集群，但在测试环境中使用自己的数据库。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「生產環境」、「測試環境」、「數據庫集群」。

Maintainer decision: `pending`

### 70. kubernetes-docs-zh-cn-v1/page-04-sentence-0065

Changed: `risk`

Input:

```text
如果你使用的是第三方工具，请使用全小写的工具名称，并将空格和其他标点符号更改为短划线（`-`）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 關於工具命名的約定，測試「全小寫」、「短劃線」。

Maintainer decision: `pending`

### 71. kubernetes-docs-zh-cn-v1/page-04-sentence-0079

Changed: `script`

Input:

```text
在需要添加额外的端点之前，Kubernetes 不会创建新的 EndpointSlice。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: `EndpointSlice` 和「額外端點」的關係，是很好的術語測試。

Maintainer decision: `pending`

### 72. kubernetes-docs-zh-cn-v1/page-04-sentence-0081

Changed: `script, risk`

Input:

```text
EndpointSlice API 是旧版 Endpoints API 的演进版本。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: `EndpointSlice` API 和 `Endpoints` API 的演進關係。

Maintainer decision: `pending`

### 73. kubernetes-docs-zh-cn-v1/page-04-sentence-0088

Changed: `script`

Input:

```text
如出现端点过多的情况，Kubernetes 选择最多 1000 个可能的后端端点存储到 Endpoints 对象中，并在 Endpoints 上设置 `endpoints.kubernetes.io/over-capacity: truncated`。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 包含註解 `endpoints.kubernetes.io/over-capacity: truncated`，測試含註解的文本。

Maintainer decision: `pending`

### 74. kubernetes-docs-zh-cn-v1/page-04-sentence-0090

Changed: `script, risk`

Input:

```text
请求流量仍会被发送到后端，但任何依赖旧版 Endpoints API 的负载均衡机制最多只能将流量发送到 1000 个可用的支撑端点。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「請求流量」、「後端」、「負載均衡機制」、「支撐端點」。

Maintainer decision: `pending`

### 75. kubernetes-docs-zh-cn-v1/page-04-sentence-0094

Changed: `script, risk`

Input:

```text
此字段的取值会被映射到对应的 Endpoints 和 EndpointSlice 对象中。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「字段」、「取值」、「映射」、「對應」。

Maintainer decision: `pending`

### 76. kubernetes-docs-zh-cn-v1/page-04-sentence-0110

Changed: `script`

Input:

```text
为了让 Service 可通过节点端口访问，Kubernetes 会为 Service 配置集群 IP 地址，相当于你请求了 `type: ClusterIP` 的 Service。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 包含 `type: ClusterIP`，測試「節點端口」、「集群 IP 地址」。

Maintainer decision: `pending`

### 77. kubernetes-docs-zh-cn-v1/page-04-sentence-0133

Changed: `script, risk`

Input:

```text
集群中的每个节点都将自己配置为监听所分配的端口，并将流量转发到与该 Service 关联的某个就绪端点。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「集群」、「節點」、「監聽」、「轉發流量」、「就緒端點」。

Maintainer decision: `pending`

### 78. kubernetes-docs-zh-cn-v1/page-04-sentence-0138

Changed: `script`

Input:

```text
你还必须使用有效的端口号，该端口号在配置用于 NodePort 的范围内。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試 NodePort 範圍和「有效端口號」的說法。

Maintainer decision: `pending`

### 79. kubernetes-docs-zh-cn-v1/page-04-sentence-0140

Changed: `eligible, script, domain, risk`

Input:

```text
当某个用于希望创建一个使用特定端口的 NodePort Service 时，该目标端口可能与另一个已经被分配的端口冲突。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Markdown 结构或链接文字移除后成为残句、列表片段或格式残留，离开上下文后不适合独立裁决。

Gemini reason: 測試 NodePort Service 端口衝突的描述。

Maintainer decision: `pending`

### 80. kubernetes-docs-zh-cn-v1/page-04-sentence-0163

Changed: `script`

Input:

```text
如果没有设置 `loadBalancerIP` 字段，平台将会给负载均衡器分配一个临时 IP。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: `loadBalancerIP` 和「臨時 IP」的描述，測試 API 欄位處理。

Maintainer decision: `pending`

### 81. kubernetes-docs-zh-cn-v1/page-04-sentence-0173

Changed: `script, risk`

Input:

```text
Kubernetes API 没有定义如何为 Kubernetes 托管负载均衡器实施运行状况检查，而是由云提供商（以及集成代码的实现人员）决定其行为。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「託管負載均衡器」、「實施」、「運行狀況檢查」、「雲提供商」。

Maintainer decision: `pending`

### 82. kubernetes-docs-zh-cn-v1/page-04-sentence-0194

Changed: `script`

Input:

```text
默认值是 "VIP"，意味着流量被传递到目的地设置为负载均衡器 IP 和端口的节点上。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試 `VIP` 和「目的地」等網路術語。

Maintainer decision: `pending`

### 83. kubernetes-docs-zh-cn-v1/page-04-sentence-0195

Changed: `script`

Input:

```text
如果流量被传递到节点，然后 DNAT 到 Pod，则目的地将被设置为节点的 IP 和节点端口；如果流量被直接传递到 Pod，则目的地将被设置为 Pod 的 IP 和端口。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試 DNAT、Pod IP、節點 IP 等網路轉發細節描述。

Maintainer decision: `pending`

### 84. kubernetes-docs-zh-cn-v1/page-04-sentence-0198

Changed: `script, risk`

Input:

```text
在水平分割（Split-Horizon）DNS 环境中，你需要两个 Service 才能将内部和外部流量都路由到你的端点。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「水平分割 DNS」環境的描述。

Maintainer decision: `pending`

### 85. kubernetes-docs-zh-cn-v1/page-04-sentence-0200

Changed: `script, risk`

Input:

```text
你可以使用 `spec.externalName` 参数指定这些 Service。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 包含 `spec.externalName`，測試 API 欄位。

Maintainer decision: `pending`

### 86. kubernetes-docs-zh-cn-v1/page-04-sentence-0202

Changed: `script, risk`

Input:

```text
类似于 IPv4 地址的外部名称无法被 DNS 服务器解析。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「IPv4 地址」、「外部名稱」、「DNS 伺服器」、「解析」。

Maintainer decision: `pending`

### 87. kubernetes-docs-zh-cn-v1/page-04-sentence-0209

Changed: `risk`

Input:

```text
对于使用主机名的协议，这一差异可能会导致错误或意外响应。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「主機名」、「協議」、「意外響應」。

Maintainer decision: `pending`

### 88. kubernetes-docs-zh-cn-v1/page-04-sentence-0216

Changed: `script`

Input:

```text
无头 Service 不使用虚拟 IP 地址和代理配置路由和数据包转发；相反，无头 Service 通过内部 DNS 记录报告各个 Pod 的端点 IP 地址，这些 DNS 记录是由集群的 DNS 服务所提供的。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 「無頭 Service」是關鍵術語，測試「虛擬 IP」、「代理配置」、「數據包轉發」。

Maintainer decision: `pending`

### 89. kubernetes-docs-zh-cn-v1/page-04-sentence-0220

Changed: `script, risk`

Input:

```text
对没有定义选择算符的无头 Service，控制平面不会创建 EndpointSlice 对象。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「選擇算符」、「無頭 Service」、「控制平面」、「EndpointSlice」。

Maintainer decision: `pending`

### 90. kubernetes-docs-zh-cn-v1/page-04-sentence-0221

Changed: `script`

Input:

```text
对于 `type: ExternalName` Service，查找和配置其 CNAME 记录；对所有其他类型的 Service，针对 Service 的就绪端点的所有 IP 地址，查找和配置 DNS A / AAAA 记录：对于 IPv4 端点，DNS 系统创建 A 记录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: `type: ExternalName`、CNAME、A / AAAA 記錄，網路和 DNS 術語密集。

Maintainer decision: `pending`

### 91. kubernetes-docs-zh-cn-v1/page-04-sentence-0222

Changed: `script, risk`

Input:

```text
对于 IPv6 端点，DNS 系统创建 AAAA 记录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: IPv6 端點和 AAAA 記錄的簡單描述。

Maintainer decision: `pending`

### 92. kubernetes-docs-zh-cn-v1/page-04-sentence-0227

Changed: `script, risk`

Input:

```text
这里 Service 的名称被转为大写字母，横线被转换成下划线。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: Service 名稱在環境變數中的轉換規則。

Maintainer decision: `pending`

### 93. kubernetes-docs-zh-cn-v1/page-04-sentence-0237

Changed: `script, risk`

Input:

```text
名字空间 `my-ns` 中的 Pod 应该能够通过按名检索 `my-service` 来找到 Service （`my-service.my-ns` 也可以）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試命名空間內 Service 名稱解析的描述。

Maintainer decision: `pending`

### 94. kubernetes-docs-zh-cn-v1/page-04-sentence-0244

Changed: `script, risk`

Input:

```text
阅读虚拟 IP 和 Service 代理以了解 Kubernetes 提供的使用虚拟 IP 地址公开 Service 的机制。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 測試「虛擬 IP」、「Service 代理」等術語。

Maintainer decision: `pending`

### 95. kubernetes-docs-zh-cn-v1/page-04-sentence-0247

Changed: `script, risk`

Input:

```text
`.spec.trafficDistribution` 字段提供了另一种影响 Kubernetes Service 内流量路由的方法。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: `.spec.trafficDistribution` 欄位的介紹。

Maintainer decision: `pending`

### 96. kubernetes-docs-zh-cn-v1/page-04-sentence-0260

Changed: `script, risk`

Input:

```text
Kubernetes 不负责管理 `externalIPs` 的分配，这一工作是集群管理员的职责。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: `externalIPs` 分配職責的說明。

Maintainer decision: `pending`

### 97. kubernetes-docs-zh-cn-v1/page-04-sentence-0261

Changed: `script, risk`

Input:

```text
Service 是 Kubernetes REST API 中的顶级资源。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: Service 作為 REST API 頂級資源的描述。

Maintainer decision: `pending`

### 98. kubernetes-docs-zh-cn-v1/page-04-sentence-0262

Changed: `script, risk`

Input:

```text
你可以找到有关 Service 对象 API 的更多详细信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: 簡單的引導性句子。

Maintainer decision: `pending`

### 99. kubernetes-docs-zh-cn-v1/page-04-sentence-0265

Changed: `script, risk`

Input:

```text
Gateway 作为 Kubernetes 的扩展提供比 Ingress 更高的灵活性。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；包含真实技术语境，适合检查术语转换与识别码保留。

Gemini reason: Gateway 和 Ingress 的比較。

Maintainer decision: `pending`
