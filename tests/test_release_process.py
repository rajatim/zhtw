"""Regression tests for the Jenkins-only release pipeline."""

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from dataclasses import asdict
from pathlib import Path

import pytest

import scripts.audit_corpus_idempotency as idempotency_audit
import scripts.update_idempotency_baseline_version as baseline_updater

ROOT = Path(__file__).resolve().parents[1]
JENKINS_IDENTITY_VARIABLES = (
    "CI_PROVIDER",
    "JOB_NAME",
    "JENKINS_URL",
    "BUILD_TAG",
    "WORKSPACE",
    "ZHTW_JENKINS_RELEASE",
)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def outside_jenkins_environment() -> dict[str, str]:
    environment = os.environ.copy()
    for name in JENKINS_IDENTITY_VARIABLES:
        environment.pop(name, None)
    return environment


def test_github_actions_are_not_a_ci_or_release_path() -> None:
    workflows = ROOT / ".github" / "workflows"
    agent_rules = read("AGENTS.md")

    assert not workflows.exists() or not list(workflows.glob("*.yml"))
    assert not workflows.exists() or not list(workflows.glob("*.yaml"))
    assert "folder-scoped Jenkins" in agent_rules
    assert "1Password" in agent_rules
    assert "disposable workspace" in agent_rules


def test_direct_release_command_fails_closed() -> None:
    script = read("scripts/release.sh")

    assert "Use Jenkins zhtw/build, zhtw/verify for that build, then zhtw/release" in script
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


def test_packages_include_public_license_and_readme_metadata() -> None:
    wasm = json.loads(read("sdk/rust/zhtw-wasm/package.json"))
    dotnet = read("sdk/dotnet/Zhtw.csproj")

    assert "LICENSE" in wasm["files"]
    assert (ROOT / "sdk/rust/zhtw-wasm/LICENSE").read_bytes() == (ROOT / "LICENSE").read_bytes()
    assert "<PackageReadmeFile>README.md</PackageReadmeFile>" in dotnet
    assert '<None Include="README.md" Pack="true" PackagePath="/" />' in dotnet
    build = read("scripts/jenkins-build.sh")
    assert "tar -tzf \"$wasm_tgz\" | grep -Fx 'package/LICENSE'" in build
    assert "unzip -Z1 \"$nuget_package\" | grep -Fx 'README.md'" in build


def test_python_candidate_excludes_uv_output_helper() -> None:
    script = read("scripts/jenkins-build.sh")

    assert 'rm -f "$destination/.gitignore"' in script
    assert 'find "$OUTPUT_DIR/packages/python" -maxdepth 1 -type f | wc -l' in script


def test_jenkins_release_is_idempotent_and_covers_every_target() -> None:
    script = read("scripts/jenkins-release.sh")

    for action in (
        "preflight-git",
        "preflight-pypi",
        "preflight-npm",
        "preflight-crates",
        "preflight-nuget",
        "preflight-maven",
    ):
        assert f"{action})" in script
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
    assert "Existing PyPI file differs" in script
    assert "Existing npm package differs" in script
    assert "Existing NuGet package differs" in script
    assert "Existing Maven Central artifact differs" in script
    assert "Cargo repack differs from the archived crate" in script
    assert "publishingType=AUTOMATIC" in script


