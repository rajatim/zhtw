<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 019 (2026-07-26)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `727c29673b4ee87288d09393ccd74612ac32a74534ca62ce2fd57835edf15641`
Cases: 100
Exact Codex/Gemini classifications: 39
Maintainer review queue: 61

Field differences:

- Eligibility: 3
- Script: 0
- Domain: 0
- Risk: 59

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

The maintainer resolved all 61 advisory disagreements and batch-confirmed the 39 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. aosp-framework-zh-rcn-v1/string-002a18ce98edc794

Changed: `risk`

Input:

```text
允许应用接收与安全元件上发生的事务相关的信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: 標準 AOSP UI 權限說明。主要為簡轉繁，如「允许」轉「允許」、「应用」轉「應用程式」、「事务」轉「交易」、「信息」轉「資訊」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 02. aosp-framework-zh-rcn-v1/string-023f2382b4138962

Changed: `risk`

Input:

```text
找不到提供FACTORY_TEST操作的软件包。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: 需保護 `FACTORY_TEST` 不被錯誤轉換。`软件包` 應轉換為 `軟體套件`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 03. aosp-framework-zh-rcn-v1/string-02a52e73c37acdb6

Changed: `risk`

Input:

```text
允许该应用使用设备的基本电话功能。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: 標準 UI 權限說明。主要為簡轉繁，如「应用」轉「應用程式」、「设备」轉「裝置」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 04. aosp-framework-zh-rcn-v1/string-04f19b0f466976cb

Changed: `risk`

Input:

```text
禁用漫游指示符
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 設定標籤。「漫游」應轉為「漫遊」、「指示符」應轉為「指示器」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 05. aosp-framework-zh-rcn-v1/string-0ffcf4719fc805c4

Changed: `risk`

Input:

```text
查询所有软件包
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 權限說明。「查询」應轉為「查詢」、「软件包」應轉為「軟體套件」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 06. aosp-framework-zh-rcn-v1/string-12018ce27baa6ebd

Changed: `risk`

Input:

```text
正在重置设备…
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 狀態訊息。「重置设备」應轉為「正在重設裝置」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 07. aosp-framework-zh-rcn-v1/string-146890244b8c178b

Changed: `risk`

Input:

```text
监听网络状况的观测信息
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 權限說明。「监听网络状况」應轉為「監聽網路狀況」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 08. aosp-framework-zh-rcn-v1/string-146d19f97c0840d6

Changed: `risk`

Input:

```text
解锁设备麦克风
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 權限說明。「解锁设备麦克风」應轉為「解鎖裝置麥克風」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 09. aosp-framework-zh-rcn-v1/string-15dcb24724143674

Changed: `risk`

Input:

```text
此应用可在后台运行，这样可能会加快耗电速度。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 提示訊息。「应用」轉「應用程式」、「后台」轉「背景」、「耗电」轉「耗電量」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 10. aosp-framework-zh-rcn-v1/string-1aa95729d9b4e93b

Changed: `risk`

Input:

```text
允许该应用连接到已配对的蓝牙设备
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 權限說明。「应用」轉「應用程式」、「连接到已配对的蓝牙设备」轉「連線至已配對的藍牙裝置」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 11. aosp-framework-zh-rcn-v1/string-1ab375c3e88ffb8d

Changed: `risk`

Input:

```text
输入PIN码进行解锁
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；主要需保護 placeholder、縮寫、協定名稱或識別碼。

Gemini reason: UI 提示。「输入PIN码进行解锁」轉「輸入 PIN 碼以解鎖」。PIN 碼為台灣慣用語。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 12. aosp-framework-zh-rcn-v1/string-25334c4d3b2d3e6c

Changed: `risk`

Input:

```text
无法连接到移动网络
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 狀態訊息。「无法连接到移动网络」轉「無法連線至行動網路」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 13. aosp-framework-zh-rcn-v1/string-2a201da8614435b5

Changed: `risk`

Input:

```text
身体传感器
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 權限群組名稱，簡轉繁即可。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 14. aosp-framework-zh-rcn-v1/string-2b70311ea5f2c9c1

Changed: `risk`

Input:

```text
音乐识别管理器服务
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 服務名稱。「音乐识别管理器服务」轉「音樂辨識管理員服務」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 15. aosp-framework-zh-rcn-v1/string-2cce47053dde5088

