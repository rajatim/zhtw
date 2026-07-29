<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 058 (2026-07-30)

Status: advisory only; maintainer decisions pending

Packet SHA-256: `cb01fd80fb833009a1b9b5c458feede19b7de575881e5e4d135e0a6deebe9034`
Cases: 96
Exact Codex/Gemini classifications: 45
Maintainer review queue: 51

Field differences:

- Eligibility: 2
- Script: 21
- Domain: 2
- Risk: 47

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

Neither advisory is auto-preferred. Codex must synthesize the differences before maintainer confirmation; no classification in this report has been written into the candidate pool.

## Review Queue

### 01. aosp-framework-zh-rcn-v1/string-00a7e8cc219d5e5b

Changed: `script, risk`

Input:

```text
SPN 解锁请求失败。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete Android UI string for SIM/SPN unlock request failure.

Maintainer decision: `pending`

### 02. aosp-framework-zh-rcn-v1/string-1a6e0556ca10b275

Changed: `script, risk`

Input:

```text
%1$s 的连接受限
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete network connection notification template with format specifiers.

Maintainer decision: `pending`

### 03. aosp-framework-zh-rcn-v1/string-1e9182ec0b1382dc

Changed: `script, risk`

Input:

```text
系统无法再识别%1$s和%2$s。请重新设置指纹解锁功能。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete multi-sentence security prompt string with positional format specifiers.

Maintainer decision: `pending`

### 04. aosp-framework-zh-rcn-v1/string-623c388c1e95e498

Changed: `script, risk`

Input:

```text
“%1$s”想要显示“%2$s”图块
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete Quick Settings UI tile prompt string with dynamic placeholders.

Maintainer decision: `pending`

### 05. aosp-framework-zh-rcn-v1/string-800d22264189155e

Changed: `script, risk`

Input:

```text
%1$d 个应用正在消耗电量
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: UI string with format specifier.

Maintainer decision: `pending`

### 06. aosp-framework-zh-rcn-v1/string-83543ce4538d9d1d

Changed: `script, risk`

Input:

```text
新PIN码
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: UI label for PIN code.

Maintainer decision: `pending`

### 07. aosp-framework-zh-rcn-v1/string-aad3ea7dce47e9bf

Changed: `risk`

Input:

```text
请保持冷静，并寻找附近的避难地点。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Standard emergency prompt string.

Maintainer decision: `pending`

### 08. aosp-framework-zh-rcn-v1/string-ad8a1a6d85619913

Changed: `script, risk`

Input:

```text
建立或中断 WiMAX 网络连接
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: UI string with network terminology.

Maintainer decision: `pending`

### 09. aosp-framework-zh-rcn-v1/string-b9900485757db599

Changed: `script, risk`

Input:

```text
高优先顺序 SIM 卡状态
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: UI label with status and priority wording.

Maintainer decision: `pending`

### 10. aosp-framework-zh-rcn-v1/string-c4c3978186018f25

Changed: `risk`

Input:

```text
系统变更
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Short UI title string.

Maintainer decision: `pending`

### 11. aosp-framework-zh-rcn-v1/string-d6179f98ac22da8b

Changed: `script, risk`

Input:

```text
手指 %d
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Short UI string with placeholder.

Maintainer decision: `pending`

### 12. aosp-framework-zh-rcn-v1/string-e27eaa3bbfb5ee15

Changed: `script, risk`

Input:

```text
由“%1$s”提供。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: UI attribution string with quotes and placeholder.

Maintainer decision: `pending`

### 13. ready-gov-are-you-ready-guide-simplified-v1/sentence-004

Changed: `risk`

Input:

```text
因此，当地的急救人员和其他协助可能无法立即到位。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete statement regarding emergency responder availability.

Maintainer decision: `pending`

### 14. ready-gov-are-you-ready-guide-simplified-v1/sentence-061

Changed: `risk`

Input:

```text
描述每个枪手的情况、他们的位置和所持武器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete active shooter situational response instruction.

Maintainer decision: `pending`

### 15. ready-gov-are-you-ready-guide-simplified-v1/sentence-091

Changed: `eligible, domain, risk`

Input:

```text
定期将文件备份到加密文件或加密文件存储设备中。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | unsafe_source_translation |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex excluded this input-only case because the source text is not reliable enough for an independently judgeable conversion benchmark.

Gemini reason: Complete data backup instruction containing IT terms (文件/存储/设备).

Maintainer decision: `pending`

### 16. ready-gov-are-you-ready-guide-simplified-v1/sentence-121

Changed: `script, risk`

Input:

```text
拨打911或立即将患者送往医院。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete medical emergency instruction.

Maintainer decision: `pending`

### 17. ready-gov-are-you-ready-guide-simplified-v1/sentence-146

Changed: `risk`

Input:

