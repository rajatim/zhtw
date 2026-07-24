<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 016 (2026-07-24)

Status: advisory only; maintainer decisions pending

Packet SHA-256: `f9764f1d5d6aace6c1d65aa2ed2ef9f7034b07eb47e8d2a1702df1a413dca72b`
Cases: 24
Exact Codex/Gemini classifications: 1
Maintainer review queue: 23

Field differences:

- Eligibility: 3
- Script: 0
- Domain: 23
- Risk: 3

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

Neither advisory is auto-preferred. Codex must synthesize the differences before maintainer confirmation; no classification in this report has been written into the candidate pool.

## Review Queue

### 01. cisa-cyber-hygiene-zh-hans-v1/sentence-001

Changed: `domain`

Input:

```text
网络骗局已不是新事物了。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整消費者資安句；網路詐騙用語需要臺灣化。

Gemini reason: 「网络」需轉換為臺灣慣用語「網路」。

Maintainer decision: `pending`

### 02. cisa-cyber-hygiene-zh-hans-v1/sentence-002

Changed: `domain`

Input:

```text
每天，黑客和其他网络罪犯都在寻找最容易的网上目标。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整資安句；黑客與網上用語需要臺灣化。

Gemini reason: 「黑客」、「网络」、「网上」需轉換為「駭客」、「網路」。

Maintainer decision: `pending`

### 03. cisa-cyber-hygiene-zh-hans-v1/sentence-003

Changed: `domain`

Input:

```text
你认为自己不够有价值，不会成为网上掠食者的目标吗？
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整消費者警示句；網上掠食者需要臺灣用語判斷。

Gemini reason: 「网上」需轉換為「網路」或「線上」。

Maintainer decision: `pending`

### 04. cisa-cyber-hygiene-zh-hans-v1/sentence-004

Changed: `domain`

Input:

```text
不管是你的身份信息、你的银行账户信息，还是单纯的你的电子邮件里的内容，你的信息都是有价值的，网上罪犯也会尽其所能来获取它。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整帳號安全句；身分資訊與電子郵件用語需要臺灣化。

Gemini reason: 包含「信息」（資訊）、「账户」（帳戶）、「网上」（網路）等需區域詞彙轉換之用語。

Maintainer decision: `pending`

### 05. cisa-cyber-hygiene-zh-hans-v1/sentence-005

Changed: `eligible, domain`

Input:

```text
他们就仗着你不认为自己会是个目标呢。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | social_daily | baseline_guard | high | context_dependent |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 單獨抽出後未交代「他們」所指對象，依來源品質 gate 排除。

Gemini reason: 無大陸特有 IT 詞彙，僅需標準簡繁字形轉換。

Maintainer decision: `pending`

### 06. cisa-cyber-hygiene-zh-hans-v1/sentence-006

Changed: `eligible, domain, risk`

Input:

```text
是时候把你的盾牌举起了，开始防范自己不会成为网络罪行的受害人。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | social_daily | baseline_guard | high | malformed_translation |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 「防範自己不會成為」為不自然雙重否定，依 malformed gate 排除。

Gemini reason: 「网络」需轉換為「網路」。

Maintainer decision: `pending`

### 07. cisa-cyber-hygiene-zh-hans-v1/sentence-007

Changed: `domain`

Input:

```text
让我们以基本的网络卫生开始——最简单也是最具常理的办法来在线上保护自己。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 意思可獨立裁決；網路衛生與線上保護用語需要臺灣化。

Gemini reason: 「网络」需轉換為「網路」。

Maintainer decision: `pending`

### 08. cisa-cyber-hygiene-zh-hans-v1/sentence-008

Changed: `domain`

Input:

```text
一个密码并不足以保证你的网上安全。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整密碼安全句；網上安全需要臺灣用語判斷。

Gemini reason: 「网上」需轉換為「網路」。

Maintainer decision: `pending`

### 09. cisa-cyber-hygiene-zh-hans-v1/sentence-009

Changed: `domain`

Input:

```text
通过设置第二层的身份验证，比如确认短信、用身份验证软件生成代码、脸部或指纹识别，或安全钥匙，你会给你的银行、电子邮件供应商，或者其他你所登录的网站，一层额外的安全保障。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整驗證安全句；簡訊、驗證碼、金鑰與網站用語需要臺灣化。

Gemini reason: 包含「设置」（設定）、「短信」（簡訊）、「软件」（軟體）、「代码」（程式碼）、「登录」（登入）等多項 IT 詞彙轉換。

Maintainer decision: `pending`

### 10. cisa-cyber-hygiene-zh-hans-v1/sentence-010

Changed: `eligible, domain`

Input:

```text
多因素身份验证可以使你 99%更不会被黑客攻击或使自己的信息被盗！
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | it_api_cli | candidate_gap | high | malformed_translation |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 「99%更不會」比較結構不自然且可能造成量化語意誤讀，建議排除。

Gemini reason: 「黑客」、「信息」需轉換為「駭客」、「資訊」。

Maintainer decision: `pending`

