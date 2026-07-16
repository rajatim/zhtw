<!-- zhtw:disable -->
# Holdout Gemini Vertex Advisory (2026-07-09)

Dataset: `blind-v1`
Inputs: `benchmarks/accuracy/blind-v1.inputs.json`
Codex advisory: `docs/reports/holdout-codex-first-pass-blind-v1-expansion-127-cases-2026-07-09.json`
Raw JSON: `docs/reports/holdout-gemini-vertex-advisory-blind-v1-expansion-llm-0016-0032-2026-07-09.json`
Reviewer: `gemini_vertex`
Model: `gemini-2.5-flash`

## Policy

- Gemini saw only the input cases, not Codex recommendations.
- This report is advisory only.
- It is not ground truth and must not populate `blind-v1.expected.json` directly.
- Maintainer confirmation is required before any expected value becomes human decision.

## Summary

- Cases: 17
- Exact matches with Codex: 9
- Differences from Codex: 8
- Needs maintainer review: 12

Gemini confidence:

- `high`: 17

Domain distribution:

- `llm`: 17

## Maintainer Review Queue

- `blind-llm-0016` (llm, different, Codex high, Gemini high)
- `blind-llm-0017` (llm, different, Codex medium, Gemini high)
- `blind-llm-0019` (llm, match, Codex medium, Gemini high)
- `blind-llm-0021` (llm, different, Codex high, Gemini high)
- `blind-llm-0022` (llm, different, Codex high, Gemini high)
- `blind-llm-0023` (llm, match, Codex medium, Gemini high)
- `blind-llm-0024` (llm, different, Codex high, Gemini high)
- `blind-llm-0026` (llm, different, Codex high, Gemini high)
- `blind-llm-0027` (llm, match, Codex high, Gemini high)
- `blind-llm-0028` (llm, different, Codex high, Gemini high)
- `blind-llm-0029` (llm, different, Codex high, Gemini high)
- `blind-llm-0030` (llm, match, Codex high, Gemini high)

## Comparisons

### blind-llm-0016：different

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
请把下面这段说明改写成更适合开发者阅读的版本。
```

Codex expected:

```text
請把下面這段說明改寫成更適合開發者閱讀的版本。
```

Gemini expected:

```text
請將下方這段說明改寫成更適合開發者閱讀的版本。
```

Gemini acceptable variants:

```text
請把下方這段說明改寫成更適合開發者閱讀的版本。
```

Gemini notes:

```text
「请把」轉為「請將」更為正式；「下面」轉為「下方」更為常見；「开发者」轉為「開發者」為IT術語轉換。
```

### blind-llm-0017：different

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
这个模型会根据上下文生成摘要。
```

Codex expected:

```text
這個模型會根據上下文產生摘要。
```

Gemini expected:

```text
這個模型會根據上下文生成摘要。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「这个」轉為「這個」；「模型」為IT術語。
```

### blind-llm-0018：match

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
回答时请先列出假设，再提供解决步骤。
```

Codex expected:

```text
回答時請先列出假設，再提供解決步驟。
```

Gemini expected:

```text
回答時請先列出假設，再提供解決步驟。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「时」轉為「時」；「假设」轉為「假設」；「解决」轉為「解決」。
```

### blind-llm-0019：match

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
如果用户没有提供日志，请说明需要哪些信息。
```

Codex expected:

```text
如果使用者沒有提供日誌，請說明需要哪些資訊。
```

Gemini expected:

```text
如果使用者沒有提供日誌，請說明需要哪些資訊。
```

Gemini acceptable variants:

```text
如果用戶沒有提供日誌，請說明需要哪些資訊。
```

Gemini notes:

```text
「用户」轉為「使用者」為UI/IT常見用語；「日志」轉為「日誌」為IT術語；「信息」轉為「資訊」更符合台灣用語習慣。
```

### blind-llm-0020：match

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
这段提示词会要求模型输出 JSON 格式。
```

Codex expected:

```text
這段提示詞會要求模型輸出 JSON 格式。
```

Gemini expected:

```text
這段提示詞會要求模型輸出 JSON 格式。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「这段」轉為「這段」；「提示词」轉為「提示詞」為LLM相關術語；「模型」為IT術語；「输出」轉為「輸出」。
```

### blind-llm-0021：different

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
请把客服回复改成简短且礼貌的语气。
```

Codex expected:

```text
請把客服回覆改成簡短且禮貌的語氣。
```

Gemini expected:

```text
請將客服回覆改為簡短且禮貌的語氣。
```

Gemini acceptable variants:

```text
請把客服回覆改成簡短且禮貌的語氣。
```

Gemini notes:

```text
「请把」轉為「請將」更為正式；「回复」轉為「回覆」；「改成」轉為「改為」更為常見；「简短」轉為「簡短」；「礼貌」轉為「禮貌」。
```

