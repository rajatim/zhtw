<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 003 (2026-07-22)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `3ada05e07e54145bede74f1514bcfd1aa9d296102893e0bf8ec3e4aed19e97d3`
Cases: 62
Exact Codex/Gemini classifications: 33
Maintainer review queue: 29

Field differences:

- Eligibility: 1
- Script: 0
- Domain: 20
- Risk: 21

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

The maintainer resolved all 29 advisory disagreements and batch-confirmed the 33 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. cdc-stacks-111808-v1/p01-005

Changed: `risk`

Input:

```text
每天清洁所有“高频触碰”的物体表面。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 含區域詞或專業用語，可能需要臺灣慣用詞轉換；句意可獨立判讀。

Gemini reason: 公共衛生建議，包含『清洁』、『高频触碰』等詞語。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 02. cdc-stacks-111808-v1/p01-006

Changed: `risk`

Input:

```text
尽可能呆在特定房间中。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 含區域詞或專業用語，可能需要臺灣慣用詞轉換；句意可獨立判讀。

Gemini reason: 公共衛生建議，包含『呆在』一詞，需注意地區用詞差異。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 03. cdc-stacks-111808-v1/p02-002

Changed: `risk`

Input:

```text
COVID-19 症状包括发烧、咳嗽、呼吸短促等。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 含區域詞或專業用語，可能需要臺灣慣用詞轉換；句意可獨立判讀。

Gemini reason: 醫療症狀描述，包含『症状』、『发烧』、『咳嗽』等詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 04. cdc-stacks-111808-v1/p02-003

Changed: `risk`

Input:

```text
遵循您的医疗保健提供者和当地卫生部门的指示。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 含區域詞或專業用語，可能需要臺灣慣用詞轉換；句意可獨立判讀。

Gemini reason: 醫療指示，包含『医疗保健』、『卫生』等詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 05. cdc-stacks-111808-v1/p02-009

Changed: `risk`

Input:

```text
拨打 911 或提前致电您当地的急救机构通知接线员您为已经或可能患有 COVID-19 的人员寻求治疗。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 含區域詞或專業用語，可能需要臺灣慣用詞轉換；句意可獨立判讀。

Gemini reason: 緊急醫療指示，包含『拨打』、『致电』、『机构』、『接线员』等詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 06. cdc-stacks-116683-v1/p01-001

Changed: `domain, risk`

Input:

```text
实现健康平等是指每个人都有公平公正的机会达到最高健康水平。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 含區域詞或專業用語，可能需要臺灣慣用詞轉換；句意可獨立判讀。

Gemini reason: 公共衛生政策文件，用詞正式，包含『实现』一詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 07. cdc-stacks-116683-v1/p01-002

Changed: `domain`

Input:

```text
我们都可以在解决不公正现象和克服健康和医疗障碍方面发挥作用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 句意可獨立判讀，主要為一般字形轉換。

Gemini reason: 公共衛生政策文件，包含『解决』、『障碍』等詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 08. cdc-stacks-116683-v1/p01-003

Changed: `domain, risk`

Input:

```text
应对 COVID-19 疫情期间， CDC 始终将其健康平等工作的重点放在 COVID-19 及其他严重后果的高风险人群上。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 含機構名、疫情名稱或英文字母縮寫，應保護專名並避免過度轉換。

Gemini reason: 公共衛生政策文件，包含『疫情』、『始终』、『重点』等詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 09. cdc-stacks-116683-v1/p01-004

Changed: `domain, risk`

Input:

```text
请阅读下文的项目描述，详细了解关于 CDC 与受资助合作伙伴通过合作减少 COVID-19 相关健康差异的信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 含區域詞或專業用語，可能需要臺灣慣用詞轉換；句意可獨立判讀。

Gemini reason: 公共衛生政策文件，包含『阅读』、『详细』、『信息』等詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 10. cdc-stacks-116683-v1/p01-005

Changed: `domain`

Input:

```text
目的：开发一套新型工具，社区可以用来监测和解决污名化和种族主义如何影响 COVID-19 的差异。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 含 COVID-19 專名，應避免過度轉換；其餘主要為一般字形轉換。

Gemini reason: 專案目標描述，包含『开发』、『监测』、『解决』、『种族主义』等術語。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 11. cdc-stacks-116683-v1/p01-006

Changed: `domain`

Input:

```text
目标是更有效地应对社区中的 COVID-19 和其他公共卫生危机。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 句意可獨立判讀，主要為一般字形轉換。

Gemini reason: 專案目標描述，用詞正式。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 12. cdc-stacks-116683-v1/p01-007

Changed: `domain`

Input:

```text
支持公共卫生从业人员监测与 COVID-19 相关的污名化对历史上被边缘化、种族化和受严重影响的人群的存在、传播和影响。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | awkward_source_wording |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 句意仍可判讀，但上游翻譯措辭不自然，保留品質旗標供後續抽樣過濾。

Gemini reason: 專案目標描述，包含『从业人员』、『监测』、『边缘化』等術語。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 13. cdc-stacks-116683-v1/p01-008

Changed: `domain, risk`

Input:

```text
通过向在受 COVID-19 严重影响社区工作、生活和代表社区的可信赖基本服务人员和一线工作人员（例如，社区卫生工作者、药剂师、助产士和社会工作者）提供工具、技术援助和教育，从而充分利用以社区为基础的工作和组织。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | long_sentence |

Codex reason: 含區域詞或專業用語，可能需要臺灣慣用詞轉換；句意可獨立判讀。

Gemini reason: 長句，但語意清晰，可測試多個基本簡繁轉換的穩定性，如『通过』、『药剂师』、『组织』。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 14. cdc-stacks-116683-v1/p01-009

Changed: `domain, risk`

Input:

```text
与少数族裔媒体开展合作，分享向关注的社区传递信息的最佳做法，同时提供社区意见，以供社区工作考虑和采纳。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 含區域詞或專業用語，可能需要臺灣慣用詞轉換；句意可獨立判讀。

Gemini reason: 專案目標描述，包含『与』、『合作』、『传递』等詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 15. cdc-stacks-116683-v1/p03-001

Changed: `domain`

Input:

```text
目的：让参与残障研究和外展的全国大学中心和项目网络加入其中，以 1）促进 COVID-19 疫苗沟通， 2）确认疫苗可获得性障碍，以及 3）增强残障群体对疫苗的信心。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | candidate_gap | high | long_sentence |

Codex reason: 含區域詞或專業用語，可能需要臺灣慣用詞轉換；句意可獨立判讀。

Gemini reason: 專案目標描述，包含『残障』一詞，需注意地區用詞（如台灣用『身心障礙』）。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 16. cdc-stacks-116683-v1/p03-002

Changed: `domain, risk`

Input:

```text
项目合作伙伴共享可信的 COVID-19 免疫接种信息、应对错误信息、将信息转化为无障碍格式，并分享成功故事和所吸取的教训。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 含區域詞或專業用語，可能需要臺灣慣用詞轉換；句意可獨立判讀。

Gemini reason: 專案合作描述，包含『共享』、『错误信息』、『无障碍』等詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 17. cdc-stacks-116683-v1/p03-003

Changed: `domain, risk`

Input:

```text
此外，大学合作伙伴参与编制易于阅读且可获得的疫苗材料（信息图、故事板报、图像）并将这些材料通过其本地社区内的媒体宣传活动进行传播。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 含區域詞或專業用語，可能需要臺灣慣用詞轉換；句意可獨立判讀。

Gemini reason: 專案合作描述，包含『大学』、『信息图』、『图像』等詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 18. cdc-stacks-116683-v1/p03-004

Changed: `eligible, domain, risk`

Input:

```text
目的：制定和执行全国媒体信息传播活动，以增加 AI/AN 社区中的 COVID-19 免疫而集中。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_sentence |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 「免疫而集中」使核心目的無法可靠判讀，屬上游文字錯誤，建議排除。

Gemini reason: 專案目標描述，包含『制定』、『执行』、『全国』、『活动』等詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 19. cdc-stacks-116683-v1/p04-001

Changed: `domain, risk`

Input:

```text
目的：建立（AA 和 NH/PI）社区合作伙伴关系，以提供翻译的 COVID-19 信息，满足社区的独特需求、优势和偏好。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 「合作伙伴关系」有臺灣慣用詞差異；AA、NH/PI 與 COVID-19 應原樣保護。

Gemini reason: 專案目標描述，包含『建立』、『合作伙伴关系』、『提供』等詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 20. cdc-stacks-116683-v1/p06-001

Changed: `risk`

Input:

```text
目的：支持州卫生部门和其他组织倡导 COVID-19 疫情期间的健康生活和社会联系，同时与地方社区合作改善食品和营养安全、体育活动的安全获取以及降低孤立感和孤独感。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | long_sentence |

