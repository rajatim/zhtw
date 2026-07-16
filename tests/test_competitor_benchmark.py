# zhtw:disable  # 測試會讀取含簡體輸入的 benchmark fixture
"""Tests for the report-only competitor precision benchmark."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "competitor_benchmark.py"


def test_competitor_benchmark_fixture_matches_zhtw_expected() -> None:
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--engines",
            "zhtw",
            "--format",
            "json",
            "--fail-on-zhtw-mismatch",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr

    payload = json.loads(result.stdout)
    assert payload["engines"]["zhtw"]["available"] is True
    assert len(payload["rows"]) >= 20
    assert payload["summary"] == {"zhtw_only": len(payload["rows"])}
