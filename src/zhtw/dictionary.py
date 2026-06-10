"""
Dictionary module for loading and managing terminology mappings.

Supports:
- CN (Simplified Chinese) → TW (Taiwan Traditional)
- HK (Hong Kong Traditional) → TW (Taiwan Traditional)
"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Set

# Built-in terms directory
DATA_DIR = Path(__file__).parent / "data" / "terms"

# Bulk-imported dictionaries (machine-generated, lower trust) load FIRST so
# that every hand-curated file overrides them on key collisions. Without an
# explicit order, alphabetical glob order would let opencc.json (28k imported
# terms) silently override curated entries.
BULK_FILES = frozenset({"opencc.json"})

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
    }
)


def load_json_file(path: Path) -> Dict[str, str]:
    """Load a JSON dictionary file."""
    if not path.exists():
        return {}

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Support both wrapped format ({"terms": {...}, "version": ...}) and
    # legacy flat format ({"src": "tgt", ...}). For the legacy flat format we
    # must exclude reserved metadata keys, otherwise they leak into the term
    # mapping (e.g. version → "1.0", description → "OpenCC + ...").
    if "terms" in data:
        terms = data["terms"]
    else:
        terms = {k: v for k, v in data.items() if k not in _METADATA_KEYS}

    result = {}
    for source, target in terms.items():
        if isinstance(target, dict):
            # Extended format: {"target": "...", "category": "...", ...}
            if "target" not in target:
                continue  # Skip entries missing 'target' field
            result[source] = target["target"]
        else:
            # Simple format: "source": "target"
            result[source] = target

    return result


def iter_directory_files(directory: Path) -> List[Path]:
    """List JSON files in precedence order: bulk imports first, curated last.

    後載者覆蓋先載者，因此 bulk 匯入檔（BULK_FILES）排最前、
    手工策展檔按字母序排後 —— key 碰撞時手工詞條必定勝出。
    """
    files = sorted(directory.glob("*.json"))
    return [f for f in files if f.name in BULK_FILES] + [
        f for f in files if f.name not in BULK_FILES
    ]


def load_directory(directory: Path) -> Dict[str, str]:
    """Load all JSON files from a directory and merge them."""
    merged = {}

    if not directory.exists():
        return merged

    for json_file in iter_directory_files(directory):
        terms = load_json_file(json_file)
        merged.update(terms)

    return merged


def load_builtin(sources: Optional[List[str]] = None) -> Dict[str, str]:
    """
    Load built-in dictionaries.

    Args:
        sources: List of sources to load. Options: "cn", "hk", or None for all.

    Returns:
        Merged dictionary of all terms.
    """
    if sources is None:
        sources = ["cn", "hk"]

    merged = {}

    for source in sources:
        source_dir = DATA_DIR / source
        terms = load_directory(source_dir)
        merged.update(terms)

    return merged


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
    merged = {}

    # Load built-in dictionaries
    if include_builtin:
        merged.update(load_builtin(sources))

    # Load custom dictionary (overrides built-in)
    if custom_path:
        merged.update(load_custom(custom_path))

    return merged


def get_source_terms(terms: Dict[str, str]) -> Set[str]:
    """Get all source terms (keys) from a dictionary."""
    return set(terms.keys())


def get_target_terms(terms: Dict[str, str]) -> Set[str]:
    """Get all target terms (values) from a dictionary."""
    return set(terms.values())
