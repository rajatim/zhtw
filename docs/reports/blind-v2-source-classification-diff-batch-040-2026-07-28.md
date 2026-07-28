<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 040 (2026-07-28)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `21be9eb5c5a839c761b3cee48a7a431e7840e5f4280ff281e3d5dc23b6f4ee7e`
Cases: 96
Exact Codex/Gemini classifications: 43
Maintainer review queue: 53

Field differences:

- Eligibility: 9
- Script: 0
- Domain: 13
- Risk: 52

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

The maintainer resolved all 53 advisory disagreements and batch-confirmed the 43 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. massive-1-0-zh-cn-v1/10520

Changed: `risk`

Input:

```text
查找清单并且删除苹果
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: Clear, complete command. '清单' is a standard term.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 02. massive-1-0-zh-cn-v1/109

Changed: `risk`

Input:

```text
播放可惜没如果
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: Clear, complete command to play a song.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 03. massive-1-0-zh-cn-v1/11070

Changed: `risk`

Input:

```text
你能告诉我我的杂货清单上有什么
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: Clear, complete question. '杂货清单' is standard.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 04. massive-1-0-zh-cn-v1/11939

Changed: `risk`

Input:

```text
告诉我附近的有哪些商店
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: Clear, complete local search query.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 05. massive-1-0-zh-cn-v1/12588

Changed: `risk`

Input:

```text
这是去纽约的火车时刻表
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: A complete statement. '时刻表' is a standard term.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 06. massive-1-0-zh-cn-v1/12861

Changed: `risk`

Input:

```text
下一班去罗马的火车什么时候到
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: Clear, complete question about transportation.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 07. massive-1-0-zh-cn-v1/13582

Changed: `domain, risk`

Input:

```text
欧元兑美元的汇率是多少
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: Clear, complete question about financial data.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 08. massive-1-0-zh-cn-v1/14070

Changed: `domain`

Input:

```text
奈飞股价是多少
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: Clear, complete question. '奈飞' for Netflix is a good test case for brand names.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 09. massive-1-0-zh-cn-v1/14080

Changed: `risk`

Input:

```text
百慕大三角的成因
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: Clear search phrase for general knowledge.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 10. massive-1-0-zh-cn-v1/14302

Changed: `domain, risk`

Input:

```text
现在日元的价值是多少
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: Clear, complete question about financial data.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 11. massive-1-0-zh-cn-v1/14766

Changed: `risk`

Input:

```text
alexa 你如何描述一个球
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: A complete, if slightly philosophical, question. Contains the wake word 'alexa'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 12. massive-1-0-zh-cn-v1/15000

Changed: `eligible, domain, risk`

Input:

```text
我需要新 lg 洗衣机的定义
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | yes | social_daily | over_conversion_guard | medium | unnatural_phrasing |

Codex reason: 來源句為殘句、錯譯病句、單位不明或依賴前文，無法作為可靠且可獨立裁決的 benchmark 輸入。

Gemini reason: Grammatically valid, but the use of '定义' (definition) for a washing machine is unusual. Likely means 'specs' or 'info'. Contains brand name 'lg'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 13. massive-1-0-zh-cn-v1/15203

Changed: `risk`

Input:

```text
最新更新
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: A common and clear command phrase.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 14. massive-1-0-zh-cn-v1/15351

Changed: `risk`

Input:

```text
联系张三
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: Clear command. '张三' is a common placeholder name.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 15. massive-1-0-zh-cn-v1/1544

Changed: `eligible, domain, risk`

Input:

```text
我想听上拍音乐
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | yes | social_daily | over_conversion_guard | medium | unnatural_translation |

Codex reason: 來源句為殘句、錯譯病句、單位不明或依賴前文，無法作為可靠且可獨立裁決的 benchmark 輸入。

Gemini reason: Grammatically valid, but '上拍音乐' is an unnatural or literal translation for 'upbeat music'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 16. massive-1-0-zh-cn-v1/1690

Changed: `risk`

Input:

```text
olly 这周的天气预报怎么样
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: Clear, complete question with a wake word 'olly'.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 17. massive-1-0-zh-cn-v1/3143

Changed: `risk`

Input:

```text
这是一首五星歌曲
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: Clear statement, likely a rating command.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 18. massive-1-0-zh-cn-v1/3189

Changed: `domain, risk`

Input:

```text
叙利亚战乱结束了吗
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: Clear, complete question on a geopolitical news topic.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 19. massive-1-0-zh-cn-v1/3344

Changed: `risk`

Input:

```text
明天我几点起床啊
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: Clear, colloquial question about setting an alarm.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 20. massive-1-0-zh-cn-v1/3505

Changed: `risk`

Input:

```text
下周上海市天气怎么样啊
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: Clear, colloquial question about weather.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 21. massive-1-0-zh-cn-v1/445

Changed: `risk`

Input:

```text
重播专辑
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: Clear, concise music command.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 22. massive-1-0-zh-cn-v1/454

Changed: `risk`

Input:

```text
把厨房的灯改成蓝色
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: Clear smart home command.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 23. massive-1-0-zh-cn-v1/5026