```text
将家具，贵重物品和重要文件移到安全的高处。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete flood preparation instruction.

Maintainer decision: `pending`

### 18. ready-gov-are-you-ready-guide-simplified-v1/sentence-182

Changed: `risk`

Input:

```text
远离山体滑坡或泥石流的路径。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete landslide/mudslide evacuation guidance.

Maintainer decision: `pending`

### 19. ready-gov-are-you-ready-guide-simplified-v1/sentence-245

Changed: `risk`

Input:

```text
考虑购买电涌保护器、避雷针或避雷系统，以保护您的房子、家用电器和电子设备。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete surge protection equipment advice.

Maintainer decision: `pending`

### 20. ready-gov-are-you-ready-guide-simplified-v1/sentence-279

Changed: `script, risk`

Input:

```text
在您的应急工具包中保留几个 N95 口罩，以避免在事件发生期间和之后吸入危险微粒。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete respirator/mask preparation sentence with standard mixed Latin identifier N95.

Maintainer decision: `pending`

### 21. ready-gov-are-you-ready-guide-simplified-v1/sentence-291

Changed: `script, risk`

Input:

```text
在应急包中保留几个N95口罩，以避免在事件发生期间和之后吸入危险颗粒。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete emergency preparedness instruction regarding N95 mask usage.

Maintainer decision: `pending`

### 22. ready-gov-are-you-ready-guide-simplified-v1/sentence-317

Changed: `risk`

Input:

```text
确保每个人都了解家庭紧急通信计划，并始终都随身携带电子版或钱包卡副本。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete sentence regarding family emergency communication plan and documentation.

Maintainer decision: `pending`

### 23. ready-gov-are-you-ready-guide-simplified-v1/sentence-354

Changed: `script, risk`

Input:

```text
在灾难发生之前，向专业水管工或电工、当地公用事业提供商咨询，或在 Ready.gov上了解如何进行这些操作。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete sentence offering advisory guidance for disaster preparation.

Maintainer decision: `pending`

### 24. ready-gov-are-you-ready-guide-simplified-v1/sentence-406

Changed: `risk`

Input:

```text
您还可以使用具有本地警报功能的移动应用程序，以随时了解所在地区的危险。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete guidance sentence on using mobile app alerts for local hazards.

Maintainer decision: `pending`

### 25. ready-gov-are-you-ready-guide-simplified-v1/sentence-452

Changed: `eligible, domain, risk`

Input:

```text
缓解影响的例子包括：在屋外修剪树木，安装可用百叶窗，固定预制房屋或造个龙卷风安全室来保护家人。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | unsafe_source_translation |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex excluded this input-only case because the source text is not reliable enough for an independently judgeable conversion benchmark.

Gemini reason: Complete sentence giving actionable disaster impact mitigation examples.

Maintainer decision: `pending`

### 26. ready-gov-are-you-ready-guide-simplified-v1/sentence-489

Changed: `risk`

Input:

```text
直到帮助抵达是一个项目，该项目教授简单的救生技能，直到应急服务前来帮助为止。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete descriptive sentence explaining the Until Help Arrives program.

Maintainer decision: `pending`

### 27. ready-gov-are-you-ready-guide-simplified-v1/sentence-534

Changed: `risk`

Input:

```text
理赔员将需要您的住房和财产损失的证据来准备您的修复评估。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete sentence regarding insurance claim adjuster documentation requirements.

Maintainer decision: `pending`

### 28. zhtw-project-llm-formal-reasoning-guard-v1/formal-002

Changed: `risk`

Input:

```text
主管机关要求申请人于期限内补齐证明文件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete formal administrative statement requiring standard Simplified-to-Traditional conversion.

Maintainer decision: `pending`

### 29. zhtw-project-llm-formal-reasoning-guard-v1/formal-008

Changed: `risk`

Input:

```text
调查单位尚未确认事件发生的确切时间。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete formal statement requiring standard Simplified-to-Traditional conversion.

Maintainer decision: `pending`

### 30. zhtw-project-llm-formal-reasoning-guard-v1/formal-012

Changed: `risk`

Input:

```text
机关已通知业者改善标示不清的项目。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete formal administrative sentence requiring standard character conversion.

Maintainer decision: `pending`

### 31. zhtw-project-llm-formal-reasoning-guard-v1/formal-014

Changed: `risk`

Input:

```text
申请文件缺少适用范围与执行期间。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete formal sentence covering scope and execution period.

Maintainer decision: `pending`

### 32. zhtw-project-llm-formal-reasoning-guard-v1/formal-015

Changed: `risk`

Input:

```text
委员会将在下次会议确认修正后的条文。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete formal committee statement requiring standard character conversion.

Maintainer decision: `pending`

### 33. zhtw-project-llm-formal-reasoning-guard-v1/formal-018

Changed: `risk`

Input:

```text
报告指出目前证据不足以支持这项结论。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete formal report statement regarding evidence and conclusions.

Maintainer decision: `pending`

### 34. zhtw-project-llm-formal-reasoning-guard-v1/formal-031

Changed: `script`

Input:

```text
声明引用“status quo ante”时维持原文拼写。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Formal statement containing Latin phrase 'status quo ante' which must be preserved without over-conversion.

Maintainer decision: `pending`

### 35. zhtw-project-llm-formal-reasoning-guard-v1/formal-032

Changed: `script`

Input:

```text
法院文件保留当事人登记的 Chen Yu-Han。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Court document statement containing proper name 'Chen Yu-Han' requiring exact preservation.

Maintainer decision: `pending`

### 36. zhtw-project-llm-formal-reasoning-guard-v1/formal-034

Changed: `script`

Input:

```text
专利公告以 WO 2026/098765 标示国际申请。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Patent announcement containing international application code 'WO 2026/098765' requiring exact preservation.

Maintainer decision: `pending`

### 37. zhtw-project-llm-formal-reasoning-guard-v1/formal-035

Changed: `script`

Input:

```text
财政资料将 FY2028 视为会计年度识别码。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Financial data statement containing fiscal year code 'FY2028' requiring exact preservation.

Maintainer decision: `pending`

### 38. zhtw-project-llm-formal-reasoning-guard-v1/formal-042

Changed: `risk`

Input:

```text
主管机关保留后续查核资料的权利。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete formal statement regarding authority auditing rights.

Maintainer decision: `pending`

### 39. zhtw-project-llm-formal-reasoning-guard-v1/formal-044

Changed: `risk`

Input:

```text
委员会要求各单位指定单一联络窗口。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete committee requirement statement specifying point-of-contact designation.

Maintainer decision: `pending`

### 40. zhtw-project-llm-formal-reasoning-guard-v1/formal-047

Changed: `risk`

Input:

```text
新闻稿说明本次修正不会影响既有权利。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete press release statement regarding existing rights.

Maintainer decision: `pending`

### 41. zhtw-project-llm-formal-reasoning-guard-v1/formal-050

Changed: `risk`

Input:

```text
机关将在网站公布最终核定名单。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete official announcement sentence regarding final approved list publication.

Maintainer decision: `pending`

### 42. zhtw-project-llm-formal-reasoning-guard-v1/llm-002

Changed: `risk`

Input:

```text
模型应先说明假设，再给出可以验证的结论。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete LLM instruction prompt sentence requiring standard character conversion.

Maintainer decision: `pending`

### 43. zhtw-project-llm-formal-reasoning-guard-v1/llm-006

Changed: `risk`

Input:

```text
回答中引用的页码必须对应上传文件的实际页数。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete LLM guidance sentence regarding page number referencing.

Maintainer decision: `pending`

### 44. zhtw-project-llm-formal-reasoning-guard-v1/llm-008

Changed: `risk`

Input:

```text
请比较两个方案的成本、风险和相依性。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Valid Simplified input testing preservation of common terms like 方案.

Maintainer decision: `pending`

### 45. zhtw-project-llm-formal-reasoning-guard-v1/llm-015

Changed: `risk`

Input:

```text
回答应区分事实、推论和仍待确认的事项。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Valid Simplified input testing over-conversion guard for 事項 vs 專案.

Maintainer decision: `pending`

### 46. zhtw-project-llm-formal-reasoning-guard-v1/llm-018

Changed: `risk`

Input:

```text
摘要不得省略原文中的限制条件和例外情况。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Valid Simplified input testing baseline character conversion.

Maintainer decision: `pending`

### 47. zhtw-project-llm-formal-reasoning-guard-v1/llm-019

Changed: `risk`

Input:

```text
请确认引用内容来自正文，不是模型自动生成的补充说明。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Valid Simplified input testing standard character conversion.

Maintainer decision: `pending`

### 48. zhtw-project-llm-formal-reasoning-guard-v1/llm-024

Changed: `script, risk`

Input:

```text
请保留错误代码 E_AUTH_403 和括号内说明。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Valid Simplified input testing error code term and preservation of Latin identifier.

Maintainer decision: `pending`

### 49. zhtw-project-llm-formal-reasoning-guard-v1/llm-025

Changed: `script, risk`

Input:

```text
版本标签 v3.2.1-rc.4 不得转换或拆分。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Valid Simplified input testing tag term conversion while preserving version number.

Maintainer decision: `pending`

### 50. zhtw-project-llm-formal-reasoning-guard-v1/llm-039

Changed: `script, risk`

Input:

```text
回答中的优惠券编号 TW-2026-08 必须保持不变。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Valid Simplified input testing coupon and number terms with invariant code identifier.

Maintainer decision: `pending`

### 51. zhtw-project-llm-formal-reasoning-guard-v1/llm-045

Changed: `risk`

Input:

```text
最终回答只保留已经通过资料检核的项目。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Valid Simplified input testing contextual over-conversion guard for 項目 vs 專案.

Maintainer decision: `pending`
