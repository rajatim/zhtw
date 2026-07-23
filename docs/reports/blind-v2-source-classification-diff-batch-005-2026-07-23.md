<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 005 (2026-07-23)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `cd5746f6aacad45fa964dbb747e97dd1d20941598e8e59748f9478ae8691a357`
Cases: 100
Exact Codex/Gemini classifications: 35
Maintainer review queue: 65

Field differences:

- Eligibility: 4
- Script: 3
- Domain: 48
- Risk: 33

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

The maintainer resolved all 65 advisory disagreements and batch-confirmed the 35 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. massive-1-0-zh-cn-v1/10144

Changed: `risk`

Input:

```text
我要把一个冰饼冷藏多久
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | unusual_localized_wording |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 「冰餅」在臺灣較少使用，可能指冰皮月餅，需地區詞彙轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 02. massive-1-0-zh-cn-v1/10276

Changed: `risk`

Input:

```text
让我们玩吃鸡
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 含中國產品、交通、介面或生活用語，可能需要臺灣慣用詞轉換。

Gemini reason: 「吃雞」為遊戲術語（PUBG），應視為專有名詞，避免過度轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 03. massive-1-0-zh-cn-v1/10467

Changed: `domain`

Input:

```text
前往清单并且删除项目
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 語音助理指令，詞彙在臺灣通用，主要為字元轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 04. massive-1-0-zh-cn-v1/10615

Changed: `domain, risk`

Input:

```text
在明天前创建一个清单
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 「創建」在臺灣UI中較少用，通常為「建立」或「新增」，存在地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 05. massive-1-0-zh-cn-v1/10635

Changed: `domain`

Input:

```text
显示哪些清单可用
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 語音助理指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 06. massive-1-0-zh-cn-v1/10872

Changed: `domain, risk`

Input:

```text
在清单添加番茄酱
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 「番茄酱」在簡體中文可能指ketchup或tomato paste，在臺灣「番茄醬」通常僅指ketchup，存在細微語意差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 07. massive-1-0-zh-cn-v1/10952

Changed: `eligible, domain, risk`

Input:

```text
请删除踢球为标题的表单
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 輸入缺少可獨立判讀的必要內容，或本地化錯誤已改變原意，建議排除。

Gemini reason: 「踢球」是標題的一部分，應視為字面內容保留，避免轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 08. massive-1-0-zh-cn-v1/11084

Changed: `domain`

Input:

```text
在购物清单里删除牛奶
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 標準語音指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 09. massive-1-0-zh-cn-v1/11438

Changed: `domain`

Input:

```text
请跳转到播客的下一个节目
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 含中國產品、交通、介面或生活用語，可能需要臺灣慣用詞轉換。

Gemini reason: 臺灣常用「Podcast」或「單集」而非「播客」和「節目」，存在地區詞彙差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 10. massive-1-0-zh-cn-v1/118

Changed: `domain, risk`

Input:

```text
告诉我谁是这首歌的歌手
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 含人名、地名、品牌、媒體或作品名稱，主要測試專名保留。

Gemini reason: 標準語音指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 11. massive-1-0-zh-cn-v1/11816

Changed: `risk`

Input:

```text
小红作为当地游客我可以到哪购物
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 「小紅」為人名，應保持不變。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 12. massive-1-0-zh-cn-v1/1193

Changed: `script, domain`

Input:

```text
奥利我需要现在听萧敬腾的如果没有你
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 含人名、地名、品牌、媒體或作品名稱，主要測試專名保留。

Gemini reason: 包含喚醒詞「奧利」、歌手名「蕭敬騰」及歌名「如果沒有你」，皆需避免不當轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 13. massive-1-0-zh-cn-v1/12301

Changed: `risk`

Input:

```text
请帮我叫辆优步车
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 含中國產品、交通、介面或生活用語，可能需要臺灣慣用詞轉換。

Gemini reason: 「優步」為品牌名稱 (Uber)，應視為專有名詞處理。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 14. massive-1-0-zh-cn-v1/12393

Changed: `domain, risk`

Input:

```text
告诉我这个地方的方向
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | awkward_localization |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 含中國產品、交通、介面或生活用語，可能需要臺灣慣用詞轉換。

