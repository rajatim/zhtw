"""Review pending terms for approval."""

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from .import_terms import delete_pending, load_pending


@dataclass
class ReviewResult:
    """Result of a review session."""

    approved: int = 0
    rejected: int = 0
    skipped: int = 0
    terms: dict = field(default_factory=dict)


def get_builtin_terms_dir(source: str = "cn") -> Path:
    """Get the directory for built-in terms."""
    return Path(__file__).parent / "data" / "terms" / source


def approve_terms(
    terms: dict, target_source: str = "cn", target_file: str = "imported.json"
) -> Path:
    """Approve terms and add them to the main dictionary.

    Args:
        terms: Dict of source -> target terms to approve
        target_source: Target source directory (cn, hk)
        target_file: Target file name

    Returns:
        Path to the updated file
    """
    terms_dir = get_builtin_terms_dir(target_source)
    terms_dir.mkdir(parents=True, exist_ok=True)

    target_path = terms_dir / target_file

    # Load existing terms if file exists
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
        "description": "使用者核准的詞彙",
        "terms": existing,
    }

    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

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
    terms = data.get("terms", {})
    result = ReviewResult()

    if auto_approve:
        result.approved = len(terms)
        result.terms = terms
        return result

    if auto_reject:
        result.rejected = len(terms)
        return result

    approved_terms = {}

    for source, target in terms.items():
        if not interactive:
            # Non-interactive: approve all
            approved_terms[source] = target
            result.approved += 1
            continue

        # Interactive review
        print(f"\n📋 審核: \"{source}\" → \"{target}\"")

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
                return result
            else:
                print("   請輸入 A/R/S/Q")

    result.terms = approved_terms
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
        if delete_after:
            delete_pending(name)
        return None

    # Save approved terms
    path = approve_terms(result.terms, target_source)

    # Delete pending file
    if delete_after:
        delete_pending(name)

    return path