def test_public_release_adapter_fails_outside_jenkins() -> None:
    result = subprocess.run(
        [str(ROOT / "scripts/jenkins-release.sh"), "publish-git", "/missing"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        env=outside_jenkins_environment(),
    )

    assert result.returncode == 64
    assert "Release actions require Jenkins" in result.stderr


@pytest.mark.parametrize(
    ("script", "action", "message"),
    [
        ("scripts/jenkins-build.sh", "scan", "Formal candidates require Jenkins"),
        (
            "scripts/jenkins-verify.sh",
            "sdk-matrix",
            "Formal compatibility checks require Jenkins",
        ),
        ("scripts/jenkins-release.sh", "preview", "Release actions require Jenkins"),
    ],
)
def test_formal_cicd_adapters_fail_outside_matching_jenkins_job(
    script: str, action: str, message: str
) -> None:
    result = subprocess.run(
        [str(ROOT / script), action],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        env=outside_jenkins_environment(),
    )

    assert result.returncode == 64
    assert message in result.stderr


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
    assert "--cgroup-manager=cgroupfs --events-backend=file" in script
    assert 'chmod 700 "$runtime_root/bin/docker"' in script
    assert 'export DOCKER_CONFIG="$runtime_root/docker-config"' in script
    assert 'export REGISTRY_AUTH_FILE="$runtime_root/registry-auth.json"' in script
    assert "printf '{\"auths\":{}}\\n'" in script


def test_release_verify_is_read_only_and_version_scoped() -> None:
    script = read("scripts/release-verify.sh")

    assert "TOTAL_CHECKS=12" in script
    assert "Exact archived payload matches every public artifact" in script
    assert "pypi.org/pypi/zhtw/$VERSION" in script
    assert "registry.npmjs.org/zhtw-js/$VERSION" in script
    assert "repo1.maven.org" in script
    assert "homebrew-tap/main/Formula/zhtw.rb" in script
    assert "git commit" not in script
    assert "git push" not in script
    assert "gh run" not in script


def test_public_release_docs_require_detached_preflight_before_publish() -> None:
    rules = read(".claude/rules/releasing.md")
    checklist = read("docs/releases/RELEASE-CHECKLIST.md")

    for document in (rules, checklist):
        assert "RELEASE_ACTION=CREDENTIAL_PREFLIGHT" in document
        assert "jcli build zhtw/release -s -v" not in document
    assert "PREVIEW" in rules
    assert "PUBLISH_ALL" in rules
    assert "RESUME_ALL" in rules
    assert rules.index("RELEASE_ACTION=PREVIEW") < rules.index(
        "RELEASE_ACTION=CREDENTIAL_PREFLIGHT"
    )
    assert rules.index("RELEASE_ACTION=CREDENTIAL_PREFLIGHT") < rules.index(
        "RELEASE_ACTION=PUBLISH_ALL"
    )


def make_fake_release_curl(tmp_path: Path) -> Path:
    fake_bin = tmp_path / "bin"
    fake_bin.mkdir()
    curl = fake_bin / "curl"
    curl.write_text(
        """#!/usr/bin/env python3
import json
import os
import sys

url = sys.argv[-1]
if "sdk%2Fgo" in url:
    names = [
        "zhtw-darwin-amd64.tar.gz",
        "zhtw-darwin-arm64.tar.gz",
        "zhtw-linux-amd64.tar.gz",
        "zhtw-linux-arm64.tar.gz",
        "zhtw-windows-amd64.zip",
        "zhtw_checksums.txt",
    ]
    print(json.dumps({"assets": [{"name": name} for name in names]}))
elif "api.github.com" in url:
    print(json.dumps({"tag_name": "v9.8.7", "body": os.environ.get("RELEASE_BODY", "notes")}))
elif "homebrew-tap" in url:
    print('url "https://files.example/zhtw-9.8.7.tar.gz"')
elif "nuget.org" in url:
    print('{"versions":["9.8.7"]}')
else:
    print("{}")
""",
        encoding="utf-8",
    )
    curl.chmod(0o755)
    git = fake_bin / "git"
    git.write_text(
        """#!/usr/bin/env sh
printf '%s  %s\n' aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa "$3"
""",
        encoding="utf-8",
    )
    git.chmod(0o755)
    return fake_bin


def run_release_verify(tmp_path: Path, release_body: str) -> subprocess.CompletedProcess[str]:
    fake_bin = make_fake_release_curl(tmp_path)
    environment = os.environ.copy()
    environment.pop("GH_TOKEN", None)
    environment.update(
        {
            "PATH": f"{fake_bin}{os.pathsep}{environment['PATH']}",
            "RELEASE_BODY": release_body,
            "VERIFY_ATTEMPTS": "1",
            "VERIFY_INTERVAL": "0",
        }
    )
    return subprocess.run(
        [str(ROOT / "scripts/release-verify.sh"), "9.8.7"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        env=environment,
    )


def test_release_verify_reaches_all_twelve_checks(tmp_path: Path) -> None:
    result = run_release_verify(tmp_path, "Complete release notes")

    assert result.returncode == 0, result.stderr
    assert "12/12 checks" in result.stdout


def test_release_verify_rejects_an_empty_changelog(tmp_path: Path) -> None:
    result = run_release_verify(tmp_path, "   ")

    assert result.returncode == 1
    assert "11/12 checks" in result.stdout


def test_partial_pypi_retry_uploads_only_the_missing_file(tmp_path: Path) -> None:
    payload = tmp_path / "payload"
    distributions = payload / "packages" / "python"
    distributions.mkdir(parents=True)
    (distributions / "zhtw-9.8.7-py3-none-any.whl").write_bytes(b"wheel")
    (distributions / "zhtw-9.8.7.tar.gz").write_bytes(b"sdist")
    upload_log = tmp_path / "uploads"
    environment = os.environ.copy()
    environment.update(
        {
            "ADAPTER": str(ROOT / "scripts/jenkins-release.sh"),
            "PAYLOAD": str(payload),
            "UPLOAD_LOG": str(upload_log),
            "PYPI_TOKEN": "fixture",
        }
    )
    result = subprocess.run(
        [
            "bash",
            "-c",
            r"""
source "$ADAPTER" ignored "$PAYLOAD"
require_common() { :; }
ensure_git_release() { :; }
registry_exists() { return 0; }
pypi_file_matches() {
    case "$(basename "$1")" in
        *.whl) return 0 ;;
        *) [ -s "$UPLOAD_LOG" ] ;;
    esac
}
upload_pypi_file() { basename "$1" >> "$UPLOAD_LOG"; }
wait_for_pypi_file() { :; }
publish_pypi
""",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        env=environment,
    )

    assert result.returncode == 0, result.stderr
    assert upload_log.read_text(encoding="utf-8").splitlines() == ["zhtw-9.8.7.tar.gz"]


def test_resume_skips_exact_prior_registries_and_continues_at_nuget(
    tmp_path: Path,
) -> None:
    payload = tmp_path / "payload"
    for relative, content in (
        ("packages/python/zhtw-9.8.7-py3-none-any.whl", b"wheel"),
        ("packages/python/zhtw-9.8.7.tar.gz", b"sdist"),
        ("packages/npm/zhtw-js-9.8.7.tgz", b"js"),
        ("packages/npm/zhtw-wasm-9.8.7.tgz", b"wasm"),
        ("packages/crates/zhtw-9.8.7.crate", b"crate"),
        ("packages/nuget/Zhtw.9.8.7.nupkg", b"nuget"),
    ):
        path = payload / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    mutation_log = tmp_path / "mutations"
    result = subprocess.run(
        [
            "bash",
            "-c",
            r"""
source "$ADAPTER" ignored "$PAYLOAD"
require_common() { :; }
ensure_git_release() { :; }
registry_exists() {
    case "$1" in
        pypi|npm-js|npm-wasm|crates) return 0 ;;
        nuget) return 1 ;;
        *) return 2 ;;
    esac
}
pypi_file_matches() { :; }
npm_tarball_matches() { :; }
crate_matches() { :; }
upload_pypi_file() { printf 'unexpected-pypi-upload\n' >> "$MUTATION_LOG"; return 1; }
npm() { printf 'unexpected-npm-publish\n' >> "$MUTATION_LOG"; return 1; }
cargo() { printf 'unexpected-cargo-publish\n' >> "$MUTATION_LOG"; return 1; }
curl() { cat >/dev/null || true; printf 'nuget %s\n' "$*" >> "$MUTATION_LOG"; }
wait_for_registry() { [ "$1" = nuget ]; }
publish_pypi
publish_npm npm-js
publish_npm npm-wasm
publish_crates
publish_nuget
""",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        env={
            **os.environ,
            "ADAPTER": str(ROOT / "scripts/jenkins-release.sh"),
            "PAYLOAD": str(payload),
            "MUTATION_LOG": str(mutation_log),
            "PYPI_TOKEN": "fixture",
            "NODE_AUTH_TOKEN": "fixture",
            "CARGO_REGISTRY_TOKEN": "fixture",
            "NUGET_API_KEY": "fixture",
            "RELEASE_VERSION": "9.8.7",
        },
    )

    assert result.returncode == 0, result.stderr
    mutations = mutation_log.read_text(encoding="utf-8").splitlines()
    assert len(mutations) == 1
    assert "--request PUT" in mutations[0]
    assert "https://www.nuget.org/api/v2/package" in mutations[0]


def test_resume_refuses_an_existing_nuget_version_with_different_content(
    tmp_path: Path,
) -> None:
    package = tmp_path / "payload" / "packages" / "nuget" / "Zhtw.9.8.7.nupkg"
    package.parent.mkdir(parents=True)
    package.write_bytes(b"candidate")
    mutation_log = tmp_path / "mutations"
    result = subprocess.run(
        [
            "bash",
            "-c",
            r"""
source "$ADAPTER" ignored "$PAYLOAD"
require_common() { :; }
ensure_git_release() { :; }
registry_exists() { return 0; }
nuget_package_matches() { return 1; }
curl() { printf 'unexpected-put\n' >> "$MUTATION_LOG"; }
publish_nuget
""",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        env={
            **os.environ,
            "ADAPTER": str(ROOT / "scripts/jenkins-release.sh"),
            "PAYLOAD": str(tmp_path / "payload"),
            "MUTATION_LOG": str(mutation_log),
            "NUGET_API_KEY": "fixture",
            "RELEASE_VERSION": "9.8.7",
        },
    )

    assert result.returncode != 0
    assert not mutation_log.exists()


def test_crates_registry_probe_sends_a_named_user_agent(tmp_path: Path) -> None:
    curl_log = tmp_path / "curl-arguments"
    environment = os.environ.copy()
    environment.update(
        {
            "ADAPTER": str(ROOT / "scripts/jenkins-release.sh"),
            "CURL_LOG": str(curl_log),
        }
    )
    result = subprocess.run(
        [
            "bash",
            "-c",
            r"""
source "$ADAPTER" ignored /missing
RELEASE_VERSION=9.8.7
curl() { printf '%s\n' "$*" > "$CURL_LOG"; printf '200'; }
registry_exists crates
""",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        env=environment,
    )

    assert result.returncode == 0, result.stderr
    arguments = curl_log.read_text(encoding="utf-8")
    assert "-A zhtw-jenkins-release" in arguments
    assert "https://crates.io/api/v1/crates/zhtw/9.8.7" in arguments


def test_registry_probe_distinguishes_absence_from_service_failure() -> None:
    environment = os.environ.copy()
    environment.update({"ADAPTER": str(ROOT / "scripts/jenkins-release.sh")})
    script = r"""
source "$ADAPTER" ignored /missing
RELEASE_VERSION=9.8.7
curl() { printf '%s' "$REGISTRY_STATUS"; }
registry_exists npm-js
"""

    absent = subprocess.run(
        ["bash", "-c", script],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        env={**environment, "REGISTRY_STATUS": "404"},
    )
    unavailable = subprocess.run(
        ["bash", "-c", script],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        env={**environment, "REGISTRY_STATUS": "503"},
    )

    assert absent.returncode == 1
    assert unavailable.returncode == 2


def run_preflight_shell(
    tmp_path: Path, script: str, extra_environment: dict[str, str]
) -> subprocess.CompletedProcess[str]:
    environment = os.environ.copy()
    environment.update(
        {
            "ADAPTER": str(ROOT / "scripts/jenkins-release.sh"),
            "WORKSPACE": str(tmp_path),
            "ZHTW_SECRET_RUNTIME_ROOT": str(tmp_path / "secrets"),
            **extra_environment,
        }
    )
    return subprocess.run(
        ["bash", "-c", script],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        env=environment,
    )


def test_git_preflight_proves_both_ssh_write_paths_with_dry_runs(tmp_path: Path) -> None:
    tap = tmp_path / "tap"
    (tap / ".git").mkdir(parents=True)
    git_log = tmp_path / "git-log"
    result = run_preflight_shell(
        tmp_path,
        r"""
source "$ADAPTER" ignored /missing
require_common() { :; }
gh() {
    case "$*" in
        *"api user"*) printf 'rajatim\n' ;;
        *) printf 'true\n' ;;
    esac
}
git() {
    case "$*" in
        *"rev-parse refs/remotes/origin/main"*) printf '%040d\n' 0 ;;
        *"push --dry-run"*) printf '%s\n' "$*" >> "$GIT_LOG" ;;
        *) return 1 ;;
    esac
}
preflight_git "$TAP"
""",
        {"GH_TOKEN": "fixture", "GIT_LOG": str(git_log), "TAP": str(tap)},
    )

    assert result.returncode == 0, result.stderr
    pushes = git_log.read_text(encoding="utf-8").splitlines()
    assert len(pushes) == 2
    assert all("push --dry-run" in line for line in pushes)


def test_pypi_preflight_authenticates_without_a_file_upload(tmp_path: Path) -> None:
    curl_log = tmp_path / "curl-log"
    result = run_preflight_shell(
        tmp_path,
        r"""
source "$ADAPTER" ignored /missing
require_common() { :; }
curl() { printf '%s\n' "$*" > "$CURL_LOG"; printf '400'; }
preflight_pypi
""",
        {"PYPI_TOKEN": "pypi-" + "A" * 90, "CURL_LOG": str(curl_log)},
    )

    assert result.returncode == 0, result.stderr
    arguments = curl_log.read_text(encoding="utf-8")
    assert ":action=file_upload" in arguments
    assert "=@" not in arguments


def test_npm_preflight_checks_identity_scope_and_fourteen_day_expiry(tmp_path: Path) -> None:
    npm_log = tmp_path / "npm-log"
    result = run_preflight_shell(
        tmp_path,
        r"""
source "$ADAPTER" ignored /missing
require_common() { :; }
date() {
    case "$*" in
        *" -d "*) printf '2000000000\n' ;;
        *) printf '1900000000\n' ;;
    esac
}
npm() {
    printf '%s|%s\n' "$NPM_CONFIG_CACHE" "$*" >> "$NPM_LOG"
    case "$*" in
        *whoami*) printf 'rajatim\n' ;;
        *"token list"*)
            fingerprint="${NODE_AUTH_TOKEN:0:8}...${NODE_AUTH_TOKEN: -4}"
            printf '%s' '[{"token":"'
            printf '%s' "$fingerprint"
            printf '%s\n' '","expiry":"2099-01-01T00:00:00Z","bypass_2fa":true,' \
                '"revoked":null,"permissions":[{"name":"package","action":"write"}],' \
                '"scopes":[{"name":null,"type":"package"}]}]'
            ;;
        *"access list collaborators zhtw-js"*) printf '{"rajatim":"read-write"}\n' ;;
        *"access list collaborators zhtw-wasm"*) printf '{"rajatim":"read-write"}\n' ;;
        *) return 1 ;;
    esac
}
preflight_npm
""",
        {
            "NODE_AUTH_TOKEN": "npm_fixture_token_1234",
            "NPM_TOKEN_EXPIRES": "2099-01-01T00:00:00Z",
            "NPM_LOG": str(npm_log),
        },
    )

    assert result.returncode == 0, result.stderr
    lines = npm_log.read_text(encoding="utf-8").splitlines()
    commands = "\n".join(lines)
    assert "whoami" in commands
    assert "token list --json" in commands
    assert "access list collaborators zhtw-js rajatim" in commands
    assert "access list collaborators zhtw-wasm rajatim" in commands
    assert "access list packages" not in commands
    assert "publish" not in commands
    assert all(line.startswith(f"{tmp_path / 'secrets' / 'npm-cache'}|") for line in lines)


def test_npm_preflight_rejects_a_read_only_token(tmp_path: Path) -> None:
    result = run_preflight_shell(
        tmp_path,
        r"""
source "$ADAPTER" ignored /missing
require_common() { :; }
date() {
    case "$*" in
        *" -d "*) printf '2000000000\n' ;;
        *) printf '1900000000\n' ;;
    esac
}
npm() {
    case "$*" in
        *whoami*) printf 'rajatim\n' ;;
        *"token list"*)
            fingerprint="${NODE_AUTH_TOKEN:0:8}...${NODE_AUTH_TOKEN: -4}"
            printf '%s' '[{"token":"'
            printf '%s' "$fingerprint"
            printf '%s\n' '","expiry":"2099-01-01T00:00:00Z","bypass_2fa":true,' \
                '"revoked":null,"permissions":[{"name":"package","action":"read"}],' \
                '"scopes":[{"name":null,"type":"package"}]}]'
            ;;
        *) return 1 ;;
    esac
}
preflight_npm
""",
        {
            "NODE_AUTH_TOKEN": "npm_fixture_token_1234",
            "NPM_TOKEN_EXPIRES": "2099-01-01T00:00:00Z",
        },
    )

    assert result.returncode != 0
    assert "active package-write token with 2FA bypass" in result.stderr


def test_crates_and_nuget_preflights_use_nonpublishing_endpoints(tmp_path: Path) -> None:
    curl_log = tmp_path / "curl-log"
    result = run_preflight_shell(
        tmp_path,
        r"""
source "$ADAPTER" ignored /missing
require_common() { :; }
curl() {
    printf '%s\n' "$*" >> "$CURL_LOG"
    case "$*" in
        *crates.io/api/v1/crates/zhtw/owners*)
            printf '{"users":[{"id":405856,"login":"rajatim","kind":"user"}]}\n'
            ;;
        *"github_configs?user_id=405856"*|*"github_configs?crate=zhtw"*)
            printf '{"github_configs":[],"meta":{"total":0,"next_page":null}}\n'
            ;;
        *create-verification-key*) printf '{"Key":"ephemeral-verification-key"}\n' ;;
        *verifykey*) : ;;
        *) return 1 ;;
    esac
}
preflight_crates
preflight_nuget
""",
        {
            "CARGO_REGISTRY_TOKEN": "fixture",
            "NUGET_API_KEY": "fixture",
            "CURL_LOG": str(curl_log),
        },
    )

    assert result.returncode == 0, result.stderr
    arguments = curl_log.read_text(encoding="utf-8")
    assert "crates.io/api/v1/crates/zhtw/owners" in arguments
    assert "github_configs?user_id=405856" in arguments
    assert "github_configs?crate=zhtw" in arguments
    assert "crates.io/api/v1/me" not in arguments
    assert "create-verification-key/Zhtw" in arguments
    assert "verifykey/Zhtw" in arguments
    assert "--request PUT" not in arguments
    assert "--request DELETE" not in arguments
    assert "--form package=@" not in arguments


def test_crates_preflight_rejects_a_token_without_zhtw_scope(tmp_path: Path) -> None:
    result = run_preflight_shell(
        tmp_path,
        r"""
source "$ADAPTER" ignored /missing
require_common() { :; }
curl() {
    case "$*" in
        *crates.io/api/v1/crates/zhtw/owners*)
            printf '{"users":[{"id":405856,"login":"rajatim","kind":"user"}]}\n'
            ;;
        *"github_configs?user_id=405856"*)
            printf '{"github_configs":[],"meta":{"total":0,"next_page":null}}\n'
            ;;
        *"github_configs?crate=zhtw"*) return 22 ;;
        *) return 1 ;;
    esac
}
preflight_crates
""",
        {"CARGO_REGISTRY_TOKEN": "fixture"},
    )

    assert result.returncode != 0
    assert "scoped token authentication failed" in result.stderr


def test_maven_preflight_checks_auth_and_signing_without_upload(tmp_path: Path) -> None:
    curl_log = tmp_path / "curl-log"
    result = run_preflight_shell(
        tmp_path,
        r"""
source "$ADAPTER" ignored /missing
require_common() { :; }
gpg() { cat >/dev/null || true; }
sign_maven_file() { printf 'signature' > "$1.asc"; }
curl() { printf '%s\n' "$*" > "$CURL_LOG"; printf '404'; }
preflight_maven
""",
        {
            "CENTRAL_USERNAME": "fixture-user",
            "CENTRAL_PASSWORD": "fixture-password",
            "GPG_PRIVATE_KEY": "fixture-key",
            "GPG_PASSPHRASE": "fixture-passphrase",
            "CURL_LOG": str(curl_log),
        },
    )

    assert result.returncode == 0, result.stderr
    arguments = curl_log.read_text(encoding="utf-8")
    assert "/publisher/status" in arguments
    assert "/publisher/upload" not in arguments


def test_maven_retry_resumes_recorded_deployment_without_upload(tmp_path: Path) -> None:
    payload = tmp_path / "payload"
    payload.mkdir()
    curl_log = tmp_path / "curl-arguments"
    record = tmp_path / "maven-deployment.properties"
    deployment_id = "12345678-1234-1234-1234-123456789abc"
    environment = os.environ.copy()
    environment.update(
        {
            "ADAPTER": str(ROOT / "scripts/jenkins-release.sh"),
            "PAYLOAD": str(payload),
            "CURL_LOG": str(curl_log),
            "CENTRAL_USERNAME": "fixture-user",
            "CENTRAL_PASSWORD": "fixture-password",
            "MAVEN_DEPLOYMENT_ID": deployment_id,
            "MAVEN_DEPLOYMENT_RECORD": str(record),
            "WORKSPACE": str(tmp_path),
            "SOURCE_SHA": "a" * 40,
            "RELEASE_VERSION": "9.8.7",
        }
    )
    result = subprocess.run(
        [
            "bash",
            "-c",
            r"""
source "$ADAPTER" ignored "$PAYLOAD"
require_common() { :; }
ensure_git_release() { :; }
registry_exists() { return 1; }
wait_for_registry() { :; }
maven_artifacts_match() { :; }
curl() {
    printf '%s\n' "$*" >> "$CURL_LOG"
    printf '{"deploymentState":"PUBLISHED"}\n'
}
publish_maven
""",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        env=environment,
    )

    assert result.returncode == 0, result.stderr
    assert "Resuming Maven Central deployment" in result.stdout
    assert "/publisher/upload" not in curl_log.read_text(encoding="utf-8")
    assert f"MAVEN_DEPLOYMENT_ID={deployment_id}" in record.read_text(encoding="utf-8")


def write_nuget_fixture(path: Path, library: bytes, signed: bool) -> None:
    with zipfile.ZipFile(path, "w") as package:
        package.writestr("Zhtw.nuspec", b"<package />")
        package.writestr("lib/net8.0/Zhtw.dll", library)
        package.writestr("[Content_Types].xml", b"signed" if signed else b"unsigned")
        package.writestr("_rels/.rels", b"signed" if signed else b"unsigned")
        if signed:
            package.writestr(".signature.p7s", b"repository signature")


def run_nuget_comparison(expected: Path, public: Path) -> subprocess.CompletedProcess[str]:
    environment = os.environ.copy()
    environment.update(
        {
            "ADAPTER": str(ROOT / "scripts/jenkins-release.sh"),
            "EXPECTED": str(expected),
            "PUBLIC": str(public),
        }
    )
    return subprocess.run(
        [
            "bash",
            "-c",
            'source "$ADAPTER" ignored /missing; nuget_semantic_matches "$EXPECTED" "$PUBLIC"',
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        env=environment,
    )


def test_nuget_comparison_ignores_only_repository_signature_wrappers(tmp_path: Path) -> None:
    expected = tmp_path / "expected.nupkg"
    signed = tmp_path / "signed.nupkg"
    changed = tmp_path / "changed.nupkg"
    write_nuget_fixture(expected, b"exact library", signed=False)
    write_nuget_fixture(signed, b"exact library", signed=True)
    write_nuget_fixture(changed, b"different library", signed=True)

    assert run_nuget_comparison(expected, signed).returncode == 0
    assert run_nuget_comparison(expected, changed).returncode == 1


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
    promoted = (tmp_path / "CHANGELOG.md").read_text(encoding="utf-8")
    assert "## [9.8.7] - 2026-08-09" in promoted
    assert "[Unreleased]: https://github.com/rajatim/zhtw/compare/v9.8.7...HEAD" in promoted
    assert "[9.8.7]: https://github.com/rajatim/zhtw/compare/v1.0.0...v9.8.7" in promoted

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
    assert (tmp_path / "CHANGELOG.md").read_text(encoding="utf-8") == promoted


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
            sys.executable,
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
