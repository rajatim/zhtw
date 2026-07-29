<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 050 (2026-07-29)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `48c64ccc948fa24ed7387f086186dd88f7b14e972fd7208b090fb880bd11d342`
Cases: 80
Exact Codex/Gemini classifications: 28
Maintainer review queue: 52

Field differences:

- Eligibility: 1
- Script: 28
- Domain: 11
- Risk: 26

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

The maintainer resolved all 52 advisory disagreements and batch-confirmed the 28 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. kubernetes-docs-zh-cn-v1/page-01-sentence-0016

Changed: `script`

Input:

```text
当启用 `RelaxedServiceNameValidation` 特性门控时， Service 对象名称可以以数字开头。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Technical sentence with code identifiers. '特性门控' (feature gate) and 'Service' are key terms.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 02. kubernetes-docs-zh-cn-v1/page-01-sentence-0020

Changed: `script`

Input:

```text
例外情况是当为 Service 对象启用了 `RelaxedServiceNameValidation` 特性门控时，这允许 Service 名称以数字开头。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Technical sentence. Contains code identifiers that must not be translated.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 03. kubernetes-docs-zh-cn-v1/page-02-sentence-0015

Changed: `script`

Input:

```text
在指令式对象配置中，kubectl 命令指定操作（创建，替换等），可选标志和至少一个文件名。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Technical sentence about kubectl. '指令式' (imperative) and '标志' (flags) are key terms.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 04. kubernetes-docs-zh-cn-v1/page-02-sentence-0025

Changed: `script`

Input:

```text
对象配置需要额外的步骤来编写 YAML 文件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Simple technical sentence. The term 'YAML' must not be altered.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 05. kubernetes-docs-zh-cn-v1/page-03-sentence-0019

Changed: `script`

Input:

```text
然而，Pod 也可能以集群无法恢复的方式失败，在这种情况下，Kubernetes 不会进一步尝试修复 Pod；相反，Kubernetes 会删除 Pod 并依赖其他组件提供自动修复。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Describes system behavior. Contains proper names 'Pod' and 'Kubernetes' that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 06. kubernetes-docs-zh-cn-v1/page-03-sentence-0055

Changed: `eligible, script, domain, risk`

Input:

```text
其输出中包含 Pod 中每个容器的状态。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | no | null | null | high | missing_referent |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Ineligible due to the pronoun '其' (its) which requires external context to be understood.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 07. kubernetes-docs-zh-cn-v1/page-03-sentence-0072

Changed: `script`

Input:

```text
当 Pod 中的容器无法正常启动，并反复进入尝试与失败的循环时就会出现。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_reference |
| Gemini | no | null | null | high | sentence_fragment |

Codex reason: 條件句缺少所指狀態，單句無法判斷「出現」的對象。

Gemini reason: Ineligible sentence fragment. It describes a 'when' clause but is missing the 'what happens' part.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 08. kubernetes-docs-zh-cn-v1/page-03-sentence-0181

Changed: `script`

Input:

```text
当 kubelet 检测到 Pod 不具备配置了网络的运行时沙箱时，`PodReadyToStartContainers` 状况将被设置为 `False`。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Technical sentence with multiple code identifiers. '运行时沙箱' (runtime sandbox) is also a key technical term.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 09. kubernetes-docs-zh-cn-v1/page-03-sentence-0183

Changed: `script`

Input:

```text
在 Pod 生命周期的末期阶段，Pod 的沙箱由于以下原因被销毁时：节点重启时 Pod 没有被驱逐对于使用虚拟机进行隔离的容器运行时，Pod 沙箱虚拟机重启时，需要创建一个新的沙箱和全新的容器网络配置。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | no | null | null | high | malformed_sentence, fragment |

Codex reason: 來源句將多個清單項目連接成單句，句界與條件關係缺失。

Gemini reason: Ineligible: Grammatically broken sentence, appears to be a list of conditions mashed together without clear separation or conjunctions.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 10. kubernetes-docs-zh-cn-v1/page-03-sentence-0227

Changed: `script`

Input:

```text
`Unknown`（未知） : 诊断失败，因此不会采取任何行动。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Clear definition for a status code in software documentation. The keyword `Unknown` must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 11. kubernetes-docs-zh-cn-v1/page-03-sentence-0234

