# Holdout Codex/Gemini Diff Review - blind-v1 batch5 100 cases

Generated: 2026-07-09

This report compares Codex first-pass advisory with independent Gemini CLI advisory. It is not ground truth and promotion is not allowed without maintainer confirmation.

## Summary

- Total cases: 100
- Exact matches: 92
- Differences: 8
- Exact but policy review: 42
- No immediate question: 50
- Maintainer queue total: 50
- Difference recommendations: {"gemini": 3, "codex": 5}
- zhtw current status for differences: {"needs_followup_if_confirmed": 2, "in_recommended_acceptable": 5, "matches_recommended": 1}
- Promotion allowed: False

## Differences

### blind-it-0094

- Domain: it
- Risk: candidate_gap
- Recommendation: gemini
- zhtw current status: needs_followup_if_confirmed
- Reason: Gemini uses the recent holdout style for engineering migration as 「遷移指令碼」; both AI reviewers prefer 「復原步驟」 over current zhtw 「回滾步驟」 for this deployment rollback context.

```text
请在迁移脚本里新增回滚步骤。
```

Codex:
```text
請在移轉指令碼裡新增復原步驟。
```

Gemini:
```text
請在遷移指令碼裡新增復原步驟。
```

Recommended:
```text
請在遷移指令碼裡新增復原步驟。
```

zhtw current:
```text
請在遷移指令碼裡新增回滾步驟。
```

### blind-ui-0068

- Domain: ui
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: in_recommended_acceptable
- Reason: Prefer Taiwan UI wording 「目前」 for current subscription plan; 「當前」 is understandable but less idiomatic for this product UI sentence.

```text
设置页面会显示当前订阅方案。
```

Codex:
```text
設定頁面會顯示目前訂閱方案。
```

Gemini:
```text
設定頁面會顯示當前訂閱方案。
```

Recommended:
```text
設定頁面會顯示目前訂閱方案。
```

zhtw current:
```text
設定頁面會顯示當前訂閱方案。
```

### blind-ui-0069

- Domain: ui
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: in_recommended_acceptable
- Reason: For direct UI control interaction, prior holdout notes prefer 「點選」 as primary while 「點擊」 remains a valid acceptable variant.

```text
点击重试按钮后会重新加载列表。
```

Codex:
```text
點選重試按鈕後會重新載入清單。
```

Gemini:
```text
點擊重試按鈕後會重新載入清單。
```

Recommended:
```text
點選重試按鈕後會重新載入清單。
```

zhtw current:
```text
點擊重試按鈕後會重新載入清單。
```

### blind-ui-0074

- Domain: ui
- Risk: candidate_gap
- Recommendation: gemini
- zhtw current status: needs_followup_if_confirmed
- Reason: 「欄位標題」 is clearer for a table column header than the shorter 「欄標題」.

```text
拖动列标题可以调整显示顺序。
```

Codex:
```text
拖曳欄標題可以調整顯示順序。
```

Gemini:
```text
拖曳欄位標題可以調整顯示順序。
```

Recommended:
```text
拖曳欄位標題可以調整顯示順序。
```

zhtw current:
```text
拖動列標題可以調整顯示順序。
```

### blind-ui-0077

- Domain: ui
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: in_recommended_acceptable
- Reason: Sidebar favorites are usually pinned in UI copy; existing regression style uses 「釘選」 for this concept.

```text
用户可以在侧边栏固定常用项目。
```

Codex:
```text
使用者可以在側邊欄釘選常用項目。
```

Gemini:
```text
使用者可以在側邊欄固定常用項目。
```

Recommended:
```text
使用者可以在側邊欄釘選常用項目。
```

zhtw current:
```text
使用者可以在側邊欄固定常用項目。
```

### blind-llm-0055

- Domain: llm
- Risk: candidate_gap
- Recommendation: gemini
- zhtw current status: matches_recommended
- Reason: Messaging-app copy commonly uses 「聊天記錄」; 「聊天紀錄」 can remain an acceptable stylistic variant.

```text
聊天记录会保留最近五轮对话。
```

Codex:
```text
聊天紀錄會保留最近五輪對話。
```

Gemini:
```text
聊天記錄會保留最近五輪對話。
```

Recommended:
```text
聊天記錄會保留最近五輪對話。
```

zhtw current:
```text
聊天記錄會保留最近五輪對話。
```

### blind-social-0052

- Domain: social
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: in_recommended_acceptable
- Reason: Existing social regression for 「這部劇」 in streaming context promotes 「這部影集」 as the primary Taiwan wording, with 「這部劇」 acceptable in colloquial use.

```text
朋友说这部剧的结局很催泪。
```

Codex:
```text
朋友說這部影集的結局很催淚。
```

Gemini:
```text
朋友說這部劇的結局很催淚。
```

Recommended:
```text
朋友說這部影集的結局很催淚。
```

zhtw current:
```text
朋友說這部劇的結局很催淚。
```

### blind-high-risk-0031

- Domain: high_risk
- Risk: candidate_gap
- Recommendation: codex
- zhtw current status: in_recommended_acceptable
- Reason: Prior high-risk holdout decisions prefer Taiwan medical wording 「病患」 as primary; 「患者」 remains acceptable but should not be the primary expected without maintainer approval.

```text
医师应向患者说明手术风险和替代方案。
```

