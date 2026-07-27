<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 024 (2026-07-27)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `a9b76a63b5d9150d75b02ac287fe24c75e2a88044d69d6558ce87d572aab585b`
Cases: 100
Exact Codex/Gemini classifications: 59
Maintainer review queue: 41

Field differences:

- Eligibility: 0
- Script: 0
- Domain: 15
- Risk: 40

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

The maintainer resolved all 41 advisory disagreements and batch-confirmed the 59 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. zhtw-project-formal-llm-balance-v1/formal-001

Changed: `domain, risk`

Input:

```text
审计委员会要求各部门补交原始凭证，并说明支出用途。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 金融審計相關的正式文本，屬高風險領域。保留「原始憑證」等專有名詞至關重要，具過度轉換風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 02. zhtw-project-formal-llm-balance-v1/formal-002

Changed: `domain, risk`

Input:

```text
主管机关核准申请后，业者仍须完成消防安全检查。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 涉及政府法規與消防安全，屬高風險領域。專有名詞「主管機關」、「消防安全檢查」需準確轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 03. zhtw-project-formal-llm-balance-v1/formal-003

Changed: `domain, risk`

Input:

```text
地方议会将在下次会议审查追加预算与执行进度。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 涉及政府預算審查，屬財經、法律相關的高風險領域。保留「追加預算」等術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 04. zhtw-project-formal-llm-balance-v1/formal-004

Changed: `risk`

Input:

```text
法院认定契约条款显失公平，因此判决该条款无效。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 法律判決文本，屬高風險領域。法律術語如「顯失公平」、「條款無效」需精確對應。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 05. zhtw-project-formal-llm-balance-v1/formal-005

Changed: `risk`

Input:

```text
消费者申请解除契约时，应保存订单与付款记录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；含臺灣術語正規化候選。

Gemini reason: 消費者合約相關，涉及法律與金融，屬高風險領域。保留「解除契約」等法律用語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 06. zhtw-project-formal-llm-balance-v1/formal-006

Changed: `risk`

Input:

```text
研究机构公布调查结果前，先完成样本资料检核。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 研究調查相關的正式寫作，術語「樣本資料檢核」需準確轉換，具過度轉換風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 07. zhtw-project-formal-llm-balance-v1/formal-007

Changed: `domain, risk`

Input:

```text
公报列出的核定名称必须与登记资料完全一致。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 政府公報與登記資料，屬法律性質的高風險領域。要求完全一致，避免過度轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 08. zhtw-project-formal-llm-balance-v1/formal-009

Changed: `domain`

Input:

```text
承办人员应在期限内回复申请人，不得无故延误。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 行政程序規定，屬高風險領域，但句子本身用語通用，可視為基準案例。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 09. zhtw-project-formal-llm-balance-v1/formal-010

Changed: `risk`

Input:

```text
银行完成客户身份查核后，才会启用跨境汇款功能。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 銀行金融業務，屬高風險領域。術語如「客戶身份查核」、「跨境匯款」需準確保留。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 10. zhtw-project-formal-llm-balance-v1/formal-011

Changed: `risk`

Input:

```text
保险公司不得以定型化契约条款排除法定责任。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 保險合約的法律規定，屬高風險領域。法律術語「定型化契約條款」、「法定責任」需保留。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 11. zhtw-project-formal-llm-balance-v1/formal-012

Changed: `domain, risk`

Input:

```text
董事会决议出售闲置资产，并委托独立机构估价。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 公司治理與資產處分，屬財經性質的高風險領域。術語「閒置資產」、「獨立機構估價」需準確。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 12. zhtw-project-formal-llm-balance-v1/formal-013

Changed: `risk`

Input:

```text
会计师查核财务报告时，发现收入认列期间有误。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 會計查核，屬財經高風險領域。「財務報告」、「收入認列」為專業術語，需避免過度轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 13. zhtw-project-formal-llm-balance-v1/formal-014

Changed: `domain, risk`

Input:

```text
主管机关将抽查商品标示，并要求限期改善缺失。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 政府監管行為，屬高風險領域。「主管機關」等詞在兩岸語境可能不同，有潛在的在地化差異風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 14. zhtw-project-formal-llm-balance-v1/formal-015

Changed: `risk`

Input:

```text
市府规划新增转运站，以改善偏远地区交通。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 都市規劃，屬正式新聞。詞彙「轉運站」在台灣有特定用法，可能與中國大陸用法不同。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 15. zhtw-project-formal-llm-balance-v1/formal-017

Changed: `risk`

Input:

```text
气象报告指出锋面接近，山区可能出现短时强降雨。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 氣象報告，屬正式新聞。用詞「鋒面」在兩岸通用，但「短時強降雨」在台灣可能更常用「短延時強降雨」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 16. zhtw-project-formal-llm-balance-v1/formal-019

Changed: `risk`

Input:

```text
医院启动大量伤患应变机制，优先调度急诊人力。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 醫療應變，屬高風險領域。「大量傷患」、「急診」等術語在台灣有特定用法，需考慮在地化差異。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 17. zhtw-project-formal-llm-balance-v1/formal-020

Changed: `risk`

Input:

```text
药品说明书应清楚标示剂量、禁忌与不良反应。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；含臺灣術語正規化候選。

Gemini reason: 藥品說明書，屬醫療高風險領域。術語「禁忌」、「不良反應」必須精確保留。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 18. zhtw-project-formal-llm-balance-v1/formal-021

Changed: `risk`

Input:

```text
实验室重新校准仪器，以排除系统性测量误差。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 科學實驗流程，屬正式寫作。術語「校准」、「系统性测量误差」需精確轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 19. zhtw-project-formal-llm-balance-v1/formal-022

Changed: `risk`

Input:

```text
研究团队依照预注册方案分析数据，没有更改主要指标。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 學術研究方法，屬正式寫作。「预注册方案」、「主要指标」為專業術語，需保留。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 20. zhtw-project-formal-llm-balance-v1/formal-024

Changed: `risk`

Input:

```text
记者取得双方回应，并在报道中说明尚待查证的部分。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；含臺灣術語正規化候選。

Gemini reason: 新聞報導原則，屬正式新聞，用語通用，為基準案例。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 21. zhtw-project-formal-llm-balance-v1/formal-026

Changed: `risk`

Input:

```text
学校审核课程计划后，要求补充学习成果评量方式。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 教育行政，屬正式寫作。「学习成果评量」在台灣有特定術語，如「學習成果評量」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 22. zhtw-project-formal-llm-balance-v1/formal-027

Changed: `domain, risk`

Input:

```text
评审委员应揭露利益冲突，并回避相关案件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 法律及倫理規定，屬高風險領域。術語「利益衝突」、「迴避」需精確保留。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 23. zhtw-project-formal-llm-balance-v1/formal-028

Changed: `risk`

Input:

```text
劳资双方同意延长协商，并维持现有劳动条件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 勞資關係，屬高風險領域。「劳动条件」在台灣通常稱為「勞動條件」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 24. zhtw-project-formal-llm-balance-v1/formal-029

Changed: `risk`

Input:

```text
工会代表要求雇主提供完整的工时与薪资明细。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 勞資關係，屬高風險領域。「工会」在台灣稱為「工會」，「薪资」為「薪資」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 25. zhtw-project-formal-llm-balance-v1/formal-030

Changed: `domain, risk`

Input:

```text
厂商交付设备前，必须完成压力测试与安全认证。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 合約交付標準，涉及安全，屬高風險領域。「压力测试」、「安全认证」為技術術語，需準確轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 26. zhtw-project-formal-llm-balance-v1/formal-031

Changed: `domain, risk`

Input:

```text
采购文件载明验收标准，但未限制特定品牌投标。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 政府採購文件，屬法律高風險領域。「验收标准」、「投标」為專業術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 27. zhtw-project-formal-llm-balance-v1/formal-032

