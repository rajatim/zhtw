"""
Dictionary module for loading and managing terminology mappings.

Supports:
- CN (Simplified Chinese) → TW (Taiwan Traditional)
- HK (Hong Kong Traditional) → TW (Taiwan Traditional)
"""

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

from .rules import (
    RULE_DOMAINS,
    ReviewStatus,
    RuleCatalogError,
    RuleClass,
    RuleRecord,
    SourceLocale,
    TrustLevel,
    legacy_rule_record,
    validate_rule_catalog,
)

# Built-in terms directory
DATA_DIR = Path(__file__).parent / "data" / "terms"

# Bulk-imported dictionaries (machine-generated, lower trust) load FIRST so
# that every hand-curated file overrides them on key collisions. Without an
# explicit order, alphabetical glob order would let opencc.json (28k imported
# terms) silently override curated entries.
BULK_FILES = frozenset({"opencc.json"})
TARGET_GUARD_FILES = frozenset({"target-guards.json"})

# Reserved top-level keys that must NOT be loaded as term mappings
# when a JSON file uses the legacy flat format (no "terms" wrapper).
_METADATA_KEYS = frozenset(
    {
        "version",
        "description",
        "source",
        "status",
        "category",
        "license",
        "schema_version",
    }
)

_RULE_CLASS_PRIORITY = {
    RuleClass.BULK: 100,
    RuleClass.GENERATED_GUARD: 200,
    RuleClass.CURATED: 300,
    RuleClass.CUSTOM: 400,
}

_RULE_CLASS_TRUST = {
    RuleClass.BULK: TrustLevel.IMPORTED,
    RuleClass.GENERATED_GUARD: TrustLevel.GENERATED,
    RuleClass.CURATED: TrustLevel.CURATED,
    RuleClass.CUSTOM: TrustLevel.CUSTOM,
}


@dataclass(frozen=True, slots=True)
class DictionaryLoadResult:
    """Effective runtime terms plus the complete descriptive rule catalog."""

    terms: Dict[str, str]
    catalog: tuple[RuleRecord, ...]


def _rule_class_for_file(path: Path) -> RuleClass:
    if path.name in BULK_FILES:
        return RuleClass.BULK
    if path.name in TARGET_GUARD_FILES:
        return RuleClass.GENERATED_GUARD
    return RuleClass.CURATED


def _domain_for_file(path: Path) -> str:
    return path.stem if path.stem in RULE_DOMAINS else "general"


def _evidence_source(path: Path) -> str:
    package_dir = Path(__file__).resolve().parent
    try:
        return path.resolve().relative_to(package_dir).as_posix()
    except ValueError:
        return path.name


def _legacy_terms(data: dict[str, Any]) -> dict[str, Any]:
    if "terms" in data:
        terms = data["terms"]
        if not isinstance(terms, dict):
            raise RuleCatalogError("legacy terms must be an object")
        return terms
    return {key: value for key, value in data.items() if key not in _METADATA_KEYS}


def _iter_legacy_entries(
    data: dict[str, Any],
    path: Path,
) -> list[tuple[str, str, str]]:
    entries: list[tuple[str, str, str]] = []
    default_domain = _domain_for_file(path)
    for source, value in _legacy_terms(data).items():
        if not isinstance(source, str) or source.startswith("_"):
            continue

        domain = default_domain
        if isinstance(value, dict):
            if "target" not in value:
                continue
            target = value["target"]
            candidate_domain = value.get("category")
            if candidate_domain in RULE_DOMAINS:
                domain = candidate_domain
        else:
            target = value

        if not isinstance(target, str) or not target:
            raise RuleCatalogError(f"legacy target for {source!r} must be a non-empty string")
        entries.append((source, target, domain))
    return entries


def _load_legacy_data(
    data: dict[str, Any],
    *,
    path: Path,
    source_locale: SourceLocale,
    rule_class: RuleClass,
) -> DictionaryLoadResult:
    terms: Dict[str, str] = {}
    records: list[RuleRecord] = []
    evidence_source = _evidence_source(path)

    for source, target, domain in _iter_legacy_entries(data, path):
        terms[source] = target
        records.append(
            legacy_rule_record(
                source_locale=source_locale,
                source=source,
                target=target,
                rule_class=rule_class,
                domain=domain,
                trust_level=_RULE_CLASS_TRUST[rule_class],
                priority=_RULE_CLASS_PRIORITY[rule_class],
                evidence_source=evidence_source,
            )
        )

    return DictionaryLoadResult(terms=terms, catalog=validate_rule_catalog(records))


def _read_dictionary_file(path: Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict):
        raise RuleCatalogError("dictionary file must contain an object")
    return data


