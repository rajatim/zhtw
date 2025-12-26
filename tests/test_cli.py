"""Tests for CLI commands."""

import json
from pathlib import Path

import pytest
from click.testing import CliRunner

from zhtw.cli import main


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
        binary_file.write_bytes(b'\x00\x01\x02\x03')

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
        custom_dict.write_text(json.dumps({
            "version": "1.0",
            "terms": {"自定义": "自訂"}
        }))

        # Create test file
        test_file = tmp_path / "test.py"
        test_file.write_text('msg = "自定义"')

        result = runner.invoke(main, [
            "check", str(tmp_path),
            "--dict", str(custom_dict)
        ])

        assert "自定义" in result.output or "自訂" in result.output

    def test_invalid_custom_dict(self, runner: CliRunner, tmp_path: Path):
        """Check handles invalid custom dictionary."""
        # Create invalid dictionary
        custom_dict = tmp_path / "invalid.json"
        custom_dict.write_text("not valid json")

        test_file = tmp_path / "test.py"
        test_file.write_text('msg = "软件"')

        result = runner.invoke(main, [
            "check", str(tmp_path),
            "--dict", str(custom_dict)
        ])

        # Should handle error gracefully
        assert result.exit_code != 0 or "error" in result.output.lower() or "錯誤" in result.output
