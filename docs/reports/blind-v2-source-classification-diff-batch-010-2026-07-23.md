<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 010 (2026-07-23)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `c7ce213e6c8805c0a9e51431d663f5e8108b7067dc765a64c6f50e3f40981799`
Cases: 100
Exact Codex/Gemini classifications: 41
Maintainer review queue: 59

Field differences:

- Eligibility: 17
- Script: 0
- Domain: 20
- Risk: 59

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

The maintainer resolved all 59 advisory disagreements and batch-confirmed the 41 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. osha-chainsaw-safety-simplified-v1/sentence-001

Changed: `risk`

Input:

```text
操作链锯存在危险，使用适当的个人防护装备和遵守安全操作程序可以最大限度地减少潜在的伤害。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 標準鏈鋸安全操作說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 02. osha-chainsaw-safety-simplified-v1/sentence-005

Changed: `risk`

Input:

```text
在距离加油区至少 10 英尺（3米）的地方启动，并开启链锯制动器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 標準鏈鋸安全操作說明，包含英制單位。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 03. osha-chainsaw-safety-simplified-v1/sentence-006

Changed: `risk`

Input:

```text
使用经认可的容器给链锯加油。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 標準鏈鋸安全操作說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 04. osha-chainsaw-safety-simplified-v1/sentence-007

Changed: `risk`

Input:

```text
进行加油操作时，需要在距离所有火源至少 10 英尺（3米）的地方进行；加油时禁止吸烟。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 標準鏈鋸安全操作說明，包含英制單位。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 05. osha-chainsaw-safety-simplified-v1/sentence-010

Changed: `risk`

Input:

```text
清除链锯导板上的污垢、碎片、小树枝和石块。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 標準鏈鋸安全操作說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 06. osha-chainsaw-safety-simplified-v1/sentence-014

Changed: `risk`

Input:

```text
操作链锯时必须佩戴适当的个人防护装备，包括手、脚、腿、眼睛、面部、听力和头部的保护装置。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 標準鏈鋸安全操作說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 07. osha-chainsaw-safety-simplified-v1/sentence-019

Changed: `risk`

Input:

```text
为避免反冲，请勿使用端头进行切割。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 「反冲」的對應台灣用語可能不同。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 08. osha-disaster-cleanup-simplified-v1/sentence-005

Changed: `risk`

Input:

```text
如果您是参与清理和重建活动的雇主、工人、房主或市民，请务必在参与这些活动之前评估危险性和（或）遇到危险的可能性。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 災後清理的安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 09. osha-disaster-cleanup-simplified-v1/sentence-008

Changed: `eligible, domain, risk`

Input:

```text
被洪水淹没的工业和废弃矿场的有毒物质。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | heading_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 來源為缺少必要上下文的列表或名詞片段，無法獨立裁決。

Gemini reason: 災後清理的安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 10. osha-disaster-cleanup-simplified-v1/sentence-009

Changed: `eligible, domain, risk`

Input:

```text
空气中的霉菌和真菌。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | heading_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 來源為缺少必要上下文的列表或名詞片段，無法獨立裁決。

Gemini reason: 災後清理的安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 11. osha-disaster-cleanup-simplified-v1/sentence-010

Changed: `risk`

Input:

```text
对封闭空间用新鲜空气进行通风。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 災後清理的安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 12. osha-disaster-cleanup-simplified-v1/sentence-024

Changed: `eligible, domain, risk`

Input:

```text
树木的修剪与杂物清除与倒下的电力线相连接的电线或树枝有带电的危险，与之接触会导致触电。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | heading_text_join |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: PDF 標題與正文黏連，會把版面抽取錯誤帶入評測。

Gemini reason: 災後清理的安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 13. osha-disaster-cleanup-simplified-v1/sentence-026

Changed: `eligible, domain, risk`

Input:

```text
链锯和切割机等设备造成的伤害。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | heading_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 來源為缺少必要上下文的列表或名詞片段，無法獨立裁決。

Gemini reason: 災後清理的安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 14. osha-disaster-cleanup-simplified-v1/sentence-030

Changed: `risk`

Input:

```text
做出清晰的标记，以标示出树木残片可能落到工人身上的危险区域。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 災後清理的安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 15. osha-disaster-cleanup-simplified-v1/sentence-036

