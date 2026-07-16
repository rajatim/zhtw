<!-- zhtw:disable -->
# Holdout Gemini Vertex Advisory (2026-07-09)

Dataset: `blind-v1`
Inputs: `benchmarks/accuracy/blind-v1.inputs.json`
Codex advisory: `docs/reports/holdout-codex-first-pass-blind-v1-expansion-127-cases-2026-07-09.json`
Raw JSON: `docs/reports/holdout-gemini-vertex-advisory-blind-v1-expansion-formal-0016-0033-2026-07-09.json`
Reviewer: `gemini_vertex`
Model: `gemini-2.5-flash`

## Policy

- Gemini saw only the input cases, not Codex recommendations.
- This report is advisory only.
- It is not ground truth and must not populate `blind-v1.expected.json` directly.
- Maintainer confirmation is required before any expected value becomes human decision.

## Summary

- Cases: 18
- Exact matches with Codex: 16
- Differences from Codex: 2
- Needs maintainer review: 6

Gemini confidence:

- `high`: 18

Domain distribution:

- `formal`: 18

## Maintainer Review Queue

- `blind-formal-0023` (formal, match, Codex medium, Gemini high)
- `blind-formal-0026` (formal, match, Codex high, Gemini high)
- `blind-formal-0027` (formal, different, Codex high, Gemini high)
- `blind-formal-0028` (formal, match, Codex high, Gemini high)
- `blind-formal-0029` (formal, different, Codex high, Gemini high)
- `blind-formal-0030` (formal, match, Codex high, Gemini high)

## Comparisons

### blind-formal-0016：match

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
本公司将于下周发布年度营运报告。
```

Codex expected:

```text
本公司將於下週發布年度營運報告。
```

Gemini expected:

```text
本公司將於下週發布年度營運報告。
```

Gemini acceptable variants:

```text
本公司將於下週發佈年度營運報告。
```

Gemini notes:

```text
將於 (将于), 下週 (下周), 發布 (发布), 營運 (营运), 報告 (报告) 為台灣繁體中文常用詞彙。
```

### blind-formal-0017：match

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
申请人应于期限内补交相关证明文件。
```

Codex expected:

```text
申請人應於期限內補交相關證明文件。
```

Gemini expected:

```text
申請人應於期限內補交相關證明文件。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
申請 (申请), 補交 (补交), 證明 (证明) 為台灣繁體中文常用詞彙。
```

### blind-formal-0018：match

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
会议主席宣布本案延后审议。
```

Codex expected:

```text
會議主席宣布本案延後審議。
```

Gemini expected:

```text
會議主席宣布本案延後審議。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
會議 (会议), 審議 (审议) 為台灣繁體中文常用詞彙。
```

### blind-formal-0019：match

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
该计划预计提升公共服务效率。
```

Codex expected:

```text
該計畫預計提升公共服務效率。
```

Gemini expected:

```text
該計畫預計提升公共服務效率。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
該 (该), 計畫 (计划), 預計 (预计) 為台灣繁體中文常用詞彙。
```

### blind-formal-0020：match

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
新闻稿表示，双方将建立长期合作机制。
```

Codex expected:

```text
新聞稿表示，雙方將建立長期合作機制。
```

Gemini expected:

```text
新聞稿表示，雙方將建立長期合作機制。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
新聞稿 (新闻稿), 雙方 (双方), 將 (将), 機制 (机制) 為台灣繁體中文常用詞彙。
```

### blind-formal-0021：match

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
委员会要求各部门提出改善方案。
```

Codex expected:

```text
委員會要求各部門提出改善方案。
```

Gemini expected:

```text
委員會要求各部門提出改善方案。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
委員會 (委员会), 部門 (部门) 為台灣繁體中文常用詞彙。
```

### blind-formal-0022：match

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
本次调查结果将作为后续政策参考。
```

Codex expected:

```text
本次調查結果將作為後續政策參考。
```

Gemini expected:

```text
本次調查結果將作為後續政策參考。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
調查 (调查), 結果 (结果), 將 (将), 作為 (作为), 後續 (后续), 參考 (参考) 為台灣繁體中文常用詞彙。
```

### blind-formal-0023：match

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
承办单位应保存完整申请记录。
```

