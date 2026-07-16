<!-- zhtw:disable -->
# blind-v1 batch 11 語意複核後私有基準摘要

- 日期：2026-07-14
- 密封案例：841
- 可接受：795
- miss：46
- 可接受準確率：94.53%
- 95% Wilson CI：92.87%–95.96%
- primary exact：624
- acceptable variant exact：171
- 冪等率：98.34%

本報告只保存彙總統計與來源雜湊，不包含 input、expected、acceptable、實際輸出或逐筆 benchmark row。完整基準輸出只位於 `/tmp/zhtw-blind-v1-private-benchmark-after-batch11-semantic-reaudit-2026-07-14.json`，不納入版本庫。

語意複核後，4 筆臺灣可接受同義表達加入 private acceptable variants；10 筆明確能力缺口移出密封集，通過公開 regression promotion gate；11 筆仍保留為嚴格私有 holdout signal。
