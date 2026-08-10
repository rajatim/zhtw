# 版本發布核對清單

此舊路徑保留作為相容入口。唯一維護中的核對清單是：

[`docs/releases/RELEASE-CHECKLIST.md`](../releases/RELEASE-CHECKLIST.md)

請勿依賴舊版的 tag 直接發布步驟。zhtw 只走 Jenkins：先完成 `zhtw/build`，再用
`zhtw/verify` 的 `all` 驗證同一份封存候選，最後才可執行 `zhtw/release` 的
`PREVIEW`；使用者明確核准同一組 build/verify 後才可 `PUBLISH_ALL`。GitHub Actions
與手動 registry publish 都不是備援路徑。
