"""
CLI interface for ZHTW.

Usage:
    zhtw check ./src           # Check mode (report only)
    zhtw fix ./src             # Fix mode (modify files)
    zhtw check ./src --json    # JSON output for CI/CD
    zhtw stats                 # Show dictionary statistics
    zhtw validate              # Validate dictionary quality
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Callable, List, Optional

import click

from . import __version__
from .converter import ConversionResult, Issue, process_directory
from .dictionary import DATA_DIR, load_dictionary, load_json_file


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
                f"✅ 已修正 {result.files_modified} 個檔案 "
                f"({result.total_issues} 處)",
                fg="green",
            )
        )
    elif result.total_issues > 0:
        click.echo(
            click.style(
                f"⚠️  發現 {result.total_issues} 處問題 "
                f"（{result.files_with_issues} 個檔案）",
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


@click.group()
@click.version_option(version=__version__, prog_name="zhtw")
def main():
    """
    🇹🇼 ZHTW - 簡轉繁台灣用語轉換器

    將程式碼和文件中的簡體中文/香港繁體轉換為台灣繁體中文。

    rajatim 出品 ✨
    """
    pass


@main.command()
@click.argument("path", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--source",
    "-s",
    type=str,
    default="cn,hk",
    help="轉換來源: cn (簡體), hk (港式), 或 cn,hk (預設)",
)
@click.option(
    "--dict",
    "-d",
    "custom_dict",
    type=click.Path(exists=True, path_type=Path),
    help="自訂詞庫 JSON 檔案路徑",
)
@click.option(
    "--exclude",
    "-e",
    type=str,
    help="排除的目錄（逗號分隔）",
)
@click.option(
    "--json",
    "json_output",
    is_flag=True,
    help="輸出 JSON 格式（供 CI/CD 使用）",
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="顯示詳細資訊（包含上下文）",
)
@click.option(
    "--encoding",
    "-E",
    type=str,
    default=None,
    help="輸入編碼 (auto=自動偵測，預設)",
)
def check(
    path: Path,
    source: str,
    custom_dict: Optional[Path],
    exclude: Optional[str],
    json_output: bool,
    verbose: bool,
    encoding: Optional[str],
):
    """
    檢查模式：掃描檔案並報告問題，不修改檔案。

    Example:

        zhtw check ./src

        zhtw check ./src --source cn

        zhtw check ./src --json
    """
    sources = [s.strip() for s in source.split(",")]
    excludes = set(e.strip() for e in exclude.split(",")) if exclude else None

    # Get encoding from env if not specified
    input_encoding = encoding or get_env_str("ZHTW_ENCODING")

    if not json_output:
        click.echo(f"📁 掃描 {path}")

    # Create progress callback (disabled for JSON output)
    progress_callback, _ = create_progress_callback(
        enabled=not json_output, prefix="掃描中"
    )

    result = process_directory(
        directory=path,
        sources=sources,
        custom_dict=custom_dict,
        fix=False,
        excludes=excludes,
        on_progress=progress_callback,
        input_encoding=input_encoding,
    )

    if json_output:
        print_json(result)
    else:
        print_results(result, verbose=verbose)

    # Exit with error code if issues found
    sys.exit(1 if result.total_issues > 0 else 0)


@main.command()
@click.argument("path", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--source",
    "-s",
    type=str,
    default="cn,hk",
    help="轉換來源: cn (簡體), hk (港式), 或 cn,hk (預設)",
)
@click.option(
    "--dict",
    "-d",
    "custom_dict",
    type=click.Path(exists=True, path_type=Path),
    help="自訂詞庫 JSON 檔案路徑",
)
@click.option(
    "--exclude",
    "-e",
    type=str,
    help="排除的目錄（逗號分隔）",
)
@click.option(
    "--json",
    "json_output",
    is_flag=True,
    help="輸出 JSON 格式（供 CI/CD 使用）",
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="顯示詳細資訊（包含上下文）",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="模擬執行，不實際修改檔案",
)
@click.option(
    "--show-diff",
    is_flag=True,
    help="顯示修改預覽，確認後才執行",
)
@click.option(
    "--backup",
    is_flag=True,
    help="修改前備份原檔到 .zhtw-backup/",
)
@click.option(
    "--encoding",
    "-E",
    type=str,
    default=None,
    help="輸入編碼 (auto=自動偵測，預設)",
)
@click.option(
    "--output-encoding",
    "-O",
    type=click.Choice(["auto", "utf-8", "keep"]),
    default="auto",
    help="輸出編碼: auto=安全時保留原編碼，utf-8=強制 UTF-8，keep=保留原編碼",
)
@click.option(
    "--yes",
    "-y",
    is_flag=True,
    help="自動確認，不互動（CI/CD 模式）",
)
def fix(
    path: Path,
    source: str,
    custom_dict: Optional[Path],
    exclude: Optional[str],
    json_output: bool,
    verbose: bool,
    dry_run: bool,
    show_diff: bool,
    backup: bool,
    encoding: Optional[str],
    output_encoding: str,
    yes: bool,
):
    """
    修正模式：掃描檔案並自動修正問題。

    Example:

        zhtw fix ./src

        zhtw fix ./src --dry-run

        zhtw fix ./src --show-diff

        zhtw fix ./src --backup

        zhtw fix ./src --source cn

        zhtw fix ./src --output-encoding utf-8
    """
    sources = [s.strip() for s in source.split(",")]
    excludes = set(e.strip() for e in exclude.split(",")) if exclude else None

    # Get values from environment if not specified
    input_encoding = encoding or get_env_str("ZHTW_ENCODING")
    out_encoding = output_encoding or get_env_str("ZHTW_OUTPUT_ENCODING", "auto")
    auto_yes = yes or get_env_bool("ZHTW_YES")

    # Helper function to perform backup if needed
    def do_backup_if_needed(result: ConversionResult) -> None:
        if backup and result.total_issues > 0:
            files_to_backup = list(set(issue.file for issue in result.issues))
            base = path if path.is_dir() else path.parent
            backup_dir = create_backup(files_to_backup, base)
            msg = f"📦 已備份 {len(files_to_backup)} 個檔案到 {backup_dir}"
            click.echo(click.style(msg, fg="cyan"))

    # Warn if not in git and not using backup (only for actual fixes)
    if not dry_run and not backup and not json_output and not auto_yes:
        if not check_git_status(path):
            click.echo(
                click.style(
                    "⚠️  警告：此目錄不在 git 版控下，修改後無法輕易恢復",
                    fg="yellow",
                )
            )
            click.echo("   建議使用 --backup 建立備份，或 --dry-run 先預覽")
            if not click.confirm("確定要繼續？"):
                sys.exit(1)

    # Create progress callback (disabled for JSON output)
    progress_callback, _ = create_progress_callback(
        enabled=not json_output, prefix="掃描中"
    )

    # show_diff implies dry-run first, then fix after confirmation
    if show_diff:
        if not json_output:
            click.echo(f"🔍 預覽模式：掃描 {path}")

        # First pass: check only (don't fix)
        result = process_directory(
            directory=path,
            sources=sources,
            custom_dict=custom_dict,
            fix=False,
            excludes=excludes,
            on_progress=progress_callback,
            input_encoding=input_encoding,
            output_encoding=out_encoding,
        )

        if result.total_issues == 0:
            if json_output:
                print_json(result)
            else:
                click.echo(click.style("\n✅ 未發現需要修正的問題", fg="green"))
            sys.exit(0)

        # Show diff
        if not json_output:
            click.echo(format_diff(result))
            click.echo()
            click.echo("━" * 50)
            click.echo(
                click.style(
                    f"📊 將修正 {result.total_issues} 處問題（{result.files_with_issues} 個檔案）",
                    fg="yellow",
                )
            )

            # Ask for confirmation (skip if --yes)
            if not auto_yes and not click.confirm("\n確認執行修正？"):
                click.echo(click.style("❌ 已取消", fg="red"))
                sys.exit(1)

            # Backup before fixing
            do_backup_if_needed(result)

            # Second pass: actually fix
            click.echo("\n🔧 執行修正...")
            result = process_directory(
                directory=path,
                sources=sources,
                custom_dict=custom_dict,
                fix=True,
                excludes=excludes,
                on_progress=progress_callback,
                input_encoding=input_encoding,
                output_encoding=out_encoding,
            )
            print_results(result, verbose=verbose)
        else:
            print_json(result)
            sys.exit(1 if result.total_issues > 0 else 0)

        sys.exit(0)

    # Normal mode (no show_diff)
    if not json_output:
        mode = "模擬" if dry_run else "修正"
        click.echo(f"🔧 {mode}模式：掃描 {path}")

    # For backup mode without show_diff, we need to check first
    if backup and not dry_run:
        # First pass: check what will be modified
        check_result = process_directory(
            directory=path,
            sources=sources,
            custom_dict=custom_dict,
            fix=False,
            excludes=excludes,
            on_progress=progress_callback,
            input_encoding=input_encoding,
            output_encoding=out_encoding,
        )
        do_backup_if_needed(check_result)

    result = process_directory(
        directory=path,
        sources=sources,
        custom_dict=custom_dict,
        fix=not dry_run,
        excludes=excludes,
        on_progress=progress_callback,
        input_encoding=input_encoding,
        output_encoding=out_encoding,
    )

    if json_output:
        print_json(result)
    else:
        print_results(result, verbose=verbose)

    # Exit with success after fixing (or error if dry-run found issues)
    if dry_run:
        sys.exit(1 if result.total_issues > 0 else 0)
    else:
        sys.exit(0)


@main.command()
@click.option(
    "--source",
    "-s",
    type=str,
    default="cn,hk",
    help="顯示來源: cn (簡體), hk (港式), 或 cn,hk (預設)",
)
@click.option(
    "--json",
    "json_output",
    is_flag=True,
    help="輸出 JSON 格式",
)
def stats(source: str, json_output: bool):
    """
    顯示詞庫統計資訊。

    Example:

        zhtw stats

        zhtw stats --source cn

        zhtw stats --json
    """
    sources = [s.strip() for s in source.split(",")]

    # Collect stats for each source
    stats_data = {"sources": {}, "total_terms": 0}

    for src in sources:
        src_dir = DATA_DIR / src
        if not src_dir.exists():
            continue

        src_stats = {"files": {}, "total": 0}

        for json_file in sorted(src_dir.glob("*.json")):
            terms = load_json_file(json_file)
            count = len(terms)
            src_stats["files"][json_file.stem] = count
            src_stats["total"] += count

        stats_data["sources"][src] = src_stats
        stats_data["total_terms"] += src_stats["total"]

    if json_output:
        click.echo(json.dumps(stats_data, ensure_ascii=False, indent=2))
    else:
        click.echo("📊 ZHTW 詞庫統計\n")
        click.echo("━" * 40)

        for src, src_stats in stats_data["sources"].items():
            src_name = {"cn": "簡體中文", "hk": "香港繁體"}.get(src, src)
            click.echo(f"\n📁 {src_name} ({src}/)")

            for file_name, count in src_stats["files"].items():
                click.echo(f"   {file_name}.json: {count} 個詞彙")

            click.echo(
                click.style(f"   小計: {src_stats['total']} 個詞彙", fg="cyan")
            )

        click.echo("\n" + "━" * 40)
        click.echo(
            click.style(
                f"📈 總計: {stats_data['total_terms']} 個詞彙",
                fg="green",
                bold=True,
            )
        )


@main.command()
@click.option(
    "--source",
    "-s",
    type=str,
    default="cn,hk",
    help="驗證來源: cn (簡體), hk (港式), 或 cn,hk (預設)",
)
def validate(source: str):
    """
    驗證詞庫品質，檢查潛在問題。

    檢查項目：
    - 目標詞彙是否與其他來源詞彙衝突
    - 來源與目標是否相同（無效轉換）
    - 重複的來源詞彙

    Example:

        zhtw validate

        zhtw validate --source cn
    """
    sources = [s.strip() for s in source.split(",")]

    click.echo("🔍 驗證詞庫品質\n")
    click.echo("━" * 50)

    # Load all terms
    all_sources = {}
    all_targets = {}

    for src in sources:
        src_dir = DATA_DIR / src
        if not src_dir.exists():
            continue

        for json_file in src_dir.glob("*.json"):
            terms = load_json_file(json_file)
            for source_term, target_term in terms.items():
                all_sources[source_term] = (src, json_file.stem, target_term)
                if target_term not in all_targets:
                    all_targets[target_term] = []
                all_targets[target_term].append((src, json_file.stem, source_term))

    issues = []

    # Check 1: Target terms that are also source terms (potential false positives)
    click.echo("\n📋 檢查目標詞彙衝突...")
    conflicts = []
    for target, sources_list in all_targets.items():
        if target in all_sources:
            src, file, original_source = all_sources[target]
            conflicts.append(
                f"   ⚠️  「{target}」是 {src}/{file}.json 的目標，"
                f"但也是來源詞彙 → 可能誤轉換"
            )

    if conflicts:
        for c in conflicts[:10]:  # Show max 10
            click.echo(c)
        if len(conflicts) > 10:
            click.echo(f"   ... 還有 {len(conflicts) - 10} 個衝突")
        issues.extend(conflicts)
    else:
        click.echo("   ✅ 無衝突")

    # Check 2: Source equals target (useless conversion)
    click.echo("\n📋 檢查無效轉換（來源=目標）...")
    same_terms = []
    for source_term, (src, file, target_term) in all_sources.items():
        if source_term == target_term:
            same_terms.append(f"   ⚠️  {src}/{file}.json: 「{source_term}」→「{target_term}」")

    if same_terms:
        for s in same_terms[:10]:
            click.echo(s)
        if len(same_terms) > 10:
            click.echo(f"   ... 還有 {len(same_terms) - 10} 個")
        issues.extend(same_terms)
    else:
        click.echo("   ✅ 無無效轉換")

    # Check 3: Duplicate source terms across files
    click.echo("\n📋 檢查重複來源詞彙...")
    source_files = {}
    duplicates = []
    for src in sources:
        src_dir = DATA_DIR / src
        if not src_dir.exists():
            continue

        for json_file in src_dir.glob("*.json"):
            terms = load_json_file(json_file)
            for source_term in terms:
                key = (src, source_term)
                if key in source_files:
                    duplicates.append(
                        f"   ⚠️  {src}/: 「{source_term}」同時出現在 "
                        f"{source_files[key]}.json 和 {json_file.stem}.json"
                    )
                else:
                    source_files[key] = json_file.stem

    if duplicates:
        for d in duplicates[:10]:
            click.echo(d)
        if len(duplicates) > 10:
            click.echo(f"   ... 還有 {len(duplicates) - 10} 個")
        issues.extend(duplicates)
    else:
        click.echo("   ✅ 無重複")

    # Summary
    click.echo("\n" + "━" * 50)
    if issues:
        click.echo(
            click.style(
                f"⚠️  發現 {len(issues)} 個潛在問題",
                fg="yellow",
            )
        )
        sys.exit(1)
    else:
        click.echo(
            click.style(
                "✅ 詞庫驗證通過，無問題",
                fg="green",
            )
        )
        sys.exit(0)


# =============================================================================
# v2.0 Commands: import, review, usage, config
# =============================================================================


@main.command("import")
@click.argument("source", type=str)
@click.option(
    "--no-pending",
    is_flag=True,
    help="直接匯入，跳過暫存審核（不建議）",
)
@click.option(
    "--name",
    "-n",
    type=str,
    help="暫存檔案名稱（預設從來源自動產生）",
)
def import_cmd(source: str, no_pending: bool, name: Optional[str]):
    """
    匯入外部詞庫。

    SOURCE 可以是 URL 或本地檔案路徑。

    Example:

        zhtw import ./external-terms.json

        zhtw import https://example.com/terms.json

        zhtw import ./terms.json --name my-terms
    """
    from .import_terms import ImportError as TermImportError
    from .import_terms import import_terms, save_to_pending

    click.echo(f"📥 匯入詞庫: {source}")

    # Load existing terms for conflict detection
    try:
        existing = load_dictionary(sources=["cn", "hk"])
    except Exception:
        existing = {}

    try:
        result = import_terms(source, existing_terms=existing)
    except TermImportError as e:
        click.echo(click.style(f"❌ 匯入失敗: {e}", fg="red"))
        sys.exit(1)

    click.echo("\n📊 匯入結果:")
    click.echo(f"   總數: {result.total}")
    click.echo(f"   有效: {result.valid}")
    click.echo(f"   無效: {result.invalid}")
    click.echo(f"   重複: {result.duplicates}")
    click.echo(f"   衝突: {result.conflicts}")

    if result.errors and len(result.errors) <= 10:
        click.echo("\n⚠️ 問題詳情:")
        for error in result.errors:
            click.echo(f"   {error}")
    elif result.errors:
        click.echo(f"\n⚠️ 發現 {len(result.errors)} 個問題（顯示前 10 個）:")
        for error in result.errors[:10]:
            click.echo(f"   {error}")

    if result.valid == 0:
        click.echo(click.style("\n❌ 無有效詞彙可匯入", fg="red"))
        sys.exit(1)

    if no_pending:
        # Direct import (not recommended)
        from .review import approve_terms

        path = approve_terms(result.terms)
        click.echo(click.style(f"\n✅ 已直接匯入 {result.valid} 個詞彙到 {path}", fg="green"))
    else:
        # Save to pending
        if not name:
            # Generate name from source
            if source.startswith("http"):
                name = source.split("/")[-1].replace(".json", "")
            else:
                name = Path(source).stem
            name = f"import_{name}"

        path = save_to_pending(result.terms, name)
        click.echo(click.style(f"\n✅ 已儲存 {result.valid} 個詞彙到暫存區", fg="green"))
        click.echo(f"   檔案: {path}")
        click.echo("\n💡 使用 'zhtw review' 審核並核准詞彙")


@main.command()
@click.option(
    "--list",
    "-l",
    "list_only",
    is_flag=True,
    help="列出待審核檔案",
)
@click.option(
    "--no-llm",
    is_flag=True,
    help="停用 LLM 輔助審核（預設啟用 LLM）",
)
@click.option(
    "--approve-all",
    is_flag=True,
    help="核准所有待審核詞彙",
)
@click.option(
    "--reject-all",
    is_flag=True,
    help="拒絕所有待審核詞彙",
)
@click.option(
    "--file",
    "-f",
    "file_name",
    type=str,
    help="指定要審核的檔案",
)
@click.option(
    "--force",
    is_flag=True,
    help="強制執行，忽略 LLM 用量限制",
)
def review(
    list_only: bool,
    no_llm: bool,
    approve_all: bool,
    reject_all: bool,
    file_name: Optional[str],
    force: bool,
):
    """
    審核待匯入的詞彙（預設啟用 LLM 驗證）。

    Example:

        zhtw review --list

        zhtw review

        zhtw review --no-llm

        zhtw review --approve-all
    """
    from .import_terms import list_pending
    from .review import finalize_review, review_pending_file

    pending = list_pending()

    if not pending:
        click.echo("📋 暫無待審核詞彙")
        click.echo("\n💡 使用 'zhtw import <file>' 匯入詞庫")
        return

    if list_only:
        click.echo("📋 待審核檔案:\n")
        for item in pending:
            click.echo(f"   📄 {item['name']}")
            click.echo(f"      詞彙數: {item['terms_count']}")
            click.echo(f"      說明: {item['description']}")
            click.echo()
        return

    # Get LLM client (enabled by default)
    llm_client = None
    if not no_llm:
        try:
            from .llm import GeminiClient

            llm_client = GeminiClient(force=force)
            if not llm_client.is_available():
                click.echo(click.style("⚠️ GEMINI_API_KEY 未設定，將不使用 LLM", fg="yellow"))
                llm_client = None
        except ImportError:
            click.echo(click.style("⚠️ LLM 模組未安裝，將不使用 LLM", fg="yellow"))

    # Determine which file to review
    if file_name:
        target_files = [
            f for f in pending
            if f["name"] == file_name or f["name"] == file_name + ".json"
        ]
        if not target_files:
            click.echo(click.style(f"❌ 找不到檔案: {file_name}", fg="red"))
            sys.exit(1)
    else:
        target_files = pending

    total_approved = 0
    total_rejected = 0

    for item in target_files:
        name = item["name"]
        click.echo(f"\n📋 審核: {name} ({item['terms_count']} 個詞彙)")
        click.echo("━" * 40)

        try:
            result = review_pending_file(
                name=name,
                llm_client=llm_client,
                interactive=not (approve_all or reject_all),
                auto_approve=approve_all,
                auto_reject=reject_all,
            )

            total_approved += result.approved
            total_rejected += result.rejected

            if result.approved > 0:
                path = finalize_review(name, result)
                click.echo(f"\n✅ 已核准 {result.approved} 個詞彙 → {path}")
            else:
                finalize_review(name, result, delete_after=True)
                msg = f"核准: {result.approved}, 拒絕: {result.rejected}, 跳過: {result.skipped}"
                click.echo(f"\n📋 已處理（{msg}）")

        except Exception as e:
            click.echo(click.style(f"❌ 審核失敗: {e}", fg="red"))

    click.echo(f"\n📊 審核完成: 核准 {total_approved}, 拒絕 {total_rejected}")


@main.command()
@click.option(
    "--json",
    "json_output",
    is_flag=True,
    help="輸出 JSON 格式",
)
@click.option(
    "--reset",
    is_flag=True,
    help="重設用量統計（需確認）",
)
def usage(json_output: bool, reset: bool):
    """
    顯示 LLM 用量統計。

    Example:

        zhtw usage

        zhtw usage --json

        zhtw usage --reset
    """
    from .llm.usage import UsageTracker

    tracker = UsageTracker()

    if reset:
        if click.confirm("確定要重設所有用量統計？"):
            tracker.reset()
            click.echo(click.style("✅ 用量已重設", fg="green"))
        return

    report = tracker.format_usage_report(json_output=json_output)
    click.echo(report)


@main.command()
@click.argument("action", type=click.Choice(["show", "set", "reset"]))
@click.argument("args", nargs=-1)
def config(action: str, args: tuple):
    """
    管理設定。

    Example:

        zhtw config show

        zhtw config set llm.limits.daily_cost_usd 0.05

        zhtw config reset
    """
    from .config import load_config, reset_config, set_config_value

    if action == "show":
        cfg = load_config()
        click.echo(json.dumps(cfg, indent=2, ensure_ascii=False))

    elif action == "set":
        if len(args) < 2:
            click.echo(click.style("❌ 用法: zhtw config set <key> <value>", fg="red"))
            click.echo("   例如: zhtw config set llm.limits.daily_cost_usd 0.05")
            sys.exit(1)

        key = args[0]
        value = args[1]

        # Try to parse as number or boolean
        if value.lower() == "true":
            value = True
        elif value.lower() == "false":
            value = False
        else:
            try:
                if "." in value:
                    value = float(value)
                else:
                    value = int(value)
            except ValueError:
                pass  # Keep as string

        set_config_value(key, value)
        click.echo(click.style(f"✅ 已設定 {key} = {value}", fg="green"))

    elif action == "reset":
        if click.confirm("確定要重設為預設設定？"):
            reset_config()
            click.echo(click.style("✅ 設定已重設", fg="green"))


# Update validate command to support --llm
@main.command("validate-llm")
@click.option(
    "--source",
    "-s",
    type=str,
    default="cn,hk",
    help="驗證來源: cn (簡體), hk (港式), 或 cn,hk (預設)",
)
@click.option(
    "--limit",
    "-l",
    type=int,
    default=50,
    help="限制驗證數量（預設 50）",
)
@click.option(
    "--force",
    is_flag=True,
    help="強制執行，忽略用量限制",
)
def validate_llm(source: str, limit: int, force: bool):
    """
    使用 LLM 驗證詞庫品質。

    Example:

        zhtw validate-llm

        zhtw validate-llm --limit 100

        zhtw validate-llm --force
    """
    from .llm import GeminiClient, LLMError, UsageLimitError

    sources_list = [s.strip() for s in source.split(",")]

    click.echo("🤖 LLM 驗證詞庫品質\n")
    click.echo("━" * 50)

    # Initialize LLM client
    try:
        client = GeminiClient(force=force)
        if not client.is_available():
            click.echo(click.style("❌ 請先設定 GEMINI_API_KEY 環境變數", fg="red"))
            click.echo("\n設定方式:")
            click.echo('  export GEMINI_API_KEY="your-api-key"')
            click.echo("  或使用 direnv: echo 'export GEMINI_API_KEY=\"your-key\"' > .envrc")
            sys.exit(1)
    except Exception as e:
        click.echo(click.style(f"❌ 初始化 LLM 失敗: {e}", fg="red"))
        sys.exit(1)

    # Load terms
    terms = load_dictionary(sources=sources_list)
    terms_list = list(terms.items())[:limit]

    click.echo(f"📋 驗證 {len(terms_list)} 個詞彙（共 {len(terms)} 個）\n")

    correct_count = 0
    incorrect_count = 0
    error_count = 0
    incorrect_terms = []

    with click.progressbar(terms_list, label="驗證中") as bar:
        for src, tgt in bar:
            try:
                result = client.validate_term(src, tgt)
                if result["correct"]:
                    correct_count += 1
                else:
                    incorrect_count += 1
                    incorrect_terms.append({
                        "source": src,
                        "target": tgt,
                        "reason": result.get("reason", ""),
                        "suggestion": result.get("suggestion"),
                    })
            except UsageLimitError as e:
                click.echo(f"\n{e}")
                break
            except LLMError:
                error_count += 1

    click.echo("\n" + "━" * 50)
    click.echo(f"✅ 正確: {correct_count}")
    click.echo(f"❌ 可能有誤: {incorrect_count}")
    if error_count:
        click.echo(f"⚠️ 錯誤: {error_count}")

    if incorrect_terms:
        click.echo("\n📋 可能有誤的詞彙:")
        for item in incorrect_terms[:10]:
            click.echo(f"\n   「{item['source']}」→「{item['target']}」")
            if item["reason"]:
                click.echo(f"   理由: {item['reason']}")
            if item["suggestion"]:
                click.echo(f"   建議: {item['suggestion']}")

        if len(incorrect_terms) > 10:
            click.echo(f"\n   ... 還有 {len(incorrect_terms) - 10} 個")

    # Show usage
    click.echo("\n" + "━" * 50)
    from .llm.usage import UsageTracker

    tracker = UsageTracker()
    warning = tracker.get_warning()
    if warning:
        click.echo(warning)


if __name__ == "__main__":
    main()
