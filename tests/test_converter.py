"""Tests for converter module."""

from pathlib import Path

from zhtw.converter import (
    contains_chinese,
    convert_text,
    get_ignored_lines,
    should_check_file,
)
from zhtw.matcher import Matcher


class TestContainsChinese:
    """Test Chinese character detection."""

    def test_contains_chinese_true(self):
        """Test text with Chinese characters."""
        assert contains_chinese("Hello 你好") is True
        assert contains_chinese("中文") is True

    def test_contains_chinese_false(self):
        """Test text without Chinese characters."""
        assert contains_chinese("Hello World") is False
        assert contains_chinese("123 abc") is False
        assert contains_chinese("") is False


class TestShouldCheckFile:
    """Test file filtering logic."""

    def test_allowed_extensions(self):
        """Test files with allowed extensions are checked."""
        assert should_check_file(Path("test.py")) is True
        assert should_check_file(Path("test.ts")) is True
        assert should_check_file(Path("test.md")) is True
        assert should_check_file(Path("test.json")) is True

    def test_disallowed_extensions(self):
        """Test files with disallowed extensions are skipped."""
        assert should_check_file(Path("test.exe")) is False
        assert should_check_file(Path("test.png")) is False
        assert should_check_file(Path("test.dll")) is False

    def test_excluded_directories(self):
        """Test files in excluded directories are skipped."""
        assert should_check_file(Path("node_modules/test.js")) is False
        assert should_check_file(Path(".git/config")) is False
        assert should_check_file(Path("dist/bundle.js")) is False

    def test_excluded_files(self):
        """Test excluded files are skipped."""
        assert should_check_file(Path("package-lock.json")) is False
        assert should_check_file(Path("yarn.lock")) is False


class TestConvertText:
    """Test text conversion."""

    def test_convert_text_find_matches(self):
        """Test finding matches in text."""
        terms = {"软件": "軟體", "硬件": "硬體"}
        matcher = Matcher(terms)

        text = "这是软件和硬件"
        result_text, matches = convert_text(text, matcher, fix=False)

        assert result_text == text  # Not modified when fix=False
        assert len(matches) == 2

    def test_convert_text_with_fix(self):
        """Test fixing text."""
        terms = {"软件": "軟體"}
        matcher = Matcher(terms)

        text = "这是软件"
        result_text, matches = convert_text(text, matcher, fix=True)

        assert result_text == "这是軟體"
        assert len(matches) == 1

    def test_convert_text_no_matches(self):
        """Test text with no matches."""
        terms = {"软件": "軟體"}
        matcher = Matcher(terms)

        text = "沒有匹配的文字"
        result_text, matches = convert_text(text, matcher, fix=True)

        assert result_text == text
        assert len(matches) == 0


class TestIgnoreDirectives:
    """Test ignore directive parsing."""

    def test_disable_line(self):
        """Test zhtw:disable-line directive."""
        text = "软件  # zhtw:disable-line\n硬件"
        ignored = get_ignored_lines(text)

        assert 1 in ignored
        assert 2 not in ignored

    def test_disable_next(self):
        """Test zhtw:disable-next directive."""
        text = "# zhtw:disable-next\n软件\n硬件"
        ignored = get_ignored_lines(text)

        assert 1 not in ignored
        assert 2 in ignored
        assert 3 not in ignored

    def test_disable_block(self):
        """Test zhtw:disable/enable block directive."""
        text = "正常\n# zhtw:disable\n软件\n硬件\n# zhtw:enable\n正常"
        ignored = get_ignored_lines(text)

        assert 1 not in ignored
        assert 2 not in ignored  # The disable line itself
        assert 3 in ignored
        assert 4 in ignored
        assert 5 not in ignored  # The enable line itself
        assert 6 not in ignored

    def test_convert_with_ignore(self):
        """Test conversion respects ignore directives."""
        terms = {"软件": "軟體", "硬件": "硬體"}
        matcher = Matcher(terms)

        text = "软件  # zhtw:disable-line\n硬件"
        ignored = get_ignored_lines(text)
        result_text, matches = convert_text(text, matcher, fix=True, ignored_lines=ignored)

        # Line 1 should be preserved, line 2 should be converted
        assert "软件" in result_text  # Preserved
        assert "硬體" in result_text  # Converted
        assert len(matches) == 1  # Only one match reported

    def test_convert_block_ignore(self):
        """Test conversion respects block ignore."""
        terms = {"软件": "軟體", "硬件": "硬體"}
        matcher = Matcher(terms)

        text = "# zhtw:disable\n软件\n硬件\n# zhtw:enable"
        ignored = get_ignored_lines(text)
        result_text, matches = convert_text(text, matcher, fix=True, ignored_lines=ignored)

        # Both should be preserved
        assert "软件" in result_text
        assert "硬件" in result_text
        assert len(matches) == 0
