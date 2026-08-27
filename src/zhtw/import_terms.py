"""Import terms from external sources."""

import hashlib
import json
import re
import string
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, List, Optional, Tuple

from .rules import (
    ReviewStatus,
    RuleCatalogError,
    RuleClass,
    RuleRecord,
    SourceLocale,
    TrustLevel,
)
from .unicode_ranges import contains_han, is_han_character


@dataclass
class ImportResult:
    """Result of an import operation."""

    total: int = 0
    valid: int = 0
    invalid: int = 0
    duplicates: int = 0
    conflicts: int = 0
    errors: list = field(default_factory=list)
    terms: dict = field(default_factory=dict)


class ImportError(Exception):
    """Error during import."""

    pass


def _list_to_dict(data: list) -> Tuple[dict, List[str], int]:
    """Convert list format to dict, detecting duplicates.

    Returns:
        Tuple of (terms_dict, duplicate_sources, total_items)
    """
    result = {}
    duplicates = []
    total = 0
    for item in data:
        if not isinstance(item, dict):
            continue
        if "source" not in item or "target" not in item:
            continue
        total += 1
        src = item["source"]
        if src in result:
            duplicates.append(src)
        result[src] = item["target"]
    return result, duplicates, total


def _extract_terms(data: Any) -> Tuple[dict, List[str], int]:
    """Extract terms plus metadata from supported payload formats."""
    if isinstance(data, dict):
        terms = data.get("terms", data)
        if not isinstance(terms, dict):
            raise ImportError(f"無法識別的格式: {type(terms)}")
        return terms, [], len(terms)

    if isinstance(data, list):
        return _list_to_dict(data)

    raise ImportError(f"無法識別的格式: {type(data)}")


_simplified_chars_cache: Optional[set] = None
_TECHNICAL_ASCII = frozenset(string.ascii_letters + string.digits + " .+#-_/:@")


def get_pending_dir() -> Path:
    """Get the pending terms directory."""
    # Get the data directory relative to this file
    data_dir = Path(__file__).parent / "data" / "terms" / "pending"
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir


def is_simplified_chinese(char: str) -> bool:
    """Check if a character is likely simplified Chinese.

    Uses the charmap data (safe_chars.json) as the source of truth.
    A character is simplified if it appears as a key in the charmap
    (meaning it has a different traditional form).
    """
    global _simplified_chars_cache
    if _simplified_chars_cache is None:
        charmap_path = Path(__file__).parent / "data" / "charmap" / "safe_chars.json"
        try:
            data = json.loads(charmap_path.read_text("utf-8"))
            _simplified_chars_cache = set(data.get("chars", {}).keys())
        except Exception:
            _simplified_chars_cache = set()
    return char in _simplified_chars_cache


def validate_term(source: str, target: str, existing_terms: dict) -> tuple[bool, Optional[str]]:
    """Validate a term pair.

    Returns:
        (is_valid, error_message)
    """
    if not isinstance(source, str) or not isinstance(target, str) or not source or not target:
        return False, "來源或目標為空"

    if source == target:
        return False, "來源與目標相同"

    if len(source) > 20 or len(target) > 20:
        return False, "詞彙過長（超過 20 字元）"

    if source != source.strip() or target != target.strip():
        return False, "來源或目標含前後空白"

    if any(ord(character) < 0x20 or ord(character) == 0x7F for character in source + target):
        return False, "來源或目標含控制字元或換行"

    if not contains_han(source):
        return False, "來源缺少中文字元（純非中文）"
    if not contains_han(target):
        return False, "目標缺少中文字元（純非中文）"

    for label, value in (("來源", source), ("目標", target)):
        if any(
            not is_han_character(character) and character not in _TECHNICAL_ASCII
            for character in value
        ):
            return False, f"{label}包含不支援的非中文字元"

    source_non_han = "".join(character for character in source if not is_han_character(character))
    target_non_han = "".join(character for character in target if not is_han_character(character))
    if source_non_han != target_non_han:
        return False, "來源與目標的非中文字元序列不同"

    # Check for conflicts with existing terms
    if source in existing_terms:
        if existing_terms[source] != target:
            return False, f"與現有詞庫衝突：{source} → {existing_terms[source]}"

    return True, None


def load_from_url(url: str) -> dict:
    """Load terms from a URL.

    Returns:
        Dict of source -> target terms
    """
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "zhtw/2.0"},
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            content = resp.read().decode("utf-8")
            data = json.loads(content)
            terms, _duplicates, _total = _extract_terms(data)
            return terms

    except urllib.error.URLError as e:
        raise ImportError(f"無法載入 URL: {e.reason}")
    except json.JSONDecodeError as e:
        raise ImportError(f"JSON 解析錯誤: {e}")


def load_from_file(path: Path) -> dict:
    """Load terms from a local file.

    Returns:
        Dict of source -> target terms
    """
    if not path.exists():
        raise ImportError(f"檔案不存在: {path}")

    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
            terms, _duplicates, _total = _extract_terms(data)
            return terms

    except json.JSONDecodeError as e:
        raise ImportError(f"JSON 解析錯誤: {e}")


