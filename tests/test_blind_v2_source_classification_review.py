"""Tests for Blind-v2 Codex/Gemini source classification comparison."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from scripts.compare_blind_v2_source_classifications import build_comparison, render_markdown

ROOT = Path(__file__).resolve().parents[1]
ACCURACY_ROOT = ROOT / "benchmarks" / "accuracy"
PACKET_PATH = ACCURACY_ROOT / "review-packets/blind-v2-source-classification-batch-001.json"
CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-001-2026-07-20.json"
)
GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-001-2026-07-20.json"
)
DIFF_PATH = ROOT / "docs/reports/blind-v2-source-classification-diff-batch-001-2026-07-20.md"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def test_committed_advisories_cover_packet_and_diff_is_reproducible() -> None:
    packet = load(PACKET_PATH)
    codex = load(CODEX_PATH)
    gemini = load(GEMINI_PATH)
    packet_hash = hashlib.sha256(PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in gemini["cases"]] == [case["id"] for case in packet["cases"]]
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 60,
        "review_queue": 40,
        "by_field": {"eligible": 21, "script": 0, "domain": 28, "risk": 35},
    }
    assert len(differences) == 40
    assert gemini["stats"]["policy_violations"] == 16
    allowed_domains = {
        "it_api_cli",
        "ui_i18n",
        "llm_generated",
        "formal_news",
        "social_daily",
        "high_stakes",
        None,
    }
    allowed_risks = {"candidate_gap", "over_conversion_guard", "baseline_guard", None}
    for report in (codex, gemini):
        for case in report["cases"]:
            assert case["domain"] in allowed_domains
            assert case["risk"] in allowed_risks
            if not case["eligible"]:
                assert case["domain"] is case["risk"] is None
    assert DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet, codex, gemini, generated_date="2026-07-20"
    )
