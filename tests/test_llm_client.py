"""Tests for llm/client.py module."""

import json
import urllib.error
from unittest.mock import MagicMock, patch

import pytest

from zhtw.llm.client import (
    APIError,
    APIKeyError,
    GeminiClient,
    LLMError,
)


class TestExceptions:
    """Test exception classes."""

    def test_llm_error_is_exception(self):
        """Test LLMError is an Exception."""
        assert issubclass(LLMError, Exception)

    def test_api_key_error_is_llm_error(self):
        """Test APIKeyError is an LLMError."""
        assert issubclass(APIKeyError, LLMError)

    def test_api_error_is_llm_error(self):
        """Test APIError is an LLMError."""
        assert issubclass(APIError, LLMError)

    def test_raise_api_key_error(self):
        """Test raising APIKeyError."""
        with pytest.raises(APIKeyError) as exc_info:
            raise APIKeyError("No API key")
        assert "No API key" in str(exc_info.value)

    def test_raise_api_error(self):
        """Test raising APIError."""
        with pytest.raises(APIError) as exc_info:
            raise APIError("API failed")
        assert "API failed" in str(exc_info.value)


class TestGeminiClientInit:
    """Test GeminiClient initialization."""

    @patch("zhtw.llm.client.load_config")
    @patch.dict("os.environ", {"GEMINI_API_KEY": "test-key"})
    def test_init_with_api_key(self, mock_config):
        """Test initialization with API key."""
        mock_config.return_value = {"llm": {"model": "gemini-1.5-flash"}}
        client = GeminiClient()
        assert client.api_key == "test-key"
        assert client.force is False
        assert client.model == "gemini-1.5-flash"

    @patch("zhtw.llm.client.load_config")
    @patch.dict("os.environ", {}, clear=True)
    def test_init_without_api_key(self, mock_config):
        """Test initialization without API key."""
        mock_config.return_value = {}
        # Clear GEMINI_API_KEY if it exists
        with patch.dict("os.environ", {"GEMINI_API_KEY": ""}, clear=False):
            import os

            os.environ.pop("GEMINI_API_KEY", None)
            client = GeminiClient()
            assert client.api_key is None

    @patch("zhtw.llm.client.load_config")
    @patch.dict("os.environ", {"GEMINI_API_KEY": "test-key"})
    def test_init_with_force(self, mock_config):
        """Test initialization with force=True."""
        mock_config.return_value = {}
        client = GeminiClient(force=True)
        assert client.force is True

    @patch("zhtw.llm.client.load_config")
    @patch.dict("os.environ", {"GEMINI_API_KEY": "test-key"})
    def test_init_default_model(self, mock_config):
        """Test initialization with default model."""
        mock_config.return_value = {}
        client = GeminiClient()
        assert client.model == "gemini-2.0-flash"


class TestGeminiClientIsAvailable:
    """Test is_available method."""

    @patch("zhtw.llm.client.load_config")
    @patch.dict("os.environ", {"GEMINI_API_KEY": "test-key"})
    def test_is_available_with_key(self, mock_config):
        """Test is_available returns True with API key."""
        mock_config.return_value = {}
        client = GeminiClient()
        assert client.is_available() is True

    @patch("zhtw.llm.client.load_config")
    def test_is_available_without_key(self, mock_config):
        """Test is_available returns False without API key."""
        mock_config.return_value = {}
        with patch.dict("os.environ", {}, clear=True):
            import os

            os.environ.pop("GEMINI_API_KEY", None)
            client = GeminiClient()
            client.api_key = None
            assert client.is_available() is False


class TestGeminiClientCheckApiKey:
    """Test check_api_key method."""

    @patch("zhtw.llm.client.load_config")
    @patch.dict("os.environ", {"GEMINI_API_KEY": "test-key"})
    def test_check_api_key_with_key(self, mock_config):
        """Test check_api_key passes with key."""
        mock_config.return_value = {}
        client = GeminiClient()
        client.check_api_key()  # Should not raise

    @patch("zhtw.llm.client.load_config")
    def test_check_api_key_without_key(self, mock_config):
        """Test check_api_key raises without key."""
        mock_config.return_value = {}
        client = GeminiClient()
        client.api_key = None
        with pytest.raises(APIKeyError) as exc_info:
            client.check_api_key()
        assert "GEMINI_API_KEY" in str(exc_info.value)


