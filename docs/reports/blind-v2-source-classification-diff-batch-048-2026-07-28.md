<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 048 (2026-07-28)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `009b7c52f788915ec0d5970a824861b1087d69f4e0c555869187635b9499513d`
Cases: 96
Exact Codex/Gemini classifications: 35
Maintainer review queue: 61

Field differences:

- Eligibility: 8
- Script: 3
- Domain: 39
- Risk: 42

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

The maintainer resolved all 61 advisory disagreements and batch-confirmed the 35 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. kubernetes-docs-zh-cn-v1/page-01-sentence-0027

Changed: `script, risk`

Input:

```text
参阅 Kubernetes 标识符和名称的设计文档。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Standard IT documentation. The term '标识符' (identifier) is a potential lexical gap, possibly having a different preferred term in Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 02. kubernetes-docs-zh-cn-v1/page-03-sentence-0020

Changed: `eligible, script, domain, risk`

Input:

```text
如果 Pod 被调度到某个而该节点之后失效， Pod 会被视为不健康，最终 Kubernetes 会删除 Pod。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | it_api_cli | candidate_gap | high | awkward_phrasing |

Codex reason: 來源句有明顯抽取缺漏或錯譯，無法可靠建立獨立裁決案例。

Gemini reason: Describes a failure scenario. Contains key technical terms ('调度', '节点', '失效') which may have different lexical choices in Taiwan. Phrasing is slightly unnatural.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 03. kubernetes-docs-zh-cn-v1/page-03-sentence-0030

Changed: `script, risk`

Input:

```text
该阶段并不是对容器或 Pod 状态的综合汇总，也不是为了成为完整的状态机。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: A conceptual sentence about system design. '综合汇总' (comprehensive summary) and '状态机' (state machine) are good lexical test candidates.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 04. kubernetes-docs-zh-cn-v1/page-03-sentence-0140

Changed: `risk`

Input:

```text
Init 容器按顺序重新运行。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Contains an English technical term 'Init' which must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 05. kubernetes-docs-zh-cn-v1/page-03-sentence-0141

Changed: `risk`

Input:

```text
此特性的一个关键点是所有容器都会被重启，包括之前已成功完成或失败的容器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Standard technical documentation sentence, straightforward conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 06. kubernetes-docs-zh-cn-v1/page-03-sentence-0243

Changed: `risk`

Input:

```text
在这种情况下，就绪态探针可能与存活态探针相同，但是规约中的就绪态探针的存在意味着 Pod 将在启动阶段不接收任何数据，并且只有在探针探测成功后才开始接收数据。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Technical jargon like '就绪态探针' (readiness probe), '存活态探针' (liveness probe), and '规约' (spec) present a significant lexical challenge for Taiwan-specific conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 07. kubernetes-docs-zh-cn-v1/page-03-sentence-0273

Changed: `risk`

Input:

```text
可用的信号列表取决于 Pod 调度到的操作系统。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Tests common IT terms like '调度' (schedule) which may have different lexical preferences in Taiwan (e.g., '排程'). The identifier 'Pod' must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 08. kubernetes-docs-zh-cn-v1/page-03-sentence-0291

Changed: `eligible, domain, risk`

Input:

```text
一些应用程序不仅需要完成对打开的连接的处理，还需要更进一步的体面终止逻辑 - 比如：排空和完成会话。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 來源句有明顯抽取缺漏或錯譯，無法可靠建立獨立裁決案例。

Gemini reason: Rich in technical concepts like '体面终止' (graceful termination), '排空' (draining), and '会话' (session) which are prime candidates for lexical differences in Taiwan IT terminology.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 09. kubernetes-docs-zh-cn-v1/page-04-sentence-0013

Changed: `risk`

Input:

```text
例如，考虑一个无状态的图像处理后端，其中运行 3 个副本（Replicas）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Technical documentation. The keyword `Replicas`, presented as an annotation for the translated term '副本', must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 10. kubernetes-docs-zh-cn-v1/page-04-sentence-0095

Changed: `risk`

Input:

```text
此字段遵循标准的 Kubernetes 标签语法。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Technical documentation. While `Kubernetes` is a guard, terms like '字段' (field) and '标签语法' (label syntax) are primary candidates for lexical conversion to their Taiwan equivalents ('欄位', '標籤語法').

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 11. kubernetes-docs-zh-cn-v1/page-04-sentence-0097

