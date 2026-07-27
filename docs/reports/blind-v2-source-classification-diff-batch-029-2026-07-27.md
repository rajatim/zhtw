<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 029 (2026-07-27)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `8b2548e28d733aaf6cdf04da9f1392f1a201cd72815050542c3e88863a4874ad`
Cases: 70
Exact Codex/Gemini classifications: 18
Maintainer review queue: 52

Field differences:

- Eligibility: 5
- Script: 6
- Domain: 15
- Risk: 50

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

The maintainer resolved all 52 advisory disagreements and batch-confirmed the 18 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. census-newsroom-zh-hans-v1/page-01-sentence-015

Changed: `risk`

Input:

```text
由于州以下的各级数据和特征数据是重点，因此国会席位分配数据完成后能在第一时间开始分析。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | null | high | - |

Codex reason: 完整且可独立判读的美国人口普查官方简体句，适合检验正式资讯与机构语境。

Gemini reason: 完整句子，內容關於數據分析流程，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 02. census-newsroom-zh-hans-v1/page-01-sentence-037

Changed: `risk`

Input:

```text
人口普查局将密切注意 2020 年人口普查的成效以及不同地域和人口群组人数的统计情况。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可独立判读的美国人口普查官方简体句，适合检验正式资讯与机构语境。

Gemini reason: 完整句子，說明人口普查局的職責，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 03. census-newsroom-zh-hans-v1/page-02-sentence-013

Changed: `domain, risk`

Input:

```text
包括所有截至 4 月 1 日在您的住宅生活和留宿的人，即使他们暂时住在别的地方也要算上他们。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的美国人口普查官方简体句，适合检验正式资讯与机构语境。

Gemini reason: 完整句子，為填寫普查的具體指令，屬高風險應用場景，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 04. census-newsroom-zh-hans-v1/page-04-sentence-016

Changed: `risk`

Input:

```text
这些工作人员与社区组织合作，讲解回答 2020 年人口普查调查有多么容易、安全和重要。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | null | high | - |

Codex reason: 完整且可独立判读的美国人口普查官方简体句，适合检验正式资讯与机构语境。

Gemini reason: 完整句子，描述工作人員的職責，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 05. census-newsroom-zh-hans-v1/page-06-sentence-019

Changed: `domain, risk`

Input:

```text
将为他们发放个人防护装备，并将遵循当地的使用指南准则。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的美国人口普查官方简体句，适合检验正式资讯与机构语境。

Gemini reason: 完整句子，關於個人防護裝備的規定，涉及安全，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 06. census-newsroom-zh-hans-v1/page-06-sentence-028

Changed: `script, risk`

Input:

```text
在过去的几个月里，CPEP 的宣传工作主要是通过虚拟的方式进行，以支持留在住宅的命令和社交疏离要求。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | null | high | - |

Codex reason: 完整且可独立判读的美国人口普查官方简体句，适合检验正式资讯与机构语境。

Gemini reason: 完整句子，描述疫情期間的應對措施，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 07. census-newsroom-zh-hans-v1/page-07-sentence-002

Changed: `risk`

Input:

```text
计划明信片将在人口普查员开始拜访尚未回答住户的几个星期之前 7 月 22 日到 7 月 28 日期间送达。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | null | high | - |

Codex reason: 完整且可独立判读的美国人口普查官方简体句，适合检验正式资讯与机构语境。

Gemini reason: 完整句子，提供具體時間資訊，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 08. census-newsroom-zh-hans-v1/page-07-sentence-005

Changed: `risk`

Input:

```text
国家约 61.7% 的住户自从邀请在 3 月 12 日开始送达邮政信箱后已经通过在线、电话或邮件回答。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | null | high | - |

Codex reason: 完整且可独立判读的美国人口普查官方简体句，适合检验正式资讯与机构语境。

Gemini reason: 完整句子，包含統計數據，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 09. census-newsroom-zh-hans-v1/page-09-sentence-004

Changed: `risk`

Input:

```text
我们鼓励住户在收到邀请邮包后尽快回答 2020 年人口普查。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | null | high | - |

Codex reason: 完整且可独立判读的美国人口普查官方简体句，适合检验正式资讯与机构语境。

Gemini reason: 完整句子，鼓勵民眾盡快回應普查，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 10. cisa-personal-security-zh-hans-v1/sentence-005

Changed: `risk`

Input:

```text
本指南概括介绍了如何在家中、工作场所、公共场所和网上保持安全。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，概括安全指南內容，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 11. cisa-personal-security-zh-hans-v1/sentence-046

Changed: `risk`

Input:

```text
向警方提供任何监控录像、手机视频或照片，因为这可能有助于调查。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，指導如何協助警方調查，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 12. cisa-personal-security-zh-hans-v1/sentence-098

Changed: `risk`

Input:

```text
此外，始终确保您的车辆有足够的燃料（如果是电动车，则有足够的电量）供您完成旅程。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，關於行車安全的建議，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 13. cisa-personal-security-zh-hans-v1/sentence-106

Changed: `risk`

Input:

```text
请只从信誉良好的“应用程序商店”安装应用程序，以避免潜在的有害下载。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，關於網絡安全的建議，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 14. cisa-personal-security-zh-hans-v1/sentence-115

Changed: `risk`

Input:

```text
确保您使用的应用程序具有端到端加密功能。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，關於通訊安全的建議，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 15. cisa-personal-security-zh-hans-v1/sentence-127

Changed: `risk`

Input:

```text
针对人肉搜索的法律因辖区而异，因此在考虑预防和缓解方案时，一定要查阅所在地区的相关法律。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，提供關於「人肉搜索」的法律建議，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 16. osha-disaster-cleanup-simplified-v1/sentence-001

Changed: `eligible, domain, risk`

Input:

```text
在灾后清理以及重建时确保工人安全自然灾害可能导致洪水的大范围泛滥，并对财产和基础设施造成破坏。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 标题、版面或清单结构移除后成为串接句、残句、空泛指代或宣传标题，不适合离开上下文独立裁决。

Gemini reason: 完整句子，介紹災後重建的安全主題，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 17. osha-disaster-cleanup-simplified-v1/sentence-007

Changed: `eligible, domain`

Input:

```text
我们将会给您提供帮助。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | formal_news | null | high | - |

Codex reason: 标题、版面或清单结构移除后成为串接句、残句、空泛指代或宣传标题，不适合离开上下文独立裁决。

Gemini reason: 完整句子，雖然簡短但語意完整，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 18. osha-disaster-cleanup-simplified-v1/sentence-022

Changed: `risk`

Input:

```text
与所有倒下的电力线路保持至少10英尺（3米）的距离。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，提供避免觸電的明確安全距離指令，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 19. osha-disaster-cleanup-simplified-v1/sentence-044

Changed: `eligible, script, domain, risk`

Input:

```text
发电机废气中有毒的一氧化碳(CO)。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | no | null | null | high | fragment |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 不完整的句子，缺少動詞，描述一個危險來源但未構成完整陳述，排除。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 20. osha-disaster-cleanup-simplified-v1/sentence-051

Changed: `script, risk`

Input:

```text
穿着符合ANSI/ISEA 107-2004标准的高反光服装和安全帽。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，提供穿著高反光服裝的安全指令，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 21. osha-disaster-cleanup-simplified-v1/sentence-056

Changed: `eligible, domain, risk`

Input:

```text
施工活动在拆除房屋和建筑物时，接触被石棉污染的材料。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 标题、版面或清单结构移除后成为串接句、残句、空泛指代或宣传标题，不适合离开上下文独立裁决。

Gemini reason: 完整句子，描述接觸石棉的風險，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 22. osha-disaster-cleanup-simplified-v1/sentence-071

Changed: `script, risk`

Input:

```text
如果工人认为他们的雇主没有遵守OSHA标准或存在严重的危险，他们可以提出投诉、让OSHA检查他们的工作场所。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，說明工人提出投訴的權利與程序，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 23. ready-gov-drought-zh-hans-v1/sentence-014

Changed: `domain, risk`

