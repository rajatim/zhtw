# zhtw:disable
"""
Export command for ZHTW CLI.

Generates SDK data files for multi-language SDK usage.
"""

from __future__ import annotations

from pathlib import Path

import click


@click.command()
@click.option(
    "--output",
    "-o",
    type=click.Path(),
    default=None,
    help="輸出目錄（預設 ./sdk/data/）",
)
@click.option(
    "--source",
    "-s",
    type=str,
    default="cn,hk",
    help="詞庫來源: cn, hk, 或 cn,hk (預設)",
)
@click.option("--verbose", "-v", is_flag=True, help="顯示匯出統計")
def export(output: str | None, source: str, verbose: bool) -> None:
    """
    匯出 SDK 資料檔（maintainer-only）。

    \b
    產生 zhtw-data.json 和 golden-test.json 供多語言 SDK 使用。
    預設輸出到 ./sdk/data/，可用 --output 指定其他路徑。
    """
    from .export import write_export

    sources = [s.strip() for s in source.split(",")]

    # Determine output directory
    if output:
        output_dir = Path(output)
        output_dir.mkdir(parents=True, exist_ok=True)
    else:
        output_dir = Path("sdk/data")
        if not output_dir.exists():
            click.echo(
                click.style("錯誤：", fg="red", bold=True)
                + "找不到 sdk/data/ 目錄。請在 repo 根目錄執行，"
                + "或使用 --output 指定路徑。",
                err=True,
            )
            raise SystemExit(1)

    data_path, golden_path = write_export(
        output_dir=output_dir,
        sources=sources,
    )

    if verbose:
        import json

        data = json.loads(data_path.read_text("utf-8"))
        stats = data["stats"]
        click.echo("📦 匯出完成")
        click.echo(f"   字元映射: {stats['charmap_count']} 個")
        click.echo(f"   歧義字:   {stats['ambiguous_count']} 個")
        click.echo(f"   CN 詞條:  {stats['terms_cn_count']} 個")
        click.echo(f"   HK 詞條:  {stats['terms_hk_count']} 個")
        click.echo(f"   📄 {data_path}")
        click.echo(f"   📄 {golden_path}")
    else:
        click.echo(f"📦 匯出完成 → {output_dir}/")


# zhtw:enable
