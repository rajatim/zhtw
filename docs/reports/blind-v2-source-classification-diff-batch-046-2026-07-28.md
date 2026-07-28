<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 046 (2026-07-28)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `6de41a228a52b18a7eadefb8dc96408cc646b94c565ca9770c9a3fb6b1584e5c`
Cases: 96
Exact Codex/Gemini classifications: 19
Maintainer review queue: 77

Field differences:

- Eligibility: 8
- Script: 62
- Domain: 37
- Risk: 22

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

The maintainer resolved all 77 advisory disagreements and batch-confirmed the 19 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. kubernetes-docs-zh-cn-v1/page-01-sentence-0012

Changed: `script, risk`

Input:

```text
从 Kubernetes v1.31 及更高版本开始，这种情况发生的概率大大降低，因为服务器会尝试最多 8 次生成唯一名称，然后才返回 HTTP 409 响应。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Standard technical sentence. Terms like '服务器' (server), '概率' (probability), and '响应' (response) are common and this is a baseline conversion case.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 02. kubernetes-docs-zh-cn-v1/page-03-sentence-0032

Changed: `script`

Input:

```text
除了本文档中列举的内容外，不应该再假定 Pod 有其他的 `phase` 值。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: The identifiers 'Pod' and 'phase' are code literals that must not be converted or translated.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 03. kubernetes-docs-zh-cn-v1/page-03-sentence-0049

Changed: `script`

Input:

```text
如果某节点死掉或者与集群中其他节点失联，Kubernetes 会实施一种策略，将失去的节点上运行的所有 Pod 的 `phase` 设置为 `Failed`。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: The identifiers 'Pod', 'phase', and 'Failed' must be preserved. Also contains regional term candidates like '失联' (lost contact).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 04. kubernetes-docs-zh-cn-v1/page-03-sentence-0056

Changed: `script`

Input:

```text
如果容器并不处在 `Running` 或 `Terminated` 状态之一，它就处在 `Waiting` 状态。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: The state names 'Running', 'Terminated', and 'Waiting' are identifiers and must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 05. kubernetes-docs-zh-cn-v1/page-03-sentence-0060

Changed: `script, risk`

Input:

```text
如果配置了 `postStart` 回调，那么该回调已经执行且已完成。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: The term '回调' (callback) is a classic Mainland preference; Taiwan technical context often uses '回呼'. The identifier 'postStart' must also be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 06. kubernetes-docs-zh-cn-v1/page-03-sentence-0063

Changed: `script`

Input:

```text
如果你使用 `kubectl` 来查询包含 `Terminated` 状态的容器的 Pod 时，你会看到容器进入此状态的原因、退出代码以及容器执行期间的起止时间。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Contains the identifiers 'kubectl', 'Terminated', and 'Pod', which must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 07. kubernetes-docs-zh-cn-v1/page-03-sentence-0064

Changed: `script, risk`

Input:

```text
如果容器配置了 `preStop` 回调，则该回调会在容器进入 `Terminated` 状态之前执行。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Contains the term '回调' (callback), a candidate for localization to '回呼' in Taiwan, and identifiers 'preStop' and 'Terminated' which must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 08. kubernetes-docs-zh-cn-v1/page-03-sentence-0081

Changed: `eligible, domain, risk`

Input:

```text
这通常是诊断导致崩溃的问题的最直接方法。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 以「這通常是」承接前文方法，單句缺少明確指涉對象。

Gemini reason: '崩溃' (crash) is a Mainland-preferred term. Taiwan often uses '當機' for system/application crashes, although '崩潰' is also understood.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 09. kubernetes-docs-zh-cn-v1/page-03-sentence-0082

Changed: `eligible, domain, risk`

Input:

```text
检查事件：使用 `kubectl describe pod ` 查看 Pod 的事件，这可以提供有关配置或资源问题的提示。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 抽取後的 `kubectl describe pod ` 命令缺少必要 Pod 名稱或占位參數。

Gemini reason: The code snippet '`kubectl describe pod `' is a command and must not be altered. The term '配置' (configuration) is also a minor candidate_gap, as Taiwan often prefers '組態'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 10. kubernetes-docs-zh-cn-v1/page-03-sentence-0174

Changed: `script, risk`

Input:

```text
你可以使用 Kubernetes 客户端库之一来编写代码，针对 Pod 就绪态设置定制的 Pod 状况。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: This sentence contains multiple Mainland-specific IT terms requiring localization: '客户端库' (client library -> 用戶端函式庫), '就绪态' (readiness state -> 就緒狀態), '定制' (custom -> 自訂), '状况' (condition -> 狀況/狀態).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 11. kubernetes-docs-zh-cn-v1/page-03-sentence-0180