Changed: `script`

Input:

```text
如果容器不提供就绪态探针，则默认状态为 `Success`。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Technical sentence from documentation. `Success` is a fixed keyword that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 12. kubernetes-docs-zh-cn-v1/page-03-sentence-0251

Changed: `script`

Input:

```text
关于 kubelet 如何处理 Pod 删除的更多信息，请参见 Pod 终止。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Documentation cross-reference. Contains proper names/identifiers (`kubelet`, `Pod`) that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 13. kubernetes-docs-zh-cn-v1/page-03-sentence-0266

Changed: `script`

Input:

```text
许多容器运行时遵循容器镜像内定义的 `STOPSIGNAL` 值，如果不同，则发送容器镜像中配置的 STOPSIGNAL，而不是 TERM 信号。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Technical explanation with code identifiers (`STOPSIGNAL`, `TERM`) that must not be converted.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 14. kubernetes-docs-zh-cn-v1/page-03-sentence-0281

Changed: `script`

Input:

```text
如果 Pod 中的容器之一定义了 `preStop` 回调且 Pod 规约中的 `terminationGracePeriodSeconds` 未设为 0， `kubelet` 开始在容器内运行该回调逻辑。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Complex technical sentence full of code identifiers (`preStop`, `terminationGracePeriodSeconds`, `kubelet`) that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 15. kubernetes-docs-zh-cn-v1/page-03-sentence-0282

Changed: `script, risk`

Input:

```text
如果 `preStop` 回调在体面期结束后仍在运行，kubelet 将请求短暂的、一次性的体面期延长 2 秒。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | unusual_translation |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: The translation of 'grace period' as '体面期' is literal and a likely candidate for a different lexical choice in Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 16. kubernetes-docs-zh-cn-v1/page-03-sentence-0341

Changed: `script, risk`

Input:

```text
这种传统行为在很长一段时间内都是默认设置的，但给 Kubernetes 用户带来了一些问题，尤其是在大规模部署场景中。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Standard IT documentation. Contains common lexical conversion candidates like '默认', '用户', '大规模', '场景'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 17. kubernetes-docs-zh-cn-v1/page-04-sentence-0002

Changed: `script, risk`

Input:

```text
你可以在 Pod 集合中运行代码，无论该代码是为云原生环境设计的，还是被容器化的老应用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Standard IT documentation. The term '云原生' (cloud-native) is a key concept with potential regional variations.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 18. kubernetes-docs-zh-cn-v1/page-04-sentence-0004

Changed: `script`

Input:

```text
如果你使用来运行你的应用， Deployment 可以动态地创建和销毁 Pod。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | no | null | null | high | sentence_fragment, placeholder_text |

Codex reason: 「如果你使用來運行」缺少使用對象，來源句抽取不完整。

Gemini reason: Ineligible. The phrase '如果你使用来运行' is incomplete, likely missing a variable or token after '使用', making it a malformed fragment.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 19. kubernetes-docs-zh-cn-v1/page-04-sentence-0129

Changed: `risk`

Input:

```text
每个节点将该端口（每个节点上的相同端口号）上的流量代理到你的 Service。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Contains multiple key technical terms with common lexical differences ('节点', '端口'). 'Service' is a fixed term but the other items present a stronger conversion risk.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 20. kubernetes-docs-zh-cn-v1/page-04-sentence-0150

Changed: `script`

Input:

```text
例如，如果你使用 `--nodeport-addresses=127.0.0.0/8` 标志启动 kube-proxy，则 kube-proxy 仅选择 NodePort Service 的本地回路接口。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Technical sentence with a command-line flag and specific networking terms that should not be altered. '本地回路接口' (local loopback interface) needs careful handling.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 21. kubernetes-docs-zh-cn-v1/page-04-sentence-0176

Changed: `script`

Input:

```text
当 Service 中定义了多个端口时，特性门控 `MixedProtocolLBService`（从 kube-apiserver 1.24 版本起默认为启用）允许 LoadBalancer 类型的 Service 使用不同的协议。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code, has_version_number |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Technical sentence with a code identifier ('MixedProtocolLBService') and version number. Terms like '特性门控' (feature gate) are specific jargon.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 22. kubernetes-docs-zh-cn-v1/page-04-sentence-0193

Changed: `script`

Input:

```text
`.status.loadBalancer.ingress.ipMode` 有两个可能的值："VIP" 和 "Proxy"。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Defines specific string literal values for a code path. These must not be translated.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 23. kubernetes-docs-zh-cn-v1/page-04-sentence-0206

