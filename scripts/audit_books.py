#!/usr/bin/env python3
"""
多書籍大規模品質審計。

從 epub 書籍提取簡體中文文字，執行 zhtw 轉換，分析：
1. 殘留簡體字（未轉換的字元）
2. 疑似過度轉換
3. 古字/異體字
4. 效能基準
5. 各書籍的問題詞彙

用法：
    python scripts/audit_books.py [--books-dir DIR] [--max-books N] [--output FILE]
"""

import argparse
import sys
import time
import warnings
from collections import Counter
from pathlib import Path

# 抑制 XML 解析警告
warnings.filterwarnings("ignore", category=UserWarning)

try:
    import ebooklib
    from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
    from ebooklib import epub

    warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
except ImportError:
    print("需要安裝：pip install ebooklib beautifulsoup4 lxml", file=sys.stderr)
    sys.exit(1)

# zhtw 模組
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from zhtw.charconv import get_translate_table, load_charmap  # noqa: E402
from zhtw.dictionary import load_dictionary  # noqa: E402
from zhtw.matcher import Matcher  # noqa: E402

# ── 常數 ──────────────────────────────────────

ARCHAIC_CHARS = set("纔閤纍衆爲牀竈糉")

# 已知的過度轉換模式（converted → 原文應該是什麼）
OVER_CONVERSION_PATTERNS = [
    ("週知", "周知"),  # 众所周知
    ("週到", "周到"),  # 周到的服务
    ("週圍", "周圍"),  # 周围环境 → 周圍 才對
    ("週全", "周全"),
    ("錶情", "表情"),  # 表情包
    ("錶面", "表面"),  # 表面
    ("閤理", "合理"),
    ("閤作", "合作"),
    ("纔能", "才能"),
    ("計程車卒", "的士卒"),  # Aho-Corasick 重疊
]


def extract_text_from_epub(epub_path: Path) -> str:
    """從 epub 提取純文字。"""
    try:
        book = epub.read_epub(str(epub_path), options={"ignore_ncx": True})
    except Exception:
        return ""

    parts = []
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        try:
            soup = BeautifulSoup(item.get_content(), "lxml")
            text = soup.get_text(separator="\n")
            if text.strip():
                parts.append(text)
        except Exception:
            continue
    return "\n".join(parts)


def find_residual_simplified(text: str, charmap: dict) -> Counter:
    """找出轉換後仍殘留的簡體字。"""
    residual = Counter()
    for ch in text:
        if ch in charmap:
            residual[ch] += 1
    return residual


def find_archaic_chars(text: str) -> Counter:
    """找出古字/異體字。"""
    found = Counter()
    for ch in text:
        if ch in ARCHAIC_CHARS:
            found[ch] += 1
    return found


def find_over_conversions(text: str) -> list:
    """找出疑似過度轉換。"""
    found = []
    for wrong, correct in OVER_CONVERSION_PATTERNS:
        count = text.count(wrong)
        if count > 0:
            found.append((wrong, correct, count))
    return found


def audit_one_book(
    epub_path: Path,
    matcher: Matcher,
    char_table: dict,
    charmap: dict,
) -> dict:
    """審計單一書籍，回傳結果字典。"""
    name = epub_path.stem
    text = extract_text_from_epub(epub_path)
    if not text or len(text) < 100:
        return {"name": name, "error": "無法提取文字或內容過短", "chars": 0}

    # 限制每本書最多處理 500K 字元（避免超大書籍卡住）
    MAX_CHARS = 500_000
    full_char_count = len(text)
    if len(text) > MAX_CHARS:
        text = text[:MAX_CHARS]

    char_count = full_char_count  # 記錄原始大小
    byte_count = len(text.encode("utf-8"))

    # 轉換
    start = time.perf_counter()
    converted = matcher.replace_all(text)
    converted = converted.translate(char_table)
    elapsed = time.perf_counter() - start

    throughput = (byte_count / 1024) / elapsed if elapsed > 0 else float("inf")

    # 分析
    residual = find_residual_simplified(converted, charmap)
    archaic = find_archaic_chars(converted)
    over_conv = find_over_conversions(converted)

    # 殘留率
    total_simplified_possible = sum(1 for ch in text if ch in charmap)
    residual_total = sum(residual.values())
    residual_rate = (
        residual_total / total_simplified_possible * 100 if total_simplified_possible > 0 else 0
    )

    return {
        "name": name,
        "chars": char_count,
        "bytes": byte_count,
        "elapsed_ms": round(elapsed * 1000),
        "throughput_kbs": round(throughput),
        "residual_count": residual_total,
        "residual_rate_pct": round(residual_rate, 2),
        "residual_top10": residual.most_common(10),
        "archaic_count": sum(archaic.values()),
        "archaic_chars": dict(archaic),
        "over_conversion": over_conv,
    }