Codex expected:

```text
承辦單位應保存完整申請紀錄。
```

Gemini expected:

```text
承辦單位應保存完整申請紀錄。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
承辦 (承办), 單位 (单位), 申請 (申请), 紀錄 (记录) 為台灣繁體中文常用詞彙。
```

### blind-formal-0024：match

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
报告指出，资料质量会影响统计结果。
```

Codex expected:

```text
報告指出，資料品質會影響統計結果。
```

Gemini expected:

```text
報告指出，資料品質會影響統計結果。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
報告 (报告), 資料 (资料), 品質 (质量), 影響 (影响), 統計 (统计), 結果 (结果) 為台灣繁體中文常用詞彙。
```

### blind-formal-0025：match

- Domain: `formal`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
公告内容将同步发布于官方网站。
```

Codex expected:

```text
公告內容將同步發布於官方網站。
```

Gemini expected:

```text
公告內容將同步發布於官方網站。
```

Gemini acceptable variants:

```text
公告內容將同步發佈於官方網站。
```

Gemini notes:

```text
內容 (内容), 將 (将), 發布 (发布), 網站 (网站) 為台灣繁體中文常用詞彙。
```

### blind-formal-0026：match

- Domain: `formal`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
契约条款不得排除消费者依法享有的权利。
```

Codex expected:

```text
契約條款不得排除消費者依法享有的權利。
```

Gemini expected:

```text
契約條款不得排除消費者依法享有的權利。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
契約 (契约), 條款 (条款), 消費者 (消费者), 權利 (权利) 為台灣繁體中文常用詞彙。
```

### blind-formal-0027：different

- Domain: `formal`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
既有用户权益不因系统更新而受影响。
```

Codex expected:

```text
既有使用者權益不因系統更新而受影響。
```

Gemini expected:

```text
既有用戶權益不因系統更新而受影響。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
用戶 (用户), 權益 (权益), 影響 (影响) 為台灣繁體中文常用詞彙。
```

### blind-formal-0028：match

- Domain: `formal`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
文件中的机关名称应依原核定名称记载。
```

Codex expected:

```text
文件中的機關名稱應依原核定名稱記載。
```

Gemini expected:

```text
文件中的機關名稱應依原核定名稱記載。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
機關 (机关), 名稱 (名称), 記載 (记载) 為台灣繁體中文常用詞彙。
```

### blind-formal-0029：different

- Domain: `formal`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
本案涉及台北市既有法规用语。
```

Codex expected:

```text
本案涉及台北市既有法規用語。
```

Gemini expected:

```text
本案涉及臺北市既有法規用語。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
臺北 (台北), 法規 (法规), 用語 (用语) 為台灣繁體中文常用詞彙。
```

### blind-formal-0030：match

- Domain: `formal`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
公文附件内的专有名词不得任意改写。
```

Codex expected:

```text
公文附件內的專有名詞不得任意改寫。
```

Gemini expected:

```text
公文附件內的專有名詞不得任意改寫。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
專有 (专有), 名詞 (名词), 改寫 (改写) 為台灣繁體中文常用詞彙。
```

### blind-formal-0031：match

- Domain: `formal`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
本通知自发布日起生效。
```

Codex expected:

```text
本通知自發布日起生效。
```

Gemini expected:

```text
本通知自發布日起生效。
```

Gemini acceptable variants:

```text
本通知自發佈日起生效。
```

Gemini notes:

```text
發布 (发布) 為台灣繁體中文常用詞彙。
```

### blind-formal-0032：match

- Domain: `formal`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
请各单位依限完成资料汇整。
```

Codex expected:

```text
請各單位依限完成資料彙整。
```

Gemini expected:

```text
請各單位依限完成資料彙整。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
請 (请), 單位 (单位), 資料 (资料), 彙整 (汇整) 為台灣繁體中文常用詞彙。
```

### blind-formal-0033：match

- Domain: `formal`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
相关费用由申请人自行负担。
```

Codex expected:

```text
相關費用由申請人自行負擔。
```

Gemini expected:

```text
相關費用由申請人自行負擔。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
相關 (相关), 申請 (申请), 負擔 (负担) 為台灣繁體中文常用詞彙。
```
