"""
Converter module for processing files and text.

Supports:
- Single file processing
- Directory scanning (sequential; see convert_directory for the workers note)
- Pre-filtering (skip non-Chinese files)
- .zhtwignore file support
"""

from __future__ import annotations

import fnmatch
import re
import threading
from bisect import bisect_right
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Set

from .dictionary import load_dictionary
from .encoding import EncodingInfo
from .matcher import Match, Matcher

# Valid values for the `sources` argument of `convert()`.
# Keeping this in sync with the subdirectories under `src/zhtw/data/terms/`.
VALID_SOURCES: frozenset = frozenset({"cn", "hk"})

# Valid values for the `ambiguity_mode` argument.
VALID_AMBIGUITY_MODES: frozenset = frozenset({"strict", "balanced"})


def inject_protect_terms(
    terms: dict[str, str],
    sources: Optional[List[str]] = None,
) -> None:
    """注入 disambiguation.json 的 protect_terms 為 identity mapping。

    必須在所有 Matcher 建構之前呼叫。Identity terms（source == target）
    讓 Aho-Corasick 的 covered positions 保護歧義字不被 term/char/balanced
    layer 錯誤轉換。

    Args:
        terms: 詞典 dict，會被 in-place 修改。
        sources: 來源清單；僅 CN 相關時才注入。
    """
    if sources is None or "cn" in sources:
        from .charconv import get_protect_terms

        for _char, pterms in get_protect_terms().items():
            for term in pterms:
                terms[term] = term


# Regex to detect Chinese characters
CHINESE_PATTERN = re.compile(r"[\u4e00-\u9fff]")

# Ignore directive patterns
IGNORE_LINE_PATTERN = re.compile(r"zhtw:disable-line")
IGNORE_NEXT_PATTERN = re.compile(r"zhtw:disable-next")
IGNORE_START_PATTERN = re.compile(r"zhtw:disable\b")
IGNORE_END_PATTERN = re.compile(r"zhtw:enable\b")

# Default file extensions to check
DEFAULT_EXTENSIONS: Set[str] = {
    # Code
    ".py",
    ".ts",
    ".tsx",
    ".js",
    ".jsx",
    ".java",
    ".vue",
    ".go",
    ".rs",
    # Config
    ".json",
    ".yml",
    ".yaml",
    ".xml",
    ".properties",
    ".toml",
    # Documentation
    ".md",
    ".txt",
    ".html",
    ".css",
    ".scss",
}

# Default directories to exclude
DEFAULT_EXCLUDES: Set[str] = {
    "node_modules",
    ".git",
    "dist",
    "build",
    "target",
    "__pycache__",
    ".venv",
    "venv",
    ".idea",
    ".vscode",
    "coverage",
    ".zhtw-backup",
}

# Default files to exclude
DEFAULT_EXCLUDE_FILES: Set[str] = {
    "package-lock.json",
    "yarn.lock",
    "pnpm-lock.yaml",
    "Cargo.lock",
}


def load_zhtwignore(base_path: Path) -> List[str]:
    """
    Load patterns from .zhtwignore file.

    Args:
        base_path: Base directory to search for .zhtwignore.

    Returns:
        List of ignore patterns.
    """
    ignore_file = base_path / ".zhtwignore"
    if not ignore_file.exists():
        # Also check parent directories up to 3 levels
        for parent in list(base_path.parents)[:3]:
            ignore_file = parent / ".zhtwignore"
            if ignore_file.exists():
                break
        else:
            return []

    patterns = []
    try:
        for line in ignore_file.read_text().splitlines():
            line = line.strip()
            # Skip empty lines and comments
            if line and not line.startswith("#"):
                patterns.append(line)
    except Exception:
        return []

    return patterns


