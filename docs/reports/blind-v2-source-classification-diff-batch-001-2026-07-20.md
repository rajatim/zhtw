<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 001 (2026-07-20)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `432f4d299ec4509b64f1705e1c2bb1b1a750df573d85ef29a0d59c580da844f0`
Cases: 100
Exact Codex/Gemini classifications: 60
Maintainer review queue: 40

Field differences:

- Eligibility: 21
- Script: 0
- Domain: 28
- Risk: 35

## Policy Finding

Gemini marked 16 cases as eligible even though its own quality flags identified malformed or fragmentary input. These suggestions fail the declared source-quality rule and are not auto-adopted.

The maintainer resolved all 40 advisory disagreements and batch-confirmed the 60 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. flores-200-zho-hans-v1/dev-0094

Changed: `risk`

Input:

```text
这与先前的报道相矛盾，先前的报道称取消决选本来是违反宪法的。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 句意完整；依輸入語域與詞彙風險分類。

Gemini reason: 標準正式新聞用語，簡體轉繁體。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 02. flores-200-zho-hans-v1/dev-0165

Changed: `risk`

Input:

```text
它属于美国海军第七舰队，部署在日本长崎佐世保。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 句意完整；依輸入語域與詞彙風險分類。

Gemini reason: 標準新聞報導，地名與組織名。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 03. flores-200-zho-hans-v1/dev-0262

Changed: `risk`

Input:

```text
尼日利亚日前宣布，计划在峰会召开的前一周内加入非洲大陆自由贸易区 (AfCFTA)。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 句意完整；依輸入語域與詞彙風險分類。

Gemini reason: 國際新聞，涉及國家與組織名稱。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 04. flores-200-zho-hans-v1/dev-0305

Changed: `domain`

Input:

```text
20 世纪 60 年代，他回到刚刚独立的阿尔及利亚，教授电影导演知识。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 句意完整；依輸入語域與詞彙風險分類。

Gemini reason: 一般敘事句，詞彙通用。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 05. flores-200-zho-hans-v1/dev-0529

Changed: `domain, risk`

Input:

```text
现代击剑运动分为多个级别：有大学学生初步学习的级别，也有专业和奥林匹克竞技的级别。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 句意完整；依輸入語域與詞彙風險分類。

Gemini reason: 一般性描述，詞彙普遍。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 06. flores-200-zho-hans-v1/dev-0620

Changed: `domain`

Input:

```text
在听取别人分享他们个人、家庭和组织的故事时，我们对过去以及一些对组织文化有或好或坏影响的人物有了宝贵的认识。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 句意完整；依輸入語域與詞彙風險分類。

Gemini reason: 標準敘述，詞彙通用。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 07. flores-200-zho-hans-v1/dev-0621

Changed: `domain`

Input:

```text
虽然理解历史并不意味着理解文化，但至少可以帮助人们了解自己在组织历史中的位置。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 句意完整；依輸入語域與詞彙風險分類。

Gemini reason: 標準敘述，詞彙通用。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 08. flores-200-zho-hans-v1/devtest-0100

Changed: `domain, risk`

Input:

```text
莫尔 (Moll) 博士认为，有些病人可能是在医院感染了病菌，而且至少有两名病人是医院的医护人员。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 句意完整；依輸入語域與詞彙風險分類。

Gemini reason: 包含音譯人名'莫尔'。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 09. flores-200-zho-hans-v1/devtest-0208

Changed: `domain`

Input:

```text
海地正义与民主研究所 (Haitian Institute for Justice and Democracy) 引用的独立研究表明，是尼泊尔的联合国维和部队在不知情的情况下将这种疾病带到了海地。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 句意完整；依輸入語域與詞彙風險分類。

Gemini reason: 國際新聞，包含國家與組織名。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 10. flores-200-zho-hans-v1/devtest-0284

Changed: `risk`

Input:

```text
事故发生的道路暂时封闭，紧急救援人员将司机从红色奥迪 TT 中救了出来。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 句意完整；依輸入語域與詞彙風險分類。

