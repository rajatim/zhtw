<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 025 (2026-07-27)

Status: advisory only; maintainer decisions pending

Packet SHA-256: `429922cb4772c5ff22d2bd24a3f8c8adb48ecc321884bbfa1e5940af2d93dabd`
Cases: 100
Exact Codex/Gemini classifications: 47
Maintainer review queue: 53

Field differences:

- Eligibility: 7
- Script: 3
- Domain: 17
- Risk: 49

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

Neither advisory is auto-preferred. Codex must synthesize the differences before maintainer confirmation; no classification in this report has been written into the candidate pool.

## Review Queue

### 01. census-newsroom-zh-hans-v1/page-01-sentence-001

Changed: `risk`

Input:

```text
2020 年 12 月 7 日 — 美国人口普查局公布了发布质量信息的更新计划，以及普查的第一个结果，包括前所未有的数据质量指标。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 美國人口普查局新聞稿，正式書面語，句子結構完整。包含'质量'、'计划'、'结果'、'数据'等基本轉換詞彙。

Maintainer decision: `pending`

### 02. census-newsroom-zh-hans-v1/page-01-sentence-002

Changed: `risk`

Input:

```text
每十年，人口普查局都会对人口普查进行广泛评估，发布一组数据质量指标。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 美國人口普查局新聞稿，正式書面語，描述標準流程。測試'进行'、'广泛'、'发布'等詞的轉換。

Maintainer decision: `pending`

### 03. census-newsroom-zh-hans-v1/page-01-sentence-004

Changed: `eligible, domain, risk`

Input:

```text
与外部专家合作评估数据质量。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | medium | fragment |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 原頁條列片段缺少完整述語或主句，離開版面脈絡後不可獨立裁決。

Gemini reason: 美國人口普查局新聞稿，句子簡短完整。測試'与'、'专家'、'数据质量'。

Maintainer decision: `pending`

### 04. census-newsroom-zh-hans-v1/page-01-sentence-007

Changed: `risk`

Input:

```text
所有这些工作的目的都是为了支持对人口普查质量的评估 — 分析流程、仔细审核数据并将结果与其他人口总数做比较。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 美國人口普查局新聞稿，正式書面語，句子結構完整。測試'质量'、'审核'、'数据'等詞。

Maintainer decision: `pending`

### 05. census-newsroom-zh-hans-v1/page-01-sentence-008

Changed: `domain`

Input:

```text
人口普查局计划首次发布全国、州 (state)、哥伦比亚特区和波多黎各的数据质量指标，以及 2020 年人口普查的第一个结果 — 此数据用于美国众议院的国会席位分配。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整的官方人口普查文本；含法律、機關、地名、英文專名或識別字，需防止誤改專名與制度語意。

Gemini reason: 政府新聞稿，包含英文單字 state，必須保留不轉換。

Maintainer decision: `pending`

### 06. census-newsroom-zh-hans-v1/page-01-sentence-016

Changed: `domain, risk`

Input:

```text
有权访问内部人口普查局数据的专家将有特殊的宣誓状态，这意味着他们与人口普查局员工一样，有誓言和法律义务始终为个人身份信息保密。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整的官方人口普查文本；含法律、機關、地名、英文專名或識別字，需防止誤改專名與制度語意。

Gemini reason: 政府新聞稿，'访问' 在此數據情境下應為'存取'，考驗詞庫的精準度。

Maintainer decision: `pending`

### 07. census-newsroom-zh-hans-v1/page-01-sentence-022

Changed: `eligible, domain, risk`

Input:

```text
受访者对回答人口普查在隐私权和保密性方面的关注。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | medium | fragment |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 原頁條列片段缺少完整述語或主句，離開版面脈絡後不可獨立裁決。

Gemini reason: 政府新聞稿，標準書面語，測試'隐私权'、'关注'等詞。

Maintainer decision: `pending`

### 08. census-newsroom-zh-hans-v1/page-01-sentence-023

Changed: `eligible, domain, risk`

Input:

```text
与普查过后的问卷调查有关的双系统估算。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | medium | fragment |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 原頁條列片段缺少完整述語或主句，離開版面脈絡後不可獨立裁決。

Gemini reason: 政府新聞稿，'问卷调查'是核心術語，需要詞庫支援才能正確轉換為'問卷調查'。

Maintainer decision: `pending`

### 09. census-newsroom-zh-hans-v1/page-01-sentence-024

Changed: `eligible, domain, risk`

