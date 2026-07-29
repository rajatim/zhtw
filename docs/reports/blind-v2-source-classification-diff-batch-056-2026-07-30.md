<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 056 (2026-07-30)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `1b162b7c3feb4e65d94d8191bc35941ff987291229fe71911de9efdb3ed39a1c`
Cases: 96
Exact Codex/Gemini classifications: 63
Maintainer review queue: 33

Field differences:

- Eligibility: 4
- Script: 2
- Domain: 13
- Risk: 27

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

The maintainer resolved all 33 advisory disagreements and batch-confirmed the 63 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. aosp-framework-zh-rcn-v1/string-20608a27fbf8d63a

Changed: `risk`

Input:

```text
进行身份验证时出错
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Standard error message where basic character conversion is likely sufficient.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 02. aosp-framework-zh-rcn-v1/string-21b184866f2a2a39

Changed: `risk`

Input:

```text
系统无法再识别%s。请重新设置指纹解锁功能。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | placeholder_present |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Error message combining a required vocabulary change ('设置' to '設定') and a placeholder.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 03. aosp-framework-zh-rcn-v1/string-2fc2e324dcc2854b

Changed: `risk`

Input:

```text
允许应用与近距离无线通信(NFC)标签、卡和读取器通信。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Permission description with multiple technical nouns that require vocabulary conversion for Taiwan (app, tag, reader).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 04. aosp-framework-zh-rcn-v1/string-8d7036f1bd59d407

Changed: `domain`

Input:

```text
RUIM Hrpd 解锁请求失败。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_acronym |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Technical error message with acronyms 'RUIM' and 'Hrpd' that must not be converted.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 05. aosp-framework-zh-rcn-v1/string-bcafcdb814610714

Changed: `risk`

Input:

```text
已启用服务。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A simple status message where direct character conversion is likely sufficient.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 06. aosp-framework-zh-rcn-v1/string-d7eb0b671e580367

Changed: `risk`

Input:

```text
修改您的照片收藏
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Straightforward permission string where 'photo' and 'collection' have high overlap.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 07. aosp-framework-zh-rcn-v1/string-e4191448243a7e37

Changed: `domain`

Input:

```text
正在请求 RUIM 服务提供商解锁…
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | has_acronym |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Technical status message with an acronym and several terms ('service provider', 'unlock') needing conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 08. ready-gov-are-you-ready-guide-simplified-v1/sentence-031

Changed: `risk`

Input:

```text
备灾的关键第一步是了解社区中普遍存在的危害类型。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This sentence contains common disaster preparedness terminology suitable for baseline testing.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 09. ready-gov-are-you-ready-guide-simplified-v1/sentence-235

Changed: `eligible, domain, risk`

Input:

```text
如果驾船或游泳，请立即上岸，并找到坚固的接地避难所或车辆。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | unsafe_source_translation |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: The phrase 坚固的接地避难所 is an unsafe and unclear source translation for lightning shelter guidance.

Gemini reason: The phrase '接地避难所' (grounded shelter) is specific and tests vocabulary for severe weather.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 10. ready-gov-are-you-ready-guide-simplified-v1/sentence-264

Changed: `risk`

Input:

```text
了解并练习社区疏散计划，规划出从家到工作场所的路线。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A standard instruction for evacuation planning, suitable for baseline conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 11. ready-gov-are-you-ready-guide-simplified-v1/sentence-287

Changed: `risk`

Input:

```text
施工前，务必检查并遵守当地的建筑法规。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This is a standard sentence regarding regulations that should convert directly.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 12. ready-gov-are-you-ready-guide-simplified-v1/sentence-345

Changed: `risk`

Input:

```text
与家人、朋友或当地的政府制定计划。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | awkward_source_translation |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A straightforward sentence about planning suitable for baseline conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 13. ready-gov-are-you-ready-guide-simplified-v1/sentence-347

Changed: `script`

Input:

```text
请注意收音机或智能手机 / 平板电脑，遵循当地的撤离指示。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Tests common device names ('智能手机', '平板电脑') and handling of punctuation like the slash separator.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 14. ready-gov-are-you-ready-guide-simplified-v1/sentence-351

Changed: `domain, risk`

Input:

```text
拔下收音机、电视和小家电的电气设备的插头。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | awkward_source_translation |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A standard instructional sentence with common appliance names.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 15. ready-gov-are-you-ready-guide-simplified-v1/sentence-355

Changed: `eligible, domain, risk`

Input:

```text
留下便条，告诉他人您何时离开以及要去 • 哪里。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_extraction |
| Gemini | yes | social_daily | baseline_guard | high | formatting_artifact |

Codex reason: A bullet marker splits the phrase 要去哪里, so the extracted sentence is malformed.

Gemini reason: A simple instructional sentence, but it contains a formatting artifact (bullet point).

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 16. ready-gov-are-you-ready-guide-simplified-v1/sentence-393

Changed: `eligible, domain, risk`

Input:

```text
财务和法律文件，例如银行对帐单和工资单。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: This is a document-list fragment without a standalone instruction or statement.

