#!/usr/bin/env python3
"""
從 OpenCC 和 MediaWiki 匯入簡繁詞彙到 zhtw 詞庫。

資料來源：
  1. OpenCC STPhrases.txt   — ~49K 簡→繁通用詞彙 (Apache-2.0)
  2. OpenCC TWPhrases.txt   — ~520 台灣特定詞彙 (Apache-2.0)
  3. zhconv (MediaWiki)     — ~7K+ 繁體詞彙 + ~964 台灣詞彙 (GPL-2.0+)

用法：
  python scripts/import_opencc.py [--dry-run] [--output PATH]
"""

from __future__ import annotations

import json
import urllib.request
from pathlib import Path

# ── Paths ──

PROJECT_ROOT = Path(__file__).resolve().parent.parent
TERMS_DIR = PROJECT_ROOT / "src" / "zhtw" / "data" / "terms" / "cn"
CHARMAP_FILE = PROJECT_ROOT / "src" / "zhtw" / "data" / "charmap" / "safe_chars.json"
OUTPUT_FILE = TERMS_DIR / "opencc.json"

# ── OpenCC raw URLs (Apache-2.0) ──

OPENCC_BASE = "https://raw.githubusercontent.com/BYVoid/OpenCC/master/data/dictionary"
OPENCC_FILES = {
    "STPhrases": f"{OPENCC_BASE}/STPhrases.txt",
    "TWPhrases": f"{OPENCC_BASE}/TWPhrases.txt",
    "TWVariantsRevPhrases": f"{OPENCC_BASE}/TWVariantsRevPhrases.txt",
}


