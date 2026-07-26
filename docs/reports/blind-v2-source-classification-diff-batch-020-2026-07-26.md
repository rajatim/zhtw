<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 020 (2026-07-26)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `6c14bba7c61829f927fdbf311040aefb70c71a3bfb19dbebcc9089c6eee4cb42`
Cases: 100
Exact Codex/Gemini classifications: 23
Maintainer review queue: 77

Field differences:

- Eligibility: 6
- Script: 0
- Domain: 34
- Risk: 59

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

The maintainer resolved all 77 advisory disagreements and batch-confirmed the 23 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. cisa-personal-security-zh-hans-v1/sentence-013

Changed: `risk`

Input:

```text
您是否表现出某种群体身份，该身份会让您成为具有吸引力的目标？
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 個人安全問題，語氣正式。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 02. cisa-personal-security-zh-hans-v1/sentence-040

Changed: `risk`

Input:

```text
如果公众抗议或示威活动发生在您家或您的营业场所附近，或甚至就发生在您的房产中，无论其任务和意图如何，请保持冷静。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 應對突發事件的指示，語氣正式。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 03. cisa-personal-security-zh-hans-v1/sentence-053

Changed: `risk`

Input:

```text
考虑随时携带手机。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 個人安全建議，簡單明確。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 04. cisa-personal-security-zh-hans-v1/sentence-067

Changed: `risk`

Input:

```text
避免打电话、戴耳机或发送长短信。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 具體行為建議，保持警覺。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 05. cisa-personal-security-zh-hans-v1/sentence-069

Changed: `risk`

Input:

```text
使用银行 ATM 机时，请避免在公众视线范围内展示货币。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；代碼、縮寫、機構名或技術搭配需保守保留。

Gemini reason: 金融安全提示，具體場景。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 06. cisa-personal-security-zh-hans-v1/sentence-080

Changed: `domain, risk`

Input:

```text
在社交媒体上传播任何实施攻击的图像或想法。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | high_stakes | baseline_guard | high | context_dependent_fragment |
| Gemini | no | null | null | high | fragment |

Codex reason: 單獨抽出後為條列片段、黏連標題、聯絡資訊或來源文字異常，依 input-only 品質 gate 排除。

Gemini reason: 句子不完整，疑似清單項目，缺乏上下文。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 07. cisa-personal-security-zh-hans-v1/sentence-095

Changed: `risk`

Input:

```text
确保在旅途中锁好所有车门和后备箱。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 車輛安全指示，清楚明確。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 08. cisa-personal-security-zh-hans-v1/sentence-102

Changed: `risk`

Input:

```text
如果可以，请前往最近的警察局，切勿开车回家。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 緊急情況下的應對指示，重要性高。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 09. cisa-personal-security-zh-hans-v1/sentence-128

Changed: `risk`

Input:

```text
如果担心自身人身安全，请联系当地执法部门了解下一步措施。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 官方建議，指導民眾尋求協助。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 10. ftc-heads-up-simplified-v1/sentence-015

Changed: `risk`

Input:

```text
问一下自己：“想不想让某人在午餐时与全餐厅的人分享那张照片或者那个视频？”
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 社交媒體隱私建議，使用問句引導思考。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 11. ftc-heads-up-simplified-v1/sentence-019

Changed: `risk`

Input:

```text
发布前问一下他们：“您同意我在社交媒体上发布这个东西吗？”
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 社交禮儀建議，關於尊重他人。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 12. ftc-heads-up-simplified-v1/sentence-034

Changed: `risk`

Input:

```text
网上容易产生误解。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 網路社交觀察，句子簡短但完整。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 13. ftc-heads-up-simplified-v1/sentence-039

Changed: `eligible`

Input:

```text
网上书写的这种风格就跟面对面大喊大叫一样没有区别。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | social_daily | baseline_guard | high | context_dependent_fragment |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 單獨抽出後為條列片段、黏連標題、聯絡資訊或來源文字異常，依 input-only 品質 gate 排除。

Gemini reason: 解釋網路行為的比喻，生動易懂。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 14. ftc-heads-up-simplified-v1/sentence-062

Changed: `domain`

Input:

```text
检查自己的位置设置。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；適合作為高風險或日常語境的基準轉換案例。

Gemini reason: 數位安全操作指令，簡潔。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 15. ftc-heads-up-simplified-v1/sentence-069

Changed: `domain, risk`

Input:

```text
每次都扪心自问：“这个应用软件需要知道我的位置吗？”
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 引導使用者思考隱私設定，實用性高。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 16. ftc-heads-up-simplified-v1/sentence-071

Changed: `risk`

Input:

```text
通过短信、社交媒体或电子游戏交朋友可能很有趣 — 但有些人的实际身份与网上身份大相径庭。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 關於網路交友的提醒，揭示風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 17. ftc-heads-up-simplified-v1/sentence-075

Changed: `domain, risk`

Input:

```text
即使邮件像是来自认识的朋友、家人或公司 — 或者说不回复会有不好的后果也不要给出个人信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 網路安全警語，關於個資保護。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 18. ftc-heads-up-simplified-v1/sentence-093

Changed: `domain`

Input:

```text
不要与任何人分享密码，即使是最好的朋友或恋人。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；適合作為高風險或日常語境的基準轉換案例。

Gemini reason: 密碼安全金句，適用各種關係。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 19. ftc-heads-up-simplified-v1/sentence-102

Changed: `domain, risk`

Input:

```text
多重身份验证将你知道的事物（例如密码）和你有的事物（例如应用软件生成的密码）或你自身（例如指纹）组合到一起。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；代碼、縮寫、機構名或技術搭配需保守保留。

Gemini reason: 解釋多重要素驗證的定義。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 20. ftc-heads-up-simplified-v1/sentence-103

Changed: `domain`

Input:

```text
如果密码泄露，请迅速更改。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；適合作為高風險或日常語境的基準轉換案例。

Gemini reason: 密碼洩露後的標準應對程序。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 21. ftc-heads-up-simplified-v1/sentence-106

Changed: `risk`

Input:

```text
什么是最好的在线体验方式？
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 開放式問題，引導思考。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 22. ftc-heads-up-simplified-v1/sentence-109

Changed: `eligible, domain`

Input:

```text
这样有助于防范新的安全威胁。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | social_daily | baseline_guard | high | context_dependent_fragment |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 單獨抽出後為條列片段、黏連標題、聯絡資訊或來源文字異常，依 input-only 品質 gate 排除。

Gemini reason: 軟體更新的重要性，資訊安全領域。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 23. osha-chainsaw-safety-simplified-v1/sentence-002

Changed: `risk`

Input:

```text
检查控制装置、链条张力以及所有的螺栓和手柄，以确保它们正常工作并依照制造商的说明书进行了调整。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 操作機械前的安全檢查步驟。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 24. osha-chainsaw-safety-simplified-v1/sentence-009

Changed: `risk`

Input:

```text
切勿尝试为运行中的链锯或热的链锯加油。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 操作機械時的禁止事項，安全規則。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 25. osha-chainsaw-safety-simplified-v1/sentence-012

Changed: `risk`

Input:

```text
在崎岖不平的地形上搬运链锯时，请关闭链锯或接通链锯制动器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 特定情境下的安全操作指南。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 26. osha-chainsaw-safety-simplified-v1/sentence-016

Changed: `risk`

Input:

```text
注意不要让树干或树枝卡住锯条。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 操作中的注意事項，預防意外。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 27. osha-chainsaw-safety-simplified-v1/sentence-020

Changed: `risk`

Input:

```text
保持端头防护装置开启。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 安全裝置的使用指示，簡潔有力。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 28. osha-disaster-cleanup-simplified-v1/sentence-025

Changed: `domain, risk`

Input:

```text
被倒下的树枝砸中或压伤。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | high_stakes | baseline_guard | high | context_dependent_fragment |
| Gemini | no | null | null | high | fragment |

Codex reason: 單獨抽出後為條列片段、黏連標題、聯絡資訊或來源文字異常，依 input-only 品質 gate 排除。

Gemini reason: 句子不完整，為清單項目，描述一種危險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 29. osha-disaster-cleanup-simplified-v1/sentence-027

Changed: `domain, risk`

Input:

```text
在抬起、移动树枝和其他碎片时拉伤和扭伤。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | high_stakes | baseline_guard | high | context_dependent_fragment |
| Gemini | no | null | null | high | fragment |

Codex reason: 單獨抽出後為條列片段、黏連標題、聯絡資訊或來源文字異常，依 input-only 品質 gate 排除。

Gemini reason: 句子不完整，為清單項目，描述一種傷害。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 30. osha-disaster-cleanup-simplified-v1/sentence-028

Changed: `risk`

Input:

```text
联系供电公司断电，并将电力线进行接地或屏蔽。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 處理電力線的安全程序。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 31. osha-disaster-cleanup-simplified-v1/sentence-045

Changed: `domain, risk`

Input:

```text
由于加油及燃料储存不当而引起的火灾。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | high_stakes | baseline_guard | high | context_dependent_fragment |
| Gemini | no | null | null | high | fragment |

Codex reason: 單獨抽出後為條列片段、黏連標題、聯絡資訊或來源文字異常，依 input-only 品質 gate 排除。

Gemini reason: 句子不完整，為清單項目，描述一種火災風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 32. osha-disaster-cleanup-simplified-v1/sentence-053

Changed: `risk`

Input:

```text
使用适当的照明、信号旗手和工地通讯。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 工地交通與通訊安全措施。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 33. osha-disaster-cleanup-simplified-v1/sentence-054

Changed: `risk`

Input:

```text
确保车辆操作人员已经接受适当的培训。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 對車輛操作人員的培訓要求。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 34. osha-disaster-cleanup-simplified-v1/sentence-055

Changed: `risk`

Input:

```text
始终使用安全带和翻车保护装置。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 車輛安全裝置的強制使用規定。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 35. osha-disaster-cleanup-simplified-v1/sentence-057

Changed: `domain, risk`

Input:

```text
进入受限的、有窒息危险的地方，以及其他的密闭空间。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | high_stakes | baseline_guard | high | context_dependent_fragment |
| Gemini | no | null | null | high | fragment |

Codex reason: 單獨抽出後為條列片段、黏連標題、聯絡資訊或來源文字異常，依 input-only 品質 gate 排除。

Gemini reason: 句子不完整，為清單項目，描述一種危險空間。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 36. osha-disaster-cleanup-simplified-v1/sentence-060

Changed: `risk`

Input:

```text
正确选择和使用个人防护装备（PPE），其中可能包括呼吸保护设备，同时遵守29 CFR 1926.1101中所列的其他程序。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；代碼、縮寫、機構名或技術搭配需保守保留。

Gemini reason: 個人防護裝備的規定，提及法規編號。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 37. osha-disaster-cleanup-simplified-v1/sentence-063

Changed: `eligible`

Input:

```text
通过在构筑定边坡、边坡、撑柱或掩护支架来防止塌陷。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | high_stakes | baseline_guard | high | malformed_source_text |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 單獨抽出後為條列片段、黏連標題、聯絡資訊或來源文字異常，依 input-only 品質 gate 排除。

Gemini reason: 防止塌陷的工程方法。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 38. osha-disaster-cleanup-simplified-v1/sentence-076

Changed: `domain, risk`

Input:

```text
语音电话是(202)693-1999；电传打字机(TTY)是： (877)889-5627。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | high_stakes | over_conversion_guard | high | contact_information_only |
| Gemini | no | null | null | high | contact_info |

Codex reason: 單獨抽出後為條列片段、黏連標題、聯絡資訊或來源文字異常，依 input-only 品質 gate 排除。

Gemini reason: 僅包含聯絡電話，無通用內容。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 39. osha-fallen-workers-family-simplified-v1/sentence-001

Changed: `domain, risk`

Input:

```text
来自 Tonya Ford的信息 OSHA家庭联络员亲人的离世是一个家庭最痛苦的事情之一。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | high_stakes | baseline_guard | high | malformed_source_text |
| Gemini | no | null | null | high | context_dependent |

Codex reason: 單獨抽出後為條列片段、黏連標題、聯絡資訊或來源文字異常，依 input-only 品質 gate 排除。

Gemini reason: 信件開頭，包含特定人名與職稱，非通用語句。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 40. osha-fallen-workers-family-simplified-v1/sentence-003

Changed: `domain`

Input:

```text
请在您方便的时候与我联系。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；適合作為高風險或日常語境的基準轉換案例。

Gemini reason: 標準的商業或官方溝通信件用語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 41. osha-fallen-workers-family-simplified-v1/sentence-005

Changed: `domain`

Input:

```text
OSHA 对您的损失深表遗憾。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；適合作為高風險或日常語境的基準轉換案例。

Gemini reason: 官方的制式慰問語句。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 42. osha-fallen-workers-family-simplified-v1/sentence-006

Changed: `domain`

Input:

```text
我们将竭诚为您服务。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；適合作為高風險或日常語境的基準轉換案例。

Gemini reason: 官方的制式服務承諾語句。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 43. osha-fallen-workers-family-simplified-v1/sentence-009

Changed: `domain`

Input:

```text
承认你的失落和哀伤感情。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；適合作為高風險或日常語境的基準轉換案例。

Gemini reason: 心理健康建議，語氣溫和。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 44. osha-fallen-workers-family-simplified-v1/sentence-010

Changed: `domain`

Input:

```text
专注于可以掌控的生活方面。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；適合作為高風險或日常語境的基準轉換案例。

Gemini reason: 心理健康建議，關於掌控感。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 45. osha-fallen-workers-family-simplified-v1/sentence-012

