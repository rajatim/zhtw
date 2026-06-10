# Third-Party Notices / 第三方授權宣告

本專案程式碼以 [MIT License](LICENSE) 釋出。詞庫資料中有一部分匯入自
第三方專案，其授權與出處如下。

## 詞庫資料（`src/zhtw/data/terms/cn/opencc.json`）

此檔案的詞條匯入自以下來源（亦隨 `sdk/data/zhtw-data.json` 內嵌於各語言 SDK 釋出）：

| 來源 | 內容 | 授權 |
|------|------|------|
| [OpenCC](https://github.com/BYVoid/OpenCC)（STPhrases / TWPhrases 詞表） | 簡→繁詞彙、台灣用語轉換表 | Apache License 2.0 |
| [MediaWiki](https://www.mediawiki.org/)（`ZhConversion.php` 轉換表） | 簡繁轉換詞表 | GPL-2.0-or-later |

匯入後本專案進行過清理與修正（變體字正規化、移除違反「寧可少轉，
不要錯轉」原則的條目等），修改內容見 git 歷史。

### 授權注意事項

- OpenCC 詞表（Apache-2.0）與本專案的 MIT 授權相容。
- MediaWiki ZhConversion 詞表為 **GPL-2.0-or-later**。純詞彙對應表
  是否構成受著作權保護之著作，依司法管轄區而異；為透明起見，
  本專案明確標註此來源。若你的使用情境對 GPL 相容性有嚴格要求，
  請自行評估，或改用 `--source` 排除內建詞庫、提供自訂詞典。

## 致謝

- [OpenCC](https://github.com/BYVoid/OpenCC) — BYVoid 及貢獻者
- [MediaWiki](https://www.mediawiki.org/) — Wikimedia Foundation 及貢獻者
- [pyahocorasick](https://github.com/WojciechMula/pyahocorasick) —
  本專案的多模式比對核心依賴（BSD-3-Clause）