def _dictionary_schema_version(data: dict[str, Any]) -> int | None:
    value = data.get("schema_version")
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int):
        raise RuleCatalogError(f"unsupported dictionary schema_version: {value!r}")
    return value


def _load_v2_data(
    data: dict[str, Any],
    *,
    expected_source: SourceLocale | None,
    expected_rule_class: RuleClass | None,
    allowed_sources: set[SourceLocale] | None,
) -> DictionaryLoadResult:
    unknown = set(data) - {"schema_version", "rules"}
    if unknown:
        raise RuleCatalogError(f"unknown schema-v2 fields: {', '.join(sorted(unknown))}")
    raw_records = data.get("rules")
    if not isinstance(raw_records, list):
        raise RuleCatalogError("schema-v2 rules must be an array")

    parsed = [RuleRecord.from_mapping(value) for value in raw_records]
    records = validate_rule_catalog(parsed)
    for record in records:
        if expected_source is not None and record.source_locale is not expected_source:
            raise RuleCatalogError(
                f"rule {record.id!r} source_locale does not match its dictionary directory"
            )
        if expected_rule_class is not None and record.rule_class is not expected_rule_class:
            raise RuleCatalogError(
                f"rule {record.id!r} rule_class does not match its dictionary file"
            )

    if allowed_sources is not None:
        records = tuple(record for record in records if record.source_locale in allowed_sources)

    terms = {
        record.source: record.target
        for record in records
        if record.review_status is ReviewStatus.APPROVED
    }
    return DictionaryLoadResult(terms=terms, catalog=records)


def load_rule_file(
    path: Path,
    *,
    source_locale: SourceLocale | str = SourceLocale.CN,
    rule_class: RuleClass | str = RuleClass.CUSTOM,
    allowed_sources: Optional[List[str]] = None,
) -> DictionaryLoadResult:
    """Load a legacy or schema-v2 rule file without changing runtime precedence."""

    if not path.exists():
        return DictionaryLoadResult(terms={}, catalog=())

    data = _read_dictionary_file(path)

    locale = SourceLocale(source_locale)
    kind = RuleClass(rule_class)
    schema_version = _dictionary_schema_version(data)
    allowed = (
        None if allowed_sources is None else {SourceLocale(value) for value in allowed_sources}
    )
    if schema_version is None or schema_version == 1:
        result = _load_legacy_data(
            data,
            path=path,
            source_locale=locale,
            rule_class=kind,
        )
        # Legacy custom files never declared a locale and historically applied
        # for every selected source. Preserve that behavior until the file is
        # explicitly migrated to schema v2.
        if kind is RuleClass.CUSTOM or allowed is None or locale in allowed:
            return result
        return DictionaryLoadResult(terms={}, catalog=())
    if schema_version == 2:
        return _load_v2_data(
            data,
            expected_source=None if kind is RuleClass.CUSTOM else locale,
            expected_rule_class=kind,
            allowed_sources=allowed,
        )
    raise RuleCatalogError(f"unsupported dictionary schema_version: {schema_version!r}")


def _load_effective_rule_file(
    path: Path,
    *,
    source_locale: SourceLocale,
    rule_class: RuleClass,
    allowed_sources: Optional[List[str]] = None,
) -> Dict[str, str]:
    """Load only runtime terms, avoiding catalog allocation on the hot path."""

    if not path.exists():
        return {}
    data = _read_dictionary_file(path)
    schema_version = _dictionary_schema_version(data)
    if schema_version is None or schema_version == 1:
        return {source: target for source, target, _domain in _iter_legacy_entries(data, path)}
    if schema_version == 2:
        allowed = (
            None if allowed_sources is None else {SourceLocale(value) for value in allowed_sources}
        )
        return _load_v2_data(
            data,
            expected_source=None if rule_class is RuleClass.CUSTOM else source_locale,
            expected_rule_class=rule_class,
            allowed_sources=allowed,
        ).terms
    raise RuleCatalogError(f"unsupported dictionary schema_version: {schema_version!r}")


def load_json_file(path: Path) -> Dict[str, str]:
    """Load effective terms from a legacy or schema-v2 custom file."""

    return _load_effective_rule_file(
        path,
        source_locale=SourceLocale.CN,
        rule_class=RuleClass.CUSTOM,
    )


def iter_directory_files(directory: Path) -> List[Path]:
    """List JSON files in precedence order: bulk imports first, curated last.

    後載者覆蓋先載者，因此 bulk 匯入檔（BULK_FILES）排最前、
    手工策展檔按字母序排後 —— key 碰撞時手工詞條必定勝出。
    """
    files = sorted(directory.glob("*.json"))
    return (
        [f for f in files if f.name in BULK_FILES]
        + [f for f in files if f.name in TARGET_GUARD_FILES]
        + [f for f in files if f.name not in BULK_FILES and f.name not in TARGET_GUARD_FILES]
    )


