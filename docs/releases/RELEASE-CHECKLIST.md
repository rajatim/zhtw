# 釋出核對清單

> 機械步驟已由 `scripts/release.sh` 自動把關；本清單只剩**人的判斷**。
> 完整流程說明：`.claude/rules/releasing.md`

## 釋出前（人工判斷）

- [ ] **使用者/Maintainer 明確同意釋出**（最高規則：沒有同意不可釋出）
- [ ] `CHANGELOG.md` 的 `[Unreleased]` 內容**寫給人看**：使用者能否從中判斷要不要升級？
- [ ] 版本號符合語意：breaking → major、新功能 → minor、修復 → patch
  （mono-versioning：6 個 SDK 一律同號，不個別論證）
- [ ] 詞庫有改動時：依 `docs/precision-standard.md` 跑精準度 release gate

## 釋出（一鍵）

```bash
make release-dry VERSION=X.Y.Z   # 預演：閘門 + 測試，不做任何變更
make release VERSION=X.Y.Z       # 正式（含 y/N 確認）
```

指令碼自動把關，失敗即中止、不發布半成品：
main 分支 ✓ 工作樹乾淨 ✓ 與 origin 同步 ✓ tag 不存在 ✓
Dependabot 無 medium+ 弱點 ✓ CHANGELOG 非空 ✓ version/export freshness ✓
暫存 worktree 產生 bump 後候選 ✓ 固定 corpus ✓ 詞庫與 idempotency ✓
全部 SDK 與 Go lint ✓ → 人工確認 → release commit push → 遠端 conformance ✓ →
雙 tag（`vX.Y.Z` + `sdk/go/vX.Y.Z`）→ GitHub Release → 不可變 tag gate →
分派各 registry 與 Go binary 發布

## 釋出後

```bash
make release-verify VERSION=X.Y.Z   # 7 workflows + 7 registries + Homebrew
```

- [ ] 7 個精確對應版本的 workflow 全綠（Conformance / PyPI / Java / TS /
  Rust / .NET / Go binaries）
- [ ] Registry 7 項全可見（Maven Central 可能落後 30 分鐘＋，重跑同指令即可）
- [ ] Homebrew tap 已推送（指令碼半自動，確認 diff 後按 y）

## 出事時（部分 registry 發布失敗）

Maven Central / PyPI artifact **不可變**——同版本號不能重傳成功過的，
但「失敗的」可以重跑：

```bash
gh run list --branch vX.Y.Z       # 找出該版本失敗的 workflow
gh run rerun <run-id>             # 重跑（重新投遞同一 release 事件）
```

若是程式碼問題導致發布失敗：修正 → commit → **升 patch 版重走全流程**，
不要嘗試改歷史或重用版本號。
