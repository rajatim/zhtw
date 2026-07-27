<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 035 (2026-07-27)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `bca4a8b496dbdd270e5e42b45f39ff3d9dc98250d068d26e636ee26680c519b5`
Cases: 96
Exact Codex/Gemini classifications: 61
Maintainer review queue: 35

Field differences:

- Eligibility: 6
- Script: 1
- Domain: 15
- Risk: 29

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

The maintainer resolved all 35 advisory disagreements and batch-confirmed the 61 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. census-newsroom-zh-hans-v1/page-02-sentence-002

Changed: `risk`

Input:

```text
美国宪法强制规定每十年开展一次人口普查。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；用於檢驗正式用語、統計術語及受保護英文名稱。

Gemini reason: 動詞「开展」可能需要轉換為台灣慣用詞「進行」或「舉辦」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 02. census-newsroom-zh-hans-v1/page-02-sentence-021

Changed: `eligible, domain, risk`

Input:

```text
现在就回答，最大限度地减少人口普查员在今年晚些时候拜访您的住宅对您跟进访谈。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 來源句含句法重複、錯置、未閉合引文或缺少受詞，無法作為可靠且可獨立裁決的 benchmark 輸入。

Gemini reason: 語句結構與用詞（如「跟进访谈」）需大幅在地化。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 03. census-newsroom-zh-hans-v1/page-02-sentence-023

Changed: `risk`

Input:

```text
所有尚未在线回答的住户都将在 4 月 8 日到 16 日之间收到一份纸质问卷。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；用於檢驗正式用語、統計術語及受保護英文名稱。

Gemini reason: 標準體例，基準轉換即可。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 04. census-newsroom-zh-hans-v1/page-03-sentence-009

Changed: `eligible, domain, risk`

Input:

```text
将于 6 月底将宣布这 6 个地区人口普查办公室 (area census offices)。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 來源句含句法重複、錯置、未閉合引文或缺少受詞，無法作為可靠且可獨立裁決的 benchmark 輸入。

Gemini reason: 含英文術語 (area census offices)，需保護。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 05. census-newsroom-zh-hans-v1/page-04-sentence-007

Changed: `risk`

Input:

```text
不太可能在线回答的住户也将在首次邀请中收到纸质问卷。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；用於檢驗正式用語、統計術語及受保護英文名稱。

Gemini reason: 標準體例，基準轉換即可。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 06. census-newsroom-zh-hans-v1/page-04-sentence-010

Changed: `risk`

Input:

```text
从 5 月中旬开始，全国各地的人口普查员将走访那些没有回答的住户，亲自收集答案。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；用於檢驗正式用語、統計術語及受保護英文名稱。

Gemini reason: 動詞「走访」可能需轉換為台灣慣用詞「訪視」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 07. census-newsroom-zh-hans-v1/page-05-sentence-010

Changed: `risk`

Input:

```text
所有复工的工作人员都将得到关于社交疏离规则的安全培训，并在重新开始工作前收到个人防护装备。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；用於檢驗正式用語、統計術語及受保護英文名稱。

Gemini reason: 「社交疏离」需轉換為台灣慣用詞「社交距離」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 08. census-newsroom-zh-hans-v1/page-06-sentence-006

Changed: `eligible, domain, risk`

Input:

```text
人口普查局将在 6 月 14 日继续更新/普查操作。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 來源句含句法重複、錯置、未閉合引文或缺少受詞，無法作為可靠且可獨立裁決的 benchmark 輸入。

Gemini reason: 「操作」需轉換為「作業」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 09. census-newsroom-zh-hans-v1/page-08-sentence-001

Changed: `risk`

Input:

```text
2020 年 12 月 15 日 — 美国人口普查局今天发布了 2020 年人口分析报告，该报告提供了截至 2020 年 4 月 1 日国家人口的一系列的低、中和高估计值。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；用於檢驗正式用語、統計術語及受保護英文名稱。

Gemini reason: 「估值」應為「估計值」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 10. census-newsroom-zh-hans-v1/page-08-sentence-005

Changed: `eligible, domain, risk`

Input:

```text
“人口分析是一个有价值的资源，可以帮助我们分析 2020 年人口普查人口人数的完整性。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | unmatched_quote |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 來源句含句法重複、錯置、未閉合引文或缺少受詞，無法作為可靠且可獨立裁決的 benchmark 輸入。

Gemini reason: 用詞需微調以符合台灣語氣，如「有价值的资源」可為「寶貴的資源」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 11. census-newsroom-zh-hans-v1/page-08-sentence-037

Changed: `script, risk`

Input:

```text
2020 年人口分析主页(仅英语) 有完整的表格。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | medium | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的人口普查新聞敘述；用於檢驗正式用語、統計術語及受保護英文名稱。

Gemini reason: 含需保護的標記「(仅英语)」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 12. massive-1-0-zh-cn-v1/11552

Changed: `eligible, domain, risk`

Input:

```text
更多更清晰和以主题为导向
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | social_daily | candidate_gap | medium | - |

Codex reason: 來源句含句法重複、錯置、未閉合引文或缺少受詞，無法作為可靠且可獨立裁決的 benchmark 輸入。

Gemini reason: 「以主题为导向」的說法較書面語，台灣口語可能用「主題導向的」或「更聚焦主題」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 13. massive-1-0-zh-cn-v1/12027

Changed: `domain, risk`

Input:

```text
在西部地区举行的巡回竞赛
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 可獨立判讀的語音助理請求；用於檢驗日常用語、產品實體與區域詞差異。

Gemini reason: 「巡回竞赛」在台灣通常稱為「巡迴賽」，存在詞彙差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 14. massive-1-0-zh-cn-v1/12312

Changed: `eligible, domain, risk`

Input:

```text
考虑到公园大道
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 來源句含句法重複、錯置、未閉合引文或缺少受詞，無法作為可靠且可獨立裁決的 benchmark 輸入。

Gemini reason: 「公园大道」可能為街道專有名詞（如 Park Avenue），應視為專有名詞處理。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 15. massive-1-0-zh-cn-v1/12867

Changed: `risk`

Input:

```text
请用优步
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的語音助理請求；用於檢驗日常用語、產品實體與區域詞差異。

Gemini reason: 「优步」是品牌名稱 Uber 的中文譯名，為專有名詞，不可轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 16. massive-1-0-zh-cn-v1/13281

Changed: `domain`

Input:

```text
我想给我的妻子写一些原创的浪漫的短信
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 可獨立判讀的語音助理請求；用於檢驗日常用語、產品實體與區域詞差異。

Gemini reason: 「短信」是中國大陸用語，台灣稱「簡訊」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 17. massive-1-0-zh-cn-v1/13642

Changed: `risk`

Input:

```text
请定义纹理
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 可獨立判讀的語音助理請求；用於檢驗日常用語、產品實體與區域詞差異。

Gemini reason: 「纹理」在台灣也用，但在電腦圖學等領域常稱「材質」，存在領域詞彙差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 18. massive-1-0-zh-cn-v1/13721

Changed: `risk`

Input:

```text
加币兑美元的汇率
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 可獨立判讀的語音助理請求；用於檢驗日常用語、產品實體與區域詞差異。

Gemini reason: 「加币」是加拿大元的簡稱，台灣多稱「加幣」，但用語習慣上可能有些微差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 19. massive-1-0-zh-cn-v1/156

Changed: `domain`

Input:

```text
调低亮度
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | medium | - |

Codex reason: 可獨立判讀的語音助理請求；用於檢驗日常用語、產品實體與區域詞差異。

Gemini reason: 「调低」在台灣可能也會用，但「降低」可能更常用於此情境。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 20. massive-1-0-zh-cn-v1/2282

Changed: `domain, risk`

Input:

```text
把我房子里所有的灯都设置成蓝色
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 可獨立判讀的語音助理請求；用於檢驗日常用語、產品實體與區域詞差異。

Gemini reason: 智慧家庭指令，基本字元轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 21. massive-1-0-zh-cn-v1/3363

Changed: `domain`

Input:

```text
一位神父走进一间酒吧
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 可獨立判讀的語音助理請求；用於檢驗日常用語、產品實體與區域詞差異。

Gemini reason: 笑話開頭，基本字元轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 22. massive-1-0-zh-cn-v1/6890

Changed: `risk`

Input:

```text
告诉我演出时间是什么时候
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 可獨立判讀的語音助理請求；用於檢驗日常用語、產品實體與區域詞差異。

Gemini reason: 「演出时间」在台灣多用「表演時間」或「上映時間」，存在詞彙差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 23. zhtw-project-llm-social-baseline-v1/llm-003

Changed: `risk`

Input:

```text
系统会保存最近十轮对话，超过范围的消息不会传给模型。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的 LLM 實務敘述；用於檢驗模型產品語彙、技術 token 與過度轉換防禦。

Gemini reason: IT/LLM 領域用語，'消息' 在台灣慣用'訊息'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 24. zhtw-project-llm-social-baseline-v1/llm-004

Changed: `risk`

Input:

```text
评估报告分别列出准确率、召回率和无法作答的比例。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的 LLM 實務敘述；用於檢驗模型產品語彙、技術 token 與過度轉換防禦。

