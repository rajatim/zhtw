# 貢獻方式

ZHTW 歡迎程式、文件、詞彙與可合法公開的真實語料貢獻。完整開發流程以 [repo 的 `CONTRIBUTING.md`](https://github.com/rajatim/zhtw/blob/main/CONTRIBUTING.md) 為準。

## 回報錯轉或漏轉

請在 [GitHub Issues](https://github.com/rajatim/zhtw/issues) 提供：

1. zhtw 版本、source 與 ambiguity mode。
2. 最短但保留必要語境的完整輸入。
3. 實際結果與建議的台灣繁體結果。
4. 台灣用法的理由或公開來源。
5. 新規則可能誤傷的反例。

不要只提供缺少語境的單一歧義詞。安全漏洞請依 [Security Policy](https://github.com/rajatim/zhtw/blob/main/SECURITY.md) 私下回報。

## 修改詞庫

「寧可少轉，不要錯轉」優先於增加規則數。廣泛詞彙需要台灣語境證據；會誤傷子字串時要加入 identity mapping 與回歸測試。

```bash
uv sync --extra dev
uv run zhtw validate
uv run pytest
make docs-build
```

若變更版本，所有 SDK 必須用 `make bump VERSION=X.Y.Z` 同步，不可手動只升一個套件。

## AI 與人工決策

AI 可以整理候選、找反例與提供 advisory（建議），但 benchmark expected、annotation 與詞彙是否採用，必須由 maintainer 做最後決定。不要把 AI 輸出直接當成 ground truth。

提交內容不得包含憑證、客戶資料、私有 expected 或沒有公開權利的第三方文字。
