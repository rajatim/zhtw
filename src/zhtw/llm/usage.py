"""Usage tracking and limits for LLM API calls."""

import json
from datetime import datetime
from typing import Optional

from ..config import calculate_cost, get_config_dir, load_config


class UsageLimitError(Exception):
    """Raised when usage limit is reached."""

    pass


class UsageTracker:
    """Track and limit LLM API usage."""

    def __init__(self):
        self.usage_file = get_config_dir() / "usage.json"
        self._ensure_usage_file()

    def _ensure_usage_file(self) -> None:
        """Ensure usage file exists with proper structure."""
        if not self.usage_file.exists():
            self._save_usage(self._empty_usage())

    def _empty_usage(self) -> dict:
        """Return empty usage structure."""
        return {
            "daily": {},
            "monthly": {},
            "total": {
                "input_tokens": 0,
                "output_tokens": 0,
                "requests": 0,
                "cost_usd": 0.0,
            },
        }

    def _load_usage(self) -> dict:
        """Load usage data from file."""
        try:
            with open(self.usage_file, encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return self._empty_usage()

    def _save_usage(self, usage: dict) -> None:
        """Save usage data to file. Raises PermissionError if write is denied."""
        with open(self.usage_file, "w", encoding="utf-8") as f:
            json.dump(usage, f, indent=2, ensure_ascii=False)

    def _today_key(self) -> str:
        """Get today's date key."""
        return datetime.now().strftime("%Y-%m-%d")

    def _month_key(self) -> str:
        """Get current month key."""
        return datetime.now().strftime("%Y-%m")

    def record(
        self,
        input_tokens: int,
        output_tokens: int,
        provider: str = "gemini",
        model: str = "gemini-2.0-flash",
    ) -> None:
        """Record a usage event."""
        usage = self._load_usage()
        cost = calculate_cost(input_tokens, output_tokens, provider, model)

        today = self._today_key()
        month = self._month_key()

        # Initialize daily if needed
        if today not in usage["daily"]:
            usage["daily"][today] = {
                "input_tokens": 0,
                "output_tokens": 0,
                "requests": 0,
                "cost_usd": 0.0,
            }

        # Initialize monthly if needed
        if month not in usage["monthly"]:
            usage["monthly"][month] = {
                "input_tokens": 0,
                "output_tokens": 0,
                "requests": 0,
                "cost_usd": 0.0,
            }

        # Update daily
        usage["daily"][today]["input_tokens"] += input_tokens
        usage["daily"][today]["output_tokens"] += output_tokens
        usage["daily"][today]["requests"] += 1
        usage["daily"][today]["cost_usd"] += cost

        # Update monthly
        usage["monthly"][month]["input_tokens"] += input_tokens
        usage["monthly"][month]["output_tokens"] += output_tokens
        usage["monthly"][month]["requests"] += 1
        usage["monthly"][month]["cost_usd"] += cost

        # Update total
        usage["total"]["input_tokens"] += input_tokens
        usage["total"]["output_tokens"] += output_tokens
        usage["total"]["requests"] += 1
        usage["total"]["cost_usd"] += cost

        self._save_usage(usage)

    def get_daily_usage(self) -> dict:
        """Get today's usage."""
        usage = self._load_usage()
        today = self._today_key()
        return usage["daily"].get(
            today,
            {"input_tokens": 0, "output_tokens": 0, "requests": 0, "cost_usd": 0.0},
        )

    def get_monthly_usage(self) -> dict:
        """Get this month's usage."""
        usage = self._load_usage()
        month = self._month_key()
        return usage["monthly"].get(
            month,
            {"input_tokens": 0, "output_tokens": 0, "requests": 0, "cost_usd": 0.0},
        )

    def get_total_usage(self) -> dict:
        """Get total usage."""
        usage = self._load_usage()
        return usage["total"]

    def get_all_usage(self) -> dict:
        """Get all usage data."""
        return self._load_usage()

    def get_limits(self) -> dict:
        """Get current limits from config."""
        config = load_config()
        return config.get("llm", {}).get("limits", {})

    def check_limits(self, force: bool = False) -> tuple[bool, Optional[str]]:
        """Check if any limit is reached.

        Returns:
            (can_proceed, error_message)
            - can_proceed: True if within limits or force=True
            - error_message: None if ok, or error message if limit reached
        """
        if force:
            return True, None

        limits = self.get_limits()
        daily = self.get_daily_usage()
        monthly = self.get_monthly_usage()

        # Check daily requests
        daily_requests_limit = limits.get("daily_requests", 100)
        if daily["requests"] >= daily_requests_limit:
            return False, f"已達每日請求上限（{daily_requests_limit} 次）"

        # Check daily cost
        daily_cost_limit = limits.get("daily_cost_usd", 0.10)
        if daily["cost_usd"] >= daily_cost_limit:
            return False, f"已達每日費用上限（${daily_cost_limit:.2f}）"

        # Check monthly cost
        monthly_cost_limit = limits.get("monthly_cost_usd", 1.00)
        if monthly["cost_usd"] >= monthly_cost_limit:
            return False, f"已達每月費用上限（${monthly_cost_limit:.2f}）"

        return True, None

    def get_warning(self) -> Optional[str]:
        """Get warning if approaching limits."""
        limits = self.get_limits()
        daily = self.get_daily_usage()
        monthly = self.get_monthly_usage()
        warn_percent = limits.get("warn_at_percent", 80) / 100

        warnings = []

        # Check daily requests
        daily_requests_limit = limits.get("daily_requests", 100)
        if daily["requests"] >= daily_requests_limit * warn_percent:
            pct = (daily["requests"] / daily_requests_limit) * 100
            req = daily["requests"]
            warnings.append(f"每日請求已達 {pct:.0f}%（{req}/{daily_requests_limit}）")

        # Check daily cost
        daily_cost_limit = limits.get("daily_cost_usd", 0.10)
        if daily["cost_usd"] >= daily_cost_limit * warn_percent:
            pct = (daily["cost_usd"] / daily_cost_limit) * 100
            cost = daily["cost_usd"]
            warnings.append(f"每日費用已達 {pct:.0f}%（${cost:.4f}/${daily_cost_limit:.2f}）")

        # Check monthly cost
        monthly_cost_limit = limits.get("monthly_cost_usd", 1.00)
        if monthly["cost_usd"] >= monthly_cost_limit * warn_percent:
            pct = (monthly["cost_usd"] / monthly_cost_limit) * 100
            cost = monthly["cost_usd"]
            warnings.append(f"每月費用已達 {pct:.0f}%（${cost:.4f}/${monthly_cost_limit:.2f}）")

        if warnings:
            return "⚠️ " + "；".join(warnings)
        return None

    def reset(self) -> None:
        """Reset all usage data."""
        self._save_usage(self._empty_usage())

    def format_usage_report(self, json_output: bool = False) -> str:
        """Format usage data for display."""
        daily = self.get_daily_usage()
        monthly = self.get_monthly_usage()
        total = self.get_total_usage()
        limits = self.get_limits()

        if json_output:
            return json.dumps(
                {
                    "daily": daily,
                    "monthly": monthly,
                    "total": total,
                    "limits": limits,
                    "date": self._today_key(),
                    "month": self._month_key(),
                },
                indent=2,
                ensure_ascii=False,
            )

        daily_req_limit = limits.get("daily_requests", 100)
        daily_cost_limit = limits.get("daily_cost_usd", 0.10)
        monthly_cost_limit = limits.get("monthly_cost_usd", 1.00)

        daily_req_pct = (daily["requests"] / daily_req_limit * 100) if daily_req_limit else 0
        daily_cost_pct = (daily["cost_usd"] / daily_cost_limit * 100) if daily_cost_limit else 0
        monthly_cost_pct = 0
        if monthly_cost_limit:
            monthly_cost_pct = monthly["cost_usd"] / monthly_cost_limit * 100

        lines = [
            "📊 LLM 用量統計",
            "━" * 40,
            f"今日 ({self._today_key()}):",
            f"  請求: {daily['requests']} / {daily_req_limit} ({daily_req_pct:.1f}%)",
            f"  費用: ${daily['cost_usd']:.4f} / ${daily_cost_limit:.2f} ({daily_cost_pct:.1f}%)",
            f"  Tokens: {daily['input_tokens']:,} 輸入 / {daily['output_tokens']:,} 輸出",
            "",
            f"本月 ({self._month_key()}):",
            f"  請求: {monthly['requests']}",
            f"  費用: ${monthly['cost_usd']:.4f} / ${monthly_cost_limit:.2f} ({monthly_cost_pct:.1f}%)",  # noqa: E501
            f"  Tokens: {monthly['input_tokens']:,} 輸入 / {monthly['output_tokens']:,} 輸出",
            "",
            "累計:",
            f"  總請求: {total['requests']}",
            f"  總費用: ${total['cost_usd']:.4f}",
            f"  總 Tokens: {total['input_tokens']:,} 輸入 / {total['output_tokens']:,} 輸出",
            "━" * 40,
        ]

        return "\n".join(lines)
