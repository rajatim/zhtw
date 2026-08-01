"""Tests for Blind-v2 Codex/Gemini source classification comparison."""
# ruff: noqa: F401

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from scripts.build_blind_v2_codex_synthesis import build_synthesis
from scripts.compare_blind_v2_source_classifications import build_comparison, render_markdown
from scripts.record_blind_v2_source_classification_decision import (
    build_decision,
    validate_decision,
)

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
DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-001-2026-07-21.json"
)
SECOND_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-002.json"
)
SECOND_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-002-2026-07-21.json"
)
SECOND_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-002-2026-07-21.json"
)
SECOND_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-002-2026-07-21.md"
)
SECOND_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-002-2026-07-21.json"
)
THIRD_PACKET_PATH = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-003.json")
THIRD_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-003-2026-07-22.json"
)
THIRD_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-003-2026-07-22.json"
)
THIRD_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-003-2026-07-22.md"
)
THIRD_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-003-2026-07-22.json"
)
FOURTH_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-004.json"
)
FOURTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-004-2026-07-23.json"
)
FOURTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-004-2026-07-23.json"
)
FOURTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-004-2026-07-23.json"
)
FOURTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-004-2026-07-23.md"
)
FOURTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-004-2026-07-23.json"
)
FIFTH_PACKET_PATH = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-005.json")
FIFTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-005-2026-07-23.json"
)
FIFTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-005-2026-07-23.json"
)
FIFTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-005-2026-07-23.json"
)
FIFTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-005-2026-07-23.md"
)
FIFTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-005-2026-07-23.json"
)
SIXTH_PACKET_PATH = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-006.json")
SIXTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-006-2026-07-23.json"
)
SIXTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-006-2026-07-23.json"
)
SIXTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-006-2026-07-23.json"
)
SIXTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-006-2026-07-23.md"
)
SIXTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-006-2026-07-23.json"
)
SEVENTH_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-007.json"
)
SEVENTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-007-2026-07-23.json"
)
SEVENTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-007-2026-07-23.json"
)
SEVENTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-007-2026-07-23.json"
)
SEVENTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-007-2026-07-23.md"
)
SEVENTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-007-2026-07-23.json"
)
EIGHTH_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-008.json"
)
EIGHTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-008-2026-07-23.json"
)
EIGHTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-008-2026-07-23.json"
)
EIGHTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-008-2026-07-23.json"
)
EIGHTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-008-2026-07-23.md"
)
EIGHTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-008-2026-07-23.json"
)
TENTH_PACKET_PATH = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-010.json")
TENTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-010-2026-07-23.json"
)
TENTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-010-2026-07-23.json"
)
TENTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-010-2026-07-23.json"
)
TENTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-010-2026-07-23.md"
)
TENTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-010-2026-07-24.json"
)
ELEVENTH_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-011.json"
)
ELEVENTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-011-2026-07-24.json"
)
ELEVENTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-011-2026-07-24.json"
)
ELEVENTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-011-2026-07-24.json"
)
ELEVENTH_ADJUSTMENTS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-adjustments-batch-011-2026-07-24.json"
)
ELEVENTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-011-2026-07-24.md"
)
ELEVENTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-011-2026-07-24.json"
)
ELEVENTH_GEMINI_CASE_IDS = {
    "vscode-loc-zh-hans-v1/entry-0e09bd6f9c17b08d",
    "vscode-loc-zh-hans-v1/entry-28115d85b27abca4",
    "vscode-loc-zh-hans-v1/entry-3bc2558a39853869",
    "vscode-loc-zh-hans-v1/entry-695847b5a35b3aea",
}
TWELFTH_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-012.json"
)
TWELFTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-012-2026-07-24.json"
)
TWELFTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-012-2026-07-24.json"
)
TWELFTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-012-2026-07-24.json"
)
TWELFTH_ADJUSTMENTS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-adjustments-batch-012-2026-07-24.json"
)
TWELFTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-012-2026-07-24.md"
)
TWELFTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-012-2026-07-24.json"
)
THIRTEENTH_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-013.json"
)
THIRTEENTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-013-2026-07-24.json"
)
THIRTEENTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-013-2026-07-24.json"
)
THIRTEENTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-013-2026-07-24.json"
)
THIRTEENTH_ADJUSTMENTS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-adjustments-batch-013-2026-07-24.json"
)
THIRTEENTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-013-2026-07-24.md"
)
THIRTEENTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-013-2026-07-24.json"
)
THIRTEENTH_GEMINI_CASE_IDS = {
    f"zhtw-project-formal-llm-semantic-v1/{case_id}"
    for case_id in (
        "formal-036",
        "llm-009",
        "llm-011",
        "llm-012",
        "llm-015",
        "llm-016",
        "llm-021",
        "llm-024",
        "llm-025",
        "llm-026",
        "llm-027",
        "llm-028",
        "llm-032",
        "llm-033",
        "llm-034",
        "llm-035",
        "llm-036",
        "llm-037",
        "llm-041",
        "llm-042",
        "llm-044",
        "llm-045",
        "llm-046",
        "llm-049",
    )
}
FOURTEENTH_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-014.json"
)
FOURTEENTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-014-2026-07-24.json"
)
FOURTEENTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-014-2026-07-24.json"
)
FOURTEENTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-014-2026-07-24.json"
)
FOURTEENTH_ADJUSTMENTS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-adjustments-batch-014-2026-07-24.json"
)
FOURTEENTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-014-2026-07-24.md"
)
FOURTEENTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-014-2026-07-24.json"
)
FOURTEENTH_GEMINI_CASE_IDS = {
    f"aosp-framework-zh-rcn-v1/{case_id}"
    for case_id in (
        "string-04e490f612fcaa02",
        "string-114f2dd20598dd3d",
        "string-6b65b8fa97b1b2c5",
        "string-7179b94f61589660",
        "string-cd5eacc89701c0a9",
    )
}
FIFTEENTH_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-015.json"
)
FIFTEENTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-015-2026-07-24.json"
)
FIFTEENTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-015-2026-07-24.json"
)
FIFTEENTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-015-2026-07-24.json"
)
FIFTEENTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-015-2026-07-24.md"
)
FIFTEENTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-015-2026-07-24.json"
)
FIFTEENTH_GEMINI_CASE_IDS = {
    f"zhtw-project-formal-entity-guard-v1/{case_id}"
    for case_id in (
        "baseline-001",
        "baseline-002",
        "baseline-007",
        "baseline-008",
        "baseline-019",
        "code-012",
        "code-016",
        "code-018",
        "entity-015",
        "quote-001",
        "quote-003",
        "quote-005",
        "title-009",
        "title-015",
        "title-016",
    )
}
SIXTEENTH_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-016.json"
)
SIXTEENTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-016-2026-07-24.json"
)
SIXTEENTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-016-2026-07-24.json"
)
SIXTEENTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-016-2026-07-24.json"
)
SIXTEENTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-016-2026-07-24.md"
)
SIXTEENTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-016-2026-07-24.json"
)
SEVENTEENTH_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-017.json"
)
SEVENTEENTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-017-2026-07-24.json"
)
SEVENTEENTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-017-2026-07-24.json"
)
SEVENTEENTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-017-2026-07-24.json"
)
SEVENTEENTH_ADJUSTMENTS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-adjustments-batch-017-2026-07-24.json"
)
SEVENTEENTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-017-2026-07-24.md"
)
SEVENTEENTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-017-2026-07-25.json"
)
SEVENTEENTH_GEMINI_CASE_IDS = {
    "cisa-personal-security-zh-hans-v1/sentence-010",
    "cisa-personal-security-zh-hans-v1/sentence-020",
    "cisa-personal-security-zh-hans-v1/sentence-039",
}
EIGHTEENTH_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-018.json"
)
EIGHTEENTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-018-2026-07-26.json"
)
EIGHTEENTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-018-2026-07-26.json"
)
EIGHTEENTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-018-2026-07-26.json"
)
EIGHTEENTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-018-2026-07-26.md"
)
EIGHTEENTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-018-2026-07-26.json"
)
EIGHTEENTH_GEMINI_CASE_IDS = {
    f"zhtw-project-it-llm-ui-guard-v1/{case_id}"
    for case_id in (
        "llm-009",
        "llm-011",
        "llm-024",
        "llm-027",
        "ui-015",
        "ui-019",
    )
}
NINETEENTH_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-019.json"
)
NINETEENTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-019-2026-07-26.json"
)
NINETEENTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-019-2026-07-26.json"
)
NINETEENTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-019-2026-07-26.json"
)
NINETEENTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-019-2026-07-26.md"
)
NINETEENTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-019-2026-07-26.json"
)
NINETEENTH_GEMINI_CASE_IDS = {
    f"aosp-framework-zh-rcn-v1/{case_id}"
    for case_id in (
        "string-41fe8896d8230745",
        "string-5a5974d7da8c2911",
        "string-8df6c3c7d0c01665",
        "string-bcdd661feca46e04",
        "string-e4707e773f73e282",
        "string-f614093d4cc36a75",
    )
}
TWENTIETH_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-020.json"
)
TWENTIETH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-020-2026-07-26.json"
)
TWENTIETH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-020-2026-07-26.json"
)
TWENTIETH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-020-2026-07-26.json"
)
TWENTIETH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-020-2026-07-26.md"
)
TWENTIETH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-020-2026-07-26.json"
)
TWENTY_FIRST_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-021.json"
)
TWENTY_FIRST_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-021-2026-07-26.json"
)
TWENTY_FIRST_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-021-2026-07-26.json"
)
TWENTY_FIRST_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-021-2026-07-26.json"
)
TWENTY_FIRST_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-021-2026-07-26.md"
)
TWENTY_FIRST_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-021-2026-07-27.json"
)
TWENTY_FIRST_GEMINI_CASE_IDS = {"zhtw-project-balanced-baseline-guard-v1/ui-010"}
TWENTY_SECOND_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-022.json"
)
TWENTY_SECOND_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-022-2026-07-27.json"
)
TWENTY_SECOND_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-022-2026-07-27.json"
)
TWENTY_SECOND_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-022-2026-07-27.json"
)
TWENTY_SECOND_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-022-2026-07-27.md"
)
TWENTY_SECOND_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-022-2026-07-27.json"
)
TWENTY_SECOND_GEMINI_CASE_IDS = {
    "ready-gov-drought-zh-hans-v1/sentence-011",
    "ready-gov-home-fires-zh-hans-v1/sentence-045",
    "ready-gov-landslides-debris-flow-zh-hans-v1/sentence-001",
    "ready-gov-landslides-debris-flow-zh-hans-v1/sentence-002",
    "ready-gov-landslides-debris-flow-zh-hans-v1/sentence-004",
    "ready-gov-landslides-debris-flow-zh-hans-v1/sentence-009",
    "ready-gov-landslides-debris-flow-zh-hans-v1/sentence-011",
    "ready-gov-landslides-debris-flow-zh-hans-v1/sentence-023",
    "ready-gov-landslides-debris-flow-zh-hans-v1/sentence-025",
    "ready-gov-landslides-debris-flow-zh-hans-v1/sentence-028",
    "ready-gov-landslides-debris-flow-zh-hans-v1/sentence-037",
    "ready-gov-landslides-debris-flow-zh-hans-v1/sentence-047",
    "ready-gov-landslides-debris-flow-zh-hans-v1/sentence-049",
    "ready-gov-landslides-debris-flow-zh-hans-v1/sentence-053",
    "ready-gov-landslides-debris-flow-zh-hans-v1/sentence-061",
    "ready-gov-radiation-zh-hans-v1/sentence-035",
    "ready-gov-radiation-zh-hans-v1/sentence-036",
    "ready-gov-radiation-zh-hans-v1/sentence-050",
}
TWENTY_THIRD_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-023.json"
)
TWENTY_THIRD_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-023-2026-07-27.json"
)
TWENTY_THIRD_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-023-2026-07-27.json"
)
TWENTY_THIRD_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-023-2026-07-27.json"
)
TWENTY_THIRD_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-023-2026-07-27.md"
)
TWENTY_THIRD_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-023-2026-07-27.json"
)
TWENTY_FOURTH_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-024.json"
)
TWENTY_FOURTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-024-2026-07-27.json"
)
TWENTY_FOURTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-024-2026-07-27.json"
)
TWENTY_FOURTH_ADJUSTMENTS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-adjustments-batch-024-2026-07-27.json"
)
TWENTY_FOURTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-024-2026-07-27.json"
)
TWENTY_FOURTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-024-2026-07-27.md"
)
TWENTY_FOURTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-024-2026-07-27.json"
)
TWENTY_FOURTH_GEMINI_CASE_IDS = {
    f"zhtw-project-formal-llm-balance-v1/formal-{number:03d}"
    for number in (2, 3, 4, 6, 7, 9, 10, 11, 12, 13, 17, 27, 30, 31, 38, 39, 40, 42, 44, 46, 47, 49)
}
TWENTY_FIFTH_PACKET_PATH = ACCURACY_ROOT / (
    "review-packets/blind-v2-source-classification-batch-025.json"
)
TWENTY_FIFTH_CODEX_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-first-pass-batch-025-2026-07-27.json"
)
TWENTY_FIFTH_GEMINI_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-gemini-independent-batch-025-2026-07-27.json"
)
TWENTY_FIFTH_SYNTHESIS_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-codex-synthesis-batch-025-2026-07-27.json"
)
TWENTY_FIFTH_DIFF_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-diff-batch-025-2026-07-27.md"
)
TWENTY_FIFTH_DECISION_PATH = ROOT / (
    "docs/reports/blind-v2-source-classification-maintainer-decision-batch-025-2026-07-27.json"
)
TWENTY_FIFTH_GEMINI_CASE_IDS = {
    f"census-newsroom-zh-hans-v1/{case_id}"
    for case_id in (
        "page-01-sentence-036",
        "page-02-sentence-012",
        "page-03-sentence-001",
        "page-03-sentence-004",
        "page-03-sentence-005",
        "page-03-sentence-006",
        "page-03-sentence-008",
        "page-03-sentence-011",
        "page-03-sentence-021",
        "page-03-sentence-026",
        "page-03-sentence-027",
        "page-04-sentence-012",
        "page-04-sentence-014",
        "page-08-sentence-029",
        "page-08-sentence-030",
        "page-08-sentence-031",
        "page-08-sentence-034",
        "page-09-sentence-001",
    )
}


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))
