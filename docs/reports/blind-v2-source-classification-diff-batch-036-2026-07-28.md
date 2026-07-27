<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 036 (2026-07-28)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `1c7c6f2ed9d05976b9c67ddf5844c05f1019aafb2ea6eeedbc9d1b267f096e53`
Cases: 96
Exact Codex/Gemini classifications: 45
Maintainer review queue: 51

Field differences:

- Eligibility: 2
- Script: 1
- Domain: 20
- Risk: 38

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

The maintainer resolved all 51 advisory disagreements and batch-confirmed the 45 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. census-newsroom-zh-hans-v1/page-01-sentence-011

Changed: `risk`

Input:

```text
如果有与 2010 年人口普查指标做对比的 2020 年人口普查指标，人口普查局也将发布此指标。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；用於檢驗正式用語、統計術語及受保護英文名稱。

Gemini reason: 正式新聞稿風格，標準轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 02. census-newsroom-zh-hans-v1/page-01-sentence-017

Changed: `script, risk`

Input:

```text
在接下来的四年中，人口普查局将对 2020 年人口普查的运作情况进行评估和测评(仅英语)，并向公众公布相关信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；用於檢驗正式用語、統計術語及受保護英文名稱。

Gemini reason: 混合英文，括號中的「仅英语」需注意避免過度轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 03. census-newsroom-zh-hans-v1/page-01-sentence-026

Changed: `risk`

Input:

```text
除了通过上述活动分析普查流程，还通过与其他人口总数做比较来评估普查。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；用於檢驗正式用語、統計術語及受保護英文名稱。

Gemini reason: 正式新聞稿，標準轉換風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 04. census-newsroom-zh-hans-v1/page-01-sentence-038

Changed: `risk`

Input:

```text
人口普查局将使用该信息并利用机会进行革新，为下一个十年，也就是 2030 年的人口普查做好准备。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；用於檢驗正式用語、統計術語及受保護英文名稱。

Gemini reason: 正式新聞稿，標準轉換風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 05. census-newsroom-zh-hans-v1/page-02-sentence-010

Changed: `domain`

Input:

```text
现在比以往任何时候都更容易自行回答，都不需要与人口普查员见面。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；用於檢驗正式用語、統計術語及受保護英文名稱。

Gemini reason: 公眾宣導風格，標準轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 06. census-newsroom-zh-hans-v1/page-02-sentence-011

Changed: `risk`

Input:

```text
这一点非常重要，因为目前国家、州和地方卫生当局正在提供健康和安全指导。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；用於檢驗正式用語、統計術語及受保護英文名稱。

Gemini reason: 新聞稿風格，標準轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 07. census-newsroom-zh-hans-v1/page-02-sentence-020

Changed: `domain`

Input:

```text
然后，请确保您的朋友、家庭和社交网络了解回答的重要性，并鼓励他们完成人口普查。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；用於檢驗正式用語、統計術語及受保護英文名稱。

Gemini reason: 社交口吻，「网络」是潛在的詞彙轉換點。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 08. census-newsroom-zh-hans-v1/page-03-sentence-031

Changed: `risk`

Input:

```text
人口普查统计数据在接下来的十年内将帮助确定每个州 (state) 在美国众议院中的席位，并确定每年成百上千亿美元的联邦资金将如何在州 (state) 和社区分配。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；用於檢驗正式用語、統計術語及受保護英文名稱。

Gemini reason: 包含英文原文(state)與「数据」，有詞彙轉換與原文保護的雙重風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 09. census-newsroom-zh-hans-v1/page-06-sentence-003

Changed: `risk`

Input:

```text
截止今天，已经有超过 9000 万住户回答了 2020 年人口普查，每五个住户中超过四个住户通过在线回答。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；用於檢驗正式用語、統計術語及受保護英文名稱。

Gemini reason: 「在线」是典型的地區詞彙差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 10. census-newsroom-zh-hans-v1/page-06-sentence-005

Changed: `risk`

Input:

```text
以下概述的操作更新信息包括更新/普查、未回复随访、Alaska 偏远地区操作、合作关系活动、移动问卷帮助 (MQA) 计划以及综合交流和合作关系宣传活动。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；用於檢驗正式用語、統計術語及受保護英文名稱。

Gemini reason: 包含多個潛在的詞彙轉換點，如「信息」、「回复」、「移动」、「计划」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 11. census-newsroom-zh-hans-v1/page-06-sentence-024

Changed: `domain`

Input:

```text
如果人们通常不住在其他地方，而是住在露营地、房车公园、游艇码头和宾馆，人口普查员会在 9 月 3 日到 9 月 28 日之间算上他们。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；用於檢驗正式用語、統計術語及受保護英文名稱。

Gemini reason: 包含「房车」、「公园」等地區詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 12. census-newsroom-zh-hans-v1/page-06-sentence-027

Changed: `risk`

Input:

```text
在当地政府指导方针的协调下，合作伙伴关系专员于 6 月初恢复了面对面的工作，与 37 万多个合作伙伴组织合作，并在全国各地安全的区域参加了面对面活动。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；用於檢驗正式用語、統計術語及受保護英文名稱。

Gemini reason: 正式新聞稿，用語標準。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 13. census-newsroom-zh-hans-v1/page-06-sentence-035

Changed: `risk`

Input:

```text
其他付费媒体计划在七月、八月和九月开展工作。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；用於檢驗正式用語、統計術語及受保護英文名稱。

Gemini reason: 「计划」和「开展」是潛在的詞彙轉換點。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 14. census-newsroom-zh-hans-v1/page-07-sentence-013

Changed: `domain, risk`

Input:

```text
虽然从 8 月 11 日开始，人口普查员将开始拜访尚未回答的住户，但这些住户在 10 月 31 日拜访结束前都可以自行回答。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；用於檢驗正式用語、統計術語及受保護英文名稱。

Gemini reason: 公眾宣導語氣，標準轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 15. census-newsroom-zh-hans-v1/page-08-sentence-004

Changed: `risk`

Input:

```text
“人口普查局不遗余力地保证我们的工作质量” , 人口普查局常务局长兼首席运营官 Ron Jarmin 博士说。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；用於檢驗正式用語、統計術語及受保護英文名稱。

Gemini reason: 引文中的「质量」是關鍵的地區詞彙差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 16. census-newsroom-zh-hans-v1/page-08-sentence-028

Changed: `risk`

Input:

```text
由于这些估计依靠随时间变化的历史记录和种族指标，所以只能包含有限的种族详细信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；用於檢驗正式用語、統計術語及受保護英文名稱。

Gemini reason: 包含「记录」、「信息」等潛在轉換詞。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 17. census-newsroom-zh-hans-v1/page-09-sentence-006

Changed: `domain`

Input:

```text
住户可以用英语或其他 12 种语言在线上回答，也可以使用邮包中的人口普查号码 (Census ID) 通过电话回答，或者完成送达他们的纸质问卷并通过邮件寄回。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；用於檢驗正式用語、統計術語及受保護英文名稱。

Gemini reason: 包含英文(Census ID)，需避免轉換。同時包含「线上」、「邮包」等具地區性的詞語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 18. massive-1-0-zh-cn-v1/11605

Changed: `risk`

Input:

```text
武汉市最好的提供素食的运动酒吧有哪些
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的日常指令或敘述；用於檢驗臺灣慣用語與實體名稱保護。

Gemini reason: 地名「武漢市」為專有名詞。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 19. massive-1-0-zh-cn-v1/13874

Changed: `eligible, domain, risk`

Input:

```text
大打击加州
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | yes | social_daily | over_conversion_guard | medium | - |

Codex reason: 來源句含明顯機器翻譯錯置、不可解片段或依賴未提供的指涉，無法作為可靠且可獨立裁決的 benchmark 輸入。

Gemini reason: 地名「加州」為專有名詞。句子本身語意不完整，但可獨立判斷。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 20. massive-1-0-zh-cn-v1/14279

Changed: `domain, risk`

Input:

```text
请定义印刷作品
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的日常指令或敘述；用於檢驗臺灣慣用語與實體名稱保護。

Gemini reason: 標準術語，穩定轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 21. massive-1-0-zh-cn-v1/14294

Changed: `domain, risk`

Input:

```text
解释卢比对美元的汇率
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的日常指令或敘述；用於檢驗臺灣慣用語與實體名稱保護。

Gemini reason: 財經領域，標準術語轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 22. massive-1-0-zh-cn-v1/14674

Changed: `risk`

Input:

```text
东方人穿什么样的衣服
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的日常指令或敘述；用於檢驗臺灣慣用語與實體名稱保護。

Gemini reason: 日常詢問，標準轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 23. massive-1-0-zh-cn-v1/14717

Changed: `domain`

Input:

```text
告诉我红旗汽车的股价
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的日常指令或敘述；用於檢驗臺灣慣用語與實體名稱保護。

Gemini reason: 品牌名稱「紅旗汽車」為專有名詞，需防過度轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 24. massive-1-0-zh-cn-v1/2755

Changed: `domain`

Input:

```text
包头最近的新闻
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的日常指令或敘述；用於檢驗臺灣慣用語與實體名稱保護。

