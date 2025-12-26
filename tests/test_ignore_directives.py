"""Tests for ignore directives (zhtw:disable)."""

from pathlib import Path

import pytest

from zhtw.converter import convert_file, convert_text, get_ignored_lines
from zhtw.matcher import Matcher


@pytest.fixture
def matcher():
    """Create a matcher with test terms."""
    return Matcher({
        "软件": "軟體",
        "硬件": "硬體",
        "用户": "使用者",
    })


def check_text(text: str, matcher: Matcher):
    """Helper to check text with ignore directives."""
    ignored_lines = get_ignored_lines(text)
    _, matches = convert_text(text, matcher, ignored_lines=ignored_lines)
    return matches


class TestDisableLine:
    """Tests for zhtw:disable-line directive."""

    def test_disable_line_python_comment(self, matcher: Matcher):
        """Disable line with Python comment."""
        text = 'data = "软件"  # zhtw:disable-line'
        matches = check_text(text, matcher)
        assert matches == []

    def test_disable_line_js_comment(self, matcher: Matcher):
        """Disable line with JavaScript comment."""
        text = 'const data = "软件";  // zhtw:disable-line'
        matches = check_text(text, matcher)
        assert matches == []

    def test_disable_line_html_comment(self, matcher: Matcher):
        """Disable line with HTML comment."""
        text = '<div>软件</div>  <!-- zhtw:disable-line -->'
        matches = check_text(text, matcher)
        assert matches == []

    def test_disable_line_only_affects_current_line(self, matcher: Matcher):
        """Disable-line only affects the current line."""
        text = '''data1 = "软件"  # zhtw:disable-line
data2 = "硬件"'''
        matches = check_text(text, matcher)
        # Line 1 ignored, Line 2 should have issue
        assert len(matches) == 1
        assert matches[0][0].source == "硬件"

    def test_disable_line_multiple_terms(self, matcher: Matcher):
        """Disable-line ignores all terms on that line."""
        text = 'data = "软件和硬件"  # zhtw:disable-line'
        matches = check_text(text, matcher)
        assert matches == []


class TestDisableNext:
    """Tests for zhtw:disable-next directive."""

    def test_disable_next_python(self, matcher: Matcher):
        """Disable next line with Python comment."""
        text = '''# zhtw:disable-next
data = "软件"'''
        matches = check_text(text, matcher)
        assert matches == []

    def test_disable_next_js(self, matcher: Matcher):
        """Disable next line with JavaScript comment."""
        text = '''// zhtw:disable-next
const data = "软件";'''
        matches = check_text(text, matcher)
        assert matches == []

    def test_disable_next_only_affects_next_line(self, matcher: Matcher):
        """Disable-next only affects the next line."""
        text = '''# zhtw:disable-next
data1 = "软件"
data2 = "硬件"'''
        matches = check_text(text, matcher)
        # Line 2 ignored, Line 3 should have issue
        assert len(matches) == 1
        assert matches[0][0].source == "硬件"

    def test_disable_next_consecutive(self, matcher: Matcher):
        """Multiple disable-next only affects immediate next lines."""
        text = '''# zhtw:disable-next
data1 = "软件"
# zhtw:disable-next
data2 = "硬件"
data3 = "用户"'''
        matches = check_text(text, matcher)
        # Line 2 and 4 ignored, Line 5 should have issue
        assert len(matches) == 1
        assert matches[0][0].source == "用户"


