<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 008 (2026-07-23)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `91979d925fd5e084ef315fe78982d9cd3031e2a81bba3c531c18f2cd2907b3e2`
Cases: 32
Exact Codex/Gemini classifications: 7
Maintainer review queue: 25

Field differences:

- Eligibility: 2
- Script: 0
- Domain: 22
- Risk: 15

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

The maintainer resolved all 25 advisory disagreements and batch-confirmed the 7 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. nps-essential-acadia-simplified-v1/sentence-001

Changed: `domain, risk`

Input:

```text
欢迎来到阿卡迪亚国家公园，它是北大西洋海岸线上的皇冠瑰宝。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整旅遊介紹句；保留國家公園專名。

Gemini reason: 公園介紹，用語較為正式。'瑰宝'在台灣較常用'瑰寶'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 02. nps-essential-acadia-simplified-v1/sentence-002

Changed: `domain`

Input:

```text
请在 nps.gov/acadia 上了解有关公园的更多信息并制定游览计划。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整旅遊規劃句；網址需保持不變。

Gemini reason: 包含不應轉換的網址 (URL)。'游览'在台灣多用'遊覽'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 03. nps-essential-acadia-simplified-v1/sentence-003

Changed: `domain`

Input:

```text
所有 16 岁及以上的游客都必须持有公园通行证。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整入園規定；通行證語境具地域用語價值。

Gemini reason: 涉及公園入場規定，屬重要資訊。'通行证'在台灣多用'通行證'，'游客'多用'遊客'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 04. nps-essential-acadia-simplified-v1/sentence-004

Changed: `domain, risk`

Input:

```text
所有车辆必须出示通过挡风玻璃清晰可见的通行证。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整車輛通行證規定。

Gemini reason: 涉及車輛規定，為重要安全資訊。'车辆'對應'車輛'，'挡风玻璃'對應'擋風玻璃'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 05. nps-essential-acadia-simplified-v1/sentence-005

Changed: `eligible, domain, risk`

Input:

```text
go.nps.gov/ AcadiaPass 在线全面介绍了通行证购买选项。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_url_subject |
| Gemini | yes | formal_news | over_conversion_guard | high | minor_spacing_issue |

Codex reason: 以帶空格的裸網址作句子主詞，屬網頁版面殘留。

Gemini reason: 包含不應轉換的網址及專有名稱(AcadiaPass)。'在线'在台灣多用'線上'。網址與後文間有不自然的空格。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 06. nps-essential-acadia-simplified-v1/sentence-006

Changed: `domain, risk`

Input:

```text
如果您想在5月下旬至10月中旬之间开车沿凯迪拉克山峰路行驶，您还需要预订车辆。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整旅遊預約句；保留山峰路專名。

Gemini reason: 涉及車輛預約規定，為重要資訊。'凯迪拉克'為地名，'预订'在台灣多用'預約'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 07. nps-essential-acadia-simplified-v1/sentence-007

Changed: `domain`

Input:

```text
预定只能提前在线出售，不能在公园内亲自购买。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整線上預約規則，具臺灣用語差異。

Gemini reason: 購票規定，屬重要資訊。'预定'對應'預訂'，'在线'在台灣多用'線上'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 08. nps-essential-acadia-simplified-v1/sentence-008

Changed: `domain`

Input:

```text
在公园露营地露营需要提前在 Recreation.gov 上预订。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整露營預約句；網站名稱需保持不變。

Gemini reason: 露營規定，屬重要資訊。包含不應轉換的專有網址(Recreation.gov)。'预订'在台灣多用'預約'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 09. nps-essential-acadia-simplified-v1/sentence-009

Changed: `domain, risk`

Input:

```text
阿卡迪亚的任何地方都不允许野外露营或过夜停车。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整公園禁止事項，含露營與停車用語。

Gemini reason: 禁止規定，關乎公共秩序與安全。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 10. nps-essential-acadia-simplified-v1/sentence-010

Changed: `eligible, domain, risk`

Input:

```text
附近的城镇可以提供住宿。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 「附近」缺少句內參照地點，無法獨立裁決。

Gemini reason: 提供旅遊資訊。'城镇'在台灣多用'城鎮'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 11. nps-essential-acadia-simplified-v1/sentence-011

Changed: `domain`

Input:

```text
除凯迪拉克山以外的公园大部分地区和周边社区，都可提供免票的 Island Explorer 服务。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整交通服務句；保留服務與地名專名。

Gemini reason: 提供交通資訊。包含不應轉換的專有名稱(Island Explorer)。'凯迪拉克'為地名。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 12. nps-essential-acadia-simplified-v1/sentence-013

Changed: `domain, risk`

Input:

```text
阿卡迪亚公园欢迎宠物，但必须遵守相关规定。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整寵物規定引介；保留公園專名。

Gemini reason: 寵物規定，關乎公共秩序。'宠物'在台灣用'寵物'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 13. nps-essential-acadia-simplified-v1/sentence-015

Changed: `domain`

Input:

```text
请收集动物粪便并丢弃在垃圾容器中。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整寵物清潔指示，垃圾容器具地域用語差異。

Gemini reason: 公共衛生規定。'垃圾容器'在台灣多用'垃圾桶'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 14. nps-essential-acadia-simplified-v1/sentence-017

Changed: `risk`

Input:

```text
您的安全取决于您自己的正确判断。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 可獨立理解的安全提醒。

Gemini reason: 強調個人責任的安全警告。'判断'對應'判斷'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 15. nps-essential-acadia-simplified-v1/sentence-019

Changed: `risk`

Input:

```text
请不要将手机当作地图或手电筒。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整手機與戶外安全提醒。

Gemini reason: 安全建議，提醒勿過度依賴電子產品。'手机'對應'手機'，'手电筒'對應'手電筒'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 16. nps-essential-acadia-simplified-v1/sentence-021

Changed: `domain, risk`

Input:

```text
自行车和马匹不允许在徒步道上骑行。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整步道使用規定。

Gemini reason: 明確的禁止規定。'自行车'在台灣也用'自行車'或'腳踏車'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 17. nps-essential-acadia-simplified-v1/sentence-022

Changed: `domain, risk`

Input:

```text
马车道全年开放，可供多种娱乐使用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整休閒設施說明。

Gemini reason: 設施用途說明。'马车道'對應'馬車道'，'娱乐'對應'娛樂'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 18. nps-essential-acadia-simplified-v1/sentence-023

Changed: `risk`

Input:

```text
行人必须为马让路，骑自行车的人必须为马和行人让路。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整通行安全規則，含讓路語境。

Gemini reason: 路權規定，關乎安全。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 19. nps-essential-acadia-simplified-v1/sentence-024

Changed: `domain`

Input:

```text
只有1类电动自行车才允许在马车道上行驶。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整電動自行車分類規定。

Gemini reason: 交通工具規定。'1类' 指 'Class 1'，'电动自行车'在台灣稱'電動輔助自行車'或'電動自行車'，定義可能不同。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 20. nps-essential-acadia-simplified-v1/sentence-025

Changed: `domain`

Input:

```text
禁止使用机动车辆和2类、3类电动自行车。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整車輛禁止規定，機動車輛具地域語境。

Gemini reason: 禁止規定。'机动车辆'對應'機動車輛'。'2类、3类'指'Class 2, Class 3'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 21. nps-essential-acadia-simplified-v1/sentence-027

Changed: `domain, risk`

Input:

```text
请让阿卡迪亚保持原有的样子。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整環境保護號召；保留公園專名。

Gemini reason: 保護環境的原則性呼籲。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 22. nps-essential-acadia-simplified-v1/sentence-028

Changed: `domain, risk`

Input:

```text
您只能在指定的步道和耐用的地面上行走。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整步道與地面使用規定。

Gemini reason: 環境保護及個人安全規定，屬於 Leave No Trace 原則。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 23. nps-essential-acadia-simplified-v1/sentence-029

Changed: `domain, risk`

Input:

```text
请收拾垃圾和宠物垃圾。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整垃圾清理指示。

Gemini reason: 環境衛生規定。'宠物垃圾'對應'寵物排泄物'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 24. nps-essential-acadia-simplified-v1/sentence-031

Changed: `domain`

Input:

```text
请勿堆放岩石或改变用于步道导航的石标。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整步道保護規定，石標與導航用語具地域價值。

Gemini reason: 禁止改變環境及破壞步道標示，關乎多數遊客安全。'石标'在台灣可能稱'石堆'或'疊石路標'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`

### 25. nps-essential-acadia-simplified-v1/sentence-032

Changed: `domain`

Input:

```text
如果您发现文物，请将它放在原处，拍张照片，记下位置，然后告诉公园护林员。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整文物處置規定，護林員具臺灣地域用語差異。

Gemini reason: 關於發現文物的處理方式規定。'护林员'在台灣常稱'巡山員'或'森林護管員'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-23`