Gemini reason: 包含汽車品牌'奥迪'，為專有名詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 11. flores-200-zho-hans-v1/devtest-0376

Changed: `risk`

Input:

```text
随着时间的推移，新的种群开始适应新的环境，它们开始变得与其他种群越来越不相似了。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 句意完整；依輸入語域與詞彙風險分類。

Gemini reason: 科普內容，詞彙通用。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 12. flores-200-zho-hans-v1/devtest-0425

Changed: `risk`

Input:

```text
1624 年，荷兰东印度公司在台湾地区西南部建立基地，开始改变原住民的粮食生产方式，并雇佣华工在其水稻和蔗糖种植园工作。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 句意完整；依輸入語域與詞彙風險分類。

Gemini reason: 涉及臺灣歷史，用詞需精確，但本句詞彙尚屬通用。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 13. flores-200-zho-hans-v1/devtest-0584

Changed: `domain`

Input:

```text
这个术语源于人们对臭虫的熟悉，臭虫是一种非常适应寄生于人类的昆虫。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | medium | - |
| Gemini | yes | social_daily | candidate_gap | medium | - |

Codex reason: 句意完整；依輸入語域與詞彙風險分類。

Gemini reason: '术语'一詞在臺灣雖可用'術語'，但有時'用語'或'專有名詞'更自然。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 14. flores-200-zho-hans-v1/devtest-0837

Changed: `risk`

Input:

```text
咖喱饭菜是一道以香草和香料为主的菜肴，并配以肉类或蔬菜。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 句意完整；依輸入語域與詞彙風險分類。

Gemini reason: 描述食物，詞彙通用。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 15. ud-chinese-cfl-v1/CFL_A_1-14_ori

Changed: `eligible, domain, risk`

Input:

```text
就是对我来说难忘的经历。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 缺少可獨立判讀的完整語境。

Gemini reason: 學習者語料，日常對話。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 16. ud-chinese-cfl-v1/CFL_A_1-7_ori

Changed: `eligible, domain, risk`

Input:

```text
还有我们和军人一起拍照。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 缺少可獨立判讀的完整語境。

Gemini reason: 學習者語料，日常對話。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 17. ud-chinese-cfl-v1/CFL_A_2-11_ori

Changed: `eligible, domain, risk`

Input:

```text
对我来说很难忘也感觉很新鲜的旅行。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 缺少可獨立判讀的完整語境。

Gemini reason: 學習者語料，日常對話。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 18. ud-chinese-cfl-v1/CFL_B_1-21_ori

Changed: `eligible, domain, risk`

Input:

```text
我每次想起来那个10天的时候感动坏了。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed |
| Gemini | yes | social_daily | baseline_guard | high | malformed |

Codex reason: 學習者語法、用字或語意錯誤影響可用性。

Gemini reason: 學習者語料，'感动坏了'語法較不自然。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 19. ud-chinese-cfl-v1/CFL_B_1-3_ori

Changed: `eligible, domain, risk`

Input:

```text
讲为什么感动之前，把麦加介绍一下。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 缺少可獨立判讀的完整語境。

Gemini reason: 學習者語料，包含地名'麦加'。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 20. ud-chinese-cfl-v1/CFL_C_1-21_ori

Changed: `eligible, domain, risk`

Input:

```text
又及。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | social_daily | baseline_guard | high | fragment |

Codex reason: 缺少可獨立判讀的完整語境。

Gemini reason: 片段，書信結尾用語。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 21. ud-chinese-cfl-v1/CFL_C_1-6_ori

Changed: `eligible, domain, risk`

Input:

```text
因我的意见不是偶然的，我的态度是正确的，所以总统无可奈何地重视我指出的，开始跟我互相帮助和互相合作，而我们一起改善国家内的情况和条件，越发地使白俄罗斯发展，也增家祖国的世界舞台的位置......
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed |
| Gemini | yes | social_daily | over_conversion_guard | high | malformed |

Codex reason: 學習者語法、用字或語意錯誤影響可用性。

Gemini reason: 學習者語料，包含國名'白俄罗斯'。'增家'應為'增加'之誤。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 22. ud-chinese-cfl-v1/CFL_C_1-9_ori

Changed: `eligible, domain, risk`

Input:

```text
其次，我提议妥善的答案。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed |
| Gemini | yes | social_daily | baseline_guard | medium | malformed |

Codex reason: 學習者語法、用字或語意錯誤影響可用性。

Gemini reason: 學習者語料，'提议妥善的答案'語意稍不順暢。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 23. ud-chinese-cfl-v1/CFL_D_1-10_ori

Changed: `eligible, domain, risk`

Input:

```text
只有想快点去酒店休息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragment |
| Gemini | yes | social_daily | baseline_guard | high | fragment |

Codex reason: 缺少可獨立判讀的完整語境。

Gemini reason: 學習者語料，語句不完整。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 24. ud-chinese-cfl-v1/CFL_D_1-26_ori

Changed: `eligible, domain, risk`

Input:

```text
风雨交加的时候也却看来很美丽。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed |
| Gemini | yes | social_daily | baseline_guard | high | malformed |

Codex reason: 學習者語法、用字或語意錯誤影響可用性。

Gemini reason: 學習者語料，'也却'重複，語法錯誤。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 25. ud-chinese-cfl-v1/CFL_D_1-29_ori

Changed: `eligible, domain, risk`

Input:

```text
那里的好回忆是感动的。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed |
| Gemini | yes | social_daily | baseline_guard | high | malformed |

Codex reason: 學習者語法、用字或語意錯誤影響可用性。

Gemini reason: 學習者語料，'回忆是感动的'語法不自然。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 26. ud-chinese-cfl-v1/CFL_D_2-11_ori

Changed: `eligible, domain, risk`

Input:

```text
我到山顶看海岸，就感觉秀色可餐。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed |
| Gemini | yes | social_daily | baseline_guard | high | malformed |

Codex reason: 學習者語法、用字或語意錯誤影響可用性。

Gemini reason: 學習者語料，成語'秀色可餐'使用不當。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 27. ud-chinese-cfl-v1/CFL_D_2-14_ori

Changed: `eligible, domain, risk`

Input:

```text
我一个人吃也好吃极了。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 學習者語法、用字或語意錯誤影響可用性。

Gemini reason: 學習者語料，日常對話。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 28. ud-chinese-cfl-v1/CFL_E_1-14_ori

Changed: `eligible, domain, risk`

Input:

```text
过去周末后，快去医院就见的是很多老人，除了我之外没有年轻人。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed |
| Gemini | yes | social_daily | baseline_guard | high | malformed |

Codex reason: 學習者語法、用字或語意錯誤影響可用性。

Gemini reason: 學習者語料，語句不通順，語法錯誤。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 29. ud-chinese-cfl-v1/CFL_F_1-16_ori

Changed: `risk`

Input:

```text
他的用心让我感觉暖和。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | malformed |

Codex reason: 句意可獨立判讀；保留學習者語料特性。

Gemini reason: 學習者語料，用詞不當，應為'温暖'而非'暖和'。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 30. ud-chinese-cfl-v1/CFL_F_1-20_ori

Changed: `eligible, domain, risk`

Input:

```text
终于我们精疲力尽地到了哪家西餐厅。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed |
| Gemini | yes | social_daily | baseline_guard | high | malformed |

Codex reason: 學習者語法、用字或語意錯誤影響可用性。

Gemini reason: 學習者語料，'哪家'應為'那家'之誤。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 31. ud-chinese-cfl-v1/CFL_G_1-3_ori

