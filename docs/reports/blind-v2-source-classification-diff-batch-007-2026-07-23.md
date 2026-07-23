<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 007 (2026-07-23)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `ab08de50069ca4f06fb0daeb3ccdcb2fb5d6d4778e6abbeb57960496bd8c1adf`
Cases: 81
Exact Codex/Gemini classifications: 53
Maintainer review queue: 28

Field differences:

- Eligibility: 22
- Script: 0
- Domain: 25
- Risk: 26

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

The maintainer resolved all 28 advisory disagreements and batch-confirmed the 53 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. ftc-small-business-simplified-v1/sentence-004

Changed: `eligible, domain, risk`

Input:

```text
然后，告诉你的员工和同事有哪些相关的注意事项，以防被骗。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | no | null | null | high | deictic_dependency |

Codex reason: 含詐騙、金融、法律、企業或資安領域的中國用語，臺灣語境可能需要詞彙調整。

Gemini reason: 開頭的'然後'使其依賴前文，不具備獨立性，不符資格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 02. ftc-small-business-simplified-v1/sentence-006

Changed: `eligible, domain, risk`

Input:

```text
他们会假称是你知道的某个公司或政府机构，让你向他们付款。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 含缺少前文的代名詞、承接語或指示語，無法從單一句子獨立裁決，建議排除。

Gemini reason: 描述冒充政府或公司的詐騙手法，屬高風險領域。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 03. ftc-small-business-simplified-v1/sentence-007

Changed: `eligible, domain, risk`

Input:

```text
但是，这是一个骗局。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 含缺少前文的代名詞、承接語或指示語，無法從單一句子獨立裁決，建議排除。

Gemini reason: 簡短的陳述句，是詐騙情境的一部分。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 04. ftc-small-business-simplified-v1/sentence-009

Changed: `eligible, domain, risk`

Input:

```text
他们会希望你立即行动，不给你机会进行查证。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 含缺少前文的代名詞、承接語或指示語，無法從單一句子獨立裁決，建議排除。

Gemini reason: 描述詐騙手法，'查证' 一詞在台灣可能用 '查證'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 05. ftc-small-business-simplified-v1/sentence-011

Changed: `risk`

Input:

```text
诈骗犯会要求你以特定方式进行付款。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 含詐騙、金融、法律、企業或資安領域的中國用語，臺灣語境可能需要詞彙調整。

Gemini reason: 描述詐騙付款手法的引子。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 06. ftc-small-business-simplified-v1/sentence-012

Changed: `eligible, domain, risk`

Input:

```text
他们通常会要求你通过电汇，加密货币或礼品卡的方式汇款。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 含缺少前文的代名詞、承接語或指示語，無法從單一句子獨立裁決，建議排除。

Gemini reason: 提及'电汇', '加密货币', '礼品卡'，涉及金融與科技，屬於 IT API/CLI 風險。這些詞彙在兩岸有不同慣用法。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 07. ftc-small-business-simplified-v1/sentence-013

Changed: `eligible, domain, risk`

Input:

```text
切勿向要求你使用上述支付方法的人员付款。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | no | null | null | high | deictic_dependency |

Codex reason: 主要驗證一般字形與完整句的保守轉換，未見明確區域術語缺口。

Gemini reason: '上述支付方法' 依賴前文，無法獨立評估，不符資格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 08. ftc-small-business-simplified-v1/sentence-015

Changed: `domain`

Input:

```text
对员工进行培训，告诉他们不要通过电子邮件发送密码或敏感信息，即使索要这些信息的邮件看似来自某位经理。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 含詐騙、金融、法律、企業或資安領域的中國用語，臺灣語境可能需要詞彙調整。

Gemini reason: 涉及密碼、電子郵件等資訊安全議題，屬 IT 風險。'密码', '敏感信息' 為潛在術語差異點。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 09. ftc-small-business-simplified-v1/sentence-019

Changed: `domain`

Input:

```text
如果对方要求你通过电汇，加密货币或礼品卡的方式支付，切勿付款。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 含詐騙、金融、法律、企業或資安領域的中國用語，臺灣語境可能需要詞彙調整。

Gemini reason: 重複提及'电汇', '加密货币', '礼品卡'，這些金融科技詞彙具地區差異性。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 10. ftc-small-business-simplified-v1/sentence-025

Changed: `eligible, domain, risk`

Input:

```text
了解他人对该公司的评价。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 含缺少前文的代名詞、承接語或指示語，無法從單一句子獨立裁決，建議排除。

Gemini reason: 通用的建議，轉換風險較低。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 11. ftc-small-business-simplified-v1/sentence-028

Changed: `eligible, domain, risk`

Input:

```text
他们的目的是要让为你支付账单的人员认定这些发票的真实性，从而支付款项。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 含缺少前文的代名詞、承接語或指示語，無法從單一句子獨立裁決，建議排除。

Gemini reason: 描述詐騙心理，'认定', '真实性' 等詞在書面語中通用，但口語可能有別。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 12. ftc-small-business-simplified-v1/sentence-032

Changed: `eligible, domain, risk`

Input:

```text
这时，请千万不要付款。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 含缺少前文的代名詞、承接語或指示語，無法從單一句子獨立裁決，建議排除。

Gemini reason: 直接的財務建議，'这时' 指涉的時間點雖模糊但指令本身是獨立的。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 13. ftc-small-business-simplified-v1/sentence-036

Changed: `eligible, domain, risk`

Input:

```text
之后，你会收到大额账单，这时诈骗犯会利用他们先前在电话中了解到的详细信息——甚至是录音——迫使你付款。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 含缺少前文的代名詞、承接語或指示語，無法從單一句子獨立裁決，建議排除。

Gemini reason: 涉及錄音證據和催款，'录音' 詞在台灣通用，但整個句子情境下的用詞可能需調整。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 14. ftc-small-business-simplified-v1/sentence-040

Changed: `eligible, domain, risk`

Input:

```text
他们可能会声称原因是你有拖欠税费或需要更新执照或登记信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 含缺少前文的代名詞、承接語或指示語，無法從單一句子獨立裁決，建議排除。

Gemini reason: 提及欠稅、執照更新，'拖欠税费', '执照', '登记信息' 都是需要注意的術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 15. ftc-small-business-simplified-v1/sentence-044

Changed: `eligible, domain, risk`

Input:

```text
其他一些情况下，他们会假称你欠下了其他注册服务的费用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 含缺少前文的代名詞、承接語或指示語，無法從單一句子獨立裁決，建議排除。

Gemini reason: 描述註冊服務費用的詐騙，'注册服务' 用詞需斟酌。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 16. ftc-small-business-simplified-v1/sentence-048

Changed: `eligible, domain, risk`

Input:

```text
他们的目的其实只是为了骗取你的钱财，访问你的电脑，或两者皆有。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 含缺少前文的代名詞、承接語或指示語，無法從單一句子獨立裁決，建議排除。

Gemini reason: 描述詐騙目的，包含騙錢和訪問電腦，'访问你的电脑' 是 IT 操作。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 17. ftc-small-business-simplified-v1/sentence-049

Changed: `eligible, domain, risk`

Input:

```text
他们会要求你就修复某个你根本不存在的问题，将你的企业纳入根本不存在的或毫无用处的电脑维护项目付款，或潜入你的电脑网络抓取机密数据来实施身份盗窃。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 含缺少前文的代名詞、承接語或指示語，無法從單一句子獨立裁決，建議排除。

Gemini reason: 涉及電腦維護、電腦網路、機密數據和身份盜竊，大量 IT 和資安術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 18. ftc-small-business-simplified-v1/sentence-051

Changed: `eligible, domain, risk`

Input:

```text
其通常会在一开始以网络钓鱼电子邮件，社交媒体联系人或看似来自某个可靠来源的电话（如主管或其他高层人员）——来制造紧迫感或引起你的害怕。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 含缺少前文的代名詞、承接語或指示語，無法從單一句子獨立裁決，建議排除。