Changed: `eligible, domain, risk`

Input:

```text
由具体实现所定义的、带有 `mycompany.com/my-custom-protocol` 这类前缀的名称。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | sentence_fragment |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 清單抽取後只剩不完整述語或名詞片段，無法獨立裁決。

Gemini reason: Technical sentence with an embedded code/path identifier that should be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 12. kubernetes-docs-zh-cn-v1/page-04-sentence-0214

Changed: `risk`

Input:

```text
无头 Service 不会获得集群 IP，kube-proxy 不会处理这类 Service，而且平台也不会为它们提供负载均衡或路由支持。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Technical sentence with a key lexical gap: '负载均衡' (load balancing) is '負載平衡' in Taiwan. Also contains identifiers.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 13. ready-gov-cybersecurity-zh-hans-v1/sentence-001

Changed: `domain`

Input:

```text
网络攻击是指访问或损坏电脑或网络系统的恶意企图，可能导致金钱损失或个人、财务和医疗信息被盗。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Formal text on cybersecurity. Contains key lexical items like '网络' (network), '电脑' (computer), and '信息' (information) that require mapping to Taiwan usage.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 14. ready-gov-cybersecurity-zh-hans-v1/sentence-002

Changed: `domain, risk`

Input:

```text
这些攻击可能会损害受害者的声誉和安全。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Straightforward sentence, primarily a test of character conversion rather than significant lexical choice.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 15. ready-gov-cybersecurity-zh-hans-v1/sentence-003

Changed: `domain`

Input:

```text
网络安全涉及预防、检测和应对可能对个人、组织、社区和国家产生广泛影响的网络攻击。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Good formal sentence with common IT/security terms like '网络' (network) and '检测' (detection) that have different lexical choices in Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 16. ready-gov-cybersecurity-zh-hans-v1/sentence-004

Changed: `eligible, domain, risk`

Input:

```text
访问个人电脑、手机、游戏系统和其他连接互联网和蓝牙的设备。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | no | it_api_cli | over_conversion_guard | high | fragment |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Ineligible sentence fragment. Lacks a subject and appears to be an item from a list. Contains terms like '蓝牙' (Bluetooth) that should be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 17. ready-gov-cybersecurity-zh-hans-v1/sentence-006

Changed: `domain, risk`

Input:

```text
阻止访问或删除个人信息和帐户。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | sentence_fragment |
| Gemini | no | it_api_cli | candidate_gap | high | fragment |

Codex reason: 清單抽取後只剩不完整述語或名詞片段，無法獨立裁決。

Gemini reason: Ineligible sentence fragment. Describes actions without a subject. Contains '信息' (information) and '帐户' (account) which are lexical gaps.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 18. ready-gov-cybersecurity-zh-hans-v1/sentence-007

Changed: `domain, risk`

Input:

```text
使就业或商业服务更加复杂。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | sentence_fragment |
| Gemini | no | formal_news | baseline_guard | high | fragment |

Codex reason: 清單抽取後只剩不完整述語或名詞片段，無法獨立裁決。

Gemini reason: Ineligible sentence fragment. Starts with a verb ('使' - to cause) but lacks a subject to perform the action.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 19. ready-gov-cybersecurity-zh-hans-v1/sentence-008

Changed: `domain, risk`

Input:

```text
影响交通和电网。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | sentence_fragment |
| Gemini | no | formal_news | baseline_guard | high | fragment |

Codex reason: 清單抽取後只剩不完整述語或名詞片段，無法獨立裁決。

Gemini reason: Ineligible sentence fragment. A verb phrase ('affect traffic and power grids') without a subject.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 20. ready-gov-cybersecurity-zh-hans-v1/sentence-009

Changed: `eligible, domain`

Input:

```text
限制在线共享的个人信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | no | ui_i18n | candidate_gap | high | fragment |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Ineligible sentence fragment. Contains lexical gaps '在线' (online) and '信息' (information).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 21. ready-gov-cybersecurity-zh-hans-v1/sentence-010