def is_ignored_by_patterns(path: Path, base_path: Path, patterns: List[str]) -> bool:
    """
    Check if path matches any ignore pattern.

    Args:
        path: File path to check.
        base_path: Base directory for relative path calculation.
        patterns: List of ignore patterns.

    Returns:
        True if path should be ignored.
    """
    if not patterns:
        return False

    try:
        rel_path = path.relative_to(base_path)
    except ValueError:
        rel_path = path

    rel_str = str(rel_path)

    for pattern in patterns:
        # Directory pattern (ends with /)
        if pattern.endswith("/"):
            dir_pattern = pattern.rstrip("/")
            if rel_str.startswith(dir_pattern + "/") or rel_str.startswith(dir_pattern):
                return True
            # Check if any parent matches
            for part in rel_path.parts:
                if fnmatch.fnmatch(part, dir_pattern):
                    return True
        else:
            # File or glob pattern
            if fnmatch.fnmatch(rel_str, pattern):
                return True
            if fnmatch.fnmatch(path.name, pattern):
                return True

    return False


@dataclass
class Issue:
    """Represents an issue found in a file."""

    file: Path
    line: int
    column: int
    source: str
    target: str
    context: str = ""


@dataclass
class FileResult:
    """Result of processing a single file."""

    file: Path
    issues: List[Issue] = field(default_factory=list)
    modified: bool = False
    skipped: bool = False
    error: Optional[str] = None
    encoding_info: Optional[EncodingInfo] = None
    encoding_converted: bool = False
    output_encoding: Optional[str] = None


@dataclass
class ConversionResult:
    """Result of processing multiple files."""

    files_checked: int = 0
    files_with_issues: int = 0
    files_modified: int = 0
    files_skipped: int = 0
    total_issues: int = 0
    issues: List[Issue] = field(default_factory=list)
    encoding_conversions: int = 0
    files_needing_conversion: List[Path] = field(default_factory=list)


def contains_chinese(text: str) -> bool:
    """Check if text contains any Chinese characters."""
    return bool(CHINESE_PATTERN.search(text))


def get_ignored_lines(text: str) -> Set[int]:
    """
    Parse text and return set of line numbers that should be ignored.

    Supports:
    - zhtw:disable-line  (ignore current line)
    - zhtw:disable-next  (ignore next line)
    - zhtw:disable ... zhtw:enable  (ignore block)

    Args:
        text: Text to parse.

    Returns:
        Set of 1-based line numbers to ignore.
    """
    ignored: Set[int] = set()
    lines = text.split("\n")
    in_disabled_block = False

    for i, line in enumerate(lines):
        line_num = i + 1  # 1-based

        # Check for block start/end
        if IGNORE_START_PATTERN.search(line):
            # Make sure it's not disable-line or disable-next
            if not IGNORE_LINE_PATTERN.search(line) and not IGNORE_NEXT_PATTERN.search(line):
                in_disabled_block = True
                continue

        if IGNORE_END_PATTERN.search(line):
            in_disabled_block = False
            continue

        # If in disabled block, ignore this line
        if in_disabled_block:
            ignored.add(line_num)
            continue

        # Check for line-level ignores
        if IGNORE_LINE_PATTERN.search(line):
            ignored.add(line_num)

        if IGNORE_NEXT_PATTERN.search(line):
            ignored.add(line_num + 1)

    return ignored


def should_check_file(
    path: Path,
    extensions: Optional[Set[str]] = None,
    excludes: Optional[Set[str]] = None,
    exclude_files: Optional[Set[str]] = None,
) -> bool:
    """
    Check if a file should be processed.

    Args:
        path: File path to check.
        extensions: Allowed file extensions.
        excludes: Directory names to exclude.
        exclude_files: File names to exclude.

    Returns:
        True if file should be processed.
    """
    if extensions is None:
        extensions = DEFAULT_EXTENSIONS
    if excludes is None:
        excludes = DEFAULT_EXCLUDES
    if exclude_files is None:
        exclude_files = DEFAULT_EXCLUDE_FILES

    # Check extension
    if path.suffix.lower() not in extensions:
        return False

    # Check excluded directories
    for part in path.parts:
        if part in excludes:
            return False

    # Check excluded files
    if path.name in exclude_files:
        return False

    return True


