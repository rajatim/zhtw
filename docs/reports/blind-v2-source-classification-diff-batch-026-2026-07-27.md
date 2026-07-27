<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 026 (2026-07-27)

Status: advisory only; maintainer decisions pending

Packet SHA-256: `c08c3e7d39d16a58c51941eb15b98eadfc0335610510b620a5e55b2fc681b302`
Cases: 80
Exact Codex/Gemini classifications: 12
Maintainer review queue: 68

Field differences:

- Eligibility: 0
- Script: 0
- Domain: 24
- Risk: 64

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

Neither advisory is auto-preferred. Codex must synthesize the differences before maintainer confirmation; no classification in this report has been written into the candidate pool.

## Review Queue

### 01. zhtw-project-competitor-risk-taxonomy-v1/boundary-001

Changed: `risk`

Input:

```text
负责守夜的士兵每两小时更换一次岗位。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試常用詞「負責」、「士兵」、「更換」、「崗位」的基本轉換。

Maintainer decision: `pending`

### 02. zhtw-project-competitor-risk-taxonomy-v1/boundary-002

Changed: `risk`

Input:

```text
参加典礼的士官都穿着正式制服。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試常用詞「典禮」、「士官」、「穿著」、「制服」的轉換。

Maintainer decision: `pending`

### 03. zhtw-project-competitor-risk-taxonomy-v1/boundary-004

Changed: `domain`

Input:

```text
那只装有样品的箱子必须保持密封。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試「那只装有」，此處「只」為量詞，應轉換為「隻」。

Maintainer decision: `pending`

### 04. zhtw-project-competitor-risk-taxonomy-v1/boundary-005

Changed: `domain, risk`

Input:

```text
一个中型团队通常需要明确的分工。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試中國用語「团队」(團隊)的轉換。

Maintainer decision: `pending`

### 05. zhtw-project-competitor-risk-taxonomy-v1/boundary-006

Changed: `domain, risk`

Input:

```text
每一个中文字段都要经过编码检查。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 IT 術語「字段」(欄位)和「编码」(編碼)。

Maintainer decision: `pending`

### 06. zhtw-project-competitor-risk-taxonomy-v1/boundary-007

Changed: `risk`

Input:

```text
系统将字节长度写入消息标头。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 IT 術語「字节」(位元組)和「消息标头」(訊息標頭)。

Maintainer decision: `pending`

### 07. zhtw-project-competitor-risk-taxonomy-v1/boundary-008

Changed: `risk`

Input:

```text
这家公司的字节流处理模块正在更新。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 IT 術語「字节流」(位元組流)和「模块」(模組)。

Maintainer decision: `pending`

### 08. zhtw-project-competitor-risk-taxonomy-v1/boundary-009

Changed: `risk`

Input:

```text
线程名称包含产品代号时不得拆开改写。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 IT 術語「线程」(執行緒)和「产品」(產品)。

Maintainer decision: `pending`

### 09. zhtw-project-competitor-risk-taxonomy-v1/boundary-010

Changed: `domain, risk`

Input:

```text
开发人员在线程结束后释放暂存资源。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 IT 術語「开发人员」(開發人員)、「线程」(執行緒)、「暂存」(暫存)。

Maintainer decision: `pending`

### 10. zhtw-project-competitor-risk-taxonomy-v1/entity-001

Changed: `risk`

Input:

```text
黄河科技学院公布了今年的招生简章。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試專有名詞「黄河科技学院」應不轉換，而「公布」、「简章」應轉換。

Maintainer decision: `pending`

### 11. zhtw-project-competitor-risk-taxonomy-v1/entity-002

Changed: `risk`

Input:

```text
白云山制药厂更新了产品包装。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試專有名詞「白云山制药厂」，應不轉換或部分轉換，同時測試「产品包装」的轉換。

Maintainer decision: `pending`

### 12. zhtw-project-competitor-risk-taxonomy-v1/entity-006

Changed: `risk`

Input:

```text
范家村保存着一座清代石桥。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試地名「范家村」不轉換，而「保存」、「清代」應轉換。

