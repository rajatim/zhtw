<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 017 (2026-07-24)

Status: advisory only; maintainer decisions pending

Packet SHA-256: `ec8fe952e9bedee004d20d1e9c390f0848d0ac1faaa8a83ccda776aebdace21e`
Cases: 100
Exact Codex/Gemini classifications: 55
Maintainer review queue: 45

Field differences:

- Eligibility: 3
- Script: 0
- Domain: 26
- Risk: 31

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

Neither advisory is auto-preferred. Codex must synthesize the differences before maintainer confirmation; no classification in this report has been written into the candidate pool.

## Review Queue

### 01. cisa-personal-security-zh-hans-v1/sentence-002

Changed: `risk`

Input:

```text
关键基础设施员工从事大量的服务工作，负责操作、运行和维护现代美国生活所必需的关键系统和资产。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: complete

Maintainer decision: `pending`

### 02. cisa-personal-security-zh-hans-v1/sentence-003

Changed: `risk`

Input:

```text
注意与您工作相关的任何风险或威胁，并遵守所有安全程序将有助于保护您、您身边的人以及您所服务的基础设施。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; technical terms, abbreviations, or context-sensitive wording must be preserved carefully.

Gemini reason: complete

Maintainer decision: `pending`

### 03. cisa-personal-security-zh-hans-v1/sentence-004

Changed: `risk`

Input:

```text
个人安全可分为三个主要部分：人身安全、态势感知和网络安全。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: complete

Maintainer decision: `pending`

### 04. cisa-personal-security-zh-hans-v1/sentence-010

Changed: `eligible`

Input:

```text
是否有可靠证据表明您面临风险？
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | high_stakes | baseline_guard | high | context_dependent_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: The extracted text is a list fragment, incomplete phrase, or depends on missing context.

Gemini reason: question

Maintainer decision: `pending`

### 05. cisa-personal-security-zh-hans-v1/sentence-016

Changed: `risk`

Input:

```text
在评估您的个人安全时，关键在于采取一种平衡的方法，并记得把您的家庭和工作生活考虑在内—在您采取个人安全实践和培养此类习惯时保持警惕，并不断评估您周围的环境。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: complete

Maintainer decision: `pending`

### 06. cisa-personal-security-zh-hans-v1/sentence-020

Changed: `risk`

Input:

```text
攻击者将个人作为目标时可谓花样百出。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: complete

Maintainer decision: `pending`

### 07. cisa-personal-security-zh-hans-v1/sentence-024

Changed: `risk`

Input:

```text
您可用锁、钥匙、警报器和灯来保护门窗，并评估是否需要安装闭路电视 (CCTV) 系统。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; technical terms, abbreviations, or context-sensitive wording must be preserved carefully.

Gemini reason: complete

Maintainer decision: `pending`

### 08. cisa-personal-security-zh-hans-v1/sentence-025

Changed: `risk`

Input:

```text
您可考虑在入口处和窗户上采用先进的门锁系统，并安装监控（多视角）视频监视系统。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: complete

Maintainer decision: `pending`

### 09. cisa-personal-security-zh-hans-v1/sentence-036

Changed: `risk`

Input:

```text
请将车停在光线充足的地方、 CCTV 摄像头能看到的地方或有人看管的停车场。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; technical terms, abbreviations, or context-sensitive wording must be preserved carefully.

Gemini reason: cctv

Maintainer decision: `pending`

### 10. cisa-personal-security-zh-hans-v1/sentence-039

Changed: `risk`

Input:

```text
除了车辆定位服务，还可启用包含声音和视觉通知的系统，以协助警方加快应对的脚步。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: tracking

Maintainer decision: `pending`

### 11. cisa-personal-security-zh-hans-v1/sentence-047

Changed: `domain, risk`

Input:

```text
CISA 发布的《公众示威期间保护基础设施情况说明书》为可能在公众示威期间成为非法行为目标的企业提供了安全建议。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; technical terms, abbreviations, or context-sensitive wording must be preserved carefully.

Gemini reason: factsheet

Maintainer decision: `pending`

### 12. cisa-personal-security-zh-hans-v1/sentence-048

Changed: `risk`

Input:

```text
态势感知是指了解周围发生的一切，考虑到所有情况并调整自己的行为，以降低自己、家人或同事受伤的风险。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: awareness

Maintainer decision: `pending`

### 13. cisa-personal-security-zh-hans-v1/sentence-052

Changed: `eligible`

Input:

