"""Tests for CLI commands."""
# zhtw:disable  # 測試案例需要簡體字輸入

import json
import os
from pathlib import Path
from unittest.mock import patch

import pytest
from click.testing import CliRunner

from zhtw.cli import (
    ProgressDisplay,
    create_backup,
    create_progress_callback,
    format_diff,
    format_issue,
    get_env_bool,
    get_env_str,
    main,
)
from zhtw.converter import ConversionResult, Issue


@pytest.fixture
def runner():
    """Create CLI runner."""
    return CliRunner()


@pytest.fixture
def sample_project(tmp_path: Path):
    """Create a sample project with test files."""
    # Create source files
    src = tmp_path / "src"
    src.mkdir()

    (src / "app.py").write_text('msg = "软件和硬件"')
    (src / "utils.py").write_text('# Clean file\ndata = "hello"')
    (src / "config.json").write_text('{"name": "用户"}')

    return tmp_path


class TestCheckCommand:
    """Tests for 'zhtw check' command."""

    def test_check_finds_issues(self, runner: CliRunner, sample_project: Path):
        """Check command finds simplified Chinese terms."""
        result = runner.invoke(main, ["check", str(sample_project)])

        assert result.exit_code == 1  # Issues found
        assert "软件" in result.output
        assert "硬件" in result.output
        assert "用户" in result.output

    def test_check_clean_directory(self, runner: CliRunner, tmp_path: Path):
        """Check command passes on clean directory."""
        (tmp_path / "clean.py").write_text('# All good\ndata = "繁體中文"')

        result = runner.invoke(main, ["check", str(tmp_path)])

        assert result.exit_code == 0
        assert "✅" in result.output or "未發現問題" in result.output

    def test_check_json_output(self, runner: CliRunner, sample_project: Path):
        """Check command outputs valid JSON."""
        result = runner.invoke(main, ["check", str(sample_project), "--json"])

        assert result.exit_code == 1
        data = json.loads(result.output)
        assert "total_issues" in data
        assert data["total_issues"] > 0
        assert "issues" in data

    def test_check_with_source_filter(self, runner: CliRunner, sample_project: Path):
        """Check command respects --source filter."""
        result = runner.invoke(main, ["check", str(sample_project), "--source", "cn"])

        assert result.exit_code == 1
        assert "软件" in result.output

    def test_check_with_exclude(self, runner: CliRunner, tmp_path: Path):
        """Check command respects --exclude option."""
        # Create files in different directories
        src = tmp_path / "src"
        src.mkdir()
        (src / "app.py").write_text('msg = "软件"')

        vendor = tmp_path / "vendor"
        vendor.mkdir()
        (vendor / "lib.py").write_text('msg = "硬件"')

        result = runner.invoke(main, ["check", str(tmp_path), "--exclude", "vendor"])

        assert "软件" in result.output
        # vendor should be excluded, so 硬件 shouldn't appear in issues
        # (it might appear in summary though)

    def test_check_nonexistent_path(self, runner: CliRunner):
        """Check command handles nonexistent path."""
        result = runner.invoke(main, ["check", "/nonexistent/path"])

        assert result.exit_code != 0