Gemini reason: 地名「包頭」為專有名詞，需防過度轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 25. massive-1-0-zh-cn-v1/3006

Changed: `risk`

Input:

```text
创作这首歌的艺术家叫什么名字
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的日常指令或敘述；用於檢驗臺灣慣用語與實體名稱保護。

Gemini reason: 日常詢問，標準轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 26. massive-1-0-zh-cn-v1/3398

Changed: `risk`

Input:

```text
给我设个下午五点的闹铃
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的日常指令或敘述；用於檢驗臺灣慣用語與實體名稱保護。

Gemini reason: 日常用語，標準轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 27. massive-1-0-zh-cn-v1/3683

Changed: `domain`

Input:

```text
olly 保存我听过不止一次的所有歌
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的日常指令或敘述；用於檢驗臺灣慣用語與實體名稱保護。

Gemini reason: 包含不應轉換的英文名稱 'olly'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 28. massive-1-0-zh-cn-v1/3820

Changed: `risk`

Input:

```text
请注意当前的歌
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的日常指令或敘述；用於檢驗臺灣慣用語與實體名稱保護。

Gemini reason: 日常用語，標準轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 29. massive-1-0-zh-cn-v1/5926

Changed: `risk`

Input:

```text
搜索关于苹果手机的最新消息
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的日常指令或敘述；用於檢驗臺灣慣用語與實體名稱保護。

Gemini reason: 「手機」是兩岸慣用詞差異的典型案例。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 30. massive-1-0-zh-cn-v1/7446

Changed: `eligible, domain, risk`

Input:

```text
我需要建一个仅和这几个人的事项
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 來源句含明顯機器翻譯錯置、不可解片段或依賴未提供的指涉，無法作為可靠且可獨立裁決的 benchmark 輸入。

Gemini reason: 日常用語，標準轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 31. massive-1-0-zh-cn-v1/826

Changed: `risk`

Input:

```text
外面当前的气温多少啊
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的日常指令或敘述；用於檢驗臺灣慣用語與實體名稱保護。

Gemini reason: 日常詢問，標準轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 32. massive-1-0-zh-cn-v1/840

Changed: `risk`

Input:

```text
从必胜客给晚上七点点外卖比萨
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的日常指令或敘述；用於檢驗臺灣慣用語與實體名稱保護。

Gemini reason: 包含品牌「必勝客」，且「點外賣」、「比薩」均為兩岸慣用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 33. zhtw-project-llm-social-baseline-v1/llm-011

Changed: `risk`

Input:

```text
模型把两个不同的人名合并了，需要重新检查实体对应关系。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的 LLM 使用情境；用於檢驗模型、工具、格式與受保護技術字串。

Gemini reason: 關於 AI 模型的行為描述，用詞直接，轉換風險低。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 34. zhtw-project-llm-social-baseline-v1/llm-012

Changed: `risk`

Input:

```text
请只改写语气，不要改变数字、日期或否定关系。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的 LLM 使用情境；用於檢驗模型、工具、格式與受保護技術字串。

Gemini reason: 給予 AI 的指令，用字簡單明確，屬於穩定轉換範圍。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 35. zhtw-project-llm-social-baseline-v1/llm-015

Changed: `domain, risk`

Input:

```text
如果问题涉及医疗风险，助手应建议咨询合格的专业人员。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的 LLM 使用情境；用於檢驗模型、工具、格式與受保護技術字串。

Gemini reason: 涉及醫療建議，屬於高風險領域。用詞「助手」在臺灣可能需依情境調整為「助理」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 36. zhtw-project-llm-social-baseline-v1/llm-019

Changed: `domain`

Input:

```text
模型返回 429 错误后，客户端按照 Retry-After 延迟重试。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 LLM 使用情境；用於檢驗模型、工具、格式與受保護技術字串。

Gemini reason: 描述 API 客戶端行為，包含不應轉換的 HTTP 標頭 `Retry-After`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 37. zhtw-project-llm-social-baseline-v1/llm-020

Changed: `domain`

Input:

```text
向量索引重建期间，旧版本仍可用于线上查询。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的 LLM 使用情境；用於檢驗模型、工具、格式與受保護技術字串。

Gemini reason: IT 技術描述，包含中國大陸慣用詞「线上」，在臺灣應轉換為「線上」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 38. zhtw-project-llm-social-baseline-v1/llm-021

Changed: `domain`

Input:

```text
这个代理只能读取工单，不能修改状态或发送消息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的 LLM 使用情境；用於檢驗模型、工具、格式與受保護技術字串。

