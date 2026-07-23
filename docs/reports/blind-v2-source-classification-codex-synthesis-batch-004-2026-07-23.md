<!-- zhtw:disable -->
# Blind-v2 Source Classification Synthesis 004

Status: advisory only; maintainer confirmation pending

Packet: `benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-004.json`

## Summary

- Total: 100
- Exact Codex/Gemini matches: 69
- Review queue: 31
- Eligibility differences: 0
- Script differences: 0
- Domain differences: 5
- Risk differences: 27
- Recommended Gemini advisory: 21
- Recommended Codex advisory: 9
- Recommended field-level hybrid: 1

All 100 inputs are complete Simplified Chinese product scenarios. Both reviewers recommend
eligibility for every case. These project-original inputs were drafted by Codex and are
synthetic coverage material, not evidence of organic market frequency.

## Recommendation

The initial Codex pass used `baseline_guard` too broadly for several sentences containing
clear Mainland product terms such as `用户`, `文件`, `搜索`, `消息`, `设备`,
`本地`, `刷新`, and `禁用`. Gemini is preferred for those risk labels. Codex is
preferred where Gemini broadened `candidate_gap` merely because a sentence was technical,
or moved LLM product-governance cases into `it_api_cli` or `high_stakes` without a better
primary-domain fit.

| ID | Recommendation | Final domain | Final risk | Reason |
|----|----------------|--------------|------------|--------|
| llm-007 | Gemini | llm_generated | candidate_gap | `用户` is a regional product term. |
| llm-019 | Gemini | llm_generated | candidate_gap | `界面` is a Taiwan terminology target. |
| llm-026 | Hybrid | llm_generated | baseline_guard | LLM governance is the primary domain; wording needs no regional rewrite beyond script. |
| llm-029 | Gemini | llm_generated | candidate_gap | `返回的数据` exercises the Taiwan `回傳的資料` terminology gap; no literal requires preservation. |
| llm-032 | Gemini | it_api_cli | candidate_gap | File mutation workflow fits developer tooling more directly. |
| llm-033 | Gemini | it_api_cli | candidate_gap | Code review and main-branch workflow fits developer tooling. |
| llm-035 | Gemini | llm_generated | candidate_gap | `评测` is a likely Taiwan evaluation-term gap. |
| llm-038 | Codex | llm_generated | baseline_guard | Technical subject alone does not make the wording a regional gap. |
| llm-042 | Codex | llm_generated | over_conversion_guard | The sentence explicitly requires preserving proper nouns. |
| llm-048 | Codex | llm_generated | over_conversion_guard | Code is an explicit non-translation boundary. |
| llm-049 | Codex | llm_generated | candidate_gap | Batch generation is presented as an LLM product workflow, not specifically CLI/API. |
| llm-050 | Codex | llm_generated | candidate_gap | Model feature degradation is an LLM product behavior. |
| ui-001 | Gemini | ui_i18n | candidate_gap | `用户` is a regional product term. |
| ui-002 | Codex | ui_i18n | baseline_guard | Form and focus wording needs ordinary script conversion only. |
| ui-004 | Gemini | ui_i18n | candidate_gap | `文件` commonly maps to Taiwan `檔案` in this context. |
| ui-005 | Gemini | ui_i18n | candidate_gap | `文件大小` exercises the file terminology gap. |
| ui-006 | Codex | ui_i18n | baseline_guard | Date picker and keyboard wording is already region-neutral. |
| ui-008 | Gemini | ui_i18n | candidate_gap | `搜索` commonly maps to Taiwan `搜尋`. |
| ui-012 | Gemini | ui_i18n | candidate_gap | `界面` and `布局` are regional UI terminology targets. |
| ui-014 | Gemini | ui_i18n | candidate_gap | `日程` may require Taiwan product-context wording. |
| ui-015 | Gemini | ui_i18n | candidate_gap | `语言区域` exercises locale terminology. |
| ui-019 | Gemini | ui_i18n | candidate_gap | `消息` commonly maps to Taiwan `訊息`. |
| ui-021 | Gemini | ui_i18n | candidate_gap | `加载` commonly maps to Taiwan `載入`. |
| ui-031 | Codex | ui_i18n | baseline_guard | Request handling and duplicate submission are region-neutral here. |
| ui-034 | Gemini | ui_i18n | candidate_gap | `消息` is a regional UI term. |
| ui-035 | Gemini | ui_i18n | candidate_gap | `设备` commonly maps to Taiwan `裝置`. |
| ui-037 | Gemini | ui_i18n | candidate_gap | `本地` commonly maps to Taiwan `本機` in product UI. |
| ui-039 | Codex | ui_i18n | baseline_guard | Phone-number field wording does not require a regional lexical rewrite. |
| ui-042 | Gemini | ui_i18n | candidate_gap | `刷新页面` commonly maps to `重新整理頁面`. |
| ui-043 | Gemini | ui_i18n | candidate_gap | `禁用` commonly maps to Taiwan `停用`. |
| ui-045 | Gemini | ui_i18n | candidate_gap | `提交按钮` commonly maps to a Taiwan `送出按鈕` expression. |

## Human Gate

The 69 exact matches and the 31 recommendations above remain AI advisory. They must not be
recorded as maintainer decisions or promoted into the candidate pool until the maintainer
confirms them.
