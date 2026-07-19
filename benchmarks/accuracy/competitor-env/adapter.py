#!/usr/bin/env python3
"""JSONL adapter entrypoint for locked Python competitor converters."""

from __future__ import annotations

import hashlib
import importlib.metadata
import json
import os
import sys
from pathlib import Path
from typing import Any, Callable

Converter = Callable[[str], str]


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def load_engine(engine_id: str) -> tuple[Converter, dict[str, str]]:
    if engine_id == "opencc-s2twp":
        import opencc

        converter = opencc.OpenCC("s2twp")
        config_path = (
            Path(opencc.__file__).resolve().parent / "clib" / "share" / "opencc" / "s2twp.json"
        )
        probe = {
            "engine": engine_id,
            "family": "opencc",
            "version": importlib.metadata.version("OpenCC"),
            "config": "s2twp.json",
            "config_sha256": sha256_bytes(config_path.read_bytes()),
        }
        return converter.convert, probe
    if engine_id == "zhconv-zh-tw":
        import zhconv

        probe = {
            "engine": engine_id,
            "family": "mediawiki-zhconv",
            "version": importlib.metadata.version("zhconv"),
            "config": "zh-tw",
            "config_sha256": sha256_bytes(b"zh-tw"),
        }
        return lambda text: zhconv.convert(text, "zh-tw"), probe
    if engine_id == "zhconv-rs-zh-tw":
        from zhconv_rs import zhconv as rust_zhconv

        probe = {
            "engine": engine_id,
            "family": "mediawiki-zhconv",
            "version": importlib.metadata.version("zhconv-rs"),
            "config": "zh-TW",
            "config_sha256": sha256_bytes(b"zh-tw"),
        }
        return lambda text: rust_zhconv(text, "zh-tw"), probe
    raise ValueError(f"unsupported engine: {engine_id}")


def write_response(response: dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(response, ensure_ascii=False, separators=(",", ":")) + "\n")
    sys.stdout.flush()


def serve(engine_id: str) -> int:
    if engine_id == "opencc-js-cn-twp":
        os.execv(
            "/usr/local/bin/node",
            ["node", "/opt/competitors/opencc-js-adapter.mjs"],
        )
    try:
        convert, probe = load_engine(engine_id)
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 2

    for line in sys.stdin:
        request_id: Any = None
        try:
            request = json.loads(line)
            if not isinstance(request, dict):
                raise ValueError("request must be an object")
            request_id = request.get("id")
            operation = request.get("op")
            if operation == "probe":
                write_response({"ok": True, "id": request_id, **probe})
                continue
            if operation != "convert" or not isinstance(request.get("text"), str):
                raise ValueError("convert request requires string text")
            write_response(
                {
                    "ok": True,
                    "id": request_id,
                    "output": convert(request["text"]),
                }
            )
        except Exception as exc:
            write_response({"ok": False, "id": request_id, "error": str(exc)})
    return 0


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: adapter.py ENGINE_ID", file=sys.stderr)
        return 2
    return serve(sys.argv[1])


if __name__ == "__main__":
    raise SystemExit(main())
