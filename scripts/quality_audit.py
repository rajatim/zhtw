#!/usr/bin/env python3
"""
zhtw 大規模品質審計腳本。

對比 zhtw 轉換結果與 gold standard（繁體中文原文），
逐章、逐段、逐字分析差異，產出品質報告。

用法：
    python scripts/quality_audit.py
    python scripts/quality_audit.py --chapters 100
    python scripts/quality_audit.py --output reports/audit_report.md
"""

from __future__ import annotations

import argparse
import sys
import time
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

SIMPLIFIED_DIR = PROJECT_ROOT / "tests" / "data" / "novel" / "chapters"
GOLD_DIR = Path("/Users/tim/GitHub/noval-guardian-of-dafeng/chapters")
CHARMAP_FILE = PROJECT_ROOT / "src" / "zhtw" / "data" / "charmap" / "safe_chars.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "tests" / "data" / "novel" / "audit_report.md"


@dataclass
class DiffItem:
    """單一差異項。"""

    chapter: int
    paragraph: str  # 段落前 30 字
    position: int
    our_char: str
    gold_char: str
    context: str  # 差異處前後 5 字


@dataclass
class ChapterResult:
    """單章比對結果。"""

    chapter_num: int
    total_paragraphs: int = 0
    matched_paragraphs: int = 0
    total_chars_compared: int = 0
    matching_chars: int = 0
    diffs: list = field(default_factory=list)
    our_better: list = field(default_factory=list)  # zhtw 比 gold 更好的
    gold_better: list = field(default_factory=list)  # gold 比 zhtw 更好的
    neutral: list = field(default_factory=list)  # 兩者不同但各有道理


@dataclass
class AuditReport:
    """總審計報告。"""

    chapters_tested: int = 0
    total_paragraphs: int = 0
    matched_paragraphs: int = 0
    total_chars: int = 0
    matching_chars: int = 0
    conversion_time: float = 0.0
    total_source_bytes: int = 0
    diff_categories: dict = field(
        default_factory=lambda: {
            "our_better": [],
            "gold_better": [],
            "neutral": [],
            "source_diff": [],
        }
    )
    char_diff_counter: Counter = field(default_factory=Counter)
    chapter_results: list = field(default_factory=list)


def load_converter():
    """載入 zhtw 轉換器。"""
    from zhtw.charconv import get_translate_table
    from zhtw.dictionary import load_dictionary
    from zhtw.matcher import Matcher

    terms = load_dictionary(sources=["cn"])
    matcher = Matcher(terms)
    char_table = get_translate_table()
    return matcher, char_table


def convert(text: str, matcher, char_table) -> str:
    """全管線轉換。"""
    result = matcher.replace_all(text)
    return result.translate(char_table)


def extract_paragraphs(text: str, min_len: int = 8) -> list[str]:
    """提取有意義的段落（排除標題、短行）。"""
    lines = []
    for line in text.split("\n"):
        line = line.strip()
        if line and len(line) >= min_len:
            # 排除廣告浮水印殘留
            if "hetushu" not in line.lower() and "hjwzw" not in line.lower():
                lines.append(line)
    return lines


def match_paragraphs(
    converted: list[str], gold: list[str], threshold: float = 0.5
) -> list[tuple[str, str, float]]:
    """段落模糊配對。

    Returns: [(converted_line, gold_line, similarity), ...]
    """
    matches = []
    used_gold = set()

    for conv in converted:
        best_idx = -1
        best_ratio = 0.0

        for j, g in enumerate(gold):
            if j in used_gold:
                continue
            # 比較前 30 字元
            compare_len = min(30, len(conv), len(g))
            if compare_len == 0:
                continue
            common = sum(1 for a, b in zip(conv[:compare_len], g[:compare_len]) if a == b)
            ratio = common / compare_len
            if ratio > best_ratio:
                best_ratio = ratio
                best_idx = j

        if best_idx >= 0 and best_ratio >= threshold:
            matches.append((conv, gold[best_idx], best_ratio))
            used_gold.add(best_idx)

    return matches