Changed: `domain`

Input:

```text
更改隐私设置，不要使用位置功能。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Standard UI/instructional text. Key lexical gap: '设置' (settings). '隐私' (privacy) is also a good test case.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 22. ready-gov-cybersecurity-zh-hans-v1/sentence-012

Changed: `domain`

Input:

```text
使用大小写字母、数字和特殊字符创建强密码。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Password creation rule. Potential lexical gaps in '创建' (create) and '强密码' (strong password).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 23. ready-gov-cybersecurity-zh-hans-v1/sentence-015

Changed: `domain`

Input:

```text
点击之前应深思。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Common security slogan 'Think before you click'. Tests '点击' (click) and the stylistic conversion of a short, impactful phrase.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 24. ready-gov-cybersecurity-zh-hans-v1/sentence-016

Changed: `domain, risk`

Input:

```text
有疑问时不要点击。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Security advice 'When in doubt, don't click'. Tests '点击' (click) within a common cautionary phrase.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 25. ready-gov-cybersecurity-zh-hans-v1/sentence-017

Changed: `domain, risk`

Input:

```text
使用安全的互联网连接和 Wi-Fi 网络保护好家庭和/或企业，定期更改密码。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | contains_latin |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Formal security guideline. Strong lexical gap with '互联网' (internet) vs. TW '網際網路' and '网络' (network) vs. TW '網路'. Also tests preservation of 'Wi-Fi'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 26. ready-gov-cybersecurity-zh-hans-v1/sentence-023

Changed: `domain`

Input:

```text
使用能创建更安全连接的虚拟专用网络 (VPN)。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | contains_latin |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Technical instruction. '虚拟专用网络' (Virtual Private Network) is a key technical term. The acronym 'VPN' must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 27. ready-gov-cybersecurity-zh-hans-v1/sentence-024

Changed: `domain`

Input:

```text
使用防病毒和反恶意软件解决方案及防火墙来阻止威胁。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Technical recommendation. Strong lexical gaps: '软件' (software) and '解决方案' (solution). These are classic PRC vs. Taiwan vocabulary differences.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 28. ready-gov-cybersecurity-zh-hans-v1/sentence-025

Changed: `domain`

Input:

```text
定期在加密文件或加密文件储存设备中备份文件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | slightly_awkward |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Technical instruction on backups. A key lexical gap candidate is '设备' (device) vs. TW '裝置'. The source phrasing is slightly awkward and repetitive.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 29. ready-gov-cybersecurity-zh-hans-v1/sentence-026

Changed: `domain`

Input:

```text
不要点击陌生人发来短信或电子邮件中的链接。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Standard cybersecurity advice. Contains common lexical gaps like '短信' (SMS/text message, TW: 簡訊) and '链接' (link, TW: 連結).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 30. ready-gov-cybersecurity-zh-hans-v1/sentence-027

Changed: `domain`

Input:

```text
诈骗者可能会创建指向网站的虚假链接。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Cybersecurity context. '链接' (link, TW: 連結) is a key lexical gap.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 31. ready-gov-cybersecurity-zh-hans-v1/sentence-029

Changed: `domain`

Input:

```text
还要记住，诈骗者可能会试图利用在家工作的机会、债务合并优惠和学生贷款还款计划来利用财务恐惧。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Complex sentence listing scam types. Good for testing conversion of longer phrases which may not be idiomatic in Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 32. ready-gov-cybersecurity-zh-hans-v1/sentence-031

Changed: `risk`

Input:

```text
检查信用报告中是否有任何自己未开设的新账户或贷款。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Financial security advice. Terms like '信用报告', '账户', '贷款' are mostly standard, serving as a good baseline test.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 33. ready-gov-cybersecurity-zh-hans-v1/sentence-034

Changed: `domain`

Input:

```text
考虑关闭受影响的设备，交给专业人员扫描潜在病毒，并删除发现的任何病毒。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: IT security instruction. '设备' (device) is a potential lexical gap for Taiwan's more common '裝置'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 34. ready-gov-cybersecurity-zh-hans-v1/sentence-036

Changed: `domain`

Input:

```text
这是一种常见的骗局。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Simple, declarative sentence. Good baseline case with no expected conversion issues.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 35. ready-gov-cybersecurity-zh-hans-v1/sentence-039