class TestGeminiClientGenerate:
    """Test generate method."""

    @patch("zhtw.llm.client.load_config")
    @patch.dict("os.environ", {"GEMINI_API_KEY": "test-key"})
    def test_generate_success(self, mock_config):
        """Test successful generation."""
        mock_config.return_value = {}
        client = GeminiClient()
        client.usage = MagicMock()
        client.usage.check_limits.return_value = (True, None)
        client.usage.get_warning.return_value = None

        mock_response = {
            "candidates": [{"content": {"parts": [{"text": "Hello world"}]}}],
            "usageMetadata": {"promptTokenCount": 10, "candidatesTokenCount": 5},
        }

        with patch("urllib.request.urlopen") as mock_urlopen:
            mock_resp = MagicMock()
            mock_resp.read.return_value = json.dumps(mock_response).encode()
            mock_resp.__enter__ = MagicMock(return_value=mock_resp)
            mock_resp.__exit__ = MagicMock(return_value=False)
            mock_urlopen.return_value = mock_resp

            result = client.generate("Test prompt")
            assert result == "Hello world"
            client.usage.record.assert_called_once()

    @patch("zhtw.llm.client.load_config")
    @patch.dict("os.environ", {"GEMINI_API_KEY": "test-key"})
    def test_generate_http_error(self, mock_config):
        """Test generation with HTTP error."""
        mock_config.return_value = {}
        client = GeminiClient()
        client.usage = MagicMock()
        client.usage.check_limits.return_value = (True, None)
        client.usage.get_warning.return_value = None

        with patch("urllib.request.urlopen") as mock_urlopen:
            error = urllib.error.HTTPError("http://test", 400, "Bad Request", {}, None)
            error.read = MagicMock(return_value=b'{"error": {"message": "Invalid"}}')
            mock_urlopen.side_effect = error

            with pytest.raises(APIError) as exc_info:
                client.generate("Test prompt")
            assert "Invalid" in str(exc_info.value)

    @patch("zhtw.llm.client.load_config")
    @patch.dict("os.environ", {"GEMINI_API_KEY": "test-key"})
    def test_generate_url_error(self, mock_config):
        """Test generation with URL error."""
        mock_config.return_value = {}
        client = GeminiClient()
        client.usage = MagicMock()
        client.usage.check_limits.return_value = (True, None)
        client.usage.get_warning.return_value = None

        with patch("urllib.request.urlopen") as mock_urlopen:
            mock_urlopen.side_effect = urllib.error.URLError("Connection refused")

            with pytest.raises(APIError) as exc_info:
                client.generate("Test prompt")
            assert "網路錯誤" in str(exc_info.value)

    @patch("zhtw.llm.client.load_config")
    @patch.dict("os.environ", {"GEMINI_API_KEY": "test-key"})
    def test_generate_invalid_response(self, mock_config):
        """Test generation with invalid response format."""
        mock_config.return_value = {}
        client = GeminiClient()
        client.usage = MagicMock()
        client.usage.check_limits.return_value = (True, None)
        client.usage.get_warning.return_value = None

        mock_response = {"candidates": []}  # Missing expected structure

        with patch("urllib.request.urlopen") as mock_urlopen:
            mock_resp = MagicMock()
            mock_resp.read.return_value = json.dumps(mock_response).encode()
            mock_resp.__enter__ = MagicMock(return_value=mock_resp)
            mock_resp.__exit__ = MagicMock(return_value=False)
            mock_urlopen.return_value = mock_resp

            with pytest.raises(APIError) as exc_info:
                client.generate("Test prompt")
            assert "無法解析" in str(exc_info.value)


