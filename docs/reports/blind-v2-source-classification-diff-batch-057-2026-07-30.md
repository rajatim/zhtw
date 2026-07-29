<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 057 (2026-07-30)

Status: advisory only; maintainer decisions pending

Packet SHA-256: `83dd2efc0282a265405539e17b5eb17aae66ee12333acb3f9584ce99c76b6c76`
Cases: 96
Exact Codex/Gemini classifications: 31
Maintainer review queue: 65

Field differences:

- Eligibility: 2
- Script: 0
- Domain: 33
- Risk: 45

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

Neither advisory is auto-preferred. Codex must synthesize the differences before maintainer confirmation; no classification in this report has been written into the candidate pool.

## Review Queue

### 01. aosp-framework-zh-rcn-v1/string-089947c163bb825b

Changed: `risk`

Input:

```text
离开此页
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A standard UI phrase requiring basic character conversion.

Maintainer decision: `pending`

### 02. aosp-framework-zh-rcn-v1/string-2d7bc10e6505533a

Changed: `risk`

Input:

```text
%d秒后重试。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A common UI string with a format placeholder; conversion is primarily character-based.

Maintainer decision: `pending`

### 03. aosp-framework-zh-rcn-v1/string-3e21526c95e0cfb8

Changed: `risk`

Input:

```text
正在移动%s
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A standard UI status message with a format placeholder, requiring simple character conversion.

Maintainer decision: `pending`

### 04. aosp-framework-zh-rcn-v1/string-46b593523dd1b6da

Changed: `risk`

Input:

```text
记住我的选择
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A standard UI option that should be a straightforward character conversion.

Maintainer decision: `pending`

### 05. aosp-framework-zh-rcn-v1/string-49cd270bfc87446f

Changed: `risk`

Input:

```text
取消置顶%1$s
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A UI action with a placeholder; the term '置顶' (pin) is common and requires direct character conversion.

Maintainer decision: `pending`

### 06. aosp-framework-zh-rcn-v1/string-58aa48860c4b51d9

Changed: `risk`

Input:

```text
%1$s目前正在运行。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A process status message where the verb '运行' (running) should be converted to '執行中' for Taiwan.

Maintainer decision: `pending`

### 07. aosp-framework-zh-rcn-v1/string-6bc65c54768ca77e

Changed: `risk`

Input:

```text
移动网络不可用，请插入有效的 SIM 卡并重新启动。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: System instruction where '移动网络' (mobile network) and '重新启动' (restart) should be converted to '行動網路' and '重新開機'.

Maintainer decision: `pending`

### 08. aosp-framework-zh-rcn-v1/string-80b3688924d60d00

Changed: `risk`

Input:

```text
此应用未获得录音权限，但能通过此 USB 设备录制音频。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Conversion requires mapping common IT terms like '应用' (app) and '设备' (device) to Taiwan equivalents, while preserving 'USB'.

Maintainer decision: `pending`

### 09. aosp-framework-zh-rcn-v1/string-dad950876ef1ff5e

Changed: `domain`

Input:

```text
绑定到条件提供程序服务
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The technical term '提供程序' (provider) requires a specific phrase-level conversion.

Maintainer decision: `pending`

### 10. aosp-framework-zh-rcn-v1/string-e1e9c921697dedef

Changed: `risk`

Input:

```text
您尝试解锁 Android TV 设备失败的次数已达 %1$d 次。如果再尝试 %2$d 次后仍不成功，您的 Android TV 设备就会恢复出厂设置，而且所有用户数据都会丢失。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Requires converting multiple terms ('设备', '数据', '恢复出厂设置') while preserving the 'Android TV' entity and format specifiers.

Maintainer decision: `pending`

### 11. aosp-framework-zh-rcn-v1/string-eb538719c81de20d

Changed: `risk`

Input:

```text
已由您的管理员更新
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This is a straightforward UI message with direct character-level conversion.

Maintainer decision: `pending`

### 12. aosp-framework-zh-rcn-v1/string-edb6c5ccfe2fcbdb

Changed: `domain`

Input:

```text
允许该应用使用“location”类型的前台服务
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The type identifier 'location' must be preserved, while other terms like '应用' and '前台服务' need conversion.

