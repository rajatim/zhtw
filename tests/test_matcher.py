"""Tests for matcher module."""


from zhtw.matcher import Matcher


class TestMatcher:
    """Test Matcher class."""

    def test_find_matches_basic(self):
        """Test basic pattern matching."""
        terms = {"软件": "軟體", "硬件": "硬體"}
        matcher = Matcher(terms)

        matches = list(matcher.find_matches("这是软件和硬件"))

        assert len(matches) == 2
        assert matches[0].source == "软件"
        assert matches[0].target == "軟體"
        assert matches[1].source == "硬件"
        assert matches[1].target == "硬體"

    def test_find_matches_no_match(self):
        """Test when no matches are found."""
        terms = {"软件": "軟體"}
        matcher = Matcher(terms)

        matches = list(matcher.find_matches("這裡沒有匹配"))

        assert len(matches) == 0

    def test_find_matches_positions(self):
        """Test that match positions are correct."""
        terms = {"软件": "軟體"}
        matcher = Matcher(terms)

        matches = list(matcher.find_matches("软件"))

        assert len(matches) == 1
        assert matches[0].start == 0
        assert matches[0].end == 2

    def test_replace_all(self):
        """Test replacing all matches."""
        terms = {"软件": "軟體", "硬件": "硬體"}
        matcher = Matcher(terms)

        result = matcher.replace_all("这是软件和硬件的说明")

        assert result == "这是軟體和硬體的说明"

    def test_replace_all_no_match(self):
        """Test replace when no matches."""
        terms = {"软件": "軟體"}
        matcher = Matcher(terms)

        text = "這裡沒有匹配"
        result = matcher.replace_all(text)

        assert result == text

    def test_has_matches(self):
        """Test has_matches method."""
        terms = {"软件": "軟體"}
        matcher = Matcher(terms)

        assert matcher.has_matches("这是软件") is True
        assert matcher.has_matches("這裡沒有") is False

    def test_count_matches(self):
        """Test count_matches method."""
        terms = {"软件": "軟體"}
        matcher = Matcher(terms)

        assert matcher.count_matches("软件和软件") == 2
        assert matcher.count_matches("沒有匹配") == 0

    def test_find_matches_with_lines(self):
        """Test finding matches with line info."""
        terms = {"软件": "軟體"}
        matcher = Matcher(terms)

        text = "第一行\n软件在這裡"
        matches = list(matcher.find_matches_with_lines(text))

        assert len(matches) == 1
        match, line, col = matches[0]
        assert line == 2
        assert col == 1
        assert match.source == "软件"

    def test_empty_terms(self):
        """Test with empty terms dictionary."""
        matcher = Matcher({})

        assert list(matcher.find_matches("任何文字")) == []
        assert matcher.replace_all("任何文字") == "任何文字"

    def test_identity_mapping_priority_over_overlap(self):
        """Test that identity mapping takes precedence over overlapping conversion.

        When "文檔"→"文件" and "檔案"→"檔案" overlap in "中文檔案",
        the identity mapping should win to protect the valid word "檔案".
        """
        terms = {"文檔": "文件", "檔案": "檔案"}
        matcher = Matcher(terms)

        # "中文檔案" should NOT be converted to "中文件案"
        result = matcher.replace_all("無中文檔案")
        assert result == "無中文檔案"

        # Verify no matches are reported (identity mapping is skipped)
        matches = list(matcher.find_matches("無中文檔案"))
        assert len(matches) == 0

    def test_identity_mapping_does_not_block_valid_conversion(self):
        """Test that identity mapping doesn't block valid conversions elsewhere."""
        terms = {"文檔": "文件", "檔案": "檔案"}
        matcher = Matcher(terms)

        # Standalone "文檔" should still be converted
        result = matcher.replace_all("請查看文檔")
        assert result == "請查看文件"

        # Both cases in same text
        result = matcher.replace_all("文檔和中文檔案")
        assert result == "文件和中文檔案"
