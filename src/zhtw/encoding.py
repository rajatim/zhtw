"""
Encoding detection and handling for zhtw.

Supports automatic detection and conversion of various encodings:
- UTF-8 (with/without BOM)
- UTF-16 LE/BE
- Big5, Big5-HKSCS
- GB2312, GBK, GB18030
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from charset_normalizer import from_path

# Encodings that can fully represent Traditional Chinese
TRADITIONAL_CHINESE_SAFE = frozenset({
    "utf-8",
    "utf-16",
    "utf-16-le",
    "utf-16-be",
    "utf-32",
    "utf-32-le",
    "utf-32-be",
    "big5",
    "big5hkscs",
    "gb18030",
})

# Encodings that cannot fully represent Traditional Chinese
TRADITIONAL_CHINESE_UNSAFE = frozenset({
    "gb2312",
    "gbk",
    "hz",
    "iso-2022-cn",
})

# Encoding aliases for normalization
ENCODING_ALIASES = {
    "utf8": "utf-8",
    "utf16": "utf-16",
    "utf-16le": "utf-16-le",
    "utf-16be": "utf-16-be",
    "big-5": "big5",
    "cp950": "big5",
    "gb2312": "gb2312",
    "gbk": "gbk",
    "cp936": "gbk",
    "gb18030": "gb18030",
}


@dataclass
class EncodingInfo:
    """Information about a file's encoding."""

    encoding: str
    has_bom: bool
    confidence: float
    can_represent_traditional: bool

    @property
    def needs_conversion(self) -> bool:
        """Whether the encoding needs to be converted to represent Traditional Chinese."""
        return not self.can_represent_traditional


def normalize_encoding(encoding: str) -> str:
    """Normalize encoding name to a standard form."""
    enc = encoding.lower().replace("_", "-").replace(" ", "-")
    return ENCODING_ALIASES.get(enc, enc)


def can_represent_traditional(encoding: str) -> bool:
    """Check if an encoding can represent Traditional Chinese characters."""
    enc = normalize_encoding(encoding)
    if enc in TRADITIONAL_CHINESE_SAFE:
        return True
    if enc in TRADITIONAL_CHINESE_UNSAFE:
        return False
    # Unknown encoding, assume it can (UTF-8 variants, etc.)
    return enc.startswith("utf")


def detect_encoding(file_path: Path) -> EncodingInfo:
    """
    Detect the encoding of a file.

    Args:
        file_path: Path to the file to detect.

    Returns:
        EncodingInfo with detected encoding details.
    """
    result = from_path(file_path)
    best = result.best()

    if best is None:
        # Fallback to UTF-8 if detection fails
        return EncodingInfo(
            encoding="utf-8",
            has_bom=False,
            confidence=0.0,
            can_represent_traditional=True,
        )

    encoding = normalize_encoding(best.encoding)

    return EncodingInfo(
        encoding=encoding,
        has_bom=bool(best.bom),
        confidence=best.encoding_aliases[0] if best.encoding_aliases else 1.0,
        can_represent_traditional=can_represent_traditional(encoding),
    )


def read_file(
    file_path: Path,
    encoding: str | None = None,
) -> tuple[str, EncodingInfo]:
    """
    Read a file with automatic or specified encoding detection.

    Args:
        file_path: Path to the file to read.
        encoding: Optional encoding to use. If None, auto-detect.

    Returns:
        Tuple of (file content, encoding info).
    """
    if encoding and encoding != "auto":
        # Use specified encoding
        enc = normalize_encoding(encoding)
        with open(file_path, "r", encoding=enc) as f:
            content = f.read()
        return content, EncodingInfo(
            encoding=enc,
            has_bom=False,
            confidence=1.0,
            can_represent_traditional=can_represent_traditional(enc),
        )

    # Auto-detect encoding
    info = detect_encoding(file_path)

    with open(file_path, "r", encoding=info.encoding, errors="replace") as f:
        content = f.read()

    # Remove BOM if present in content
    if content.startswith("\ufeff"):
        content = content[1:]
        info = EncodingInfo(
            encoding=info.encoding,
            has_bom=True,
            confidence=info.confidence,
            can_represent_traditional=info.can_represent_traditional,
        )

    return content, info


def write_file(
    file_path: Path,
    content: str,
    output_encoding: str = "auto",
    original_info: EncodingInfo | None = None,
    preserve_bom: bool = True,
) -> str:
    """
    Write content to a file with specified encoding handling.

    Args:
        file_path: Path to write to.
        content: Content to write.
        output_encoding: Output encoding strategy:
            - "auto": Keep original if safe, otherwise UTF-8
            - "utf-8": Force UTF-8
            - "keep": Force keep original encoding
            - specific encoding name
        original_info: Original encoding info for "auto" and "keep" modes.
        preserve_bom: Whether to preserve BOM if original had one.

    Returns:
        The encoding used for writing.

    Raises:
        UnicodeEncodeError: If content cannot be encoded with the target encoding.
    """
    # Determine target encoding
    if output_encoding == "auto":
        if original_info and original_info.can_represent_traditional:
            target_encoding = original_info.encoding
        else:
            target_encoding = "utf-8"
    elif output_encoding == "keep":
        if original_info:
            target_encoding = original_info.encoding
        else:
            target_encoding = "utf-8"
    elif output_encoding == "utf-8":
        target_encoding = "utf-8"
    else:
        target_encoding = normalize_encoding(output_encoding)

    # Handle BOM
    write_bom = False
    if preserve_bom and original_info and original_info.has_bom:
        if target_encoding in ("utf-8", "utf-16", "utf-16-le", "utf-16-be"):
            write_bom = True

    # Write file
    with open(file_path, "w", encoding=target_encoding) as f:
        if write_bom:
            f.write("\ufeff")
        f.write(content)

    return target_encoding


def get_encoding_display_name(encoding: str) -> str:
    """Get a user-friendly display name for an encoding."""
    names = {
        "utf-8": "UTF-8",
        "utf-16": "UTF-16",
        "utf-16-le": "UTF-16 LE",
        "utf-16-be": "UTF-16 BE",
        "big5": "Big5",
        "big5hkscs": "Big5-HKSCS",
        "gb2312": "GB2312",
        "gbk": "GBK",
        "gb18030": "GB18030",
    }
    return names.get(normalize_encoding(encoding), encoding.upper())


def get_encoding_status_emoji(info: EncodingInfo) -> str:
    """Get a status emoji for an encoding."""
    if info.can_represent_traditional:
        return "✅"
    else:
        return "❌"