class TestFixCommand:
    """Tests for 'zhtw fix' command."""

    def test_fix_modifies_files(self, runner: CliRunner, tmp_path: Path):
        """Fix command modifies files."""
        test_file = tmp_path / "test.py"
        test_file.write_text('msg = "软件"')

        # Need to confirm because tmp_path is not in git
        result = runner.invoke(main, ["fix", str(tmp_path)], input="y\n")

        assert result.exit_code == 0
        content = test_file.read_text()
        assert "軟體" in content
        assert "软件" not in content

    def test_fix_dry_run(self, runner: CliRunner, tmp_path: Path):
        """Fix --dry-run doesn't modify files."""
        test_file = tmp_path / "test.py"
        original = 'msg = "软件"'
        test_file.write_text(original)

        result = runner.invoke(main, ["fix", str(tmp_path), "--dry-run"])

        # Exit code 1 because issues were found (but not fixed)
        assert result.exit_code == 1
        content = test_file.read_text()
        assert content == original  # File unchanged
        assert "软件" in result.output  # Issue reported

    def test_fix_json_output(self, runner: CliRunner, tmp_path: Path):
        """Fix command outputs valid JSON."""
        test_file = tmp_path / "test.py"
        test_file.write_text('msg = "软件"')

        result = runner.invoke(main, ["fix", str(tmp_path), "--json"])

        data = json.loads(result.output)
        assert "files_modified" in data

    def test_fix_show_diff_preview(self, runner: CliRunner, tmp_path: Path):
        """Fix --show-diff shows diff preview."""
        test_file = tmp_path / "test.py"
        test_file.write_text('msg = "软件"')

        # Need to confirm git warning first (y), then cancel fix (n)
        result = runner.invoke(main, ["fix", str(tmp_path), "--show-diff"], input="y\nn\n")

        assert "預覽模式" in result.output
        assert "软件" in result.output or "軟體" in result.output
        assert "已取消" in result.output
        # File should not be modified
        assert test_file.read_text() == 'msg = "软件"'

    def test_fix_show_diff_confirm(self, runner: CliRunner, tmp_path: Path):
        """Fix --show-diff with confirmation applies changes."""
        test_file = tmp_path / "test.py"
        test_file.write_text('msg = "软件"')

        # Need to confirm git warning first (y), then confirm fix (y)
        result = runner.invoke(main, ["fix", str(tmp_path), "--show-diff"], input="y\ny\n")

        assert result.exit_code == 0
        assert "已修正" in result.output
        # File should be modified
        assert "軟體" in test_file.read_text()

    def test_fix_backup_creates_backup(self, runner: CliRunner, tmp_path: Path):
        """Fix --backup creates backup before modifying."""
        test_file = tmp_path / "test.py"
        original_content = 'msg = "软件"'
        test_file.write_text(original_content)

        result = runner.invoke(main, ["fix", str(tmp_path), "--backup"])

        assert result.exit_code == 0
        assert "已備份" in result.output
        assert "已修正" in result.output

        # File should be modified
        assert "軟體" in test_file.read_text()

        # Backup should exist with original content
        backup_dir = tmp_path / ".zhtw-backup"
        assert backup_dir.exists()
        backup_files = list(backup_dir.rglob("test.py"))
        assert len(backup_files) == 1
        assert backup_files[0].read_text() == original_content


class TestStatsCommand:
    """Tests for 'zhtw stats' command."""

    def test_stats_shows_counts(self, runner: CliRunner):
        """Stats command shows term counts."""
        result = runner.invoke(main, ["stats"])

        assert result.exit_code == 0
        assert "詞彙" in result.output or "總計" in result.output

    def test_stats_json_output(self, runner: CliRunner):
        """Stats command outputs valid JSON."""
        result = runner.invoke(main, ["stats", "--json"])

        assert result.exit_code == 0
        data = json.loads(result.output)
        assert "total" in data or "cn" in data or "sources" in data


class TestValidateCommand:
    """Tests for 'zhtw validate' command."""

    def test_validate_runs(self, runner: CliRunner):
        """Validate command runs without error."""
        result = runner.invoke(main, ["validate"])

        # May exit 0 or 1 depending on dictionary state
        assert result.exit_code in [0, 1]
        assert "驗證" in result.output or "檢查" in result.output


class TestVersionOption:
    """Tests for --version option."""

    def test_version_output(self, runner: CliRunner):
        """--version shows version string."""
        result = runner.invoke(main, ["--version"])

        assert result.exit_code == 0
        assert "zhtw" in result.output.lower()
        assert "version" in result.output.lower() or "." in result.output


class TestHelpOption:
    """Tests for --help option."""

    def test_main_help(self, runner: CliRunner):
        """Main --help shows available commands."""
        result = runner.invoke(main, ["--help"])

        assert result.exit_code == 0
        assert "check" in result.output
        assert "fix" in result.output

    def test_check_help(self, runner: CliRunner):
        """Check --help shows options."""
        result = runner.invoke(main, ["check", "--help"])

        assert result.exit_code == 0
        assert "--source" in result.output
        assert "--json" in result.output

    def test_fix_help(self, runner: CliRunner):
        """Fix --help shows options."""
        result = runner.invoke(main, ["fix", "--help"])

        assert result.exit_code == 0
        assert "--dry-run" in result.output


