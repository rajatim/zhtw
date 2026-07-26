<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 022 (2026-07-27)

Status: advisory only; maintainer decisions pending

Packet SHA-256: `cb66ffbcc92bbe7b299e40b98b08704283164771c91862cac229930a39b94957`
Cases: 100
Exact Codex/Gemini classifications: 43
Maintainer review queue: 57

Field differences:

- Eligibility: 7
- Script: 0
- Domain: 26
- Risk: 39

## Policy Finding

Gemini marked 10 cases as eligible even though its own quality flags identified malformed or fragmentary input. These suggestions fail the declared source-quality rule and are not auto-adopted.

Neither advisory is auto-preferred. Codex must synthesize the differences before maintainer confirmation; no classification in this report has been written into the candidate pool.

## Review Queue

### 01. ready-gov-drought-zh-hans-v1/sentence-001

Changed: `domain, risk`

Input:

```text
美国几乎每个地区都会经历降雨减少的时期。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；專名、縮寫、數值單位或既有正確用語需保守保留。

Gemini reason: 基本字詞轉換，無特殊用語。'地区' -> '地區'。

Maintainer decision: `pending`

### 02. ready-gov-drought-zh-hans-v1/sentence-003

Changed: `domain`

Input:

```text
防备干旱的最好方法就是节水。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；適合作為一般字形與不需地域改寫的基準案例。

Gemini reason: 基本字詞轉換。'防备' -> '防備', '干旱' -> '乾旱', '节水' -> '節水'。

Maintainer decision: `pending`

### 03. ready-gov-drought-zh-hans-v1/sentence-005

Changed: `domain`

Input:

```text
还能作他用时，切勿将水倒入下水道，例如，可用来浇灌室内植物或花园。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；適合作為一般字形與不需地域改寫的基準案例。

Gemini reason: '下水道'、'浇灌'、'室内'、'花园' 均為兩岸通用或可直接轉換，風險較低。

Maintainer decision: `pending`

### 04. ready-gov-drought-zh-hans-v1/sentence-011

Changed: `domain, risk`

Input:

```text
将水管绝缘，减少热量损失，防止破裂。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | translation_artifact |

Codex reason: 完整且可獨立判讀；適合作為一般字形與不需地域改寫的基準案例。

Gemini reason: 用語'绝缘'在此應指保溫或隔熱，臺灣多用'隔熱'處理來'减少热量损失'(減少熱量損失)。'绝缘'(絕緣)多指電力方面。此處存在用詞差異。

Maintainer decision: `pending`

### 05. ready-gov-drought-zh-hans-v1/sentence-012

Changed: `domain`

Input:

```text
仅在水中矿物质会损坏管道时才安装软水系统。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: '软水系统'、'矿物质'在臺灣通用，但'管道'常依情境稱為'管線'。此處保留'管道'亦可理解。

Maintainer decision: `pending`

### 06. ready-gov-drought-zh-hans-v1/sentence-016

Changed: `domain, risk`

Input:

```text
安装马桶排水装置，减少冲洗所需水量。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 基本字詞轉換。'马桶' -> '馬桶', '装置' -> '裝置'。

Maintainer decision: `pending`

### 07. ready-gov-drought-zh-hans-v1/sentence-017

Changed: `domain`

Input:

```text
在水箱中放一个一加仑的塑料水罐取代马桶水流。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 中國用語'塑料'在臺灣對應'塑膠'。'加仑' -> '加侖'。主要風險為地域用詞轉換。

Maintainer decision: `pending`

### 08. ready-gov-drought-zh-hans-v1/sentence-020

Changed: `domain`

Input:

```text
不要使用垃圾处理器，将食物扔进垃圾箱或堆肥堆处理。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | translation_artifact |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: '垃圾处理器'在臺灣不普及，對應的詞是'廚餘處理機'。'垃圾箱'在臺灣通常稱為'垃圾桶'。存在用詞差異。

Maintainer decision: `pending`

### 09. ready-gov-drought-zh-hans-v1/sentence-022