Input:

```text
不会说英语的人士和复杂住户居民，包括儿童。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | medium | fragment |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 原頁條列片段缺少完整述語或主句，離開版面脈絡後不可獨立裁決。

Gemini reason: 政府新聞稿，列舉人口群體，測試'复杂'等基本轉換。

Maintainer decision: `pending`

### 10. census-newsroom-zh-hans-v1/page-01-sentence-025

Changed: `eligible, domain, risk`

Input:

```text
整合合作关系和交流计划的各个方面。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | medium | fragment |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 原頁條列片段缺少完整述語或主句，離開版面脈絡後不可獨立裁決。

Gemini reason: 政府新聞稿，測試'关系'、'计划'等標準轉換。

Maintainer decision: `pending`

### 11. census-newsroom-zh-hans-v1/page-01-sentence-028

Changed: `risk`

Input:

```text
人口统计分析 — 2020 年 12 月 15 日，人口普查局将发布人口统计分析，它是一组在国家层面按年龄、性别、有限种族和西班牙后裔群组对美国人口的估算。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，包含日期和'人口统计'、'后裔'等術語，作為基準測試。

Maintainer decision: `pending`

### 12. census-newsroom-zh-hans-v1/page-01-sentence-031

Changed: `risk`

Input:

```text
此外，人口普查局还在计划生成几组实验性质的人口统计数据估算，按年龄、种族和西班牙后裔类别提供更多估算。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，測試'计划'、'数据'等標準轉換。

Maintainer decision: `pending`

### 13. census-newsroom-zh-hans-v1/page-01-sentence-036

Changed: `risk`

Input:

```text
人口普查局初步计划在 2021 年 11 月发布第一批结果，更多结果将在 2022 年 2 月发布。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，包含日期，測試'计划'、'发布'、'结果'等標準轉換。

Maintainer decision: `pending`

### 14. census-newsroom-zh-hans-v1/page-02-sentence-004

Changed: `domain, risk`

Input:

```text
人口普查统计数据用于确定每个州在美国众议院的席位数量，并告知立法区边界。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含法律、機關、地名、英文專名或識別字，需防止誤改專名與制度語意。

Gemini reason: 政府新聞稿，標準書面語，測試'统计数据'、'确定'、'众议院'、'边界'。

Maintainer decision: `pending`

### 15. census-newsroom-zh-hans-v1/page-02-sentence-012

Changed: `risk`

Input:

```text
为 4 月 1 日（人口普查日）您所居住的地址回答。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，祈使句，語氣直接，作為基本轉換測試。

Maintainer decision: `pending`

### 16. census-newsroom-zh-hans-v1/page-02-sentence-024

Changed: `domain, risk`

Input:

```text
请注意：根据联邦、州和地方卫生当局持续评估的指导方针，人口普查局决定暂停 2020 年人口普查的外勤操作，额外延迟两周至 2020 年 4 月 15 日。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整的官方人口普查文本；含法律、機關、地名、英文專名或識別字，需防止誤改專名與制度語意。

Gemini reason: 政府新聞稿，'外勤操作'對應台灣常用語'外勤作業'，需要詞庫支援。

Maintainer decision: `pending`

### 17. census-newsroom-zh-hans-v1/page-03-sentence-001

Changed: `risk`

Input:

```text
2020 年 6 月 23 日 – 目前 10 个住户中约有 4 个住户还没有回答 2020 年人口普查，美国人口普查局今天宣布已准备好进行多项后续活动，以确保统计人数的完整和准确。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，測試'后续活动'、'确保'、'准确'等基本轉換。

Maintainer decision: `pending`

### 18. census-newsroom-zh-hans-v1/page-03-sentence-004

Changed: `risk`

Input:

```text
人口普查电话中心的工作人员已从 4 月 22 日开始打电话。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，包含日期，作為基本轉換測試。

Maintainer decision: `pending`

### 19. census-newsroom-zh-hans-v1/page-03-sentence-005

Changed: `risk`

Input:

```text
如果住户不接电话，工作人员会留下语音留言，提供一个 12 位数字的 ID 作为参考号码。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，包含英文'ID'，必須保留不轉換。

Maintainer decision: `pending`

### 20. census-newsroom-zh-hans-v1/page-03-sentence-006

Changed: `risk`

Input:

```text
这项工作将一直持续到回答阶段末尾 10 月 31 日。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，包含日期，作為基本轉換測試。

Maintainer decision: `pending`