Changed: `risk`

Input:

```text
如果启用了 `PodReadyToStartContainersCondition` 特性门控（Kubernetes 版本中默认启用）， `PodReadyToStartContainers` 状况会被添加到 Pod 的 `status.conditions` 字段中。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Multiple Mainland-specific IT terms need localization: '特性门控' (feature gate), '默认' (default), '状况' (condition), and '字段' (field). The identifiers are over-conversion guards.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 12. kubernetes-docs-zh-cn-v1/page-03-sentence-0184

Changed: `risk`

Input:

```text
在运行时插件成功完成 Pod 的沙箱创建和网络配置后， kubelet 会将 `PodReadyToStartContainers` 状况设置为 `True`。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Mainland-specific IT terms requiring localization: '运行时插件' (runtime plugin), '网络' (network), and '状况' (condition).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 13. kubernetes-docs-zh-cn-v1/page-03-sentence-0202

Changed: `eligible, script, domain, risk`

Input:

```text
这种方法：适用于任何 Kubernetes 版本。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 「這種方法」缺少前文所指方法，且冒號後僅接適用範圍。

Gemini reason: A simple, standard sentence that mainly requires character-level conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 14. kubernetes-docs-zh-cn-v1/page-03-sentence-0220

Changed: `risk`

Input:

```text
如果端口打开，则诊断被认为是成功的。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: A straightforward sentence with common terms ('端口', '诊断') requiring standard character conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 15. kubernetes-docs-zh-cn-v1/page-03-sentence-0224

Changed: `eligible, domain, risk`

Input:

```text
这种场景下，请考虑使用其他探针机制以避免额外的开销。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 「這種場景」依賴前文診斷情境，無法由單句確認條件。

Gemini reason: The term '开销' (overhead) is a Mainland-specific IT term that needs to be localized for Taiwan (e.g., to '額外負擔').

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 16. kubernetes-docs-zh-cn-v1/page-03-sentence-0258

Changed: `script, risk`

Input:

```text
由于 Pod 所代表的是在集群中节点上运行的进程，当不再需要这些进程时允许其体面地终止是很重要的。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: The phrase '体面地终止' (graceful termination) requires careful localization to standard Taiwan IT terminology, e.g., '正常終止' or '優雅地終止'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 17. kubernetes-docs-zh-cn-v1/page-03-sentence-0289

Changed: `eligible, domain, risk`

Input:

```text
和其他工作负载资源不再将关闭进程中的 Pod 视为合法的、能够提供服务的副本。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 句子以「和其他工作負載資源」起首但缺少並列主體，抽取後語法不完整。

Gemini reason: Mainland-specific IT terms like '工作负载' (workload) and '副本' (replica) require localization for a Taiwan audience. `Pod` should be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 18. kubernetes-docs-zh-cn-v1/page-03-sentence-0301

Changed: `script, risk`

Input:

```text
API 服务器删除 Pod 的 API 对象，从任何客户端都无法再看到该对象。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Mainland term '服务器' (server) should be localized to '伺服器' for Taiwan. '客户端' (client) is often '用戶端'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 19. kubernetes-docs-zh-cn-v1/page-03-sentence-0306

Changed: `script`

Input:

```text
如果 Pod 仍然运行于某节点上，强制删除操作会触发 `kubelet` 立即执行清理操作。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: The identifier 'kubelet' must not be converted. '节点' (node) and '清理' (cleanup) are standard terms.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 20. kubernetes-docs-zh-cn-v1/page-04-sentence-0016

Changed: `eligible, script, domain, risk`

Input:

```text
Service 抽象使这种解耦成为可能。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 「這種解耦」依賴前文所述元件關係，單句缺少可裁決內容。

Gemini reason: The proper noun 'Service' is an identifier within the Kubernetes context and must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 21. kubernetes-docs-zh-cn-v1/page-04-sentence-0017

Changed: `eligible, script, domain, risk`

Input:

