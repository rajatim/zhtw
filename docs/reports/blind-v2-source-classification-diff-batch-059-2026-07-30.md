<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 059 (2026-07-30)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `baaff86856252f5729b76eaa3e832bf347603bbd0dc95c818c35c94e8e1d245c`
Cases: 96
Exact Codex/Gemini classifications: 30
Maintainer review queue: 66

Field differences:

- Eligibility: 4
- Script: 22
- Domain: 14
- Risk: 58

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

The maintainer resolved all 66 advisory disagreements and batch-confirmed the 30 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. aosp-framework-zh-rcn-v1/string-095b1a9558f5a29a

Changed: `eligible, script, domain, risk`

Input:

```text
要在""%4$s""中更新%1$s、%2$s和%3$s吗？
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_formatting |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex excluded this input-only case because the source text is not reliable enough for an independently judgeable conversion benchmark.

Gemini reason: Complete UI confirmation string with positional parameters.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 02. aosp-framework-zh-rcn-v1/string-0a81c079e142f72c

Changed: `script, risk`

Input:

```text
正在检查%s…
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete UI progress status string with placeholder.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 03. aosp-framework-zh-rcn-v1/string-0bd6441dd9eb69c0

Changed: `script, risk`

Input:

```text
当前PIN码
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete UI label for current PIN code.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 04. aosp-framework-zh-rcn-v1/string-1051aff928b0de5b

Changed: `risk`

Input:

```text
请将手机拿近一点
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete UI instruction prompt.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 05. aosp-framework-zh-rcn-v1/string-42a2c1fbb6bb7299

Changed: `risk`

Input:

```text
没有服务
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete mobile network status string.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 06. aosp-framework-zh-rcn-v1/string-451bc6e12518d336

Changed: `script, risk`

Input:

```text
已将内容移至%s
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete notification string with placeholder.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 07. aosp-framework-zh-rcn-v1/string-68b6ba8b4db24860

Changed: `script, risk`

Input:

```text
PIN码更改
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete UI menu or dialog title string.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 08. aosp-framework-zh-rcn-v1/string-6adcfcdd14784a8d

Changed: `script, risk`

Input:

```text
已配置“%s”
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete system configuration status string with placeholder.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 09. aosp-framework-zh-rcn-v1/string-73dd6da99f4de148

Changed: `risk`

Input:

```text
在手机上继续操作
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete cross-device guidance prompt string.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 10. aosp-framework-zh-rcn-v1/string-7fc45bbd4a14dc5f

Changed: `script, risk`

Input:

```text
%1$s将会在不保存的情况下关闭
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete UI warning string with parameter.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 11. aosp-framework-zh-rcn-v1/string-8000a6454087a523

Changed: `risk`

Input:

```text
拨打电话
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete UI action button label string.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 12. aosp-framework-zh-rcn-v1/string-896dca5c1be49579

Changed: `risk`

Input:

```text
ICCID 解锁 PIN 码
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete Android UI string for ICCID unlock PIN code.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 13. aosp-framework-zh-rcn-v1/string-a127f1ce093ef149

Changed: `risk`

Input:

```text
正在弹出…
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete UI status text with ellipsis.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 14. aosp-framework-zh-rcn-v1/string-b0d9b88578c64d2b

Changed: `risk`

Input:

```text
第三个工作%1$s
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete UI template string with format placeholder.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 15. aosp-framework-zh-rcn-v1/string-b706df11d0c80205

Changed: `risk`

Input:

```text
您输入的PIN码不一致。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete PIN mismatch error message.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 16. aosp-framework-zh-rcn-v1/string-c8b823a227665b7a

Changed: `risk`

Input:

```text
选择月份和日期
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete date selection UI prompt.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 17. aosp-framework-zh-rcn-v1/string-e009ca03ab8d36a2

Changed: `risk`

Input:

```text
SIM 卡不支持语音
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete warning string for unsupported SIM voice capability.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 18. aosp-framework-zh-rcn-v1/string-e35d449a382ceb38

Changed: `risk`

Input:

```text
<b>%1$s</b>想要向 <b>%2$s</b> 发送一条短信。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete formatted UI string with HTML tags and placeholders.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 19. aosp-framework-zh-rcn-v1/string-f55f1da12348ad4e