Codex reason: 含區域詞或專業用語，可能需要臺灣慣用詞轉換；句意可獨立判讀。

Gemini reason: 公共衛生倡議，包含『倡导』、『体育活动』、『营养』等詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 21. cdc-stacks-116683-v1/p06-002

Changed: `domain, risk`

Input:

```text
目的：通过加强与社区组织 (CBO) 的合作伙伴关系并提高 CBO 应对突发公共卫生事件（包括流行病）的能力，改善员工的应急准备和应对做法。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 含區域詞或專業用語，可能需要臺灣慣用詞轉換；句意可獨立判讀。

Gemini reason: 公共衛生應急準備，包含『加强』、『合作伙伴关系』、『组织』、『应对』等詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 22. cdc-stacks-116683-v1/p07-001

Changed: `domain`

Input:

```text
目的：招募成熟且值得信赖的组织，动员处于 COVID-19 疾病和死亡风险较高的非裔美国人和非西班牙裔黑人社区采用和保持 COVID-19 预防措施和社区缓解策略。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 句意可獨立判讀，主要為一般字形轉換。

Gemini reason: 公共衛生項目描述，包含『招募』、『组织』、『动员』、『风险』等詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 23. cdc-stacks-116683-v1/p08-001

Changed: `risk`

Input:

```text
目的：确保更多艾滋病毒感染者获得四个月的每日药品包。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 含區域詞或專業用語，可能需要臺灣慣用詞轉換；句意可獨立判讀。

Gemini reason: 醫療項目描述，包含『艾滋病毒』、『药品』等專業詞彙。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 24. cdc-stacks-116683-v1/p08-002

Changed: `risk`

Input:

```text
该项目还包括更新治疗指导方针，以指定如何以最佳方式做到多月配药，并培训医疗服务提供者实施该过程。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 含區域詞或專業用語，可能需要臺灣慣用詞轉換；句意可獨立判讀。

Gemini reason: 醫療項目描述，包含『治疗』、『指导方针』、『医疗服务提供者』、『实施』等詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 25. cdc-stacks-116683-v1/p08-003

Changed: `domain, risk`

Input:

```text
目的：在受 COVID-19 影响最严重的社区以及 COVID-19 接触、感染和疾病风险更高的人群（包括受到长期健康差异严重影响的人）中培训和部署 CHW，这些 CHW 将通过解决现有的健康差异问题，帮助建立和加强社区对抗 COVID-19 的灵活性。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | awkward_source_wording |
| Gemini | yes | formal_news | baseline_guard | high | long_sentence |

Codex reason: 句意仍可判讀，但上游翻譯措辭不自然，保留品質旗標供後續抽樣過濾。

Gemini reason: 公共衛生項目描述，長句，包含『部署』、『解决』、『加强』等詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 26. cdc-stacks-120024-v1/p01-001

Changed: `domain, risk`

Input:

```text
美国疾病控制和预防中心制作了这份活动手册，目的是为父母们提供一种互动方式，与孩子们谈论牙齿护理的方法。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 含機構名、疫情名稱或英文字母縮寫，應保護專名並避免過度轉換。

Gemini reason: 兒童活動手冊的引言，包含『美国』、『制作』、『活动』、『与』、『谈论』等詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 27. cdc-stacks-120024-v1/p01-002

Changed: `risk`

Input:

```text
有规律的口腔健康习惯（比如刷牙、用牙线洁牙、定期去看牙医）都有助于预防蛀牙。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 含區域詞或專業用語，可能需要臺灣慣用詞轉換；句意可獨立判讀。

Gemini reason: 給父母和兒童的健康建議，包含『有规律』、『习惯』、『洁牙』等詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 28. cdc-stacks-120024-v1/p06-002

Changed: `domain`

Input:

```text
刷牙时听两分钟自己最喜欢的歌曲会有帮助。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 句意可獨立判讀，主要為一般字形轉換。

Gemini reason: 生活建議，包含『听』、『歌曲』。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`

### 29. cdc-stacks-120024-v1/p06-003

Changed: `domain`

Input:

```text
每次刷牙时，把歌曲或计时器设置为两分钟。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 句意可獨立判讀，主要為一般字形轉換。

Gemini reason: 生活建議，包含『计时器』、『设置为』。

Maintainer decision: `codex` accepted by `tim` on `2026-07-22`
