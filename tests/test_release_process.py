"""Regression tests for the fail-closed release pipeline."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_go_binary_requires_gated_workflow_dispatch() -> None:
    workflow = read(".github/workflows/go-binary.yml")

    assert "workflow_dispatch:" in workflow
    assert "tags: ['sdk/go/v*']" not in workflow
    assert "ref: ${{ inputs.tag }}" in workflow


def test_conformance_ignores_go_binary_release_event() -> None:
    workflow = read(".github/workflows/sdk-conformance.yml")

    assert "startsWith(github.event.release.tag_name, 'v')" in workflow
    assert "^v[0-9]+\\.[0-9]+\\.[0-9]+$" in workflow
    assert "ref: ${{ github.event_name == 'release'" in workflow


def test_release_waits_for_remote_gate_before_tags_and_release() -> None:
    script = read("scripts/release.sh")

    gate = script.index('gh run watch "$RUN_ID" --exit-status')
    tag = script.index('git tag -a "v$VERSION"')
    release = script.index('gh release create "v$VERSION"')
    assert gate < tag < release
    assert "ALLOW_ALERT_CHECK_FAILURE" in script


def test_release_gate_uses_pinned_corpus_and_go_lint() -> None:
    makefile = read("Makefile")
    lock = read("tests/data/corpus.lock").strip()

    assert "release-gate: test-corpus-prepare" in makefile
    assert "golangci-lint/cmd/golangci-lint@v1.64.8" in makefile
    assert len(lock) == 40
    assert all(char in "0123456789abcdef" for char in lock)


def test_release_verify_is_version_scoped_and_fail_closed() -> None:
    script = read("scripts/release-verify.sh")

    assert '--branch "$branch" --event "$event"' in script
    assert "發布 workflows 等待逾時" in script
    assert "registry artifact 等待逾時" in script
    assert 'git -C "$TAP_DIR" pull --ff-only' in script
    assert "diff --quiet -- Formula/zhtw.rb" in script
