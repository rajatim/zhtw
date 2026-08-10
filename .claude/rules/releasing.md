# 釋出流程

> zhtw 的建置、驗證與公開發布只走 Jenkins。GitHub Actions、手動 tag、
> `gh workflow run`、本機 registry publish 都不是備援路徑。

## 最高優先順序規則

```text
⛔ 沒有使用者明確同意，不可公開釋出
⛔ 不可用 make release、手動 tag 或手動 publish 繞過 Jenkins
⛔ 已被 registry 接受的版本不可回滾、覆蓋或重用
✅ 所有 SDK 必須維持 mono-versioning
✅ build、verify、read-only preview、正式 publication 必須使用同一份封存候選
```

## 角色分工

- 貢獻者可以執行 `make bump VERSION=X.Y.Z`、`make version-check`、
  `make release-gate`，但不能因此建立正式版本。
- `zhtw/build` 計算版本、產生候選 patch、測試一次並封存所有套件。
- `zhtw/verify` 只能選成功的 main `zhtw/build`；`VERIFY_SUITE=all` 通過後會封存
  繫結 SHA、tree、版本與候選 checksum 的 release-eligible receipt。
- `zhtw/release` 預設 `PREVIEW`，而且連 preview 都必須提供完全相符的成功
  verification receipt。`CREDENTIAL_PREFLIGHT` 會安全驗證所有發布 credential，
  但不建立 tag、Release 或 registry version；只有明確核准後才可 `PUBLISH_ALL`。
- `make release` 與 `make release-dry` 會 fail-closed，提醒改用 Jenkins。

## 標準流程

### 1. 建立完整候選

```bash
jcli build zhtw/build \
  -p BRANCH=main \
  -p VERSION_BUMP=patch
```

`patch` 用於修正、`minor` 用於向下相容的新功能、`major` 用於 breaking
change。Jenkins 會同步更新所有 SDK 版本、提升 CHANGELOG `[Unreleased]`、跑完整
release gate，阻擋 open medium 以上 Dependabot 警示與即將到期的 npm token，並建出
PyPI、npm x2、crate、NuGet、Maven 與五種 Go binary。

### 2. 驗證同一份候選

```bash
jcli build zhtw/verify \
  -p BUILD_NUMBER=<成功的-zhtw-build> \
  -p VERIFY_SUITE=all
```

只有 `all` 會產生可供發布的 receipt。`sdk-matrix` 與 `competitor-benchmark` 可以單獨
診斷，但不能解除 release gate。

### 3. 唯讀預演

```bash
jcli build zhtw/release \
  -p BUILD_NUMBER=<成功的-zhtw-build> \
  -p VERIFY_BUILD_NUMBER=<相符的-zhtw-verify> \
  -p RELEASE_ACTION=PREVIEW \
  -p SKIP_CONFIRMATION=false
```

預演會先驗證 receipt 與候選的 checksum、base SHA、base tree、candidate tree、版本
完全相同，再檢查 main 前進關係與既有 tag。它不繫結 registry credential，也不改
Git 或外部服務。

### 4. 安全驗證所有 credential

```bash
jcli build zhtw/release \
  -p BUILD_NUMBER=<成功的-zhtw-build> \
  -p VERIFY_BUILD_NUMBER=<相符的-zhtw-verify> \
  -p RELEASE_ACTION=CREDENTIAL_PREFLIGHT \
  -p SKIP_CONFIRMATION=false
```

這個動作只做 authentication 與權限 probe，不上傳套件。它會驗證 GitHub API/SSH、
PyPI、npm 兩個 package 的 read-write scope 與到期日、crates.io、NuGet、Maven
Central token，以及 Maven GPG 簽章。

### 5. 明確核准後正式發布

```bash
jcli build zhtw/release \
  -p BUILD_NUMBER=<同一個-zhtw-build> \
  -p VERIFY_BUILD_NUMBER=<同一個-zhtw-verify> \
  -p RELEASE_ACTION=PUBLISH_ALL \
  -p SKIP_CONFIRMATION=true
```

正常順序是：雙 tag 與 GitHub Release → PyPI → npm `zhtw-js` → npm
`zhtw-wasm` → crates.io → NuGet → Maven Central → Homebrew → 完整公開驗證。

`SKIP_CONFIRMATION=true` 只代表使用者已在目前對話核准這組確切 build 與 verify，
不會略過 receipt、來源、checksum、tag 或 registry 驗證。

所有長時間 job 都要 detached 啟動，再用 Jenkins UI 或 API 監看回傳的 build number；
不可使用 attached `jcli -s -v`。CLI 連線中斷曾經直接中止還在執行的 Jenkins build。

## 失敗處理

公開 registry 沒有網站部署式 rollback。某一步失敗時：

1. 停止後續發布。
2. 使用同一組 `zhtw/build` 與 `zhtw/verify` 編號重跑 `PUBLISH_ALL`，或選對應的
   `RETRY_*`。
3. 已存在的版本只有在公開內容與封存候選相符時才會略過；PyPI 只補傳缺少的檔案。
4. 如果已發布內容本身有錯，只能修正後升下一個 patch；不可刪 tag 或重用版號。

Maven 上傳後會立即封存 deployment ID。若狀態查詢斷線，使用
`RETRY_MAVEN` 加上該 ID 續查既有 deployment，不可建立第二次 upload。

可用的修復動作：`RETRY_GIT`、`RETRY_PYPI`、`RETRY_NPM_JS`、
`RETRY_NPM_WASM`、`RETRY_CRATES`、`RETRY_NUGET`、`RETRY_MAVEN`、
`RETRY_HOMEBREW`。每個動作仍是不可逆公開操作，必須確認。

## 限制

目前 Jenkins 只有 Linux builder。Python、Java、Node、Rust、Go 與 .NET 的 Linux
版本矩陣已搬到 `zhtw/verify`；Go 也會交叉編譯 Darwin/Windows binary。但 macOS 與
Windows 原生執行測試要等新增 Jenkins agent，不能把交叉編譯說成原生驗證。

內部 credential、job 維護與首次發布證據請依 private Jenkins runbook；公開 repo
不保存 Jenkins URL 或 secret 細節。

---

*需要時讀取：準備版本釋出*
