<!-- zhtw:disable -->
# Holdout Gemini Vertex Advisory (2026-07-09)

Dataset: `blind-v1`
Inputs: `benchmarks/accuracy/blind-v1.inputs.json`
Codex advisory: `docs/reports/holdout-codex-first-pass-blind-v1-expansion-127-cases-2026-07-09.json`
Raw JSON: `docs/reports/holdout-gemini-vertex-advisory-blind-v1-expansion-ui-0041-0047-2026-07-09.json`
Reviewer: `gemini_vertex`
Model: `gemini-2.5-flash`

## Policy

- Gemini saw only the input cases, not Codex recommendations.
- This report is advisory only.
- It is not ground truth and must not populate `blind-v1.expected.json` directly.
- Maintainer confirmation is required before any expected value becomes human decision.

## Summary

- Cases: 7
- Exact matches with Codex: 7
- Differences from Codex: 0
- Needs maintainer review: 4

Gemini confidence:

- `high`: 7

Domain distribution:

- `ui`: 7

## Maintainer Review Queue

- `blind-ui-0041` (ui, match, Codex high, Gemini high)
- `blind-ui-0042` (ui, match, Codex high, Gemini high)
- `blind-ui-0043` (ui, match, Codex high, Gemini high)
- `blind-ui-0044` (ui, match, Codex high, Gemini high)

## Comparisons

### blind-ui-0041：match

- Domain: `ui`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
页面标题里的品牌名称必须保持原样。
```

Codex expected:

```text
頁面標題裡的品牌名稱必須保持原樣。
```

Gemini expected:

```text
頁面標題裡的品牌名稱必須保持原樣。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「页面」轉為「頁面」，「标题」轉為「標題」，「里」轉為「裡」，「名称」轉為「名稱」，「必须」轉為「必須」，「原样」轉為「原樣」。
```

### blind-ui-0042：match

- Domain: `ui`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
用户自订标签不会套用地区词转换。
```

Codex expected:

```text
使用者自訂標籤不會套用地區詞轉換。
```

Gemini expected:

```text
使用者自訂標籤不會套用地區詞轉換。
```

Gemini acceptable variants:

```text
用戶自訂標籤不會套用地區詞轉換。
```

Gemini notes:

```text
「用户」在台灣UI語境中常轉為「使用者」；「自订」轉為「自訂」，「标签」轉為「標籤」，「不会」轉為「不會」，「地区词」轉為「地區詞」，「转换」轉為「轉換」。
```

### blind-ui-0043：match

- Domain: `ui`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
请保留繁体说明中的专有名词。
```

Codex expected:

```text
請保留繁體說明中的專有名詞。
```

Gemini expected:

```text
請保留繁體說明中的專有名詞。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「请」轉為「請」，「繁体」轉為「繁體」，「说明」轉為「說明」，「专有名词」轉為「專有名詞」。
```

### blind-ui-0044：match

- Domain: `ui`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
导览列中的 OpenAPI 字样不需要转换。
```

Codex expected:

```text
導覽列中的 OpenAPI 字樣不需要轉換。
```

Gemini expected:

```text
導覽列中的 OpenAPI 字樣不需要轉換。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「导览列」轉為「導覽列」，「字样」轉為「字樣」，「不需要」轉為「不需要」，「转换」轉為「轉換」。OpenAPI 為專有名詞，保持不變。
```

### blind-ui-0045：match

- Domain: `ui`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
这个页面目前没有任何通知。
```

Codex expected:

```text
這個頁面目前沒有任何通知。
```

Gemini expected:

```text
這個頁面目前沒有任何通知。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「这个」轉為「這個」，「页面」轉為「頁面」，「没有」轉為「沒有」。
```

### blind-ui-0046：match

- Domain: `ui`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
取消操作后会回到上一页。
```

Codex expected:

```text
取消操作後會回到上一頁。
```

Gemini expected:

```text
取消操作後會回到上一頁。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「后」轉為「後」，「会」轉為「會」，「上一页」轉為「上一頁」。
```

### blind-ui-0047：match

- Domain: `ui`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
密码长度必须至少八个字符。
```

Codex expected:

```text
密碼長度必須至少八個字元。
```

Gemini expected:

```text
密碼長度必須至少八個字元。
```

Gemini acceptable variants:

```text
密碼長度必須至少八個字符。
```

Gemini notes:

```text
「密码」轉為「密碼」，「长度」轉為「長度」，「必须」轉為「必須」，「八个」轉為「八個」。在IT語境中，「字符」在台灣常轉為「字元」。
```
