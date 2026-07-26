<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 023 (2026-07-27)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `a932c5d04aafd958ae618db3888473a875d479ad753a90c43cbe8bf1009c106b`
Cases: 100
Exact Codex/Gemini classifications: 85
Maintainer review queue: 15

Field differences:

- Eligibility: 2
- Script: 0
- Domain: 2
- Risk: 15

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

The maintainer resolved all 15 advisory disagreements and batch-confirmed the 85 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. chromium-strings-zh-cn-v1/translation-1547469039832541117

Changed: `risk`

Input:

```text
结束突出显示的任务。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 UI 字串；含中國軟體用語或臺灣慣用詞差異，適合 candidate-gap 評估。

Gemini reason: UI訊息，純簡體，為基準轉換標的。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 02. chromium-strings-zh-cn-v1/translation-2135919691573380097

Changed: `risk`

Input:

```text
举报此网站
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 UI 字串；含中國軟體用語或臺灣慣用詞差異，適合 candidate-gap 評估。

Gemini reason: UI標籤，純簡體，為基準轉換標的。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 03. chromium-strings-zh-cn-v1/translation-3667616615096815454

Changed: `risk`

Input:

```text
无法安装，服务器无法识别该应用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 UI 字串；含中國軟體用語或臺灣慣用詞差異，適合 candidate-gap 評估。

Gemini reason: UI錯誤訊息，純簡體，為基準轉換標的。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 04. chromium-strings-zh-cn-v1/translation-4549180975214802957

Changed: `risk`

Input:

```text
举报您认为有害的网站，帮助我们为所有人改善网络安全环境。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 UI 字串；含中國軟體用語或臺灣慣用詞差異，適合 candidate-gap 評估。

Gemini reason: UI說明文字，純簡體，為基準轉換標的。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 05. chromium-strings-zh-cn-v1/translation-4598116752460667024

Changed: `risk`

Input:

```text
从列表中搜索任何进程。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 UI 字串；含中國軟體用語或臺灣慣用詞差異，適合 candidate-gap 評估。

Gemini reason: UI操作提示，純簡體，為基準轉換標的。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 06. chromium-strings-zh-cn-v1/translation-5174969993834422967

Changed: `risk`

Input:

```text
您通常会屏蔽通知。要允许此网站向您发送通知，请点击位置栏右侧的通知图标。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 UI 字串；含中國軟體用語或臺灣慣用詞差異，適合 candidate-gap 評估。

Gemini reason: UI提示訊息，純簡體，為基準轉換標的。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 07. chromium-strings-zh-cn-v1/translation-5346389065299425353

Changed: `risk`

Input:

```text
添加多个标签页、文件和工具，让搜索更深入、更精准
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 UI 字串；含中國軟體用語或臺灣慣用詞差異，適合 candidate-gap 評估。

Gemini reason: UI說明文字，純簡體，為基準轉換標的。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 08. chromium-strings-zh-cn-v1/translation-5579324208890605088

Changed: `risk`

Input:

```text
启动错误：请以普通用户身份（非管理员身份）运行安装程序。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 UI 字串；含中國軟體用語或臺灣慣用詞差異，適合 candidate-gap 評估。

Gemini reason: UI錯誤訊息，純簡體，為基準轉換標的。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 09. chromium-strings-zh-cn-v1/translation-5924017743176219022

Changed: `risk`

Input:

```text
正在连接到互联网…
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 UI 字串；含中國軟體用語或臺灣慣用詞差異，適合 candidate-gap 評估。

Gemini reason: UI狀態訊息，純簡體，為基準轉換標的。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 10. chromium-strings-zh-cn-v1/translation-6182736845697986886

Changed: `risk`

Input:

```text
更新服务器出现内部错误，因此安装失败。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 UI 字串；含中國軟體用語或臺灣慣用詞差異，適合 candidate-gap 評估。

Gemini reason: UI錯誤訊息，純簡體，為基準轉換標的。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 11. chromium-strings-zh-cn-v1/translation-6648212540664651655

Changed: `eligible, domain, risk`

Input:

```text
从上次停下的地方继续：Chromium 已恢复您上次会话中的标签页。如需关闭此功能，请前往
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | truncated_fragment |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 字串以「請前往」結尾但缺少目的地，是脫離 placeholder 後無法獨立判讀的截斷片段。

Gemini reason: UI說明文字，簡體混合拉丁產品名，有過度轉換風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 12. chromium-strings-zh-cn-v1/translation-7413153308467572558

Changed: `eligible, domain, risk`

Input:

```text
从上次停下的地方继续：Chromium 会在您每次重启后恢复标签页。如需关闭此功能，请前往
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | truncated_fragment |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 字串以「請前往」結尾但缺少目的地，是脫離 placeholder 後無法獨立判讀的截斷片段。

Gemini reason: UI說明文字，簡體混合拉丁產品名，有過度轉換風險。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 13. chromium-strings-zh-cn-v1/translation-7624307931717240213

Changed: `risk`

Input:

```text
我们会使用这些信息来改进此服务。请参阅《隐私权政策》和《服务条款》。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 UI 字串；含中國軟體用語或臺灣慣用詞差異，適合 candidate-gap 評估。

Gemini reason: UI法律條款說明，純簡體，為基準轉換標的。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 14. chromium-strings-zh-cn-v1/translation-8556420416730706394

Changed: `risk`

Input:

```text
您可以固定图片搜索功能以方便访问，点击侧边栏顶部的“固定”按钮即可
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 UI 字串；含中國軟體用語或臺灣慣用詞差異，適合 candidate-gap 評估。

Gemini reason: UI操作提示，純簡體，為基準轉換標的。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`

### 15. chromium-strings-zh-cn-v1/translation-945522503751344254

Changed: `risk`

Input:

```text
发送反馈
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 UI 字串；含中國軟體用語或臺灣慣用詞差異，適合 candidate-gap 評估。

Gemini reason: UI按鈕，純簡體，為基準轉換標的。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-27`
