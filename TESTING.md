# ZHTW 測試文件

> 測試框架說明、策略與貢獻指南

---

## 測試哲學

> **「寧可少轉，不要錯轉」**

這是 zhtw 的核心設計原則，測試策略也圍繞此展開：

| 優先級 | 測試重點 | 原因 |
|--------|----------|------|
| 1 | **誤轉防護** | 錯誤轉換比漏轉更糟糕 |
| 2 | **Identity Mapping** | 保護不該轉的詞 |
| 3 | **一字多義** | 語境決定轉換結果 |
| 4 | **覆蓋率** | 轉換更多詞彙 |

### 測試設計原則

```
✅ 每個 Bug 都要有對應的迴歸測試
✅ 每個 Identity Mapping 都要有測試保護
✅ 新增詞彙前先寫測試
❌ 不追求 100% 覆蓋率，追求關鍵路徑覆蓋
```

---

## 測試金字塔

```
                    /\
                   /  \     E2E 測試
                  / 5% \    CLI 完整流程、檔案處理
                 /------\
                /        \   整合測試
               /   25%    \  詞庫 + Matcher + Converter
              /------------\
             /              \  單元測試
            /      70%       \ 純函數、獨立模組
           --------------------
```

### 各層測試對應

| 層級 | 檔案 | 說明 |
|------|------|------|
| **單元** | `test_matcher.py` | Matcher 類別方法 |
| **單元** | `test_dictionary.py` | 詞庫載入邏輯 |
| **單元** | `test_encoding.py` | 編碼偵測 |
| **整合** | `test_char_conversion.py` | 詞庫 + Matcher 整合 |
| **整合** | `test_converter.py` | 轉換流程整合 |
| **E2E** | `test_cli.py` | CLI 指令端對端 |

---

## 概覽

| 項目 | 數值 |
|------|------|
| 測試框架 | pytest |
| 測試案例數 | 208 |
| 測試檔案數 | 11 |
| 程式碼行數 | ~2,650 行 |

---

## 執行測試

```bash
# 安裝開發依賴
pip install -e ".[dev]"

# 執行所有測試
pytest

# 執行特定測試檔
pytest tests/test_char_conversion.py

# 執行特定測試類別
pytest tests/test_char_conversion.py::TestFa

# 顯示詳細輸出
pytest -v

# 顯示 print 輸出
pytest -s

# 執行並顯示覆蓋率
pytest --cov=zhtw --cov-report=term-missing
```

---

## 測試分類

### 1. 核心功能測試（單元）

| 檔案 | 行數 | 說明 |
|------|------|------|
| `test_converter.py` | 154 | 轉換核心邏輯 |
| `test_matcher.py` | 127 | 匹配演算法（最長匹配優先） |
| `test_dictionary.py` | 93 | 詞庫載入與合併 |

### 2. 一字多義測試（整合，最重要）

| 檔案 | 行數 | 說明 |
|------|------|------|
| `test_char_conversion.py` | 621 | 一對多字元轉換 |

覆蓋的危險字：

| 簡體 | 繁體變體 | 測試類別 |
|------|----------|----------|
| 發 | 發/髮 | `TestFa` |
| 面 | 面/麵 | `TestMian` |
| 裡 | 裡/裡 | `TestLi` |
| 後 | 後/後 | `TestHou` |
| 複 | 複/復 | `TestFu` |
| 准 | 準/准 | `TestZhun` |
| 範 | 範/範 | `TestFan` |
| 几 | 幾/几 | `TestJi` |
| 雲 | 雲/雲 | `TestYun` |
| 當 | 當 | `TestDang` |
| 髒 | 髒/臟 | `TestZang` |
| 捨 | 捨/捨 | `TestShe` |
| 並 | 並 | `TestBing` |
| 卷 | 捲/卷 | `TestJuan` |
| 須 | 鬚/須 | `TestXu` |
| 胡 | 鬍/胡 | `TestHu` |
| 盡 | 盡/儘 | `TestJin` |
| 于 | 於 | `TestYu2` |
| 游 | 遊/游 | `TestYou` |
| 採 | 採/採 | `TestCai` |
| 表 | 錶/表 | `TestBiao` |
| 症 | 癥/症 | `TestZheng2` |

### 3. 功能測試（E2E）

| 檔案 | 行數 | 說明 |
|------|------|------|
| `test_cli.py` | 324 | CLI 指令（scan, fix, validate） |
| `test_encoding.py` | 185 | 檔案編碼偵測與處理 |
| `test_config.py` | 160 | 設定檔載入 |

