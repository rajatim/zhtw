<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 039 (2026-07-28)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `48ccd0b9dda2c1e457913156557e3e560f415116c95e2f3fb48601bbe38d2fb8`
Cases: 96
Exact Codex/Gemini classifications: 49
Maintainer review queue: 47

Field differences:

- Eligibility: 5
- Script: 3
- Domain: 18
- Risk: 40

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

The maintainer resolved all 47 advisory disagreements and batch-confirmed the 49 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. massive-1-0-zh-cn-v1/10879

Changed: `risk`

Input:

```text
我今天有什么清单吗
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具明確查詢或操作意圖。

Gemini reason: 日常個人助理查詢，'清单'需轉換為'清單'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 02. massive-1-0-zh-cn-v1/1088

Changed: `domain`

Input:

```text
让自己静音
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具明確查詢或操作意圖。

Gemini reason: 裝置控制指令。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 03. massive-1-0-zh-cn-v1/11593

Changed: `domain, risk`

Input:

```text
多少税
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具明確查詢或操作意圖。

Gemini reason: 金融相關查詢，準確度要求高。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 04. massive-1-0-zh-cn-v1/12306

Changed: `risk`

Input:

```text
订一张去上海的一等座的火车票
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具明確查詢或操作意圖。

Gemini reason: 旅遊預訂指令。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 05. massive-1-0-zh-cn-v1/13259

Changed: `domain, risk`

Input:

```text
给我看看过去十年瑞士的人口增长率
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具明確查詢或操作意圖。

Gemini reason: 數據查詢，包含國名與專業術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 06. massive-1-0-zh-cn-v1/13275

Changed: `risk`

Input:

```text
我在什么位置
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具明確查詢或操作意圖。

Gemini reason: 地點查詢。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 07. massive-1-0-zh-cn-v1/13388

Changed: `domain, risk`

Input:

```text
目前的美元兑欧元汇率是多少
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具明確查詢或操作意圖。

Gemini reason: 金融匯率查詢，準確度要求高。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 08. massive-1-0-zh-cn-v1/13968

Changed: `risk`

Input:

```text
亚伯拉罕·林肯什么时候出生
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具明確查詢或操作意圖。

Gemini reason: 常識性歷史人物問題。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 09. massive-1-0-zh-cn-v1/15531

Changed: `eligible, domain, risk`

Input:

```text
发微博告诉大润发告诉他们他们的客户服务很糟糕
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 來源句含重複、語序錯置、缺少主詞或未指明代名詞，無法作為可靠且可獨立裁決的 benchmark 輸入。

Gemini reason: 社群媒體指令，包含品牌名稱與客戶服務等詞彙。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 10. massive-1-0-zh-cn-v1/15997

Changed: `risk`

Input:

```text
有任何来自梅梅的新的电子邮件吗
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具明確查詢或操作意圖。

Gemini reason: 電子郵件查詢。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 11. massive-1-0-zh-cn-v1/16462

Changed: `script`

Input:

```text
我有什么新讯息吗
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具明確查詢或操作意圖。

Gemini reason: 訊息查詢，'讯息'需轉換為'訊息'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 12. massive-1-0-zh-cn-v1/2019

Changed: `domain, risk`

Input:

```text
将灯光转由蓝色转到绿色再转到黄色
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具明確查詢或操作意圖。

Gemini reason: 智慧家庭裝置控制指令。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 13. massive-1-0-zh-cn-v1/2564

Changed: `risk`

Input:

```text
设个下星期五六点半的闹钟
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具明確查詢或操作意圖。

Gemini reason: 鬧鐘設定指令。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 14. massive-1-0-zh-cn-v1/3606

Changed: `risk`

Input:

```text
北京时间是多少
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具明確查詢或操作意圖。

Gemini reason: 時間查詢。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 15. massive-1-0-zh-cn-v1/4316

Changed: `domain`

Input:

```text
把所有的灯都关掉
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具明確查詢或操作意圖。

Gemini reason: 智慧家庭裝置控制指令。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 16. massive-1-0-zh-cn-v1/4852

Changed: `risk`

Input:

```text
能定个闹铃吗
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具明確查詢或操作意圖。

Gemini reason: 鬧鐘設定指令。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 17. massive-1-0-zh-cn-v1/4878

Changed: `risk`

Input:

```text
加个早上五点的闹钟替换晚上九点的闹钟
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具明確查詢或操作意圖。

Gemini reason: 修改鬧鐘設定指令。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 18. massive-1-0-zh-cn-v1/5359

Changed: `domain, risk`

Input:

```text
切换到东部时区
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具明確查詢或操作意圖。

