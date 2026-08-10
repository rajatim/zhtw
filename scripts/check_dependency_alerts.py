#!/usr/bin/env python3
"""Fail a release candidate when GitHub reports medium-or-higher alerts."""

from __future__ import annotations

import argparse
import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

BLOCKING_SEVERITIES = {"medium", "high", "critical"}


def load_alerts(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("Dependabot response must be a JSON array")
    for alert in payload:
        if not isinstance(alert, dict):
            raise ValueError("Every Dependabot alert must be an object")
    return payload


def summarize(alerts: list[dict[str, Any]], repository: str) -> dict[str, Any]:
    normalized: list[dict[str, Any]] = []
    for alert in alerts:
        advisory = alert.get("security_advisory") or {}
        vulnerability = alert.get("security_vulnerability") or {}
        dependency = alert.get("dependency") or {}
        package = dependency.get("package") or {}
        patched = vulnerability.get("first_patched_version") or {}
        severity = str(advisory.get("severity") or "").lower()
        state = str(alert.get("state") or "").lower()
        if not severity or not state:
            raise ValueError("Dependabot alert is missing state or severity")
        normalized.append(
            {
                "number": alert.get("number"),
                "state": state,
                "severity": severity,
                "package": package.get("name"),
                "manifest": dependency.get("manifest_path"),
                "vulnerable_range": vulnerability.get("vulnerable_version_range"),
                "patched_version": patched.get("identifier"),
            }
        )

    blocking = [
        alert
        for alert in normalized
        if alert["state"] == "open" and alert["severity"] in BLOCKING_SEVERITIES
    ]
    return {
        "schema_version": 1,
        "repository": repository,
        "checked_at": datetime.now(UTC).replace(microsecond=0).isoformat(),
        "policy": "block open medium, high, and critical Dependabot alerts",
        "open_alert_count": sum(alert["state"] == "open" for alert in normalized),
        "blocking_alert_count": len(blocking),
        "blocking_alerts": blocking,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--repository", default="rajatim/zhtw")
    args = parser.parse_args()

    summary = summarize(load_alerts(args.input), args.repository)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    if summary["blocking_alert_count"]:
        print(
            "ERROR: Dependabot reports "
            f"{summary['blocking_alert_count']} open medium-or-higher alert(s)",
        )
        return 1
    print("Dependabot release gate: PASS (0 open medium-or-higher alerts)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
