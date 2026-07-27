<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 028 (2026-07-27)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `bf4c643ea5d989199fe5f188ce7a1b9d3698dce7bd36f144c93b89663121fa84`
Cases: 90
Exact Codex/Gemini classifications: 3
Maintainer review queue: 87

Field differences:

- Eligibility: 10
- Script: 74
- Domain: 10
- Risk: 40

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

The maintainer resolved all 87 advisory disagreements and batch-confirmed the 3 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. kubernetes-docs-zh-cn-v1/page-01-sentence-0001

Changed: `eligible, domain, risk`

Input:

```text
集群中的每一个都有一个名称来标识在同类资源中的唯一性。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Markdown 结构、链接文字或表格标记移除后成为残句、格式残留或指代不清，离开上下文后不适合独立裁决。

Gemini reason: 標準的技術文檔句子，說明資源的唯一性。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 02. kubernetes-docs-zh-cn-v1/page-01-sentence-0017

Changed: `script`

Input:

```text
某些资源类型需要其名称遵循 RFC 1123 所定义的 DNS 标签标准。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_jargon |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及技術標準 RFC 1123，此類術語不應翻譯。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 03. kubernetes-docs-zh-cn-v1/page-01-sentence-0019

Changed: `script`

Input:

```text
尽管 RFC 1123 在技术上允许标签以数字开头，当前的 Kubernetes 实现要求 RFC 1035 和 RFC 1123 标签都以字母字符开头。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_jargon, long_sentence |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及技術標準 RFC 1035 和 RFC 1123，此類術語不應翻譯。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 04. kubernetes-docs-zh-cn-v1/page-01-sentence-0022

Changed: `risk`

Input:

```text
换句话说，其名称不能是 `.`、`..`，也不可以包含 `/` 或 `%` 这些字符。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整且可独立判读的 Kubernetes 技术文件句；适合作为保守字形转换基准。

Gemini reason: 列出不能使用的特殊字符，這些字符在轉換中必須保持原樣。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 05. kubernetes-docs-zh-cn-v1/page-02-sentence-0023

Changed: `risk`

Input:

```text
对象配置提供了用于创建新对象的模板。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含中国大陆技术用语或台湾术语正规化候选。

Gemini reason: 關於「對象配置」的基本技術概念解釋。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 06. kubernetes-docs-zh-cn-v1/page-02-sentence-0030

Changed: `risk`

Input:

```text
使用声明式对象配置时，用户对本地存储的对象配置文件进行操作，但是用户未定义要对该文件执行的操作。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | long_sentence |

Codex reason: 完整的 Kubernetes 技术文件句；含中国大陆技术用语或台湾术语正规化候选。

Gemini reason: 描述聲明式對象配置，句子較長但邏輯清晰。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 07. kubernetes-docs-zh-cn-v1/page-02-sentence-0034

Changed: `script, risk`

Input:

```text
可以通过使用 `patch` API 操作仅写入观察到的差异，而不是使用 `replace` API 操作来替换整个对象配置来实现。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | technical_jargon, has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 比較 patch 和 replace API 操作，涉及關鍵技術術語的區別。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 08. kubernetes-docs-zh-cn-v1/page-02-sentence-0039

Changed: `script, risk`

Input:

```text
使用 diff 产生的部分更新会创建复杂的合并和补丁操作。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | technical_jargon, has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及 diff、合併和補丁，均為軟體開發中的關鍵術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 09. kubernetes-docs-zh-cn-v1/page-03-sentence-0001

Changed: `script`

Input:

```text
本页面讲述 Pod 的生命周期。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_jargon |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 介紹頁面主題，核心概念 Pod 不應翻譯。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 10. kubernetes-docs-zh-cn-v1/page-03-sentence-0015

Changed: `script, risk`

Input:

```text
你可以使用 Pod 调度就绪态来延迟 Pod 的调度，直到所有的调度门控都被移除。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 解釋 Pod 調度就緒態的用途。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 11. kubernetes-docs-zh-cn-v1/page-03-sentence-0037

Changed: `eligible, script, domain, risk`

Input:

```text
`Succeeded`（成功） | Pod 中的所有容器都已成功结束，并且不会再重启。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_list_format |

Codex reason: Markdown 结构、链接文字或表格标记移除后成为残句、格式残留或指代不清，离开上下文后不适合独立裁决。

Gemini reason: 表格格式的項目，其中術語 Succeeded 不應翻譯。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 12. kubernetes-docs-zh-cn-v1/page-03-sentence-0044

Changed: `script`

Input:

```text
确保不要将 Status（kubectl 用于用户直觉的显示字段）与 Pod 的 `phase` 混淆。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 區分 kubectl 顯示的 Status 和 Pod 的 phase，涉及特定工具輸出和 API 字段。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 13. kubernetes-docs-zh-cn-v1/page-03-sentence-0045

Changed: `script`

Input:

```text
Pod 阶段（phase）是 Kubernetes 数据模型和 Pod API 的一个明确的部分。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 強調 Pod 階段 (phase) 是 API 的一部分，術語需準確。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 14. kubernetes-docs-zh-cn-v1/page-03-sentence-0054

Changed: `eligible, script, domain, risk`

Input:

```text
要检查 Pod 中容器的状态，你可以使用 `kubectl describe pod `。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: Markdown 结构、链接文字或表格标记移除后成为残句、格式残留或指代不清，离开上下文后不适合独立裁决。

Gemini reason: 包含 kubectl describe pod 命令，此類命令和參數不應更改。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 15. kubernetes-docs-zh-cn-v1/page-03-sentence-0061

Changed: `script`

Input:

```text
如果你使用 `kubectl` 来查询包含 `Running` 状态的容器的 Pod 时，你也会看到关于容器进入 `Running` 状态的信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及 kubectl 和 Running 狀態，均為特定術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 16. kubernetes-docs-zh-cn-v1/page-03-sentence-0065

Changed: `script`

Input:

```text
Kubernetes 通过在 Pod `spec` 中定义的 `restartPolicy` 管理 Pod 内容器出现的失效。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及 Pod spec 中的 restartPolicy 字段，為 API 關鍵字。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 17. kubernetes-docs-zh-cn-v1/page-03-sentence-0084

Changed: `script, risk`

Input:

```text
检查资源限制：确保容器被分配了足够的 CPU 和内存。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 關於資源限制的通用性建議。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 18. kubernetes-docs-zh-cn-v1/page-03-sentence-0085

Changed: `script, risk`

Input:

```text
有时，增加 Pod 定义中的资源可以解决问题。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 增加資源配置是解決問題的常見方法。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 19. kubernetes-docs-zh-cn-v1/page-03-sentence-0086

Changed: `risk`

Input:

```text
调试应用程序：应用程序代码中可能存在错误或配置不当。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含中国大陆技术用语或台湾术语正规化候选。

Gemini reason: 關於應用程式調試的通用性建議。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 20. kubernetes-docs-zh-cn-v1/page-03-sentence-0087

Changed: `risk`

Input:

```text
在本地或开发环境中运行此容器镜像有助于诊断应用程序的特定问题。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含中国大陆技术用语或台湾术语正规化候选。

Gemini reason: 在本地環境重現問題是標準的調試步驟。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 21. kubernetes-docs-zh-cn-v1/page-03-sentence-0091

Changed: `script, risk`

Input:

```text
Kubernetes 项目建议遵循云原生原则，包括能够应对未预告或随意重启的弹性设计。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及「雲原生原則」和「彈性設計」，這些是需要準確理解和翻譯的行業術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 22. kubernetes-docs-zh-cn-v1/page-03-sentence-0093

Changed: `risk`

Input:

```text
无论哪种方式，都有助于确保即使在部分故障的情况下，你的整体工作负载依然保持可用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含中国大陆技术用语或台湾术语正规化候选。

Gemini reason: 關於工作負載可用性的通用性陳述。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 23. kubernetes-docs-zh-cn-v1/page-03-sentence-0099

Changed: `script`

Input:

```text
`OnFailure`：只有在容器错误退出（退出状态非零）时才重新启动容器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 解釋 OnFailure 重啟策略，OnFailure 是 API 的枚舉值。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 24. kubernetes-docs-zh-cn-v1/page-03-sentence-0109

Changed: `script`

Input:

```text
如果你的集群启用了 `ContainerRestartRules` 特性门控，你可以针对单个容器指定 `restartPolicy` 和 `restartPolicyRules` 来覆盖 Pod 重启策略。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code, technical_jargon |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及特性門控 ContainerRestartRules 和字段 restartPolicy，均為專有術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 25. kubernetes-docs-zh-cn-v1/page-03-sentence-0116

Changed: `script`

Input:

```text
此外，单个容器可以指定 `restartPolicyRules`。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及 restartPolicyRules 字段，為 API 關鍵字。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 26. kubernetes-docs-zh-cn-v1/page-03-sentence-0118

Changed: `script`

Input:

```text
`restartPolicyRules` 定义了一系列在容器退出时应用的规则。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 解釋 restartPolicyRules 的作用，為 API 關鍵字。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 27. kubernetes-docs-zh-cn-v1/page-03-sentence-0127

Changed: `script`

Input:

```text
如果 Init 容器失败，则 Pod 也会失败。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_jargon |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及 Init 容器，為 Kubernetes 專有概念。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 28. kubernetes-docs-zh-cn-v1/page-03-sentence-0129

Changed: `risk`

Input:

```text
重启规则可用于许多其他高级的生命周期管理场景。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含中国大陆技术用语或台湾术语正规化候选。

Gemini reason: 關於重啟規則應用的通用性描述。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 29. kubernetes-docs-zh-cn-v1/page-03-sentence-0144

Changed: `script`

Input:

```text
边车容器可以监控主应用的健康状态，如果该应用进入不可恢复的状态，则触发整个 Pod 重启。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_jargon |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 描述邊車容器（Sidecar container）的作用，為常見設計模式。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 30. kubernetes-docs-zh-cn-v1/page-03-sentence-0145

Changed: `script`

Input:

```text
考虑一种工作负载，其中 watcher 边车负责在主应用出错时从已知良好状态重启主应用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_jargon |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及 watcher 邊車，為一種具體的邊車實現模式。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 31. kubernetes-docs-zh-cn-v1/page-03-sentence-0147

Changed: `script`

Input:

```text
`watcher-sidecar` 执行命令后以退出码 `88` 退出。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及特定的退出碼 88，數字和術語 watcher-sidecar 不應更改。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 32. kubernetes-docs-zh-cn-v1/page-03-sentence-0150

Changed: `script`

Input:

```text
Pod 保留其 UID、沙箱、IP 和卷。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_jargon |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 列出 Pod 的屬性（UID、沙箱、IP、卷），為技術術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 33. kubernetes-docs-zh-cn-v1/page-03-sentence-0177

Changed: `script`

Input:

```text
在其早期开发过程中，这种状况被命名为 `PodHasNetwork`。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及歷史命名 PodHasNetwork，此類開發術語應保持原樣。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 34. kubernetes-docs-zh-cn-v1/page-03-sentence-0205

Changed: `script`

Input:

```text
考虑使用 PodDisruptionBudget 来控制可用性。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_jargon |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 建議使用 PodDisruptionBudget，為 Kubernetes API 對象。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 35. kubernetes-docs-zh-cn-v1/page-03-sentence-0215

Changed: `script`

Input:

```text
如果响应的状态是 "SERVING"，则认为诊断成功。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及 gRPC 探針的 SERVING 狀態，為特定協議的狀態值。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 36. kubernetes-docs-zh-cn-v1/page-03-sentence-0217

Changed: `risk`

Input:

```text
如果响应的状态码大于等于 200 且小于 400，则诊断被认为是成功的。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含中国大陆技术用语或台湾术语正规化候选。

Gemini reason: 描述基於 HTTP 狀態碼的健康檢查成功條件，是通用實踐。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 37. kubernetes-docs-zh-cn-v1/page-03-sentence-0221

Changed: `risk`

Input:

```text
如果远程系统（容器）在打开连接后立即将其关闭，这算作是健康的。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可独立判读的 Kubernetes 技术文件句；适合作为保守字形转换基准。

Gemini reason: 描述 TCP 探針的一種邊緣情況，需要準確理解和表達。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 38. kubernetes-docs-zh-cn-v1/page-03-sentence-0222

Changed: `script`

Input:

```text
和其他机制不同，`exec` 探针的实现涉及每次执行时创建/复制多个进程。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及 exec 探針，並描述其性能影響。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 39. kubernetes-docs-zh-cn-v1/page-03-sentence-0232

Changed: `script`

Input:

```text
控制器将从与该 Pod 匹配的所有 Service 的 EndpointSlice 中删除该 Pod 的 IP 地址。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_jargon |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及 Service 和 EndpointSlice，均為 Kubernetes API 對象。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 40. kubernetes-docs-zh-cn-v1/page-03-sentence-0235

Changed: `script`

Input:

```text
`startupProbe` : 指示容器中的应用是否已经启动。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 定義 startupProbe 的用途，為 API 關鍵字。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 41. kubernetes-docs-zh-cn-v1/page-03-sentence-0242

Changed: `script, risk`

Input:

```text
如果要仅在探测成功时才开始向 Pod 发送请求流量，请指定就绪态探针。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 解釋就緒態探針的用途，是流量管理的常見模式。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 42. kubernetes-docs-zh-cn-v1/page-03-sentence-0271

Changed: `script`

Input:

```text
如果启用了 `ContainerStopSignals` 特性门控（feature gate），你可以通过容器的生命周期（Lifecycle）配置自定义的终止信号。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_jargon, has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及特性門控 ContainerStopSignals 和生命周期配置，均為專有術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 43. kubernetes-docs-zh-cn-v1/page-03-sentence-0303

Changed: `risk`

Input:

```text
默认情况下，所有的删除操作都会附有 30 秒钟的宽限期限。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含中国大陆技术用语或台湾术语正规化候选。

Gemini reason: 描述默認的 30 秒寬限期。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 44. kubernetes-docs-zh-cn-v1/page-03-sentence-0310

Changed: `script, risk`

Input:

```text
在节点侧，被设置为立即终止的 Pod 仍然会在被强行杀死之前获得一点点的宽限时间。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 解釋節點側 Pod 的終止行為。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 45. kubernetes-docs-zh-cn-v1/page-03-sentence-0320

Changed: `script`

Input:

```text
同样地，如果 Pod 有一个 `preStop` 钩子超过了终止宽限期，可能会发生紧急终止。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及 preStop 鉤子，為 Pod 生命週期的一部分。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 46. kubernetes-docs-zh-cn-v1/page-03-sentence-0325

Changed: `eligible, script, domain, risk`

Input:

```text
孤儿 Pod - 绑定到不再存在的节点，计划外终止的 Pod 终止过程中的 Pod，绑定到有 `node.kubernetes.io/out-of-service` 污点的未就绪节点。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code, technical_jargon |

Codex reason: Markdown 结构、链接文字或表格标记移除后成为残句、格式残留或指代不清，离开上下文后不适合独立裁决。

Gemini reason: 列舉孤兒 Pod 的幾種情況，並提及污點 node.kubernetes.io/out-of-service。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 47. kubernetes-docs-zh-cn-v1/page-03-sentence-0327

Changed: `script`

Input:

```text
此外，PodGC 在清理孤儿 Pod 时会添加 Pod 干扰状况。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_jargon |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及 PodGC，為 Kubernetes 的一個組件。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 48. kubernetes-docs-zh-cn-v1/page-03-sentence-0347

Changed: `eligible, script, domain, risk`

Input:

```text
进一步了解 Sidecar 容器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_jargon |

Codex reason: Markdown 结构、链接文字或表格标记移除后成为残句、格式残留或指代不清，离开上下文后不适合独立裁决。

Gemini reason: 引導讀者了解 Sidecar 容器。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 49. kubernetes-docs-zh-cn-v1/page-04-sentence-0026

Changed: `script`

Input:

```text
只要 Service 中的 Pod 集合发生变化，Kubernetes 就会为其更新 EndpointSlice。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_jargon |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及 Service 和 EndpointSlice，均為 Kubernetes API 對象。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 50. kubernetes-docs-zh-cn-v1/page-04-sentence-0036

Changed: `script`

Input:

```text
Kubernetes 为该 Service 分配一个 IP 地址（称为“集群 IP”），供虚拟 IP 地址机制使用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_jargon |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及「集群 IP」（Cluster IP），為 Kubernetes 網絡的核心概念。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 51. kubernetes-docs-zh-cn-v1/page-04-sentence-0043

Changed: `script`

Input:

```text
启用该特性后，Service 对象的名称必须符合 RFC 1123 标签名称的规范。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_jargon |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及 RFC 1123 標籤名稱規範。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 52. kubernetes-docs-zh-cn-v1/page-04-sentence-0048

Changed: `script`

Input:

```text
Service 的默认协议是 TCP；你还可以使用其他受支持的任何协议。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及 Service 的默認協議是 TCP。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 53. kubernetes-docs-zh-cn-v1/page-04-sentence-0049

Changed: `script, risk`

Input:

```text
由于许多 Service 需要公开多个端口，所以 Kubernetes 为同一 Service 定义多个端口。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 解釋 Service 支持多端口的設計原因。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 54. kubernetes-docs-zh-cn-v1/page-04-sentence-0053

Changed: `eligible, script, domain, risk`

Input:

```text
你希望让你的 Service 指向另一个中或其它集群中的 Service。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Markdown 结构、链接文字或表格标记移除后成为残句、格式残留或指代不清，离开上下文后不适合独立裁决。

Gemini reason: 描述 Service 指向其他集群中 Service 的用例。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 55. kubernetes-docs-zh-cn-v1/page-04-sentence-0069

Changed: `script`

Input:

```text
在没有选择算符的 Service 示例中，流量被路由到 EndpointSlice 清单中定义的两个端点之一：通过 TCP 协议连接到 10.1.2.3 或 10.4.5.6 的端口 9376。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 包含 IP 地址和端口號的具體示例，不應更改。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 56. kubernetes-docs-zh-cn-v1/page-04-sentence-0070

Changed: `script, risk`

Input:

```text
Kubernetes API 服务器不允许将流量代理到未被映射至 Pod 上的端点。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 解釋 API 服務器的一個重要安全約束。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 57. kubernetes-docs-zh-cn-v1/page-04-sentence-0071

Changed: `script`

Input:

```text
由于此约束，当 Service 没有选择算符时，诸如 `kubectl port-forward service/ forwardedPort:servicePort` 之类的操作将会失败。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 包含一個失敗的 kubectl 命令示例，此命令不應更改。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 58. kubernetes-docs-zh-cn-v1/page-04-sentence-0072

Changed: `script, risk`

Input:

```text
这可以防止 Kubernetes API 服务器被用作调用者可能无权访问的端点的代理。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 解釋 API 服務器代理限制的安全原因。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 59. kubernetes-docs-zh-cn-v1/page-04-sentence-0074

Changed: `eligible, script, domain, risk`

Input:

```text
更多的相关信息，请参阅 ExternalName 一节。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: Markdown 结构、链接文字或表格标记移除后成为残句、格式残留或指代不清，离开上下文后不适合独立裁决。

Gemini reason: 引導讀者參考 ExternalName 章節。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 60. kubernetes-docs-zh-cn-v1/page-04-sentence-0075

Changed: `script`

Input:

```text
EndpointSlice 对象表示某个 Service 的后端网络端点的子集（切片）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_jargon |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 定義 EndpointSlice 對象。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 61. kubernetes-docs-zh-cn-v1/page-04-sentence-0076

Changed: `script`

Input:

```text
你的 Kubernetes 集群会跟踪每个 EndpointSlice 所表示的端点数量。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_jargon |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 解釋集群如何跟踪 EndpointSlice。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 62. kubernetes-docs-zh-cn-v1/page-04-sentence-0085

Changed: `script`

Input:

```text
Kubernetes 限制单个 Endpoints 对象中可以容纳的端点数量。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_jargon |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及 Endpoints 對象的數量限制。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 63. kubernetes-docs-zh-cn-v1/page-04-sentence-0086