### 4. 忽略規則測試

| 檔案 | 行數 | 說明 |
|------|------|------|
| `test_zhtwignore.py` | 223 | `.zhtwignore` 檔案規則 |
| `test_ignore_directives.py` | 271 | 行內 `zhtw:disable` 指令 |

### 5. 其他測試

| 檔案 | 行數 | 說明 |
|------|------|------|
| `test_import_terms.py` | 256 | 詞彙匯入功能 |
| `test_usage.py` | 233 | LLM 用量追蹤 |

---

## 測試模式

### 模式 1：字典匹配測試

測試詞庫中的詞彙是否正確轉換：

```python
def test_common_words(self, matcher: Matcher):
    cases = {
        "软件": "軟體",
        "硬件": "硬體",
    }
    for src, expected in cases.items():
        assert matcher.replace_all(src) == expected
```

### 模式 2：Identity Mapping 測試

測試不該轉換的詞保持不變：

```python
def test_queen_unchanged(self, matcher: Matcher):
    # 皇后的「后」不應轉為「後」
    assert matcher.replace_all("皇后") == "皇后"
```

### 模式 3：混合文本測試

測試完整句子的轉換：

```python
def test_sentence(self, matcher: Matcher):
    cases = {
        "头发被风吹乱了": "頭髮被風吹亂了",
        "游泳之后吃面条": "游泳之後吃麵條",
    }
    for src, expected in cases.items():
        assert matcher.replace_all(src) == expected
```

### 模式 4：無誤轉測試

確保已是繁體的字不會被改動：

```python
def test_no_false_positive(self, matcher: Matcher):
    cases = {
        "測試": "測試",
        "頭髮": "頭髮",
    }
    for src, expected in cases.items():
        assert matcher.replace_all(src) == expected
```

---

## 迴歸測試機制

### Bug → 測試對應

每個修復的 Bug 都應該有對應的測試案例：

```python
class TestRegressions:
    """迴歸測試 - 修復過的 Bug"""

    def test_issue_42_queen_converted(self, matcher: Matcher):
        """Issue #42: 皇后被誤轉為皇後

        修復：新增 identity mapping "皇后" → "皇后"
        """
        assert matcher.replace_all("皇后") == "皇后"

    def test_issue_55_usb_missing(self, matcher: Matcher):
        """Issue #55: 优盘 沒有轉換

        修復：新增 "优盘" → "隨身碟"
        """
        assert matcher.replace_all("优盘") == "隨身碟"
```

### 測試標記

使用 pytest markers 標記迴歸測試：

```python
import pytest

@pytest.mark.regression
@pytest.mark.issue(42)
def test_issue_42_queen_converted(self, matcher: Matcher):
    ...
```

執行特定標記的測試：

```bash
# 只執行迴歸測試
pytest -m regression

# 執行特定 issue 的測試
pytest -m "issue(42)"
```

---

## 量化指標

### 指標定義

| 指標 | 公式 | 說明 |
|------|------|------|
| **精確率 (Precision)** | 正確轉換數 / 總轉換數 | 轉的都對 |
| **召回率 (Recall)** | 正確轉換數 / 應轉換數 | 該轉的都轉了 |
| **誤轉率** | 誤轉數 / 總字數 | 不該轉但轉了 |
| **F1 Score** | 2 × P × R / (P + R) | 綜合指標 |

### zhtw 的目標

```
精確率 > 召回率（寧可少轉，不要錯轉）

目標：
- 精確率：> 99%
- 召回率：> 90%
- 誤轉率：< 0.1%
```

### 量化測試範例

```python
def test_precision_on_corpus(self, matcher: Matcher):
    """測試精確率"""
    test_cases = load_test_corpus("tests/data/corpus.json")

    correct = 0
    total_conversions = 0

    for case in test_cases:
        result = matcher.replace_all(case["input"])
        conversions = count_conversions(case["input"], result)
        correct_conversions = count_correct(result, case["expected"])

        total_conversions += conversions
        correct += correct_conversions

    precision = correct / total_conversions if total_conversions > 0 else 1.0
    assert precision >= 0.99, f"Precision {precision:.2%} below 99%"
```

---

## 效能測試

### 基準測試

