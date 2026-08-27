"""Versioned rule records and stable identifiers.

The 4.5 rule catalog is descriptive only. Runtime matching continues to use the
effective ``dict[str, str]`` produced by the existing loader until the catalog
compatibility layer has proven that the effective mapping is unchanged.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from enum import Enum
from typing import Any, Iterable, Mapping


class RuleCatalogError(ValueError):
    """Raised when rule data is malformed or internally inconsistent."""


class SourceLocale(str, Enum):
    """Source locale currently supported by the production dictionary."""

    CN = "cn"
    HK = "hk"


class RuleClass(str, Enum):
    """Precedence class that describes the existing loader order."""

    BULK = "bulk"
    GENERATED_GUARD = "generated_guard"
    CURATED = "curated"
    CUSTOM = "custom"


class TrustLevel(str, Enum):
    """Evidence level recorded for review and explanation."""

    IMPORTED = "imported"
    GENERATED = "generated"
    CURATED = "curated"
    CUSTOM = "custom"


class ReviewStatus(str, Enum):
    """Human review state. Only approved rules may enter released data."""

    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


RULE_DOMAINS = frozenset(
    {
        "general",
        "business",
        "daily",
        "ecommerce",
        "education",
        "finance",
        "formal",
        "gaming",
        "geography",
        "it",
        "legal",
        "medical",
        "social",
        "ui",
    }
)

_RULE_ID_RE = re.compile(r"^[a-z0-9][a-z0-9._:-]{2,127}$")
_RECORD_KEYS = frozenset(
    {
        "id",
        "source_locale",
        "source",
        "target",
        "rule_class",
        "domain",
        "trust_level",
        "priority",
        "context",
        "evidence_source",
        "review_status",
    }
)


def _enum_value(value: str | Enum) -> str:
    return value.value if isinstance(value, Enum) else value


def legacy_rule_id(
    source_locale: SourceLocale | str,
    source: str,
    target: str,
    rule_class: RuleClass | str,
) -> str:
    """Return a deterministic legacy ID that does not depend on a file path."""

    locale = SourceLocale(_enum_value(source_locale))
    kind = RuleClass(_enum_value(rule_class))
    if not isinstance(source, str) or not source:
        raise RuleCatalogError("rule source must be a non-empty string")
    if not isinstance(target, str) or not target:
        raise RuleCatalogError("rule target must be a non-empty string")

    identity = {
        "rule_class": kind.value,
        "source": source,
        "source_locale": locale.value,
        "target": target,
    }
    canonical = json.dumps(
        identity,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    digest = hashlib.sha256(canonical).hexdigest()[:24]
    return f"legacy:{locale.value}:{kind.value}:{digest}"


@dataclass(frozen=True, slots=True)
class RuleRecord:
    """A schema-v2 rule record shared by authoring and SDK exports."""

    id: str
    source_locale: SourceLocale
    source: str
    target: str
    rule_class: RuleClass
    domain: str
    trust_level: TrustLevel
    priority: int
    context: tuple[str, ...]
    evidence_source: str | None
    review_status: ReviewStatus

    def __post_init__(self) -> None:
        if not isinstance(self.id, str) or not _RULE_ID_RE.fullmatch(self.id):
            raise RuleCatalogError("rule id has an invalid format")
        if not isinstance(self.source_locale, SourceLocale):
            raise RuleCatalogError("source_locale must be a SourceLocale")
        if not isinstance(self.rule_class, RuleClass):
            raise RuleCatalogError("rule_class must be a RuleClass")
        if not isinstance(self.trust_level, TrustLevel):
            raise RuleCatalogError("trust_level must be a TrustLevel")
        if not isinstance(self.review_status, ReviewStatus):
            raise RuleCatalogError("review_status must be a ReviewStatus")
        if not isinstance(self.source, str) or not self.source:
            raise RuleCatalogError("rule source must be a non-empty string")
        if not isinstance(self.target, str) or not self.target:
            raise RuleCatalogError("rule target must be a non-empty string")
        if self.domain not in RULE_DOMAINS:
            raise RuleCatalogError(f"unknown rule domain: {self.domain!r}")
        if isinstance(self.priority, bool) or not isinstance(self.priority, int):
            raise RuleCatalogError("rule priority must be an integer")
        if not -1000 <= self.priority <= 1000:
            raise RuleCatalogError("rule priority must be between -1000 and 1000")
        if not isinstance(self.context, tuple):
            raise RuleCatalogError("rule context must be a tuple")
        if any(not isinstance(value, str) or not value for value in self.context):
            raise RuleCatalogError("rule context values must be non-empty strings")
        if len(set(self.context)) != len(self.context):
            raise RuleCatalogError("rule context values must be unique")
        if self.evidence_source is not None and (
            not isinstance(self.evidence_source, str) or not self.evidence_source
        ):
            raise RuleCatalogError("evidence_source must be null or a non-empty string")
        if self.review_status is ReviewStatus.APPROVED and self.evidence_source is None:
            raise RuleCatalogError("approved schema-v2 rules require evidence_source")

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any]) -> RuleRecord:
        """Parse one schema-v2 record and reject unknown or missing fields."""

        if not isinstance(value, Mapping):
            raise RuleCatalogError("rule record must be an object")
        keys = set(value)
        unknown = keys - _RECORD_KEYS
        missing = _RECORD_KEYS - keys
        if unknown:
            raise RuleCatalogError(f"unknown rule fields: {', '.join(sorted(unknown))}")
        if missing:
            raise RuleCatalogError(f"missing rule fields: {', '.join(sorted(missing))}")

        context = value["context"]
        if not isinstance(context, list):
            raise RuleCatalogError("rule context must be an array")

        try:
            return cls(
                id=value["id"],
                source_locale=SourceLocale(value["source_locale"]),
                source=value["source"],
                target=value["target"],
                rule_class=RuleClass(value["rule_class"]),
                domain=value["domain"],
                trust_level=TrustLevel(value["trust_level"]),
                priority=value["priority"],
                context=tuple(context),
                evidence_source=value["evidence_source"],
                review_status=ReviewStatus(value["review_status"]),
            )
        except (TypeError, ValueError) as exc:
            raise RuleCatalogError(f"invalid rule record: {exc}") from exc

    def to_mapping(self) -> dict[str, Any]:
        """Return the canonical JSON-compatible representation."""

        return {
            "id": self.id,
            "source_locale": self.source_locale.value,
            "source": self.source,
            "target": self.target,
            "rule_class": self.rule_class.value,
            "domain": self.domain,
            "trust_level": self.trust_level.value,
            "priority": self.priority,
            "context": list(self.context),
            "evidence_source": self.evidence_source,
            "review_status": self.review_status.value,
        }


def legacy_rule_record(
    *,
    source_locale: SourceLocale | str,
    source: str,
    target: str,
    rule_class: RuleClass | str,
    domain: str = "general",
    trust_level: TrustLevel | str = TrustLevel.CURATED,
    priority: int = 0,
    context: Iterable[str] = (),
    evidence_source: str,
) -> RuleRecord:
    """Create approved descriptive metadata for one legacy effective rule."""

    locale = SourceLocale(_enum_value(source_locale))
    kind = RuleClass(_enum_value(rule_class))
    trust = TrustLevel(_enum_value(trust_level))
    return RuleRecord(
        id=legacy_rule_id(locale, source, target, kind),
        source_locale=locale,
        source=source,
        target=target,
        rule_class=kind,
        domain=domain,
        trust_level=trust,
        priority=priority,
        context=tuple(context),
        evidence_source=evidence_source,
        review_status=ReviewStatus.APPROVED,
    )


def validate_rule_catalog(records: Iterable[RuleRecord]) -> tuple[RuleRecord, ...]:
    """Validate stable identities and let later equivalent metadata win."""

    by_id: dict[str, RuleRecord] = {}
    ordered: list[RuleRecord] = []
    positions: dict[str, int] = {}
    for record in records:
        if not isinstance(record, RuleRecord):
            raise RuleCatalogError("catalog items must be RuleRecord instances")
        previous = by_id.get(record.id)
        if previous is None:
            by_id[record.id] = record
            positions[record.id] = len(ordered)
            ordered.append(record)
            continue

        previous_identity = (
            previous.source_locale,
            previous.source,
            previous.target,
            previous.rule_class,
        )
        record_identity = (
            record.source_locale,
            record.source,
            record.target,
            record.rule_class,
        )
        if previous_identity != record_identity:
            raise RuleCatalogError(f"rule id {record.id!r} points to different content")
        by_id[record.id] = record
        ordered[positions[record.id]] = record
    return tuple(ordered)
