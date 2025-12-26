"""Gemini API client with usage tracking."""

import json
import os
import urllib.error
import urllib.request
from typing import Optional

from ..config import load_config
from .usage import UsageLimitError, UsageTracker


class LLMError(Exception):
    """Base exception for LLM errors."""

    pass


class APIKeyError(LLMError):
    """Raised when API key is missing or invalid."""

    pass


class APIError(LLMError):
    """Raised when API returns an error."""

    pass


class GeminiClient:
    """Client for Google Gemini API with usage tracking."""

    API_BASE = "https://generativelanguage.googleapis.com/v1beta/models"

    def __init__(self, force: bool = False):
        """Initialize the client.

        Args:
            force: If True, bypass usage limits
        """
        self.api_key = os.environ.get("GEMINI_API_KEY")
        self.force = force
        self.usage = UsageTracker()
        self.config = load_config()
        self.model = self.config.get("llm", {}).get("model", "gemini-2.0-flash")

    def is_available(self) -> bool:
        """Check if the client is properly configured."""
        return bool(self.api_key)

    def check_api_key(self) -> None:
        """Raise error if API key is not set."""
        if not self.api_key:
            raise APIKeyError(
                "未設定 GEMINI_API_KEY 環境變數\n"
                "設定方式:\n"
                "  1. 取得 API Key: https://aistudio.google.com/apikey\n"
                '  2. 設定環境變數: export GEMINI_API_KEY="your-key"\n'
                "  3. 或使用 direnv: echo 'export GEMINI_API_KEY=\"your-key\"' > .envrc"
            )

    def generate(self, prompt: str, max_tokens: int = 500) -> str:
        """Generate a response from the model.

        Args:
            prompt: The prompt to send
            max_tokens: Maximum tokens in response

        Returns:
            The generated text

        Raises:
            APIKeyError: If API key is not set
            UsageLimitError: If usage limit is reached (and not force)
            APIError: If API returns an error
        """
        self.check_api_key()

        # Check limits
        can_proceed, error_msg = self.usage.check_limits(force=self.force)
        if not can_proceed:
            raise UsageLimitError(
                f"❌ {error_msg}\n" "   使用 --force 強制執行，或調整 zhtw config 設定"
            )

        # Show warning if approaching limits
        warning = self.usage.get_warning()
        if warning and not self.force:
            print(warning)

        # Make API request
        url = f"{self.API_BASE}/{self.model}:generateContent?key={self.api_key}"

        data = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "maxOutputTokens": max_tokens,
                "temperature": 0.1,  # Low temperature for consistent results
            },
        }

        req = urllib.request.Request(
            url,
            data=json.dumps(data).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                result = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8")
            try:
                error_data = json.loads(error_body)
                error_msg = error_data.get("error", {}).get("message", str(e))
            except json.JSONDecodeError:
                error_msg = error_body or str(e)
            raise APIError(f"API 錯誤: {error_msg}")
        except urllib.error.URLError as e:
            raise APIError(f"網路錯誤: {e.reason}")

        # Extract response text
        try:
            text = result["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            raise APIError(f"無法解析 API 回應: {result}")

        # Extract token usage
        usage_metadata = result.get("usageMetadata", {})
        input_tokens = usage_metadata.get("promptTokenCount", 0)
        output_tokens = usage_metadata.get("candidatesTokenCount", 0)

        # Record usage
        self.usage.record(
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            provider="gemini",
            model=self.model,
        )

        return text.strip()

    def validate_term(self, source: str, target: str) -> dict:
        """Validate a term conversion using LLM.

        Args:
            source: Source term (e.g., "软件")
            target: Target term (e.g., "軟體")

        Returns:
            Dict with keys: correct (bool), reason (str), suggestion (Optional[str])
        """
        from .prompts import VALIDATE_TERM_PROMPT

        prompt = VALIDATE_TERM_PROMPT.format(source=source, target=target)

        try:
            response = self.generate(prompt, max_tokens=200)
            # Try to parse as JSON
            result = json.loads(response)
            return {
                "correct": result.get("correct", True),
                "reason": result.get("reason", ""),
                "suggestion": result.get("suggestion"),
            }
        except json.JSONDecodeError:
            # If not valid JSON, try to extract info
            is_correct = "正確" in response or "correct" in response.lower()
            return {
                "correct": is_correct,
                "reason": response,
                "suggestion": None,
            }

    def batch_validate(
        self, terms: list[tuple[str, str]], callback: Optional[callable] = None
    ) -> list[dict]:
        """Validate multiple terms.

        Args:
            terms: List of (source, target) tuples
            callback: Optional callback called after each validation with (index, result)

        Returns:
            List of validation results
        """
        results = []
        for i, (source, target) in enumerate(terms):
            try:
                result = self.validate_term(source, target)
                result["source"] = source
                result["target"] = target
                result["error"] = None
            except (UsageLimitError, APIError) as e:
                result = {
                    "source": source,
                    "target": target,
                    "correct": None,
                    "reason": None,
                    "suggestion": None,
                    "error": str(e),
                }
            results.append(result)

            if callback:
                callback(i, result)

        return results
