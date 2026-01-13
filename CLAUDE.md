# ZHTW - AI 開發指南

> **v2.8.5** | 簡轉繁轉換器 | 指南：`.claude/guides/`

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

## 📚 模組化規則

| 檔案 | 內容 | 讀取時機 |
|------|------|----------|
| @.claude/rules/releasing.md | 版本發佈流程 | 準備發佈版本 |
| @.claude/rules/git-workflow.md | 分支策略、提交規範 | 開發分支、合併 |
| `.claude/guides/vocabulary.md` | 詞庫操作 | 新增/修改詞彙 |
| `.claude/guides/debugging.md` | 問題排查 | 轉換錯誤 |
| `.claude/guides/decision-trees.md` | 決策樹 | 複雜判斷 |
| `.claude/guides/deep-testing.md` | 深度測試 | 完整驗證 |

> 💡 **Maintainer 注意**：內部規則（如 CI/CD 細節）在 `*-internal.md` 檔案中，不公開版控。

## 🔗 關聯外部 Repo

| Repo | 用途 | 注意事項 |
|------|------|----------|
| [zhtw-test-corpus](https://github.com/rajatim/zhtw-test-corpus) | 簡體中文測試語料 | **勿轉換！** 需保持簡體 |

### 測試語料使用

```bash
# 下載語料（在 zhtw 目錄）
git clone https://github.com/rajatim/zhtw-test-corpus tests/data/corpus

# 執行語料測試
pytest tests/test_corpus.py
```

> ⚠️ 測試語料獨立 repo 是因為：此 repo 的 hooks 會自動轉換簡體字

## 🧪 深度測試專家角色

**語言專家：** 台灣母語者、中國母語者、香港母語者、語言學者
**領域專家：** IT 工程師、醫療人員、法律/財經專業
**技術測試：** QA 工程師、文字編輯、NLP 專家

> 💡 最有價值：**台灣 IT 從業者**（同時覆蓋每日 + 技術術語）

詳細說明：`.claude/guides/deep-testing.md`

---

**開始開發：遵守黃金規則，按需讀取模組化指南**
