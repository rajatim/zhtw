<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 014 (2026-07-24)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `c1d4641b153ac4827143b5d26cba263ea6da22f762252cfe59a2feeefe9e500a`
Cases: 100
Exact Codex/Gemini classifications: 75
Maintainer review queue: 25

Field differences:

- Eligibility: 0
- Script: 0
- Domain: 1
- Risk: 25

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

The maintainer resolved all 25 advisory disagreements and batch-confirmed the 75 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. aosp-framework-zh-rcn-v1/string-04e490f612fcaa02

Changed: `risk`

Input:

```text
PIN码不符，请重试。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整 Android UI 字串；含臺灣產品介面常需正規化的簡體用語。

Gemini reason: 常見 PIN 碼輸入錯誤 UI 提示。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 02. aosp-framework-zh-rcn-v1/string-114f2dd20598dd3d

Changed: `risk`

Input:

```text
已取出 SIM 卡
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整 Android UI 字串；主要需要字形轉換，保留作基準護衛。

Gemini reason: SIM 卡拔出系統通知。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 03. aosp-framework-zh-rcn-v1/string-2c548aef4c9b8a7e

Changed: `risk`

Input:

```text
停用相机
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Android UI 字串；主要需要字形轉換，保留作基準護衛。

Gemini reason: 相機停用動作名稱。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 04. aosp-framework-zh-rcn-v1/string-33ea5d6d1619e312

Changed: `risk`

Input:

```text
拨打/接听SIP电话
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Android UI 字串；格式參數、通訊縮寫或服務類型識別內容必須保留。

Gemini reason: SIP 電話撥打與接聽權限標題。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 05. aosp-framework-zh-rcn-v1/string-494f5b86cc9c7377

Changed: `risk`

Input:

```text
请输入时间
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Android UI 字串；主要需要字形轉換，保留作基準護衛。

Gemini reason: 時間輸入框佔位提示。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 06. aosp-framework-zh-rcn-v1/string-4a58f86c1c7a6b6a

Changed: `risk`

Input:

```text
漫游 - 可用系统
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Android UI 字串；主要需要字形轉換，保留作基準護衛。

Gemini reason: 電信漫遊可用系統標題。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 07. aosp-framework-zh-rcn-v1/string-626a12d2f524d3db

Changed: `risk`

Input:

```text
允许该应用使用“specialUse”类型的前台服务
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Android UI 字串；格式參數、通訊縮寫或服務類型識別內容必須保留。

Gemini reason: 特殊前景服務權限說明。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 08. aosp-framework-zh-rcn-v1/string-6b65b8fa97b1b2c5

Changed: `risk`

Input:

```text
面孔 %d
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | candidate_gap | high | has_placeholder |

Codex reason: 完整 Android UI 字串；格式參數、通訊縮寫或服務類型識別內容必須保留。

Gemini reason: 含數字佔位符的臉部標籤。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 09. aosp-framework-zh-rcn-v1/string-7179b94f61589660

Changed: `risk`

Input:

```text
%1$s 文件
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | has_placeholder |

Codex reason: 完整 Android UI 字串；格式參數、通訊縮寫或服務類型識別內容必須保留。

Gemini reason: 含佔位符的檔案標籤。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 10. aosp-framework-zh-rcn-v1/string-733a23a842172f89

Changed: `risk`

Input:

```text
所有国家/地区
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Android UI 字串；主要需要字形轉換，保留作基準護衛。

Gemini reason: 國家與地區下拉清單選項。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 11. aosp-framework-zh-rcn-v1/string-762cf6bfaabd23dd

Changed: `risk`

Input:

```text
找不到该网址。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Android UI 字串；主要需要字形轉換，保留作基準護衛。

Gemini reason: 網址未找到錯誤提示。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 12. aosp-framework-zh-rcn-v1/string-818e3249352984ff

Changed: `risk`

Input:

```text
运行“specialUse”类型的前台服务
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Android UI 字串；格式參數、通訊縮寫或服務類型識別內容必須保留。

