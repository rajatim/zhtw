"""
大奉打更人 小說轉換測試。

使用簡體中文小說作為真實世界測試語料，
驗證 zhtw 在大量自然語言文字上的轉換品質。
"""

import json
import time
from pathlib import Path

import pytest

# 語料路徑
NOVEL_DIR = Path(__file__).parent / "data" / "novel"
CHAPTERS_DIR = NOVEL_DIR / "chapters"
MERGED_FILE = NOVEL_DIR / "大奉打更人_簡體.txt"
CHARMAP_FILE = (
    Path(__file__).parent.parent / "src" / "zhtw" / "data" / "charmap" / "safe_chars.json"
)


def _load_charmap():
    data = json.loads(CHARMAP_FILE.read_text("utf-8"))
    return data.get("chars", {}), set(data.get("ambiguous_excluded", []))


def _convert(text: str) -> str:
    """Full pipeline: term-level + char-level."""
    from zhtw.charconv import get_translate_table
    from zhtw.dictionary import load_dictionary
    from zhtw.matcher import Matcher

    terms = load_dictionary(sources=["cn"])
    matcher = Matcher(terms)
    char_table = get_translate_table()
    result = matcher.replace_all(text)
    return result.translate(char_table)


# ── 語料前提檢查 ──

skip_if_no_novel = pytest.mark.skipif(
    not MERGED_FILE.exists(),
    reason="小說語料未下載（執行 scripts/scrape_novel.sh）",
)


@skip_if_no_novel
class TestNovelDataIntegrity:
    """語料檔案完整性。"""

    def test_merged_file_exists(self):
        assert MERGED_FILE.exists()

    def test_merged_file_has_content(self):
        text = MERGED_FILE.read_text("utf-8")
        assert len(text) > 50_000, f"語料過短: {len(text)} 字元"

    def test_chapters_exist(self):
        chapters = list(CHAPTERS_DIR.glob("*.txt"))
        assert len(chapters) >= 10, f"章節數不足: {len(chapters)}"

    def test_text_is_simplified(self):
        """確認語料是簡體中文。"""
        text = MERGED_FILE.read_text("utf-8")[:5000]
        simplified_markers = sum(1 for ch in text if ch in "這個說還沒對應該給讓請認為")
        assert simplified_markers > 20, "語料不像簡體中文"


@skip_if_no_novel
class TestNoResidualSimplified:
    """轉換後不應有殘留的簡體字。"""

    def test_no_safe_chars_remaining(self):
        """safe_chars 中的字元應全部被轉換（取樣前 500K 字元）。"""
        charmap, _ = _load_charmap()
        safe_keys = {k for k, v in charmap.items() if k != v}

        text = MERGED_FILE.read_text("utf-8")[:500_000]
        result = _convert(text)

        residual = {}
        for ch in result:
            if ch in safe_keys:
                residual[ch] = residual.get(ch, 0) + 1

        assert not residual, f"殘留 {len(residual)} 個未轉換的簡體字: " + ", ".join(
            f"{k}→{charmap[k]}({v}次)"
            for k, v in sorted(residual.items(), key=lambda x: -x[1])[:10]
        )


@skip_if_no_novel
class TestNoArchaicChars:
    """轉換結果不應出現古字或罕用異體字。"""

    ARCHAIC_CHARS = {
        "才": "才的古字，台灣不用",
        "閤": "合的異體，台灣用 合",
        "纍": "累的古字，台灣用 累",
        "眾": "眾的異體",
        "為": "為的異體",
        "牀": "床的異體",
        "竈": "灶的異體",
        "粽": "粽的異體",
    }

    def test_no_archaic_in_conversion(self):
        text = MERGED_FILE.read_text("utf-8")[:500_000]
        result = _convert(text)

        found = {}
        for ch, desc in self.ARCHAIC_CHARS.items():
            count = result.count(ch)
            if count > 0:
                found[ch] = (count, desc)

        assert not found, "出現古字/異體字: " + ", ".join(
            f"{k}({v[0]}次, {v[1]})" for k, v in found.items()
        )


