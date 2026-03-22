"""
字元級簡繁轉換。

使用 str.translate() 做 O(n) 字元替換，作為詞彙級轉換的補底層。
只處理安全的一對一映射，歧義字由詞庫層（Aho-Corasick）處理。
"""

from __future__ import annotations

import json
import threading
from pathlib import Path
from typing import Dict, List, Optional

CHARMAP_DIR = Path(__file__).parent / "data" / "charmap"
CHARMAP_FILE = CHARMAP_DIR / "safe_chars.json"

# 模組級快取（執行緒安全）
_lock = threading.Lock()
_cached_charmap: Optional[Dict[str, str]] = None
_cached_table: Optional[Dict[int, str]] = None
_cached_ambiguous: Optional[List[str]] = None


def load_charmap(path: Optional[Path] = None) -> Dict[str, str]:
    """載入字元映射表。"""
    global _cached_charmap
    if _cached_charmap is not None and path is None:
        return _cached_charmap

    p = path or CHARMAP_FILE
    with open(p, encoding="utf-8") as f:
        data = json.load(f)

    result = data.get("chars", data)
    if path is None:
        with _lock:
            _cached_charmap = result
    return result


def build_translate_table(charmap: Dict[str, str]) -> Dict[int, str]:
    """從字元映射建立 str.translate() 表。"""
    return {ord(k): v for k, v in charmap.items()}


def get_translate_table(path: Optional[Path] = None) -> Dict[int, str]:
    """取得快取的轉換表（單例模式）。"""
    global _cached_table
    if _cached_table is not None and path is None:
        return _cached_table

    table = build_translate_table(load_charmap(path))
    if path is None:
        with _lock:
            _cached_table = table
    return table


def char_convert(text: str, table: Dict[int, str]) -> str:
    """對文字做字元級轉換。"""
    return text.translate(table)


def get_ambiguous_chars(path: Optional[Path] = None) -> List[str]:
    """取得歧義字清單（供報告用）。"""
    global _cached_ambiguous
    if _cached_ambiguous is not None and path is None:
        return _cached_ambiguous

    p = path or CHARMAP_FILE
    with open(p, encoding="utf-8") as f:
        data = json.load(f)

    result = data.get("ambiguous_excluded", [])
    if path is None:
        with _lock:
            _cached_ambiguous = result
    return result


def get_charmap_stats(path: Optional[Path] = None) -> Dict[str, int]:
    """取得字元映射統計（供 stats 指令用）。"""
    charmap = load_charmap(path)
    ambiguous = get_ambiguous_chars(path)
    return {
        "safe_chars": len(charmap),
        "ambiguous_excluded": len(ambiguous),
        "total_coverage": len(charmap) + len(ambiguous),
    }


def clear_cache() -> None:
    """清除快取（供測試用）。"""
    global _cached_charmap, _cached_table, _cached_ambiguous
    with _lock:
        _cached_charmap = None
        _cached_table = None
        _cached_ambiguous = None
