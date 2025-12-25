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


def load_json_file(path: Path) -> Dict[str, str]:
    """Load a JSON dictionary file."""
    if not path.exists():
        return {}

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Support both simple format and extended format
    terms = data.get("terms", data)

    result = {}
    for source, target in terms.items():
        if isinstance(target, dict):
            # Extended format: {"target": "...", "category": "...", ...}
            result[source] = target.get("target", target)
        else:
            # Simple format: "source": "target"
            result[source] = target

    return result


def load_directory(directory: Path) -> Dict[str, str]:
    """Load all JSON files from a directory and merge them."""
    merged = {}

    if not directory.exists():
        return merged

    for json_file in sorted(directory.glob("*.json")):
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
