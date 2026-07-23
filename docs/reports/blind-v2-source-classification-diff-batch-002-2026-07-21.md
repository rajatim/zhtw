<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 002 (2026-07-21)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `0e646d6113b7c0134b449de725d9a08afba21f2d42fef7af65c271037fd0e305`
Cases: 100
Exact Codex/Gemini classifications: 55
Maintainer review queue: 45

Field differences:

- Eligibility: 9
- Script: 0
- Domain: 27
- Risk: 31

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

The maintainer resolved all 45 advisory disagreements and batch-confirmed the 55 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. flores-200-zho-hans-v1/dev-0243

Changed: `risk`

Input:

```text
除了搭载三台重要的科学仪器，月球探测器的每一侧都印有印度国旗图案。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 句子結構完整，為正式新聞描述。術語「月球探測器」和「搭載」在台灣有對應的常用詞彙，屬於常規轉換。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 02. flores-200-zho-hans-v1/dev-0253

Changed: `risk`

Input:

```text
被称为“11 号宇航员”的列昂诺夫是苏联最早的宇航员团队中的一员。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 包含人名（列昂諾夫）、國名（蘇聯），以及特定術語「宇航員」（台灣常用「太空人」），存在地區用詞差異。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 03. flores-200-zho-hans-v1/dev-0335

Changed: `risk`

Input:

```text
然后，旋转的苦行僧出现在舞台上。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 句子簡潔，描述性內容。專有名詞「旋轉的苦行僧」轉換直接，風險較低。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 04. flores-200-zho-hans-v1/dev-0501

Changed: `risk`

Input:

```text
它是由约翰•史密斯 (John Smith) 在 20 世纪 70 年代研发的，用于帮助缺乏经验的折纸人或动手能力差的人。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 包含人名「約翰•史密斯」，需保護其不被錯誤轉換。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 05. flores-200-zho-hans-v1/dev-0659

Changed: `domain`

Input:

```text
在夏季，也要注意北欧的蚊子。虽然这些蚊子不会传播任何疾病，但它们可能会让人感到不适。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 描述北歐旅遊注意事項，用詞通用，風險低。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 06. flores-200-zho-hans-v1/dev-0660

Changed: `risk`

Input:

```text
旧金山的经济与自身是世界级旅游胜地这一点有关，但旧金山的经济却是多元化的。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 包含地名「舊金山」，需確保專有名詞正確。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 07. flores-200-zho-hans-v1/dev-0672

Changed: `domain, risk`

Input:

```text
因此，如果启程日期为 5 月，野地露营许可证将在 1 月 1 日发放。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 描述許可證規定，用詞正式且通用。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 08. flores-200-zho-hans-v1/dev-0772

Changed: `domain`

Input:

```text
喀拉拉邦的寺庙节日极其有趣，通常有装饰华丽的大象游行、寺庙管弦乐队表演和其他庆典活动。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 包含地名「喀拉拉邦」，需保護專有名詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 09. flores-200-zho-hans-v1/dev-0775

Changed: `eligible, domain, risk`

Input:

```text
世界园艺博览会是展示花卉、植物园和与植物有关的一切。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_sentence |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 輸入殘缺、語意不清或病句程度過高，不納入候選池。

Gemini reason: 描述園藝博覽會，用詞通用。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 10. flores-200-zho-hans-v1/dev-0864

Changed: `domain`

Input:

```text
而且，在温暖的气候下细菌既可以快速繁殖，又可以在体外存活更久。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 科普內容，描述細菌繁殖，用詞通用。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 11. flores-200-zho-hans-v1/dev-0870

Changed: `domain`

Input:

```text
在不了解当地动物群的地区，切勿睡在地上的床垫或垫子上。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 旅遊建議，關於野外睡眠安全，用詞通用。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 12. flores-200-zho-hans-v1/dev-0877

Changed: `domain, risk`

Input:

```text
对于那些不熟悉医学术语的人来说，”传染性”和“触染性”这两个词的含义截然不同。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 解釋醫學術語，用詞正式，風險低。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 13. flores-200-zho-hans-v1/dev-0893

Changed: `domain, risk`

Input:

```text
雪被压实，缝隙也被填满，并用旗帜做了标记。只有专门的拖拉机以及拖着装有燃料和补给的雪橇才能通行。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 「拖拉机」在台灣多稱「牽引機」或「拖拉機」，「补给」常用「補給」，存在地區用詞差異。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 14. flores-200-zho-hans-v1/dev-0895

Changed: `domain`

Input:

```text
冬天最常见的事故原因是道路和路面（人行道）湿滑，特别是台阶。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 用詞「濕滑」、「路面」、「人行道」兩岸通用，風險低。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 15. flores-200-zho-hans-v1/dev-0910

Changed: `domain`

Input:

```text
事实上，区域码对非法复制毫无影响；一份逐位拷贝的磁盘副本在任何可以播放原盘的设备上都可以顺利播放。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 「区域码」在台灣稱「區碼」，「非法复制」稱「非法拷貝/盜拷」，「磁盘」稱「磁碟」，存在多處地區用詞差異。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 16. flores-200-zho-hans-v1/dev-0933

Changed: `domain, risk`

Input:

```text
与普通旅游签证或商务签证相比，学生签证通常有不同的要求和申请程序。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 描述簽證資訊，用詞正式通用。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 17. flores-200-zho-hans-v1/devtest-0038

Changed: `risk`

Input:

```text
一颗恒星的罗斯贝数由其光度和旋度共同决定，与等离子体流有关。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 天文學術語，用詞專業，兩岸差異小。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 18. flores-200-zho-hans-v1/devtest-0117

Changed: `domain`

Input:

```text
由于缺乏资金，且与其他疾病相比优先级较低，今年向历史上疫情最严重的地区提供疫苗的计划被推迟了。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 「疫苗」兩岸通用，但「优先级」在台灣多用「優先級」或「優先順序」，存在用詞差異。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 19. flores-200-zho-hans-v1/devtest-0152

Changed: `domain`

Input:

```text
无国界医生组织的发言人理查德·维尔曼 (Richard Veerman) 说：“安哥拉正面临有史以来最严重的疫情，当地的局势仍然非常糟糕。”
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 包含組織名、人名、地名（無國界醫生組織、理查德·維爾曼、安哥拉），需保護專有名詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 20. flores-200-zho-hans-v1/devtest-0183

Changed: `risk`

Input:

```text
美国地质调查局 (USGS) 及美国国家地震信息中心目前还没有收到有关地震破坏的即时报告。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 包含組織名稱，且「信息」在台灣稱「資訊」，存在地區用詞差異。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 21. flores-200-zho-hans-v1/devtest-0283

Changed: `risk`

Input:

```text
然而，司机的头部受到了重创。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 描述事故後果，用詞通用。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 22. flores-200-zho-hans-v1/devtest-0402

Changed: `domain`

Input:

```text
如果你看过电影《国家宝藏》，你可能会以为《独立宣言》背面会画着一份藏宝图。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 包含電影名《國家寶藏》，需保護其譯名不被錯誤轉換。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 23. flores-200-zho-hans-v1/devtest-0480

Changed: `eligible, domain, risk`

Input:

```text
事件发生的时代通常被称为欧洲史的中世纪盛时，即的 11、12 和 13世纪时期（公元 1000-1300 年）。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_sentence |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 輸入殘缺、語意不清或病句程度過高，不納入候選池。

Gemini reason: 歐洲歷史分期描述，用詞通用。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 24. flores-200-zho-hans-v1/devtest-0578

Changed: `domain`

Input:

```text
当今，几乎所有投入使用的计算机都是以处理二进制编码的信息为基础的。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 「计算机」在台灣稱「電腦」，「二进制编码」稱「二進位編碼」，存在地區用詞差異。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 25. flores-200-zho-hans-v1/devtest-0637

Changed: `risk`

Input:

```text
哲学家亚里士多德提出一种理论，即任何事物都是由土、水、空气和火四种元素中的一种或多种组成的。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 包含人名「亞里士多德」，需保護專有名詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 26. flores-200-zho-hans-v1/devtest-0687

Changed: `domain`

Input:

```text
例如，北卡罗莱纳州本尼特学校 ( Bennet School) 的学生每年都会设计一个有关他们的州府之行的网站。网站每年都会重新设计，但是老版本会在线保存，用作剪贴簿。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | candidate_gap | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 包含地名、學校名，且「网站」在台灣稱「網站」，「在线」稱「線上」，「剪贴簿」稱「剪貼簿」，存在多處地區用詞差異。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 27. flores-200-zho-hans-v1/devtest-0727

Changed: `domain`

Input:

```text
买一张万能卡（Wild Card）也有不少好处。带着这张卡，你可以进入南非的一些公园或全部的国家公园。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 包含專有名詞「萬能卡（Wild Card）」及地名「南非」，需謹慎處理。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 28. flores-200-zho-hans-v1/devtest-0808

Changed: `domain`

Input:

```text
游猎活动也许是非洲最吸引人的旅游活动，也是许多游客行程中的亮点。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 「游猎活动」在台灣多稱「狩獵旅遊」或「野外狩獵」，存在地區用詞差異。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 29. ud-chinese-cfl-v1/CFL_A_1-6_ori

Changed: `eligible, domain, risk`

Input:

```text
因为我人生第一次亲眼看见军队。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | fragmentary |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 輸入殘缺、語意不清或病句程度過高，不納入候選池。

Gemini reason: 個人生活經歷的簡單陳述，用語直接，屬於常規轉換。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 30. ud-chinese-cfl-v1/CFL_C_1-5_ori

Changed: `domain`

Input:

```text
因此为了实现这项重要的、深远的、迫切的任务，我个人得使总统理解必须注意的事项。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 語氣正式的個人陳述，句子結構完整。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 31. ud-chinese-cfl-v1/CFL_D_1-11_ori

