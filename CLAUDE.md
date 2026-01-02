# ZHTW - AI 開發指南

> **v2.6.0** | 簡轉繁轉換器 | 指南：`.claude/guides/`

## 🚨 黃金規則

```
1. 寧可少轉，不要錯轉
2. 不用 OpenCC（會過度轉換）
3. 詞庫修改要謹慎（確認臺灣不用該詞）
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

## 🚀 發佈流程

PyPI 發佈由 **GitHub Actions 自動處理**：

1. 更新版本號：`pyproject.toml` + `src/zhtw/__init__.py`
2. 更新 `CHANGELOG.md`
3. 建立 git tag：`git tag -a v版本號 -m "訊息"`
4. 推送：`git push && git push origin v版本號`
5. 建立 GitHub Release：`gh release create v版本號 --title "標題" --notes "內容"`
6. **自動觸發** `.github/workflows/publish.yml` → 發佈到 PyPI

> ⚠️ PyPI Token 存放於 **GitHub Secrets**（`PYPI_API_TOKEN`），不在 1Password

## 📚 按需讀取

| 主題 | 檔案 |
|-----|------|
| 詞庫操作 | `.claude/guides/vocabulary.md` |
| 問題排查 | `.claude/guides/debugging.md` |
| 決策樹 | `.claude/guides/decision-trees.md` |
