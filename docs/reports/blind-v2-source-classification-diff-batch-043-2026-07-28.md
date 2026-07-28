<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 043 (2026-07-28)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `c23bcf6ad53f9d5932303ef24c21e9ec17750d4f9f713a4b5b60e96c41785bbf`
Cases: 96
Exact Codex/Gemini classifications: 26
Maintainer review queue: 70

Field differences:

- Eligibility: 1
- Script: 47
- Domain: 20
- Risk: 26

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

The maintainer resolved all 70 advisory disagreements and batch-confirmed the 26 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. chromium-strings-zh-cn-v1/translation-2738871930057338499

Changed: `script, domain, risk`

Input:

```text
无法连接到互联网。发生 HTTP 403 Forbidden 错误，请检查您的代理配置。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Chromium UI 字串；依臺灣介面詞彙與產品名稱保留風險分類。

Gemini reason: Technical error message. The identifier 'HTTP 403 Forbidden' must be preserved and not converted.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 02. chromium-strings-zh-cn-v1/translation-3975724895399328945

Changed: `script`

Input:

```text
关于 Google Chrome for Testing(&G)
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Chromium UI 字串；依臺灣介面詞彙與產品名稱保留風險分類。

Gemini reason: Proper name 'Google Chrome for Testing' and the UI mnemonic '(&G)' should be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 03. chromium-strings-zh-cn-v1/translation-4987820182225656817

Changed: `script, risk`

Input:

```text
访客使用Chromium不会留下任何痕迹。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Chromium UI 字串；依臺灣介面詞彙與產品名稱保留風險分類。

Gemini reason: The proper name 'Chromium' must be preserved and not converted.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 04. chromium-strings-zh-cn-v1/translation-5123973130450702873

Changed: `script`

Input:

```text
Chromium 需要获得权限，才能跟踪您的手部动作
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Chromium UI 字串；依臺灣介面詞彙與產品名稱保留風險分類。

Gemini reason: Permission request string. '跟踪' (track) is a key term that may have regional variants (e.g., 追蹤).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 05. chromium-strings-zh-cn-v1/translation-5473971139929175403

Changed: `script, domain, risk`

Input:

```text
Chromium 可能无法正常运行，因为它不再支持此 Linux 发行版
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Chromium UI 字串；依臺灣介面詞彙與產品名稱保留風險分類。

Gemini reason: Technical warning. The proper names 'Chromium' and 'Linux' must be preserved. The term '发行版' (distribution) might also require normalization.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 06. chromium-strings-zh-cn-v1/translation-5596627076506792578

Changed: `risk`

Input:

```text
更多选项
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 可獨立判讀的 Chromium UI 字串；依臺灣介面詞彙與產品名稱保留風險分類。

Gemini reason: A common UI label where direct character-for-character conversion is generally sufficient.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 07. chromium-strings-zh-cn-v1/translation-5800158606660203929

Changed: `script`

Input:

```text
自定义和控制 Chromium。将 Chromium 设为默认浏览器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Chromium UI 字串；依臺灣介面詞彙與產品名稱保留風險分類。

Gemini reason: Contains classic mainland Chinese terms like '自定义' (customize) and '默认' (default) that require normalization for a Taiwanese locale (e.g., to '自訂' and '預設').

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 08. chromium-strings-zh-cn-v1/translation-615103374448673771

Changed: `script`

Input:

```text
如果您允许使用 Cookie，Chromium 便可能会使用 Cookie 进行预加载
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Chromium UI 字串；依臺灣介面詞彙與產品名稱保留風險分類。

Gemini reason: UI string for cookie settings. Contains proper nouns 'Chromium' and 'Cookie' that should not be converted.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 09. chromium-strings-zh-cn-v1/translation-6248988683584659830

Changed: `risk`

Input:

```text
搜索设置
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 可獨立判讀的 Chromium UI 字串；依臺灣介面詞彙與產品名稱保留風險分類。

Gemini reason: Standard UI label. Straightforward character conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 10. chromium-strings-zh-cn-v1/translation-6388799252195623474

Changed: `risk`

Input:

```text
帮我解决这个问题
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 可獨立判讀的 Chromium UI 字串；依臺灣介面詞彙與產品名稱保留風險分類。

Gemini reason: Common phrase for a help or action button.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 11. chromium-strings-zh-cn-v1/translation-67706546131546258

Changed: `script, risk`

Input:

```text
Chromium 建议您扫描此文件，因为它可能包含危险因素。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Chromium UI 字串；依臺灣介面詞彙與產品名稱保留風險分類。

Gemini reason: Security warning message. Contains proper noun 'Chromium'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 12. chromium-strings-zh-cn-v1/translation-751935028865900641

Changed: `script, risk`

Input:

```text
网站很可能会按预期运行。关闭所有 Chromium 窗口后，您将会从大多数网站退出账号；但如果您已登录 Chromium，则您的 Google 账号不会退出。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Chromium UI 字串；依臺灣介面詞彙與產品名稱保留風險分類。

Gemini reason: Explanatory text for login/session behavior. Contains proper names 'Chromium' and 'Google'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 13. chromium-strings-zh-cn-v1/translation-8372327902843331129

Changed: `script, risk`

Input:

```text
如需获取您所有设备上的密码等信息，请登录 Chromium。登录后，该密码将保存到您的 Google 账号。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Chromium UI 字串；依臺灣介面詞彙與產品名稱保留風險分類。

Gemini reason: UI text for account/password sync. Contains proper nouns 'Chromium' and 'Google'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 14. chromium-strings-zh-cn-v1/translation-904366664621834601

Changed: `script`

Input:

```text
Chromium 阻止了此项下载操作，因为归档文件包含可能隐藏恶意软件的其他文件
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Chromium UI 字串；依臺灣介面詞彙與產品名稱保留風險分類。

Gemini reason: Download security warning. Regional terms for 'archive file' (归档文件) and 'malware' (恶意软件) may need normalization.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 15. chromium-strings-zh-cn-v1/translation-965162752251293939

Changed: `script`

Input:

```text
谁在使用 Chromium？
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Chromium UI 字串；依臺灣介面詞彙與產品名稱保留風險分類。

Gemini reason: User profile selection prompt. Contains the proper name 'Chromium'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 16. ftc-how-to-avoid-scam-simplified-v1/sentence-001

Changed: `domain, risk`

Input:

```text
诈骗者假装来自于您知道的组织。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 可獨立判讀的 FTC 防詐句；依臺灣用語差異與安全語意風險分類。

Gemini reason: Standard formal sentence. '来自于' is a minor regional phrasing difference.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 17. ftc-how-to-avoid-scam-simplified-v1/sentence-004

Changed: `domain, risk`

Input:

```text
有些人假装来自您知道的企业，例如，公用事业公司、科技公司或者甚至是要求捐款的慈善机构。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 可獨立判讀的 FTC 防詐句；依臺灣用語差異與安全語意風險分類。

Gemini reason: Sentence contains a list of business types requiring standard conversion and checking for regional term preferences.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 18. ftc-how-to-avoid-scam-simplified-v1/sentence-005

Changed: `domain, risk`

Input:

```text
他们使用技术来更改来电显示上的电话号码。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 FTC 防詐句；依臺灣用語差異與安全語意風險分類。

Gemini reason: Technical term '来电显示' (caller ID) requires correct regional mapping.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 19. ftc-how-to-avoid-scam-simplified-v1/sentence-006

Changed: `domain`

Input:

```text
因此，您看到的名称和号码可能不是真实的。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的 FTC 防詐句；依臺灣用語差異與安全語意風險分類。

Gemini reason: Straightforward sentence with common character conversions.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 20. ftc-how-to-avoid-scam-simplified-v1/sentence-007

Changed: `domain`

Input:

```text
诈骗者迫使您立即采取行动。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的 FTC 防詐句；依臺灣用語差異與安全語意風險分類。

