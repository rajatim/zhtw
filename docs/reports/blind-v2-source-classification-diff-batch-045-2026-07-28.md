<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 045 (2026-07-28)

Status: advisory only; maintainer decisions pending

Packet SHA-256: `1a39e7c32843eae3d5a130cb1d3d58c2fa9b9dc84b0f0346d1b6a98ab3873b46`
Cases: 96
Exact Codex/Gemini classifications: 10
Maintainer review queue: 86

Field differences:

- Eligibility: 8
- Script: 24
- Domain: 41
- Risk: 51

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

Neither advisory is auto-preferred. Codex must synthesize the differences before maintainer confirmation; no classification in this report has been written into the candidate pool.

## Review Queue

### 01. ready-gov-campus-zh-hans-v1/sentence-001

Changed: `eligible, domain, risk`

Input:

```text
了解哪些灾害可能会影响您所在的地区，这可能需要疏散以及何时就地避难。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 句內「這可能需要疏散以及何時就地避難」並列關係殘缺，無法穩定判讀原意。

Gemini reason: Standard public safety guidance. A good baseline case for common vocabulary like 'disaster', 'area', and 'evacuate'.

Maintainer decision: `pending`

### 02. ready-gov-campus-zh-hans-v1/sentence-002

Changed: `script, domain`

Input:

```text
将NOAA天气收音机调到您当地的应急站，并监控电视、收音机并关注有关您所在地区恶劣天气的移动警报和移动警告。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: Contains specific terminology ('NOAA', 'mobile alerts') which tests for correct localization beyond simple character conversion. The phrasing '移动警报和移动警告' also tests handling of repeated terms.

Maintainer decision: `pending`

### 03. ready-gov-campus-zh-hans-v1/sentence-003

Changed: `script, domain`

Input:

```text
下载FEMA应用程序并从国家气象局获取美国任何地方最多五个不同地点的天气警报。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: Classic Mainland vs. Taiwan vocabulary test: '应用程序' (application) is common in Mainland China, whereas Taiwan typically uses 'App' or '應用程式'.

Maintainer decision: `pending`

### 04. ready-gov-campus-zh-hans-v1/sentence-004

Changed: `domain, risk`

Input:

```text
在发生灾害时，学院和大学是联邦、州、地方、部落、领地和私营部门组织的重要应急管理合作伙伴。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: Tests the conversion of a list of formal governmental terms. A naive converter might just swap characters, but correct conversion requires using the appropriate formal terms in Taiwan for entities like '部落' (tribe) and '领地' (territory).

Maintainer decision: `pending`

### 05. ready-gov-campus-zh-hans-v1/sentence-005

Changed: `domain, risk`

Input:

```text
鼓励机构每年多次定期审查、更新和演练其应急计划。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: A straightforward baseline case with common formal verbs like 'review', 'update', 'practice', and nouns like 'institution' and 'plan'.

Maintainer decision: `pending`

### 06. ready-gov-kids-tornadoes-zh-hans-v1/sentence-001

Changed: `domain, risk`

Input:

```text
龙卷风是自然界最猛烈的风暴。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: Simple, factual statement for an educational context. Good for baseline character mapping of common words.

Maintainer decision: `pending`

### 07. ready-gov-kids-tornadoes-zh-hans-v1/sentence-002

Changed: `eligible, domain, risk`

Input:

```text
它们看起来像漏斗或锥形云，风速超过每小时 200 英里。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 以「它們」指涉前句的龍捲風，離開前文後主體不明。

Gemini reason: Tests handling of units. '英里' (miles) is used, but a high-quality localization might also provide a conversion to kilometers, which are standard in Taiwan. It's a test of whether to simply transliterate or to adapt.

Maintainer decision: `pending`

### 08. ready-gov-kids-tornadoes-zh-hans-v1/sentence-003

Changed: `domain`

Input:

```text
龙卷风警示：当恶劣天气可能导致龙卷风形成时发出的警告。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: The sentence defines '龙卷风警示' (tornado watch). The key challenge is the distinction and correct translation of '警示' (watch) and '警告' (warning), which are distinct concepts in emergency notifications. Taiwan typically uses '警報' for warnings.

