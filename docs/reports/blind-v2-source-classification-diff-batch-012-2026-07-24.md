<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 012 (2026-07-24)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `be7a588478ff27dbcf26fbc3e693469912e9f59573d3fe354f83caf86906651c`
Cases: 100
Exact Codex/Gemini classifications: 49
Maintainer review queue: 51

Field differences:

- Eligibility: 1
- Script: 0
- Domain: 25
- Risk: 34

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

The maintainer resolved all 51 advisory disagreements and batch-confirmed the 49 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. ftc-heads-up-simplified-v1/sentence-001

Changed: `domain, risk`

Input:

```text
要在生活中帮助您的孩子安全上网，当心：停一停、想一想、问一问。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 包含「上网」，在台灣通常說「上網」，字形雖同但為地域用語。整體為網路安全宣導內容。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 02. ftc-heads-up-simplified-v1/sentence-002

Changed: `domain`

Input:

```text
有一些想法可以帮助您与他们开始对话。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 標準書面語，無特殊轉換風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 03. ftc-heads-up-simplified-v1/sentence-003

Changed: `domain`

Input:

```text
选择一节共同阅读，了解如何谨慎分享、友好在线、防范网络欺凌以及在线保护他们（和自己）的个人信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 包含「在线」、「网络欺凌」、「信息」，在台灣多用「線上」、「網路霸凌」、「資訊」，有地域化轉換需求。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 04. ftc-heads-up-simplified-v1/sentence-004

Changed: `domain`

Input:

```text
这些工具可以帮助您向孩子们展示如何做出正确的选择、负责任地使用科技。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 「科技」一詞兩岸通用，風險較低。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 05. ftc-heads-up-simplified-v1/sentence-006

Changed: `risk`

Input:

```text
上网是生活的一部分。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 「上网」為大陸用語，台灣多稱「上網」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 06. ftc-heads-up-simplified-v1/sentence-008

Changed: `risk`

Input:

```text
但在网上发布内容、娱乐和交流时会面临风险。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 「内容」是需要轉換的地域詞彙，對應台灣的「內容」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 07. ftc-heads-up-simplified-v1/sentence-010

Changed: `domain, risk`

Input:

```text
无论手指在键盘、手机或平板电脑上移动得有多快，头脑和时间才是避免网络风险最好的工具。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 包含「键盘」、「手机」、「平板电脑」、「网络」，皆為 IT 術語，在台灣有特定對應說法如「鍵盤」、「手機」、「平板」、「網路」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 08. ftc-heads-up-simplified-v1/sentence-011

Changed: `domain, risk`

Input:

```text
停一停，认真想一想面临的情况可以帮助保护你自己、朋友和家人、你的账户和设备。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 包含「账户」和「设备」，台灣多用「帳號」和「裝置」，需要地域化轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 09. ftc-heads-up-simplified-v1/sentence-012

Changed: `risk`

Input:

```text
否则，最终可能会分享过多信息，让自己或他人尴尬，产生电脑故障，或者与戴着假面具的人交谈。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 包含「信息」和「电脑」，對應台灣的「資訊」和「電腦」，有轉換需求。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 10. ftc-heads-up-simplified-v1/sentence-013

Changed: `domain`

Input:

```text
想要完全控制谁可以看到你的个人资料、图片、视频或文本是不可能的 — 即使用了在内容被查看后或在 24 小时内将其删除的隐私设置或应用软件也不可能完全控制。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 包含「个人资料」、「视频」、「文本」、「隐私设置」、「应用软件」，皆是需要高度地域化的 IT 術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 11. ftc-heads-up-simplified-v1/sentence-023

Changed: `risk`

Input:

```text
发贴前停一停，想一想。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 「发贴」在台灣多稱「發文」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 12. ftc-heads-up-simplified-v1/sentence-025

Changed: `domain, risk`

Input:

```text
发送色情信息：不要这样做。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 討論「Sexting」的敏感話題，屬於高風險內容，但用詞直接。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 13. ftc-heads-up-simplified-v1/sentence-026

Changed: `domain, risk`

Input:

```text
你可能在学校或者新闻中听到过人们“发送色情信息” — 用其手机发裸照。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 同前，涉及「Sexting」，高風險內容。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 14. ftc-heads-up-simplified-v1/sentence-027

Changed: `domain`

Input:

```text
绝对不能这么做。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 簡單警告句，風險低。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 15. ftc-heads-up-simplified-v1/sentence-028

Changed: `domain`

Input:

```text
创建、转发甚至保存色情照片、视频或信息会使你面临失去友谊和声誉的风险。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 包含「视频」，台灣用「影片」。此句涉及法律與個人聲譽，風險高。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 16. ftc-heads-up-simplified-v1/sentence-029

Changed: `domain`

Input:

```text
更糟的是，你的行为还可能违法。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 涉及法律後果，為高風險內容。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 17. ftc-heads-up-simplified-v1/sentence-030

