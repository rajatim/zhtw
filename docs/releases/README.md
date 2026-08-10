# Releases

zhtw 的唯一 CI/CD 與公開發布入口是 Jenkins：`zhtw/build` → 同一候選的
`zhtw/verify`（`all`）→ `zhtw/release`（先 `PREVIEW`，明確核准後才發布）。

公開變更說明來自 `CHANGELOG.md` 的 `[Unreleased]`，Jenkins 會把該區塊提升為版本
章節並原樣寫入 GitHub Release notes。完整人工檢查請使用
[`RELEASE-CHECKLIST.md`](RELEASE-CHECKLIST.md)。
