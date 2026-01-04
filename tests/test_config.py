"""Tests for config module."""

import json
import tempfile
from pathlib import Path
from unittest.mock import patch

from zhtw.config import (
    DEFAULT_CONFIG,
    _deep_merge,
    calculate_cost,
    get_config_dir,
    get_config_path,
    get_config_value,
    get_pricing,
    load_config,
    reset_config,
    save_config,
    set_config_value,
)


class TestDeepMerge:
    """Test deep merge helper."""

    def test_simple_merge(self):
        """Test simple dictionary merge."""
        base = {"a": 1, "b": 2}
        override = {"b": 3, "c": 4}
        result = _deep_merge(base, override)

        assert result == {"a": 1, "b": 3, "c": 4}

    def test_nested_merge(self):
        """Test nested dictionary merge."""
        base = {"a": {"x": 1, "y": 2}}
        override = {"a": {"y": 3, "z": 4}}
        result = _deep_merge(base, override)

        assert result == {"a": {"x": 1, "y": 3, "z": 4}}

    def test_base_unchanged(self):
        """Test that base dict is not modified."""
        base = {"a": 1}
        override = {"b": 2}
        _deep_merge(base, override)

        assert base == {"a": 1}


class TestLoadConfig:
    """Test config loading."""

    def test_load_default_config(self):
        """Test loading default config when no file exists."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.json"
            with patch("zhtw.config.get_config_path", return_value=config_path):
                config = load_config()

        assert config == DEFAULT_CONFIG

    def test_load_user_config(self):
        """Test loading user config merges with defaults."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.json"

            # Write user config
            user_config = {"llm": {"model": "custom-model"}}
            with open(config_path, "w") as f:
                json.dump(user_config, f)

            with patch("zhtw.config.get_config_path", return_value=config_path):
                config = load_config()

        # User override applied
        assert config["llm"]["model"] == "custom-model"
        # Defaults preserved
        assert config["llm"]["provider"] == "gemini"
        assert "limits" in config["llm"]

    def test_load_invalid_json(self):
        """Test handling of invalid JSON file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.json"
            config_path.write_text("not valid json")

            with patch("zhtw.config.get_config_path", return_value=config_path):
                config = load_config()

        assert config == DEFAULT_CONFIG


class TestSaveConfig:
    """Test config saving."""

    def test_save_and_load(self):
        """Test saving and loading config."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.json"

            test_config = {"llm": {"model": "test-model"}}

            with patch("zhtw.config.get_config_path", return_value=config_path):
                save_config(test_config)

            with open(config_path, encoding="utf-8") as f:
                loaded = json.load(f)

            assert loaded == test_config


class TestResetConfig:
    """Test config reset."""

    def test_reset_config(self):
        """Test resetting config to defaults."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.json"

            # Write custom config
            with open(config_path, "w") as f:
                json.dump({"custom": "value"}, f)

            with patch("zhtw.config.get_config_path", return_value=config_path):
                reset_config()

            with open(config_path, encoding="utf-8") as f:
                loaded = json.load(f)

            assert loaded == DEFAULT_CONFIG


class TestPricing:
    """Test pricing functions."""

    def test_get_gemini_pricing(self):
        """Test getting Gemini pricing."""
        pricing = get_pricing("gemini", "gemini-2.0-flash")

        assert pricing["input"] == 0.10
        assert pricing["output"] == 0.40

    def test_get_unknown_pricing(self):
        """Test getting pricing for unknown provider."""
        pricing = get_pricing("unknown", "model")

        assert pricing == {"input": 0, "output": 0}

    def test_calculate_cost(self):
        """Test cost calculation."""
        # 1 million input tokens, 1 million output tokens
        cost = calculate_cost(1_000_000, 1_000_000, "gemini", "gemini-2.0-flash")

        # $0.10 for input + $0.40 for output = $0.50
        assert cost == 0.50

    def test_calculate_cost_small(self):
        """Test cost calculation for small token counts."""
        # 1000 input tokens, 500 output tokens
        cost = calculate_cost(1000, 500, "gemini", "gemini-2.0-flash")

        # 0.001 * $0.10 + 0.0005 * $0.40 = $0.0001 + $0.0002 = $0.0003
        assert abs(cost - 0.0003) < 0.00001


class TestGetConfigDir:
    """Test get_config_dir function."""

    def test_get_config_dir_returns_path(self):
        """Test that get_config_dir returns a Path."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch("zhtw.config.Path.home", return_value=Path(tmpdir)):
                config_dir = get_config_dir()
                assert isinstance(config_dir, Path)
                assert config_dir.name == "zhtw"
                assert config_dir.parent.name == ".config"


