<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 055 (2026-07-30)

Status: advisory only; maintainer decisions pending

Packet SHA-256: `fc81603d369ea0859b6dbe872452be88128d0ff2a30b39a248182ac2d4847762`
Cases: 96
Exact Codex/Gemini classifications: 61
Maintainer review queue: 35

Field differences:

- Eligibility: 5
- Script: 0
- Domain: 19
- Risk: 25

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

Neither advisory is auto-preferred. Codex must synthesize the differences before maintainer confirmation; no classification in this report has been written into the candidate pool.

## Review Queue

### 01. aosp-framework-zh-rcn-v1/string-01087053cd1a1587

Changed: `risk`

Input:

```text
SS 请求已更改为普通通话
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The phrase "普通通话" requires a standard vocabulary conversion to "一般通話" for Taiwan usage.

Maintainer decision: `pending`

### 02. aosp-framework-zh-rcn-v1/string-01c0efaaf9438832

Changed: `domain, risk`

Input:

```text
Android USB 外设端口
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: "外设端口" needs conversion to the standard Taiwan IT term like "周邊裝置連接埠", while protecting the "Android USB" identifiers.

Maintainer decision: `pending`

### 03. aosp-framework-zh-rcn-v1/string-0f5de09eb7d78ef4

Changed: `risk`

Input:

```text
已展开解锁区域。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This is a straightforward UI message that should be handled correctly by baseline character conversion.

Maintainer decision: `pending`

### 04. aosp-framework-zh-rcn-v1/string-1d37943515c4db14

Changed: `domain`

Input:

```text
周一至周五夜间
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A common date/time phrase that requires only standard character conversion.

Maintainer decision: `pending`

### 05. aosp-framework-zh-rcn-v1/string-1d91e549a4d7d527

Changed: `domain`

Input:

```text
RUIM hrpd 解锁 PIN 码
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains technical acronyms (RUIM, hrpd, PIN) that must be preserved, while "解锁" and "码" are converted.

Maintainer decision: `pending`

### 06. aosp-framework-zh-rcn-v1/string-28a1db800ec9f522

Changed: `risk`

Input:

```text
指纹图标
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The term "图标" should be converted to "圖示" which is more common in Taiwan UI terminology.

Maintainer decision: `pending`

### 07. aosp-framework-zh-rcn-v1/string-4809b73ce51e5a8b

Changed: `risk`

Input:

```text
详情请与您的 IT 管理员联系
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Requires vocabulary conversion for "详情" (to "詳細資訊") and "管理员" (to "管理員"), while preserving "IT".

Maintainer decision: `pending`

### 08. aosp-framework-zh-rcn-v1/string-82fa41f1d5373433

Changed: `risk`

Input:

```text
允许该应用建立和断开平板电脑与 WiMAX 网络之间的连接。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This permission string requires multiple standard IT vocabulary conversions ("应用", "网络", "连接") while preserving "WiMAX".

Maintainer decision: `pending`

### 09. aosp-framework-zh-rcn-v1/string-8e0e8eed25f4cc61

Changed: `risk`

Input:

```text
双击可以进行缩放控制
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This is a straightforward UI instruction.

Maintainer decision: `pending`

### 10. aosp-framework-zh-rcn-v1/string-b61bfcc25cf226bd

Changed: `domain`

Input:

```text
地理围栏服务
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This tests the translation of the technical term 'geofencing service'.

Maintainer decision: `pending`

### 11. aosp-framework-zh-rcn-v1/string-c079ea22c59ee135

Changed: `risk`

Input:

```text
没有应用可执行此操作。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This is a standard and common system message.

Maintainer decision: `pending`

### 12. aosp-framework-zh-rcn-v1/string-c91d02d1c37ae3c5

Changed: `domain, risk`

Input:

```text
允许具有该权限的应用开始查看某个应用的功能信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This is a formal permission description with standard IT terms.

Maintainer decision: `pending`

### 13. aosp-framework-zh-rcn-v1/string-cbb4eeb877604903

Changed: `risk`

Input:

```text
最近没有运行任何应用
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This is a standard UI string for an empty 'recent apps' list.

Maintainer decision: `pending`

### 14. aosp-framework-zh-rcn-v1/string-d2c71079faa2a4df

Changed: `risk`

Input:

```text
打开声音
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The phrase '打开声音' (turn on sound) may have a more idiomatic equivalent in Taiwan.

Maintainer decision: `pending`

### 15. aosp-framework-zh-rcn-v1/string-d37853a20ad70674

Changed: `risk`

Input:

```text
设备会在%2$s无法访问互联网时使用%1$s（可能需要支付相应的费用）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This tests the crucial vocabulary difference for '互联网' (internet) and handling of placeholders.

Maintainer decision: `pending`

### 16. aosp-framework-zh-rcn-v1/string-ee7cac52d96c69c7

Changed: `risk`

Input:

```text
允许以状态栏形式显示应用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This is a standard permission description involving the term 'status bar'.

Maintainer decision: `pending`

### 17. ready-gov-are-you-ready-guide-simplified-v1/sentence-034

Changed: `risk`

Input:

```text
最后，与您的朋友和邻居讨论，以了解他们正在准备的紧急情况的类型以及他们将要采取的措施。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | awkward_source_translation |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The sentence is a clear directive on emergency preparedness, and terms like "情况" (situation) may have different common usage in Taiwan.

Maintainer decision: `pending`

### 18. ready-gov-are-you-ready-guide-simplified-v1/sentence-075

Changed: `eligible, domain, risk`

Input:

```text
他们可能必须沿途经过伤者。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: The pronoun has no standalone antecedent, so the sentence cannot be judged fairly without context.

Gemini reason: The sentence uses common, unambiguous terms and serves as a good baseline for simple conversion.

