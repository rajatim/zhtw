# 版本發布核對清單

此舊路徑保留作為相容入口。唯一維護中的核對清單是：

[`docs/releases/RELEASE-CHECKLIST.md`](../releases/RELEASE-CHECKLIST.md)

請勿依賴舊版的 tag 直接發布步驟；目前流程必須先通過 release commit 的遠端
conformance，再建立雙 tag 與 GitHub Release，之後由不可變 tag gate 分派發布。
