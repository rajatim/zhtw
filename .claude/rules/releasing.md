# 發佈流程

> 版本發佈透過手動操作執行

## 🚨 最高優先級規則

```
⛔ 沒有使用者明確同意，不可發佈
✅ 手動建立 tag + GitHub Release
✅ PyPI 透過 GitHub Actions publish workflow 自動發佈
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

### 2. 手動發佈（Maintainer 操作）

```bash
# 建立 Tag
git tag -a vX.Y.Z -m "vX.Y.Z: 簡短說明"
git push origin vX.Y.Z

# 建立 GitHub Release
gh release create vX.Y.Z \
  --title "vX.Y.Z: 標題" \
  --notes "變更內容（可從 CHANGELOG 複製）"
```

> Push tag 會自動觸發 `.github/workflows/publish.yml` 發佈到 PyPI。

### 3. 更新 Homebrew Tap（Maintainer 操作）

PyPI 發佈成功後，更新 `rajatim/homebrew-tap`：

```bash
cd ~/GitHub/homebrew-tap

# 取得新版 tarball SHA256
curl -sL https://files.pythonhosted.org/packages/source/z/zhtw/zhtw-X.Y.Z.tar.gz | shasum -a 256

# 更新 Formula/zhtw.rb 的 url 和 sha256
# commit + push
```

### 4. 發佈後驗證

```bash
pip install zhtw==X.Y.Z    # PyPI 安裝測試
zhtw --version              # 版本確認
zhtw check .                # 基本功能
brew upgrade zhtw            # Homebrew 更新測試
```

---

*需要時讀取：準備版本發佈*
