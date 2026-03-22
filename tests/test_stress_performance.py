"""壓力與效能測試。驗證大規模文字轉換的效能和穩定性。"""
# zhtw:disable  # 測試案例需要簡體字輸入

import time

import pytest

from zhtw.charconv import clear_cache, get_translate_table, load_charmap
from zhtw.dictionary import load_dictionary
from zhtw.matcher import Matcher

# 壓力測試用簡體中文樣本
SAMPLE_TEXT = "这个软件的信息安全系统需要网络服务器来处理计算机的内存数据。"


def _build_text(size_kb: int) -> str:
    """建立指定大小的測試文字（重複樣本至目標大小）。"""
    target_bytes = size_kb * 1024
    repeats = target_bytes // len(SAMPLE_TEXT.encode("utf-8")) + 1
    text = SAMPLE_TEXT * repeats
    # 截斷至接近目標大小
    while len(text.encode("utf-8")) > target_bytes:
        text = text[:-1]
    return text


def _measure_throughput(text: str, matcher: Matcher, char_table: dict) -> float:
    """執行完整轉換管線並回傳吞吐量（KB/s）。"""
    text_bytes = len(text.encode("utf-8"))
    start = time.perf_counter()
    result = matcher.replace_all(text)
    result = result.translate(char_table)
    elapsed = time.perf_counter() - start
    assert len(result) > 0, "轉換結果不應為空"
    if elapsed == 0:
        return float("inf")
    return (text_bytes / 1024) / elapsed


@pytest.fixture(scope="module")
def terms():
    """載入完整詞庫。"""
    return load_dictionary(sources=["cn", "hk"])


@pytest.fixture(scope="module")
def matcher(terms):
    """建立 Aho-Corasick matcher。"""
    return Matcher(terms)


@pytest.fixture(scope="module")
def char_table():
    """取得字元轉換表。"""
    return get_translate_table()


class TestThroughputBenchmarks:
    """不同大小文字的吞吐量基準。"""

    @pytest.mark.parametrize(
        "size_kb, min_throughput_kbs",
        [
            (1, 100),
            (10, 50),
            (100, 20),
            (1000, 5),
        ],
        ids=["1KB", "10KB", "100KB", "1MB"],
    )
    def test_throughput(self, matcher, char_table, size_kb, min_throughput_kbs):
        """驗證 {size_kb}KB 文字的吞吐量 >= {min_throughput_kbs} KB/s。"""
        text = _build_text(size_kb)

        # 暖機：避免首次執行偏差
        _ = matcher.replace_all(text[:100])

        throughput = _measure_throughput(text, matcher, char_table)
        assert (
            throughput >= min_throughput_kbs
        ), f"{size_kb}KB 文字吞吐量 {throughput:.1f} KB/s 低於門檻 {min_throughput_kbs} KB/s"


class TestComponentPerformance:
    """各組件效能。"""

    def test_dictionary_load_time(self):
        """載入 31K 詞彙應在 1 秒內完成。"""
        start = time.perf_counter()
        terms = load_dictionary(sources=["cn", "hk"])
        elapsed = time.perf_counter() - start

        assert len(terms) > 10000, f"詞庫數量不足：{len(terms)}"
        assert elapsed < 1.0, f"載入耗時 {elapsed:.3f}s，超過 1s 門檻"

    def test_charmap_load_time(self):
        """載入字元映射應在 0.1 秒內完成。"""
        clear_cache()
        start = time.perf_counter()
        charmap = load_charmap()
        elapsed = time.perf_counter() - start

        assert len(charmap) > 1000, f"字元映射數量不足：{len(charmap)}"
        assert elapsed < 0.1, f"載入耗時 {elapsed:.3f}s，超過 0.1s 門檻"

    def test_matcher_build_time(self):
        """建立 Aho-Corasick 自動機應在 2 秒內完成。"""
        terms = load_dictionary(sources=["cn", "hk"])

        start = time.perf_counter()
        m = Matcher(terms)
        elapsed = time.perf_counter() - start

        assert m is not None
        assert elapsed < 2.0, f"建立自動機耗時 {elapsed:.3f}s，超過 2s 門檻"

    def test_char_translate_only(self, char_table):
        """100KB 文字的 str.translate 應在 50ms 內完成。"""
        text = _build_text(100)

        start = time.perf_counter()
        result = text.translate(char_table)
        elapsed = time.perf_counter() - start

        assert len(result) > 0
        assert elapsed < 0.05, f"字元轉換耗時 {elapsed:.3f}s，超過 50ms 門檻"

    def test_term_matching_only(self, matcher):
        """100KB 文字的 matcher.replace_all 應在 5 秒內完成。

        注意：replace_all 內部使用字串切片替換（O(n*m)），
        高密度匹配文字會比實際使用場景慢。門檻設定較寬鬆以適應 CI 環境。
        """
        text = _build_text(100)

        start = time.perf_counter()
        result = matcher.replace_all(text)
        elapsed = time.perf_counter() - start

        assert len(result) > 0
        assert elapsed < 5.0, f"詞彙比對耗時 {elapsed:.3f}s，超過 5s 門檻"