class TestGetConfigPath:
    """Test get_config_path function."""

    def test_get_config_path_returns_json_path(self):
        """Test that get_config_path returns config.json path."""
        with tempfile.TemporaryDirectory() as tmpdir:
            mock_dir = Path(tmpdir) / ".config" / "zhtw"
            with patch("zhtw.config.get_config_dir", return_value=mock_dir):
                config_path = get_config_path()
                assert config_path.name == "config.json"
                assert config_path.parent == mock_dir


class TestGetConfigValue:
    """Test get_config_value function."""

    def test_get_simple_value(self):
        """Test getting a simple config value."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.json"
            config_path.write_text('{"llm": {"model": "test-model"}}')

            with patch("zhtw.config.get_config_path", return_value=config_path):
                value = get_config_value("llm.model")
                assert value == "test-model"

    def test_get_nested_value(self):
        """Test getting a deeply nested config value."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.json"

            with patch("zhtw.config.get_config_path", return_value=config_path):
                value = get_config_value("llm.limits.daily_requests")
                # From DEFAULT_CONFIG
                assert value == 100

    def test_get_nonexistent_value(self):
        """Test getting a nonexistent config value returns None."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.json"

            with patch("zhtw.config.get_config_path", return_value=config_path):
                value = get_config_value("nonexistent.key")
                assert value is None

    def test_get_value_from_non_dict(self):
        """Test getting a value when parent is not a dict."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.json"
            config_path.write_text('{"llm": "string-value"}')

            with patch("zhtw.config.get_config_path", return_value=config_path):
                value = get_config_value("llm.model")
                assert value is None


class TestSetConfigValue:
    """Test set_config_value function."""

    def test_set_simple_value(self):
        """Test setting a simple config value."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.json"

            with patch("zhtw.config.get_config_path", return_value=config_path):
                set_config_value("llm.model", "new-model")
                value = get_config_value("llm.model")
                assert value == "new-model"

    def test_set_nested_value(self):
        """Test setting a deeply nested config value."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.json"

            with patch("zhtw.config.get_config_path", return_value=config_path):
                set_config_value("llm.limits.daily_requests", 200)
                value = get_config_value("llm.limits.daily_requests")
                assert value == 200

    def test_set_new_key(self):
        """Test setting a new key that doesn't exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.json"

            with patch("zhtw.config.get_config_path", return_value=config_path):
                set_config_value("new.nested.key", "value")
                value = get_config_value("new.nested.key")
                assert value == "value"

    def test_set_value_type_conversion_int(self):
        """Test that int values are preserved."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.json"

            with patch("zhtw.config.get_config_path", return_value=config_path):
                # First set to establish type
                set_config_value("llm.limits.daily_requests", 100)
                # Then set with string that should convert
                set_config_value("llm.limits.daily_requests", "200")
                value = get_config_value("llm.limits.daily_requests")
                assert value == 200
                assert isinstance(value, int)

    def test_set_value_type_conversion_float(self):
        """Test that float values are preserved."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.json"

            with patch("zhtw.config.get_config_path", return_value=config_path):
                # First set to establish type
                set_config_value("llm.limits.daily_cost_usd", 0.10)
                # Then set with string that should convert
                set_config_value("llm.limits.daily_cost_usd", "0.25")
                value = get_config_value("llm.limits.daily_cost_usd")
                assert value == 0.25
                assert isinstance(value, float)

    def test_set_value_invalid_conversion(self):
        """Test that invalid type conversion is handled gracefully."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.json"

            with patch("zhtw.config.get_config_path", return_value=config_path):
                # First set to establish type as int
                set_config_value("llm.limits.daily_requests", 100)
                # Then set with non-numeric string
                set_config_value("llm.limits.daily_requests", "not-a-number")
                value = get_config_value("llm.limits.daily_requests")
                # Should keep the string since conversion failed
                assert value == "not-a-number"
