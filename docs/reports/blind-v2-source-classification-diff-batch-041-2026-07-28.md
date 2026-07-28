<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 041 (2026-07-28)

Status: advisory only; maintainer decisions pending

Packet SHA-256: `8466172bf781262313a93c4ba8e651f6eeb23b870b7de16631c2c859d7396f4e`
Cases: 96
Exact Codex/Gemini classifications: 21
Maintainer review queue: 75

Field differences:

- Eligibility: 8
- Script: 0
- Domain: 12
- Risk: 73

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

Neither advisory is auto-preferred. Codex must synthesize the differences before maintainer confirmation; no classification in this report has been written into the candidate pool.

## Review Queue

### 01. massive-1-0-zh-cn-v1/10778

Changed: `risk`

Input:

```text
我今天有一个必做清单是吗
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；專名、操作或口語用詞具有簡轉臺繁評測價值。

Gemini reason: A clear and complete question.

Maintainer decision: `pending`

### 02. massive-1-0-zh-cn-v1/11367

Changed: `risk`

Input:

```text
倒带这集播客
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；專名、操作或口語用詞具有簡轉臺繁評測價值。

Gemini reason: A clear media control command ('rewind this podcast').

Maintainer decision: `pending`

### 03. massive-1-0-zh-cn-v1/12594

Changed: `risk`

Input:

```text
你能给我订一张明天的火车票吗
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；專名、操作或口語用詞具有簡轉臺繁評測價值。

Gemini reason: A clear and complete question asking to book a train ticket.

Maintainer decision: `pending`

### 04. massive-1-0-zh-cn-v1/15217

Changed: `eligible, domain, risk`

Input:

```text
照片
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 僅有「照片」一詞，無法由輸入判定查詢或操作意圖。

Gemini reason: A single-word phrase with clear intent in a voice-assistant context (e.g., 'show photos').

Maintainer decision: `pending`

### 05. massive-1-0-zh-cn-v1/16885

Changed: `domain, risk`

Input:

```text
发送电子邮件给韩女士问她迪恩是否交了最后一份家庭作业
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；專名、操作或口語用詞具有簡轉臺繁評測價值。

Gemini reason: A complex but complete command to send an email, containing proper names ('韩女士', '迪恩').

Maintainer decision: `pending`

### 06. massive-1-0-zh-cn-v1/17114

Changed: `domain`

Input:

```text
你能回复那封电子邮件吗
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；專名、操作或口語用詞具有簡轉臺繁評測價值。

Gemini reason: A complete and valid question, although it relies on context ('that email').

Maintainer decision: `pending`

### 07. massive-1-0-zh-cn-v1/1808

Changed: `eligible, domain, risk`

Input:

```text
标题
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 僅有「標題」一詞，缺少可獨立裁決的語境。

Gemini reason: A single-word phrase with clear intent (e.g., 'what is the title').

Maintainer decision: `pending`

### 08. massive-1-0-zh-cn-v1/1965

Changed: `risk`

Input:

```text
嗨给我播放周杰伦今年新发的歌的歌单
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；專名、操作或口語用詞具有簡轉臺繁評測價值。

Gemini reason: A clear command to play music, containing a proper name ('周杰伦').

Maintainer decision: `pending`

### 09. massive-1-0-zh-cn-v1/2009

Changed: `risk`

Input:

```text
这周天气情况咋样啊
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；專名、操作或口語用詞具有簡轉臺繁評測價值。

Gemini reason: A colloquial but clear and complete question about the weather.

Maintainer decision: `pending`

### 10. massive-1-0-zh-cn-v1/229

Changed: `risk`

Input:

```text
拉斯维加斯现在几点
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；專名、操作或口語用詞具有簡轉臺繁評測價值。

Gemini reason: A clear question asking for the time in a specific location ('拉斯维加斯').

Maintainer decision: `pending`

### 11. massive-1-0-zh-cn-v1/3420