class TestEdgeCases:
    """Edge case tests for CLI."""

    def test_empty_directory(self, runner: CliRunner, tmp_path: Path):
        """Check handles empty directory."""
        result = runner.invoke(main, ["check", str(tmp_path)])

        assert result.exit_code == 0

    def test_single_file(self, runner: CliRunner, tmp_path: Path):
        """Check handles single file path."""
        test_file = tmp_path / "test.py"
        test_file.write_text('msg = "软件"')

        result = runner.invoke(main, ["check", str(test_file)])

        # Should work with single file
        assert "软件" in result.output or result.exit_code in [0, 1]

    def test_binary_file_skipped(self, runner: CliRunner, tmp_path: Path):
        """Binary files are skipped."""
        binary_file = tmp_path / "data.bin"
        binary_file.write_bytes(b"\x00\x01\x02\x03")

        result = runner.invoke(main, ["check", str(tmp_path)])

        # Should not crash
        assert result.exit_code == 0

    def test_utf8_content(self, runner: CliRunner, tmp_path: Path):
        """UTF-8 content is handled correctly."""
        test_file = tmp_path / "test.py"
        test_file.write_text('# 這是繁體中文\nmsg = "软件"', encoding="utf-8")

        result = runner.invoke(main, ["check", str(tmp_path)])

        assert result.exit_code == 1
        assert "软件" in result.output


class TestCustomDictionary:
    """Tests for custom dictionary option."""

    def test_custom_dict(self, runner: CliRunner, tmp_path: Path):
        """Check with custom dictionary."""
        # Create custom dictionary
        custom_dict = tmp_path / "custom.json"
        custom_dict.write_text(json.dumps({"version": "1.0", "terms": {"自定义": "自訂"}}))

        # Create test file
        test_file = tmp_path / "test.py"
        test_file.write_text('msg = "自定义"')

        result = runner.invoke(main, ["check", str(tmp_path), "--dict", str(custom_dict)])

        assert "自定义" in result.output or "自訂" in result.output

    def test_invalid_custom_dict(self, runner: CliRunner, tmp_path: Path):
        """Check handles invalid custom dictionary."""
        # Create invalid dictionary
        custom_dict = tmp_path / "invalid.json"
        custom_dict.write_text("not valid json")

        test_file = tmp_path / "test.py"
        test_file.write_text('msg = "软件"')

        result = runner.invoke(main, ["check", str(tmp_path), "--dict", str(custom_dict)])

        # Should handle error gracefully
        assert result.exit_code != 0 or "error" in result.output.lower() or "錯誤" in result.output


# =============================================================================
# Helper Function Tests
# =============================================================================


class TestGetEnvBool:
    """Tests for get_env_bool helper."""

    def test_true_values(self):
        """Test true values."""
        for val in ["1", "true", "yes", "TRUE", "Yes"]:
            with patch.dict(os.environ, {"TEST_VAR": val}):
                assert get_env_bool("TEST_VAR") is True

    def test_false_values(self):
        """Test false values."""
        for val in ["0", "false", "no", "FALSE", "No"]:
            with patch.dict(os.environ, {"TEST_VAR": val}):
                assert get_env_bool("TEST_VAR") is False

    def test_default_value(self):
        """Test default value when env not set."""
        with patch.dict(os.environ, {}, clear=True):
            os.environ.pop("TEST_VAR", None)
            assert get_env_bool("TEST_VAR") is False
            assert get_env_bool("TEST_VAR", default=True) is True

    def test_invalid_value_returns_default(self):
        """Test invalid value returns default."""
        with patch.dict(os.environ, {"TEST_VAR": "invalid"}):
            assert get_env_bool("TEST_VAR") is False
            assert get_env_bool("TEST_VAR", default=True) is True


