<!-- zhtw:disable -->
# zhtw 競品差異化案例人工審核（2026-07-03）

## 摘要

來源：`docs/reports/competitor-diffs-full-2026-07-03.json`

本次完整掃描 500 筆 corpus，結果為 `all_match = 192`、`zhtw_advantage = 308`、`candidate_gap = 0`、`all_wrong = 0`。以下從 308 筆 `zhtw_advantage` 中抽看 30 筆；所有抽看案例皆為 `zhtw_correct`。

結論：

- 不改詞庫。
- 不新增 competitor-derived 詞條。
- 可把本報告中的案例作為「少錯轉」與「台灣 IT/UI 用語」差異化證據。
- 若之後要擴充 benchmark，優先從 `保護案例` 中挑選已有人類 expected 的 regression。

## 分類統計

| 類型 | 數量 | 說明 |
|------|------|------|
| `保護案例` | 13 | 競品常見過度轉換；適合防回歸 |
| `台灣 IT/UI 用語` | 12 | zhtw 明確比競品更符合台灣技術或介面用語 |
| `台灣通用用語` | 5 | 非 IT，但能展示台灣用語取向 |

## 已審核案例

| # | ID | 類型 | 判斷 | zhtw 優勢 |
|---|----|------|------|-----------|
| 1 | `regressions/regression_045` | 保護案例 | `zhtw_correct` | 「寫程式」與「法律程序」雙語境同句處理正確；OpenCC 把法律程序錯轉成法律程式 |
| 2 | `regressions/regression_044` | 保護案例 | `zhtw_correct` | 正式文件語境保留「文件」；OpenCC 過度轉成「官方檔案」 |
| 3 | `wiki/wiki_060` | 保護案例 | `zhtw_correct` | 「保存歷史文物」保留保存；OpenCC 過度轉成「儲存歷史文物」 |
| 4 | `regressions/regression_036` | 保護案例 | `zhtw_correct` | 「保存文化遺產」保留保存；OpenCC 過度轉成儲存 |
| 5 | `regressions/regression_032` | 保護案例 | `zhtw_correct` | 一般語境「支持決定」保留支持；OpenCC 過度轉成支援 |
| 6 | `news/news_065` | 保護案例 | `zhtw_correct` | 「支持遠端辦公」保留支持；OpenCC 過度轉成支援 |
| 7 | `regressions/regression_034` | 保護案例 | `zhtw_correct` | 結婚對象保留「對象」；OpenCC 過度轉成「物件」 |
| 8 | `social/social_027` | 保護案例 | `zhtw_correct` | 社群語境「我把文件上傳」保留文件；OpenCC 過度轉成檔案 |
| 9 | `regressions/regression_081` | 保護案例 | `zhtw_correct` | 同句分辨「登出帳戶」與「註銷公司」；兩個競品都混淆其中一邊 |
| 10 | `regressions/regression_051` | 保護案例 | `zhtw_correct` | 「好消息」保留消息；OpenCC 過度轉成訊息 |
| 11 | `tech/tech_010` | 保護案例 | `zhtw_correct` | 「日誌文件」保留文件；OpenCC 過度轉成檔案 |
| 12 | `tech/tech_049` | 保護案例 | `zhtw_correct` | 「透過參數」符合此句 expected；OpenCC 轉成引數，zhconv 保留通過 |
| 13 | `news/news_068` | 保護案例 | `zhtw_correct` | 新聞語境「央行宣布」保留宣布；OpenCC 轉成宣佈 |
| 14 | `tech/tech_004` | 台灣 IT/UI 用語 | `zhtw_correct` | 非同步、回呼、網路三個技術詞同時符合 expected；zhconv 偏中國用語 |
| 15 | `tech/tech_076` | 台灣 IT/UI 用語 | `zhtw_correct` | 伺服器憑證符合台灣技術語境；OpenCC/zhconv 保留證書 |
| 16 | `tech/tech_094` | 台灣 IT/UI 用語 | `zhtw_correct` | 函式庫、函式皆符合台灣程式語境；競品保留庫或函數 |
| 17 | `wiki/wiki_024` | 台灣 IT/UI 用語 | `zhtw_correct` | 網路、協議、設備、通訊皆符合 corpus expected；zhconv 保留網絡/通信 |
| 18 | `tech/tech_081` | 台灣 IT/UI 用語 | `zhtw_correct` | 消息隊列轉為訊息佇列；zhconv 保留消息隊列 |
| 19 | `wiki/wiki_043` | 台灣 IT/UI 用語 | `zhtw_correct` | 雲端運算符合台灣 IT 用語；OpenCC/zhconv 分別輸出雲端計算/雲計算 |
| 20 | `regressions/regression_090` | 台灣 IT/UI 用語 | `zhtw_correct` | 用戶端、伺服器端、通訊皆符合 expected；競品各漏一部分 |
| 21 | `regressions/regression_043` | 台灣 IT/UI 用語 | `zhtw_correct` | 文件系統轉檔案系統；zhconv 保留文件系統 |
| 22 | `tech/tech_039` | 台灣 IT/UI 用語 | `zhtw_correct` | 介面、回傳、回應標頭皆符合 API 語境；競品保留返回/響應頭 |
| 23 | `tech/tech_021` | 台灣 IT/UI 用語 | `zhtw_correct` | 持續整合管線符合台灣技術語境；競品保留流水線或集成 |
| 24 | `tech/tech_026` | 台灣 IT/UI 用語 | `zhtw_correct` | 函式、拋出例外符合程式語境；競品保留異常或函數 |
| 25 | `tech/tech_014` | 台灣 IT/UI 用語 | `zhtw_correct` | 後端服務回傳狀態碼；競品保留返回狀態碼 |
| 26 | `regressions/regression_039` | 台灣 IT/UI 用語 | `zhtw_correct` | UI「撤销操作」轉為復原操作；競品保留撤銷 |
| 27 | `social/social_071` | 台灣通用用語 | `zhtw_correct` | 社群「评论区」轉留言區；競品保留評論區 |
| 28 | `news/news_022` | 台灣通用用語 | `zhtw_correct` | 台積電、宣布、先進製程皆符合 expected；zhconv 出現「先進位程」錯轉 |
| 29 | `social/social_025` | 台灣通用用語 | `zhtw_correct` | 視頻轉影片；zhconv 保留視頻 |
| 30 | `social/social_012` | 台灣通用用語 | `zhtw_correct` | 自行车轉腳踏車，周末轉週末；zhconv 保留自行車與周末 |

## 建議後續

1. 不進詞庫修正，因為本輪沒有 `candidate_gap`。
2. 從本表挑 10-15 筆放進產品文件或 README 的「精準度案例」段落。
3. 若要擴充 `benchmarks/precision_cases.json`，優先選保護案例：
   - `regressions/regression_045`
   - `regressions/regression_044`
   - `wiki/wiki_060`
   - `regressions/regression_081`
   - `regressions/regression_034`
4. 下一輪 discovery 可跑全 500 筆：

```bash
uv run --with opencc-python-reimplemented --with zhconv python scripts/discover_competitor_diffs.py --limit -1 --format md --output docs/reports/competitor-diffs-full-2026-07-03.md
```