Codex:
```text
醫師應向病患說明手術風險和替代方案。
```

Gemini:
```text
醫師應向患者說明手術風險和替代方案。
```

Recommended:
```text
醫師應向病患說明手術風險和替代方案。
```

zhtw current:
```text
醫師應向患者說明手術風險和替代方案。
```

## Exact But Policy Review

- `blind-it-0089` (it, candidate_gap): Codex confidence medium, Gemini confidence medium
- `blind-it-0091` (it, candidate_gap): Codex confidence medium, Gemini confidence medium
- `blind-it-0102` (it, candidate_gap): Codex confidence medium, Gemini confidence medium
- `blind-it-0105` (it, candidate_gap): Codex confidence medium, Gemini confidence medium
- `blind-it-0106` (it, over_conversion_guard): over-conversion guard
- `blind-it-0107` (it, over_conversion_guard): over-conversion guard
- `blind-it-0108` (it, over_conversion_guard): over-conversion guard
- `blind-it-0109` (it, over_conversion_guard): over-conversion guard
- `blind-ui-0073` (ui, candidate_gap): Codex confidence medium
- `blind-ui-0080` (ui, over_conversion_guard): over-conversion guard
- `blind-ui-0081` (ui, over_conversion_guard): over-conversion guard
- `blind-ui-0082` (ui, over_conversion_guard): over-conversion guard
- `blind-ui-0083` (ui, over_conversion_guard): over-conversion guard
- `blind-ui-0084` (ui, over_conversion_guard): over-conversion guard
- `blind-ui-0087` (ui, baseline_guard): Codex confidence medium
- `blind-llm-0049` (llm, candidate_gap): Codex confidence medium
- `blind-llm-0051` (llm, candidate_gap): Codex confidence medium
- `blind-llm-0057` (llm, over_conversion_guard): over-conversion guard
- `blind-llm-0058` (llm, over_conversion_guard): over-conversion guard
- `blind-llm-0059` (llm, over_conversion_guard): over-conversion guard
- `blind-llm-0060` (llm, over_conversion_guard): over-conversion guard
- `blind-formal-0050` (formal, candidate_gap): Codex confidence medium
- `blind-formal-0055` (formal, candidate_gap): Codex confidence medium
- `blind-formal-0057` (formal, over_conversion_guard): over-conversion guard
- `blind-formal-0058` (formal, over_conversion_guard): over-conversion guard
- `blind-formal-0059` (formal, over_conversion_guard): over-conversion guard
- `blind-formal-0060` (formal, over_conversion_guard): over-conversion guard
- `blind-social-0049` (social, candidate_gap): Codex confidence medium
- `blind-social-0056` (social, candidate_gap): Codex confidence medium
- `blind-social-0057` (social, over_conversion_guard): over-conversion guard
- `blind-social-0058` (social, over_conversion_guard): over-conversion guard
- `blind-social-0059` (social, over_conversion_guard): over-conversion guard
- `blind-social-0060` (social, over_conversion_guard): over-conversion guard
- `blind-high-risk-0032` (high_risk, candidate_gap): high-risk domain
- `blind-high-risk-0033` (high_risk, candidate_gap): high-risk domain, Codex confidence medium
- `blind-high-risk-0034` (high_risk, candidate_gap): high-risk domain
- `blind-high-risk-0035` (high_risk, candidate_gap): high-risk domain, Codex confidence medium
- `blind-high-risk-0036` (high_risk, over_conversion_guard): high-risk domain, over-conversion guard, Codex confidence medium
- `blind-high-risk-0037` (high_risk, over_conversion_guard): high-risk domain, over-conversion guard
- `blind-high-risk-0038` (high_risk, over_conversion_guard): high-risk domain, over-conversion guard
- `blind-high-risk-0039` (high_risk, over_conversion_guard): high-risk domain, over-conversion guard, Codex confidence medium
- `blind-high-risk-0040` (high_risk, baseline_guard): high-risk domain

## No Immediate Question

`blind-it-0088`, `blind-it-0090`, `blind-it-0092`, `blind-it-0093`, `blind-it-0095`, `blind-it-0096`, `blind-it-0097`, `blind-it-0098`, `blind-it-0099`, `blind-it-0100`, `blind-it-0101`, `blind-it-0103`, `blind-it-0104`, `blind-it-0110`, `blind-it-0111`, `blind-it-0112`, `blind-ui-0070`, `blind-ui-0071`, `blind-ui-0072`, `blind-ui-0075`, `blind-ui-0076`, `blind-ui-0078`, `blind-ui-0079`, `blind-ui-0085`, `blind-ui-0086`, `blind-llm-0048`, `blind-llm-0050`, `blind-llm-0052`, `blind-llm-0053`, `blind-llm-0054`, `blind-llm-0056`, `blind-llm-0061`, `blind-llm-0062`, `blind-formal-0049`, `blind-formal-0051`, `blind-formal-0052`, `blind-formal-0053`, `blind-formal-0054`, `blind-formal-0056`, `blind-formal-0061`, `blind-formal-0062`, `blind-formal-0063`, `blind-social-0050`, `blind-social-0051`, `blind-social-0053`, `blind-social-0054`, `blind-social-0055`, `blind-social-0061`, `blind-social-0062`, `blind-social-0063`