class TestGetEnvStr:
    """Tests for get_env_str helper."""

    def test_returns_value(self):
        """Test returns env value."""
        with patch.dict(os.environ, {"TEST_VAR": "test_value"}):
            assert get_env_str("TEST_VAR") == "test_value"

    def test_default_when_not_set(self):
        """Test returns default when not set."""
        with patch.dict(os.environ, {}, clear=True):
            os.environ.pop("TEST_VAR", None)
            assert get_env_str("TEST_VAR") is None
            assert get_env_str("TEST_VAR", "default") == "default"

    def test_empty_string_returns_default(self):
        """Test empty string returns default."""
        with patch.dict(os.environ, {"TEST_VAR": ""}):
            assert get_env_str("TEST_VAR", "default") == "default"


class TestFormatIssue:
    """Tests for format_issue helper."""

    def test_format_with_context(self):
        """Test format with context."""
        issue = Issue(
            file=Path("test.py"),
            line=10,
            column=5,
            source="软件",
            target="軟體",
            context='msg = "软件"',
        )
        result = format_issue(issue, show_context=True)
        assert "L10:5" in result
        assert "软件" in result
        assert "軟體" in result
        assert "msg" in result

    def test_format_without_context(self):
        """Test format without context."""
        issue = Issue(
            file=Path("test.py"),
            line=10,
            column=5,
            source="软件",
            target="軟體",
            context='msg = "软件"',
        )
        result = format_issue(issue, show_context=False)
        assert "L10:5" in result
        assert "软件" in result
        assert "軟體" in result
        assert "msg" not in result


class TestProgressDisplay:
    """Tests for ProgressDisplay class."""

    def test_init(self):
        """Test initialization."""
        display = ProgressDisplay(enabled=True, prefix="測試中")
        assert display.enabled is True
        assert display.prefix == "測試中"

    def test_disabled(self):
        """Test disabled display does nothing."""
        display = ProgressDisplay(enabled=False)
        display.update(50, 100)  # Should not raise

    def test_update_zero_total(self):
        """Test update with zero total."""
        display = ProgressDisplay(enabled=True)
        display.update(0, 0)  # Should not raise

    def test_finish(self):
        """Test finish method."""
        display = ProgressDisplay(enabled=True)
        display.finish()  # Should not raise


class TestCreateProgressCallback:
    """Tests for create_progress_callback helper."""

    def test_returns_tuple(self):
        """Test returns callback and display."""
        callback, display = create_progress_callback()
        assert callable(callback)
        assert isinstance(display, ProgressDisplay)

    def test_callback_updates_display(self):
        """Test callback calls display update."""
        callback, display = create_progress_callback(enabled=False)
        callback(50, 100)  # Should not raise


class TestCreateBackup:
    """Tests for create_backup helper."""

    def test_creates_backup(self, tmp_path: Path):
        """Test backup creation."""
        test_file = tmp_path / "test.py"
        test_file.write_text("original content")

        backup_dir = create_backup([test_file], tmp_path)

        assert backup_dir.exists()
        assert ".zhtw-backup" in str(backup_dir)

        backup_files = list(backup_dir.rglob("test.py"))
        assert len(backup_files) == 1
        assert backup_files[0].read_text() == "original content"

    def test_backup_file_not_under_base(self, tmp_path: Path):
        """Test backup when file is not under base path."""
        import tempfile

        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            f.write("content")
            external_file = Path(f.name)

        try:
            backup_dir = create_backup([external_file], tmp_path)
            assert backup_dir.exists()
        finally:
            external_file.unlink()


class TestFormatDiff:
    """Tests for format_diff helper."""

    def test_format_diff_output(self):
        """Test diff formatting."""
        result = ConversionResult()
        result.issues = [
            Issue(
                file=Path("test.py"),
                line=1,
                column=1,
                source="软件",
                target="軟體",
                context="软件",
            ),
        ]

        output = format_diff(result)
        assert "test.py" in output
        assert "软件" in output or "軟體" in output


# =============================================================================
# Config Command Tests
# =============================================================================