Changed: `domain`

Input:

```text
如果发现问题，应断开设备的互联网连接，并执行完整的系统还原。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Technical IT instruction. Contains multiple potential lexical gaps: '设备' (device, TW: 裝置), '互联网' (internet, TW: 網際網路), and the phrase '系统还原' (system restore).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 36. ready-gov-cybersecurity-zh-hans-v1/sentence-042

Changed: `domain`

Input:

```text
可能需要暂停受到攻击的帐户。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Standard formal instruction. The term '帐户' is a key lexical conversion test for Taiwan Traditional, where '帳戶' is used.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 37. ready-gov-cybersecurity-zh-hans-v1/sentence-044

Changed: `domain, risk`

Input:

```text
报告有人可能在使用您的身份。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: A baseline formal sentence. Conversion is mostly straightforward character-level changes. '身份' vs. '身分' is a minor lexical nuance.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 38. ready-gov-cybersecurity-zh-hans-v1/sentence-047

Changed: `eligible, domain, risk`

Input:

```text
他们会审查投诉并交给适当的机构。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_pronoun |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 代名詞缺少可獨立辨識的先行詞，需依賴前文。

Gemini reason: Good lexical gap test case. '审查' (review) vs. '審核' and '投诉' (complaint) vs. '申訴' are common conversion challenges.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 39. ready-gov-cybersecurity-zh-hans-v1/sentence-048

Changed: `risk`

Input:

```text
向当地警方报案，以便有事件的正式记录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: A standard high-stakes sentence with common legal/formal vocabulary ('警方', '报案'). Serves as a good baseline for character conversion accuracy.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 40. ready-gov-cybersecurity-zh-hans-v1/sentence-049

Changed: `risk`

Input:

```text
向联邦贸易委员会报告身份盗窃。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Involves a proper noun ('联邦贸易委员会' - Federal Trade Commission) and a key legal term ('身份盗窃' - identity theft). Tests preservation of the proper noun.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 41. ready-gov-cybersecurity-zh-hans-v1/sentence-054

Changed: `eligible, domain, risk`

Input:

```text
iKeepSafe 为儿童、学校和家庭提供安全的数字环境。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | third_party_resource_blurb |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 第三方資源介紹不屬於本來源宣告納入的 FEMA 本文範圍。

Gemini reason: Critical over-conversion guard case. The brand name 'iKeepSafe' must be preserved verbatim. Also tests '数字' to '數位'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 42. ready-gov-cybersecurity-zh-hans-v1/sentence-055

Changed: `eligible, domain, risk`

Input:

```text
iSafe 证明数字产品符合处理受保护个人信息的州和联邦要求。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | third_party_resource_blurb |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 第三方資源介紹不屬於本來源宣告納入的 FEMA 本文範圍。

Gemini reason: Over-conversion guard for the product name 'iSafe'. The sentence also contains formal regulatory terms like '联邦要求' (federal requirements).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 43. zhtw-project-formal-llm-context-guard-v1/formal-002

Changed: `domain`

Input:

```text
主管机关要求申请人补充资金来源说明。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Formal sentence about financial documentation. The phrasing '主管机关要求' (competent authority requests) is common in mainland official contexts and presents a potential lexical gap for Taiwan usage.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 44. zhtw-project-formal-llm-context-guard-v1/formal-016

Changed: `domain, risk`

Input:

```text
承办人员确认附件均已完成用印。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Formal statement on document processing. The terminology ('承办人员', '用印') is standard in formal and legal contexts in both mainland and Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 45. zhtw-project-formal-llm-context-guard-v1/formal-025

Changed: `risk`

Input:

```text
管理单位说明场地租借的优先顺序。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | medium | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Formal notice. The term '管理单位' (management unit) is a generic mainland phrasing; a more specific term would typically be used in Taiwan, indicating a subtle lexical gap.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 46. zhtw-project-formal-llm-context-guard-v1/formal-029

Changed: `risk`

Input:

```text
新闻资料引用专家对市场趋势的观察。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Sentence from press materials. The terminology ('新闻资料', '市场趋势') is standard in both mainland and Taiwan, requiring only character conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 47. zhtw-project-formal-llm-context-guard-v1/formal-030