```text
Service 所对应的 Pod 集合通常由你定义的来确定。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 「由你定義的來確定」缺少被定義的 selector 等名詞，來源抽取後語意殘缺。

Gemini reason: A straightforward case for character conversion. The identifiers 'Service' and 'Pod' should be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 22. kubernetes-docs-zh-cn-v1/page-04-sentence-0033

Changed: `script, risk`

Input:

```text
你可以定义一个 Service 来发布该 TCP 侦听器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Mainland term '侦听器' (listener) should be localized to '接聽器' for Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 23. kubernetes-docs-zh-cn-v1/page-04-sentence-0055

Changed: `script, risk`

Input:

```text
在评估所采用的方法时，你仅在 Kubernetes 中运行一部分后端。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Mainland term '后端' (backend) is typically '後端' in Taiwan. This tests a common localization need.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 24. kubernetes-docs-zh-cn-v1/page-04-sentence-0068

Changed: `script, risk`

Input:

```text
访问没有选择算符的 Service 与有选择算符的 Service 的原理相同。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: The technical term '选择算符' (selector operator) is more commonly and idiomatically rendered as '選擇器' (selector) in Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 25. kubernetes-docs-zh-cn-v1/page-04-sentence-0101

Changed: `script, risk`

Input:

```text
与一般的 Kubernetes 名称一样，端口名称只能包含小写字母、数字和 `-`。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: A classic IT terminology gap: '端口' (port) in Mainland Chinese is '埠' or '連接埠' in Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 26. kubernetes-docs-zh-cn-v1/page-04-sentence-0125

Changed: `script`

Input:

```text
你所选择的 IP 地址必须是合法的 IPv4 或者 IPv6 地址，并且这个 IP 地址在 API 服务器上所配置的 `service-cluster-ip-range` CIDR 范围内。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Protects the code identifier `service-cluster-ip-range` and standard technical terms. '服务器' (server) is a potential candidate for localization but is widely understood.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 27. kubernetes-docs-zh-cn-v1/page-04-sentence-0130

Changed: `script`

Input:

```text
你的 Service 在其 `.spec.ports[*].nodePort` 字段中报告已分配的端口。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Protects the code identifier `.spec.ports[*].nodePort`. The term '报告' (report) is standard.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 28. kubernetes-docs-zh-cn-v1/page-04-sentence-0142

Changed: `risk`

Input:

```text
动态端口分配默认使用较高的端口段，并且在较高的端口段耗尽时也可以使用较低的端口段。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: A straightforward sentence with standard technical terms like '动态' (dynamic), '端口' (port), '默认' (default), and '耗尽' (exhausted) that require only character conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 29. kubernetes-docs-zh-cn-v1/page-04-sentence-0145

Changed: `script`

Input:

```text
你可以配置集群中的节点使用特定 IP 地址来支持 NodePort Service。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Protects the proper name `NodePort Service`. Terms like '集群' (cluster) and '节点' (node) are common but worth noting for consistency checks.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 30. kubernetes-docs-zh-cn-v1/page-04-sentence-0151

Changed: `script`

Input:

```text
`--nodeport-addresses` 的默认值是一个空的列表。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術文件完整句；依臺灣技術用語與識別碼保留風險分類。

Gemini reason: Protects the CLI flag identifier `--nodeport-addresses`.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 31. kubernetes-docs-zh-cn-v1/page-04-sentence-0153

Changed: `eligible, domain, risk`

Input:

```text
此 Service 的可见形式为 `:spec.ports[].nodePort` 以及 `.spec.clusterIP:spec.ports[].port`。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可見形式以冒號開頭且欄位組合缺少主機部分，抽取後格式無法穩定判讀。

Gemini reason: Contains English identifiers `:spec.ports[].nodePort` and `.spec.clusterIP:spec.ports[].port` which must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 32. zhtw-project-formal-llm-overconversion-guard-v1/formal-002

Changed: `script`

Input:

```text
委员会文件编号 COM(2026) 318 final 应保持完整。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The input requires preserving the alphanumeric document identifier 'COM(2026) 318 final'. This is a clear guard against damaging codes or proper names during conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 33. zhtw-project-formal-llm-overconversion-guard-v1/formal-005

Changed: `script`

Input:

```text
公报附件沿用标题 Annex IV，不改写罗马数字。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The input explicitly states to preserve the original title 'Annex IV', including the Roman numeral. This is a guard against incorrect modification of non-Chinese text.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 34. zhtw-project-formal-llm-overconversion-guard-v1/formal-006

Changed: `script`

Input:

```text
声明引用原文“without prejudice”，引号内文字不得意译。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The instruction is to not translate the quoted English phrase 'without prejudice'. This is a direct guard against unintended semantic alteration of a quoted foreign term of art.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 35. zhtw-project-formal-llm-overconversion-guard-v1/formal-011