def generate_report(results: list, output_path: Path, elapsed_total: float):
    """生成 Markdown 審計報告。"""
    total_chars = sum(r["chars"] for r in results if "error" not in r)
    total_bytes = sum(r.get("bytes", 0) for r in results if "error" not in r)
    total_residual = sum(r.get("residual_count", 0) for r in results)
    total_archaic = sum(r.get("archaic_count", 0) for r in results)
    total_over = sum(sum(c for _, _, c in r.get("over_conversion", [])) for r in results)
    successful = [r for r in results if "error" not in r]

    # 彙整所有殘留簡體字
    all_residual = Counter()
    for r in successful:
        for ch, cnt in r.get("residual_top10", []):
            all_residual[ch] += cnt

    # 彙整所有過度轉換
    all_over = Counter()
    for r in successful:
        for wrong, correct, cnt in r.get("over_conversion", []):
            all_over[(wrong, correct)] += cnt

    lines = []
    lines.append("# zhtw 多書籍品質審計報告\n")
    lines.append(f"**生成時間**: {time.strftime('%Y-%m-%d %H:%M')}")
    lines.append("**語料來源**: Nan-nx/Book GitHub repo\n")

    lines.append("## 總覽\n")
    lines.append("| 指標 | 數值 |")
    lines.append("|------|------|")
    lines.append(f"| 書籍數 | {len(successful)}/{len(results)} |")
    lines.append(f"| 總字元數 | {total_chars:,} |")
    lines.append(f"| 總位元組 | {total_bytes / 1024 / 1024:.1f} MB |")
    lines.append(f"| 轉換總耗時 | {elapsed_total:.1f}s |")
    lines.append(
        f"| 平均吞吐量 | {total_bytes / 1024 / elapsed_total:.0f} KB/s |"
        if elapsed_total > 0
        else "| 平均吞吐量 | - |"
    )
    lines.append(f"| 殘留簡體字總數 | {total_residual} |")
    lines.append(f"| 古字/異體字總數 | {total_archaic} |")
    lines.append(f"| 過度轉換總數 | {total_over} |")

    # 殘留簡體字彙整
    if all_residual:
        lines.append("\n## 殘留簡體字（未轉換）\n")
        lines.append("| 字元 | 次數 | 說明 |")
        lines.append("|------|------|------|")
        for ch, cnt in all_residual.most_common(30):
            lines.append(f"| {ch} | {cnt} | 需調查是否應加入 charmap 或詞庫 |")

    # 過度轉換彙整
    if all_over:
        lines.append("\n## 過度轉換偵測\n")
        lines.append("| 錯誤形式 | 正確形式 | 次數 |")
        lines.append("|---------|---------|------|")
        for (wrong, correct), cnt in all_over.most_common():
            lines.append(f"| {wrong} | {correct} | {cnt} |")

    # 逐書摘要
    lines.append("\n## 逐書摘要\n")
    lines.append("| 書名 | 字元數 | 耗時 | 吞吐量 | 殘留 | 古字 | 過度轉換 |")
    lines.append("|------|-------:|-----:|-------:|-----:|-----:|---------:|")
    for r in sorted(successful, key=lambda x: x["chars"], reverse=True):
        over_cnt = sum(c for _, _, c in r.get("over_conversion", []))
        lines.append(
            f"| {r['name'][:20]} | {r['chars']:,} | "
            f"{r['elapsed_ms']}ms | {r['throughput_kbs']} KB/s | "
            f"{r['residual_count']} | {r['archaic_count']} | {over_cnt} |"
        )

    # 問題書籍詳情
    problem_books = [
        r
        for r in successful
        if r["residual_count"] > 0 or r["archaic_count"] > 0 or r.get("over_conversion")
    ]
    if problem_books:
        lines.append("\n## 問題詳情\n")
        for r in problem_books:
            lines.append(f"### {r['name']}\n")
            if r["residual_count"] > 0:
                lines.append(f"- 殘留簡體字: {r['residual_top10']}")
            if r["archaic_count"] > 0:
                lines.append(f"- 古字: {r['archaic_chars']}")
            if r.get("over_conversion"):
                for wrong, correct, cnt in r["over_conversion"]:
                    lines.append(f"- 過度轉換: {wrong}→應為{correct} ({cnt}次)")
            lines.append("")

    # 錯誤書籍
    errors = [r for r in results if "error" in r]
    if errors:
        lines.append("\n## 無法處理的書籍\n")
        for r in errors:
            lines.append(f"- {r['name']}: {r['error']}")

    report = "\n".join(lines)
    output_path.write_text(report, encoding="utf-8")
    return report


