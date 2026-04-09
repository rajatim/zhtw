# 釋出流程

> 版本釋出透過手動操作執行

## 🚨 最高優先順序規則

```
⛔ 沒有使用者明確同意，不可釋出
⛔ 升版必須 mono-versioning（所有 SDK 同步，見 CLAUDE.md 黃金規則 6）
✅ 手動建立 tag + GitHub Release
✅ PyPI 透過 GitHub Actions publish workflow 自動釋出
✅ Maven Central 透過 sdk-java.yml（release trigger）自動釋出
```

> **重要**：push tag 後會「同時」觸發 PyPI + Maven Central 兩條釋出線。若 `sdk/java/pom.xml` 的版本跟 tag 不一致，`mvn deploy` 會失敗（Central artifact 不可變）。

## 釋出步驟

### 1. 準備版本（貢獻者/AI 可做）

**一鍵升所有 SDK + 驗證 + 重新匯出資料檔：**

```bash
make bump VERSION=X.Y.Z
```

會自動更新這 7 個地方（mono-versioning）：

| # | 檔案 | 內容 |
|---|------|------|
| 1 | `pyproject.toml` | `version = "X.Y.Z"` |
| 2 | `src/zhtw/__init__.py` | `__version__ = "X.Y.Z"` |
| 3 | `sdk/java/pom.xml` | `<version>X.Y.Z</version>` |
| 4 | `sdk/typescript/package.json` | `"version": "X.Y.Z"` |
| 5 | `sdk/rust/Cargo.toml` | `version = "X.Y.Z"` |
| 6 | `sdk/dotnet/Zhtw.csproj` | `<Version>X.Y.Z</Version>` |
| 7 | `sdk/data/zhtw-data.json` + `golden-test.json` | `zhtw export` 重新產生 |

若因特殊原因需手動改：改完**務必**跑 `make version-check`，任一檔案不一致就會 exit 1。

**然後手動更新 `CHANGELOG.md`**（AI 可做，`make bump` 不自動寫 CHANGELOG）：

```markdown
## [X.Y.Z] - YYYY-MM-DD
### Added / Changed / Fixed / Breaking
- ...
```

最後：
- `pytest` 確保測試透過
- `cd sdk/java && mvn -q verify --batch-mode` 確保 Java SDK 建置透過
- Commit + Push 到 main

### 2. 手動釋出（Maintainer 操作）

```bash
# 建立 Tag
git tag -a vX.Y.Z -m "vX.Y.Z: 簡短說明"
git push origin vX.Y.Z

# 建立 GitHub Release
gh release create vX.Y.Z \
  --title "vX.Y.Z: 標題" \
  --notes "變更內容（可從 CHANGELOG 複製）"
```

> Push tag 會自動觸發 `.github/workflows/publish.yml` 釋出到 PyPI。

### 3. 更新 Homebrew Tap（Maintainer 操作）

PyPI 釋出成功後，更新 `rajatim/homebrew-tap`：

```bash
cd ~/GitHub/homebrew-tap

# 取得新版 tarball SHA256
curl -sL https://files.pythonhosted.org/packages/source/z/zhtw/zhtw-X.Y.Z.tar.gz | shasum -a 256

# 更新 Formula/zhtw.rb 的 url 和 sha256
# commit + push
```

### 4. 釋出後驗證

```bash
pip install zhtw==X.Y.Z    # PyPI 安裝測試
zhtw --version              # 版本確認
zhtw check .                # 基本功能
brew upgrade zhtw            # Homebrew 更新測試
```

---

*需要時讀取：準備版本釋出*