Changed: `risk`

Input:

```text
从 Android 13 开始，您安装的应用需要您授予相应权限才能发送通知。点按即可为现有应用更改此权限。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 提示訊息。需保護 `Android 13`。「应用」轉「應用程式」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 16. aosp-framework-zh-rcn-v1/string-2da608a993f54c02

Changed: `risk`

Input:

```text
不支持卫星紧急呼救功能
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 狀態訊息。「不支持卫星紧急呼救功能」轉「不支援衛星緊急呼救功能」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 17. aosp-framework-zh-rcn-v1/string-312fa1bd385e41f3

Changed: `risk`

Input:

```text
有网络获取了设备 ID
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 狀態訊息。「有网络获取了设备 ID」轉「有網路擷取了裝置 ID」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 18. aosp-framework-zh-rcn-v1/string-318f4bc7e24721ed

Changed: `risk`

Input:

```text
点按即可管理网络。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 提示。「点按即可管理网络」轉「輕觸即可管理網路」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 19. aosp-framework-zh-rcn-v1/string-38559b715b47eb62

Changed: `risk`

Input:

```text
允许该应用停用键锁以及任何关联的密码安全措施。例如，让手机在接听来电时停用键锁，在通话结束后重新启用键锁。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 權限說明。「应用」轉「應用程式」、「停用键锁」轉「停用按鍵鎖」、「关联」轉「相關聯」、「启用」轉「啟用」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 20. aosp-framework-zh-rcn-v1/string-40dccf85e052716c

Changed: `risk`

Input:

```text
屏幕上的无障碍功能快捷方式选择器
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 元件名稱。「无障碍功能快捷方式选择器」轉「無障礙功能捷徑選擇器」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 21. aosp-framework-zh-rcn-v1/string-41fe8896d8230745

Changed: `risk`

Input:

```text
正在分享错误报告…
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 狀態訊息。「正在分享错误报告」轉「正在分享錯誤報告」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 22. aosp-framework-zh-rcn-v1/string-4851d5d46b06bfc3

Changed: `risk`

Input:

```text
切换到工作资料
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 操作按鈕。「切换到工作资料」轉「切換至公司設定檔」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 23. aosp-framework-zh-rcn-v1/string-48a6d27f60ea8e1f

Changed: `risk`

Input:

```text
无法使用移动数据服务
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 狀態訊息。「无法使用移动数据服务」轉「無法使用行動數據服務」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 24. aosp-framework-zh-rcn-v1/string-4a29c5797bd60253

Changed: `risk`

Input:

```text
人脸解锁存在问题
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 狀態訊息，簡轉繁即可。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 25. aosp-framework-zh-rcn-v1/string-4ade323520ddd9e2

Changed: `risk`

Input:

```text
平板电脑中没有 SIM 卡。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；主要需保護 placeholder、縮寫、協定名稱或識別碼。

Gemini reason: UI 狀態訊息。「平板电脑」轉「平板電腦」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 26. aosp-framework-zh-rcn-v1/string-4dc65cad3e5bb72b

Changed: `eligible`

Input:

```text
要在""%3$s""中更新%1$s和%2$s吗？
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | ui_i18n | over_conversion_guard | high | malformed_source_escaping |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 來源字串含重複或未閉合引號，無法可靠還原實際使用者介面文字。

Gemini reason: UI 確認對話框。需保護 `%1$s`、`%2$s`、`%3$s`。「更新」在台灣語境通常指軟體，若指聯絡人等資料可用「更新」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 27. aosp-framework-zh-rcn-v1/string-53343decbacde448

Changed: `risk`

Input:

```text
已超出移动数据流量上限
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 狀態訊息。「已超出移动数据流量上限」轉「已超出行動數據流量上限」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 28. aosp-framework-zh-rcn-v1/string-54fefd5d0291a089

Changed: `risk`

Input:

```text
允许应用阻止平板电脑进入休眠状态。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 權限說明。「应用」轉「應用程式」、「平板电脑」轉「平板電腦」、「休眠状态」轉「休眠狀態」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 29. aosp-framework-zh-rcn-v1/string-58160384a156a61e

Changed: `risk`

Input:

```text
漫游时无法通过您的手机来更改来电转接设置。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 錯誤訊息。「漫游」轉「漫遊」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 30. aosp-framework-zh-rcn-v1/string-5a5974d7da8c2911

Changed: `risk`

Input:

```text
%1$s占用的内存已超出限制
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整 AOSP UI 輸入；主要需保護 placeholder、縮寫、協定名稱或識別碼。

Gemini reason: UI 錯誤訊息。需保護 `%1$s`。「内存」應轉為「記憶體」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 31. aosp-framework-zh-rcn-v1/string-6085144c2705c63d

Changed: `risk`

Input:

```text
无障碍功能快捷方式
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 標籤。「无障碍功能快捷方式」轉「無障礙功能捷徑」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 32. aosp-framework-zh-rcn-v1/string-744297ed74509a35

Changed: `risk`

Input:

```text
无需用户操作即可更新应用
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 權限說明。「无需用户操作即可更新应用」轉「不需使用者操作即可更新應用程式」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 33. aosp-framework-zh-rcn-v1/string-75b7e9fdd6bee705

Changed: `risk`

Input:

```text
正在通过 USB 为此设备充电
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 狀態訊息。需保護 `USB`。「为此设备充电」轉「正在為這個裝置充電」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 34. aosp-framework-zh-rcn-v1/string-790903a7da19497e

Changed: `risk`

Input:

```text
绑定到通知侦听器服务
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 權限說明。「绑定到通知侦听器服务」轉「繫結至通知接聽器服務」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 35. aosp-framework-zh-rcn-v1/string-8527a21e410c89b6

Changed: `risk`

Input:

```text
允许配套应用从后台启动前台服务。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 權限說明。「配套应用」轉「配套應用程式」、「后台」轉「背景」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 36. aosp-framework-zh-rcn-v1/string-8bb09bad9216fb39

Changed: `risk`

Input:

```text
继续进行来自其他应用的通话
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 提示。「继续进行来自其他应用的通话」轉「接續其他應用程式的通話」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 37. aosp-framework-zh-rcn-v1/string-8c1c23cf92751cd9

Changed: `risk`

Input:

```text
取消暂停应用
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 操作按鈕。「取消暂停应用」轉「取消暫停應用程式」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 38. aosp-framework-zh-rcn-v1/string-8df6c3c7d0c01665

Changed: `risk`

Input:

```text
前往“设置”
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 按鈕文字。「前往“设置”」轉「前往「設定」」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 39. aosp-framework-zh-rcn-v1/string-931512dca7eef905

Changed: `risk`

Input:

```text
使用屏幕键盘
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 提示。「使用屏幕键盘」轉「使用螢幕鍵盤」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 40. aosp-framework-zh-rcn-v1/string-9cfd744ace808666

Changed: `risk`

Input:

```text
请点按以删除您的脸部模型，然后再添加您的脸部模型
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 提示。「请点按以删除您的脸部模型...」轉「請輕觸以刪除你的人臉模型...」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 41. aosp-framework-zh-rcn-v1/string-9f176d552784b47f

Changed: `eligible`

Input:

```text
要保存到""%1$s""吗？
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | ui_i18n | over_conversion_guard | high | malformed_source_escaping |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 來源字串含重複或未閉合引號，無法可靠還原實際使用者介面文字。

Gemini reason: UI 確認對話框。需保護 `%1$s`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 42. aosp-framework-zh-rcn-v1/string-aab3b55e12989ccf

Changed: `risk`

Input:

```text
无法存储新的人脸数据。请先删除旧的人脸数据。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 錯誤訊息。「无法存储新的人脸数据」轉「無法儲存新的人臉資料」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 43. aosp-framework-zh-rcn-v1/string-b25527b293d5216d

Changed: `risk`

Input:

```text
读取您共享存储空间中的内容
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 權限說明。「读取您共享存储空间中的内容」轉「讀取您共用儲存空間中的內容」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 44. aosp-framework-zh-rcn-v1/string-b6333ff9c1a866f2

Changed: `risk`

Input:

```text
点按即可了解详情或停止应用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 提示。「点按即可了解详情或停止应用」轉「輕觸即可瞭解詳情或停止應用程式」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 45. aosp-framework-zh-rcn-v1/string-b6950cd8aef4c268

Changed: `risk`

Input:

```text
在全屏模式下打开“%s”可改善预览效果
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 提示。需保護 `%s`。「预览效果」轉「預覽效果」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 46. aosp-framework-zh-rcn-v1/string-b7877f68622d0dda

Changed: `eligible, risk`

Input:

```text
如需使用人脸解锁功能，请在“设置”>“隐私权”中开启""摄像头使用权限
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | ui_i18n | over_conversion_guard | high | malformed_source_escaping |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 來源字串含重複或未閉合引號，無法可靠還原實際使用者介面文字。

Gemini reason: UI 提示。「隐私权」轉「隱私權」、「摄像头使用权限」轉「相機使用權限」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 47. aosp-framework-zh-rcn-v1/string-b8eab5143130a9ce

Changed: `risk`

Input:

```text
访问与您的生命体征相关的传感器数据
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 權限說明。「访问与您的生命体征相关的传感器数据」轉「存取與你的生命體徵相關的感應器資料」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 48. aosp-framework-zh-rcn-v1/string-b907d464bd9b6d1d

Changed: `risk`

Input:

```text
结束会话
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 按鈕文字。「结束会话」轉「結束工作階段」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 49. aosp-framework-zh-rcn-v1/string-bb62a0d3b16d92e9

Changed: `risk`

Input:

```text
允许应用更改绑定网络连接的状态。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 權限說明。「应用」轉「應用程式」、「绑定网络连接」轉「繫結網路連線」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 50. aosp-framework-zh-rcn-v1/string-bcdd661feca46e04

Changed: `risk`

Input:

```text
实体键盘
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 標籤。「实体键盘」轉「實體鍵盤」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 51. aosp-framework-zh-rcn-v1/string-c6286d49853e5688

Changed: `risk`

Input:

```text
外部设备
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 標籤。「外部设备」轉「外部裝置」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 52. aosp-framework-zh-rcn-v1/string-d6e109ea93d97cc3

Changed: `risk`

Input:

```text
无法复制到剪贴板
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 錯誤訊息。「无法复制到剪贴板」轉「無法複製到剪貼簿」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 53. aosp-framework-zh-rcn-v1/string-db508ee5d7d32308

Changed: `risk`

Input:

```text
无法截取错误报告的屏幕截图
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 錯誤訊息。「无法截取错误报告的屏幕截图」轉「無法擷取錯誤報告的螢幕截圖」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 54. aosp-framework-zh-rcn-v1/string-e4707e773f73e282

Changed: `risk`

Input:

```text
自动化测试框架模式已启用
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 狀態訊息。「自动化测试框架模式已启用」轉「自動化測試架構模式已啟用」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 55. aosp-framework-zh-rcn-v1/string-e875ab12789ec47f

Changed: `risk`

Input:

```text
截取屏幕截图
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 操作按鈕。「截取屏幕截图」轉「擷取螢幕截圖」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 56. aosp-framework-zh-rcn-v1/string-e9caa8a4c81e562a

Changed: `risk`

Input:

```text
目前无法在您的%1$s上访问此内容。您可以尝试在平板电脑上访问。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 錯誤訊息。需保護 `%1$s`。「平板电脑」轉「平板電腦」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 57. aosp-framework-zh-rcn-v1/string-f614093d4cc36a75

Changed: `risk`

Input:

```text
读取同步设置
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 權限說明。「读取同步设置」轉「讀取同步設定」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 58. aosp-framework-zh-rcn-v1/string-fa36de99d8f0af41

Changed: `risk`

Input:

```text
USB 端口中有液体或碎屑
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | over_conversion_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 警告訊息。需保護 `USB`。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 59. aosp-framework-zh-rcn-v1/string-fab446ca8fd868da

Changed: `risk`

Input:

```text
此设备不支持人脸解锁
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 狀態訊息。「此设备不支持人脸解锁」轉「此裝置不支援人臉解鎖」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 60. aosp-framework-zh-rcn-v1/string-fc6ecb5dc786fc2a

Changed: `risk`

Input:

```text
访问通知
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 權限說明。「访问通知」轉「存取通知」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`

### 61. aosp-framework-zh-rcn-v1/string-ffa64e8101462310

Changed: `risk`

Input:

```text
使用其他应用
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | candidate_gap | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整 AOSP UI 輸入；含臺灣介面或技術用語正規化候選。

Gemini reason: UI 動作建議。「使用其他应用」轉「使用其他應用程式」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-26`