Maintainer decision: `pending`

### 09. ready-gov-kids-tornadoes-zh-hans-v1/sentence-004

Changed: `eligible, domain, risk`

Input:

```text
这意味着您应该关注电视、广播，并确保打开天气广播。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 以「這意味著」承接前句定義，單獨取樣時缺少指涉內容。

Gemini reason: Standard informational sentence. Good baseline case. Contains common simplified characters like '关', '电视', '广播'.

Maintainer decision: `pending`

### 10. ready-gov-kids-tornadoes-zh-hans-v1/sentence-005

Changed: `domain, risk`

Input:

```text
确保您的手机可以接收无线紧急警报。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: Standard instruction. '无线紧急警报' (Wireless Emergency Alerts) is a technical term that should convert straightforwardly.

Maintainer decision: `pending`

### 11. ready-gov-kids-tornadoes-zh-hans-v1/sentence-007

Changed: `domain`

Input:

```text
当您的城镇或县发布龙卷风警告时，您应该立即找到一个安全的避难所。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: This sentence uses '警告' (warning), contrasting with '警示' (watch) used earlier. It also contains regional terms like '城镇' (town) which might be '鄉鎮' in Taiwan. This tests both specific term conversion and regional vocabulary.

Maintainer decision: `pending`

### 12. ready-gov-kids-tornadoes-zh-hans-v1/sentence-009

Changed: `domain, risk`

Input:

```text
如果天气条件合适，龙卷风可能随时随地发生。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: Simple, declarative sentence. Good baseline case.

Maintainer decision: `pending`

### 13. ready-gov-kids-tornadoes-zh-hans-v1/sentence-010

Changed: `domain, risk`

Input:

```text
在美国，落基山脉以东的中部地区平均遭遇龙卷风的次数最多。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: Geographical fact. Contains common simplified characters ('国', '脉', '东', '数') and proper nouns.

Maintainer decision: `pending`

### 14. ready-gov-kids-tornadoes-zh-hans-v1/sentence-011

Changed: `eligible, domain, risk`

Input:

```text
但是，风险在每个季节都会发生变化。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 以「但是」承接前文的地區分布，單句缺少完整對比對象。

Gemini reason: Simple, common sentence structure. Good baseline.

Maintainer decision: `pending`

### 15. ready-gov-kids-tornadoes-zh-hans-v1/sentence-012

Changed: `domain, risk`

Input:

```text
冬季，从路易斯安那州到乔治亚州的墨西哥湾沿岸州平均遭遇龙卷风的次数最多。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: Contains transliterated proper nouns. Tests the conversion of characters within names like '亚' (亞) and '湾' (灣).

Maintainer decision: `pending`

### 16. ready-gov-kids-tornadoes-zh-hans-v1/sentence-014

Changed: `eligible, domain, risk`

Input:

```text
到夏季，风险区域向北移动到中部和北部平原。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 「到夏季」承接前句季節序列，且「風險區域」缺少明確事件主體。

Gemini reason: Standard geographical and directional terms from a government public service source for children.

Maintainer decision: `pending`

### 17. ready-gov-kids-tornadoes-zh-hans-v1/sentence-016

Changed: `eligible, domain, risk`

Input:

```text
最后，风险区域在冬季回到墨西哥湾沿岸各州。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 以「最後」承接前文季節序列，單句缺少完整上下文。

Gemini reason: The term for 'Gulf of Mexico' and 'Gulf Coast states' may differ.

Maintainer decision: `pending`

### 18. ready-gov-kids-tornadoes-zh-hans-v1/sentence-017

Changed: `risk`

Input:

```text
帮助家人准备应急包。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: Tests common term '应急包' (emergency kit).