### 21. census-newsroom-zh-hans-v1/page-03-sentence-008

Changed: `risk`

Input:

```text
从 7 月中旬开始，来自 6 个地区人口普查办公室 (area census offices) (每个人口普查局地区一个)的人口普查员将开始访谈尚未回答 2020 年人口普查作出回应的住户。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，包含英文 'area census offices'，必須保留不轉換。

Maintainer decision: `pending`

### 22. census-newsroom-zh-hans-v1/page-03-sentence-011

Changed: `risk`

Input:

```text
除了作为软启动的一部分的地区人口普查办公室 (area census offices)，其余的地区人口普查办公室 (area census offices) 将在 8 月 11 日开始未回复随访，并于 10 月 31 日之前结束。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，包含重複的英文 'area census offices'，必須保留不轉換。

Maintainer decision: `pending`

### 23. census-newsroom-zh-hans-v1/page-03-sentence-021

Changed: `risk`

Input:

```text
在 4 月 1 日（人口普查日）居住在这个住户的人可能曾经也可能没有在那里居住过。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，標準書面語，作為基本轉換測試。

Maintainer decision: `pending`

### 24. census-newsroom-zh-hans-v1/page-03-sentence-022

Changed: `eligible, domain, risk`

Input:

```text
那些在 4 月 1 日到访谈时间之间搬出住户的人。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | medium | fragment |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 原頁條列片段缺少完整述語或主句，離開版面脈絡後不可獨立裁決。

Gemini reason: 政府新聞稿，標準書面語，作為基本轉換測試。

Maintainer decision: `pending`

### 25. census-newsroom-zh-hans-v1/page-03-sentence-024

Changed: `risk`

Input:

```text
根据人口普查局的户籍规定，访谈员还会收集有关备选地址的信息，以确定人口普查日居住的人。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，測試'户籍'、'备选'等詞的轉換。

Maintainer decision: `pending`

### 26. census-newsroom-zh-hans-v1/page-03-sentence-026

Changed: `risk`

Input:

```text
对于在未回复随访重新访谈和人口普查后问卷调查中被联系的住户，人口普查局敦促这些少数住户花几分钟时间与人口普查员交流，以确保 2020 年人口普查的质量。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，標準書面語，測試'敦促'、'确保'、'质量'。

Maintainer decision: `pending`

### 27. census-newsroom-zh-hans-v1/page-03-sentence-027

Changed: `risk`

Input:

```text
所有人口普查员都有正式的政府徽章 ID，上面有他们的姓名、照片、美国商业部水印和到期日期。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整的官方人口普查文本；主要檢查基礎字形轉換與保守保留。

Gemini reason: 政府新聞稿，包含英文'ID'，必須保留不轉換。

Maintainer decision: `pending`

### 28. census-newsroom-zh-hans-v1/page-03-sentence-028

Changed: `domain, risk`

Input:

```text
人口普查局所执行的所有操作都遵循两条重要原则： (1) 保护我们的员工和公众的健康，并 (2) 履行我们的宪法责任，按时将 2020 年人口普查人数统计提交至总统。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含法律、機關、地名、英文專名或識別字，需防止誤改專名與制度語意。

Gemini reason: 政府新聞稿，標準書面語，測試'履行'、'宪法'、'责任'。

Maintainer decision: `pending`

### 29. census-newsroom-zh-hans-v1/page-03-sentence-029

Changed: `domain`

Input:

```text
我们与国家、州(state) 和地方卫生部门密切合作，以确保将这些政府机构的指导方针纳入我们的操作。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整的官方人口普查文本；含法律、機關、地名、英文專名或識別字，需防止誤改專名與制度語意。

Gemini reason: 政府新聞稿，包含英文'state'，必須保留不轉換。

Maintainer decision: `pending`

### 30. census-newsroom-zh-hans-v1/page-04-sentence-003

Changed: `script, risk`

Input:

```text
“通过让住户选择用英语或其他 12 种语言通过在线或电话回答，我们为居民提供了他们被算上所需要的工具，并鼓励他们塑造自己的未来”人口普查局局长 Steven Dillingham 说道。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整的官方人口普查文本；含法律、機關、地名、英文專名或識別字，需防止誤改專名與制度語意。

Gemini reason: 政府新聞稿，包含引述，'在线'對應'線上'，需詞庫支援。

Maintainer decision: `pending`

### 31. census-newsroom-zh-hans-v1/page-04-sentence-006