Maintainer decision: `pending`

### 13. ready-gov-are-you-ready-guide-simplified-v1/sentence-018

Changed: `domain, risk`

Input:

```text
制定通讯计划，为撤离和避难做好准备。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This sentence requires checking the standard Taiwanese term for 'communication plan'.

Maintainer decision: `pending`

### 14. ready-gov-are-you-ready-guide-simplified-v1/sentence-023

Changed: `risk`

Input:

```text
重要的是要购买所需保险，并了解保险的承保范围。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This tests insurance-related terminology which can differ between regions.

Maintainer decision: `pending`

### 15. ready-gov-are-you-ready-guide-simplified-v1/sentence-074

Changed: `risk`

Input:

```text
知道执法人员的首要任务是结束事件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Tests terminology for law enforcement, which is a key phrase-level conversion.

Maintainer decision: `pending`

### 16. ready-gov-are-you-ready-guide-simplified-v1/sentence-080

Changed: `domain`

Input:

```text
注意危险性增加的迹象，包括最近的雪崩和斜坡上的裂缝。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A good baseline case for simple character conversion of common warning terms.

Maintainer decision: `pending`

### 17. ready-gov-are-you-ready-guide-simplified-v1/sentence-086

Changed: `domain, risk`

Input:

```text
网络袭击 • 保持软件和操作系统更新。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This sentence tests common IT terminology like 'cyber attack' and 'operating system'.

Maintainer decision: `pending`

### 18. ready-gov-are-you-ready-guide-simplified-v1/sentence-094

Changed: `eligible, domain, risk`

Input:

```text
定期更改管理以及无线网络（Wi-Fi）的密码以保护您的家庭网络。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | unsafe_source_translation |
| Gemini | yes | it_api_cli | over_conversion_guard | high | awkward_phrasing |

Codex reason: The phrase 更改管理以及无线网络的密码 has a missing modifier and unreliable source meaning.

Gemini reason: Tests protection of the 'Wi-Fi' token and requires careful handling of the slightly ambiguous 'management password' phrase.

Maintainer decision: `pending`

### 19. ready-gov-are-you-ready-guide-simplified-v1/sentence-109

Changed: `eligible, domain, risk`

Input:

```text
遮住嘴巴以保护自己，同时不要大喊大叫，而是用口哨。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | unsafe_source_translation |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: The instruction ends with 而是用口哨 and omits the action needed to preserve its safety meaning.

Gemini reason: A simple, everyday sentence that serves as a good baseline conversion test.

Maintainer decision: `pending`

### 20. ready-gov-are-you-ready-guide-simplified-v1/sentence-110

Changed: `risk`

Input:

```text
如果您处在容易发生海啸的区域，请在摇晃停止后立即前往内陆或更高的地面。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Tests disaster-related terminology and common phrases for location and direction.

Maintainer decision: `pending`

### 21. ready-gov-are-you-ready-guide-simplified-v1/sentence-156

Changed: `domain`

Input:

```text
请注意，屋内可能有蛇和其他动物。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: An extremely simple sentence for a baseline check of common nouns.

Maintainer decision: `pending`

### 22. ready-gov-are-you-ready-guide-simplified-v1/sentence-167

Changed: `domain, risk`

Input:

```text
在管道中安装止回阀以防止倒灌。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This tests specialized technical terminology for plumbing ('check valve', 'backflow').

Maintainer decision: `pending`

### 23. ready-gov-are-you-ready-guide-simplified-v1/sentence-176

Changed: `risk`

Input:

```text
避免在有山体滑坡危险的区域中建房，例如陡峭的斜坡或靠近悬崖，或靠近排水道或溪流的地方。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Tests specific terminology for natural disasters ('landslide') which often varies.

Maintainer decision: `pending`

### 24. ready-gov-are-you-ready-guide-simplified-v1/sentence-177

Changed: `risk`

Input:

```text
种植地面覆盖物并建造墙壁，以引导泥石流绕过建筑物。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Good test for a specific disaster term ('mudflow') that has a common regional variant.

Maintainer decision: `pending`

### 25. ready-gov-are-you-ready-guide-simplified-v1/sentence-201

