#!/usr/bin/env bash

set -euo pipefail

ACTION="${1:-}"
ARTIFACT_DIR="${ARTIFACT_DIR:-artifacts}"
STATE_DIR="${DEPLOY_STATE_DIR:-.jenkins-docs-deploy-state}"
SITE_DIR="$STATE_DIR/site"

die() {
    printf 'ERROR: %s\n' "$*" >&2
    exit 64
}

require_common() {
    [ "${CI_PROVIDER:-}" = jenkins ] || die "Docs publication requires Jenkins"
    [ "${JOB_NAME:-}" = zhtw/docs-publish ] || die "JOB_NAME must be zhtw/docs-publish"
    [[ "${DOCS_BUILD_NUMBER:-}" =~ ^[1-9][0-9]*$ ]] || die "DOCS_BUILD_NUMBER must be a positive integer"
    [[ "${SOURCE_SHA:-}" =~ ^[0-9a-f]{40}$ ]] || die "SOURCE_SHA must be a full Git SHA"
    [[ "${PROJECT_TREE_SHA:-}" =~ ^[0-9a-f]{40}$ ]] || die "PROJECT_TREE_SHA must be a full Git tree SHA"
    [ "${DOCS_BASE_URL:-}" = "https://zhtw.rajatim.com" ] || die "Unexpected DOCS_BASE_URL"
    [ "${AWS_REGION:-}" = us-east-1 ] || die "AWS_REGION must be us-east-1"
    [ "${DOCS_STACK_NAME:-}" = zhtw-public-docs ] || die "Unexpected stack name"
    [ "${DOCS_BUCKET_NAME:-}" = rajatim-zhtw-docs-381083412708-use1 ] || die "Unexpected bucket name"
    [ -s "$ARTIFACT_DIR/manifest.properties" ] || die "Artifact manifest is missing"
    [ -s "$ARTIFACT_DIR/SHA256SUMS" ] || die "Artifact checksum inventory is missing"
    [ -s "$ARTIFACT_DIR/payload/site.tar.gz" ] || die "Site archive is missing"
    grep -Fx "SYSTEM=zhtw-docs" "$ARTIFACT_DIR/manifest.properties" >/dev/null
    grep -Fx "BUILD_NUMBER=$DOCS_BUILD_NUMBER" "$ARTIFACT_DIR/manifest.properties" >/dev/null
    grep -Fx "SOURCE_SHA=$SOURCE_SHA" "$ARTIFACT_DIR/manifest.properties" >/dev/null
    grep -Fx "PROJECT_TREE_SHA=$PROJECT_TREE_SHA" "$ARTIFACT_DIR/manifest.properties" >/dev/null
    (cd "$ARTIFACT_DIR" && sha256sum -c SHA256SUMS >/dev/null)
}

require_aws() {
    require_common
    [ -n "${AWS_ACCESS_KEY_ID:-}" ] || die "AWS_ACCESS_KEY_ID must come from Jenkins Credentials"
    [ -n "${AWS_SECRET_ACCESS_KEY:-}" ] || die "AWS_SECRET_ACCESS_KEY must come from Jenkins Credentials"
    [ -z "${AWS_PROFILE:-}" ] || die "AWS_PROFILE is forbidden in Jenkins publication"
    command -v aws >/dev/null 2>&1 || die "aws CLI is required"
    export AWS_PAGER=""
}

site_sha256() {
    sha256sum "$ARTIFACT_DIR/payload/site.tar.gz" | cut -d' ' -f1
}

distribution_id() {
    aws cloudformation describe-stacks --region "$AWS_REGION" --stack-name "$DOCS_STACK_NAME" \
        --query 'Stacks[0].Outputs[?OutputKey==`DistributionId`].OutputValue | [0]' --output text
}

inspect_release() {
    require_common
    printf 'target=%s\nsource_sha=%s\nproject_tree_sha=%s\ndocs_build=%s\nsite_sha256=%s\n' \
        "$DOCS_BASE_URL" "$SOURCE_SHA" "$PROJECT_TREE_SHA" "$DOCS_BUILD_NUMBER" "$(site_sha256)"
    curl --fail --silent --show-error --max-time 15 "$DOCS_BASE_URL/deployment.json" || \
        printf '%s\n' 'current_release=not-published'
}

credential_preflight() {
    require_aws
    local account bucket distribution
    account="$(aws sts get-caller-identity --query Account --output text)"
    [ "$account" = "${AWS_ACCOUNT_ID:-381083412708}" ] || die "Unexpected AWS account"
    bucket="$(aws cloudformation describe-stacks --region "$AWS_REGION" --stack-name "$DOCS_STACK_NAME" \
        --query 'Stacks[0].Outputs[?OutputKey==`BucketName`].OutputValue | [0]' --output text)"
    [ "$bucket" = "$DOCS_BUCKET_NAME" ] || die "Stack bucket output mismatch"
    distribution="$(distribution_id)"
    [[ "$distribution" =~ ^[A-Z0-9]+$ ]] || die "Invalid CloudFront distribution ID"
    aws s3api list-objects-v2 --bucket "$DOCS_BUCKET_NAME" --prefix current/ --max-items 1 \
        --query 'KeyCount' --output text >/dev/null
    aws s3api get-bucket-versioning --bucket "$DOCS_BUCKET_NAME" --query Status --output text | grep -Fx Enabled >/dev/null
    aws cloudfront get-distribution --id "$distribution" --query 'Distribution.Status' --output text | grep -Fx Deployed >/dev/null
    printf 'credential_preflight=PASS\naccount=%s\nbucket=%s\ndistribution=%s\n' "$account" "$bucket" "$distribution"
}

