<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 038 (2026-07-28)

Status: all advisory disagreements resolved by maintainer

Packet SHA-256: `5bf0b75ae05fd8aae18c36096186134222776b3d8508df3ab8eeece4b7a4a76e`
Cases: 96
Exact Codex/Gemini classifications: 45
Maintainer review queue: 51

Field differences:

- Eligibility: 4
- Script: 6
- Domain: 16
- Risk: 47

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its execution recorded 0 tool calls and 0 API errors.

The maintainer resolved all 51 advisory disagreements and batch-confirmed the 45 exact AI matches after reviewing the Codex synthesis. No classification in this report has been written into the candidate pool.

## Review Queue

### 01. cisa-personal-security-zh-hans-v1/sentence-009

Changed: `risk`

Input:

```text
您的工作或职业是否会让您成为具有吸引力的目标？
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 個人安全相關，用詞直接，屬於基準測試。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 02. cisa-personal-security-zh-hans-v1/sentence-014

Changed: `risk`

Input:

```text
如今，关键基础设施员工可能面临各种威胁，如普通犯罪活动和暴力极端分子阴谋。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 涉及關鍵基礎設施安全，多個詞彙需正確轉換，可當基準。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 03. cisa-personal-security-zh-hans-v1/sentence-026

Changed: `risk`

Input:

```text
您需要维护房产外的墙壁和栅栏等结构，确保任何可用于进入您家的工具或梯子存放在安全位置。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 居家安全建議，標準轉換詞彙多，適合做基準。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 04. cisa-personal-security-zh-hans-v1/sentence-075

Changed: `risk`

Input:

```text
如果您发现有人在您家、您的工作场所或车辆附近丢弃物品或包裹，请立即报警。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 公共安全情境，包含地點、物品等名詞，是好的基準案例。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 05. cisa-personal-security-zh-hans-v1/sentence-086

Changed: `risk`

Input:

```text
请记住，“缓和”并非指您的行为，而是您的目标。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 解釋術語「緩和」，測試引號及概念詞轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 06. massive-1-0-zh-cn-v1/10483

Changed: `eligible, domain, risk`

Input:

```text
艾德·希兰中我最喜欢的音乐有哪些可用的列表
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 來源句不完整、依賴前文或語意明顯錯置，無法作為可獨立裁決的 benchmark 輸入。

Gemini reason: 完整的日常對話句子，涉及人名與音樂。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 07. massive-1-0-zh-cn-v1/10755

Changed: `domain, risk`

Input:

```text
删掉我的待办清单
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | ui_product | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 明確的 UI 指令，適合測試基礎詞彙「待辦清單」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 08. massive-1-0-zh-cn-v1/10886

Changed: `risk`

Input:

```text
我能查看我的清单吗
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 日常詢問，語意完整。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 09. massive-1-0-zh-cn-v1/11139

Changed: `domain, risk`

Input:

```text
保存新清单
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | ui_product | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 常見的 UI 操作指令。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 10. massive-1-0-zh-cn-v1/11496

Changed: `eligible, domain, risk`

Input:

```text
播放一席播客
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 來源句不完整、依賴前文或語意明顯錯置，無法作為可獨立裁決的 benchmark 輸入。

Gemini reason: 指令包含專有名詞「一席」，適合測試。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 11. massive-1-0-zh-cn-v1/13176

Changed: `risk`

Input:

```text
找最近的名人活动
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 查詢活動資訊，語意完整。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 12. massive-1-0-zh-cn-v1/14857

Changed: `risk`

Input:

```text
你能解释一下过高的意思吗
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 解釋詞義的請求，語意完整。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 13. massive-1-0-zh-cn-v1/14860

Changed: `risk`

Input:

```text
将美元兑换成欧元
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 常見的貨幣換算指令。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 14. massive-1-0-zh-cn-v1/2405

Changed: `domain`

Input:

```text
该把厨房的灯调暗了
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | ui_product | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 明確的智慧家庭控制指令。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 15. massive-1-0-zh-cn-v1/3151

Changed: `domain, risk`

Input:

```text
移除早先的闹钟
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | ui_product | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 移除鬧鐘的指令，語意清晰。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 16. massive-1-0-zh-cn-v1/3328

Changed: `risk`

Input:

```text
给我展示新闻
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 常見的新聞查詢指令。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 17. massive-1-0-zh-cn-v1/3334

Changed: `domain, risk`

Input:

```text
让扫地机器人打扫房间
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | ui_product | over_conversion_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 智慧家庭指令，包含「扫地机器人」，需注意是否過度轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 18. massive-1-0-zh-cn-v1/4197

Changed: `domain, risk`

Input:

```text
重复下一首歌
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | ui_product | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 音樂播放控制指令。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 19. massive-1-0-zh-cn-v1/5807

Changed: `domain`

Input:

