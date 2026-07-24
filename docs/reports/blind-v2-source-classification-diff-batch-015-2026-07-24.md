<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 015 (2026-07-24)

Status: advisory only; maintainer decisions pending

Packet SHA-256: `e7370151640f2ec4e65b3f43a465d834f808f988c901807b1b8b178a5bc2969e`
Cases: 100
Exact Codex/Gemini classifications: 73
Maintainer review queue: 27

Field differences:

- Eligibility: 0
- Script: 0
- Domain: 24
- Risk: 3

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

Neither advisory is auto-preferred. Codex must synthesize the differences before maintainer confirmation; no classification in this report has been written into the candidate pool.

## Review Queue

### 01. zhtw-project-formal-entity-guard-v1/baseline-001

Changed: `risk`

Input:

```text
委员会完成调查后公布报告，并说明资料搜集方法。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整正式文本；含臺灣正式用語需要的詞彙正規化。

Gemini reason: 公文/報告基準例句，測試基本字形轉換。

Maintainer decision: `pending`

### 02. zhtw-project-formal-entity-guard-v1/baseline-002

Changed: `domain`

Input:

```text
地方政府将在月底前提出预算执行情况说明。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整正式文本；主要需要一般字形轉換，無額外地域改寫。

Gemini reason: 地方政府預算執行公文，基準轉換測試。

Maintainer decision: `pending`

### 03. zhtw-project-formal-entity-guard-v1/baseline-007

Changed: `domain`

Input:

```text
审计人员核对支出凭证与付款日期。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整正式文本；主要需要一般字形轉換，無額外地域改寫。

Gemini reason: 審計人員核對支出憑證，財務基準句。

Maintainer decision: `pending`

### 04. zhtw-project-formal-entity-guard-v1/baseline-008

Changed: `risk`

Input:

```text
出版社发布修订版前再次确认引用来源。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整正式文本；含臺灣正式用語需要的詞彙正規化。

Gemini reason: 出版社修訂版引用來源確認，基準轉換測試。

Maintainer decision: `pending`

### 05. zhtw-project-formal-entity-guard-v1/baseline-012

Changed: `risk`

Input:

```text
主管机关要求业者改善标示内容。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整正式文本；專名、引文、標題、型號、代碼或符號必須保留。

Gemini reason: 主管機關要求改善標示，行政公文基準句。

Maintainer decision: `pending`

### 06. zhtw-project-formal-entity-guard-v1/baseline-019

Changed: `domain`

Input:

```text
公司董事会通过年度财务报告。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | baseline_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整正式文本；主要需要一般字形轉換，無額外地域改寫。

Gemini reason: 公司董事會財務報告，金融/商業基準句。

Maintainer decision: `pending`

### 07. zhtw-project-formal-entity-guard-v1/code-001

Changed: `domain`

Input:

```text
统计报告将变量 β₁ 与 β₂ 分别列在模型公式中。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整正式文本；專名、引文、標題、型號、代碼或符號必須保留。

Gemini reason: 統計模型希臘字母與下標符號（β₁、β₂），需防過度轉換。

Maintainer decision: `pending`

### 08. zhtw-project-formal-entity-guard-v1/code-012

Changed: `domain`

Input:

```text
金融公报以 ISIN US0378331005 标识证券。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整正式文本；專名、引文、標題、型號、代碼或符號必須保留。

Gemini reason: 國際證券識別碼 ISIN，金融代碼不可改寫。

Maintainer decision: `pending`

### 09. zhtw-project-formal-entity-guard-v1/code-015

Changed: `domain`

Input:

```text
货运文件中的 UN 3480 是危险品运输编号。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整正式文本；專名、引文、標題、型號、代碼或符號必須保留。

Gemini reason: 聯合國危險品編號 UN 3480，防法規運輸代碼改壞。

Maintainer decision: `pending`

### 10. zhtw-project-formal-entity-guard-v1/code-016

Changed: `domain`

Input:

```text
专利公报以 WO 2026/012345 标识国际申请。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整正式文本；專名、引文、標題、型號、代碼或符號必須保留。

Gemini reason: 國際專利申請號 WO 2026/012345，法律專利代碼保護。

Maintainer decision: `pending`

### 11. zhtw-project-formal-entity-guard-v1/code-018

Changed: `domain`

Input:

```text
财政表格保留科目代码 4010-A。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整正式文本；專名、引文、標題、型號、代碼或符號必須保留。

Gemini reason: 會計科目代碼 4010-A，防財政表格編碼變更。

Maintainer decision: `pending`

### 12. zhtw-project-formal-entity-guard-v1/entity-002

Changed: `domain`

Input:

```text
世界卫生组织引用 WHO 编号时，不应改写编号格式。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整正式文本；專名、引文、標題、型號、代碼或符號必須保留。

Gemini reason: 世衛組織縮寫 WHO 及編號格式保護。

Maintainer decision: `pending`

### 13. zhtw-project-formal-entity-guard-v1/entity-003

Changed: `domain`

Input:

```text
国际货币基金组织将 IMF 写在报告标题之后。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整正式文本；專名、引文、標題、型號、代碼或符號必須保留。

Gemini reason: 國際貨幣基金組織 IMF 縮寫保護。

Maintainer decision: `pending`

### 14. zhtw-project-formal-entity-guard-v1/entity-015

Changed: `domain`

Input:

```text
法院文件以当事人登记的 Chen Wei-Lun 为准。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整正式文本；專名、引文、標題、型號、代碼或符號必須保留。

Gemini reason: 法院登記拼音姓名 Chen Wei-Lun，法律文件人名保護。

Maintainer decision: `pending`

### 15. zhtw-project-formal-entity-guard-v1/entity-020

Changed: `domain`

Input:

```text
外交公报中的 Côte d’Ivoire 应维持官方拼写。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整正式文本；專名、引文、標題、型號、代碼或符號必須保留。

Gemini reason: 國名官方法文拼寫 Côte d’Ivoire 保護。

Maintainer decision: `pending`

### 16. zhtw-project-formal-entity-guard-v1/quote-001

Changed: `domain`

Input:

```text
发言人强调原文使用的是“due process”，引文不得意译。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整正式文本；專名、引文、標題、型號、代碼或符號必須保留。

Gemini reason: 法律引語 “due process”，原文不可意譯或改寫。

Maintainer decision: `pending`

### 17. zhtw-project-formal-entity-guard-v1/quote-003

Changed: `domain`

Input:

```text
学者引用“habeas corpus”时维持拉丁文拼写。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整正式文本；專名、引文、標題、型號、代碼或符號必須保留。

Gemini reason: 拉丁文法律專有名詞 “habeas corpus” 原文保護。

Maintainer decision: `pending`

### 18. zhtw-project-formal-entity-guard-v1/quote-004

Changed: `domain`

Input:

```text
声明中的“status quo ante”属于原文引语。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整正式文本；專名、引文、標題、型號、代碼或符號必須保留。

Gemini reason: 拉丁文引語 “status quo ante”，原文引述保護。

Maintainer decision: `pending`

### 19. zhtw-project-formal-entity-guard-v1/quote-005

Changed: `domain`

Input:

```text
判决理由引用“amicus curiae”，不得改成机构名称。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整正式文本；專名、引文、標題、型號、代碼或符號必須保留。

Gemini reason: 法律術語 “amicus curiae”，判決理由原文保護。

Maintainer decision: `pending`

### 20. zhtw-project-formal-entity-guard-v1/quote-007

Changed: `domain`

Input:

```text
测试报告中的 ThinkPad X1 Carbon 不应拆分翻译。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整正式文本；專名、引文、標題、型號、代碼或符號必須保留。

Gemini reason: 電腦產品型號 ThinkPad X1 Carbon，防型號拆分誤譯。

Maintainer decision: `pending`

### 21. zhtw-project-formal-entity-guard-v1/quote-017

Changed: `domain`

Input:

```text
地图图例以 WGS 84 标示坐标参考系统。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整正式文本；專名、引文、標題、型號、代碼或符號必須保留。

Gemini reason: 地理座標系統 WGS 84，技術標準代號保護。

Maintainer decision: `pending`

### 22. zhtw-project-formal-entity-guard-v1/title-009

Changed: `domain`

Input:

```text
技术规范引用 ISO/IEC 27001:2022 的完整版本标记。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | over_conversion_guard | high | - |

Codex reason: 完整正式文本；專名、引文、標題、型號、代碼或符號必須保留。

Gemini reason: 資訊安全標準 ISO/IEC 27001:2022，技術規範號保護。

Maintainer decision: `pending`

### 23. zhtw-project-formal-entity-guard-v1/title-011

Changed: `domain`

Input:

```text
委员会将文件编号 COM(2026) 42 final 列在页首。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整正式文本；專名、引文、標題、型號、代碼或符號必須保留。

Gemini reason: 歐盟委員會官方文件編號 COM(2026) 42 final 保護。

Maintainer decision: `pending`

### 24. zhtw-project-formal-entity-guard-v1/title-012

Changed: `domain`

Input:

```text
决议附件沿用 Annex III，不改写罗马数字。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整正式文本；專名、引文、標題、型號、代碼或符號必須保留。

Gemini reason: 官方文件附件代號 Annex III，羅馬數字保護。

Maintainer decision: `pending`

### 25. zhtw-project-formal-entity-guard-v1/title-015

Changed: `domain`

Input:

```text
官方译本保留文件代号 A/HRC/56/12。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整正式文本；專名、引文、標題、型號、代碼或符號必須保留。

Gemini reason: 聯合國人權理事會文件代號 A/HRC/56/12 保護。

Maintainer decision: `pending`

### 26. zhtw-project-formal-entity-guard-v1/title-016

Changed: `domain`

Input:

```text
预算书将 FY2027 视为财政年度识别码。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整正式文本；專名、引文、標題、型號、代碼或符號必須保留。

Gemini reason: 財政年度識別碼 FY2027，會計代碼保護。

Maintainer decision: `pending`

### 27. zhtw-project-formal-entity-guard-v1/title-017

Changed: `domain`

Input:

```text
调查报告的 Exhibit B-4 必须对应原始附件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 完整正式文本；專名、引文、標題、型號、代碼或符號必須保留。

Gemini reason: 法庭/調查展覽件編號 Exhibit B-4，證物代號保護。

Maintainer decision: `pending`
