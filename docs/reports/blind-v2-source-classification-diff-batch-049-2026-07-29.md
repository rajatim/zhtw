<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 049 (2026-07-29)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `0de619f0e0b60bc47651ee26855f4219b557e1eea11e2b4692a73753c755aaa5`
Cases: 96
Exact Codex/Gemini classifications: 34
Maintainer review queue: 62

Field differences:

- Eligibility: 7
- Script: 16
- Domain: 33
- Risk: 33

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

The maintainer resolved all 62 advisory disagreements and batch-confirmed the 34 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. kubernetes-docs-zh-cn-v1/page-01-sentence-0010

Changed: `script`

Input:

```text
使用 `generateName` 时，所提供的值将作为名称前缀，服务器会在其后附加一个生成的后缀。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code_identifier |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Technical documentation. Contains a code identifier `generateName` that must be preserved. '服务器' (server) is a lexical gap (TW: 伺服器).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 02. kubernetes-docs-zh-cn-v1/page-02-sentence-0001

Changed: `script`

Input:

```text
`kubectl` 命令行工具支持多种不同的方式来创建和管理 Kubernetes。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code_identifier, has_brand_name |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Technical documentation. Contains the tool name `kubectl` and product name `Kubernetes` which should be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 03. kubernetes-docs-zh-cn-v1/page-02-sentence-0016

Changed: `script`

Input:

```text
指定的文件必须包含 YAML 或 JSON 格式的对象的完整定义。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_tech_acronym |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Technical documentation. Contains format names YAML and JSON which must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 04. kubernetes-docs-zh-cn-v1/page-03-sentence-0016

Changed: `script`

Input:

```text
例如，你可能想要定义一组 Pod，但只有在所有 Pod 都被创建完成后才会触发调度。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_tech_term |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Technical documentation. Contains the Kubernetes-specific term 'Pod', which must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 05. kubernetes-docs-zh-cn-v1/page-03-sentence-0027

Changed: `script`

Input:

```text
如果 Pod 因为任何原因被删除，甚至某完全相同的替代 Pod 被创建时，这个相关的对象（例如这里的卷）也会被删除并重建。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_tech_term |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Technical documentation. Contains the Kubernetes-specific term 'Pod'. Also contains '卷' (volume), which can have regional differences (TW: 磁碟區).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 06. kubernetes-docs-zh-cn-v1/page-03-sentence-0038

Changed: `eligible, domain, risk`

Input:

```text
`Failed`（失败） | Pod 中的所有容器都已终止，并且至少有一个容器是因为失败终止。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code_identifier, has_tech_term, is_definition |

Codex reason: 來源句有表格殘片、括號截斷、詞序重複、句界缺失或明顯錯譯，無法可靠裁決。

Gemini reason: Technical documentation, likely from a table. Defines the `Failed` state. Contains terms `Failed` and `Pod` that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 07. kubernetes-docs-zh-cn-v1/page-03-sentence-0052

Changed: `script`

Input:

```text
一旦将 Pod 分派给某个节点，`kubelet` 就通过开始为 Pod 创建容器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_tech_term, has_code_identifier |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Technical documentation. Contains technical terms `Pod` and `kubelet` that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 08. kubernetes-docs-zh-cn-v1/page-03-sentence-0294

Changed: `script`

Input:

```text
如果需要排空正被终止的 Pod 上的流量，可以将 `serving` 状况作为实际的就绪状态。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_terms, contains_english, code_snippet |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: K8s docs. Contains code-formatted term 'serving' and entity 'Pod' that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 09. kubernetes-docs-zh-cn-v1/page-03-sentence-0316

Changed: `script`

Input:

```text
这样确保了 Sidecar 容器继续为 Pod 中的其他容器提供服务，直到完全不再需要为止。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_terms, contains_english |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: K8s docs. Contains entities 'Sidecar' and 'Pod' that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 10. kubernetes-docs-zh-cn-v1/page-04-sentence-0012

Changed: `script`

Input:

```text
每个 Service 对象定义端点的一个逻辑集合（通常这些端点就是 Pod）以及如何访问到这些 Pod 的策略。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_terms, contains_english |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: K8s docs. Contains entities 'Service' and 'Pod' that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 11. kubernetes-docs-zh-cn-v1/page-04-sentence-0066