Gemini reason: 標準請求，詞彙通用，但臺灣口語可能更常用「路線」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 15. massive-1-0-zh-cn-v1/12903

Changed: `domain`

Input:

```text
告诉我火车的时间
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 標準請求，但「火車時刻」在臺灣語境下更精確。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 16. massive-1-0-zh-cn-v1/13301

Changed: `domain`

Input:

```text
帮助我入睡
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 標準請求，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 17. massive-1-0-zh-cn-v1/13540

Changed: `domain`

Input:

```text
查找救护车的定义
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 標準請求，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 18. massive-1-0-zh-cn-v1/14056

Changed: `domain, risk`

Input:

```text
美元兑欧元汇率是多少
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 臺灣口語和書面更常用「對」而非「兌」來表示匯率交換，存在用詞頻率差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 19. massive-1-0-zh-cn-v1/14337

Changed: `domain`

Input:

```text
谷歌在股市上表现得好吗
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 含人名、地名、品牌、媒體或作品名稱，主要測試專名保留。

Gemini reason: 「谷歌」為品牌名稱 (Google)，應視為專有名詞。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 20. massive-1-0-zh-cn-v1/14413

Changed: `risk`

Input:

```text
告诉我新的清洁机干得怎么样
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | awkward_localization |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 「幹得怎麼樣」是大陸口語，臺灣會說「做得怎麼樣」或「表現怎麼樣」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 21. massive-1-0-zh-cn-v1/14778

Changed: `script, domain, risk`

Input:

```text
艾利克斯以英里为单位宇宙有多大
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 含人名、地名、品牌、媒體或作品名稱，主要測試專名保留。

Gemini reason: 包含喚醒詞「艾利克斯」。語句結構在臺灣較書面，但不影響理解。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 22. massive-1-0-zh-cn-v1/15127

Changed: `domain`

Input:

```text
定义扬声器
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 含中國產品、交通、介面或生活用語，可能需要臺灣慣用詞轉換。

Gemini reason: 「揚聲器」為中國大陸用詞，臺灣慣用「喇叭」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 23. massive-1-0-zh-cn-v1/15225

Changed: `domain, risk`

Input:

```text
显示我最新的通知
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 含中國產品、交通、介面或生活用語，可能需要臺灣慣用詞轉換。

Gemini reason: 標準語音指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 24. massive-1-0-zh-cn-v1/15448

Changed: `risk`

Input:

```text
发条微博说小米的音量问题
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 含人名、地名、品牌、媒體或作品名稱，主要測試專名保留。

Gemini reason: 「發條微博」是大陸網路用語，臺灣會說「發一篇文」或「發文」。「微博」和「小米」是專名。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 25. massive-1-0-zh-cn-v1/15870

Changed: `risk`

Input:

```text
家俊的电子邮件地址是什么
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 「家俊」為人名，應保持不變。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 26. massive-1-0-zh-cn-v1/15939

Changed: `eligible, domain, risk`

Input:

```text
请将以下消息通过电子邮件发送给此联系人
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | missing_message_content |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 輸入缺少可獨立判讀的必要內容，或本地化錯誤已改變原意，建議排除。

Gemini reason: 臺灣UI中，「聯絡人」比「聯繫人」更常用，存在用詞頻率差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 27. massive-1-0-zh-cn-v1/16001

Changed: `domain`

Input:

```text
查看电子邮件
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 標準指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 28. massive-1-0-zh-cn-v1/16168

Changed: `domain`

Input:

```text
最近十五分钟内有没有收到电子邮件
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 標準指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 29. massive-1-0-zh-cn-v1/162

Changed: `risk`

Input:

```text
煮一杯咖啡给我
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 臺灣對於製作咖啡，更常用「泡」或「沖」，「煮」通常指特定烹煮方式。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 30. massive-1-0-zh-cn-v1/16436

Changed: `domain`

Input:

```text
天猫精灵找出所有新的电子邮件
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 含人名、地名、品牌、媒體或作品名稱，主要測試專名保留。

Gemini reason: 「天貓精靈」為品牌名稱，應視為專有名詞。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 31. massive-1-0-zh-cn-v1/16682