Changed: `risk`

Input:

```text
港务单位检查货柜封条后，才准许车辆离开管制区。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 港口管理，屬正式寫作。「货柜」在台灣稱為「貨櫃」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 28. zhtw-project-formal-llm-balance-v1/formal-034

Changed: `domain, risk`

Input:

```text
铁路号志异常期间，列车将减速通过施工区段。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 鐵路安全，屬高風險領域。「号志」在台灣稱為「號誌」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 29. zhtw-project-formal-llm-balance-v1/formal-036

Changed: `risk`

Input:

```text
水库管理单位评估蓄水量，并调整农业供水计划。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 水資源管理，屬正式新聞。「水库」在台灣稱為「水庫」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 30. zhtw-project-formal-llm-balance-v1/formal-037

Changed: `risk`

Input:

```text
环保人员采集河川水样，检验重金属与悬浮固体。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 環境監測，屬正式新聞。「重金属」、「悬浮固体」在台灣分別為「重金屬」、「懸浮固體」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 31. zhtw-project-formal-llm-balance-v1/formal-038

Changed: `risk`

Input:

```text
调查报告分别列出事实认定、争点与改进建议。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 報告結構說明，屬正式寫作。術語「事实认定」、「争点」需準確。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 32. zhtw-project-formal-llm-balance-v1/formal-039

Changed: `domain, risk`

Input:

```text
法院公告记载案号与开庭日期，不公开当事人住址。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 法律公告，屬高風險領域。保護個資與法律用詞「案号」的準確性很重要。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 33. zhtw-project-formal-llm-balance-v1/formal-040

Changed: `risk`

Input:

```text
机关保存电子公文时，应同时记录版本与签核流程。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 檔案管理規定，屬正式寫作。「电子公文」、「签核」為專業術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 34. zhtw-project-formal-llm-balance-v1/formal-041

Changed: `risk`

Input:

```text
档案目录采用统一分类号，方便跨部门查询。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 檔案管理，屬正式寫作。「分类号」為專業術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 35. zhtw-project-formal-llm-balance-v1/formal-042

Changed: `risk`

Input:

```text
统计公报以中位数呈现所得分布，避免平均值受到极端值影响。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 統計學報告，屬正式寫作。術語「中位数」、「平均值」、「极端值」需精確。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 36. zhtw-project-formal-llm-balance-v1/formal-043

Changed: `risk`

Input:

```text
论文附录公开分析代码，但未包含可识别个人的数据。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 學術倫理與個資保護，屬正式寫作，要求高度準確性。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 37. zhtw-project-formal-llm-balance-v1/formal-044

Changed: `domain, risk`

Input:

```text
专利说明书区分实施例与权利要求，不得混用编号。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 專利文件撰寫規則，屬法律高風險領域。「实施例」、「权利要求」為法律專業術語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 38. zhtw-project-formal-llm-balance-v1/formal-046

Changed: `domain, risk`

Input:

```text
选务机关封存选票后，由监察人员共同签名确认。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 選舉程序，屬法律高風險領域。「选务机关」、「监察人员」需準確。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 39. zhtw-project-formal-llm-balance-v1/formal-047

Changed: `risk`

Input:

```text
比赛裁判查阅录像后，维持原判并说明理由。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 體育賽事，屬正式新聞。「录像」在台灣多稱為「錄影」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 40. zhtw-project-formal-llm-balance-v1/formal-048

Changed: `risk`

Input:

```text
出版商取得授权后，发行该作品的有声版本。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 出版業，屬正式寫作。「有声版本」需準確轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 41. zhtw-project-formal-llm-balance-v1/formal-049

Changed: `domain, risk`

Input:

```text
基金会公布捐款流向，并委托第三方查核年度账目。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整且可獨立判讀的正式文本；適合作為保守字形與既有臺灣用語基準。

Gemini reason: 非營利組織財報，屬財經高風險領域。「捐款流向」、「第三方查核」需準確。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`
