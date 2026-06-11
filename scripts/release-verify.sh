#!/usr/bin/env bash
# zhtw 發布後驗證（由 `make release-verify VERSION=x.y.z` 呼叫）
#
# 1. 等待並檢查 6 個 SDK workflow（release 事件觸發）全綠
# 2. 逐一驗證 registry 上的 artifact 可見性
# 3. 半自動更新 Homebrew tap（算 sha256、改 formula、show diff、等確認）
#
# 用法：scripts/release-verify.sh 4.4.0

set -euo pipefail

VERSION="${1:-}"
[ -n "$VERSION" ] || { echo "用法: scripts/release-verify.sh X.Y.Z" >&2; exit 1; }

TAP_DIR="${TAP_DIR:-$HOME/GitHub/homebrew-tap}"
say() { printf '\033[1;36m%s\033[0m\n' "$*"; }
ok()  { printf '  ✅ %s\n' "$*"; }
ng()  { printf '  ⏳ %s\n' "$*"; }

# ────────────────── 1. Workflow 狀態 ──────────────────
say "[1/3] 等待 release 觸發的 workflows（PyPI/Java/TS/Rust/.NET/Go/binaries）"
for i in $(seq 1 30); do
    RUNS="$(gh run list --limit 15 --json status,conclusion,name,event \
        --jq '[.[] | select(.event=="release" or .event=="push")] | .[0:10]')"
    PENDING="$(echo "$RUNS" | python3 -c 'import json,sys; rs=json.load(sys.stdin); print(sum(1 for r in rs if r["status"]!="completed"))')"
    FAILED="$(echo "$RUNS" | python3 -c 'import json,sys; rs=json.load(sys.stdin); [print("  ❌", r["name"]) for r in rs if r.get("conclusion")=="failure"]')"
    if [ -n "$FAILED" ]; then
        echo "$FAILED"
        echo "  ⚠️  有 workflow 失敗，請 gh run list 檢查；registry 驗證照常繼續"
        break
    fi
    if [ "$PENDING" = "0" ]; then
        ok "全部 workflow 完成"
        break
    fi
    ng "還有 $PENDING 個 workflow 進行中…（$i/30，每 30 秒輪詢）"
    sleep 30
done

# ────────────────── 2. Registry 驗證 ──────────────────
say "[2/3] Registry artifact 驗證（Maven Central 同步可能落後 30 分鐘以上）"
check() { # check <名稱> <URL> [grep-pattern]
    local name="$1" url="$2" pat="${3:-}"
    local body
    if body="$(curl -fsSL --max-time 20 -A 'zhtw-release-verify' "$url" 2>/dev/null)"; then
        if [ -z "$pat" ] || echo "$body" | grep -q "$pat"; then
            ok "$name"
            return 0
        fi
    fi
    ng "$name 尚未可見 → $url"
    return 1
}

PASS=0; TOTAL=7
check "PyPI zhtw==$VERSION"       "https://pypi.org/pypi/zhtw/$VERSION/json" && PASS=$((PASS+1)) || true
check "npm zhtw-js@$VERSION"      "https://registry.npmjs.org/zhtw-js/$VERSION" && PASS=$((PASS+1)) || true
check "npm zhtw-wasm@$VERSION"    "https://registry.npmjs.org/zhtw-wasm/$VERSION" && PASS=$((PASS+1)) || true
check "crates.io zhtw@$VERSION"   "https://crates.io/api/v1/crates/zhtw/$VERSION" && PASS=$((PASS+1)) || true
check "NuGet Zhtw $VERSION"       "https://api.nuget.org/v3-flatcontainer/zhtw/index.json" "\"$VERSION\"" && PASS=$((PASS+1)) || true
check "Maven com.rajatim:zhtw:$VERSION" "https://repo1.maven.org/maven2/com/rajatim/zhtw/$VERSION/" && PASS=$((PASS+1)) || true
# 對 Go proxy 的請求本身會觸發模組快取（首次查詢順便暖機）
check "Go proxy sdk/go/v$VERSION" "https://proxy.golang.org/github.com/rajatim/zhtw/sdk/go/v4/@v/v$VERSION.info" && PASS=$((PASS+1)) || true
echo "  → $PASS/$TOTAL 可見（未齊請稍後重跑本指令）"

# ────────────────── 3. Homebrew tap ──────────────────
say "[3/3] Homebrew tap 更新（PyPI sdist sha256）"
if [ ! -d "$TAP_DIR" ]; then
    echo "  ⚠️  找不到 $TAP_DIR，略過（手動：更新 Formula/zhtw.rb 的 url + sha256）"
    exit 0
fi
SDIST_INFO="$(curl -fsSL --max-time 20 "https://pypi.org/pypi/zhtw/$VERSION/json" 2>/dev/null \
    | python3 -c 'import json,sys; d=json.load(sys.stdin); s=[u for u in d["urls"] if u["packagetype"]=="sdist"][0]; print(s["url"], s["digests"]["sha256"])' 2>/dev/null)" || true
if [ -z "$SDIST_INFO" ]; then
    echo "  ⏳ PyPI sdist 尚未可見，稍後重跑本指令再更新 Homebrew"
    exit 0
fi
SDIST_URL="${SDIST_INFO%% *}"
SDIST_SHA="${SDIST_INFO##* }"
echo "  sdist: $SDIST_URL"
echo "  sha256: $SDIST_SHA"

FORMULA="$TAP_DIR/Formula/zhtw.rb"
sed -i '' -E "s|^  url \".*\"|  url \"$SDIST_URL\"|" "$FORMULA"
sed -i '' -E "s|^  sha256 \".*\"|  sha256 \"$SDIST_SHA\"|" "$FORMULA"
(cd "$TAP_DIR" && git --no-pager diff Formula/zhtw.rb)
printf '  推送 homebrew-tap？ [y/N] '
read -r REPLY
if [ "$REPLY" = "y" ] || [ "$REPLY" = "Y" ]; then
    (cd "$TAP_DIR" && git add Formula/zhtw.rb && git commit -m "zhtw $VERSION" && git push)
    ok "homebrew-tap 已更新"
else
    (cd "$TAP_DIR" && git checkout -- Formula/zhtw.rb)
    echo "  已還原 formula（未推送）"
fi

say "✅ 驗證完成。煙霧測試（自選）："
echo "   pip install zhtw==$VERSION && zhtw --version"
echo "   brew update && brew upgrade zhtw"