### blind-llm-0022：different

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
模型可能会把函数名称误认为普通词语。
```

Codex expected:

```text
模型可能會把函式名稱誤認為普通詞語。
```

Gemini expected:

```text
模型可能會將函式名稱誤認為普通詞語。
```

Gemini acceptable variants:

```text
模型可能會把函式名稱誤認為普通詞語。
```

Gemini notes:

```text
「模型」為IT術語；「会把」轉為「會將」更為正式；「函数」轉為「函式」為IT術語；「词语」轉為「詞語」。
```

### blind-llm-0023：match

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
生成的说明需要包含安装步骤和常见错误。
```

Codex expected:

```text
產生的說明需要包含安裝步驟和常見錯誤。
```

Gemini expected:

```text
產生的說明需要包含安裝步驟和常見錯誤。
```

Gemini acceptable variants:

```text
生成的說明需要包含安裝步驟和常見錯誤。
```

Gemini notes:

```text
「生成」轉為「產生」更符合台灣口語習慣；「说明」轉為「說明」；「安装」轉為「安裝」；「常见」轉為「常見」。
```

### blind-llm-0024：different

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
请根据会议记录整理三点行动项目。
```

Codex expected:

```text
請根據會議紀錄整理三點行動項目。
```

Gemini expected:

```text
請根據會議記錄整理三點行動項目。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「会议」轉為「會議」；「点」轉為「點」。
```

### blind-llm-0025：match

- Domain: `llm`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
如果资料不足，请不要编造版本号。
```

Codex expected:

```text
如果資料不足，請不要編造版本號。
```

Gemini expected:

```text
如果資料不足，請不要編造版本號。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「资料」轉為「資料」；「编造」轉為「編造」；「版本号」轉為「版本號」。
```

### blind-llm-0026：different

- Domain: `llm`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
请保留原文中的台湾用语，不要自动改写。
```

Codex expected:

```text
請保留原文中的台灣用語，不要自動改寫。
```

Gemini expected:

```text
請保留原文中的臺灣用語，不要自動改寫。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「请」轉為「請」；「台湾」轉為「臺灣」為官方名稱；「自动」轉為「自動」；「改写」轉為「改寫」。
```

### blind-llm-0027：match

- Domain: `llm`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
系统提示词要求保留产品名称和变量名。
```

Codex expected:

```text
系統提示詞要求保留產品名稱和變數名稱。
```

Gemini expected:

```text
系統提示詞要求保留產品名稱和變數名稱。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「系统」轉為「系統」；「提示词」轉為「提示詞」為LLM相關術語；「产品」轉為「產品」；「变量名」轉為「變數名稱」為IT術語。
```

### blind-llm-0028：different

- Domain: `llm`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
范例输出里的台北地址应保持原样。
```

Codex expected:

```text
範例輸出裡的台北地址應保持原樣。
```

Gemini expected:

```text
範例輸出裡的臺北地址應保持原樣。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「范例」轉為「範例」；「输出」轉為「輸出」；「台北」轉為「臺北」為官方名稱。
```

### blind-llm-0029：different

- Domain: `llm`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
请勿把已审核的繁体摘要再转换一次。
```

Codex expected:

```text
請勿把已審核的繁體摘要再轉換一次。
```

Gemini expected:

```text
請勿將已審核的繁體摘要再轉換一次。
```

Gemini acceptable variants:

```text
請勿把已審核的繁體摘要再轉換一次。
```

Gemini notes:

```text
「请勿把」轉為「請勿將」更為正式；「审核」轉為「審核」；「转换」轉為「轉換」。
```

### blind-llm-0030：match

- Domain: `llm`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
这段内容混合了英文 API 名称和中文说明。
```

Codex expected:

```text
這段內容混合了英文 API 名稱和中文說明。
```

Gemini expected:

```text
這段內容混合了英文 API 名稱和中文說明。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「这段」轉為「這段」；「内容」轉為「內容」；「名称」轉為「名稱」為IT術語；「说明」轉為「說明」。
```

### blind-llm-0031：match

- Domain: `llm`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
请用两句话总结这篇文章。
```

Codex expected:

```text
請用兩句話總結這篇文章。
```

Gemini expected:

```text
請用兩句話總結這篇文章。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「请」轉為「請」；「两」轉為「兩」；「总结」轉為「總結」；「这」轉為「這」。
```

### blind-llm-0032：match

- Domain: `llm`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
如果答案不确定，请明确说明限制。
```

Codex expected:

```text
如果答案不確定，請明確說明限制。
```

Gemini expected:

```text
如果答案不確定，請明確說明限制。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「不确定」轉為「不確定」；「明确」轉為「明確」。
```