Maintainer decision: `pending`

### 13. zhtw-project-competitor-risk-taxonomy-v1/entity-007

Changed: `domain, risk`

Input:

```text
项目名称 Project Cedar 必须保留原始拼写。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試包含英文的句子，英文部分「Project Cedar」應保持不變。

Maintainer decision: `pending`

### 14. zhtw-project-competitor-risk-taxonomy-v1/entity-008

Changed: `risk`

Input:

```text
报告引用 Côte d’Ivoire 的官方英文名称。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試包含非 ASCII 字符的外文「Côte d’Ivoire」應保持不變。

Maintainer decision: `pending`

### 15. zhtw-project-competitor-risk-taxonomy-v1/entity-009

Changed: `domain, risk`

Input:

```text
设备型号 ThinkPad T14s 不应拆分翻译。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試包含字母和數字的型號「ThinkPad T14s」應保持不變。

Maintainer decision: `pending`

### 16. zhtw-project-competitor-risk-taxonomy-v1/entity-010

Changed: `risk`

Input:

```text
登记姓名 Chen Yu-Han 必须与护照一致。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試羅馬拼音人名「Chen Yu-Han」應保持不變。

Maintainer decision: `pending`

### 17. zhtw-project-competitor-risk-taxonomy-v1/formal-001

Changed: `risk`

Input:

```text
主管机关设置临时服务站协助民众申请。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試正式用語「主管机关」(主管機關)、「设置」(設置/設定)、「服务站」(服務站)。

Maintainer decision: `pending`

### 18. zhtw-project-competitor-risk-taxonomy-v1/formal-002

Changed: `domain, risk`

Input:

```text
系统设置会同步到使用同一账号的设备。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 IT/UI 詞彙「系统设置」(系統設定)、「账号」(帳號)、「设备」(裝置/設備)。

Maintainer decision: `pending`

### 19. zhtw-project-competitor-risk-taxonomy-v1/formal-003

Changed: `risk`

Input:

```text
高级中学应在期限内完成消防设备检查。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試詞彙「高级中学」(高級中學)、「设备」(設備)的轉換。

Maintainer decision: `pending`

### 20. zhtw-project-competitor-risk-taxonomy-v1/formal-004

Changed: `domain, risk`

Input:

```text
进阶课程将介绍高阶函数的实际应用。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 IT 術語「进阶」(進階)和「高阶函数」(高階函式)。

Maintainer decision: `pending`

### 21. zhtw-project-competitor-risk-taxonomy-v1/formal-005

Changed: `risk`

Input:

```text
财政支持方案须经议会审议通过。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試政治用語「财政」(財政)、「议会」(議會)、「审议」(審議)。

Maintainer decision: `pending`

### 22. zhtw-project-competitor-risk-taxonomy-v1/formal-006

Changed: `domain, risk`

Input:

```text
技术支持人员会远程检查错误记录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 IT 用語「技术支持」(技術支援)、「远程」(遠端)。

Maintainer decision: `pending`

### 23. zhtw-project-competitor-risk-taxonomy-v1/formal-007

Changed: `risk`

Input:

```text
住宅社区附近不得堆放危险化学品。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試中國用語「社区」(社區)的轉換。

Maintainer decision: `pending`

### 24. zhtw-project-competitor-risk-taxonomy-v1/formal-008

Changed: `domain, risk`

Input:

```text
开源社群将在周末举行线上交流活动。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 IT 用語「开源社群」(開源社群)、「线上」(線上)。

Maintainer decision: `pending`

### 25. zhtw-project-competitor-risk-taxonomy-v1/formal-009

Changed: `risk`

Input:

```text
统计资料应说明数据来源与计算方法。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試中國用語「数据」(數據)。

Maintainer decision: `pending`

### 26. zhtw-project-competitor-risk-taxonomy-v1/formal-010

Changed: `domain, risk`

Input:

```text
个人资料仅能用于申请人同意的目的。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試涉及隱私的常用詞「个人资料」(個人資料)。