Changed: `domain, risk`

Input:

```text
给家明写封邮件内容是我有兴趣看看你出售的车可以约个时间见面吗发送
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | run_on_utterance |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 「家明」為人名，應保持不變。指令結構是典型的長語音輸入。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 32. massive-1-0-zh-cn-v1/17000

Changed: `domain`

Input:

```text
显示我最后一封电子邮件
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 標準語音指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 33. massive-1-0-zh-cn-v1/17031

Changed: `domain`

Input:

```text
我需要给我妈妈发一封电子邮件我正计划去看她问她天气如何这样我就知道如何收拾行李了
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | run_on_utterance |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 長語音指令，但詞彙和語法通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 34. massive-1-0-zh-cn-v1/17108

Changed: `domain`

Input:

```text
给我最近的电子邮件
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 標準語音指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 35. massive-1-0-zh-cn-v1/1866

Changed: `domain`

Input:

```text
现在的天气报告
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 標準指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 36. massive-1-0-zh-cn-v1/2096

Changed: `risk`

Input:

```text
全聚德烤鸭能在线订购吗
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 含中國產品、交通、介面或生活用語，可能需要臺灣慣用詞轉換。

Gemini reason: 「全聚德」為品牌名稱，應視為專有名詞。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 37. massive-1-0-zh-cn-v1/2248

Changed: `domain`

Input:

```text
周三天气完全变了吗
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 標準指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 38. massive-1-0-zh-cn-v1/2260

Changed: `domain`

Input:

```text
请播放梁博歌曲
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 含人名、地名、品牌、媒體或作品名稱，主要測試專名保留。

Gemini reason: 「梁博」為人名，應視為專有名詞。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 39. massive-1-0-zh-cn-v1/2651

Changed: `risk`

Input:

```text
该地区的最新消息
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 含中國產品、交通、介面或生活用語，可能需要臺灣慣用詞轉換。

Gemini reason: 新聞用語，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 40. massive-1-0-zh-cn-v1/2685

Changed: `script`

Input:

```text
olly 我需要一个有趣的笑话告诉山姆
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 含人名、地名、品牌、媒體或作品名稱，主要測試專名保留。

Gemini reason: 包含喚醒詞「olly」和人名「山姆」，需避免不當轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 41. massive-1-0-zh-cn-v1/2992

Changed: `risk`

Input:

```text
最近的科技头条
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 「科技」一詞通用，但「頭條」在臺灣多聯想到特定媒體，用「重點新聞」可能更中性。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 42. massive-1-0-zh-cn-v1/3061

Changed: `risk`

Input:

```text
我想知道这个新消息来源是什么
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 含中國產品、交通、介面或生活用語，可能需要臺灣慣用詞轉換。

Gemini reason: 新聞相關用語，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 43. massive-1-0-zh-cn-v1/3399

Changed: `domain`

Input:

```text
我需要一个晚上九点的闹钟
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 標準指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 44. massive-1-0-zh-cn-v1/3777

Changed: `domain`

Input:

```text
我现在想要橙色灯
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 標準指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 45. massive-1-0-zh-cn-v1/5355

Changed: `domain`

Input:

```text
关掉房间中间的灯
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 標準指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 46. massive-1-0-zh-cn-v1/5601

Changed: `domain`

Input:

```text
天气预报怎么样
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 標準指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 47. massive-1-0-zh-cn-v1/5869

Changed: `risk`

Input:

```text
今天上海天气报告啥情况啊
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 含中國產品、交通、介面或生活用語，可能需要臺灣慣用詞轉換。

Gemini reason: 「上海」為地名。口語「啥情況啊」在臺灣較少用，但可理解。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 48. massive-1-0-zh-cn-v1/635

Changed: `domain, risk`

Input:

```text
请启动扫地机器人
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 「掃地機器人」詞彙通用，但「啟動」在臺灣UI情境中，「開啟」或「開始」更常用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 49. massive-1-0-zh-cn-v1/6887

Changed: `eligible, domain, risk`

Input:

```text
好
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | contextless_fragment |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 輸入缺少可獨立判讀的必要內容，或本地化錯誤已改變原意，建議排除。

Gemini reason: 單字「好」，通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 50. massive-1-0-zh-cn-v1/6965

Changed: `domain`

Input:

```text
今天晚上有什么待处理的提醒
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 含中國產品、交通、介面或生活用語，可能需要臺灣慣用詞轉換。

Gemini reason: 「待處理」通用，但「提醒」在臺灣常用作名詞，「提醒事項」更完整。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 51. massive-1-0-zh-cn-v1/709

Changed: `risk`

Input:

```text
给我看选举投票的最新消息
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 含人名、地名、品牌、媒體或作品名稱，主要測試專名保留。

Gemini reason: 新聞用語，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 52. massive-1-0-zh-cn-v1/7168

Changed: `risk`

Input:

```text
告诉我每年三月二十六日举办的方程式比赛的细节
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 含人名、地名、品牌、媒體或作品名稱，主要測試專名保留。

Gemini reason: 「方程式比賽」在臺灣通常稱為「方程式賽車」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 53. massive-1-0-zh-cn-v1/7179

Changed: `domain`

Input:

```text
在下周六会议前两小时给我个提醒
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 標準指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 54. massive-1-0-zh-cn-v1/7344

Changed: `domain, risk`

Input:

```text
删除日历上所有事件
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 含中國產品、交通、介面或生活用語，可能需要臺灣慣用詞轉換。

Gemini reason: 標準指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 55. massive-1-0-zh-cn-v1/7423

Changed: `eligible, domain, risk`

Input:

```text
星期一的会议
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | contextless_fragment |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 輸入缺少可獨立判讀的必要內容，或本地化錯誤已改變原意，建議排除。

Gemini reason: 日常用語，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 56. massive-1-0-zh-cn-v1/748

Changed: `domain`

Input:

```text
请把这首歌的音量调低
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 標準指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 57. massive-1-0-zh-cn-v1/7595

Changed: `domain`

Input:

```text
为曲奇设置五分钟的计时器
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 含中國產品、交通、介面或生活用語，可能需要臺灣慣用詞轉換。

Gemini reason: 「曲奇」在臺灣通常稱為「餅乾」，前者是香港及大陸常用詞。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 58. massive-1-0-zh-cn-v1/7718

Changed: `domain`

Input:

```text
给罗斯先生发一份本周五的会议邀请并把我周五下午的日程安排在日程表上
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 含人名、地名、品牌、媒體或作品名稱，主要測試專名保留。

Gemini reason: 「羅斯先生」為人名。「日程」在臺灣多用「行程」或「行事曆」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 59. massive-1-0-zh-cn-v1/787

Changed: `risk`

Input:

```text
今天天咋样啊
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 「天咋樣啊」是北方口語，臺灣會說「天氣怎麼樣」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 60. massive-1-0-zh-cn-v1/8077

Changed: `domain`

Input:

```text
提醒我十分钟内取邮件
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 標準指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 61. massive-1-0-zh-cn-v1/8116

Changed: `domain`

Input:

```text
在二月一日和三月十六日之间有什么会议吗
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 標準指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 62. massive-1-0-zh-cn-v1/8225

Changed: `domain, risk`

Input:

```text
删除星期二的活动
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 含中國產品、交通、介面或生活用語，可能需要臺灣慣用詞轉換。

Gemini reason: 標準指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 63. massive-1-0-zh-cn-v1/8769

Changed: `domain, risk`

Input:

```text
删除接下来的活动
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 含中國產品、交通、介面或生活用語，可能需要臺灣慣用詞轉換。

Gemini reason: 標準指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 64. massive-1-0-zh-cn-v1/9099

Changed: `domain, risk`

Input:

```text
把我加在二月十二日上午九点的医生的预约取消
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 含中國產品、交通、介面或生活用語，可能需要臺灣慣用詞轉換。

Gemini reason: 標準指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 65. massive-1-0-zh-cn-v1/961

Changed: `domain`

Input:

```text
请提高这个房间的亮度
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 語意可獨立判讀，主要覆蓋一般字形與區域中性的短指令。

Gemini reason: 標準指令，詞彙通用。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`