```python
import pytest

@pytest.mark.benchmark
class TestPerformance:
    """效能基準測試"""

    def test_small_text_speed(self, matcher: Matcher, benchmark):
        """小文本轉換速度"""
        text = "软件开发文档" * 10  # 60 字
        result = benchmark(matcher.replace_all, text)
        assert result is not None

    def test_large_text_speed(self, matcher: Matcher, benchmark):
        """大文本轉換速度"""
        text = "软件开发文档" * 1000  # 6,000 字
        result = benchmark(matcher.replace_all, text)
        assert result is not None

    def test_dictionary_load_time(self, benchmark):
        """詞庫載入時間"""
        from zhtw.dictionary import load_dictionary
        result = benchmark(load_dictionary, sources=["cn", "hk"])
        assert len(result) > 0
```

### 效能目標

| 操作 | 目標 |
|------|------|
| 詞庫載入 | < 100ms |
| 1,000 字轉換 | < 10ms |
| 10,000 字轉換 | < 100ms |
| 記憶體佔用 | < 50MB |

### 執行效能測試

```bash
# 需要安裝 pytest-benchmark
pip install pytest-benchmark

# 執行效能測試
pytest tests/test_performance.py --benchmark-only
```

---

## 真實語料驗證

### 語料來源

| 來源 | 說明 | 用途 |
|------|------|------|
| GitHub Issues | 用戶回報的誤轉 | 迴歸測試 |
| 新聞文章 | 真實簡體新聞 | 覆蓋率測試 |
| 技術文檔 | README、API 文檔 | 領域測試 |
| 社群媒體 | 微博、知乎 | 口語測試 |

### 語料測試結構

```
tests/
└── data/
    └── corpus/
        ├── news.json        # 新聞語料
        ├── tech.json        # 技術文檔
        ├── social.json      # 社群媒體
        └── regressions.json # 迴歸案例
```

### 語料格式

```json
{
  "corpus": [
    {
      "id": "news_001",
      "source": "新華網",
      "input": "软件开发人员需要...",
      "expected": "軟體開發人員需要...",
      "tags": ["it", "news"]
    }
  ]
}
```

### 語料測試執行

```python
import json
import pytest

class TestCorpus:
    """真實語料測試"""

    @pytest.fixture
    def corpus(self):
        with open("tests/data/corpus/tech.json") as f:
            return json.load(f)["corpus"]

    def test_tech_corpus(self, matcher: Matcher, corpus):
        """技術文檔語料測試"""
        failures = []
        for case in corpus:
            result = matcher.replace_all(case["input"])
            if result != case["expected"]:
                failures.append({
                    "id": case["id"],
                    "input": case["input"],
                    "expected": case["expected"],
                    "actual": result
                })

        assert len(failures) == 0, f"Failed {len(failures)} cases: {failures[:3]}"
```

---

## 進階測試類型（未來）

### 1. 屬性測試 (Property-based Testing)

使用 `hypothesis` 自動生成測試案例：

```python
from hypothesis import given, strategies as st

@given(st.text(alphabet="简体字集", min_size=1, max_size=100))
def test_idempotent(self, matcher: Matcher, text: str):
    """轉換應該是冪等的（轉兩次結果相同）"""
    once = matcher.replace_all(text)
    twice = matcher.replace_all(once)
    assert once == twice
```

### 2. 模糊測試 (Fuzz Testing)

```python
def test_fuzz_no_crash(self, matcher: Matcher):
    """隨機輸入不應導致崩潰"""
    import random
    chars = "简体繁體混合English123!@#"
    for _ in range(1000):
        length = random.randint(0, 1000)
        text = "".join(random.choices(chars, k=length))
        try:
            result = matcher.replace_all(text)
            assert isinstance(result, str)
        except Exception as e:
            pytest.fail(f"Crashed on input: {text[:50]}... Error: {e}")
```

### 3. 快照測試 (Snapshot Testing)

```python
def test_dictionary_snapshot(self, snapshot):
    """詞庫變更追蹤"""
    from zhtw.dictionary import load_dictionary
    terms = load_dictionary(sources=["cn"])
    snapshot.assert_match(json.dumps(terms, sort_keys=True, indent=2))
```

### 4. 比較測試（與 OpenCC 基準）

```python
def test_compare_with_opencc(self, matcher: Matcher):
    """與 OpenCC 結果比較（僅供參考）"""
    import opencc
    cc = opencc.OpenCC('s2twp')

    text = "软件开发"
    zhtw_result = matcher.replace_all(text)
    opencc_result = cc.convert(text)

    # 記錄差異，不強制一致
    if zhtw_result != opencc_result:
        print(f"Diff: zhtw={zhtw_result}, opencc={opencc_result}")
```