def get_context(text: str, start: int, end: int, context_chars: int = 20) -> str:
    """Get context around a match."""
    ctx_start = max(0, start - context_chars)
    ctx_end = min(len(text), end + context_chars)

    prefix = "..." if ctx_start > 0 else ""
    suffix = "..." if ctx_end < len(text) else ""

    context = text[ctx_start:ctx_end].replace("\n", " ")
    return f"{prefix}{context}{suffix}"


def _apply_term_layer(text: str, matcher: Matcher) -> tuple[str, set[int]]:
    """詞庫層替換，並收集已覆蓋的字元位置。

    covered_positions 包含「所有詞庫層命中的位置」，含 identity mapping
    （茶几→茶几 這類保護性 mapping），因此 balanced defaults 不會再改動
    詞庫層已處理過的字元。

    Args:
        text: 要處理的文字。
        matcher: Matcher 實例。

    Returns:
        Tuple of (replaced_text, covered_positions)，covered_positions 是
        詞庫層已處理的字元位置集合（0-based，對應原始 text）。
    """
    if not matcher.terms:
        return text, set()

    covered = matcher.get_covered_positions(text)
    replaced = matcher.replace_all(text)
    return replaced, covered


# 合併（balanced defaults ∘ char_table）後的 translate 表快取。
# value 同時持有來源 dict 的強引用，確保 id() 在快取存活期間不被回收重用。
_MERGED_TABLE_CACHE: dict = {}


def _merged_translate_table(
    char_table: Optional[dict[int, str]],
    defaults: Optional[dict[str, str]],
) -> dict[int, str]:
    """組合 balanced defaults 與 char_table 為單一 str.translate 表。

    語義等價於逐字「先查 defaults，再把結果過 char_table」，
    讓未被 covered 的整段文字可走 C 層級的 str.translate fast path。
    """
    key = (id(char_table), id(defaults))
    cached = _MERGED_TABLE_CACHE.get(key)
    if cached is not None:
        return cached[2]

    merged: dict[int, str] = {}
    if defaults:
        for c, d in defaults.items():
            final = char_table.get(ord(d), d) if char_table else d
            if final != c:
                merged[ord(c)] = final
    if char_table:
        for cp, t in char_table.items():
            if not defaults or chr(cp) not in defaults:
                merged[cp] = t

    if len(_MERGED_TABLE_CACHE) > 8:
        _MERGED_TABLE_CACHE.clear()
    _MERGED_TABLE_CACHE[key] = (char_table, defaults, merged)
    return merged


def _transform_uncovered_segment(
    segment: str,
    start_offset: int,
    covered_positions: set[int],
    sorted_covered: list[int],
    char_table: Optional[dict[int, str]] = None,
    ambiguity_mode: str = "strict",
) -> str:
    """Apply balanced defaults and char-level mapping only outside covered ranges."""
    if not segment or (not char_table and ambiguity_mode != "balanced"):
        return segment

    defaults = None
    if ambiguity_mode == "balanced":
        from .charconv import get_balanced_defaults

        defaults = get_balanced_defaults()

    merged = _merged_translate_table(char_table, defaults)

    # Fast path：區段與 covered 無交集（絕大多數情況）→ C 層級 translate。
    # covered 來自 identity 保護詞與未被選上的重疊命中，通常稀疏。
    if sorted_covered:
        idx = bisect_right(sorted_covered, start_offset - 1)
        intersects = idx < len(sorted_covered) and sorted_covered[idx] < start_offset + len(segment)
    else:
        intersects = False
    if not intersects:
        return segment.translate(merged)

    # Slow path：逐字並跳過 covered 位置（identity 保護區內）
    chars = list(segment)
    for i, ch in enumerate(chars):
        if start_offset + i in covered_positions:
            continue
        chars[i] = merged.get(ord(ch), ch)
    return "".join(chars)