Changed: `eligible, domain, risk`

Input:

```text
如果不可行，请使用更多的工人和适当的举升方式。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 句子依賴未收錄的前文或指涉，無法獨立裁決。

Gemini reason: 災後清理的安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 16. osha-disaster-cleanup-simplified-v1/sentence-041

Changed: `risk`

Input:

```text
遵从适当的用梯安全（如：梯子架设在坚固稳定的地方，上下梯时保持“三点”接触，不要站在最上面的梯级上）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 災後清理的安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 17. osha-disaster-cleanup-simplified-v1/sentence-043

Changed: `eligible, domain, risk`

Input:

```text
便携发电机燃气或柴油发电机导致的电击和触电。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | heading_text_join |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: PDF 標題與正文黏連，會把版面抽取錯誤帶入評測。

Gemini reason: 災後清理的安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 18. osha-disaster-cleanup-simplified-v1/sentence-062

Changed: `eligible, domain, risk`

Input:

```text
相关的详细信息请参阅29 CFR 1910.146。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 句子依賴未收錄的前文或指涉，無法獨立裁決。

Gemini reason: 包含法規編號，不應翻譯。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 19. osha-disaster-cleanup-simplified-v1/sentence-075

Changed: `eligible, domain, risk`

Input:

```text
这些信息将根据要求提供给有视听障碍的人。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 句子依賴未收錄的前文或指涉，無法獨立裁決。

Gemini reason: 標準的無障礙服務說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 20. osha-disaster-falls-simplified-v1/sentence-001

Changed: `risk`

Input:

```text
应急救援人员在应对自然和人为灾难时，会面临因滑倒、绊倒和跌倒而受伤甚至死亡的风险。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 災難應變人員安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 21. osha-disaster-falls-simplified-v1/sentence-002

Changed: `domain, risk`

Input:

```text
雇主必须采取的、确保工人安全的步骤包括：制定事前灾难响应方案并确保应急救援人员了解该方案。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 災難應變人員安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 22. osha-disaster-falls-simplified-v1/sentence-004

Changed: `risk`

Input:

```text
提供防护装备以防止滑倒、绊倒和跌倒，它们包括：防滑鞋（例如橡胶鞋底）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 災難應變人員安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 23. osha-disaster-falls-simplified-v1/sentence-005

Changed: `eligible, domain, risk`

Input:

```text
手套，工人可以牢固地抓住栏杆 / 梯子以稳定自己。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_source_text |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 來源文字有明顯缺漏、重複或錯誤黏連，無法可靠裁決。

Gemini reason: 災難應變人員安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 24. osha-disaster-falls-simplified-v1/sentence-008

Changed: `risk`

Input:

```text
使用手电筒或头盔灯，以避开洞口或地板开口、潮湿或光滑的表面、以及碎片或设备。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 災難應變人員安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 25. osha-disaster-falls-simplified-v1/sentence-009

Changed: `risk`

Input:

```text
在目视检查以确保没有孔洞或薄弱处、并且可以支撑工人及其设备的重量之前，请勿踏上任何表面。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 災難應變人員安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 26. osha-disaster-falls-simplified-v1/sentence-011

Changed: `risk`

Input:

```text
使用背包和工具带以固定设备、解放双手。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 災難應變人員安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 27. osha-disaster-falls-simplified-v1/sentence-012

Changed: `risk`

Input:

```text
在高空未受保护的边缘附近移动或执行应急救援时，使用防坠落保护装置。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 災難應變人員安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 28. osha-disaster-falls-simplified-v1/sentence-013

Changed: `risk`

Input:

```text
将滑倒、绊倒和跌倒的危险用通讯设备——尤其是免提设备——通知雇主/救援主管和其他工人。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 災難應變人員安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 29. osha-electrical-safety-simplified-v1/sentence-004

Changed: `risk`

Input:

```text
切勿接触掉落的架空电线，通知电力公司该掉落的电线。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 標準電氣安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 30. osha-electrical-safety-simplified-v1/sentence-005

Changed: `risk`

Input:

```text
在清理和其他活动期间，与架空电线保持至少 10英尺（3米）的距离。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 標準電氣安全說明，包含英制單位。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 31. osha-electrical-safety-simplified-v1/sentence-006