Changed: `domain, risk`

Input:

```text
计划书应说明风险评估与应对措施。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Sentence from a formal plan. '计划书' (plan/proposal) is a mainland term (Taiwan prefers '計畫書' or '企劃書'). This is a strong indicator for a lexical gap.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 48. zhtw-project-formal-llm-context-guard-v1/formal-031

Changed: `risk`

Input:

```text
主管机关公布获准设置的服务据点。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Standard formal announcement about service locations. A straightforward case for script conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 49. zhtw-project-formal-llm-context-guard-v1/formal-032

Changed: `risk`

Input:

```text
统计资料依年龄与居住地区分别汇整。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Formal statistical context regarding data compilation. Standard character conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 50. zhtw-project-formal-llm-context-guard-v1/formal-037

Changed: `domain, risk`

Input:

```text
承包商必须保存材料检验的原始资料。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: High-stakes contractual or regulatory language about data preservation. Standard character conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 51. zhtw-project-formal-llm-context-guard-v1/llm-005

Changed: `risk`

Input:

```text
评测资料包含多轮对话与单轮问答。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: LLM-specific context about evaluation data. Vocabulary is standard in the tech domain.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 52. zhtw-project-formal-llm-context-guard-v1/llm-006

Changed: `domain, risk`

Input:

```text
检索结果会依相关性重新排序。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Standard IT/search context about sorting results. Vocabulary is common in tech.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 53. zhtw-project-formal-llm-context-guard-v1/llm-008

Changed: `risk`

Input:

```text
工具回传空结果时不要编造后续内容。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | clear, instructional |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: A clear instruction for an LLM on handling empty tool results. Vocabulary is standard and conversion should be straightforward.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 54. zhtw-project-formal-llm-context-guard-v1/llm-009

Changed: `risk`

Input:

```text
提示词要求保留输入中的专有名称。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | clear, instructional, meta |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: An instruction about preserving proper nouns, which is a meta-level guard against over-conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 55. zhtw-project-formal-llm-context-guard-v1/llm-010

Changed: `domain`

Input:

```text
系统会遮蔽记录中的敏感个人资料。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | clear, formal, privacy |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Describes a system's PII masking function. The word '遮蔽' (mask) is correct but may differ from the common Taiwan IT term '遮罩', creating a minor lexical gap.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 56. zhtw-project-formal-llm-context-guard-v1/llm-025

Changed: `risk`

Input:

```text
模型应完整保留引用文字的原始语气。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Instruction for an LLM to preserve original quoted text, which is a clear guard against over-conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 57. zhtw-project-formal-llm-context-guard-v1/llm-033

Changed: `domain`

Input:

```text
系统会在传送前验证附件是否可读取。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: IT system message with several terms (verify, attachment, read) that have specific lexical choices in Taiwan, making it a good candidate for testing vocabulary gaps.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 58. zhtw-project-formal-llm-context-guard-v1/llm-035

Changed: `domain, risk`

Input:

```text
回应中的日期必须与来源资料一致。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Tests the lexical choice between '回应' (mainland) and the more common Taiwan term '回覆' for 'response'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 59. zhtw-project-formal-llm-context-guard-v1/llm-040

Changed: `domain, risk`

Input:

```text
系统会把外部内容标记为不受信任的资料。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Standard IT security message. A good baseline test for correct character conversion without major lexical shifts.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 60. zhtw-project-formal-llm-context-guard-v1/llm-043

Changed: `risk`

Input:

```text
助理应说明无法完成请求的具体限制。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: A standard instruction for a virtual assistant. Serves as a baseline conversion test.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`

### 61. zhtw-project-formal-llm-context-guard-v1/llm-048

Changed: `risk`

Input:

```text
助理应在数字资料不足时避免精确估算。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: Codex 依 input-only 獨立可裁決性與臺灣領域語境分類；未接觸 converter output 或 expected。

Gemini reason: Tests the lexical choice around '数字' (numerical), as '數值' is often preferred in Taiwan for numerical data, making it a good lexical gap candidate.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-29`
