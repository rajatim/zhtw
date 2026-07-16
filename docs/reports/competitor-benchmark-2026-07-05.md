<!-- zhtw:disable -->
# 競品 Benchmark 報告（2026-07-05）

## 摘要

本報告使用 `benchmarks/precision_cases.json` 的 37 筆人工標註 expected，比較 zhtw 與兩個可選競品轉換器。競品結果只作為候選問題偵測，不作為詞庫來源。

本次相較 2026-07-03 報告新增 11 筆已人工審核的 `over_conversion_guard` 案例，來源為 `docs/reports/competitor-advantage-review-2026-07-03.md` 的保護案例。這批新增案例只用來防回歸，不改詞庫。

執行指令：

```bash
uv run --with opencc-python-reimplemented --with zhconv python scripts/competitor_benchmark.py --format json --fail-on-zhtw-mismatch --output docs/reports/competitor-benchmark-2026-07-05.json
```

引擎：

| 引擎 | 版本 | 狀態 |
|------|------|------|
| zhtw | 4.4.1 | available |
| opencc-s2twp | 0.1.7 | available |
| zhconv-zh-tw | 1.4.3 | available |

結果：

| 分類 | 數量 | 判讀 |
|------|------|------|
| `candidate_gap` | 0 | 沒有發現「競品符合 expected、zhtw 不符合」的案例 |
| `zhtw_miss` | 0 | 沒有發現 zhtw 未符合人工 expected 的案例 |
| `zhtw_advantage` | 32 | zhtw 符合 expected，但至少一個競品不符合 |
| `all_match` | 5 | zhtw 與兩個競品都符合 expected |
| `zhtw_only` | 0 | 本次所有競品都可用 |

結論：本次新增案例應保留為 regression guard；不應從競品輸出導入詞條。

## 本次新增保護案例

| ID | 領域 | 輸入 | expected | 保護重點 |
|----|------|------|----------|----------|
| `guard-program-legal-procedure` | mixed | 写程序前先看法律程序 | 寫程式前先看法律程序 | 程式語境轉「程式」，法律語境保留「程序」 |
| `guard-preserve-historical-relics` | culture | 博物馆保存历史文物。 | 博物館保存歷史文物。 | 文化保存語境保留「保存」 |
| `guard-support-decision` | daily | 我支持这个决定 | 我支持這個決定 | 一般支持語境保留「支持」 |
| `guard-support-remote-work` | news | 调查显示年轻族群支持远程办公。 | 調查顯示年輕族群支持遠端辦公。 | 支持工作型態保留「支持」，遠程辦公轉「遠端辦公」 |
| `guard-marriage-object` | daily | 他的结婚对象很温柔 | 他的結婚對象很溫柔 | 結婚對象保留「對象」 |
| `guard-upload-document` | social | 我把文件上传到群组了。 | 我把文件上傳到群組了。 | 模糊「文件」不強制轉成「檔案」 |
| `guard-logout-account-company` | mixed | 注销账户不是注销公司 | 登出帳戶不是註銷公司 | 帳戶語境用「登出」，公司語境保留「註銷」 |
| `guard-good-news` | daily | 好消息传来 | 好消息傳來 | 好消息保留「消息」 |
| `guard-log-document` | it | 日志文件记录错误信息。 | 日誌文件記錄錯誤資訊。 | 本句 expected 保留「日誌文件」 |
| `guard-through-parameter` | it | 日志等级可以通过参数调整。 | 日誌等級可以透過參數調整。 | 透過參數，不轉成引數或保留通過 |
| `guard-central-bank-announce` | news | 央行宣布维持利率政策不变。 | 央行宣布維持利率政策不變。 | 新聞語境保留「宣布」 |

## 後續判斷

- 這批新增案例全部為 `zhtw_advantage`，沒有 `candidate_gap`。
- 下一步應把這批 guard 視為 M1 regression seed，繼續從 full discovery 的 308 筆 `zhtw_advantage` 中擴到 100-200 筆。
- 擴充時仍維持人工 expected 優先；競品輸出只用來定位差異，不可作為 expected 來源。
