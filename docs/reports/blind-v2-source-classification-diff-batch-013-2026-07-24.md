<!-- zhtw:disable -->
# Blind-v2 Source Classification Diff 013 (2026-07-24)

Status: advisory only; maintainer decisions pending

Packet SHA-256: `42467a73426931d5153f555036d323fae3af302d7c45a8e4043939e19ba45957`
Cases: 100
Exact Codex/Gemini classifications: 57
Maintainer review queue: 43

Field differences:

- Eligibility: 0
- Script: 0
- Domain: 11
- Risk: 35

## Policy Finding

Gemini reported no eligibility/quality-policy conflicts; its validation also recorded zero tool calls and zero API errors.

Neither advisory is auto-preferred. Codex must synthesize the differences before maintainer confirmation; no classification in this report has been written into the candidate pool.

## Review Queue

### 01. zhtw-project-formal-llm-semantic-v1/formal-003

Changed: `risk`

Input:

```text
委员会通过决议前，应先确认出席人数达到法定门槛。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 法定表決程序完整且需保留通過語義。

Gemini reason: 一般門檻轉寫，無特殊歧義

Maintainer decision: `pending`

### 02. zhtw-project-formal-llm-semantic-v1/formal-005

Changed: `domain`

Input:

```text
公司计划发行公司债，以筹措长期建设所需资金。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 金融發行語境完整，不得誤作一般發布。

Gemini reason: 金融發行語境，防誤改發布

Maintainer decision: `pending`

### 03. zhtw-project-formal-llm-semantic-v1/formal-006

Changed: `domain`

Input:

```text
中央银行将发行纪念币，但不会改变现行货币政策。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 貨幣發行屬金融高風險語境。

Gemini reason: 貨幣發行語境，防誤改發布

Maintainer decision: `pending`

### 04. zhtw-project-formal-llm-semantic-v1/formal-008

Changed: `risk`

Input:

```text
主管机关发布调查报告时，应同时公开统计方法。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 機關發布報告屬正式文字。

Gemini reason: 政府發布報告，標準用語

Maintainer decision: `pending`

### 05. zhtw-project-formal-llm-semantic-v1/formal-009

Changed: `risk`

Input:

```text
市政府发布最新人口统计，并说明资料修订原因。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 政府發布統計的正式語境完整。

Gemini reason: 發布統計資料，標準用語

Maintainer decision: `pending`

### 06. zhtw-project-formal-llm-semantic-v1/formal-013

Changed: `domain`

Input:

```text
研究对象均已签署同意书，并可随时退出研究。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 人體研究同意與研究對象屬高風險語境。

Gemini reason: 研究對象語境，防誤轉物件

Maintainer decision: `pending`

### 07. zhtw-project-formal-llm-semantic-v1/formal-014

Changed: `domain`

Input:

```text
本项服务的对象包括独居长者与行动不便者。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 社福服務對象語境完整。

Gemini reason: 服務對象語境，防誤轉物件

Maintainer decision: `pending`

### 08. zhtw-project-formal-llm-semantic-v1/formal-015

Changed: `domain`

Input:

```text
多数委员支持这项提案，但要求补充财政影响评估。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 正式審議中的支持語義清楚。

Gemini reason: 支持提案語境，防誤改支援

Maintainer decision: `pending`

### 09. zhtw-project-formal-llm-semantic-v1/formal-018

Changed: `domain`

Input:

```text
承办机关应确实执行决议，不得自行增加限制条件。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 機關執行決議的正式語境完整。

Gemini reason: 行政執行決議，防過度轉換

Maintainer decision: `pending`

### 10. zhtw-project-formal-llm-semantic-v1/formal-026

Changed: `risk`

Input:

```text
主管机关不得以注销账号代替注销公司登记。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | medium | - |
| Gemini | yes | high_stakes | candidate_gap | high | - |

Codex reason: 帳號與公司註銷的對照完整，但帳號動作仍需語境判斷。

Gemini reason: 含帳號詞彙，需台化轉換

Maintainer decision: `pending`

### 11. zhtw-project-formal-llm-semantic-v1/formal-027

Changed: `risk`

Input:

```text
这项研究应用既有理论解释新发现，没有改变原始定义。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 應用理論不是應用程式。

Gemini reason: 學術定義語境，標準轉換

Maintainer decision: `pending`

### 12. zhtw-project-formal-llm-semantic-v1/formal-029

Changed: `domain, risk`

Input:

```text
偏远地区需要长期医疗支持，不能只依赖短期巡回服务。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 偏遠醫療支持屬高風險公共服務語境。

Gemini reason: 醫療支援服務，標準轉換

Maintainer decision: `pending`

### 13. zhtw-project-formal-llm-semantic-v1/formal-032

Changed: `risk`

Input:

```text
比赛项目分为个人组与团体组，计分方式各不相同。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 項目為比賽項目，不是專案。

Gemini reason: 體育賽事分組，標準轉換

Maintainer decision: `pending`

### 14. zhtw-project-formal-llm-semantic-v1/formal-035

Changed: `domain, risk`

Input:

```text
服务对象的需求不同，补助标准不宜一律相同。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 補助與服務對象屬高風險公共政策語境。

