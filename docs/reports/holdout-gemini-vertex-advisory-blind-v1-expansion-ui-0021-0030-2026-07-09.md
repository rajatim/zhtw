<!-- zhtw:disable -->
# Holdout Gemini Vertex Advisory (2026-07-09)

Dataset: `blind-v1`
Inputs: `benchmarks/accuracy/blind-v1.inputs.json`
Codex advisory: `docs/reports/holdout-codex-first-pass-blind-v1-expansion-127-cases-2026-07-09.json`
Raw JSON: `docs/reports/holdout-gemini-vertex-advisory-blind-v1-expansion-ui-0021-0030-2026-07-09.json`
Reviewer: `gemini_vertex`
Model: `gemini-2.5-flash`

## Policy

- Gemini saw only the input cases, not Codex recommendations.
- This report is advisory only.
- It is not ground truth and must not populate `blind-v1.expected.json` directly.
- Maintainer confirmation is required before any expected value becomes human decision.

## Summary

- Cases: 10
- Exact matches with Codex: 9
- Differences from Codex: 1
- Needs maintainer review: 4

Gemini confidence:

- `high`: 10

Domain distribution:

- `ui`: 10

## Maintainer Review Queue

- `blind-ui-0021` (ui, match, Codex medium, Gemini high)
- `blind-ui-0025` (ui, match, Codex medium, Gemini high)
- `blind-ui-0028` (ui, match, Codex medium, Gemini high)
- `blind-ui-0030` (ui, different, Codex medium, Gemini high)

## Comparisons

### blind-ui-0021：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
点击刷新按钮后，列表会重新加载。
```

Codex expected:

```text
點擊重新整理按鈕後，清單會重新載入。
```

Gemini expected:

```text
點擊重新整理按鈕後，清單會重新載入。
```

Gemini acceptable variants:

```text
點擊重新整理按鈕後，列表會重新載入。
點擊刷新按鈕後，清單會重新載入。
```

Gemini notes:

```text
「刷新」在台灣UI中常用「重新整理」；「列表」在台灣UI中常用「清單」；「加载」在台灣UI中常用「載入」。
```

### blind-ui-0022：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
请输入手机号码以接收验证码。
```

Codex expected:

```text
請輸入手機號碼以接收驗證碼。
```

Gemini expected:

```text
請輸入手機號碼以接收驗證碼。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「手机」轉為「手機」；「号码」轉為「號碼」；「验证码」轉為「驗證碼」。
```

### blind-ui-0023：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
这个选项会影响通知的显示方式。
```

Codex expected:

```text
這個選項會影響通知的顯示方式。
```

Gemini expected:

```text
這個選項會影響通知的顯示方式。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「这个」轉為「這個」；「选项」轉為「選項」；「影响」轉為「影響」；「显示」轉為「顯示」。
```

### blind-ui-0024：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
如果上传失败，请稍后再试。
```

Codex expected:

```text
如果上傳失敗，請稍後再試。
```

Gemini expected:

```text
如果上傳失敗，請稍後再試。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「上传」轉為「上傳」；「失败」轉為「失敗」；「稍后」轉為「稍後」；「再试」轉為「再試」。
```

### blind-ui-0025：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
用户可以在设置页管理订阅方案。
```

Codex expected:

```text
使用者可以在設定頁管理訂閱方案。
```

Gemini expected:

```text
使用者可以在設定頁管理訂閱方案。
```

Gemini acceptable variants:

```text
使用者可以在設定頁面管理訂閱方案。
用戶可以在設定頁管理訂閱方案。
```

Gemini notes:

```text
「用户」在台灣UI中常用「使用者」；「设置页」在台灣UI中常用「設定頁」；「订阅」轉為「訂閱」。
```

### blind-ui-0026：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
搜索框会在输入三个字后显示建议。
```

Codex expected:

```text
搜尋框會在輸入三個字後顯示建議。
```

Gemini expected:

```text
搜尋框會在輸入三個字後顯示建議。
```

Gemini acceptable variants:

```text
搜索框會在輸入三個字後顯示建議。
```

Gemini notes:

```text
「搜索」在台灣UI中常用「搜尋」；「输入」轉為「輸入」；「显示」轉為「顯示」；「建议」轉為「建議」。
```

### blind-ui-0027：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
请先同意服务条款再继续。
```

Codex expected:

```text
請先同意服務條款再繼續。
```

Gemini expected:

```text
請先同意服務條款再繼續。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「请」轉為「請」；「服务」轉為「服務」；「条款」轉為「條款」；「继续」轉為「繼續」。
```

### blind-ui-0028：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
弹窗关闭后不会保存草稿内容。
```

Codex expected:

```text
彈出視窗關閉後不會儲存草稿內容。
```

Gemini expected:

```text
彈出視窗關閉後不會儲存草稿內容。
```

Gemini acceptable variants:

```text
彈窗關閉後不會儲存草稿內容。
彈出視窗關閉後不會保存草稿內容。
```

Gemini notes:

```text
「弹窗」在台灣UI中常用「彈出視窗」；「保存」在台灣UI中常用「儲存」；「内容」轉為「內容」。
```

### blind-ui-0029：match

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
这个页面会显示最近使用的文件。
```

Codex expected:

```text
這個頁面會顯示最近使用的檔案。
```

Gemini expected:

```text
這個頁面會顯示最近使用的檔案。
```

Gemini acceptable variants:

```text
這個頁面會顯示最近使用的文件。
```

Gemini notes:

```text
「这个」轉為「這個」；「页面」轉為「頁面」；「显示」轉為「顯示」；「文件」在台灣IT用語中常用「檔案」。
```

### blind-ui-0030：different

- Domain: `ui`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
付款完成后，收据会寄到你的邮箱。
```

Codex expected:

```text
付款完成後，收據會寄到你的信箱。
```

Gemini expected:

```text
付款完成後，收據會寄到你的電子郵件信箱。
```

Gemini acceptable variants:

```text
付款完成後，收據會寄到你的信箱。
```

Gemini notes:

```text
「收据」轉為「收據」；「邮箱」在台灣IT用語中常用「電子郵件信箱」或「信箱」。
```