def load_directory(directory: Path) -> Dict[str, str]:
    """Load all JSON files from a directory and merge them."""
    if not directory.exists():
        return {}
    source_locale = SourceLocale(directory.name)
    merged: Dict[str, str] = {}
    for json_file in iter_directory_files(directory):
        merged.update(
            _load_effective_rule_file(
                json_file,
                source_locale=source_locale,
                rule_class=_rule_class_for_file(json_file),
            )
        )
    return merged


def load_directory_catalog(
    directory: Path,
    source_locale: SourceLocale | str,
) -> DictionaryLoadResult:
    """Load one locale directory and retain every descriptive record."""

    merged: Dict[str, str] = {}
    records: list[RuleRecord] = []

    if not directory.exists():
        return DictionaryLoadResult(terms=merged, catalog=())

    for json_file in iter_directory_files(directory):
        result = load_rule_file(
            json_file,
            source_locale=source_locale,
            rule_class=_rule_class_for_file(json_file),
        )
        merged.update(result.terms)
        records.extend(result.catalog)

    return DictionaryLoadResult(terms=merged, catalog=validate_rule_catalog(records))


def load_builtin(sources: Optional[List[str]] = None) -> Dict[str, str]:
    """
    Load built-in dictionaries.

    Args:
        sources: List of sources to load. Options: "cn", "hk", or None for all.

    Returns:
        Merged dictionary of all terms.
    """
    selected_sources = ["cn", "hk"] if sources is None else sources
    merged: Dict[str, str] = {}
    for source in selected_sources:
        merged.update(load_directory(DATA_DIR / source))
    return merged


def load_builtin_catalog(sources: Optional[List[str]] = None) -> DictionaryLoadResult:
    """Load built-in effective terms and the complete v1/v2 catalog."""

    if sources is None:
        sources = ["cn", "hk"]

    merged: Dict[str, str] = {}
    records: list[RuleRecord] = []
    for source in sources:
        locale = SourceLocale(source)
        result = load_directory_catalog(DATA_DIR / source, locale)
        merged.update(result.terms)
        records.extend(result.catalog)
    return DictionaryLoadResult(terms=merged, catalog=validate_rule_catalog(records))


def load_custom(path: Path) -> Dict[str, str]:
    """Load a custom dictionary file."""
    return load_json_file(path)


def load_dictionary(
    sources: Optional[List[str]] = None,
    custom_path: Optional[Path] = None,
    include_builtin: bool = True,
) -> Dict[str, str]:
    """
    Load and merge dictionaries.

    Args:
        sources: List of sources to load ("cn", "hk"). Default: all.
        custom_path: Path to custom dictionary file.
        include_builtin: Whether to include built-in dictionaries.

    Returns:
        Merged dictionary of all terms.
    """
    merged: Dict[str, str] = {}
    if include_builtin:
        merged.update(load_builtin(sources))
    if custom_path:
        selected_sources = ["cn", "hk"] if sources is None else sources
        merged.update(
            _load_effective_rule_file(
                custom_path,
                source_locale=SourceLocale.CN,
                rule_class=RuleClass.CUSTOM,
                allowed_sources=selected_sources,
            )
        )
    return merged


def load_dictionary_catalog(
    sources: Optional[List[str]] = None,
    custom_path: Optional[Path] = None,
    include_builtin: bool = True,
) -> DictionaryLoadResult:
    """Load runtime terms and catalog while preserving the existing winner order."""

    selected_sources = ["cn", "hk"] if sources is None else sources
    merged: Dict[str, str] = {}
    records: list[RuleRecord] = []
    if include_builtin:
        builtins = load_builtin_catalog(selected_sources)
        merged.update(builtins.terms)
        records.extend(builtins.catalog)
    if custom_path:
        custom = load_rule_file(
            custom_path,
            source_locale=SourceLocale.CN,
            rule_class=RuleClass.CUSTOM,
            allowed_sources=selected_sources,
        )
        merged.update(custom.terms)
        records.extend(custom.catalog)
    return DictionaryLoadResult(terms=merged, catalog=validate_rule_catalog(records))


def get_source_terms(terms: Dict[str, str]) -> Set[str]:
    """Get all source terms (keys) from a dictionary."""
    return set(terms.keys())


def get_target_terms(terms: Dict[str, str]) -> Set[str]:
    """Get all target terms (values) from a dictionary."""
    return set(terms.values())