Changed: `risk`

Input:

```text
我坐公交车去酒店。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 簡單日常陳述，用詞直接。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 32. ud-chinese-cfl-v1/CFL_D_2-22_ori

Changed: `risk`

Input:

```text
那条公路沿海岸，所以途径中有海岛和很大的桥梁。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 描述沿途風景，句子完整。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 33. ud-chinese-cfl-v1/CFL_D_2-7_ori

Changed: `eligible, domain, risk`

Input:

```text
我因开车就睡着了。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | medium | unclear_meaning |
| Gemini | yes | social_daily | baseline_guard | medium | - |

Codex reason: 輸入殘缺、語意不清或病句程度過高，不納入候選池。

Gemini reason: 句子語法稍有不自然（「因開車就睡著了」），但意思尚清晰，屬於個人日常描述。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 34. ud-chinese-cfl-v1/CFL_F_2-4_ori

Changed: `eligible, domain, risk`

Input:

```text
所以我一有时间，就带着一把钱和一个行李箱去旅行。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_sentence |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 輸入殘缺、語意不清或病句程度過高，不納入候選池。

Gemini reason: 個人旅行習慣描述，用詞直接。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 35. ud-chinese-cfl-v1/CFL_H_1-10_ori

Changed: `risk`

Input:

```text
丛林的家里没有电和没有卫生间。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 簡單描述句，結構清晰。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 36. ud-chinese-cfl-v1/CFL_H_2-12_ori

Changed: `risk`

Input:

```text
晚上和朋友在山脚下的客栈里面开派对玩游戏，教他们玩韩国的游戏，真的特别有趣！
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 包含地名「韓國」，需保護專有名詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 37. ud-chinese-cfl-v1/CFL_I_1-12_ori

Changed: `eligible, domain, risk`

Input:

```text
有一天，他给我介绍一个他的堂妹了，然后那个堂妹真的喜欢我了，所以她给家人告诉了我真的是一个真的好女孩儿。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_sentence |
| Gemini | yes | social_daily | baseline_guard | medium | - |

Codex reason: 輸入殘缺、語意不清或病句程度過高，不納入候選池。

Gemini reason: 句子稍長且結構有些繞，但基本語意清晰。存在「告訴了我真的是一個真的好女孩兒」等輕微語法瑕疵。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 38. ud-chinese-cfl-v1/CFL_I_1-4_ori

Changed: `risk`

Input:

```text
虽然他的年龄比我小俩岁，但看起来好像个成熟的男人。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 包含口語化的「小倆歲」，但句子整體通順。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 39. ud-chinese-cfl-v1/CFL_I_1-8_ori

Changed: `risk`

Input:

```text
然后他给我表白了，我们成为情侣了。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 個人關係的描述，用詞直接。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 40. ud-chinese-cfl-v1/CFL_L_1-10_ori

Changed: `eligible, domain, risk`

Input:

```text
时光很快快过两个月了。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_sentence |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 輸入殘缺、語意不清或病句程度過高，不納入候選池。

Gemini reason: 個人感受描述，句子通順。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 41. ud-chinese-cfl-v1/CFL_L_1-15_ori

Changed: `eligible, domain, risk`

Input:

```text
那时我的心情是这样的：“天池不是令我流了很多眼泪的那个池吗？
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | medium | fragmentary, malformed_sentence |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 輸入殘缺、語意不清或病句程度過高，不納入候選池。

Gemini reason: 包含地名「天池」，需保護專有名詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 42. ud-chinese-cfl-v1/CFL_L_1-1_ori

Changed: `risk`

Input:

```text
对我来说最难忘记的事就是有关天池和找对象的事情。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | high | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 包含地名「天池」，需保護專有名詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 43. ud-chinese-cfl-v1/CFL_M_1-31_ori

Changed: `eligible, domain, risk`

Input:

```text
辛亏我遇到她，否则我不会了解爱情的意义，我来中国学习汉语便很快忘记了她，可是我很怕以后爱上别的女孩子，因为分手的感觉很难过，我不想再来一次。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | typo |
| Gemini | no | null | null | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 「辛亏」應為「幸虧」，且句子邏輯「來中國學習漢語便很快忘記了她」不甚連貫，不適合作為基準。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 44. ud-chinese-cfl-v1/CFL_P_1-6_ori

Changed: `risk`

Input:

```text
另外和我以前想象完全不一的是中国的饮食非常符合我的味口。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | typo |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 「味口」應為「胃口」，包含地名「中國」，需保護專有名詞。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`

### 45. ud-chinese-cfl-v1/CFL_Z_1-21_ori

Changed: `risk`

Input:

```text
看来自行车已经成为大多北京人生活中不可缺少的一部分。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 句意可獨立判讀；依輸入語域與詞彙風險分類。

Gemini reason: 個人觀察總結，句子通順。

Maintainer decision: `codex` accepted by `tim` on `2026-07-21`
