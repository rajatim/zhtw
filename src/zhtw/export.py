"""Export module for generating SDK data and golden test files."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from . import __version__
from .charconv import (
    get_ambiguous_chars,
    get_balanced_defaults,
    get_protect_terms,
    get_translate_table,
    load_charmap,
)
from .converter import convert, convert_text, inject_protect_terms
from .dictionary import DATA_DIR, load_dictionary, load_directory_catalog
from .explain import explain
from .json_adapter import transform_json_values
from .lookup import lookup_word
from .matcher import Matcher
from .rules import (
    RuleClass,
    SourceLocale,
    TrustLevel,
    legacy_rule_record,
    validate_rule_catalog,
)

DATA_SCHEMA_VERSION = 2
GOLDEN_SCHEMA_VERSION = 2
JSON_ADAPTER_GOLDEN_SCHEMA_VERSION = 1


def _group_rule_catalog(catalog: list) -> Dict[str, Any]:
    """Compact repeated metadata while keeping every rule independently addressable."""

    groups: Dict[tuple, Dict[str, Any]] = {}
    for record in catalog:
        key = (
            record.source_locale.value,
            record.rule_class.value,
            record.domain,
            record.trust_level.value,
            record.priority,
            record.context,
            record.evidence_source,
            record.review_status.value,
        )
        group = groups.get(key)
        if group is None:
            group = {
                "source_locale": record.source_locale.value,
                "rule_class": record.rule_class.value,
                "domain": record.domain,
                "trust_level": record.trust_level.value,
                "priority": record.priority,
                "context": list(record.context),
                "evidence_source": record.evidence_source,
                "review_status": record.review_status.value,
                "rules": {},
            }
            groups[key] = group
        group["rules"][record.id] = [record.source, record.target]
    return {"format": "grouped-v1", "groups": list(groups.values())}


def export_data(sources: Optional[List[str]] = None) -> Dict[str, Any]:
    """Assemble export data from dictionaries and charmap.

    Args:
        sources: List of sources to export ("cn", "hk"). Default: ["cn", "hk"].

    Returns:
        Dict matching zhtw-data.json schema.
    """
    if sources is None:
        sources = ["cn", "hk"]

    charmap = load_charmap()
    ambiguous = get_ambiguous_chars()

    terms: Dict[str, Dict[str, str]] = {}
    terms_counts: Dict[str, int] = {}
    catalog = []
    for src in sources:
        loaded = load_directory_catalog(DATA_DIR / src, src)
        terms[src] = loaded.terms
        catalog.extend(loaded.catalog)

    # Bake protect_terms into CN terms so SDKs get them without special code.
    # Identity entries (source == target) are handled natively by all SDKs'
    # Aho-Corasick matching — no SDK-side changes needed.
    if "cn" in terms:
        for _char, pterms in get_protect_terms().items():
            for term in pterms:
                terms["cn"][term] = term
                catalog.append(
                    legacy_rule_record(
                        source_locale=SourceLocale.CN,
                        source=term,
                        target=term,
                        rule_class=RuleClass.GENERATED_GUARD,
                        domain="general",
                        trust_level=TrustLevel.GENERATED,
                        priority=200,
                        evidence_source="data/charmap/disambiguation.json",
                    )
                )

    catalog = list(validate_rule_catalog(catalog))

    for src in sources:
        terms_counts[src] = len(terms[src])

    return {
        "schema_version": DATA_SCHEMA_VERSION,
        "version": __version__,
        "stats": {
            "charmap_count": len(charmap),
            "ambiguous_count": len(ambiguous),
            "terms_cn_count": terms_counts.get("cn", 0),
            "terms_hk_count": terms_counts.get("hk", 0),
            "rule_catalog_count": len(catalog),
        },
        "charmap": {
            "chars": charmap,
            "ambiguous": sorted(ambiguous),
            "balanced_defaults": get_balanced_defaults(),
            "balanced_protect_terms": get_protect_terms(),
        },
        "terms": terms,
        "rule_catalog": _group_rule_catalog(catalog),
    }


# Golden test cases — inputs that exercise key conversion scenarios
# Uses Unicode escapes to prevent pre-commit zhtw hook from converting inputs.
_GOLDEN_CASES = [
    # (input_text, sources, description)
    ("\u8f6f\u4ef6\u6d4b\u8bd5", ["cn"], "term layer: multi-term"),
    ("\u8fd9\u4e2a\u670d\u52a1\u5668\u7684\u5185\u5b58\u4e0d\u591f", ["cn"], "mixed"),
    ("\u5934\u53d1\u5f88\u5e72", ["cn"], "ambiguous chars"),
    ("\u8edf\u4ef6\u5de5\u7a0b\u5e2b", ["hk"], "HK source: term only"),
    ("\u5df2\u7d93\u662f\u7e41\u9ad4", ["cn"], "no conversion needed"),
    ("\u6570\u636e\u5e93\u670d\u52a1\u5668", ["cn"], "term layer: compound terms"),
    ("\u4e91\u8ba1\u7b97", ["cn"], "ambiguous: cloud"),
    ("\u53d1\u5c55\u5f88\u5feb", ["cn"], "ambiguous: fa"),
    (
        "\u5e94\u7528\u4e8e",
        ["cn"],
        "overlap: losing suffix term must not block char conversion",
    ),
    (
        "\u4e24\u5343\u4e07",
        ["cn"],
        "overlap: selected prefix leaves suffix available to char conversion",
    ),
    # Identity-term protection: char layer must NOT convert chars inside identity terms
    ("\u5c38\u4f4d\u7d20\u9910", ["cn"], "identity: \u5c38\u4f4d\u7d20\u9910 protects \u5c38"),
    ("\u4eba\u4e91\u4ea6\u4e91", ["cn"], "identity: \u4eba\u4e91\u4ea6\u4e91 protects \u4e91"),
    (
        "\u6025\u75c7\u5f88\u4e25\u91cd",
        ["cn"],
        "identity+char: \u6025\u75c7 protected, \u4e25\u91cd char-converted",
    ),
    ("\u708e\u75c7", ["cn"], "identity: \u708e\u75c7 protects \u75c7 (medical pattern)"),
    (
        "\u515a\u592a\u5c09\u5403\u5339\u98df",
        ["cn"],
        "identity: \u515a\u592a\u5c09\u5403\u5339\u98df protects \u515a (proper name)",
    ),
    # Balanced mode: disambiguation v2 protect_terms
    ("\u4ee5\u540e\u518d\u8bf4", ["cn"], "balanced: \u540e default \u5f8c", "balanced"),
    ("\u7687\u540e\u5f88\u7f8e", ["cn"], "balanced: \u7687\u540e protected", "balanced"),
    ("\u5bb6\u91cc\u5f88\u5927", ["cn"], "balanced: \u91cc default \u88e1", "balanced"),
    ("\u516c\u91cc\u6570\u5f88\u5927", ["cn"], "balanced: \u516c\u91cc protected", "balanced"),
    (
        "\u5f71\u540e\u5f97\u5956",
        ["cn"],
        "balanced: \u5f71\u540e protected (not in base dict)",
        "balanced",
    ),
    # Balanced mode: bare balanced_defaults char (NOT in dictionary, NOT in charmap)
    ("\u4e30\u6ee1", ["cn"], "balanced: \u4e30 default \u8c50 (bare char)", "balanced"),
]

# Lookup test cases — individual words/chars
# Format: (word, sources) or (word, sources, ambiguity_mode)
_LOOKUP_CASES = [
    ("\u8f6f\u4ef6", ["cn"]),
    ("\u8fd9", ["cn"]),
    ("\u53f0", ["cn"]),
    ("\u5934\u53d1", ["cn"]),
    ("\u8edf\u4ef6", ["hk"]),
    ("\u6025\u75c7", ["cn"]),  # identity term: no conversion expected
    ("\u4f19\u5934", ["cn"]),  # term target contains charmap-convertible char: 伙頭 not 夥頭
    ("\u4e30\u6ee1", ["cn"], "balanced"),  # balanced: 丰→豐 default + 滿→滿 charmap
    ("\u5f71\u540e", ["cn"], "balanced"),  # balanced: 影後 protect_term → no conversion
]

# zhtw:disable - shared fixtures intentionally contain Simplified Chinese input
_JSON_ADAPTER_CASES = [
    (
        "nested-values-and-number-bytes",
        '{\n  "软件 key": "软件", "nested": ["服务器", 1.00e+02, true, null],\n'
        '  "object": {"接口": "接口", "empty": ""}\n}\n',
        ["cn"],
        "strict",
    ),
    (
        "escaped-quote-backslash-newline",
        '{"value":"软件\\"C:\\\\tmp\\n"}',
        ["cn"],
        "strict",
    ),
    (
        "unchanged-escape-bytes",
        '{"escaped":"\\u8edf\\u9ad4","slash":"a\\/b"}',
        ["cn"],
        "strict",
    ),
    (
        "supplementary-han-and-repeated-values",
        '{"rare":"\\ud840\\udc00软件","items":["软件","软件"]}',
        ["cn"],
        "strict",
    ),
    (
        "mixed-text-and-surrounding-space",
        '{"mixed":"USB接口 v2","space":" 软件 "}',
        ["cn"],
        "strict",
    ),
    (
        "balanced-string-value",
        '{"value":"丰满"}',
        ["cn"],
        "balanced",
    ),
]

_JSON_ADAPTER_REJECT_CASES = [
    ("duplicate-key", '{"key":"软件","key":"軟體"}', "duplicate_key"),
    ("escaped-duplicate-key", '{"key":"软件","\\u006bey":"軟體"}', "duplicate_key"),
    ("trailing-comma", '{"key":"软件",}', "invalid_json"),
    ("non-standard-number", '{"value":NaN}', "invalid_json"),
    ("unpaired-surrogate", '{"value":"\\ud800"}', "invalid_json"),
]

_JSON_ADAPTER_WRITE_FAILURES = [
    ("read-only-file", '{"value":"软件"}', "read_only"),
    ("atomic-replace-failure", '{"value":"软件"}', "replace_failure"),
    ("encoding-failure", '{"value":"软件"}', "encoding_failure"),
]
# zhtw:enable


def generate_json_adapter_golden(
    sources: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Generate exact-byte JSON adapter fixtures shared by every SDK."""

    cases = []
    for case_id, input_text, srcs, mode in _JSON_ADAPTER_CASES:
        if sources is not None and not all(source in sources for source in srcs):
            continue
        result = transform_json_values(
            input_text,
            lambda value, selected=srcs, selected_mode=mode: convert(
                value,
                sources=selected,
                ambiguity_mode=selected_mode,
            ),
        )
        entry: Dict[str, Any] = {
            "id": case_id,
            "input": input_text,
            "sources": srcs,
            "expected": result.output,
            "changed_values": len(result.changes),
        }
        if mode != "strict":
            entry["ambiguity_mode"] = mode
        cases.append(entry)

    return {
        "schema_version": JSON_ADAPTER_GOLDEN_SCHEMA_VERSION,
        "version": __version__,
        "escaping": "json-compact-unicode-v1",
        "cases": cases,
        "reject": [
            {"id": case_id, "input": input_text, "error_code": error_code}
            for case_id, input_text, error_code in _JSON_ADAPTER_REJECT_CASES
        ],
        "write_failures": [
            {
                "id": case_id,
                "input": input_text,
                "converted": transform_json_values(
                    input_text,
                    lambda value: convert(value, sources=["cn"]),
                ).output,
                "failure": failure,
                "expected_after_failure": input_text,
            }
            for case_id, input_text, failure in _JSON_ADAPTER_WRITE_FAILURES
        ],
    }