Changed: `eligible, domain, risk`

Input:

```text
第二天早上7点半我起床了起了很快，8点我上车到朋友的学校，到大学以后，她和其他的女士门，我们互相认识，然后请我们吃好吃的清真的饭，过了一会儿我门去上车开始第一次爬山的旅行开始了。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed |
| Gemini | yes | social_daily | baseline_guard | high | malformed |

Codex reason: 學習者語法、用字或語意錯誤影響可用性。

Gemini reason: 學習者語料，語句冗長且包含多處語法及錯別字錯誤（'女士门'、'我门'）。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 32. ud-chinese-cfl-v1/CFL_H_1-2_ori

Changed: `eligible, domain, risk`

Input:

```text
所以我希望了长大以后我要去菲律宾旅行。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed |
| Gemini | yes | social_daily | over_conversion_guard | high | malformed |

Codex reason: 學習者語法、用字或語意錯誤影響可用性。

Gemini reason: 學習者語料，包含國名'菲律宾'。'希望了'語法錯誤。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 33. ud-chinese-cfl-v1/CFL_I_1-1_ori

Changed: `eligible, domain, risk`

Input:

```text
我要开始讲对我的初恋。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed |
| Gemini | yes | social_daily | baseline_guard | high | malformed |

Codex reason: 學習者語法、用字或語意錯誤影響可用性。

Gemini reason: 學習者語料，'讲对'語法不自然。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 34. ud-chinese-cfl-v1/CFL_J_1-6_ori

Changed: `eligible, domain, risk`

Input:

```text
我被着惊人的举动惊呆了，一个残疾人都可以做到的事，为什么我们做不到？
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed |
| Gemini | yes | social_daily | baseline_guard | high | malformed |

Codex reason: 學習者語法、用字或語意錯誤影響可用性。

Gemini reason: 學習者語料，'被着'應為'被這'之誤。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 35. ud-chinese-cfl-v1/CFL_L_1-13_ori

Changed: `eligible, domain, risk`

Input:

```text
那时，我决定公开求婚在山顶上。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed |
| Gemini | yes | social_daily | baseline_guard | high | malformed |

Codex reason: 學習者語法、用字或語意錯誤影響可用性。

Gemini reason: 學習者語料，語序'公开求婚在山顶上'不自然。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 36. ud-chinese-cfl-v1/CFL_L_1-6_ori

Changed: `eligible, domain, risk`

Input:

```text
在兰州我给她打个电话，突然她说告别。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 學習者語法、用字或語意錯誤影響可用性。

Gemini reason: 學習者語料，包含地名'兰州'。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 37. ud-chinese-cfl-v1/CFL_P_1-5_ori

Changed: `risk`

Input:

```text
我觉得这可能是因为中国上班比较早，所以一般中国人没有吃早饭的时间。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 句意可獨立判讀；保留學習者語料特性。

Gemini reason: 學習者語料，包含'中国'。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 38. ud-chinese-cfl-v1/CFL_X_1-2_ori

Changed: `risk`

Input:

```text
胜利是属于最前面那个黑人！
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 句意可獨立判讀；保留學習者語料特性。

Gemini reason: 學習者語料，日常對話。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 39. ud-chinese-cfl-v1/CFL_Y_1-4_ori

Changed: `risk`

Input:

```text
学校的早晨是有声有色的，一到学校门口两旁树上的小鸟便会叽叽喳喳地叫，好像在说：“老师，同学们，早上好！”
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 句意可獨立判讀；保留學習者語料特性。

Gemini reason: 學習者語料，描述性文字。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 40. ud-chinese-cfl-v1/CFL_Y_1-6_ori

Changed: `risk`

Input:

```text
因为快要上课了，他们害怕迟到，所以他们一边吃着早饭，一边跑去教室。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 句意可獨立判讀；保留學習者語料特性。

Gemini reason: 學習者語料，日常敘述。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`
