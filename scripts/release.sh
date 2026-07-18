#!/usr/bin/env bash
# zhtw fail-closed release script (called by `make release VERSION=x.y.z`).

set -euo pipefail

VERSION="${1:-}"
DRY_RUN="${DRY_RUN:-0}"
REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

say() { printf '\033[1;36m%s\033[0m\n' "$*"; }
ok() { printf '  ✅ %s\n' "$*"; }
die() { printf '\033[1;31m❌ %s\033[0m\n' "$*" >&2; exit 1; }

promote_changelog() {
    local version="$1" date="$2"
    VERSION="$version" RELEASE_DATE="$date" python3 - <<'PY'
import os
from pathlib import Path

path = Path("CHANGELOG.md")
text = path.read_text(encoding="utf-8")
version = os.environ["VERSION"]
date = os.environ["RELEASE_DATE"]
text = text.replace(
    "## [Unreleased]\n",
    f"## [Unreleased]\n\n## [{version}] - {date}\n",
    1,
)
path.write_text(text, encoding="utf-8")
PY
}

cleanup_candidate() {
    if [ -n "${CANDIDATE_DIR:-}" ] && [ -d "$CANDIDATE_DIR" ]; then
        git worktree remove --force "$CANDIDATE_DIR" >/dev/null 2>&1 || true
    fi
    if [ -n "${TEMP_DIR:-}" ] && [ -d "$TEMP_DIR" ]; then
        rm -rf "$TEMP_DIR"
    fi
}
trap cleanup_candidate EXIT

