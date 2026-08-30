#!/usr/bin/env bash

set -euo pipefail

ACTION="${1:-}"
OUTPUT_DIR="${2:-}"

die() {
    printf 'ERROR: %s\n' "$*" >&2
    exit 64
}

require_runtime() {
    [ "${CI_PROVIDER:-}" = jenkins ] || die "Formal docs artifacts require Jenkins"
    [ "${JOB_NAME:-}" = zhtw/docs-build ] || die "JOB_NAME must be zhtw/docs-build"
    [ -n "${JENKINS_URL:-}" ] || die "JENKINS_URL is required"
    [ -n "${WORKSPACE:-}" ] || die "WORKSPACE is required"
    [ "${SOURCE_BRANCH:-}" = main ] || die "SOURCE_BRANCH must be main"
    [[ "${SOURCE_SHA:-}" =~ ^[0-9a-f]{40}$ ]] || die "SOURCE_SHA must be a full Git SHA"
    [[ "${PROJECT_TREE_SHA:-}" =~ ^[0-9a-f]{40}$ ]] || die "PROJECT_TREE_SHA must be a full Git tree SHA"
    [[ "${BUILD_CI_CONTROL_SHA:-}" =~ ^[0-9a-f]{40}$ ]] || die "BUILD_CI_CONTROL_SHA must be a full Git SHA"
    [[ "${BUILD_NUMBER:-}" =~ ^[1-9][0-9]*$ ]] || die "BUILD_NUMBER must be a positive integer"
}

check_source_identity() {
    [ "$(git rev-parse HEAD)" = "$SOURCE_SHA" ] || die "Checkout is not SOURCE_SHA"
    [ "$(git rev-parse "$SOURCE_SHA^{tree}")" = "$PROJECT_TREE_SHA" ] || die "PROJECT_TREE_SHA mismatch"
    [ -z "$(git status --porcelain)" ] || die "Docs source checkout is dirty"
}

create_archive() {
    python3 - "$OUTPUT_DIR/payload/site.tar.gz" <<'PY'
import gzip
import os
import tarfile
from pathlib import Path
import sys

source = Path("site")
target = Path(sys.argv[1])
with target.open("wb") as raw:
    with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as compressed:
        with tarfile.open(fileobj=compressed, mode="w", format=tarfile.PAX_FORMAT) as archive:
            for path in sorted(source.rglob("*"), key=lambda item: item.as_posix()):
                relative = path.relative_to(source)
                info = archive.gettarinfo(str(path), arcname=relative.as_posix())
                info.uid = info.gid = 0
                info.uname = info.gname = ""
                info.mtime = 0
                if path.is_file():
                    with path.open("rb") as stream:
                        archive.addfile(info, stream)
                else:
                    archive.addfile(info)
PY
}

build_artifact() {
    require_runtime
    check_source_identity
    [ -n "$OUTPUT_DIR" ] || die "build requires an output directory"
    [ ! -e "$OUTPUT_DIR" ] || die "Output directory must not already exist"

    uv sync --frozen --extra dev
    make docs-build
    [ -s site/index.html ] || die "Traditional Chinese site index is missing"
    [ -s site/en/index.html ] || die "English site index is missing"

    cat > site/deployment.json <<EOF
{"source_sha":"$SOURCE_SHA","project_tree_sha":"$PROJECT_TREE_SHA","docs_build_number":"$BUILD_NUMBER"}
EOF
    mkdir -p "$OUTPUT_DIR/payload" "$OUTPUT_DIR/metadata"
    create_archive
    cat > "$OUTPUT_DIR/manifest.properties" <<EOF
SCHEMA_VERSION=2
CI_PROVIDER=jenkins
SYSTEM=zhtw-docs
SOURCE_REPO=https://github.com/rajatim/zhtw.git
SOURCE_BRANCH=main
SOURCE_SHA=$SOURCE_SHA
PROJECT_TREE_SHA=$PROJECT_TREE_SHA
BUILD_JOB=zhtw/docs-build
BUILD_NUMBER=$BUILD_NUMBER
BUILD_CI_CONTROL_SHA=$BUILD_CI_CONTROL_SHA
BUILT_AT=${BUILT_AT:-unknown}
EOF
    printf '%s\n' "$SOURCE_SHA" > "$OUTPUT_DIR/metadata/source-sha"
    printf '%s\n' "$PROJECT_TREE_SHA" > "$OUTPUT_DIR/metadata/project-tree-sha"
    (
        cd "$OUTPUT_DIR"
        find payload metadata -type f -print0 | LC_ALL=C sort -z | xargs -0 sha256sum > SHA256SUMS
        sha256sum -c SHA256SUMS
    )
}

verify_artifact() {
    require_runtime
    check_source_identity
    [ -n "$OUTPUT_DIR" ] || die "verify requires an artifact directory"
    [ -s "$OUTPUT_DIR/manifest.properties" ] || die "Artifact manifest is missing"
    [ -s "$OUTPUT_DIR/SHA256SUMS" ] || die "Artifact checksum inventory is missing"
    [ -s "$OUTPUT_DIR/payload/site.tar.gz" ] || die "Site archive is missing"
    grep -Fx "SYSTEM=zhtw-docs" "$OUTPUT_DIR/manifest.properties" >/dev/null
    grep -Fx "SCHEMA_VERSION=2" "$OUTPUT_DIR/manifest.properties" >/dev/null
    grep -Fx "SOURCE_SHA=$SOURCE_SHA" "$OUTPUT_DIR/manifest.properties" >/dev/null
    grep -Fx "PROJECT_TREE_SHA=$PROJECT_TREE_SHA" "$OUTPUT_DIR/manifest.properties" >/dev/null
    grep -Fx "BUILD_CI_CONTROL_SHA=$BUILD_CI_CONTROL_SHA" "$OUTPUT_DIR/manifest.properties" >/dev/null
    (cd "$OUTPUT_DIR" && sha256sum -c SHA256SUMS)
    python3 - "$OUTPUT_DIR/payload/site.tar.gz" "$SOURCE_SHA" <<'PY'
import json
import tarfile
import sys

archive_path, expected_sha = sys.argv[1:]
with tarfile.open(archive_path, "r:gz") as archive:
    names = set(archive.getnames())
    required = {"index.html", "en/index.html", "deployment.json"}
    missing = sorted(required - names)
    if missing:
        raise SystemExit(f"site archive is missing: {', '.join(missing)}")
    for member in archive.getmembers():
        if member.name.startswith("/") or ".." in member.name.split("/") or member.issym() or member.islnk():
            raise SystemExit(f"unsafe archive member: {member.name}")
    payload = json.load(archive.extractfile("deployment.json"))
    if payload.get("source_sha") != expected_sha:
        raise SystemExit("deployment.json source SHA mismatch")
PY
}

case "$ACTION" in
    build) build_artifact ;;
    verify) verify_artifact ;;
    *) die "Usage: scripts/jenkins-docs-build.sh {build|verify} <directory>" ;;
esac
