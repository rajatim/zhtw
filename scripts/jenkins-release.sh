#!/usr/bin/env bash

set -euo pipefail

ACTION="${1:-}"
PAYLOAD_DIR="${2:-}"
TOOLS_ROOT="${ZHTW_TOOLS_ROOT:-$HOME/.local/share/zhtw-tools}"
export PATH="$HOME/.cargo/bin:$TOOLS_ROOT/dotnet:$TOOLS_ROOT/go/bin:$TOOLS_ROOT/wasm-pack:$PATH"

die() {
    printf 'ERROR: %s\n' "$*" >&2
    exit 64
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

registry_exists() {
    case "$1" in
        pypi) curl -fsS --max-time 20 "https://pypi.org/pypi/zhtw/$RELEASE_VERSION/json" >/dev/null ;;
        npm-js) curl -fsS --max-time 20 "https://registry.npmjs.org/zhtw-js/$RELEASE_VERSION" >/dev/null ;;
        npm-wasm) curl -fsS --max-time 20 "https://registry.npmjs.org/zhtw-wasm/$RELEASE_VERSION" >/dev/null ;;
        crates) curl -fsS --max-time 20 "https://crates.io/api/v1/crates/zhtw/$RELEASE_VERSION" >/dev/null ;;
        nuget) curl -fsS --max-time 20 "https://api.nuget.org/v3-flatcontainer/zhtw/$RELEASE_VERSION/zhtw.$RELEASE_VERSION.nupkg" >/dev/null ;;
        maven) curl -fsS --max-time 20 "https://repo1.maven.org/maven2/com/rajatim/zhtw/$RELEASE_VERSION/zhtw-$RELEASE_VERSION.pom" >/dev/null ;;
        go) curl -fsS --max-time 20 "https://proxy.golang.org/github.com/rajatim/zhtw/sdk/go/v4/@v/v$RELEASE_VERSION.info" >/dev/null ;;
        *) die "Unknown registry: $1" ;;
    esac
}

wait_for_registry() {
    local target="$1" attempt
    for attempt in $(seq 1 120); do
        if registry_exists "$target"; then
            printf '%s %s is visible\n' "$target" "$RELEASE_VERSION"
            return
        fi
        sleep 15
    done
    die "$target did not expose $RELEASE_VERSION before timeout"
}

publish_pypi() {
    require_common
    ensure_git_release
    [ -n "${PYPI_TOKEN:-}" ] || die "PYPI_TOKEN is required"
    if registry_exists pypi; then
        printf 'PyPI %s already exists; skipping\n' "$RELEASE_VERSION"
        return
    fi
    TWINE_USERNAME=__token__ TWINE_PASSWORD="$PYPI_TOKEN" \
        UV_CACHE_DIR="${UV_CACHE_DIR:-$HOME/.cache/uv}" \
        uvx --from twine==6.1.0 twine upload --non-interactive \
        "$PAYLOAD_DIR"/packages/python/*
    wait_for_registry pypi
}

publish_npm() {
    local target="$1" package_name tarball temporary_config
    require_common
    ensure_git_release
    [ -n "${NODE_AUTH_TOKEN:-}" ] || die "NODE_AUTH_TOKEN is required"
    case "$target" in
        npm-js) package_name=zhtw-js ;;
        npm-wasm) package_name=zhtw-wasm ;;
        *) die "Unknown npm target: $target" ;;
    esac
    if registry_exists "$target"; then
        printf '%s %s already exists; skipping\n' "$package_name" "$RELEASE_VERSION"
        return
    fi
    tarball="$PAYLOAD_DIR/packages/npm/$package_name-$RELEASE_VERSION.tgz"
    [ -s "$tarball" ] || die "Missing npm tarball: $tarball"
    temporary_config="$(mktemp)"
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
    if registry_exists crates; then
        printf 'crates.io %s already exists; skipping\n' "$RELEASE_VERSION"
        return
    fi
    local expected actual
    expected="$(sha256sum "$PAYLOAD_DIR/packages/crates/zhtw-$RELEASE_VERSION.crate" | cut -d' ' -f1)"
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
    if registry_exists nuget; then
        printf 'NuGet %s already exists; skipping\n' "$RELEASE_VERSION"
        return
    fi
    local package
    package="$PAYLOAD_DIR/packages/nuget/Zhtw.$RELEASE_VERSION.nupkg"
    [ -s "$package" ] || die "Missing NuGet package: $package"
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
    [ -n "${GPG_PRIVATE_KEY:-}" ] || die "GPG_PRIVATE_KEY is required"
    [ -n "${GPG_PASSPHRASE:-}" ] || die "GPG_PASSPHRASE is required"
    if registry_exists maven; then
        printf 'Maven Central %s already exists; skipping\n' "$RELEASE_VERSION"
        return
    fi

    local temporary layout bundle auth deployment_id attempt status
    temporary="$(mktemp -d)"
    trap "rm -rf -- '$temporary'" EXIT
    export GNUPGHOME="$temporary/gnupg"
    mkdir -m 700 "$GNUPGHOME"
    printf '%s' "$GPG_PRIVATE_KEY" | gpg --batch --import >/dev/null
    layout="$temporary/com/rajatim/zhtw/$RELEASE_VERSION"
    mkdir -p "$layout"
    cp "$PAYLOAD_DIR"/packages/maven/* "$layout/"
    local file algorithm suffix
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
    auth="$(printf '%s:%s' "$CENTRAL_USERNAME" "$CENTRAL_PASSWORD" | base64 | tr -d '\n')"
    deployment_id="$(
        printf 'Authorization: Bearer %s\n' "$auth" | \
            curl -fsS --request POST --header @- \
            --form "bundle=@$bundle;type=application/octet-stream" \
            "https://central.sonatype.com/api/v1/publisher/upload?name=zhtw-$RELEASE_VERSION&publishingType=AUTOMATIC"
    )"
    [[ "$deployment_id" =~ ^[0-9a-f-]{36}$ ]] || die "Unexpected Maven deployment ID: $deployment_id"
    for attempt in $(seq 1 120); do
        status="$(
            printf 'Authorization: Bearer %s\n' "$auth" | \
                curl -fsS --request POST --header @- \
                "https://central.sonatype.com/api/v1/publisher/status?id=$deployment_id"
        )"
        case "$(printf '%s' "$status" | jq -r .deploymentState)" in
            PUBLISHED) break ;;
            FAILED) printf '%s\n' "$status" | jq . >&2; die "Maven Central deployment failed" ;;
            *) sleep 15 ;;
        esac
    done
    [ "$(printf '%s' "$status" | jq -r .deploymentState)" = PUBLISHED ] || \
        die "Maven Central deployment timed out: $deployment_id"
    rm -rf -- "$temporary"
    trap - EXIT
    wait_for_registry maven
}

publish_homebrew() {
    local tap_dir="$1"
    require_common
    ensure_git_release
    [ -d "$tap_dir/.git" ] || die "Homebrew tap checkout not found: $tap_dir"
    registry_exists pypi || die "PyPI must be visible before Homebrew"
    [ -z "$(git -C "$tap_dir" status --porcelain)" ] || die "Homebrew tap checkout is dirty"
    local info sdist_url sdist_sha formula
    info="$(curl -fsS --max-time 20 "https://pypi.org/pypi/zhtw/$RELEASE_VERSION/json")"
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

case "$ACTION" in
    prepare) prepare_candidate ;;
    preview) preview_release ;;
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
