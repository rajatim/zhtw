# ZHTW - AI 開發指南

> **v4.2.1** | 簡轉繁轉換器 | 指南：`.claude/guides/`

## 🚨 黃金規則

```
1. 寧可少轉，不要錯轉
2. 不用 OpenCC（會過度轉換）
3. 詞庫修改要謹慎（確認臺灣不用該詞）
4. 修改後跑 pytest
5. 子字串加 identity mapping
6. ALWAYS 升版 = 所有 SDK 同步（mono-versioning）
```

### 規則 6 展開：升版 mono-versioning

**任何版本變動都必須同時更新這 8 個地方，一個都不能漏：**

| # | 檔案 | 內容 |
|---|------|------|
| 1 | `pyproject.toml` | `version = "X.Y.Z"` |
| 2 | `src/zhtw/__init__.py` | `__version__ = "X.Y.Z"` |
| 3 | `sdk/java/pom.xml` | `<version>X.Y.Z</version>` |
| 4 | `sdk/typescript/package.json` | `"version": "X.Y.Z"` |
| 5 | `sdk/rust/Cargo.toml` | `version = "X.Y.Z"` |
| 6 | `sdk/dotnet/Zhtw.csproj` | `<Version>X.Y.Z</Version>` |
| 7 | `sdk/data/zhtw-data.json` + `golden-test.json` | 透過 `zhtw export` 重新產生 |
| 8 | `sdk/rust/zhtw-wasm/package.json` | `"version": "X.Y.Z"` |

**絕對禁止：**
- ❌ 只升 Python 不升 Java — 會讓 `sdk-java.yml` 的 `mvn deploy` 失敗（Maven Central artifact 不可變）
- ❌ 手動改一部分 SDK 就 commit — 請用下面的指令
- ❌ 論證「某 SDK 沒有 breaking change 所以不用升」 — mono-versioning 優先於 strict SemVer

**正確做法（擇一）：**

```bash
# 方法 A：一鍵升版（推薦）
make bump VERSION=X.Y.Z
# 會自動：sed 6 個檔案 → zhtw export → version-check 驗證

# 方法 B：手動改後驗證
# ...手動改檔案...
make version-check   # 任一檔案不一致就 exit 1
```

**理由：** Git tag push 會同時觸發 `publish.yml`（PyPI）和 `sdk-java.yml`（Maven Central），兩邊的版本必須跟 tag 對齊，否則釋出會失敗或語意混亂。共享的 `sdk/data/zhtw-data.json` 也嵌入版本號，多語言 SDK 讀這份資料會做版本比對。

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
| @.claude/rules/releasing.md | 版本釋出流程 | 準備釋出版本 |
| `docs/RELEASE-CHECKLIST.md` | 版本釋出核對清單 | 每次升版時逐項勾選 |
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