Changed: `domain, risk`

Input:

```text
在核事件发生后，这些设备将继续发挥作用，而移动电话、短信、电视和互联网服务则可能无法使用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Excellent case for multiple common technology terms that differ in Taiwan ('mobile phone', 'text message', 'internet').

Maintainer decision: `pending`

### 26. ready-gov-are-you-ready-guide-simplified-v1/sentence-220

Changed: `domain`

Input:

```text
停电期间，仅可使用手电筒照明。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A straightforward case testing common terms for a household emergency.

Maintainer decision: `pending`

### 27. ready-gov-are-you-ready-guide-simplified-v1/sentence-262

Changed: `risk`

Input:

```text
注册本地的海啸警报系统，并遵照所提供的指导操作。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This emergency instruction may require phrase-level adaptation for Taiwan, e.g., 'guidance' and 'system'.

Maintainer decision: `pending`

### 28. ready-gov-are-you-ready-guide-simplified-v1/sentence-278

Changed: `risk`

Input:

```text
戴上护目镜和眼镜（而不是隐形眼镜）以及长袖衫裤，以减少与灰烬接触。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Phrase choices for protective gear and clothing might differ in Taiwan.

Maintainer decision: `pending`

### 29. ready-gov-are-you-ready-guide-simplified-v1/sentence-288

Changed: `risk`

Input:

```text
寻找带软管的户外水源，可以连接到房屋任何地方。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The terms for 'hose' and the phrasing for 'connect anywhere' may require idiomatic changes.

Maintainer decision: `pending`

### 30. ready-gov-are-you-ready-guide-simplified-v1/sentence-297

Changed: `risk`

Input:

```text
在应急物资包中增加保暖衣物和毯子。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The term for 'emergency supply kit' likely differs and requires a candidate lookup.

Maintainer decision: `pending`

### 31. ready-gov-are-you-ready-guide-simplified-v1/sentence-348

Changed: `domain, risk`

Input:

```text
带上宠物，但请注意，公共庇护所只允许携带服务性动物。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Terms like 'shelter' and 'service animal' may have different standard translations in Taiwan.

Maintainer decision: `pending`

### 32. ready-gov-are-you-ready-guide-simplified-v1/sentence-361

Changed: `risk`

Input:

```text
在您的工具包中准备几个并试戴每个口罩以确保密闭性。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | potential_source_mistranslation |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The term 'toolkit' is likely a source mistranslation for 'emergency kit', and 'tight seal' may be phrased differently.

Maintainer decision: `pending`

### 33. ready-gov-are-you-ready-guide-simplified-v1/sentence-375

Changed: `domain, risk`

Input:

```text
考虑其他的因素，例如年龄、饮食、健康、移动能力和当地气候。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The term for 'mobility' might differ, requiring a vocabulary check.

Maintainer decision: `pending`

### 34. ready-gov-are-you-ready-guide-simplified-v1/sentence-376

Changed: `risk`

Input:

```text
由于您不知道发生紧急情况时您会在哪里，因此请在家里、工作场所和车辆上准备好物资用品。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The term for 'supplies' is a bit verbose and may be simplified in Taiwan.

Maintainer decision: `pending`

### 35. ready-gov-are-you-ready-guide-simplified-v1/sentence-403

Changed: `domain, risk`

Input:

```text
一旦注册后，所在地区的官员就可以向您发送有关当地紧急情况的短信或电子邮件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains '短信' which should be '簡訊' for Taiwan, a classic vocabulary difference.

Maintainer decision: `pending`

### 36. ready-gov-are-you-ready-guide-simplified-v1/sentence-439

Changed: `domain, risk`

Input:

```text
即使您不在高风险地区，以防万一发生洪水，购买保险也是一个好主意。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | medium | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: The phrasing '以防万一' and '好主意' might be expressed differently in idiomatic Taiwan Mandarin.

Maintainer decision: `pending`

### 37. ready-gov-are-you-ready-guide-simplified-v1/sentence-460

Changed: `risk`

Input:

```text
居住在现有房屋中的人们也可以采取措施以减轻灾难的影响，例如升级门窗和车库门等措施，以达到抵御强风或风载碎屑冲击的标准。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains technical terms like 'wind-borne debris' which require specialized vocabulary lookup for Taiwan.

Maintainer decision: `pending`

### 38. ready-gov-are-you-ready-guide-simplified-v1/sentence-543

Changed: `risk`

Input:

```text
如果发生重大索赔事件，由于提交的索赔数量众多，处理索赔和付款时间可能会比正常情况更长。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This sentence uses insurance-specific jargon like 'claims event' which may have a different standard term in Taiwan.

Maintainer decision: `pending`

### 39. zhtw-project-llm-formal-reasoning-guard-v1/formal-001

Changed: `risk`

Input:

```text
委员会完成调查后，将公开报告与附件目录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Standard formal sentence where basic character conversion should be sufficient.

Maintainer decision: `pending`

### 40. zhtw-project-llm-formal-reasoning-guard-v1/formal-006

Changed: `risk`

Input:

```text
地方政府说明预算执行结果符合核定范围。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Standard governmental sentence with vocabulary common to both regions.

Maintainer decision: `pending`

### 41. zhtw-project-llm-formal-reasoning-guard-v1/formal-007

Changed: `domain`

Input:

```text
法院通知当事人补正送达地址。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | candidate_gap | medium | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Legal terminology like '补正' and '送达' requires careful validation for Taiwan's legal context.

Maintainer decision: `pending`

### 42. zhtw-project-llm-formal-reasoning-guard-v1/formal-009

Changed: `risk`

Input:

```text
新闻稿引用的统计资料截至今年六月底。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Standard press release sentence where direct character conversion should be adequate.

Maintainer decision: `pending`

### 43. zhtw-project-llm-formal-reasoning-guard-v1/formal-017

Changed: `risk`

Input:

```text
该项措施仅适用于公告指定的地区。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A standard formal sentence with vocabulary common across both regions.

Maintainer decision: `pending`

### 44. zhtw-project-llm-formal-reasoning-guard-v1/formal-020

Changed: `risk`

Input:

```text
审议结果须经核定后才能对外发布。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Formal procedural sentence with vocabulary that should convert directly.

Maintainer decision: `pending`

### 45. zhtw-project-llm-formal-reasoning-guard-v1/formal-023

Changed: `domain`

Input:

```text
公报引用法规编号 Law No. 108-17。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains a legal identifier 'Law No. 108-17' that must be protected from conversion.

Maintainer decision: `pending`

### 46. zhtw-project-llm-formal-reasoning-guard-v1/formal-024

Changed: `domain`

Input:

```text
调查表保留案件代码 CASE-7B-204。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Includes a technical identifier 'CASE-7B-204' that must be preserved.

Maintainer decision: `pending`

### 47. zhtw-project-llm-formal-reasoning-guard-v1/formal-025

Changed: `domain`

Input:

```text
审计报告沿用科目代码 4010-A。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains an accounting code '4010-A' which is an identifier to be preserved.

Maintainer decision: `pending`

### 48. zhtw-project-llm-formal-reasoning-guard-v1/formal-030

Changed: `domain`

Input:

```text
运输文件以 UN 3481 标示锂电池类别。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Includes the international standard identifier 'UN 3481' which must be protected.

Maintainer decision: `pending`

### 49. zhtw-project-llm-formal-reasoning-guard-v1/formal-037

Changed: `risk`

Input:

```text
公文应使用核定日期，不得改用收件日期。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A formal instruction with standard vocabulary suitable for direct conversion.

Maintainer decision: `pending`

### 50. zhtw-project-llm-formal-reasoning-guard-v1/formal-040

Changed: `domain, risk`

Input:

```text
公告载明不得以定型化契约条款排除责任。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Legal sentence containing the term '定型化契约' which has a direct and correct equivalent in Taiwan law.

Maintainer decision: `pending`

### 51. zhtw-project-llm-formal-reasoning-guard-v1/formal-043

Changed: `risk`

Input:

```text
核定金额不包含另行支付的行政费用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Standard financial/administrative sentence with vocabulary common to both locales.

Maintainer decision: `pending`

### 52. zhtw-project-llm-formal-reasoning-guard-v1/formal-049

Changed: `risk`

Input:

```text
报告附注说明计算方式与四舍五入规则。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Straightforward formal sentence with common financial/mathematical terms.

