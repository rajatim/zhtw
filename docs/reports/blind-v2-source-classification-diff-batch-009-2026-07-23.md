<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 009 (2026-07-23)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `451e06b19c60778f2f8adcb71a1fbb2bfeb22c106043b6a0c954b5d484365a8a`
Cases: 100
Exact Codex/Gemini classifications: 68
Maintainer review queue: 32

Field differences:

- Eligibility: 8
- Script: 0
- Domain: 14
- Risk: 28

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

The maintainer resolved all 32 advisory disagreements and batch-confirmed the 68 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. ready-gov-earthquakes-zh-hans-v1/sentence-005

Changed: `eligible, domain, risk`

Input:

```text
制定应急计划：制定一个有州外联系人的家庭应急通信计划。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | no | null | null | high | headline_mixed_with_body |

Codex reason: 完整且可獨立裁決的防災或人身安全資訊，含臺灣用語差異候選。

Gemini reason: 標題與內文黏合（制定应急计划：），不符合單一完整句的標準。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 02. ready-gov-earthquakes-zh-hans-v1/sentence-009

Changed: `eligible, domain, risk`

Input:

```text
切记：并非每个人都能负担得起储备应对需要的必需品。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | no | null | null | high | headline_mixed_with_body |

Codex reason: 完整且可獨立裁決的防災資訊，主要驗證保守字形轉換。

Gemini reason: 句首 '切记：' 屬於指令或標題，與正文混合。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 03. ready-gov-earthquakes-zh-hans-v1/sentence-011

Changed: `eligible, domain, risk`

Input:

```text
保护住房：固定好家中的重物，如书柜、冰箱、热水器、电视和墙上挂的物品。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | no | null | null | high | headline_mixed_with_body |

Codex reason: 完整且可獨立裁決的防災或人身安全資訊，含臺灣用語差異候選。

Gemini reason: 標題與內文黏合（保护住房：），不符合單一完整句的標準。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 04. ready-gov-earthquakes-zh-hans-v1/sentence-024

Changed: `risk`

Input:

```text
如果附近有坚固的桌子或书桌，爬到下面用作庇护所。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的防災資訊，主要驗證保守字形轉換。

Gemini reason: '书桌' 在台灣多稱 '書桌'，但 '庇护所' 用法較正式，日常可能用 '掩護'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 05. ready-gov-earthquakes-zh-hans-v1/sentence-029

Changed: `eligible, domain, risk`

Input:

```text
如果坐着且无法爬到在地，向前弯腰，用双手盖住头部和颈部。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_source_text |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 句內「爬到在地」語法殘缺，來源文字本身無法可靠裁決。

Gemini reason: 緊急指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 06. ready-gov-earthquakes-zh-hans-v1/sentence-032

Changed: `risk`

Input:

```text
如果感到余震，准备好爬下、盖住和扶好。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的防災或人身安全資訊，含臺灣用語差異候選。

Gemini reason: 緊急指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 07. ready-gov-earthquakes-zh-hans-v1/sentence-044

Changed: `risk`

Input:

```text
穿好防护服，包括长袖衬衫，长裤，工作手套和坚固的厚底鞋。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的防災或人身安全資訊，含臺灣用語差異候選。

Gemini reason: '衬衫' (襯衫), '长裤' (長褲), '手套' (手套), '厚底鞋' (厚底鞋)。皆為基礎轉換測試。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 08. ready-gov-floods-zh-hans-v1/sentence-001

Changed: `domain`

Input:

```text
洪水就是大水暂时溢出到通常干燥的土地上，是美国最常见的自然灾害。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的防災或人身安全資訊，含臺灣用語差異候選。

Gemini reason: '大水' 在台灣口語常用，但書面語可能用 '洪水'。'自然灾害' (天然災害) 是基礎轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 09. ready-gov-floods-zh-hans-v1/sentence-005

Changed: `risk`

Input:

```text
山洪暴发可能毫无征兆。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的防災資訊，主要驗證保守字形轉換。

Gemini reason: '山洪暴发' 較書面，台灣可能用 '山洪爆發' 或更口語的 '溪水暴漲'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 10. ready-gov-floods-zh-hans-v1/sentence-008

Changed: `risk`

Input:

```text
切勿步行、游泳或驾车穿越洪水。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立裁決的防災資訊，主要驗證保守字形轉換。