Changed: `domain, risk`

Input:

```text
种植当地和/或耐旱的青草、地被、灌木和树木，长成后无需太多浇水。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 基本詞彙轉換。'耐旱'、'青草'、'灌木'、'树木'(樹木)等詞語通用。

Maintainer decision: `pending`

### 10. ready-gov-drought-zh-hans-v1/sentence-024

Changed: `domain`

Input:

```text
除非使用循环再用水，否则不要安装装饰性水景（如喷泉）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: '循环再用水' 在台灣多稱為 '回收水' 或 '中水'。'水景' 一詞可用，但 '水景設施' 或 '景觀水池' 更常見。

Maintainer decision: `pending`

### 11. ready-gov-drought-zh-hans-v1/sentence-031

Changed: `domain`

Input:

```text
割草时留得更高，草根就能长得更深，留住更多土壤水分。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；適合作為一般字形與不需地域改寫的基準案例。

Gemini reason: 基本字詞轉換。'割草'、'草根'、'土壤'、'水分' 為兩岸通用詞。

Maintainer decision: `pending`

### 12. ready-gov-drought-zh-hans-v1/sentence-033

Changed: `domain`

Input:

```text
减少或消除不常用的草坪。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；適合作為一般字形與不需地域改寫的基準案例。

Gemini reason: 基本字詞轉換。'草坪'為兩岸通用詞。

Maintainer decision: `pending`

### 13. ready-gov-drought-zh-hans-v1/sentence-037

Changed: `domain`

Input:

```text
秋冬两季仅在需要时手动浇水。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；適合作為一般字形與不需地域改寫的基準案例。

Gemini reason: '秋冬两季' -> '秋冬兩季'，'手动' -> '手動'，皆為基本轉換。

Maintainer decision: `pending`

### 14. ready-gov-drought-zh-hans-v1/sentence-039

Changed: `domain`

Input:

```text
购买天气或智能灌溉控制器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: '智能灌溉控制器' 中的 '智能' 在臺灣資訊科技領域多用 '智慧'，如 '智慧型手機'。此處可轉換為 '智慧灌溉控制器'。

Maintainer decision: `pending`

### 15. ready-gov-drought-zh-hans-v1/sentence-044

Changed: `domain`

Input:

```text
盖好泳池和水疗设备，减少水蒸发。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: '水疗设备' 在此上下文中指的應是 spa pool 或 hot tub，直翻 '水療設備' 稍嫌奇怪，台灣較常見的說法可能是 '水療池'、'按摩浴缸'。需依原文確認。

Maintainer decision: `pending`

### 16. ready-gov-drought-zh-hans-v1/sentence-047

Changed: `domain`

Input:

```text
将纸巾、昆虫和其他类似废物放入垃圾桶，而非马桶。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；適合作為一般字形與不需地域改寫的基準案例。

Gemini reason: '纸巾'(衛生紙)、'昆虫'(昆蟲)、'垃圾桶'、'马桶'(馬桶) 皆為通用或可直接對應的詞語。

Maintainer decision: `pending`

### 17. ready-gov-drought-zh-hans-v1/sentence-049

Changed: `domain, risk`

Input:

```text
只在湿身和用皂时打开水，然后再打开水洗净。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | medium | awkward_phrasing |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 句子 '只在湿身和用皂时打开水' 語法稍不自然，但意思尚可理解。應指 '僅在淋濕身體與塗抹肥皂時才開水'。'洗净'(洗淨) 為基本轉換。

Maintainer decision: `pending`

### 18. ready-gov-drought-zh-hans-v1/sentence-057

Changed: `eligible, domain, risk`

Input:

```text
接住用作他用（如植物浇水），或在炉子上或微波炉中加热。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | social_daily | baseline_guard | high | context_dependent_fragment |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 單獨抽出後缺少必要前文、含聯絡指令或來源文字異常，依 input-only 品質 gate 排除。

Gemini reason: '接住' 在此指收集流出的冷水，用 '收集' 或 '承接' 可能更貼切。'炉子' 詞意較廣，此處指 '瓦斯爐'。'微波炉' -> '微波爐'。

