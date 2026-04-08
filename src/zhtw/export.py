"""Export module for generating SDK data and golden test files."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from . import __version__
from .charconv import get_ambiguous_chars, load_charmap
from .dictionary import DATA_DIR, load_directory


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
        "exported_at": datetime.now(timezone.utc).isoformat(),
        "stats": {
            "charmap_count": len(charmap),
            "ambiguous_count": len(ambiguous),
            "terms_cn_count": terms_counts.get("cn", 0),
            "terms_hk_count": terms_counts.get("hk", 0),
        },
        "charmap": {
            "chars": charmap,
            "ambiguous": sorted(ambiguous),
        },
        "terms": terms,
    }
