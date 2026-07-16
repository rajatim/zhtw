#!/usr/bin/env bash
# zhtw 一鍵釋出腳本（由 `make release VERSION=x.y.z` 呼叫）
#
# 流程：前置閘門 → 測試 → bump → CHANGELOG 確認 → 人工同意 →
#       commit → 雙 tag（vX.Y.Z + sdk/go/vX.Y.Z）→ push → GitHub Release
#
# GitHub Release 發布後會自動扇出到 6 個 registry：
#   PyPI / Maven Central / npm(zhtw-js + zhtw-wasm) / crates.io / NuGet / Go
# 之後請執行 `make release-verify VERSION=x.y.z` 做發布後驗證。
#
# 用法：
#   scripts/release.sh 4.4.0            # 正式釋出（有 y/N 確認）
#   DRY_RUN=1 scripts/release.sh 4.4.0  # 只跑閘門與計畫，不做任何變更
#   SKIP_JAVA=1 scripts/release.sh ...  # 跳過 Java 本地驗證（不建議）

set -euo pipefail

VERSION="${1:-}"
DRY_RUN="${DRY_RUN:-0}"
SKIP_JAVA="${SKIP_JAVA:-0}"
REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

say()  { printf '\033[1;36m%s\033[0m\n' "$*"; }
ok()   { printf '  ✅ %s\n' "$*"; }
die()  { printf '\033[1;31m❌ %s\033[0m\n' "$*" >&2; exit 1; }
plan() { if [ "$DRY_RUN" = "1" ]; then printf '  [dry-run] %s\n' "$*"; else "$@"; fi; }

# ────────────────────────── 閘門 0：參數 ──────────────────────────
[ -n "$VERSION" ] || die "用法: scripts/release.sh X.Y.Z"
echo "$VERSION" | grep -Eq '^[0-9]+\.[0-9]+\.[0-9]+$' || die "VERSION 格式須為 X.Y.Z（拿到: $VERSION）"

CURRENT="$(grep -E '^version = ' pyproject.toml | sed 's/version = "\(.*\)"/\1/')"
say "🚀 zhtw release: $CURRENT → $VERSION $([ "$DRY_RUN" = "1" ] && echo '（DRY RUN）')"

# ────────────────────────── 閘門 1：git 狀態 ──────────────────────────
say "[1/7] Git 狀態檢查"
BRANCH="$(git branch --show-current)"
[ "$BRANCH" = "main" ] || die "必須在 main 分支釋出（目前: $BRANCH）"
ok "分支 = main"

[ -z "$(git status --porcelain)" ] || die "工作目錄不乾淨，請先 commit 或 stash（release commit 只能包含 bump 變更）"
ok "工作目錄乾淨"

git fetch origin main --quiet
[ "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)" ] || die "main 與 origin/main 不同步，請先 push / pull"
ok "與 origin/main 同步"

for t in "v$VERSION" "sdk/go/v$VERSION"; do
    git rev-parse -q --verify "refs/tags/$t" >/dev/null && die "tag $t 已存在"
done
ok "tag v$VERSION / sdk/go/v$VERSION 均不存在"

gh auth status >/dev/null 2>&1 || die "gh 未登入（gh auth login）"
ok "gh 已認證"

# Dependabot 弱點閘門：medium 以上開放警報 → 擋下（ALLOW_VULNS=1 可逃生，不建議）
ALERTS="$(gh api 'repos/{owner}/{repo}/dependabot/alerts?state=open&per_page=100' \
    --jq '[.[] | select(.security_advisory.severity=="critical" or .security_advisory.severity=="high" or .security_advisory.severity=="medium")] | length' 2>/dev/null || echo "?")"
if [ "$ALERTS" = "?" ]; then
    echo "  ⚠️  無法讀取 Dependabot alerts（API/權限）— 請自行確認 GitHub Security 頁面"
elif [ "$ALERTS" -gt 0 ] && [ "${ALLOW_VULNS:-0}" != "1" ]; then
    gh api 'repos/{owner}/{repo}/dependabot/alerts?state=open&per_page=100' \
        --jq '.[] | "     - [\(.security_advisory.severity)] \(.dependency.package.name) (\(.dependency.manifest_path))"' 2>/dev/null || true
    die "有 $ALERTS 個開放中的 Dependabot 弱點（medium+）— 先修掉，或 ALLOW_VULNS=1 略過（不建議）"
else
    ok "Dependabot 無 medium+ 開放弱點"
fi

# ────────────────────────── 閘門 2：CHANGELOG ──────────────────────────
say "[2/7] CHANGELOG 檢查"
if grep -q "^## \[$VERSION\]" CHANGELOG.md; then
    ok "已有 ## [$VERSION] 區塊"
    PROMOTE_CHANGELOG=0