```text
你也可以在家里添加额外的开关来控制更多的设备
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | baseline_guard | medium | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 描述智慧家庭設備功能，句子結構完整。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 20. massive-1-0-zh-cn-v1/6792

Changed: `risk`

Input:

```text
告诉我我的事项
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 查詢個人事項，語意完整。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 21. massive-1-0-zh-cn-v1/7451

Changed: `domain, risk`

Input:

```text
请将这项活动添加到我的日历
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | ui_product | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 新增日曆活動的指令。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 22. massive-1-0-zh-cn-v1/7458

Changed: `domain, risk`

Input:

```text
记住中午十二点以前到机场接我我下午三点有个会议
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 複合指令，包含時間、地點和事件，適合做為高要求測試。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 23. massive-1-0-zh-cn-v1/8525

Changed: `domain, risk`

Input:

```text
三点到五点会面的提醒
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | ui_product | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 設定提醒事項的指令。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 24. massive-1-0-zh-cn-v1/9173

Changed: `domain, risk`

Input:

```text
提醒我五月二十三日和牙医的会议
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 可獨立判讀的日常語音助理輸入；可檢驗臺灣用語與實體保護。

Gemini reason: 包含日期和事件的提醒指令，屬於高準確度要求場景。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 25. ready-gov-home-fires-zh-hans-v1/sentence-005

Changed: `risk`

Input:

```text
火焰中的楼面室温可达 100 度，但在眼睛的高度处能升到 600 度。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 消防安全資訊，度量衡與單位轉換詞「度」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 26. ready-gov-home-fires-zh-hans-v1/sentence-010

Changed: `risk`

Input:

```text
有效的烟雾报警器能显着增加在致命家中火灾中幸存的机会。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 消防安全資訊，常用詞「煙霧」、「顯著」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 27. ready-gov-home-fires-zh-hans-v1/sentence-047

Changed: `domain`

Input:

```text
在离开现场之前，消防部门应确保公用设施可安全使用或断开连接。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 官方程序說明，涉及術語「公用設施」、「斷開連接」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 28. ready-gov-home-fires-zh-hans-v1/sentence-066

Changed: `risk`

Input:

```text
使蜡烛与易燃材料保持至少 12 英寸的距离，或考虑使用无焰蜡烛。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 消防安全建議，常用詞「蠟燭」、「考慮」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 29. ready-gov-home-fires-zh-hans-v1/sentence-075

Changed: `script, risk`

Input:

```text
只买国家认可实验室评估过的加热器，例如，美国保险商实验室 (UL)。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 消費安全建議，含組織名稱「保險商實驗室」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 30. ready-gov-home-fires-zh-hans-v1/sentence-076

Changed: `risk`

Input:

```text
确保便携式加热器有恒温器控制机制，倒地时会自动关闭。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 產品安全說明，涉及技術詞彙「便攜式」、「恆溫器」、「機制」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 31. ready-gov-home-fires-zh-hans-v1/sentence-077

Changed: `script, risk`

Input:

```text
在煤油加热器中只用晶莹剔透的 K-1 煤油。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 特定產品使用說明，含專有型號 K-1。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 32. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-003

Changed: `risk`

Input:

```text
当大量的岩石、泥土或碎片沿着斜坡移动时，就会发生山体滑坡。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | baseline_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 定義「山體滑坡」，屬防災主題，為重要術語轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 33. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-018

Changed: `script, risk`

Input:

```text
但是，您可以使用沙袋、挡土墙或k-rails（泽西护栏）来保护您的财产免受洪水或泥浆的侵袭。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 包含專有名詞「擋土牆」與「澤西護欄」（紐澤西護欄）。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 34. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-022

Changed: `risk`

Input:

```text
如果您面临山体滑坡的风险，请咨询您的保险代理人。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 簡短句子，包含「面臨」、「風險」、「保險」等基本詞彙。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 35. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-027

Changed: `risk`

Input:

```text
随着山体滑坡的临近，可以注意到音量逐渐增大的微弱隆隆声。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 描述山崩前兆，包含「隨著」、「鄰近」、「隆隆聲」等基本轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 36. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-041

Changed: `eligible, domain, risk`

Input:

```text
他们根据您社区中的威胁提供最新建议。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | context_dependent_fragment |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 來源句不完整、依賴前文或語意明顯錯置，無法作為可獨立裁決的 benchmark 輸入。

Gemini reason: 句子雖短，但測試「根據」、「社區」、「威脅」等高頻詞。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 37. ready-gov-landslides-debris-flow-zh-hans-v1/sentence-043

Changed: `eligible, domain, risk`

Input:

```text
许多人死于山体滑坡是在人们睡觉时发生的。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | no | null | null | high | malformed_translation |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 來源句不完整、依賴前文或語意明顯錯置，無法作為可獨立裁決的 benchmark 輸入。

Gemini reason: 描述事實，包含「許多」、「人們」、「睡覺」等常用詞。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 38. ready-gov-radiation-zh-hans-v1/sentence-026

Changed: `risk`

Input:

```text
如果它在地面上引爆，爆炸会将物质吸入空气中，并产生危险的、类似沙子的放射性粒子，称为沉降物。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 包含「粒子」、「沉降物」等術語，可作為基準轉換測試。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 39. ready-gov-radiation-zh-hans-v1/sentence-056

