#!/usr/bin/env bash

set -euo pipefail

OUTPUT_FILE="${1:-}"
[ -n "$OUTPUT_FILE" ] || {
    echo 'Usage: scripts/write-toolchain-evidence.sh OUTPUT_FILE' >&2
    exit 64
}

mkdir -p "$(dirname "$OUTPUT_FILE")"

first_line() {
    "$@" 2>&1 | sed -n '1p' | tr '\r\n' '  '
}

required_version() {
    local name="$1"
    shift
    command -v "$1" >/dev/null 2>&1 || {
        printf 'ERROR: required tool is missing: %s\n' "$1" >&2
        exit 64
    }
    printf '%s=%s\n' "$name" "$(first_line "$@")"
}

{
    printf 'SCHEMA_VERSION=1\n'
    printf 'RECORDED_AT=%s\n' "$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
    printf 'SOURCE_SHA=%s\n' "${SOURCE_SHA:-unknown}"
    required_version GIT git --version
    required_version UV uv --version
    required_version PYTHON python3 --version
    required_version JAVA java -version
    required_version JAVAC javac -version
    required_version MAVEN mvn --version
    required_version NODE node --version
    required_version NPM npm --version
    required_version PNPM pnpm --version
    required_version RUSTC rustc --version
    required_version CARGO cargo --version
    required_version GO go version
    required_version DOTNET dotnet --version
    required_version WASM_PACK wasm-pack --version
    required_version JQ jq --version
} > "$OUTPUT_FILE"

chmod 600 "$OUTPUT_FILE"
