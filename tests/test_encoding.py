"""Tests for encoding detection and handling."""

from __future__ import annotations

from pathlib import Path

from zhtw.encoding import (
    EncodingInfo,
    can_represent_traditional,
    normalize_encoding,
    read_file,
    write_file,
)


class TestNormalizeEncoding:
    """Test encoding name normalization."""

    def test_normalize_utf8_variants(self):
        assert normalize_encoding("utf8") == "utf-8"
        assert normalize_encoding("UTF-8") == "utf-8"
        assert normalize_encoding("UTF_8") == "utf-8"

    def test_normalize_big5_variants(self):
        assert normalize_encoding("big-5") == "big5"
        assert normalize_encoding("cp950") == "big5"
        assert normalize_encoding("BIG5") == "big5"

    def test_normalize_gbk_variants(self):
        assert normalize_encoding("gbk") == "gbk"
        assert normalize_encoding("GBK") == "gbk"
        assert normalize_encoding("cp936") == "gbk"


class TestCanRepresentTraditional:
    """Test Traditional Chinese encoding safety check."""

    def test_safe_encodings(self):
        assert can_represent_traditional("utf-8") is True
        assert can_represent_traditional("utf-16") is True
        assert can_represent_traditional("big5") is True
        assert can_represent_traditional("gb18030") is True

    def test_unsafe_encodings(self):
        assert can_represent_traditional("gb2312") is False
        assert can_represent_traditional("gbk") is False
        assert can_represent_traditional("hz") is False

    def test_unknown_utf_encoding(self):
        # Unknown UTF variants should be assumed safe
        assert can_represent_traditional("utf-32") is True


class TestReadWriteFile:
    """Test file reading and writing with encoding support."""

    def test_read_utf8_file(self, tmp_path: Path):
        """Test reading a UTF-8 encoded file."""
        test_file = tmp_path / "test.txt"
        content = "測試文件內容"
        test_file.write_text(content, encoding="utf-8")

        read_content, info = read_file(test_file)

        assert read_content == content
        assert info.encoding == "utf-8"
        assert info.can_represent_traditional is True
        assert info.needs_conversion is False

    def test_read_big5_file(self, tmp_path: Path):
        """Test reading a Big5 encoded file."""
        test_file = tmp_path / "test.txt"
        content = "測試文件內容"
        test_file.write_bytes(content.encode("big5"))

        read_content, info = read_file(test_file)

        assert "測試" in read_content  # Content should be readable
        assert info.can_represent_traditional is True

    def test_read_with_specified_encoding(self, tmp_path: Path):
        """Test reading with explicit encoding."""
        test_file = tmp_path / "test.txt"
        content = "測試文件內容"
        test_file.write_text(content, encoding="utf-8")

        read_content, info = read_file(test_file, encoding="utf-8")

        assert read_content == content
        assert info.encoding == "utf-8"
        assert info.confidence == 1.0  # Full confidence when explicitly specified

    def test_write_file_auto_encoding(self, tmp_path: Path):
        """Test writing file with auto encoding selection."""
        test_file = tmp_path / "test.txt"
        content = "測試文件內容"

        # Write with auto encoding
        used_encoding = write_file(test_file, content, output_encoding="auto")

        # Should default to UTF-8 when no original info
        assert used_encoding == "utf-8"
        assert test_file.read_text(encoding="utf-8") == content

    def test_write_file_force_utf8(self, tmp_path: Path):
        """Test writing file with forced UTF-8."""
        test_file = tmp_path / "test.txt"
        content = "測試文件內容"

        used_encoding = write_file(test_file, content, output_encoding="utf-8")

        assert used_encoding == "utf-8"
        assert test_file.read_text(encoding="utf-8") == content

    def test_write_file_keep_encoding(self, tmp_path: Path):
        """Test writing file while keeping original encoding."""
        test_file = tmp_path / "test.txt"
        content = "測試文件內容"

        # Simulate original Big5 encoding
        original_info = EncodingInfo(
            encoding="big5",
            has_bom=False,
            confidence=1.0,
            can_represent_traditional=True,
        )

        used_encoding = write_file(
            test_file,
            content,
            output_encoding="keep",
            original_info=original_info,
        )

        assert used_encoding == "big5"
        # Verify content is correctly encoded
        assert test_file.read_bytes().decode("big5") == content

    def test_write_file_preserve_bom(self, tmp_path: Path):
        """Test that BOM is preserved when original had BOM."""
        test_file = tmp_path / "test.txt"
        content = "測試文件內容"

        original_info = EncodingInfo(
            encoding="utf-8",
            has_bom=True,
            confidence=1.0,
            can_represent_traditional=True,
        )

        write_file(
            test_file,
            content,
            output_encoding="auto",
            original_info=original_info,
            preserve_bom=True,
        )

        # Check that file starts with BOM
        raw = test_file.read_bytes()
        assert raw.startswith(b"\xef\xbb\xbf") or raw.decode("utf-8").startswith("\ufeff")


class TestEncodingInfo:
    """Test EncodingInfo dataclass."""

    def test_needs_conversion_true(self):
        """Test needs_conversion for unsafe encodings."""
        info = EncodingInfo(
            encoding="gb2312",
            has_bom=False,
            confidence=0.9,
            can_represent_traditional=False,
        )
        assert info.needs_conversion is True

    def test_needs_conversion_false(self):
        """Test needs_conversion for safe encodings."""
        info = EncodingInfo(
            encoding="utf-8",
            has_bom=False,
            confidence=1.0,
            can_represent_traditional=True,
        )
        assert info.needs_conversion is False