def _apply_conversion_layers(
    text: str,
    matcher: Matcher,
    char_table: Optional[dict[int, str]] = None,
    ambiguity_mode: str = "strict",
    scan: Optional[tuple[List[Match], set[int]]] = None,
) -> str:
    """Apply term, balanced, and char layers while preserving term-covered output.

    Args:
        scan: 預先計算的 ``matcher.scan(text)`` 結果。傳入可避免重複的
            automaton 掃描（convert_text 熱路徑）；None 則自行掃描。
    """
    if not text:
        return text

    if scan is None:
        matches, covered = matcher.scan(text)
    else:
        matches, covered = scan
    sorted_covered = sorted(covered) if covered else []

    if not matches:
        return _transform_uncovered_segment(
            text, 0, covered, sorted_covered, char_table, ambiguity_mode
        )

    parts: list[str] = []
    last_end = 0
    for match in matches:
        parts.append(
            _transform_uncovered_segment(
                text[last_end : match.start],
                last_end,
                covered,
                sorted_covered,
                char_table,
                ambiguity_mode,
            )
        )
        parts.append(match.target)
        last_end = match.end

    parts.append(
        _transform_uncovered_segment(
            text[last_end:],
            last_end,
            covered,
            sorted_covered,
            char_table,
            ambiguity_mode,
        )
    )
    return "".join(parts)


def convert_text(
    text: str,
    matcher: Matcher,
    fix: bool = False,
    ignored_lines: Optional[Set[int]] = None,
    char_table: Optional[dict[int, str]] = None,
    ambiguity_mode: str = "strict",
) -> tuple[str, List[tuple[Match, int, int]]]:
    """
    Convert text using matcher.

    Args:
        text: Text to process.
        matcher: Matcher instance.
        fix: Whether to apply fixes.
        ignored_lines: Set of line numbers to skip.
        char_table: Character-level translate table (str.translate format).
        ambiguity_mode: 歧義處理模式，"strict"（預設）或 "balanced"。

    Returns:
        Tuple of (processed_text, list of (match, line, col)).
    """
    if ambiguity_mode not in VALID_AMBIGUITY_MODES:
        raise ValueError(
            f"Invalid ambiguity_mode: {ambiguity_mode!r}. "
            f"Valid modes are: {sorted(VALID_AMBIGUITY_MODES)}"
        )

    if ignored_lines is None:
        ignored_lines = set()

    # 單次 automaton 掃描：matches 供回報，covered 供字元層跳過。
    # 舊版在這裡 + _apply_conversion_layers + _find_balanced_matches
    # 共跑 3 次掃描，automaton.iter 是整條管線的主要成本。
    scan_matches, covered_positions = matcher.scan(text)

    # 行號索引（與 Matcher.find_matches_with_lines 等價，但重用同一次掃描）
    line_starts = [0]
    for i, ch in enumerate(text):
        if ch == "\n":
            line_starts.append(i + 1)

    all_matches = []
    for m in scan_matches:
        li = bisect_right(line_starts, m.start) - 1
        all_matches.append((m, li + 1, m.start - line_starts[li] + 1))

    # Filter out matches on ignored lines
    matches = [(m, line, col) for m, line, col in all_matches if line not in ignored_lines]

    if fix and (matches or char_table or ambiguity_mode == "balanced"):
        text = _replace_with_ignores(
            text,
            matcher,
            ignored_lines,
            char_table,
            ambiguity_mode,
            scan=(scan_matches, covered_positions),
        )

    # In check mode, also detect char-level and balanced-level conversions
    if not fix:
        if char_table:
            char_matches = _find_char_matches(
                text,
                char_table,
                ignored_lines,
                covered_positions=covered_positions,
            )
            matches = matches + char_matches
        if ambiguity_mode == "balanced":
            balanced_matches = _find_balanced_matches(
                text, matcher, ignored_lines, covered=covered_positions
            )
            matches = matches + balanced_matches

    return text, matches