Gemini reason: 機器學習評估指標術語，'准确率'、'召回率' 在台灣有特定對應詞 '準確率'、'召回率'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 25. zhtw-project-llm-social-baseline-v1/llm-009

Changed: `risk`

Input:

```text
这个工作流会先调用搜索工具，再根据来源生成带引用的回答。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的 LLM 實務敘述；用於檢驗模型產品語彙、技術 token 與過度轉換防禦。

Gemini reason: 涉及 IT 術語的地區用詞差異，例如'调用' (呼叫)、'工作流' (工作流程)。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 26. zhtw-project-llm-social-baseline-v1/llm-010

Changed: `domain`

Input:

```text
管理员可以查看令牌用量，但看不到对话中的敏感字段。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的 LLM 實務敘述；用於檢驗模型產品語彙、技術 token 與過度轉換防禦。

Gemini reason: IT 用語差異：'令牌' (權杖)、'字段' (欄位)。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 27. zhtw-project-llm-social-baseline-v1/llm-013

Changed: `domain, risk`

Input:

```text
批量任务完成后，页面会显示成功、失败和跳过的记录数。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的 LLM 實務敘述；用於檢驗模型產品語彙、技術 token 與過度轉換防禦。

Gemini reason: UI/IT 用語差異：'批量' (批次)、'记录' (紀錄)。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 28. zhtw-project-llm-social-baseline-v1/llm-024

Changed: `risk`

Input:

```text
训练资料包含重复样本时，验证分数可能被高估。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | medium | - |

Codex reason: 完整且可獨立判讀的 LLM 實務敘述；用於檢驗模型產品語彙、技術 token 與過度轉換防禦。

Gemini reason: ML 術語，'训练资料'、'验证分数' 用詞可更精確（如：訓練資料集、驗證集分數），但目前表述也可理解。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 29. zhtw-project-llm-social-baseline-v1/llm-038

Changed: `domain`

Input:

```text
请维持 SQL 查询原样，只解释各个条件的用途。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的 LLM 實務敘述；用於檢驗模型產品語彙、技術 token 與過度轉換防禦。

Gemini reason: 包含應受保護的英文縮寫 'SQL'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 30. zhtw-project-llm-social-baseline-v1/llm-039

Changed: `domain`

Input:

```text
模型建议的补丁尚未执行，必须先通过测试和代码审查。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的 LLM 實務敘述；用於檢驗模型產品語彙、技術 token 與過度轉換防禦。

Gemini reason: 軟體開發用語，'补丁' (修補程式)、'代码审查' (程式碼審查) 是地區用詞差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 31. zhtw-project-llm-social-baseline-v1/llm-040

Changed: `risk`

Input:

```text
分段策略改变后，检索到的上下文顺序也发生了变化。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的 LLM 實務敘述；用於檢驗模型產品語彙、技術 token 與過度轉換防禦。

Gemini reason: 標準技術用語('检索' -> '檢索')，簡繁轉換即可。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 32. zhtw-project-llm-social-baseline-v1/llm-041

Changed: `risk`

Input:

```text
请识别客服对话中的主要诉求，不要推测用户的身份。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | baseline_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的 LLM 實務敘述；用於檢驗模型產品語彙、技術 token 與過度轉換防禦。

Gemini reason: 用語差異：'用户' (使用者)。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 33. zhtw-project-llm-social-baseline-v1/social-031

Changed: `risk`

Input:

```text
这个杯子的盖子不太紧，放进包里容易漏水。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整且自然的日常社群敘述；用於檢驗臺灣生活用語與區域詞差異。

Gemini reason: 口語用詞差異：'盖子' (蓋子/杯蓋)，'盖子' 較偏向中國北方用語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 34. zhtw-project-llm-social-baseline-v1/social-033

Changed: `risk`

Input:

```text
周末想去剪头发，但熟悉的设计师刚好休假。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整且自然的日常社群敘述；用於檢驗臺灣生活用語與區域詞差異。

Gemini reason: 用語差異：剪髮的 '设计师' 在台灣通常稱為 '髮型師'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 35. zhtw-project-llm-social-baseline-v1/social-044

Changed: `risk`

Input:

```text
我把旧书整理成三箱，准备周末拿去捐赠。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整且自然的日常社群敘述；用於檢驗臺灣生活用語與區域詞差異。

Gemini reason: 口語用詞差異：量詞 '三箱' 在台灣更常說 '三箱的書' 或直接說 '三大箱書'。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`