# ── 差異分類知識庫 ──

# zhtw 比 gold 更好的模式
OUR_BETTER_PATTERNS = {
    ("牆", "墻"): "台灣標準用 牆",
    ("係", "系"): "關係 是正確繁體",
    ("裡", "裏"): "台灣標準用 裡",
    ("群", "羣"): "台灣標準用 群",
    ("鍊", "煉"): "鍛鍊/項鍊 用 鍊，gold 不區分",
    ("吃", "喫"): "台灣用 吃，喫 是古字",
    ("製", "制"): "製造 用 製，gold 可能未區分",
}

# gold 比 zhtw 更好的模式（zhtw 漏轉）
GOLD_BETTER_PATTERNS: dict = {
    # 已全部修復，暫無
}

# 來源差異（非轉換問題）
SOURCE_DIFF_PATTERNS = {
    (
        """, "'"): "引號風格差異",
    (""",
        "'",
    ): "引號風格差異",
    ("|", ""): "審查遮罩",
}


def classify_diff(our_char: str, gold_char: str, context: str = "") -> str:
    """分類差異。Returns: 'our_better', 'gold_better', 'neutral', 'source_diff'"""
    # 引號差異
    if our_char in '""' and gold_char in "''":
        return "source_diff"
    if gold_char in '""' and our_char in "''":
        return "source_diff"

    # 遮罩字元 / 標點差異
    if "|" in (our_char, gold_char):
        return "source_diff"
    # 段落內容錯位（逗號vs的 等）通常是來源段落不完全相同
    if our_char in "，。、；：！？" or gold_char in "，。、；：！？":
        return "source_diff"

    # 已知 zhtw 更好
    for (a, b), _ in OUR_BETTER_PATTERNS.items():
        if our_char == a and gold_char == b:
            return "our_better"

    # 已知 gold 更好
    for (a, b), _ in GOLD_BETTER_PATTERNS.items():
        if our_char == a and gold_char == b:
            return "gold_better"

    # 兩者都是合法繁體字
    if "\u4e00" <= our_char <= "\u9fff" and "\u4e00" <= gold_char <= "\u9fff":
        return "neutral"

    return "neutral"


def compare_chapter(
    chapter_num: int, simplified_path: Path, gold_path: Path, matcher, char_table
) -> ChapterResult:
    """比對單章。"""
    result = ChapterResult(chapter_num=chapter_num)

    sc_text = simplified_path.read_text("utf-8")
    tc_text = gold_path.read_text("utf-8")

    # 轉換
    converted = convert(sc_text, matcher, char_table)

    # 提取段落
    conv_paras = extract_paragraphs(converted)
    gold_paras = extract_paragraphs(tc_text)

    result.total_paragraphs = len(conv_paras)

    # 配對
    matches = match_paragraphs(conv_paras, gold_paras)
    result.matched_paragraphs = len(matches)

    # 逐字比對
    for conv_line, gold_line, _ in matches:
        compare_len = min(len(conv_line), len(gold_line))
        result.total_chars_compared += compare_len

        for pos in range(compare_len):
            if conv_line[pos] == gold_line[pos]:
                result.matching_chars += 1
            else:
                category = classify_diff(conv_line[pos], gold_line[pos])
                ctx_start = max(0, pos - 3)
                ctx_end = min(compare_len, pos + 4)
                context = conv_line[ctx_start:ctx_end]

                diff = DiffItem(
                    chapter=chapter_num,
                    paragraph=conv_line[:30],
                    position=pos,
                    our_char=conv_line[pos],
                    gold_char=gold_line[pos],
                    context=context,
                )

                if category == "our_better":
                    result.our_better.append(diff)
                elif category == "gold_better":
                    result.gold_better.append(diff)
                elif category == "source_diff":
                    pass  # 不計入
                else:
                    result.neutral.append(diff)

    return result