backup_current() {
    require_aws
    install -d -m 0700 "$STATE_DIR"
    if aws s3 cp "s3://$DOCS_BUCKET_NAME/deploy-state/current.properties" "$STATE_DIR/previous.properties" --no-progress 2>/dev/null; then
        grep -E '^SOURCE_SHA=[0-9a-f]{40}$' "$STATE_DIR/previous.properties" >/dev/null || die "Invalid previous deployment state"
    else
        printf 'SOURCE_SHA=NONE\n' > "$STATE_DIR/previous.properties"
    fi
}

extract_site() {
    rm -rf "$SITE_DIR"
    mkdir -p "$SITE_DIR"
    python3 - "$ARTIFACT_DIR/payload/site.tar.gz" "$SITE_DIR" <<'PY'
import tarfile
from pathlib import Path
import sys

archive_path, target_path = sys.argv[1:]
target = Path(target_path).resolve()
with tarfile.open(archive_path, "r:gz") as archive:
    for member in archive.getmembers():
        if member.name.startswith("/") or ".." in member.name.split("/") or member.issym() or member.islnk():
            raise SystemExit(f"unsafe archive member: {member.name}")
    archive.extractall(target)
PY
}

write_release_inventory() {
    (
        cd "$SITE_DIR"
        find . -type f ! -name RELEASE_SHA256SUMS -print0 | LC_ALL=C sort -z | \
            xargs -0 sha256sum > RELEASE_SHA256SUMS
        sha256sum -c RELEASE_SHA256SUMS >/dev/null
    )
}

verify_release_prefix() {
    local remote_dir="$STATE_DIR/remote-release"
    rm -rf "$remote_dir"
    mkdir -p "$remote_dir"
    aws s3 sync "s3://$DOCS_BUCKET_NAME/releases/$SOURCE_SHA/" "$remote_dir/" \
        --delete --only-show-errors
    [ -s "$remote_dir/RELEASE_SHA256SUMS" ] || die "Remote release checksum inventory is missing"
    cmp "$SITE_DIR/RELEASE_SHA256SUMS" "$remote_dir/RELEASE_SHA256SUMS" >/dev/null || \
        die "Remote release checksum inventory does not match the selected artifact"
    (cd "$remote_dir" && sha256sum -c RELEASE_SHA256SUMS >/dev/null)
    python3 - "$remote_dir" "$SOURCE_SHA" <<'PY'
import json
from pathlib import Path
import sys

root = Path(sys.argv[1])
inventory = root / "RELEASE_SHA256SUMS"
expected = {
    line.split("  ", 1)[1]
    for line in inventory.read_text(encoding="utf-8").splitlines()
    if line
}
actual = {
    f"./{path.relative_to(root).as_posix()}"
    for path in root.rglob("*")
    if path.is_file() and path != inventory
}
if actual != expected:
    raise SystemExit("Remote release file inventory mismatch")
payload = json.loads((root / "deployment.json").read_text(encoding="utf-8"))
if payload.get("source_sha") != sys.argv[2]:
    raise SystemExit("Remote deployment.json source SHA mismatch")
PY
    rm -rf "$remote_dir"
}

transfer_release() {
    require_aws
    extract_site
    write_release_inventory
    local release_state expected existing
    release_state="deploy-state/releases/$SOURCE_SHA.properties"
    expected="$(site_sha256)"
    existing="$(aws s3 cp "s3://$DOCS_BUCKET_NAME/$release_state" - --no-progress 2>/dev/null || true)"
    if [ -n "$existing" ]; then
        grep -Fx "SITE_SHA256=$expected" <<<"$existing" >/dev/null || die "Immutable release prefix checksum mismatch"
        verify_release_prefix
        return 0
    fi
    aws s3 sync "$SITE_DIR/" "s3://$DOCS_BUCKET_NAME/releases/$SOURCE_SHA/" \
        --only-show-errors --cache-control 'public,max-age=300'
    while IFS= read -r -d '' file; do
        key="${file#"$SITE_DIR/"}"
        aws s3 cp "$file" "s3://$DOCS_BUCKET_NAME/releases/$SOURCE_SHA/$key" \
            --only-show-errors --cache-control 'no-cache, max-age=0, must-revalidate'
    done < <(find "$SITE_DIR" -type f \( -name '*.html' -o -name '*.json' -o -name '*.xml' \) -print0)
    verify_release_prefix
    printf 'SOURCE_SHA=%s\nPROJECT_TREE_SHA=%s\nDOCS_BUILD_NUMBER=%s\nSITE_SHA256=%s\n' \
        "$SOURCE_SHA" "$PROJECT_TREE_SHA" "$DOCS_BUILD_NUMBER" "$expected" | \
        aws s3 cp - "s3://$DOCS_BUCKET_NAME/$release_state" --only-show-errors \
            --content-type text/plain --cache-control no-store
}

