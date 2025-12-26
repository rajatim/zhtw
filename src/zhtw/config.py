"""Configuration management for zhtw."""

import json
from pathlib import Path
from typing import Any

# Default configuration
DEFAULT_CONFIG = {
    "llm": {
        "provider": "gemini",
        "model": "gemini-2.0-flash",
        "limits": {
            "daily_requests": 100,
            "daily_cost_usd": 0.10,
            "monthly_cost_usd": 1.00,
            "warn_at_percent": 80,
        },
    },
}

# Pricing per million tokens (USD)
PRICING = {
    "gemini": {
        "gemini-2.0-flash": {"input": 0.10, "output": 0.40},
        "gemini-1.5-flash": {"input": 0.075, "output": 0.30},
    },
}


def get_config_dir() -> Path:
    """Get the configuration directory path."""
    config_dir = Path.home() / ".config" / "zhtw"
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir


def get_config_path() -> Path:
    """Get the configuration file path."""
    return get_config_dir() / "config.json"


def load_config() -> dict:
    """Load configuration from file, with defaults."""
    config_path = get_config_path()

    if config_path.exists():
        try:
            with open(config_path, encoding="utf-8") as f:
                user_config = json.load(f)
            # Merge with defaults
            return _deep_merge(DEFAULT_CONFIG.copy(), user_config)
        except (json.JSONDecodeError, IOError):
            return DEFAULT_CONFIG.copy()

    return DEFAULT_CONFIG.copy()


def save_config(config: dict) -> None:
    """Save configuration to file."""
    config_path = get_config_path()
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)


def get_config_value(key: str) -> Any:
    """Get a configuration value by dot-separated key.

    Example: get_config_value("llm.limits.daily_cost_usd")
    """
    config = load_config()
    keys = key.split(".")

    value = config
    for k in keys:
        if isinstance(value, dict) and k in value:
            value = value[k]
        else:
            return None

    return value


def set_config_value(key: str, value: Any) -> None:
    """Set a configuration value by dot-separated key.

    Example: set_config_value("llm.limits.daily_cost_usd", 0.05)
    """
    config = load_config()
    keys = key.split(".")

    # Navigate to the parent
    current = config
    for k in keys[:-1]:
        if k not in current:
            current[k] = {}
        current = current[k]

    # Convert value type if needed
    final_key = keys[-1]
    if final_key in current and isinstance(current[final_key], (int, float)):
        try:
            if isinstance(current[final_key], int):
                value = int(value)
            else:
                value = float(value)
        except (ValueError, TypeError):
            pass

    current[final_key] = value
    save_config(config)


def reset_config() -> None:
    """Reset configuration to defaults."""
    save_config(DEFAULT_CONFIG.copy())


def get_pricing(provider: str, model: str) -> dict:
    """Get pricing for a specific provider and model."""
    return PRICING.get(provider, {}).get(model, {"input": 0, "output": 0})


def calculate_cost(
    input_tokens: int, output_tokens: int, provider: str = "gemini", model: str = "gemini-2.0-flash"
) -> float:
    """Calculate cost in USD for given token counts."""
    pricing = get_pricing(provider, model)
    input_cost = (input_tokens / 1_000_000) * pricing["input"]
    output_cost = (output_tokens / 1_000_000) * pricing["output"]
    return input_cost + output_cost


def _deep_merge(base: dict, override: dict) -> dict:
    """Deep merge two dictionaries."""
    result = base.copy()
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = _deep_merge(result[key], value)
        else:
            result[key] = value
    return result
