"""Regression tests for the Jenkins-only release pipeline."""

import hashlib
import json
import re
import shutil
import subprocess
from dataclasses import asdict
from pathlib import Path

import pytest

import scripts.audit_corpus_idempotency as idempotency_audit
import scripts.update_idempotency_baseline_version as baseline_updater

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_github_actions_are_not_a_ci_or_release_path() -> None:
    workflows = ROOT / ".github" / "workflows"

    assert not workflows.exists() or not list(workflows.glob("*.yml"))
    assert not workflows.exists() or not list(workflows.glob("*.yaml"))


def test_direct_release_command_fails_closed() -> None:
    script = read("scripts/release.sh")

    assert "Use Jenkins zhtw/build, then zhtw/release" in script
    assert "exit 64" in script
    assert "git push" not in script
    assert "gh release" not in script
    assert "gh workflow" not in script


def test_jenkins_build_creates_one_complete_candidate() -> None:
    script = read("scripts/jenkins-build.sh")

    for phase in ("scan", "build", "test", "package", "verify"):
        assert f"{phase})" in script
    for package in ("python", "npm", "crates", "nuget", "maven", "go"):
        assert f"packages/{package}" in script
    assert "make release-gate" in script
    assert "candidate-tree-sha" in script
    assert "release.patch" in script
    assert "zhtw_checksums.txt" in script


def test_nuget_package_builds_every_target_before_no_build_pack() -> None:
    script = read("scripts/jenkins-build.sh")
    restore = "dotnet restore sdk/dotnet/Zhtw.csproj"
    build = "dotnet build sdk/dotnet/Zhtw.csproj -c Release --no-restore"
    pack = 'dotnet pack sdk/dotnet/Zhtw.csproj -c Release --no-build --no-restore -o "$destination"'

    assert script.index(restore) < script.index(build) < script.index(pack)


def test_python_candidate_excludes_uv_output_helper() -> None:
    script = read("scripts/jenkins-build.sh")

    assert 'rm -f "$destination/.gitignore"' in script
    assert 'find "$OUTPUT_DIR/packages/python" -maxdepth 1 -type f | wc -l' in script


def test_jenkins_release_is_idempotent_and_covers_every_target() -> None:
    script = read("scripts/jenkins-release.sh")

    for action in (
        "publish-git",
        "publish-pypi",
        "publish-npm-js",
        "publish-npm-wasm",
        "publish-crates",
        "publish-nuget",
        "publish-maven",
        "publish-homebrew",
    ):
        assert f"{action})" in script
    assert "registry_exists" in script
    assert "git push --atomic" in script
    assert "Existing GitHub asset differs" in script
    assert "Cargo repack differs from the archived crate" in script
    assert "publishingType=AUTOMATIC" in script


def test_release_secrets_are_not_command_line_arguments() -> None:
    script = read("scripts/jenkins-release.sh")

    assert '--password "$PYPI_TOKEN"' not in script
    assert '--api-key "$NUGET_API_KEY"' not in script
    assert '--token "$CARGO_REGISTRY_TOKEN"' not in script
    assert 'TWINE_PASSWORD="$PYPI_TOKEN"' in script
    assert "X-NuGet-ApiKey: %s" in script
    assert "_authToken=${NODE_AUTH_TOKEN}" in script


def test_release_secret_files_stay_in_disposable_workspace() -> None:
    script = read("scripts/jenkins-release.sh")

    assert "ZHTW_SECRET_RUNTIME_ROOT is required for publication" in script
    assert "ZHTW_SECRET_RUNTIME_ROOT must stay inside WORKSPACE" in script
    assert 'mktemp "$runtime_root/npmrc.XXXXXX"' in script
    assert 'mktemp -d "$runtime_root/maven.XXXXXX"' in script
    assert 'temporary_config="$(mktemp)"' not in script