Maintainer decision: `pending`

### 19. ready-gov-are-you-ready-guide-simplified-v1/sentence-128

Changed: `eligible, domain, risk`

Input:

```text
储蓄节省金钱和维持一笔应急资金是明智的做法，可以使您在灾后能够帮助您自己、亲人和社区。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | unsafe_source_translation |
| Gemini | yes | high_stakes | candidate_gap | high | redundant_phrasing |

Codex reason: The opening phrase 储蓄节省金钱 is duplicated and semantically broken.

Gemini reason: The phrase "储蓄节省金钱" is redundant, and terms like "应急资金" might have specific Taiwanese equivalents.

Maintainer decision: `pending`

### 20. ready-gov-are-you-ready-guide-simplified-v1/sentence-218

Changed: `risk`

Input:

```text
手机和任何电池供电的设备要保持充电状态，并确保有备用的充电方法，例如车载充电器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The sentence contains technical but widely standardized terms like "手机" and "充电器" which should convert directly.

Maintainer decision: `pending`

### 21. ready-gov-are-you-ready-guide-simplified-v1/sentence-258

Changed: `domain`

Input:

```text
清理期间要穿厚底鞋、长裤，戴工作手套。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Standard safety instruction, simple vocabulary.

Maintainer decision: `pending`

### 22. ready-gov-are-you-ready-guide-simplified-v1/sentence-265

Changed: `eligible, domain, risk`

Input:

```text
选择海拔100英尺或更高或庇护所，或在内陆至少一英里内。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | unsafe_source_translation |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: The evacuation instruction is missing its main action and has broken altitude and inland-distance logic.

Gemini reason: Standard safety guidance with unit measurements.

Maintainer decision: `pending`

### 23. ready-gov-are-you-ready-guide-simplified-v1/sentence-318

Changed: `domain`

Input:

```text
您还应该将副本张贴在家里的中央位置，例如冰箱或家庭布告栏上。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The term '布告栏' (bulletin board) might have a different common usage in Taiwan.

Maintainer decision: `pending`

### 24. ready-gov-are-you-ready-guide-simplified-v1/sentence-370

Changed: `domain, risk`

Input:

```text
彻底更换衣服，包括长袖衬衫、长裤和结实的鞋子。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Basic vocabulary for clothing and personal safety.

Maintainer decision: `pending`

### 25. ready-gov-are-you-ready-guide-simplified-v1/sentence-371

Changed: `eligible, domain, risk`

Input:

```text
露营用厨具、纸杯、塑料盘子和餐具以及纸巾。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: This is a supplies-list fragment without a standalone instruction or statement.

Gemini reason: The term for '塑料' (plastic) is a known regional difference.

Maintainer decision: `pending`

### 26. ready-gov-are-you-ready-guide-simplified-v1/sentence-392

Changed: `risk`

Input:

```text
这是至关重要的步骤，因为您可能需要此财产清单来作为保险记录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | awkward_source_translation |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Standard financial/insurance terminology.

Maintainer decision: `pending`

### 27. ready-gov-are-you-ready-guide-simplified-v1/sentence-424

Changed: `risk`

Input:

```text
确保检查您的保单，了解它承保了哪些危险以及在什么情况下。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Standard insurance policy language.

Maintainer decision: `pending`

### 28. ready-gov-are-you-ready-guide-simplified-v1/sentence-436

Changed: `domain`

Input:

```text
洪水影响到每个地区和州，并且可能发生在任何地方。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: General statement about floods, standard vocabulary.

Maintainer decision: `pending`

### 29. ready-gov-are-you-ready-guide-simplified-v1/sentence-453

Changed: `domain`

Input:

```text
加强房屋的减灾技术通常对不止一种类型的灾难有益。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | awkward_source_translation |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The term '减灾' (disaster mitigation) may require a phrase-level adaptation for Taiwan.

Maintainer decision: `pending`

### 30. ready-gov-are-you-ready-guide-simplified-v1/sentence-468

Changed: `domain, risk`

Input:

```text
确保重要文件的安全和更新。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | awkward_source_translation |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A simple and clear instruction with common vocabulary.

Maintainer decision: `pending`

### 31. ready-gov-are-you-ready-guide-simplified-v1/sentence-523

Changed: `eligible, domain, risk`

Input:

```text
您所在的地区可能有生效的《烧水通知》。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | unsafe_source_translation |
| Gemini | yes | high_stakes | candidate_gap | high | proper_noun |

Codex reason: The phrase 烧水通知 is an unsafe source translation of a boil-water advisory.

Gemini reason: The specific term '烧水通知' (Boil Water Notice) might be an official name requiring specific localization.

Maintainer decision: `pending`

### 32. ready-gov-are-you-ready-guide-simplified-v1/sentence-561

Changed: `domain`

Input:

```text
要求提供带照片的官方身份证件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Standard request for identification.

Maintainer decision: `pending`

### 33. zhtw-project-ui-social-baseline-guard-v1/ui-016

Changed: `domain`

Input:

```text
远程地址验证失败，请检查网络连接。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The word for 'network' ('网络' vs. '網路') is a common and important distinction for localization.

Maintainer decision: `pending`

### 34. zhtw-project-ui-social-baseline-guard-v1/ui-032

Changed: `risk`

Input:

```text
停用成员后，历史操作记录仍会保留。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: UI text where terms like 'deactivate member' and 'history log' may have more idiomatic Taiwan equivalents.

Maintainer decision: `pending`

### 35. zhtw-project-ui-social-baseline-guard-v1/ui-045

Changed: `domain`

Input:

```text
快捷键 Ctrl+Shift+P 会打开命令面板。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This UI text includes a key combination ('Ctrl+Shift+P') that must be protected from conversion.

Maintainer decision: `pending`