Changed: `eligible, domain, risk`

Input:

```text
音乐节拍跟踪
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 名詞片段未表明查詢或操作意圖，無法獨立裁決。

Gemini reason: A noun phrase used as a command, likely referring to a feature ('music beat tracking').

Maintainer decision: `pending`

### 12. massive-1-0-zh-cn-v1/380

Changed: `eligible, domain, risk`

Input:

```text
清播放骚动乐团的游戏
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 句首多出「清」且「樂團的遊戲」語意不明，屬明顯病句。

Gemini reason: The command has a typo ('清' instead of '请') but the intent is clear. It contains proper nouns for a band and song ('骚动乐团', '游戏').

Maintainer decision: `pending`

### 13. massive-1-0-zh-cn-v1/4760

Changed: `risk`

Input:

```text
预报下雪吗
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；專名、操作或口語用詞具有簡轉臺繁評測價值。

Gemini reason: A clear and complete question about a weather forecast.

Maintainer decision: `pending`

### 14. massive-1-0-zh-cn-v1/5657

Changed: `risk`

Input:

```text
给我放一些蔡依林的音乐
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；專名、操作或口語用詞具有簡轉臺繁評測價值。

Gemini reason: A command to play music, containing a proper name ('蔡依林').

Maintainer decision: `pending`

### 15. massive-1-0-zh-cn-v1/6347

Changed: `risk`

Input:

```text
嗨小度最近怎么样
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；專名、操作或口語用詞具有簡轉臺繁評測價值。

Gemini reason: A conversational phrase addressed to a named AI assistant ('小度').

Maintainer decision: `pending`

### 16. massive-1-0-zh-cn-v1/679

Changed: `domain, risk`

Input:

```text
我想你在给手机充好电之前关掉智能插座
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；專名、操作或口語用詞具有簡轉臺繁評測價值。

Gemini reason: A clear command for an IoT device (smart plug).

Maintainer decision: `pending`

### 17. massive-1-0-zh-cn-v1/7090

Changed: `eligible, domain, risk`

Input:

```text
谷歌日历
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 僅有產品名稱，未表明要開啟、查詢或操作的意圖。

Gemini reason: An app name ('谷歌日历') used as a command.

Maintainer decision: `pending`

### 18. massive-1-0-zh-cn-v1/8609

Changed: `risk`

Input:

```text
取消我周二和丽莎的会议把它改到周四
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；專名、操作或口語用詞具有簡轉臺繁評測價值。

Gemini reason: A clear calendar management command that includes a proper name ('丽莎').

Maintainer decision: `pending`

### 19. massive-1-0-zh-cn-v1/9071

Changed: `domain`

Input:

```text
设置会议通知
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；專名、操作或口語用詞具有簡轉臺繁評測價值。

Gemini reason: A clear command to configure a setting.

Maintainer decision: `pending`

### 20. massive-1-0-zh-cn-v1/950

Changed: `risk`

Input:

```text
上海天气怎么样啊
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；專名、操作或口語用詞具有簡轉臺繁評測價值。

Gemini reason: A colloquial but clear question about the weather, containing a proper name ('上海').

Maintainer decision: `pending`

### 21. ready-gov-tornadoes-zh-hans-v1/sentence-002

Changed: `eligible, domain, risk`

Input:

```text
带来强风，每小时超过 200 英里。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 缺少主詞或前文指涉，無法單獨判定「帶來」的對象。

Gemini reason: The sentence is a complete descriptive statement. The term '英里' for miles is common, but Taiwan sometimes uses '哩', making it a minor regional difference candidate.

Maintainer decision: `pending`

### 22. ready-gov-tornadoes-zh-hans-v1/sentence-004

Changed: `risk`

Input:

```text
遵循州府、地方和部落官员的指示。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方防災或健康安全指示；屬高風險公共安全語料。

Gemini reason: The instruction is clear and uses standard terminology like '州府' and '部落官员' that translates well.