Gemini reason: 社會補助標準，標準轉換

Maintainer decision: `pending`

### 15. zhtw-project-formal-llm-semantic-v1/formal-036

Changed: `risk`

Input:

```text
电视节目将完整播出访谈，不剪除受访者的重要说明。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | formal_news | baseline_guard | high | - |

Codex reason: 節目為電視內容，不是軟體程式。

Gemini reason: 媒體訪談節目，標準轉換

Maintainer decision: `pending`

### 16. zhtw-project-formal-llm-semantic-v1/formal-038

Changed: `domain`

Input:

```text
港口发现受损容器后，立即划设安全区域。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | high_stakes | over_conversion_guard | high | - |
| Gemini | yes | formal_news | over_conversion_guard | high | - |

Codex reason: 港口受損容器涉及現場安全。

Gemini reason: 港口受損容器，防誤改軟體容器

Maintainer decision: `pending`

### 17. zhtw-project-formal-llm-semantic-v1/formal-040

Changed: `domain`

Input:

```text
地方分支机构可以受理申请，但无权变更审查标准。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | over_conversion_guard | high | - |
| Gemini | yes | high_stakes | over_conversion_guard | high | - |

Codex reason: 分支為組織分支，語義完整。

Gemini reason: 地方分支機構，防誤改程式分支

Maintainer decision: `pending`

### 18. zhtw-project-formal-llm-semantic-v1/formal-047

Changed: `domain, risk`

Input:

```text
审议结果返回委员会后，还需安排第二次表决。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | formal_news | candidate_gap | high | - |
| Gemini | yes | high_stakes | baseline_guard | high | - |

Codex reason: 正式審議語境中的返回較可能需要在地化為退回。

Gemini reason: 委員會審議流程，標準轉換

Maintainer decision: `pending`

### 19. zhtw-project-formal-llm-semantic-v1/llm-009

Changed: `risk`

Input:

```text
餐厅菜单与软件导航菜单可能需要不同的本地化处理。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 餐廳與軟體選單語境對照。

Gemini reason: 菜單與選單本地化提示

Maintainer decision: `pending`

### 20. zhtw-project-formal-llm-semantic-v1/llm-011

Changed: `risk`

Input:

```text
地址可能指邮寄地点，也可能出现在网络配置说明中。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 郵寄地址與網路位址語境對照。

Gemini reason: 地址與位址語境辨識

Maintainer decision: `pending`

### 21. zhtw-project-formal-llm-semantic-v1/llm-012

Changed: `risk`

Input:

```text
远程山区与远程连接的语境不同，摘要时应保留原意。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 偏遠地區與遠端連線語境對照。

Gemini reason: 遠程與遠端語境區分

Maintainer decision: `pending`

### 22. zhtw-project-formal-llm-semantic-v1/llm-015

Changed: `risk`

Input:

```text
行政事务与数据库事务不能因为写法相同就视为同一概念。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 行政事務與資料庫交易語境對照。

Gemini reason: 行政事務與資料庫交易區分

Maintainer decision: `pending`

### 23. zhtw-project-formal-llm-semantic-v1/llm-016

Changed: `risk`

Input:

```text
教材中的实例是说明案例，云端文件中的实例则可能指运算资源。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 案例與雲端執行個體語境對照。

Gemini reason: 說明實例與雲端執行個體區分

Maintainer decision: `pending`

### 24. zhtw-project-formal-llm-semantic-v1/llm-021

Changed: `risk`

Input:

```text
港口新闻中的端口可能只是原文误用，模型应先确认语境。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | medium | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 港口與技術端口對照完整，但句中也要求先確認原文語境。

Gemini reason: 海港港口與網路連接埠區分

Maintainer decision: `pending`

### 25. zhtw-project-formal-llm-semantic-v1/llm-024

Changed: `risk`

Input:

```text
公共图书馆与软件程序库都可能被简称为库，回答应避免歧义。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 圖書館與程式庫語境對照。

Gemini reason: 圖書館與程式庫之簡稱歧義

Maintainer decision: `pending`

### 26. zhtw-project-formal-llm-semantic-v1/llm-025

Changed: `risk`

Input:

```text
快递包裹与软件包属于不同领域，翻译时不能只看单字。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 包裹與軟體套件語境對照。

Gemini reason: 快遞包裹與軟體套件區分

Maintainer decision: `pending`

### 27. zhtw-project-formal-llm-semantic-v1/llm-026

Changed: `risk`

Input:

```text
产品类别与程序设计类都涉及分类，但术语用法并不完全相同。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 產品類別與程式類別語境對照。

Gemini reason: 產品類別與程式類別區分

Maintainer decision: `pending`

### 28. zhtw-project-formal-llm-semantic-v1/llm-027

Changed: `risk`

Input:

```text
原文中的同一个词可能指农田，也可能指资料字段，模型应参考整句。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 農田與資料欄位語境對照。

Gemini reason: 農田與資料欄位多義字區分

Maintainer decision: `pending`