Changed: `domain`

Input:

```text
根据美国卫生部长的说法，使用社交媒体可能会对你造成伤害，具体取决于在社交平台上花费的时间，看到的内容类型，及其对人的健康至关重要的睡眠或锻炼等活动的干扰程度。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 「社交媒体」、「平台」、「内容」皆為大陸用語，台灣說「社群媒體」、「平台」、「內容」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 18. ftc-heads-up-simplified-v1/sentence-035

Changed: `risk`

Input:

```text
在发送消息前，问自己: “其他人会对这条消息有什么感觉？”
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 通用問句，無特別地域詞彙。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 19. ftc-heads-up-simplified-v1/sentence-038

Changed: `domain`

Input:

```text
不要全部使用大写字母，也不要用一连串的感叹号或粗大字体。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 描述文字格式，屬於 UI/UX 指導，用詞直接。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 20. ftc-heads-up-simplified-v1/sentence-040

Changed: `risk`

Input:

```text
不要把所有东西都放在群聊里。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 「群聊」在台灣也普遍使用，或稱「群組聊天」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 21. ftc-heads-up-simplified-v1/sentence-041

Changed: `risk`

Input:

```text
在群发消息或点击“全部回复”前，停下来想一想：谁需要看到这条消息？
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 「群发」和「全部回复」是電子郵件/訊息功能，用詞接近。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 22. ftc-heads-up-simplified-v1/sentence-043

Changed: `risk`

Input:

```text
如果看到朋友发送了轻率或不安全的内容，提醒他们。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 「内容」對應「內容」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 23. ftc-heads-up-simplified-v1/sentence-046

Changed: `domain`

Input:

```text
大部分应用软件和平台都有报告有危险或不当行为的途径。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 「应用软件」和「平台」是需轉換的 IT 詞彙。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 24. ftc-heads-up-simplified-v1/sentence-053

Changed: `domain`

Input:

```text
大部分应用软件和平台都有报告不当或危险行为的工具。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 「应用软件」和「平台」是需轉換的 IT 詞彙。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 25. ftc-heads-up-simplified-v1/sentence-055

Changed: `domain`

Input:

```text
欺凌还可能导致校方或警方的介入。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 涉及校方和警方，屬於高風險內容。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 26. ftc-heads-up-simplified-v1/sentence-056

Changed: `risk`

Input:

```text
如果你目睹了网络欺凌，想办法加以阻止 — 勇敢出面主持公道。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 「网络欺凌」對應「網路霸凌」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 27. ftc-heads-up-simplified-v1/sentence-059

Changed: `domain, risk`

Input:

```text
通过以下步骤确保痕迹不会导致泄露不想分享的信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的日常網路與社群安全文字。

Gemini reason: 「信息」對應「資訊」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 28. ftc-heads-up-simplified-v1/sentence-061

Changed: `risk`

Input:

```text
它可帮助限制谁能看到你所在的位置、所发的帖子以及谁能与你联系。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的帳號、隱私或裝置安全文字。

Gemini reason: 用詞直接，風險較低。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 29. ftc-heads-up-simplified-v1/sentence-066

Changed: `risk`

Input:

```text
如果不需要，关闭位置共享。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的帳號、隱私或裝置安全文字。

Gemini reason: 「位置共享」是 IT 功能，但詞語本身直接。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 30. ftc-heads-up-simplified-v1/sentence-068

Changed: `risk`

Input:

```text
如果不想每次自拍都让所有人看到自己的位置，请关闭手机摄像头上的位置功能。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的帳號、隱私或裝置安全文字。

Gemini reason: 「自拍」和「手机」在台灣也使用，但「摄像头」是大陸用語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 31. ftc-heads-up-simplified-v1/sentence-070

Changed: `domain`

Input:

```text
将网友限制为自己生活中认识的人。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的帳號、隱私或裝置安全文字。

Gemini reason: 「网友」一詞台灣也用，或稱「網友」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 32. ftc-heads-up-simplified-v1/sentence-072

Changed: `domain, risk`

Input:

```text
如果不小心，可能会与陌生人分享个人信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的帳號、隱私或裝置安全文字。

Gemini reason: 「信息」對應「資訊」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 33. ftc-heads-up-simplified-v1/sentence-073

Changed: `domain`

Input:

```text
一旦给了陌生人自己的个人信息 — 例如社保号、密码或者银行账户信息，就没有办法再收回。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的帳號、隱私或裝置安全文字。

Gemini reason: 「社保号」和「银行账户信息」對應台灣的「身分證號碼」和「銀行帳戶資訊」，屬高風險個資。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 34. ftc-heads-up-simplified-v1/sentence-076

Changed: `risk`

Input:

```text
很可能它们是假冒的，想要窃取个人信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的帳號、隱私或裝置安全文字。