class TestGeminiClientValidateTerm:
    """Test validate_term method."""

    @patch("zhtw.llm.client.load_config")
    @patch.dict("os.environ", {"GEMINI_API_KEY": "test-key"})
    def test_validate_term_correct(self, mock_config):
        """Test validating a correct term."""
        mock_config.return_value = {}
        client = GeminiClient()

        json_response = '{"correct": true, "reason": "正確轉換", "suggestion": null}'

        with patch.object(client, "generate", return_value=json_response):
            result = client.validate_term("軟體", "軟體")
            assert result["correct"] is True
            assert result["reason"] == "正確轉換"
            assert result["suggestion"] is None

    @patch("zhtw.llm.client.load_config")
    @patch.dict("os.environ", {"GEMINI_API_KEY": "test-key"})
    def test_validate_term_incorrect(self, mock_config):
        """Test validating an incorrect term."""
        mock_config.return_value = {}
        client = GeminiClient()

        json_response = '{"correct": false, "reason": "錯誤轉換", "suggestion": "建議詞"}'

        with patch.object(client, "generate", return_value=json_response):
            result = client.validate_term("test", "wrong")
            assert result["correct"] is False
            assert result["reason"] == "錯誤轉換"
            assert result["suggestion"] == "建議詞"

    @patch("zhtw.llm.client.load_config")
    @patch.dict("os.environ", {"GEMINI_API_KEY": "test-key"})
    def test_validate_term_non_json_response(self, mock_config):
        """Test validating with non-JSON response."""
        mock_config.return_value = {}
        client = GeminiClient()

        # Non-JSON response containing "正確"
        with patch.object(client, "generate", return_value="這個轉換是正確的"):
            result = client.validate_term("軟體", "軟體")
            assert result["correct"] is True
            assert "正確" in result["reason"]

    @patch("zhtw.llm.client.load_config")
    @patch.dict("os.environ", {"GEMINI_API_KEY": "test-key"})
    def test_validate_term_non_json_incorrect(self, mock_config):
        """Test validating with non-JSON response indicating incorrect."""
        mock_config.return_value = {}
        client = GeminiClient()

        # Non-JSON response not containing "正確" or "correct"
        with patch.object(client, "generate", return_value="這個轉換有問題"):
            result = client.validate_term("test", "wrong")
            assert result["correct"] is False


class TestGeminiClientBatchValidate:
    """Test batch_validate method."""

    @patch("zhtw.llm.client.load_config")
    @patch.dict("os.environ", {"GEMINI_API_KEY": "test-key"})
    def test_batch_validate_success(self, mock_config):
        """Test batch validation success."""
        mock_config.return_value = {}
        client = GeminiClient()

        validate_results = [
            {"correct": True, "reason": "OK", "suggestion": None},
            {"correct": False, "reason": "Wrong", "suggestion": "fix"},
        ]

        with patch.object(client, "validate_term", side_effect=validate_results):
            results = client.batch_validate([("a", "A"), ("b", "B")])
            assert len(results) == 2
            assert results[0]["correct"] is True
            assert results[0]["source"] == "a"
            assert results[1]["correct"] is False
            assert results[1]["source"] == "b"

    @patch("zhtw.llm.client.load_config")
    @patch.dict("os.environ", {"GEMINI_API_KEY": "test-key"})
    def test_batch_validate_with_callback(self, mock_config):
        """Test batch validation with callback."""
        mock_config.return_value = {}
        client = GeminiClient()

        callback_calls = []

        def callback(idx, result):
            callback_calls.append((idx, result))

        validate_result = {"correct": True, "reason": "OK", "suggestion": None}

        with patch.object(client, "validate_term", return_value=validate_result):
            client.batch_validate([("a", "A"), ("b", "B")], callback=callback)
            assert len(callback_calls) == 2
            assert callback_calls[0][0] == 0
            assert callback_calls[1][0] == 1

    @patch("zhtw.llm.client.load_config")
    @patch.dict("os.environ", {"GEMINI_API_KEY": "test-key"})
    def test_batch_validate_with_error(self, mock_config):
        """Test batch validation handles errors."""
        mock_config.return_value = {}
        client = GeminiClient()

        with patch.object(client, "validate_term", side_effect=APIError("API failed")):
            results = client.batch_validate([("a", "A")])
            assert len(results) == 1
            assert results[0]["correct"] is None
            assert results[0]["error"] == "API failed"
