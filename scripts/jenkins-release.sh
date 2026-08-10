#!/usr/bin/env bash

set -euo pipefail

ACTION="${1:-}"
PAYLOAD_DIR="${2:-}"
TOOLS_ROOT="${ZHTW_TOOLS_ROOT:-$HOME/.local/share/zhtw-tools}"
REGISTRY_USER_AGENT="${ZHTW_REGISTRY_USER_AGENT:-zhtw-jenkins-release}"
export PATH="$HOME/.cargo/bin:$TOOLS_ROOT/dotnet:$TOOLS_ROOT/go/bin:$TOOLS_ROOT/wasm-pack:$PATH"

die() {
    printf 'ERROR: %s\n' "$*" >&2
    exit 64
}

require_jenkins_release_runtime() {
    [ "${CI_PROVIDER:-}" = jenkins ] || die "Release actions require Jenkins"
    [ "${ZHTW_JENKINS_RELEASE:-}" = 1 ] || die "Release actions require zhtw/release"
    [ "${JOB_NAME:-}" = zhtw/release ] || die "JOB_NAME must be zhtw/release"
    [ -n "${JENKINS_URL:-}" ] || die "JENKINS_URL is required for publication"
    [ -n "${BUILD_TAG:-}" ] || die "BUILD_TAG is required for publication"
    [ -n "${WORKSPACE:-}" ] || die "WORKSPACE is required for publication"
}

