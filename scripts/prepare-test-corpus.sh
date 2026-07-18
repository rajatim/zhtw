#!/usr/bin/env bash

set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
CORPUS_DIR="$ROOT/tests/data/corpus"
LOCK_FILE="$ROOT/tests/data/corpus.lock"
REPOSITORY="https://github.com/rajatim/zhtw-test-corpus"
EXPECTED="$(tr -d '[:space:]' < "$LOCK_FILE")"

[[ "$EXPECTED" =~ ^[0-9a-f]{40}$ ]] || {
    echo "invalid corpus lock: $LOCK_FILE" >&2
    exit 1
}

if [ ! -d "$CORPUS_DIR/.git" ]; then
    rm -rf "$CORPUS_DIR"
    git clone --filter=blob:none --no-checkout "$REPOSITORY" "$CORPUS_DIR"
    git -C "$CORPUS_DIR" fetch --depth 1 origin "$EXPECTED"
    git -C "$CORPUS_DIR" checkout --detach "$EXPECTED"
fi

ACTUAL="$(git -C "$CORPUS_DIR" rev-parse HEAD)"
[ "$ACTUAL" = "$EXPECTED" ] || {
    echo "corpus version mismatch: expected $EXPECTED, got $ACTUAL" >&2
    echo "remove tests/data/corpus and run 'make test-corpus-prepare'" >&2
    exit 1
}

CORPUS_STATUS="$(git -C "$CORPUS_DIR" status --porcelain --untracked-files=all -- \
    news regressions social tech wiki)"
[ -z "$CORPUS_STATUS" ] || {
    echo "curated corpus files differ from the pinned commit:" >&2
    printf '%s\n' "$CORPUS_STATUS" >&2
    exit 1
}

echo "corpus ready: $EXPECTED"
