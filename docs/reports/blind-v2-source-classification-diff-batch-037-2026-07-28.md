<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 037 (2026-07-28)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `6a885b223c090f22a6c7100c3d8609cde9daf43b1c65cc5431aac0a68a3c3d16`
Cases: 96
Exact Codex/Gemini classifications: 31
Maintainer review queue: 65

Field differences:

- Eligibility: 6
- Script: 6
- Domain: 23
- Risk: 53

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

The maintainer resolved all 65 advisory disagreements and batch-confirmed the 31 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. census-newsroom-zh-hans-v1/page-01-sentence-021

Changed: `script`

Input:

```text
在线回答语言选项的成效。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | no | null | null | high | - |

Codex reason: 來源句不完整、依賴前文或語意異常，無法作為可獨立裁決的 benchmark 輸入。

Gemini reason: 內容不完整，只是一個短語，無法構成獨立判斷的句子，更像是標題或列表項。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 02. census-newsroom-zh-hans-v1/page-01-sentence-032

Changed: `risk`

Input:

```text
这些估算将在 2021 年和 2022 年出台。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；可檢驗正式用語與專名保護。

Gemini reason: 包含『這些』、『估算』、『將』、『出台』等詞，其中『估算』在臺灣多用『估計』，有評測價值。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 03. census-newsroom-zh-hans-v1/page-02-sentence-017

Changed: `risk`

Input:

```text
但是，如果他们住在校外的私人住宅或公寓里，即使他们应该使用校外地址自行回答人口普查，即使当前暂时居住别处也应如此。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；可檢驗正式用語與專名保護。

Gemini reason: 句子結構較複雜，但用詞直接，可作為基準線測試，確保在複雜句中基本字詞的正確轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 04. census-newsroom-zh-hans-v1/page-06-sentence-007

Changed: `risk`

Input:

```text
人口普查员将更新人口普查局的地址名单，其包括部分 Maine 北部地区和 Alaska 东南部的偏远地区，也将与住户进行 2020 年人口普查访谈。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；可檢驗正式用語與專名保護。

Gemini reason: 包含英文地名（Maine, Alaska），可測試混合語言內容的處理能力。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 05. census-newsroom-zh-hans-v1/page-07-sentence-004

Changed: `risk`

Input:

```text
现在回答将使人口普查员拜访住宅亲自收集答案的必要性降到最低。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；可檢驗正式用語與專名保護。

Gemini reason: 標準陳述句，詞彙簡單直接，適合做為基礎正確性的基準線測試。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 06. census-newsroom-zh-hans-v1/page-08-sentence-011

Changed: `eligible, domain, risk`

Input:

```text
“人口统计分析使我们能够利用现有的数据，例如当前和历史管理记录及问卷调查数据，来估计人口的规模，”人口司人口分析资深技术专家 Eric Jensen 说：“自 1960 年人口普查以来，我们一直在进行人口统计分析。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | unmatched_quote |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 來源句不完整、依賴前文或語意異常，無法作為可獨立裁決的 benchmark 輸入。

Gemini reason: 包含引述、人名及『統計』、『數據』、『問卷』、『調查』、『規模』等豐富的待轉換詞彙。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 07. census-newsroom-zh-hans-v1/page-08-sentence-012

Changed: `risk`

Input:

```text
随着时间的推移，我们的估计不仅得益于方法的改进，而且得益于现有管理记录的改进。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；可檢驗正式用語與專名保護。

Gemini reason: 包含『隨著』、『估計』、『得益於』、『改進』等詞，適合測試常用動詞與片語的轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 08. massive-1-0-zh-cn-v1/10643

Changed: `risk`

Input:

```text
清单上的最后一项漏了
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 日常生活用語，轉換風險低。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 09. massive-1-0-zh-cn-v1/10647

Changed: `eligible, domain, risk`

Input:

```text
把清洁小狗放在清洁清单最上面
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 來源句不完整、依賴前文或語意異常，無法作為可獨立裁決的 benchmark 輸入。

Gemini reason: 智慧助理指令，轉換風險低。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 10. massive-1-0-zh-cn-v1/11819

Changed: `risk`

Input:

```text
帮我找一个卖啤酒的店
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 日常生活用語，轉換風險低。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 11. massive-1-0-zh-cn-v1/12507

Changed: `risk`

Input:

```text
我要一张去俄勒冈的火车票
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 旅遊相關請求，專有名詞轉換直接。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 12. massive-1-0-zh-cn-v1/13515

Changed: `risk`

Input:

```text
一个地球日是多长时间
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 一般知識性問題，轉換風險低。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 13. massive-1-0-zh-cn-v1/13538

Changed: `risk`

Input:

```text
你能描述一下她在那部电影里的穿着吗
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 日常對話，轉換風險低。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 14. massive-1-0-zh-cn-v1/142

Changed: `risk`

Input:

```text
那是一首好歌
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 簡繁同形，可作為過度轉換的防護案例。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 15. massive-1-0-zh-cn-v1/14485

Changed: `risk`

Input:

```text
一美元在加拿大是多少
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 貨幣與國家名稱，轉換直接。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 16. massive-1-0-zh-cn-v1/14861

Changed: `risk`

Input:

```text
如果我有五美元那澳元是多少
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 貨幣名稱，轉換直接。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 17. massive-1-0-zh-cn-v1/15711

Changed: `eligible, domain, risk`

Input:

```text
消费者发微博
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 來源句不完整、依賴前文或語意異常，無法作為可獨立裁決的 benchmark 輸入。

Gemini reason: 「发微博」是中國大陸用法，臺灣多用「發文」或「發微博」，動詞「发」是重點。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 18. massive-1-0-zh-cn-v1/15989

Changed: `domain`

Input:

```text
这个人发过任何电子邮件吗
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 動詞「发」在此意為「寄送」，與「发微博」的「發表」不同，可測試情境區分。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 19. massive-1-0-zh-cn-v1/16155

Changed: `risk`

Input:

```text
李雷的地址是什么
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 日常問題，轉換風險低。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 20. massive-1-0-zh-cn-v1/16944

Changed: `risk`

Input:

```text
给奶奶发封电子邮件说我们星期六来拜访到时候见
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 日常指令，句子雖長但用詞標準，風險低。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 21. massive-1-0-zh-cn-v1/2319

Changed: `domain, risk`

Input:

```text
关闭电源灯
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | ui_product | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 裝置操作指令，用詞標準。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 22. massive-1-0-zh-cn-v1/3559

Changed: `risk`

Input:

```text
切换到我的运动歌单
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 音樂播放指令，用詞「歌单」兩岸通用，風險低。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 23. massive-1-0-zh-cn-v1/6268

Changed: `domain, risk`

Input:

```text
如果为了救三个人你必须杀一个人你会这样做吗如果会告诉我为什么
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 哲學性問題，類似 LLM 提問，用字直接，風險低。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 24. massive-1-0-zh-cn-v1/6334

Changed: `script, risk`

Input:

```text
olly 我今天度过了最糟糕的一天
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 日常感嘆，轉換風險低。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 25. massive-1-0-zh-cn-v1/6921

Changed: `risk`

Input:

```text
设定一个通知三月十一号与罗德里格斯先生有个面试
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 包含外文譯名「罗德里格斯」，但整體用詞標準，可作基準案例。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 26. massive-1-0-zh-cn-v1/7986

Changed: `risk`

Input:

```text
你能删除这个晚餐聚会吗
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 日常指令，轉換風險低。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 27. massive-1-0-zh-cn-v1/8090

Changed: `risk`

Input:

```text
我的星期六预约的时间是几点
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 日常問題，用詞「预约」兩岸通用，風險低。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 28. massive-1-0-zh-cn-v1/8847

Changed: `risk`

Input:

```text
提醒我带上我的雨衣因为会下雨
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 包含多義字「会」，可測試轉換的準確性，避免過度轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 29. massive-1-0-zh-cn-v1/8883