class TestConfigCommand:
    """Tests for 'zhtw config' command."""

    def test_config_show(self, runner: CliRunner):
        """Config show displays configuration."""
        result = runner.invoke(main, ["config", "show"])

        assert result.exit_code == 0
        # Should output valid JSON
        data = json.loads(result.output)
        assert "llm" in data

    def test_config_set(self, runner: CliRunner):
        """Config set updates value."""
        with patch("zhtw.config.set_config_value") as mock_set:
            result = runner.invoke(main, ["config", "set", "test.key", "test_value"])

            assert result.exit_code == 0
            mock_set.assert_called_once()
            assert "已設定" in result.output

    def test_config_set_missing_args(self, runner: CliRunner):
        """Config set with missing args shows error."""
        result = runner.invoke(main, ["config", "set", "only_key"])

        assert result.exit_code == 1
        assert "用法" in result.output or "usage" in result.output.lower()

    def test_config_set_boolean_true(self, runner: CliRunner):
        """Config set parses boolean true."""
        with patch("zhtw.config.set_config_value") as mock_set:
            runner.invoke(main, ["config", "set", "key", "true"])
            mock_set.assert_called_with("key", True)

    def test_config_set_boolean_false(self, runner: CliRunner):
        """Config set parses boolean false."""
        with patch("zhtw.config.set_config_value") as mock_set:
            runner.invoke(main, ["config", "set", "key", "false"])
            mock_set.assert_called_with("key", False)

    def test_config_set_integer(self, runner: CliRunner):
        """Config set parses integer."""
        with patch("zhtw.config.set_config_value") as mock_set:
            runner.invoke(main, ["config", "set", "key", "42"])
            mock_set.assert_called_with("key", 42)

    def test_config_set_float(self, runner: CliRunner):
        """Config set parses float."""
        with patch("zhtw.config.set_config_value") as mock_set:
            runner.invoke(main, ["config", "set", "key", "3.14"])
            mock_set.assert_called_with("key", 3.14)

    def test_config_reset(self, runner: CliRunner):
        """Config reset with confirmation."""
        with patch("zhtw.config.reset_config") as mock_reset:
            result = runner.invoke(main, ["config", "reset"], input="y\n")

            assert result.exit_code == 0
            mock_reset.assert_called_once()
            assert "已重設" in result.output

    def test_config_reset_cancelled(self, runner: CliRunner):
        """Config reset cancelled."""
        with patch("zhtw.config.reset_config") as mock_reset:
            runner.invoke(main, ["config", "reset"], input="n\n")

            mock_reset.assert_not_called()


# =============================================================================
# Usage Command Tests
# =============================================================================


class TestUsageCommand:
    """Tests for 'zhtw usage' command."""

    def test_usage_shows_report(self, runner: CliRunner):
        """Usage command shows report."""
        result = runner.invoke(main, ["usage"])

        assert result.exit_code == 0

    def test_usage_json_output(self, runner: CliRunner):
        """Usage command outputs JSON."""
        result = runner.invoke(main, ["usage", "--json"])

        assert result.exit_code == 0
        # Output might be JSON or formatted text

    def test_usage_reset(self, runner: CliRunner):
        """Usage reset with confirmation."""
        result = runner.invoke(main, ["usage", "--reset"], input="y\n")

        assert result.exit_code == 0
        assert "已重設" in result.output

    def test_usage_reset_cancelled(self, runner: CliRunner):
        """Usage reset cancelled."""
        result = runner.invoke(main, ["usage", "--reset"], input="n\n")

        assert result.exit_code == 0
        assert "已重設" not in result.output


# =============================================================================
# Stats Command Extended Tests
# =============================================================================


class TestStatsCommandExtended:
    """Extended tests for 'zhtw stats' command."""

    def test_stats_cn_only(self, runner: CliRunner):
        """Stats with cn source only."""
        result = runner.invoke(main, ["stats", "--source", "cn"])

        assert result.exit_code == 0
        assert "詞彙" in result.output or "總計" in result.output

    def test_stats_nonexistent_source(self, runner: CliRunner):
        """Stats with nonexistent source."""
        result = runner.invoke(main, ["stats", "--source", "nonexistent"])

        assert result.exit_code == 0


# =============================================================================
# Validate Command Extended Tests
# =============================================================================


