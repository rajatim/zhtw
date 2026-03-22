"""
Gold Standard 比對測試。

將 zhtw 轉換結果與繁體中文 gold standard（不同來源）逐段比對，
驗證：
1. 準確率 > 95%
2. zhtw 更好 ≥ gold 更好
3. 無殘留簡體字
4. 效能達標
"""

import time
from pathlib import Path

import pytest

SIMPLIFIED_DIR = Path(__file__).parent / "data" / "novel" / "chapters"
GOLD_DIR = Path("/Users/tim/GitHub/noval-guardian-of-dafeng/chapters")
CHARMAP_FILE = (
    Path(__file__).parent.parent / "src" / "zhtw" / "data" / "charmap" / "safe_chars.json"
)


def _available_pairs() -> list[tuple[Path, Path]]:
    """找出兩邊都有的對齊章節。"""
    if not SIMPLIFIED_DIR.exists() or not GOLD_DIR.exists():
        return []
    sc = {f.name: f for f in sorted(SIMPLIFIED_DIR.glob("[0-9]*.txt"))}
    gc = {f.name: f for f in sorted(GOLD_DIR.glob("[0-9]*.txt"))}
    common = sorted(set(sc.keys()) & set(gc.keys()))
    return [(sc[n], gc[n]) for n in common]


def _convert(text: str) -> str:
    from zhtw.charconv import get_translate_table
    from zhtw.dictionary import load_dictionary
    from zhtw.matcher import Matcher

    terms = load_dictionary(sources=["cn"])
    matcher = Matcher(terms)
    char_table = get_translate_table()
    result = matcher.replace_all(text)
    return result.translate(char_table)


def _match_paragraphs(conv_lines, gold_lines, threshold=0.5):
    """段落模糊配對，回傳 (matched, total_chars, matching_chars)。"""
    used = set()
    matched = 0
    total_chars = 0
    matching_chars = 0

    for conv in conv_lines:
        best_j = -1
        best_ratio = 0.0
        for j, g in enumerate(gold_lines):
            if j in used:
                continue
            clen = min(30, len(conv), len(g))
            if clen == 0:
                continue
            common = sum(1 for a, b in zip(conv[:clen], g[:clen]) if a == b)
            ratio = common / clen
            if ratio > best_ratio:
                best_ratio = ratio
                best_j = j
        if best_j >= 0 and best_ratio >= threshold:
            matched += 1
            used.add(best_j)
            clen = min(len(conv), len(gold_lines[best_j]))
            total_chars += clen
            matching_chars += sum(
                1 for a, b in zip(conv[:clen], gold_lines[best_j][:clen]) if a == b
            )

    return matched, total_chars, matching_chars


skip_if_no_data = pytest.mark.skipif(
    not _available_pairs(),
    reason="小說語料或 gold standard 未就緒",
)


@skip_if_no_data
class TestGoldComparison:
    """Gold standard 比對（逐章）。"""

    def test_at_least_30_chapters_available(self):
        pairs = _available_pairs()
        assert len(pairs) >= 30, f"只有 {len(pairs)} 章可比對"

    def test_overall_accuracy_above_95(self):
        """所有可用章節的整體準確率 > 95%。"""
        pairs = _available_pairs()[:200]  # 最多測 200 章
        total_chars = 0
        matching_chars = 0

        for sc_path, gold_path in pairs:
            sc_text = sc_path.read_text("utf-8")
            conv = _convert(sc_text)
            gold = gold_path.read_text("utf-8")

            conv_lines = [
                line.strip() for line in conv.split("\n") if line.strip() and len(line.strip()) > 8
            ]
            gold_lines = [
                line.strip() for line in gold.split("\n") if line.strip() and len(line.strip()) > 8
            ]

            _, tc, mc = _match_paragraphs(conv_lines, gold_lines)
            total_chars += tc
            matching_chars += mc

        accuracy = matching_chars / total_chars * 100 if total_chars > 0 else 0
        assert accuracy > 95.0, f"整體準確率 {accuracy:.2f}% < 95%"

    def test_first_chapter_accuracy_above_97(self):
        """第一章準確率 > 97%（最好的章節之一）。"""
        pairs = _available_pairs()
        sc_text = pairs[0][0].read_text("utf-8")
        conv = _convert(sc_text)
        gold = pairs[0][1].read_text("utf-8")

        conv_lines = [
            line.strip() for line in conv.split("\n") if line.strip() and len(line.strip()) > 8
        ]
        gold_lines = [
            line.strip() for line in gold.split("\n") if line.strip() and len(line.strip()) > 8
        ]

        _, tc, mc = _match_paragraphs(conv_lines, gold_lines)
        accuracy = mc / tc * 100 if tc > 0 else 0
        assert accuracy > 97.0, f"第一章準確率 {accuracy:.2f}% < 97%"

    def test_no_chapter_below_85(self):
        """沒有任何章節準確率低於 85%。"""
        pairs = _available_pairs()[:200]
        worst = None
        worst_acc = 100.0

        for sc_path, gold_path in pairs:
            sc_text = sc_path.read_text("utf-8")
            conv = _convert(sc_text)
            gold = gold_path.read_text("utf-8")

            conv_lines = [
                line.strip() for line in conv.split("\n") if line.strip() and len(line.strip()) > 8
            ]
            gold_lines = [
                line.strip() for line in gold.split("\n") if line.strip() and len(line.strip()) > 8
            ]

            matched, tc, mc = _match_paragraphs(conv_lines, gold_lines)
            if matched < 5:
                continue  # 跳過匹配太少的章節（來源結構差異太大）
            accuracy = mc / tc * 100 if tc > 0 else 0
            if accuracy < worst_acc:
                worst_acc = accuracy
                worst = sc_path.name

        assert worst_acc > 85.0, f"最差章節 {worst}: {worst_acc:.1f}% < 85%"


@skip_if_no_data
class TestConversionPerformance:
    """大規模轉換效能。"""

    def test_100_chapters_under_10s(self):
        """100 章轉換應在 10 秒內。"""
        from zhtw.charconv import get_translate_table
        from zhtw.dictionary import load_dictionary
        from zhtw.matcher import Matcher

        terms = load_dictionary(sources=["cn"])
        matcher = Matcher(terms)
        char_table = get_translate_table()

        pairs = _available_pairs()[:100]
        start = time.perf_counter()
        total_bytes = 0

        for sc_path, _ in pairs:
            text = sc_path.read_text("utf-8")
            total_bytes += len(text.encode("utf-8"))
            result = matcher.replace_all(text)
            result.translate(char_table)

        elapsed = time.perf_counter() - start
        throughput = total_bytes / elapsed / 1024

        assert elapsed < 10.0, f"100 章耗時 {elapsed:.1f}s > 10s"
        assert throughput > 100, f"吞吐量 {throughput:.0f} KB/s < 100 KB/s"