Changed: `risk`

Input:

```text
向 SIM 卡发送命令
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete operation string for sending command to SIM card.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 20. aosp-framework-zh-rcn-v1/string-f7a5708bfb37ea59

Changed: `risk`

Input:

```text
请略微调整头部的位置
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete camera/biometric guidance prompt string.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 21. ready-gov-are-you-ready-guide-simplified-v1/sentence-020

Changed: `risk`

Input:

```text
此外，使用您的社交网络来帮助朋友和家人做好准备，并参加社区范围的备灾活动。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains terminology differences such as 社交网络 (社交網路) and 备灾 (備災).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 22. ready-gov-are-you-ready-guide-simplified-v1/sentence-021

Changed: `risk`

Input:

```text
此外，您应该收集应急用品，并保管好开始恢复所需的信息和重要文件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains term mapping gaps including 信息 (資訊) and 应急 (應急/防災).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 23. ready-gov-are-you-ready-guide-simplified-v1/sentence-082

Changed: `risk`

Input:

```text
戴好头盔，以减少头部受伤，并戴上雪崩信标以帮助其他人找到您。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains domain specific term 雪崩信标.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 24. ready-gov-are-you-ready-guide-simplified-v1/sentence-092

Changed: `risk`

Input:

```text
减少您在线共享的个人信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains vocabulary conversion candidates such as 在线 (線上) and 个人信息 (個人資訊).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 25. ready-gov-are-you-ready-guide-simplified-v1/sentence-097

Changed: `risk`

Input:

```text
如果附近有结实的家具，而且您可以爬到那里同时不需穿过杂物碎片，请在结实家具下掩护以保护身体，并用手臂和其他物体遮盖住头颈部。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete complex emergency instruction involving terms like 结实 and 掩护.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 26. ready-gov-are-you-ready-guide-simplified-v1/sentence-181

Changed: `risk`

Input:

```text
山体滑坡的迹象可能不明显，但危险仍然存在。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains disaster vocabulary 山体滑坡 (土石流/山崩).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 27. ready-gov-are-you-ready-guide-simplified-v1/sentence-196

Changed: `risk`

Input:

```text
您的家人应该就地呆在室内。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Tests character disambiguation for 呆在 (待在).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 28. ready-gov-are-you-ready-guide-simplified-v1/sentence-198

Changed: `risk`

Input:

```text
在事件发生前，请确定您最常去的地方，例如住家、工作场所或学校，附近的最佳庇护所位置。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains emergency terminology 庇护所 (避難所).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 29. ready-gov-are-you-ready-guide-simplified-v1/sentence-208

Changed: `script, risk`

Input:

```text
如果没有肥皂和水，请使用酒精含量至少 60％的免洗洗手液。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains high-frequency term discrepancy 免洗洗手液 (乾洗手).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 30. ready-gov-are-you-ready-guide-simplified-v1/sentence-210

Changed: `risk`

Input:

```text
如有可能，请留在家中并与他人，保持社交距离。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | awkward_punctuation |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete public health instruction testing 社交距离 (社交距離), despite mid-sentence comma placement.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 31. ready-gov-are-you-ready-guide-simplified-v1/sentence-225

Changed: `risk`

Input:

```text
切勿使用燃气灶或烤箱取暖。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete public safety instruction regarding heating appliances.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 32. ready-gov-are-you-ready-guide-simplified-v1/sentence-228

Changed: `risk`

Input:

```text
在冰箱和冰柜中放置温度计，以监测温度。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete food safety monitoring sentence.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 33. ready-gov-are-you-ready-guide-simplified-v1/sentence-252

Changed: `eligible, domain, risk`

Input:

```text
如果您无法到达防风洞或安全室，下一个最佳保护措施是：确定最佳可用避难区（BARA）；或位于坚固建筑物最底层没有水灾风险的，内部无窗小房间。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | unsafe_source_translation |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex excluded this input-only case because the source text is not reliable enough for an independently judgeable conversion benchmark.

Gemini reason: Complete shelter advisory statement containing a Latin acronym.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 34. ready-gov-are-you-ready-guide-simplified-v1/sentence-369

Changed: `eligible, domain, risk`

Input:

```text
每个人的睡袋或保暖毯；如果您居住在寒冷的气候中，则可能需要额外的被褥。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | no | null | null | high | fragment_without_context |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Excluded due to list item fragment structure starting with a noun phrase and semicolon.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 35. ready-gov-are-you-ready-guide-simplified-v1/sentence-419

Changed: `eligible, domain, risk`

Input:

```text
人造房屋、公寓和农场都有特殊的保险保单。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | unsafe_source_translation |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex excluded this input-only case because the source text is not reliable enough for an independently judgeable conversion benchmark.

Gemini reason: Complete insurance policy description sentence.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 36. ready-gov-are-you-ready-guide-simplified-v1/sentence-438

Changed: `script, risk`

Input:

```text
仅 1 英寸水深所造成的损失可能超过 2.5 万美元。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete flood damage cost estimation sentence.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 37. ready-gov-are-you-ready-guide-simplified-v1/sentence-443

Changed: `risk`

Input:

```text
如果您找不到能满足需要的保险公司，请与州保险部门联系。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete guidance sentence for seeking insurance department assistance.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 38. ready-gov-are-you-ready-guide-simplified-v1/sentence-461

Changed: `risk`

Input:

```text
此外，可以在专业人员帮助下在现有房屋加装龙卷风安全室等防护措施。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete retrofitting advice sentence for tornado safety rooms.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 39. ready-gov-are-you-ready-guide-simplified-v1/sentence-568

Changed: `risk`

Input:

```text
您可能需要准备好个人信息，例如社会安全号码和银行帐号，以申请帮助。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete personal information preparation instruction for disaster relief.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 40. ready-gov-are-you-ready-guide-simplified-v1/sentence-571

Changed: `risk`

Input:

```text
FEMA检查人员检查损坏情况，但不雇用或支持特定承包商修理房屋或建议维修。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete FEMA inspector policy and fraud advisory sentence.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 41. zhtw-project-llm-formal-reasoning-guard-v1/formal-003

Changed: `domain, risk`

Input:

```text
审计人员将核对原始凭证与授权记录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete formal sentence regarding financial and audit verification records.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 42. zhtw-project-llm-formal-reasoning-guard-v1/formal-005

Changed: `risk`

Input:

```text
公告内容自发布次日起正式生效。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete official announcement sentence specifying effective date.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 43. zhtw-project-llm-formal-reasoning-guard-v1/formal-016

Changed: `risk`

Input:

```text
公开资料未包含仍在调查中的个案。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete formal statement concerning exclusion of active investigation cases.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 44. zhtw-project-llm-formal-reasoning-guard-v1/formal-019

Changed: `risk`

Input:

```text
主管机关将另行公布申请方式与审查标准。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete formal notice from governing authority regarding future announcements.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 45. zhtw-project-llm-formal-reasoning-guard-v1/formal-021

Changed: `script`

Input:

```text
决议编号 GOV-TW-2026-041 应列在文件首页。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Formal document layout rule containing an alphanumeric identifier string.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 46. zhtw-project-llm-formal-reasoning-guard-v1/formal-022

Changed: `script, risk`

Input:

```text
附件 A-3 记载各单位的联络窗口。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete formal sentence detailing attachment contact information.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 47. zhtw-project-llm-formal-reasoning-guard-v1/formal-026

Changed: `script, domain`

Input:

```text
判决附件引用文件代号 A/HRC/56/12。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Legal and judicial reference sentence containing an official document code.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 48. zhtw-project-llm-formal-reasoning-guard-v1/formal-027

Changed: `script`

Input:

```text
委员会文件以 COM(2026) 57 final 为正式编号。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Official committee reference sentence containing an EU document code.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 49. zhtw-project-llm-formal-reasoning-guard-v1/formal-028

Changed: `script, domain, risk`

Input:

```text
技术规范引用 ISO/IEC 27001:2022。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Technical specification sentence citing an ISO standard identifier.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 50. zhtw-project-llm-formal-reasoning-guard-v1/formal-038

Changed: `risk`

Input:

```text
统计结果依年龄层和地区分别呈现。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete formal sentence describing demographic breakdown of statistical results.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 51. zhtw-project-llm-formal-reasoning-guard-v1/formal-039

Changed: `risk`

Input:

```text
审查意见未涉及申请人的其他项目。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete administrative review finding sentence.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 52. zhtw-project-llm-formal-reasoning-guard-v1/formal-041

Changed: `domain, risk`

Input:

```text
跨行汇款手续费由申请人自行负担。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Financial and banking rules sentence regarding wire transfer fee obligations.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 53. zhtw-project-llm-formal-reasoning-guard-v1/formal-048

Changed: `risk`

Input:

```text
会议决议仅用于后续行政程序。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Formal procedural statement regarding meeting resolution scope.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 54. zhtw-project-llm-formal-reasoning-guard-v1/llm-003

Changed: `risk`

Input:

```text
如果证据不足，请明确回答目前无法判断。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: LLM prompt instruction specifying response protocol under insufficient evidence.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 55. zhtw-project-llm-formal-reasoning-guard-v1/llm-007

Changed: `domain`

Input:

```text
工具调用失败后，助理应显示可执行的重试建议。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Complete prompt instruction for assistant handling tool calls, testing IT term conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 56. zhtw-project-llm-formal-reasoning-guard-v1/llm-023

Changed: `script, risk`

Input:

```text
模型输出中的 HTTPS URL 不应加入多余空格。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Formatting constraint containing Latin acronyms and output terminology.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 57. zhtw-project-llm-formal-reasoning-guard-v1/llm-026

Changed: `script, domain, risk`

Input:

```text
引用 Git commit 7f3a9c2 时必须维持七位字符。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Technical instruction referencing Git commit hash and testing character/byte terminology.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 58. zhtw-project-llm-formal-reasoning-guard-v1/llm-027

Changed: `script, domain, risk`

Input:

```text
模型应将变量 max_retry_count 视为程序识别码。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Code-level specification testing variable and program term conversions alongside code identifiers.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 59. zhtw-project-llm-formal-reasoning-guard-v1/llm-030

Changed: `script`

Input:

```text
请勿翻译产品名称 ThinkPad X1 Carbon Gen 13。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Instruction containing hardware product name, guarding against over-conversion of brand identifiers.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 60. zhtw-project-llm-formal-reasoning-guard-v1/llm-036

Changed: `domain`

Input:

```text
请说明消息消费者停止后尚有多少待处理消息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Message consumer domain sentence testing message queue terminology conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 61. zhtw-project-llm-formal-reasoning-guard-v1/llm-043

Changed: `risk`

Input:

```text
模型应指出这段文字可能来自旧版说明。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Standard instruction sentence without complex IT terminology gaps, serving as baseline conversion guard.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 62. zhtw-project-llm-formal-reasoning-guard-v1/llm-044

Changed: `script`

Input:

```text
请比较 Codex 与 Gemini 的判断，并列出需要人工确认的差异。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Comparison prompt referencing model proper nouns Codex and Gemini.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 63. zhtw-project-llm-formal-reasoning-guard-v1/llm-046

Changed: `script, domain, risk`

Input:

```text
请不要把 Web 视图当成台湾常用的产品名称。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: UI i18n related sentence testing view terminology in web software contexts.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 64. zhtw-project-llm-formal-reasoning-guard-v1/llm-047

Changed: `script`

Input:

```text
模型应在引用原话时保留“due process”这个词组。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Instruction requiring literal preservation of the quoted legal phrase 'due process'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 65. zhtw-project-llm-formal-reasoning-guard-v1/llm-048

Changed: `script, domain, risk`

Input:

```text
请维持命令 zhtw validate --strict 的参数顺序。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: CLI command parameter constraint testing command line flag and argument terminology.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 66. zhtw-project-llm-formal-reasoning-guard-v1/llm-049

Changed: `risk`

Input:

```text
回答需要说明哪些结论是根据现有资料推得。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Standard reasoning instruction testing baseline character conversion without specific term traps.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`
