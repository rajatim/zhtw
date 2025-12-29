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
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Iterator, List, Optional, Set

from .dictionary import load_dictionary
from .encoding import EncodingInfo, read_file, write_file
from .matcher import Match, Matcher

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


def convert_text(
    text: str,
    matcher: Matcher,
    fix: bool = False,
    ignored_lines: Optional[Set[int]] = None,
) -> tuple[str, List[tuple[Match, int, int]]]:
    """
    Convert text using matcher.

    Args:
        text: Text to process.
        matcher: Matcher instance.
        fix: Whether to apply fixes.
        ignored_lines: Set of line numbers to skip.

    Returns:
        Tuple of (processed_text, list of (match, line, col)).
    """
    if ignored_lines is None:
        ignored_lines = set()

    all_matches = list(matcher.find_matches_with_lines(text))

    # Filter out matches on ignored lines
    matches = [(m, line, col) for m, line, col in all_matches if line not in ignored_lines]

    if fix and matches:
        # Only replace non-ignored matches
        # We need to do this carefully to preserve ignored content
        text = _replace_with_ignores(text, matcher, ignored_lines)

    return text, matches


def _replace_with_ignores(text: str, matcher: Matcher, ignored_lines: Set[int]) -> str:
    """Replace matches while respecting ignored lines."""
    if not ignored_lines:
        return matcher.replace_all(text)

    # Process line by line
    lines = text.split("\n")
    result_lines = []

    for i, line in enumerate(lines):
        line_num = i + 1
        if line_num in ignored_lines:
            # Keep line as-is
            result_lines.append(line)
        else:
            # Replace matches in this line
            result_lines.append(matcher.replace_all(line))

    return "\n".join(result_lines)


def convert_file(
    path: Path,
    matcher: Matcher,
    fix: bool = False,
    input_encoding: str | None = None,
    output_encoding: str = "auto",
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
    new_content, matches = convert_text(content, matcher, fix=fix, ignored_lines=ignored_lines)

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

    # Write back if fixed
    if fix and matches:
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
    directory: Path,
    matcher: Matcher,
    fix: bool = False,
    extensions: Optional[Set[str]] = None,
    excludes: Optional[Set[str]] = None,
    workers: Optional[int] = None,
    on_progress: Optional[ProgressCallback] = None,
    input_encoding: str | None = None,
    output_encoding: str = "auto",
) -> Iterator[FileResult]:
    """
    Process all files in a directory.

    Args:
        directory: Directory to scan.
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
    # Load .zhtwignore patterns
    ignore_patterns = load_zhtwignore(directory)

    # Collect files to process
    files = [
        f
        for f in directory.rglob("*")
        if f.is_file()
        and should_check_file(f, extensions, excludes)
        and not is_ignored_by_patterns(f, directory, ignore_patterns)
    ]

    total = len(files)

    # Process files (single-threaded for now to avoid pickle issues with Matcher)
    # TODO: Implement proper parallel processing
    for i, file_path in enumerate(files):
        if on_progress:
            on_progress(i + 1, total)
        yield convert_file(
            file_path,
            matcher,
            fix=fix,
            input_encoding=input_encoding,
            output_encoding=output_encoding,
        )


def process_directory(
    directory: Path,
    sources: Optional[List[str]] = None,
    custom_dict: Optional[Path] = None,
    fix: bool = False,
    extensions: Optional[Set[str]] = None,
    excludes: Optional[Set[str]] = None,
    on_progress: Optional[ProgressCallback] = None,
    input_encoding: str | None = None,
    output_encoding: str = "auto",
) -> ConversionResult:
    """
    Process a directory and return aggregated results.

    Args:
        directory: Directory to scan.
        sources: Sources to use ("cn", "hk").
        custom_dict: Path to custom dictionary.
        fix: Whether to apply fixes.
        extensions: Allowed file extensions.
        excludes: Directory names to exclude.
        on_progress: Callback for progress updates (current, total).
        input_encoding: Input encoding (None or "auto" for auto-detect).
        output_encoding: Output encoding strategy.

    Returns:
        Aggregated ConversionResult.
    """
    # Load dictionary and create matcher
    terms = load_dictionary(sources=sources, custom_path=custom_dict)
    matcher = Matcher(terms)

    result = ConversionResult()

    for file_result in convert_directory(
        directory,
        matcher,
        fix=fix,
        extensions=extensions,
        excludes=excludes,
        on_progress=on_progress,
        input_encoding=input_encoding,
        output_encoding=output_encoding,
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
        if (
            file_result.encoding_info
            and file_result.encoding_info.needs_conversion
            and not fix
        ):
            result.files_needing_conversion.append(file_result.file)

    return result