def generate_report(report: AuditReport) -> str:
    """產生 Markdown 格式報告。"""
    accuracy = report.matching_chars / report.total_chars * 100 if report.total_chars > 0 else 0
    throughput = (
        report.total_source_bytes / report.conversion_time / 1024
        if report.conversion_time > 0
        else 0
    )

    # 統計差異類別
    all_our_better = []
    all_gold_better = []
    all_neutral = []
    for cr in report.chapter_results:
        all_our_better.extend(cr.our_better)
        all_gold_better.extend(cr.gold_better)
        all_neutral.extend(cr.neutral)

    # 差異字元頻率
    our_better_chars = Counter(f"{d.our_char}→{d.gold_char}" for d in all_our_better)
    gold_better_chars = Counter(f"{d.our_char}→{d.gold_char}" for d in all_gold_better)
    neutral_chars = Counter(f"{d.our_char}→{d.gold_char}" for d in all_neutral)

    lines = []
    lines.append("# zhtw 品質審計報告")
    lines.append("")
    lines.append(f"**生成時間**: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("**測試語料**: 大奉打更人（簡體→zhtw 轉換→與繁體 gold standard 比對）")
    lines.append("")
    lines.append("## 總覽")
    lines.append("")
    lines.append("| 指標 | 數值 |")
    lines.append("|------|------|")
    lines.append(f"| 測試章節數 | {report.chapters_tested} |")
    lines.append(f"| 段落總數 | {report.total_paragraphs} |")
    lines.append(f"| 匹配段落 | {report.matched_paragraphs} |")
    lines.append(f"| 比對字元數 | {report.total_chars:,} |")
    lines.append(f"| 一致字元數 | {report.matching_chars:,} |")
    lines.append(f"| **字元準確率** | **{accuracy:.2f}%** |")
    lines.append(f"| 轉換耗時 | {report.conversion_time:.2f}s |")
    lines.append(f"| 吞吐量 | {throughput:.0f} KB/s |")
    lines.append("")

    lines.append("## 差異分類")
    lines.append("")
    lines.append("| 類別 | 數量 | 說明 |")
    lines.append("|------|------|------|")
    lines.append(f"| zhtw 更好 | {len(all_our_better)} | zhtw 用台灣標準，gold 用了通用/錯誤形式 |")
    lines.append(f"| gold 更好 | {len(all_gold_better)} | zhtw 漏轉或轉錯 |")
    lines.append(f"| 中性差異 | {len(all_neutral)} | 兩者都合理但不同 |")
    lines.append("")

    if our_better_chars:
        lines.append("### zhtw 更好的轉換（Top 10）")
        lines.append("")
        lines.append("| 差異 | 次數 | 說明 |")
        lines.append("|------|------|------|")
        for pair, count in our_better_chars.most_common(10):
            our, gold = pair.split("→")
            desc = OUR_BETTER_PATTERNS.get((our, gold), "")
            lines.append(f"| {pair} | {count} | {desc} |")
        lines.append("")

    if gold_better_chars:
        lines.append("### zhtw 需改進（gold 更好）")
        lines.append("")
        lines.append("| 差異 | 次數 | 說明 |")
        lines.append("|------|------|------|")
        for pair, count in gold_better_chars.most_common(10):
            our, gold = pair.split("→")
            desc = GOLD_BETTER_PATTERNS.get((our, gold), "")
            lines.append(f"| {pair} | {count} | {desc} |")
        lines.append("")

    if neutral_chars:
        lines.append("### 中性差異（Top 20）")
        lines.append("")
        lines.append("| 差異 | 次數 |")
        lines.append("|------|------|")
        for pair, count in neutral_chars.most_common(20):
            lines.append(f"| {pair} | {count} |")
        lines.append("")

    # 逐章摘要
    lines.append("## 逐章摘要")
    lines.append("")
    lines.append("| 章 | 段落 | 匹配 | 比對字元 | 準確率 | 差異數 |")
    lines.append("|---:|-----:|-----:|---------:|-------:|-------:|")
    for cr in report.chapter_results:
        acc = (
            cr.matching_chars / cr.total_chars_compared * 100 if cr.total_chars_compared > 0 else 0
        )
        total_diffs = len(cr.our_better) + len(cr.gold_better) + len(cr.neutral)
        lines.append(
            f"| {cr.chapter_num} | {cr.total_paragraphs} | {cr.matched_paragraphs} "
            f"| {cr.total_chars_compared:,} | {acc:.1f}% | {total_diffs} |"
        )
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="zhtw 品質審計")
    parser.add_argument("--chapters", type=int, default=0, help="測試章節數（0=全部）")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="報告輸出路徑")
    args = parser.parse_args()

    print("=" * 60)
    print("  zhtw 品質審計")
    print("=" * 60)

    # 檢查語料
    if not SIMPLIFIED_DIR.exists():
        print(f"錯誤：簡體語料不存在: {SIMPLIFIED_DIR}")
        print("請先執行 scripts/scrape_novel.sh")
        sys.exit(1)

    if not GOLD_DIR.exists():
        print(f"錯誤：繁體 gold standard 不存在: {GOLD_DIR}")
        sys.exit(1)

    sc_files = sorted(SIMPLIFIED_DIR.glob("[0-9]*.txt"))
    gold_files = sorted(GOLD_DIR.glob("[0-9]*.txt"))

    if not sc_files or not gold_files:
        print("錯誤：找不到章節檔案")
        sys.exit(1)

    # 對齊章節
    max_chapters = min(len(sc_files), len(gold_files))
    if args.chapters > 0:
        max_chapters = min(max_chapters, args.chapters)

    print(f"\n  簡體章節: {len(sc_files)}")
    print(f"  繁體章節: {len(gold_files)}")
    print(f"  測試章節: {max_chapters}")

    # 載入轉換器
    print("\n  載入轉換器...", end=" ", flush=True)
    matcher, char_table = load_converter()
    print("OK")

    # 逐章比對
    print(f"\n  開始比對（{max_chapters} 章）...\n")

    report = AuditReport()
    total_start = time.perf_counter()

    for i in range(max_chapters):
        sc_path = sc_files[i]
        gold_path = gold_files[i]

        # 計時
        start = time.perf_counter()
        cr = compare_chapter(i + 1, sc_path, gold_path, matcher, char_table)
        elapsed = time.perf_counter() - start

        report.total_source_bytes += sc_path.stat().st_size
        report.chapter_results.append(cr)
        report.chapters_tested += 1
        report.total_paragraphs += cr.total_paragraphs
        report.matched_paragraphs += cr.matched_paragraphs
        report.total_chars += cr.total_chars_compared
        report.matching_chars += cr.matching_chars

        acc = cr.matching_chars / cr.total_chars_compared * 100 if cr.total_chars_compared else 0
        total_diffs = len(cr.our_better) + len(cr.gold_better) + len(cr.neutral)
        print(
            f"  [{i+1:3d}/{max_chapters}] Ch.{cr.chapter_num:03d} "
            f"| {cr.matched_paragraphs:2d}/{cr.total_paragraphs:2d} 段 "
            f"| {acc:5.1f}% "
            f"| diff: {total_diffs:2d} "
            f"| {elapsed*1000:.0f}ms"
        )

    report.conversion_time = time.perf_counter() - total_start

    # 產生報告
    report_text = generate_report(report)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report_text, encoding="utf-8")

    overall_acc = report.matching_chars / report.total_chars * 100 if report.total_chars else 0
    print(f"\n{'=' * 60}")
    print(f"  測試章節: {report.chapters_tested}")
    print(f"  比對字元: {report.total_chars:,}")
    print(f"  字元準確率: {overall_acc:.2f}%")
    print(f"  轉換耗時: {report.conversion_time:.2f}s")
    print(f"  報告: {args.output}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
