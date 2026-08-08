#!/usr/bin/env bash

set -euo pipefail

VERSION="${1:-}"
[[ "$VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || {
    echo "Usage: scripts/release-verify.sh X.Y.Z" >&2
    exit 64
}

ATTEMPTS="${VERIFY_ATTEMPTS:-120}"
INTERVAL="${VERIFY_INTERVAL:-15}"
TAG="v$VERSION"
GO_TAG="sdk/go/v$VERSION"

check_url() {
    local url="$1" pattern="${2:-}" body
    body="$(curl -fsSL --max-time 20 -A zhtw-jenkins-verify "$url" 2>/dev/null)" || return 1
    [ -z "$pattern" ] || grep -Fq "$pattern" <<< "$body"
}

github_api() {
    local url="$1"
    if [ -n "${GH_TOKEN:-}" ]; then
        printf 'Authorization: Bearer %s\n' "$GH_TOKEN" | \
            curl -fsSL --max-time 20 -A zhtw-jenkins-verify --header @- "$url"
    else
        curl -fsSL --max-time 20 -A zhtw-jenkins-verify "$url"
    fi
}

check_all() {
    local pass=0 root_release go_release root_sha go_sha
    root_release="$(github_api \
        "https://api.github.com/repos/rajatim/zhtw/releases/tags/$TAG" 2>/dev/null)" || root_release=''
    go_release="$(github_api \
        "https://api.github.com/repos/rajatim/zhtw/releases/tags/sdk%2Fgo%2Fv$VERSION" 2>/dev/null)" || go_release=''
    [ "$(printf '%s' "$root_release" | jq -r '.tag_name // empty')" = "$TAG" ] && pass=$((pass + 1)) || true
    [ "$(printf '%s' "$go_release" | jq '[.assets[]? | select(.name | test("^(zhtw-(darwin|linux)-(amd64|arm64)\\.tar\\.gz|zhtw-windows-amd64\\.zip|zhtw_checksums\\.txt)$"))] | length')" = 6 ] && \
        pass=$((pass + 1)) || true
    check_url "https://pypi.org/pypi/zhtw/$VERSION/json" && pass=$((pass + 1)) || true
    check_url "https://registry.npmjs.org/zhtw-js/$VERSION" && pass=$((pass + 1)) || true
    check_url "https://registry.npmjs.org/zhtw-wasm/$VERSION" && pass=$((pass + 1)) || true
    check_url "https://crates.io/api/v1/crates/zhtw/$VERSION" && pass=$((pass + 1)) || true
    check_url "https://api.nuget.org/v3-flatcontainer/zhtw/index.json" "\"$VERSION\"" && pass=$((pass + 1)) || true
    check_url "https://repo1.maven.org/maven2/com/rajatim/zhtw/$VERSION/zhtw-$VERSION.pom" && pass=$((pass + 1)) || true
    check_url "https://proxy.golang.org/github.com/rajatim/zhtw/sdk/go/v4/@v/v$VERSION.info" && pass=$((pass + 1)) || true
    check_url "https://raw.githubusercontent.com/rajatim/homebrew-tap/main/Formula/zhtw.rb" "zhtw-$VERSION.tar.gz" && \
        pass=$((pass + 1)) || true

    root_sha="$(git ls-remote https://github.com/rajatim/zhtw.git "refs/tags/$TAG^{}" | awk '{print $1}')"
    go_sha="$(git ls-remote https://github.com/rajatim/zhtw.git "refs/tags/$GO_TAG^{}" | awk '{print $1}')"
    [ -n "$root_sha" ] && [ "$root_sha" = "$go_sha" ] && pass=$((pass + 1)) || true
    printf '%s\n' "$pass"
}

for attempt in $(seq 1 "$ATTEMPTS"); do
    passed="$(check_all)"
    if [ "$passed" -eq 12 ]; then
        printf 'zhtw %s verification passed: 12/12 checks\n' "$VERSION"
        exit 0
    fi
    printf 'Waiting for zhtw %s publication: %s/12 checks (%s/%s)\n' \
        "$VERSION" "$passed" "$attempt" "$ATTEMPTS"
    sleep "$INTERVAL"
done

echo "ERROR: zhtw $VERSION did not pass all release checks" >&2
exit 1
