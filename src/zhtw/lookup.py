"""
Lookup module for querying conversion results with layer attribution.

Provides word/sentence lookup with detail on which conversion layer
(term dictionary vs character map) is responsible for each change.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

from .matcher import Matcher


@dataclass
class ConversionDetail:
    """單一轉換點的資訊。"""

    source: str
    target: str
    layer: str  # "term" | "char"
    position: int


@dataclass
class LookupResult:
    """一個查詢詞/句的完整結果。"""

    input: str
    output: str
    details: List[ConversionDetail] = field(default_factory=list)
    changed: bool = False


def lookup_word(
    word: str,
    matcher: Matcher,
    char_table: Optional[dict[int, str]] = None,
    ambiguity_mode: str = "strict",
) -> LookupResult:
    """查詢單一詞/句的轉換結果與來源歸因。"""
    if not word:
        return LookupResult(input="", output="", details=[], changed=False)

    details: List[ConversionDetail] = []
    covered = matcher.get_covered_positions(word)

    # 1. 詞彙層：Aho-Corasick 匹配
    for match in matcher.find_matches(word):
        details.append(
            ConversionDetail(
                source=match.source,
                target=match.target,
                layer="term",
                position=match.start,
            )
        )

    # 2. Balanced defaults 層：未被覆蓋的歧義字套用預設值
    #    balanced_defaults 是 CN→TW 對映，char_table 是 CN 啟用的指標
    if ambiguity_mode == "balanced" and char_table is not None:
        from .charconv import get_balanced_defaults

        defaults = get_balanced_defaults()
        if defaults:
            for i, ch in enumerate(word):
                if i not in covered and ch in defaults:
                    details.append(
                        ConversionDetail(
                            source=ch,
                            target=defaults[ch],
                            layer="char",
                            position=i,
                        )
                    )

    # 3. 字元層：逐字掃描未被詞彙層覆蓋的位置
    if char_table:
        for i, ch in enumerate(word):
            if i not in covered:
                cp = ord(ch)
                if cp in char_table and char_table[cp] != ch:
                    details.append(
                        ConversionDetail(
                            source=ch,
                            target=char_table[cp],
                            layer="char",
                            position=i,
                        )
                    )

    # 3. 按位置排序
    details.sort(key=lambda d: d.position)

    # 4. 產生轉換後文字
    output = _build_output(word, details)
    changed = output != word

    return LookupResult(input=word, output=output, details=details, changed=changed)


def _build_output(text: str, details: List[ConversionDetail]) -> str:
    """根據 details 組合轉換後文字。"""
    if not details:
        return text

    parts: list[str] = []
    last_end = 0

    for d in details:
        parts.append(text[last_end : d.position])
        parts.append(d.target)
        last_end = d.position + len(d.source)

    parts.append(text[last_end:])
    return "".join(parts)


def lookup_words(
    words: List[str],
    matcher: Matcher,
    char_table: Optional[dict[int, str]] = None,
    ambiguity_mode: str = "strict",
) -> List[LookupResult]:
    """批次查詢多個詞/句。"""
    return [lookup_word(w, matcher, char_table, ambiguity_mode) for w in words]
