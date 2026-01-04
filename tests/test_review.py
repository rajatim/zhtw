"""Tests for review.py module."""

import json
from unittest.mock import MagicMock, patch

from zhtw.review import (
    ReviewResult,
    approve_terms,
    finalize_review,
    get_builtin_terms_dir,
    review_pending_file,
)


class TestReviewResult:
    """Test ReviewResult dataclass."""

    def test_default_values(self):
        """Test default values."""
        result = ReviewResult()
        assert result.approved == 0
        assert result.rejected == 0
        assert result.skipped == 0
        assert result.terms == {}

    def test_custom_values(self):
        """Test custom values."""
        result = ReviewResult(approved=5, rejected=2, skipped=1, terms={"a": "b"})
        assert result.approved == 5
        assert result.rejected == 2
        assert result.skipped == 1
        assert result.terms == {"a": "b"}


class TestGetBuiltinTermsDir:
    """Test get_builtin_terms_dir function."""

    def test_cn_source(self):
        """Test cn source directory."""
        path = get_builtin_terms_dir("cn")
        assert path.name == "cn"
        assert path.parent.name == "terms"

    def test_hk_source(self):
        """Test hk source directory."""
        path = get_builtin_terms_dir("hk")
        assert path.name == "hk"
        assert path.parent.name == "terms"

    def test_default_source(self):
        """Test default source is cn."""
        path = get_builtin_terms_dir()
        assert path.name == "cn"


class TestApproveTerms:
    """Test approve_terms function."""

    def test_approve_new_terms(self, tmp_path):
        """Test approving terms to a new file."""
        with patch("zhtw.review.get_builtin_terms_dir", return_value=tmp_path):
            terms = {"簡體": "簡體", "軟體": "軟體"}
            result_path = approve_terms(terms, "cn", "test.json")

            assert result_path.exists()
            with open(result_path, encoding="utf-8") as f:
                data = json.load(f)
            assert data["terms"] == terms

    def test_approve_merge_terms(self, tmp_path):
        """Test merging with existing terms."""
        # Create existing file
        existing_file = tmp_path / "test.json"
        existing_data = {"version": "1.0", "terms": {"existing": "現有"}}
        with open(existing_file, "w", encoding="utf-8") as f:
            json.dump(existing_data, f)

        with patch("zhtw.review.get_builtin_terms_dir", return_value=tmp_path):
            terms = {"new": "新"}
            result_path = approve_terms(terms, "cn", "test.json")

            with open(result_path, encoding="utf-8") as f:
                data = json.load(f)
            assert data["terms"]["existing"] == "現有"
            assert data["terms"]["new"] == "新"

    def test_approve_corrupted_file(self, tmp_path):
        """Test handling corrupted existing file."""
        # Create corrupted file
        corrupted_file = tmp_path / "test.json"
        with open(corrupted_file, "w") as f:
            f.write("not valid json")

        with patch("zhtw.review.get_builtin_terms_dir", return_value=tmp_path):
            terms = {"new": "新"}
            result_path = approve_terms(terms, "cn", "test.json")

            with open(result_path, encoding="utf-8") as f:
                data = json.load(f)
            assert data["terms"] == {"new": "新"}


class TestReviewPendingFile:
    """Test review_pending_file function."""

    def test_auto_approve(self):
        """Test auto-approve mode."""
        mock_data = {"terms": {"a": "A", "b": "B"}}
        with patch("zhtw.review.load_pending", return_value=mock_data):
            result = review_pending_file("test", auto_approve=True)
            assert result.approved == 2
            assert result.rejected == 0
            assert result.terms == {"a": "A", "b": "B"}

    def test_auto_reject(self):
        """Test auto-reject mode."""
        mock_data = {"terms": {"a": "A", "b": "B"}}
        with patch("zhtw.review.load_pending", return_value=mock_data):
            result = review_pending_file("test", auto_reject=True)
            assert result.rejected == 2
            assert result.approved == 0
            assert result.terms == {}

    def test_non_interactive(self):
        """Test non-interactive mode (approves all)."""
        mock_data = {"terms": {"a": "A", "b": "B"}}
        with patch("zhtw.review.load_pending", return_value=mock_data):
            result = review_pending_file("test", interactive=False)
            assert result.approved == 2
            assert result.terms == {"a": "A", "b": "B"}

    def test_empty_terms(self):
        """Test empty terms."""
        mock_data = {"terms": {}}
        with patch("zhtw.review.load_pending", return_value=mock_data):
            result = review_pending_file("test", auto_approve=True)
            assert result.approved == 0
            assert result.terms == {}


