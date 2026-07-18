#!/usr/bin/env bash
# Fail-closed post-release verification for one immutable version.

set -euo pipefail

VERSION="${1:-}"
[[ "$VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || {
    echo "用法: scripts/release-verify.sh X.Y.Z" >&2
    exit 1
}

TAG="v$VERSION"
GO_TAG="sdk/go/v$VERSION"
TAP_DIR="${TAP_DIR:-$HOME/GitHub/homebrew-tap}"
WORKFLOW_ATTEMPTS="${WORKFLOW_ATTEMPTS:-60}"
REGISTRY_ATTEMPTS="${REGISTRY_ATTEMPTS:-120}"
VERIFY_INTERVAL="${VERIFY_INTERVAL:-15}"

say() { printf '\033[1;36m%s\033[0m\n' "$*"; }
ok() { printf '  ✅ %s\n' "$*"; }
wait_msg() { printf '  ⏳ %s\n' "$*"; }
die() { printf '  ❌ %s\n' "$*" >&2; exit 1; }

RELEASE_JSON="$(gh release view "$TAG" --json tagName,publishedAt,url 2>/dev/null)" || die "找不到 GitHub Release $TAG"
PUBLISHED_AT="$(printf '%s' "$RELEASE_JSON" | python3 -c 'import json,sys; print(json.load(sys.stdin)["publishedAt"])')"
RELEASE_URL="$(printf '%s' "$RELEASE_JSON" | python3 -c 'import json,sys; print(json.load(sys.stdin)["url"])')"

say "[1/3] 精確追蹤 $TAG 的發布 workflows"
WORKFLOWS=$(cat <<EOF
sdk-conformance.yml|$TAG|release|SDK Conformance
publish.yml|$TAG|workflow_dispatch|Publish to PyPI
sdk-java.yml|$TAG|workflow_dispatch|SDK Java
sdk-typescript.yml|$TAG|workflow_dispatch|SDK TypeScript
sdk-rust.yml|$TAG|workflow_dispatch|SDK Rust
sdk-dotnet.yml|$TAG|workflow_dispatch|SDK .NET
go-binary.yml|$GO_TAG|workflow_dispatch|Go Binary Release
EOF
)

workflow_run() {
    local workflow="$1" branch="$2" event="$3"
    gh run list --workflow "$workflow" --branch "$branch" --event "$event" --limit 20 \
        --json databaseId,status,conclusion,createdAt,url \
        --jq "[.[] | select(.createdAt >= \"$PUBLISHED_AT\")] | sort_by(.createdAt) | reverse | .[0] // {}"
}

WORKFLOWS_OK=0
for attempt in $(seq 1 "$WORKFLOW_ATTEMPTS"); do
    missing=0
    pending=0
    failed=0
    while IFS='|' read -r workflow branch event name; do
        run="$(workflow_run "$workflow" "$branch" "$event")"
        run_id="$(printf '%s' "$run" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("databaseId", ""))')"
        if [ -z "$run_id" ]; then
            missing=$((missing + 1))
            continue
        fi
        status="$(printf '%s' "$run" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("status", ""))')"
        conclusion="$(printf '%s' "$run" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("conclusion", ""))')"
        if [ "$status" != completed ]; then
            pending=$((pending + 1))
        elif [ "$conclusion" != success ]; then
            echo "  ❌ $name run $run_id: $conclusion"
            failed=$((failed + 1))
        fi
    done <<< "$WORKFLOWS"

    [ "$failed" -eq 0 ] || die "$failed 個發布 workflow 失敗；停止 registry/Homebrew 驗證"
    if [ "$missing" -eq 0 ] && [ "$pending" -eq 0 ]; then
        WORKFLOWS_OK=1
        break
    fi
    wait_msg "缺少 $missing、執行中 $pending（$attempt/$WORKFLOW_ATTEMPTS）"
    sleep "$VERIFY_INTERVAL"
done
[ "$WORKFLOWS_OK" -eq 1 ] || die "發布 workflows 等待逾時"
ok "7 個發布 workflow 全部成功"

check_url() {
    local url="$1" pattern="${2:-}" body
    body="$(curl -fsSL --max-time 20 -A 'zhtw-release-verify' "$url" 2>/dev/null)" || return 1
    [ -z "$pattern" ] || grep -q "$pattern" <<< "$body"
}

say "[2/3] 等待 7 個 registry artifact 可見"
REGISTRIES_OK=0
for attempt in $(seq 1 "$REGISTRY_ATTEMPTS"); do
    pass=0
    check_url "https://pypi.org/pypi/zhtw/$VERSION/json" && pass=$((pass + 1)) || true
    check_url "https://registry.npmjs.org/zhtw-js/$VERSION" && pass=$((pass + 1)) || true
    check_url "https://registry.npmjs.org/zhtw-wasm/$VERSION" && pass=$((pass + 1)) || true
    check_url "https://crates.io/api/v1/crates/zhtw/$VERSION" && pass=$((pass + 1)) || true
    check_url "https://api.nuget.org/v3-flatcontainer/zhtw/index.json" "\"$VERSION\"" && pass=$((pass + 1)) || true
    check_url "https://repo1.maven.org/maven2/com/rajatim/zhtw/$VERSION/zhtw-$VERSION.pom" && pass=$((pass + 1)) || true
    check_url "https://proxy.golang.org/github.com/rajatim/zhtw/sdk/go/v4/@v/v$VERSION.info" && pass=$((pass + 1)) || true
    if [ "$pass" -eq 7 ]; then
        REGISTRIES_OK=1
        break
    fi
    wait_msg "$pass/7 可見（$attempt/$REGISTRY_ATTEMPTS）"
    sleep "$VERIFY_INTERVAL"
done
[ "$REGISTRIES_OK" -eq 1 ] || die "registry artifact 等待逾時"
ok "7/7 registry artifact 均可見"

say "[3/3] Homebrew tap idempotent 更新"
if [ ! -d "$TAP_DIR/.git" ]; then
    die "找不到 $TAP_DIR；registry 已驗證，但 Homebrew 尚未完成"
fi
[ -z "$(git -C "$TAP_DIR" status --porcelain)" ] || die "Homebrew tap 工作樹不乾淨：$TAP_DIR"
git -C "$TAP_DIR" pull --ff-only

SDIST_INFO="$(curl -fsSL --max-time 20 "https://pypi.org/pypi/zhtw/$VERSION/json" \
    | python3 -c 'import json,sys; d=json.load(sys.stdin); s=next(u for u in d["urls"] if u["packagetype"]=="sdist"); print(s["url"], s["digests"]["sha256"])')"