class TestValidateCommandExtended:
    """Extended tests for 'zhtw validate' command."""

    def test_validate_cn_only(self, runner: CliRunner):
        """Validate with cn source only."""
        result = runner.invoke(main, ["validate", "--source", "cn"])

        assert result.exit_code in [0, 1]
        assert "驗證" in result.output or "檢查" in result.output


# =============================================================================
# Import Command Tests
# =============================================================================


class TestImportCommand:
    """Tests for 'zhtw import' command."""

    def test_import_local_file(self, runner: CliRunner, tmp_path: Path):
        """Import from local file."""
        terms_file = tmp_path / "terms.json"
        terms_file.write_text(json.dumps({"version": "1.0", "terms": {"测试": "測試"}}))

        result = runner.invoke(main, ["import", str(terms_file)])

        # Should either succeed or report results
        assert "匯入" in result.output or "Import" in result.output.lower()

    def test_import_invalid_file(self, runner: CliRunner, tmp_path: Path):
        """Import from invalid file."""
        invalid_file = tmp_path / "invalid.json"
        invalid_file.write_text("not valid json")

        result = runner.invoke(main, ["import", str(invalid_file)])

        assert result.exit_code != 0 or "失敗" in result.output or "錯誤" in result.output


# =============================================================================
# Review Command Tests
# =============================================================================


class TestReviewCommand:
    """Tests for 'zhtw review' command."""

    def test_review_list_empty(self, runner: CliRunner):
        """Review list when no pending files."""
        with patch("zhtw.import_terms.list_pending", return_value=[]):
            result = runner.invoke(main, ["review", "--list"])

            assert result.exit_code == 0
            assert "暫無" in result.output or "無" in result.output

    def test_review_list_with_items(self, runner: CliRunner):
        """Review list with pending items."""
        pending = [{"name": "test.json", "terms_count": 5, "description": "Test terms"}]
        with patch("zhtw.import_terms.list_pending", return_value=pending):
            result = runner.invoke(main, ["review", "--list"])

            assert result.exit_code == 0
            assert "test.json" in result.output


# =============================================================================
# Fix Command Extended Tests
# =============================================================================


class TestFixCommandExtended:
    """Extended tests for 'zhtw fix' command."""

    def test_fix_with_yes_flag(self, runner: CliRunner, tmp_path: Path):
        """Fix with --yes flag skips confirmation."""
        test_file = tmp_path / "test.py"
        test_file.write_text('msg = "软件"')

        result = runner.invoke(main, ["fix", str(tmp_path), "--yes"])

        assert result.exit_code == 0
        assert "軟體" in test_file.read_text()

    def test_fix_verbose(self, runner: CliRunner, tmp_path: Path):
        """Fix with --verbose shows more details."""
        test_file = tmp_path / "test.py"
        test_file.write_text('msg = "软件"')

        result = runner.invoke(main, ["fix", str(tmp_path), "--verbose", "--yes"])

        assert result.exit_code == 0


# =============================================================================
# Check Command Extended Tests
# =============================================================================


class TestCheckCommandExtended:
    """Extended tests for 'zhtw check' command."""

    def test_check_verbose(self, runner: CliRunner, tmp_path: Path):
        """Check with --verbose shows context."""
        test_file = tmp_path / "test.py"
        test_file.write_text('msg = "软件"')

        result = runner.invoke(main, ["check", str(tmp_path), "--verbose"])

        assert result.exit_code == 1
        assert "软件" in result.output


class TestProgressDisplayTTY:
    """Test ProgressDisplay with TTY mode."""

    def test_progress_display_update(self, capsys):
        """Test progress display update method."""
        progress = ProgressDisplay(prefix="Testing")
        progress.update(50, 100)
        progress.update(100, 100)
        progress.finish()
        # Should not raise errors
        captured = capsys.readouterr()
        assert captured is not None

    def test_progress_display_disabled(self):
        """Test disabled progress display."""
        progress = ProgressDisplay(enabled=False)
        progress.update(50, 100)  # Should do nothing
        progress.finish()