def download(url: str) -> str:
    """Download text from URL."""
    print(f"  下載 {url.split('/')[-1]} ...", end=" ", flush=True)
    req = urllib.request.Request(url, headers={"User-Agent": "zhtw-importer/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        text = resp.read().decode("utf-8")
    print(f"OK ({len(text):,} bytes)")
    return text


def parse_opencc(text: str) -> dict[str, str]:
    """
    Parse OpenCC tab-separated format.
    Format: simplified\ttraditional1 traditional2 ...
    For one-to-many, take the first value.
    """
    result = {}
    for line in text.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        key = parts[0].strip()
        values = parts[1].strip().split(" ")
        # Take first value (most common/standard)
        val = values[0].strip()
        if key and val:
            result[key] = val
    return result


def load_existing_terms() -> dict[str, str]:
    """Load all existing zhtw terms."""
    all_terms: dict[str, str] = {}
    for json_file in sorted(TERMS_DIR.glob("*.json")):
        if json_file.name == "opencc.json":
            continue  # Skip our own output
        try:
            data = json.loads(json_file.read_text("utf-8"))
            terms = data.get("terms", data)
            for k, v in terms.items():
                if not k.startswith("_comment"):
                    all_terms[k] = v
        except Exception:
            continue
    return all_terms


def load_charmap_keys() -> set[str]:
    """Load character-level mapping keys (single chars already handled)."""
    try:
        data = json.loads(CHARMAP_FILE.read_text("utf-8"))
        return set(data.get("chars", {}).keys())
    except Exception:
        return set()


def try_load_zhconv() -> dict[str, str]:
    """Try to load MediaWiki conversion tables via zhconv package."""
    try:
        import json as _json
        import os

        import zhconv as _zhconv

        pkg_dir = os.path.dirname(_zhconv.__file__)
        dict_file = os.path.join(pkg_dir, "zhcdict.json")
        data = _json.load(open(dict_file, encoding="utf-8"))

        tables = {}

        # zh2Hant: generic simplified→traditional phrases
        zh2hant = data.get("zh2Hant", {})
        for k, v in zh2hant.items():
            if len(k) > 1:  # phrase only
                tables[k] = v
        print(
            f"  zh2Hant: {len(zh2hant):,} entries ({sum(1 for k in zh2hant if len(k)>1):,} phrases)"
        )

        # zh2TW: Taiwan-specific (higher priority, override)
        zh2tw = data.get("zh2TW", {})
        for k, v in zh2tw.items():
            tables[k] = v  # override generic with TW-specific
        print(f"  zh2TW: {len(zh2tw):,} entries")

        print(f"  zhconv 合併: {len(tables):,} entries")
        return tables
    except Exception as e:
        print(f"  zhconv load failed: {e}, skipping MediaWiki data")
        return {}


def filter_terms(
    candidates: dict[str, str],
    existing: dict[str, str],
    charmap_keys: set[str],
) -> tuple[dict[str, str], dict[str, int]]:
    """
    Filter candidate terms with Taiwan conformance check.

    Filters:
    - Identity mappings (key == value)
    - Single-char already in charmap
    - Conflicts with existing terms (existing wins)
    - **Taiwan conformance**: if the candidate value uses non-Taiwan forms
      for subterms that zhtw already knows (e.g., OpenCC 軟件 vs zhtw 軟體)
    """
    filtered = {}
    stats = {
        "identity": 0,
        "charmap_covered": 0,
        "conflict": 0,
        "tw_mismatch": 0,
        "duplicate": 0,
        "accepted": 0,
    }

    import re

    punct_re = re.compile(r"[。，、；：！？「」『』（）《》\[\]【】" "''…—．]")

    # Build existing matcher for Taiwan conformance check
    from zhtw.matcher import Matcher as _Matcher

    existing_matcher = _Matcher(existing)

    for key, val in candidates.items():
        # Skip comments
        if key.startswith("_comment"):
            continue

        # Skip entries with punctuation in key
        if punct_re.search(key):
            stats["identity"] += 1
            continue

        # Skip identity mappings
        if key == val:
            stats["identity"] += 1
            continue

        # Skip single-char if already in charmap
        if len(key) == 1 and key in charmap_keys:
            stats["charmap_covered"] += 1
            continue

        # Skip if already exists in zhtw with same value
        if key in existing and existing[key] == val:
            stats["duplicate"] += 1
            continue

        # Skip if already exists with DIFFERENT value (existing wins)
        if key in existing and existing[key] != val:
            stats["conflict"] += 1
            continue

        # Taiwan conformance check:
        # Convert the key using existing zhtw terms. If the result differs
        # from the candidate value, the candidate uses non-Taiwan forms
        # (e.g., generic 軟件 instead of Taiwan 軟體).
        tw_converted = existing_matcher.replace_all(key)
        if tw_converted != key and tw_converted != val:
            # Existing terms produce a different result → candidate is non-TW
            stats["tw_mismatch"] += 1
            continue

        # Skip if already accepted (earlier source wins)
        if key in filtered:
            continue

        filtered[key] = val
        stats["accepted"] += 1

    return filtered, stats


def main():
    import argparse

    parser = argparse.ArgumentParser(description="匯入 OpenCC 詞彙到 zhtw")
    parser.add_argument("--dry-run", action="store_true", help="只顯示統計，不寫入")
    parser.add_argument("--output", type=Path, default=OUTPUT_FILE, help="輸出路徑")
    args = parser.parse_args()

    print("=" * 60)
    print("  zhtw OpenCC 詞彙匯入工具")
    print("=" * 60)

    # 1. Load existing terms
    print("\n[1/4] 載入現有詞庫...")
    existing = load_existing_terms()
    charmap_keys = load_charmap_keys()
    print(f"  現有詞彙: {len(existing):,}")
    print(f"  字元映射: {len(charmap_keys):,}")

    # 2. Download OpenCC data
    print("\n[2/4] 下載 OpenCC 詞庫...")
    all_candidates: dict[str, str] = {}

    # TWPhrases first (Taiwan-specific, highest priority)
    for name, url in OPENCC_FILES.items():
        try:
            text = download(url)
            parsed = parse_opencc(text)
            print(f"    {name}: {len(parsed):,} entries")
            # TWPhrases overrides STPhrases
            if "TW" in name:
                for k, v in parsed.items():
                    all_candidates[k] = v  # TW takes priority
            else:
                for k, v in parsed.items():
                    if k not in all_candidates:
                        all_candidates[k] = v
        except Exception as e:
            print(f"    {name}: FAILED ({e})")

    print(f"  OpenCC 總計: {len(all_candidates):,}")

    # 3. Try zhconv (MediaWiki)
    print("\n[3/4] 載入 MediaWiki 詞庫...")
    zhconv_terms = try_load_zhconv()
    # MediaWiki TW terms override OpenCC generic
    for k, v in zhconv_terms.items():
        all_candidates[k] = v

    print(f"  合併後總計: {len(all_candidates):,}")

    # 4. Filter
    print("\n[4/4] 過濾與去重...")
    filtered, stats = filter_terms(all_candidates, existing, charmap_keys)

    print(f"  Identity (跳過):     {stats['identity']:,}")
    print(f"  Charmap (跳過):      {stats['charmap_covered']:,}")
    print(f"  重複 (跳過):         {stats['duplicate']:,}")
    print(f"  衝突 (現有優先):     {stats['conflict']:,}")
    print(f"  非台灣用法 (跳過):   {stats['tw_mismatch']:,}")
    print(f"  新增詞彙:            {stats['accepted']:,}")

    # Sort by key for consistent output
    sorted_terms = dict(sorted(filtered.items()))

    print(f"\n{'=' * 60}")
    print(f"  匯入結果: {len(sorted_terms):,} 新詞彙")
    print(f"  合併後總計: {len(existing) + len(sorted_terms):,} 詞彙")
    print(f"{'=' * 60}")

    if args.dry_run:
        print("\n[DRY RUN] 未寫入檔案")
        # Show some samples
        print("\n  前 20 筆範例:")
        for i, (k, v) in enumerate(sorted_terms.items()):
            if i >= 20:
                break
            print(f"    {k} → {v}")
        return

    # Write output
    output_data = {
        "version": "1.0",
        "description": "OpenCC + MediaWiki 匯入詞彙 (Apache-2.0 / GPL-2.0+)",
        "source": "OpenCC STPhrases + TWPhrases + MediaWiki ZhConversion",
        "terms": sorted_terms,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output_data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"\n  已寫入: {args.output}")
    print(f"  檔案大小: {args.output.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()
