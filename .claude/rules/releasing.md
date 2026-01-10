# 發佈流程

> 版本發佈必須透過 Jenkins Pipeline 執行

## 🚨 最高優先級規則

```
⛔ 禁止手動發佈（gh release create、git tag）
⛔ 沒有使用者明確同意，不可發佈
✅ 只能透過 Jenkins Pipeline 發佈
```

## Jenkins 發佈

| 項目 | 值 |
|------|-----|
| Jenkins URL | [REDACTED-JENKINS-URL] |
| Pipeline 檔案 | `[REDACTED-PIPELINE-PATH]` |
| 觸發方式 | 手動（需 審核） |

## 發佈步驟

### 1. 準備（Claude 可做）

- 更新 `pyproject.toml` → version
- 更新 `src/zhtw/__init__.py` → __version__
- 更新 `CHANGELOG.md` → 新增版本區塊
- Commit + Push 到 main

### 2. 發佈（需使用者操作）

- 使用者到 Jenkins 觸發 `zhtw-release`
- 審核通過後自動發佈

> ⚠️ 三處版本號必須一致！Jenkins 會驗證。

## 自動執行內容

Pipeline 會自動：
1. 驗證版本號一致性
2. 執行完整測試
3. 建立 Git tag
4. 建立 GitHub Release
5. 發佈至 PyPI
6. 發送 通知

---

*需要時讀取：準備版本發佈*
