# 問題排查指南

## 常見問題速查

| 症狀 | 原因 | 解決 |
|------|------|------|
| 「演算法」→「演演算法」| 缺少 identity mapping | 加 `"演算法": "演算法"` |
| 正確的詞被轉換 | 詞庫有誤轉規則 | 移除或加 identity |
| 檔案亂碼 | 編碼偵測錯誤 | 用 `--encoding` 指定 |
| 忽略註解沒效 | 語法錯誤 | 檢查 `zhtw:disable` 格式 |

---

## 誤判問題排查

### 1. 確認是哪個詞造成的

```python
from zhtw.matcher import Matcher
from zhtw.dictionary import load_builtin

# 載入詞庫
terms = load_builtin(["cn", "hk"])
m = Matcher(terms)

# 測試問題文字
text = "這是有問題的文字"
matches = m.find_matches_with_lines(text)
for match in matches:
    print(f"{match.source} → {match.target} at {match.start}")
```

### 2. 判斷修復方式

```
如果是誤轉（不該轉的被轉了）：
  → 加 identity mapping 保護

如果是漏轉（該轉的沒轉）：
  → 加入詞庫

如果是錯轉（轉錯了）：
  → 修改詞庫對應
```

### 3. 驗證修復

```bash
# 測試單一檔案
echo "測試文字" | python -c "
from zhtw.matcher import Matcher
from zhtw.dictionary import load_builtin
import sys
m = Matcher(load_builtin())
print(m.replace_all(sys.stdin.read()))
"
```

---

## 編碼問題排查

### 偵測檔案編碼

```python
from zhtw.encoding import detect_encoding

info = detect_encoding("path/to/file")
print(f"編碼: {info.encoding}")
print(f"信心度: {info.confidence}")
print(f"有 BOM: {info.has_bom}")
```

### 強制指定編碼

```bash
# 輸入編碼
zhtw check file.txt --encoding big5

# 輸出編碼
zhtw fix file.txt --output-encoding utf-8

# 保留原編碼
zhtw fix file.txt --output-encoding keep
```

### 常見編碼對應

| 來源 | 編碼 |
|------|------|
| 簡體中文 Windows | GBK / GB2312 / GB18030 |
| 繁體中文 Windows | Big5 |
| macOS / Linux | UTF-8 |
| 有 BOM 的 UTF-8 | UTF-8-SIG |

---

## 效能問題排查

### 處理速度慢

```bash
# 檢查是否有大量非文字檔案
find . -type f | wc -l

# 使用 --exclude 排除
zhtw check . --exclude "node_modules,dist,*.min.js"
```

### 記憶體使用高

大檔案會佔用較多記憶體，因為要載入整個檔案進行比對。

解決：分割大檔案，或增加系統記憶體。

---

## 忽略註解問題

### 正確語法

```python
# zhtw:disable-line    ← 忽略這一行
x = "软件"              # zhtw:disable-line

# zhtw:disable-next    ← 忽略下一行
# zhtw:disable-next
y = "硬件"

# zhtw:disable         ← 開始忽略區塊
"""
这里的内容不会被转换
"""
# zhtw:enable          ← 結束忽略區塊
```

### 常見錯誤

```python
# ❌ 大小寫錯誤
# ZHTW:disable-line

# ❌ 拼寫錯誤
# zhtw:disable-lines

# ❌ 沒有空格
#zhtw:disable-line

# ✅ 正確
# zhtw:disable-line
```

---

## 測試失敗排查

### pytest 失敗

```bash
# 詳細輸出
pytest -v --tb=long

# 只跑失敗的測試
pytest --lf

# 跑特定測試
pytest tests/test_matcher.py::test_identity_mapping -v
```

### 常見失敗原因

| 錯誤訊息 | 原因 | 解決 |
|---------|------|------|
| `AssertionError: expected X got Y` | 邏輯錯誤 | 檢查程式碼 |
| `ModuleNotFoundError` | 未安裝依賴 | `pip install -e ".[dev]"` |
| `JSONDecodeError` | 詞庫格式錯誤 | 檢查 JSON 語法 |