secret_runtime_root() {
    local root="${ZHTW_SECRET_RUNTIME_ROOT:-}"
    [ -n "$root" ] || die "ZHTW_SECRET_RUNTIME_ROOT is required for publication"
    [ -n "${WORKSPACE:-}" ] || die "WORKSPACE is required for publication"
    case "$root" in
        "$WORKSPACE"/*) ;;
        *) die "ZHTW_SECRET_RUNTIME_ROOT must stay inside WORKSPACE" ;;
    esac
    mkdir -p "$root"
    chmod 700 "$root"
    printf '%s\n' "$root"
}

require_common() {
    local name
    for name in SOURCE_SHA CANDIDATE_TREE_SHA RELEASE_VERSION VERSION_TAG; do
        [ -n "${!name:-}" ] || die "$name is required"
    done
    [ -d "$PAYLOAD_DIR" ] || die "Payload directory not found: $PAYLOAD_DIR"
    [[ "$SOURCE_SHA" =~ ^[0-9a-f]{40}$ ]] || die "SOURCE_SHA must be a full Git SHA"
    [[ "$CANDIDATE_TREE_SHA" =~ ^[0-9a-f]{40}$ ]] || die "CANDIDATE_TREE_SHA must be a full Git tree SHA"
    [[ "$RELEASE_VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || die "Invalid RELEASE_VERSION"
    [ "$VERSION_TAG" = "v$RELEASE_VERSION" ] || die "VERSION_TAG does not match RELEASE_VERSION"
}

candidate_tree() {
    local temporary_index
    temporary_index="$(mktemp)"
    rm -f "$temporary_index"
    GIT_INDEX_FILE="$temporary_index" git read-tree HEAD
    GIT_INDEX_FILE="$temporary_index" git add -u
    GIT_INDEX_FILE="$temporary_index" git write-tree
    rm -f "$temporary_index"
}

prepare_candidate() {
    require_common
    [ "$(git rev-parse HEAD)" = "$SOURCE_SHA" ] || die "Checkout is not SOURCE_SHA"
    [ -z "$(git status --porcelain --untracked-files=no)" ] || die "Checkout is not clean"
    [ "$(tr -d '[:space:]' < "$PAYLOAD_DIR/metadata/source-sha")" = "$SOURCE_SHA" ]
    [ "$(tr -d '[:space:]' < "$PAYLOAD_DIR/metadata/candidate-tree-sha")" = "$CANDIDATE_TREE_SHA" ]
    git apply --check "$PAYLOAD_DIR/candidate/release.patch"
    git apply "$PAYLOAD_DIR/candidate/release.patch"
    [ "$(candidate_tree)" = "$CANDIDATE_TREE_SHA" ] || die "Reconstructed candidate tree mismatch"
    make version-check
    git diff --check
}

local_release_sha() {
    local root_sha go_sha
    root_sha="$(git rev-parse -q --verify "refs/tags/$VERSION_TAG^{commit}" || true)"
    go_sha="$(git rev-parse -q --verify "refs/tags/sdk/go/$VERSION_TAG^{commit}" || true)"
    [ -n "$root_sha" ] && [ -n "$go_sha" ] || return 1
    [ "$root_sha" = "$go_sha" ] || die "Root and Go tags point to different commits"
    printf '%s\n' "$root_sha"
}

verify_release_commit() {
    local release_sha="$1"
    [ "$(git rev-parse "$release_sha^{tree}")" = "$CANDIDATE_TREE_SHA" ] || \
        die "Published tag does not match the archived candidate tree"
    git merge-base --is-ancestor "$SOURCE_SHA" "$release_sha" || \
        die "Published release is not descended from the archived source"
}

preview_release() {
    require_common
    local remote_main release_sha remote_tree
    git fetch --quiet origin main '+refs/tags/*:refs/tags/*'
    remote_main="$(git rev-parse refs/remotes/origin/main)"
    if release_sha="$(local_release_sha)"; then
        verify_release_commit "$release_sha"
        [ "$remote_main" = "$release_sha" ] || die "Tags exist but origin/main is not the release commit"
        printf 'Existing immutable release is valid: %s\n' "$release_sha"
        return
    fi
    if [ "$remote_main" = "$SOURCE_SHA" ]; then
        printf 'Release preview is ready from source %s\n' "$SOURCE_SHA"
        return
    fi
    remote_tree="$(git rev-parse "$remote_main^{tree}")"
    if [ "$remote_tree" = "$CANDIDATE_TREE_SHA" ] && git merge-base --is-ancestor "$SOURCE_SHA" "$remote_main"; then
        printf 'Release commit exists without the complete tag set: %s\n' "$remote_main"
        return
    fi
    die "origin/main moved to unrelated source after the archived build"
}

ensure_release_asset() {
    local tag="$1" file="$2" name temporary downloaded_sha expected_sha
    name="$(basename "$file")"
    temporary="$(mktemp -d)"
    if gh release download "$tag" --pattern "$name" --dir "$temporary" >/dev/null 2>&1; then
        expected_sha="$(sha256sum "$file" | cut -d' ' -f1)"
        downloaded_sha="$(sha256sum "$temporary/$name" | cut -d' ' -f1)"
        rm -rf -- "$temporary"
        [ "$expected_sha" = "$downloaded_sha" ] || die "Existing GitHub asset differs: $name"
        printf 'GitHub asset already matches: %s\n' "$name"
    else
        rm -rf -- "$temporary"
        gh release upload "$tag" "$file"
    fi
}

publish_git() {
    require_common
    [ -n "${GH_TOKEN:-}" ] || die "GH_TOKEN is required"
    local remote_main remote_tree release_sha root_sha go_sha commit_created
    git fetch --quiet origin main '+refs/tags/*:refs/tags/*'
    remote_main="$(git rev-parse refs/remotes/origin/main)"
    root_sha="$(git rev-parse -q --verify "refs/tags/$VERSION_TAG^{commit}" || true)"
    go_sha="$(git rev-parse -q --verify "refs/tags/sdk/go/$VERSION_TAG^{commit}" || true)"
    commit_created=0

    if [ -n "$root_sha" ] || [ -n "$go_sha" ]; then
        release_sha="${root_sha:-$go_sha}"
        [ -z "$root_sha" ] || [ "$root_sha" = "$release_sha" ] || die "Root tag mismatch"
        [ -z "$go_sha" ] || [ "$go_sha" = "$release_sha" ] || die "Go tag mismatch"
        verify_release_commit "$release_sha"
        [ "$remote_main" = "$release_sha" ] || die "Existing tag is not the origin/main release commit"
    elif [ "$remote_main" = "$SOURCE_SHA" ]; then
        git config user.name Jenkins
        git config user.email jenkins@tim-dev
        git add -u
        [ "$(git write-tree)" = "$CANDIDATE_TREE_SHA" ] || die "Candidate tree changed before commit"
        git commit -m "chore: 發布 $VERSION_TAG"
        release_sha="$(git rev-parse HEAD)"
        commit_created=1
    else
        remote_tree="$(git rev-parse "$remote_main^{tree}")"
        [ "$remote_tree" = "$CANDIDATE_TREE_SHA" ] || die "origin/main moved after candidate build"
        git merge-base --is-ancestor "$SOURCE_SHA" "$remote_main" || die "Existing candidate is not forward-only"
        release_sha="$remote_main"
    fi

    git config user.name Jenkins
    git config user.email jenkins@tim-dev
    if ! git rev-parse -q --verify "refs/tags/$VERSION_TAG" >/dev/null; then
        git tag -a "$VERSION_TAG" "$release_sha" -m "$VERSION_TAG"
    fi
    if ! git rev-parse -q --verify "refs/tags/sdk/go/$VERSION_TAG" >/dev/null; then
        git tag -a "sdk/go/$VERSION_TAG" "$release_sha" -m "sdk/go $VERSION_TAG"
    fi
    [ "$(git rev-parse "$VERSION_TAG^{commit}")" = "$release_sha" ]
    [ "$(git rev-parse "sdk/go/$VERSION_TAG^{commit}")" = "$release_sha" ]

    if [ "$commit_created" = 1 ]; then
        git push --atomic origin \
            "$release_sha:refs/heads/main" \
            "refs/tags/$VERSION_TAG" \
            "refs/tags/sdk/go/$VERSION_TAG"
    else
        git push --atomic origin "refs/tags/$VERSION_TAG" "refs/tags/sdk/go/$VERSION_TAG"
    fi

    if ! gh release view "$VERSION_TAG" >/dev/null 2>&1; then
        gh release create "$VERSION_TAG" --title "$VERSION_TAG" \
            --notes-file "$PAYLOAD_DIR/candidate/release-notes.md" --latest
    fi
    if ! gh release view "sdk/go/$VERSION_TAG" >/dev/null 2>&1; then
        gh release create "sdk/go/$VERSION_TAG" --title "Go CLI $VERSION_TAG" \
            --notes "Jenkins-built Go CLI for $VERSION_TAG." --latest=false
    fi
    local asset
    for asset in "$PAYLOAD_DIR"/packages/go/*.tar.gz \
                 "$PAYLOAD_DIR"/packages/go/*.zip \
                 "$PAYLOAD_DIR"/packages/go/zhtw_checksums.txt; do
        ensure_release_asset "sdk/go/$VERSION_TAG" "$asset"
    done
    printf '%s\n' "$release_sha" > "$PAYLOAD_DIR/metadata/release-sha"
}

ensure_git_release() {
    local release_sha
    release_sha="$(local_release_sha)" || die "Publish the immutable Git release first"
    verify_release_commit "$release_sha"
}

pypi_release_json() {
    curl -fsS --max-time 20 -A "$REGISTRY_USER_AGENT" \
        "https://pypi.org/pypi/zhtw/$RELEASE_VERSION/json"
}

pypi_file_matches() {
    local file="$1" info public_sha expected_sha name
    info="$(pypi_release_json 2>/dev/null)" || return 2
    name="$(basename "$file")"
    public_sha="$(printf '%s' "$info" | jq -r --arg name "$name" \
        '.urls[]? | select(.filename == $name) | .digests.sha256')"
    [ -n "$public_sha" ] || return 1
    expected_sha="$(sha256sum "$file" | cut -d' ' -f1)"
    [ "$public_sha" = "$expected_sha" ] || die "Existing PyPI file differs: $name"
}

wait_for_pypi_file() {
    local file="$1" attempt result
    for attempt in $(seq 1 120); do
        if pypi_file_matches "$file"; then
            printf 'PyPI file is visible and exact: %s\n' "$(basename "$file")"
            return
        else
            result=$?
        fi
        if [ "$result" -eq 2 ]; then
            printf 'PyPI metadata request failed; retrying (%s/120)\n' "$attempt" >&2
        fi
        sleep 15
    done
    die "PyPI did not expose the exact file before timeout: $(basename "$file")"
}

upload_pypi_file() {
    local file="$1"
    TWINE_USERNAME=__token__ TWINE_PASSWORD="$PYPI_TOKEN" \
        UV_CACHE_DIR="${UV_CACHE_DIR:-$HOME/.cache/uv}" \
        uvx --from twine==6.1.0 twine upload --non-interactive "$file"
}

npm_tarball_matches() {
    local package_name="$1" tarball="$2" info public_sha expected_sha
    info="$(curl -fsS --max-time 20 -A "$REGISTRY_USER_AGENT" \
        "https://registry.npmjs.org/$package_name/$RELEASE_VERSION" 2>/dev/null)" || return 1
    public_sha="$(printf '%s' "$info" | jq -r '.dist.shasum // empty')"
    [ -n "$public_sha" ] || return 1
    expected_sha="$(sha1sum "$tarball" | cut -d' ' -f1)"
    [ "$public_sha" = "$expected_sha" ] || \
        die "Existing npm package differs: $package_name@$RELEASE_VERSION"
}

crate_matches() {
    local crate="$1" info public_sha expected_sha
    info="$(curl -fsS --max-time 20 -A "$REGISTRY_USER_AGENT" \
        "https://crates.io/api/v1/crates/zhtw/$RELEASE_VERSION" 2>/dev/null)" || return 1
    public_sha="$(printf '%s' "$info" | jq -r '.version.checksum // empty')"
    [ -n "$public_sha" ] || return 1
    expected_sha="$(sha256sum "$crate" | cut -d' ' -f1)"
    [ "$public_sha" = "$expected_sha" ] || \
        die "Existing crates.io package differs: zhtw@$RELEASE_VERSION"
}

download_matches() {
    local url="$1" expected="$2" temporary actual_sha expected_sha
    temporary="$(mktemp -d)"
    if ! curl -fsSL --max-time 60 -A "$REGISTRY_USER_AGENT" \
        -o "$temporary/download" "$url" 2>/dev/null; then
        rm -rf -- "$temporary"
        return 1
    fi
    actual_sha="$(sha256sum "$temporary/download" | cut -d' ' -f1)"
    expected_sha="$(sha256sum "$expected" | cut -d' ' -f1)"
    rm -rf -- "$temporary"
    [ "$actual_sha" = "$expected_sha" ]
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

nuget_package_matches() {
    local package="$1" temporary
    temporary="$(mktemp -d)"
    if ! curl -fsSL --max-time 60 -A "$REGISTRY_USER_AGENT" \
        -o "$temporary/public.nupkg" \
        "https://api.nuget.org/v3-flatcontainer/zhtw/$RELEASE_VERSION/zhtw.$RELEASE_VERSION.nupkg" \
        2>/dev/null; then
        rm -rf -- "$temporary"
        die "Could not download existing NuGet package: Zhtw.$RELEASE_VERSION"
    fi
    nuget_semantic_matches "$package" "$temporary/public.nupkg" || {
        rm -rf -- "$temporary"
        die "Existing NuGet package differs: Zhtw.$RELEASE_VERSION"
    }
    rm -rf -- "$temporary"
}

maven_artifacts_match() {
    local file name count=0
    for file in "$PAYLOAD_DIR"/packages/maven/*; do
        [ -f "$file" ] || continue
        count=$((count + 1))
        name="$(basename "$file")"
        download_matches \
            "https://repo1.maven.org/maven2/com/rajatim/zhtw/$RELEASE_VERSION/$name" \
            "$file" || die "Existing Maven Central artifact differs: $name"
    done
    [ "$count" -eq 4 ] || die "Expected four archived Maven artifacts, found $count"
}

registry_exists() {
    local url status
    case "$1" in
        pypi) url="https://pypi.org/pypi/zhtw/$RELEASE_VERSION/json" ;;
        npm-js) url="https://registry.npmjs.org/zhtw-js/$RELEASE_VERSION" ;;
        npm-wasm) url="https://registry.npmjs.org/zhtw-wasm/$RELEASE_VERSION" ;;
        crates) url="https://crates.io/api/v1/crates/zhtw/$RELEASE_VERSION" ;;
        nuget) url="https://api.nuget.org/v3-flatcontainer/zhtw/$RELEASE_VERSION/zhtw.$RELEASE_VERSION.nupkg" ;;
        maven) url="https://repo1.maven.org/maven2/com/rajatim/zhtw/$RELEASE_VERSION/zhtw-$RELEASE_VERSION.pom" ;;
        go) url="https://proxy.golang.org/github.com/rajatim/zhtw/sdk/go/v4/@v/v$RELEASE_VERSION.info" ;;
        *) die "Unknown registry: $1" ;;
    esac
    status="$(curl -sSL --max-time 20 -A "$REGISTRY_USER_AGENT" \
        --output /dev/null --write-out '%{http_code}' "$url")" || return 2
    case "$status" in
        200) return 0 ;;
        404) return 1 ;;
        *) return 2 ;;
    esac
}

wait_for_registry() {
    local target="$1" attempt result
    for attempt in $(seq 1 120); do
        if registry_exists "$target"; then
            printf '%s %s is visible\n' "$target" "$RELEASE_VERSION"
            return
        else
            result=$?
        fi
        if [ "$result" -eq 2 ]; then
            printf '%s registry request failed; retrying (%s/120)\n' \
                "$target" "$attempt" >&2
        fi
        sleep 15
    done
    die "$target did not expose $RELEASE_VERSION before timeout"
}

preflight_git() {
    local tap_dir="${1:-}"
    require_common
    [ -n "${GH_TOKEN:-}" ] || die "GH_TOKEN is required"
    [ -d "$tap_dir/.git" ] || die "Homebrew tap preflight checkout is required"
    local login push_permission remote_main
    login="$(gh api user --jq '.login')"
    [ "$login" = rajatim ] || die "GitHub token belongs to an unexpected account: $login"
    push_permission="$(gh api repos/rajatim/zhtw --jq '.permissions.push')"
    [ "$push_permission" = true ] || die "GitHub token cannot write rajatim/zhtw"
    remote_main="$(git rev-parse refs/remotes/origin/main)"
    git push --dry-run origin "$remote_main:refs/heads/main" >/dev/null
    git -C "$tap_dir" push --dry-run origin HEAD:refs/heads/main >/dev/null
    printf 'GitHub API and SSH write credential preflight passed for zhtw and Homebrew\n'
}

preflight_pypi() {
    require_common
    [ -n "${PYPI_TOKEN:-}" ] || die "PYPI_TOKEN is required"
    [[ "$PYPI_TOKEN" =~ ^pypi-[A-Za-z0-9_-]{85,}$ ]] || die "PyPI token format is invalid"
    local runtime_root response_file auth status
    runtime_root="$(secret_runtime_root)"
    response_file="$(mktemp "$runtime_root/pypi-preflight.XXXXXX")"
    auth="$(printf '%s' "__token__:$PYPI_TOKEN" | base64 | tr -d '\n')"
    status="$(
        printf 'Authorization: Basic %s\n' "$auth" | \
            curl -sS --max-time 20 -A "$REGISTRY_USER_AGENT" --header @- \
                --output "$response_file" --write-out '%{http_code}' \
                --form ':action=file_upload' --form 'protocol_version=1' \
                https://upload.pypi.org/legacy/
    )"
    rm -f "$response_file"
    [ "$status" = 400 ] || die "PyPI rejected the project token during non-uploading authentication check (HTTP $status)"
    printf 'PyPI project token authentication preflight passed\n'
}

preflight_npm() {
    require_common
    [ -n "${NODE_AUTH_TOKEN:-}" ] || die "NODE_AUTH_TOKEN is required"
    [ -n "${NPM_TOKEN_EXPIRES:-}" ] || die "NPM_TOKEN_EXPIRES is required"
    local expires_epoch minimum_epoch runtime_root temporary_config login access
    expires_epoch="$(date -u -d "$NPM_TOKEN_EXPIRES" +%s 2>/dev/null)" || die "Invalid npm token expiry: $NPM_TOKEN_EXPIRES"
    minimum_epoch="$(( $(date -u +%s) + 7 * 24 * 60 * 60 ))"
    [ "$expires_epoch" -gt "$minimum_epoch" ] || die "npm token expires within seven days: $NPM_TOKEN_EXPIRES"
    runtime_root="$(secret_runtime_root)"
    temporary_config="$(mktemp "$runtime_root/npmrc.XXXXXX")"
    chmod 600 "$temporary_config"
    printf '%s\n' \
        'registry=https://registry.npmjs.org/' \
        '//registry.npmjs.org/:_authToken=${NODE_AUTH_TOKEN}' > "$temporary_config"
    login="$(NPM_CONFIG_USERCONFIG="$temporary_config" npm whoami --registry=https://registry.npmjs.org/)"
    [ "$login" = rajatim ] || die "npm token belongs to an unexpected account: $login"
    access="$(NPM_CONFIG_USERCONFIG="$temporary_config" npm access list packages rajatim --json \
        --registry=https://registry.npmjs.org/)"
    printf '%s' "$access" | jq -e \
        '(."zhtw-js" == "read-write") and (."zhtw-wasm" == "read-write")' >/dev/null || \
        die "npm token does not report read-write access to both packages"
    rm -f "$temporary_config"
    printf 'npm token preflight passed for both packages; expiry=%s\n' "$NPM_TOKEN_EXPIRES"
}

preflight_crates() {
    require_common
    [ -n "${CARGO_REGISTRY_TOKEN:-}" ] || die "CARGO_REGISTRY_TOKEN is required"
    local identity
    identity="$(
        printf 'Authorization: %s\n' "$CARGO_REGISTRY_TOKEN" | \
            curl -fsS --max-time 20 -A "$REGISTRY_USER_AGENT" --header @- \
                https://crates.io/api/v1/me
    )"
    printf '%s' "$identity" | jq -e '.user.login == "rajatim"' >/dev/null || \
        die "crates.io token belongs to an unexpected account"
    printf 'crates.io token authentication preflight passed\n'
}

preflight_nuget() {
    require_common
    [ -n "${NUGET_API_KEY:-}" ] || die "NUGET_API_KEY is required"
    local verification key
    verification="$(
        printf 'X-NuGet-ApiKey: %s\nX-NuGet-Protocol-Version: 4.1.0\n' "$NUGET_API_KEY" | \
            curl -fsS --max-time 20 --request POST --header @- \
                https://www.nuget.org/api/v2/package/create-verification-key/Zhtw
    )"
    key="$(printf '%s' "$verification" | jq -r '.Key // .key // empty')"
    [ -n "$key" ] || die "NuGet did not issue a verification key"
    printf 'X-NuGet-ApiKey: %s\nX-NuGet-Protocol-Version: 4.1.0\n' "$key" | \
        curl -fsS --max-time 20 --header @- \
            https://www.nuget.org/api/v2/verifykey/Zhtw >/dev/null
    unset key verification
    printf 'NuGet package-scoped API key preflight passed\n'
}

preflight_maven() {
    require_common
    [ -n "${CENTRAL_USERNAME:-}" ] || die "CENTRAL_USERNAME is required"
    [ -n "${CENTRAL_PASSWORD:-}" ] || die "CENTRAL_PASSWORD is required"
    [ -n "${GPG_PRIVATE_KEY:-}" ] || die "GPG_PRIVATE_KEY is required"
    [ -n "${GPG_PASSPHRASE:-}" ] || die "GPG_PASSPHRASE is required"
    local runtime_root temporary auth response status
    runtime_root="$(secret_runtime_root)"
    temporary="$(mktemp -d "$runtime_root/maven-preflight.XXXXXX")"
    export GNUPGHOME="$temporary/gnupg"
    mkdir -m 700 "$GNUPGHOME"
    printf '%s' "$GPG_PRIVATE_KEY" | gpg --batch --import >/dev/null
    printf 'zhtw Maven signing preflight\n' > "$temporary/message"
    sign_maven_file "$temporary/message"
    gpg --batch --verify "$temporary/message.asc" "$temporary/message" >/dev/null 2>&1

    auth="$(printf '%s:%s' "$CENTRAL_USERNAME" "$CENTRAL_PASSWORD" | base64 | tr -d '\n')"
    response="$temporary/central-response"
    status="$(
        printf 'Authorization: Bearer %s\n' "$auth" | \
            curl -sS --max-time 20 --request POST --header @- \
                --output "$response" --write-out '%{http_code}' \
                'https://central.sonatype.com/api/v1/publisher/status?id=00000000-0000-0000-0000-000000000000'
    )"
    case "$status" in
        400|404) ;;
        *) rm -rf -- "$temporary"; die "Maven Central token authentication failed (HTTP $status)" ;;
    esac
    rm -rf -- "$temporary"
    unset GNUPGHOME
    printf 'Maven Central token and GPG signing preflight passed\n'
}

publish_pypi() {
    require_common
    ensure_git_release
    [ -n "${PYPI_TOKEN:-}" ] || die "PYPI_TOKEN is required"
    local file registry_result release_exists=0 match_result
    local -a files=() missing=()
    while IFS= read -r file; do
        files+=("$file")
    done < <(find "$PAYLOAD_DIR/packages/python" -maxdepth 1 -type f -print | LC_ALL=C sort)
    [ "${#files[@]}" -eq 2 ] || die "Expected exactly two Python distributions"
    if registry_exists pypi; then
        release_exists=1
    else
        registry_result=$?
        [ "$registry_result" -eq 1 ] || die "Could not determine whether PyPI $RELEASE_VERSION exists"
    fi
    for file in "${files[@]}"; do
        if [ "$release_exists" -eq 1 ] && pypi_file_matches "$file"; then
            printf 'PyPI file already matches: %s\n' "$(basename "$file")"
        else
            match_result=$?
            if [ "$release_exists" -eq 1 ] && [ "$match_result" -eq 2 ]; then
                die "Could not read PyPI file metadata: $(basename "$file")"
            fi
            missing+=("$file")
        fi
    done
    if [ "${#missing[@]}" -eq 0 ]; then
        printf 'PyPI %s is complete and exact; skipping\n' "$RELEASE_VERSION"
        return
    fi
    for file in "${missing[@]}"; do
        upload_pypi_file "$file"
        wait_for_pypi_file "$file"
    done
    for file in "${files[@]}"; do
        if ! pypi_file_matches "$file"; then
            die "PyPI release remains incomplete or unreadable: $(basename "$file")"
        fi
    done
}

publish_npm() {
    local target="$1" package_name tarball temporary_config runtime_root
    require_common
    ensure_git_release
    [ -n "${NODE_AUTH_TOKEN:-}" ] || die "NODE_AUTH_TOKEN is required"
    case "$target" in
        npm-js) package_name=zhtw-js ;;
        npm-wasm) package_name=zhtw-wasm ;;
        *) die "Unknown npm target: $target" ;;
    esac
    tarball="$PAYLOAD_DIR/packages/npm/$package_name-$RELEASE_VERSION.tgz"
    [ -s "$tarball" ] || die "Missing npm tarball: $tarball"
    if registry_exists "$target"; then
        npm_tarball_matches "$package_name" "$tarball"
        printf '%s %s already exists and matches; skipping\n' "$package_name" "$RELEASE_VERSION"
        return
    else
        local registry_result=$?
        [ "$registry_result" -eq 1 ] || die "Could not determine whether $package_name $RELEASE_VERSION exists"
    fi
    runtime_root="$(secret_runtime_root)"
    temporary_config="$(mktemp "$runtime_root/npmrc.XXXXXX")"
    chmod 600 "$temporary_config"
    printf '%s\n' \
        'registry=https://registry.npmjs.org/' \
        '//registry.npmjs.org/:_authToken=${NODE_AUTH_TOKEN}' > "$temporary_config"
    NPM_CONFIG_USERCONFIG="$temporary_config" npm publish "$tarball" --access public
    rm -f "$temporary_config"
    wait_for_registry "$target"
}

publish_crates() {
    require_common
    ensure_git_release
    [ -n "${CARGO_REGISTRY_TOKEN:-}" ] || die "CARGO_REGISTRY_TOKEN is required"
    local crate expected actual
    crate="$PAYLOAD_DIR/packages/crates/zhtw-$RELEASE_VERSION.crate"
    [ -s "$crate" ] || die "Missing archived crate: $crate"
    if registry_exists crates; then
        crate_matches "$crate"
        printf 'crates.io %s already exists and matches; skipping\n' "$RELEASE_VERSION"
        return
    else
        local registry_result=$?
        [ "$registry_result" -eq 1 ] || die "Could not determine whether crates.io $RELEASE_VERSION exists"
    fi
    expected="$(sha256sum "$crate" | cut -d' ' -f1)"
    rm -f sdk/rust/target/package/zhtw-"$RELEASE_VERSION".crate
    cargo package --manifest-path sdk/rust/zhtw/Cargo.toml --allow-dirty --no-verify
    actual="$(sha256sum "sdk/rust/target/package/zhtw-$RELEASE_VERSION.crate" | cut -d' ' -f1)"
    [ "$expected" = "$actual" ] || die "Cargo repack differs from the archived crate"
    cargo publish --manifest-path sdk/rust/zhtw/Cargo.toml --allow-dirty --no-verify
    wait_for_registry crates
}

publish_nuget() {
    require_common
    ensure_git_release
    [ -n "${NUGET_API_KEY:-}" ] || die "NUGET_API_KEY is required"
    local package
    package="$PAYLOAD_DIR/packages/nuget/Zhtw.$RELEASE_VERSION.nupkg"
    [ -s "$package" ] || die "Missing NuGet package: $package"
    if registry_exists nuget; then
        nuget_package_matches "$package"
        printf 'NuGet %s already exists and matches; skipping\n' "$RELEASE_VERSION"
        return
    else
        local registry_result=$?
        [ "$registry_result" -eq 1 ] || die "Could not determine whether NuGet $RELEASE_VERSION exists"
    fi
    printf 'X-NuGet-ApiKey: %s\nX-NuGet-Protocol-Version: 4.1.0\n' "$NUGET_API_KEY" | \
        curl -fsS --request PUT --header @- \
        --form "package=@$package;type=application/octet-stream" \
        https://www.nuget.org/api/v2/package
    wait_for_registry nuget
}

sign_maven_file() {
    local file="$1"
    printf '%s' "$GPG_PASSPHRASE" | gpg --batch --yes --pinentry-mode loopback \
        --passphrase-fd 0 --armor --detach-sign "$file"
}

publish_maven() {
    require_common
    ensure_git_release
    [ -n "${CENTRAL_USERNAME:-}" ] || die "CENTRAL_USERNAME is required"
    [ -n "${CENTRAL_PASSWORD:-}" ] || die "CENTRAL_PASSWORD is required"
    [ -n "${MAVEN_DEPLOYMENT_RECORD:-}" ] || die "MAVEN_DEPLOYMENT_RECORD is required"
    case "$MAVEN_DEPLOYMENT_RECORD" in
        "$WORKSPACE"/*) ;;
        *) die "MAVEN_DEPLOYMENT_RECORD must stay inside WORKSPACE" ;;
    esac
    if registry_exists maven; then
        maven_artifacts_match
        printf 'Maven Central %s already exists and matches; skipping\n' "$RELEASE_VERSION"
        return
    else
        local registry_result=$?
        [ "$registry_result" -eq 1 ] || die "Could not determine whether Maven Central $RELEASE_VERSION exists"
    fi

    local temporary='' layout bundle auth deployment_id attempt status state runtime_root
    local file algorithm suffix
    deployment_id="${MAVEN_DEPLOYMENT_ID:-}"
    if [ -n "$deployment_id" ]; then
        [[ "$deployment_id" =~ ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ ]] || \
            die "Invalid MAVEN_DEPLOYMENT_ID: $deployment_id"
        printf 'Resuming Maven Central deployment %s without creating another upload\n' "$deployment_id"
    else
        [ -n "${GPG_PRIVATE_KEY:-}" ] || die "GPG_PRIVATE_KEY is required"
        [ -n "${GPG_PASSPHRASE:-}" ] || die "GPG_PASSPHRASE is required"
        runtime_root="$(secret_runtime_root)"
        temporary="$(mktemp -d "$runtime_root/maven.XXXXXX")"
        trap "rm -rf -- '$temporary'" EXIT
        export GNUPGHOME="$temporary/gnupg"
        mkdir -m 700 "$GNUPGHOME"
        printf '%s' "$GPG_PRIVATE_KEY" | gpg --batch --import >/dev/null
        layout="$temporary/com/rajatim/zhtw/$RELEASE_VERSION"
        mkdir -p "$layout"
        cp "$PAYLOAD_DIR"/packages/maven/* "$layout/"
        for file in "$layout"/*; do
            sign_maven_file "$file"
        done
        for file in "$layout"/*; do
            for algorithm in md5 sha1 sha256 sha512; do
                suffix="$algorithm"
                [ "$algorithm" != sha1 ] || suffix=sha1
                "${algorithm}sum" "$file" | cut -d' ' -f1 > "$file.$suffix"
            done
        done
        bundle="$temporary/zhtw-$RELEASE_VERSION-central.zip"
        (cd "$temporary" && zip -qr "$bundle" com)
    fi

    auth="$(printf '%s:%s' "$CENTRAL_USERNAME" "$CENTRAL_PASSWORD" | base64 | tr -d '\n')"
    if [ -z "$deployment_id" ]; then
        deployment_id="$(
            printf 'Authorization: Bearer %s\n' "$auth" | \
                curl -fsS --request POST --header @- \
                --form "bundle=@$bundle;type=application/octet-stream" \
                "https://central.sonatype.com/api/v1/publisher/upload?name=zhtw-$RELEASE_VERSION&publishingType=AUTOMATIC"
        )"
        [[ "$deployment_id" =~ ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ ]] || \
            die "Unexpected Maven deployment ID: $deployment_id"
    fi
    {
        printf 'MAVEN_DEPLOYMENT_ID=%s\n' "$deployment_id"
        printf 'RELEASE_VERSION=%s\n' "$RELEASE_VERSION"
        printf 'SOURCE_SHA=%s\n' "$SOURCE_SHA"
        printf 'RECORDED_AT=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    } > "$MAVEN_DEPLOYMENT_RECORD"

    status=''
    state=''
    for attempt in $(seq 1 120); do
        if ! status="$(
            printf 'Authorization: Bearer %s\n' "$auth" | \
                curl -fsS --max-time 30 --request POST --header @- \
                "https://central.sonatype.com/api/v1/publisher/status?id=$deployment_id"
        )"; then
            printf 'Maven Central status request failed; retrying (%s/120)\n' "$attempt" >&2
            sleep 15
            continue
        fi
        state="$(printf '%s' "$status" | jq -r '.deploymentState // empty' 2>/dev/null || true)"
        case "$state" in
            PUBLISHED) break ;;
            FAILED) printf '%s\n' "$status" | jq . >&2; die "Maven Central deployment failed" ;;
            *) sleep 15 ;;
        esac
    done
    [ "$state" = PUBLISHED ] || \
        die "Maven Central deployment timed out: $deployment_id"
    if [ -n "$temporary" ]; then
        rm -rf -- "$temporary"
        trap - EXIT
        unset GNUPGHOME
    fi
    wait_for_registry maven
    maven_artifacts_match
}

publish_homebrew() {
    local tap_dir="$1"
    require_common
    ensure_git_release
    [ -d "$tap_dir/.git" ] || die "Homebrew tap checkout not found: $tap_dir"
    if ! registry_exists pypi; then
        die "PyPI must be visible and readable before Homebrew"
    fi
    [ -z "$(git -C "$tap_dir" status --porcelain)" ] || die "Homebrew tap checkout is dirty"
    local info sdist_url sdist_sha formula
    info="$(curl -fsS --max-time 20 -A "$REGISTRY_USER_AGENT" \
        "https://pypi.org/pypi/zhtw/$RELEASE_VERSION/json")"
    sdist_url="$(printf '%s' "$info" | jq -r '.urls[] | select(.packagetype == "sdist") | .url')"
    sdist_sha="$(printf '%s' "$info" | jq -r '.urls[] | select(.packagetype == "sdist") | .digests.sha256')"
    [ -n "$sdist_url" ] && [ -n "$sdist_sha" ] || die "PyPI sdist metadata is incomplete"
    formula="$tap_dir/Formula/zhtw.rb"
    FORMULA="$formula" SDIST_URL="$sdist_url" SDIST_SHA="$sdist_sha" python3 - <<'PY'
import os
import re
from pathlib import Path

path = Path(os.environ["FORMULA"])
text = path.read_text(encoding="utf-8")
text, urls = re.subn(r'^  url ".*"$', f'  url "{os.environ["SDIST_URL"]}"', text, count=1, flags=re.MULTILINE)
text, hashes = re.subn(r'^  sha256 ".*"$', f'  sha256 "{os.environ["SDIST_SHA"]}"', text, count=1, flags=re.MULTILINE)
if urls != 1 or hashes != 1:
    raise SystemExit("Homebrew formula url/sha256 fields were not found")
path.write_text(text, encoding="utf-8")
PY
    if git -C "$tap_dir" diff --quiet -- Formula/zhtw.rb; then
        printf 'Homebrew formula already matches %s\n' "$RELEASE_VERSION"
        return
    fi
    git -C "$tap_dir" config user.name Jenkins
    git -C "$tap_dir" config user.email jenkins@tim-dev
    git -C "$tap_dir" add Formula/zhtw.rb
    git -C "$tap_dir" commit -m "zhtw $RELEASE_VERSION"
    git -C "$tap_dir" push origin HEAD:main
}

if [ "${BASH_SOURCE[0]}" != "$0" ]; then
    return 0
fi

case "$ACTION" in
    preview|preflight-*|publish-*) require_jenkins_release_runtime ;;
esac

case "$ACTION" in
    prepare) prepare_candidate ;;
    preview) preview_release ;;
    preflight-git) preflight_git "${3:-}" ;;
    preflight-pypi) preflight_pypi ;;
    preflight-npm) preflight_npm ;;
    preflight-crates) preflight_crates ;;
    preflight-nuget) preflight_nuget ;;
    preflight-maven) preflight_maven ;;
    publish-git) publish_git ;;
    publish-pypi) publish_pypi ;;
    publish-npm-js) publish_npm npm-js ;;
    publish-npm-wasm) publish_npm npm-wasm ;;
    publish-crates) publish_crates ;;
    publish-nuget) publish_nuget ;;
    publish-maven) publish_maven ;;
    publish-homebrew) publish_homebrew "${3:-}" ;;
    *) die "Unknown release action: $ACTION" ;;
esac
