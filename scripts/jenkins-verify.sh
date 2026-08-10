#!/usr/bin/env bash

set -euo pipefail

SUITE="${1:-all}"
TOOLS_ROOT="${ZHTW_TOOLS_ROOT:-$HOME/.local/share/zhtw-tools}"
export PATH="$HOME/.cargo/bin:$TOOLS_ROOT/security/bin:$TOOLS_ROOT/dotnet:$TOOLS_ROOT/go/bin:$TOOLS_ROOT/wasm-pack:$PATH"
export UV_PYTHON=3.13
export UV_PYTHON_PREFERENCE=only-managed
EVIDENCE_DIR="${ZHTW_VERIFY_EVIDENCE_DIR:-${WORKSPACE:-}/verification-evidence}"

die() {
    printf 'ERROR: %s\n' "$*" >&2
    exit 64
}

require_jenkins_verify_runtime() {
    [ "${CI_PROVIDER:-}" = jenkins ] || die "Formal compatibility checks require Jenkins"
    [ "${JOB_NAME:-}" = zhtw/verify ] || die "JOB_NAME must be zhtw/verify"
    [ -n "${JENKINS_URL:-}" ] || die "JENKINS_URL is required"
    [ -n "${BUILD_TAG:-}" ] || die "BUILD_TAG is required"
    [ -n "${WORKSPACE:-}" ] || die "WORKSPACE is required"
    case "$EVIDENCE_DIR" in
        "$WORKSPACE"/*) ;;
        *) die "ZHTW_VERIFY_EVIDENCE_DIR must stay inside WORKSPACE" ;;
    esac
    [[ "${RELEASE_DATE:-}" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]] || \
        die "RELEASE_DATE must be YYYY-MM-DD"
}

prepare_container_cli() {
    local runtime_root="$PWD/.jenkins-container-runtime"
    local podman_socket="/home/jenkins-agent/.local/run/podman.sock"
    mkdir -p "$runtime_root/bin" "$runtime_root/docker-config"
    chmod 700 "$runtime_root" "$runtime_root/bin" "$runtime_root/docker-config"
    printf '{"auths":{}}\n' > "$runtime_root/registry-auth.json"
    chmod 600 "$runtime_root/registry-auth.json"
    export DOCKER_CONFIG="$runtime_root/docker-config"
    export REGISTRY_AUTH_FILE="$runtime_root/registry-auth.json"
    export TESTCONTAINERS_RYUK_DISABLED=true

    if [ -S "$podman_socket" ]; then
        command -v podman >/dev/null 2>&1 || die "Docker or Podman is required for competitor verification"
        export DOCKER_HOST="unix://$podman_socket"
        printf '#!/usr/bin/env bash\nexec %q --remote --url %q "$@"\n' \
            "$(command -v podman)" "$DOCKER_HOST" > "$runtime_root/bin/docker"
        chmod 700 "$runtime_root/bin/docker"
        export PATH="$runtime_root/bin:$PATH"
    elif ! command -v docker >/dev/null 2>&1; then
        local xdg_root="$runtime_root/xdg"
        local storage_root="$runtime_root/storage"
        local storage_runroot="$runtime_root/runroot"
        local podman_tmp="$runtime_root/tmp"
        command -v podman >/dev/null 2>&1 || die "Docker or Podman is required for competitor verification"
        mkdir -p "$xdg_root" "$storage_root" "$storage_runroot" "$podman_tmp"
        chmod 700 "$xdg_root" "$storage_root" "$storage_runroot" "$podman_tmp"
        printf '#!/usr/bin/env bash\nexport XDG_RUNTIME_DIR=%q\nexec %q --root %q --runroot %q --tmpdir %q --cgroup-manager=cgroupfs --events-backend=file "$@"\n' \
            "$xdg_root" "$(command -v podman)" "$storage_root" "$storage_runroot" "$podman_tmp" \
            > "$runtime_root/bin/docker"
        chmod 700 "$runtime_root/bin/docker"
        export PATH="$runtime_root/bin:$PATH"
    fi
    docker --version
}

verify_sdk_matrix() {
    local version environment java_home node_bin rust_toolchain go_bin index failed
    local -a python_pids=() python_versions=()

    for version in 3.10 3.11 3.12 3.13; do
        environment="$PWD/.venv-python-${version/./}"
        (
            UV_PROJECT_ENVIRONMENT="$environment" uv sync --python "$version" --frozen --extra dev
            UV_PROJECT_ENVIRONMENT="$environment" uv run pytest tests/ -q
        ) > "$EVIDENCE_DIR/python-$version.log" 2>&1 &
        python_pids+=("$!")
        python_versions+=("$version")
    done
    failed=0
    for index in "${!python_pids[@]}"; do
        if ! wait "${python_pids[$index]}"; then
            printf 'Python %s compatibility test failed\n' "${python_versions[$index]}" >&2
            failed=1
        fi
        cat "$EVIDENCE_DIR/python-${python_versions[$index]}.log"
    done
    [ "$failed" -eq 0 ] || die "One or more Python compatibility tests failed"
    UV_PROJECT_ENVIRONMENT="$PWD/.venv-python-313" uv run ruff check .

    for version in 11 17 21; do
        java_home="$TOOLS_ROOT/jdks/$version"
        [ -x "$java_home/bin/java" ] || die "JDK $version is missing at $java_home"
        (cd sdk/java && JAVA_HOME="$java_home" PATH="$java_home/bin:$PATH" mvn verify --batch-mode)
    done

    for version in 20 22; do
        node_bin="$TOOLS_ROOT/node-$version/bin"
        [ -x "$node_bin/node" ] || die "Node $version is missing at $node_bin"
        (
            cd sdk/typescript
            PATH="$node_bin:$PATH" pnpm install --frozen-lockfile
            PATH="$node_bin:$PATH" pnpm exec tsc --noEmit
            PATH="$node_bin:$PATH" pnpm test
            PATH="$node_bin:$PATH" pnpm build
            PATH="$node_bin:$PATH" pnpm test:package
        )
    done

    for rust_toolchain in 1.80.1 stable; do
        (cd sdk/rust && cargo "+$rust_toolchain" build -p zhtw --release)
        (cd sdk/rust && cargo "+$rust_toolchain" test -p zhtw --release)
    done
    (cd sdk/rust && cargo +stable clippy -p zhtw -- -D warnings)
    (cd sdk/rust && cargo +stable fmt -p zhtw --check)

    for go_bin in "$TOOLS_ROOT/go-min/bin/go" "$TOOLS_ROOT/go/bin/go"; do
        [ -x "$go_bin" ] || die "Go matrix tool is missing: $go_bin"
        (cd sdk/go && "$go_bin" test ./... -race)
        (cd sdk/go && "$go_bin" vet ./...)
    done

    (cd sdk/dotnet && DOTNET_ROLL_FORWARD=Major dotnet build Zhtw.csproj -c Release)
    (cd sdk/dotnet && DOTNET_ROLL_FORWARD=Major dotnet test tests/Zhtw.Tests/Zhtw.Tests.csproj -c Release)
}

verify_competitor_benchmark() {
    local benchmark_dir="$EVIDENCE_DIR/benchmarks"
    mkdir -p "$benchmark_dir"
    prepare_container_cli
    uv sync --frozen --extra dev
    uv run python scripts/validate_competitor_environment.py
    make benchmark-competitor-probe
    uv run pytest tests/test_competitor_environment.py -q
    uv run python scripts/run_ud_gsd_benchmark.py \
        --generated-date "$RELEASE_DATE" --output-prefix "$benchmark_dir/ud-gsd"
    uv run python scripts/run_naer_terms_benchmark.py \
        --generated-date "$RELEASE_DATE" --output-prefix "$benchmark_dir/naer-terms"
    uv run python scripts/validate_benchmark_non_regression.py \
        docs/reports/ud-gsd-benchmark-2026-07-31.json \
        "$benchmark_dir/ud-gsd.json"
    uv run python scripts/validate_benchmark_non_regression.py \
        docs/reports/naer-terms-benchmark-2026-07-31.json \
        "$benchmark_dir/naer-terms.json"
    make benchmark-paired-import-check

    local image benchmark_id
    image="zhtw-benchmark-competitors:$(jq -r '.environment.environment_sha256' \
        benchmarks/accuracy/competitors.lock.json | cut -c1-12)"
    for benchmark_id in aosp-framework-paired-ui-v1 vscode-paired-ui-v1 firefox-paired-ui-v1; do
        uv run python scripts/run_paired_localization_benchmark.py \
            --manifest "benchmarks/accuracy/manifests/$benchmark_id.json" \
            --engines zhtw,opencc-s2twp,zhconv-zh-tw \
            --container-image "$image" \
            --generated-date "$RELEASE_DATE" \
            --output-prefix "$benchmark_dir/$benchmark_id"
        uv run python scripts/validate_benchmark_non_regression.py \
            "docs/reports/$benchmark_id-benchmark-2026-07-31.json" \
            "$benchmark_dir/$benchmark_id.json"
    done

    uv run python scripts/reproduce_public_benchmarks.py \
        --operator jenkins \
        --organization rajatim/zhtw \
        --local-smoke-test \
        --output "$benchmark_dir/public-benchmark-attestation.json"
    uv run python scripts/validate_public_benchmark_attestation.py \
        --allow-local-smoke-test \
        "$benchmark_dir/public-benchmark-attestation.json"
}

require_jenkins_verify_runtime
mkdir -p "$EVIDENCE_DIR"
chmod 700 "$EVIDENCE_DIR"

case "$SUITE" in
    sdk-matrix) verify_sdk_matrix ;;
    competitor-benchmark) verify_competitor_benchmark ;;
    all)
        verify_sdk_matrix
        verify_competitor_benchmark
        ;;
    *) die "Usage: scripts/jenkins-verify.sh {sdk-matrix|competitor-benchmark|all}" ;;
esac

./scripts/write-toolchain-evidence.sh "$EVIDENCE_DIR/toolchain.properties"
(
    cd "$EVIDENCE_DIR"
    find . -type f ! -name SHA256SUMS -print0 | LC_ALL=C sort -z | \
        xargs -0 -r sha256sum > SHA256SUMS
    test -s SHA256SUMS
    sha256sum -c SHA256SUMS
)
