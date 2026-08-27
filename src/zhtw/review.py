"""Review pending terms for approval."""

import json
from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Iterable, Optional

from .import_terms import (
    delete_pending,
    extract_pending_records,
    extract_pending_terms,
    load_pending,
)
from .rules import ReviewStatus, RuleRecord, validate_rule_catalog


@dataclass
class ReviewResult:
    """Result of a review session."""

    approved: int = 0
    rejected: int = 0
    skipped: int = 0
    terms: dict = field(default_factory=dict)
    records: dict[str, RuleRecord] = field(default_factory=dict)


def get_builtin_terms_dir(source: str = "cn") -> Path:
    """Get the directory for built-in terms."""
    return Path(__file__).parent / "data" / "terms" / source


def approve_terms(
    terms: dict,
    target_source: str = "cn",
    target_file: str = "imported.json",
    *,
    records: Iterable[RuleRecord] | None = None,
) -> Path:
    """Approve terms and add them to the main dictionary.

    Args:
        terms: Dict of source -> target terms to approve
        target_source: Target source directory (cn, hk)
        target_file: Target file name

    Returns:
        Path to the updated file
    """
    approved_records = tuple(records or ())
    if approved_records and target_file == "imported.json":
        target_file = "imported-v2.json"

    terms_dir = get_builtin_terms_dir(target_source)
    terms_dir.mkdir(parents=True, exist_ok=True)

    target_path = terms_dir / target_file

    if approved_records:
        record_terms = {record.source: record.target for record in approved_records}
        if len(record_terms) != len(approved_records) or record_terms != terms:
            raise ValueError("核准詞彙與 schema v2 規則不一致")
        if any(record.source_locale.value != target_source for record in approved_records):
            raise ValueError("schema v2 規則的 source_locale 與目標詞庫不一致")

        existing_records: tuple[RuleRecord, ...] = ()
        if target_path.exists():
            with open(target_path, encoding="utf-8") as f:
                data = json.load(f)
            if data.get("schema_version") != 2:
                raise ValueError("不可把 schema v2 規則合併進 legacy 詞庫檔")
            existing_records = tuple(RuleRecord.from_mapping(item) for item in data["rules"])

        promoted = tuple(
            replace(record, review_status=ReviewStatus.APPROVED) for record in approved_records
        )
        merged = validate_rule_catalog((*existing_records, *promoted))
        data = {"schema_version": 2, "rules": [record.to_mapping() for record in merged]}
        with open(target_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write("\n")
        return target_path

    # Load existing legacy terms if file exists.
    existing = {}
    if target_path.exists():
        try:
            with open(target_path, encoding="utf-8") as f:
                data = json.load(f)
                existing = data.get("terms", {})
        except (json.JSONDecodeError, IOError):
            pass

    # Merge terms
    existing.update(terms)

    # Save
    data = {
        "version": "1.0",
        "description": "使用者覈准的詞彙",
        "terms": existing,
    }

    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    return target_path


def review_pending_file(
    name: str,
    llm_client=None,
    interactive: bool = True,
    auto_approve: bool = False,
    auto_reject: bool = False,
) -> ReviewResult:
    """Review a pending file.

    Args:
        name: Name of the pending file
        llm_client: Optional LLM client for validation
        interactive: Whether to prompt for each term
        auto_approve: Approve all without prompting
        auto_reject: Reject all without prompting

    Returns:
        ReviewResult with statistics
    """
    data = load_pending(name)
    terms = extract_pending_terms(data)
    pending_records = {record.source: record for record in extract_pending_records(data)}
    result = ReviewResult()

    if auto_approve:
        result.approved = len(terms)
        result.terms = terms
        result.records = pending_records
        return result

    if auto_reject:
        result.rejected = len(terms)
        return result

    approved_terms = {}
    approved_records = {}

    for source, target in terms.items():
        if not interactive:
            # Non-interactive: approve all
            approved_terms[source] = target
            if source in pending_records:
                approved_records[source] = pending_records[source]
            result.approved += 1
            continue

        # Interactive review
        print(f'\n📋 審核: "{source}" → "{target}"')

        # Get LLM validation if available
        if llm_client:
            try:
                validation = llm_client.validate_term(source, target)
                if validation["correct"]:
                    print("   🤖 LLM 判斷: ✅ 正確")
                else:
                    print("   🤖 LLM 判斷: ❌ 可能有誤")
                if validation["reason"]:
                    print(f"   理由: {validation['reason']}")
                if validation["suggestion"]:
                    print(f"   建議: {validation['suggestion']}")
            except Exception as e:
                print(f"   ⚠️ LLM 驗證失敗: {e}")

        # Prompt for action
        while True:
            action = input("\n   [A]pprove / [R]eject / [S]kip / [Q]uit? ").strip().lower()

            if action in ("a", "approve"):
                approved_terms[source] = target
                if source in pending_records:
                    approved_records[source] = pending_records[source]
                result.approved += 1
                break
            elif action in ("r", "reject"):
                result.rejected += 1
                break
            elif action in ("s", "skip"):
                result.skipped += 1
                break
            elif action in ("q", "quit"):
                result.terms = approved_terms
                result.records = approved_records
                return result
            else:
                print("   請輸入 A/R/S/Q")

    result.terms = approved_terms
    result.records = approved_records
    return result


def finalize_review(
    name: str,
    result: ReviewResult,
    target_source: str = "cn",
    delete_after: bool = True,
) -> Optional[Path]:
    """Finalize a review by saving approved terms.

    Args:
        name: Name of the pending file
        result: Review result
        target_source: Target source directory
        delete_after: Whether to delete the pending file after

    Returns:
        Path to the updated terms file, or None if no terms approved
    """
    if not result.terms:
        # 有 skip 的詞 → 保留 pending 檔（使用者尚未做最終決定）
        if delete_after and result.skipped == 0:
            delete_pending(name)
        return None

    # Save approved terms
    path = approve_terms(
        result.terms,
        target_source,
        records=result.records.values() if result.records else None,
    )

    # 只在沒有 skipped 詞時刪除（全部已審核完畢）
    if delete_after and result.skipped == 0:
        delete_pending(name)

    return path