Maintainer decision: `pending`

### 19. ready-gov-drought-zh-hans-v1/sentence-061

Changed: `domain`

Input:

```text
大雨过后，两周内都不需要浇水。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；適合作為一般字形與不需地域改寫的基準案例。

Gemini reason: 基本字詞轉換。'大雨'、'浇水'(澆水)為通用詞。

Maintainer decision: `pending`

### 20. ready-gov-drought-zh-hans-v1/sentence-065

Changed: `eligible, domain`

Input:

```text
踩着时会弹回来，草坪就不需要水。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | social_daily | baseline_guard | high | context_dependent_fragment |
| Gemini | yes | high_stakes | baseline_guard | medium | awkward_phrasing |

Codex reason: 單獨抽出後缺少必要前文、含聯絡指令或來源文字異常，依 input-only 品質 gate 排除。

Gemini reason: '踩着时会弹回来' 語法較不順，應指 '踩踏後能回彈'。'草坪' 為通用詞。

Maintainer decision: `pending`

### 21. ready-gov-drought-zh-hans-v1/sentence-067

Changed: `domain, risk`

Input:

```text
要让草坪能更好地吸收水分并避免径流，分几次短时间浇水，而非一次长时间浇水。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀；適合作為一般字形與不需地域改寫的基準案例。

Gemini reason: '径流'是專業術語，對應繁體為'逕流'。轉換風險在於是否為常用詞，但術語對應直接。

Maintainer decision: `pending`

### 22. ready-gov-drought-zh-hans-v1/sentence-068

Changed: `domain`

Input:

```text
在车道或人行道上清洁树叶和其他碎屑时，应使用扫帚或鼓风机，而非水管。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: '鼓风机'在此情境下指'吹葉機'，直接轉換會詞意不清。'车道' -> '車道'。'人行道' -> '人行道'。

Maintainer decision: `pending`

### 23. ready-gov-drought-zh-hans-v1/sentence-069

Changed: `domain`

Input:

```text
使用洒水器或水管时，一定要有人看着。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；適合作為一般字形與不需地域改寫的基準案例。

Gemini reason: '洒水器'(灑水器)、'水管'為通用詞語。

Maintainer decision: `pending`

### 24. ready-gov-drought-zh-hans-v1/sentence-070

Changed: `domain`

Input:

```text
一根花园水管几个小时就能流出至少 600 加仑水。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀；專名、縮寫、數值單位或既有正確用語需保守保留。

Gemini reason: '加仑' 為單位，需正確轉為 '加侖'，並注意數字 '600' 不可變動。'花园水管' -> '花園水管'。

Maintainer decision: `pending`

### 25. ready-gov-drought-zh-hans-v1/sentence-071

Changed: `domain`

Input:

```text
极度干旱时，让草坪枯死，保住树木和大灌木。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；適合作為一般字形與不需地域改寫的基準案例。

Gemini reason: 基本字詞轉換。'干旱'(乾旱)、'草坪'、'树木'(樹木)、'灌木'。

Maintainer decision: `pending`

### 26. ready-gov-home-fires-zh-hans-v1/sentence-006

Changed: `risk`

Input:

```text
吸入这种超热空气会烧焦肺部，让衣服融化在皮肤上。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 基本字詞轉換。'烧焦'(燒焦)、'肺部'、'皮肤'(皮膚)。

Maintainer decision: `pending`

### 27. ready-gov-home-fires-zh-hans-v1/sentence-015

Changed: `risk`

Input:

```text
视障者可用听觉警报器，听障者可用带振动垫或闪光灯的烟雾警报器。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；專名、縮寫、數值單位或既有正確用語需保守保留。

Gemini reason: '视障者'(視障者)、'听障者'(聽障者)、'闪光灯'(閃光燈)等詞語兩岸通用。

Maintainer decision: `pending`

### 28. ready-gov-home-fires-zh-hans-v1/sentence-017

Changed: `risk`

Input:

```text
如已投保，联系保险公司获取详细说明，了解如何保护财产、进行盘点和联系火灾损失复原公司。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: '投保'、'保险公司'(保險公司)、'盘点'(盤點)等詞語可直接轉換。

