"""File and directory orchestration for the Python converter."""

from pathlib import Path
from typing import Callable, Iterator, List, Optional, Set

from .converter import (
    VALID_AMBIGUITY_MODES,
    ConversionResult,
    FileResult,
    Issue,
    contains_chinese,
    convert_text,
    get_context,
    get_ignored_lines,
    inject_protect_terms,
    is_ignored_by_patterns,
    load_zhtwignore,
    should_check_file,
)
from .dictionary import load_dictionary
from .encoding import read_file, write_file
from .matcher import Matcher


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
    if ambiguity_mode not in VALID_AMBIGUITY_MODES:
        raise ValueError(
            f"Invalid ambiguity_mode: {ambiguity_mode!r}. "
            f"Valid modes are: {sorted(VALID_AMBIGUITY_MODES)}"
        )

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
        workers: 保留參數，目前未使用（實作為循序處理）。
            歷史上文件宣稱平行處理但從未實作；保留簽名以維持
            向後相容，未來實作平行化時沿用。
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
    if ambiguity_mode not in VALID_AMBIGUITY_MODES:
        raise ValueError(
            f"Invalid ambiguity_mode: {ambiguity_mode!r}. "
            f"Valid modes are: {sorted(VALID_AMBIGUITY_MODES)}"
        )

    # Load dictionary and create matcher
    terms = load_dictionary(sources=sources, custom_path=custom_dict)
    inject_protect_terms(terms, sources)
    matcher = Matcher(terms)

    # Load character-level conversion table.
    # sources=None means "all sources" (which includes cn) — must match
    # convert()'s semantics, otherwise the char layer silently turns off
    # for API callers that rely on the default.
    char_table = None
    if char_convert and (sources is None or "cn" in sources):
        from .charconv import get_translate_table

        char_table = get_translate_table()

    # balanced defaults are CN→TW mappings; disable when cn not in sources
    effective_mode = ambiguity_mode
    if ambiguity_mode == "balanced" and sources is not None and "cn" not in sources:
        effective_mode = "strict"

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
        ambiguity_mode=effective_mode,
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
