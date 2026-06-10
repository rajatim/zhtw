#!/bin/bash
# pre-commit hook: 自動將簡體字轉換為繁體
# 統一使用 zhtw 原生排除機制（# zhtw:disable + .zhtwignore）
#
# 重要：用 PYTHONPATH 指向 repo 的 src/，確保跑的是「當前版本」的
# 程式碼與詞庫。過去直接 import 系統安裝的舊版 zhtw，曾用已修正的
# 舊詞條反覆腐化文件（如 380e5d4 修復的 docs 損毀）。

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

REPO_ROOT=$(git rev-parse --show-toplevel)

PYTHONPATH="$REPO_ROOT/src" $PYTHON - "${files[@]}" << 'PYTHON_SCRIPT'
import sys
import subprocess
from pathlib import Path

try:
    from zhtw.dictionary import load_dictionary
    from zhtw.matcher import Matcher
    from zhtw.converter import (
        convert_file,
        inject_protect_terms,
        is_ignored_by_patterns,
        load_zhtwignore,
    )
except ImportError:
    sys.exit(0)

terms = load_dictionary(sources=["cn", "hk"])
inject_protect_terms(terms, ["cn", "hk"])
matcher = Matcher(terms)

EXTENSIONS = {".py", ".md", ".txt", ".rst", ".html", ".yaml", ".yml", ".toml"}

# pre-commit 的 cwd 是 repo root；尊重 .zhtwignore（過去未讀取，
# 導致 tests/、詞庫範例文件被 hook 錯誤轉換）
repo_root = Path.cwd()
ignore_patterns = load_zhtwignore(repo_root)

modified_files = []

for filepath in sys.argv[1:]:
    path = Path(filepath)

    if path.suffix.lower() not in EXTENSIONS:
        continue

    if not path.exists():
        continue

    if is_ignored_by_patterns(path, repo_root, ignore_patterns):
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
