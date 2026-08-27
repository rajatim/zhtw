"""Tests for exact-byte JSON string-value conversion."""
# zhtw:disable  # fixtures need simplified source text

from __future__ import annotations

import json
import os
from pathlib import Path

import pytest

from zhtw.encoding import EncodingInfo
from zhtw.json_adapter import (
    JsonAdapterError,
    atomic_write_json_text,
    convert_json,
    transform_json_values,
)


def test_only_string_values_change_and_every_other_byte_is_preserved() -> None:
    source = (
        '{\n  "软件 key": "软件", "nested": ["服务器", 1.00e+02, true, null],\n'
        '  "object": {"接口": "接口", "empty": ""}\n}\n'
    )

    result = transform_json_values(
        source,
        lambda value: {
            "软件": "軟體",
            "服务器": "伺服器",
            "接口": "介面",
        }.get(value, value),
    )

    assert result.output == (
        '{\n  "软件 key": "軟體", "nested": ["伺服器", 1.00e+02, true, null],\n'
        '  "object": {"接口": "介面", "empty": ""}\n}\n'
    )
    assert [(change.source, change.target) for change in result.changes] == [
        ("软件", "軟體"),
        ("服务器", "伺服器"),
        ("接口", "介面"),
    ]


def test_unchanged_string_tokens_keep_original_escape_bytes() -> None:
    source = '{"escaped":"\\u8edf\\u9ad4","slash":"a\\/b","quote":"\\""}'

    result = transform_json_values(source, lambda value: value)

    assert result.output == source
    assert result.changes == ()


def test_changed_values_use_fixed_json_escaping() -> None:
    source = '{"value":"软件\\"C:\\\\tmp\\n"}'

    result = transform_json_values(source, lambda value: value.replace("软件", "軟體"))

    assert result.output == '{"value":"軟體\\"C:\\\\tmp\\n"}'
    assert json.loads(result.output)["value"] == '軟體"C:\\tmp\n'


def test_escaped_supplementary_han_value_can_change() -> None:
    source = '{"rare":"\\ud840\\udc00"}'

    result = transform_json_values(source, lambda value: value.replace(chr(0x20000), chr(0x20001)))

    assert result.output == f'{{"rare":"{chr(0x20001)}"}}'


@pytest.mark.parametrize(
    "source",
    [
        '{"key":"软件","key":"軟體"}',
        '{"key":"软件","\\u006bey":"軟體"}',
    ],
)
def test_duplicate_keys_fail_closed(source: str) -> None:
    with pytest.raises(JsonAdapterError, match="duplicate JSON object key") as error:
        transform_json_values(source, lambda value: value)
    assert error.value.code == "duplicate_key"


@pytest.mark.parametrize(
    "source",
    ['{"key":', '{"key":"value",}', '{"n":NaN}', '{"value":"\\ud800"}'],
)
def test_invalid_or_non_standard_json_fails_closed(source: str) -> None:
    with pytest.raises(JsonAdapterError) as error:
        transform_json_values(source, lambda value: value)
    assert error.value.code == "invalid_json"


def test_converter_failure_returns_no_partial_output() -> None:
    def fail(_value: str) -> str:
        raise RuntimeError("conversion failed")

    with pytest.raises(RuntimeError, match="conversion failed"):
        transform_json_values('{"a":"软件","b":"服务器"}', fail)


def test_converter_must_return_a_string() -> None:
    with pytest.raises(JsonAdapterError, match="must return a string"):
        transform_json_values('{"a":"软件"}', lambda _value: None)  # type: ignore[arg-type]


def test_public_convert_json_keeps_keys_and_converts_values() -> None:
    source = '{"软件":"这个软件","number":1}'

    output = convert_json(source, sources=["cn"])

    assert output == '{"软件":"這個軟體","number":1}'


def _utf8_info() -> EncodingInfo:
    return EncodingInfo(
        encoding="utf-8",
        has_bom=False,
        confidence=1.0,
        can_represent_traditional=True,
    )


def test_atomic_write_replaces_file_after_flush(tmp_path: Path) -> None:
    path = tmp_path / "data.json"
    path.write_text('{"value":"软件"}\n', encoding="utf-8")

    encoding = atomic_write_json_text(
        path,
        '{"value":"軟體"}\n',
        original_info=_utf8_info(),
    )

    assert encoding == "utf-8"
    assert path.read_bytes() == '{"value":"軟體"}\n'.encode()
    assert list(tmp_path.glob(".data.json.*.tmp")) == []


def test_atomic_write_preserves_utf8_bom(tmp_path: Path) -> None:
    path = tmp_path / "data.json"
    path.write_bytes(b"\xef\xbb\xbf" + '{"value":"software"}'.encode())
    original_info = EncodingInfo(
        encoding="utf-8",
        has_bom=True,
        confidence=1.0,
        can_represent_traditional=True,
    )

    atomic_write_json_text(
        path,
        '{"value":"軟體"}',
        original_info=original_info,
    )

    assert path.read_bytes() == b"\xef\xbb\xbf" + '{"value":"軟體"}'.encode()


def test_atomic_write_refuses_read_only_file(tmp_path: Path) -> None:
    path = tmp_path / "data.json"
    original = b'{"value":"software"}\n'
    path.write_bytes(original)
    path.chmod(0o444)

    with pytest.raises(PermissionError, match="read-only"):
        atomic_write_json_text(path, '{"value":"軟體"}\n', original_info=_utf8_info())

    assert path.read_bytes() == original


def test_atomic_replace_failure_preserves_original_and_removes_temp(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    path = tmp_path / "data.json"
    original = b'{"value":"software"}\n'
    path.write_bytes(original)

    def fail_replace(_source: os.PathLike[str], _target: os.PathLike[str]) -> None:
        raise OSError("replace failed")

    monkeypatch.setattr(os, "replace", fail_replace)
    with pytest.raises(OSError, match="replace failed"):
        atomic_write_json_text(path, '{"value":"軟體"}\n', original_info=_utf8_info())

    assert path.read_bytes() == original
    assert list(tmp_path.glob(".data.json.*.tmp")) == []


def test_atomic_encoding_failure_preserves_original(tmp_path: Path) -> None:
    path = tmp_path / "data.json"
    original = b'{"value":"software"}\n'
    path.write_bytes(original)

    with pytest.raises(UnicodeEncodeError):
        atomic_write_json_text(
            path,
            '{"value":"軟體"}\n',
            output_encoding="ascii",
            original_info=_utf8_info(),
        )

    assert path.read_bytes() == original
    assert list(tmp_path.glob(".data.json.*.tmp")) == []
