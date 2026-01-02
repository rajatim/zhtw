#!/bin/bash
# pre-commit hook: 自動將簡體字轉換為繁體
# 統一使用 zhtw 原生排除機制（# zhtw:disable）

set -e

files=("$@")

if [ ${#files[@]} -eq 0 ]; then
    exit 0
fi

PYTHON=""
for py in python3 python; do
    if command -v $py &> /dev/null; then
        PYTHON=$py
        break
    fi
done

if [ -z "$PYTHON" ]; then
    echo "zhtw: Python 未安裝，跳過"
    exit 0
fi

$PYTHON - "${files[@]}" << 'PYTHON_SCRIPT'
import sys
import subprocess
from pathlib import Path

try:
    from zhtw.dictionary import load_dictionary
    from zhtw.matcher import Matcher
    from zhtw.converter import convert_file
except ImportError:
    sys.exit(0)

terms = load_dictionary(sources=["cn", "hk"])
matcher = Matcher(terms)

EXTENSIONS = {".py", ".md", ".txt", ".rst", ".html", ".yaml", ".yml", ".toml"}

modified_files = []

for filepath in sys.argv[1:]:
    path = Path(filepath)

    if path.suffix.lower() not in EXTENSIONS:
        continue

    if not path.exists():
        continue

    # 自動轉換（zhtw 會處理 # zhtw:disable 等排除規則）
    result = convert_file(path, matcher, fix=True)

    if result.modified:
        modified_files.append(filepath)
        print(f"zhtw: 已轉換 {filepath}")

if modified_files:
    # 自動 git add，讓 commit 繼續完成
    subprocess.run(["git", "add"] + modified_files, check=True)
    print(f"zhtw: 共轉換 {len(modified_files)} 個檔案")

sys.exit(0)
PYTHON_SCRIPT