Gemini reason: 裝置系統設定指令。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 19. massive-1-0-zh-cn-v1/5749

Changed: `risk`

Input:

```text
十一月八号是周一还是周几
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具明確查詢或操作意圖。

Gemini reason: 日期與日曆查詢。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 20. massive-1-0-zh-cn-v1/6621

Changed: `risk`

Input:

```text
电影院最新的电影
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具明確查詢或操作意圖。

Gemini reason: 娛樂資訊查詢。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 21. massive-1-0-zh-cn-v1/6908

Changed: `risk`

Input:

```text
我每一天上午九点都需要一个提醒
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具明確查詢或操作意圖。

Gemini reason: 重複性提醒設定。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 22. massive-1-0-zh-cn-v1/747

Changed: `risk`

Input:

```text
从我的派对歌单播放歌曲
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具明確查詢或操作意圖。

Gemini reason: 音樂播放指令，'歌单'需轉換為'歌單'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 23. massive-1-0-zh-cn-v1/7589

Changed: `eligible, domain, risk`

Input:

```text
我有个活动钟提醒我
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 來源句含重複、語序錯置、缺少主詞或未指明代名詞，無法作為可靠且可獨立裁決的 benchmark 輸入。

Gemini reason: 用詞奇特（活动钟），考驗逐字轉換的邊界情況。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 24. massive-1-0-zh-cn-v1/771

Changed: `domain, risk`

Input:

```text
给我中国新闻网的最新新闻
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具明確查詢或操作意圖。

Gemini reason: 新聞查詢，包含特定媒體名稱。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 25. massive-1-0-zh-cn-v1/8002

Changed: `risk`

Input:

```text
删除我的明天的预约
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具明確查詢或操作意圖。

Gemini reason: 個人行程管理指令。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 26. massive-1-0-zh-cn-v1/9003

Changed: `risk`

Input:

```text
我需要在星期四和首席财务官开个会议
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；短句仍具明確查詢或操作意圖。

Gemini reason: 會議安排指令，包含特定職稱。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 27. osha-disaster-cleanup-simplified-v1/sentence-020

Changed: `risk`

Input:

```text
首先假定所有电力线都带电或仍旧通电。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: Complete and clear safety instruction. It's a good candidate for testing high-stakes domain conversion.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 28. osha-disaster-cleanup-simplified-v1/sentence-034

Changed: `risk`

Input:

```text
不要太靠近切割机；严禁将手伸入正在运行的切割机中。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: Compound sentence with a strong warning. Excellent for testing conversion of formal prohibitions.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 29. osha-disaster-cleanup-simplified-v1/sentence-049

Changed: `risk`

Input:

```text
加油前应当先关闭发电机；严禁将燃料或发电机存放在室内。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: Two clear, related safety instructions. Good test for technical terms and formal prohibitions.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 30. osha-disaster-cleanup-simplified-v1/sentence-074

Changed: `script, domain, risk`

Input:

```text
有关OSHA标准或法规的合规要求的完整列表，请参阅《美国联邦法规》第29篇。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: Formal sentence with proper nouns and titles. Tests handling of named entities and formal language. The domain is more formal/regulatory than direct safety.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 31. ready-gov-drought-zh-hans-v1/sentence-035

Changed: `risk`

Input:

```text
施用含有不溶于水的缓释氮肥。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: A technical instruction related to agriculture/gardening. It tests the handling of specific compound nouns. It's a good baseline guardrail for a specialized domain.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 32. ready-gov-drought-zh-hans-v1/sentence-043

Changed: `risk`

Input:

```text
使用传统过滤器时，一次反冲洗就要用 180 到 250 加仑水。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: A factual statement with technical terms ('反冲洗') and units ('加仑'). It's a good baseline guardrail to check handling of technical vocabulary and loanwords.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 33. ready-gov-floods-zh-hans-v1/sentence-018

Changed: `risk`

Input:

```text
房屋保险保单不包括洪水。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: A complete, factual sentence about insurance policies. It is a good baseline case.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 34. ready-gov-hurricanes-zh-hans-v1/sentence-003

Changed: `risk`

Input:

```text
历史上，风暴潮是美国飓风灾害死亡的主要原因。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: A clear, complete sentence about a historical fact. Serves as a good baseline guard for general conversion quality.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 35. ready-gov-hurricanes-zh-hans-v1/sentence-009

Changed: `risk`

Input:

```text
了解降雨、强风、洪水甚至龙卷风如何在飓风或热带风暴登陆点内陆很远的地方发生。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: A complete instructional sentence. Contains a list of weather phenomena, which is good for testing.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 36. ready-gov-hurricanes-zh-hans-v1/sentence-019

Changed: `script, risk`

Input:

```text
订阅您所在地区的社区警报，了解无需注册即可接收的紧急警报系统（EAS）和无线紧急警报（WEA）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: A complex instructional sentence. Contains technical acronyms (EAS, WEA) and specific terms like '社区警报' (community alerts), which tests the dictionary's breadth.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 37. ready-gov-hurricanes-zh-hans-v1/sentence-026

Changed: `risk`

Input:

```text
飓风过后，您可能数天甚至数周无法获取这些物资。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: A simple, well-formed sentence about a potential future situation. Good baseline case.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 38. ready-gov-hurricanes-zh-hans-v1/sentence-027

Changed: `domain, risk`

Input:

```text
帮助您的邻居与邻居、老年人或可能需要额外帮助以制定飓风应对计划的人士沟通，了解您该如何为他人提供帮助。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | no | high_stakes | baseline_guard | high | awkward_phrasing, redundant |

Codex reason: 來源句含重複、語序錯置、缺少主詞或未指明代名詞，無法作為可靠且可獨立裁決的 benchmark 輸入。

Gemini reason: The phrase '帮助您的邻居与邻居...沟通' (Help your neighbors communicate with neighbors) is redundant and makes the sentence awkward and unnatural. The sentence structure is confusing and not suitable for a quality benchmark.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 39. ready-gov-hurricanes-zh-hans-v1/sentence-028

Changed: `domain, risk`

Input:

```text
及时了解事态注意紧急信息和警报。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | no | high_stakes | baseline_guard | high | fragment, awkward_phrasing |

Codex reason: 來源句含重複、語序錯置、缺少主詞或未指明代名詞，無法作為可靠且可獨立裁決的 benchmark 輸入。

Gemini reason: This appears to be two sentence fragments ('及时了解事态' and '注意紧急信息和警报') concatenated without proper punctuation or conjunction. It is not a grammatically complete or well-formed sentence.

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 40. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-020

Changed: `eligible, domain, risk`

Input:

```text
但是请注意，当流量足够大时，它会流向它喜欢的地方。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 來源句含重複、語序錯置、缺少主詞或未指明代名詞，無法作為可靠且可獨立裁決的 benchmark 輸入。

Gemini reason: 完整的警告句子。其中「它喜欢的地方」帶有擬人化的口語色彩，但整體仍在公共安全指引的範疇內。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 41. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-021

Changed: `eligible, domain, risk`

Input:

```text
此外，如果您转移流量并流向邻居的财产，您可能需要承担损害赔偿责任。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 來源句含重複、語序錯置、缺少主詞或未指明代名詞，無法作為可靠且可獨立裁決的 benchmark 輸入。

Gemini reason: 包含法律和財務責任的完整句子，是典型的高風險領域文本。測試「损害赔偿责任」等專業術語的準確轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 42. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-026

Changed: `risk`

Input:

```text
不寻常的声音，如树木开裂或巨石撞击在一起，可能表明有移动的碎片。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 描述 landslide 前兆的完整句子，適合測試描述性詞彙的轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 43. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-031

Changed: `eligible`

Input:

```text
灰泥、瓷砖、砖块或地基出现新裂缝。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | no | high_stakes | baseline_guard | high | fragment |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 句子不完整，是一個名詞列表加上動詞片語，缺乏主語，很可能是原文中的一個清單項目。因其為句子片段，故不適合做為獨立的 benchmark sentence。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 44. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-038

Changed: `risk`

Input:

```text
地面朝一个方向向下倾斜，并且可能会在您的脚下开始朝该方向移动。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 描述親身體驗的警告信號，句子結構完整，包含方向與動作，是良好的測試案例。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 45. zhtw-project-llm-it-ui-baseline-v1/it-018

Changed: `domain`

Input:

```text
网络延迟过高时，应用程序会显示警告。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整的 project-original baseline 敘述；可檢驗 LLM、IT 或 UI 的基本臺灣用語轉換。

Gemini reason: 標準應用程式 UI 提示。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 46. zhtw-project-llm-it-ui-baseline-v1/it-027

Changed: `domain`

Input:

```text
下载中断后可以从上次进度继续。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整的 project-original baseline 敘述；可檢驗 LLM、IT 或 UI 的基本臺灣用語轉換。

Gemini reason: 常見的下載功能描述。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 47. zhtw-project-llm-it-ui-baseline-v1/it-029

Changed: `domain`

Input:

```text
权限更新后，用户需要重新登录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整的 project-original baseline 敘述；可檢驗 LLM、IT 或 UI 的基本臺灣用語轉換。

Gemini reason: 常見的身份驗證流程。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`
