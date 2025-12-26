"""Tests for config module."""

import json
import tempfile
from pathlib import Path
from unittest.mock import patch

from zhtw.config import (
    DEFAULT_CONFIG,
    _deep_merge,
    calculate_cost,
    get_pricing,
    load_config,
    reset_config,
    save_config,
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