def import_terms(
    source: str,
    existing_terms: Optional[dict] = None,
    validate: bool = True,
    allow_insecure: bool = False,
) -> ImportResult:
    """Import terms from a URL or file path.

    Args:
        source: URL or file path
        existing_terms: Existing terms dict for conflict detection
        validate: Whether to validate terms
        allow_insecure: Whether to allow insecure HTTP connections

    Returns:
        ImportResult with import statistics and validated terms
    """
    result = ImportResult()
    existing = existing_terms or {}

    # Load raw data
    if source.startswith(("http://", "https://")):
        if source.startswith("http://") and not allow_insecure:
            raise ImportError("不安全的 HTTP 連線，請使用 HTTPS 或加上 --allow-insecure")
        req = urllib.request.Request(
            source,
            headers={"User-Agent": "zhtw/2.0"},
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                content = resp.read().decode("utf-8")
                data = json.loads(content)
        except urllib.error.URLError as e:
            raise ImportError(f"無法載入 URL: {e.reason}")
        except json.JSONDecodeError as e:
            raise ImportError(f"JSON 解析錯誤: {e}")
    else:
        path = Path(source)
        if not path.exists():
            raise ImportError(f"檔案不存在: {path}")
        try:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            raise ImportError(f"JSON 解析錯誤: {e}")

    raw_terms, duplicate_sources, total_terms = _extract_terms(data)
    duplicate_source_set = set(duplicate_sources)

    result.total = total_terms
    result.duplicates = len(duplicate_sources)
    result.errors.extend(f"重複: {src}" for src in duplicate_sources)

    # Validate each term
    for src, tgt in raw_terms.items():
        if src in duplicate_source_set:
            result.invalid += 1
            continue
        if validate:
            is_valid, error = validate_term(src, tgt, existing)
            if not is_valid:
                result.invalid += 1
                if "衝突" in error:
                    result.conflicts += 1
                result.errors.append(f"{src} → {tgt}: {error}")
                continue

        result.valid += 1
        result.terms[src] = tgt

    return result


def _candidate_rule_id(source_locale: SourceLocale, source: str, target: str) -> str:
    identity = json.dumps(
        {
            "rule_class": RuleClass.CUSTOM.value,
            "source": source,
            "source_locale": source_locale.value,
            "target": target,
        },
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return f"candidate:{source_locale.value}:custom:{hashlib.sha256(identity).hexdigest()[:24]}"


def save_to_pending(
    terms: dict,
    name: str,
    *,
    evidence_source: str | None = None,
    source_locale: str = "cn",
) -> Path:
    """Save terms to pending directory for review.

    Args:
        terms: Dict of source -> target terms
        name: Name for the pending file

    Returns:
        Path to the saved file
    """
    # Clean up name
    clean_name = re.sub(r"[^\w\-]", "_", name)
    if not clean_name.endswith(".json"):
        clean_name += ".json"

    pending_dir = get_pending_dir()
    path = pending_dir / clean_name
    locale = SourceLocale(source_locale)
    provenance = evidence_source or name
    packet_context = f"import-packet:{Path(clean_name).stem}"
    records = [
        RuleRecord(
            id=_candidate_rule_id(locale, source, target),
            source_locale=locale,
            source=source,
            target=target,
            rule_class=RuleClass.CUSTOM,
            domain="general",
            trust_level=TrustLevel.IMPORTED,
            priority=0,
            context=(packet_context,),
            evidence_source=provenance,
            review_status=ReviewStatus.PENDING,
        )
        for source, target in sorted(terms.items())
    ]
    data = {"schema_version": 2, "rules": [record.to_mapping() for record in records]}

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    return path


def extract_pending_records(data: Any) -> tuple[RuleRecord, ...]:
    """Parse a schema-v2 pending packet and reject malformed review state."""

    if not isinstance(data, dict) or data.get("schema_version") != 2:
        return ()
    if set(data) != {"schema_version", "rules"} or not isinstance(data["rules"], list):
        raise ImportError("待審核 schema v2 格式不正確")
    try:
        records = tuple(RuleRecord.from_mapping(item) for item in data["rules"])
    except RuleCatalogError as exc:
        raise ImportError(f"待審核規則格式不正確: {exc}") from exc
    if any(record.review_status is not ReviewStatus.PENDING for record in records):
        raise ImportError("待審核規則的 review_status 必須是 pending")
    if len({record.id for record in records}) != len(records):
        raise ImportError("待審核規則含重複 ID")
    if len({record.source for record in records}) != len(records):
        raise ImportError("待審核規則含重複來源")
    return records


def extract_pending_terms(data: Any) -> dict[str, str]:
    """Return terms from schema-v2 packets or legacy pending files."""

    records = extract_pending_records(data)
    if records:
        return {record.source: record.target for record in records}
    if isinstance(data, dict) and data.get("schema_version") == 2:
        return {}
    terms = data.get("terms", {}) if isinstance(data, dict) else {}
    if not isinstance(terms, dict):
        raise ImportError("待審核詞彙格式不正確")
    return terms


def list_pending() -> list[dict]:
    """List all pending term files.

    Returns:
        List of dicts with file info
    """
    pending_dir = get_pending_dir()
    results = []

    for path in sorted(pending_dir.glob("*.json")):
        try:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
                records = extract_pending_records(data)
                terms = extract_pending_terms(data)
                results.append(
                    {
                        "path": path,
                        "name": path.name,
                        "terms_count": len(terms),
                        "description": data.get(
                            "description",
                            records[0].evidence_source if records else "",
                        ),
                        "status": "pending" if records else data.get("status", "pending"),
                    }
                )
        except (json.JSONDecodeError, IOError, ImportError):
            continue

    return results


def load_pending(name: str) -> dict:
    """Load a pending term file.

    Args:
        name: Name of the pending file

    Returns:
        Dict with file data including terms
    """
    pending_dir = get_pending_dir()

    if not name.endswith(".json"):
        name += ".json"

    path = pending_dir / name

    if not path.exists():
        raise ImportError(f"待審核檔案不存在: {name}")

    with open(path, encoding="utf-8") as f:
        return json.load(f)


def delete_pending(name: str) -> None:
    """Delete a pending term file.

    Args:
        name: Name of the pending file
    """
    pending_dir = get_pending_dir()

    if not name.endswith(".json"):
        name += ".json"

    path = pending_dir / name

    if path.exists():
        path.unlink()