Maintainer decision: `pending`

### 29. ready-gov-home-fires-zh-hans-v1/sentence-028

Changed: `eligible, risk`

Input:

```text
联系当地消防部门，获取有关正确使用和维护的协助。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | high_stakes | baseline_guard | high | context_dependent_fragment |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 單獨抽出後缺少必要前文、含聯絡指令或來源文字異常，依 input-only 品質 gate 排除。

Gemini reason: '联系' 在臺灣常用 '聯絡'。'消防部门' 可用，'消防局' 更常見。

Maintainer decision: `pending`

### 30. ready-gov-home-fires-zh-hans-v1/sentence-039

Changed: `risk`

Input:

```text
如果衣服着火，停下、趴下和滚动：立即停下，趴在地上，用手盖住脸部。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: '趴下'、'滚动'(滾動) 是標準的消防口訣用詞 'Stop, Drop, and Roll' 的翻譯，兩岸通用。

Maintainer decision: `pending`

### 31. ready-gov-home-fires-zh-hans-v1/sentence-045

Changed: `risk`

Input:

```text
与消防部门核实，确保住所可以安全进入。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀；適合作為一般字形與不需地域改寫的基準案例。

Gemini reason: 用語'核实'在臺灣較少使用，通常用'確認'。'消防部门' 可對應 '消防局' 或 '消防單位'。

Maintainer decision: `pending`

### 32. ready-gov-home-fires-zh-hans-v1/sentence-050

Changed: `risk`

Input:

```text
先放好任何火灾损失费用相关收据。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: '放好'、'收据'(收據)，基本字詞轉換。

Maintainer decision: `pending`

### 33. ready-gov-home-fires-zh-hans-v1/sentence-072

Changed: `risk`

Input:

```text
使用足够重的壁炉屏风，阻止滚动的柴火，要大到足以覆盖壁炉的整个开口才能挡住飞溅的火花。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: '壁炉屏风'(壁爐屏風)、'柴火'、'火花' 等詞語可直接轉換。

Maintainer decision: `pending`

### 34. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-001

Changed: `risk`

Input:

```text
山体滑坡发生在美国所有州和地区，可能由许多因素引起，包括地震、风暴、火山爆发、火灾和土地的人为改造。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀；專名、縮寫、數值單位或既有正確用語需保守保留。

Gemini reason: '山体滑坡'在臺灣稱為'山崩'。'风暴' -> '風暴'。'火灾' -> '火災'。此為重要地域性用詞差異。

Maintainer decision: `pending`

### 35. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-002

Changed: `risk`

Input:

```text
最危险、最危及生命和最致命的山体滑坡是那些发生得很快的山体滑坡，通常很少有人注意到。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀；適合作為一般字形與不需地域改寫的基準案例。

Gemini reason: '山体滑坡' 在臺灣稱為 '山崩'。'很少有人注意到' 在台灣可說 '幾乎不會被察覺'。

Maintainer decision: `pending`

### 36. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-004

Changed: `risk`

Input:

```text
当野火烧毁斜坡时，会在数年内增加山体滑坡的可能性。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀；適合作為一般字形與不需地域改寫的基準案例。

Gemini reason: '野火'、'斜坡' 為通用詞。'山体滑坡' -> '山崩'。

Maintainer decision: `pending`

### 37. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-009

Changed: `risk`

Input:

```text
虽然这些山体滑坡很少造成人员伤亡，但随着时间的推移，它们会对土地和财产造成破坏。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀；適合作為一般字形與不需地域改寫的基準案例。

Gemini reason: '山体滑坡' -> '山崩'。'人员伤亡' -> '人員傷亡'。

Maintainer decision: `pending`

### 38. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-011

Changed: `risk`

Input:

```text
注册您社区的警告系统。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀；適合作為一般字形與不需地域改寫的基準案例。

