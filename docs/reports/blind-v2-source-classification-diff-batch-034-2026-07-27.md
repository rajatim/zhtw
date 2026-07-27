<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 034 (2026-07-27)

Status: advisory only; maintainer decisions pending

Packet SHA-256: `2404d887831fc173f37f530c566ec66a89df27930cee1484b2b09a0d3a4f611b`
Cases: 96
Exact Codex/Gemini classifications: 39
Maintainer review queue: 57

Field differences:

- Eligibility: 2
- Script: 0
- Domain: 45
- Risk: 31

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 3 tool calls and 0 API errors.

Neither advisory is auto-preferred. Codex must synthesize the differences before maintainer confirmation; no classification in this report has been written into the candidate pool.

## Review Queue

### 01. massive-1-0-zh-cn-v1/10751

Changed: `domain, risk`

Input:

```text
谷歌翻译
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整或可獨立判讀的語音助理請求；用於檢驗日常用語、產品實體與區域詞差異。

Gemini reason: 「谷歌」是中國大陸用法，台灣稱「Google」。術語「翻譯」需要轉換。屬於專有名詞保護。

Maintainer decision: `pending`

### 02. massive-1-0-zh-cn-v1/12480

Changed: `risk`

Input:

```text
帮我现在找辆去机场的滴滴顺风车
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 完整或可獨立判讀的語音助理請求；用於檢驗日常用語、產品實體與區域詞差異。

Gemini reason: 「滴滴順風車」是中國大陸的特定服務名稱，在台灣並不存在。屬於專有名詞，應予以保護，不應轉換。

Maintainer decision: `pending`

### 03. massive-1-0-zh-cn-v1/1284

Changed: `risk`

Input:

```text
把这个时间换成中国标准时间
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 完整或可獨立判讀的語音助理請求；用於檢驗日常用語、產品實體與區域詞差異。

Gemini reason: 「中國標準時間」是專有名稱，應保留其指涉的特定時區，僅做字元轉換。

Maintainer decision: `pending`

### 04. massive-1-0-zh-cn-v1/15170

Changed: `domain`

Input:

```text
人民日报有在微博发了什么新帖吗
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整或可獨立判讀的語音助理請求；用於檢驗日常用語、產品實體與區域詞差異。

Gemini reason: 「人民日報」和「微博」是專有名詞，應予以保護。

Maintainer decision: `pending`

### 05. massive-1-0-zh-cn-v1/16510

Changed: `domain`

Input:

```text
将这个回复发送到收到的电子邮件
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整或可獨立判讀的語音助理請求；用於檢驗日常用語、產品實體與區域詞差異。

Gemini reason: 語法和用詞帶有翻譯腔。「回覆到收到的電子郵件」不自然，台灣 UI 會說「回覆此郵件」。涉及語氣和習慣用語差異。

Maintainer decision: `pending`

### 06. massive-1-0-zh-cn-v1/3447

Changed: `eligible, domain, risk`

Input:

```text
周六会来雨吗
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 來源句含明顯機器翻譯錯置或不可解片段，不適合作為可裁決 benchmark 輸入。

Gemini reason: 「會來雨嗎」語法不自然，台灣說「會下雨嗎」。涉及動詞搭配和習慣用法。

Maintainer decision: `pending`

### 07. massive-1-0-zh-cn-v1/3488

Changed: `domain`

Input:

```text
开始播放我的歌曲列表
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整或可獨立判讀的語音助理請求；用於檢驗日常用語、產品實體與區域詞差異。

Gemini reason: 「歌曲列表」在台灣通常稱為「播放清單」。涉及術語轉換。

Maintainer decision: `pending`

### 08. massive-1-0-zh-cn-v1/4464

Changed: `domain`

Input:

```text
在播放列表中保存我的歌曲偏好
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整或可獨立判讀的語音助理請求；用於檢驗日常用語、產品實體與區域詞差異。

Gemini reason: 「播放列表」在台灣通常稱為「播放清單」。