Changed: `script, risk`

Input:

```text
如果后来你决定将数据库移到集群中，则可以启动其 Pod，添加适当的选择算符或端点并更改 Service 的 `type`。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | has_code |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Potential lexical gaps for '集群' (cluster vs 叢集) and '选择算符' (selector). 'Pod' is a proper name to be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 24. kubernetes-docs-zh-cn-v1/page-04-sentence-0229

Changed: `script, risk`

Input:

```text
否则，这些客户端 Pod 中将不会出现对应的环境变量。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Standard IT sentence about environment variables. 'Pod' is a proper name. '客户端' (client) vs '客戶端'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 25. kubernetes-docs-zh-cn-v1/page-04-sentence-0231

Changed: `script`

Input:

```text
Kubernetes 还支持并提供与 Docker Engine 的 "legacy container links" 兼容的变量。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_english |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Contains a quoted English technical term ('legacy container links') that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 26. kubernetes-docs-zh-cn-v1/page-04-sentence-0250

Changed: `script`

Input:

```text
`PreferSameZone` : 表示优先将流量路由到与客户端处于同一区域中的端点。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Defines a code identifier which must not be translated. The description contains several IT terms with potential lexical gaps ('流量', '路由', '区域', '端点').

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 27. kubernetes-docs-zh-cn-v1/page-04-sentence-0251

Changed: `script`

Input:

```text
`PreferSameNode` : 表示优先将流量路由到与客户端处于同一节点上的端点。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | code_identifier, technical_term |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: IT documentation. `PreferSameNode` is a code identifier and must not be converted.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 28. ready-gov-cybersecurity-zh-hans-v1/sentence-014

Changed: `risk`

Input:

```text
注意那些要求立即做某事、提供听起来好得令人难以置信的东西或需要个人信息的可疑活动。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | security_advice |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: High-stakes government cybersecurity advice. The vocabulary is general and widely understood.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 29. ready-gov-cybersecurity-zh-hans-v1/sentence-021

Changed: `risk`

Input:

```text
共享个人财务信息时要谨慎，例如，银行帐号、社会保险号或信用卡号。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | financial_advice, pii_related, region_specific_concept |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: High-stakes security advice. 'Social Security Number' is a US-specific concept with a non-equivalent regional counterpart in Taiwan ('身分證字號'); a direct conversion would be incorrect.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 30. ready-gov-cybersecurity-zh-hans-v1/sentence-028

Changed: `risk`

Input:

```text
切记：政府不会就欠款打电话、发短信或通过社交媒体联系您。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | security_advice |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: High-stakes government advice about scams. A solid baseline case, as vocabulary like '发短信' (send SMS) vs. '傳簡訊' is a common, but low-impact, regional difference.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 31. ready-gov-cybersecurity-zh-hans-v1/sentence-040

Changed: `risk`

Input:

```text
如果认为自己是网络攻击的受害者，应向适当的联邦、州和地方当局报告。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Standard instruction to report a cyberattack.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 32. ready-gov-evacuation-zh-hans-v1/sentence-005

Changed: `risk`

Input:

```text
如果建议疏散，请计划好如何离开，以及将去往何处。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Standard emergency evacuation instruction.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 33. zhtw-project-formal-llm-context-guard-v1/formal-006

Changed: `risk`

Input:

```text
审计报告指出采购程序缺少书面记录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Formal sentence about an audit; standard terms.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 34. zhtw-project-formal-llm-context-guard-v1/formal-008

Changed: `risk`

Input:

```text
研究团队发布人口变化的初步分析。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Formal sentence about research; standard terms.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 35. zhtw-project-formal-llm-context-guard-v1/formal-011

Changed: `risk`

Input:

```text
执行单位须按季度提交进度报告。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Formal requirement sentence. '执行单位' (executing unit) and '季度' (quarter) are common Mainland terms that may differ in Taiwan usage.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 36. zhtw-project-formal-llm-context-guard-v1/formal-019

Changed: `risk`

Input:

```text
委员会要求业者改善收费资讯的揭露方式。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Formal directive. The term '业者' (operators/businesses) is a potential lexical gap, as '廠商' might be preferred in Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 37. zhtw-project-formal-llm-context-guard-v1/formal-026

