"""Tests for permissioned GitHub issue preview and confirmed import."""
# zhtw:disable  # GitHub fixture 中的 input 必須保持簡體

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any

import pytest

from scripts.import_permissioned_user_report_issue import (
    IntakeError,
    append_confirmed,
    main,
    parse_issue,
    prepare_imports,
)
from scripts.validate_permissioned_user_reports import validate_collection

CONSENT = """- [x] 我是文字原作者或有權提供，內容不是從受保護的資料直接複製。
- [x] 我在可處分權利範圍內適用 [CC0 1.0 Universal](https://example.test)。
- [x] 我了解文字、GitHub 帳號、issue 與同意紀錄會公開。
- [x] 內容不含個資、帳號、客戶資料、密碼或未公開資料。
- [x] 我只提交 input，未提交 expected 或 converter output。"""


def collection() -> dict[str, Any]:
    return {
        "version": 1,
        "id": "permissioned-user-report-batch-001",
        "batch_number": 1,
        "created_date": "2026-07-23",
        "status": "collecting",
        "source_class": "permissioned",
        "target_count": 100,
        "input_only": True,
        "converter_output_used": False,
        "consent_policy_version": "permissioned-user-report-v1",
        "redaction_policy": "reject_and_resubmit_no_automatic_mutation",
        "cases": [],
    }


def issue(
    number: int = 101,
    inputs: str = "请检查当前设置。\n打开页面后应该显示提示。",
) -> dict[str, Any]:
    return {
        "number": number,
        "title": "[語料回報] 設定頁",
        "body": (
            f"### 簡體中文原句\n\n{inputs}\n\n"
            "### 非敏感情境說明\n\n軟體設定頁\n\n"
            f"### 權利、公開與資料安全確認\n\n{CONSENT}"
        ),
        "created_at": "2026-07-23T08:00:00Z",
        "html_url": f"https://github.com/rajatim/zhtw/issues/{number}",
    }


def test_parse_issue_extracts_only_inputs_and_provenance() -> None:
    parsed = parse_issue(issue(), repository="rajatim/zhtw")

    assert parsed["inputs"] == ["请检查当前设置。", "打开页面后应该显示提示。"]
    assert parsed["issue_url"].endswith("/101")
    assert len(parsed["issue_body_sha256"]) == 64
    assert "軟體設定頁" not in json.dumps(parsed, ensure_ascii=False)


def test_unchecked_consent_is_rejected() -> None:
    payload = issue()
    payload["body"] = payload["body"].replace("- [x] 我只提交 input", "- [ ] 我只提交 input")

    with pytest.raises(IntakeError, match="consent item is not checked"):
        parse_issue(payload, repository="rajatim/zhtw")


def test_unexpected_expected_section_is_rejected() -> None:
    payload = issue()
    payload["body"] += "\n\n### expected\n\n請檢查目前設定。"

    with pytest.raises(IntakeError, match="unexpected issue sections: expected"):
        parse_issue(payload, repository="rajatim/zhtw")


@pytest.mark.parametrize(
    "text",
    [
        "联络邮箱：alice@example.com",
        "电话：0912-345-678",
        "api_key=abcd1234",
    ],
)
def test_sensitive_input_rejects_the_entire_issue(text: str) -> None:
    with pytest.raises(IntakeError, match="contains sensitive patterns"):
        parse_issue(issue(inputs=f"普通句子。\n{text}"), repository="rajatim/zhtw")


def test_duplicate_input_across_issues_is_rejected() -> None:
    with pytest.raises(IntakeError, match="duplicate normalized input proposed"):
        prepare_imports(
            collection(),
            [issue(101, "重复句子。"), issue(102, "  重复句子。 ")],
            repository="rajatim/zhtw",
        )


def test_confirmed_import_adds_auditable_review_metadata() -> None:
    source = collection()
    proposals = prepare_imports(source, [issue()], repository="rajatim/zhtw")

    updated = append_confirmed(
        source,
        proposals,
        maintainer="tim",
        reviewed_at="2026-07-23T17:00:00+08:00",
    )

    assert source["cases"] == []
    assert [case["id"] for case in updated["cases"]] == ["report-0001", "report-0002"]
    assert updated["cases"][0]["intake_review"] == {
        "reviewer": "tim",
        "reviewed_at": "2026-07-23T17:00:00+08:00",
        "decision": "accepted",
        "issue_body_sha256": proposals[0]["issue_body_sha256"],
    }
    assert validate_collection(updated) == []


def test_review_time_requires_timezone() -> None:
    proposals = prepare_imports(collection(), [issue()], repository="rajatim/zhtw")

    with pytest.raises(IntakeError, match="include a UTC offset"):
        append_confirmed(
            collection(),
            proposals,
            maintainer="tim",
            reviewed_at="2026-07-23T17:00:00",
        )


def test_cli_defaults_to_preview_without_modifying_collection(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    collection_path = tmp_path / "collection.json"
    issue_path = tmp_path / "issue.json"
    collection_path.write_text(json.dumps(collection(), ensure_ascii=False), encoding="utf-8")
    issue_path.write_text(json.dumps(issue(), ensure_ascii=False), encoding="utf-8")
    before = collection_path.read_bytes()
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "import_permissioned_user_report_issue.py",
            "--collection",
            str(collection_path),
            "--issue-json",
            str(issue_path),
        ],
    )

    assert main() == 0
    assert collection_path.read_bytes() == before
    assert "proposed=2" in capsys.readouterr().out


def test_cli_write_is_atomic_after_explicit_confirmation(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    collection_path = tmp_path / "collection.json"
    issue_path = tmp_path / "issue.json"
    collection_path.write_text(json.dumps(collection(), ensure_ascii=False), encoding="utf-8")
    issue_path.write_text(json.dumps(issue(), ensure_ascii=False), encoding="utf-8")
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "import_permissioned_user_report_issue.py",
            "--collection",
            str(collection_path),
            "--issue-json",
            str(issue_path),
            "--write",
            "--maintainer",
            "tim",
            "--reviewed-at",
            "2026-07-23T17:00:00+08:00",
        ],
    )

    assert main() == 0
    written = json.loads(collection_path.read_text(encoding="utf-8"))
    assert len(written["cases"]) == 2
    assert not collection_path.with_suffix(".json.tmp").exists()


def test_failed_write_leaves_collection_unchanged(tmp_path: Path) -> None:
    source = collection()
    proposals = prepare_imports(source, [issue()], repository="rajatim/zhtw")
    changed = copy.deepcopy(proposals)
    changed[0]["input"] = "账号：A123456"

    with pytest.raises(IntakeError, match="updated collection is invalid"):
        append_confirmed(
            source,
            changed,
            maintainer="tim",
            reviewed_at="2026-07-23T17:00:00+08:00",
        )
    assert source["cases"] == []