Gemini reason: Simple, direct sentence with standard character mappings (e.g., 采取 -> 採取).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 21. ftc-how-to-avoid-scam-simplified-v1/sentence-012

Changed: `risk`

Input:

```text
诈骗者通知您要用特定的方式付款。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 可獨立判讀的 FTC 防詐句；依臺灣用語差異與安全語意風險分類。

Gemini reason: Instruction about payment, a high-stakes topic. '付款' is common but context matters.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 22. ftc-how-to-avoid-scam-simplified-v1/sentence-021

Changed: `domain`

Input:

```text
采取措施，阻止骚扰的来电并过滤骚扰的短信。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 FTC 防詐句；依臺灣用語差異與安全語意風險分類。

Gemini reason: Classic candidate_gap: '短信' (text message) should be converted to '簡訊' for Taiwan locale.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 23. ftc-how-to-avoid-scam-simplified-v1/sentence-031

Changed: `script, risk`

Input:

```text
切勿向坚持要求您仅可通过加密货币、 MoneyGram 或 Western Union 等公司的电汇服务、用支付应用程序或礼品卡付款的人员付款、并且切勿存入支票并随后将款项返回给某人。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 FTC 防詐句；依臺灣用語差異與安全語意風險分類。

Gemini reason: Contains proper nouns 'MoneyGram' and 'Western Union' which must not be converted. Also contains terms like '支付应用程序' (payment apps) which are candidates for localization ('支付APP').

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 24. ftc-how-to-avoid-scam-simplified-v1/sentence-032

Changed: `domain`

Input:

```text
停下来，并与您信任的人谈一谈。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的 FTC 防詐句；依臺灣用語差異與安全語意風險分類。

Gemini reason: Simple, common-language sentence where direct character conversion is sufficient.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 25. kubernetes-docs-zh-cn-v1/page-01-sentence-0021

Changed: `risk`

Input:

```text
某些资源类型要求名称能被安全地用作路径中的片段。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術句；命令、欄位與資源名稱須原樣保留。

Gemini reason: Standard technical sentence from Kubernetes documentation.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 26. kubernetes-docs-zh-cn-v1/page-02-sentence-0033

Changed: `risk`

Input:

```text
声明式对象配置保留其他编写者所做的修改，即使这些更改并未合并到对象配置文件中。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術句；命令、欄位與資源名稱須原樣保留。

Gemini reason: Standard technical sentence about declarative configuration.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 27. kubernetes-docs-zh-cn-v1/page-02-sentence-0038

Changed: `risk`

Input:

```text
声明式对象配置难于调试并且出现异常时结果难以理解。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術句；命令、欄位與資源名稱須原樣保留。

Gemini reason: Standard sentence about debugging technical configurations.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 28. kubernetes-docs-zh-cn-v1/page-03-sentence-0089

Changed: `eligible, domain, risk`

Input:

```text
但重启并不总是合适的；例如，只在 Pod 启动期间运行一次（如果成功）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 例句省略執行一次的主體並依賴前文，無法離開上下文穩定裁決。

Gemini reason: Contains identifier `Pod` and the example is slightly fragmented but understandable.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 29. kubernetes-docs-zh-cn-v1/page-03-sentence-0288

Changed: `script`

Input:

```text
在 `kubelet` 启动 Pod 的体面关闭逻辑的同时，控制平面会评估是否将关闭的 Pod 从对应的 EndpointSlice 对象中移除，过滤条件是 Pod 被对应的以某选定。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | no | null | null | high | incomplete_sentence, ungrammatical_ending |

Codex reason: 句尾「Pod 被對應的以某選定」明顯殘缺錯接，來源語意不可靠。

Gemini reason: Sentence is incomplete and ends with an ungrammatical, nonsensical phrase '以某选定'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 30. kubernetes-docs-zh-cn-v1/page-03-sentence-0307

Changed: `script`

Input:

```text
使用 kubectl 时，你必须在设置 `--grace-period=0` 的同时额外设置 `--force` 参数才能发起强制删除请求。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術句；命令、欄位與資源名稱須原樣保留。