def test_jenkins_verify_uses_isolated_podman_compatible_cli() -> None:
    script = read("scripts/jenkins-verify.sh")

    assert "prepare_container_cli" in script
    assert 'ln -sf "$(command -v podman)"' in script
    assert 'export DOCKER_CONFIG="$runtime_root/docker-config"' in script
    assert 'export REGISTRY_AUTH_FILE="$runtime_root/registry-auth.json"' in script
    assert "printf '{\"auths\":{}}\\n'" in script


def test_release_verify_is_read_only_and_version_scoped() -> None:
    script = read("scripts/release-verify.sh")

    assert "12/12 checks" in script
    assert "pypi.org/pypi/zhtw/$VERSION" in script
    assert "registry.npmjs.org/zhtw-js/$VERSION" in script
    assert "repo1.maven.org" in script
    assert "homebrew-tap/main/Formula/zhtw.rb" in script
    assert "git commit" not in script
    assert "git push" not in script
    assert "gh run" not in script


def test_version_bump_is_portable(tmp_path: Path) -> None:
    files = (
        "pyproject.toml",
        "src/zhtw/__init__.py",
        "sdk/java/pom.xml",
        "sdk/typescript/package.json",
        "sdk/rust/Cargo.toml",
        "sdk/rust/zhtw-wasm/package.json",
        "sdk/dotnet/Zhtw.csproj",
        "AGENTS.md",
        "README.md",
        "README.en.md",
        "sdk/java/BENCHMARK.md",
        "sdk/java/README.md",
        "sdk/go/README.md",
        "sdk/dotnet/README.md",
        "sdk/rust/zhtw/README.md",
    )
    for relative in files:
        source = ROOT / relative
        destination = tmp_path / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

    subprocess.run(
        ["python3", str(ROOT / "scripts/bump_version.py"), "9.8.7"],
        cwd=tmp_path,
        check=True,
    )
    assert 'version = "9.8.7"' in (tmp_path / "pyproject.toml").read_text()
    assert '"version": "9.8.7"' in (tmp_path / "sdk/typescript/package.json").read_text()
    assert "sed -i ''" not in read("Makefile")


def test_release_candidate_keeps_unreleased_notes(tmp_path: Path) -> None:
    (tmp_path / "CHANGELOG.md").write_text(
        "# Changelog\n\n"
        "## [Unreleased]\n\n"
        "### Changed\n\n"
        "- Candidate fixture note.\n\n"
        "## [1.0.0] - 2026-01-01\n\n"
        "- Previous release.\n",
        encoding="utf-8",
    )
    notes = tmp_path / "release-notes.md"

    subprocess.run(
        [
            "python3",
            str(ROOT / "scripts/prepare_release_candidate.py"),
            "--version",
            "9.8.7",
            "--date",
            "2026-08-09",
            "--notes-output",
            str(notes),
        ],
        cwd=tmp_path,
        check=True,
    )
    assert "Candidate fixture note." in notes.read_text(encoding="utf-8")
    assert "## [9.8.7] - 2026-08-09" in (tmp_path / "CHANGELOG.md").read_text(encoding="utf-8")


def test_version_bump_refreshes_local_benchmark_lock(tmp_path: Path) -> None:
    lock_path = tmp_path / "benchmarks/accuracy/competitors.lock.json"
    data_path = tmp_path / "sdk/data/zhtw-data.json"
    lock_path.parent.mkdir(parents=True)
    data_path.parent.mkdir(parents=True)
    shutil.copy2(ROOT / "benchmarks/accuracy/competitors.lock.json", lock_path)
    payload = json.loads((ROOT / "sdk/data/zhtw-data.json").read_text(encoding="utf-8"))
    payload["version"] = "9.8.7"
    data_path.write_text(json.dumps(payload, ensure_ascii=False) + "\n", encoding="utf-8")

    subprocess.run(
        ["python3", str(ROOT / "scripts/update_local_benchmark_lock.py"), "9.8.7"],
        cwd=tmp_path,
        check=True,
    )

    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    local = next(item for item in lock["competitors"] if item["id"] == "zhtw")
    digest = hashlib.sha256(data_path.read_bytes()).hexdigest()
    assert local["version"] == "9.8.7"
    assert local["artifact_sha256"]["sdk/data/zhtw-data.json"] == digest
    assert local["config_sha256"] == digest