def main():
    parser = argparse.ArgumentParser(description="多書籍品質審計")
    parser.add_argument("--books-dir", default="tests/data/corpus/Book", help="epub 書籍目錄")
    parser.add_argument("--max-books", type=int, default=0, help="最多處理幾本（0=全部）")
    parser.add_argument("--output", default="docs/audit-report-books.md", help="報告輸出路徑")
    args = parser.parse_args()

    books_dir = Path(args.books_dir)
    if not books_dir.exists():
        print(f"錯誤：目錄不存在 {books_dir}", file=sys.stderr)
        sys.exit(1)

    epubs = sorted(books_dir.glob("**/*.epub"))
    if args.max_books > 0:
        epubs = epubs[: args.max_books]

    print("=" * 60)
    print("  zhtw 多書籍品質審計")
    print("=" * 60)
    print(f"\n  書籍目錄: {books_dir}")
    print(f"  epub 數量: {len(epubs)}")

    # 載入轉換器
    print("  載入轉換器...", end=" ", flush=True)
    terms = load_dictionary(sources=["cn"])
    matcher = Matcher(terms)
    char_table = get_translate_table()
    charmap = load_charmap()
    print(f"OK（{len(terms):,} 詞條 + {len(charmap):,} 字元映射）\n")

    results = []
    elapsed_total = 0

    for i, ep in enumerate(epubs, 1):
        print(f"  [{i:3d}/{len(epubs)}] {ep.stem[:40]}...", end=" ", flush=True)

        result = audit_one_book(ep, matcher, char_table, charmap)
        results.append(result)

        if "error" in result:
            print(f"跳過: {result['error']}")
        else:
            elapsed_total += result["elapsed_ms"] / 1000
            flags = []
            if result["residual_count"] > 0:
                flags.append(f"殘留:{result['residual_count']}")
            if result["archaic_count"] > 0:
                flags.append(f"古字:{result['archaic_count']}")
            if result.get("over_conversion"):
                cnt = sum(c for _, _, c in result["over_conversion"])
                flags.append(f"過度:{cnt}")
            flag_str = " | " + ", ".join(flags) if flags else ""
            print(
                f"{result['chars']:>8,} 字 | "
                f"{result['elapsed_ms']:>5}ms | "
                f"{result['throughput_kbs']:>4} KB/s"
                f"{flag_str}"
            )

    # 生成報告
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    generate_report(results, output, elapsed_total)

    total_chars = sum(r["chars"] for r in results if "error" not in r)
    print(f"\n{'=' * 60}")
    print(f"  成功: {sum(1 for r in results if 'error' not in r)}/{len(results)} 本")
    print(f"  總字元: {total_chars:,}")
    print(f"  總耗時: {elapsed_total:.1f}s")
    print(f"  報告: {output}")
    print("=" * 60)


if __name__ == "__main__":
    main()