Gemini reason: IT/CLI documentation. Contains command-line flags (`--grace-period=0`, `--force`) that must not be converted.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 31. kubernetes-docs-zh-cn-v1/page-04-sentence-0044

Changed: `script`

Input:

```text
Pod 中的端口定义是有名字的，你可以在 Service 的 `targetPort` 属性中引用这些名字。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術句；命令、欄位與資源名稱須原樣保留。

Gemini reason: IT/API documentation. Contains technical identifiers (Pod, Service, `targetPort`) that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 32. kubernetes-docs-zh-cn-v1/page-04-sentence-0111

Changed: `script`

Input:

```text
`LoadBalancer` : 使用云平台的负载均衡器向外部公开 Service。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術句；命令、欄位與資源名稱須原樣保留。

Gemini reason: IT/API documentation. Contains technical identifiers (`LoadBalancer`, Service) that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 33. kubernetes-docs-zh-cn-v1/page-04-sentence-0131

Changed: `script`

Input:

```text
使用 NodePort 可以让你自由设置自己的负载均衡解决方案，配置 Kubernetes 不完全支持的环境，甚至直接公开一个或多个节点的 IP 地址。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術句；命令、欄位與資源名稱須原樣保留。

Gemini reason: IT/API documentation. Contains mainland China IT terms like '负载均衡解决方案' (load balancing solution) that may need localization in Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 34. kubernetes-docs-zh-cn-v1/page-04-sentence-0201

Changed: `script`

Input:

```text
`type: ExternalName` 的 Service 接受 IPv4 地址字符串，但将该字符串视为由数字组成的 DNS 名称，而不是 IP 地址（然而，互联网不允许在 DNS 中使用此类名称）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術句；命令、欄位與資源名稱須原樣保留。

Gemini reason: IT/API documentation. High density of technical identifiers (`type: ExternalName`, Service, IPv4, DNS, IP).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 35. kubernetes-docs-zh-cn-v1/page-04-sentence-0204

Changed: `script`

Input:

```text
当查找主机 `my-service.prod.svc.cluster.local` 时，集群 DNS 服务返回 `CNAME` 记录，其值为 `my.database.example.com`。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術句；命令、欄位與資源名稱須原樣保留。

Gemini reason: IT/API documentation. Contains FQDNs and technical terms (`CNAME`) that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 36. kubernetes-docs-zh-cn-v1/page-04-sentence-0242

Changed: `script`

Input:

```text
Kubernetes DNS 服务器是唯一的一种能够访问 `ExternalName` 类型的 Service 的方式。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術句；命令、欄位與資源名稱須原樣保留。

Gemini reason: IT/API documentation. Contains technical identifiers (Kubernetes DNS, `ExternalName`, Service) that must not be converted.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 37. kubernetes-docs-zh-cn-v1/page-04-sentence-0245

Changed: `script`

Input:

```text
你可以设置 `.spec.internalTrafficPolicy` 和 `.spec.externalTrafficPolicy` 字段来控制 Kubernetes 如何将流量路由到健康（“就绪”）的后端。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Kubernetes 技術句；命令、欄位與資源名稱須原樣保留。

Gemini reason: IT/API documentation. Contains spec paths (`.spec.internalTrafficPolicy`, `.spec.externalTrafficPolicy`) that are code and must not be converted.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 38. ready-gov-tornadoes-zh-hans-v1/sentence-008

Changed: `risk`

Input:

```text
在平坦的低处更安全。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的龍捲風安全指示；依臺灣用語與機構標識保留風險分類。

Gemini reason: Simple, direct safety advice.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 39. ready-gov-tornadoes-zh-hans-v1/sentence-013

Changed: `domain`

Input:

```text
在美国，中西部和东南部更可能发生龙卷风。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的龍捲風安全指示；依臺灣用語與機構標識保留風險分類。

Gemini reason: Factual statement involving geographical locations with standard character conversions.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 40. ready-gov-tornadoes-zh-hans-v1/sentence-015

Changed: `domain, risk`

Input:

```text
注册社区警报系统。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 可獨立判讀的龍捲風安全指示；依臺灣用語與機構標識保留風險分類。

