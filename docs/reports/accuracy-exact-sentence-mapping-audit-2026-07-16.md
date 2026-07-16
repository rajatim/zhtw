# Exact-sentence Mapping Audit（2026-07-16）

## 方法

在記憶體中一次移除全部帶句號且具有 target identity 的完整句 source mapping，僅以
剩餘泛化規則重新轉換每個 source 與 target。

## 結果

- 原始完整句 pairs：373
- 不需 source mapping 即可得到 expected：4
- 已移除 source mappings：4
- 保留 exact-sentence guards：369
- 移除 target identities：0

四筆 target identity 不能刪除；移除後第二次轉換會分別改壞「發布」、「分區」、
「命名空間」與「綁定」。因此只刪冗餘 source，保留 identity。

## 解讀限制

剩餘 369 筆是保守的公開 regression protection，不計為 fresh-blind generalization。
不得為了減少句型數而自動拆成裸詞；任何短詞化必須另有負向案例與人工確認。