class TestMemoryStability:
    """記憶體穩定性（無洩漏）。"""

    def test_repeated_conversion_stable(self, matcher, char_table):
        """重複轉換同一段文字 100 次，不應崩潰或產生異常。"""
        text = SAMPLE_TEXT * 10

        for i in range(100):
            result = matcher.replace_all(text)
            result = result.translate(char_table)
            assert len(result) > 0, f"第 {i+1} 次轉換結果為空"

    def test_repeated_load_stable(self):
        """重複載入詞庫 10 次，不應有問題。"""
        for i in range(10):
            terms = load_dictionary(sources=["cn", "hk"])
            assert len(terms) > 10000, f"第 {i+1} 次載入詞庫數量異常：{len(terms)}"

    def test_large_batch_sequential(self, matcher, char_table):
        """依序轉換 1000 段不同短文，驗證穩定性。"""
        base_texts = [
            "这个软件需要更新。",
            "服务器的内存不足。",
            "请检查网络连接状态。",
            "数据库备份已完成。",
            "用户信息已经保存。",
        ]

        for i in range(1000):
            text = base_texts[i % len(base_texts)] + f"（第{i}條）"
            result = matcher.replace_all(text)
            result = result.translate(char_table)
            assert len(result) > 0, f"第 {i} 段轉換結果為空"


class TestConcurrentLoad:
    """高負載場景。"""

    def test_rapid_fire(self, matcher, char_table):
        """10,000 次短文轉換，總耗時應在 5 秒內。"""
        short_text = "这是一个简单的测试文本。"

        start = time.perf_counter()
        for _ in range(10_000):
            result = matcher.replace_all(short_text)
            result = result.translate(char_table)
        elapsed = time.perf_counter() - start

        assert elapsed < 5.0, f"10,000 次轉換耗時 {elapsed:.2f}s，超過 5s 門檻"

    def test_mixed_sizes(self, matcher, char_table):
        """交替處理 100 位元組和 10KB 文字，共 100 輪。"""
        small_text = SAMPLE_TEXT[:30]  # 約 100 位元組
        large_text = _build_text(10)  # 10KB

        start = time.perf_counter()
        for _ in range(100):
            r1 = matcher.replace_all(small_text)
            r1 = r1.translate(char_table)

            r2 = matcher.replace_all(large_text)
            r2 = r2.translate(char_table)
        elapsed = time.perf_counter() - start

        assert len(r1) > 0
        assert len(r2) > 0
        # 100 輪混合大小文字不應超過 30 秒
        assert elapsed < 30.0, f"混合大小轉換 100 輪耗時 {elapsed:.2f}s，超過 30s 門檻"


class TestScalingBehavior:
    """效能線性增長驗證。"""

    def test_linear_scaling(self, matcher, char_table):
        """驗證文字大小增長時，處理時間不會爆炸性增長。

        注意：replace_all 使用字串切片替換，在高密度匹配文字下為
        超線性 O(n*m)。此測試驗證 2 倍輸入的耗時比不超過 8 倍，
        確保不會出現指數級退化。
        """
        sizes_kb = [5, 10]
        times = {}

        for size in sizes_kb:
            text = _build_text(size)

            # 取三次中位數減少波動
            measurements = []
            for _ in range(3):
                start = time.perf_counter()
                result = matcher.replace_all(text)
                result = result.translate(char_table)
                elapsed = time.perf_counter() - start
                measurements.append(elapsed)

            times[size] = sorted(measurements)[1]  # 中位數

        time_small = times[5]
        time_large = times[10]

        # 2 倍輸入的耗時比不應超過 8 倍（允許超線性但不可指數級退化）
        if time_small > 0.001:
            ratio = time_large / time_small
            assert ratio < 8.0, (
                f"2 倍文字耗時比為 {ratio:.1f}x（預期 < 8x），"
                f"5KB={time_small:.4f}s, 10KB={time_large:.4f}s"
            )
