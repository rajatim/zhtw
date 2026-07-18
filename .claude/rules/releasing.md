# 釋出流程

> 版本釋出透過手動操作執行

## 🚨 最高優先順序規則

```
⛔ 沒有使用者明確同意，不可釋出
⛔ 升版必須 mono-versioning（所有 SDK 同步，見 CLAUDE.md 黃金規則 6）
✅ release commit 的遠端 conformance 通過後，才建立 tag + GitHub Release
✅ GitHub Release 的不可變 tag gate 通過後，才分派所有發布 workflow
```

> **重要**：release commit 推上 main 後，必須先通過遠端全 SDK conformance gate，
> 才能建立 tag 與 GitHub Release。Release 發布後會再以相同 gate 驗證不可變 tag，
> 通過才分派所有 registry 與 Go binary workflow。

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
- `make release-gate` 以固定 corpus commit 執行 Python、所有 SDK、Go lint、
  版本、匯出、詞庫與 idempotency 驗證
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
dry-run 會在暫存 worktree 中完成 bump，測試實際候選版本，不修改目前工作樹。
正式流程會自動：測試 bump 後候選 → 人工確認 → 建立並推送 release commit →
等待該 commit 的遠端 conformance 全綠 → 建立雙 tag
（vX.Y.Z + sdk/go/vX.Y.Z）→ GitHub Release（notes 取自 CHANGELOG）。

**方法 B：手動（fallback）**

```bash
# 先完成 make bump、CHANGELOG、make release-gate、commit 與 push
# 找出 release commit 對應的 SDK Conformance run，且必須等到成功
RELEASE_SHA=$(git rev-parse HEAD)
gh run list --workflow "SDK Conformance" --branch main --event push \
  --json databaseId,headSha,conclusion \
  --jq ".[] | select(.headSha == \"$RELEASE_SHA\")"
gh run watch <run-id> --exit-status

# 遠端 gate 成功後才能建立 tag 與 release
git tag -a vX.Y.Z -m "vX.Y.Z: 簡短說明"
git tag -a sdk/go/vX.Y.Z -m "sdk/go vX.Y.Z"   # Go 子目錄 module 需要
git push origin vX.Y.Z sdk/go/vX.Y.Z
gh release create vX.Y.Z --title "vX.Y.Z: 標題" --notes "（從 CHANGELOG 複製）"
```

> **GitHub Release（published 事件）會驗證不可變 tag**；全綠後才分派發布：
> PyPI、Maven Central、npm（zhtw-js + zhtw-wasm）、crates.io、NuGet，
> 以及 Go binaries。Go tag 本身不會直接發布 binary。

### 3. 釋出後驗證 + Homebrew（一鍵）

```bash
make release-verify VERSION=X.Y.Z
```

自動：只追蹤該版本的 7 個 workflow 並等待全綠 → 輪詢 registry artifact
（PyPI / npm×2 / crates.io / NuGet / Maven / Go proxy）→
idempotent 更新 `~/GitHub/homebrew-tap`（同步、算 sha256、無差異即略過）。
任一 workflow 失敗、registry 逾時或 Homebrew 未完成都會非零退出。

煙霧測試（自選）：`pip install zhtw==X.Y.Z && zhtw --version`、`brew upgrade zhtw`

---

## 📋 核對清單

每次釋出前請參照 [`docs/releases/RELEASE-CHECKLIST.md`](../../docs/releases/RELEASE-CHECKLIST.md)，逐項確認。

---

*需要時讀取：準備版本釋出*