Gemini reason: '注册' 在台灣多用於 '註冊' (如帳號)，此處 '登記' 或 '訂閱' 可能更適合 '警告系统'(警報系統)。

Maintainer decision: `pending`

### 39. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-014

Changed: `eligible, domain, risk`

Input:

```text
将SHELTER + 您的邮政编码发送至43362( 4FEMA )，以查找您所在地区最近的避难所（例如：避难所 12345）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | high_stakes | baseline_guard | high | contact_information_only |
| Gemini | yes | it_api_cli | over_conversion_guard | high | contains_code |

Codex reason: 單獨抽出後缺少必要前文、含聯絡指令或來源文字異常，依 input-only 品質 gate 排除。

Gemini reason: 包含指令'SHELTER'、數字'43362'、'4FEMA'、'12345'，絕不可轉換。'邮政编码'在臺灣稱為'郵遞區號'。混合了指令和需要地域轉換的詞彙，風險高。

Maintainer decision: `pending`

### 40. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-023

Changed: `risk`

Input:

```text
国家洪水保险计划(NFIP)的洪水保险政策可能涵盖泥石流。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | contains_code |

Codex reason: 完整且可獨立判讀；專名、縮寫、數值單位或既有正確用語需保守保留。

Gemini reason: '国家洪水保险计划(NFIP)' 專有名詞需謹慎處理。'泥石流' -> '土石流'。

Maintainer decision: `pending`

### 41. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-025

Changed: `risk`

Input:

```text
聆听并注意是否有湍急的水流、泥浆或异常的声音。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 基本詞彙轉換。'湍急'、'泥浆'(泥漿)、'声音'(聲音)。

Maintainer decision: `pending`

### 42. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-028

Changed: `risk`

Input:

```text
景观中的巨石可能是过去泥石流的迹象。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀；適合作為一般字形與不需地域改寫的基準案例。

Gemini reason: '巨石'、'景观'(景觀)通用。'泥石流' -> '土石流'。

Maintainer decision: `pending`

### 43. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-037

Changed: `risk`

Input:

```text
栅栏、挡土墙、电线杆或树木倾斜或移动。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: '栅栏'(柵欄)、'挡土墙'(擋土牆)、'电线杆'(電線桿)、'树木'(樹木) 轉換直接。

Maintainer decision: `pending`

### 44. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-047

Changed: `risk`

Input:

```text
如果您确实被困在山体滑坡的路径上，请尽快上坡。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀；適合作為一般字形與不需地域改寫的基準案例。

Gemini reason: '山体滑坡' -> '山崩'。'路径'(路徑)、'上坡' 可直接轉換。

Maintainer decision: `pending`

### 45. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-049

Changed: `risk`

Input:

```text
如果您靠近溪流或河道，请注意水流突然增加或减少或水从清澈变为浑浊。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: '溪流'、'河道'、'清澈'、'浑浊'(混濁) 為通用詞。

Maintainer decision: `pending`

### 46. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-050

Changed: `eligible, risk`

Input:

```text
这些可能是山体滑坡即将来临的迹象。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | high_stakes | baseline_guard | high | context_dependent_fragment |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 單獨抽出後缺少必要前文、含聯絡指令或來源文字異常，依 input-only 品質 gate 排除。

Gemini reason: '山体滑坡' -> '山崩'。'来临'(來臨) -> '即將發生'。

Maintainer decision: `pending`

### 47. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-051

Changed: `eligible, risk`

Input:

```text
额外的载玻片可能会带来危险。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | high_stakes | baseline_guard | high | malformed_source_text |
| Gemini | yes | high_stakes | candidate_gap | medium | translation_artifact |

Codex reason: 單獨抽出後缺少必要前文、含聯絡指令或來源文字異常，依 input-only 品質 gate 排除。

Gemini reason: '额外的载玻片' (Extra slides) 是明顯的誤譯，應為 '额外的山崩' (Additional landslides)。'载玻片'是實驗室用品 (microscope slide)。

Maintainer decision: `pending`

### 48. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-053

Changed: `risk`

Input:

```text
洪水有时会在山体滑坡和泥石流之后发生，因为它们可能是由相同的条件引发的。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀；適合作為一般字形與不需地域改寫的基準案例。

