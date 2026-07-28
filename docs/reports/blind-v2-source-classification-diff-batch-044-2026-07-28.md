<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 044 (2026-07-28)

Status: advisory only; maintainer decisions pending

Packet SHA-256: `ff3cdad5a9056ad0eefffd1ba04a6fc90239a9003a9de45fc71c2e2926a439a1`
Cases: 96
Exact Codex/Gemini classifications: 41
Maintainer review queue: 55

Field differences:

- Eligibility: 1
- Script: 10
- Domain: 27
- Risk: 34

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

Neither advisory is auto-preferred. Codex must synthesize the differences before maintainer confirmation; no classification in this report has been written into the candidate pool.

## Review Queue

### 01. flores-200-zho-hans-v1/dev-0123

Changed: `risk`

Input:

```text
位于肯尼亚内罗毕的美国大使馆发出了警告称，“索马里极端分子”正策划在肯尼亚和埃塞俄比亚发动自杀性炸弹袭击。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 可獨立判讀的 FLORES 句子；依新聞、社會或高風險語境與專名保留風險分類。

Gemini reason: Contains multiple geographic names (Kenya, Nairobi, Ethiopia) that require translation normalization for Taiwan ('肯亞', '奈洛比', '衣索比亞').

Maintainer decision: `pending`

### 02. flores-200-zho-hans-v1/dev-0139

Changed: `domain`

Input:

```text
人如果吸入通过风和海浪进入空气的受污染水气，就可能受到影响。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的 FLORES 句子；依新聞、社會或高風險語境與專名保留風險分類。

Gemini reason: This sentence consists of common words that should convert directly, serving as a good baseline test.

Maintainer decision: `pending`

### 03. flores-200-zho-hans-v1/dev-0350

Changed: `risk`

Input:

```text
科学家目前致力打造一种可通过相同的方式产生能量的反应堆。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 可獨立判讀的 FLORES 句子；依新聞、社會或高風險語境與專名保留風險分類。

Gemini reason: The term '打造' is a potential candidate gap; '建造' or '研發' might be more idiomatic in Taiwan for a scientific context.

Maintainer decision: `pending`

### 04. flores-200-zho-hans-v1/dev-0583

Changed: `domain`

Input:

```text
龙卷风能将树木连根拔起，将建筑物上的木板撕下，把汽车抛向天空。龙卷风中的百分之二最为猛烈，能持续肆虐三小时以上。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的 FLORES 句子；依新聞、社會或高風險語境與專名保留風險分類。

Gemini reason: Descriptive sentence with standard vocabulary. Straightforward conversion.

Maintainer decision: `pending`

### 05. flores-200-zho-hans-v1/dev-0648

Changed: `risk`

Input:

```text
我们中有很多人，都发现自己观看的电视节目在告诉我们某种过程或经验，但我们却永远不会参与或应用这些知识。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | medium | - |

Codex reason: 可獨立判讀的 FLORES 句子；依新聞、社會或高風險語境與專名保留風險分類。

Gemini reason: Slight potential candidate gap with '应用', where '運用' might be more idiomatic for applying knowledge in Taiwan.

Maintainer decision: `pending`

### 06. flores-200-zho-hans-v1/devtest-0179

Changed: `domain, risk`

Input:

```text
跳羚队以五连败收官。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 FLORES 句子；依新聞、社會或高風險語境與專名保留風險分類。

Gemini reason: Proper noun '跳羚队' and sports jargon '收官' are key points, but both are used similarly across locales.

Maintainer decision: `pending`

### 07. flores-200-zho-hans-v1/devtest-0196

Changed: `domain`

Input:

```text
这名摄影师被送往加州大学洛杉矶分校罗纳德·里根医疗中心，其后不治。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | medium | - |

Codex reason: 可獨立判讀的 FLORES 句子；依新聞、社會或高風險語境與專名保留風險分類。

Gemini reason: Contains multiple proper nouns (university, medical center, person's name) whose translations might have official or conventional variants in Taiwan.

Maintainer decision: `pending`

### 08. flores-200-zho-hans-v1/devtest-0590

Changed: `risk`

Input:

```text
这些夫妇可能会为他们的孩子制定收养计划。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 可獨立判讀的 FLORES 句子；依新聞、社會或高風險語境與專名保留風險分類。