Changed: `domain, risk`

Input:

```text
22 个州计划（21 个州和波多黎各）既包括私营企业，也包括州和地方政府部门。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；代碼、縮寫、機構名或技術搭配需保守保留。

Gemini reason: 對州計劃覆蓋範圍的說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 46. osha-fallen-workers-family-simplified-v1/sentence-018

Changed: `domain, risk`

Input:

```text
您可以与当地的 OSHA 办事处联系，询问案件的进展情况或提出问题。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；代碼、縮寫、機構名或技術搭配需保守保留。

Gemini reason: 指導民眾如何與政府機構互動。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 47. osha-fallen-workers-family-simplified-v1/sentence-019

Changed: `domain, risk`

Input:

```text
如果你能提供有助于检查的信息或证据，请通过写信、打电话或发电子邮件的方式与当地 OSHA 办事处分享。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；代碼、縮寫、機構名或技術搭配需保守保留。

Gemini reason: 指導民眾如何提供資訊給政府機構。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 48. osha-small-business-consultation-simplified-v1/sentence-001

Changed: `domain, risk`

Input:

```text
每个已避免的工伤节省大约 8500美元，一个已避免的工人赔偿诉求可以让您的保险率，以及受伤致病率保持在低水平，而这可以让您在其他公司选择可靠的业务合作伙伴时更加具有吸引力。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 說明工傷預防的經濟效益，包含具體數字。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 49. osha-small-business-consultation-simplified-v1/sentence-003

Changed: `domain`

Input:

```text
工人更倾向于留在一个关注他们健康的公司。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；適合作為高風險或日常語境的基準轉換案例。

Gemini reason: 關於員工留存與企業健康的正面陳述。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 50. osha-small-business-consultation-simplified-v1/sentence-006

Changed: `domain, risk`

Input:

```text
安全咨询可以帮助企业去提问和思考必要的问题，来创建一个安全的工作环境。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 說明安全諮詢服務的價值。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 51. osha-small-business-consultation-simplified-v1/sentence-009

Changed: `domain, risk`

Input:

```text
目标是在现在以及未来去降低工人受伤或致疾的可能性。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 陳述安全工作的目標。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 52. osha-small-business-consultation-simplified-v1/sentence-012

Changed: `domain, risk`

Input:

```text
顾问会与管理层和工人代表会面，谈论顾问的职责和雇主的义务。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 描述諮詢流程中的一個步驟。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 53. osha-small-business-consultation-simplified-v1/sentence-014

Changed: `domain, risk`

Input:

```text
顾问可以审阅您的安全与健康管理项目，甚至可以免费为您提供职业健康样本。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 說明顧問可提供的具體服務。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 54. osha-small-business-consultation-simplified-v1/sentence-016

Changed: `domain, risk`

Input:

```text
您会得知需要提高哪些方面，您所做的正确举动，成本方面的考虑，以及如何持续进步。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 總結諮詢服務帶來的益處。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 55. osha-small-business-consultation-simplified-v1/sentence-020

Changed: `domain, risk`

Input:

```text
他们的专业背景，结合OSHA 的培训，使他们成为了理想选择，来帮助您找到有安全与健康隐患之处，不管是在您所有的设备中，还是在部分设备中。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 描述顧問的專業資格與能力。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 56. osha-work-zone-traffic-simplified-v1/sentence-003

Changed: `risk`

Input:

```text
司机、徒步工人和行人必须能够看到并理解正确的路线。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 工作區交通管制的基本原則。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 57. osha-work-zone-traffic-simplified-v1/sentence-006

Changed: `risk`

Input:

```text
经批准的交通控制装置，包括锥筒、桶、分隔物和标志物，也可在作业区内使用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 列舉可使用的交通控制裝置。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 58. ready-gov-earthquakes-zh-hans-v1/sentence-015

Changed: `risk`

Input:

```text
标准的房主保险不包括地震损坏。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 關於保險覆蓋範圍的重要資訊。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 59. ready-gov-earthquakes-zh-hans-v1/sentence-017

Changed: `risk`

Input:

```text
放好驻车制动器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 駕駛時的地震應對指令。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 60. ready-gov-earthquakes-zh-hans-v1/sentence-020

Changed: `risk`

Input:

```text
如在室内，呆在里面，不要跑到外面，避开门口。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 室內地震應對指令。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 61. ready-gov-earthquakes-zh-hans-v1/sentence-037

Changed: `risk`

Input:

```text
如果所在地区可能发生海啸，在震动停止后应立即前往内陆或地势较高的地方。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 地震後應對海嘯風險的指示。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 62. ready-gov-floods-zh-hans-v1/sentence-003

Changed: `eligible`

Input:

```text
由雨、雪、沿海风暴、风暴潮及大坝和其他水系统溢流造成。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | high_stakes | baseline_guard | high | context_dependent_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 單獨抽出後為條列片段、黏連標題、聯絡資訊或來源文字異常，依 input-only 品質 gate 排除。

Gemini reason: 解釋洪水成因。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 63. ready-gov-floods-zh-hans-v1/sentence-016

Changed: `risk`

Input:

```text
紧急警示系统 (EAS) 和国家海洋和大气管理局 (NOAA) 气象无线电也提供紧急情况警示。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；代碼、縮寫、機構名或技術搭配需保守保留。

Gemini reason: 提供獲取緊急警報的途徑資訊。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 64. ready-gov-floods-zh-hans-v1/sentence-032

Changed: `risk`

Input:

```text
如果生病并需要就医，请联系医护人员。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 關於尋求醫療協助的建議。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 65. ready-gov-floods-zh-hans-v1/sentence-033

Changed: `risk`

Input:

```text
如果可能，请等待进一步的医护服务说明和适当的庇护所。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 災時尋求庇護的建議。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 66. ready-gov-floods-zh-hans-v1/sentence-034

Changed: `risk`

Input:

```text
收听 EAS、NOAA 天气广播或当地警示系统，了解有关洪水的最新紧急信息和说明。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；代碼、縮寫、機構名或技術搭配需保守保留。

Gemini reason: 獲取最新緊急資訊的指示。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 67. ready-gov-floods-zh-hans-v1/sentence-050

Changed: `risk`

Input:

```text
如果安全，要关闭电源以防触电。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 預防觸電的安全指示。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 68. ready-gov-hurricanes-zh-hans-v1/sentence-006

Changed: `domain`

Input:

```text
大西洋飓风季：6月1日至11月30日。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；適合作為高風險或日常語境的基準轉換案例。

Gemini reason: 資訊性陳述，提供颶風季節時間。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 69. ready-gov-hurricanes-zh-hans-v1/sentence-007

Changed: `domain`

Input:

```text
中太平洋台风季：6月1日至11月30日。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；適合作為高風險或日常語境的基準轉換案例。

Gemini reason: 資訊性陳述，提供颱風季節時間。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 70. ready-gov-hurricanes-zh-hans-v1/sentence-008

Changed: `eligible`

Input:

```text
了解您的飓风风险飓风不仅是沿海地区的问题。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | high_stakes | baseline_guard | high | merged_heading |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 單獨抽出後為條列片段、黏連標題、聯絡資訊或來源文字異常，依 input-only 品質 gate 排除。

Gemini reason: 提醒民眾颶風風險的普遍性。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 71. ready-gov-hurricanes-zh-hans-v1/sentence-012

Changed: `domain, risk`

Input:

```text
确保您的企业制定了业务连续性计划，以便在灾难发生时维持运营。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 對企業的災難應變建議。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 72. ready-gov-hurricanes-zh-hans-v1/sentence-015

Changed: `risk`

Input:

```text
遵循当地应急管理人员的指示，他们会与州、地方、部落及领地机构和合作伙伴密切协作。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 強調聽從官方指示的重要性。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 73. ready-gov-hurricanes-zh-hans-v1/sentence-024

Changed: `eligible`

Input:

```text
收集物资为家庭储备足够的物资。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | high_stakes | baseline_guard | high | merged_heading |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 單獨抽出後為條列片段、黏連標題、聯絡資訊或來源文字異常，依 input-only 品質 gate 排除。

Gemini reason: 準備防災物資的指令。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 74. ready-gov-hurricanes-zh-hans-v1/sentence-029

Changed: `risk`

Input:

```text
若您居住在强制疏散区，且当地官员要求您撤离，请立即行动。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 關於強制疏散的明確指示。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 75. ready-gov-hurricanes-zh-hans-v1/sentence-031

Changed: `risk`

Input:

```text
在指定的风暴避难所或室内房间避风。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 風暴期間的避難指令。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 76. ready-gov-hurricanes-zh-hans-v1/sentence-039

Changed: `risk`

Input:

```text
清理霉菌或其他杂物时，请穿戴防护服并使用合适的面部防护罩或口罩。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 災後清理時使用防護裝備的指示。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 77. ready-gov-hurricanes-zh-hans-v1/sentence-052

Changed: `domain`

Input:

```text
请联系您的保险公司寻求帮助。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；適合作為高風險或日常語境的基準轉換案例。

Gemini reason: 災後處理保險事務的建議。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`