Changed: `script, risk`

Input:

```text
根据美国社区问卷调查 (American Community Survey) 2013 年至 2017 年收集的数据，在人口普查区(约有 4000 户)，20% 或更多主要讲西班牙语的所有住户都将收到这些双语邀请。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整的官方人口普查文本；含法律、機關、地名、英文專名或識別字，需防止誤改專名與制度語意。

Gemini reason: 政府新聞稿，'问卷调查'和'数据'是核心術語，需要詞庫支援。

Maintainer decision: `pending`

### 32. census-newsroom-zh-hans-v1/page-04-sentence-009

Changed: `eligible, domain, risk`

Input:

```text
（收到双语邀请的住户将收到英语/西班牙语纸质问卷。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 輸入只有左括號且句子明顯截斷，不符合完整、可獨立裁決的來源品質門檻。

Gemini reason: 政府新聞稿，括號內的補充說明，'纸质问卷'對應'紙本問卷'。

Maintainer decision: `pending`

### 33. census-newsroom-zh-hans-v1/page-04-sentence-012

Changed: `risk`

Input:

```text
指南也提供盲文和大字号印刷体的英文版本。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整的官方人口普查文本；主要檢查基礎字形轉換與保守保留。

Gemini reason: 政府新聞稿，'大字号'對應'大字體'，需詞庫支援。

Maintainer decision: `pending`

### 34. census-newsroom-zh-hans-v1/page-04-sentence-014

Changed: `risk`

Input:

```text
人口普查局还宣传和编制了英语和 12 种其他语言的宣传资料，并提供 59 种非英语语言的词汇表，提供与人口普查有关的关键字的翻译，以帮助社区和 2020 年人口普查合作伙伴开展宣传活动。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，測試'宣传'、'词汇表'、'关键字'等基本轉換。

Maintainer decision: `pending`

### 35. census-newsroom-zh-hans-v1/page-05-sentence-003

Changed: `script, risk`

Input:

```text
人口普查局局长 Steven Dillingham 博士通过视频消息感谢已经答复的群众，使普查工作达到这一里程碑，并鼓励尚未回答的人们尽快回答人口普查，帮助塑造未来十年我们大家的未来。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整的官方人口普查文本；含法律、機關、地名、英文專名或識別字，需防止誤改專名與制度語意。

Gemini reason: 政府新聞稿，'视频消息'對應'影片訊息'，需詞庫支援。

Maintainer decision: `pending`

### 36. census-newsroom-zh-hans-v1/page-05-sentence-007

Changed: `risk`

Input:

```text
作为这一分阶段复工的一部分，在大多数住户住宅收不到邮件的区域，人口普查局恢复了将 2020 年人口普查邀请函邮包送达住户门口的工作。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，測試'邮件'、'恢复'、'邮包'等基本轉換。

Maintainer decision: `pending`

### 37. census-newsroom-zh-hans-v1/page-06-sentence-011

Changed: `domain`

Input:

```text
所有人口普查员都接受过社交疏离培训，并将获得个人防护装备(PPE)，遵循当地的使用指南准则。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整的官方人口普查文本；含法律、機關、地名、英文專名或識別字，需防止誤改專名與制度語意。

Gemini reason: 政府新聞稿，包含英文縮寫'PPE'，必須保留不轉換。

Maintainer decision: `pending`

### 38. census-newsroom-zh-hans-v1/page-06-sentence-039

Changed: `domain`

Input:

```text
上述操作的更新都纳入了最新的联邦、州 (state) 和地方关于个人防护设备 PPE 和法规的指导准则。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整的官方人口普查文本；含法律、機關、地名、英文專名或識別字，需防止誤改專名與制度語意。

Gemini reason: 政府新聞稿，包含英文'state'和'PPE'，必須保留不轉換。

Maintainer decision: `pending`

### 39. census-newsroom-zh-hans-v1/page-06-sentence-040

Changed: `domain, risk`

Input:

```text
为了我们的工作人员和公众的安全，人口普查局已下令为包括在外勤办公室工作的人员在内的所有外勤工作人员配备个人防护装备。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，測試'外勤'等基本轉換。

Maintainer decision: `pending`

### 40. census-newsroom-zh-hans-v1/page-06-sentence-042

Changed: `domain, risk`

Input:

```text
人口普查局工作人员佩带个人防护装备时将遵照地方卫生官员的指导准则。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，'佩带'在台灣常用'佩戴'，可作為基本轉換測試。