Maintainer decision: `pending`

### 19. ready-gov-kids-tornadoes-zh-hans-v1/sentence-018

Changed: `risk`

Input:

```text
如果您有宠物，请确保包括它们需要的东西。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: Simple, common vocabulary in a conditional sentence.

Maintainer decision: `pending`

### 20. ready-gov-kids-tornadoes-zh-hans-v1/sentence-019

Changed: `risk`

Input:

```text
制定家庭沟通计划。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: Tests common term '沟通计划' (communication plan).

Maintainer decision: `pending`

### 21. ready-gov-kids-tornadoes-zh-hans-v1/sentence-020

Changed: `risk`

Input:

```text
计划在龙卷风来袭时停电或不在家时如何与家人沟通。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: Instructional headline format. Tests common emergency-related terms.

Maintainer decision: `pending`

### 22. ready-gov-kids-tornadoes-zh-hans-v1/sentence-022

Changed: `domain, risk`

Input:

```text
练习与父母和宠物一起去安全的地方。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: A standard sentence about safety, suitable for baseline conversion.

Maintainer decision: `pending`

### 23. ready-gov-kids-tornadoes-zh-hans-v1/sentence-023

Changed: `eligible, domain, risk`

Input:

```text
这可能是地下室、地窖或建筑物中最低的洪水区。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 以「這可能是」承接前句所稱安全地點，單句指涉不完整。

Gemini reason: Contains a list of locations, good for checking consistency. The term '洪水区' (flood zone) is slightly formal but correct.

Maintainer decision: `pending`

### 24. ready-gov-kids-tornadoes-zh-hans-v1/sentence-024

Changed: `domain`

Input:

```text
如果您没有地下室，请去壁橱或走廊等室内房间。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: The word '壁橱' (closet) is a good test for regional vocabulary differences, as Taiwan may use '衣櫃' or '儲藏室'.

Maintainer decision: `pending`

### 25. ready-gov-kids-tornadoes-zh-hans-v1/sentence-025

Changed: `domain`

Input:

```text
如果您住在移动房屋中，如果您所在的地区处于龙卷风警报之下，选择安全的地方（如坚固的建筑物或风暴避难所）很重要。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: This complex sentence contains several specific terms like '移动房屋' (mobile home) and '龙卷风警报' (tornado warning) that test terminology conversion.

Maintainer decision: `pending`

### 26. ready-gov-kids-tornadoes-zh-hans-v1/sentence-026

Changed: `domain, risk`

Input:

```text
如果您无法到达更安全的地方，请在沟渠中趴着并用手护住头部。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: A clear, instructional sentence with common verbs and nouns like '沟渠' (ditch) and '护' (protect).

Maintainer decision: `pending`

### 27. ready-gov-kids-tornadoes-zh-hans-v1/sentence-027

Changed: `domain`

Input:

```text
穿上结实的鞋子。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: Tests the adjective '结实' (sturdy), which may have different preferred synonyms in Taiwan like '堅固' or '牢固'.

Maintainer decision: `pending`

### 28. ready-gov-kids-tornadoes-zh-hans-v1/sentence-028

Changed: `domain`

Input:

```text
如果您有自行车头盔，请戴上它以保护您的头部。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: Classic regionalism test case. '自行车' (bicycle) is primarily used in Mainland China, while Taiwan prefers '腳踏車' or also uses '自行車'.

Maintainer decision: `pending`

### 29. ready-gov-kids-tornadoes-zh-hans-v1/sentence-029

Changed: `domain, risk`

Input:

```text
立即前往家人选择的安全地点，如果有时间，请带上您的宠物。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: A straightforward sentence with common words that have direct character-to-character conversions, serving as a good baseline check.

Maintainer decision: `pending`

### 30. ready-gov-kids-tornadoes-zh-hans-v1/sentence-030

Changed: `domain, risk`

Input:

```text
听从父母、看护人或老师的指示。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: The term '看护人' (kānhùrén) is less common in Taiwan than '監護人' (jiānhùrén, guardian), making this a good baseline test for regional vocabulary.