---

## 新增測試指南

### 步驟 1：選擇測試檔案

| 測試類型 | 檔案 |
|----------|------|
| 新的一字多義 | `test_char_conversion.py` |
| 匹配演算法 | `test_matcher.py` |
| CLI 功能 | `test_cli.py` |
| 詞庫載入 | `test_dictionary.py` |
| 迴歸測試 | `test_regressions.py`（建議新增） |

### 步驟 2：新增測試類別

```python
class TestNewChar:
    """新字 → X/Y"""

    def test_case_a(self, matcher: Matcher):
        """轉「X」的情況"""
        cases = {
            "词A": "詞A",
            "词B": "詞B",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected

    def test_case_b(self, matcher: Matcher):
        """保持「Y」的情況"""
        cases = {
            "词C": "詞C",
        }
        for src, expected in cases.items():
            assert matcher.replace_all(src) == expected
```

### 步驟 3：執行測試

```bash
# 只執行新測試
pytest tests/test_char_conversion.py::TestNewChar -v

# 確保沒有破壞其他測試
pytest
```

---

## 測試命名規範

### 檔案命名

```
test_{模組名}.py
```

### 類別命名

```python
class Test{功能名}:
    """說明"""
```

### 方法命名

```python
def test_{情境}_{預期結果}(self):
    """docstring 說明"""
```

範例：

```python
def test_fa_hair(self, matcher: Matcher):
    """特例轉「髮」"""
```

---

## Fixture 使用

### 完整詞庫 Matcher

```python
@pytest.fixture
def matcher():
    """建立包含完整詞庫的 matcher"""
    terms = load_dictionary(sources=["cn", "hk"])
    return Matcher(terms)
```

### 自訂詞庫 Matcher

```python
def test_custom(self):
    terms = {"简": "繁"}
    matcher = Matcher(terms)
    assert matcher.replace_all("简") == "繁"
```

---

## 測試檔案標記

所有包含簡體字的測試檔案必須加上禁用標記：

```python
# zhtw:disable  # 測試案例需要簡體字輸入
```

這防止 `zhtw scan` 誤報測試檔案中的簡體字。

---

## 覆蓋率

執行覆蓋率報告：

```bash
pytest --cov=zhtw --cov-report=html
open htmlcov/index.html
```

目標覆蓋率：

| 模組 | 目標 | 說明 |
|------|------|------|
| `converter.py` | >90% | 核心邏輯 |
| `matcher.py` | >90% | 核心邏輯 |
| `dictionary.py` | >80% | 載入邏輯 |
| `cli.py` | >70% | UI 層 |

---

## 持續整合

GitHub Actions 自動執行：

```yaml
# .github/workflows/test.yml
- name: Run tests
  run: pytest --cov=zhtw

- name: Upload coverage
  uses: codecov/codecov-action@v3
```

每次 push 和 PR 都會執行測試。

---

## 常見問題

### Q: 測試失敗但不知道原因？

```bash
# 顯示完整錯誤訊息
pytest -v --tb=long

# 只執行失敗的測試
pytest --lf
```

### Q: 如何測試特定詞彙？

```bash
# 快速測試
python3 -c "
from zhtw.dictionary import load_dictionary
from zhtw.matcher import Matcher
terms = load_dictionary(sources=['cn', 'hk'])
m = Matcher(terms)
print(m.replace_all('你要測試的詞'))
"
```

### Q: 新增詞庫後測試失敗？

1. 檢查是否與現有規則衝突
2. 執行 `zhtw validate` 檢查詞庫
3. 可能需要新增 identity mapping

### Q: 如何新增迴歸測試？

1. 在 `test_char_conversion.py` 或新建 `test_regressions.py`
2. 記錄 Issue 編號和問題描述
3. 確保修復前測試失敗，修復後通過

---

## 相關文件

| 文件 | 說明 |
|------|------|
| [CONTRIBUTING.md](CONTRIBUTING.md) | 貢獻指南 |
| [.claude/guides/deep-testing.md](.claude/guides/deep-testing.md) | 深度測試計畫 |
| [.claude/guides/vocabulary.md](.claude/guides/vocabulary.md) | 詞庫操作指南 |

---

*最後更新：2026-01-03*