Gemini reason: '驾车' 在台灣通常說 '開車'。'驾' 若單獨轉換可能出錯。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 11. ready-gov-floods-zh-hans-v1/sentence-010

Changed: `eligible, domain, risk`

Input:

```text
切记：只需 6 英寸的流水就能击倒人，而 1 英尺流水就能将车辆冲走。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | no | null | null | high | headline_mixed_with_body |

Codex reason: 完整且可獨立裁決的防災或人身安全資訊，含臺灣用語差異候選。

Gemini reason: 句首 '切记：' 屬於指令或標題，與正文混合。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 12. ready-gov-floods-zh-hans-v1/sentence-013

Changed: `risk`

Input:

```text
去到更高的地面或更高的楼层。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的防災或人身安全資訊，含臺灣用語差異候選。

Gemini reason: 緊急指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 13. ready-gov-floods-zh-hans-v1/sentence-014

Changed: `risk`

Input:

```text
访问 FEMA 洪水地图服务中心，了解所在地区的洪水风险类型。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整防災資訊；FEMA、NFIP 或機構專名需保留，適合作為過度轉換防護案例。

Gemini reason: 包含組織名稱 'FEMA' 和服務名稱 '洪水地图服务中心'，後者需要確認台灣有無對應官方翻譯。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 14. ready-gov-floods-zh-hans-v1/sentence-019

Changed: `risk`

Input:

```text
保单生效通常需要长达 30 天的时间，因此购买时间应在灾害发生之前。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的防災或人身安全資訊，含臺灣用語差異候選。

Gemini reason: '保单' (保單), '生效' (生效), '灾害' (災害)。基礎轉換測試。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 15. ready-gov-floods-zh-hans-v1/sentence-020

Changed: `risk`

Input:

```text
从国家洪水保险计划 (NFIP) 购买洪水保险。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整防災資訊；FEMA、NFIP 或機構專名需保留，適合作為過度轉換防護案例。

Gemini reason: 專有名稱 '国家洪水保险计划 (NFIP)' 需要確認台灣有無對應官方翻譯或通用名稱。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 16. ready-gov-floods-zh-hans-v1/sentence-021

Changed: `risk`

Input:

```text
制定一个计划供家庭（包括宠物）使用，以便您和您的家人知道该做什么、去哪里及您需要什么来保护自己免受洪水侵害。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的防災或人身安全資訊，含臺灣用語差異候選。

Gemini reason: 標準防災計劃建議。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 17. ready-gov-floods-zh-hans-v1/sentence-025

Changed: `domain`

Input:

```text
创建密码保护的数字副本。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的防災或人身安全資訊，含臺灣用語差異候選。

Gemini reason: '密码保护' 在台灣常用 '密碼保護'。'数字副本' (數位副本)。雖然情境是防災，但這句涉及 IT 操作。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 18. ready-gov-floods-zh-hans-v1/sentence-031

Changed: `eligible, domain, risk`

Input:

```text
当地的响应者用来将交通安全地引出洪水区。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 句子缺少主詞、指涉或必要前文，無法獨立裁決。

Gemini reason: '当地的响应者' 在台灣可能指 '當地應變人員' 或 '第一線反應人員'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 19. ready-gov-floods-zh-hans-v1/sentence-042

Changed: `risk`

Input:

```text
只有在当局说安全时才能回家。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的防災資訊，主要驗證保守字形轉換。

Gemini reason: '当局' 在台灣通常指 '當局' 或 '有關單位'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 20. ready-gov-floods-zh-hans-v1/sentence-043

Changed: `risk`

Input:

```text
除非有紧急情况，否则要避免开车。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立裁決的防災資訊，主要驗證保守字形轉換。

Gemini reason: '开车' 在台灣用 '開車'，'驾车' 轉換需正確。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 21. ready-gov-floods-zh-hans-v1/sentence-047

Changed: `risk`

Input:

```text
请注意，蛇和其他动物可能在您的房屋中。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的防災或人身安全資訊，含臺灣用語差異候選。

Gemini reason: 標準警告句。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 22. ready-gov-hurricanes-zh-hans-v1/sentence-004

Changed: `domain, risk`

Input:

```text
在西北太平洋部分地区，飓风被称为台风。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立裁決的防災或人身安全資訊，含臺灣用語差異候選。

Gemini reason: 專有名詞解釋，'台风' (颱風) 在此情境下不應被反向轉換。測試 identity mapping 的重要案例。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 23. ready-gov-hurricanes-zh-hans-v1/sentence-005

Changed: `eligible, domain, risk`

Input:

```text
东太平洋飓风季：5月15日至11月30日。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | no | null | null | high | headline_mixed_with_body |

Codex reason: 完整且可獨立裁決的防災資訊，主要驗證保守字形轉換。

Gemini reason: 標題與日期黏合。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 24. ready-gov-hurricanes-zh-hans-v1/sentence-010

Changed: `risk`

Input:

```text
制定应急计划确保家庭每个成员了解并掌握您的飓风应对计划。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的防災或人身安全資訊，含臺灣用語差異候選。

Gemini reason: 標準防災建議。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 25. ready-gov-hurricanes-zh-hans-v1/sentence-016

Changed: `eligible, domain, risk`

Input:

```text
他们将根据社区面临的威胁提供最新建议，发布安全措施。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 句子缺少主詞、指涉或必要前文，無法獨立裁決。

Gemini reason: '最新建议' (最新建議), '安全措施' (安全措施)。'发布' (發布/發佈)。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 26. ready-gov-hurricanes-zh-hans-v1/sentence-018

Changed: `domain, risk`

Input:

```text
请下载 FEMA 应用程序，您可以最多就全国五个区域，接收来自国家气象局的实时天气和紧急警报。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整防災資訊；FEMA、NFIP 或機構專名需保留，適合作為過度轉換防護案例。

Gemini reason: 包含 'FEMA 应用程序' (FEMA App/應用程式), '下载' (下載), '国家气象局' (國家氣象局), '实时天气' (即時天氣), '紧急警报' (緊急警報)。IT術語與專有名詞混合。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 27. ready-gov-hurricanes-zh-hans-v1/sentence-021

Changed: `domain`

Input:

```text
制作副本并将其保存在安全、受密码保护的数字空间内。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的防災或人身安全資訊，含臺灣用語差異候選。

Gemini reason: '受密码保护的数字空间' (受密碼保護的數位空間)。IT 安全術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 28. ready-gov-hurricanes-zh-hans-v1/sentence-035

Changed: `risk`

Input:

```text
不要在洪水中行走、游泳或开车。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立裁決的防災資訊，主要驗證保守字形轉換。

Gemini reason: '开车' 在台灣用 '開車'，'驾车' 轉換需正確。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 29. ready-gov-hurricanes-zh-hans-v1/sentence-036

Changed: `risk`

Input:

```text
仅六英寸的快速流动的水就可以将您击倒，一英尺的流动水可以冲走您的车辆。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的防災或人身安全資訊，含臺灣用語差異候選。

Gemini reason: 通用警告句，數字和單位的轉換是重點。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 30. ready-gov-hurricanes-zh-hans-v1/sentence-037

Changed: `risk`

Input:

```text
请关注当地官方发布的信息和特别指示。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的防災資訊，主要驗證保守字形轉換。

Gemini reason: '当地官方' (當地官方)。'发布' (發布/發佈)。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 31. ready-gov-hurricanes-zh-hans-v1/sentence-049

Changed: `risk`

Input:

```text
灾后电话系统通常会中断或占线。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的防災資訊，主要驗證保守字形轉換。

Gemini reason: '占线' 在台灣稱 '佔線'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 32. ready-gov-hurricanes-zh-hans-v1/sentence-053

Changed: `domain`

Input:

```text
部分资源可能仅提供英文版本。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的防災資訊，主要驗證保守字形轉換。

Gemini reason: 關於內容語言的說明，常見於網站 UI。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`