Maintainer decision: `pending`

### 27. zhtw-project-competitor-risk-taxonomy-v1/glyph-001

Changed: `risk`

Input:

```text
会议结束后，工作人员从后门搬出器材。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試基本字形轉換：「后门」(後門)、「会议」(會議)。

Maintainer decision: `pending`

### 28. zhtw-project-competitor-risk-taxonomy-v1/glyph-004

Changed: `domain`

Input:

```text
施工单位正在干燥的河床附近架设围栏。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試詞彙「干燥」(乾燥)中「干」的正確轉換。

Maintainer decision: `pending`

### 29. zhtw-project-competitor-risk-taxonomy-v1/glyph-006

Changed: `domain, risk`

Input:

```text
请把会议摘要放在附件里面。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試「里面」(裡面)中「里」的正確轉換。

Maintainer decision: `pending`

### 30. zhtw-project-competitor-risk-taxonomy-v1/glyph-007

Changed: `domain`

Input:

```text
山谷里的居民接到大雨警报后立即撤离。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試「山谷里」(山谷裡)，並確保「谷」字不被誤轉為「穀」。

Maintainer decision: `pending`

### 31. zhtw-project-competitor-risk-taxonomy-v1/glyph-009

Changed: `domain, risk`

Input:

```text
校方公布历年报名人数与录取比例。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試基本字形轉換：「公布」(公佈)、「历年」(歷年)。

Maintainer decision: `pending`

### 32. zhtw-project-competitor-risk-taxonomy-v1/glyph-010

Changed: `domain`

Input:

```text
钟表修复完成后仍需观察一天。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試字形轉換：「钟表」(鐘錶)、「后」(後)。

Maintainer decision: `pending`

### 33. zhtw-project-competitor-risk-taxonomy-v1/it-001

Changed: `risk`

Input:

```text
后台进程会定期清理已经过期的缓存文件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 IT 術語「后台进程」(背景行程)和「缓存」(快取)。

Maintainer decision: `pending`

### 34. zhtw-project-competitor-risk-taxonomy-v1/it-002

Changed: `risk`

Input:

```text
申请流程进入审核阶段后不能更换负责人。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試常用詞「流程」、「审核」(審核)、「更换」(更換)。

Maintainer decision: `pending`

### 35. zhtw-project-competitor-risk-taxonomy-v1/it-003

Changed: `risk`

Input:

```text
容器启动失败时，请先检查环境变量。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 IT 術語「容器」、「启动」(啟動)、「环境变量」(環境變數)。

Maintainer decision: `pending`

### 36. zhtw-project-competitor-risk-taxonomy-v1/it-004

Changed: `risk`

Input:

```text
运输容器抵达仓库后必须核对封条编号。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試「容器」在非 IT 情境（貨運）下的轉換。

Maintainer decision: `pending`

### 37. zhtw-project-competitor-risk-taxonomy-v1/it-005

Changed: `risk`

Input:

```text
接口返回 HTTP 409 表示资源发生冲突。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 IT 術語「接口」(介面)和「返回」(回傳)。

Maintainer decision: `pending`

### 38. zhtw-project-competitor-risk-taxonomy-v1/it-006

Changed: `risk`

Input:

```text
服务窗口将在中午暂停受理现场申请。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試「服务窗口」在非 IT 情境（臨櫃）下的轉換。

Maintainer decision: `pending`

### 39. zhtw-project-competitor-risk-taxonomy-v1/it-007

Changed: `risk`

Input:

```text
数据库连接池达到上限时会拒绝新的请求。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 IT 術語「数据库连接池」(資料庫連線池)。

Maintainer decision: `pending`

### 40. zhtw-project-competitor-risk-taxonomy-v1/it-008

Changed: `risk`

Input:

```text
游泳池完成消毒后才会重新开放。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試「池」在非 IT 情境（游泳池）下的轉換。

Maintainer decision: `pending`

### 41. zhtw-project-competitor-risk-taxonomy-v1/it-009