Gemini reason: '洪水'、'山体滑坡' -> '山崩'、'泥石流' -> '土石流'。均為地域性詞彙差異。

Maintainer decision: `pending`

### 49. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-061

Changed: `risk`

Input:

```text
专业人士可以建议您预防或降低山体滑坡风险的最佳方法，而不会造成进一步的危险。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀；適合作為一般字形與不需地域改寫的基準案例。

Gemini reason: '专业人士' -> '專業人士'。'滑坡' -> '邊坡滑動' 或 '山崩'。

Maintainer decision: `pending`

### 50. ready-gov-radiation-zh-hans-v1/sentence-013

Changed: `eligible, risk`

Input:

```text
包括为每个家庭成员准备的备用换洗衣服、一个用于装受污染衣物的垃圾袋以及密封的食物、水和药品。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | high_stakes | baseline_guard | high | context_dependent_fragment |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 單獨抽出後缺少必要前文、含聯絡指令或來源文字異常，依 input-only 品質 gate 排除。

Gemini reason: '垃圾袋'通用。'受污染' 在臺灣也用，但 '遭污染' 或 '受汙染' 更常見。'药品' -> '藥品'。

Maintainer decision: `pending`

### 51. ready-gov-radiation-zh-hans-v1/sentence-017

Changed: `risk`

Input:

```text
如果您需要撤离，请与朋友或家人一起制定计划，以确定安全的住宿地点。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀；適合作為一般字形與不需地域改寫的基準案例。

Gemini reason: '撤离' 在台灣稱 '疏散'。'住宿' 通用。

Maintainer decision: `pending`

### 52. ready-gov-radiation-zh-hans-v1/sentence-032

Changed: `risk`

Input:

```text
最安全的建筑物有砖墙或混凝土墙。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀；適合作為一般字形與不需地域改寫的基準案例。

Gemini reason: '砖墙' -> '磚牆'。'混凝土' 在台灣亦稱 '混凝土' 或口語 '水泥'。

Maintainer decision: `pending`

### 53. ready-gov-radiation-zh-hans-v1/sentence-035

Changed: `risk`

Input:

```text
在最初的24小时内，辐射水平迅速下降，危险性明显降低。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；專名、縮寫、數值單位或既有正確用語需保守保留。

Gemini reason: '辐射水平'(輻射水平)、'危险性'(危險性)，可直接轉換。

Maintainer decision: `pending`

### 54. ready-gov-radiation-zh-hans-v1/sentence-036

Changed: `risk`

Input:

```text
待在室内：除非另有说明，否则请避难。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: 基本句，'待在室内'(待在室內)。'避难'(避難)。

Maintainer decision: `pending`

### 55. ready-gov-radiation-zh-hans-v1/sentence-040

Changed: `risk`

Input:

```text
庇护通常持续至少 24 小时。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: '庇护'(庇護)通用。數字 '24' 不應變動。

Maintainer decision: `pending`

### 56. ready-gov-radiation-zh-hans-v1/sentence-043

Changed: `risk`

Input:

```text
如果您已经撤离，请不要返回，直到当地政府告知您可以安全返回。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀；適合作為一般字形與不需地域改寫的基準案例。

Gemini reason: '撤离' -> '疏散'。'当地政府' -> '地方政府'。

Maintainer decision: `pending`

### 57. ready-gov-radiation-zh-hans-v1/sentence-050

Changed: `risk`

Input:

```text
如果您无法清洗，请使用抹布或干净的湿布擦拭未覆盖的任何皮肤或头发。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀；含臺灣用語或專業術語正規化候選。

Gemini reason: '抹布'、'湿布'(濕布)、'皮肤'(皮膚)、'头发'(頭髮)通用。

Maintainer decision: `pending`