Changed: `script`

Input:

```text
如果直接使用 `kubectl` 之类的工具来管理 EndpointSlice 对象，请使用用来描述这种手动管理的名称，例如 `"staff"` 或 `"cluster-admins"`。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_terms, contains_english, code_snippet |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: K8s docs. Contains code-formatted CLI tool, object, and string examples to preserve.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 12. kubernetes-docs-zh-cn-v1/page-04-sentence-0087

Changed: `script`

Input:

```text
由于一个 Service 可以链接到多个 EndpointSlice 之上，所以 1000 个支撑端点的限制仅影响旧版的 Endpoints API。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_terms, contains_english |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: K8s docs. Contains entities 'Service', 'EndpointSlice', 'Endpoints API' to preserve.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 13. kubernetes-docs-zh-cn-v1/page-04-sentence-0092

Changed: `script`

Input:

```text
`appProtocol` 字段提供了一种为每个 Service 端口设置应用协议的方式。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_terms, contains_english, code_snippet |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: K8s docs. Contains code-formatted field 'appProtocol' and entity 'Service' to preserve.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 14. kubernetes-docs-zh-cn-v1/page-04-sentence-0100

Changed: `script`

Input:

```text
为 Service 使用多个端口时，必须为所有端口提供名称，以使它们无歧义。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_terms, contains_english |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: K8s docs. Contains entity 'Service' that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 15. kubernetes-docs-zh-cn-v1/page-04-sentence-0117

Changed: `risk`

Input:

```text
但是，这种层层递进的形式有一个例外。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Generic sentence from K8s docs. Standard conversion, baseline case.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 16. kubernetes-docs-zh-cn-v1/page-04-sentence-0136

Changed: `script`

Input:

```text
控制平面将或者为你分配该端口，或者报告 API 事务失败。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Technical sentence. Key terms like '控制平面' (control plane) and '事务' (transaction) might have specific lexical equivalents in Taiwan that a simple character conversion would miss.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 17. kubernetes-docs-zh-cn-v1/page-04-sentence-0149

Changed: `eligible, domain, risk`

Input:

```text
kube-proxy 应视将其视为所在节点的本机地址。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | it_api_cli | over_conversion_guard | high | awkward_phrasing |

Codex reason: 來源句有表格殘片、括號截斷、詞序重複、句界缺失或明顯錯譯，無法可靠裁決。

Gemini reason: Technical sentence with a specific component name `kube-proxy` that must be preserved. Phrasing '应视将其视为' is slightly awkward but clear.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 18. kubernetes-docs-zh-cn-v1/page-04-sentence-0217

Changed: `eligible, domain, risk`

Input:

```text
这些 DNS 记录是由集群内部 DNS 服务所提供的要定义无头 Service，你需要将 `.spec.type` 设置为 ClusterIP（这也是 `type` 的默认值），并进一步将 `.spec.clusterIP` 设置为 `None`。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | it_api_cli | over_conversion_guard | high | missing_punctuation |

Codex reason: 來源句有表格殘片、括號截斷、詞序重複、句界缺失或明顯錯譯，無法可靠裁決。

Gemini reason: Dense technical sentence with many identifiers (`DNS`, `Service`, `ClusterIP`, etc.) that must be preserved. The term '无头 Service' (headless Service) is a key concept. Lacks a comma after '提供的', creating a run-on sentence.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 19. ready-gov-cybersecurity-zh-hans-v1/sentence-005

Changed: `eligible, domain, risk`

Input:

```text
损害财务安全，包括身份盗用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | sentence_fragment |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 清單抽取後只剩述語片段，缺少可獨立辨識的主詞。

Gemini reason: Formal cybersecurity advice. The term for 'identity theft' (身份盗用) may have a different lexical choice in Taiwan (e.g., 身分盜竊).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 20. ready-gov-cybersecurity-zh-hans-v1/sentence-011

Changed: `domain`

Input:

```text
使软件应用程序和操作系统保持最新。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Classic IT terminology with known lexical gaps. '软件' (software) is '軟體' and '操作系统' (operating system) is '作業系統' in Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 21. ready-gov-cybersecurity-zh-hans-v1/sentence-013

