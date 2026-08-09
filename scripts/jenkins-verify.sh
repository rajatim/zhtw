#!/usr/bin/env bash

set -euo pipefail

SUITE="${1:-all}"
TOOLS_ROOT="${ZHTW_TOOLS_ROOT:-$HOME/.local/share/zhtw-tools}"
export PATH="$HOME/.cargo/bin:$TOOLS_ROOT/dotnet:$TOOLS_ROOT/go/bin:$TOOLS_ROOT/wasm-pack:$PATH"

die() {
    printf 'ERROR: %s\n' "$*" >&2
    exit 64
}

prepare_container_cli() {
    local runtime_root="$PWD/.jenkins-container-runtime"
    mkdir -p "$runtime_root/bin" "$runtime_root/docker-config"
    chmod 700 "$runtime_root" "$runtime_root/bin" "$runtime_root/docker-config"
    printf '{"auths":{}}\n' > "$runtime_root/registry-auth.json"
    chmod 600 "$runtime_root/registry-auth.json"
    export DOCKER_CONFIG="$runtime_root/docker-config"
    export REGISTRY_AUTH_FILE="$runtime_root/registry-auth.json"

    if ! command -v docker >/dev/null 2>&1; then
        command -v podman >/dev/null 2>&1 || die "Docker or Podman is required for competitor verification"
        ln -sf "$(command -v podman)" "$runtime_root/bin/docker"
        export PATH="$runtime_root/bin:$PATH"
    fi
    docker --version
}

verify_sdk_matrix() {
    local version environment java_home node_bin rust_toolchain go_bin

    for version in 3.10 3.11 3.12 3.13; do
        environment="$PWD/.venv-python-${version/./}"
        UV_PROJECT_ENVIRONMENT="$environment" uv sync --python "$version" --frozen --extra dev
        UV_PROJECT_ENVIRONMENT="$environment" uv run ruff check .
        UV_PROJECT_ENVIRONMENT="$environment" uv run pytest tests/ -q
    done

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
    prepare_container_cli
    uv sync --frozen --extra dev
    uv run python scripts/validate_competitor_environment.py
    make benchmark-competitor-probe
    uv run pytest tests/test_competitor_environment.py -q
    uv run python scripts/run_ud_gsd_benchmark.py \
        --generated-date 2026-07-31 --output-prefix /tmp/zhtw-jenkins-ud-gsd
    uv run python scripts/run_naer_terms_benchmark.py \
        --generated-date 2026-07-31 --output-prefix /tmp/zhtw-jenkins-naer-terms
    diff <(jq -S .scores docs/reports/ud-gsd-benchmark-2026-07-31.json) \
         <(jq -S .scores /tmp/zhtw-jenkins-ud-gsd.json)
    diff <(jq -S .scores docs/reports/naer-terms-benchmark-2026-07-31.json) \
         <(jq -S .scores /tmp/zhtw-jenkins-naer-terms.json)
    make benchmark-paired-import-check

    local image benchmark_id
    image="zhtw-benchmark-competitors:$(jq -r '.environment.environment_sha256' \
        benchmarks/accuracy/competitors.lock.json | cut -c1-12)"
    for benchmark_id in aosp-framework-paired-ui-v1 vscode-paired-ui-v1 firefox-paired-ui-v1; do
        uv run python scripts/run_paired_localization_benchmark.py \
            --manifest "benchmarks/accuracy/manifests/$benchmark_id.json" \
            --engines zhtw,opencc-s2twp,zhconv-zh-tw \
            --container-image "$image" \
            --generated-date 2026-07-31 \
            --output-prefix "/tmp/zhtw-jenkins-$benchmark_id"
        diff \
            <(jq -S '{engines,paired_comparisons}' \
                "docs/reports/$benchmark_id-benchmark-2026-07-31.json") \
            <(jq -S '{engines,paired_comparisons}' \
                "/tmp/zhtw-jenkins-$benchmark_id.json")
    done

    uv run python scripts/reproduce_public_benchmarks.py \
        --operator jenkins \
        --organization rajatim/zhtw \
        --local-smoke-test \
        --output /tmp/zhtw-public-benchmark-attestation.json
    uv run python scripts/validate_public_benchmark_attestation.py \
        --allow-local-smoke-test \
        /tmp/zhtw-public-benchmark-attestation.json
}

case "$SUITE" in
    sdk-matrix) verify_sdk_matrix ;;
    competitor-benchmark) verify_competitor_benchmark ;;
    all)
        verify_sdk_matrix
        verify_competitor_benchmark
        ;;
    *) die "Usage: scripts/jenkins-verify.sh {sdk-matrix|competitor-benchmark|all}" ;;
esac