Maintainer decision: `pending`

### 09. massive-1-0-zh-cn-v1/6749

Changed: `domain`

Input:

```text
朗读最近的提醒
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整或可獨立判讀的語音助理請求；用於檢驗日常用語、產品實體與區域詞差異。

Gemini reason: 標準簡轉繁句。

Maintainer decision: `pending`

### 10. massive-1-0-zh-cn-v1/705

Changed: `risk`

Input:

```text
告诉我些好玩的事
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | medium | - |

Codex reason: 完整或可獨立判讀的語音助理請求；用於檢驗日常用語、產品實體與區域詞差異。

Gemini reason: 「告訴我些」的用法較偏口語，台灣書面或較正式語氣會用「告訴我一些」。

Maintainer decision: `pending`

### 11. massive-1-0-zh-cn-v1/7772

Changed: `risk`

Input:

```text
告诉我这周的会议
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整或可獨立判讀的語音助理請求；用於檢驗日常用語、產品實體與區域詞差異。

Gemini reason: 「這周」是中國大陸用法，台灣慣用「這週」或「這個星期」。

Maintainer decision: `pending`

### 12. massive-1-0-zh-cn-v1/8229

Changed: `domain, risk`

Input:

```text
我的工作项目洽谈的地点在哪里
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整或可獨立判讀的語音助理請求；用於檢驗日常用語、產品實體與區域詞差異。

Gemini reason: 「項目」是中國大陸用語，台灣稱「專案」。涉及商業術語轉換。

Maintainer decision: `pending`

### 13. massive-1-0-zh-cn-v1/8808

Changed: `risk`

Input:

```text
周一有什么会议需要提醒我吗
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整或可獨立判讀的語音助理請求；用於檢驗日常用語、產品實體與區域詞差異。

Gemini reason: 「週一」在台灣雖可用，但「星期一」更普遍。

Maintainer decision: `pending`

### 14. massive-1-0-zh-cn-v1/9192

Changed: `domain`

Input:

```text
将此日期设置为重复提醒
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | medium | - |

Codex reason: 完整或可獨立判讀的語音助理請求；用於檢驗日常用語、產品實體與區域詞差異。

Gemini reason: 用語稍嫌書面，「設定為重複提醒」或「設定為定期提醒」在台灣 UI 中更常見。

Maintainer decision: `pending`

### 15. massive-1-0-zh-cn-v1/9939

Changed: `eligible, domain, risk`

Input:

```text
油煎炸麦薯条温度多少
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | yes | social_daily | candidate_gap | medium | unusual_phrasing |

Codex reason: 來源句含明顯機器翻譯錯置或不可解片段，不適合作為可裁決 benchmark 輸入。

Gemini reason: 「麥薯條」不是標準詞彙，可能是「炸薯條」的誤植或特殊菜餚。「油煎炸」說法冗贅，通常只用「油炸」。

Maintainer decision: `pending`

### 16. ready-gov-drought-zh-hans-v1/sentence-004

Changed: `domain, risk`

Input:

```text
在日常生活中习惯节水。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 用語差異：「節水」在台灣更常用「省水」。

Maintainer decision: `pending`

### 17. ready-gov-drought-zh-hans-v1/sentence-007

Changed: `domain, risk`

Input:

```text
每秒漏一滴水，每年就会浪费 2,700 加仑水。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 標準簡轉繁，「加侖」為通用單位詞。

Maintainer decision: `pending`

### 18. ready-gov-drought-zh-hans-v1/sentence-008

Changed: `domain, risk`

Input:

```text
检查所有管道是否漏水，请管道工修理任何漏水的管道。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 用語差異：「管道工」在台灣多稱「水管工人」或「水電工」。

Maintainer decision: `pending`

### 19. ready-gov-drought-zh-hans-v1/sentence-009

Changed: `domain, risk`

Input:

```text
安装带限流器的起泡器，改装家中所有水龙头。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 「起泡器」、「限流器」為技術名詞，應可直接轉換，但需確認台灣是否有更常用術語。

Maintainer decision: `pending`

### 20. ready-gov-drought-zh-hans-v1/sentence-010

Changed: `domain`

Input:

```text
在水槽上安装即时热水器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 用語差異：「即時熱水器」在台灣多稱「瞬熱式」或「即熱式」電熱水器。

Maintainer decision: `pending`

### 21. ready-gov-drought-zh-hans-v1/sentence-015

Changed: `domain`

Input:

```text
考虑购买小容量马桶，用水量不到旧型号的一半。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 用語差異：「小容量馬桶」在台灣通常以功能性稱呼為「省水馬桶」。

Maintainer decision: `pending`

### 22. ready-gov-drought-zh-hans-v1/sentence-018

Changed: `domain`

Input:

```text
确保不会干扰马桶操作部件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 標準簡轉繁。

Maintainer decision: `pending`

### 23. ready-gov-drought-zh-hans-v1/sentence-019

Changed: `domain`

Input:

```text
使用超低流量的淋浴喷头。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 用語差異：「淋浴噴頭」在台灣的通用詞是「蓮蓬頭」。

Maintainer decision: `pending`

### 24. ready-gov-drought-zh-hans-v1/sentence-023

Changed: `domain`

Input:

```text
按用水量分开种。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 標準簡轉繁。

Maintainer decision: `pending`

### 25. ready-gov-drought-zh-hans-v1/sentence-026

Changed: `domain, risk`

Input:

```text
联系当地供水商获取信息和协助。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 用語差異：「聯繫」在台灣多用「聯絡」；「供水商」多為「自來水公司」。

Maintainer decision: `pending`

### 26. ready-gov-drought-zh-hans-v1/sentence-027

Changed: `domain, risk`

Input:

```text
放置洒水器时，要让水洒落在草坪和灌木上，而非铺砌的地方。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 標準簡轉繁。

Maintainer decision: `pending`

### 27. ready-gov-drought-zh-hans-v1/sentence-028

Changed: `domain, risk`

Input:

```text
修好喷出细雾的洒水器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 標準簡轉繁。

Maintainer decision: `pending`

### 28. ready-gov-drought-zh-hans-v1/sentence-034

Changed: `domain`

Input:

```text
草坪不要过度施肥，施肥越多，用水越多。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 標準簡轉繁。

Maintainer decision: `pending`

### 29. ready-gov-drought-zh-hans-v1/sentence-036

Changed: `domain`

Input:

```text
为树木、灌木和花卉选择节水灌溉系统（如滴灌）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 用語差異：「節水」在台灣更常用「省水」。

Maintainer decision: `pending`

### 30. ready-gov-drought-zh-hans-v1/sentence-038

Changed: `domain, risk`

Input:

```text
在树木和植物周围使用护根物，不但能保留土壤中的水分，还有助于控制与植物争水的杂草。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 「護根物」為園藝術語，可直接轉換。

Maintainer decision: `pending`

### 31. ready-gov-drought-zh-hans-v1/sentence-040

Changed: `domain, risk`

Input:

```text
这些设备能根据土壤湿度、雨水、风力及蒸发和蒸腾速率自动调整浇水时间和频率。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 句子含科學術語，可標準簡轉繁。

Maintainer decision: `pending`

### 32. ready-gov-drought-zh-hans-v1/sentence-041

Changed: `domain`

Input:

```text
询问当地水务机构，看看购买智能控制器是否有折扣。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 用語差異：「水務機構」非台灣常用詞，通常指「自來水公司」或「水利署」。

Maintainer decision: `pending`

### 33. ready-gov-drought-zh-hans-v1/sentence-042

Changed: `domain`

Input:

```text
安装泳池节水过滤器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 用語差異：「節水」在台灣更常用「省水」。

Maintainer decision: `pending`

### 34. ready-gov-drought-zh-hans-v1/sentence-045

Changed: `domain, risk`

Input:

```text
在干旱期间，务必遵守州府和地方的用水限制。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 「州府」一詞適用於特定國家政體，非用語轉換問題。

