"""
Converter module for processing files and text.

Supports:
- Single file processing
- Directory scanning with parallel processing
- Pre-filtering (skip non-Chinese files)
"""

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator, List, Optional, Set

from .dictionary import load_dictionary
from .matcher import Match, Matcher

# Regex to detect Chinese characters
CHINESE_PATTERN = re.compile(r"[\u4e00-\u9fff]")

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
}

# Default files to exclude
DEFAULT_EXCLUDE_FILES: Set[str] = {
    "package-lock.json",
    "yarn.lock",
    "pnpm-lock.yaml",
    "Cargo.lock",
}


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


@dataclass
class ConversionResult:
    """Result of processing multiple files."""

    files_checked: int = 0
    files_with_issues: int = 0
    files_modified: int = 0
    files_skipped: int = 0
    total_issues: int = 0
    issues: List[Issue] = field(default_factory=list)


def contains_chinese(text: str) -> bool:
    """Check if text contains any Chinese characters."""
    return bool(CHINESE_PATTERN.search(text))


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
) -> tuple[str, List[tuple[Match, int, int]]]:
    """
    Convert text using matcher.

    Args:
        text: Text to process.
        matcher: Matcher instance.
        fix: Whether to apply fixes.

    Returns:
        Tuple of (processed_text, list of (match, line, col)).
    """
    matches = list(matcher.find_matches_with_lines(text))

    if fix and matches:
        text = matcher.replace_all(text)

    return text, matches


def convert_file(
    path: Path,
    matcher: Matcher,
    fix: bool = False,
) -> FileResult:
    """
    Process a single file.

    Args:
        path: File to process.
        matcher: Matcher instance.
        fix: Whether to apply fixes.

    Returns:
        FileResult with issues found.
    """
    result = FileResult(file=path)

    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        result.skipped = True
        return result
    except Exception as e:
        result.error = str(e)
        return result

    # Skip files without Chinese characters
    if not contains_chinese(content):
        result.skipped = True
        return result

    # Find matches
    new_content, matches = convert_text(content, matcher, fix=fix)

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
            path.write_text(new_content, encoding="utf-8")
            result.modified = True
        except Exception as e:
            result.error = f"Failed to write: {e}"

    return result


def convert_directory(
    directory: Path,
    matcher: Matcher,
    fix: bool = False,
    extensions: Optional[Set[str]] = None,
    excludes: Optional[Set[str]] = None,
    workers: Optional[int] = None,
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

    Yields:
        FileResult for each processed file.
    """
    # Collect files to process
    files = [
        f
        for f in directory.rglob("*")
        if f.is_file() and should_check_file(f, extensions, excludes)
    ]

    # Process files (single-threaded for now to avoid pickle issues with Matcher)
    # TODO: Implement proper parallel processing
    for file_path in files:
        yield convert_file(file_path, matcher, fix=fix)


def process_directory(
    directory: Path,
    sources: Optional[List[str]] = None,
    custom_dict: Optional[Path] = None,
    fix: bool = False,
    extensions: Optional[Set[str]] = None,
    excludes: Optional[Set[str]] = None,
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

    Returns:
        Aggregated ConversionResult.
    """
    # Load dictionary and create matcher
    terms = load_dictionary(sources=sources, custom_path=custom_dict)
    matcher = Matcher(terms)

    result = ConversionResult()

    for file_result in convert_directory(
        directory, matcher, fix=fix, extensions=extensions, excludes=excludes
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

    return result
