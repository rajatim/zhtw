"""Presentation and environment helpers for the Click CLI."""

import json
import os
import sys
from pathlib import Path
from typing import Callable, List

import click

from .converter import ConversionResult, Issue


def get_env_bool(name: str, default: bool = False) -> bool:
    """Get boolean value from environment variable."""
    val = os.environ.get(name, "").lower()
    if val in ("1", "true", "yes"):
        return True
    if val in ("0", "false", "no"):
        return False
    return default


def get_env_str(name: str, default: str | None = None) -> str | None:
    """Get string value from environment variable."""
    return os.environ.get(name, default) or default


class ProgressDisplay:
    """
    Progress display handler for TTY and non-TTY environments.

    TTY: Dynamic progress bar with carriage return
    Non-TTY (CI/Jenkins): Static progress lines at intervals
    """

    def __init__(self, enabled: bool = True, prefix: str = "掃描中"):
        self.enabled = enabled
        self.prefix = prefix
        self.is_tty = sys.stderr.isatty()
        self._last_percent = -1

    def update(self, current: int, total: int) -> None:
        """Update progress display."""
        if not self.enabled or total == 0:
            return

        percent = (current * 100) // total

        if self.is_tty:
            # Dynamic progress bar for TTY
            bar_width = 30
            filled = (current * bar_width) // total
            bar = "█" * filled + "░" * (bar_width - filled)
            click.echo(f"\r{self.prefix} [{bar}] {current}/{total}", nl=False, err=True)
            if current >= total:
                click.echo(err=True)  # New line at end
        else:
            # Static progress for non-TTY (Jenkins, CI)
            # Only print at 0%, 25%, 50%, 75%, 100%
            if percent in (0, 25, 50, 75, 100) and percent != self._last_percent:
                click.echo(f"{self.prefix}... {percent}% ({current}/{total})", err=True)
                self._last_percent = percent

    def finish(self) -> None:
        """Ensure clean line ending."""
        if self.is_tty and self.enabled:
            # Ensure we're on a new line
            pass  # update() already handles this


def create_progress_callback(
    enabled: bool = True, prefix: str = "掃描中"
) -> tuple[Callable[[int, int], None], ProgressDisplay]:
    """
    Create a progress callback function.

    Returns:
        Tuple of (callback function, display instance).
    """
    display = ProgressDisplay(enabled=enabled, prefix=prefix)
    return display.update, display


def format_issue(issue: Issue, show_context: bool = True) -> str:
    """Format an issue for console output."""
    location = f"L{issue.line}:{issue.column}"
    change = f'"{issue.source}" → "{issue.target}"'

    if show_context:
        return f"   {location}: {change}\n      {issue.context}"
    return f"   {location}: {change}"


def create_backup(files: List[Path], base_path: Path) -> Path:
    """
    Create backup of files before modification.

    Args:
        files: List of file paths to backup.
        base_path: Base directory for backup.

    Returns:
        Path to backup directory.
    """
    import shutil
    from datetime import datetime

    # Create backup directory with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = base_path / ".zhtw-backup" / timestamp

    for file_path in files:
        try:
            rel_path = file_path.relative_to(base_path)
        except ValueError:
            rel_path = file_path.name

        dest = backup_dir / rel_path
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file_path, dest)

    return backup_dir


def check_git_status(path: Path) -> bool:
    """Check if path is in a git repository with clean status."""
    import subprocess

    try:
        # Check if in git repo
        result = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            cwd=path if path.is_dir() else path.parent,
            capture_output=True,
            text=True,
        )
        return result.returncode == 0
    except Exception:
        return False


