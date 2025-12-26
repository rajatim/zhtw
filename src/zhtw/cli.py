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
from .dictionary import DATA_DIR, load_json_file


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


if __name__ == "__main__":
    main()