Maintainer decision: `pending`

### 23. ready-gov-tornadoes-zh-hans-v1/sentence-005

Changed: `risk`

Input:

```text
立即前往安全的避难所，例如，安全室、地下室、风暴地窖或坚固建筑物最低层的小型室内房间。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方防災或健康安全指示；屬高風險公共安全語料。

Gemini reason: This is a clear, actionable instruction. The terms for shelters ('安全室', '地下室', '风暴地窖') are specific and understandable, even if '风暴地窖' is less common in some regions.

Maintainer decision: `pending`

### 24. ready-gov-tornadoes-zh-hans-v1/sentence-009

Changed: `risk`

Input:

```text
注意可能导致受伤或死亡的飞溅碎片。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方防災或健康安全指示；屬高風險公共安全語料。

Gemini reason: This is a standard warning phrase with no significant regional variations.

Maintainer decision: `pending`

### 25. ready-gov-tornadoes-zh-hans-v1/sentence-022

Changed: `risk`

Input:

```text
宠物也是重要的亲人，因此需要纳入家庭应急计划。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方防災或健康安全指示；屬高風險公共安全語料。

Gemini reason: The sentence is a complete thought and uses common, shared terminology.

Maintainer decision: `pending`

### 26. ready-gov-tornadoes-zh-hans-v1/sentence-023

Changed: `risk`

Input:

```text
为长期待在家里或就地避难做好准备，收集应急用品、清洁用品、不易腐烂的食物、用水、医疗用品和药物。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方防災或健康安全指示；屬高風險公共安全語料。

Gemini reason: This is a standard preparedness instruction with widely understood terms.

Maintainer decision: `pending`

### 27. ready-gov-tornadoes-zh-hans-v1/sentence-024

Changed: `risk`

Input:

```text
立即前往确定的安全地点。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方防災或健康安全指示；屬高風險公共安全語料。

Gemini reason: A clear, concise, and standard emergency instruction.

Maintainer decision: `pending`

### 28. ready-gov-tornadoes-zh-hans-v1/sentence-027

Changed: `risk`

Input:

```text
不要试图开车跑过龙卷风。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方防災或健康安全指示；屬高風險公共安全語料。

Gemini reason: A clear and direct prohibition that is easily understood.

Maintainer decision: `pending`

### 29. ready-gov-tornadoes-zh-hans-v1/sentence-031

Changed: `risk`

Input:

```text
远离掉落的电线或损坏的公用设施线路。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方防災或健康安全指示；屬高風險公共安全語料。

Gemini reason: The terminology for 'electric wires' and 'utility lines' is standard and clear.

Maintainer decision: `pending`

### 30. ready-gov-tornadoes-zh-hans-v1/sentence-032

Changed: `risk`

Input:

```text
如果生病并需就医，联系医务人员。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方防災或健康安全指示；屬高風險公共安全語料。

Gemini reason: This medical instruction uses standard, universally understood terms like '就医' (seek medical care) and '医务人员' (medical personnel).

Maintainer decision: `pending`

### 31. ready-gov-tornadoes-zh-hans-v1/sentence-033

Changed: `risk`

Input:

```text
等待进一步的医治指示并继续就地避难。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方防災或健康安全指示；屬高風險公共安全語料。

Gemini reason: This is a clear, standard instruction for a post-disaster or emergency scenario.

Maintainer decision: `pending`

### 32. ready-gov-tornadoes-zh-hans-v1/sentence-034

Changed: `risk`

Input:

```text
在清理过程中，穿戴合适的装备，例如，厚底鞋、长裤和工作手套，清理霉菌或其他碎屑时，戴上合适的面罩或口罩。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方防災或健康安全指示；屬高風險公共安全語料。

Gemini reason: The instruction about personal protective equipment ('厚底鞋', '长裤', '工作手套', '面罩', '口罩') uses clear, standard terms.

Maintainer decision: `pending`

