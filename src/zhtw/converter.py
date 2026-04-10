"""
Converter module for processing files and text.

Supports:
- Single file processing
- Directory scanning with parallel processing
- Pre-filtering (skip non-Chinese files)
- .zhtwignore file support
"""

from __future__ import annotations

import fnmatch
import re
import threading
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Iterator, List, Optional, Set

from .dictionary import load_dictionary
from .encoding import EncodingInfo, read_file, write_file
from .matcher import Match, Matcher

# Valid values for the `sources` argument of `convert()`.
# Keeping this in sync with the subdirectories under `src/zhtw/data/terms/`.
VALID_SOURCES: frozenset = frozenset({"cn", "hk"})

# Valid values for the `ambiguity_mode` argument.
VALID_AMBIGUITY_MODES: frozenset = frozenset({"strict", "balanced"})

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

    covered: set[int] = set()
    # Collect covered positions from ALL automaton hits, including identity
    # mappings that find_matches() would normally filter out.
    for end_pos, (source, _target) in matcher.automaton.iter(text):
        start_pos = end_pos - len(source) + 1
        covered.update(range(start_pos, end_pos + 1))

    replaced = matcher.replace_all(text)
    return replaced, covered


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

    all_matches = list(matcher.find_matches_with_lines(text))

    # Filter out matches on ignored lines
    matches = [(m, line, col) for m, line, col in all_matches if line not in ignored_lines]

    if fix and (matches or char_table or ambiguity_mode == "balanced"):
        text = _replace_with_ignores(text, matcher, ignored_lines, char_table, ambiguity_mode)

    # In check mode, also detect char-level and balanced-level conversions
    if not fix:
        if char_table:
            char_matches = _find_char_matches(text, char_table, ignored_lines)
            matches = matches + char_matches
        if ambiguity_mode == "balanced":
            balanced_matches = _find_balanced_matches(text, matcher, ignored_lines)
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
                f"Invalid source(s): {invalid}. " f"Valid sources are: {sorted(VALID_SOURCES)}"
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
                matcher = Matcher(terms)
                char_table = None
                if sources is None or "cn" in sources:
                    from .charconv import get_translate_table

                    char_table = get_translate_table()
                cached = (matcher, char_table)
                _DEFAULT_CONVERT_CACHE[key] = cached

    matcher, char_table = cached
    result, _ = convert_text(
        text, matcher, fix=True, char_table=char_table, ambiguity_mode=ambiguity_mode
    )
    return result


def _find_char_matches(
    text: str,
    char_table: dict[int, str],
    ignored_lines: Set[int],
) -> List[tuple[Match, int, int]]:
    """Find characters that would be converted by char_table (for check mode)."""
    results: List[tuple[Match, int, int]] = []
    lines = text.split("\n")
    pos = 0
    for i, line in enumerate(lines):
        line_num = i + 1
        if line_num not in ignored_lines:
            for col_idx, ch in enumerate(line):
                cp = ord(ch)
                if cp in char_table and char_table[cp] != ch:
                    m = Match(
                        start=pos + col_idx,
                        end=pos + col_idx + 1,
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
) -> List[tuple[Match, int, int]]:
    """Find chars that would be converted by balanced defaults (for check mode)."""
    from .charconv import get_balanced_defaults

    defaults = get_balanced_defaults()
    if not defaults:
        return []

    _, covered = _apply_term_layer(text, matcher)
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
) -> str:
    """Replace matches while respecting ignored lines."""
    is_balanced = ambiguity_mode == "balanced"
    if is_balanced:
        from .charconv import apply_balanced_defaults

    if not ignored_lines:
        result, covered = _apply_term_layer(text, matcher)
        if is_balanced:
            result = apply_balanced_defaults(result, covered)
        if char_table:
            result = result.translate(char_table)
        return result

    # Process line by line
    lines = text.split("\n")
    result_lines = []

    # Compute per-line character offsets in the original text so we can
    # build line-level covered_positions (relative to each line's start).
    line_offsets: list[int] = []
    offset = 0
    for line in lines:
        line_offsets.append(offset)
        offset += len(line) + 1  # +1 for the "\n" separator

    # Build full-text covered positions from the full-text term layer so that
    # line-level balanced application uses correct positions.
    if is_balanced:
        _, full_covered = _apply_term_layer(text, matcher)
    else:
        full_covered = set()

    for i, line in enumerate(lines):
        line_num = i + 1
        if line_num in ignored_lines:
            # Keep line as-is
            result_lines.append(line)
        else:
            # Replace matches in this line, then apply balanced/char-level conversion
            converted = matcher.replace_all(line)
            if is_balanced:
                line_start = line_offsets[i]
                line_end = line_start + len(line)
                line_covered = {p - line_start for p in full_covered if line_start <= p < line_end}
                converted = apply_balanced_defaults(converted, line_covered)
            if char_table:
                converted = converted.translate(char_table)
            result_lines.append(converted)

    return "\n".join(result_lines)