[ -n "$VERSION" ] || die "用法: scripts/release.sh X.Y.Z"
[[ "$VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || die "VERSION 格式須為 X.Y.Z（拿到: $VERSION）"

CURRENT="$(sed -n 's/^version = "\(.*\)"/\1/p' pyproject.toml)"
RELEASE_DATE="$(date +%F)"
say "🚀 zhtw release: $CURRENT → $VERSION $([ "$DRY_RUN" = 1 ] && echo '（DRY RUN）')"

say "[1/7] Git 與安全狀態"
[ "$(git branch --show-current)" = main ] || die "必須在 main 分支釋出"
[ -z "$(git status --porcelain)" ] || die "工作目錄不乾淨"
git fetch origin main --quiet
[ "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)" ] || die "main 與 origin/main 不同步"
for tag in "v$VERSION" "sdk/go/v$VERSION"; do
    git rev-parse -q --verify "refs/tags/$tag" >/dev/null && die "tag $tag 已存在"
    git ls-remote --exit-code --tags origin "refs/tags/$tag" >/dev/null 2>&1 && die "遠端 tag $tag 已存在"
done
gh auth status >/dev/null 2>&1 || die "gh 未登入（gh auth login）"

if ! ALERTS="$(gh api 'repos/{owner}/{repo}/dependabot/alerts?state=open&per_page=100' \
    --jq '[.[] | select(.security_advisory.severity=="critical" or .security_advisory.severity=="high" or .security_advisory.severity=="medium")] | length' 2>/dev/null)"; then
    [ "${ALLOW_ALERT_CHECK_FAILURE:-0}" = 1 ] || \
        die "無法讀取 Dependabot alerts（緊急略過需明確設定 ALLOW_ALERT_CHECK_FAILURE=1）"
    echo "  ⚠️  已明確略過 Dependabot alerts API 讀取失敗"
    ALERTS=0
fi
if [ "$ALERTS" -gt 0 ] && [ "${ALLOW_VULNS:-0}" != 1 ]; then
    die "有 $ALERTS 個 medium+ Dependabot 弱點（ALLOW_VULNS=1 可緊急略過）"
fi
ok "分支、同步、tag、認證與安全檢查通過"

say "[2/7] CHANGELOG"
if grep -q "^## \[$VERSION\]" CHANGELOG.md; then
    PROMOTE_CHANGELOG=0
    ok "已有 [$VERSION] 區塊"
else
    UNRELEASED_LINES="$(awk '/^## \[Unreleased\]/{flag=1;next}/^## \[/{flag=0}flag' CHANGELOG.md | grep -cv '^\s*$' || true)"
    [ "$UNRELEASED_LINES" -gt 0 ] || die "CHANGELOG [Unreleased] 無內容"
    PROMOTE_CHANGELOG=1
    ok "將升級 [Unreleased] 為 [$VERSION] - $RELEASE_DATE"
fi

say "[3/7] 在暫存 worktree 測試實際候選版本"
TEMP_DIR="$(mktemp -d)"
CANDIDATE_DIR="$TEMP_DIR/candidate"
CANDIDATE_PATCH="$TEMP_DIR/candidate.patch"
git worktree add --detach --quiet "$CANDIDATE_DIR" HEAD
(
    cd "$CANDIDATE_DIR"
    make bump VERSION="$VERSION"
    if [ "$PROMOTE_CHANGELOG" = 1 ]; then
        promote_changelog "$VERSION" "$RELEASE_DATE"
    fi
    make release-gate
    git diff --check
    git diff --binary > "$CANDIDATE_PATCH"
)
CANDIDATE_HASH="$(git hash-object "$CANDIDATE_PATCH")"
ok "候選版本完整 gate 通過"

if [ "$DRY_RUN" = 1 ]; then
    say "✅ dry-run 完成；原工作樹與遠端均未變更"
    exit 0
fi

say "[4/7] 人工確認並建立 release commit"
printf '  確認釋出 v%s？通過遠端 gate 前不會建立 tag 或 Release [y/N] ' "$VERSION"
read -r REPLY
[[ "$REPLY" = y || "$REPLY" = Y ]] || die "已取消，未修改工作樹"

make bump VERSION="$VERSION"
if [ "$PROMOTE_CHANGELOG" = 1 ]; then
    promote_changelog "$VERSION" "$RELEASE_DATE"
fi
APPLIED_HASH="$(git diff --binary | git hash-object --stdin)"
[ "$APPLIED_HASH" = "$CANDIDATE_HASH" ] || die "正式候選內容與已測試 worktree 不一致"

if [ -n "$(git status --porcelain)" ]; then
    git add -A
    git commit -m "chore: release v$VERSION"
else
    ok "版本與 CHANGELOG 已在目前 commit，沿用現有 HEAD"
fi
RELEASE_SHA="$(git rev-parse HEAD)"
git push origin main
ok "release commit 已推送：$RELEASE_SHA"

say "[5/7] 等待 release commit 的遠端 conformance"
RUN_ID=""
for _ in $(seq 1 60); do
    RUN_ID="$(gh run list --workflow sdk-conformance.yml --event push --commit "$RELEASE_SHA" --limit 10 \
        --json databaseId --jq '.[0].databaseId // empty')"
    [ -n "$RUN_ID" ] && break
    sleep 5
done
[ -n "$RUN_ID" ] || die "找不到 release commit 的 SDK Conformance run"
echo "  run: https://github.com/${GITHUB_REPOSITORY:-rajatim/zhtw}/actions/runs/$RUN_ID"
gh run watch "$RUN_ID" --exit-status || die "遠端 conformance 失敗；未建立 tag 或 Release"
CONCLUSION="$(gh run view "$RUN_ID" --json conclusion --jq .conclusion)"
[ "$CONCLUSION" = success ] || die "遠端 conformance 結果不是 success：$CONCLUSION"
ok "遠端 conformance 通過"

say "[6/7] 建立並推送不可變雙 tag"
git tag -a "v$VERSION" -m "v$VERSION"
git tag -a "sdk/go/v$VERSION" -m "sdk/go v$VERSION"
git push origin "v$VERSION" "sdk/go/v$VERSION"
ok "雙 tag 已推送"

say "[7/7] 建立 GitHub Release"
NOTES_FILE="$(mktemp)"
awk -v version="$VERSION" '$0 ~ "^## \\["version"\\]"{flag=1;next}/^## \[/{flag=0}flag' CHANGELOG.md > "$NOTES_FILE"
if [ -s "$NOTES_FILE" ]; then
    gh release create "v$VERSION" --title "v$VERSION" --notes-file "$NOTES_FILE"
else
    gh release create "v$VERSION" --title "v$VERSION" --generate-notes
fi
rm -f "$NOTES_FILE"

say "✅ v$VERSION 已建立；registry 與 Go binary 只會在 release gate 成功後分派"
echo "   make release-verify VERSION=$VERSION"
