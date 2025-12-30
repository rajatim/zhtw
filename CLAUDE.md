# ZHTW - AI 開發指南

> **v2.5.0** | 簡轉繁台灣用語轉換器 | 詳細指南見 `.claude/guides/`

---

## 🚨 黃金規則

```
1. 寧可少轉，不要錯轉 — 核心理念
2. 不用 OpenCC — 會過度轉換（如 權限→許可權）
3. 詞庫修改要謹慎 — 確認是台灣「不使用」的用語才加
4. 修改後跑 pytest — 確認測試通過
5. 子字串要加 identity mapping — 防止「演算法」→「演演算法」
```

---

## 📍 檔案定位

| 要做什麼 | 找這個檔案 |
|---------|-----------|
| CLI 指令 | `src/zhtw/cli.py` |
| 轉換邏輯 | `src/zhtw/converter.py` |
| 比對演算法 | `src/zhtw/matcher.py` |
| 編碼處理 | `src/zhtw/encoding.py` |
| 詞庫載入 | `src/zhtw/dictionary.py` |
| 簡體詞庫 | `src/zhtw/data/terms/cn/*.json` |
| 港式詞庫 | `src/zhtw/data/terms/hk/*.json` |

---

## ✅ DO

- 修改前先 `Read` 檔案，理解現有邏輯
- 新增詞彙前確認台灣確實不用該詞
- 加 identity mapping 防誤判（如 `"演算法": "演算法"`）
- 用 `zhtw validate` 檢查詞庫衝突
- 用繁體中文回應和寫 commit message

## ❌ DON'T

- 用 OpenCC 或自動轉換工具
- 新增不確定的詞彙
- 把台灣正確用語加入詞庫（如「權限」不轉）
- 加太廣泛的詞（如「表情」→「表情符號」會誤轉「臉部表情」）
- 修改後不跑測試

---

## 🔧 常用指令

```bash
pip install -e ".[dev]"     # 安裝
pytest                       # 測試
ruff check .                 # Lint
python -m zhtw check ./src   # 本地測試
zhtw validate                # 詞庫驗證
```

---

## 📚 詳細指南（按需讀取）

| 主題 | 檔案 |
|------|------|
| 詞庫操作 | `.claude/guides/vocabulary.md` |
| 問題排查 | `.claude/guides/debugging.md` |
| 決策樹 | `.claude/guides/decision-trees.md` |
| zhtw-db 架構 | `docs/zhtw-db/ARCHITECTURE.md` |

---

## 🎯 開發中 (GitHub Issues)

| # | 功能 | 狀態 |
|---|------|------|
| 10 | 資料庫支援 | 架構完成 |
| 11 | 瀏覽器擴充 | 待開發 |
| 8 | VS Code 擴充 | 待開發 |

---

*Token 最佳化版：80 行 ≈ 1,200 tokens（原 465 行 ≈ 6,500 tokens）*