Changed: `risk`

Input:

```text
使灯光变得自然
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: Clear smart home command for lighting.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 24. massive-1-0-zh-cn-v1/5551

Changed: `risk`

Input:

```text
最近的还在营业的餐馆是哪家
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: Clear, complete local search question.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 25. massive-1-0-zh-cn-v1/7945

Changed: `risk`

Input:

```text
十一月二十日有什么事
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: Clear calendar-related query.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 26. massive-1-0-zh-cn-v1/9093

Changed: `risk`

Input:

```text
清除三月日历中的所有的活动
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: Clear calendar management command.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 27. massive-1-0-zh-cn-v1/9255

Changed: `risk`

Input:

```text
打开收音机
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: Clear, classic command to turn on a device.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 28. massive-1-0-zh-cn-v1/9462

Changed: `risk`

Input:

```text
调新闻频道
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具有明確查詢或操作意圖。

Gemini reason: Clear, concise command to change a channel.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 29. ready-gov-winter-weather-zh-hans-v1/sentence-001

Changed: `risk`

Input:

```text
冬季风暴会增加发生车祸、体温过低、冻伤、一氧化碳中毒和因过度劳累引起的心脏病的风险。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全指引；依輸入本身分類，未參考 converter output。

Gemini reason: 完整句子，公共安全指引，属于高风险领域。包含多个专业术语，是良好的基线测试案例。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 30. ready-gov-winter-weather-zh-hans-v1/sentence-002

Changed: `risk`

Input:

```text
包括暴风雪在内的冬季风暴会带来极冷、冻雨、大雪、冰冻和大风。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全指引；依輸入本身分類，未參考 converter output。

Gemini reason: 完整句子，公共安全指引。包含多个天气术语。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 31. ready-gov-winter-weather-zh-hans-v1/sentence-013

Changed: `eligible, domain, risk`

Input:

```text
注册社区警告系统。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | no | null | null | high | fragment |

Codex reason: 完整且可獨立判讀的公共安全指引；依輸入本身分類，未參考 converter output。

Gemini reason: 祈使句，但更像是清单或标题，结构过于简单，可视为片段。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 32. ready-gov-winter-weather-zh-hans-v1/sentence-017

Changed: `eligible, domain, risk`

Input:

```text
安装和测试带有备用电池的烟雾报警器和一氧化碳探测器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | no | null | null | high | fragment |

Codex reason: 完整且可獨立判讀的公共安全指引；依輸入本身分類，未參考 converter output。

Gemini reason: 指令性片段，清单项目，非完整叙述性句子。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 33. ready-gov-winter-weather-zh-hans-v1/sentence-018

Changed: `risk`

Input:

```text
收集用品，以防家中停电几天之需。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全指引；依輸入本身分類，未參考 converter output。

Gemini reason: 完整的祈使句，包含目的状语从句，可以独立理解。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 34. ready-gov-winter-weather-zh-hans-v1/sentence-019

Changed: `risk`

Input:

```text
切记每个人的特定需求，包括药物。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全指引；依輸入本身分類，未參考 converter output。

Gemini reason: 完整的祈使句，可以独立理解。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 35. ready-gov-winter-weather-zh-hans-v1/sentence-022

Changed: `eligible, domain, risk`

Input:

```text
在家中、单位和汽车防备冬季天气。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | no | null | null | medium | fragment, unnatural_phrasing |

Codex reason: 完整且可獨立判讀的公共安全指引；依輸入本身分類，未參考 converter output。

Gemini reason: 清单式祈使句，结构更接近标题或列表项，非完整叙述句。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 36. ready-gov-winter-weather-zh-hans-v1/sentence-023

Changed: `risk`

Input:

```text
在车中准备一个应急用品包。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全指引；依輸入本身分類，未參考 converter output。

Gemini reason: 完整的祈使句，可以独立理解。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 37. ready-gov-winter-weather-zh-hans-v1/sentence-026

Changed: `eligible, domain, risk`

Input:

```text
避免一氧化碳中毒。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | no | null | null | high | fragment |

Codex reason: 完整且可獨立判讀的公共安全指引；依輸入本身分類，未參考 converter output。

Gemini reason: 指令性片段，更像是小标题，非完整句子。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 38. ready-gov-winter-weather-zh-hans-v1/sentence-027

Changed: `risk`

Input:

```text
仅在室外且远离窗户的地方使用发电机和烤架。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全指引；依輸入本身分類，未參考 converter output。

Gemini reason: 完整祈使句。‘发电机’中的‘发’ (fā) vs ‘髮’ (fà) 和 ‘机’ (jī) vs ‘幾’ (jǐ) 是常见的转换测试点。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 39. ready-gov-winter-weather-zh-hans-v1/sentence-028

Changed: `risk`

Input:

```text
切勿使用燃气炉灶或烤箱为住房供暖。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全指引；依輸入本身分類，未參考 converter output。

Gemini reason: 完整的否定祈使句，安全警告。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 40. ready-gov-winter-weather-zh-hans-v1/sentence-029

Changed: `risk`

Input:

```text
切勿使用燃气炉或烤箱在家中取暖。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | duplicate_meaning |

Codex reason: 完整且可獨立判讀的公共安全指引；依輸入本身分類，未參考 converter output。

Gemini reason: 与上一句意思几乎完全相同，只是措辞略有不同。可作为一致性测试。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 41. ready-gov-winter-weather-zh-hans-v1/sentence-031

Changed: `risk`

Input:

```text
尽可能远离道路。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全指引；依輸入本身分類，未參考 converter output。

Gemini reason: 完整祈使句，安全建议。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 42. ready-gov-winter-weather-zh-hans-v1/sentence-032

Changed: `risk`

Input:

```text
如被困在车内，应待在车内。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全指引；依輸入本身分類，未參考 converter output。

Gemini reason: 完整的条件句。‘车’是简繁转换的经典案例。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 43. ready-gov-winter-weather-zh-hans-v1/sentence-033

Changed: `eligible, domain, risk`

Input:

```text
限制在室外的时间。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | no | null | null | high | fragment |

Codex reason: 完整且可獨立判讀的公共安全指引；依輸入本身分類，未參考 converter output。

Gemini reason: 指令性片段，清单体，非完整叙述句。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 44. ready-gov-winter-weather-zh-hans-v1/sentence-034

Changed: `risk`

Input:

```text
如需外出，应多穿几层保暖的衣服。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全指引；依輸入本身分類，未參考 converter output。

Gemini reason: 完整的条件句。‘几’ vs ‘幾’ 是简繁转换测试点。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 45. ready-gov-winter-weather-zh-hans-v1/sentence-035

Changed: `risk`

Input:

```text
注意是否有冻伤和体温过低的迹象。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全指引；依輸入本身分類，未參考 converter output。

Gemini reason: 完整祈使句，包含医学术语。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 46. ready-gov-winter-weather-zh-hans-v1/sentence-037

Changed: `risk`

Input:

```text
冻伤会导致面部、手指和脚趾周围失去感觉和颜色。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全指引；依輸入本身分類，未參考 converter output。

Gemini reason: 完整句子，描述医疗症状。‘面’(脸/面条) 和 ‘颜色’ vs ‘颜料’ 是潜在的过度转换风险点。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 47. ready-gov-winter-weather-zh-hans-v1/sentence-040

Changed: `risk`

Input:

```text
不要按摩或使用加热垫。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全指引；依輸入本身分類，未參考 converter output。

Gemini reason: 完整祈使句，医疗建议。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 48. ready-gov-winter-weather-zh-hans-v1/sentence-045

Changed: `risk`

Input:

```text
保持干燥并用温暖的毯子包裹，包括头部和颈部。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全指引；依輸入本身分類，未參考 converter output。

Gemini reason: 完整祈使句。‘干燥’ 中的 ‘干’ (gān) vs ‘幹’ (gàn) 是一个典型的过度转换保护案例。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 49. ready-gov-winter-weather-zh-hans-v1/sentence-046

Changed: `risk`

Input:

```text
停电时，发电机会很有帮助。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全指引；依輸入本身分類，未參考 converter output。

Gemini reason: 完整句子。‘发电机’ 是一个好的简繁转换测试词。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 50. ready-gov-winter-weather-zh-hans-v1/sentence-047

Changed: `eligible, domain, risk`

Input:

```text
了解如何安全使用它们以防止一氧化碳(CO)中毒和其他危害非常重要。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 來源句為殘句、錯譯病句、單位不明或依賴前文，無法作為可靠且可獨立裁決的 benchmark 輸入。

Gemini reason: 完整句子，包含英文缩写，属于混合脚本。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 51. ready-gov-winter-weather-zh-hans-v1/sentence-049

Changed: `eligible, domain, risk`

Input:

```text
在您家的每一层都安装工作的一氧化碳探测器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | yes | high_stakes | over_conversion_guard | medium | unnatural_phrasing |

Codex reason: 來源句為殘句、錯譯病句、單位不明或依賴前文，無法作為可靠且可獨立裁決的 benchmark 輸入。

Gemini reason: 句子语法完整但“安装工作的一氧化碳探测器”的表述稍显生硬，‘工作’在此处意为‘正常运作的’，可能构成转换挑战。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 52. ready-gov-winter-weather-zh-hans-v1/sentence-052

Changed: `risk`

Input:

```text
触摸潮湿的发电机或与之相连的设备可能会导致触电。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全指引；依輸入本身分類，未參考 converter output。

Gemini reason: 完整句子，安全警告。包含‘发电机’、‘设备’等多个简繁转换测试点。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 53. ready-gov-winter-weather-zh-hans-v1/sentence-054

Changed: `risk`

Input:

```text
加油前让发电机冷却。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全指引；依輸入本身分類，未參考 converter output。

Gemini reason: 完整祈使句。包含‘发电机’。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`
