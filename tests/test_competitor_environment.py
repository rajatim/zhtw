"""Tests for the locked competitor container and JSONL protocol."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

from scripts import competitor_benchmark
from scripts.competitor_benchmark import Engine
from scripts.container_competitors import JsonlProcessClient
from scripts.run_accuracy_benchmark import assert_formal_engines_locked
from scripts.validate_competitor_environment import load_json, validate_lock

ROOT = Path(__file__).resolve().parents[1]
LOCK_PATH = ROOT / "benchmarks" / "accuracy" / "competitors.lock.json"
ADAPTER = ROOT / "benchmarks" / "accuracy" / "competitor-env" / "adapter.py"


def test_committed_competitor_lock_is_reproducible() -> None:
    lock = load_json(LOCK_PATH)

    assert validate_lock(LOCK_PATH) == []
    assert lock["status"] == "locked"
    assert "latest" not in json.dumps(lock).lower()
    assert len(lock["environment"]["environment_sha256"]) == 64
    assert set(lock["formal_engine_ids"]) == {
        "zhtw",
        "opencc-s2twp",
        "opencc-js-cn-twp",
        "zhconv-zh-tw",
        "zhconv-rs-zh-tw",
    }


def test_jsonl_client_enforces_ids_and_unicode(tmp_path: Path) -> None:
    script = tmp_path / "fixture_adapter.py"
    script.write_text(
        """
import json, sys
for line in sys.stdin:
    request = json.loads(line)
    response = {"ok": True, "id": request["id"]}
    if request["op"] == "convert":
        response["output"] = request["text"].replace("软件", "軟體")
    print(json.dumps(response, ensure_ascii=False), flush=True)
""".strip()
        + "\n",
        encoding="utf-8",
    )
    client = JsonlProcessClient([sys.executable, str(script)], timeout_seconds=1)
    try:
        assert client.request("convert", text="开发软件")["output"] == "开发軟體"
    finally:
        client.close()


def test_jsonl_client_times_out_and_stops_process(tmp_path: Path) -> None:
    script = tmp_path / "slow_adapter.py"
    script.write_text(
        "import sys, time\nfor line in sys.stdin:\n    time.sleep(60)\n",
        encoding="utf-8",
    )
    client = JsonlProcessClient([sys.executable, str(script)], timeout_seconds=0.05)

    with pytest.raises(TimeoutError, match="timed out"):
        client.request("convert", text="输入")

    assert client.process.poll() is not None


def test_container_adapter_rejects_unknown_engine() -> None:
    client = JsonlProcessClient(
        [sys.executable, str(ADAPTER), "not-an-engine"],
        timeout_seconds=1,
    )
    with pytest.raises(RuntimeError, match="adapter"):
        client.request("probe")


def test_formal_runner_requires_every_locked_engine_and_metadata() -> None:
    lock = load_json(LOCK_PATH)
    locked = {item["id"]: item for item in lock["competitors"]}
    environment_hash = lock["environment"]["environment_sha256"]
    engines = [
        Engine(
            name=engine_id,
            available=True,
            version=locked[engine_id]["version"],
            family=locked[engine_id]["family"],
            adapter=locked[engine_id]["adapter"],
            config_sha256=locked[engine_id]["config_sha256"],
            environment_sha256=None if engine_id == "zhtw" else environment_hash,
        )
        for engine_id in lock["formal_engine_ids"]
    ]

    assert_formal_engines_locked(lock["formal_engine_ids"], engines, lock)
    with pytest.raises(ValueError, match="every locked engine"):
        assert_formal_engines_locked(["zhtw"], engines[:1], lock)

    wrong = [*engines[:-1], Engine(name="zhconv-rs-zh-tw", available=True, version="wrong")]
    with pytest.raises(ValueError, match="lock mismatch"):
        assert_formal_engines_locked(lock["formal_engine_ids"], wrong, lock)


def test_container_engine_runs_by_inspected_image_id(monkeypatch: pytest.MonkeyPatch) -> None:
    lock = load_json(LOCK_PATH)
    environment_hash = lock["environment"]["environment_sha256"]
    image_id = "sha256:" + "a" * 64
    commands: list[list[str]] = []

    class FakeClient:
        def __init__(self, command: list[str], *, timeout_seconds: float) -> None:
            commands.append(command)

        def request(self, operation: str, **payload: object) -> dict[str, object]:
            if operation == "probe":
                return {
                    "ok": True,
                    "engine": "opencc-s2twp",
                    "family": "opencc",
                    "version": "1.4.1",
                    "config_sha256": (
                        "681dd1ff5f3a1efe93a6f56006ee7f58f767fa0366fd3a2ec6165c983e39415d"
                    ),
                }
            return {"ok": True, "output": str(payload["text"])}

        def close(self) -> None:
            return None

    monkeypatch.setattr(
        competitor_benchmark,
        "inspect_image_environment",
        lambda image: (environment_hash, image_id),
    )
    monkeypatch.setattr(competitor_benchmark, "JsonlProcessClient", FakeClient)

    engine = competitor_benchmark.load_container_engine(
        "opencc-s2twp",
        lock=lock,
        image="mutable-tag",
    )

    assert engine.available is True
    assert commands[0][-2:] == [image_id, "opencc-s2twp"]
    assert engine.convert is not None
    assert engine.convert("开发") == "开发"
