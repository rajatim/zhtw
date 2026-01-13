# 發佈流程

> 版本發佈透過 CI/CD Pipeline 執行

## 🚨 最高優先級規則

```
⛔ 禁止手動發佈（gh release create、git tag）
⛔ 沒有使用者明確同意，不可發佈
✅ 只能透過 CI/CD Pipeline 發佈
```

## 發佈步驟

### 1. 準備版本（貢獻者/AI 可做）

更新以下三處版本號（**必須一致**）：

```bash
# 1. pyproject.toml
version = "x.y.z"

# 2. src/zhtw/__init__.py
__version__ = "x.y.z"

# 3. CHANGELOG.md 新增版本區塊
## [x.y.z] - YYYY-MM-DD
### Added / Changed / Fixed
- ...
```

然後：
- 執行 `pytest` 確保測試通過
- Commit + Push 到 main

### 2. 觸發發佈（Maintainer 操作）

- Maintainer 觸發 CI/CD Pipeline
- 審核通過後自動發佈

> ⚠️ Pipeline 會驗證三處版本號一致性，不一致會失敗。

## Pipeline 自動執行

1. 驗證版本號一致性
2. 執行完整測試
3. 建立 Git tag
4. 建立 GitHub Release
5. 發佈至 PyPI

---

*需要時讀取：準備版本發佈*