Gemini reason: This case involves financial terms where Taiwan-specific vocabulary might be preferred.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 17. ready-gov-are-you-ready-guide-simplified-v1/sentence-425

Changed: `risk`

Input:

```text
房屋保险的保单可能为房屋和个人财产承保不同危险。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Formal insurance sentence where direct character conversion is likely sufficient.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 18. ready-gov-are-you-ready-guide-simplified-v1/sentence-440

Changed: `risk`

Input:

```text
洪水保险的费用只是轻微洪水所造成的损失的一小部分。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A simple sentence about insurance costs with common, directly convertible terms.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 19. ready-gov-are-you-ready-guide-simplified-v1/sentence-474

Changed: `domain`

Input:

```text
联系当地的应急事务经理，了解附近的机会。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | awkward_source_translation |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: This sentence tests the localization of an official government title.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 20. ready-gov-are-you-ready-guide-simplified-v1/sentence-498

Changed: `eligible, domain, risk`

Input:

```text
健康和安全准则灾后，请务必遵循安全准则，注意身体健康。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fused_heading |
| Gemini | yes | social_daily | baseline_guard | high | awkward_phrasing |

Codex reason: The heading and body were fused without a sentence boundary, making the extraction unreliable.

Gemini reason: The sentence structure is slightly awkward, combining a title and an instruction.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 21. ready-gov-are-you-ready-guide-simplified-v1/sentence-508

Changed: `domain, risk`

Input:

```text
在进家之前用手电筒检查房屋。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A straightforward instruction with common objects.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 22. ready-gov-are-you-ready-guide-simplified-v1/sentence-511

Changed: `domain, risk`

Input:

```text
您不仅会了解建筑物是否安全，而且还会了解需要进行哪些维修。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | repetitive_phrasing |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Standard sentence structure, though the word '了解' is used repetitively.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 23. ready-gov-are-you-ready-guide-simplified-v1/sentence-529

Changed: `script`

Input:

```text
第第 1步1步第第 2步2步第第 3步3步提出保险索赔如果承保的危险损害了房屋，您应迅速采取行动，使索赔程序顺利进行。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | corrupted_extraction |
| Gemini | no | null | null | high | extraction_error, duplicate_text, missing_punctuation |

Codex reason: Repeated step labels and missing boundaries severely corrupt the extracted sentence.

Gemini reason: The sentence is malformed due to repetitive text artifacts and missing punctuation.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 24. zhtw-project-ui-social-baseline-guard-v1/social-005

Changed: `risk`

Input:

```text
这张优惠券只能在实体门市使用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains a key phrase '实体门市' which has a common regional equivalent in Taiwan.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 25. zhtw-project-ui-social-baseline-guard-v1/social-007

Changed: `risk`

Input:

```text
我晚一点会把照片上传到共享相簿。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A typical sentence about sharing photos online, testing common digital life vocabulary.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 26. zhtw-project-ui-social-baseline-guard-v1/social-015

Changed: `domain, risk`

Input:

```text
她正在帮家人办理手机号码过户。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: A formal sentence about transferring phone number ownership with regional-specific terminology.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 27. zhtw-project-ui-social-baseline-guard-v1/social-042

Changed: `domain`

Input:

```text
USB-C 充电线放在黑色收纳袋里。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Contains a technical identifier 'USB-C' that must be preserved.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 28. zhtw-project-ui-social-baseline-guard-v1/ui-006

Changed: `risk`

Input:

```text
单选按钮一次只能选择一个项目。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Standard UI string that requires basic character conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 29. zhtw-project-ui-social-baseline-guard-v1/ui-019

Changed: `risk`

Input:

```text
类别名称最多可以输入三十个字符。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Standard UI text that should convert correctly with character-level mapping.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 30. zhtw-project-ui-social-baseline-guard-v1/ui-024

Changed: `risk`

Input:

```text
筛选条件清除后，应恢复显示所有结果。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Basic UI instruction where direct character conversion is likely sufficient.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 31. zhtw-project-ui-social-baseline-guard-v1/ui-031

Changed: `risk`

Input:

```text
删除前会显示受影响资料的数量。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Straightforward UI sentence with shared terminology suitable for baseline conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 32. zhtw-project-ui-social-baseline-guard-v1/ui-040

Changed: `risk`

Input:

```text
验证码将在五分钟后失效。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Standard UI notification using shared terms that should convert correctly.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`

### 33. zhtw-project-ui-social-baseline-guard-v1/ui-049

Changed: `domain, risk`

Input:

```text
核定名称与申请资料不同时会显示警告。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Codex reviewed this input-only case for completeness, source quality, and Taiwan conversion relevance; no converter output or expected text was used.

Gemini reason: Formal language with shared terminology that should convert correctly.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-30`
