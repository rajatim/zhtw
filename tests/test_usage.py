"""Tests for LLM usage tracking module."""

import json
import tempfile
from pathlib import Path
from unittest.mock import patch

from zhtw.llm.usage import UsageTracker


class TestUsageTracker:
    """Test usage tracker."""

    def _create_tracker(self, tmpdir):
        """Create a tracker with a temp directory."""
        usage_file = Path(tmpdir) / "usage.json"
        tracker = UsageTracker()
        tracker.usage_file = usage_file
        return tracker

    def test_empty_usage(self):
        """Test initial empty usage."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tracker = self._create_tracker(tmpdir)

            daily = tracker.get_daily_usage()

            assert daily["input_tokens"] == 0
            assert daily["output_tokens"] == 0
            assert daily["requests"] == 0
            assert daily["cost_usd"] == 0.0

    def test_record_usage(self):
        """Test recording usage."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tracker = self._create_tracker(tmpdir)

            tracker.record(1000, 500, "gemini", "gemini-2.0-flash")

            daily = tracker.get_daily_usage()
            assert daily["input_tokens"] == 1000
            assert daily["output_tokens"] == 500
            assert daily["requests"] == 1
            assert daily["cost_usd"] > 0

    def test_record_multiple(self):
        """Test recording multiple usage events."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tracker = self._create_tracker(tmpdir)

            tracker.record(1000, 500, "gemini", "gemini-2.0-flash")
            tracker.record(2000, 1000, "gemini", "gemini-2.0-flash")

            daily = tracker.get_daily_usage()
            assert daily["input_tokens"] == 3000
            assert daily["output_tokens"] == 1500
            assert daily["requests"] == 2

    def test_get_total_usage(self):
        """Test getting total usage."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tracker = self._create_tracker(tmpdir)

            tracker.record(1000, 500, "gemini", "gemini-2.0-flash")

            total = tracker.get_total_usage()
            assert total["input_tokens"] == 1000
            assert total["requests"] == 1

    def test_reset(self):
        """Test resetting usage."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tracker = self._create_tracker(tmpdir)

            tracker.record(1000, 500, "gemini", "gemini-2.0-flash")
            tracker.reset()

            daily = tracker.get_daily_usage()
            assert daily["requests"] == 0

    def test_check_limits_within(self):
        """Test check limits when within limits."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tracker = self._create_tracker(tmpdir)

            # Mock get_limits to return test limits
            with patch.object(tracker, "get_limits", return_value={
                "daily_requests": 100,
                "daily_cost_usd": 0.10,
                "monthly_cost_usd": 1.00,
            }):
                can_proceed, error = tracker.check_limits()

                assert can_proceed is True
                assert error is None

    def test_check_limits_exceeded(self):
        """Test check limits when exceeded."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tracker = self._create_tracker(tmpdir)

            # Record 100 requests to hit limit
            for _ in range(100):
                tracker.record(100, 50, "gemini", "gemini-2.0-flash")

            with patch.object(tracker, "get_limits", return_value={
                "daily_requests": 100,
                "daily_cost_usd": 10.00,  # High enough not to trigger
                "monthly_cost_usd": 100.00,
            }):
                can_proceed, error = tracker.check_limits()

                assert can_proceed is False
                assert "每日請求上限" in error

    def test_check_limits_force(self):
        """Test force flag bypasses limits."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tracker = self._create_tracker(tmpdir)

            # Record to exceed limits
            for _ in range(100):
                tracker.record(100, 50, "gemini", "gemini-2.0-flash")

            with patch.object(tracker, "get_limits", return_value={
                "daily_requests": 100,
                "daily_cost_usd": 0.10,
                "monthly_cost_usd": 1.00,
            }):
                can_proceed, error = tracker.check_limits(force=True)

                assert can_proceed is True
                assert error is None

    def test_get_warning_none(self):
        """Test no warning when usage is low."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tracker = self._create_tracker(tmpdir)

            with patch.object(tracker, "get_limits", return_value={
                "daily_requests": 100,
                "daily_cost_usd": 0.10,
                "monthly_cost_usd": 1.00,
                "warn_at_percent": 80,
            }):
                warning = tracker.get_warning()

                assert warning is None

    def test_get_warning_when_approaching(self):
        """Test warning when approaching limits."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tracker = self._create_tracker(tmpdir)

            # Record 85 requests (85%)
            for _ in range(85):
                tracker.record(100, 50, "gemini", "gemini-2.0-flash")

            with patch.object(tracker, "get_limits", return_value={
                "daily_requests": 100,
                "daily_cost_usd": 10.00,  # High enough
                "monthly_cost_usd": 100.00,
                "warn_at_percent": 80,
            }):
                warning = tracker.get_warning()

                assert warning is not None
                assert "每日請求" in warning

    def test_format_usage_report(self):
        """Test formatting usage report."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tracker = self._create_tracker(tmpdir)

            tracker.record(1000, 500, "gemini", "gemini-2.0-flash")

            with patch.object(tracker, "get_limits", return_value={
                "daily_requests": 100,
                "daily_cost_usd": 0.10,
                "monthly_cost_usd": 1.00,
            }):
                report = tracker.format_usage_report()

                assert "LLM 用量統計" in report
                assert "今日" in report
                assert "本月" in report

    def test_format_usage_report_json(self):
        """Test formatting usage report as JSON."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tracker = self._create_tracker(tmpdir)

            tracker.record(1000, 500, "gemini", "gemini-2.0-flash")

            with patch.object(tracker, "get_limits", return_value={
                "daily_requests": 100,
                "daily_cost_usd": 0.10,
                "monthly_cost_usd": 1.00,
            }):
                report = tracker.format_usage_report(json_output=True)
                data = json.loads(report)

                assert "daily" in data
                assert "monthly" in data
                assert "total" in data