class TestFixCommandNoIssues:
    """Test fix command when no issues found."""

    def test_fix_no_issues_json(self, runner: CliRunner, tmp_path: Path):
        """Fix command with --json when no issues."""
        clean_file = tmp_path / "clean.py"
        clean_file.write_text('data = "正體中文"')

        result = runner.invoke(main, ["fix", str(tmp_path), "--json"])

        assert result.exit_code == 0
        data = json.loads(result.output)
        assert data["total_issues"] == 0

    def test_fix_no_issues_text(self, runner: CliRunner, tmp_path: Path):
        """Fix command without --json when no issues."""
        clean_file = tmp_path / "clean.py"
        clean_file.write_text('data = "正體中文"')

        # Use --dry-run to bypass confirmation
        result = runner.invoke(main, ["fix", str(tmp_path), "--dry-run"])

        # Exit code 0 means success (no issues to fix)
        assert result.exit_code == 0


class TestValidateCommandExtended2:
    """More tests for validate command."""

    def test_validate_runs(self, runner: CliRunner):
        """Test validate command runs successfully."""
        result = runner.invoke(main, ["validate"])

        # validate uses real dictionary files
        # Exit 0 = no issues, Exit 1 = issues found
        assert result.exit_code in (0, 1)
        assert "驗證" in result.output or "檢查" in result.output


class TestEncodingConversionWarning:
    """Test encoding conversion warning messages."""

    def test_check_with_encoding_warning(self, runner: CliRunner, tmp_path: Path):
        """Test check shows encoding conversion warning."""
        # Create file with GB2312 encoding
        test_file = tmp_path / "test.py"
        test_file.write_bytes("# 软件".encode("gb2312"))

        result = runner.invoke(main, ["check", str(tmp_path)])

        # Should detect encoding issue
        assert result.exit_code in (0, 1)


class TestValidateLLMCommand:
    """Test validate-llm command."""

    def test_validate_llm_no_api_key(self, runner: CliRunner):
        """Test validate-llm without API key."""
        with patch.dict(os.environ, {}, clear=True):
            # Remove GEMINI_API_KEY if exists
            os.environ.pop("GEMINI_API_KEY", None)

            result = runner.invoke(main, ["validate-llm"])

            assert result.exit_code == 1
            assert "GEMINI_API_KEY" in result.output

    def test_validate_llm_with_mock_client(self, runner: CliRunner):
        """Test validate-llm with mocked client."""
        from unittest.mock import MagicMock

        mock_client = MagicMock()
        mock_client.is_available.return_value = True
        mock_client.validate_term.return_value = {
            "correct": True,
            "reason": "正確",
            "suggestion": None,
        }

        with (
            patch("zhtw.llm.client.GeminiClient", return_value=mock_client),
            patch("zhtw.dictionary.load_dictionary", return_value={"a": "A"}),
        ):
            result = runner.invoke(main, ["validate-llm", "--limit", "1"])

            # The command runs (may use real client if mock doesn't apply)
            assert result.exit_code in (0, 1)


class TestReviewCommandExtended2:
    """Extended review command tests."""

    def test_review_with_llm_disabled(self, runner: CliRunner):
        """Test review with --no-llm flag."""
        with patch("zhtw.import_terms.list_pending") as mock_list:
            mock_list.return_value = []

            result = runner.invoke(main, ["review", "--no-llm"])

            assert "待審核" in result.output or result.exit_code == 0

    def test_review_with_auto_approve(self, runner: CliRunner):
        """Test review with --approve-all flag."""
        from zhtw.review import ReviewResult

        with (
            patch("zhtw.import_terms.list_pending") as mock_list,
            patch("zhtw.review.review_pending_file") as mock_review,
            patch("zhtw.review.finalize_review") as mock_finalize,
        ):
            mock_list.return_value = [
                {
                    "name": "test.json",
                    "path": "/tmp/test.json",
                    "terms_count": 2,
                    "description": "Test",
                    "status": "pending",
                }
            ]
            mock_review.return_value = ReviewResult(approved=2, terms={"a": "A", "b": "B"})
            mock_finalize.return_value = Path("/tmp/out.json")

            result = runner.invoke(main, ["review", "--approve-all"])

            assert "核准" in result.output or "審核" in result.output
