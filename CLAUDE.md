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

## 🧪 深度測試專家角色

深度測試本產品需要以下專家：

**語言專家：**
- 台灣母語者：驗證轉換結果符合台灣用語
- 中國母語者：提供真實簡體樣本
- 香港母語者：測試 HK→TW 轉換
- 語言學者：一字多義（後/後、發/髮）語境判斷

**領域專家：**
- IT 工程師：軟體/軟體、函式/函式 等術語
- 醫療人員：愛滋/愛滋、超音波/超音波
- 法律/財經專業：正式文書用語

**技術測試：**
- QA 工程師：邊界條件、效能、回歸測試
- 文字編輯：大量真實文字校對
- NLP 專家：LLM 模式語境準確度

> 💡 最有價值：**台灣 IT 從業者**（同時覆蓋每日 + 技術術語）

## 🔀 Git 工作流程

### 預設行為
- 一般修改直接 commit 到 main
- 每次 commit 都要有清楚的 commit message

### 何時需要 Branch

| 情境 | 分支 | 說明 |
|------|------|------|
| 詞庫擴充/修正 | ❌ | 直接 main |
| 小修正/文件 | ❌ | 直接 main |
| **zhtw-db 開發** | ✅ | 每個 DB 一個 branch |
| **核心重構** | ✅ | 先詢問再開 |
| **實驗性變更** | ✅ | 先詢問再開 |

需要開 branch 時，先詢問：
> 這次變更會 [簡述影響]，建議開 branch `feature/xxx` 進行，要嗎？

### Branch 命名
- `feature/功能簡述`（如 `feature/db-postgres`）
- `refactor/範圍簡述`
- `experiment/嘗試內容`
- `fix/問題簡述`

### 合併前確認
```
## 準備合併 [branch name] → main

**變更內容：**
- [檔案清單]

**功能說明：**
- [完成了什麼]

**注意事項：**
- [破壞性變更或額外步驟]

確認合併？
```

### Commit 規範
格式：`type: 簡短描述`

| 類型 | 用途 |
|------|------|
| `feat` | 新功能 |
| `fix` | 修復問題 |
| `refactor` | 重構（不改功能） |
| `docs` | 文件更新 |
| `chore` | 雜項（依賴、設定） |
