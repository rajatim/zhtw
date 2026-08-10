#!/usr/bin/env bash

set -euo pipefail

ACTION="${1:-}"
OUTPUT_DIR="${2:-}"
STATE_DIR=".jenkins-release"
TOOLS_ROOT="${ZHTW_TOOLS_ROOT:-$HOME/.local/share/zhtw-tools}"
export PATH="$TOOLS_ROOT/node-20/bin:$HOME/.cargo/bin:$TOOLS_ROOT/dotnet:$TOOLS_ROOT/go/bin:$TOOLS_ROOT/wasm-pack:$PATH"
export UV_PYTHON=3.13
export UV_PYTHON_PREFERENCE=only-managed
PYTHON_SDIST_MAX_BYTES=$((10 * 1024 * 1024))

die() {
    printf 'ERROR: %s\n' "$*" >&2
    exit 64
}

require_jenkins_build_runtime() {
    [ "${CI_PROVIDER:-}" = jenkins ] || die "Formal candidates require Jenkins"
    [ "${JOB_NAME:-}" = zhtw/build ] || die "JOB_NAME must be zhtw/build"
    [ -n "${JENKINS_URL:-}" ] || die "JENKINS_URL is required"
    [ -n "${BUILD_TAG:-}" ] || die "BUILD_TAG is required"
    [ -n "${WORKSPACE:-}" ] || die "WORKSPACE is required"
}

