#!/bin/bash
# 大奉打更人 簡體中文版 文字擷取腳本
# 來源：hetushu.com（和圖書，簡體版）
# 用途：擷取簡體中文小說作為 zhtw 轉換測試語料
#
# 用法：./scrape_novel.sh [起始章號] [結束章號]
#   ./scrape_novel.sh           → 預設前 30 章
#   ./scrape_novel.sh 1 10      → 第 1~10 章
#   ./scrape_novel.sh 1 915     → 全部章節

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"

BASE_URL="https://www.hetushu.com"
BOOK_ID="5763"
OUTPUT_DIR="$ROOT/tests/data/novel/chapters"
DELAY=2  # 請求間隔(秒)，避免被封鎖

START_CH="${1:-1}"
END_CH="${2:-30}"

UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

mkdir -p "$OUTPUT_DIR"

# ── Step 1: 擷取章節目錄 ──────────────────────
echo "=== Step 1: 擷取章節目錄 ==="

INDEX_URL="${BASE_URL}/book/${BOOK_ID}/index.html"
echo "  下載目錄頁: ${INDEX_URL}"

INDEX_HTML=$(curl -s -L -A "$UA" "$INDEX_URL" 2>/dev/null || true)

if [ -z "$INDEX_HTML" ]; then
    echo "錯誤：無法下載目錄頁" >&2
    exit 1
fi

# 擷取章節連結：/book/5763/XXXXXXX.html
LINKS_FILE="$OUTPUT_DIR/_chapter_links.txt"
# 先存全部連結再用 sed 切片，避免 pipefail + head 造成 SIGPIPE
ALL_LINKS=$(echo "$INDEX_HTML" | tr '"' '\n' | grep "^/book/${BOOK_ID}/[0-9]" || true)
echo "$ALL_LINKS" | sed -n "${START_CH},${END_CH}p" > "$LINKS_FILE"

TOTAL=$(wc -l < "$LINKS_FILE" | tr -d ' ')
echo "  擷取範圍: 第 ${START_CH}~${END_CH} 章"
echo "  找到 ${TOTAL} 個章節連結"

if [ "$TOTAL" -eq 0 ]; then
    echo "錯誤：未找到章節連結" >&2
    exit 1
fi

# ── Step 2: 逐章擷取正文 ──────────────────────
echo ""
echo "=== Step 2: 擷取正文（簡體中文）==="

# COUNT 使用絕對章號（START_CH 開始），確保多次執行不覆寫
COUNT=$((START_CH - 1))
while IFS= read -r link; do
    COUNT=$((COUNT + 1))
    outfile="${OUTPUT_DIR}/$(printf '%04d' $COUNT).txt"

    # 斷點續傳：已存在且 >100 bytes 就跳過
    if [ -f "$outfile" ] && [ "$(wc -c < "$outfile" | tr -d ' ')" -gt 100 ]; then
        echo "  [${COUNT}/${TOTAL}] 跳過 (已存在)"
        continue
    fi

    echo -n "  [${COUNT}/${TOTAL}] 擷取中..."

    html=$(curl -s -L -A "$UA" "${BASE_URL}${link}" 2>/dev/null || true)

    if [ -z "$html" ]; then
        echo " 失敗"
        continue
    fi

    # 用 Python 解析 id="content" 的正文
    python3 -c "
import re, sys, html as htmlmod

raw = sys.stdin.read()

# 擷取標題
t = re.search(r'class=\"title\">(.*?)</div>', raw, re.S)
if not t:
    t = re.search(r'<h2 class=\"h2\">(.*?)</h2>', raw, re.S)
if not t:
    t = re.search(r'<h2>(.*?)</h2>', raw, re.S)
title = re.sub(r'<[^>]+>', '', t.group(1)).strip() if t else ''

# 擷取正文內容
m = re.search(r'id=\"content\"[^>]*>(.*?)</div>\s*</div>\s*</div>', raw, re.S)
if not m:
    m = re.search(r'id=\"content\"[^>]*>(.*)', raw, re.S)

if not m:
    print(title or '(無法擷取正文)')
    sys.exit(0)

txt = m.group(1)

# 移除廣告浮水印（<strike>, <samp>, <bdo> 標籤及內容）
txt = re.sub(r'<strike>.*?</strike>', '', txt, flags=re.S)
txt = re.sub(r'<samp>.*?</samp>', '', txt, flags=re.S)
txt = re.sub(r'<bdo>.*?</bdo>', '', txt, flags=re.S)

# 每個 <div> 是一個段落
txt = re.sub(r'<div[^>]*>', '\n', txt)
txt = re.sub(r'</div>', '', txt)
txt = re.sub(r'<br\s*/?>', '\n', txt)
txt = re.sub(r'<h2[^>]*>.*?</h2>', '', txt, flags=re.S)

# 移除剩餘 HTML 標籤
txt = re.sub(r'<[^>]+>', '', txt)
txt = htmlmod.unescape(txt)

lines = [l.strip() for l in txt.split('\n') if l.strip()]
body = '\n'.join(lines)

if title:
    print(title)
    print()
print(body)
" <<< "$html" > "$outfile"

    size=$(wc -c < "$outfile" | tr -d ' ')
    first=$(head -1 "$outfile" 2>/dev/null || echo "")
    if [ "$size" -lt 100 ]; then
        echo " 警告: 內容過短 (${size}B)"
    else
        echo " OK: ${first} (${size}B)"
    fi

    sleep "$DELAY"
done < "$LINKS_FILE"

# ── Step 3: 合併全文 ──────────────────────────
echo ""
echo "=== Step 3: 合併測試語料 ==="

MERGED="$ROOT/tests/data/novel/大奉打更人_简体.txt"
{
    echo "大奉打更人（简体中文测试语料）"
    echo "作者：卖报小郎君"
    echo "来源：hetushu.com"
    echo "用途：zhtw 简繁转换测试"
    echo "========================"
    echo ""
} > "$MERGED"

for f in "$OUTPUT_DIR"/[0-9]*.txt; do
    [ -f "$f" ] || continue
    cat "$f" >> "$MERGED"
    printf "\n---\n\n" >> "$MERGED"
done

FINAL_SIZE=$(du -h "$MERGED" | cut -f1)
echo "  合併完成: ${MERGED} (${FINAL_SIZE})"
echo ""
echo "=== 完成 ==="
echo "  章節目錄: ${OUTPUT_DIR}/"
echo "  合併語料: ${MERGED}"
echo "  章節數量: ${TOTAL}"
