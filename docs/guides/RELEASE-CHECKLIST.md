# 版本釋出核對清單

> 每次版本更新時複製此清單到 PR / Issue，逐項勾選。
> `make release VERSION=X.Y.Z` 會自動處理標示 🤖 的專案。

## 1. 準備版本

```bash
make bump VERSION=X.Y.Z    # 或 make release VERSION=X.Y.Z 一次到底
```

### Mono-versioning（8 個檔案）🤖

- [ ] `pyproject.toml` → `version = "X.Y.Z"`
- [ ] `src/zhtw/__init__.py` → `__version__ = "X.Y.Z"`
- [ ] `sdk/java/pom.xml` → `<version>X.Y.Z</version>`
- [ ] `sdk/typescript/package.json` → `"version": "X.Y.Z"`
- [ ] `sdk/rust/Cargo.toml` → `version = "X.Y.Z"`（workspace.package）
- [ ] `sdk/dotnet/Zhtw.csproj` → `<Version>X.Y.Z</Version>`
- [ ] `sdk/rust/zhtw-wasm/package.json` → `"version": "X.Y.Z"`
- [ ] `sdk/data/zhtw-data.json` + `golden-test.json` → `zhtw export` 重新產生

驗證：`make version-check`（任一不一致就 exit 1）

### README 版本引用 🤖

- [ ] `README.md` — Maven/Gradle/crate/pre-commit 版本號
- [ ] `README.en.md` — 同上
- [ ] `sdk/java/BENCHMARK.md` — SDK Version 表頭

### 手動更新

- [ ] `README.md` — Standalone binary 下載連結中的版本（`sdk%2Fgo%2FvX.Y.Z`）
- [ ] `README.en.md` — 同上
- [ ] `CHANGELOG.md` — 新增版本區塊
- [ ] `sdk/rust/Cargo.lock` — `cargo check` 後 commit 更新的 lockfile

## 2. 測試

- [ ] `pytest` — Python 全測透過
- [ ] `cd sdk/java && mvn -q verify --batch-mode` — Java 建置透過
- [ ] `make version-check` — 版本對齊確認

## 3. 釋出

### Tag（兩個）🤖

- [ ] `git tag -a vX.Y.Z` — Root tag
- [ ] `git tag -a sdk/go/vX.Y.Z` — Go subdirectory tag（**必須指向 commit，不是 tag object**）

> ⚠️ Go module 在 `sdk/go/` 子目錄，Go proxy 只認 `sdk/go/vX.Y.Z` 格式的 tag。
> 漏建這個 tag 會導致 Go 版本停在舊版（v4.3.0 就踩過這個坑）。
> `make release` 會自動建兩個 tag。手動操作時務必記得。

### Push + GitHub Release 🤖

- [ ] `git push && git push origin vX.Y.Z sdk/go/vX.Y.Z`
- [ ] `gh release create vX.Y.Z --title "vX.Y.Z: 標題" --generate-notes`

## 4. CI/CD 確認

Push tag 後會**同時觸發**多條釋出線：

- [ ] `.github/workflows/publish.yml` → PyPI ✅
- [ ] `.github/workflows/sdk-java.yml` → Maven Central ✅
- [ ] `.github/workflows/sdk-typescript.yml` → npm (zhtw-js) ✅
- [ ] `.github/workflows/sdk-rust.yml` → crates.io + npm (zhtw-wasm) ✅
- [ ] `.github/workflows/sdk-dotnet.yml` → NuGet ✅
- [ ] `.github/workflows/go-binary.yml` → GitHub Release binary artifacts ✅

## 5. 釋出後驗證

### Registry 確認

- [ ] PyPI — `pip install zhtw==X.Y.Z && zhtw --version`
- [ ] Maven Central — `https://central.sonatype.com/artifact/com.rajatim/zhtw/X.Y.Z`
- [ ] npm (zhtw-js) — `npm view zhtw-js version`
- [ ] npm (zhtw-wasm) — `npm view zhtw-wasm version`
- [ ] crates.io — `https://crates.io/crates/zhtw/X.Y.Z`
- [ ] NuGet — `https://www.nuget.org/packages/Zhtw/X.Y.Z`
- [ ] Go proxy — `curl -s https://proxy.golang.org/github.com/rajatim/zhtw/sdk/go/v4/@latest`（有 ~30 分鐘快取）
- [ ] Homebrew — 更新 `rajatim/homebrew-tap`（SHA256 + version）

### Observability（log.rajatim.com）

- [ ] Exporter 版本一致 — `curl http://localhost:9150/metrics | grep version_info`
- [ ] Dashboard 6 個 SDK 版本面板都顯示 `vX.Y.Z`
- [ ] 無 ghost series（不應有舊版本殘留）

## 6. 常見踩坑

| 坑 | 原因 | 預防 |
|----|------|------|
| Go 版本停在舊版 | 缺 `sdk/go/vX.Y.Z` subdirectory tag | 用 `make release`；手動時記得建雙 tag |
| Maven deploy 失敗 | `pom.xml` 版本跟 tag 不一致 | `make version-check` 先驗證 |
| Prometheus ghost series | 版本 metric 發了 `version="unknown"` | Exporter 已改 skip-when-empty |
| README binary 連結舊版 | `make bump` 不更新 URL 中的 encoded 版本 | 手動搜尋 `v舊版` 確認 |
| Cargo.lock 沒 commit | `make bump` 改了 Cargo.toml 但沒更新 lockfile | bump 後跑 `cargo check` 再 commit |