Input:

```text
选择效率更高、性能更佳的设备。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | formal_news | null | high | - |

Codex reason: 完整且可独立判读的节水生活指引，适合检验日常用语与设备名称。

Gemini reason: 完整句子，為節約用水的建議，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 24. ready-gov-drought-zh-hans-v1/sentence-021

Changed: `domain, risk`

Input:

```text
如果自动泵不用水时会打开和关闭，则说明在漏水。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | formal_news | null | high | - |

Codex reason: 完整且可独立判读的节水生活指引，适合检验日常用语与设备名称。

Gemini reason: 完整句子，提供檢查漏水的方法，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 25. ready-gov-drought-zh-hans-v1/sentence-029

Changed: `domain, risk`

Input:

```text
定期检查自动洒水系统和计时装置，确保能正常运行。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | formal_news | null | high | - |

Codex reason: 完整且可独立判读的节水生活指引，适合检验日常用语与设备名称。

Gemini reason: 完整句子，關於維護灑水系統的建議，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 26. ready-gov-drought-zh-hans-v1/sentence-030

Changed: `domain, risk`

Input:

```text
将割草机刀片升高到至少三英寸或最高水平。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | formal_news | null | high | - |

Codex reason: 完整且可独立判读的节水生活指引，适合检验日常用语与设备名称。

Gemini reason: 完整句子，關於草坪維護以節水的建議，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 27. ready-gov-drought-zh-hans-v1/sentence-032

Changed: `domain, risk`

Input:

```text
种植抗旱的草种。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | formal_news | null | high | - |

Codex reason: 完整且可独立判读的节水生活指引，适合检验日常用语与设备名称。

Gemini reason: 完整句子，關於選擇草種的建議，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 28. ready-gov-drought-zh-hans-v1/sentence-050

Changed: `risk`

Input:

```text
刷牙、洗脸或剃须时，不要让水不停地流。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | null | high | - |

Codex reason: 完整且可独立判读的节水生活指引，适合检验日常用语与设备名称。

Gemini reason: 完整句子，關於日常節約用水的建議，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 29. ready-gov-drought-zh-hans-v1/sentence-052

Changed: `risk`

Input:

```text
自动洗碗机装满了再洗。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | null | high | - |

Codex reason: 完整且可独立判读的节水生活指引，适合检验日常用语与设备名称。

Gemini reason: 完整句子，關於節約用水的建議，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 30. ready-gov-drought-zh-hans-v1/sentence-054

Changed: `risk`

Input:

```text
手动洗碗时，用两个容器放满水，一个放肥皂水，另一个放含少量氯漂白剂的漂洗水。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | null | high | - |

Codex reason: 完整且可独立判读的节水生活指引，适合检验日常用语与设备名称。

Gemini reason: 完整句子，提供手動洗碗節約用水的具體方法，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 31. ready-gov-drought-zh-hans-v1/sentence-064

Changed: `domain, risk`

Input:

```text
如果土壤仍然潮湿，则无需浇水。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | formal_news | null | high | - |

Codex reason: 完整且可独立判读的节水生活指引，适合检验日常用语与设备名称。

Gemini reason: 完整句子，提供判斷是否需要澆水的建議，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 32. ready-gov-drought-zh-hans-v1/sentence-072

Changed: `domain, risk`

Input:

```text
使用利用回收水的商用洗车场。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | formal_news | null | high | - |

Codex reason: 完整且可独立判读的节水生活指引，适合检验日常用语与设备名称。

Gemini reason: 完整句子，提供節約用水洗車的建議，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 33. ready-gov-home-fires-zh-hans-v1/sentence-027

Changed: `risk`

Input:

```text
在厨房放一个灭火器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，關於放置滅火器的安全建議，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 34. ready-gov-home-fires-zh-hans-v1/sentence-035

Changed: `risk`

Input:

```text
告诉急救人员此人所在地方。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，指導如何在火災後向急救人員提供信息，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 35. ready-gov-home-fires-zh-hans-v1/sentence-036

Changed: `risk`

Input:

```text
如有宠物困在家中，立即告诉消防员。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，指導如何救助寵物，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 36. ready-gov-home-fires-zh-hans-v1/sentence-051

Changed: `domain, risk`

Input:

```text
保险公司以后可能需要这些收据，核实所得税索赔损失也可能需要。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | null | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，關於火災後處理財物損失的建議，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 37. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-016

Changed: `risk`

Input:

```text
根据合格岩土工程专家的建议和/或当地市/县关于防止泥石流和洪水的指南保护您的财产。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，提供防災的專業建議，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 38. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-017

Changed: `risk`

Input:

```text
您无法阻止或改变泥石流的路径。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，陳述關於泥石流的重要事實，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 39. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-024

Changed: `risk`

Input:

```text
如果您在野火燃烧区附近，请注册紧急警报并注意燃烧区的天气预报。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，提供監測天氣預報以防災的指令，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 40. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-034

Changed: `risk`

Input:

```text
地下公用事业线路断裂。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，描述山體滑坡的警示信號，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 41. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-040

Changed: `risk`

Input:

```text
始终遵循当地应急管理人员的指示。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，強調聽從官方指示的重要性，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 42. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-044

Changed: `risk`

Input:

```text
请注意，当您确定泥石流即将来临时，再安全逃离就为时已晚。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，關於泥石流逃生的重要警告，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 43. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-055

Changed: `eligible, domain, risk`

Input:

```text
引导救援人员到他们的位置。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 标题、版面或清单结构移除后成为串接句、残句、空泛指代或宣传标题，不适合离开上下文独立裁决。

Gemini reason: 完整句子，指導如何在災害後協助救援，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 44. ready-gov-radiation-zh-hans-v1/sentence-002

Changed: `risk`

Input:

```text
辐射紧急情况的一些例子包括：核爆炸（爆炸）、核电站事故、涉及运输放射性材料的运输事故，或在医疗保健或研究环境的职业中暴露。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，定義並舉例說明輻射緊急情況，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 45. ready-gov-radiation-zh-hans-v1/sentence-009

Changed: `script, risk`

Input:

```text
下载FEMA应用程序并从国家气象局接收全国最多五个地点的实时警报。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，提供獲取緊急警報的建議，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 46. ready-gov-radiation-zh-hans-v1/sentence-022

Changed: `risk`

Input:

```text
进入室内：如果警告可能存在辐射危害，请立即进入最近的建筑物并远离窗户。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，提供輻射緊急情況下的核心防護指令，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 47. ready-gov-radiation-zh-hans-v1/sentence-023

Changed: `risk`

Input:

```text
在您和外界之间放置尽可能多的墙，以保护您免受外界辐射。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，解釋防護原理，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 48. ready-gov-radiation-zh-hans-v1/sentence-031

Changed: `risk`

Input:

```text
如果在爆炸后的几分钟内可以安全到达多层建筑或地下室，请立即前往。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，提供核爆後的避難指令，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 49. ready-gov-radiation-zh-hans-v1/sentence-033

Changed: `risk`

Input:

```text
地下停车场和地铁也可以提供良好的庇护所。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，提供額外的庇護所建議，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 50. ready-gov-radiation-zh-hans-v1/sentence-038

Changed: `risk`

Input:

```text
关闭壁炉阻尼器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，簡短但清晰的防護指令，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 51. ready-gov-radiation-zh-hans-v1/sentence-059

Changed: `risk`

Input:

```text
来自室外的未密封食品可能被放射性物质污染。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可独立判读的官方安全指引，适合检验高风险语境、专业术语与识别码保留。

Gemini reason: 完整句子，關於食品安全的警告，合格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 52. ready-gov-radiation-zh-hans-v1/sentence-064

Changed: `script`

Input:

```text
PrepTalks：Brooke Buddemeier“在核爆炸后挽救生命”。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | no | null | null | high | title_or_heading |

Codex reason: 标题、版面或清单结构移除后成为串接句、残句、空泛指代或宣传标题，不适合离开上下文独立裁决。

Gemini reason: 引用標題，非完整敘述句，排除。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`