Gemini reason: Daily life topic, potential for regional term normalization (e.g., plan, adoption).

Maintainer decision: `pending`

### 09. flores-200-zho-hans-v1/devtest-1002

Changed: `risk`

Input:

```text
更传统的教堂常常在复活节周末的周六晚上举行复活节守夜活动，会众通常在午夜钟声敲响之时涌入庆典，庆祝基督的复活。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 FLORES 句子；依新聞、社會或高風險語境與專名保留風險分類。

Gemini reason: Description of a religious event with specific terms.

Maintainer decision: `pending`

### 10. ftc-heads-up-simplified-v1/sentence-005

Changed: `domain, risk`

Input:

```text
通过交谈，您可以让孩子知道一旦他们犯了错误，有可以信赖的成年人会帮助他们。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 可獨立判讀的公共領域句子；依臺灣用語、正式語境與安全語意風險分類。

Gemini reason: General advice, potential for minor regional term differences.

Maintainer decision: `pending`

### 11. ftc-heads-up-simplified-v1/sentence-031

Changed: `domain`

Input:

```text
由于在网上看不到别人的面部表情、肢体语言或其他视觉线索，你可能会发布或说出不会当面说的话。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 可獨立判讀的公共領域句子；依臺灣用語、正式語境與安全語意風險分類。

Gemini reason: Online communication advice with terms that have common regional variants (e.g., online, post).

Maintainer decision: `pending`

### 12. ftc-heads-up-simplified-v1/sentence-052

Changed: `domain`

Input:

```text
保存记录并向可以信赖的成年人求助。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的公共領域句子；依臺灣用語、正式語境與安全語意風險分類。

Gemini reason: Instructional sentence from a guide.

Maintainer decision: `pending`

### 13. ftc-heads-up-simplified-v1/sentence-083

Changed: `domain`

Input:

```text
你的网上账户中有大量的个人信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 可獨立判讀的公共領域句子；依臺灣用語、正式語境與安全語意風險分類。

Gemini reason: The terms '网上' (online) and '信息' (information) are common in Mainland China but '網路上' and '資訊' are preferred in Taiwan.

Maintainer decision: `pending`

### 14. ftc-how-to-avoid-scam-simplified-v1/sentence-008

Changed: `domain`

Input:

```text
诈骗者希望您在有时间思考之前就采取行动。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的公共領域句子；依臺灣用語、正式語境與安全語意風險分類。

Gemini reason: This is a straightforward sentence requiring standard character conversion.

Maintainer decision: `pending`

### 15. ftc-how-to-avoid-scam-simplified-v1/sentence-011

Changed: `domain`

Input:

```text
他们可能会说您的计算机即将损坏。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 可獨立判讀的公共領域句子；依臺灣用語、正式語境與安全語意風險分類。

Gemini reason: The term '计算机' (computer) is primarily used in Mainland China, while Taiwan uses '電腦'.

Maintainer decision: `pending`

### 16. ftc-identity-theft-simplified-v1/sentence-008

Changed: `risk`

Input:

```text
您是否收到了您从未开立过账户的账单？
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的公共領域句子；依臺灣用語、正式語境與安全語意風險分類。

Gemini reason: The phrasing is standard and mainly requires character-level conversion.

Maintainer decision: `pending`

### 17. ftc-identity-theft-simplified-v1/sentence-011

Changed: `risk`

Input:

```text
将您的出生证明、社会保障卡和账户对账单等正式文件保存在安全的地方。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | medium | - |

Codex reason: 可獨立判讀的公共領域句子；依臺灣用語、正式語境與安全語意風險分類。

Gemini reason: '社会保障卡' (Social Security card) is a specific US entity. Its translation should be handled carefully to avoid misinterpretation, making it an over-conversion risk.

Maintainer decision: `pending`

### 18. ftc-identity-theft-simplified-v1/sentence-017

Changed: `domain`

Input:

```text
为提供多重身份验证功能的帐户添加多重身份验证，例如通过短信获取访问代码。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 可獨立判讀的公共領域句子；依臺灣用語、正式語境與安全語意風險分類。

Gemini reason: Contains Mainland China terms such as '短信' (SMS/text message), for which Taiwan commonly uses '簡訊'.

Maintainer decision: `pending`

### 19. ftc-identity-theft-simplified-v1/sentence-019

Changed: `risk`

Input:

```text
仔细查看您未购买商品的费用或意外账单。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的公共領域句子；依臺灣用語、正式語境與安全語意風險分類。

Gemini reason: Standard sentence with common vocabulary that requires basic character conversion.

Maintainer decision: `pending`

### 20. ready-gov-earthquakes-zh-hans-v1/sentence-002

Changed: `domain, risk`

Input:

```text
虽然可能在没有警告的情况下在任何地方发生，但是，地震风险较高的地区包括阿拉斯加、加州、夏威夷、俄勒冈、波多黎各、华盛顿和整个密西西比河谷。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的公共領域句子；依臺灣用語、正式語境與安全語意風險分類。

Gemini reason: This sentence contains a list of proper nouns (place names) that should be preserved during character conversion, posing an over-conversion risk.

Maintainer decision: `pending`

### 21. ready-gov-floods-zh-hans-v1/sentence-027

Changed: `risk`

Input:

```text
清理排水管和檐沟。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的公共領域句子；依臺灣用語、正式語境與安全語意風險分類。

Gemini reason: Standard instruction.

Maintainer decision: `pending`

### 22. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-007

Changed: `risk`

Input:

```text
并非所有的山体滑坡都很快。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 可獨立判讀的公共領域句子；依臺灣用語、正式語境與安全語意風險分類。

Gemini reason: '山体滑坡' is a mainland term; Taiwan often uses '山崩'.

Maintainer decision: `pending`

### 23. ready-gov-radiation-zh-hans-v1/sentence-005

Changed: `risk`

Input:

```text
在任何辐射紧急情况下保持安全的最佳方法是进入室内，待在室内并保持关注。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 可獨立判讀的公共領域句子；依臺灣用語、正式語境與安全語意風險分類。

Gemini reason: '保持关注' is a formal mainland phrase that might be localized to '保持留意' or '注意收聽' in Taiwan.

Maintainer decision: `pending`

### 24. ready-gov-radiation-zh-hans-v1/sentence-053

Changed: `script, risk`

Input:

```text
遵循CDC关于为自己和他人消除核污染的指南。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的公共領域句子；依臺灣用語、正式語境與安全語意風險分類。

Gemini reason: Standard simplified Chinese sentence, appears to be public safety guidance.

Maintainer decision: `pending`

### 25. ready-gov-tornadoes-zh-hans-v1/sentence-001

Changed: `domain`

Input:

```text
龙卷风是剧烈旋转的气柱，从雷暴延伸到地面，能摧毁建筑物，翻转汽车，并产生致命的飞溅碎片。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 可獨立判讀的公共領域句子；依臺灣用語、正式語境與安全語意風險分類。

Gemini reason: Standard meteorological description in simplified Chinese.

Maintainer decision: `pending`

### 26. ready-gov-tornadoes-zh-hans-v1/sentence-018

Changed: `domain, risk`

Input:

```text
气象员能预测什么情况最可能发生龙卷风。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 可獨立判讀的公共領域句子；依臺灣用語、正式語境與安全語意風險分類。

Gemini reason: The term '气象员' may require regional adaptation in Taiwan (e.g., '氣象預報員').

Maintainer decision: `pending`

### 27. ready-gov-winter-weather-zh-hans-v1/sentence-008

Changed: `eligible, domain, risk`

Input:

```text
提醒公众注意可能发生暴风雪、大雪、强冻雨或大雨夹雪。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 句子僅說明「提醒公眾」但缺少發出提醒的主體，離開前文後無法穩定裁決。

Gemini reason: Standard weather alert terminology in simplified Chinese.

Maintainer decision: `pending`

### 28. ready-gov-winter-weather-zh-hans-v1/sentence-009

Changed: `script, domain, risk`

Input:

```text
冬季风暴观察通常在冬季风暴开始前 12 至 48 小时发布。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的公共領域句子；依臺灣用語、正式語境與安全語意風險分類。

Gemini reason: Contains numerals which should be preserved. '冬季风暴观察' might be a specific term.

Maintainer decision: `pending`

### 29. ready-gov-winter-weather-zh-hans-v1/sentence-012

Changed: `risk`

Input:

```text
收听紧急信息和警示。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 可獨立判讀的公共領域句子；依臺灣用語、正式語境與安全語意風險分類。

Gemini reason: The word '信息' (xìnxī) is common in mainland China, while '資訊' (zīxùn) is standard in Taiwan for 'information'.

Maintainer decision: `pending`

### 30. vscode-loc-zh-hans-v1/entry-1bc2d120c0821a7f

Changed: `risk`

Input:

```text
自动换行(&&W)
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 VS Code UI 字串；依臺灣介面用語與占位符保留風險分類。

Gemini reason: UI menu item with a keyboard mnemonic that should be preserved.

Maintainer decision: `pending`

### 31. vscode-loc-zh-hans-v1/entry-2c85090743bfc31a

Changed: `risk`

Input:

```text
语音录制已停止
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 可獨立判讀的 VS Code UI 字串；依臺灣介面用語與占位符保留風險分類。

Gemini reason: For voice context, '录制' (recording) might be better localized as '錄音' in Taiwan.

Maintainer decision: `pending`

### 32. vscode-loc-zh-hans-v1/entry-374e2ac3e2f1c83c

Changed: `domain`

Input:

```text
省略语言时，"contributes.{0}.path" 的值必须为一个 ".code-snippets" 文件。提供的值: {1}
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 VS Code UI 字串；依臺灣介面用語與占位符保留風險分類。

Gemini reason: Technical error message. Code paths and placeholders like 'contributes.{0}.path' must be preserved.

Maintainer decision: `pending`

### 33. vscode-loc-zh-hans-v1/entry-633aa45197b3dce7

Changed: `domain, risk`

Input:

```text
视图的类型。对于基于树状视图的视图，这可以是 "tree"，对于基于 Web 视图的视图，这可以是 "webview"。默认值为 "tree"。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 VS Code UI 字串；依臺灣介面用語與占位符保留風險分類。

Gemini reason: Technical description where keywords like 'tree' and 'webview' are identifiers and must not be translated.

Maintainer decision: `pending`

### 34. vscode-loc-zh-hans-v1/entry-8c957017a839953e

Changed: `risk`

Input:

```text
继续操作前，请确保你信任该代码。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 可獨立判讀的 VS Code UI 字串；依臺灣介面用語與占位符保留風險分類。

Gemini reason: Standard UI security prompt. The term '代码' (code) is a key candidate for regional normalization, e.g., to '程式碼' in Taiwan.

Maintainer decision: `pending`

### 35. vscode-loc-zh-hans-v1/entry-af83496e04575bf7

Changed: `risk`

Input:

```text
按名称排列文件和文件夹。两者穿插显示。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 可獨立判讀的 VS Code UI 字串；依臺灣介面用語與占位符保留風險分類。

Gemini reason: Standard file sorting UI text. Terms like '文件' (file) and '文件夹' (folder) are common and should convert straightforwardly.

Maintainer decision: `pending`

### 36. vscode-loc-zh-hans-v1/entry-c19d884c9e5923ca

Changed: `domain, risk`

Input:

```text
执行单元格和焦点容器
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 VS Code UI 字串；依臺灣介面用語與占位符保留風險分類。