Changed: `risk`

Input:

```text
能源报告比较不同月份的用电需求。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Standard sentence from a formal report. Serves as a good baseline case with technical but common vocabulary.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 38. zhtw-project-formal-llm-context-guard-v1/formal-027

Changed: `domain, risk`

Input:

```text
监管机关依法受理消费者提出的申诉。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: High-stakes legal/regulatory context. '监管机关' (regulatory authority) is a key Mainland term likely requiring localization for Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 39. zhtw-project-formal-llm-context-guard-v1/formal-036

Changed: `risk`

Input:

```text
机关核定名称后才会制作正式标牌。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Formal administrative process. Terms like '机关', '核定', and '标牌' may have regional differences.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 40. zhtw-project-formal-llm-context-guard-v1/formal-038

Changed: `risk`

Input:

```text
调查人员查核支出凭证与付款纪录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Formal auditing/investigative language. '查核', '凭证', '纪录' are potential lexical gaps.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 41. zhtw-project-formal-llm-context-guard-v1/formal-042

Changed: `domain`

Input:

```text
预算审查将优先处理法定支出项目。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Government budget review process. '预算审查' and '法定支出' are high-stakes terms with potential regional differences.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 42. zhtw-project-formal-llm-context-guard-v1/formal-043

Changed: `risk`

Input:

```text
主管单位请各机构指定联络窗口。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Formal inter-agency communication. '主管单位' and '联络窗口' are key terms to test for regional variants (e.g., vs. '联系人').

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 43. zhtw-project-formal-llm-context-guard-v1/llm-015

Changed: `domain`

Input:

```text
系统记录每次工具调用的开始与结束时间。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: IT/API context. '工具调用' (tool call) is a technical term with potential lexical variation in Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 44. zhtw-project-formal-llm-context-guard-v1/llm-016

Changed: `risk`

Input:

```text
模型会根据对话内容补充必要的上下文。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Core LLM behavior description. Vocabulary is standard across regions.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 45. zhtw-project-formal-llm-context-guard-v1/llm-018

Changed: `domain`

Input:

```text
检索器应排除已经失效的文件版本。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: IT/retrieval system context. '检索器' and '失效' are potential lexical gap candidates.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 46. zhtw-project-formal-llm-context-guard-v1/llm-020

Changed: `domain`

Input:

```text
助理应先确认高风险建议的适用范围。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Explicitly mentions 'high-risk', placing it in the high_stakes domain. The vocabulary is fairly standard.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 47. zhtw-project-formal-llm-context-guard-v1/llm-028

Changed: `domain`

Input:

```text
系统会合并重复出现的检索结果。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: IT system behavior. '检索' is a likely lexical gap candidate.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 48. zhtw-project-formal-llm-context-guard-v1/llm-031

Changed: `domain`

Input:

```text
评测集不得用于调整待测系统的规则。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Formal rule for system evaluation. '评测集' is a strong lexical gap candidate vs. TW '評估'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 49. zhtw-project-formal-llm-context-guard-v1/llm-032

Changed: `risk`

Input:

```text
助理应避免扩大原始声明的适用对象。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Standard instruction for LLM behavior regarding the scope of its statements.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 50. zhtw-project-formal-llm-context-guard-v1/llm-038

Changed: `script, domain, risk`

Input:

```text
工具失败时系统会保留可诊断的错误讯息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | mixed_script |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Contains '讯息', the traditional form for 'message', while other characters are simplified. '讯息' is common in Taiwan and should be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 51. zhtw-project-formal-llm-context-guard-v1/llm-044

Changed: `domain, risk`

Input:

```text
系统会限制一次能够处理的附件数量。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: A typical system limitation notice about processing attachments.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 52. zhtw-project-formal-llm-context-guard-v1/llm-046

Changed: `script, domain, risk`

Input:

```text
使用者可以选择是否保留对话纪录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | mixed_script |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Mixed script: uses traditional '纪录' (record) with simplified characters. '纪录' is the standard term in Taiwan and should be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`