Gemini reason: The word '注册' (register) is a common mainland term; Taiwan usage often prefers '登記' for signing up for services, though '註冊' is also used.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 41. ready-gov-tornadoes-zh-hans-v1/sentence-017

Changed: `risk`

Input:

```text
如果社区有警报器，应熟悉警报音。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 可獨立判讀的龍捲風安全指示；依臺灣用語與機構標識保留風險分類。

Gemini reason: Standard safety instruction. '社区' (community) and '警报器' (alarm/siren) are key terms.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 42. ready-gov-tornadoes-zh-hans-v1/sentence-019

Changed: `script`

Input:

```text
识别并练习前往安全避难所，例如，使用 FEMA 标准建造的安全室或根据 ICC 500 标准建造的风暴避难所。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的龍捲風安全指示；依臺灣用語與機構標識保留風險分類。

Gemini reason: Contains proper nouns (FEMA, ICC 500) that must not be converted. Key terms are '避难所' (shelter) and '风暴' (storm).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 43. ready-gov-tornadoes-zh-hans-v1/sentence-020

Changed: `risk`

Input:

```text
下一个最佳保护措施是坚固建筑物最低层的小型室内无窗房间或地下室。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的龍捲風安全指示；依臺灣用語與機構標識保留風險分類。

Gemini reason: Straightforward descriptive sentence. Focus on correct glyph conversion for common terms like '建筑' (building) and '室内' (indoor).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 44. ready-gov-tornadoes-zh-hans-v1/sentence-021

Changed: `risk`

Input:

```text
为宠物制定计划。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 可獨立判讀的龍捲風安全指示；依臺灣用語與機構標識保留風險分類。

Gemini reason: Short imperative sentence. '宠物' (pet) and '计划' (plan) are key terms.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 45. ready-gov-tornadoes-zh-hans-v1/sentence-028

Changed: `risk`

Input:

```text
如在车内或室外且无法进入建筑物，尽可能用手臂遮住头部和颈部，并用外套或毯子遮住身体。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 可獨立判讀的龍捲風安全指示；依臺灣用語與機構標識保留風險分類。

Gemini reason: Conditional safety instruction. Involves common objects like '车' (vehicle) and body parts.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 46. ready-gov-tornadoes-zh-hans-v1/sentence-030

Changed: `script`

Input:

```text
注意紧急警示系统 (EAS)、国家海洋和大气管理局 (NOAA) 天气电台和地方当局，了解最新信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的龍捲風安全指示；依臺灣用語與機構標識保留風險分類。

Gemini reason: Contains acronyms (EAS, NOAA) and a long proper name of an agency. Acronyms must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 47. zhtw-project-it-ui-llm-formal-guard-v1/formal-005

Changed: `script`

Input:

```text
研究报告保留资料集名称 World Values Survey Wave 7。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: Project-original 保留情境可獨立判讀；識別碼、專名、引文或格式不得改寫。

Gemini reason: The sentence is eligible. The main risk is to incorrectly convert the English proper noun 'World Values Survey Wave 7'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 48. zhtw-project-it-ui-llm-formal-guard-v1/formal-006

Changed: `script, domain`

Input:

```text
法院文件以案号 2:26-cv-00417 标识本案。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Project-original 保留情境可獨立判讀；識別碼、專名、引文或格式不得改寫。

Gemini reason: The sentence is eligible. The main risk is to incorrectly convert the case number identifier '2:26-cv-00417'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 49. zhtw-project-it-ui-llm-formal-guard-v1/formal-012

Changed: `script`

Input:

```text
外交公报中的姓名 José Álvarez 保留重音符号。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: Project-original 保留情境可獨立判讀；識別碼、專名、引文或格式不得改寫。

Gemini reason: The sentence is eligible. The main risk is to incorrectly convert the foreign name 'José Álvarez' or remove its diacritics.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 50. zhtw-project-it-ui-llm-formal-guard-v1/formal-015

Changed: `script, domain`

Input:

```text
标准作业程序引用表单 Form QA-17B。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Project-original 保留情境可獨立判讀；識別碼、專名、引文或格式不得改寫。

Gemini reason: The sentence is eligible. The main risk is to incorrectly convert the form identifier 'Form QA-17B'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 51. zhtw-project-it-ui-llm-formal-guard-v1/it-002

Changed: `script`

Input:

```text
请勿改写 URI 路径中的 /v2/userProfiles/{profileId}。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Project-original 保留情境可獨立判讀；識別碼、專名、引文或格式不得改寫。

Gemini reason: The sentence is eligible. The main risk is to incorrectly convert the URI path '/v2/userProfiles/{profileId}'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 52. zhtw-project-it-ui-llm-formal-guard-v1/it-003

Changed: `script`

Input:

```text
服务账户名称 ci-release@acme-prod.iam.gserviceaccount.com 必须保持不变。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Project-original 保留情境可獨立判讀；識別碼、專名、引文或格式不得改寫。

Gemini reason: The sentence is eligible. The main risk is to incorrectly convert the service account name 'ci-release@acme-prod.iam.gserviceaccount.com'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 53. zhtw-project-it-ui-llm-formal-guard-v1/it-004

Changed: `script`

Input:

```text
数据库约束名称 fk_orders_customer_id 会出现在迁移日志中。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Project-original 保留情境可獨立判讀；識別碼、專名、引文或格式不得改寫。

Gemini reason: The sentence is eligible. The main risk is to incorrectly convert the database constraint name 'fk_orders_customer_id'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 54. zhtw-project-it-ui-llm-formal-guard-v1/it-013

Changed: `script`

Input:

```text
构建产物必须包含 linux-arm64 与 darwin-arm64 两个平台。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Project-original 保留情境可獨立判讀；識別碼、專名、引文或格式不得改寫。

Gemini reason: The sentence is eligible. The main risk is to incorrectly convert platform identifiers like 'linux-arm64'. '构建产物' is also a potential localization gap for Taiwan ('建置產出').

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 55. zhtw-project-it-ui-llm-formal-guard-v1/llm-005

Changed: `script`

Input:

```text
评测结果将 abstain 视为独立标签。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: Project-original 保留情境可獨立判讀；識別碼、專名、引文或格式不得改寫。

Gemini reason: The English technical term 'abstain' must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 56. zhtw-project-it-ui-llm-formal-guard-v1/llm-006

Changed: `script, domain`

Input:

```text
向量索引字段 embedding_v2 不得重新命名。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Project-original 保留情境可獨立判讀；識別碼、專名、引文或格式不得改寫。

Gemini reason: The technical identifier 'embedding_v2' must be preserved. '字段' is a mainland term; Taiwan equivalent is '欄位'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 57. zhtw-project-it-ui-llm-formal-guard-v1/llm-009

Changed: `script, domain`

Input:

```text
检索查询采用 hybrid_search 并将 k 设为 20。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Project-original 保留情境可獨立判讀；識別碼、專名、引文或格式不得改寫。

Gemini reason: Technical identifiers 'hybrid_search' and 'k' must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 58. zhtw-project-it-ui-llm-formal-guard-v1/llm-010

Changed: `script, domain`

Input:

```text
引用格式 [source:manual#section-4] 必须完整保留。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Project-original 保留情境可獨立判讀；識別碼、專名、引文或格式不得改寫。

Gemini reason: The reference string '[source:manual#section-4]' is a literal and must not be altered.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 59. zhtw-project-it-ui-llm-formal-guard-v1/llm-012

Changed: `script, domain`

Input:

```text
安全评估把 policy_violation 与 prompt_injection 分开统计。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Project-original 保留情境可獨立判讀；識別碼、專名、引文或格式不得改寫。

Gemini reason: The snake_case identifiers 'policy_violation' and 'prompt_injection' must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 60. zhtw-project-it-ui-llm-formal-guard-v1/llm-015

Changed: `script`

Input:

```text
解码器遇到 stop sequence </answer> 时停止生成。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: Project-original 保留情境可獨立判讀；識別碼、專名、引文或格式不得改寫。

Gemini reason: The English phrase 'stop sequence' and code-like tag '</answer>' must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 61. zhtw-project-it-ui-llm-formal-guard-v1/llm-024

Changed: `script, domain`

Input:

```text
红队案例中的字符串 DROP TABLE users; 只是测试资料。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Project-original 保留情境可獨立判讀；識別碼、專名、引文或格式不得改寫。

Gemini reason: The SQL code 'DROP TABLE users;' is a literal and must be preserved exactly.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 62. zhtw-project-it-ui-llm-formal-guard-v1/ui-001

Changed: `script`

Input:

```text
菜单项目显示“Open in New Window”，产品要求保留英文。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: Project-original 保留情境可獨立判讀；識別碼、專名、引文或格式不得改寫。

Gemini reason: The sentence itself requires preserving the English UI label 'Open in New Window'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 63. zhtw-project-it-ui-llm-formal-guard-v1/ui-002

Changed: `script`

Input:

```text
错误对话框中的代码 ERR_NETWORK_CHANGED 不得翻译。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: Project-original 保留情境可獨立判讀；識別碼、專名、引文或格式不得改寫。

Gemini reason: Identifier ERR_NETWORK_CHANGED should be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 64. zhtw-project-it-ui-llm-formal-guard-v1/ui-005

Changed: `script`

Input:

```text
拖放区域只接受 MIME 类型 text/csv。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: Project-original 保留情境可獨立判讀；識別碼、專名、引文或格式不得改寫。

Gemini reason: MIME type 'text/csv' is a technical identifier that should not be altered.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 65. zhtw-project-it-ui-llm-formal-guard-v1/ui-006

Changed: `risk`

Input:

```text
分页控件显示第 3 页，共 18 页。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Project-original 保留情境可獨立判讀；識別碼、專名、引文或格式不得改寫。

Gemini reason: Standard UI string requiring basic character conversion (e.g., 页 to 頁).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 66. zhtw-project-it-ui-llm-formal-guard-v1/ui-007

Changed: `script`

Input:

```text
状态标签“Beta”是产品名称的一部分，不随语言改变。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: Project-original 保留情境可獨立判讀；識別碼、專名、引文或格式不得改寫。

Gemini reason: The product label 'Beta' should be preserved and not translated.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 67. zhtw-project-it-ui-llm-formal-guard-v1/ui-008

Changed: `script`

Input:

```text
文件菜单中的“Save As…”使用单一省略号字符。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: Project-original 保留情境可獨立判讀；識別碼、專名、引文或格式不得改寫。

Gemini reason: Focuses on preserving the specific 'Save As…' string including the single ellipsis character (U+2026).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 68. zhtw-project-it-ui-llm-formal-guard-v1/ui-012

Changed: `script`

Input:

```text
确认窗口中的资源名称 Acme Studio 不得改写。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: Project-original 保留情境可獨立判讀；識別碼、專名、引文或格式不得改寫。

Gemini reason: Proper noun 'Acme Studio' must be preserved without modification.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 69. zhtw-project-it-ui-llm-formal-guard-v1/ui-018

Changed: `script, domain`

Input:

```text
切换按钮的状态值只能是 on 或 off。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Project-original 保留情境可獨立判讀；識別碼、專名、引文或格式不得改寫。

Gemini reason: State keywords 'on' and 'off' must be preserved as they are likely fixed values in code.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 70. zhtw-project-it-ui-llm-formal-guard-v1/ui-023

Changed: `script, risk`

Input:

```text
空白值在表格中显示为 em dash，而不是数字零。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Project-original 保留情境可獨立判讀；識別碼、專名、引文或格式不得改寫。

Gemini reason: Describes a display convention; requires standard character conversion without complex localization risks.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`