require_env() {
    local name
    for name in SOURCE_SHA PROJECT_TREE_SHA RELEASE_VERSION BUILD_VERSION VERSION_TAG RELEASE_DATE; do
        [ -n "${!name:-}" ] || die "$name is required"
    done
    [[ "$SOURCE_SHA" =~ ^[0-9a-f]{40}$ ]] || die "SOURCE_SHA must be a full Git SHA"
    [[ "$PROJECT_TREE_SHA" =~ ^[0-9a-f]{40}$ ]] || die "PROJECT_TREE_SHA must be a full Git tree SHA"
    [[ "$RELEASE_VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || die "Invalid RELEASE_VERSION"
    [ "$VERSION_TAG" = "v$RELEASE_VERSION" ] || die "VERSION_TAG does not match RELEASE_VERSION"
}

require_tools() {
    local tool
    for tool in uv python3 java mvn node pnpm cargo rustc go dotnet wasm-pack jq zip unzip git sha256sum; do
        command -v "$tool" >/dev/null 2>&1 || die "Required tool is missing: $tool"
    done
}

check_source_identity() {
    [ "$(git rev-parse HEAD)" = "$SOURCE_SHA" ] || die "Checkout is not SOURCE_SHA"
    [ "$(git rev-parse "$SOURCE_SHA^{tree}")" = "$PROJECT_TREE_SHA" ] || die "PROJECT_TREE_SHA mismatch"
}

scan() {
    require_env
    check_source_identity
    if git grep -IlE -- '-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----' -- . \
        ':!tests/**' ':!docs/**' | grep -q .; then
        die "A private-key header exists in publishable source"
    fi
    uv sync --frozen --extra dev
    uv run ruff check .
    git diff --check
}

build_candidate() {
    require_env
    require_tools
    check_source_identity
    mkdir -p "$STATE_DIR"
    uv sync --frozen --extra dev
    make bump VERSION="$RELEASE_VERSION"
    uv run python scripts/prepare_release_candidate.py \
        --version "$RELEASE_VERSION" \
        --date "$RELEASE_DATE" \
        --notes-output "$STATE_DIR/release-notes.md"
    make version-check
    git diff --check
}

test_candidate() {
    require_env
    require_tools
    [ -s "$STATE_DIR/release-notes.md" ] || die "Candidate was not prepared"
    make release-gate
    git diff --check
}

package_python() {
    local destination="$1" wheel
    mkdir -p "$destination"
    rm -rf dist
    uv build --out-dir "$destination"
    # uv creates this helper for output directories. It is not a distribution
    # artifact and Jenkins' default archive excludes it, so never checksum it.
    rm -f "$destination/.gitignore"
    wheel="$(find "$destination" -maxdepth 1 -name 'zhtw-*.whl' -print -quit)"
    [ -n "$wheel" ] || die "Python wheel is missing after build"
    validate_python_sdist "$destination/zhtw-$RELEASE_VERSION.tar.gz" "$wheel"
}

validate_python_sdist() {
    local archive="$1" expected_wheel="${2:-}" root size required forbidden
    [ -s "$archive" ] || die "Python sdist is missing: $archive"
    root="zhtw-$RELEASE_VERSION"
    size="$(wc -c < "$archive" | tr -d '[:space:]')"
    [ "$size" -le "$PYTHON_SDIST_MAX_BYTES" ] || \
        die "Python sdist is too large: $size bytes (limit $PYTHON_SDIST_MAX_BYTES)"

    for required in pyproject.toml README.md LICENSE src/zhtw/__init__.py; do
        tar -tzf "$archive" | grep -Fx "$root/$required" >/dev/null || \
            die "Python sdist is missing required file: $required"
    done
    for forbidden in benchmarks docs sdk tests; do
        if tar -tzf "$archive" | grep -E "^$root/$forbidden/" >/dev/null; then
            die "Python sdist contains non-package tree: $forbidden/"
        fi
    done
    if tar -tzf "$archive" | \
        grep -E "^$root/src/zhtw/data/terms/pending/.*\.json$" >/dev/null; then
        die "Python sdist contains a pending term draft"
    fi

    [ -z "$expected_wheel" ] || (
        local temporary rebuilt_wheel
        temporary="$(mktemp -d)"
        trap 'rm -rf -- "$temporary"' EXIT
        uv build --wheel --out-dir "$temporary" "$archive"
        rebuilt_wheel="$temporary/zhtw-$RELEASE_VERSION-py3-none-any.whl"
        [ -s "$rebuilt_wheel" ] || die "Python sdist could not rebuild the expected wheel"
        cmp -s "$expected_wheel" "$rebuilt_wheel" || \
            die "Python sdist rebuilt wheel differs from the direct wheel"
    )
}

package_typescript() {
    local destination="$1"
    mkdir -p "$destination"
    (
        cd sdk/typescript
        pnpm install --frozen-lockfile
        pnpm build
        pnpm pack --pack-destination "$destination"
    )
}

package_wasm() {
    local destination="$1"
    mkdir -p "$destination"
    (
        cd sdk/rust/zhtw-wasm
        rm -rf pkg
        wasm-pack build --target bundler --release
        RELEASE_VERSION="$RELEASE_VERSION" python3 - <<'PY'
import json
import os
from pathlib import Path

path = Path("pkg/package.json")
payload = json.loads(path.read_text(encoding="utf-8"))
payload["version"] = os.environ["RELEASE_VERSION"]
path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
PY
        npm pack ./pkg --pack-destination "$destination"
    )
}

package_crate() {
    local destination="$1"
    mkdir -p "$destination"
    rm -f sdk/rust/target/package/zhtw-*.crate
    cargo package --manifest-path sdk/rust/zhtw/Cargo.toml --allow-dirty --no-verify
    cp sdk/rust/target/package/zhtw-"$RELEASE_VERSION".crate "$destination/"
}

package_nuget() {
    local destination="$1"
    mkdir -p "$destination"
    dotnet restore sdk/dotnet/Zhtw.csproj
    dotnet build sdk/dotnet/Zhtw.csproj -c Release --no-restore
    dotnet pack sdk/dotnet/Zhtw.csproj -c Release --no-build --no-restore -o "$destination"
}

package_maven() {
    local destination="$1"
    mkdir -p "$destination"
    (
        cd sdk/java
        mvn package -P release -Dgpg.skip=true --batch-mode
    )
    cp "sdk/java/target/zhtw-$RELEASE_VERSION.jar" "$destination/"
    cp "sdk/java/target/zhtw-$RELEASE_VERSION-sources.jar" "$destination/"
    cp "sdk/java/target/zhtw-$RELEASE_VERSION-javadoc.jar" "$destination/"
    cp sdk/java/pom.xml "$destination/zhtw-$RELEASE_VERSION.pom"
}

package_go() {
    local destination="$1"
    local temporary goos goarch extension binary archive
    mkdir -p "$destination"
    temporary="$(mktemp -d)"
    trap "rm -rf -- '$temporary'" EXIT
    cp LICENSE "$temporary/"
    while read -r goos goarch; do
        extension=""
        [ "$goos" != windows ] || extension=".exe"
        binary="zhtw-${goos}-${goarch}${extension}"
        (
            cd sdk/go
            CGO_ENABLED=0 GOOS="$goos" GOARCH="$goarch" \
                go build -trimpath -ldflags "-s -w -X main.version=$RELEASE_VERSION" \
                -o "$temporary/$binary" ./cmd/zhtw
        )
        if [ "$goos" = windows ]; then
            archive="zhtw-${goos}-${goarch}.zip"
            (cd "$temporary" && zip -q "$destination/$archive" "$binary" LICENSE)
        else
            archive="zhtw-${goos}-${goarch}.tar.gz"
            chmod +x "$temporary/$binary"
            tar -C "$temporary" -czf "$destination/$archive" "$binary" LICENSE
        fi
    done <<'EOF'
darwin amd64
darwin arm64
linux amd64
linux arm64
windows amd64
EOF
    (cd "$destination" && sha256sum ./*.tar.gz ./*.zip > zhtw_checksums.txt)
    rm -rf -- "$temporary"
    trap - EXIT
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

check_patch_applies_to_head() {
    local patch_file="$1" temporary_index
    temporary_index="$(mktemp)"
    rm -f "$temporary_index"
    GIT_INDEX_FILE="$temporary_index" git read-tree HEAD
    GIT_INDEX_FILE="$temporary_index" git apply --cached --check "$patch_file"
    rm -f "$temporary_index"
}

package_candidate() {
    require_env
    require_tools
    [ -n "$OUTPUT_DIR" ] || die "package requires an output directory"
    [ -s "$STATE_DIR/release-notes.md" ] || die "Candidate was not prepared"
    mkdir -p "$OUTPUT_DIR/packages" "$OUTPUT_DIR/candidate" "$OUTPUT_DIR/metadata"

    package_python "$OUTPUT_DIR/packages/python"
    package_typescript "$OUTPUT_DIR/packages/npm"
    package_wasm "$OUTPUT_DIR/packages/npm"
    package_crate "$OUTPUT_DIR/packages/crates"
    package_nuget "$OUTPUT_DIR/packages/nuget"
    package_maven "$OUTPUT_DIR/packages/maven"
    package_go "$OUTPUT_DIR/packages/go"

    git diff --check
    git diff --binary HEAD -- . > "$OUTPUT_DIR/candidate/release.patch"
    [ -s "$OUTPUT_DIR/candidate/release.patch" ] || die "Candidate patch is empty"
    check_patch_applies_to_head "$OUTPUT_DIR/candidate/release.patch"
    cp "$STATE_DIR/release-notes.md" "$OUTPUT_DIR/candidate/release-notes.md"

    printf '%s\n' "$RELEASE_VERSION" > "$OUTPUT_DIR/metadata/release-version"
    printf '%s\n' "$BUILD_VERSION" > "$OUTPUT_DIR/metadata/build-version"
    printf '%s\n' "$VERSION_TAG" > "$OUTPUT_DIR/metadata/version-tag"
    printf '%s\n' "$SOURCE_SHA" > "$OUTPUT_DIR/metadata/source-sha"
    printf '%s\n' "$PROJECT_TREE_SHA" > "$OUTPUT_DIR/metadata/project-tree-sha"
    candidate_tree > "$OUTPUT_DIR/metadata/candidate-tree-sha"
    printf '%s\n' "$RELEASE_DATE" > "$OUTPUT_DIR/metadata/release-date"
}

package_json_version() {
    tar -xOf "$1" package/package.json | python3 -c \
        'import json,sys; print(json.load(sys.stdin)["version"])'
}

verify_candidate() {
    require_env
    require_tools
    [ -n "$OUTPUT_DIR" ] || die "verify requires an output directory"
    [ "$(tr -d '[:space:]' < "$OUTPUT_DIR/metadata/release-version")" = "$RELEASE_VERSION" ]
    [ "$(tr -d '[:space:]' < "$OUTPUT_DIR/metadata/build-version")" = "$BUILD_VERSION" ]
    [ "$(tr -d '[:space:]' < "$OUTPUT_DIR/metadata/source-sha")" = "$SOURCE_SHA" ]
    [ "$(tr -d '[:space:]' < "$OUTPUT_DIR/metadata/project-tree-sha")" = "$PROJECT_TREE_SHA" ]
    [ "$(tr -d '[:space:]' < "$OUTPUT_DIR/metadata/candidate-tree-sha")" = "$(candidate_tree)" ]
    check_patch_applies_to_head "$OUTPUT_DIR/candidate/release.patch"

    compgen -G "$OUTPUT_DIR/packages/python/zhtw-$RELEASE_VERSION.tar.gz" >/dev/null
    compgen -G "$OUTPUT_DIR/packages/python/zhtw-$RELEASE_VERSION-*.whl" >/dev/null
    [ "$(find "$OUTPUT_DIR/packages/python" -maxdepth 1 -type f | wc -l | tr -d ' ')" = 2 ]
    validate_python_sdist "$OUTPUT_DIR/packages/python/zhtw-$RELEASE_VERSION.tar.gz"
    local js_tgz wasm_tgz nuget_package
    js_tgz="$(find "$OUTPUT_DIR/packages/npm" -maxdepth 1 -name "zhtw-js-$RELEASE_VERSION.tgz" -print -quit)"
    wasm_tgz="$(find "$OUTPUT_DIR/packages/npm" -maxdepth 1 -name "zhtw-wasm-$RELEASE_VERSION.tgz" -print -quit)"
    [ -n "$js_tgz" ] && [ "$(package_json_version "$js_tgz")" = "$RELEASE_VERSION" ]
    [ -n "$wasm_tgz" ] && [ "$(package_json_version "$wasm_tgz")" = "$RELEASE_VERSION" ]
    tar -tzf "$wasm_tgz" | grep -Fx 'package/LICENSE' >/dev/null
    [ -s "$OUTPUT_DIR/packages/crates/zhtw-$RELEASE_VERSION.crate" ]
    nuget_package="$OUTPUT_DIR/packages/nuget/Zhtw.$RELEASE_VERSION.nupkg"
    [ -s "$nuget_package" ]
    unzip -Z1 "$nuget_package" | grep -Fx 'README.md' >/dev/null
    [ -s "$OUTPUT_DIR/packages/maven/zhtw-$RELEASE_VERSION.jar" ]
    [ -s "$OUTPUT_DIR/packages/maven/zhtw-$RELEASE_VERSION-sources.jar" ]
    [ -s "$OUTPUT_DIR/packages/maven/zhtw-$RELEASE_VERSION-javadoc.jar" ]
    [ -s "$OUTPUT_DIR/packages/maven/zhtw-$RELEASE_VERSION.pom" ]
    [ "$(find "$OUTPUT_DIR/packages/go" -maxdepth 1 \( -name '*.tar.gz' -o -name '*.zip' \) | wc -l | tr -d ' ')" = 5 ]
    (cd "$OUTPUT_DIR/packages/go" && sha256sum -c zhtw_checksums.txt)
}

require_jenkins_build_runtime

case "$ACTION" in
    scan) scan ;;
    build) build_candidate ;;
    test) test_candidate ;;
    package) package_candidate ;;
    verify) verify_candidate ;;
    *) die "Usage: scripts/jenkins-build.sh {scan|build|test|package <dir>|verify <dir>}" ;;
esac