Gemini reason: 描述'网络钓鱼电子邮件'、'社交媒体'等攻擊媒介，屬 IT 資安領域。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 19. ftc-small-business-simplified-v1/sentence-055

Changed: `eligible, domain, risk`

Input:

```text
他们会假装承诺，如果您想要企业取得成功，只要购买他们“经过验证”的独家系统，就能实现显著效果。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 含缺少前文的代名詞、承接語或指示語，無法從單一句子獨立裁決，建議排除。

Gemini reason: 描述詐騙的虛假承諾，'“经过验证”的独家系统' 是典型的行銷話術。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 20. ftc-small-business-simplified-v1/sentence-056

Changed: `eligible, domain, risk`

Input:

```text
他们还会在一开始以低价来诱惑你，目的是为了在以后骗取你大量的钱财。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 含缺少前文的代名詞、承接語或指示語，無法從單一句子獨立裁決，建議排除。

Gemini reason: 描述低價誘惑的詐騙手法。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 21. ftc-small-business-simplified-v1/sentence-057

Changed: `eligible, domain, risk`

Input:

```text
而事实上，诈骗犯并不会给这些新手企业家们任何他们想要的帮助，只会给其留下巨额债务。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 含缺少前文的代名詞、承接語或指示語，無法從單一句子獨立裁決，建議排除。

Gemini reason: 描述詐騙後果，'新手企业家', '巨额债务' 等詞需注意。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 22. ftc-small-business-simplified-v1/sentence-059

Changed: `risk`

Input:

```text
但是，发布虚假评价是违法行为。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 主要驗證一般字形與完整句的保守轉換，未見明確區域術語缺口。

Gemini reason: 陳述法律事實，'虚假评价', '违法'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 23. ftc-small-business-simplified-v1/sentence-065

Changed: `eligible, domain, risk`

Input:

```text
其他一些已知的骗局是事后更改条款。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 含缺少前文的代名詞、承接語或指示語，無法從單一句子獨立裁決，建議排除。

Gemini reason: 提及事後更改條款的騙局。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 24. ftc-small-business-simplified-v1/sentence-067

Changed: `eligible, domain, risk`

Input:

```text
如果他们予以拒绝或承诺稍后提供以拖延时间，那么这可能就表明你遇到了诈骗。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 含缺少前文的代名詞、承接語或指示語，無法從單一句子獨立裁決，建議排除。

Gemini reason: 描述判斷是否為詐騙的跡象。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 25. ftc-small-business-simplified-v1/sentence-069

Changed: `eligible, domain, risk`

Input:

```text
之后，他们会要求你将多出的钱款返还给他们或某个其他人员。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 含缺少前文的代名詞、承接語或指示語，無法從單一句子獨立裁決，建議排除。

Gemini reason: 描述騙局的下一步，要求返還多餘款項。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 26. ftc-small-business-simplified-v1/sentence-076

Changed: `domain, risk`

Input:

```text
通知你所在州的总检察长。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 主要驗證一般字形與完整句的保守轉換，未見明確區域術語缺口。

Gemini reason: 提供通報管道的建議，'总检察长' 在不同地區有不同稱謂。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 27. ftc-small-business-simplified-v1/sentence-077

Changed: `risk`

Input:

```text
请记住，你最有效的防御就是训练有素的员工。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 含詐騙、金融、法律、企業或資安領域的中國用語，臺灣語境可能需要詞彙調整。

Gemini reason: 重複的結論性建議。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 28. ftc-small-business-simplified-v1/sentence-079

Changed: `eligible, domain, risk`

Input:

```text
与你的员工一同阅览本手册。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | no | null | null | high | deictic_dependency |

Codex reason: 主要驗證一般字形與完整句的保守轉換，未見明確區域術語缺口。

Gemini reason: '本手册' 指代不明，句子無法獨立存在，不符合資格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`