def convert_file(
    path: Path,
    matcher: Matcher,
    fix: bool = False,
    input_encoding: str | None = None,
    output_encoding: str = "auto",
    char_table: Optional[dict[int, str]] = None,
    ambiguity_mode: str = "strict",
) -> FileResult:
    """
    Process a single file.

    Args:
        path: File to process.
        matcher: Matcher instance.
        fix: Whether to apply fixes.
        input_encoding: Input encoding (None or "auto" for auto-detect).
        output_encoding: Output encoding strategy ("auto", "utf-8", "keep").

    Returns:
        FileResult with issues found.
    """
    result = FileResult(file=path)

    try:
        content, encoding_info = read_file(path, encoding=input_encoding)
        result.encoding_info = encoding_info
    except UnicodeDecodeError as e:
        result.error = f"Encoding error: {e}"
        result.skipped = True
        return result
    except Exception as e:
        result.error = str(e)
        return result

    # Skip files without Chinese characters
    if not contains_chinese(content):
        result.skipped = True
        return result

    # Check if encoding conversion is needed
    if encoding_info.needs_conversion:
        result.encoding_converted = True

    # Parse ignore directives
    ignored_lines = get_ignored_lines(content)

    # Find matches
    new_content, matches = convert_text(
        content,
        matcher,
        fix=fix,
        ignored_lines=ignored_lines,
        char_table=char_table,
        ambiguity_mode=ambiguity_mode,
    )

    # Build issues list
    for match, line, col in matches:
        context = get_context(content, match.start, match.end)
        result.issues.append(
            Issue(
                file=path,
                line=line,
                column=col,
                source=match.source,
                target=match.target,
                context=context,
            )
        )

    # Write back if fixed and content actually changed
    if fix and new_content != content:
        try:
            used_encoding = write_file(
                path,
                new_content,
                output_encoding=output_encoding,
                original_info=encoding_info,
            )
            result.modified = True
            result.output_encoding = used_encoding
            if used_encoding != encoding_info.encoding:
                result.encoding_converted = True
        except UnicodeEncodeError as e:
            result.error = f"Cannot encode with {output_encoding}: {e}"
        except Exception as e:
            result.error = f"Failed to write: {e}"

    return result


# Type for progress callback: (current, total) -> None
ProgressCallback = Callable[[int, int], None]


def convert_directory(
    path: Path,
    matcher: Matcher,
    fix: bool = False,
    extensions: Optional[Set[str]] = None,
    excludes: Optional[Set[str]] = None,
    workers: Optional[int] = None,
    on_progress: Optional[ProgressCallback] = None,
    input_encoding: str | None = None,
    output_encoding: str = "auto",
    char_table: Optional[dict[int, str]] = None,
    ambiguity_mode: str = "strict",
) -> Iterator[FileResult]:
    """
    Process files in a directory or a single file.

    Args:
        path: Directory to scan or single file to process.
        matcher: Matcher instance.
        fix: Whether to apply fixes.
        extensions: Allowed file extensions.
        excludes: Directory names to exclude.
        workers: Number of parallel workers.
        on_progress: Callback for progress updates (current, total).
        input_encoding: Input encoding (None or "auto" for auto-detect).
        output_encoding: Output encoding strategy.

    Yields:
        FileResult for each processed file.
    """
    # Handle single file
    if path.is_file():
        if should_check_file(path, extensions, excludes):
            if on_progress:
                on_progress(1, 1)
            yield convert_file(
                path,
                matcher,
                fix=fix,
                input_encoding=input_encoding,
                output_encoding=output_encoding,
                char_table=char_table,
                ambiguity_mode=ambiguity_mode,
            )
        return

    # Handle directory
    base_dir = path
    ignore_patterns = load_zhtwignore(base_dir)

    # Collect files to process
    files = [
        f
        for f in base_dir.rglob("*")
        if f.is_file()
        and should_check_file(f, extensions, excludes)
        and not is_ignored_by_patterns(f, base_dir, ignore_patterns)
    ]

    total = len(files)

    for i, file_path in enumerate(files):
        if on_progress:
            on_progress(i + 1, total)
        yield convert_file(
            file_path,
            matcher,
            fix=fix,
            input_encoding=input_encoding,
            output_encoding=output_encoding,
            char_table=char_table,
            ambiguity_mode=ambiguity_mode,
        )


def process_directory(
    path: Path,
    sources: Optional[List[str]] = None,
    custom_dict: Optional[Path] = None,
    fix: bool = False,
    extensions: Optional[Set[str]] = None,
    excludes: Optional[Set[str]] = None,
    on_progress: Optional[ProgressCallback] = None,
    input_encoding: str | None = None,
    output_encoding: str = "auto",
    char_convert: bool = True,
    ambiguity_mode: str = "strict",
) -> ConversionResult:
    """
    Process a directory or single file and return aggregated results.

    Args:
        path: Directory to scan or single file to process.
        sources: Sources to use ("cn", "hk").
        custom_dict: Path to custom dictionary.
        fix: Whether to apply fixes.
        extensions: Allowed file extensions.
        excludes: Directory names to exclude.
        on_progress: Callback for progress updates (current, total).
        input_encoding: Input encoding (None or "auto" for auto-detect).
        output_encoding: Output encoding strategy.
        char_convert: Whether to apply character-level conversion.

    Returns:
        Aggregated ConversionResult.
    """
    # Load dictionary and create matcher
    terms = load_dictionary(sources=sources, custom_path=custom_dict)
    matcher = Matcher(terms)

    # Load character-level conversion table
    char_table = None
    if char_convert and sources and "cn" in sources:
        from .charconv import get_translate_table

        char_table = get_translate_table()

    result = ConversionResult()

    for file_result in convert_directory(
        path,
        matcher,
        fix=fix,
        extensions=extensions,
        excludes=excludes,
        on_progress=on_progress,
        input_encoding=input_encoding,
        output_encoding=output_encoding,
        char_table=char_table,
        ambiguity_mode=ambiguity_mode,
    ):
        if file_result.skipped:
            result.files_skipped += 1
            continue

        result.files_checked += 1

        if file_result.issues:
            result.files_with_issues += 1
            result.total_issues += len(file_result.issues)
            result.issues.extend(file_result.issues)

        if file_result.modified:
            result.files_modified += 1

        if file_result.encoding_converted:
            result.encoding_conversions += 1

        # Track files that need encoding conversion but weren't fixed
        if file_result.encoding_info and file_result.encoding_info.needs_conversion and not fix:
            result.files_needing_conversion.append(file_result.file)

    return result