Maintainer decision: `pending`

### 31. ready-gov-kids-tornadoes-zh-hans-v1/sentence-031

Changed: `eligible, domain, risk`

Input:

```text
用手臂遮住头部或颈部，并在身上或身上盖上毯子等物品，以保护自己。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 「在身上或身上」出現重複且關係不明的來源翻譯，無法穩定裁決。

Gemini reason: A straightforward sentence with standard character conversions like '头' -> '頭' and '颈' -> '頸'.

Maintainer decision: `pending`

### 32. ready-gov-kids-tornadoes-zh-hans-v1/sentence-032

Changed: `domain`

Input:

```text
如果您在车里，请下车进入坚固的建筑物。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: Contains common simplified characters ('车', '坚', '进') and phrasing ('车里') that have standard equivalents in Traditional Chinese.

Maintainer decision: `pending`

### 33. ready-gov-kids-tornadoes-zh-hans-v1/sentence-033

Changed: `domain`

Input:

```text
如果您能看到龙卷风，而且距离很远，交通不繁忙，您可以以与龙卷风成直角的方向驶离龙卷风的路径。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: -

Maintainer decision: `pending`

### 34. ready-gov-kids-tornadoes-zh-hans-v1/sentence-034

Changed: `domain`

Input:

```text
如果您在龙卷风期间被困在车里，无法安全离开，请系好安全带留在车里。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: The term '龙卷风' (lóngjuǎnfēng) requires direct character conversion to '龍捲風'. The rest of the sentence uses common vocabulary.

Maintainer decision: `pending`

### 35. ready-gov-kids-tornadoes-zh-hans-v1/sentence-035

Changed: `domain`

Input:

```text
将头放在窗户下方，用手和毯子、外套或其他垫子（如果可能）遮住头部。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: Tests standard character conversions for terms like '将头' (jiāng tóu) and '垫子' (diànzi).

Maintainer decision: `pending`

### 36. ready-gov-kids-tornadoes-zh-hans-v1/sentence-036

Changed: `domain, risk`

Input:

```text
避免在桥下寻找避难所，因为桥下可能会造成交通危险，并且无法提供足够的保护。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: This is a standard instructional sentence. Key conversions include '桥' -> '橋' and '避难所' -> '避難所'.

Maintainer decision: `pending`

### 37. ready-gov-kids-tornadoes-zh-hans-v1/sentence-038

Changed: `domain, risk`

Input:

```text
不要触摸电线等裸露的电线。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: The input '电线等裸露的电线' is slightly redundant but clear. It tests basic character conversion ('电', '线', '触摸').

Maintainer decision: `pending`

### 38. ready-gov-kids-tornadoes-zh-hans-v1/sentence-039

Changed: `domain`

Input:

```text
如果您闻到煤气味，请告诉您的父母。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: Clear, complete sentence. Tests common vocabulary conversion (e.g., 闻, 气, 您的).

Maintainer decision: `pending`

### 39. ready-gov-kids-tornadoes-zh-hans-v1/sentence-040

Changed: `domain`

Input:

```text
您可以帮助您的父母或护理人员联系您的亲人，让他们知道您没事。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: Good sentence with multiple standard conversion points like 'help' (帮助), 'contact' (联系), and 'know' (知道).

Maintainer decision: `pending`

### 40. ready-gov-kids-tornadoes-zh-hans-v1/sentence-041

Changed: `domain`

Input:

```text
知道感到焦虑或压力是正常的。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: A simple statement. Tests conversion for 'anxiety' (焦虑) and 'pressure' (压力).

Maintainer decision: `pending`

### 41. ready-gov-kids-tornadoes-zh-hans-v1/sentence-042

Changed: `domain`