def generate_golden_test(
    sources: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Generate golden test JSON from Python pipeline results.

    Args:
        sources: Only include cases matching these sources. Default: all.

    Runs the actual Python conversion on test cases and records results.
    SDKs must reproduce these exact results.
    """
    convert_cases = []
    check_cases = []
    lookup_cases = []
    explain_cases = []

    for case in _GOLDEN_CASES:
        input_text, srcs, _desc = case[0], case[1], case[2]
        mode = case[3] if len(case) > 3 else "strict"

        if sources is not None and not all(s in sources for s in srcs):
            continue

        terms = load_dictionary(sources=srcs)
        inject_protect_terms(terms, srcs)
        matcher = Matcher(terms)
        char_table = get_translate_table() if "cn" in srcs else None

        # Convert
        converted, _ = convert_text(
            input_text,
            matcher,
            fix=True,
            char_table=char_table,
            ambiguity_mode=mode,
        )
        entry: Dict[str, Any] = {
            "input": input_text,
            "sources": srcs,
            "expected": converted,
        }
        if mode != "strict":
            entry["ambiguity_mode"] = mode
        convert_cases.append(entry)

        # Check — get matches with positions
        _, matches = convert_text(
            input_text,
            matcher,
            fix=False,
            char_table=char_table,
            ambiguity_mode=mode,
        )
        check_entry: Dict[str, Any] = {
            "input": input_text,
            "sources": srcs,
            "expected_matches": [
                {
                    "start": m.start,
                    "end": m.end,
                    "source": m.source,
                    "target": m.target,
                }
                for m, _line, _col in matches
            ],
        }
        if mode != "strict":
            check_entry["ambiguity_mode"] = mode
        check_cases.append(check_entry)

        explained = explain(input_text, sources=srcs, ambiguity_mode=mode)
        if explained.output != converted:
            raise RuntimeError("golden explain output diverged from convert output")
        explain_entry: Dict[str, Any] = {
            "input": input_text,
            "sources": srcs,
            "expected_output": explained.output,
            "expected_events": [event.to_mapping() for event in explained.events],
        }
        if mode != "strict":
            explain_entry["ambiguity_mode"] = mode
        explain_cases.append(explain_entry)

    for case in _LOOKUP_CASES:
        word, srcs = case[0], case[1]
        mode = case[2] if len(case) > 2 else "strict"

        if sources is not None and not all(s in sources for s in srcs):
            continue
        terms = load_dictionary(sources=srcs)
        inject_protect_terms(terms, srcs)
        matcher = Matcher(terms)
        char_table = get_translate_table() if "cn" in srcs else None
        result = lookup_word(word, matcher, char_table, ambiguity_mode=mode)
        entry: Dict[str, Any] = {
            "input": word,
            "sources": srcs,
            "expected_output": result.output,
            "expected_changed": result.changed,
            "expected_details": [
                {
                    "source": d.source,
                    "target": d.target,
                    "layer": d.layer,
                    "position": d.position,
                }
                for d in result.details
            ],
        }
        if mode != "strict":
            entry["ambiguity_mode"] = mode
        lookup_cases.append(entry)

    return {
        "schema_version": GOLDEN_SCHEMA_VERSION,
        "version": __version__,
        "description": "SDK consistency test — all SDKs must pass",
        "convert": convert_cases,
        "check": check_cases,
        "lookup": lookup_cases,
        "explain": explain_cases,
    }


def _sort_dict(d: dict) -> dict:
    """Recursively sort dict keys for deterministic output."""
    result = {}
    for k in sorted(d.keys()):
        v = d[k]
        if isinstance(v, dict):
            result[k] = _sort_dict(v)
        else:
            result[k] = v
    return result


def write_export(
    output_dir: Path,
    sources: Optional[List[str]] = None,
) -> tuple[Path, Path, Path]:
    """Export data and golden test to files.

    Args:
        output_dir: Directory to write files to.
        sources: Sources to export. Default: ["cn", "hk"].

    Returns:
        Tuple of (data_path, golden_path, json_adapter_path).
    """
    data = export_data(sources=sources)
    golden = generate_golden_test(sources=sources)
    json_adapter = generate_json_adapter_golden(sources=sources)

    # Sort for deterministic output
    sorted_data = _sort_dict(data)

    data_path = output_dir / "zhtw-data.json"
    golden_path = output_dir / "golden-test.json"
    json_adapter_path = output_dir / "json-adapter-golden.json"

    data_path.write_text(
        json.dumps(sorted_data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    golden_path.write_text(
        json.dumps(golden, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    json_adapter_path.write_text(
        json.dumps(json_adapter, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    return data_path, golden_path, json_adapter_path