else
    # [Unreleased] 區塊必須有內容，將自動升級為 [X.Y.Z] - 今天
    UNREL="$(awk '/^## \[Unreleased\]/{flag=1;next}/^## \[/{flag=0}flag' CHANGELOG.md | grep -cv '^\s*$' || true)"
    [ "$UNREL" -gt 0 ] || die "CHANGELOG.md 的 [Unreleased] 是空的，且無 [$VERSION] 區塊 — 請先寫釋出說明（這是人的工作）"
    ok "[Unreleased] 有 $UNREL 行內容 → 將升級為 [$VERSION] - $(date +%F)"
    PROMOTE_CHANGELOG=1
fi

# ────────────────────────── 閘門 3：資料與測試 ──────────────────────────
say "[3/7] 資料與測試（先驗證實際將發布的 SDK data）"
make version-check
make export-check
uv run zhtw validate
uv run python scripts/audit_idempotency.py --sources cn,hk --curated-only --fail-on-issues
ok "版本、SDK data、詞庫與 target idempotency 通過"
make test-python
ok "pytest 通過"
if [ "$SKIP_JAVA" = "1" ]; then
    echo "  ⚠️  SKIP_JAVA=1：跳過 Java 本地驗證（風險自負）"
else
    make test-java
    ok "mvn verify 通過"
fi

# ────────────────────────── 步驟 4：bump + CHANGELOG ──────────────────────────
say "[4/7] 版本同步（mono-versioning，8 處 + README + export）"
if [ "$DRY_RUN" = "1" ]; then
    echo "  [dry-run] make bump VERSION=$VERSION"
    [ "$PROMOTE_CHANGELOG" = "1" ] && echo "  [dry-run] CHANGELOG: [Unreleased] → [$VERSION] - $(date +%F)"
else
    make bump VERSION="$VERSION"
    make export-check
    if [ "$PROMOTE_CHANGELOG" = "1" ]; then
        DATE="$(date +%F)" VER="$VERSION" python3 - <<'PY'
import os
ver, date = os.environ["VER"], os.environ["DATE"]
p = "CHANGELOG.md"
s = open(p, encoding="utf-8").read()
s = s.replace("## [Unreleased]\n",
              f"## [Unreleased]\n\n## [{ver}] - {date}\n", 1)
open(p, "w", encoding="utf-8").write(s)
PY
        ok "CHANGELOG 升級完成"
    fi
fi

# ────────────────────────── 閘門 5：人工同意 ──────────────────────────
say "[5/7] 釋出確認（規則：沒有明確同意不可釋出）"
echo "  將執行：commit → tag v$VERSION + sdk/go/v$VERSION → push → GitHub Release"
echo "  Release 發布會自動觸發：PyPI、Maven Central、npm×2、crates.io、NuGet、Go binaries"
if [ "$DRY_RUN" = "1" ]; then
    echo "  [dry-run] 到此為止，未做任何變更 ✋"
    git status --short | head -5
    exit 0
fi
printf '  確認釋出 v%s？ [y/N] ' "$VERSION"
read -r REPLY
[ "$REPLY" = "y" ] || [ "$REPLY" = "Y" ] || die "已取消（未做 commit/tag）"

# ────────────────────────── 步驟 6：commit + tag + push ──────────────────────────
say "[6/7] Commit、tag、push"
git add -A   # 閘門 1 已保證樹乾淨 → 此處只會包含 bump/CHANGELOG 變更
git commit -m "chore: release v$VERSION"
git tag -a "v$VERSION" -m "v$VERSION"
git tag -a "sdk/go/v$VERSION" -m "sdk/go v$VERSION"
git push origin main "v$VERSION" "sdk/go/v$VERSION"
ok "已推送 main + 雙 tag"

# ────────────────────────── 步驟 7：GitHub Release ──────────────────────────
say "[7/7] GitHub Release（notes 取自 CHANGELOG [$VERSION] 區塊）"
NOTES_FILE="$(mktemp)"
awk -v ver="$VERSION" '$0 ~ "^## \\["ver"\\]"{flag=1;next}/^## \[/{flag=0}flag' CHANGELOG.md > "$NOTES_FILE"
if [ -s "$NOTES_FILE" ]; then
    gh release create "v$VERSION" --title "v$VERSION" --notes-file "$NOTES_FILE"
else
    gh release create "v$VERSION" --title "v$VERSION" --generate-notes
fi
rm -f "$NOTES_FILE"

say "✅ v$VERSION 已釋出。下一步："
echo "   make release-verify VERSION=$VERSION   # 盯 workflow、驗 6 個 registry、更新 Homebrew"