Input:

```text
每个人对压力情况的反应都不同。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: Clear statement testing conversion for 'everyone' (每个人), 'pressure' (压力), and 'reaction' (反应).

Maintainer decision: `pending`

### 42. ready-gov-kids-tornadoes-zh-hans-v1/sentence-043

Changed: `domain`

Input:

```text
照顾好自己的身体，如果您感到不安，请与您的父母或其他可信赖的成年人交谈。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 可獨立判讀的公有領域完整句；依臺灣用語與公共安全語意風險分類。

Gemini reason: A good compound sentence testing multiple common character conversions (e.g., 照顾, 身体, 与, 谈).

Maintainer decision: `pending`

### 43. zhtw-project-it-llm-social-guard-v1/it-007

Changed: `script`

Input:

```text
Docker 镜像标签 api-gateway:2026.07 不应自动升级。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Contains technical terms 'Docker', '镜像', '标签' and a version string that must not be converted. '镜像' (mirror/image) is a key term with regional variants.

Maintainer decision: `pending`

### 44. zhtw-project-it-llm-social-guard-v1/it-009

Changed: `script`

Input:

```text
命令 npm ci --ignore-scripts 会按照锁定文件安装依赖。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Contains a command 'npm ci --ignore-scripts' that must be preserved. Technical terms '锁定文件' (lock file) and '依赖' (dependencies) are key.

Maintainer decision: `pending`

### 45. zhtw-project-it-llm-social-guard-v1/it-014

Changed: `script`

Input:

```text
Terraform 变量 var.region 的默认值设为 ap-northeast-1。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Contains a tool name 'Terraform', a variable 'var.region', and a value 'ap-northeast-1' that must not be converted.

Maintainer decision: `pending`

### 46. zhtw-project-it-llm-social-guard-v1/it-025

Changed: `script, risk`

Input:

```text
WebSocket 关闭代码 1008 表示违反策略。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Standard technical sentence about WebSocket protocol codes. '关闭代码' (close code) and '违反策略' (policy violation) are key phrases.

Maintainer decision: `pending`

### 47. zhtw-project-it-llm-social-guard-v1/it-027

Changed: `script`

Input:

```text
缓存键 user:{tenant_id}:{user_id} 包含两个占位符。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: The key format string 'user:{tenant_id}:{user_id}' must be preserved. The term '缓存' (cache) has a common regional variant '快取' in Taiwan.

Maintainer decision: `pending`

### 48. zhtw-project-it-llm-social-guard-v1/it-031

Changed: `script`

Input:

```text
systemd 服务名称 worker@queue-a.service 不能省略后缀。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: The systemd service name 'worker@queue-a.service' is a literal that must not be altered. The term '后缀' (suffix) is also key.

Maintainer decision: `pending`

### 49. zhtw-project-it-llm-social-guard-v1/it-037

Changed: `script`

Input:

```text
GitHub Actions 机密名称 PROD_DEPLOY_TOKEN 不应出现在日志中。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: The secret name 'PROD_DEPLOY_TOKEN' must be preserved. The term '日志' (log) has a common regional variant '日誌' in Taiwan.

Maintainer decision: `pending`

### 50. zhtw-project-it-llm-social-guard-v1/llm-007

Changed: `risk`

Input:

```text
请比较候选答案的完整性，不要只计算关键词重合率。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Clear, complete sentence about LLM evaluation. Tests common terms like 'candidate' and 'keyword'.

Maintainer decision: `pending`

### 51. zhtw-project-it-llm-social-guard-v1/llm-009

Changed: `domain, risk`

Input:

```text
内容过滤器只保存风险类别，不保存被拦截的原始文本。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Describes a content filter's behavior. Tests conversion of IT terms like 'filter', 'intercept', and 'risk'.

Maintainer decision: `pending`

### 52. zhtw-project-it-llm-social-guard-v1/llm-020

Changed: `risk`

Input:

```text
训练资料含有重复样本时，验证结果可能过于乐观。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Standard ML concept. Good baseline for technical terms like 'training', 'samples', and 'validation'.

