# 品質與證據

ZHTW 的品質主張必須同時列出版本、資料集、樣本數、評分方式與限制。公開報告可重現，不把內部發布工作編號當成精準度證據。

## 正式 Blind-v2 歷史結果

Blind-v2 是 **zhtw 4.4.2** 的凍結 one-shot benchmark，共 **1,960 筆**。它用來保存當時未經調校的正式比較結果，不是 4.5.0 的即時分數，也不會因後續版本改善而回寫。

完整數字、競品版本、容器 digest、資料雜湊與限制請看：

- [正式市場比較報告](https://github.com/rajatim/zhtw/blob/main/docs/reports/formal-market-benchmark-2026-07-31.md)
- [公開第三方重現方式](https://github.com/rajatim/zhtw/blob/main/docs/testing/public-benchmark-third-party-reproduction.md)
- [公開 paired localization benchmark](https://github.com/rajatim/zhtw/blob/main/docs/testing/public-paired-localization-benchmarks.md)

## 持續品質 gate

每個 release candidate 會檢查：

- Python 與所有 SDK 的共用 golden fixtures。
- 詞庫結構、schema、版本與匯出資料一致性。
- 過度轉換回歸、identity protection 與 idempotency。
- JSON adapter exact-byte 案例與 `explain` event 契約。
- 公開文件雙語配對、版本、範例與 strict site build。

## 如何解讀結果

- Exact match 要求整句完全相同，對標點或可接受變體很敏感。
- Accepted score 可納入事先核准的合理變體，但不得在看過工具輸出後補答案。
- Idempotency 只證明第二次執行不再改變結果，不等於第一次轉換一定正確。
- 公開 paired data 可用來診斷，不可取代未看過的 sealed holdout。

Blind-v3 尚未執行。它不是 4.5.0 的發布條件；未來若產生新主張，會另外公開版本、凍結方式與限制。
