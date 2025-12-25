"""
CLI interface for ZHTW.

Usage:
    zhtw check ./src           # Check mode (report only)
    zhtw fix ./src             # Fix mode (modify files)
    zhtw check ./src --json    # JSON output for CI/CD
"""

import json
import sys
from pathlib import Path
from typing import List, Optional

import click

from . import __version__
from .converter import ConversionResult, Issue, process_directory


def format_issue(issue: Issue, show_context: bool = True) -> str:
    """Format an issue for console output."""
    location = f"L{issue.line}:{issue.column}"
    change = f'"{issue.source}" → "{issue.target}"'

    if show_context:
        return f"   {location}: {change}\n      {issue.context}"
    return f"   {location}: {change}"


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
        f"(跳過 {result.files_skipped} 個無中文檔案)"
    )


def print_json(result: ConversionResult) -> None:
    """Print results as JSON."""
    output = {
        "total_issues": result.total_issues,
        "files_with_issues": result.files_with_issues,
        "files_checked": result.files_checked,
        "files_modified": result.files_modified,
        "files_skipped": result.files_skipped,
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
def check(
    path: Path,
    source: str,
    custom_dict: Optional[Path],
    exclude: Optional[str],
    json_output: bool,
    verbose: bool,
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

    if not json_output:
        click.echo(f"📁 掃描 {path}")

    result = process_directory(
        directory=path,
        sources=sources,
        custom_dict=custom_dict,
        fix=False,
        excludes=excludes,
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
def fix(
    path: Path,
    source: str,
    custom_dict: Optional[Path],
    exclude: Optional[str],
    json_output: bool,
    verbose: bool,
    dry_run: bool,
):
    """
    修正模式：掃描檔案並自動修正問題。

    Example:

        zhtw fix ./src

        zhtw fix ./src --dry-run

        zhtw fix ./src --source cn
    """
    sources = [s.strip() for s in source.split(",")]
    excludes = set(e.strip() for e in exclude.split(",")) if exclude else None

    if not json_output:
        mode = "模擬" if dry_run else "修正"
        click.echo(f"🔧 {mode}模式：掃描 {path}")

    result = process_directory(
        directory=path,
        sources=sources,
        custom_dict=custom_dict,
        fix=not dry_run,
        excludes=excludes,
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


if __name__ == "__main__":
    main()