Changed: `risk`

Input:

```text
如果您在高处工作或处理长物体，请在工作开始前核实该区域是否存在架空电线。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 標準電氣安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 32. osha-electrical-safety-simplified-v1/sentence-007

Changed: `risk`

Input:

```text
如果在您驾车时，架空电线掉落至您的车辆上，请留在车内并继续驶离电线；如果发动机熄火，请勿离开车辆。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 標準電氣安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 33. osha-electrical-safety-simplified-v1/sentence-011

Changed: `risk`

Input:

```text
除非有相关资质和授权，切勿修理插线板或电气设备。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 標準電氣安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 34. osha-electrical-safety-simplified-v1/sentence-012

Changed: `risk`

Input:

```text
在通电前，让有资质的电工检查曾经受潮的电气设备。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 標準電氣安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 35. osha-fallen-workers-family-simplified-v1/sentence-008

Changed: `domain, risk`

Input:

```text
分享/创建纪念物品或活动。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的正式行政或職場資訊。

Gemini reason: 處理哀傷的建議。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 36. osha-fallen-workers-family-simplified-v1/sentence-013

Changed: `risk`

Input:

```text
其他 7 个州计划（康涅狄格州、伊利诺伊州、缅因州、马萨诸塞州、新泽西州、纽约州和维尔京群岛）仅涵盖州和地方政府工作人员。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立裁決的正式行政或職場資訊。

Gemini reason: 包含多個美國州名，需注意專有名詞轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 37. osha-fallen-workers-family-simplified-v1/sentence-014

Changed: `eligible, domain, risk`

Input:

```text
须知和期望 OSHA 将对您亲人的事故进行调查，以确定是否违反了 OSHA 规定。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | heading_text_join |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: PDF 標題與正文黏連，會把版面抽取錯誤帶入評測。

Gemini reason: 包含組織名稱 OSHA。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 38. osha-fallen-workers-family-simplified-v1/sentence-020

Changed: `risk`

Input:

```text
检查结束后，地区主管将回答你的问题并解释处理方案。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的正式行政或職場資訊。

Gemini reason: 行政程序說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 39. osha-small-business-consultation-simplified-v1/sentence-002

Changed: `risk`

Input:

```text
工地的有效安全与健康项目会让您的工人更好地，更有效率地工作，提高生产率，并确保产品质量。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的正式行政或職場資訊。

Gemini reason: 關於企業安全與健康項目的說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 40. osha-small-business-consultation-simplified-v1/sentence-007

Changed: `risk`

Input:

```text
小型企业可能没有预算来雇佣一个安全专家，但是这个项目可以免费提供相似的建议。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的正式行政或職場資訊。

Gemini reason: 關於企業安全與健康項目的說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 41. osha-small-business-consultation-simplified-v1/sentence-008

Changed: `risk`

Input:

```text
即使您的企业还没有经历任何与工作相关的伤亡事件，但是评估工作环境的安全隐患是很重要的。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的正式行政或職場資訊。

Gemini reason: 關於企業安全與健康項目的說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 42. osha-small-business-consultation-simplified-v1/sentence-010

Changed: `eligible, domain, risk`

Input:

```text
告诉我们您的安全顾虑 — 咨询会帮您找出解决方案联系当地现场咨询办公室，预约一次咨询访问。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | heading_text_join |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: PDF 標題與正文黏連，會把版面抽取錯誤帶入評測。

Gemini reason: 關於企業安全與健康項目的說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 43. osha-small-business-consultation-simplified-v1/sentence-011

Changed: `risk`

Input:

```text
您的企业唯一义务是，在合理的时间内，纠正不安全，不健康的工作条件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的正式行政或職場資訊。

Gemini reason: 關於企業安全與健康項目的說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 44. osha-small-business-consultation-simplified-v1/sentence-013

Changed: `risk`

Input:

```text
雇主，工人代表，以及顾问，三者协同详谈该企业，并找出现有的和潜在的安全隐患。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的正式行政或職場資訊。

Gemini reason: 關於企業安全與健康項目的說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 45. osha-small-business-consultation-simplified-v1/sentence-015

Changed: `risk`

Input:

```text
在结束会议上，顾问会和您，以及工人代表，一起详细查看所找出的安全隐患。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的正式行政或職場資訊。

Gemini reason: 關於企業安全與健康項目的說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 46. osha-small-business-consultation-simplified-v1/sentence-017

Changed: `risk`

Input:

```text
顾问离开后，您会收到一份详细的纸质版咨询报告总结，确认所需纠正之处。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的正式行政或職場資訊。

Gemini reason: 關於企業安全與健康項目的說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 47. osha-small-business-consultation-simplified-v1/sentence-018

Changed: `risk`

Input:

```text
若一个情况被定义为“严重”的安全隐患，顾问会帮您开展一个计划，在合理的时间框架内，纠正安全隐患，并同时保护您的工人。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的正式行政或職場資訊。

Gemini reason: 關於企業安全與健康項目的說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 48. osha-small-business-consultation-simplified-v1/sentence-021

Changed: `risk`

Input:

```text
顾问会帮您找出您企业中的安全与健康需求，并预约一个对您方便的日期。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的正式行政或職場資訊。

Gemini reason: 關於企業安全與健康項目的說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 49. osha-work-zone-traffic-simplified-v1/sentence-001

Changed: `risk`

Input:

```text
工人在作业区的死亡或受伤，很多是由车辆或其他移动装置的撞击所导致。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 作業區交通安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 50. osha-work-zone-traffic-simplified-v1/sentence-002

Changed: `eligible, domain, risk`

Input:

```text
作业区的交通需要通过标识、锥筒、筒和分隔物来划分、控制。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_source_text |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 來源文字有明顯缺漏、重複或錯誤黏連，無法可靠裁決。

Gemini reason: 作業區交通安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 51. osha-work-zone-traffic-simplified-v1/sentence-004

Changed: `domain, risk`

Input:

```text
建设或拆迁工地内的交通控制方案由施工项目经理确定。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 作業區交通安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 52. osha-work-zone-traffic-simplified-v1/sentence-005

Changed: `risk`

Input:

```text
司机按照交通控制设备、信号灯和标示牌所指示的路线，在远离作业区的地方行驶。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 作業區交通安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 53. osha-work-zone-traffic-simplified-v1/sentence-007

Changed: `eligible, domain, risk`

Input:

```text
作业区防护：各种混凝土、水马、沙袋、可折叠标识物、防撞垫和卡车减震器可以用来限制司机未经授权进入施工区域。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | no | null | null | high | heading_text_join |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 包含「作业区防护：」標題。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 54. osha-work-zone-traffic-simplified-v1/sentence-008

Changed: `eligible, domain, risk`

Input:

```text
信号：信号旗手应穿着具有荧光背景并由反光材料制成的高可见度的工作服，这使其在任何方向至少1000英尺（300米）的范围内都可被看见。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | no | null | null | high | heading_text_join |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 包含「信号：」標題。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 55. osha-work-zone-traffic-simplified-v1/sentence-011

Changed: `risk`

Input:

```text
信号旗手应使用“停止/减速”棒、带灯的信号棒，或（仅在紧急情况下）信号旗。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 作業區交通安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 56. osha-work-zone-traffic-simplified-v1/sentence-012

Changed: `eligible, domain, risk`

Input:

```text
照明：信号站应有良好的照明。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | no | null | null | high | heading_text_join |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 包含「照明：」標題。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 57. osha-work-zone-traffic-simplified-v1/sentence-014

Changed: `risk`

Input:

```text
在现有照明不足的情况下，应使用频闪灯或燃烧棒；使用时应控制或消除眩光。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 作業區交通安全說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 58. osha-work-zone-traffic-simplified-v1/sentence-015

Changed: `eligible, domain, risk`

Input:

```text
培训：信号旗手必须经过培训并经认证，且使用经授权的信号装置。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | no | null | null | high | heading_text_join |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 包含「培训：」標題。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 59. osha-work-zone-traffic-simplified-v1/sentence-016

Changed: `eligible, domain, risk`

Input:

```text
行驶：应按照制造商的建议在设备和车辆上使用安全带和翻车保护装置。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | no | null | null | high | heading_text_join |

Codex reason: 完整且可獨立裁決的職業安全資訊，屬高風險內容。

Gemini reason: 包含「行驶：」標題。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`