Maintainer decision: `pending`

### 53. zhtw-project-llm-formal-reasoning-guard-v1/llm-004

Changed: `domain`

Input:

```text
系统提示要求保留原始文件名与扩展名。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Standard IT instruction, requires mapping technical terms like '文件名' (filename) and '扩展名' (extension) to Taiwan equivalents.

Maintainer decision: `pending`

### 54. zhtw-project-llm-formal-reasoning-guard-v1/llm-005

Changed: `domain`

Input:

```text
请把会议摘要改写成适合传到群组的简短消息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A common instruction for summarizing and sharing information in a chat '群组' (group).

Maintainer decision: `pending`

### 55. zhtw-project-llm-formal-reasoning-guard-v1/llm-013

Changed: `domain, risk`

Input:

```text
使用者要求删除记录时，助理应先确认影响范围。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Clear instruction in a software context, using standard terms like '使用者' (user) and '删除记录' (delete record).

Maintainer decision: `pending`

### 56. zhtw-project-llm-formal-reasoning-guard-v1/llm-014

Changed: `domain, risk`

Input:

```text
请从附件中找出核定名称、联络窗口和生效日期。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Formal instruction to extract specific business information; '联络窗口' (contact window) is common.

Maintainer decision: `pending`

### 57. zhtw-project-llm-formal-reasoning-guard-v1/llm-017

Changed: `domain`

Input:

```text
请用条列方式说明资料检核失败的原因。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Instruction for formatting an error report, testing UI term '资料检核' (data validation).

Maintainer decision: `pending`

### 58. zhtw-project-llm-formal-reasoning-guard-v1/llm-020

Changed: `risk`

Input:

```text
回答前先检查问题是否缺少时间范围或适用对象。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A clear instruction for an LLM to check for missing context before answering.

Maintainer decision: `pending`

### 59. zhtw-project-llm-formal-reasoning-guard-v1/llm-021

Changed: `domain`

Input:

```text
API 回传的 request_id 必须原样保留。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Tests the ability to preserve technical identifiers like 'request_id' and acronyms like 'API'.

Maintainer decision: `pending`

### 60. zhtw-project-llm-formal-reasoning-guard-v1/llm-022

Changed: `domain`

Input:

```text
请勿改写 JSON 字段 user_profile_id。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Tests preserving technical identifiers ('user_profile_id'), acronyms ('JSON'), and mapping terms ('字段' to '欄位').

Maintainer decision: `pending`

### 61. zhtw-project-llm-formal-reasoning-guard-v1/llm-028

Changed: `domain`

Input:

```text
请保留 SQL 条件 WHERE active = true 的大小写。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Tests preservation of a code snippet's case and keywords ('WHERE active = true').

Maintainer decision: `pending`

### 62. zhtw-project-llm-formal-reasoning-guard-v1/llm-029

Changed: `domain`

Input:

```text
回答中的 ISO 8601 时间 2026-07-30T09:15:00+08:00 必须完整。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_code |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Tests the preservation of a standardized ISO 8601 timestamp format.

Maintainer decision: `pending`

### 63. zhtw-project-llm-formal-reasoning-guard-v1/llm-032

Changed: `domain`

Input:

```text
请将远程地址与本机地址分别列出。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Tests common networking terms ('远程地址', '本机地址') that have different idiomatic translations (e.g., '位址').

Maintainer decision: `pending`

### 64. zhtw-project-llm-formal-reasoning-guard-v1/llm-033

Changed: `domain`

Input:

```text
回答应使用相依性锁定文件中记录的实际版本。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Technical sentence about '相依性锁定文件' (dependency lock file), testing specific developer vocabulary.

Maintainer decision: `pending`

### 65. zhtw-project-llm-formal-reasoning-guard-v1/llm-035

Changed: `domain`

Input:

```text
模型必须区分预留位置、占位符和空白状态。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Good case for testing nuanced UI/UX terminology ('预留位置', '占位符', '空白状态') with potential ambiguity.

Maintainer decision: `pending`