def test_version_bump_advances_only_an_unchanged_idempotency_baseline(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    inputs = tmp_path / "inputs.json"
    baseline = tmp_path / "baseline.json"
    inputs.write_text("{}\n", encoding="utf-8")
    summary = idempotency_audit.Summary(
        schema_version=1,
        dataset="fixture",
        converter_version="9.8.7",
        inputs_sha256="a" * 64,
        total_cases=10,
        idempotent_cases=9,
        non_idempotent_cases=1,
        idempotency_rate=0.9,
        non_idempotent_ids_sha256="b" * 64,
    )
    payload = asdict(summary)
    payload["converter_version"] = "4.4.3"
    baseline.write_text(json.dumps(payload), encoding="utf-8")
    monkeypatch.setattr(baseline_updater, "build_summary", lambda _: summary)

    baseline_updater.update_baseline("9.8.7", inputs, baseline)

    updated = json.loads(baseline.read_text(encoding="utf-8"))
    assert updated == asdict(summary)


def test_version_bump_rejects_changed_idempotency_results(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    inputs = tmp_path / "inputs.json"
    baseline = tmp_path / "baseline.json"
    inputs.write_text("{}\n", encoding="utf-8")
    summary = idempotency_audit.Summary(
        schema_version=1,
        dataset="fixture",
        converter_version="9.8.7",
        inputs_sha256="a" * 64,
        total_cases=10,
        idempotent_cases=9,
        non_idempotent_cases=1,
        idempotency_rate=0.9,
        non_idempotent_ids_sha256="b" * 64,
    )
    payload = asdict(summary)
    payload["converter_version"] = "4.4.3"
    payload["idempotent_cases"] = 8
    baseline.write_text(json.dumps(payload), encoding="utf-8")
    monkeypatch.setattr(baseline_updater, "build_summary", lambda _: summary)

    with pytest.raises(ValueError, match="idempotent_cases"):
        baseline_updater.update_baseline("9.8.7", inputs, baseline)


def test_idempotency_baseline_updater_runs_as_a_script(tmp_path: Path) -> None:
    baseline = tmp_path / "baseline.json"
    shutil.copy2(ROOT / "benchmarks/accuracy/blind-v2.idempotency-baseline.json", baseline)

    subprocess.run(
        [
            "python3",
            str(ROOT / "scripts/update_idempotency_baseline_version.py"),
            idempotency_audit.__version__,
            "--inputs",
            str(ROOT / "benchmarks/accuracy/blind-v2.inputs.json"),
            "--baseline",
            str(baseline),
        ],
        cwd=tmp_path,
        check=True,
    )

    assert (
        json.loads(baseline.read_text(encoding="utf-8"))["converter_version"]
        == idempotency_audit.__version__
    )


def test_release_gate_uses_pinned_corpus_and_go_lint() -> None:
    makefile = read("Makefile")
    lock = read("tests/data/corpus.lock").strip()

    assert "release-gate: test-corpus-prepare" in makefile
    assert "golangci-lint/cmd/golangci-lint@v1.64.8" in makefile
    assert len(lock) == 40
    assert all(char in "0123456789abcdef" for char in lock)


def test_shell_variables_before_non_ascii_text_are_braced() -> None:
    pattern = re.compile(r"\$[A-Za-z_][A-Za-z0-9_]*[^\x00-\x7f]")

    for script in (ROOT / "scripts").glob("*.sh"):
        assert not pattern.search(read(str(script.relative_to(ROOT)))), script