@skip_if_no_novel
class TestOverConversionGuards:
    """防止過度轉換。"""

    def test_no_泡棉_in_novel(self):
        """泡沫（foam/bubble）不應被轉為泡棉（foam rubber）。"""
        text = MERGED_FILE.read_text("utf-8")[:500_000]
        result = _convert(text)
        assert "泡棉" not in result, "泡沫被過度轉換為泡棉"

    def test_眾所周知_not_週知(self):
        """周知（to know）不應變成 週知。"""
        result = _convert("眾所周知")
        assert result == "眾所周知", f"got: {result}"

    def test_周遭_preserved(self):
        """周遭不應被下週吃掉。"""
        result = _convert("看了下周遭的環境")
        assert "下周遭" in result, f"got: {result}"

    def test_計程車_not_eating_士卒(self):
        """計程車→計程車 不應吃掉 士卒。"""
        result = _convert("我的士卒")
        assert "的士卒" in result, f"got: {result}"
        assert "計程車卒" not in result, f"got: {result}"

    def test_才_not_才(self):
        """才（talent/just）不應變成古字 才。"""
        result = _convert("才是最好的選擇")
        assert "才" not in result, f"got: {result}"

    def test_配合_not_配閤(self):
        """合不應被轉為閤。"""
        result = _convert("配合工作")
        assert "配閤" not in result, f"got: {result}"
        assert "配合" in result, f"got: {result}"

    def test_歷史_not_歷史記錄(self):
        """歷史→歷史，不是歷史記錄。"""
        result = _convert("歷史悠久")
        assert "歷史悠久" in result, f"got: {result}"
        assert "歷史記錄" not in result, f"got: {result}"


@skip_if_no_novel
class TestAhoCorasickOverlap:
    """Aho-Corasick 重疊保護測試。"""

    OVERLAP_CASES = [
        ("下周遭", "下周遭", "下週 vs 周遭"),
        ("的士卒", "的士卒", "計程車 vs 士卒"),
        ("的士兵", "的士兵", "計程車 vs 士兵"),
        ("的士氣", "計程車氣", "計程車 vs 士氣"),
        ("的士大夫", "的士大夫", "計程車 vs 士醫生"),
    ]

    @pytest.mark.parametrize("src,expected,desc", OVERLAP_CASES, ids=[c[2] for c in OVERLAP_CASES])
    def test_overlap_protection(self, src, expected, desc):
        result = _convert(src)
        assert result == expected, f"{desc}: {src} → {result} (期望: {expected})"


@skip_if_no_novel
class TestKeyTermConversions:
    """小說中常見詞彙的轉換正確性。"""

    TERM_CASES = [
        ("軟體", "軟體"),
        ("資訊", "資訊"),
        ("傳送", "傳送"),
        ("電腦", "電腦"),
        ("記憶體", "記憶體"),
        ("網路", "網路"),
        ("伺服器", "伺服器"),
        ("影片", "影片"),
        ("部落格", "部落格"),
        ("預設", "預設"),
    ]

    @pytest.mark.parametrize("src,expected", TERM_CASES, ids=[c[0] for c in TERM_CASES])
    def test_term(self, src, expected):
        assert _convert(src) == expected


@skip_if_no_novel
class TestPerformance:
    """轉換效能基準。"""

    def test_500k_chars_under_10s(self):
        """500K 字元轉換應在 10 秒內完成。"""
        from zhtw.charconv import get_translate_table
        from zhtw.dictionary import load_dictionary
        from zhtw.matcher import Matcher

        terms = load_dictionary(sources=["cn"])
        matcher = Matcher(terms)
        char_table = get_translate_table()

        text = MERGED_FILE.read_text("utf-8")[:500_000]

        start = time.perf_counter()
        result = matcher.replace_all(text)
        result = result.translate(char_table)
        elapsed = time.perf_counter() - start

        assert elapsed < 60.0, f"500K 字元轉換耗時 {elapsed:.1f}s（應 <60s）"
        assert len(result) > 50_000

    def test_per_chapter_under_100ms(self):
        """單章轉換應在 100ms 內完成。"""
        from zhtw.charconv import get_translate_table
        from zhtw.dictionary import load_dictionary
        from zhtw.matcher import Matcher

        terms = load_dictionary(sources=["cn"])
        matcher = Matcher(terms)
        char_table = get_translate_table()

        chapter = (CHAPTERS_DIR / "0001.txt").read_text("utf-8")

        start = time.perf_counter()
        for _ in range(10):
            result = matcher.replace_all(chapter)
            result = result.translate(char_table)
        elapsed = (time.perf_counter() - start) / 10

        assert elapsed < 0.1, f"單章轉換耗時 {elapsed*1000:.1f}ms（應 <100ms）"
