# ZHTW - AI 開發指南

> **v2.5.0** | 簡轉繁轉換器 | 指南：`.claude/guides/`

## 🚨 黃金規則

```
1. 寧可少轉，不要錯轉
2. 不用 OpenCC（會過度轉換）
3. 詞庫修改要謹慎（確認台灣不用該詞）
4. 修改後跑 pytest
5. 子字串加 identity mapping
```

## 📍 檔案定位

| 任務 | 檔案 |
|-----|------|
| CLI | `src/zhtw/cli.py` |
| 轉換 | `src/zhtw/converter.py` |
| 比對 | `src/zhtw/matcher.py` |
| 編碼 | `src/zhtw/encoding.py` |
| 詞庫 | `src/zhtw/data/terms/{cn,hk}/*.json` |

## ✅ DO

- 修改前先 Read 檔案
- 加 identity mapping 防誤判
- 用 `zhtw validate` 檢查衝突
- 繁體中文回應和 commit

## ❌ DON'T

- 用 OpenCC
- 新增不確定的詞彙
- 加太廣泛的詞（如「表情」）
- 修改後不跑測試

## 🔧 指令

```bash
pip install -e ".[dev]"  # 安裝
pytest                    # 測試
zhtw validate             # 驗證詞庫
```

## 📚 按需讀取

| 主題 | 檔案 |
|-----|------|
| 詞庫操作 | `.claude/guides/vocabulary.md` |
| 問題排查 | `.claude/guides/debugging.md` |
| 決策樹 | `.claude/guides/decision-trees.md` |