class TestDisableBlock:
    """Tests for zhtw:disable ... zhtw:enable block."""

    def test_disable_block_python(self, matcher: Matcher):
        """Disable block with Python comments."""
        text = '''# zhtw:disable
data1 = "软件"
data2 = "硬件"
# zhtw:enable'''
        matches = check_text(text, matcher)
        assert matches == []

    def test_disable_block_js(self, matcher: Matcher):
        """Disable block with JavaScript comments."""
        text = '''// zhtw:disable
const data1 = "软件";
const data2 = "硬件";
// zhtw:enable'''
        matches = check_text(text, matcher)
        assert matches == []

    def test_disable_block_html(self, matcher: Matcher):
        """Disable block with HTML comments."""
        text = '''<!-- zhtw:disable -->
<div>软件</div>
<div>硬件</div>
<!-- zhtw:enable -->'''
        matches = check_text(text, matcher)
        assert matches == []

    def test_disable_block_partial(self, matcher: Matcher):
        """Code before and after block is still checked."""
        text = '''before = "软件"
# zhtw:disable
ignored = "硬件"
# zhtw:enable
after = "用户"'''
        matches = check_text(text, matcher)
        # Line 1 and 5 should have issues, Line 3 ignored
        assert len(matches) == 2
        sources = [m[0].source for m in matches]
        assert "软件" in sources
        assert "用户" in sources
        assert "硬件" not in sources

    def test_disable_block_nested_content(self, matcher: Matcher):
        """Block can contain multiple lines with terms."""
        text = '''# zhtw:disable
test_data = [
    "软件",
    "硬件",
    "用户",
]
# zhtw:enable'''
        matches = check_text(text, matcher)
        assert matches == []

    def test_unclosed_block_ignores_rest(self, matcher: Matcher):
        """Unclosed disable block ignores rest of file."""
        text = '''# zhtw:disable
data1 = "软件"
data2 = "硬件"'''
        matches = check_text(text, matcher)
        assert matches == []


class TestMixedDirectives:
    """Tests for mixed directive usage."""

    def test_disable_line_inside_block(self, matcher: Matcher):
        """Disable-line inside block (redundant but valid)."""
        text = '''# zhtw:disable
data = "软件"  # zhtw:disable-line
# zhtw:enable'''
        matches = check_text(text, matcher)
        assert matches == []

    def test_disable_next_before_block(self, matcher: Matcher):
        """Disable-next before block start."""
        text = '''data1 = "软件"
# zhtw:disable-next
# zhtw:disable
data2 = "硬件"
# zhtw:enable'''
        matches = check_text(text, matcher)
        # Line 1 has issue, rest ignored
        assert len(matches) == 1
        assert matches[0][0].source == "软件"


class TestFileIntegration:
    """Integration tests with actual files."""

    def test_file_with_disable_line(self, tmp_path: Path, matcher: Matcher):
        """Process file with disable-line directive."""
        test_file = tmp_path / "test.py"
        test_file.write_text('''data1 = "软件"  # zhtw:disable-line
data2 = "硬件"
''')
        result = convert_file(test_file, matcher)
        assert len(result.issues) == 1
        assert result.issues[0].source == "硬件"

    def test_file_with_disable_block(self, tmp_path: Path, matcher: Matcher):
        """Process file with disable block."""
        test_file = tmp_path / "test.py"
        test_file.write_text('''# zhtw:disable
test_data = ["软件", "硬件"]
# zhtw:enable
real_data = "用户"
''')
        result = convert_file(test_file, matcher)
        assert len(result.issues) == 1
        assert result.issues[0].source == "用户"


class TestEdgeCases:
    """Edge case tests."""

    def test_directive_in_string_still_works(self, matcher: Matcher):
        """Directive in string literal still activates."""
        # This is current behavior - might want to change
        text = 'msg = "软件 zhtw:disable-line"'
        matches = check_text(text, matcher)
        # Currently this would ignore the line
        assert matches == []

    def test_case_sensitive_directive(self, matcher: Matcher):
        """Directives are case sensitive."""
        text = 'data = "软件"  # ZHTW:DISABLE-LINE'
        matches = check_text(text, matcher)
        # Uppercase doesn't work
        assert len(matches) == 1

    def test_partial_directive_matches(self, matcher: Matcher):
        """Partial directive names still match (substring match)."""
        # Note: "disable-lines" contains "disable-line" as substring
        # Current behavior: matches. May want to add word boundary later.
        text = 'data = "软件"  # zhtw:disable-lines'
        matches = check_text(text, matcher)
        assert matches == []  # Line is ignored

    def test_empty_file(self, matcher: Matcher):
        """Empty file with directives."""
        text = '''# zhtw:disable
# zhtw:enable'''
        matches = check_text(text, matcher)
        assert matches == []

    def test_directive_only_file(self, matcher: Matcher):
        """File with only directives, no content."""
        text = '''# zhtw:disable-next
# zhtw:disable-line'''
        matches = check_text(text, matcher)
        assert matches == []
