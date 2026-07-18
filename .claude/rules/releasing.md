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

> **重要**：發布 GitHub Release 後會先執行全 SDK conformance gate，通過才分派
> 各 registry 發布 workflow。若任一 SDK 版本跟 tag 不一致，gate 必須中止發布。

## 釋出步驟

### 1. 準備版本（貢獻者/AI 可做）

**一鍵升所有 SDK + 驗證 + 重新匯出資料檔：**

```bash
make bump VERSION=X.Y.Z
```

會自動更新這 8 個地方（mono-versioning）：

| # | 檔案 | 內容 |
|---|------|------|
| 1 | `pyproject.toml` | `version = "X.Y.Z"` |
| 2 | `src/zhtw/__init__.py` | `__version__ = "X.Y.Z"` |
| 3 | `sdk/java/pom.xml` | `<version>X.Y.Z</version>` |
| 4 | `sdk/typescript/package.json` | `"version": "X.Y.Z"` |
| 5 | `sdk/rust/Cargo.toml` | `version = "X.Y.Z"` |
| 6 | `sdk/dotnet/Zhtw.csproj` | `<Version>X.Y.Z</Version>` |
| 7 | `sdk/data/zhtw-data.json` + `golden-test.json` | `zhtw export` 重新產生 |
| 8 | `sdk/rust/zhtw-wasm/package.json` | `"version": "X.Y.Z"` |

若因特殊原因需手動改：改完**務必**跑 `make version-check`，任一檔案不一致就會 exit 1。

**然後手動更新 `CHANGELOG.md`**（AI 可做，`make bump` 不自動寫 CHANGELOG）：

```markdown
## [X.Y.Z] - YYYY-MM-DD
### Added / Changed / Fixed / Breaking
- ...
```

最後：
- `make test-all` 確保 Python 與所有 SDK 測試透過
- Commit + Push 到 main

### 2. 釋出（Maintainer 操作）

**方法 A：一鍵釋出（推薦，`scripts/release.sh`）**

```bash
make release-dry VERSION=X.Y.Z   # 先預演：閘門 + 測試，不做任何變更
make release VERSION=X.Y.Z       # 正式釋出（含 y/N 確認）
```

指令碼閘門：main 分支、工作樹乾淨、與 origin 同步、tag 不存在、
Dependabot 無 medium+ 開放弱點、CHANGELOG 有內容、版本同步、SDK data 與 fresh
export 完全一致、詞庫驗證、curated target idempotency、全部 SDK 測試。
正式流程會自動把 `[Unreleased]` 升級為 `[X.Y.Z]`。
通過後自動：bump → commit → 雙 tag（vX.Y.Z + sdk/go/vX.Y.Z）→ push →
GitHub Release（notes 取自 CHANGELOG）。

**方法 B：手動（fallback）**

```bash
git tag -a vX.Y.Z -m "vX.Y.Z: 簡短說明"
git tag -a sdk/go/vX.Y.Z -m "sdk/go vX.Y.Z"   # Go 子目錄 module 需要
git push origin vX.Y.Z sdk/go/vX.Y.Z
gh release create vX.Y.Z --title "vX.Y.Z: 標題" --notes "（從 CHANGELOG 複製）"
```

> **GitHub Release（published 事件）會先觸發全 SDK conformance gate**；全綠後才分派發布：
> PyPI、Maven Central、npm（zhtw-js + zhtw-wasm）、crates.io、NuGet；
> `sdk/go/v*` tag 另觸發 Go binaries 建置。

### 3. 釋出後驗證 + Homebrew（一鍵）

```bash
make release-verify VERSION=X.Y.Z
```

自動：等待 6 個 workflow 全綠 → 逐一驗證 registry artifact
（PyPI / npm×2 / crates.io / NuGet / Maven / Go proxy）→
半自動更新 `~/GitHub/homebrew-tap`（算 sha256、改 formula、確認後推送）。
Maven Central 同步可能落後 30 分鐘以上，未齊時稍後重跑同一指令即可。

煙霧測試（自選）：`pip install zhtw==X.Y.Z && zhtw --version`、`brew upgrade zhtw`

---

## 📋 核對清單

每次釋出前請參照 [`docs/releases/RELEASE-CHECKLIST.md`](../../docs/releases/RELEASE-CHECKLIST.md)，逐項確認。

---

*需要時讀取：準備版本釋出*
