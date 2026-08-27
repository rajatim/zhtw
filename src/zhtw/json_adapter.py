"""Exact-byte JSON string-value conversion with fail-closed validation."""

from __future__ import annotations

import json
import os
import stat
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Optional

from .encoding import EncodingInfo, normalize_encoding


class JsonAdapterError(ValueError):
    """Raised when JSON cannot be converted without preserving its structure."""

    def __init__(self, message: str, *, code: str = "invalid_json") -> None:
        super().__init__(message)
        self.code = code


@dataclass(frozen=True, slots=True)
class JsonValueChange:
    """One changed JSON string value token."""

    token_start: int
    token_end: int
    source: str
    target: str
    replacement: str


@dataclass(frozen=True, slots=True)
class JsonAdapterResult:
    """Converted JSON text and changed value tokens."""

    output: str
    changes: tuple[JsonValueChange, ...]


def _reject_duplicate_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise JsonAdapterError(
                "duplicate JSON object key",
                code="duplicate_key",
            )
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise JsonAdapterError(f"non-standard JSON number: {value}")


def _validate_unicode_scalars(value: Any) -> None:
    if isinstance(value, str):
        try:
            value.encode("utf-8")
        except UnicodeEncodeError as exc:
            raise JsonAdapterError("JSON contains an unpaired Unicode surrogate") from exc
        return
    if isinstance(value, list):
        for item in value:
            _validate_unicode_scalars(item)
        return
    if isinstance(value, dict):
        for key, item in value.items():
            _validate_unicode_scalars(key)
            _validate_unicode_scalars(item)


def _parse_json(text: str) -> Any:
    try:
        parsed = json.loads(
            text,
            object_pairs_hook=_reject_duplicate_pairs,
            parse_constant=_reject_constant,
        )
        _validate_unicode_scalars(parsed)
        return parsed
    except JsonAdapterError:
        raise
    except (json.JSONDecodeError, UnicodeDecodeError, RecursionError) as exc:
        raise JsonAdapterError(f"invalid JSON: {exc}") from exc


@dataclass(frozen=True, slots=True)
class _StringToken:
    start: int
    end: int
    value: str


class _ValueStringScanner:
    """Locate JSON string values after the standard parser validates syntax."""

    def __init__(self, text: str):
        self.text = text
        self.position = 0
        self.values: list[_StringToken] = []

    def scan(self) -> tuple[_StringToken, ...]:
        self._skip_whitespace()
        self._parse_value(collect_string=True)
        self._skip_whitespace()
        if self.position != len(self.text):
            raise JsonAdapterError("JSON token scanner did not consume the document")
        return tuple(self.values)

    def _skip_whitespace(self) -> None:
        while self.position < len(self.text) and self.text[self.position] in " \t\r\n":
            self.position += 1

    def _expect(self, value: str) -> None:
        if not self.text.startswith(value, self.position):
            raise JsonAdapterError(f"JSON token scanner expected {value!r}")
        self.position += len(value)

    def _scan_string(self) -> _StringToken:
        start = self.position
        self._expect('"')
        escaped = False
        while self.position < len(self.text):
            character = self.text[self.position]
            self.position += 1
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == '"':
                raw = self.text[start : self.position]
                try:
                    value = json.loads(raw)
                except json.JSONDecodeError as exc:
                    raise JsonAdapterError(f"invalid JSON string token: {exc}") from exc
                return _StringToken(start=start, end=self.position, value=value)
        raise JsonAdapterError("unterminated JSON string token")

    def _parse_value(self, *, collect_string: bool) -> None:
        self._skip_whitespace()
        if self.position >= len(self.text):
            raise JsonAdapterError("missing JSON value")
        character = self.text[self.position]
        if character == '"':
            token = self._scan_string()
            if collect_string:
                self.values.append(token)
            return
        if character == "{":
            self._parse_object()
            return
        if character == "[":
            self._parse_array()
            return

        start = self.position
        while self.position < len(self.text) and self.text[self.position] not in ",]} \t\r\n":
            self.position += 1
        if self.position == start:
            raise JsonAdapterError("invalid JSON primitive token")

    def _parse_object(self) -> None:
        self._expect("{")
        self._skip_whitespace()
        if self.position < len(self.text) and self.text[self.position] == "}":
            self.position += 1
            return
        while True:
            self._skip_whitespace()
            self._scan_string()  # Object keys are never converted.
            self._skip_whitespace()
            self._expect(":")
            self._parse_value(collect_string=True)
            self._skip_whitespace()
            if self.position < len(self.text) and self.text[self.position] == "}":
                self.position += 1
                return
            self._expect(",")

    def _parse_array(self) -> None:
        self._expect("[")
        self._skip_whitespace()
        if self.position < len(self.text) and self.text[self.position] == "]":
            self.position += 1
            return
        while True:
            self._parse_value(collect_string=True)
            self._skip_whitespace()
            if self.position < len(self.text) and self.text[self.position] == "]":
                self.position += 1
                return
            self._expect(",")


