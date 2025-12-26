"""Tests for dictionary module."""

import json
import tempfile
from pathlib import Path

from zhtw.dictionary import (
    load_builtin,
    load_custom,
    load_dictionary,
    load_json_file,
)


class TestDictionary:
    """Test dictionary loading functions."""

    def test_load_builtin_cn(self):
        """Test loading CN (Simplified) dictionary."""
        terms = load_builtin(sources=["cn"])

        assert len(terms) > 0
        assert "软件" in terms
        assert terms["软件"] == "軟體"

    def test_load_builtin_hk(self):
        """Test loading HK dictionary."""
        terms = load_builtin(sources=["hk"])

        assert len(terms) > 0

    def test_load_builtin_all(self):
        """Test loading all built-in dictionaries."""
        terms = load_builtin()

        # Should have terms from both cn and hk
        assert len(terms) > 0

    def test_load_dictionary_default(self):
        """Test load_dictionary with defaults."""
        terms = load_dictionary()

        assert len(terms) > 0
        assert "软件" in terms

    def test_load_custom_simple_format(self):
        """Test loading custom dictionary with simple format."""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump({"自定义": "自訂"}, f, ensure_ascii=False)
            f.flush()

            terms = load_custom(Path(f.name))

        assert terms == {"自定义": "自訂"}

    def test_load_custom_with_terms_key(self):
        """Test loading custom dictionary with terms key."""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            data = {
                "version": "1.0",
                "terms": {"自定义": "自訂"},
            }
            json.dump(data, f, ensure_ascii=False)
            f.flush()

            terms = load_custom(Path(f.name))

        assert terms == {"自定义": "自訂"}

    def test_load_dictionary_with_custom(self):
        """Test load_dictionary merges custom terms."""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump({"自定义": "自訂"}, f, ensure_ascii=False)
            f.flush()

            terms = load_dictionary(custom_path=Path(f.name))

        # Should have both builtin and custom
        assert "软件" in terms
        assert "自定义" in terms

    def test_load_nonexistent_file(self):
        """Test loading non-existent file returns empty dict."""
        terms = load_json_file(Path("/nonexistent/path.json"))

        assert terms == {}