Maintainer decision: `pending`

### 35. ready-gov-drought-zh-hans-v1/sentence-046

Changed: `domain`

Input:

```text
联系州府或当地政府，了解最新信息和建议。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 用語差異：「聯繫」在台灣多用「聯絡」。

Maintainer decision: `pending`

### 36. ready-gov-drought-zh-hans-v1/sentence-048

Changed: `domain, risk`

Input:

```text
短时间洗淋浴，而非泡澡。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 用語差異：「淋浴」雖可使用，但在台灣日常用語中「沖澡」更為普遍。

Maintainer decision: `pending`

### 37. ready-gov-drought-zh-hans-v1/sentence-051

Changed: `domain`

Input:

```text
洗衣机装满了衣服再洗，按衣服的多少设置水位。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 標準簡轉繁。

Maintainer decision: `pending`

### 38. ready-gov-drought-zh-hans-v1/sentence-053

Changed: `domain, risk`

Input:

```text
使用“轻洗”功能，减少用水量。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: UI標籤「輕洗」為特定功能名稱，可能對應台灣洗衣機的「柔洗」或「快洗」，不宜直接字面轉換。

Maintainer decision: `pending`

### 39. ready-gov-drought-zh-hans-v1/sentence-055

Changed: `domain`

Input:

```text
洗菜时用装满水的平底锅，而非水龙头流出的自来水。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 標準簡轉繁。

Maintainer decision: `pending`

### 40. ready-gov-drought-zh-hans-v1/sentence-056

Changed: `domain`

Input:

```text
等待水龙头的水变热时，不要让水流掉。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 語氣可理解，但「讓水流掉」的說法在台灣可能較少用。

Maintainer decision: `pending`

### 41. ready-gov-drought-zh-hans-v1/sentence-058

Changed: `domain`

Input:

```text
放入洗碗机前不要冲洗盘子，只需拿掉大粒的食物。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 標準簡轉繁。

Maintainer decision: `pending`

### 42. ready-gov-drought-zh-hans-v1/sentence-059

Changed: `domain`

Input:

```text
勿用流水解冻肉类或其他冷冻食品。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 標準簡轉繁。

Maintainer decision: `pending`

### 43. ready-gov-drought-zh-hans-v1/sentence-060

Changed: `domain`

Input:

```text
放在冰箱中过夜解冻，或使用微波炉的解冻设置。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 標準簡轉繁。

Maintainer decision: `pending`

### 44. ready-gov-drought-zh-hans-v1/sentence-062

Changed: `domain, risk`

Input:

```text
一年中大部分时间，草坪每周只需一英寸水。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 標準簡轉繁。

Maintainer decision: `pending`

### 45. ready-gov-drought-zh-hans-v1/sentence-063

Changed: `domain, risk`

Input:

```text
用土壤探头、铁锹或大螺丝刀检查土壤水分含量。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 用語差異：「鐵鍬」在台灣多稱「鏟子」或「圓鍬」；「螺絲刀」稱「螺絲起子」。

Maintainer decision: `pending`

### 46. ready-gov-drought-zh-hans-v1/sentence-066

Changed: `domain`

Input:

```text
如果确实需要浇水，应在温度较低的清晨或傍晚浇水。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 標準簡轉繁。

Maintainer decision: `pending`

### 47. ready-gov-drought-zh-hans-v1/sentence-073

Changed: `domain`

Input:

```text
自己洗车时，使用可将水管调至精细喷雾的开关水枪。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整或可獨立判讀的節水指令；用於檢驗高風險公共資訊中的一般字形、臺灣用語與數值保留。

Gemini reason: 用語差異：洗車用的「水槍」在台灣多稱「高壓噴槍」或描述其可調式噴頭，單稱「水槍」易誤解為玩具。

Maintainer decision: `pending`

### 48. zhtw-project-llm-social-baseline-v1/llm-001

Changed: `risk`

Input:

```text
模型根据用户上传的文件生成摘要，并标出无法确认的细节。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的 LLM 實務敘述；用於補強模型產品語彙、受保護 token 與過度轉換防禦。

