#!/usr/bin/env bash

set -euo pipefail

VERSION="${1:-}"
PAYLOAD_DIR="${2:-}"
[[ "$VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || {
    echo "Usage: scripts/release-verify.sh X.Y.Z [payload-directory]" >&2
    exit 64
}
[ -z "$PAYLOAD_DIR" ] || [ -d "$PAYLOAD_DIR" ] || {
    echo "ERROR: payload directory not found: $PAYLOAD_DIR" >&2
    exit 64
}

ATTEMPTS="${VERIFY_ATTEMPTS:-120}"
INTERVAL="${VERIFY_INTERVAL:-15}"
TOTAL_CHECKS=12
TAG="v$VERSION"
GO_TAG="sdk/go/v$VERSION"
USER_AGENT="zhtw-jenkins-verify"

check_url() {
    local url="$1" pattern="${2:-}" body
    body="$(curl -fsSL --max-time 20 -A "$USER_AGENT" "$url" 2>/dev/null)" || return 1
    [ -z "$pattern" ] || grep -Fq "$pattern" <<< "$body"
}

github_api() {
    local url="$1"
    if [ -n "${GH_TOKEN:-}" ]; then
        printf 'Authorization: Bearer %s\n' "$GH_TOKEN" | \
            curl -fsSL --max-time 20 -A "$USER_AGENT" --header @- "$url"
    else
        curl -fsSL --max-time 20 -A "$USER_AGENT" "$url"
    fi
}

check_all() {
    local pass=0 root_release latest_release go_release root_sha go_sha
    local expected_notes actual_notes go_notes
    local commit_json expected_tree
    root_release="$(github_api \
        "https://api.github.com/repos/rajatim/zhtw/releases/tags/$TAG" 2>/dev/null)" || root_release=''
    latest_release="$(github_api \
        "https://api.github.com/repos/rajatim/zhtw/releases/latest" 2>/dev/null)" || latest_release=''
    go_release="$(github_api \
        "https://api.github.com/repos/rajatim/zhtw/releases/tags/sdk%2Fgo%2Fv$VERSION" 2>/dev/null)" || go_release=''
    printf '%s' "$root_release" | jq -e \
        --arg tag "$TAG" \
        '.tag_name == $tag and .name == $tag and .draft == false and .prerelease == false' \
        >/dev/null && \
        [ "$(printf '%s' "$latest_release" | jq -r '.tag_name // empty')" = "$TAG" ] && \
        pass=$((pass + 1)) || true
    actual_notes="$(printf '%s' "$root_release" | jq -r '.body // ""')"
    if [ -n "$PAYLOAD_DIR" ]; then
        expected_notes="$(cat "$PAYLOAD_DIR/candidate/release-notes.md")"
        [ "$actual_notes" = "$expected_notes" ] && pass=$((pass + 1)) || true
    else
        [ -n "$(printf '%s' "$actual_notes" | tr -d '[:space:]')" ] && pass=$((pass + 1)) || true
    fi
    go_notes="$(printf '%s' "$go_release" | jq -r '.body // ""')"
    if printf '%s' "$go_release" | jq -e \
        --arg tag "$GO_TAG" \
        --arg title "Go CLI $TAG" \
        '.tag_name == $tag and .name == $title and
         .draft == false and .prerelease == false and
         ([.assets[]?.name] | sort) == ([
           "zhtw-darwin-amd64.tar.gz", "zhtw-darwin-arm64.tar.gz",
           "zhtw-linux-amd64.tar.gz", "zhtw-linux-arm64.tar.gz",
           "zhtw-windows-amd64.zip", "zhtw_checksums.txt"
         ] | sort)' >/dev/null && \
        [ "$go_notes" = "Jenkins-built Go CLI for $TAG." ]; then
        pass=$((pass + 1)) || true
    fi
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
    if [ -n "$root_sha" ] && [ "$root_sha" = "$go_sha" ]; then
        if [ -n "$PAYLOAD_DIR" ]; then
            expected_tree="$(tr -d '[:space:]' < "$PAYLOAD_DIR/metadata/candidate-tree-sha")"
            commit_json="$(github_api \
                "https://api.github.com/repos/rajatim/zhtw/git/commits/$root_sha" 2>/dev/null)" || \
                commit_json=''
            [ "$(printf '%s' "$commit_json" | jq -r '.tree.sha // empty')" = "$expected_tree" ] && \
                pass=$((pass + 1)) || true
        else
            pass=$((pass + 1))
        fi
    fi
    printf '%s\n' "$pass"
}

download_matches() {
    local url="$1" expected="$2" destination="$3"
    curl -fsSL --max-time 60 -A "$USER_AGENT" -o "$destination" "$url" 2>/dev/null || return 1
    [ "$(sha256sum "$destination" | cut -d' ' -f1)" = \
      "$(sha256sum "$expected" | cut -d' ' -f1)" ]
}

nuget_semantic_matches() {
    local expected="$1" public="$2"
    python3 - "$expected" "$public" <<'PY'
import sys
import zipfile

ignored = {".signature.p7s", "[Content_Types].xml", "_rels/.rels"}


def authored_files(path: str) -> dict[str, bytes]:
    with zipfile.ZipFile(path) as archive:
        return {
            name: archive.read(name)
            for name in archive.namelist()
            if not name.endswith("/") and name not in ignored
        }


expected_files = authored_files(sys.argv[1])
public_files = authored_files(sys.argv[2])
if not expected_files or expected_files != public_files:
    raise SystemExit(1)
PY
}

verify_exact_payload() (
    [ -n "$PAYLOAD_DIR" ] || return 0
    local temporary pypi_info npm_info crates_info formula expected_url expected_sha
    local file name public_sha local_sha public_url
    local -a files=()
    temporary="$(mktemp -d)"
    trap 'rm -rf -- "$temporary"' EXIT

    while IFS= read -r file; do
        files+=("$file")
    done < <(find "$PAYLOAD_DIR/packages/python" -maxdepth 1 -type f -print | LC_ALL=C sort)
    [ "${#files[@]}" -eq 2 ] || return 1
    pypi_info="$(curl -fsSL --max-time 20 -A "$USER_AGENT" \
        "https://pypi.org/pypi/zhtw/$VERSION/json" 2>/dev/null)" || return 1
    [ "$(printf '%s' "$pypi_info" | jq '.urls | length')" -eq "${#files[@]}" ] || return 1
    for file in "${files[@]}"; do
        name="$(basename "$file")"
        public_sha="$(printf '%s' "$pypi_info" | jq -r --arg name "$name" \
            '.urls[]? | select(.filename == $name) | .digests.sha256')"
        local_sha="$(sha256sum "$file" | cut -d' ' -f1)"
        [ -n "$public_sha" ] && [ "$public_sha" = "$local_sha" ] || return 1
    done

    for name in zhtw-js zhtw-wasm; do
        file="$PAYLOAD_DIR/packages/npm/$name-$VERSION.tgz"
        [ -s "$file" ] || return 1
        npm_info="$(curl -fsSL --max-time 20 -A "$USER_AGENT" \
            "https://registry.npmjs.org/$name/$VERSION" 2>/dev/null)" || return 1
        [ "$(printf '%s' "$npm_info" | jq -r '.dist.shasum // empty')" = \
          "$(sha1sum "$file" | cut -d' ' -f1)" ] || return 1
    done

    file="$PAYLOAD_DIR/packages/crates/zhtw-$VERSION.crate"
    [ -s "$file" ] || return 1
    crates_info="$(curl -fsSL --max-time 20 -A "$USER_AGENT" \
        "https://crates.io/api/v1/crates/zhtw/$VERSION" 2>/dev/null)" || return 1
    [ "$(printf '%s' "$crates_info" | jq -r '.version.checksum // empty')" = \
      "$(sha256sum "$file" | cut -d' ' -f1)" ] || return 1

    file="$PAYLOAD_DIR/packages/nuget/Zhtw.$VERSION.nupkg"
    [ -s "$file" ] || return 1
    curl -fsSL --max-time 60 -A "$USER_AGENT" \
        -o "$temporary/nuget.nupkg" \
        "https://api.nuget.org/v3-flatcontainer/zhtw/$VERSION/zhtw.$VERSION.nupkg" \
        2>/dev/null || return 1
    nuget_semantic_matches "$file" "$temporary/nuget.nupkg" || return 1

    files=()
    while IFS= read -r file; do
        files+=("$file")
    done < <(find "$PAYLOAD_DIR/packages/maven" -maxdepth 1 -type f -print | LC_ALL=C sort)
    [ "${#files[@]}" -eq 4 ] || return 1
    for file in "${files[@]}"; do
        name="$(basename "$file")"
        download_matches \
            "https://repo1.maven.org/maven2/com/rajatim/zhtw/$VERSION/$name" \
            "$file" "$temporary/$name" || return 1
        check_url \
            "https://repo1.maven.org/maven2/com/rajatim/zhtw/$VERSION/$name.asc" || return 1
    done

    files=()
    while IFS= read -r file; do
        files+=("$file")
    done < <(find "$PAYLOAD_DIR/packages/go" -maxdepth 1 -type f -print | LC_ALL=C sort)
    [ "${#files[@]}" -eq 6 ] || return 1
    for file in "${files[@]}"; do
        name="$(basename "$file")"
        public_url="$(github_api \
            "https://api.github.com/repos/rajatim/zhtw/releases/tags/sdk%2Fgo%2Fv$VERSION" | \
            jq -r --arg name "$name" '.assets[]? | select(.name == $name) | .browser_download_url')"
        [ -n "$public_url" ] || return 1
        download_matches "$public_url" "$file" "$temporary/$name" || return 1
    done

    file="$PAYLOAD_DIR/packages/python/zhtw-$VERSION.tar.gz"
    [ -s "$file" ] || return 1
    expected_sha="$(sha256sum "$file" | cut -d' ' -f1)"
    expected_url="$(printf '%s' "$pypi_info" | jq -r \
        '.urls[]? | select(.packagetype == "sdist") | .url')"
    formula="$(curl -fsSL --max-time 20 -A "$USER_AGENT" \
        https://raw.githubusercontent.com/rajatim/homebrew-tap/main/Formula/zhtw.rb 2>/dev/null)" || return 1
    grep -Fq "url \"$expected_url\"" <<< "$formula" || return 1
    grep -Fq "sha256 \"$expected_sha\"" <<< "$formula" || return 1

    printf 'Exact archived payload matches every public artifact for %s\n' "$VERSION"
)

for attempt in $(seq 1 "$ATTEMPTS"); do
    passed="$(check_all)"
    if [ "$passed" -eq "$TOTAL_CHECKS" ] && verify_exact_payload; then
        printf 'zhtw %s verification passed: %s/%s checks\n' \
            "$VERSION" "$TOTAL_CHECKS" "$TOTAL_CHECKS"
        exit 0
    fi
    printf 'Waiting for zhtw %s publication: %s/%s checks (%s/%s)\n' \
        "$VERSION" "$passed" "$TOTAL_CHECKS" "$attempt" "$ATTEMPTS"
    sleep "$INTERVAL"
done

echo "ERROR: zhtw $VERSION did not pass all release checks" >&2
exit 1