Changed: `domain`

Input:

```text
使用密码管理器和两种验证方法。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: IT security context. While '密码' (password) and '验证' (verification) are common, Taiwan may prefer specific phrasings like '雙重驗證' for 'two verification methods'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 22. ready-gov-cybersecurity-zh-hans-v1/sentence-022

Changed: `domain`

Input:

```text
不要使用证书无效的网站。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: IT term with a known lexical gap. '证书' (certificate), especially for digital certificates, is often '憑證' in Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 23. ready-gov-cybersecurity-zh-hans-v1/sentence-032

Changed: `domain`

Input:

```text
警惕要求提供私人信息的电子邮件和社交媒体用户。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Common lexical gap: '信息' (information) is typically '資訊' or '訊息' in Taiwan. '电子邮件' (email) is also a more formal mainland term.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 24. ready-gov-cybersecurity-zh-hans-v1/sentence-037

Changed: `domain, risk`

Input:

```text
告诉工作单位、学校或其他系统所有者发生了什么。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: General advice. '工作单位' (work unit) is a common mainland term, but the sentence is largely standard Mandarin with low conversion risk.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 25. ready-gov-cybersecurity-zh-hans-v1/sentence-041

Changed: `domain, risk`

Input:

```text
联系持有账户的银行、信用卡公司和其他金融服务公司。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Standard formal instruction regarding financial services.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 26. ready-gov-cybersecurity-zh-hans-v1/sentence-043

Changed: `domain, risk`

Input:

```text
关闭任何未经授权的信用或收费账户。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Clear, formal instruction about closing unauthorized accounts.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 27. ready-gov-cybersecurity-zh-hans-v1/sentence-046

Changed: `domain`

Input:

```text
向联邦调查局 (FBI) 互联网犯罪投诉中心 (IC3) 提出投诉。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Contains official agency names and acronyms (FBI, IC3) which are sensitive to over-conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 28. ready-gov-cybersecurity-zh-hans-v1/sentence-050

Changed: `domain`

Input:

```text
视被盗信息情况，应联系其他适当机构。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: The term '信息' is a common lexical difference ('資訊' in TW).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 29. ready-gov-cybersecurity-zh-hans-v1/sentence-052

Changed: `domain`

Input:

```text
向当地的美国特勤局 (USSS) 电子犯罪特别工作组或互联网犯罪投诉中心报告在线犯罪或欺诈行为。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Contains multiple official agency names and acronyms that should be preserved carefully.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 30. ready-gov-cybersecurity-zh-hans-v1/sentence-053

Changed: `eligible, domain, risk`

Input:

```text
国家网络安全联盟，一个非营利组织，致力于打造更安全的互联世界。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | third_party_resource_blurb |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 第三方資源介紹不屬於本來源宣告納入的 FEMA 本文範圍。

Gemini reason: Contains '网络' and '互联', primary lexical gap candidates ('網路', '互連' in TW).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 31. ready-gov-evacuation-zh-hans-v1/sentence-002

Changed: `domain, risk`

Input:

```text
在某些情况下，各位可能有一两天的时间准备，而其他情况可能需要立即疏散。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Standard informational sentence on emergency preparedness.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 32. ready-gov-evacuation-zh-hans-v1/sentence-006

Changed: `domain`

Input:

```text
向当地官员了解今年有哪些避难所的名额。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Lexical choices '官员' and '名额' could be candidate gaps; different terms may be preferred in TW.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 33. ready-gov-evacuation-zh-hans-v1/sentence-010

Changed: `domain, risk`

Input:

```text
大多数公共庇护所只允许服务性动物。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: The term '庇护所' (shelter) is a potential lexical gap; '避難所' is more common in Taiwan for human evacuation shelters.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 34. ready-gov-evacuation-zh-hans-v1/sentence-015

Changed: `domain, risk`

Input:

```text
准备一个“行囊”，当步行或乘坐公共交通工具撤离时可以携带，如果你有车，则准备好长距离旅行的用品。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Standard instructional sentence. No major lexical gaps or over-conversion risks identified.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 35. ready-gov-evacuation-zh-hans-v1/sentence-023

Changed: `domain, risk`

Input:

```text
收听电池供电的收音机，遵守当地的疏散指示。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Clear instruction, straightforward conversion. The term '收音机' is used, while '廣播' is also common in Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 36. ready-gov-evacuation-zh-hans-v1/sentence-024

Changed: `domain, risk`

Input:

```text
带上应急用品包。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Significant lexical gap: '应急用品包' vs. the common Taiwan term '緊急避難包' (emergency evacuation kit).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 37. ready-gov-evacuation-zh-hans-v1/sentence-027

Changed: `domain, risk`

Input:

```text
现在就计划在紧急情况下如何照顾自己的宠物。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Standard sentence, primarily involves character-level conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 38. ready-gov-evacuation-zh-hans-v1/sentence-028

Changed: `domain`

Input:

```text
如果时间允许：依照家庭通讯计划中的州外联系人打电话或发电子邮件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Contains a US-specific term '州外' (out-of-state) and a minor lexical choice ('发' vs. '寄' for email) that presents a conversion challenge.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 39. ready-gov-evacuation-zh-hans-v1/sentence-031

Changed: `domain, risk`

Input:

```text
拔掉收音机、电视和小家电等电器设备的插头。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Straightforward instruction with common technical terms that are shared between regions.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 40. ready-gov-evacuation-zh-hans-v1/sentence-036

Changed: `eligible, domain, risk`

Input:

```text
向可能需要搭车的邻居查询。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | formal_news | candidate_gap | high | awkward_phrasing |

Codex reason: 來源句有表格殘片、括號截斷、詞序重複、句界缺失或明顯錯譯，無法可靠裁決。

Gemini reason: The use of '查询' (query/look up) is awkward for asking a neighbor; '询问' (ask) would be more natural. This represents a subtle lexical choice gap.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 41. ready-gov-evacuation-zh-hans-v1/sentence-042

Changed: `risk`

Input:

```text
如果要返回受灾地区，在重大事件发生后，要为日常活动的中断做好准备，并记住在风暴废墟被清理之前返回家园是很危险的。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Standard formal instructional sentence. Good baseline case.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 42. ready-gov-evacuation-zh-hans-v1/sentence-044

Changed: `risk`

Input:

```text
为设备充电，并考虑购买备用电池，以防继续停电。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Standard instructional sentence with common vocabulary.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 43. ready-gov-evacuation-zh-hans-v1/sentence-049

Changed: `risk`

Input:

```text
只在室外使用发电机，并远离家，千万不要在家里或车库里运行发电机或将其连接到家庭电气系统。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Clear, standard safety instruction. Good baseline case.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 44. ready-gov-kids-tornadoes-zh-hans-v1/sentence-006

Changed: `risk`

Input:

```text
龙卷风警告：龙卷风警告意味着已经发现龙卷风，或者多普勒雷达显示可能引发龙卷风的雷暴环流。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Contains a technical term '多普勒雷达' (Doppler radar) that should be preserved carefully during conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 45. ready-gov-kids-tornadoes-zh-hans-v1/sentence-008

Changed: `domain`

Input:

```text
漏斗云：一种长云形状，顶部较宽，底部较细，像冰淇淋甜筒。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | medium | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Educational definition. '冰淇淋' is a potential lexical gap, as other terms are common in Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 46. ready-gov-kids-tornadoes-zh-hans-v1/sentence-013

Changed: `domain`

Input:

```text
春季，该地区转移到德克萨斯州中北部和俄克拉荷马州。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Contains transliterated place names ('德克萨斯州', '俄克拉荷马州') which have specific standard forms that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 47. ready-gov-kids-tornadoes-zh-hans-v1/sentence-037

Changed: `eligible, domain, risk`

Input:

```text
如果已经损坏，请远离并听从成人的指示。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_reference |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 條件子句缺少可辨識的指涉對象，需依賴前文。

Gemini reason: Simple, standard safety instruction for children. Good baseline case.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 48. zhtw-project-formal-llm-context-guard-v1/formal-005

Changed: `domain`

Input:

```text
法院裁定原处分应由原机关重新审查。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Formal legal sentence. Terminology like '处分' and '机关' may have specific regional equivalents in a legal context.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 49. zhtw-project-formal-llm-context-guard-v1/formal-015

Changed: `risk`

Input:

```text
评选结果将在异议处理完成后公告。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Formal procedural announcement about selection results, in Simplified Chinese.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 50. zhtw-project-formal-llm-context-guard-v1/formal-018

Changed: `risk`

Input:

```text
财政部门说明税收估算采用的基准。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: The term '部门' (department) is a general Mainland China term; Taiwan might use a more specific official name.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 51. zhtw-project-formal-llm-context-guard-v1/formal-021

Changed: `risk`

Input:

```text
农业部门评估连续降雨造成的损失。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: The term '部门' (department) is a general Mainland China term; Taiwan might use a more specific official name for the agricultural authority.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 52. zhtw-project-formal-llm-context-guard-v1/formal-039

Changed: `risk`

Input:

```text
公听会资料已上传至机关网站。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Standard government announcement. Tests common character conversions like '听'->'聽', '会'->'會', and '网'->'網'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 53. zhtw-project-formal-llm-context-guard-v1/formal-045

Changed: `domain`

Input:

```text
申请资料缺少签章时应通知限期补正。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | legal_jargon |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Formal administrative/legal instruction. The phrase '限期补正' (correct within a deadline) is specific administrative jargon that requires careful conversion to sound natural in a Taiwan legal context.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 54. zhtw-project-formal-llm-context-guard-v1/llm-003

Changed: `script`

Input:

```text
使用者可以要求重新生成较精简的版本。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | mixed_script |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Mixed script sentence describing a feature. The term '生成' (generate) might be a lexical gap, with '產生' being more common in Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 55. zhtw-project-formal-llm-context-guard-v1/llm-012

Changed: `domain, risk`

Input:

```text
分类器将低信心案例交由人工复核。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Describes an ML classifier workflow. '复核' (review) is a key term with potential lexical differences in Taiwan (e.g., '覆核').

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 56. zhtw-project-formal-llm-context-guard-v1/llm-014

Changed: `script, domain`

Input:

```text
回应需要符合使用者指定的语言与地区。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | mixed_script |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Mixed script sentence about localization. The term '回应' (response) is a potential lexical gap, as '回覆' is very common in Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 57. zhtw-project-formal-llm-context-guard-v1/llm-017

Changed: `risk`

Input:

```text
评测人员只会看到去除产品名称的输出。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Describes an evaluation process. Vocabulary ('评测', '产品', '输出') has direct character conversions.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 58. zhtw-project-formal-llm-context-guard-v1/llm-019

Changed: `risk`

Input:

```text
对话太长时系统会压缩较早的消息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Describes chat history management. '消息' (message) is a significant lexical gap, as '訊息' is standard in Taiwan for digital messages.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 59. zhtw-project-formal-llm-context-guard-v1/llm-023

Changed: `domain, risk`

Input:

```text
系统会检查结构化输出是否符合格式。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Standard sentence about data format validation. '结构化输出' (structured output) is a standard technical term.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 60. zhtw-project-formal-llm-context-guard-v1/llm-026

Changed: `risk`

Input:

```text
安全过滤器可能要求提供额外说明。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Standard sentence about LLM/system behavior. Tests conversion of '过滤器' (filter).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 61. zhtw-project-formal-llm-context-guard-v1/llm-027

Changed: `risk`

Input:

```text
助理可以先提出一个必要的澄清问题。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Basic sentence about an AI assistant's action. Standard character conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 62. zhtw-project-formal-llm-context-guard-v1/llm-049

Changed: `risk`

Input:

```text
系统会在发布前移除内部审查备注。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: A system process description. Good test for software development terms like '发布' (release) and '审查' (review).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`