# Lazy-cached (matcher, char_table) pairs for convert() convenience wrapper.
# Keyed by normalised sources tuple so repeated calls reuse the build cost.
# Guarded by _DEFAULT_CONVERT_LOCK so concurrent first-time calls don't
# redundantly build multiple Aho-Corasick automata (or race the dict write).
_DEFAULT_CONVERT_CACHE: dict = {}
_DEFAULT_CONVERT_LOCK = threading.Lock()


def convert(text: str, sources: Optional[List[str]] = None, ambiguity_mode: str = "strict") -> str:
    """Convert Simplified/HK Traditional Chinese to Taiwan Traditional Chinese.

    High-level convenience wrapper that loads the default dictionary and
    character table on first call, caches them, and returns converted text.
    Use this for one-liner conversions; for hot loops or custom dictionaries,
    build a :class:`Matcher` once and call :func:`convert_text` directly.

    Args:
        text: Input text. May contain Simplified Chinese (e.g. "软件"),
            HK Traditional variants (e.g. "軟件"), Taiwan Traditional, or
            any mix. Non-Chinese content passes through unchanged.
        sources: Which built-in dictionaries to load. Accepted values:

            * ``None`` (default) — load every built-in source; equivalent
              to ``["cn", "hk"]``. Also loads the character-level CN→TW
              translation table.
            * ``["cn"]`` — Simplified Chinese only (vocabulary layer +
              character layer).
            * ``["hk"]`` — HK Traditional vocabulary only (no char table).
            * ``["cn", "hk"]`` — both, same as ``None``.

    Returns:
        Converted text (Taiwan Traditional Chinese). Returns a new string;
        the input is never mutated.

    Raises:
        ValueError: If ``sources`` is an empty list, or contains any value
            other than ``"cn"`` or ``"hk"``. The valid set is exposed as
            :data:`VALID_SOURCES`. Pass ``None`` (or omit the argument) to
            load every built-in source.

    Thread Safety:
        Safe for concurrent calls from multiple threads. The first call
        for a given ``sources`` key builds the underlying :class:`Matcher`
        under a lock; subsequent calls reuse the cached instance. The
        :class:`Matcher` itself is read-only after construction, so
        ``convert()`` can be called concurrently without additional
        synchronisation.

    Example:
        >>> from zhtw import convert
        >>> convert("这个软件需要优化")
        '這個軟體需要最佳化'
        >>> convert("軟件", sources=["hk"])
        '軟體'

    See Also:
        :func:`convert_text` — lower-level API that takes a pre-built
        :class:`Matcher` and reports per-match positions.

        :func:`zhtw.dictionary.load_dictionary` — load raw term mappings
        without the Aho-Corasick matcher.

        :class:`zhtw.Matcher` — reusable matcher for custom pipelines.
    """
    if sources is not None:
        if not sources:
            raise ValueError(
                "sources must be None or a non-empty list. "
                f"Valid sources are: {sorted(VALID_SOURCES)}"
            )
        invalid = sorted({s for s in sources if s not in VALID_SOURCES})
        if invalid:
            raise ValueError(
                f"Invalid source(s): {invalid}. Valid sources are: {sorted(VALID_SOURCES)}"
            )

    if ambiguity_mode not in VALID_AMBIGUITY_MODES:
        raise ValueError(
            f"Invalid ambiguity_mode: {ambiguity_mode!r}. "
            f"Valid modes are: {sorted(VALID_AMBIGUITY_MODES)}"
        )

    key = tuple(sorted(sources)) if sources else None
    cached = _DEFAULT_CONVERT_CACHE.get(key)
    if cached is None:
        with _DEFAULT_CONVERT_LOCK:
            # Double-checked: another thread may have populated the cache
            # while we were waiting for the lock.
            cached = _DEFAULT_CONVERT_CACHE.get(key)
            if cached is None:
                terms = load_dictionary(sources=sources)
                inject_protect_terms(terms, sources)
                if sources is None or "cn" in sources:
                    from .charconv import get_translate_table

                    char_table = get_translate_table()
                else:
                    char_table = None
                matcher = Matcher(terms)
                cached = (matcher, char_table)
                _DEFAULT_CONVERT_CACHE[key] = cached

    matcher, char_table = cached
    # balanced defaults are CN→TW mappings; disable when cn not in sources
    effective_mode = ambiguity_mode
    if ambiguity_mode == "balanced" and sources is not None and "cn" not in sources:
        effective_mode = "strict"
    result, _ = convert_text(
        text, matcher, fix=True, char_table=char_table, ambiguity_mode=effective_mode
    )
    return result