Gemini reason: 涉及「用戶」、「文件」等潛在詞彙轉換。

Maintainer decision: `pending`

### 49. zhtw-project-llm-social-baseline-v1/llm-008

Changed: `domain`

Input:

```text
请保留原文中的 API 名称、版本号和代码片段。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 LLM 實務敘述；用於補強模型產品語彙、受保護 token 與過度轉換防禦。

Gemini reason: 指令本身要求保留不應轉換的內容 (API 名稱、程式碼)，屬於過度轉換防護用例。

Maintainer decision: `pending`

### 50. zhtw-project-llm-social-baseline-v1/llm-027

Changed: `risk`

Input:

```text
模型无法访问本地文件，除非用户明确上传或授权工具读取。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的 LLM 實務敘述；用於補強模型產品語彙、受保護 token 與過度轉換防禦。

Gemini reason: 涉及多個潛在詞彙轉換，如「本地文件」、「用戶」、「上傳」、「讀取」。

Maintainer decision: `pending`

### 51. zhtw-project-llm-social-baseline-v1/llm-028

Changed: `domain, risk`

Input:

```text
缓存命中时仍要检查模型版本和提示词哈希是否一致。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的 LLM 實務敘述；用於補強模型產品語彙、受保護 token 與過度轉換防禦。

Gemini reason: 涉及關鍵 IT 術語「緩存」(快取) 的詞彙轉換。

Maintainer decision: `pending`

### 52. zhtw-project-llm-social-baseline-v1/llm-034

Changed: `domain`

Input:

```text
请从日志中提取 request_id，但不要输出访问令牌。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 LLM 實務敘述；用於補強模型產品語彙、受保護 token 與過度轉換防禦。

Gemini reason: 包含應受保護不轉換的 token `request_id`。同時「訪問令牌」有詞彙轉換需求（存取權杖）。

Maintainer decision: `pending`

### 53. zhtw-project-llm-social-baseline-v1/llm-046

Changed: `risk`

Input:

```text
只有通过人工确认的样本才能写入最终评测答案。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的 LLM 實務敘述；用於補強模型產品語彙、受保護 token 與過度轉換防禦。

Gemini reason: 標準的簡轉繁描述。

Maintainer decision: `pending`

### 54. zhtw-project-llm-social-baseline-v1/social-001

Changed: `risk`

Input:

```text
我刚到车站，下一班车还要等二十分钟。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整且自然的日常社群敘述；用於補強生活用語與區域詞差異。

Gemini reason: 日常對話。「車站」在台灣語境下可能更具體化，「剛」通常會說「剛剛」。

Maintainer decision: `pending`

### 55. zhtw-project-llm-social-baseline-v1/social-017

Changed: `risk`

Input:

```text
包裹外箱有凹痕，里面的商品倒是没有损坏。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整且自然的日常社群敘述；用於補強生活用語與區域詞差異。

Gemini reason: 包含常用詞彙差異：「裡面」在台灣慣用「裡面」。

Maintainer decision: `pending`

### 56. zhtw-project-llm-social-baseline-v1/social-024

Changed: `risk`

Input:

```text
我不确定这个尺寸合不合适，先去实体店试穿。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整且自然的日常社群敘述；用於補強生活用語與區域詞差異。

Gemini reason: 「實體店」在台灣雖可理解，但「實體店面」或直接說「店面」更常用。

Maintainer decision: `pending`

### 57. zhtw-project-llm-social-baseline-v1/social-048

Changed: `risk`

Input:

```text
课程录影已经上传，缺席的人可以之后补看。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整且自然的日常社群敘述；用於補強生活用語與區域詞差異。

Gemini reason: 「課程錄影」雖可理解，但「課程影片」或「上課錄影」在台灣更自然。

Maintainer decision: `pending`