Changed: `risk`

Input:

```text
给我的生日设置一个提示
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 日常指令，用詞標準。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 30. massive-1-0-zh-cn-v1/9557

Changed: `risk`

Input:

```text
目前电视上观众选择最多的节目是什么
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 媒體相關問題，用詞「电视」、「节目」為兩岸通用，風險低。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 31. ready-gov-home-fires-zh-hans-v1/sentence-014

Changed: `risk`

Input:

```text
烹饪时切勿停用烟雾报警器，因为可能致命。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 明確的安全警告，包含「煙霧報警器」等關鍵詞彙。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 32. ready-gov-home-fires-zh-hans-v1/sentence-032

Changed: `risk`

Input:

```text
开门前先摸门把手和门。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 逃生指示。可測試「門把手」在台灣是否應對應為「門把」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 33. ready-gov-home-fires-zh-hans-v1/sentence-033

Changed: `eligible, domain, risk`

Input:

```text
如果其中一个很热，或门周围有烟出来，不要开门，用第二条出路。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 來源句不完整、依賴前文或語意異常，無法作為可獨立裁決的 benchmark 輸入。

Gemini reason: 條件式逃生指令，句子結構完整，包含多個基本字轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 34. ready-gov-home-fires-zh-hans-v1/sentence-044

Changed: `risk`

Input:

```text
如需临时住所、食物和药品，联系当地救灾服务机构（如红十字会）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 災後求助資訊，可測試「聯繫」、「救災服務機構」等正式用詞。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 35. ready-gov-home-fires-zh-hans-v1/sentence-067

Changed: `domain, risk`

Input:

```text
每天给圣诞树浇水，不要让它干涸。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 居家生活用語，其中「干涸」的「干」字是很好的過度轉換測試點。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 36. ready-gov-home-fires-zh-hans-v1/sentence-068

Changed: `domain, risk`

Input:

```text
干燥的树更易燃。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 補充說明句，「干燥」的「干」字同樣可用於測試過度轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 37. ready-gov-home-fires-zh-hans-v1/sentence-083

Changed: `eligible, domain, risk`

Input:

```text
这会增加火灾和烧伤的风险，并可能损坏电器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 來源句不完整、依賴前文或語意異常，無法作為可獨立裁決的 benchmark 輸入。

Gemini reason: 風險說明句，包含「燒傷」、「風險」、「損壞電器」等標準詞彙。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 38. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-006

Changed: `domain`

Input:

```text
土地利用分区、专业检查和适当的设计可以减少许多滑坡问题，但疏散通常是保护生命免受泥石流或其他快速移动的滑坡伤害的唯一方法。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 政府公告/新聞風格，涉及「分區、專業、滑坡、泥石流」等具有兩岸差異的詞彙。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 39. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-008

Changed: `domain, risk`

Input:

```text
一些缓慢移动的山体滑坡以蜗牛的速度移动，停止和开始，并且每年前进不超过三英尺。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 標準科普句子，測試基本轉換的準確性。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 40. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-010

Changed: `domain, risk`

Input:

```text
制定一个计划，包括您的宠物，以便您和您的家人知道在发生山体滑坡时该做什么以及该去哪里。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 日常指令語氣，測試常用詞「計畫」的轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 41. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-013

Changed: `domain`

Input:

```text
如果您被告知要撤离，或者您觉得留在家里不安全，请离开。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 簡單直接的指令，適合做為基本轉換的基準案例。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 42. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-030

Changed: `eligible, domain, risk`

Input:

```text
门或窗第一次粘住或卡住。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 來源句不完整、依賴前文或語意異常，無法作為可獨立裁決的 benchmark 輸入。

Gemini reason: 清單項目格式，可獨立判斷。測試「門、粘、卡」等單字轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 43. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-033