Changed: `risk`

Input:

```text
脚本只读取 config.yaml 中指定的字段。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 IT 術語「脚本」(腳本)和「字段」(欄位)。

Maintainer decision: `pending`

### 42. zhtw-project-competitor-risk-taxonomy-v1/it-010

Changed: `risk`

Input:

```text
演员按照修改后的脚本重新排练最后一幕。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試「脚本」(腳本)在非 IT 情境（劇本）下的轉換。

Maintainer decision: `pending`

### 43. zhtw-project-competitor-risk-taxonomy-v1/semantic-001

Changed: `risk`

Input:

```text
法院要求当事人依照法定程序提出书面答辩。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試法律用語「当事人」、「程序」、「书面」、「答辩」的轉換。

Maintainer decision: `pending`

### 44. zhtw-project-competitor-risk-taxonomy-v1/semantic-002

Changed: `domain, risk`

Input:

```text
安装程序会在完成检查后自动关闭。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 IT 術語「安装程序」(安裝程式)。

Maintainer decision: `pending`

### 45. zhtw-project-competitor-risk-taxonomy-v1/semantic-003

Changed: `risk`

Input:

```text
这份文件记录了委员会讨论预算的完整过程。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試常用詞「文件」(檔案/文件)和「过程」(過程)。

Maintainer decision: `pending`

### 46. zhtw-project-competitor-risk-taxonomy-v1/semantic-004

Changed: `domain, risk`

Input:

```text
请把下载的文件移动到指定目录。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 IT 術語「文件」(檔案)和「目录」(目錄)。

Maintainer decision: `pending`

### 47. zhtw-project-competitor-risk-taxonomy-v1/semantic-005

Changed: `domain, risk`

Input:

```text
研究人员根据实验数据调整统计模型。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試術語「数据」(數據)和「模型」(模型)。

Maintainer decision: `pending`

### 48. zhtw-project-competitor-risk-taxonomy-v1/semantic-006

Changed: `risk`

Input:

```text
报名资料不完整时，主办单位会通知补件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 「补件」是台灣常用詞，測試「资料」(資料)的轉換。

Maintainer decision: `pending`

### 49. zhtw-project-competitor-risk-taxonomy-v1/semantic-007

Changed: `risk`

Input:

```text
居民支持在社区增设一处公共托儿设施。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試詞彙「社区」(社區)和「托儿」(托兒)。

Maintainer decision: `pending`

### 50. zhtw-project-competitor-risk-taxonomy-v1/semantic-008

Changed: `domain, risk`

Input:

```text
旧版浏览器不支持这项加密功能。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | it_api_cli | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 IT 術語「旧版」(舊版)、「浏览器」(瀏覽器)、「支持」(支援)。

Maintainer decision: `pending`

### 51. zhtw-project-competitor-risk-taxonomy-v1/semantic-009

Changed: `risk`

Input:

```text
列车运行期间请勿靠近车门。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試常用詞「列车」(列車)、「运行」(運行)、「期间」(期間)。

Maintainer decision: `pending`

### 52. zhtw-project-competitor-risk-taxonomy-v1/semantic-010

Changed: `risk`

Input:

```text
执行法院判决时仍应保障当事人的基本权利。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試法律用語「执行」(執行)、「保障」、「当事人」的轉換。

Maintainer decision: `pending`

### 53. zhtw-project-competitor-risk-taxonomy-v1/social-001

Changed: `risk`

Input:

```text
朋友把活动照片传到群组后就去休息了。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試日常用語「群组」(群組)與「后」(後)。

Maintainer decision: `pending`

### 54. zhtw-project-competitor-risk-taxonomy-v1/social-002

Changed: `risk`

Input:

```text
我们改约在车站旁边的室内咖啡店。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試日常用語「室内」(室內)。

Maintainer decision: `pending`

### 55. zhtw-project-competitor-risk-taxonomy-v1/social-007

Changed: `risk`

Input:

```text
大家支持他的决定，但没有替他安排后续行程。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試常用詞「支持」(支持)與「后续」(後續)的轉換。

Maintainer decision: `pending`

### 56. zhtw-project-competitor-risk-taxonomy-v1/social-008

Changed: `risk`

Input:

```text
社区活动结束后，志愿者留下来整理场地。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試常用詞「社区」(社區)、「志愿者」(志工/志願者)。

Maintainer decision: `pending`

### 57. zhtw-project-competitor-risk-taxonomy-v1/social-009

Changed: `risk`

Input:

```text
聊天记录里的链接已经无法打开。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | social_daily | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 IT 用語「链接」(連結)。

Maintainer decision: `pending`

### 58. zhtw-project-competitor-risk-taxonomy-v1/social-010

Changed: `risk`

Input:

```text
她在留言中引用“keep it simple”提醒大家。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | social_daily | over_conversion_guard | high | - |
| Gemini | yes | social_daily | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試包含英文引用的句子，英文部分應保留。

Maintainer decision: `pending`

### 59. zhtw-project-competitor-risk-taxonomy-v1/ui-001

Changed: `risk`

Input:

```text
选择默认值后，表单会自动更新预览内容。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 UI 用語「默认值」(預設值)、「表单」(表單)。

Maintainer decision: `pending`

### 60. zhtw-project-competitor-risk-taxonomy-v1/ui-002

Changed: `risk`

Input:

```text
系统设置页面会显示目前使用的语言。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 UI 用語「系统设置」(系統設定)、「语言」(語言)。

Maintainer decision: `pending`

### 61. zhtw-project-competitor-risk-taxonomy-v1/ui-003

Changed: `risk`

Input:

```text
点击高级选项可以展开更多筛选条件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 UI 用語「高级选项」(進階選項)、「筛选」(篩選)。

Maintainer decision: `pending`

### 62. zhtw-project-competitor-risk-taxonomy-v1/ui-004

Changed: `risk`

Input:

```text
搜索框为空时显示最近使用的关键字。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 UI 用語「搜索框」(搜尋框)、「关键字」(關鍵字)。

Maintainer decision: `pending`

### 63. zhtw-project-competitor-risk-taxonomy-v1/ui-005

Changed: `risk`

Input:

```text
文件上传完成后，进度条会自动消失。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 UI 用語「文件」(檔案)、「进度条」(進度條)。

Maintainer decision: `pending`

### 64. zhtw-project-competitor-risk-taxonomy-v1/ui-006

Changed: `domain, risk`

Input:

```text
关闭通知不会停止后台正在运行的任务。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | it_api_cli | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 IT 用語「后台」(後端/背景)、「运行」(運行)。

Maintainer decision: `pending`

### 65. zhtw-project-competitor-risk-taxonomy-v1/ui-007

Changed: `domain, risk`

Input:

```text
按钮文字为“继续使用当前账号”。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 UI 及帳號安全用語「账号」(帳號)。

Maintainer decision: `pending`

### 66. zhtw-project-competitor-risk-taxonomy-v1/ui-008

Changed: `domain, risk`

Input:

```text
对话框中的取消操作不会删除草稿。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 UI 用語「对话框」(對話方塊)、「草稿」。

Maintainer decision: `pending`

### 67. zhtw-project-competitor-risk-taxonomy-v1/ui-009

Changed: `risk`

Input:

```text
页面重新加载后仍会保留筛选设置。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | ui_i18n | candidate_gap | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試 UI 用語「加载」(載入)、「筛选」(篩選)、「设置」(設定)。

Maintainer decision: `pending`

### 68. zhtw-project-competitor-risk-taxonomy-v1/ui-010

Changed: `domain, risk`

Input:

```text
错误消息下方会显示 request_id。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | ui_i18n | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 完整的 project-original 风险边界句；语境足以独立判断，适合检验过度转换与词组边界。

Gemini reason: 測試高風險情境下的用詞「错误消息」(錯誤訊息)，並確保 request_id 不變。

Maintainer decision: `pending`