def format_diff(result: ConversionResult) -> str:
    """Format issues as a diff-like output."""
    output_lines = []

    # Group issues by file
    issues_by_file: dict[Path, List[Issue]] = {}
    for issue in result.issues:
        if issue.file not in issues_by_file:
            issues_by_file[issue.file] = []
        issues_by_file[issue.file].append(issue)

    for file_path, issues in sorted(issues_by_file.items()):
        output_lines.append(f"\n📄 {file_path}")

        # Group by line for cleaner output
        issues_by_line: dict[int, List[Issue]] = {}
        for issue in issues:
            if issue.line not in issues_by_line:
                issues_by_line[issue.line] = []
            issues_by_line[issue.line].append(issue)

        for line_num in sorted(issues_by_line.keys()):
            line_issues = issues_by_line[line_num]
            # Get original context from first issue
            original = line_issues[0].context

            # Build the modified version
            modified = original
            for issue in line_issues:
                modified = modified.replace(issue.source, issue.target)

            output_lines.append(click.style(f"   L{line_num}:", fg="cyan"))
            output_lines.append(click.style(f"   - {original.strip()}", fg="red"))
            output_lines.append(click.style(f"   + {modified.strip()}", fg="green"))

    return "\n".join(output_lines)


def print_results(result: ConversionResult, verbose: bool = False) -> None:
    """Print results to console."""
    # Group issues by file
    issues_by_file: dict[Path, List[Issue]] = {}
    for issue in result.issues:
        if issue.file not in issues_by_file:
            issues_by_file[issue.file] = []
        issues_by_file[issue.file].append(issue)

    # Print issues grouped by file
    for file_path, issues in sorted(issues_by_file.items()):
        click.echo(f"\n📄 {file_path}")
        for issue in sorted(issues, key=lambda i: (i.line, i.column)):
            click.echo(format_issue(issue, show_context=verbose))

    # Print summary
    click.echo()
    click.echo("━" * 50)

    if result.files_modified > 0:
        click.echo(
            click.style(
                f"✅ 已修正 {result.files_modified} 個檔案 ({result.total_issues} 處)",
                fg="green",
            )
        )
    elif result.total_issues > 0:
        click.echo(
            click.style(
                f"⚠️  發現 {result.total_issues} 處問題 （{result.files_with_issues} 個檔案）",
                fg="yellow",
            )
        )
    else:
        click.echo(click.style("✅ 檢查完成：未發現問題", fg="green"))

    click.echo(
        f"   掃描: {result.files_checked} 個檔案 "
        f"(跳過 {result.files_skipped} 個無中文檔案)"  # zhtw:disable-line
    )

    # Show encoding conversion info
    if result.encoding_conversions > 0:
        click.echo(
            click.style(
                f"   編碼轉換: {result.encoding_conversions} 個檔案 → UTF-8",
                fg="cyan",
            )
        )

    # Warn about files needing encoding conversion (check mode)
    if result.files_needing_conversion:
        click.echo()
        click.echo(
            click.style(
                f"⚠️  {len(result.files_needing_conversion)} 個檔案使用非 Unicode 編碼：",
                fg="yellow",
            )
        )
        for f in result.files_needing_conversion[:5]:
            click.echo(f"   - {f}")
        if len(result.files_needing_conversion) > 5:
            click.echo(f"   ... 還有 {len(result.files_needing_conversion) - 5} 個")
        click.echo("   使用 --output-encoding utf-8 轉換為 UTF-8")


def print_json(result: ConversionResult) -> None:
    """Print results as JSON."""
    output = {
        "total_issues": result.total_issues,
        "files_with_issues": result.files_with_issues,
        "files_checked": result.files_checked,
        "files_modified": result.files_modified,
        "files_skipped": result.files_skipped,
        "encoding_conversions": result.encoding_conversions,
        "status": "pass" if result.total_issues == 0 else "fail",
        "issues": [
            {
                "file": str(issue.file),
                "line": issue.line,
                "column": issue.column,
                "source": issue.source,
                "target": issue.target,
            }
            for issue in result.issues
        ],
    }
    if result.files_needing_conversion:
        output["files_needing_encoding_conversion"] = [
            str(f) for f in result.files_needing_conversion
        ]
    click.echo(json.dumps(output, ensure_ascii=False, indent=2))
