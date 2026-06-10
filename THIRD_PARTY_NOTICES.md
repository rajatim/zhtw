# Third-Party Notices / 第三方授權宣告

本專案程式碼以 [MIT License](LICENSE) 釋出。詞庫資料中有一部分匯入自
第三方專案，其授權與出處如下。

## 詞庫資料（`src/zhtw/data/terms/cn/opencc.json`）

此檔案的詞條匯入自以下來源（亦隨 `sdk/data/zhtw-data.json` 內嵌於各語言 SDK 釋出）：

| 來源 | 內容 | 授權 |
|------|------|------|
| [OpenCC](https://github.com/BYVoid/OpenCC)（STPhrases / TWPhrases / TWVariantsRevPhrases 詞表） | 簡→繁詞彙、台灣用語轉換表 | Apache License 2.0 |

> 歷史註記：v4.3.0 之前曾含 MediaWiki `ZhConversion.php`（GPL-2.0-or-later）
> 匯入詞條約 1,372 條，因與 MIT 主授權的相容性考量，已於 2026-06 全數移除
> （僅保留可獨立溯源至 OpenCC Apache-2.0 上游的條目）。

匯入後本專案進行過清理與修正（變體字正規化、移除違反「寧可少轉，
不要錯轉」原則的條目等），修改內容見 git 歷史。

### 授權注意事項

OpenCC 詞表（Apache-2.0）與本專案的 MIT 授權相容。

## 致謝

- [OpenCC](https://github.com/BYVoid/OpenCC) — BYVoid 及貢獻者
- [MediaWiki](https://www.mediawiki.org/) — Wikimedia Foundation 及貢獻者
- [pyahocorasick](https://github.com/WojciechMula/pyahocorasick) —
  本專案的多模式比對核心依賴（BSD-3-Clause）