Gemini reason: 描述系統權限，用詞「工单」在臺灣 IT 情境中可能用「工單」或「票證」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 39. zhtw-project-llm-social-baseline-v1/llm-025

Changed: `domain, risk`

Input:

```text
助手引用法规时必须保留条文编号和公布日期。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的 LLM 使用情境；用於檢驗模型、工具、格式與受保護技術字串。

Gemini reason: 關於引用法規的格式要求，詞彙轉換直接，風險較低。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 40. zhtw-project-llm-social-baseline-v1/llm-029

Changed: `domain`

Input:

```text
内容过滤器拦截了请求，但没有记录原始敏感文本。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的 LLM 使用情境；用於檢驗模型、工具、格式與受保護技術字串。

Gemini reason: 描述內容過濾系統，用詞「过滤器」在臺灣慣用「過濾器」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 41. zhtw-project-llm-social-baseline-v1/llm-032

Changed: `risk`

Input:

```text
评审人员只能看到输入和候选标签，不能看到产品输出。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的 LLM 使用情境；用於檢驗模型、工具、格式與受保護技術字串。

Gemini reason: 描述評審流程，詞彙雖屬特定領域但對應關係穩定。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 42. zhtw-project-llm-social-baseline-v1/llm-035

Changed: `risk`

Input:

```text
模型在回答末尾列出信心较低的判断，方便人工复核。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的 LLM 使用情境；用於檢驗模型、工具、格式與受保護技術字串。

Gemini reason: 描述 AI 模型輸出格式，詞彙轉換直接。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 43. zhtw-project-llm-social-baseline-v1/llm-044

Changed: `domain`

Input:

```text
请将结果写入 CSV，并使用 UTF-8 编码保存。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 LLM 使用情境；用於檢驗模型、工具、格式與受保護技術字串。

Gemini reason: IT 指令，包含不應轉換的檔案格式 `CSV` 與編碼 `UTF-8`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 44. zhtw-project-llm-social-baseline-v1/llm-047

Changed: `risk`

Input:

```text
请检查回答是否遗漏例外条件，而不是只比较关键词。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的 LLM 使用情境；用於檢驗模型、工具、格式與受保護技術字串。

Gemini reason: 評估 AI 回答的指令，用詞直接，轉換風險低。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 45. zhtw-project-llm-social-baseline-v1/llm-049

Changed: `domain`

Input:

```text
新的嵌入模型上线后，旧索引需要按计划逐步重建。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的 LLM 使用情境；用於檢驗模型、工具、格式與受保護技術字串。

Gemini reason: IT 技術描述，包含中國大陸慣用詞「上线」，在臺灣應轉換為「上線」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 46. zhtw-project-llm-social-baseline-v1/social-022

Changed: `risk`

Input:

```text
新买的充电线接触不良，我准备拿去换货。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的日常指令或敘述；用於檢驗臺灣慣用語與實體名稱保護。

Gemini reason: 日常購物對話，詞彙在兩岸通用，轉換直接。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 47. zhtw-project-llm-social-baseline-v1/social-023

Changed: `risk`

Input:

```text
报名表已经提交，主办方会在下周通知结果。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的日常指令或敘述；用於檢驗臺灣慣用語與實體名稱保護。

Gemini reason: 日常事務對話，詞彙轉換直接。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 48. zhtw-project-llm-social-baseline-v1/social-034

Changed: `risk`

Input:

```text
这篇文章标题很吸引人，内容却没有提供具体来源。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的日常指令或敘述；用於檢驗臺灣慣用語與實體名稱保護。

Gemini reason: 評論文章內容，用詞普遍，轉換風險低。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 49. zhtw-project-llm-social-baseline-v1/social-040

Changed: `risk`

Input:

```text
我没有看到附件，麻烦你再发送一次。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的日常指令或敘述；用於檢驗臺灣慣用語與實體名稱保護。

Gemini reason: 日常辦公對話，用詞「发送」在臺灣情境下也常用「傳送」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 50. zhtw-project-llm-social-baseline-v1/social-043

Changed: `risk`

Input:

```text
订单显示已经出货，但物流编号还查不到记录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的日常指令或敘述；用於檢驗臺灣慣用語與實體名稱保護。

Gemini reason: 網路購物情境，用詞在兩岸電商領域通用，轉換直接。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 51. zhtw-project-llm-social-baseline-v1/social-047

Changed: `risk`

Input:

```text
维修人员上午来过，但需要订购零件才能处理。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的日常指令或敘述；用於檢驗臺灣慣用語與實體名稱保護。

Gemini reason: 日常對話，詞彙轉換直接。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`
