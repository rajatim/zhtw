<!-- zhtw:disable -->
# Holdout Gemini Vertex Advisory (2026-07-09)

Dataset: `blind-v1`
Inputs: `benchmarks/accuracy/blind-v1.inputs.json`
Codex advisory: `docs/reports/holdout-codex-first-pass-blind-v1-expansion-127-cases-2026-07-09.json`
Raw JSON: `docs/reports/holdout-gemini-vertex-advisory-blind-v1-expansion-social-0016-0033-2026-07-09.json`
Reviewer: `gemini_vertex`
Model: `gemini-2.5-flash`

## Policy

- Gemini saw only the input cases, not Codex recommendations.
- This report is advisory only.
- It is not ground truth and must not populate `blind-v1.expected.json` directly.
- Maintainer confirmation is required before any expected value becomes human decision.

## Summary

- Cases: 18
- Exact matches with Codex: 13
- Differences from Codex: 5
- Needs maintainer review: 10

Gemini confidence:

- `high`: 18

Domain distribution:

- `social`: 18

## Maintainer Review Queue

- `blind-social-0016` (social, different, Codex high, Gemini high)
- `blind-social-0019` (social, match, Codex medium, Gemini high)
- `blind-social-0024` (social, different, Codex medium, Gemini high)
- `blind-social-0025` (social, different, Codex high, Gemini high)
- `blind-social-0026` (social, different, Codex high, Gemini high)
- `blind-social-0027` (social, match, Codex high, Gemini high)
- `blind-social-0028` (social, match, Codex high, Gemini high)
- `blind-social-0029` (social, different, Codex medium, Gemini high)
- `blind-social-0030` (social, match, Codex high, Gemini high)
- `blind-social-0031` (social, match, Codex high, Gemini high)

## Comparisons

### blind-social-0016：different

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
周末要不要一起去看展？
```

Codex expected:

```text
週末要不要一起去看展？
```

Gemini expected:

```text
週末要不要一起去看展覽？
```

Gemini acceptable variants:

```text
週末要不要一起去看展？
```

Gemini notes:

```text
「看展」在台灣口語中也常用，但「看展覽」更為完整且常見。
```

### blind-social-0017：match

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
你有收到群组里的活动通知吗？
```

Codex expected:

```text
你有收到群組裡的活動通知嗎？
```

Gemini expected:

```text
你有收到群組裡的活動通知嗎？
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「群组」轉為「群組」、「里」轉為「裡」、「活动」轉為「活動」為標準簡繁轉換。
```

### blind-social-0018：match

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
这家店的外带速度比上次快很多。
```

Codex expected:

```text
這家店的外帶速度比上次快很多。
```

Gemini expected:

```text
這家店的外帶速度比上次快很多。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「这家店」轉為「這家店」、「外带」轉為「外帶」為標準簡繁轉換。
```

### blind-social-0019：match

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
我晚点再把照片上传到共享相册。
```

Codex expected:

```text
我晚點再把照片上傳到共享相簿。
```

Gemini expected:

```text
我晚點再把照片上傳到共享相簿。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「晚点」轉為「晚點」、「上传」轉為「上傳」為標準簡繁轉換。「相册」在台灣慣用「相簿」。
```

### blind-social-0020：match

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
今天通勤时间比平常多了二十分钟。
```

Codex expected:

```text
今天通勤時間比平常多了二十分鐘。
```

Gemini expected:

```text
今天通勤時間比平常多了二十分鐘。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「时间」轉為「時間」、「分钟」轉為「分鐘」為標準簡繁轉換。
```

### blind-social-0021：match

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
朋友说这部影片的字幕翻得不错。
```

Codex expected:

```text
朋友說這部影片的字幕翻得不錯。
```

Gemini expected:

```text
朋友說這部影片的字幕翻得不錯。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「说」轉為「說」、「这部」轉為「這部」為標準簡繁轉換。
```

### blind-social-0022：match

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
如果下雨，我们就改约室内场地。
```

Codex expected:

```text
如果下雨，我們就改約室內場地。
```

Gemini expected:

```text
如果下雨，我們就改約室內場地。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「改约」轉為「改約」、「室内」轉為「室內」、「场地」轉為「場地」為標準簡繁轉換。
```

### blind-social-0023：match

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
这杯饮料甜度可以调整吗？
```

Codex expected:

```text
這杯飲料甜度可以調整嗎？
```

Gemini expected:

```text
這杯飲料甜度可以調整嗎？
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「这杯」轉為「這杯」、「饮料」轉為「飲料」、「调整」轉為「調整」為標準簡繁轉換。
```

### blind-social-0024：different

- Domain: `social`
- Risk: `candidate_gap`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
我已经把购物清单发到聊天窗口了。
```

Codex expected:

```text
我已經把購物清單傳到聊天視窗了。
```

Gemini expected:

```text
我已經把購物清單發到聊天視窗了。
```

Gemini acceptable variants:

```text
我已經把購物清單發到聊天室了。
```

Gemini notes:

```text
「已经」轉為「已經」、「购物」轉為「購物」、「清单」轉為「清單」、「发到」轉為「發到」為標準簡繁轉換。「聊天窗口」在台灣慣用「聊天視窗」或「聊天室」。
```

### blind-social-0025：different

- Domain: `social`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
留言里提到的台湾地名不要被改成其他说法。
```

