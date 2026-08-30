"""Fail-closed checks for public documentation hosting and Jenkins adapters."""

import os
import stat
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_docs_scripts_are_executable_and_reject_non_jenkins_use() -> None:
    for path in ("scripts/jenkins-docs-build.sh", "scripts/jenkins-docs-publish.sh"):
        script = ROOT / path
        assert script.stat().st_mode & stat.S_IXUSR

    environment = os.environ.copy()
    for name in (
        "CI_PROVIDER",
        "JOB_NAME",
        "JENKINS_URL",
        "WORKSPACE",
        "AWS_ACCESS_KEY_ID",
        "AWS_SECRET_ACCESS_KEY",
    ):
        environment.pop(name, None)
    result = subprocess.run(
        [str(ROOT / "scripts/jenkins-docs-publish.sh"), "inspect"],
        cwd=ROOT,
        env=environment,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 64
    assert "Docs publication requires Jenkins" in result.stderr


def test_cloudformation_keeps_s3_private_and_hub_out_of_scope() -> None:
    template = read("deploy/docs/cloudformation.yml")

    for setting in (
        "BlockPublicAcls: true",
        "BlockPublicPolicy: true",
        "IgnorePublicAcls: true",
        "RestrictPublicBuckets: true",
        "OriginAccessControl",
        "cloudfront.amazonaws.com",
        "ViewerProtocolPolicy: redirect-to-https",
        "MinimumProtocolVersion: TLSv1.2_2021",
        "CustomErrorResponses:",
        "ResponseCode: 404",
        "DeletionPolicy: Retain",
        "UpdateReplacePolicy: Retain",
    ):
        assert setting in template
    assert "AWS::IAM::AccessKey" not in template
    assert "S3OriginConfig" in template
    assert "WebsiteConfiguration" not in template
    assert "13.115.159.51" not in template
    assert "rajatim.wiki" not in template


def test_docs_build_is_exact_main_and_archives_bilingual_site() -> None:
    script = read("scripts/jenkins-docs-build.sh")

    assert "JOB_NAME must be zhtw/docs-build" in script
    assert 'SOURCE_BRANCH:-}" = main' in script
    assert "make docs-build" in script
    assert "site/index.html" in script
    assert "site/en/index.html" in script
    assert "deployment.json" in script
    assert "PROJECT_TREE_SHA mismatch" in script
    assert "SHA256SUMS" in script


def test_docs_publish_uses_immutable_release_and_recorded_rollback() -> None:
    script = read("scripts/jenkins-docs-publish.sh")

    assert "JOB_NAME must be zhtw/docs-publish" in script
    assert "AWS_PROFILE is forbidden" in script
    assert "releases/$SOURCE_SHA/" in script
    assert "deploy-state/current.properties" in script
    assert "previous.properties" in script
    assert "mutation-started" in script
    assert "rollback-succeeded" in script
    assert "cloudfront create-invalidation" in script
    assert "RELEASE_SHA256SUMS" in script
    assert "Remote deployment.json source SHA mismatch" in script
    assert "__zhtw_missing_page__" in script
    assert "strict-transport-security" in script
    assert "op " not in script
    assert "github workflow" not in script.lower()


def test_rules_keep_package_and_docs_publication_separate() -> None:
    agents = read("AGENTS.md")
    releasing = read(".claude/rules/releasing.md")

    for job in ("zhtw/docs-build", "zhtw/docs-publish"):
        assert job in agents
        assert job in releasing
    assert "純文件發布不變更 mono-version" in releasing
    assert "不得用 GitHub Actions、公開 S3 bucket" in agents
