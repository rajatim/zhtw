# ZHTW 最終台灣繁體中文轉譯稽核（2026-07-19）

## 結論

- 審查範圍：1,251 筆公開 regression expected、219 筆 holdout promotion cases、132 筆 acceptable variants，以及自 `96acdc9` 起 899 個詞條變更。
- 899 個變更 target 全部冪等；加上前後文後，899 個 source mapping 皆維持預期輸出，未發現新增詞條造成的上下文偏移。
- 找到 3 個明確的既有繁體誤轉風險：`租用戶 -> 租使用者`、`命名空間 -> 名稱空間`、`熱重載 -> 熱過載`。官方台灣文件核對後，建議保護「租用戶、命名空間」，並將「熱重載」明確轉為「熱重新載入」。
- 公開 regression 中有 13 筆舊 expected 值值得修正；acceptable variants 中有一批中國慣用詞應移除。
- 本文件是 Codex 第一輪與 Gemini advisory 的彙整，不是 human ground truth。maintainer 確認後才能更新 expected/acceptable。

## Maintainer 決策與實作

- Maintainer `tim` 已於 2026-07-19 回覆 `review OK`，本報告建議正式成為 human decision。
- 已修正 13 筆 regression expected，並移除 25 個 case 中共 29 筆過時 acceptable variants。
- 已加入「租用戶／命名空間」identity guard，並將「熱重載」明確轉為「熱重新載入」。
- 已同步 annotation backlog、holdout candidates、public regression、外部 corpus expected、precision fixture 與所有 SDK data export。

## 公開 Expected 建議

| ID | 現值 | Codex 建議 | Gemini |
|---|---|---|---|
| `social/social_033` | 這家店支持電子付款。 | 這家店支援電子付款。 | 未提出 |
| `social/social_034` | 默認鈴聲聽起來很普通。 | 預設鈴聲聽起來很普通。 | 未提出 |
| `social/social_036` | 照片質量比昨天好很多。 | 照片品質比昨天好很多。 | 未提出 |
| `social/social_053` | 今天空氣質量不太好。 | 今天空氣品質不太好。 | 未提出 |
| `regressions/regression_020` | 背景程式裡的日誌文件 | 背景程式裡的記錄檔 | 未提出 |
| `tech/tech_066` | 後端服務寫入日誌文件。 | 後端服務寫入記錄檔。 | 未提出 |
| `tech/tech_010` | 日誌文件記錄錯誤資訊。 | 記錄檔記錄錯誤資訊。 | 未提出 |
| `tech/tech_034` | 用戶端會保存會話權杖。 | 用戶端會儲存工作階段權杖。 | 未提出 |
| `tech/tech_037` | 命令列參數支持短選項。 | 命令列參數支援短選項。 | 未提出 |
| `tech/tech_048` | 應用程式啟動後會讀取配置。 | 應用程式啟動後會讀取設定。 | 同意 |
| `annotation/it-api-cli-0038` | 預設配置會啟用壓縮回應。 | 預設設定會啟用壓縮回應。 | 同意 |
| `tech/tech_017` | 資料庫遷移指令碼失敗了。 | 資料庫移轉指令碼失敗了。 | 同意 |
| `holdout/blind-it-0057` | 這個儲存庫同時保存英文和台灣繁體 README。 | 這個儲存庫同時保留英文和台灣繁體 README。 | 未提出 |

## Acceptable 建議移除

以下只移除列出的 acceptable，不改 primary expected：

| ID | 應移除的關鍵用語 | 理由 |
|---|---|---|
| `blind-it-0088`、`blind-formal-0084` | 發佈 | 台灣正式用字為「發布」；軟體 release 亦可用「釋出」 |
| `blind-it-0113`、`blind-it-0171`、`blind-it-0217` | 技術語境的簽名 | request/access signature 應為「簽章」 |
| `blind-it-0117`、`blind-it-0156`、`blind-it-0169` | 遷移 | 專案標準為「移轉」 |
| `blind-it-0126` | 設置 | 台灣慣用「設定」 |
| `blind-it-0140` | 中間件 | 台灣慣用「中介軟體」 |
| `blind-it-0142` | 設定映射 | 專案標準為「設定對應」；`ConfigMap` 版本另行保留 |
| `blind-it-0151` | 流水線、依賴套件 | 台灣慣用「管線、相依套件」 |
| `blind-it-0165`、`blind-it-0210`、`blind-it-0230` | 配置 | 依語境改為「設定／設定檔」 |
| `blind-it-0173` | 包管理器 | 台灣慣用「套件管理員」 |
| `blind-it-0190` | 優先級 | 台灣慣用「優先順序」 |
| `blind-it-0209` | 插件 | 台灣慣用「外掛程式」 |
| `blind-it-0217`、`blind-llm-0166` | 生成 | 台灣慣用「產生」 |
| `blind-it-0237` | 超時 | 台灣慣用「逾時」 |
| `blind-ui-0170` | 拖拽 | 台灣慣用「拖曳」 |
| `blind-ui-0181` | UI 語境的導航 | 台灣 UI 慣用「導覽」 |
| `blind-it-0269` | IT 儲存語境的保存 | 應為「儲存」 |
| `blind-llm-0158` | 本地化 | 專案標準為「在地化」 |