Gemini reason: 執行特殊前景服務權限標題。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 13. aosp-framework-zh-rcn-v1/string-850768a853e8e22d

Changed: `domain, risk`

Input:

```text
请立即从沿海和河滨区域撤离到高地等较安全的地方。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 Android UI 字串；含臺灣產品介面常需正規化的簡體用語。

Gemini reason: 緊急避難廣播警報訊息。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 14. aosp-framework-zh-rcn-v1/string-9440eb5840670613

Changed: `risk`

Input:

```text
电子邮件地址
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Android UI 字串；主要需要字形轉換，保留作基準護衛。

Gemini reason: 電子郵件地址欄位名稱。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 15. aosp-framework-zh-rcn-v1/string-9d0f7c56ca13f88a

Changed: `risk`

Input:

```text
无法同步
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Android UI 字串；主要需要字形轉換，保留作基準護衛。

Gemini reason: 無法同步錯誤標示。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 16. aosp-framework-zh-rcn-v1/string-a7e7f2f478cbd1b2

Changed: `risk`

Input:

```text
注册成功。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Android UI 字串；主要需要字形轉換，保留作基準護衛。

Gemini reason: 註冊成功狀態提示。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 17. aosp-framework-zh-rcn-v1/string-af32478cab475d8f

Changed: `risk`

Input:

```text
私人“%1$s”
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | medium | - |
| Gemini | yes | ui_i18n | baseline_guard | high | has_placeholder |

Codex reason: 完整 Android UI 字串；格式參數、通訊縮寫或服務類型識別內容必須保留。

Gemini reason: 含佔位符的私人項目標籤。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 18. aosp-framework-zh-rcn-v1/string-b87cd6acf41d4c27

Changed: `risk`

Input:

```text
直到您将其关闭
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Android UI 字串；主要需要字形轉換，保留作基準護衛。

Gemini reason: 設定持續時間副標題。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 19. aosp-framework-zh-rcn-v1/string-c32debe746f13f35

Changed: `risk`

Input:

```text
正在重新启动…
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Android UI 字串；主要需要字形轉換，保留作基準護衛。

Gemini reason: 重新啟動中狀態提示。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 20. aosp-framework-zh-rcn-v1/string-cd5eacc89701c0a9

Changed: `risk`

Input:

```text
输入PIN码
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整 Android UI 字串；含臺灣產品介面常需正規化的簡體用語。

Gemini reason: PIN 碼輸入提示。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 21. aosp-framework-zh-rcn-v1/string-d8b4cc362c506011

Changed: `risk`

Input:

```text
要分享错误报告吗？
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Android UI 字串；主要需要字形轉換，保留作基準護衛。

Gemini reason: 分享錯誤報告對話框詢問。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 22. aosp-framework-zh-rcn-v1/string-d8c148817cdc822d

Changed: `risk`

Input:

```text
运行“connectedDevice”类型的前台服务
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Android UI 字串；格式參數、通訊縮寫或服務類型識別內容必須保留。

Gemini reason: 已連線裝置前景服務權限標題。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 23. aosp-framework-zh-rcn-v1/string-dce3aca9f1101e72

Changed: `risk`

Input:

```text
地图和导航
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Android UI 字串；主要需要字形轉換，保留作基準護衛。

Gemini reason: 地圖與導航類別標題。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 24. aosp-framework-zh-rcn-v1/string-f322f38dcd55df00

Changed: `risk`

Input:

```text
紧急呼叫
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Android UI 字串；主要需要字形轉換，保留作基準護衛。

Gemini reason: 緊急呼叫按鈕標籤。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`

### 25. aosp-framework-zh-rcn-v1/string-fcb0f21fdfcadcbc

Changed: `risk`

Input:

```text
紧急回拨模式
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | baseline_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 Android UI 字串；主要需要字形轉換，保留作基準護衛。

Gemini reason: 緊急回撥模式功能名稱。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-24`