Maintainer decision: `pending`

### 53. zhtw-project-it-llm-social-guard-v1/llm-021

Changed: `domain`

Input:

```text
系统记录每次工具调用的参数、结果和耗时。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Describes API/tool call logging. Tests common IT terms with potential regional differences like 'call' (调用 vs 呼叫).

Maintainer decision: `pending`

### 54. zhtw-project-it-llm-social-guard-v1/llm-023

Changed: `domain, risk`

Input:

```text
回答引用法规时，不得省略例外条款和生效日期。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Legal/regulatory instruction. High-stakes domain where precision of terms like 'regulations' and 'clauses' is key.

Maintainer decision: `pending`

### 55. zhtw-project-it-llm-social-guard-v1/llm-027

Changed: `risk`

Input:

```text
知识库没有相关资料时，助手不应自行补写答案。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Describes AI assistant behavior. Good baseline for LLM-related terms like 'knowledge base' and 'assistant'.

Maintainer decision: `pending`

### 56. zhtw-project-it-llm-social-guard-v1/social-007

Changed: `risk`

Input:

```text
包裹由黑猫宅急便配送，查询号码是 9012-3456-7890。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Daily life scenario involving a proper noun (brand name). Tests if the converter correctly handles the brand name as a unit and preserves numbers.

Maintainer decision: `pending`

### 57. zhtw-project-it-llm-social-guard-v1/social-013

Changed: `risk`

Input:

```text
请导航到新北市板桥区县民大道二段 7 号。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Tests conversion of a real Taiwanese address written in Simplified Chinese. High-value test for geographic proper noun handling.

Maintainer decision: `pending`

### 58. zhtw-project-it-llm-social-guard-v1/social-024

Changed: `script`

Input:

```text
比赛结果是 Rakuten Monkeys 5 比 3 获胜。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Contains an English proper name (Rakuten Monkeys) that should be preserved.

Maintainer decision: `pending`

### 59. zhtw-project-it-llm-social-guard-v1/social-025

Changed: `script`

Input:

```text
我预约了 YouBike 2.0E，系统显示保留十分钟。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Contains a brand name with alphanumeric characters (YouBike 2.0E) that must be preserved.

Maintainer decision: `pending`

### 60. zhtw-project-it-llm-social-guard-v1/social-027

Changed: `script`

Input:

```text
餐厅订位登记为 O'Connor，共四位，晚上七点到。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Contains a non-Chinese proper name (O'Connor) that must be preserved.

Maintainer decision: `pending`

### 61. zhtw-project-it-llm-social-guard-v1/social-030

Changed: `script`

Input:

```text
群组公告引用「Terms of Service」，请保留英文标题。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Contains an English phrase ('Terms of Service') that the text explicitly requests to preserve.

Maintainer decision: `pending`

### 62. zhtw-project-it-ui-llm-formal-guard-v1/formal-002

Changed: `script`

Input:

```text
公告引用法规名称 Regulation (EU) 2024/1689。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Contains a formal alphanumeric identifier for a regulation that must not be altered.

Maintainer decision: `pending`

### 63. zhtw-project-it-ui-llm-formal-guard-v1/formal-003

Changed: `script`

Input:

```text
会议记录将议程项目列为 Item 7(b)。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Contains a standard item identifier (Item 7(b)) that must be preserved.

Maintainer decision: `pending`

### 64. zhtw-project-it-ui-llm-formal-guard-v1/formal-013

Changed: `script`

Input:

```text
运输文件使用 UN 1950 标示加压容器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Contains a United Nations identifier (UN 1950) that must be preserved.

Maintainer decision: `pending`

### 65. zhtw-project-it-ui-llm-formal-guard-v1/formal-018

Changed: `script`

Input:

```text
学术引用的 DOI 10.1000/example.2026.17 不得变更。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Contains a Digital Object Identifier (DOI) which is a standard that must never be altered.

Maintainer decision: `pending`

### 66. zhtw-project-it-ui-llm-formal-guard-v1/formal-019

Changed: `script, risk`

Input:

```text
年度报告将财政期间写为 FY2026/27。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Standard formal sentence. Contains a common simplified character '间' that needs conversion to '間'.

Maintainer decision: `pending`

### 67. zhtw-project-it-ui-llm-formal-guard-v1/it-010

Changed: `risk`

Input:

```text
对象存储返回的 x-amz-version-id 区分不同版本。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: The term '对象存储' (object storage) is specific to mainland China usage. The idiomatic term in Taiwan is '物件儲存'. '返回' should also be converted to '傳回' or '回傳'. The header 'x-amz-version-id' must be preserved.

Maintainer decision: `pending`

### 68. zhtw-project-it-ui-llm-formal-guard-v1/it-014

Changed: `risk`

Input:

```text
运行 go test ./... -race 检查并发访问问题。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Contains mainland China technical terms. '运行' (run) should be '執行', and '并发' (concurrency) should be '並行'. The Go command must be preserved.

Maintainer decision: `pending`

### 69. zhtw-project-it-ui-llm-formal-guard-v1/it-016

Changed: `risk`

Input:

```text
HTTP/2 连接收到 GOAWAY 后不会再建立新的串流。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Tests standard character conversions in a technical context ('连接' -> '連接', '后' -> '後'). '串流' (stream) is a shared term and should not be altered. 'GOAWAY' must be preserved.

Maintainer decision: `pending`

### 70. zhtw-project-it-ui-llm-formal-guard-v1/it-026

Changed: `risk`

Input:

```text
任务队列把 dead-letter topic 设为 orders.failed。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: The term '任务队列' (task queue) uses '队列', common in mainland China. The idiomatic Taiwan term is '任務佇列'. Technical strings 'dead-letter topic' and 'orders.failed' must be preserved.

Maintainer decision: `pending`

### 71. zhtw-project-it-ui-llm-formal-guard-v1/llm-021

Changed: `risk`

Input:

```text
评分器将 exact、partial 与 incorrect 设为枚举值。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: The term '枚举值' (enum value) is mainland China terminology. The standard term in Taiwan is '列舉值'. '评分器' (scorer) is also less common in Taiwan than '評分程式' or '評估器'.

Maintainer decision: `pending`

### 72. zhtw-project-it-ui-llm-formal-guard-v1/llm-023

Changed: `risk`

Input:

```text
推理追踪只记录 trace_summary，不保存隐藏内容。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Sentence from the LLM domain that tests standard character conversions: '追踪' -> '追蹤', '记录' -> '記錄', '隐藏' -> '隱藏'. The term 'trace_summary' must be preserved.

Maintainer decision: `pending`

### 73. zhtw-project-it-ui-llm-formal-guard-v1/ui-004

Changed: `script`

Input:

```text
输入框会将 autocomplete 属性设为 current-password。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Tests if the converter correctly ignores the technical attributes 'autocomplete' and 'current-password'.

Maintainer decision: `pending`

### 74. zhtw-project-it-ui-llm-formal-guard-v1/ui-009

Changed: `script, risk`

Input:

```text
快速键 Meta+K 在 macOS 上打开命令菜单。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Tests terminology conversion ('快速键' to '快捷鍵', '命令菜单' to '命令選單') and guards technical terms ('Meta+K', 'macOS').

Maintainer decision: `pending`

### 75. zhtw-project-it-ui-llm-formal-guard-v1/ui-010

Changed: `risk`

Input:

```text
日期选择器的最小值为 2026-01-01。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Tests if the converter correctly ignores the date string '2026-01-01'.

Maintainer decision: `pending`

### 76. zhtw-project-it-ui-llm-formal-guard-v1/ui-013

Changed: `script`

Input:

```text
载入失败时显示 request_id 供客服查询。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Tests if the converter correctly ignores the technical identifier 'request_id'.