### 29. zhtw-project-formal-llm-semantic-v1/llm-028

Changed: `risk`

Input:

```text
数学函数与程序函数应分别采用所属领域的惯用名称。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 數學函數與程式函式語境對照。

Gemini reason: 數學函數與程式函式名稱區分

Maintainer decision: `pending`

### 30. zhtw-project-formal-llm-semantic-v1/llm-029

Changed: `risk`

Input:

```text
数学变量与模板变量可以同名，但不得擅自修改变量内容。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 數學與模板變數語境對照。

Gemini reason: 數學與模板變數保護說明

Maintainer decision: `pending`

### 31. zhtw-project-formal-llm-semantic-v1/llm-032

Changed: `risk`

Input:

```text
经济恢复与备份恢复的对象不同，摘要不能省略关键名词。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 經濟恢復與備份還原語境對照。

Gemini reason: 經濟復甦與備份還原區分

Maintainer decision: `pending`

### 32. zhtw-project-formal-llm-semantic-v1/llm-033

Changed: `risk`

Input:

```text
应用科学理论与开启移动应用程序属于不同动作。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 理論應用與應用程式語境對照。

Gemini reason: 應用理論與開啟應用程式區分

Maintainer decision: `pending`

### 33. zhtw-project-formal-llm-semantic-v1/llm-034

Changed: `risk`

Input:

```text
扩展保护范围与安装浏览器扩展功能不可混写。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 範圍擴展與瀏覽器擴充功能語境對照。

Gemini reason: 擴展範圍與擴充功能區分

Maintainer decision: `pending`

### 34. zhtw-project-formal-llm-semantic-v1/llm-035

Changed: `risk`

Input:

```text
装载货物与加载网页虽然都涉及载入，但语境不同。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 貨物裝載與網頁載入語境對照。

Gemini reason: 裝載貨物與載入網頁區分

Maintainer decision: `pending`

### 35. zhtw-project-formal-llm-semantic-v1/llm-036

Changed: `risk`

Input:

```text
链条的连接处与网页链接不一定采用相同表达。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 實體連接處與網頁連結語境對照。

Gemini reason: 實體連接與網頁連結區分

Maintainer decision: `pending`

### 36. zhtw-project-formal-llm-semantic-v1/llm-037

Changed: `risk`

Input:

```text
商品标签与界面分页标签应根据实际功能分别描述。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 商品標籤與介面分頁標籤語境對照。

Gemini reason: 商品標籤與分頁標籤區分

Maintainer decision: `pending`

### 37. zhtw-project-formal-llm-semantic-v1/llm-041

Changed: `risk`

Input:

```text
舞台表现与系统性能都可评价好坏，但指标并不相同。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 舞台表現與系統效能語境對照。

Gemini reason: 舞台表現與系統效能區分

Maintainer decision: `pending`

### 38. zhtw-project-formal-llm-semantic-v1/llm-042

Changed: `risk`

Input:

```text
记者回应与接口响应的主体不同，生成摘要时应清楚标示。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 記者回應與介面回應語境對照。

Gemini reason: 記者回應與介面回應區分

Maintainer decision: `pending`

### 39. zhtw-project-formal-llm-semantic-v1/llm-044

Changed: `risk`

Input:

```text
统计指标与监控指标可以共用名称，但计算方式必须分开说明。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 統計與監控指標語境對照。

Gemini reason: 統計與監控指標區分說明

Maintainer decision: `pending`

### 40. zhtw-project-formal-llm-semantic-v1/llm-045

Changed: `risk`

Input:

```text
追踪包裹与分布式追踪使用不同技术，不应共用操作步骤。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 包裹追蹤與分散式追蹤語境對照。

Gemini reason: 包裹追蹤與分散式追蹤區分

Maintainer decision: `pending`

### 41. zhtw-project-formal-llm-semantic-v1/llm-046

Changed: `risk`

Input:

```text
人的记忆与计算机内存不是同一个概念，类比时要注明限制。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | candidate_gap | high | - |

Codex reason: 人類記憶與電腦記憶體語境對照。

Gemini reason: 人類記憶與電腦記憶體區分

Maintainer decision: `pending`

### 42. zhtw-project-formal-llm-semantic-v1/llm-049

Changed: `risk`

Input:

```text
一句话同时出现多个可能含义时，模型应指出歧义而不是猜测。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 歧義偵測與避免猜測的 LLM 情境。

Gemini reason: 多義句歧義指出指示

Maintainer decision: `pending`

### 43. zhtw-project-formal-llm-semantic-v1/llm-050

Changed: `risk`

Input:

```text
上下文不足以判断术语含义时，应请求补充信息再继续处理。
```

| Reviewer | Eligible | Domain | Risk | Confidence | Quality |
|----------|----------|--------|------|------------|---------|
| Codex | yes | llm_generated | over_conversion_guard | high | - |
| Gemini | yes | llm_generated | baseline_guard | high | - |

Codex reason: 上下文不足時要求澄清，屬語義防護。

Gemini reason: 語境不足時請求補充指示

Maintainer decision: `pending`