Codex expected:

```text
留言裡提到的台灣地名不要被改成其他說法。
```

Gemini expected:

```text
留言裡提到的臺灣地名不要被改成其他說法。
```

Gemini acceptable variants:

```text
留言裡提到的台灣地名不要被改成其他說法。
```

Gemini notes:

```text
「里」轉為「裡」、「说法」轉為「說法」為標準簡繁轉換。「台湾」的標準繁體字為「臺灣」，但「台灣」在台灣日常使用中也極為普遍。
```

### blind-social-0026：different

- Domain: `social`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
这段贴文已经是台湾朋友写的繁体版本。
```

Codex expected:

```text
這段貼文已經是台灣朋友寫的繁體版本。
```

Gemini expected:

```text
這段貼文已經是臺灣朋友寫的繁體版本。
```

Gemini acceptable variants:

```text
這段貼文已經是台灣朋友寫的繁體版本。
```

Gemini notes:

```text
「这段」轉為「這段」、「贴文」轉為「貼文」、「已经」轉為「已經」、「繁体」轉為「繁體」為標準簡繁轉換。「台湾」的標準繁體字為「臺灣」，但「台灣」在台灣日常使用中也極為普遍。
```

### blind-social-0027：match

- Domain: `social`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
昵称和频道名称应该保持原样。
```

Codex expected:

```text
暱稱和頻道名稱應該保持原樣。
```

Gemini expected:

```text
暱稱和頻道名稱應該保持原樣。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「昵称」轉為「暱稱」、「频道」轉為「頻道」、「应该」轉為「應該」、「原样」轉為「原樣」為標準簡繁轉換。
```

### blind-social-0028：match

- Domain: `social`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
请不要把社群里的品牌标签自动转换。
```

Codex expected:

```text
請不要把社群裡的品牌標籤自動轉換。
```

Gemini expected:

```text
請不要把社群裡的品牌標籤自動轉換。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「请」轉為「請」、「里」轉為「裡」、「标签」轉為「標籤」、「自动」轉為「自動」、「转换」轉為「轉換」為標準簡繁轉換。
```

### blind-social-0029：different

- Domain: `social`
- Risk: `over_conversion_guard`
- Codex confidence: `medium`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
影片标题里的台语罗马字不要改。
```

Codex expected:

```text
影片標題裡的台語羅馬字不要改。
```

Gemini expected:

```text
影片標題裡的臺語羅馬字不要改。
```

Gemini acceptable variants:

```text
影片標題裡的台語羅馬字不要改。
```

Gemini notes:

```text
「标题里」轉為「標題裡」為標準簡繁轉換。「台语」的標準繁體字為「臺語」，但「台語」在台灣日常使用中也極為普遍。
```

### blind-social-0030：match

- Domain: `social`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
用户自订表情名称需要原样保留。
```

Codex expected:

```text
使用者自訂表情名稱需要原樣保留。
```

Gemini expected:

```text
使用者自訂表情名稱需要原樣保留。
```

Gemini acceptable variants:

```text
用戶自訂表情名稱需要原樣保留。
```

Gemini notes:

```text
「用户」在台灣UI/IT語境中常用「使用者」，「用戶」亦可接受。「自订」轉為「自訂」、「名称」轉為「名稱」、「原样」轉為「原樣」為標準簡繁轉換。
```

### blind-social-0031：match

- Domain: `social`
- Risk: `over_conversion_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `true`

Input:

```text
这则评论混合了繁体和简体，先只作为输入保留。
```

Codex expected:

```text
這則評論混合了繁體和簡體，先只作為輸入保留。
```

Gemini expected:

```text
這則評論混合了繁體和簡體，先只作為輸入保留。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「这则」轉為「這則」、「评论」轉為「評論」、「繁体」轉為「繁體」、「简体」轉為「簡體」、「作为」轉為「作為」、「输入」轉為「輸入」為標準簡繁轉換。
```

### blind-social-0032：match

- Domain: `social`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
明天早上记得带雨伞。
```

Codex expected:

```text
明天早上記得帶雨傘。
```

Gemini expected:

```text
明天早上記得帶雨傘。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「记得」轉為「記得」、「带」轉為「帶」、「雨伞」轉為「雨傘」為標準簡繁轉換。
```

### blind-social-0033：match

- Domain: `social`
- Risk: `baseline_guard`
- Codex confidence: `high`
- Gemini confidence: `high`
- Needs maintainer review: `false`

Input:

```text
我先把晚餐订好，晚点再确认人数。
```

Codex expected:

```text
我先把晚餐訂好，晚點再確認人數。
```

Gemini expected:

```text
我先把晚餐訂好，晚點再確認人數。
```

Gemini acceptable variants:

```text
(none)
```

Gemini notes:

```text
「订好」轉為「訂好」、「晚点」轉為「晚點」、「确认」轉為「確認」、「人数」轉為「人數」為標準簡繁轉換。
```