Maintainer decision: `pending`

### 77. zhtw-project-it-ui-llm-formal-guard-v1/ui-016

Changed: `script, risk`

Input:

```text
表单验证消息保留字段键 billing_address.postal_code。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Tests terminology conversion ('字段键' to '欄位鍵') and guards the technical string 'billing_address.postal_code'.

Maintainer decision: `pending`

### 78. zhtw-project-it-ui-llm-formal-guard-v1/ui-020

Changed: `script`

Input:

```text
图表图例将 p50、p95 与 p99 视为指标名称。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Tests if the converter correctly ignores the technical metric names 'p50', 'p95', and 'p99'.

Maintainer decision: `pending`

### 79. zhtw-project-it-ui-llm-formal-guard-v1/ui-022

Changed: `risk`

Input:

```text
上传进度达到 100% 后按钮才恢复可用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: A baseline case for common character conversions, while guarding against converting '100%'.

Maintainer decision: `pending`

### 80. zhtw-project-it-ui-llm-formal-guard-v1/ui-024

Changed: `script, risk`

Input:

```text
对话框的初始焦点落在 data-autofocus 元素。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Tests terminology conversion ('对话框' to '對話方塊') and guards the technical attribute 'data-autofocus'.

Maintainer decision: `pending`

### 81. zhtw-project-llm-it-ui-baseline-v1/it-005

Changed: `risk`

Input:

```text
系统每天检查备份文件是否能够正常还原。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: A standard IT sentence. Key conversion test is SC '文件' (wénjiàn) to TW '檔案' (dǎng'àn) for 'file'. '还原' (huányuán - restore) is used in both, but TW also uses '還原' or '回復'.

Maintainer decision: `pending`

### 82. zhtw-project-llm-it-ui-baseline-v1/it-009

Changed: `risk`

Input:

```text
队列中的任务会依照建立时间依序处理。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Classic SC vs TW terminology gap. SC '队列' (duìliè - queue) should be converted to TW '佇列' (zhùliè). '任务' (rènwù - task) is a standard character conversion to '任務'.

Maintainer decision: `pending`

### 83. zhtw-project-llm-it-ui-baseline-v1/llm-033

Changed: `risk`

Input:

```text
检索片段会按照与问题的相关程度排序。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: A standard LLM/RAG sentence. It tests common character conversions for technical terms like '检索' (retrieval) -> '檢索', '相关' (relevance) -> '相關', and '问题' (question) -> '問題'.

Maintainer decision: `pending`

### 84. zhtw-project-llm-social-baseline-v1/llm-018

Changed: `risk`

Input:

```text
请比较三个候选答案，并说明选择依据和剩余疑点。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: A straightforward formal instruction. Serves as a good baseline test for a wide range of common character conversions in a single sentence, such as '说明' -> '說明', '选择' -> '選擇', '依据' -> '依據', and '疑点' -> '疑點'.

Maintainer decision: `pending`

### 85. zhtw-project-llm-social-baseline-v1/llm-026

Changed: `risk`

Input:

```text
请将长文分成五个主题，每个主题附上一句摘要。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: A standard instruction that is a good baseline test for common character conversions, particularly '请' -> '請' and '长' -> '長'.

Maintainer decision: `pending`

### 86. zhtw-project-llm-social-baseline-v1/social-002

Changed: `risk`

Input:

```text
这家店周末人很多，最好先在网上预约。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 可獨立判讀的 project-original 完整句；依領域、識別碼保留與臺灣用語風險分類。

Gemini reason: Tests a common daily-life lexical gap. The SC term '网上' (wǎngshang - online) should be correctly converted to the standard TW equivalent '網路上' (wǎnglùshang).

Maintainer decision: `pending`