### 33. ready-gov-winter-weather-zh-hans-v1/sentence-007

Changed: `risk`

Input:

```text
冬季风暴警告通常在事件预计开始前 12 至 24 小时发布。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方防災或健康安全指示；屬高風險公共安全語料。

Gemini reason: 完整的句子，提供官方指南，表述清晰。

Maintainer decision: `pending`

### 34. ready-gov-winter-weather-zh-hans-v1/sentence-011

Changed: `risk`

Input:

```text
注意天气报告和冰冻天气和冬季风暴的警告。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方防災或健康安全指示；屬高風險公共安全語料。

Gemini reason: 完整的指令性句子。连续使用'和'字在语法上可接受，但稍嫌冗余。

Maintainer decision: `pending`

### 35. ready-gov-winter-weather-zh-hans-v1/sentence-014

Changed: `risk`

Input:

```text
紧急警示系统 (EAS) 和国家海洋和大气管理局 (NOAA) 气象无线电也提供紧急情况警示。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的官方防災或健康安全指示；屬高風險公共安全語料。

Gemini reason: 包含大写英文缩写（EAS, NOAA），有被错误转换的风险，应作为专名保留。

Maintainer decision: `pending`

### 36. ready-gov-winter-weather-zh-hans-v1/sentence-020

Changed: `risk`

Input:

```text
切记宠物的需求。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方防災或健康安全指示；屬高風險公共安全語料。

Gemini reason: 简洁但完整的指令。

Maintainer decision: `pending`

### 37. ready-gov-winter-weather-zh-hans-v1/sentence-021

Changed: `risk`

Input:

```text
为收音机和手电筒准备额外的电池。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方防災或健康安全指示；屬高風險公共安全語料。

Gemini reason: 完整的指令性句子。

Maintainer decision: `pending`

### 38. ready-gov-winter-weather-zh-hans-v1/sentence-025

Changed: `eligible, domain, risk`

Input:

```text
留一箱满的汽油。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 「留一箱滿的汽油」不是完整自然的中文表達，且安全指示可能被誤解。

Gemini reason: 完整的指令。'一箱满的汽油' 表述虽不精炼但可独立理解。

Maintainer decision: `pending`

### 39. ready-gov-winter-weather-zh-hans-v1/sentence-038

Changed: `eligible, domain, risk`

Input:

```text
迹象：麻木、白色或灰黄色的皮肤及紧实或蜡质皮肤。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 僅列「跡象」而未指出所描述的病症，離開前文後無法獨立裁決。

Gemini reason: 清晰的症状列表短语，属于半结构化文本。医疗术语可能存在地域转换差异。

Maintainer decision: `pending`

### 40. ready-gov-winter-weather-zh-hans-v1/sentence-039

Changed: `risk`

Input:

```text
行动：去温暖的房间。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方防災或健康安全指示；屬高風險公共安全語料。

Gemini reason: 清晰直接的指令短语，属于半结构化文本。

Maintainer decision: `pending`

### 41. ready-gov-winter-weather-zh-hans-v1/sentence-041

Changed: `risk`

Input:

```text
体温过低就是异常低的体温。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方防災或健康安全指示；屬高風險公共安全語料。

Gemini reason: 定义性句子，清晰完整。

Maintainer decision: `pending`

### 42. ready-gov-winter-weather-zh-hans-v1/sentence-050

Changed: `risk`

Input:

```text
一氧化碳是一种无色无味的气体，对您、您的家人和宠物有致命的危险。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方防災或健康安全指示；屬高風險公共安全語料。

Gemini reason: 完整的警告句子，表述清晰。

Maintainer decision: `pending`

### 43. ready-gov-winter-weather-zh-hans-v1/sentence-056

Changed: `risk`

Input:

```text
仔细遵循制造商的说明。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方防災或健康安全指示；屬高風險公共安全語料。

Gemini reason: 清晰完整的指令。

Maintainer decision: `pending`

### 44. zhtw-project-llm-it-ui-baseline-v1/it-003

Changed: `risk`

Input:

```text
缓存过期后，下一次请求会重新读取资料。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a complete and clear sentence about caching.

Maintainer decision: `pending`

### 45. zhtw-project-llm-it-ui-baseline-v1/it-004

Changed: `risk`

Input:

```text
部署完成前不会切换线上流量。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a complete and clear sentence about deployment.

Maintainer decision: `pending`

### 46. zhtw-project-llm-it-ui-baseline-v1/it-015

Changed: `risk`

Input:

```text
网页内容更新后，旧缓存会逐步失效。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a complete and clear sentence about web cache invalidation.

Maintainer decision: `pending`

### 47. zhtw-project-llm-it-ui-baseline-v1/it-021

Changed: `risk`

Input:

```text
删除数据前，系统会要求再次确认。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a complete and clear sentence about user confirmation before deletion.

Maintainer decision: `pending`

### 48. zhtw-project-llm-it-ui-baseline-v1/it-023

Changed: `risk`

Input:

```text
日志会记录请求时间和处理结果。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a complete and clear sentence about logging.

Maintainer decision: `pending`

### 49. zhtw-project-llm-it-ui-baseline-v1/it-026

Changed: `risk`

Input:

```text
系统会定期清除超过保存期限的临时文件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a complete and clear sentence about system maintenance.

Maintainer decision: `pending`

### 50. zhtw-project-llm-it-ui-baseline-v1/it-028

Changed: `risk`

Input:

```text
应用程序关闭前会保存尚未提交的修改。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a complete and clear sentence about saving unsaved changes.

Maintainer decision: `pending`

### 51. zhtw-project-llm-it-ui-baseline-v1/llm-001

Changed: `risk`

Input:

```text
模型回答前会先检查问题是否包含必要背景。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a complete and clear sentence about LLM pre-condition checking.

Maintainer decision: `pending`

### 52. zhtw-project-llm-it-ui-baseline-v1/llm-002

Changed: `risk`

Input:

```text
摘要应保留原文中的时间顺序和因果关系。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a complete and clear sentence about summarization rules.

Maintainer decision: `pending`

### 53. zhtw-project-llm-it-ui-baseline-v1/llm-005

Changed: `risk`

Input:

```text
评估人员逐项检查回答是否符合引用内容。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a complete and clear sentence about human evaluation of LLM output.

Maintainer decision: `pending`

### 54. zhtw-project-llm-it-ui-baseline-v1/llm-007

Changed: `risk`

Input:

```text
系统会记录每次评估使用的提示版本。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a complete and clear sentence about versioning in evaluations.

Maintainer decision: `pending`

### 55. zhtw-project-llm-it-ui-baseline-v1/llm-008

Changed: `risk`

Input:

```text
回答过长时，助手应优先保留与问题直接相关的内容。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a complete and clear sentence about content truncation rules for LLMs.

Maintainer decision: `pending`

### 56. zhtw-project-llm-it-ui-baseline-v1/llm-009

Changed: `risk`

Input:

```text
检索结果不足时，不应编造缺少的资料。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a complete and clear sentence about avoiding hallucination/fabrication.

Maintainer decision: `pending`

### 57. zhtw-project-llm-it-ui-baseline-v1/llm-010

Changed: `risk`

Input:

```text
人工复核完成后，案例会移出待处理队列。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a complete and clear sentence about a workflow step (human review).

Maintainer decision: `pending`

### 58. zhtw-project-llm-it-ui-baseline-v1/llm-011

Changed: `risk`

Input:

```text
模型会根据前一轮反馈调整说明方式。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a complete and clear sentence about model adaptation based on feedback.

Maintainer decision: `pending`

### 59. zhtw-project-llm-it-ui-baseline-v1/llm-015

Changed: `risk`

Input:

```text
系统会检查生成内容是否遗漏关键限制条件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a complete and clear sentence about checking for constraints in generated content.

Maintainer decision: `pending`

### 60. zhtw-project-llm-it-ui-baseline-v1/llm-017

Changed: `risk`

Input:

```text
回答包含计算过程时，需要同时列出使用的条件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a complete and clear sentence about showing work in calculations.

Maintainer decision: `pending`

### 61. zhtw-project-llm-it-ui-baseline-v1/llm-019

Changed: `risk`

Input:

```text
检索系统会过滤与当前问题无关的段落。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a complete and clear sentence about filtering in retrieval systems.

Maintainer decision: `pending`

### 62. zhtw-project-llm-it-ui-baseline-v1/llm-020

Changed: `risk`

Input:

```text
评审人员可以标记语义正确但表达不自然的回答。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a complete and clear sentence about a human review process.

Maintainer decision: `pending`

### 63. zhtw-project-llm-it-ui-baseline-v1/llm-021

Changed: `risk`

Input:

```text
模型输出会先经过格式检查，再显示给用户。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a complete and clear sentence about a pre-display processing step.

Maintainer decision: `pending`

### 64. zhtw-project-llm-it-ui-baseline-v1/llm-022

Changed: `risk`

Input:

```text
系统会比较不同提示产生的回答稳定性。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a complete and clear sentence about evaluating response stability.

Maintainer decision: `pending`

### 65. zhtw-project-llm-it-ui-baseline-v1/llm-026

Changed: `risk`

Input:

```text
模型生成清单时应维持项目之间的层级关系。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a complete and clear sentence about maintaining structure in list generation.

Maintainer decision: `pending`

### 66. zhtw-project-llm-it-ui-baseline-v1/llm-027

Changed: `risk`

Input:

```text
系统只会保存完成任务所需的对话内容。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a complete and clear sentence about data retention policy.

Maintainer decision: `pending`

### 67. zhtw-project-llm-it-ui-baseline-v1/llm-029

Changed: `risk`

Input:

```text
助手会先整理用户目标，再提出执行步骤。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a complete and clear sentence about the assistant's reasoning process.

Maintainer decision: `pending`

### 68. zhtw-project-llm-it-ui-baseline-v1/ui-001

Changed: `risk`

Input:

```text
正在加载最新数据。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a common UI status message.

Maintainer decision: `pending`

### 69. zhtw-project-llm-it-ui-baseline-v1/ui-005

Changed: `risk`

Input:

```text
确定要离开这个页面吗？
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a common UI confirmation prompt.

Maintainer decision: `pending`

### 70. zhtw-project-llm-it-ui-baseline-v1/ui-010

Changed: `risk`

Input:

```text
已经复制到剪贴板。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a common UI feedback message.

Maintainer decision: `pending`

### 71. zhtw-project-llm-it-ui-baseline-v1/ui-015

Changed: `risk`

Input:

```text
正在检查可用的更新。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a common UI status message for updates.

Maintainer decision: `pending`

### 72. zhtw-project-llm-it-ui-baseline-v1/ui-019

Changed: `risk`

Input:

```text
删除失败，请稍后再试。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a common UI error message.

Maintainer decision: `pending`

### 73. zhtw-project-llm-it-ui-baseline-v1/ui-022

Changed: `risk`

Input:

```text
没有权限查看这项内容。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a common UI permission error message.

Maintainer decision: `pending`

### 74. zhtw-project-llm-it-ui-baseline-v1/ui-027

Changed: `risk`

Input:

```text
找不到指定的文件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a common UI error message.

Maintainer decision: `pending`

### 75. zhtw-project-llm-it-ui-baseline-v1/ui-029

Changed: `risk`

Input:

```text
请稍候，系统正在处理。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 project-original 基線案例；依既定來源目的標為 baseline guard。

Gemini reason: Input is Simplified Chinese. It is a common UI status message.

Maintainer decision: `pending`
