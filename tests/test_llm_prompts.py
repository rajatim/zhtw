"""Tests for llm/prompts.py module."""

from zhtw.llm.prompts import (
    BATCH_VALIDATE_PROMPT,
    DISCOVER_TERM_PROMPT,
    VALIDATE_TERM_PROMPT,
)


class TestPromptTemplates:
    """Test that prompt templates are properly defined."""

    def test_validate_term_prompt_exists(self):
        """Test VALIDATE_TERM_PROMPT is a non-empty string."""
        assert isinstance(VALIDATE_TERM_PROMPT, str)
        assert len(VALIDATE_TERM_PROMPT) > 0

    def test_validate_term_prompt_has_placeholders(self):
        """Test VALIDATE_TERM_PROMPT has required placeholders."""
        assert "{source}" in VALIDATE_TERM_PROMPT
        assert "{target}" in VALIDATE_TERM_PROMPT

    def test_discover_term_prompt_exists(self):
        """Test DISCOVER_TERM_PROMPT is a non-empty string."""
        assert isinstance(DISCOVER_TERM_PROMPT, str)
        assert len(DISCOVER_TERM_PROMPT) > 0

    def test_discover_term_prompt_has_placeholders(self):
        """Test DISCOVER_TERM_PROMPT has required placeholders."""
        assert "{term}" in DISCOVER_TERM_PROMPT
        assert "{context}" in DISCOVER_TERM_PROMPT

    def test_batch_validate_prompt_exists(self):
        """Test BATCH_VALIDATE_PROMPT is a non-empty string."""
        assert isinstance(BATCH_VALIDATE_PROMPT, str)
        assert len(BATCH_VALIDATE_PROMPT) > 0

    def test_batch_validate_prompt_has_placeholders(self):
        """Test BATCH_VALIDATE_PROMPT has required placeholders."""
        assert "{terms_list}" in BATCH_VALIDATE_PROMPT

    def test_prompts_contain_json_format(self):
        """Test prompts mention JSON output format."""
        assert "JSON" in VALIDATE_TERM_PROMPT
        assert "JSON" in DISCOVER_TERM_PROMPT
        assert "JSON" in BATCH_VALIDATE_PROMPT
