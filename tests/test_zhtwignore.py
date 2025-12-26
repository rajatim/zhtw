"""Tests for .zhtwignore functionality."""

from pathlib import Path

from zhtw.converter import (
    is_ignored_by_patterns,
    load_zhtwignore,
)


class TestLoadZhtwignore:
    """Tests for load_zhtwignore function."""

    def test_load_from_current_dir(self, tmp_path: Path):
        """Load .zhtwignore from current directory."""
        ignore_file = tmp_path / ".zhtwignore"
        ignore_file.write_text("tests/\nsrc/data/\n")

        patterns = load_zhtwignore(tmp_path)

        assert patterns == ["tests/", "src/data/"]

    def test_load_empty_file(self, tmp_path: Path):
        """Empty .zhtwignore returns empty list."""
        ignore_file = tmp_path / ".zhtwignore"
        ignore_file.write_text("")

        patterns = load_zhtwignore(tmp_path)

        assert patterns == []

    def test_load_with_comments(self, tmp_path: Path):
        """Comments are skipped."""
        ignore_file = tmp_path / ".zhtwignore"
        ignore_file.write_text("# This is a comment\ntests/\n# Another comment\n")

        patterns = load_zhtwignore(tmp_path)

        assert patterns == ["tests/"]

    def test_load_with_blank_lines(self, tmp_path: Path):
        """Blank lines are skipped."""
        ignore_file = tmp_path / ".zhtwignore"
        ignore_file.write_text("tests/\n\n\nsrc/\n")

        patterns = load_zhtwignore(tmp_path)

        assert patterns == ["tests/", "src/"]

    def test_load_strips_whitespace(self, tmp_path: Path):
        """Whitespace is stripped from patterns."""
        ignore_file = tmp_path / ".zhtwignore"
        ignore_file.write_text("  tests/  \n  src/  \n")

        patterns = load_zhtwignore(tmp_path)

        assert patterns == ["tests/", "src/"]

    def test_no_ignore_file(self, tmp_path: Path):
        """Missing .zhtwignore returns empty list."""
        patterns = load_zhtwignore(tmp_path)

        assert patterns == []

    def test_load_from_parent_dir(self, tmp_path: Path):
        """Search parent directories for .zhtwignore."""
        # Create .zhtwignore in parent
        ignore_file = tmp_path / ".zhtwignore"
        ignore_file.write_text("tests/\n")

        # Create subdirectory
        subdir = tmp_path / "src" / "components"
        subdir.mkdir(parents=True)

        patterns = load_zhtwignore(subdir)

        assert patterns == ["tests/"]


class TestIsIgnoredByPatterns:
    """Tests for is_ignored_by_patterns function."""

    def test_directory_pattern_matches(self, tmp_path: Path):
        """Directory pattern matches files in directory."""
        patterns = ["tests/"]
        file_path = tmp_path / "tests" / "test_foo.py"

        result = is_ignored_by_patterns(file_path, tmp_path, patterns)

        assert result is True

    def test_directory_pattern_nested(self, tmp_path: Path):
        """Directory pattern matches nested files."""
        patterns = ["src/data/terms/"]
        file_path = tmp_path / "src" / "data" / "terms" / "cn" / "base.json"

        result = is_ignored_by_patterns(file_path, tmp_path, patterns)

        assert result is True

    def test_directory_pattern_no_match(self, tmp_path: Path):
        """Directory pattern doesn't match other directories."""
        patterns = ["tests/"]
        file_path = tmp_path / "src" / "main.py"

        result = is_ignored_by_patterns(file_path, tmp_path, patterns)

        assert result is False

    def test_file_pattern_matches(self, tmp_path: Path):
        """File pattern matches specific file."""
        patterns = ["config.json"]
        file_path = tmp_path / "config.json"

        result = is_ignored_by_patterns(file_path, tmp_path, patterns)

        assert result is True

    def test_file_pattern_matches_in_subdir(self, tmp_path: Path):
        """File pattern matches file in subdirectory."""
        patterns = ["*.log"]
        file_path = tmp_path / "logs" / "app.log"

        result = is_ignored_by_patterns(file_path, tmp_path, patterns)

        assert result is True

    def test_glob_pattern_matches(self, tmp_path: Path):
        """Glob pattern matches files."""
        patterns = ["*.pyc"]
        file_path = tmp_path / "module.pyc"

        result = is_ignored_by_patterns(file_path, tmp_path, patterns)

        assert result is True

    def test_glob_pattern_no_match(self, tmp_path: Path):
        """Glob pattern doesn't match non-matching files."""
        patterns = ["*.pyc"]
        file_path = tmp_path / "module.py"

        result = is_ignored_by_patterns(file_path, tmp_path, patterns)

        assert result is False

    def test_empty_patterns(self, tmp_path: Path):
        """Empty patterns list ignores nothing."""
        patterns = []
        file_path = tmp_path / "anything.py"

        result = is_ignored_by_patterns(file_path, tmp_path, patterns)

        assert result is False

    def test_multiple_patterns(self, tmp_path: Path):
        """Multiple patterns work correctly."""
        patterns = ["tests/", "*.log", "temp.txt"]

        # Should match tests/
        assert is_ignored_by_patterns(
            tmp_path / "tests" / "test.py", tmp_path, patterns
        ) is True

        # Should match *.log
        assert is_ignored_by_patterns(
            tmp_path / "app.log", tmp_path, patterns
        ) is True

        # Should match temp.txt
        assert is_ignored_by_patterns(
            tmp_path / "temp.txt", tmp_path, patterns
        ) is True

        # Should not match
        assert is_ignored_by_patterns(
            tmp_path / "src" / "main.py", tmp_path, patterns
        ) is False


class TestZhtwignoreIntegration:
    """Integration tests for .zhtwignore with convert_directory."""

    def test_ignored_files_not_processed(self, tmp_path: Path):
        """Files matching .zhtwignore are not processed."""
        from zhtw.converter import convert_directory
        from zhtw.matcher import Matcher

        # Create .zhtwignore
        ignore_file = tmp_path / ".zhtwignore"
        ignore_file.write_text("ignored/\n")

        # Create test files
        (tmp_path / "ignored").mkdir()
        (tmp_path / "ignored" / "test.py").write_text("软件")

        (tmp_path / "checked").mkdir()
        (tmp_path / "checked" / "test.py").write_text("软件")

        # Create matcher
        matcher = Matcher({"软件": "軟體"})

        # Process directory
        results = list(convert_directory(tmp_path, matcher))

        # Should only process checked/test.py, not ignored/test.py
        processed_files = [r.file.name for r in results if not r.skipped]
        assert len(processed_files) == 1
        assert "test.py" in processed_files

    def test_no_zhtwignore_processes_all(self, tmp_path: Path):
        """Without .zhtwignore, all files are processed."""
        from zhtw.converter import convert_directory
        from zhtw.matcher import Matcher

        # Create test files (no .zhtwignore)
        (tmp_path / "dir1").mkdir()
        (tmp_path / "dir1" / "test.py").write_text("软件")

        (tmp_path / "dir2").mkdir()
        (tmp_path / "dir2" / "test.py").write_text("软件")

        # Create matcher
        matcher = Matcher({"软件": "軟體"})

        # Process directory
        results = list(convert_directory(tmp_path, matcher))

        # Should process both files
        processed_files = [r.file.name for r in results if not r.skipped]
        assert len(processed_files) == 2
