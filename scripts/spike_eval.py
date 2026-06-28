# zhtw:disable  # 比對簡體輸入，不可被自身轉換器轉換
"""Phase 0 精準度 spike — 比對 convert() 與人工盲標 expected。

report-only：印 diff 表 + raw match rate，**不自動分桶**。
每個 mismatch 需人工逐筆裁決：convert 錯 / 標籤錯 / 兩可。
確認為真錯轉的，補進 tests/test_golden_rule_battery.py 或 corpus regressions。

用法：
    uv run python scripts/spike_eval.py --labeled /tmp/spike.json

輸入 JSON 格式（spike_sample.py 產生、人工填好 expected 後）：
    [ { "input": "<簡體句>", "expected": "<台灣正體>" }, ... ]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from zhtw.converter import convert  # noqa: E402


def norm(s: str) -> str:
    """只比 CJK 內容，忽略標點/拉丁/空白差異。"""
    return re.sub(r"[^一-鿿]", "", s)


def char_diffs(expected: str, actual: str) -> str:
    e, a = norm(expected), norm(actual)
    if len(e) != len(a):
        return f"[長度 {len(a)}≠{len(e)}] act={a} exp={e}"
    return "  ".join(f"{ca}≠{ce}" for ce, ca in zip(e, a) if ce != ca)


def main() -> int:
    ap = argparse.ArgumentParser(description="比對 convert() 與盲標 expected（report-only）")
    ap.add_argument("--labeled", type=Path, required=True, help="已盲標的 JSON")
    args = ap.parse_args()

    cases = json.loads(args.labeled.read_text(encoding="utf-8"))
    cases = [c for c in cases if c.get("expected", "").strip()]
    if not cases:
        print("沒有已填 expected 的案例；請先人工盲標。")
        return 0

    mism = 0
    print(f"{'#':>3}  {'狀態':<4} diffs(actual≠expected)")
    print("-" * 64)
    for i, c in enumerate(cases, 1):
        act = convert(c["input"])
        ok = norm(act) == norm(c["expected"])
        mism += 0 if ok else 1
        print(f"{i:>3}  {'OK' if ok else 'XX':<4} {'' if ok else char_diffs(c['expected'], act)}")

    n = len(cases)
    print("-" * 64)
    print(f"總數={n}  相符={n - mism}  不符={mism}  raw match={((n - mism) / n):.0%}")
    print("\n（不符筆需人工裁決：convert 錯 / 標籤錯 / 兩可；真錯轉→補 golden/corpus）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