Changed: `script`

Input:

```text
当一个 Service 拥有 1000 个以上支撑端点时，Kubernetes 会截断 Endpoints 对象中的数据。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_jargon |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 解釋當端點超過 1000 個時 Endpoints 對象的行為。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 64. kubernetes-docs-zh-cn-v1/page-04-sentence-0091

Changed: `script`

Input:

```text
这一 API 限制也意味着你不能手动将 Endpoints 更新为拥有超过 1000 个端点。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_jargon |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 解釋手動更新 Endpoints 的限制。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 65. kubernetes-docs-zh-cn-v1/page-04-sentence-0096

Changed: `eligible, script, domain, risk`

Input:

```text
IANA 标准服务名称。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_jargon |

Codex reason: Markdown 结构、链接文字或表格标记移除后成为残句、格式残留或指代不清，离开上下文后不适合独立裁决。

Gemini reason: 提及 IANA 標準服務名稱。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 66. kubernetes-docs-zh-cn-v1/page-04-sentence-0112

Changed: `script, risk`

Input:

```text
Kubernetes 不直接提供负载均衡组件；你必须提供一个，或者将你的 Kubernetes 集群与某个云平台集成。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 說明 Kubernetes 本身不提供負載均衡器實現。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 67. kubernetes-docs-zh-cn-v1/page-04-sentence-0119

Changed: `script, risk`

Input:

```text
此默认 Service 类型从你的集群中为此预留的 IP 地址池中分配一个 IP 地址。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 解釋默認 Service 類型的 IP 地址分配方式。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 68. kubernetes-docs-zh-cn-v1/page-04-sentence-0126

Changed: `script`

Input:

```text
如果你尝试创建一个带有非法 `clusterIP` 地址值的 Service，API 服务器会返回 HTTP 状态码 422，表示值不合法。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及非法 clusterIP 值會導致 HTTP 422 錯誤。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 69. kubernetes-docs-zh-cn-v1/page-04-sentence-0135

Changed: `script`

Input:

```text
如果需要特定的端口号，你可以在 `nodePort` 字段中指定一个值。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及 nodePort 字段，為 API 關鍵字。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 70. kubernetes-docs-zh-cn-v1/page-04-sentence-0146

Changed: `risk`

Input:

```text
如果每个节点都连接到多个网络（例如：一个网络用于应用流量，另一网络用于节点和控制平面之间的流量），你可能想要这样做。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含中国大陆技术用语或台湾术语正规化候选。

Gemini reason: 解釋在多網絡環境下指定節點 IP 的用例。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 71. kubernetes-docs-zh-cn-v1/page-04-sentence-0158

Changed: `script`

Input:

```text
要实现 `type: LoadBalancer` 的服务，Kubernetes 通常首先进行与请求 `type: NodePort` 服务类似的更改。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 解釋 type: LoadBalancer 和 type: NodePort 服務的關係。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 72. kubernetes-docs-zh-cn-v1/page-04-sentence-0160

Changed: `script, risk`

Input:

```text
你可以将负载均衡 Service 配置为忽略分配节点端口，前提是云平台实现支持这点。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 說明可以將負載均衡服務配置為忽略節點端口。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 73. kubernetes-docs-zh-cn-v1/page-04-sentence-0162

Changed: `script`

Input:

```text
这时，平台将使用用户指定的 `loadBalancerIP` 来创建负载均衡器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及 loadBalancerIP 字段，為 API 關鍵字。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 74. kubernetes-docs-zh-cn-v1/page-04-sentence-0167

Changed: `eligible, domain, risk`

Input:

```text
它也不支持双协议栈联网。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Markdown 结构、链接文字或表格标记移除后成为残句、格式残留或指代不清，离开上下文后不适合独立裁决。

Gemini reason: 提及不支持雙協議棧，這是一個重要的功能限制。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 75. kubernetes-docs-zh-cn-v1/page-04-sentence-0172

Changed: `script, risk`

Input:

```text
负载均衡器运行状态检查对于现代应用程序至关重要，它们用于确定负载均衡器应将流量分派到哪个服务器（虚拟机或 IP 地址）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 解釋負載均衡器健康檢查的通用目的。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 76. kubernetes-docs-zh-cn-v1/page-04-sentence-0174

Changed: `script`

Input:

```text
负载均衡器运行状态检查广泛用于支持 Service 的 `externalTrafficPolicy` 字段。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及 externalTrafficPolicy 字段，為 Service 的一個重要配置。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 77. kubernetes-docs-zh-cn-v1/page-04-sentence-0179

Changed: `script, risk`

Input:

```text
这仅适用于负载均衡器的实现能够直接将流量路由到 Pod 而不是使用节点端口的情况。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 解釋一種高級路由場景：負載均衡器直接將流量路由到 Pod。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 78. kubernetes-docs-zh-cn-v1/page-04-sentence-0186

Changed: `script, risk`

Input:

```text
所有默认的负载均衡器实现（例如，由云平台所提供的）都会忽略设置了此字段的 Service。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 解釋默認負載均衡器實現的行為。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 79. kubernetes-docs-zh-cn-v1/page-04-sentence-0187

Changed: `script`

Input:

```text
`.spec.loadBalancerClass` 只能设置到类型为 `LoadBalancer` 的 Service 之上，而且一旦设置之后不可变更。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 解釋 .spec.loadBalancerClass 字段的使用限制。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 80. kubernetes-docs-zh-cn-v1/page-04-sentence-0188

Changed: `script`

Input:

```text
`.spec.loadBalancerClass` 的值必须是一个标签风格的标识符，可以有选择地带有类似 "`internal-vip`" 或 "`example.com/internal-vip`" 这类前缀。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 解釋 .spec.loadBalancerClass 值的格式要求，並給出示例。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 81. kubernetes-docs-zh-cn-v1/page-04-sentence-0211

Changed: `script, risk`

Input:

```text
有时你并不需要负载均衡，也不需要单独的 Service IP。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 描述不需要負載均衡或 Service IP 的用例。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 82. kubernetes-docs-zh-cn-v1/page-04-sentence-0232

Changed: `eligible, script, domain, risk`

Input:

```text
你可以阅读 makeLinkVariables 来了解这是如何在 Kubernetes 中实现的。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: Markdown 结构、链接文字或表格标记移除后成为残句、格式残留或指代不清，离开上下文后不适合独立裁决。

Gemini reason: 引導讀者閱讀 makeLinkVariables 了解實現細節。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 83. kubernetes-docs-zh-cn-v1/page-04-sentence-0236

Changed: `script`

Input:

```text
例如，如果你在 Kubernetes 命名空间 `my-ns` 中有一个名为 `my-service` 的 Service，则控制平面和 DNS 服务共同为 `my-service.my-ns` 生成 DNS 记录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 用具體示例 my-service.my-ns 解釋 DNS 記錄的生成。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 84. kubernetes-docs-zh-cn-v1/page-04-sentence-0239

Changed: `script, risk`

Input:

```text
这些名称将解析为分配给 Service 的集群 IP。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 解釋 DNS 名稱如何解析到集群 IP。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 85. kubernetes-docs-zh-cn-v1/page-04-sentence-0240

Changed: `script`

Input:

```text
Kubernetes 还支持命名端口的 DNS SRV（Service）记录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_jargon |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 提及支持命名端口的 DNS SRV 記錄。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 86. kubernetes-docs-zh-cn-v1/page-04-sentence-0256

Changed: `script`

Input:

```text
如果有外部 IP 能够路由到一个或多个集群节点上，则 Kubernetes Service 可以在这些 `externalIPs` 上公开出去。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 解釋 Service 如何通過 externalIPs 暴露。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 87. kubernetes-docs-zh-cn-v1/page-04-sentence-0264

Changed: `script`

Input:

```text
Ingress 负责将来自集群外部的 HTTP 和 HTTPS 请求路由给集群内的 Service。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | technical_jargon |

Codex reason: 完整的 Kubernetes 技术文件句；含专名、API、协议、字段或识别码，适合检查技术术语转换与受保护 token 保留。

Gemini reason: 解釋 Ingress 的作用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`
