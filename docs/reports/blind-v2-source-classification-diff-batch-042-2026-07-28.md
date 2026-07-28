<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 042 (2026-07-28)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `0aa60011d65c9aad108a0913a888fb343f7112a34e1b6306ee704fd4feeaf672`
Cases: 96
Exact Codex/Gemini classifications: 50
Maintainer review queue: 46

Field differences:

- Eligibility: 8
- Script: 13
- Domain: 15
- Risk: 32

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

The maintainer resolved all 46 advisory disagreements and batch-confirmed the 50 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. aosp-framework-zh-rcn-v1/string-0e913c6d9e2c6787

Changed: `script`

Input:

```text
允许应用在系统完成引导后立即自行启动。这样可能会延长 Android TV 设备的启动时间，并会因一直运行该应用而导致设备的整体运行速度变慢。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Android UI 字串；依臺灣介面用語與占位符或專名保留風險分類。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 02. aosp-framework-zh-rcn-v1/string-1b8ba37c7a7bd3a9

Changed: `script`

Input:

```text
无法在您的%1$s上访问此设置，您可以尝试在手机上访问。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Android UI 字串；依臺灣介面用語與占位符或專名保留風險分類。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 03. aosp-framework-zh-rcn-v1/string-32701d2fb7c7b262

Changed: `script`

Input:

```text
SIM卡已被停用，需要输入PUK码才能继续使用。有关详情，请联系您的运营商。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Android UI 字串；依臺灣介面用語與占位符或專名保留風險分類。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 04. aosp-framework-zh-rcn-v1/string-38adbe65fe6f0b2b

Changed: `script, risk`

Input:

```text
无法连接到始终开启的 VPN
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Android UI 字串；依臺灣介面用語與占位符或專名保留風險分類。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 05. aosp-framework-zh-rcn-v1/string-4dd0ecca554e6519

Changed: `script`

Input:

```text
允许应用发送置顶广播，这类广播在广播结束后仍会继续存在。过度使用这项功能可能会导致 Android TV 设备使用过多内存，从而降低其运行速度或稳定性。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Android UI 字串；依臺灣介面用語與占位符或專名保留風險分類。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 06. aosp-framework-zh-rcn-v1/string-4e379ec67338da50

Changed: `risk`

Input:

```text
正在搜索服务
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 可獨立判讀的 Android UI 字串；依臺灣介面用語與占位符或專名保留風險分類。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 07. aosp-framework-zh-rcn-v1/string-61233b9964793233

Changed: `script`

Input:

```text
“%s”正在其他应用的上层显示内容
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Android UI 字串；依臺灣介面用語與占位符或專名保留風險分類。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 08. aosp-framework-zh-rcn-v1/string-637341020b687ffa

Changed: `risk`

Input:

```text
后台流量受限制
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 可獨立判讀的 Android UI 字串；依臺灣介面用語與占位符或專名保留風險分類。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 09. aosp-framework-zh-rcn-v1/string-6bbacbb88f37019c

Changed: `risk`

Input:

```text
人脸解锁。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 可獨立判讀的 Android UI 字串；依臺灣介面用語與占位符或專名保留風險分類。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 10. aosp-framework-zh-rcn-v1/string-72e099f0f032808f

Changed: `risk`

Input:

```text
允许该应用修改对于各应用的网络使用情况的统计方式。普通应用不应使用此权限。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 可獨立判讀的 Android UI 字串；依臺灣介面用語與占位符或專名保留風險分類。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 11. aosp-framework-zh-rcn-v1/string-9b65b437a4a7022d

Changed: `script, risk`

Input:

```text
RUIM 网络 2 解锁请求失败。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Android UI 字串；依臺灣介面用語與占位符或專名保留風險分類。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 12. aosp-framework-zh-rcn-v1/string-d1ffddbd15d0058c

Changed: `eligible, script, domain, risk`

Input:

```text
%1$s。%3$d的微件%2$d。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_localization |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 輸入是來源殘片或格式受損字串，無法在缺少上下文時穩定裁決。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 13. aosp-framework-zh-rcn-v1/string-e07a3d16303d9e31

Changed: `risk`

Input:

```text
增大日期值
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 可獨立判讀的 Android UI 字串；依臺灣介面用語與占位符或專名保留風險分類。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 14. aosp-framework-zh-rcn-v1/string-e7facb69f398fe81

Changed: `risk`

Input:

```text
检测您与之互动的窗口的内容。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 可獨立判讀的 Android UI 字串；依臺灣介面用語與占位符或專名保留風險分類。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 15. aosp-framework-zh-rcn-v1/string-ef3f7f1bef524b07

Changed: `script, risk`

Input:

```text
尝试删除的%s数量太多。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Android UI 字串；依臺灣介面用語與占位符或專名保留風險分類。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 16. aosp-framework-zh-rcn-v1/string-f614ebb1e12f2b9e

Changed: `eligible, script, domain, risk`

Input:

```text
工作%1$s
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 輸入是來源殘片或格式受損字串，無法在缺少上下文時穩定裁決。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 17. aosp-framework-zh-rcn-v1/string-fb609cb9bbd1f923

Changed: `script`

Input:

```text
{count,plural, =1{1 分钟}other{# 分钟}}
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Android UI 字串；依臺灣介面用語與占位符或專名保留風險分類。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 18. aosp-framework-zh-rcn-v1/string-ff5b9ae343d65228

Changed: `script, risk`

Input:

```text
此应用可读取您 Android TV 设备上存储的所有短信。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的 Android UI 字串；依臺灣介面用語與占位符或專名保留風險分類。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 19. ftc-how-to-avoid-scam-simplified-v1/sentence-002

Changed: `risk`

Input:

```text
诈骗者通常假装代表政府联系您。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方消費者保護句子；詐騙、身分與金融語境具高風險評測價值。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 20. ftc-how-to-avoid-scam-simplified-v1/sentence-010

Changed: `risk`

Input:

```text
他们可能会威胁要逮捕您、起诉您、吊销您的驾照或营业执照，或将您驱逐出境。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方消費者保護句子；詐騙、身分與金融語境具高風險評測價值。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 21. ftc-how-to-avoid-scam-simplified-v1/sentence-013

Changed: `script`

Input:

```text
他们通常坚持要求您仅可通过加密货币、通过 MoneyGram 或 Western Union 等公司汇款、使用支付应用程序、或将钱存入礼品卡并在卡片背面写上金额的方式来付款。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的官方消費者保護句子；詐騙、身分與金融語境具高風險評測價值。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 22. ftc-how-to-avoid-scam-simplified-v1/sentence-014

Changed: `risk`

Input:

```text
有些诈骗者会给您邮寄一张支票（其实是假支票），然后告诉您去银行存入，并把钱汇给他们。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方消費者保護句子；詐騙、身分與金融語境具高風險評測價值。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 23. ftc-how-to-avoid-scam-simplified-v1/sentence-016

Changed: `risk`

Input:

```text
他们可能会说您在政府关系方面遇到麻烦、或您欠了钱，或您家里有人发生紧急情况。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方消費者保護句子；詐騙、身分與金融語境具高風險評測價值。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 24. ftc-how-to-avoid-scam-simplified-v1/sentence-017

Changed: `eligible, domain, risk`

Input:

```text
或者您的计算机感染了病毒。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 輸入是來源殘片或格式受損字串，無法在缺少上下文時穩定裁決。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 25. ftc-how-to-avoid-scam-simplified-v1/sentence-019

Changed: `risk`

Input:

```text
而其他诈骗者则会撒谎，说您在彩票或抽奖活动中中奖，但必须支付一定费用才能获得该奖励。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方消費者保護句子；詐騙、身分與金融語境具高風險評測價值。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 26. ftc-how-to-avoid-scam-simplified-v1/sentence-027

Changed: `risk`

Input:

```text
顶住立即采取行动的压力。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方消費者保護句子；詐騙、身分與金融語境具高風險評測價值。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 27. ftc-identity-theft-simplified-v1/sentence-001

Changed: `risk`

Input:

```text
身份盗窃是指有人在未经您许可的情况下使用您的个人或财务信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方消費者保護句子；詐騙、身分與金融語境具高風險評測價值。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 28. ftc-identity-theft-simplified-v1/sentence-002

Changed: `eligible, domain, risk`

Input:

```text
是否发现您没有购买物品的费用？
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 輸入是來源殘片或格式受損字串，無法在缺少上下文時穩定裁決。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 29. ftc-identity-theft-simplified-v1/sentence-003

Changed: `risk`

Input:

```text
留意您的银行账户对账单。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方消費者保護句子；詐騙、身分與金融語境具高風險評測價值。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 30. ftc-identity-theft-simplified-v1/sentence-004

Changed: `eligible, domain, risk`

Input:

```text
是否有您不知晓的取款？
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 輸入是來源殘片或格式受損字串，無法在缺少上下文時穩定裁決。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 31. ftc-identity-theft-simplified-v1/sentence-005

Changed: `eligible, domain, risk`

Input:

```text
是否有让您觉得意外的变化？
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 輸入是來源殘片或格式受損字串，無法在缺少上下文時穩定裁決。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 32. ftc-identity-theft-simplified-v1/sentence-006

Changed: `risk`

Input:

```text
查看您的邮件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方消費者保護句子；詐騙、身分與金融語境具高風險評測價值。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 33. ftc-identity-theft-simplified-v1/sentence-007

Changed: `risk`

Input:

```text
您是否收不到某个账单了？
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方消費者保護句子；詐騙、身分與金融語境具高風險評測價值。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 34. ftc-identity-theft-simplified-v1/sentence-009

Changed: `eligible, domain, risk`

Input:

```text
或者收到来自您不认识雇主的信？
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 輸入是來源殘片或格式受損字串，無法在缺少上下文時穩定裁決。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 35. ftc-identity-theft-simplified-v1/sentence-010

Changed: `risk`

Input:

```text
身份盗窃可能发生在任何人身上。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方消費者保護句子；詐騙、身分與金融語境具高風險評測價值。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 36. ftc-identity-theft-simplified-v1/sentence-012

Changed: `risk`

Input:

```text
在扔掉任何显示您个人信息的文件之前，先将文件粉碎。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方消費者保護句子；詐騙、身分與金融語境具高風險評測價值。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 37. ftc-identity-theft-simplified-v1/sentence-013

Changed: `risk`

Input:

```text
不要与突然意外联系您的人分享您的社会保障号码。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的官方消費者保護句子；詐騙、身分與金融語境具高風險評測價值。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 38. ftc-identity-theft-simplified-v1/sentence-015

Changed: `risk`

Input:

```text
保护您的网上和手机上的信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的官方消費者保護句子；詐騙、身分與金融語境具高風險評測價值。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 39. ftc-identity-theft-simplified-v1/sentence-020

Changed: `eligible, domain, risk`

Input:

```text
这可能是您身份被盗窃的迹象。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 輸入是來源殘片或格式受損字串，無法在缺少上下文時穩定裁決。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 40. zhtw-project-it-ui-llm-formal-guard-v1/formal-004

Changed: `domain`

Input:

```text
统计表中的代码 NACE Rev. 2 不得改写。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 project-original guard 句；識別碼、專名、引文或格式標記必須保留。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 41. zhtw-project-it-ui-llm-formal-guard-v1/formal-007

Changed: `domain`

Input:

```text
采购文件引用标准 ASTM D4169-22。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整的 project-original guard 句；識別碼、專名、引文或格式標記必須保留。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 42. zhtw-project-it-ui-llm-formal-guard-v1/formal-014

Changed: `domain`

Input:

```text
调查问卷将“不适用”编码为 N/A。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 project-original guard 句；識別碼、專名、引文或格式標記必須保留。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 43. zhtw-project-it-ui-llm-formal-guard-v1/formal-020

Changed: `domain`

Input:

```text
附件标题 Exhibit C-2 必须对应原始文件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 project-original guard 句；識別碼、專名、引文或格式標記必須保留。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 44. zhtw-project-it-ui-llm-formal-guard-v1/llm-013

Changed: `domain`

Input:

```text
多模态消息以 image_url 字段传入图片位置。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 project-original guard 句；識別碼、專名、引文或格式標記必須保留。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 45. zhtw-project-it-ui-llm-formal-guard-v1/llm-019

Changed: `domain`

Input:

```text
模型路由规则将 locale=zh-TW 传给下游服务。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 project-original guard 句；識別碼、專名、引文或格式標記必須保留。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 46. zhtw-project-it-ui-llm-formal-guard-v1/llm-022

Changed: `domain`

Input:

```text
对话汇出文件保留 message_id 与 parent_id。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整的 project-original guard 句；識別碼、專名、引文或格式標記必須保留。

Gemini reason: -

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`