Gemini reason: Technical command label. Terms like '单元格' (cell) and '容器' (container) are established technical jargon that should be preserved, converting only the characters.

Maintainer decision: `pending`

### 37. vscode-loc-zh-hans-v1/entry-d8563114f52568ca

Changed: `script, risk`

Input:

```text
属性“{0}”设置为“{1}”。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 可獨立判讀的 VS Code UI 字串；依臺灣介面用語與占位符保留風險分類。

Gemini reason: Standard property-setting message with placeholders. No significant regional variance expected.

Maintainer decision: `pending`

### 38. vscode-loc-zh-hans-v1/entry-e5adeb3575e96524

Changed: `script`

Input:

```text
[['''{0}']] 中的编辑已被拒绝
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | no | null | null | high | malformed_placeholder, unclear_context |

Codex reason: 字串含多層括號與引號殘留，無法確認原始 UI 文字和占位符邊界。

Gemini reason: The placeholder construct [[['''{0}''']] appears malformed or unrendered, making the sentence ineligible for a quality review.

Maintainer decision: `pending`

### 39. vscode-loc-zh-hans-v1/entry-ec63ec66cb3a69b7

Changed: `risk`

Input:

```text
假定未连接屏幕阅读器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 可獨立判讀的 VS Code UI 字串；依臺灣介面用語與占位符保留風險分類。

Gemini reason: Accessibility text. '屏幕阅读器' (screen reader) is a Mainland China term; Taiwan uses '螢幕閱讀器'. This requires regional adaptation.

Maintainer decision: `pending`

### 40. vscode-loc-zh-hans-v1/entry-ff6d9986f54d171a

Changed: `script, risk`

Input:

```text
已找到 {0}
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 可獨立判讀的 VS Code UI 字串；依臺灣介面用語與占位符保留風險分類。

Gemini reason: Simple, standard search result notification with a placeholder. Universal phrasing.

Maintainer decision: `pending`

### 41. zhtw-project-it-llm-social-guard-v1/it-021

Changed: `script`

Input:

```text
版本范围 >=3.2.0,<4.0.0 必须原样写入清单。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Project-original 情境可獨立判讀；識別碼、專名、引文或語意限制不得改寫。

Gemini reason: The version range string '>=3.2.0,<4.0.0' must be preserved exactly.

Maintainer decision: `pending`

### 42. zhtw-project-it-llm-social-guard-v1/it-034

Changed: `script`

Input:

```text
发布说明引用 CVE-2026-12345 时要保留完整编号。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Project-original 情境可獨立判讀；識別碼、專名、引文或語意限制不得改寫。

Gemini reason: Technical instruction where the CVE identifier must be preserved.

Maintainer decision: `pending`

### 43. zhtw-project-it-llm-social-guard-v1/llm-017

Changed: `risk`

Input:

```text
自动评分器只能检查结构，不能代替事实核查。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: Project-original 情境可獨立判讀；識別碼、專名、引文或語意限制不得改寫。

Gemini reason: LLM context. '事实核查' should be localized to '事實查核'.

Maintainer decision: `pending`

### 44. zhtw-project-it-llm-social-guard-v1/llm-025

Changed: `risk`

Input:

```text
模型无法读取本地文件，除非用户主动上传。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: Project-original 情境可獨立判讀；識別碼、專名、引文或語意限制不得改寫。

Gemini reason: A standard LLM-related sentence requiring basic character conversion and term localization (e.g., 用户->使用者).

Maintainer decision: `pending`

### 45. zhtw-project-it-llm-social-guard-v1/llm-030

Changed: `risk`

Input:

```text
提示内容只允许改写语气，数字与引用必须保持不变。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: Project-original 情境可獨立判讀；識別碼、專名、引文或語意限制不得改寫。

Gemini reason: Instruction for an LLM. '提示内容' is a mainland-specific term that needs localization.

Maintainer decision: `pending`

### 46. zhtw-project-it-llm-social-guard-v1/social-010

Changed: `script`

Input:

```text
这杯饮料点的是五十岚的「四季春珍波椰」。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: Project-original 情境可獨立判讀；識別碼、專名、引文或語意限制不得改寫。

Gemini reason: Contains a Taiwanese brand name (五十岚) and product name in traditional characters that must be preserved.

Maintainer decision: `pending`

### 47. zhtw-project-it-llm-social-guard-v1/social-020

Changed: `script, risk`

Input:

```text
台风「青鸟」接近时，学校会通过官方渠道通知停课。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: Project-original 情境可獨立判讀；識別碼、專名、引文或語意限制不得改寫。

Gemini reason: Requires regional term localization ('台风' -> '颱風') while preserving the proper name '青鸟'.

Maintainer decision: `pending`

### 48. zhtw-project-it-llm-social-guard-v1/social-022

Changed: `domain`

Input:

```text
请确认收件人是 Wu, Mei-Ling，不要调整英文姓名顺序。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Project-original 情境可獨立判讀；識別碼、專名、引文或語意限制不得改寫。

Gemini reason: High-stakes context where preserving the exact Romanized name 'Wu, Mei-Ling' is critical.

Maintainer decision: `pending`

### 49. zhtw-project-it-ui-llm-formal-guard-v1/formal-010

Changed: `script, domain`

Input:

```text
财务报表将科目代码 1100-03 列在附注中。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Project-original 情境可獨立判讀；識別碼、專名、引文或語意限制不得改寫。

Gemini reason: Financial statement context with an account code 1100-03 that must be preserved.

Maintainer decision: `pending`

### 50. zhtw-project-it-ui-llm-formal-guard-v1/formal-011

Changed: `domain`

Input:

```text
专利说明书引用序列表文件 SequenceListing.xml。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: Project-original 情境可獨立判讀；識別碼、專名、引文或語意限制不得改寫。

Gemini reason: Patent document context with a filename SequenceListing.xml that must be preserved.

Maintainer decision: `pending`

### 51. zhtw-project-it-ui-llm-formal-guard-v1/llm-016

Changed: `domain, risk`

Input:

```text
缓存命中事件的类型为 prompt_cache.hit。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Project-original 情境可獨立判讀；識別碼、專名、引文或語意限制不得改寫。

Gemini reason: Mainland term '缓存' requires normalization. Identifier 'prompt_cache.hit' must be preserved.

Maintainer decision: `pending`

### 52. zhtw-project-it-ui-llm-formal-guard-v1/llm-017

Changed: `domain, risk`

Input:

```text
测试夹具要求输出字面值 null，而不是空字符串。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: Project-original 情境可獨立判讀；識別碼、專名、引文或語意限制不得改寫。

Gemini reason: Mainland IT term '测试夹具'. Keyword 'null' must be preserved.

Maintainer decision: `pending`

### 53. zhtw-project-it-ui-llm-formal-guard-v1/llm-018

Changed: `domain`

Input:

```text
审核队列以 needs_human_review 标记低信心案例。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Project-original 情境可獨立判讀；識別碼、專名、引文或語意限制不得改寫。

Gemini reason: Identifier 'needs_human_review' must be preserved.

Maintainer decision: `pending`

### 54. zhtw-project-it-ui-llm-formal-guard-v1/llm-020

Changed: `domain`

Input:

```text
函数调用结果使用 tool_call_id 对应原始请求。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Project-original 情境可獨立判讀；識別碼、專名、引文或語意限制不得改寫。

Gemini reason: Identifier 'tool_call_id' must be preserved.

Maintainer decision: `pending`

### 55. zhtw-project-it-ui-llm-formal-guard-v1/llm-025

Changed: `domain`

Input:

```text
基准报告以 win_rate_paired 表示成对胜率。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: Project-original 情境可獨立判讀；識別碼、專名、引文或語意限制不得改寫。

Gemini reason: Identifier 'win_rate_paired' must be preserved.

Maintainer decision: `pending`