invalidate_distribution() {
    local distribution invalidation
    distribution="$(distribution_id)"
    invalidation="$(aws cloudfront create-invalidation --distribution-id "$distribution" --paths '/*' \
        --query 'Invalidation.Id' --output text)"
    aws cloudfront wait invalidation-completed --distribution-id "$distribution" --id "$invalidation"
}

switch_current() {
    require_aws
    [ -s "$STATE_DIR/previous.properties" ] || die "Backup state is missing"
    touch "$STATE_DIR/mutation-started"
    aws s3 sync "s3://$DOCS_BUCKET_NAME/releases/$SOURCE_SHA/" "s3://$DOCS_BUCKET_NAME/current/" \
        --delete --only-show-errors
    printf 'SOURCE_SHA=%s\nPROJECT_TREE_SHA=%s\nDOCS_BUILD_NUMBER=%s\nSITE_SHA256=%s\n' \
        "$SOURCE_SHA" "$PROJECT_TREE_SHA" "$DOCS_BUILD_NUMBER" "$(site_sha256)" | \
        aws s3 cp - "s3://$DOCS_BUCKET_NAME/deploy-state/current.properties" --only-show-errors \
            --content-type text/plain --cache-control no-store
    invalidate_distribution
}

verify_public() {
    require_aws
    local body status headers
    body="$(curl --fail --silent --show-error --max-time 30 "$DOCS_BASE_URL/deployment.json")"
    python3 -c 'import json,sys; assert json.load(sys.stdin)["source_sha"] == sys.argv[1]' "$SOURCE_SHA" <<<"$body"
    curl --fail --silent --show-error --max-time 30 "$DOCS_BASE_URL/" | grep -Eiq 'ZHTW|zhtw'
    curl --fail --silent --show-error --max-time 30 "$DOCS_BASE_URL/en/" | grep -Eiq 'ZHTW|zhtw'
    status="$(curl --silent --output /dev/null --write-out '%{http_code}' --max-time 30 "$DOCS_BASE_URL/__zhtw_missing_page__")"
    [ "$status" = 404 ] || die "Missing page returned HTTP $status instead of 404"
    headers="$(curl --silent --show-error --head --max-time 30 "$DOCS_BASE_URL/")"
    grep -Eiq '^strict-transport-security:' <<<"$headers" || die "HSTS header is missing"
    touch "$STATE_DIR/verified"
}

rollback_current() {
    require_aws
    [ -s "$STATE_DIR/previous.properties" ] || die "Previous deployment state is missing"
    local previous
    previous="$(sed -n 's/^SOURCE_SHA=//p' "$STATE_DIR/previous.properties")"
    if [ "$previous" = NONE ]; then
        aws s3 rm "s3://$DOCS_BUCKET_NAME/current/" --recursive --only-show-errors
        aws s3 rm "s3://$DOCS_BUCKET_NAME/deploy-state/current.properties" --only-show-errors || true
    else
        [[ "$previous" =~ ^[0-9a-f]{40}$ ]] || die "Invalid rollback source SHA"
        aws s3 sync "s3://$DOCS_BUCKET_NAME/releases/$previous/" "s3://$DOCS_BUCKET_NAME/current/" \
            --delete --only-show-errors
        aws s3 cp "s3://$DOCS_BUCKET_NAME/deploy-state/releases/$previous.properties" \
            "s3://$DOCS_BUCKET_NAME/deploy-state/current.properties" --only-show-errors
    fi
    invalidate_distribution
    touch "$STATE_DIR/rollback-succeeded"
}

finalize_release() {
    require_aws
    [ -f "$STATE_DIR/verified" ] || die "Public verification has not passed"
    rm -f "$STATE_DIR/mutation-started"
    printf 'published_source_sha=%s\n' "$SOURCE_SHA"
}

cleanup_release() {
    require_common
    if [ -f "$STATE_DIR/mutation-started" ] && [ ! -f "$STATE_DIR/rollback-succeeded" ]; then
        die "Mutation is unresolved; preserving deployment state"
    fi
    rm -rf "$SITE_DIR"
}

case "$ACTION" in
    inspect) inspect_release ;;
    credential-preflight) credential_preflight ;;
    backup) backup_current ;;
    transfer) transfer_release ;;
    switch) switch_current ;;
    verify) verify_public ;;
    rollback) rollback_current ;;
    finalize) finalize_release ;;
    cleanup) cleanup_release ;;
    *) die "Usage: scripts/jenkins-docs-publish.sh {inspect|credential-preflight|backup|transfer|switch|verify|rollback|finalize|cleanup}" ;;
esac
