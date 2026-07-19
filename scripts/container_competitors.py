#!/usr/bin/env python3
"""Persistent Docker JSONL clients for locked benchmark competitors."""

from __future__ import annotations

import atexit
import json
import queue
import subprocess
import threading
from collections import deque
from functools import lru_cache
from typing import Any

ENVIRONMENT_LABEL = "org.zhtw.benchmark.environment-sha256"


class JsonlProcessClient:
    def __init__(self, command: list[str], *, timeout_seconds: float) -> None:
        self.command = command
        self.timeout_seconds = timeout_seconds
        self.process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            bufsize=1,
        )
        self._responses: queue.Queue[dict[str, Any] | Exception] = queue.Queue()
        self._stderr: deque[str] = deque(maxlen=20)
        self._request_number = 0
        self._lock = threading.Lock()
        threading.Thread(target=self._read_stdout, daemon=True).start()
        threading.Thread(target=self._read_stderr, daemon=True).start()
        atexit.register(self.close)

    def _read_stdout(self) -> None:
        assert self.process.stdout is not None
        try:
            for line in self.process.stdout:
                value = json.loads(line)
                if not isinstance(value, dict):
                    raise ValueError("adapter response must be an object")
                self._responses.put(value)
        except Exception as exc:
            self._responses.put(exc)
        finally:
            self._responses.put(RuntimeError("adapter process closed stdout"))

    def _read_stderr(self) -> None:
        assert self.process.stderr is not None
        for line in self.process.stderr:
            self._stderr.append(line.rstrip())

    def request(self, operation: str, **payload: Any) -> dict[str, Any]:
        with self._lock:
            if self.process.poll() is not None:
                detail = "; ".join(self._stderr) or f"exit {self.process.returncode}"
                raise RuntimeError(f"adapter process is unavailable: {detail}")
            self._request_number += 1
            request_id = f"request-{self._request_number}"
            request = {"op": operation, "id": request_id, **payload}
            assert self.process.stdin is not None
            self.process.stdin.write(
                json.dumps(request, ensure_ascii=False, separators=(",", ":")) + "\n"
            )
            self.process.stdin.flush()
            try:
                response = self._responses.get(timeout=self.timeout_seconds)
            except queue.Empty as exc:
                self.close()
                raise TimeoutError(
                    f"adapter timed out after {self.timeout_seconds:.3f} seconds"
                ) from exc
            if isinstance(response, Exception):
                detail = "; ".join(self._stderr)
                raise RuntimeError(f"adapter protocol failed: {response}; {detail}")
            if response.get("id") != request_id:
                raise RuntimeError("adapter response id does not match request")
            if response.get("ok") is not True:
                raise RuntimeError(f"adapter error: {response.get('error', 'unknown error')}")
            return response

    def close(self) -> None:
        if self.process.poll() is not None:
            return
        if self.process.stdin is not None:
            try:
                self.process.stdin.close()
            except OSError:
                pass
        try:
            self.process.wait(timeout=1)
        except subprocess.TimeoutExpired:
            self.process.terminate()
            try:
                self.process.wait(timeout=1)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait(timeout=1)


@lru_cache(maxsize=8)
def inspect_image_environment(image: str) -> tuple[str, str]:
    result = subprocess.run(
        ["docker", "image", "inspect", image],
        check=False,
        capture_output=True,
        text=True,
        timeout=30,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"cannot inspect image {image}")
    payload = json.loads(result.stdout)
    if not isinstance(payload, list) or len(payload) != 1:
        raise RuntimeError("docker image inspect returned an unexpected payload")
    image_data = payload[0]
    labels = image_data.get("Config", {}).get("Labels", {}) or {}
    environment_hash = labels.get(ENVIRONMENT_LABEL)
    image_id = image_data.get("Id")
    if not isinstance(environment_hash, str) or not isinstance(image_id, str):
        raise RuntimeError("competitor image is missing identity metadata")
    return environment_hash, image_id


def docker_adapter_command(image: str, engine_id: str) -> list[str]:
    return [
        "docker",
        "run",
        "--rm",
        "--interactive",
        "--network",
        "none",
        "--read-only",
        "--cap-drop",
        "ALL",
        "--security-opt",
        "no-new-privileges",
        "--pids-limit",
        "64",
        "--tmpfs",
        "/tmp:rw,noexec,nosuid,size=16m",
        image,
        engine_id,
    ]