## 需 Maintainer 決定

1. **租用戶**：Gemini 認為應一律改為「租戶」，但 [Microsoft Entra 台灣文件](https://learn.microsoft.com/zh-tw/entra/fundamentals/how-subscriptions-associated-directory) 明確且反覆使用「租用戶」。Codex 建議保留 acceptable 並加入 identity guard；`租用戶 -> 租使用者` 是錯誤輸出。
2. **熱重載**：[Microsoft Visual Studio 台灣文件](https://learn.microsoft.com/zh-tw/visualstudio/debugger/hot-reload?view=visualstudio) 的正式術語是「熱重新載入」。Codex 採納官方證據與 Gemini 建議：移除「熱重載」acceptable，並將 `熱重載` 明確轉成「熱重新載入」，不可轉為「熱過載」。
3. **命名空間**：[Azure AKS](https://learn.microsoft.com/zh-tw/azure/aks/concepts-managed-namespaces) 與 [Google Cloud GKE 台灣文件](https://docs.cloud.google.com/kubernetes-engine/docs/learn/get-started-with-kubernetes?hl=zh-TW) 均使用「命名空間」。Codex 與 Gemini 一致建議加入 identity guard；`ConfigMap` acceptable 可保留，「設定映射」acceptable 建議移除。
4. **回滾／復原**：Codex 初判偏好「復原」，但 [Microsoft Fabric 台灣文件](https://learn.microsoft.com/zh-tw/fabric/data-warehouse/transactions) 與 [SQL Server 台灣文件](https://learn.microsoft.com/zh-tw/sql/t-sql/language-elements/rollback-transaction-transact-sql?view=sql-server-ver17) 均使用「回滾交易」，並以「復原／回復」描述結果。Codex 採納官方證據與 Gemini 建議：保留 `資料庫交易需要回滾。`，不修改 expected。
5. **發送**：Codex 認為「發送通知／發送功能開關」在台灣仍可理解且不構成語意錯誤，建議保留 acceptable；Gemini未提出異議。此項不建議為了統一而過度刪除。
6. **實例、平台、計劃**：雖非專案 preferred，但在台灣文本中仍可見且語意可成立，Codex 建議保留 acceptable，避免把風格偏好當成錯誤。

## Sealed Miss 分類

`955/1008` 的 53 筆 miss 分為：

- 33 筆 `over_conversion_guard`：其中 23 筆是題目要求保留 `台` 字面的 metalinguistic/proper-name 案例，另外 10 筆是既有繁體詞或受保護字面範圍的語境判斷。
- 17 筆 `candidate_gap`：混合真正術語缺口、句法潤飾，以及 expected 本身可爭議的案例，不可整批加入詞庫。
- 3 筆 `baseline_guard`：屬 `代碼／程式碼`、`文件／檔案`、`只／僅` 等依語境判斷。

結論：53 筆 miss 不應直接用來調參。sealed benchmark 保持評估用途，避免洩漏式最佳化。

## Advisory 狀態

- Codex：完成全部候選初審、冪等與上下文壓力測試。
- Gemini CLI：使用 `gemini-2.5-pro` 完成獨立候選審查；其建議僅作 advisory。
- Human：maintainer `tim` 已於 2026-07-19 確認 `review OK`。

## 最終驗證

- Focused accuracy tests：2,659 passed。
- Full Python tests：4,957 passed。
- Java `mvn verify`：99 passed。
- `zhtw validate`：通過，無詞彙衝突。
- SDK `export-check`：通過。
- Mono-version `version-check`：8 個版本位置均為 `4.4.1`。
- Sealed benchmark：955/1,008 accepted，94.74%；與修正前相同，無 accepted regression。