Maintainer decision: `pending`

### 41. census-newsroom-zh-hans-v1/page-07-sentence-006

Changed: `risk`

Input:

```text
人口普查局也宣布了向 130 万要求使用邮政邮箱才能接收信件的社区发送明信片的计划。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，測試'万'、'邮政邮箱'、'发送'、'计划'等基本轉換。

Maintainer decision: `pending`

### 42. census-newsroom-zh-hans-v1/page-07-sentence-008

Changed: `risk`

Input:

```text
人口普查局不会向邮政信箱发送人口普查邀请，因为每个人口普查答案必须与人们居住的实际位置相关联，而不是与他们收到邮件的位置相关联。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，測試'发送'、'相关联'、'邮件'等基本轉換。

Maintainer decision: `pending`

### 43. census-newsroom-zh-hans-v1/page-08-sentence-006

Changed: `risk`

Input:

```text
人口分析估计是使用出生与死亡记录、国际人口迁移数据和医疗记录创建的。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，測試'记录'、'数据'、'医疗'等基本轉換。

Maintainer decision: `pending`

### 44. census-newsroom-zh-hans-v1/page-08-sentence-008

Changed: `risk`

Input:

```text
例如，出生和死亡的估计被认为是相对准确的，因为估计值的生成基于非常准确和完整的美国重要的记录系统。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，測試'准确'、'记录系统'等基本轉換。

Maintainer decision: `pending`

### 45. census-newsroom-zh-hans-v1/page-08-sentence-017

Changed: `risk`

Input:

```text
这些估计值纳入了当前出生记录，当地的管辖区域目前还没有这些记录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，測試'记录'、'管辖区域'等基本轉換。

Maintainer decision: `pending`

### 46. census-newsroom-zh-hans-v1/page-08-sentence-018

Changed: `risk`

Input:

```text
2022 年将发布年龄为 0 到 17 岁白人、黑人或非洲裔美国人、美洲印第安人或阿拉斯加原住民、亚裔、夏威夷原住民或其他太平洋岛民以及两个或更多种族及西班牙后裔的估计。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，列舉多個種族分類，測試'亚裔'、'后裔'等基本轉換。

Maintainer decision: `pending`

### 47. census-newsroom-zh-hans-v1/page-08-sentence-019

Changed: `risk`

Input:

```text
这些估计纳入了自 2003 年以来出生和死亡记录中的详细种族信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，測試'记录'等基本轉換。

Maintainer decision: `pending`

### 48. census-newsroom-zh-hans-v1/page-08-sentence-020

Changed: `risk`

Input:

```text
人口分析估计是测量人口普查覆盖率的两种方法之一，它可以帮助我们了解哪些人口群体可能被低估或被高估。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，測試'低估'、'高估'等基本轉換。

Maintainer decision: `pending`

### 49. census-newsroom-zh-hans-v1/page-08-sentence-029

Changed: `risk`

Input:

```text
美国人口年龄估计的中值分别为 38.4、38.5 和 38.7 岁。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，報告統計數據，作為基本轉換測試。

Maintainer decision: `pending`

### 50. census-newsroom-zh-hans-v1/page-08-sentence-030

Changed: `risk`

Input:

```text
仅黑人的美国人口百分比估计分别为 13.4、13.7 和 13.9。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，報告統計數據，作為基本轉換測試。

Maintainer decision: `pending`

### 51. census-newsroom-zh-hans-v1/page-08-sentence-031

Changed: `risk`

Input:

```text
仅黑人或与其他种族组合的人口百分比估计分别为 14.9、15.1 和 15.4。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，報告統計數據，作為基本轉換測試。

Maintainer decision: `pending`

### 52. census-newsroom-zh-hans-v1/page-08-sentence-034

Changed: `risk`

Input:

```text
年龄在 30 岁以下人口中，西班牙裔的百分比估计值分别为 23.0、24.6 和 26.0。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，報告統計數據，作為基本轉換測試。

Maintainer decision: `pending`

### 53. census-newsroom-zh-hans-v1/page-09-sentence-001

Changed: `risk`

Input:

```text
2020 年 6 月 24日 — 美国人口普查局本周向邮政信箱是唯一可用邮寄地址社区发送估计 130 万份明信片。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的官方人口普查文本；含中國與臺灣正式用語差異，適合檢查候選詞缺口。

Gemini reason: 政府新聞稿，測試'万'、'发送'等基本轉換。

Maintainer decision: `pending`