_STRING_VALUE = object()


def _structure(value: Any) -> Any:
    if isinstance(value, str):
        return _STRING_VALUE
    if isinstance(value, list):
        return ("array", tuple(_structure(item) for item in value))
    if isinstance(value, dict):
        return ("object", tuple((key, _structure(item)) for key, item in value.items()))
    return (type(value).__name__, value)


def transform_json_values(text: str, converter: Callable[[str], str]) -> JsonAdapterResult:
    """Convert only JSON string values and preserve every unrelated character."""

    if not isinstance(text, str):
        raise TypeError("JSON input must be a string")
    original = _parse_json(text)
    tokens = _ValueStringScanner(text).scan()
    replacements: list[tuple[int, int, str]] = []
    changes: list[JsonValueChange] = []
    for token in tokens:
        target = converter(token.value)
        if not isinstance(target, str):
            raise JsonAdapterError(
                "JSON value converter must return a string",
                code="invalid_converter_result",
            )
        if target == token.value:
            continue
        encoded = json.dumps(target, ensure_ascii=False, separators=(",", ":"))
        replacements.append((token.start, token.end, encoded))
        changes.append(
            JsonValueChange(
                token_start=token.start,
                token_end=token.end,
                source=token.value,
                target=target,
                replacement=encoded,
            )
        )

    if not replacements:
        return JsonAdapterResult(output=text, changes=())

    parts: list[str] = []
    last_end = 0
    for start, end, replacement in replacements:
        parts.append(text[last_end:start])
        parts.append(replacement)
        last_end = end
    parts.append(text[last_end:])
    output = "".join(parts)

    converted = _parse_json(output)
    if _structure(converted) != _structure(original):
        raise JsonAdapterError(
            "converted JSON changed non-value structure",
            code="structure_changed",
        )
    return JsonAdapterResult(output=output, changes=tuple(changes))


def convert_json(
    text: str,
    sources: Optional[list[str]] = None,
    ambiguity_mode: str = "strict",
) -> str:
    """Convert JSON string values with the public zhtw conversion pipeline."""

    from .converter import convert

    return transform_json_values(
        text,
        lambda value: convert(value, sources=sources, ambiguity_mode=ambiguity_mode),
    ).output


def _encode_text(
    content: str,
    output_encoding: str,
    original_info: EncodingInfo,
) -> tuple[bytes, str]:
    if output_encoding == "auto":
        target_encoding = (
            original_info.encoding if original_info.can_represent_traditional else "utf-8"
        )
    elif output_encoding == "keep":
        target_encoding = original_info.encoding
    else:
        target_encoding = normalize_encoding(output_encoding)

    encoded = content.encode(target_encoding)
    if original_info.has_bom:
        bom = {
            "utf-8": b"\xef\xbb\xbf",
            "utf-16-le": b"\xff\xfe",
            "utf-16-be": b"\xfe\xff",
        }.get(target_encoding)
        if bom is not None and not encoded.startswith(bom):
            encoded = bom + encoded
    return encoded, target_encoding


def atomic_write_json_text(
    path: Path,
    content: str,
    *,
    output_encoding: str = "auto",
    original_info: EncodingInfo,
) -> str:
    """Flush, fsync, and atomically replace one JSON file in its directory."""

    path = Path(path)
    mode = stat.S_IMODE(path.stat().st_mode)
    if mode & 0o222 == 0:
        raise PermissionError(f"JSON file is read-only: {path}")
    payload, target_encoding = _encode_text(content, output_encoding, original_info)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.",
        suffix=".tmp",
        dir=path.parent,
    )
    temporary_path = Path(temporary_name)
    try:
        os.fchmod(descriptor, mode)
        with os.fdopen(descriptor, "wb") as temporary:
            temporary.write(payload)
            temporary.flush()
            os.fsync(temporary.fileno())
        os.replace(temporary_path, path)
        try:
            directory_descriptor = os.open(path.parent, os.O_RDONLY)
            try:
                os.fsync(directory_descriptor)
            finally:
                os.close(directory_descriptor)
        except OSError:
            # The atomic replace already succeeded. Some filesystems do not
            # support directory fsync, so do not report a false write failure.
            pass
    except Exception:
        try:
            os.close(descriptor)
        except OSError:
            pass
        temporary_path.unlink(missing_ok=True)
        raise
    return target_encoding
