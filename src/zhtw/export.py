"""Export module for generating SDK data and golden test files."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from . import __version__
from .charconv import get_ambiguous_chars, get_balanced_defaults, get_translate_table, load_charmap
from .converter import convert_text
from .dictionary import DATA_DIR, load_dictionary, load_directory
from .lookup import lookup_word
from .matcher import Matcher


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
    for src in sources:
        src_terms = load_directory(DATA_DIR / src)
        terms[src] = src_terms
        terms_counts[src] = len(src_terms)

    return {
        "version": __version__,
        "stats": {
            "charmap_count": len(charmap),
            "ambiguous_count": len(ambiguous),
            "terms_cn_count": terms_counts.get("cn", 0),
            "terms_hk_count": terms_counts.get("hk", 0),
        },
        "charmap": {
            "chars": charmap,
            "ambiguous": sorted(ambiguous),
            "balanced_defaults": get_balanced_defaults(),
        },
        "terms": terms,
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
    # Identity-term protection: char layer must NOT convert chars inside identity terms
    ("\u5c38\u4f4d\u7d20\u9910", ["cn"], "identity: \u5c38\u4f4d\u7d20\u9910 protects \u5c38"),
    ("\u4eba\u4e91\u4ea6\u4e91", ["cn"], "identity: \u4eba\u4e91\u4ea6\u4e91 protects \u4e91"),
    (
        "\u6025\u75c7\u5f88\u4e25\u91cd",
        ["cn"],
        "identity+char: \u6025\u75c7 protected, \u4e25\u91cd char-converted",
    ),
]

# Lookup test cases — individual words/chars
_LOOKUP_CASES = [
    ("\u8f6f\u4ef6", ["cn"]),
    ("\u8fd9", ["cn"]),
    ("\u53f0", ["cn"]),
    ("\u5934\u53d1", ["cn"]),
    ("\u8edf\u4ef6", ["hk"]),
    ("\u6025\u75c7", ["cn"]),  # identity term: no conversion expected
]


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

    for input_text, srcs, _desc in _GOLDEN_CASES:
        if sources is not None and not all(s in sources for s in srcs):
            continue
        terms = load_dictionary(sources=srcs)
        matcher = Matcher(terms)
        char_table = get_translate_table() if "cn" in srcs else None

        # Convert
        converted, _ = convert_text(input_text, matcher, fix=True, char_table=char_table)
        convert_cases.append(
            {
                "input": input_text,
                "sources": srcs,
                "expected": converted,
            }
        )

        # Check — get matches with positions
        _, matches = convert_text(input_text, matcher, fix=False, char_table=char_table)
        check_cases.append(
            {
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
        )

    for word, srcs in _LOOKUP_CASES:
        if sources is not None and not all(s in sources for s in srcs):
            continue
        terms = load_dictionary(sources=srcs)
        matcher = Matcher(terms)
        char_table = get_translate_table() if "cn" in srcs else None
        result = lookup_word(word, matcher, char_table)
        lookup_cases.append(
            {
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
        )

    return {
        "version": __version__,
        "description": "SDK consistency test — all SDKs must pass",
        "convert": convert_cases,
        "check": check_cases,
        "lookup": lookup_cases,
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
) -> tuple[Path, Path]:
    """Export data and golden test to files.

    Args:
        output_dir: Directory to write files to.
        sources: Sources to export. Default: ["cn", "hk"].

    Returns:
        Tuple of (data_path, golden_path).
    """
    data = export_data(sources=sources)
    golden = generate_golden_test(sources=sources)

    # Sort for deterministic output
    sorted_data = _sort_dict(data)

    data_path = output_dir / "zhtw-data.json"
    golden_path = output_dir / "golden-test.json"

    data_path.write_text(
        json.dumps(sorted_data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    golden_path.write_text(
        json.dumps(golden, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    return data_path, golden_path