Changed: `script`

Input:

```text
预算附件以 FY2028-Q1 标示财政期间。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The input specifies using the alphanumeric identifier 'FY2028-Q1' for a fiscal period. This code must be preserved, making it an over-conversion guard case.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 36. zhtw-project-formal-llm-overconversion-guard-v1/formal-015

Changed: `script, domain`

Input:

```text
医学论文将试验编号 NCT01234567 列在摘要末尾。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The input involves a clinical trial identifier 'NCT01234567'. Preserving such specific codes in a medical context is critical, making it a high-stakes over-conversion guard.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 37. zhtw-project-formal-llm-overconversion-guard-v1/formal-017

Changed: `script, domain`

Input:

```text
技术规范引用完整版本 ISO 8601-1:2019。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The input requires preserving the technical standard identifier 'ISO 8601-1:2019'. This is an over-conversion guard to protect formal specifications.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 38. zhtw-project-formal-llm-overconversion-guard-v1/formal-019

Changed: `script`

Input:

```text
决议正文提及 Paris Agreement 时沿用官方英文名称。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The input explicitly instructs to preserve the proper name 'Paris Agreement' in English. This is a direct over-conversion guard instruction to protect an official name.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 39. zhtw-project-formal-llm-overconversion-guard-v1/formal-020

Changed: `script`

Input:

```text
外交公报将 Côte d’Ivoire 维持为官方拼写。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: Input requires preserving the official spelling of the proper name 'Côte d’Ivoire', which contains non-ASCII characters and punctuation. This is a strong over-conversion guard case.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 40. zhtw-project-formal-llm-overconversion-guard-v1/formal-022

Changed: `domain`

Input:

```text
听证记录把证物标记为 Exhibit C-12。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: Protects a foreign-language identifier (English) in a formal legal context. The characters are simplified.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 41. zhtw-project-formal-llm-overconversion-guard-v1/formal-023

Changed: `domain`

Input:

```text
法学论文引用“stare decisis”时保留拉丁文。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: Protects a foreign-language term of art (Latin) within a formal academic context. The characters are simplified.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 42. zhtw-project-formal-llm-overconversion-guard-v1/formal-025

Changed: `domain`

Input:

```text
统计表以变量名 adjusted_R2 标示校正决定系数。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: Protects a variable name identifier from conversion. The characters are simplified.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 43. zhtw-project-formal-llm-overconversion-guard-v1/formal-026

Changed: `domain`

Input:

```text
报告将坐标参考系统写为 EPSG:3826。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: Protects a standard identifier (EPSG code) from conversion. The characters are simplified.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 44. zhtw-project-formal-llm-overconversion-guard-v1/formal-029

Changed: `script`

Input:

```text
会议决议保留投票结果 17-2-1 的连字符格式。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: Protects a numeric result's specific hyphenated formatting from conversion. The characters are simplified.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 45. zhtw-project-formal-llm-overconversion-guard-v1/formal-031

Changed: `domain`

Input:

```text
调查问卷沿用量表名称 PHQ-9。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: Protects a standard medical scale identifier (PHQ-9). The characters are simplified.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 46. zhtw-project-formal-llm-overconversion-guard-v1/formal-034

Changed: `script, domain`

Input:

```text
档案目录保留文件路径 /records/2026/final.pdf。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The file path '/records/2026/final.pdf' is an identifier and must not be altered. The surrounding text is standard simplified Chinese.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 47. zhtw-project-formal-llm-overconversion-guard-v1/formal-035

Changed: `script`

Input:

```text
声明中的“status quo ante”属于原文引语。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The Latin phrase 'status quo ante' is a direct quotation enclosed in quotes and must be preserved without alteration.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 48. zhtw-project-formal-llm-overconversion-guard-v1/formal-036

Changed: `script, domain`

Input:

```text
认证报告列出证书序号 04:7A:9C:11。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The serial number '04:7A:9C:11' is a technical identifier and must be preserved exactly. The context is formal certification.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 49. zhtw-project-formal-llm-overconversion-guard-v1/formal-038

Changed: `script, domain`

Input:

```text
资料表将空值记为 N/A，而不是数字零。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The abbreviation 'N/A' is a standard token for 'not applicable' or 'not available' in a data context and must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 50. zhtw-project-formal-llm-overconversion-guard-v1/formal-039

Changed: `script`

Input:

```text
研究计划引用资料集版本 v2026.07.1。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The version string 'v2026.07.1' is a specific identifier for a dataset and must not be converted or altered.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 51. zhtw-project-formal-llm-overconversion-guard-v1/formal-040

Changed: `script, domain`

Input:

```text
裁定书末尾保留签章识别码 SIG-8F21C0。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The signature identifier 'SIG-8F21C0' must be preserved exactly as it is a technical code within a legal document context.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 52. zhtw-project-formal-llm-overconversion-guard-v1/llm-004

Changed: `script`

Input:

```text
结构化输出必须符合 schema 名称 invoice_summary_v2。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The schema name 'invoice_summary_v2' is a technical identifier, likely for code or API responses, and must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 53. zhtw-project-formal-llm-overconversion-guard-v1/llm-006

Changed: `script`

Input:

```text
检索器会将 top_k=12 写入追踪记录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The parameter 'top_k=12' is a code artifact or log entry (common in ML/LLM contexts) and must be preserved exactly.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 54. zhtw-project-formal-llm-overconversion-guard-v1/llm-007

Changed: `script, domain`

Input:

```text
向量字段 text_embedding_3_large 不得重新命名。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The identifier 'text_embedding_3_large' must be preserved. The term '向量字段' (vector field) is technical and the conversion should handle it correctly, but the main risk is damaging the identifier.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 55. zhtw-project-formal-llm-overconversion-guard-v1/llm-008

Changed: `script, domain`

Input:

```text
引用标记 [doc:security#auth-3] 必须完整保留。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The documentation reference tag '[doc:security#auth-3]' must be preserved in its entirety.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 56. zhtw-project-formal-llm-overconversion-guard-v1/llm-009

Changed: `script, domain`

Input:

```text
提示模板使用 {{customer_name}} 作为占位符。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The placeholder '{{customer_name}}' must be preserved. The term '占位符' is standard and should convert correctly, but the key is the placeholder itself.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 57. zhtw-project-formal-llm-overconversion-guard-v1/llm-012

Changed: `script, domain`

Input:

```text
响应事件 response.reasoning_summary.delta 只携带新增内容。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The API response path 'response.reasoning_summary.delta' must be preserved. The term '响应' (response) is a potential candidate_gap (Taiwan often uses 回應), but the primary risk here is damaging the code-like token.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 58. zhtw-project-formal-llm-overconversion-guard-v1/llm-014

Changed: `script, domain`

Input:

```text
工具名称 lookup_customer_v3 不应翻译。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The tool name 'lookup_customer_v3' is an identifier and must not be altered.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 59. zhtw-project-formal-llm-overconversion-guard-v1/llm-015

Changed: `script, domain`

Input:

```text
安全分类标签 self_harm_intent 必须使用下划线。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The classification label 'self_harm_intent' is a technical identifier that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 60. zhtw-project-formal-llm-overconversion-guard-v1/llm-016

Changed: `script, domain`

Input:

```text
模型路由规则将 region=asia-east1 传给后端。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The parameter 'region=asia-east1' must be preserved. The term '后端' (backend) is a candidate_gap (Taiwan uses 後端), but the main risk is damaging the parameter.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 61. zhtw-project-formal-llm-overconversion-guard-v1/llm-017

Changed: `script, domain`

Input:

```text
缓存事件 prompt_cache.miss 与 prompt_cache.hit 分开统计。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The event names 'prompt_cache.miss' and 'prompt_cache.hit' are identifiers that must be preserved. The word '缓存' (cache) is also a candidate_gap (Taiwan often prefers 快取), but the identifiers are the key risk.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 62. zhtw-project-formal-llm-overconversion-guard-v1/llm-018

Changed: `script, domain`

Input:

```text
函数参数 additionalProperties 固定设为 false。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The identifiers 'additionalProperties' and 'false' must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 63. zhtw-project-formal-llm-overconversion-guard-v1/llm-019

Changed: `script, domain`

Input:

```text
测试案例要求输出字面值 null。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The literal value 'null' must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 64. zhtw-project-formal-llm-overconversion-guard-v1/llm-021

Changed: `script, domain`

Input:

```text
审核状态 needs_human_review 表示必须人工确认。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The identifier 'needs_human_review' must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 65. zhtw-project-formal-llm-overconversion-guard-v1/llm-023