def _find_char_matches(
    text: str,
    char_table: dict[int, str],
    ignored_lines: Set[int],
    covered_positions: Optional[set[int]] = None,
) -> List[tuple[Match, int, int]]:
    """Find characters that would be converted by char_table (for check mode)."""
    results: List[tuple[Match, int, int]] = []
    if covered_positions is None:
        covered_positions = set()
    lines = text.split("\n")
    pos = 0
    for i, line in enumerate(lines):
        line_num = i + 1
        if line_num not in ignored_lines:
            for col_idx, ch in enumerate(line):
                cp = ord(ch)
                abs_pos = pos + col_idx
                if abs_pos in covered_positions:
                    continue
                if cp in char_table and char_table[cp] != ch:
                    m = Match(
                        start=abs_pos,
                        end=abs_pos + 1,
                        source=ch,
                        target=char_table[cp],
                    )
                    results.append((m, line_num, col_idx + 1))
        pos += len(line) + 1  # +1 for newline
    return results


def _find_balanced_matches(
    text: str,
    matcher: Matcher,
    ignored_lines: Set[int],
    covered: Optional[set[int]] = None,
) -> List[tuple[Match, int, int]]:
    """Find chars that would be converted by balanced defaults (for check mode).

    Args:
        covered: 預先計算的 covered positions；None 則自行掃描。
    """
    from .charconv import get_balanced_defaults

    defaults = get_balanced_defaults()
    if not defaults:
        return []

    if covered is None:
        covered = matcher.get_covered_positions(text)
    results: List[tuple[Match, int, int]] = []
    lines = text.split("\n")
    pos = 0
    for i, line in enumerate(lines):
        line_num = i + 1
        if line_num not in ignored_lines:
            for col_idx, ch in enumerate(line):
                if ch in defaults and (pos + col_idx) not in covered:
                    m = Match(
                        start=pos + col_idx,
                        end=pos + col_idx + 1,
                        source=ch,
                        target=defaults[ch],
                    )
                    results.append((m, line_num, col_idx + 1))
        pos += len(line) + 1
    return results


def _replace_with_ignores(
    text: str,
    matcher: Matcher,
    ignored_lines: Set[int],
    char_table: Optional[dict[int, str]] = None,
    ambiguity_mode: str = "strict",
    scan: Optional[tuple[List[Match], set[int]]] = None,
) -> str:
    """Replace matches while respecting ignored lines.

    Args:
        scan: 預先計算的整段 ``matcher.scan(text)``。只在無 ignored_lines
            的快路徑重用；逐行路徑因座標系不同仍逐行掃描。
    """
    if not ignored_lines:
        return _apply_conversion_layers(text, matcher, char_table, ambiguity_mode, scan=scan)

    lines = text.split("\n")
    result_lines = []

    for i, line in enumerate(lines):
        line_num = i + 1
        if line_num in ignored_lines:
            result_lines.append(line)
        else:
            result_lines.append(_apply_conversion_layers(line, matcher, char_table, ambiguity_mode))

    return "\n".join(result_lines)


_FILE_API = frozenset({"convert_file", "convert_directory", "process_directory"})


def __getattr__(name: str):
    """Lazily expose the historical file API without a module import cycle."""
    if name not in _FILE_API:
        raise AttributeError(name)
    from . import file_converter

    value = getattr(file_converter, name)
    globals()[name] = value
    return value
