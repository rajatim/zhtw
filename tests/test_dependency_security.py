"""Behavior tests for the Jenkins Dependabot release gate."""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check_dependency_alerts.py"


def alert(number: int, severity: str, state: str = "open") -> dict[str, object]:
    return {
        "number": number,
        "state": state,
        "dependency": {
            "package": {"name": "fixture"},
            "manifest_path": "fixture.lock",
        },
        "security_advisory": {"severity": severity},
        "security_vulnerability": {
            "vulnerable_version_range": "< 2.0.0",
            "first_patched_version": {"identifier": "2.0.0"},
        },
    }


def run_gate(tmp_path: Path, alerts: list[dict[str, object]]) -> subprocess.CompletedProcess[str]:
    source = tmp_path / "alerts.json"
    output = tmp_path / "evidence.json"
    source.write_text(json.dumps(alerts), encoding="utf-8")
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(source), str(output)],
        capture_output=True,
        text=True,
        check=False,
    )


def test_dependency_gate_allows_low_and_closed_alerts(tmp_path: Path) -> None:
    result = run_gate(tmp_path, [alert(1, "low"), alert(2, "high", "dismissed")])

    assert result.returncode == 0
    evidence = json.loads((tmp_path / "evidence.json").read_text(encoding="utf-8"))
    assert evidence["blocking_alert_count"] == 0
    assert evidence["blocking_alerts"] == []
    assert evidence["checked_at"].endswith("+00:00")


def test_dependency_gate_blocks_medium_or_higher_alerts(tmp_path: Path) -> None:
    result = run_gate(tmp_path, [alert(1, "medium"), alert(2, "critical")])

    assert result.returncode == 1
    evidence = json.loads((tmp_path / "evidence.json").read_text(encoding="utf-8"))
    assert evidence["blocking_alert_count"] == 2
    assert [item["severity"] for item in evidence["blocking_alerts"]] == [
        "medium",
        "critical",
    ]


def test_dependency_gate_rejects_malformed_api_payload(tmp_path: Path) -> None:
    source = tmp_path / "alerts.json"
    output = tmp_path / "evidence.json"
    source.write_text('{"unexpected": true}', encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(SCRIPT), str(source), str(output)],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode != 0
    assert not output.exists()