### 11. cisa-cyber-hygiene-zh-hans-v1/sentence-011

Changed: `domain`

Input:

```text
黑客们会试图利用软件的缺陷和弱点。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整資安句；軟件需轉為臺灣慣用詞。

Gemini reason: 「黑客」、「软件」需轉換為「駭客」、「軟體」。

Maintainer decision: `pending`

### 12. cisa-cyber-hygiene-zh-hans-v1/sentence-012

Changed: `domain`

Input:

```text
在你所有的设备上都更新系统软件，比如手机、平板电脑和笔记本电脑。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整裝置更新句；軟件與筆記本電腦需要臺灣化。

Gemini reason: 包含「设备」（裝置）、「软件」（軟體）、「笔记本电脑」（筆記型電腦）等詞彙轉換。

Maintainer decision: `pending`

### 13. cisa-cyber-hygiene-zh-hans-v1/sentence-013

Changed: `domain`

Input:

```text
切记也要定期为你的应用查询更新——尤其是网页浏览器——在你所有的设备上。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整更新句；應用的產品語境需要臺灣化。

Gemini reason: 「应用」、「设备」需轉換為「應用程式」、「裝置」。

Maintainer decision: `pending`

### 14. cisa-cyber-hygiene-zh-hans-v1/sentence-014

Changed: `domain`

Input:

```text
直接打开你所有设备、应用、和操作系统的自动更新是最简单的办法了。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整自動更新句；應用與操作系統需要臺灣化。

Gemini reason: 「设备」、「应用」、「操作系统」需轉換為「裝置」、「應用程式」、「作業系統」。

Maintainer decision: `pending`

### 15. cisa-cyber-hygiene-zh-hans-v1/sentence-015

Changed: `domain`

Input:

```text
点击之前想一想。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 短但完整的消費者指示，僅需一般字形轉換。

Gemini reason: 「点击」轉為「點擊」屬於標準字形轉換。

Maintainer decision: `pending`

### 16. cisa-cyber-hygiene-zh-hans-v1/sentence-016

Changed: `domain`

Input:

```text
超过 90%的成功的网络攻击开始于你在钓鱼邮件里点击了一个不熟悉的链接。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整網路釣魚句；鏈接與網路攻擊用語需要臺灣化。

Gemini reason: 「网络」、「链接」需轉換為「網路」、「連結」。

Maintainer decision: `pending`

### 17. cisa-cyber-hygiene-zh-hans-v1/sentence-018

Changed: `domain`

Input:

```text
另外，钓鱼邮件也可能试图骗你运行恶意软件，也被称为恶意程序。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整惡意程式句；惡意軟件需要臺灣化。

Gemini reason: 「运行」、「软件」需轉換為「執行」、「軟體」。

Maintainer decision: `pending`

### 18. cisa-cyber-hygiene-zh-hans-v1/sentence-019

Changed: `domain`

Input:

```text
如果你不认得一个链接，相信你的直觉，点击之前想一想。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整連結安全句；鏈接需轉為臺灣慣用詞。

Gemini reason: 「链接」需轉換為「連結」。

Maintainer decision: `pending`

### 19. cisa-cyber-hygiene-zh-hans-v1/sentence-020

Changed: `domain, risk`

Input:

```text
一个强密码应该由 8 位或更多数位，并由字母、数字和特殊符号混合组成。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整密碼規則句；位數與字元表達需要臺灣化。

Gemini reason: 密碼長度脈絡下的「数位」應防止被誤轉為臺灣表示 digital 之「數位」（宜轉為位數或字元）。

Maintainer decision: `pending`

### 20. cisa-cyber-hygiene-zh-hans-v1/sentence-021

Changed: `domain, risk`

Input:

```text
避免在不同账户上使用同一个密码。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整密碼安全句，主要需要一般字形轉換。

Gemini reason: 「账户」需轉換為「帳戶」。

Maintainer decision: `pending`

### 21. cisa-cyber-hygiene-zh-hans-v1/sentence-022

Changed: `domain`

Input:

```text
理想上来说，个人也应当使用一个密码管理工具来生成或存储独特的密码。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整密碼管理句；生成與存儲需要臺灣化。

Gemini reason: 「存储」需轉換為「儲存」。

Maintainer decision: `pending`

### 22. cisa-cyber-hygiene-zh-hans-v1/sentence-023

Changed: `domain`

Input:

```text
我们的世界在不断地电子化，也在不断地联网，我们大家都有责任来真正保护我们都所依赖的电脑网络。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整網路安全句；聯網用語需要臺灣化。

Gemini reason: 「联网」、「网络」需轉換為「連網」、「網路」。

Maintainer decision: `pending`

### 23. cisa-cyber-hygiene-zh-hans-v1/sentence-024

Changed: `domain`

Input:

```text
做网络安全的冠军，分享这些窍门给你的朋友、家人和邻居。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 意思可獨立裁決；網路安全與竅門用語需要臺灣化。

Gemini reason: 「网络」需轉換為「網路」，「窍门」可轉換為「小技巧」或「撇步」。

Maintainer decision: `pending`