class TestFinalizeReview:
    """Test finalize_review function."""

    def test_finalize_with_terms(self, tmp_path):
        """Test finalizing with approved terms."""
        result = ReviewResult(approved=2, terms={"a": "A", "b": "B"})

        with (
            patch("zhtw.review.approve_terms", return_value=tmp_path / "out.json") as mock_approve,
            patch("zhtw.review.delete_pending") as mock_delete,
        ):
            path = finalize_review("test", result, delete_after=True)
            mock_approve.assert_called_once_with({"a": "A", "b": "B"}, "cn")
            mock_delete.assert_called_once_with("test")
            assert path == tmp_path / "out.json"

    def test_finalize_no_terms(self):
        """Test finalizing with no approved terms."""
        result = ReviewResult(rejected=2, terms={})

        with patch("zhtw.review.delete_pending") as mock_delete:
            path = finalize_review("test", result, delete_after=True)
            mock_delete.assert_called_once_with("test")
            assert path is None

    def test_finalize_keep_pending(self, tmp_path):
        """Test finalizing without deleting pending file."""
        result = ReviewResult(terms={"a": "A"})

        with (
            patch("zhtw.review.approve_terms", return_value=tmp_path / "out.json"),
            patch("zhtw.review.delete_pending") as mock_delete,
        ):
            finalize_review("test", result, delete_after=False)
            mock_delete.assert_not_called()


class TestInteractiveReview:
    """Test interactive review mode."""

    def test_interactive_approve(self):
        """Test interactive approve action."""
        mock_data = {"terms": {"a": "A"}}

        with (
            patch("zhtw.review.load_pending", return_value=mock_data),
            patch("builtins.input", return_value="a"),
            patch("builtins.print"),
        ):
            result = review_pending_file("test", interactive=True)
            assert result.approved == 1
            assert result.rejected == 0
            assert result.terms == {"a": "A"}

    def test_interactive_reject(self):
        """Test interactive reject action."""
        mock_data = {"terms": {"a": "A"}}

        with (
            patch("zhtw.review.load_pending", return_value=mock_data),
            patch("builtins.input", return_value="r"),
            patch("builtins.print"),
        ):
            result = review_pending_file("test", interactive=True)
            assert result.approved == 0
            assert result.rejected == 1
            assert result.terms == {}

    def test_interactive_skip(self):
        """Test interactive skip action."""
        mock_data = {"terms": {"a": "A"}}

        with (
            patch("zhtw.review.load_pending", return_value=mock_data),
            patch("builtins.input", return_value="s"),
            patch("builtins.print"),
        ):
            result = review_pending_file("test", interactive=True)
            assert result.approved == 0
            assert result.rejected == 0
            assert result.skipped == 1
            assert result.terms == {}

    def test_interactive_quit(self):
        """Test interactive quit action."""
        mock_data = {"terms": {"a": "A", "b": "B"}}

        with (
            patch("zhtw.review.load_pending", return_value=mock_data),
            patch("builtins.input", side_effect=["a", "q"]),
            patch("builtins.print"),
        ):
            result = review_pending_file("test", interactive=True)
            # First term approved, then quit
            assert result.approved == 1
            assert result.terms == {"a": "A"}

    def test_interactive_invalid_then_approve(self):
        """Test invalid input followed by approve."""
        mock_data = {"terms": {"a": "A"}}

        with (
            patch("zhtw.review.load_pending", return_value=mock_data),
            patch("builtins.input", side_effect=["x", "invalid", "a"]),
            patch("builtins.print"),
        ):
            result = review_pending_file("test", interactive=True)
            assert result.approved == 1
            assert result.terms == {"a": "A"}

    def test_interactive_with_llm_success(self):
        """Test interactive with LLM validation success."""
        mock_data = {"terms": {"a": "A"}}
        mock_llm = MagicMock()
        mock_llm.validate_term.return_value = {
            "correct": True,
            "reason": "正確轉換",
            "suggestion": None,
        }

        with (
            patch("zhtw.review.load_pending", return_value=mock_data),
            patch("builtins.input", return_value="a"),
            patch("builtins.print"),
        ):
            result = review_pending_file("test", interactive=True, llm_client=mock_llm)
            assert result.approved == 1
            mock_llm.validate_term.assert_called_once_with("a", "A")

    def test_interactive_with_llm_incorrect(self):
        """Test interactive with LLM validation incorrect."""
        mock_data = {"terms": {"a": "A"}}
        mock_llm = MagicMock()
        mock_llm.validate_term.return_value = {
            "correct": False,
            "reason": "錯誤轉換",
            "suggestion": "B",
        }

        with (
            patch("zhtw.review.load_pending", return_value=mock_data),
            patch("builtins.input", return_value="r"),
            patch("builtins.print"),
        ):
            result = review_pending_file("test", interactive=True, llm_client=mock_llm)
            assert result.rejected == 1

    def test_interactive_with_llm_error(self):
        """Test interactive with LLM validation error."""
        mock_data = {"terms": {"a": "A"}}
        mock_llm = MagicMock()
        mock_llm.validate_term.side_effect = Exception("LLM error")

        with (
            patch("zhtw.review.load_pending", return_value=mock_data),
            patch("builtins.input", return_value="a"),
            patch("builtins.print"),
        ):
            # Should still work despite LLM error
            result = review_pending_file("test", interactive=True, llm_client=mock_llm)
            assert result.approved == 1