Gemini reason: 「信息」對應「資訊」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 35. ftc-heads-up-simplified-v1/sentence-081

Changed: `risk`

Input:

```text
然后确定那个文字游戏是否真需要访问你的照片。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的帳號、隱私或裝置安全文字。

Gemini reason: 通用句子，風險低。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 36. ftc-heads-up-simplified-v1/sentence-086

Changed: `risk`

Input:

```text
至少有 12 位字符，而且同时含有大小写字母、数字和符号。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的帳號、隱私或裝置安全文字。

Gemini reason: 描述密碼規則，用詞直接。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 37. ftc-heads-up-simplified-v1/sentence-087

Changed: `risk`

Input:

```text
考虑使用随机文字组成的密码短语，让密码不易忘记。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的帳號、隱私或裝置安全文字。

Gemini reason: 「密码短语」是 IT 術語，但兩岸用法接近。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 38. ftc-heads-up-simplified-v1/sentence-090

Changed: `risk`

Input:

```text
不同的账户使用不同的密码。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的帳號、隱私或裝置安全文字。

Gemini reason: 「账户」對應「帳號」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 39. ftc-heads-up-simplified-v1/sentence-091

Changed: `risk`

Input:

```text
这样，如果有人得到了一个账户的密码，他们无法入侵其他账户。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的帳號、隱私或裝置安全文字。

Gemini reason: 「账户」對應「帳號」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 40. ftc-heads-up-simplified-v1/sentence-092

Changed: `risk`

Input:

```text
可以使用密码管理器来跟踪所有不同的密码。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的帳號、隱私或裝置安全文字。

Gemini reason: 「密码管理器」是 IT 術語，兩岸用法相同。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 41. ftc-heads-up-simplified-v1/sentence-094

Changed: `risk`

Input:

```text
精心挑选安全问题。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的帳號、隱私或裝置安全文字。

Gemini reason: 「安全问题」是 IT 術語，兩岸用法相同。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 42. ftc-heads-up-simplified-v1/sentence-096

Changed: `domain`

Input:

```text
不要选择其他人可以在网上找到答案的问题 — 例如，自己的邮政编码、出生日期或母亲的闺名。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的帳號、隱私或裝置安全文字。

Gemini reason: 「邮政编码」和「母亲的闺名」對應「郵遞區號」和「母親本名」，涉及個資，風險高。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 43. ftc-heads-up-simplified-v1/sentence-100

Changed: `risk`

Input:

```text
使用多重身份验证。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的帳號、隱私或裝置安全文字。

Gemini reason: 「多重身份验证」對應台灣的「多重要素驗證」(MFA)。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 44. ftc-heads-up-simplified-v1/sentence-105

Changed: `risk`

Input:

```text
同时更改任何使用类似密码账户的密码。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的帳號、隱私或裝置安全文字。

Gemini reason: 「账户」對應「帳號」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 45. ftc-heads-up-simplified-v1/sentence-107

Changed: `risk`

Input:

```text
确保自己设备的安全。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的帳號、隱私或裝置安全文字。

Gemini reason: 「设备」對應「裝置」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 46. ftc-heads-up-simplified-v1/sentence-110

Changed: `risk`

Input:

```text
不要点击链接或打开附件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的帳號、隱私或裝置安全文字。

Gemini reason: 「链接」和「附件」對應「連結」和「附件」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 47. ftc-heads-up-simplified-v1/sentence-112

Changed: `eligible, domain, risk`

Input:

```text
即使是免费优惠卷也不要上当。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | source_typo |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 「优惠卷」應為「优惠券」，來源文字含明確錯字，不納入正式 benchmark。

Gemini reason: 「优惠卷」對應「優惠券」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 48. ftc-heads-up-simplified-v1/sentence-114

Changed: `risk`

Input:

```text
用密码保护设备。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的帳號、隱私或裝置安全文字。

Gemini reason: 「设备」對應「裝置」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 49. ftc-heads-up-simplified-v1/sentence-115

Changed: `risk`

Input:

```text
这将有助于防止照片、消息和帐户落入坏人之手。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的帳號、隱私或裝置安全文字。

Gemini reason: 「帐户」對應「帳號」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 50. ftc-heads-up-simplified-v1/sentence-116

Changed: `domain`

Input:

```text
将它们存放在安全的场所。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立裁決的帳號、隱私或裝置安全文字。

Gemini reason: 通用建議，風險低。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 51. ftc-heads-up-simplified-v1/sentence-117

Changed: `domain`

Input:

```text
无论是手机、台式机还是平板电脑，都不要把它留在公共场所 — 即使是只有片刻。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整且可獨立裁決的帳號、隱私或裝置安全文字。

Gemini reason: 「台式机」和「平板电脑」對應「桌上型電腦」和「平板」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`
