# zhtw:disable  # 內含簡體偵測字元集，且處理簡體語料，不可被自身轉換器轉換
"""Phase 0 精準度 spike — 從 Book 語料抽真實句子供『盲標』。

刻意保留人工的三步工作流：

    1. uv run python scripts/spike_sample.py --count 30 --out /tmp/spike.json
    2. 人工（或獨立 agent，**不可看轉換器輸出**）填好每筆的 "expected"
    3. uv run python scripts/spike_eval.py --labeled /tmp/spike.json

輸出只含 input + 空白 expected，保持盲標、避免錨定偏誤。
讀 gitignored 的 tests/data/corpus/Book；--out 請寫到 repo 外或 gitignored 處
（輸出含簡體 input，勿放進受 hook 監管的路徑）。

為何不自動產生 expected：spike 的價值就在獨立盲標，自動產生會變成
「拿轉換器驗證它自己」。見 docs/plans/2026-06-28-precision-next-phase.md。
"""

from __future__ import annotations

import argparse
import html
import json
import random
import re
import zipfile
from pathlib import Path

DEFAULT_BOOK = Path(__file__).resolve().parents[1] / "tests" / "data" / "corpus" / "Book"

# 高頻「只在簡體出現」的字，用來確認句子確實含簡體（僅過濾，不參與標註）
SIMP = set(
    "这们国见关学实现经给东说对应发后习题电脑网络软际间专业认识结组织"
    "战团员风长乐书买卖钱难样动权术语义讲谈论证据"
)


def extract_text(epub_path: Path) -> str:
    chunks: list[str] = []
    try:
        with zipfile.ZipFile(epub_path) as z:
            for n in z.namelist():
                if n.lower().endswith((".html", ".xhtml", ".htm")):
                    try:
                        raw = z.read(n).decode("utf-8", errors="ignore")
                    except Exception:
                        continue
                    chunks.append(html.unescape(re.sub(r"<[^>]+>", "", raw)))
    except Exception as exc:  # pragma: no cover - 損壞檔案略過
        print(f"  ! 略過 {epub_path.name}: {exc}")
    return "\n".join(chunks)


def split_sentences(text: str, lo: int, hi: int) -> list[str]:
    out: list[str] = []
    for part in re.split(r"(?<=[。！？])", text):
        s = re.sub(r"\s+", "", part.strip())
        if not (lo <= len(s) <= hi) or s[-1] not in "。！？":
            continue
        if not any(c in SIMP for c in s):
            continue
        if any(q in s for q in '"""「」『』（）()0123456789'):
            continue
        out.append(s)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="抽 Book 語料句子供盲標 spike")
    ap.add_argument("--count", type=int, default=30, help="總抽樣句數")
    ap.add_argument("--book-dir", type=Path, default=DEFAULT_BOOK)
    ap.add_argument("--out", type=Path, required=True, help="輸出 JSON（請放 repo 外）")
    ap.add_argument("--min-len", type=int, default=12)
    ap.add_argument("--max-len", type=int, default=42)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    if not args.book_dir.exists():
        print(f"找不到 Book 語料：{args.book_dir}")
        print("請先 git clone zhtw-test-corpus 到 tests/data/corpus")
        return 1

    rng = random.Random(args.seed)
    epubs = sorted(args.book_dir.rglob("*.epub"))
    rng.shuffle(epubs)

    per_book = max(1, args.count // max(1, min(len(epubs), 8)) + 1)
    pools: list[list[str]] = []
    for ep in epubs[:8]:
        sents = split_sentences(extract_text(ep), args.min_len, args.max_len)
        rng.shuffle(sents)
        seen, picked = set(), []
        for s in sents:
            if s not in seen:
                seen.add(s)
                picked.append(s)
            if len(picked) >= per_book:
                break
        if picked:
            pools.append(picked)
        print(f"  {ep.stem}: {len(sents)} 候選 → 取 {len(picked)}")

    # round-robin 取得跨書多樣性
    samples: list[dict] = []
    i = 0
    while len(samples) < args.count and any(len(p) > i for p in pools):
        for p in pools:
            if i < len(p):
                samples.append({"input": p[i], "expected": "", "confidence": ""})
                if len(samples) >= args.count:
                    break
        i += 1

    args.out.write_text(json.dumps(samples, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n寫出 {len(samples)} 句 → {args.out}（請人工盲標 expected 後跑 spike_eval.py）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