Changed: `domain, risk`

Input:

```text
地面或街道或车道等铺砌区域出现缓慢发展、扩大的裂缝。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 描述性清單項目，包含「車道、發展、裂縫」等，可測試轉換的準確性。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 44. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-042

Changed: `domain`

Input:

```text
在可能导致山体滑坡的暴风雨中保持警惕和清醒。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 防災指令，測試「導致、警惕」等基本詞彙。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 45. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-048

Changed: `domain`

Input:

```text
危险时避开河谷和低洼地带。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 簡潔的避難指令，為良好的基本測試案例。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 46. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-054

Changed: `domain`

Input:

```text
在不进入直接滑道区域的情况下，检查滑道附近是否有受伤和被困人员。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 急救指令，測試「滑道、區域、人員」等詞語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 47. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-056

Changed: `domain`

Input:

```text
向有关当局报告断裂的公用事业线路以及损坏的公路和铁路。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 正式語氣的指令，測試「有關當局、公用事業、線路」等偏正式或具兩岸差異的用詞。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 48. zhtw-project-it-llm-social-guard-v1/it-001

Changed: `risk`

Input:

```text
服务器返回 HTTP 429 时，客户端必须读取 Retry-After 标头。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 IT 操作敘述；程式識別碼、路徑或協定名稱必須保持不變。

Gemini reason: 測試 IT 領域「伺服器」、「用戶端」、「標頭」的轉換，並保護 ASCII 字串。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 49. zhtw-project-it-llm-social-guard-v1/it-010

Changed: `risk`

Input:

```text
CI 工作流使用 ubuntu-24.04 作为固定运行环境。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 IT 操作敘述；程式識別碼、路徑或協定名稱必須保持不變。

Gemini reason: 測試 CI/CD 術語「工作流程」、「作為」、「執行環境」的轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 50. zhtw-project-it-llm-social-guard-v1/it-019

Changed: `risk`

Input:

```text
执行 SELECT ... FOR UPDATE 时要留意锁等待时间。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 IT 操作敘述；程式識別碼、路徑或協定名稱必須保持不變。

Gemini reason: 測試資料庫術語「執行」、「鎖」的基礎轉換，並保護 SQL 關鍵字。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 51. zhtw-project-it-llm-social-guard-v1/it-028

Changed: `risk`

Input:

```text
JSON Schema 使用 additionalProperties: false 限制未知字段。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 IT 操作敘述；程式識別碼、路徑或協定名稱必須保持不變。

Gemini reason: 測試關鍵術語「欄位」的轉換，並保護 `JSON Schema` 關鍵字 `additionalProperties: false`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 52. zhtw-project-it-llm-social-guard-v1/it-029

Changed: `risk`

Input:

```text
S3 对象键 reports/2026/Q3/summary.csv 区分大小写。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 IT 操作敘述；程式識別碼、路徑或協定名稱必須保持不變。

Gemini reason: 測試 S3 術語「物件金鑰」的轉換，並保護 key path `reports/2026/Q3/summary.csv`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 53. zhtw-project-it-llm-social-guard-v1/it-038

Changed: `risk`

Input:

```text
事件载荷的 schema_version 当前固定为 2.1。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 IT 操作敘述；程式識別碼、路徑或協定名稱必須保持不變。

Gemini reason: 測試技術術語「酬載」(payload) 的轉換，並保護 `schema_version`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 54. zhtw-project-it-llm-social-guard-v1/llm-002

Changed: `risk`

Input:

```text
检索器只返回相关性最高的五段内容，再交给模型整理。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整的 LLM 工作流程敘述；可檢驗技術詞彙的臺灣慣用表達。

Gemini reason: 測試 LLM 領域中「檢索器」、「相關性」、「模型」等基礎詞彙。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 55. zhtw-project-it-llm-social-guard-v1/llm-010

Changed: `risk`

Input:

```text
模型上线前要完成离线评估和小流量灰度测试。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整的 LLM 工作流程敘述；可檢驗技術詞彙的臺灣慣用表達。

Gemini reason: 測試 MLOps 術語「上線」、「離線評估」、「灰度測試」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 56. zhtw-project-it-llm-social-guard-v1/llm-016

Changed: `risk`

Input:

```text
如果输入包含多个任务，助手应先确认执行顺序。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整的 LLM 工作流程敘述；可檢驗技術詞彙的臺灣慣用表達。

Gemini reason: 測試 AI 助理互動中的常用詞「輸入」、「任務」、「助理」、「確認」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 57. zhtw-project-it-llm-social-guard-v1/llm-022

Changed: `risk`

Input:

```text
请把会议记录整理成行动项目，并标出负责人。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整的 LLM 工作流程敘述；可檢驗技術詞彙的臺灣慣用表達。

Gemini reason: 測試會議摘要任務中的常用詞彙轉換，如「行動項目」、「負責人」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 58. zhtw-project-it-llm-social-guard-v1/llm-024

Changed: `risk`

Input:

```text
多轮对话超过保存范围后，较早的消息会被移除。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整的 LLM 工作流程敘述；可檢驗技術詞彙的臺灣慣用表達。

Gemini reason: 測試聊天機器人術語「多輪對話」的轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 59. zhtw-project-it-llm-social-guard-v1/llm-028

Changed: `risk`

Input:

```text
编辑人员修正实体名称后，系统会重新生成摘要。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整的 LLM 工作流程敘述；可檢驗技術詞彙的臺灣慣用表達。

Gemini reason: 測試 NLP 術語「實體名稱」及「摘要」的轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 60. zhtw-project-it-llm-social-guard-v1/social-002

Changed: `script`

Input:

```text
周末想去看《海角七号》，先确认光点华山的场次。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 完整的日常敘述；品牌、作品、人名或識別碼必須保持不變。

Gemini reason: 保護電影名稱《海角七号》與地名「光點華山」等專有名詞不被錯誤轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 61. zhtw-project-it-llm-social-guard-v1/social-004

Changed: `domain`

Input:

```text
这张发票的统一编号是 AB-20260728，请不要改动。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整的日常敘述；品牌、作品、人名或識別碼必須保持不變。

Gemini reason: 保護統一編號 `AB-20260728` 不被轉換，並測試「發票」、「改動」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 62. zhtw-project-it-llm-social-guard-v1/social-006

Changed: `script`

Input:

```text
请把照片传到群组「暑假旅行 2026」，不要传错地方。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 完整的日常敘述；品牌、作品、人名或識別碼必須保持不變。

Gemini reason: 保護特定群組名稱「暑假旅行 2026」不被改動。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 63. zhtw-project-it-llm-social-guard-v1/social-009

Changed: `script, risk`

Input:

```text
捷运红线在中山站临时停靠较久，请预留时间。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整的日常敘述；品牌、作品、人名或識別碼必須保持不變。

Gemini reason: 測試地名與路線名稱（如「捷運紅線」）的正確轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 64. zhtw-project-it-llm-social-guard-v1/social-011

Changed: `script, domain, risk`

Input:

```text
陈医师提醒我按药袋上的指示服用，不要自行加量。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整的日常敘述；品牌、作品、人名或識別碼必須保持不變。

Gemini reason: 醫療情境，測試常用姓氏「陳」的轉換，屬於高風險基準測試。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 65. zhtw-project-it-llm-social-guard-v1/social-026

Changed: `domain`

Input:

```text
请把文件放进 Google Drive 的 Shared with me 文件夹。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | ui_product | over_conversion_guard | high | - |

Codex reason: 完整的日常敘述；品牌、作品、人名或識別碼必須保持不變。

Gemini reason: 保護產品名稱 `Google Drive` 與 UI 字串 `Shared with me`，並測試「檔案」、「資料夾」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`
