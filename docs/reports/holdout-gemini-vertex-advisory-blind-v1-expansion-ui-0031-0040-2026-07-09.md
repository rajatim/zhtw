<!-- zhtw:disable -->
# Holdout Gemini Vertex Advisory (2026-07-09)

Dataset: `blind-v1`
Inputs: `benchmarks/accuracy/blind-v1.inputs.json`
Codex advisory: `docs/reports/holdout-codex-first-pass-blind-v1-expansion-127-cases-2026-07-09.json`
Raw JSON: `docs/reports/holdout-gemini-vertex-advisory-blind-v1-expansion-ui-0031-0040-2026-07-09.json`
Reviewer: `gemini_vertex`
Model: `gemini-2.5-flash`

## Policy

- Gemini saw only the input cases, not Codex recommendations.
- This report is advisory only.
- It is not ground truth and must not populate `blind-v1.expected.json` directly.
- Maintainer confirmation is required before any expected value becomes human decision.

## Summary

- Cases: 10
- Exact matches with Codex: 7
- Differences from Codex: 3
- Needs maintainer review: 5

Gemini confidence:

- `high`: 10

Domain distribution:

- `ui`: 10

## Maintainer Review Queue

- `blind-ui-0034` (ui, different, Codex medium, Gemini high)
- `blind-ui-0035` (ui, match, Codex medium, Gemini high)
- `blind-ui-0038` (ui, match, Codex medium, Gemini high)
- `blind-ui-0039` (ui, different, Codex medium, Gemini high)
- `blind-ui-0040` (ui, different, Codex high, Gemini high)

## Comparisons

### blind-ui-0031：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
请选择要导出的资料范围。
```

Codex expected:

```text
請選擇要匯出的資料範圍。
```

Gemini expected:

```text
請選擇要匯出的資料範圍。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text

```

### blind-ui-0032：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
删除账号前需要再次输入密码。
```

Codex expected:

```text
刪除帳號前需要再次輸入密碼。
```

Gemini expected:

```text
刪除帳號前需要再次輸入密碼。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text

```

### blind-ui-0033：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
管理员可以隐藏侧边栏里的测试功能。
```

Codex expected:

```text
管理員可以隱藏側邊欄裡的測試功能。
```

Gemini expected:

```text
管理員可以隱藏側邊欄裡的測試功能。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text

```

### blind-ui-0034：different

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
表单提交成功后会返回首页。
```

Codex expected:

```text
表單送出成功後會返回首頁。
```

Gemini expected:

```text
表單提交成功後會返回首頁。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text

```

### blind-ui-0035：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
如果没有网络，应用会显示离线提示。
```

Codex expected:

```text
如果沒有網路，應用程式會顯示離線提示。
```

Gemini expected:

```text
如果沒有網路，應用程式會顯示離線提示。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text

```

### blind-ui-0036：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
请拖动滑块调整音量。
```

Codex expected:

```text
請拖曳滑桿調整音量。
```

Gemini expected:

```text
請拖曳滑桿調整音量。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text

```

### blind-ui-0037：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
系统会根据语言设置显示日期格式。
```

Codex expected:

```text
系統會根據語言設定顯示日期格式。
```

Gemini expected:

```text
系統會根據語言設定顯示日期格式。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text

```

### blind-ui-0038：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
登录逾时后，请重新验证身份。
```

Codex expected:

```text
登入逾時後，請重新驗證身分。
```

Gemini expected:

```text
登入逾時後，請重新驗證身分。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text

```

### blind-ui-0039：different

- Domain: `ui`
- Risk: `over_conversion_guard`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
请确认收藏夹里的名称没有被自动替换。
```

Codex expected:

```text
請確認我的最愛裡的名稱沒有被自動替換。
```

Gemini expected:

```text
請確認我的最愛裡的名稱沒有被自動取代。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text

```

### blind-ui-0040：different

- Domain: `ui`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
这个按钮文字已经由台湾团队审核。
```

Codex expected:

```text
這個按鈕文字已經由台灣團隊審核。
```

Gemini expected:

```text
這個按鈕文字已經由臺灣團隊審核。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text

```