```text
进入住宅后，始终与其维持近距离，最好让他们待在您面前或其他您能监测的位置。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | high_stakes | baseline_guard | high | context_dependent_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: The extracted text is a list fragment, incomplete phrase, or depends on missing context.

Gemini reason: monitoring

Maintainer decision: `pending`

### 14. cisa-personal-security-zh-hans-v1/sentence-054

Changed: `risk`

Input:

```text
始终妥善处理或销毁可能含有敏感或个人身份信息 (PII) 的机密材料。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; technical terms, abbreviations, or context-sensitive wording must be preserved carefully.

Gemini reason: pii

Maintainer decision: `pending`

### 15. cisa-personal-security-zh-hans-v1/sentence-055

Changed: `risk`

Input:

```text
PII 包括可用于识别您身份的任何个人信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; technical terms, abbreviations, or context-sensitive wording must be preserved carefully.

Gemini reason: definition

Maintainer decision: `pending`

### 16. cisa-personal-security-zh-hans-v1/sentence-060

Changed: `risk`

Input:

```text
在接受拼车和进入车辆之前，请检查司机和车辆的详细信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: rideshare

Maintainer decision: `pending`

### 17. cisa-personal-security-zh-hans-v1/sentence-073

Changed: `risk`

Input:

```text
在公共场所佩戴工牌或输入密码时要小心谨慎。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: security

Maintainer decision: `pending`

### 18. cisa-personal-security-zh-hans-v1/sentence-084

Changed: `risk`

Input:

```text
考虑自己的能力极限，在安全的情况下尽快寻求安保人员或执法人员的协助。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: security

Maintainer decision: `pending`

### 19. cisa-personal-security-zh-hans-v1/sentence-085

Changed: `risk`

Input:

```text
如果您接受过培训并熟练掌握相关技能，可以考虑采取目的明确的行动（包括有效的倾听和沟通），安全地缓和激烈的局势。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: security

Maintainer decision: `pending`

### 20. cisa-personal-security-zh-hans-v1/sentence-087

Changed: `domain, risk`

Input:

```text
及时更新软件，让攻击者无法利用敏感信息或漏洞。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: security

Maintainer decision: `pending`

### 21. cisa-personal-security-zh-hans-v1/sentence-088

Changed: `domain, risk`

Input:

```text
许多操作系统都提供自动更新功能。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: security

Maintainer decision: `pending`

### 22. cisa-personal-security-zh-hans-v1/sentence-089

Changed: `domain, risk`

Input:

```text
如果可以选择自动更新，请在设备的应用程序安全设置中打开自动更新。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: security

Maintainer decision: `pending`

### 23. cisa-personal-security-zh-hans-v1/sentence-103

Changed: `risk`

Input:

```text
尽量记下任何可疑车辆的车牌号、品牌和型号。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: vehicle

Maintainer decision: `pending`

### 24. cisa-personal-security-zh-hans-v1/sentence-107

Changed: `domain`

Input:

```text
请勿从未知或无法验证来源处下载应用程序。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: app

Maintainer decision: `pending`

### 25. cisa-personal-security-zh-hans-v1/sentence-108

Changed: `domain, risk`

Input:

```text
在每个提供多因素身份验证 (MFA) 的账户或应用程序上启用该功能。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Complete input-only sentence; technical terms, abbreviations, or context-sensitive wording must be preserved carefully.

Gemini reason: mfa

Maintainer decision: `pending`

### 26. cisa-personal-security-zh-hans-v1/sentence-109

Changed: `domain, risk`

Input:

```text
启用 MFA 有助于保护您的个人信息，如电子邮件、社交媒体、财务和其他重要信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Complete input-only sentence; technical terms, abbreviations, or context-sensitive wording must be preserved carefully.

Gemini reason: privacy

Maintainer decision: `pending`

### 27. cisa-personal-security-zh-hans-v1/sentence-110

Changed: `domain, risk`

Input:

```text
在网上发布信息时，请务必注意发布的内容和方式。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: posting

Maintainer decision: `pending`

### 28. cisa-personal-security-zh-hans-v1/sentence-111

Changed: `domain, risk`

Input:

```text
如果您发布的信息过多而又没有进行适当的隐私设置，您可能会将自己的人身安全置于危险之中。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: safety

Maintainer decision: `pending`

### 29. cisa-personal-security-zh-hans-v1/sentence-112

Changed: `domain, risk`

Input:

```text
他人可以利用这类信息来了解您的人际关系、观点、感兴趣的领域和其他主题，以便在将来加以利用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: profiling

Maintainer decision: `pending`

### 30. cisa-personal-security-zh-hans-v1/sentence-113

Changed: `domain`

Input:

```text
数据经纪商也会收集这类个人信息，并将其卖给其他公司。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: brokers

Maintainer decision: `pending`

### 31. cisa-personal-security-zh-hans-v1/sentence-114

Changed: `domain`

Input:

```text
请勿在社交媒体上接受现实生活中不认识的人的好友请求。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: friends

Maintainer decision: `pending`

### 32. cisa-personal-security-zh-hans-v1/sentence-116

Changed: `domain`

Input:

```text
限制应用程序权限。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: permissions

Maintainer decision: `pending`

### 33. cisa-personal-security-zh-hans-v1/sentence-117

Changed: `domain, risk`

Input:

```text
为您的姓名设置 Google 快讯。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Complete input-only sentence; technical terms, abbreviations, or context-sensitive wording must be preserved carefully.

Gemini reason: alerts

Maintainer decision: `pending`

### 34. cisa-personal-security-zh-hans-v1/sentence-118

Changed: `domain`

Input:

```text
考虑花点时间退出主要数据经纪商和人员搜索网站的数据共享，或者订阅一项服务来帮您退出。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: optout

Maintainer decision: `pending`

### 35. cisa-personal-security-zh-hans-v1/sentence-119

Changed: `domain, risk`

Input:

```text
社交网络平台允许用户发布基于位置的信息，支持 GPS 的手机和移动设备发布此类信息尤其方便。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Complete input-only sentence; technical terms, abbreviations, or context-sensitive wording must be preserved carefully.

Gemini reason: location

Maintainer decision: `pending`

### 36. cisa-personal-security-zh-hans-v1/sentence-120

Changed: `domain, risk`

Input:

```text
发布这类信息并不安全，任何人都能看到该信息，包括可能想伤害您的人。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: exposure

Maintainer decision: `pending`

### 37. cisa-personal-security-zh-hans-v1/sentence-122

Changed: `domain`

Input:

```text
记录下所发生的一切并截屏与调查人员分享。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: screenshot

Maintainer decision: `pending`

### 38. cisa-personal-security-zh-hans-v1/sentence-123

Changed: `domain`

Input:

```text
确定哪些信息遭到利用、威胁的严重程度和漏洞所在之处。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: assessment

Maintainer decision: `pending`

### 39. cisa-personal-security-zh-hans-v1/sentence-124

Changed: `domain`

Input:

```text
与网站管理员合作，删除网站或应用程序中的信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: removal

Maintainer decision: `pending`

### 40. cisa-personal-security-zh-hans-v1/sentence-125

Changed: `domain, risk`

Input:

```text
在隐私设置中选择私密度最高的选项。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: privacy

Maintainer decision: `pending`

### 41. cisa-personal-security-zh-hans-v1/sentence-126

Changed: `domain`

Input:

```text
注意身份盗窃的迹象，监测金融账户，设置欺诈警报，更改所有在线账户的登录和密码信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: identity

Maintainer decision: `pending`

### 42. cisa-personal-security-zh-hans-v1/sentence-129

Changed: `domain`

Input:

```text
犯罪分子经常使用网络钓鱼策略让您打开有害链接、电子邮件或附件，这些链接、电子邮件或附件可能会要求您提供个人信息或感染您的设备。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: phishing

Maintainer decision: `pending`

### 43. cisa-personal-security-zh-hans-v1/sentence-131

Changed: `domain`

Input:

```text
网络钓鱼信息可能会以电子邮件、短信、社交媒体上的直接消息或电话的形式出现。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Complete input-only sentence; Taiwan terminology needs a lexical decision beyond character conversion.

Gemini reason: channels

Maintainer decision: `pending`

### 44. cisa-personal-security-zh-hans-v1/sentence-132

Changed: `domain, risk`

Input:

```text
警惕紧急或情绪化的语言、让您发送个人信息的请求、不可信的缩短 URL 以及不正确的电子邮件地址和链接。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: Complete input-only sentence; technical terms, abbreviations, or context-sensitive wording must be preserved carefully.

Gemini reason: redflags

Maintainer decision: `pending`

### 45. cisa-personal-security-zh-hans-v1/sentence-134

Changed: `eligible, domain`

Input:

```text
您应进行报告，并删除该邮件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | it_api_cli | baseline_guard | high | context_dependent_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: The extracted text is a list fragment, incomplete phrase, or depends on missing context.

Gemini reason: action

Maintainer decision: `pending`