Changed: `risk`

Input:

```text
充分饮水和进食：进食和饮用建筑物内的食物是安全的。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | candidate_gap | medium | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整且可獨立判讀的公共安全敘述；適合高風險語境轉換檢驗。

Gemini reason: 標準陳述句，測試基本詞彙「飲水」、「進食」、「食物」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 40. zhtw-project-it-llm-social-guard-v1/llm-001

Changed: `risk`

Input:

```text
模型生成的摘要遗漏了附件中的限制条件，需要重新评估。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整的 LLM 工作流程敘述；可檢驗技術詞彙的臺灣慣用表達。

Gemini reason: LLM 相關用語，測試一般轉換的準確性。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 41. zhtw-project-it-llm-social-guard-v1/llm-003

Changed: `risk`

Input:

```text
助手无法确认资料来源时，应明确标注不确定性。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整的 LLM 工作流程敘述；可檢驗技術詞彙的臺灣慣用表達。

Gemini reason: LLM 相關用語，測試一般轉換的準確性。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 42. zhtw-project-it-llm-social-guard-v1/llm-005

Changed: `risk`

Input:

```text
模型把用户的否定句误解成肯定句，导致结论相反。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整的 LLM 工作流程敘述；可檢驗技術詞彙的臺灣慣用表達。

Gemini reason: LLM 相關用語，測試一般轉換的準確性。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 43. zhtw-project-it-llm-social-guard-v1/llm-006

Changed: `risk`

Input:

```text
这个工作流会先检索知识库，再调用外部工具补充信息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整的 LLM 工作流程敘述；可檢驗技術詞彙的臺灣慣用表達。

Gemini reason: LLM 相關用語，測試「工作流」、「知识库」等詞彙轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 44. zhtw-project-it-llm-social-guard-v1/llm-008

Changed: `risk`

Input:

```text
上下文窗口不足时，系统会优先保留最近的用户消息。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整的 LLM 工作流程敘述；可檢驗技術詞彙的臺灣慣用表達。

Gemini reason: LLM 核心術語「上下文窗口」，測試準確轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 45. zhtw-project-it-llm-social-guard-v1/llm-012

Changed: `risk`

Input:

```text
提示模板更新后，缓存中的旧回答应逐步失效。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整的 LLM 工作流程敘述；可檢驗技術詞彙的臺灣慣用表達。

Gemini reason: LLM 核心術語「提示模板」，測試準確轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 46. zhtw-project-it-llm-social-guard-v1/llm-014

Changed: `risk`

Input:

```text
助手引用网页内容时要附上标题和访问日期。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整的 LLM 工作流程敘述；可檢驗技術詞彙的臺灣慣用表達。

Gemini reason: LLM 相關用語，測試一般轉換的準確性。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 47. zhtw-project-it-llm-social-guard-v1/llm-015

Changed: `risk`

Input:

```text
模型对同一个问题连续回答三次，用来检查稳定性。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整的 LLM 工作流程敘述；可檢驗技術詞彙的臺灣慣用表達。

Gemini reason: LLM 相關用語，測試「稳定性」等詞彙轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 48. zhtw-project-it-llm-social-guard-v1/llm-019

Changed: `risk`

Input:

```text
代理准备发送消息前，必须显示收件人和完整正文。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | candidate_gap | medium | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 完整的 LLM 工作流程敘述；可檢驗技術詞彙的臺灣慣用表達。

Gemini reason: LLM 代理（Agent）相關用語，測試準確轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 49. zhtw-project-it-llm-social-guard-v1/social-001

Changed: `script, risk`

Input:

```text
我在台北车站等林怡君，她搭乘高铁 813 次。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整的日常敘述；品牌、人名、書名或識別碼必須保持不變。

Gemini reason: 日常用語，測試「车站」到「車站」的轉換，同時保留人名與高鐵班次。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 50. zhtw-project-it-llm-social-guard-v1/social-005

Changed: `script`

Input:

```text
朋友推荐我到诚品生活松烟店找这本书。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | social_daily | over_conversion_guard | high | - |

Codex reason: 完整的日常敘述；品牌、人名、書名或識別碼必須保持不變。

Gemini reason: 專有名稱「诚品生活松烟店」，需正確轉換為「誠品生活松菸店」。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`

### 51. zhtw-project-it-llm-social-guard-v1/social-015

Changed: `script, risk`

Input:

```text
我把悠游卡设成自动加值，卡号末四码是 2468。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | medium | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整的日常敘述；品牌、人名、書名或識別碼必須保持不變。

Gemini reason: 混合情境，包含臺灣特有詞彙「悠游卡」與簡體字「设」、「码」，測試準確轉換。

Maintainer decision: `synthesis` accepted by `tim` on `2026-07-28`
