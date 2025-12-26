"""Tests for import_terms module."""

import json
import tempfile
from pathlib import Path
from unittest.mock import patch

from zhtw.import_terms import (
    ImportResult,
    import_terms,
    is_simplified_chinese,
    load_from_file,
    save_to_pending,
    validate_term,
)


class TestIsSimplifiedChinese:
    """Test simplified Chinese detection."""

    def test_simplified_chars(self):
        """Test detection of simplified characters."""
        assert is_simplified_chinese("与") is True
        assert is_simplified_chinese("东") is True
        assert is_simplified_chinese("书") is True

    def test_traditional_chars(self):
        """Test traditional characters are not detected."""
        assert is_simplified_chinese("與") is False
        assert is_simplified_chinese("東") is False
        assert is_simplified_chinese("書") is False


class TestValidateTerm:
    """Test term validation."""

    def test_valid_term(self):
        """Test valid term passes validation."""
        is_valid, error = validate_term("软件", "軟體", {})

        assert is_valid is True
        assert error is None

    def test_empty_source(self):
        """Test empty source fails."""
        is_valid, error = validate_term("", "軟體", {})

        assert is_valid is False
        assert "為空" in error

    def test_empty_target(self):
        """Test empty target fails."""
        is_valid, error = validate_term("软件", "", {})

        assert is_valid is False
        assert "為空" in error

    def test_same_source_target(self):
        """Test same source and target fails."""
        is_valid, error = validate_term("軟體", "軟體", {})

        assert is_valid is False
        assert "相同" in error

    def test_too_long(self):
        """Test term too long fails."""
        long_term = "這是一個非常非常非常非常非常非常非常非常長的詞彙超過二十字"
        is_valid, error = validate_term(long_term, "短", {})

        assert is_valid is False
        assert "過長" in error

    def test_non_chinese_source(self):
        """Test non-Chinese source fails."""
        is_valid, error = validate_term("software", "軟體", {})

        assert is_valid is False
        assert "非中文" in error

    def test_conflict_with_existing(self):
        """Test conflict with existing term fails."""
        existing = {"软件": "軟件"}  # Different target
        is_valid, error = validate_term("软件", "軟體", existing)

        assert is_valid is False
        assert "衝突" in error

    def test_no_conflict_same_mapping(self):
        """Test same mapping doesn't conflict."""
        existing = {"软件": "軟體"}
        is_valid, error = validate_term("软件", "軟體", existing)

        assert is_valid is True


class TestLoadFromFile:
    """Test loading from file."""

    def test_load_simple_format(self):
        """Test loading simple format."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump({"软件": "軟體", "硬件": "硬體"}, f, ensure_ascii=False)
            path = Path(f.name)

        try:
            terms = load_from_file(path)

            assert terms == {"软件": "軟體", "硬件": "硬體"}
        finally:
            path.unlink()

    def test_load_terms_format(self):
        """Test loading format with terms key."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            data = {"version": "1.0", "terms": {"软件": "軟體"}}
            json.dump(data, f, ensure_ascii=False)
            path = Path(f.name)

        try:
            terms = load_from_file(path)

            assert terms == {"软件": "軟體"}
        finally:
            path.unlink()

    def test_load_list_format(self):
        """Test loading list format."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            data = [
                {"source": "软件", "target": "軟體"},
                {"source": "硬件", "target": "硬體"},
            ]
            json.dump(data, f, ensure_ascii=False)
            path = Path(f.name)

        try:
            terms = load_from_file(path)

            assert terms == {"软件": "軟體", "硬件": "硬體"}
        finally:
            path.unlink()

    def test_load_nonexistent_file(self):
        """Test loading nonexistent file raises error."""
        from zhtw.import_terms import ImportError

        try:
            load_from_file(Path("/nonexistent/path.json"))
            assert False, "Should have raised error"
        except ImportError as e:
            assert "不存在" in str(e)


class TestImportTerms:
    """Test import_terms function."""

    def test_import_valid_terms(self):
        """Test importing valid terms."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump({"软件": "軟體", "硬件": "硬體"}, f, ensure_ascii=False)
            path = f.name

        try:
            result = import_terms(path)

            assert result.total == 2
            assert result.valid == 2
            assert result.invalid == 0
            assert len(result.terms) == 2
        finally:
            Path(path).unlink()

    def test_import_with_invalid_terms(self):
        """Test importing with some invalid terms."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            data = {
                "软件": "軟體",  # Valid
                "same": "same",  # Invalid: not Chinese
                "相同詞": "相同詞",  # Invalid: same source and target
            }
            json.dump(data, f, ensure_ascii=False)
            path = f.name

        try:
            result = import_terms(path)

            assert result.total == 3
            assert result.valid == 1
            assert result.invalid == 2
            assert len(result.errors) == 2
        finally:
            Path(path).unlink()

    def test_import_without_validation(self):
        """Test importing without validation."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump({"same": "same"}, f, ensure_ascii=False)
            path = f.name

        try:
            result = import_terms(path, validate=False)

            assert result.valid == 1  # Passes without validation
        finally:
            Path(path).unlink()


class TestSaveToPending:
    """Test saving to pending directory."""

    def test_save_to_pending(self):
        """Test saving terms to pending."""
        with tempfile.TemporaryDirectory() as tmpdir:
            pending_dir = Path(tmpdir)

            with patch("zhtw.import_terms.get_pending_dir", return_value=pending_dir):
                terms = {"软件": "軟體"}
                path = save_to_pending(terms, "test-import")

                assert path.exists()
                assert path.name == "test-import.json"

                with open(path, encoding="utf-8") as f:
                    data = json.load(f)

                assert data["terms"] == terms
                assert data["status"] == "pending"

    def test_save_cleans_name(self):
        """Test save cleans up filename."""
        with tempfile.TemporaryDirectory() as tmpdir:
            pending_dir = Path(tmpdir)

            with patch("zhtw.import_terms.get_pending_dir", return_value=pending_dir):
                terms = {"软件": "軟體"}
                path = save_to_pending(terms, "test/file:name")

                # Special characters replaced with underscores
                assert "test_file_name" in path.name


class TestImportResult:
    """Test ImportResult dataclass."""

    def test_default_values(self):
        """Test default values."""
        result = ImportResult()

        assert result.total == 0
        assert result.valid == 0
        assert result.invalid == 0
        assert result.duplicates == 0
        assert result.conflicts == 0
        assert result.errors == []
        assert result.terms == {}
