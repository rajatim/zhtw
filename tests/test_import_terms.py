"""Tests for import_terms module."""
# zhtw:disable  # 測試案例需要簡體字輸入

import json
import tempfile
import urllib.error
from pathlib import Path
from unittest.mock import MagicMock, patch

from zhtw.import_terms import (
    ImportResult,
    delete_pending,
    extract_pending_records,
    extract_pending_terms,
    import_terms,
    is_simplified_chinese,
    list_pending,
    load_from_file,
    load_from_url,
    load_pending,
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

    def test_safe_mixed_technical_terms(self):
        """Approved technical ASCII is allowed when its sequence is unchanged."""
        for source, target in (
            ("USB接口", "USB介面"),
            ("IPv6地址", "IPv6位址"),
            ("3D打印", "3D列印"),
            ("C++程序", "C++程式"),
            ("API/接口", "API/介面"),
        ):
            assert validate_term(source, target, {}) == (True, None)

    def test_supplementary_han_mixed_term(self):
        """Supplementary-plane Han counts as Han, not unsafe punctuation."""
        assert validate_term(f"USB{chr(0x20000)}", f"USB{chr(0x20001)}", {}) == (True, None)

    def test_non_han_sequence_must_stay_identical(self):
        is_valid, error = validate_term("HTTP接口", "HTTPS介面", {})

        assert is_valid is False
        assert "序列不同" in error

    def test_rejects_leading_or_trailing_whitespace(self):
        is_valid, error = validate_term(" USB接口", " USB介面", {})

        assert is_valid is False
        assert "前後空白" in error

    def test_rejects_control_characters(self):
        is_valid, error = validate_term("USB\n接口", "USB\n介面", {})

        assert is_valid is False
        assert "控制字元" in error

    def test_rejects_unapproved_symbols(self):
        for source, target in (("USB(接口)", "USB(介面)"), ("USB😀接口", "USB😀介面")):
            is_valid, error = validate_term(source, target, {})

            assert is_valid is False
            assert "不支援" in error

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

    def test_import_list_format_detects_duplicate_sources(self):
        """Duplicate sources are reported and excluded from pending terms."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(
                [
                    {"source": "软件", "target": "軟體"},
                    {"source": "软件", "target": "軟件"},
                ],
                f,
                ensure_ascii=False,
            )
            path = f.name

        try:
            result = import_terms(path)

            assert result.total == 2
            assert result.duplicates == 1
            assert "重複: 软件" in result.errors
            assert result.invalid == 1
            assert result.terms == {}
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
                path = save_to_pending(
                    terms,
                    "test-import",
                    evidence_source="https://example.com/terms.json",
                )

                assert path.exists()
                assert path.name == "test-import.json"

                with open(path, encoding="utf-8") as f:
                    data = json.load(f)

                assert data["schema_version"] == 2
                assert extract_pending_terms(data) == terms
                records = extract_pending_records(data)
                assert len(records) == 1
                assert records[0].review_status.value == "pending"
                assert records[0].trust_level.value == "imported"
                assert records[0].evidence_source == "https://example.com/terms.json"

                from jsonschema import Draft202012Validator

                schema_path = (
                    Path(__file__).parents[1]
                    / "src"
                    / "zhtw"
                    / "data"
                    / "schemas"
                    / "rule-v2.schema.json"
                )
                schema = json.loads(schema_path.read_text("utf-8"))
                Draft202012Validator(schema).validate(data)

    def test_pending_packet_is_deterministic(self):
        """The same packet name and terms produce byte-identical review data."""
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            terms = {"USB接口": "USB介面", "IPv6地址": "IPv6位址"}
            with patch("zhtw.import_terms.get_pending_dir", return_value=Path(first)):
                first_path = save_to_pending(terms, "packet", evidence_source="fixture")
            with patch("zhtw.import_terms.get_pending_dir", return_value=Path(second)):
                second_path = save_to_pending(terms, "packet", evidence_source="fixture")

            assert first_path.read_bytes() == second_path.read_bytes()

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


class TestLoadFromUrl:
    """Test load_from_url function."""

    def test_load_dict_format(self):
        """Test loading dict format from URL."""
        mock_data = {"软件": "軟體", "硬件": "硬體"}

        mock_resp = MagicMock()
        mock_resp.read.return_value = json.dumps(mock_data).encode()
        mock_resp.__enter__ = MagicMock(return_value=mock_resp)
        mock_resp.__exit__ = MagicMock(return_value=False)

        with patch("urllib.request.urlopen", return_value=mock_resp):
            terms = load_from_url("https://example.com/terms.json")

            assert terms == mock_data

    def test_load_terms_key_format(self):
        """Test loading format with terms key from URL."""
        mock_data = {"version": "1.0", "terms": {"软件": "軟體"}}

        mock_resp = MagicMock()
        mock_resp.read.return_value = json.dumps(mock_data).encode()
        mock_resp.__enter__ = MagicMock(return_value=mock_resp)
        mock_resp.__exit__ = MagicMock(return_value=False)

        with patch("urllib.request.urlopen", return_value=mock_resp):
            terms = load_from_url("https://example.com/terms.json")

            assert terms == {"软件": "軟體"}

    def test_load_list_format(self):
        """Test loading list format from URL."""
        mock_data = [
            {"source": "软件", "target": "軟體"},
            {"source": "硬件", "target": "硬體"},
        ]

        mock_resp = MagicMock()
        mock_resp.read.return_value = json.dumps(mock_data).encode()
        mock_resp.__enter__ = MagicMock(return_value=mock_resp)
        mock_resp.__exit__ = MagicMock(return_value=False)

        with patch("urllib.request.urlopen", return_value=mock_resp):
            terms = load_from_url("https://example.com/terms.json")

            assert terms == {"软件": "軟體", "硬件": "硬體"}

    def test_load_url_error(self):
        """Test URL error handling."""
        from zhtw.import_terms import ImportError

        with patch("urllib.request.urlopen") as mock_urlopen:
            mock_urlopen.side_effect = urllib.error.URLError("Connection refused")

            try:
                load_from_url("https://example.com/terms.json")
                assert False, "Should have raised ImportError"
            except ImportError as e:
                assert "無法載入 URL" in str(e)

    def test_load_json_error(self):
        """Test JSON decode error handling."""
        from zhtw.import_terms import ImportError

        mock_resp = MagicMock()
        mock_resp.read.return_value = b"not valid json"
        mock_resp.__enter__ = MagicMock(return_value=mock_resp)
        mock_resp.__exit__ = MagicMock(return_value=False)

        with patch("urllib.request.urlopen", return_value=mock_resp):
            try:
                load_from_url("https://example.com/terms.json")
                assert False, "Should have raised ImportError"
            except ImportError as e:
                assert "JSON 解析錯誤" in str(e)

    def test_load_unknown_format(self):
        """Test unknown format error handling."""
        from zhtw.import_terms import ImportError

        mock_resp = MagicMock()
        mock_resp.read.return_value = b'"just a string"'
        mock_resp.__enter__ = MagicMock(return_value=mock_resp)
        mock_resp.__exit__ = MagicMock(return_value=False)

        with patch("urllib.request.urlopen", return_value=mock_resp):
            try:
                load_from_url("https://example.com/terms.json")
                assert False, "Should have raised ImportError"
            except ImportError as e:
                assert "無法識別的格式" in str(e)


class TestListPending:
    """Test list_pending function."""

    def test_list_empty_dir(self):
        """Test listing empty pending directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch("zhtw.import_terms.get_pending_dir", return_value=Path(tmpdir)):
                results = list_pending()
                assert results == []

    def test_list_pending_files(self):
        """Test listing pending files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            pending_dir = Path(tmpdir)

            # Create test pending files
            file1 = pending_dir / "test1.json"
            file1.write_text(
                json.dumps(
                    {
                        "terms": {"a": "A", "b": "B"},
                        "description": "Test file 1",
                        "status": "pending",
                    }
                )
            )

            file2 = pending_dir / "test2.json"
            file2.write_text(json.dumps({"terms": {"c": "C"}, "status": "reviewed"}))

            with patch("zhtw.import_terms.get_pending_dir", return_value=pending_dir):
                results = list_pending()

                assert len(results) == 2
                assert results[0]["name"] == "test1.json"
                assert results[0]["terms_count"] == 2
                assert results[0]["description"] == "Test file 1"
                assert results[1]["name"] == "test2.json"
                assert results[1]["terms_count"] == 1

    def test_list_schema_v2_pending_file(self, tmp_path):
        with patch("zhtw.import_terms.get_pending_dir", return_value=tmp_path):
            save_to_pending(
                {"USB接口": "USB介面", "IPv6地址": "IPv6位址"},
                "mixed",
                evidence_source="fixture",
            )
            results = list_pending()

        assert len(results) == 1
        assert results[0]["terms_count"] == 2
        assert results[0]["description"] == "fixture"
        assert results[0]["status"] == "pending"

    def test_list_skips_invalid_json(self):
        """Test listing skips invalid JSON files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            pending_dir = Path(tmpdir)

            # Create valid file
            valid = pending_dir / "valid.json"
            valid.write_text(json.dumps({"terms": {"a": "A"}}))

            # Create invalid file
            invalid = pending_dir / "invalid.json"
            invalid.write_text("not valid json")

            with patch("zhtw.import_terms.get_pending_dir", return_value=pending_dir):
                results = list_pending()

                assert len(results) == 1
                assert results[0]["name"] == "valid.json"


class TestLoadPending:
    """Test load_pending function."""

    def test_load_pending_file(self):
        """Test loading a pending file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            pending_dir = Path(tmpdir)

            # Create test file
            test_file = pending_dir / "test.json"
            test_data = {"terms": {"a": "A"}, "status": "pending"}
            test_file.write_text(json.dumps(test_data))

            with patch("zhtw.import_terms.get_pending_dir", return_value=pending_dir):
                data = load_pending("test")

                assert data == test_data

    def test_load_pending_with_extension(self):
        """Test loading with .json extension."""
        with tempfile.TemporaryDirectory() as tmpdir:
            pending_dir = Path(tmpdir)

            test_file = pending_dir / "test.json"
            test_data = {"terms": {"a": "A"}}
            test_file.write_text(json.dumps(test_data))

            with patch("zhtw.import_terms.get_pending_dir", return_value=pending_dir):
                data = load_pending("test.json")

                assert data == test_data

    def test_load_pending_not_found(self):
        """Test loading nonexistent file raises error."""
        from zhtw.import_terms import ImportError

        with tempfile.TemporaryDirectory() as tmpdir:
            with patch("zhtw.import_terms.get_pending_dir", return_value=Path(tmpdir)):
                try:
                    load_pending("nonexistent")
                    assert False, "Should have raised ImportError"
                except ImportError as e:
                    assert "待審核檔案不存在" in str(e)


class TestDeletePending:
    """Test delete_pending function."""

    def test_delete_pending_file(self):
        """Test deleting a pending file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            pending_dir = Path(tmpdir)

            # Create test file
            test_file = pending_dir / "test.json"
            test_file.write_text("{}")

            with patch("zhtw.import_terms.get_pending_dir", return_value=pending_dir):
                delete_pending("test")

                assert not test_file.exists()

    def test_delete_pending_with_extension(self):
        """Test deleting with .json extension."""
        with tempfile.TemporaryDirectory() as tmpdir:
            pending_dir = Path(tmpdir)

            test_file = pending_dir / "test.json"
            test_file.write_text("{}")

            with patch("zhtw.import_terms.get_pending_dir", return_value=pending_dir):
                delete_pending("test.json")

                assert not test_file.exists()

    def test_delete_nonexistent_no_error(self):
        """Test deleting nonexistent file doesn't raise error."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch("zhtw.import_terms.get_pending_dir", return_value=Path(tmpdir)):
                # Should not raise
                delete_pending("nonexistent")