Changed: `script`

Input:

```text
评分报告以 macro_f1 与 exact_match 为指标名称。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The metric names 'macro_f1' and 'exact_match' are identifiers and must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 66. zhtw-project-formal-llm-overconversion-guard-v1/llm-024

Changed: `script`

Input:

```text
提示注入测试包含字串 IGNORE_PREVIOUS_INSTRUCTIONS。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The string literal 'IGNORE_PREVIOUS_INSTRUCTIONS' must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 67. zhtw-project-formal-llm-overconversion-guard-v1/llm-026

Changed: `script, domain`

Input:

```text
红队资料中的 DROP TABLE audit_log; 只是测试内容。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The SQL code snippet 'DROP TABLE audit_log;' must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 68. zhtw-project-formal-llm-overconversion-guard-v1/llm-027

Changed: `domain`

Input:

```text
输出档名 evaluation-run-2026-07-28.json 不应改写。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The filename 'evaluation-run-2026-07-28.json' must be preserved. Input contains both simplified (应, 写) and traditional (档) characters.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 69. zhtw-project-formal-llm-overconversion-guard-v1/llm-028

Changed: `script, domain`

Input:

```text
代理将 handoff_target=human_support 写入事件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The identifier 'handoff_target=human_support' must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 70. zhtw-project-formal-llm-overconversion-guard-v1/llm-031

Changed: `script`

Input:

```text
模型快照名称 assistant-prod@2026-07-28 必须原样记录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The input contains a model snapshot name 'assistant-prod@2026-07-28' which is a technical identifier. This identifier must be preserved exactly as it is, making it a clear case for an over-conversion guard. The surrounding text is in Simplified Chinese.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 71. zhtw-project-formal-llm-overconversion-guard-v1/llm-032

Changed: `script, domain`

Input:

```text
工具错误代码 TOOL_TIMEOUT_30S 不应意译。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The input specifies an error code 'TOOL_TIMEOUT_30S' and explicitly states it should not be translated. This is a classic over-conversion guard to protect technical constants. The language is Simplified Chinese.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 72. zhtw-project-formal-llm-overconversion-guard-v1/llm-033

Changed: `script, domain`

Input:

```text
JSON 字段 finish_reason 的值为 tool_calls。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: This sentence describes a JSON structure, containing the field name 'finish_reason' and its value 'tool_calls'. Both are technical terms that must not be altered, serving as an over-conversion guard. The descriptive text is Simplified Chinese.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 73. zhtw-project-formal-llm-overconversion-guard-v1/llm-034

Changed: `script, domain`

Input:

```text
检索过滤器使用 tenant_id eq 'tw-001'。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The input includes a filter query string "tenant_id eq 'tw-001'". This is a piece of code that must be preserved verbatim, including the 'tw' identifier, which is critical in a Taiwan context. This is a strong over-conversion guard case.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 74. zhtw-project-formal-llm-overconversion-guard-v1/llm-035

Changed: `script`

Input:

```text
基准结果以 win_rate_paired 记录成对胜率。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The input contains a technical metric name 'win_rate_paired'. This identifier, used in a benchmark context, must not be converted. The surrounding Simplified Chinese text explains its purpose.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 75. zhtw-project-formal-llm-overconversion-guard-v1/llm-036

Changed: `script, domain`

Input:

```text
追踪属性 gen_ai.operation.name 设为 chat。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: This input describes a tracking attribute, where both the key 'gen_ai.operation.name' and the value 'chat' are technical identifiers. They must be preserved, making this an over-conversion guard case.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 76. zhtw-project-formal-llm-overconversion-guard-v1/llm-037

Changed: `script`

Input:

```text
模型拒答时返回状态码 safety_refusal。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: The input specifies a status code 'safety_refusal' returned by a model. As a technical constant, it must be kept as-is, which is the definition of an over-conversion guard. The context is Simplified Chinese.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 77. zhtw-project-formal-llm-overconversion-guard-v1/llm-040

Changed: `script`

Input:

```text
离线评测使用种子值 seed=20260719。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；專名、引文、代碼或識別碼必須避免過度轉換。

Gemini reason: This input describes a parameter 'seed=20260719' used for evaluation. This code-like element must not be altered, making it a clear over-conversion guard. The descriptive text is in Simplified Chinese.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`