SDIST_URL="${SDIST_INFO%% *}"
SDIST_SHA="${SDIST_INFO##* }"
FORMULA="$TAP_DIR/Formula/zhtw.rb"
FORMULA="$FORMULA" SDIST_URL="$SDIST_URL" SDIST_SHA="$SDIST_SHA" python3 - <<'PY'
import os
import re
from pathlib import Path

path = Path(os.environ["FORMULA"])
text = path.read_text(encoding="utf-8")
text, url_count = re.subn(r'^  url ".*"$', f'  url "{os.environ["SDIST_URL"]}"', text, count=1, flags=re.MULTILINE)
text, sha_count = re.subn(r'^  sha256 ".*"$', f'  sha256 "{os.environ["SDIST_SHA"]}"', text, count=1, flags=re.MULTILINE)
if url_count != 1 or sha_count != 1:
    raise SystemExit("Homebrew formula url/sha256 fields not found")
path.write_text(text, encoding="utf-8")
PY

if git -C "$TAP_DIR" diff --quiet -- Formula/zhtw.rb; then
    ok "Homebrew formula 已是 $VERSION"
else
    git -C "$TAP_DIR" --no-pager diff -- Formula/zhtw.rb
    printf '  推送 homebrew-tap？ [y/N] '
    read -r REPLY
    if [[ "$REPLY" = y || "$REPLY" = Y ]]; then
        git -C "$TAP_DIR" add Formula/zhtw.rb
        git -C "$TAP_DIR" commit -m "zhtw $VERSION"
        git -C "$TAP_DIR" push
        ok "homebrew-tap 已更新"
    else
        git -C "$TAP_DIR" restore -- Formula/zhtw.rb
        die "已還原 formula；Homebrew 尚未更新"
    fi
fi

say "✅ $TAG fail-closed 驗證完成：$RELEASE_URL"
