"""Tests for Blind-v2 Codex/Gemini source classification comparison."""

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


def test_synthesis_distinguishes_codex_and_maintainer_overrides() -> None:
    codex = {
        "packet_path": "packet.json",
        "packet_sha256": "a" * 64,
        "cases": [
            {
                "id": "case-1",
                "eligible": True,
                "script": "simplified",
                "domain": "formal_news",
                "risk": "baseline_guard",
                "quality_flags": [],
                "confidence": "high",
            }
        ],
    }
    gemini = json.loads(json.dumps(codex))
    override = {
        "case-1": {
            **codex["cases"][0],
            "risk": "candidate_gap",
        }
    }
    override["case-1"].pop("id")

    synthesis = build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-24",
        overrides=override,
        override_basis="codex_synthesis",
    )

    assert synthesis["cases"][0]["selection_basis"] == "codex_synthesis"
    assert synthesis["stats"]["by_selection_basis"] == {"codex_synthesis": 1}


def test_committed_advisories_cover_packet_and_diff_is_reproducible() -> None:
    packet = load(PACKET_PATH)
    codex = load(CODEX_PATH)
    gemini = load(GEMINI_PATH)
    decision = load(DECISION_PATH)
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
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 100,
        "confirmed_cases": 100,
        "resolved_disagreements": 40,
        "confirmed_exact_matches": 60,
        "remaining_cases": 0,
    }
    assert {case["id"] for case in decision["cases"]} == {case["id"] for case in packet["cases"]}
    assert sum(case["advisory_relation"] == "disagreement" for case in decision["cases"]) == 40
    assert sum(case["advisory_relation"] == "exact_match" for case in decision["cases"]) == 60
    assert all(case["selected_advisory"] == "codex" for case in decision["cases"])
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
        packet,
        codex,
        gemini,
        generated_date="2026-07-20",
        maintainer_decisions=decision,
    )


def test_committed_maintainer_decision_is_reproducible() -> None:
    assert load(DECISION_PATH) == build_decision(
        PACKET_PATH,
        CODEX_PATH,
        GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-21",
        selected_advisory="codex",
    )


def test_second_committed_advisories_cover_packet_and_diff_is_reproducible() -> None:
    packet = load(SECOND_PACKET_PATH)
    codex = load(SECOND_CODEX_PATH)
    gemini = load(SECOND_GEMINI_PATH)
    decision = load(SECOND_DECISION_PATH)
    packet_hash = hashlib.sha256(SECOND_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in gemini["cases"]] == [case["id"] for case in packet["cases"]]
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 55,
        "review_queue": 45,
        "by_field": {"eligible": 9, "script": 0, "domain": 27, "risk": 31},
    }
    assert len(differences) == 45
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert gemini["stats"]["policy_violations"] == 0
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 100,
        "confirmed_cases": 100,
        "resolved_disagreements": 45,
        "confirmed_exact_matches": 55,
        "remaining_cases": 0,
    }
    assert all(case["selected_advisory"] == "codex" for case in decision["cases"])
    assert SECOND_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-21",
        maintainer_decisions=decision,
    )


def test_second_committed_maintainer_decision_is_reproducible() -> None:
    assert load(SECOND_DECISION_PATH) == build_decision(
        SECOND_PACKET_PATH,
        SECOND_CODEX_PATH,
        SECOND_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-21",
        selected_advisory="codex",
    )


def test_third_committed_advisories_and_decision_cover_cdc_packet() -> None:
    packet = load(THIRD_PACKET_PATH)
    codex = load(THIRD_CODEX_PATH)
    gemini = load(THIRD_GEMINI_PATH)
    decision = load(THIRD_DECISION_PATH)
    packet_hash = hashlib.sha256(THIRD_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in gemini["cases"]] == [case["id"] for case in packet["cases"]]
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 62,
        "exact": 33,
        "review_queue": 29,
        "by_field": {"eligible": 1, "script": 0, "domain": 20, "risk": 21},
    }
    assert len(differences) == 29
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 62,
        "confirmed_cases": 62,
        "resolved_disagreements": 29,
        "confirmed_exact_matches": 33,
        "remaining_cases": 0,
    }
    assert sum(case["classification"]["eligible"] for case in decision["cases"]) == 61
    assert all(case["selected_advisory"] == "codex" for case in decision["cases"])
    assert THIRD_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-22",
        maintainer_decisions=decision,
    )


def test_third_committed_maintainer_decision_is_reproducible() -> None:
    assert load(THIRD_DECISION_PATH) == build_decision(
        THIRD_PACKET_PATH,
        THIRD_CODEX_PATH,
        THIRD_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-22",
        selected_advisory="codex",
    )


def test_fourth_advisories_cover_project_original_packet() -> None:
    packet = load(FOURTH_PACKET_PATH)
    codex = load(FOURTH_CODEX_PATH)
    gemini = load(FOURTH_GEMINI_PATH)
    decision = load(FOURTH_DECISION_PATH)
    packet_hash = hashlib.sha256(FOURTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in gemini["cases"]] == [case["id"] for case in packet["cases"]]
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 69,
        "review_queue": 31,
        "by_field": {"eligible": 0, "script": 0, "domain": 5, "risk": 27},
    }
    assert len(differences) == 31
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert gemini["stats"]["policy_violations"] == 0
    assert validate_decision(decision) == []
    assert all(case["selected_advisory"] == "synthesis" for case in decision["cases"])
    assert FOURTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-23",
        maintainer_decisions=decision,
    )


def test_fourth_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(FOURTH_DECISION_PATH) == build_decision(
        FOURTH_PACKET_PATH,
        FOURTH_CODEX_PATH,
        FOURTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-23",
        selected_advisory="synthesis",
        synthesis_path=FOURTH_SYNTHESIS_PATH,
    )


def test_fifth_advisories_synthesis_and_decision_cover_massive_packet() -> None:
    packet = load(FIFTH_PACKET_PATH)
    codex = load(FIFTH_CODEX_PATH)
    gemini = load(FIFTH_GEMINI_PATH)
    synthesis = load(FIFTH_SYNTHESIS_PATH)
    decision = load(FIFTH_DECISION_PATH)
    packet_hash = hashlib.sha256(FIFTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in gemini["cases"]] == [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in synthesis["cases"]] == [case["id"] for case in packet["cases"]]
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 35,
        "review_queue": 65,
        "by_field": {"eligible": 4, "script": 3, "domain": 48, "risk": 33},
    }
    assert len(differences) == 65
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert len(gemini["validation"]["rejected_attempts"]) == 2
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 98,
        "excluded": 2,
        "by_selection_basis": {
            "agreement": 35,
            "codex": 16,
            "gemini": 45,
            "hybrid": 4,
        },
    }
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 100,
        "confirmed_cases": 100,
        "resolved_disagreements": 65,
        "confirmed_exact_matches": 35,
        "remaining_cases": 0,
    }
    assert sum(case["classification"]["eligible"] for case in decision["cases"]) == 98
    assert all(case["selected_advisory"] == "synthesis" for case in decision["cases"])
    assert FIFTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-23",
        maintainer_decisions=decision,
    )


def test_fifth_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(FIFTH_DECISION_PATH) == build_decision(
        FIFTH_PACKET_PATH,
        FIFTH_CODEX_PATH,
        FIFTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-23",
        selected_advisory="synthesis",
        synthesis_path=FIFTH_SYNTHESIS_PATH,
    )


def test_sixth_advisories_and_synthesis_cover_project_it_packet() -> None:
    packet = load(SIXTH_PACKET_PATH)
    codex = load(SIXTH_CODEX_PATH)
    gemini = load(SIXTH_GEMINI_PATH)
    synthesis = load(SIXTH_SYNTHESIS_PATH)
    decision = load(SIXTH_DECISION_PATH)
    packet_hash = hashlib.sha256(SIXTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in gemini["cases"]] == [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in synthesis["cases"]] == [case["id"] for case in packet["cases"]]
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 58,
        "review_queue": 42,
        "by_field": {"eligible": 0, "script": 8, "domain": 0, "risk": 35},
    }
    assert len(differences) == 42
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 100,
        "excluded": 0,
        "by_selection_basis": {
            "agreement": 58,
            "codex": 13,
            "gemini": 28,
            "hybrid": 1,
        },
    }
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 100,
        "confirmed_cases": 100,
        "resolved_disagreements": 42,
        "confirmed_exact_matches": 58,
        "remaining_cases": 0,
    }
    assert sum(case["classification"]["eligible"] for case in decision["cases"]) == 100
    assert all(case["selected_advisory"] == "synthesis" for case in decision["cases"])
    assert SIXTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-23",
        maintainer_decisions=decision,
    )


def test_sixth_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(SIXTH_DECISION_PATH) == build_decision(
        SIXTH_PACKET_PATH,
        SIXTH_CODEX_PATH,
        SIXTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-23",
        selected_advisory="synthesis",
        synthesis_path=SIXTH_SYNTHESIS_PATH,
    )


def test_seventh_advisories_and_synthesis_cover_ftc_packet() -> None:
    packet = load(SEVENTH_PACKET_PATH)
    codex = load(SEVENTH_CODEX_PATH)
    gemini = load(SEVENTH_GEMINI_PATH)
    synthesis = load(SEVENTH_SYNTHESIS_PATH)
    decision = load(SEVENTH_DECISION_PATH)
    packet_hash = hashlib.sha256(SEVENTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 81,
        "exact": 53,
        "review_queue": 28,
        "by_field": {"eligible": 22, "script": 0, "domain": 25, "risk": 26},
    }
    assert len(differences) == 28
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert "73 eligible" in gemini["validation"]["raw_summary_mismatch"]
    assert synthesis["stats"] == {
        "total": 81,
        "eligible": 55,
        "excluded": 26,
        "by_selection_basis": {
            "agreement": 53,
            "codex": 19,
            "gemini": 8,
            "hybrid": 1,
        },
    }
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 81,
        "confirmed_cases": 81,
        "resolved_disagreements": 28,
        "confirmed_exact_matches": 53,
        "remaining_cases": 0,
    }
    assert sum(case["classification"]["eligible"] for case in decision["cases"]) == 55
    assert all(case["selected_advisory"] == "synthesis" for case in decision["cases"])
    assert SEVENTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-23",
        maintainer_decisions=decision,
    )


def test_seventh_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(SEVENTH_DECISION_PATH) == build_decision(
        SEVENTH_PACKET_PATH,
        SEVENTH_CODEX_PATH,
        SEVENTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-23",
        selected_advisory="synthesis",
        synthesis_path=SEVENTH_SYNTHESIS_PATH,
    )


def test_eighth_advisories_and_synthesis_cover_nps_acadia_packet() -> None:
    packet = load(EIGHTH_PACKET_PATH)
    codex = load(EIGHTH_CODEX_PATH)
    gemini = load(EIGHTH_GEMINI_PATH)
    synthesis = load(EIGHTH_SYNTHESIS_PATH)
    decision = load(EIGHTH_DECISION_PATH)
    packet_hash = hashlib.sha256(EIGHTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 32,
        "exact": 7,
        "review_queue": 25,
        "by_field": {"eligible": 2, "script": 0, "domain": 22, "risk": 15},
    }
    assert len(differences) == 25
    assert gemini["validation"]["exact_id_coverage"] == "32/32"
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert synthesis["stats"] == {
        "total": 32,
        "eligible": 30,
        "excluded": 2,
        "by_selection_basis": {
            "agreement": 7,
            "codex": 21,
            "gemini": 1,
            "hybrid": 3,
        },
    }
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 32,
        "confirmed_cases": 32,
        "resolved_disagreements": 25,
        "confirmed_exact_matches": 7,
        "remaining_cases": 0,
    }
    assert sum(case["classification"]["eligible"] for case in decision["cases"]) == 30
    assert all(case["selected_advisory"] == "synthesis" for case in decision["cases"])
    assert EIGHTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-23",
        maintainer_decisions=decision,
    )


def test_eighth_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(EIGHTH_DECISION_PATH) == build_decision(
        EIGHTH_PACKET_PATH,
        EIGHTH_CODEX_PATH,
        EIGHTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-23",
        selected_advisory="synthesis",
        synthesis_path=EIGHTH_SYNTHESIS_PATH,
    )


def test_tenth_advisories_synthesis_and_decision_cover_osha_packet() -> None:
    packet = load(TENTH_PACKET_PATH)
    codex = load(TENTH_CODEX_PATH)
    gemini = load(TENTH_GEMINI_PATH)
    synthesis = load(TENTH_SYNTHESIS_PATH)
    decision = load(TENTH_DECISION_PATH)
    packet_hash = hashlib.sha256(TENTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    packet_ids = [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert [case["id"] for case in synthesis["cases"]] == packet_ids
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 41,
        "review_queue": 59,
        "by_field": {"eligible": 17, "script": 0, "domain": 20, "risk": 59},
    }
    assert len(differences) == 59
    assert gemini["validation"]["exact_id_coverage"] == "100/100"
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 85,
        "excluded": 15,
        "by_selection_basis": {"agreement": 41, "codex": 56, "gemini": 3},
    }
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 100,
        "confirmed_cases": 100,
        "resolved_disagreements": 59,
        "confirmed_exact_matches": 41,
        "remaining_cases": 0,
    }
    assert sum(case["classification"]["eligible"] for case in decision["cases"]) == 85
    assert all(case["selected_advisory"] == "synthesis" for case in decision["cases"])
    assert TENTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-23",
        maintainer_decisions=decision,
    )


def test_tenth_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(TENTH_DECISION_PATH) == build_decision(
        TENTH_PACKET_PATH,
        TENTH_CODEX_PATH,
        TENTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-24",
        selected_advisory="synthesis",
        synthesis_path=TENTH_SYNTHESIS_PATH,
    )


def test_eleventh_advisories_and_pending_synthesis_cover_vscode_packet() -> None:
    packet = load(ELEVENTH_PACKET_PATH)
    codex = load(ELEVENTH_CODEX_PATH)
    gemini = load(ELEVENTH_GEMINI_PATH)
    synthesis = load(ELEVENTH_SYNTHESIS_PATH)
    adjustments = load(ELEVENTH_ADJUSTMENTS_PATH)
    decision = load(ELEVENTH_DECISION_PATH)
    packet_hash = hashlib.sha256(ELEVENTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    packet_ids = [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert [case["id"] for case in synthesis["cases"]] == packet_ids
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 35,
        "review_queue": 65,
        "by_field": {"eligible": 4, "script": 0, "domain": 31, "risk": 50},
    }
    assert len(differences) == 65
    assert gemini["validation"]["exact_id_coverage"] == "100/100"
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 100,
        "excluded": 0,
        "by_selection_basis": {
            "agreement": 35,
            "codex": 57,
            "gemini": 4,
            "maintainer_feedback": 4,
        },
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=ELEVENTH_GEMINI_CASE_IDS,
        generated_date="2026-07-24",
        overrides=overrides,
    )
    assert validate_decision(decision) == []
    assert sum(case["classification"]["eligible"] for case in decision["cases"]) == 100
    rendered_diff = render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-24",
        maintainer_decisions=decision,
    )
    assert ELEVENTH_DIFF_PATH.read_text(encoding="utf-8") == rendered_diff
    assert all(line == line.rstrip() for line in rendered_diff.splitlines())


def test_eleventh_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(ELEVENTH_DECISION_PATH) == build_decision(
        ELEVENTH_PACKET_PATH,
        ELEVENTH_CODEX_PATH,
        ELEVENTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-24",
        selected_advisory="synthesis",
        synthesis_path=ELEVENTH_SYNTHESIS_PATH,
    )


def test_twelfth_advisories_and_pending_synthesis_cover_ftc_heads_up_packet() -> None:
    packet = load(TWELFTH_PACKET_PATH)
    codex = load(TWELFTH_CODEX_PATH)
    gemini = load(TWELFTH_GEMINI_PATH)
    synthesis = load(TWELFTH_SYNTHESIS_PATH)
    adjustments = load(TWELFTH_ADJUSTMENTS_PATH)
    decision = load(TWELFTH_DECISION_PATH)
    packet_hash = hashlib.sha256(TWELFTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    packet_ids = [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert [case["id"] for case in synthesis["cases"]] == packet_ids
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 49,
        "review_queue": 51,
        "by_field": {"eligible": 1, "script": 0, "domain": 25, "risk": 34},
    }
    assert len(differences) == 51
    assert gemini["validation"]["exact_id_coverage"] == "100/100"
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert gemini["validation"]["response_json_extracted_from_markdown_fence"] is True
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 100,
        "excluded": 0,
        "by_selection_basis": {
            "agreement": 49,
            "codex": 50,
            "maintainer_feedback": 1,
        },
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-24",
        overrides=overrides,
    )
    assert validate_decision(decision) == []
    assert sum(case["classification"]["eligible"] for case in decision["cases"]) == 100
    assert TWELFTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-24",
        maintainer_decisions=decision,
    )


def test_twelfth_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(TWELFTH_DECISION_PATH) == build_decision(
        TWELFTH_PACKET_PATH,
        TWELFTH_CODEX_PATH,
        TWELFTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-24",
        selected_advisory="synthesis",
        synthesis_path=TWELFTH_SYNTHESIS_PATH,
    )


def test_thirteenth_advisories_and_codex_synthesis_are_reproducible() -> None:
    packet = load(THIRTEENTH_PACKET_PATH)
    codex = load(THIRTEENTH_CODEX_PATH)
    gemini = load(THIRTEENTH_GEMINI_PATH)
    synthesis = load(THIRTEENTH_SYNTHESIS_PATH)
    decision = load(THIRTEENTH_DECISION_PATH)
    adjustments = load(THIRTEENTH_ADJUSTMENTS_PATH)
    packet_hash = hashlib.sha256(THIRTEENTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    packet_ids = [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert [case["id"] for case in synthesis["cases"]] == packet_ids
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 57,
        "review_queue": 43,
        "by_field": {"eligible": 0, "script": 0, "domain": 11, "risk": 35},
    }
    assert len(differences) == 43
    assert gemini["reviewer"] == "Gemini via Antigravity CLI"
    assert gemini["model"] == "gemini-3.1-pro-high"
    assert gemini["validation"]["exact_id_coverage"] == "100/100"
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 100,
        "excluded": 0,
        "by_selection_basis": {
            "agreement": 57,
            "codex": 16,
            "codex_synthesis": 3,
            "gemini": 24,
        },
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=THIRTEENTH_GEMINI_CASE_IDS,
        generated_date="2026-07-24",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert THIRTEENTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-24",
        maintainer_decisions=decision,
    )


def test_thirteenth_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(THIRTEENTH_DECISION_PATH) == build_decision(
        THIRTEENTH_PACKET_PATH,
        THIRTEENTH_CODEX_PATH,
        THIRTEENTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-24",
        selected_advisory="synthesis",
        synthesis_path=THIRTEENTH_SYNTHESIS_PATH,
    )


def test_fourteenth_advisories_and_codex_synthesis_are_reproducible() -> None:
    packet = load(FOURTEENTH_PACKET_PATH)
    codex = load(FOURTEENTH_CODEX_PATH)
    gemini = load(FOURTEENTH_GEMINI_PATH)
    synthesis = load(FOURTEENTH_SYNTHESIS_PATH)
    decision = load(FOURTEENTH_DECISION_PATH)
    adjustments = load(FOURTEENTH_ADJUSTMENTS_PATH)
    packet_hash = hashlib.sha256(FOURTEENTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    packet_ids = [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert [case["id"] for case in synthesis["cases"]] == packet_ids
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 75,
        "review_queue": 25,
        "by_field": {"eligible": 0, "script": 0, "domain": 1, "risk": 25},
    }
    assert len(differences) == 25
    assert gemini["reviewer"] == "Gemini via Antigravity CLI"
    assert gemini["model"] == "gemini-3.1-pro-high"
    assert gemini["validation"]["exact_id_coverage"] == "100/100"
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 100,
        "excluded": 0,
        "by_selection_basis": {
            "agreement": 75,
            "codex": 19,
            "codex_synthesis": 1,
            "gemini": 5,
        },
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=FOURTEENTH_GEMINI_CASE_IDS,
        generated_date="2026-07-24",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert FOURTEENTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-24",
        maintainer_decisions=decision,
    )


def test_fourteenth_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(FOURTEENTH_DECISION_PATH) == build_decision(
        FOURTEENTH_PACKET_PATH,
        FOURTEENTH_CODEX_PATH,
        FOURTEENTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-24",
        selected_advisory="synthesis",
        synthesis_path=FOURTEENTH_SYNTHESIS_PATH,
    )


def test_fifteenth_pending_advisories_and_codex_synthesis_are_reproducible() -> None:
    packet = load(FIFTEENTH_PACKET_PATH)
    codex = load(FIFTEENTH_CODEX_PATH)
    gemini = load(FIFTEENTH_GEMINI_PATH)
    synthesis = load(FIFTEENTH_SYNTHESIS_PATH)
    decision = load(FIFTEENTH_DECISION_PATH)
    packet_hash = hashlib.sha256(FIFTEENTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    packet_ids = [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert [case["id"] for case in synthesis["cases"]] == packet_ids
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 73,
        "review_queue": 27,
        "by_field": {"eligible": 0, "script": 0, "domain": 24, "risk": 3},
    }
    assert len(differences) == 27
    assert gemini["reviewer"] == "Gemini via Antigravity CLI"
    assert gemini["model"] == "gemini-3.1-pro-high"
    assert gemini["validation"]["exact_id_coverage"] == "100/100"
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 100,
        "excluded": 0,
        "by_selection_basis": {"agreement": 73, "codex": 12, "gemini": 15},
    }
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=FIFTEENTH_GEMINI_CASE_IDS,
        generated_date="2026-07-24",
    )
    assert FIFTEENTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-24",
        maintainer_decisions=decision,
    )


def test_fifteenth_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(FIFTEENTH_DECISION_PATH) == build_decision(
        FIFTEENTH_PACKET_PATH,
        FIFTEENTH_CODEX_PATH,
        FIFTEENTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-24",
        selected_advisory="synthesis",
        synthesis_path=FIFTEENTH_SYNTHESIS_PATH,
    )


def test_sixteenth_advisories_and_codex_synthesis_are_reproducible() -> None:
    packet = load(SIXTEENTH_PACKET_PATH)
    codex = load(SIXTEENTH_CODEX_PATH)
    gemini = load(SIXTEENTH_GEMINI_PATH)
    synthesis = load(SIXTEENTH_SYNTHESIS_PATH)
    decision = load(SIXTEENTH_DECISION_PATH)
    packet_hash = hashlib.sha256(SIXTEENTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    packet_ids = [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert [case["id"] for case in synthesis["cases"]] == packet_ids
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 24,
        "exact": 1,
        "review_queue": 23,
        "by_field": {"eligible": 3, "script": 0, "domain": 23, "risk": 3},
    }
    assert len(differences) == 23
    assert gemini["reviewer"] == "Gemini via Antigravity CLI"
    assert gemini["model"] == "gemini-3.1-pro-high"
    assert gemini["validation"]["exact_id_coverage"] == "24/24"
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert synthesis["stats"] == {
        "total": 24,
        "eligible": 21,
        "excluded": 3,
        "by_selection_basis": {"agreement": 1, "codex": 23},
    }
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-24",
    )
    assert SIXTEENTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-24",
        maintainer_decisions=decision,
    )


def test_sixteenth_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(SIXTEENTH_DECISION_PATH) == build_decision(
        SIXTEENTH_PACKET_PATH,
        SIXTEENTH_CODEX_PATH,
        SIXTEENTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-24",
        selected_advisory="synthesis",
        synthesis_path=SIXTEENTH_SYNTHESIS_PATH,
    )


def test_seventeenth_advisories_and_codex_synthesis_are_reproducible() -> None:
    packet = load(SEVENTEENTH_PACKET_PATH)
    codex = load(SEVENTEENTH_CODEX_PATH)
    gemini = load(SEVENTEENTH_GEMINI_PATH)
    synthesis = load(SEVENTEENTH_SYNTHESIS_PATH)
    decision = load(SEVENTEENTH_DECISION_PATH)
    packet_hash = hashlib.sha256(SEVENTEENTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    packet_ids = [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert [case["id"] for case in synthesis["cases"]] == packet_ids
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 55,
        "review_queue": 45,
        "by_field": {"eligible": 3, "script": 0, "domain": 26, "risk": 31},
    }
    assert len(differences) == 45
    assert gemini["reviewer"] == "Gemini via Antigravity CLI"
    assert gemini["model"] == "gemini-3.1-pro-high"
    assert gemini["validation"]["exact_id_coverage"] == "100/100"
    assert gemini["validation"]["tool_calls"] == 0
    assert gemini["validation"]["api_errors"] == 0
    assert gemini["validation"]["successful_chunks"] == 4
    assert gemini["validation"]["discarded_unusable_responses"] == 8
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 90,
        "excluded": 10,
        "by_selection_basis": {
            "agreement": 55,
            "codex": 41,
            "codex_synthesis": 1,
            "gemini": 3,
        },
    }
    adjustments = load(SEVENTEENTH_ADJUSTMENTS_PATH)
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=SEVENTEENTH_GEMINI_CASE_IDS,
        generated_date="2026-07-24",
        overrides={case["id"]: case["classification"] for case in adjustments["cases"]},
        override_basis="codex_synthesis",
    )
    assert SEVENTEENTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-24",
        maintainer_decisions=decision,
    )


def test_seventeenth_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(SEVENTEENTH_DECISION_PATH) == build_decision(
        SEVENTEENTH_PACKET_PATH,
        SEVENTEENTH_CODEX_PATH,
        SEVENTEENTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-25",
        selected_advisory="synthesis",
        synthesis_path=SEVENTEENTH_SYNTHESIS_PATH,
    )


def test_eighteenth_advisories_and_confirmed_synthesis_are_reproducible() -> None:
    packet = load(EIGHTEENTH_PACKET_PATH)
    codex = load(EIGHTEENTH_CODEX_PATH)
    gemini = load(EIGHTEENTH_GEMINI_PATH)
    synthesis = load(EIGHTEENTH_SYNTHESIS_PATH)
    decision = load(EIGHTEENTH_DECISION_PATH)
    packet_hash = hashlib.sha256(EIGHTEENTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    packet_ids = [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert [case["id"] for case in synthesis["cases"]] == packet_ids
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 61,
        "review_queue": 39,
        "by_field": {"eligible": 0, "script": 0, "domain": 0, "risk": 39},
    }
    assert len(differences) == 39
    assert gemini["reviewer"] == "Gemini via Gemini CLI"
    assert gemini["model"] == "gemini-2.5-pro"
    assert gemini["execution"]["cli_version"] == "0.52.0"
    assert gemini["execution"]["tool_calls"] == 0
    assert gemini["execution"]["total_errors"] == 0
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 100,
        "excluded": 0,
        "by_selection_basis": {"agreement": 61, "codex": 33, "gemini": 6},
    }
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=EIGHTEENTH_GEMINI_CASE_IDS,
        generated_date="2026-07-26",
    )
    assert EIGHTEENTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-26",
        maintainer_decisions=decision,
    )


def test_eighteenth_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(EIGHTEENTH_DECISION_PATH) == build_decision(
        EIGHTEENTH_PACKET_PATH,
        EIGHTEENTH_CODEX_PATH,
        EIGHTEENTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-26",
        selected_advisory="synthesis",
        synthesis_path=EIGHTEENTH_SYNTHESIS_PATH,
    )


def test_nineteenth_advisories_and_confirmed_synthesis_are_reproducible() -> None:
    packet = load(NINETEENTH_PACKET_PATH)
    codex = load(NINETEENTH_CODEX_PATH)
    gemini = load(NINETEENTH_GEMINI_PATH)
    synthesis = load(NINETEENTH_SYNTHESIS_PATH)
    decision = load(NINETEENTH_DECISION_PATH)
    packet_hash = hashlib.sha256(NINETEENTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    packet_ids = [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert [case["id"] for case in synthesis["cases"]] == packet_ids
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 39,
        "review_queue": 61,
        "by_field": {"eligible": 3, "script": 0, "domain": 0, "risk": 59},
    }
    assert len(differences) == 61
    assert gemini["reviewer"] == "Gemini via Gemini CLI"
    assert gemini["model"] == "gemini-2.5-pro"
    assert gemini["execution"]["cli_version"] == "0.52.0"
    assert gemini["execution"]["tool_calls"] == 0
    assert gemini["execution"]["total_errors"] == 0
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 97,
        "excluded": 3,
        "by_selection_basis": {"agreement": 39, "codex": 55, "gemini": 6},
    }
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=NINETEENTH_GEMINI_CASE_IDS,
        generated_date="2026-07-26",
    )
    assert NINETEENTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-26",
        maintainer_decisions=decision,
    )


def test_nineteenth_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(NINETEENTH_DECISION_PATH) == build_decision(
        NINETEENTH_PACKET_PATH,
        NINETEENTH_CODEX_PATH,
        NINETEENTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-26",
        selected_advisory="synthesis",
        synthesis_path=NINETEENTH_SYNTHESIS_PATH,
    )


def test_twentieth_advisories_and_confirmed_synthesis_are_reproducible() -> None:
    packet = load(TWENTIETH_PACKET_PATH)
    codex = load(TWENTIETH_CODEX_PATH)
    gemini = load(TWENTIETH_GEMINI_PATH)
    synthesis = load(TWENTIETH_SYNTHESIS_PATH)
    decision = load(TWENTIETH_DECISION_PATH)
    packet_hash = hashlib.sha256(TWENTIETH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    packet_ids = [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert [case["id"] for case in synthesis["cases"]] == packet_ids
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 23,
        "review_queue": 77,
        "by_field": {"eligible": 6, "script": 0, "domain": 34, "risk": 59},
    }
    assert len(differences) == 77
    assert gemini["reviewer"] == "Gemini via Gemini CLI"
    assert gemini["model"] == "gemini-2.5-pro"
    assert gemini["execution"]["cli_version"] == "0.52.0"
    assert gemini["execution"]["tool_calls"] == 0
    assert gemini["execution"]["total_errors"] == 0
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 87,
        "excluded": 13,
        "by_selection_basis": {"agreement": 23, "codex": 77},
    }
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-26",
    )
    assert TWENTIETH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-26",
        maintainer_decisions=decision,
    )


def test_twentieth_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(TWENTIETH_DECISION_PATH) == build_decision(
        TWENTIETH_PACKET_PATH,
        TWENTIETH_CODEX_PATH,
        TWENTIETH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-26",
        selected_advisory="synthesis",
        synthesis_path=TWENTIETH_SYNTHESIS_PATH,
    )


def test_twenty_first_advisories_synthesis_and_decision_are_reproducible() -> None:
    packet = load(TWENTY_FIRST_PACKET_PATH)
    codex = load(TWENTY_FIRST_CODEX_PATH)
    gemini = load(TWENTY_FIRST_GEMINI_PATH)
    synthesis = load(TWENTY_FIRST_SYNTHESIS_PATH)
    decision = load(TWENTY_FIRST_DECISION_PATH)
    packet_hash = hashlib.sha256(TWENTY_FIRST_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    packet_ids = [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert [case["id"] for case in synthesis["cases"]] == packet_ids
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 47,
        "review_queue": 53,
        "by_field": {"eligible": 0, "script": 40, "domain": 0, "risk": 13},
    }
    assert len(differences) == 53
    assert gemini["reviewer"] == "Gemini via Gemini CLI"
    assert gemini["model"] == "gemini-2.5-pro"
    assert gemini["execution"]["cli_version"] == "0.52.0"
    assert gemini["execution"]["tool_calls"] == 0
    assert gemini["execution"]["total_errors"] == 0
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 100,
        "excluded": 0,
        "by_selection_basis": {"agreement": 47, "codex": 52, "gemini": 1},
    }
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=TWENTY_FIRST_GEMINI_CASE_IDS,
        generated_date="2026-07-26",
    )
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 100,
        "confirmed_cases": 100,
        "resolved_disagreements": 53,
        "confirmed_exact_matches": 47,
        "remaining_cases": 0,
    }
    assert all(case["selected_advisory"] == "synthesis" for case in decision["cases"])
    assert TWENTY_FIRST_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-26",
        maintainer_decisions=decision,
    )


def test_twenty_first_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(TWENTY_FIRST_DECISION_PATH) == build_decision(
        TWENTY_FIRST_PACKET_PATH,
        TWENTY_FIRST_CODEX_PATH,
        TWENTY_FIRST_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-27",
        selected_advisory="synthesis",
        synthesis_path=TWENTY_FIRST_SYNTHESIS_PATH,
    )


def test_twenty_second_advisories_synthesis_and_decision_are_reproducible() -> None:
    packet = load(TWENTY_SECOND_PACKET_PATH)
    codex = load(TWENTY_SECOND_CODEX_PATH)
    gemini = load(TWENTY_SECOND_GEMINI_PATH)
    synthesis = load(TWENTY_SECOND_SYNTHESIS_PATH)
    decision = load(TWENTY_SECOND_DECISION_PATH)
    packet_hash = hashlib.sha256(TWENTY_SECOND_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    packet_ids = [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert [case["id"] for case in synthesis["cases"]] == packet_ids
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 43,
        "review_queue": 57,
        "by_field": {"eligible": 7, "script": 0, "domain": 26, "risk": 39},
    }
    assert len(differences) == 57
    assert gemini["execution"]["cli_version"] == "0.52.0"
    assert gemini["execution"]["tool_calls"] == 0
    assert gemini["execution"]["total_errors"] == 0
    assert gemini["stats"]["policy_violations"] == 10
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 93,
        "excluded": 7,
        "by_selection_basis": {"agreement": 43, "codex": 39, "gemini": 18},
    }
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=TWENTY_SECOND_GEMINI_CASE_IDS,
        generated_date="2026-07-27",
    )
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 100,
        "confirmed_cases": 100,
        "resolved_disagreements": 57,
        "confirmed_exact_matches": 43,
        "remaining_cases": 0,
    }
    assert all(case["selected_advisory"] == "synthesis" for case in decision["cases"])
    assert TWENTY_SECOND_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-27",
        maintainer_decisions=decision,
    )


def test_twenty_second_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(TWENTY_SECOND_DECISION_PATH) == build_decision(
        TWENTY_SECOND_PACKET_PATH,
        TWENTY_SECOND_CODEX_PATH,
        TWENTY_SECOND_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-27",
        selected_advisory="synthesis",
        synthesis_path=TWENTY_SECOND_SYNTHESIS_PATH,
    )


def test_twenty_third_advisories_synthesis_and_decision_are_reproducible() -> None:
    packet = load(TWENTY_THIRD_PACKET_PATH)
    codex = load(TWENTY_THIRD_CODEX_PATH)
    gemini = load(TWENTY_THIRD_GEMINI_PATH)
    synthesis = load(TWENTY_THIRD_SYNTHESIS_PATH)
    decision = load(TWENTY_THIRD_DECISION_PATH)
    packet_hash = hashlib.sha256(TWENTY_THIRD_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    packet_ids = [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert [case["id"] for case in synthesis["cases"]] == packet_ids
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 85,
        "review_queue": 15,
        "by_field": {"eligible": 2, "script": 0, "domain": 2, "risk": 15},
    }
    assert len(differences) == 15
    assert gemini["execution"]["cli_version"] == "0.52.0"
    assert gemini["execution"]["tool_calls"] == 0
    assert gemini["execution"]["total_errors"] == 0
    assert gemini["stats"]["policy_violations"] == 0
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 98,
        "excluded": 2,
        "by_selection_basis": {
            "agreement": 85,
            "codex": 15,
        },
    }
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-27",
    )
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 100,
        "confirmed_cases": 100,
        "resolved_disagreements": 15,
        "confirmed_exact_matches": 85,
        "remaining_cases": 0,
    }
    assert all(case["selected_advisory"] == "synthesis" for case in decision["cases"])
    assert TWENTY_THIRD_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-27",
        maintainer_decisions=decision,
    )


def test_twenty_third_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(TWENTY_THIRD_DECISION_PATH) == build_decision(
        TWENTY_THIRD_PACKET_PATH,
        TWENTY_THIRD_CODEX_PATH,
        TWENTY_THIRD_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-27",
        selected_advisory="synthesis",
        synthesis_path=TWENTY_THIRD_SYNTHESIS_PATH,
    )


def test_twenty_fourth_advisories_synthesis_and_decision_are_reproducible() -> None:
    packet = load(TWENTY_FOURTH_PACKET_PATH)
    codex = load(TWENTY_FOURTH_CODEX_PATH)
    gemini = load(TWENTY_FOURTH_GEMINI_PATH)
    adjustments = load(TWENTY_FOURTH_ADJUSTMENTS_PATH)
    synthesis = load(TWENTY_FOURTH_SYNTHESIS_PATH)
    decision = load(TWENTY_FOURTH_DECISION_PATH)
    packet_hash = hashlib.sha256(TWENTY_FOURTH_PACKET_PATH.read_bytes()).hexdigest()

    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    packet_ids = [case["id"] for case in packet["cases"]]
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert [case["id"] for case in synthesis["cases"]] == packet_ids
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 59,
        "review_queue": 41,
        "by_field": {"eligible": 0, "script": 0, "domain": 15, "risk": 40},
    }
    assert len(differences) == 41
    assert gemini["execution"] == {
        "cli": "@google/gemini-cli",
        "cli_version": "0.52.0",
        "session_id": "7fe17c8a-9716-4454-8872-11cc28da98ee",
        "tool_calls": 0,
        "total_errors": 0,
    }
    assert gemini["stats"]["policy_violations"] == 0
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 100,
        "excluded": 0,
        "by_selection_basis": {
            "agreement": 59,
            "codex": 8,
            "codex_synthesis": 11,
            "gemini": 22,
        },
    }
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=TWENTY_FOURTH_GEMINI_CASE_IDS,
        generated_date="2026-07-27",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 100,
        "confirmed_cases": 100,
        "resolved_disagreements": 41,
        "confirmed_exact_matches": 59,
        "remaining_cases": 0,
    }
    assert all(case["selected_advisory"] == "synthesis" for case in decision["cases"])
    assert TWENTY_FOURTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-27",
        maintainer_decisions=decision,
    )


def test_twenty_fourth_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(TWENTY_FOURTH_DECISION_PATH) == build_decision(
        TWENTY_FOURTH_PACKET_PATH,
        TWENTY_FOURTH_CODEX_PATH,
        TWENTY_FOURTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-27",
        selected_advisory="synthesis",
        synthesis_path=TWENTY_FOURTH_SYNTHESIS_PATH,
    )


def test_twenty_fifth_advisories_synthesis_and_decision_are_reproducible() -> None:
    packet = load(TWENTY_FIFTH_PACKET_PATH)
    codex = load(TWENTY_FIFTH_CODEX_PATH)
    gemini = load(TWENTY_FIFTH_GEMINI_PATH)
    synthesis = load(TWENTY_FIFTH_SYNTHESIS_PATH)
    decision = load(TWENTY_FIFTH_DECISION_PATH)
    packet_hash = hashlib.sha256(TWENTY_FIFTH_PACKET_PATH.read_bytes()).hexdigest()

    packet_ids = [case["id"] for case in packet["cases"]]
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert [case["id"] for case in synthesis["cases"]] == packet_ids
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 47,
        "review_queue": 53,
        "by_field": {"eligible": 7, "script": 3, "domain": 17, "risk": 49},
    }
    assert len(differences) == 53
    assert gemini["execution"] == {
        "cli": "@google/gemini-cli",
        "cli_version": "0.52.0",
        "session_id": "faf72476-cb78-4512-8825-fd16eabdd17f",
        "tool_calls": 0,
        "total_errors": 0,
    }
    assert gemini["stats"]["policy_violations"] == 0
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 88,
        "excluded": 12,
        "by_selection_basis": {"agreement": 47, "codex": 35, "gemini": 18},
    }
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=TWENTY_FIFTH_GEMINI_CASE_IDS,
        generated_date="2026-07-27",
    )
    assert validate_decision(decision) == []
    assert decision["stats"] == {
        "packet_cases": 100,
        "confirmed_cases": 100,
        "resolved_disagreements": 53,
        "confirmed_exact_matches": 47,
        "remaining_cases": 0,
    }
    assert all(case["selected_advisory"] == "synthesis" for case in decision["cases"])
    assert TWENTY_FIFTH_DIFF_PATH.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-27",
        maintainer_decisions=decision,
    )


def test_twenty_fifth_maintainer_synthesis_decision_is_reproducible() -> None:
    assert load(TWENTY_FIFTH_DECISION_PATH) == build_decision(
        TWENTY_FIFTH_PACKET_PATH,
        TWENTY_FIFTH_CODEX_PATH,
        TWENTY_FIFTH_GEMINI_PATH,
        maintainer="tim",
        decision_date="2026-07-27",
        selected_advisory="synthesis",
        synthesis_path=TWENTY_FIFTH_SYNTHESIS_PATH,
    )


def test_twenty_sixth_and_seventh_synthesis_decisions_are_reproducible() -> None:
    expected_stats = {
        26: {"total": 80, "eligible": 80, "excluded": 0},
        27: {"total": 100, "eligible": 92, "excluded": 8},
    }
    for batch_number in (26, 27):
        packet = ACCURACY_ROOT / (
            f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )
        prefix = ROOT / "docs/reports"
        codex = prefix / (
            "blind-v2-source-classification-codex-first-pass-"
            f"batch-{batch_number:03d}-2026-07-27.json"
        )
        gemini = prefix / (
            "blind-v2-source-classification-gemini-independent-"
            f"batch-{batch_number:03d}-2026-07-27.json"
        )
        adjustments = prefix / (
            "blind-v2-source-classification-codex-synthesis-adjustments-"
            f"batch-{batch_number:03d}-2026-07-27.json"
        )
        synthesis = prefix / (
            "blind-v2-source-classification-codex-synthesis-"
            f"batch-{batch_number:03d}-2026-07-27.json"
        )
        decision = prefix / (
            "blind-v2-source-classification-maintainer-decision-"
            f"batch-{batch_number:03d}-2026-07-27.json"
        )
        diff = prefix / (
            f"blind-v2-source-classification-diff-batch-{batch_number:03d}-2026-07-27.md"
        )
        packet_data = load(packet)
        codex_data = load(codex)
        gemini_data = load(gemini)
        adjustments_data = load(adjustments)
        synthesis_data = load(synthesis)
        decision_data = load(decision)
        overrides = {case["id"]: case["classification"] for case in adjustments_data["cases"]}

        assert synthesis_data == build_synthesis(
            codex_data,
            gemini_data,
            gemini_case_ids=set(),
            generated_date="2026-07-27",
            overrides=overrides,
            override_basis="codex_synthesis",
        )
        assert synthesis_data["stats"] == {
            **expected_stats[batch_number],
            "by_selection_basis": {"codex_synthesis": expected_stats[batch_number]["total"]},
        }
        assert decision_data == build_decision(
            packet,
            codex,
            gemini,
            maintainer="tim",
            decision_date="2026-07-27",
            selected_advisory="synthesis",
            synthesis_path=synthesis,
        )
        assert diff.read_text(encoding="utf-8") == render_markdown(
            packet_data,
            codex_data,
            gemini_data,
            generated_date="2026-07-27",
            maintainer_decisions=decision_data,
        )


def test_twenty_eighth_synthesis_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-028.json")
    prior_packet_path = ACCURACY_ROOT / (
        "review-packets/blind-v2-source-classification-batch-027.json"
    )
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-028-2026-07-27.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-028-2026-07-27.json"
    )
    adjustments_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-adjustments-batch-028-2026-07-27.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-028-2026-07-27.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-028-2026-07-27.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-028-2026-07-27.md"
    packet = load(packet_path)
    prior_packet = load(prior_packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()
    packet_ids = [case["id"] for case in packet["cases"]]

    assert packet["selection_policy"] == "balanced-remaining-deterministic-sha256-v1"
    assert packet["stats"] == {"total": 90, "by_source": {"kubernetes-docs-zh-cn-v1": 90}}
    assert set(packet_ids).isdisjoint(case["id"] for case in prior_packet["cases"])
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert gemini["execution"] == {
        "cli": "@google/gemini-cli",
        "cli_version": "0.52.0",
        "session_id": "0341974b-d3bf-4c6b-b1eb-e1cac1d01f56",
        "tool_calls": 0,
        "total_errors": 0,
    }
    assert gemini["stats"]["policy_violations"] == 0
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 90,
        "exact": 3,
        "review_queue": 87,
        "by_field": {"eligible": 10, "script": 74, "domain": 10, "risk": 40},
    }
    assert len(differences) == 87
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-27",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 90,
        "eligible": 80,
        "excluded": 10,
        "by_selection_basis": {"codex_synthesis": 90},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-27",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 90,
        "confirmed_cases": 90,
        "resolved_disagreements": 87,
        "confirmed_exact_matches": 3,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-27",
        maintainer_decisions=decision,
    )


def test_twenty_ninth_synthesis_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-029.json")
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-029-2026-07-27.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-029-2026-07-27.json"
    )
    adjustments_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-adjustments-batch-029-2026-07-27.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-029-2026-07-27.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-029-2026-07-27.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-029-2026-07-27.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 29)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }

    assert packet["selection_policy"] == "balanced-remaining-deterministic-sha256-v1"
    assert packet["stats"]["total"] == 70
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert gemini["execution"] == {
        "cli": "@google/gemini-cli",
        "cli_version": "0.52.0",
        "session_id": "ce278b43-730a-4bc6-bf11-257bc6fd6c3b",
        "tool_calls": 0,
        "total_errors": 0,
    }
    assert gemini["stats"]["policy_violations"] == 0
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 70,
        "exact": 18,
        "review_queue": 52,
        "by_field": {"eligible": 5, "script": 6, "domain": 15, "risk": 50},
    }
    assert len(differences) == 52
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-27",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 70,
        "eligible": 65,
        "excluded": 5,
        "by_selection_basis": {"codex_synthesis": 70},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-27",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 70,
        "confirmed_cases": 70,
        "resolved_disagreements": 52,
        "confirmed_exact_matches": 18,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-27",
        maintainer_decisions=decision,
    )


def test_thirtieth_synthesis_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-030.json")
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-030-2026-07-27.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-030-2026-07-27.json"
    )
    adjustments_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-adjustments-batch-030-2026-07-27.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-030-2026-07-27.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-030-2026-07-27.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-030-2026-07-27.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 30)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }

    assert packet["selection_policy"] == "balanced-remaining-deterministic-sha256-v1"
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "aosp-framework-zh-rcn-v1": 16,
            "census-newsroom-zh-hans-v1": 16,
            "chromium-strings-zh-cn-v1": 16,
            "kubernetes-docs-zh-cn-v1": 16,
            "massive-1-0-zh-cn-v1": 16,
            "ready-gov-radiation-zh-hans-v1": 16,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert gemini["execution"] == {
        "cli": "@google/gemini-cli",
        "cli_version": "0.52.0",
        "session_id": "e627b12b-9f5c-47ba-a178-8360b9424634",
        "tool_calls": 0,
        "total_errors": 0,
    }
    assert gemini["stats"]["policy_violations"] == 0
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 33,
        "review_queue": 63,
        "by_field": {"eligible": 8, "script": 11, "domain": 23, "risk": 54},
    }
    assert len(differences) == 63
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-27",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 88,
        "excluded": 8,
        "by_selection_basis": {"codex_synthesis": 96},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-27",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 63,
        "confirmed_exact_matches": 33,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-27",
        maintainer_decisions=decision,
    )


def test_thirty_first_synthesis_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-031.json")
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-031-2026-07-27.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-031-2026-07-27.json"
    )
    adjustments_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-adjustments-batch-031-2026-07-27.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-031-2026-07-27.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-031-2026-07-27.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-031-2026-07-27.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 31)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }

    assert packet["selection_policy"] == "all-source-cases-sorted-v1"
    assert packet["stats"] == {
        "total": 100,
        "by_source": {"zhtw-project-llm-domain-balance-v1": 100},
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert gemini["execution"] == {
        "cli": "@google/gemini-cli",
        "cli_version": "0.52.0",
        "session_id": "26231404-30c8-424a-bf1a-d4195510450c",
        "tool_calls": 0,
        "total_errors": 0,
    }
    assert gemini["stats"]["policy_violations"] == 0
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 100,
        "exact": 43,
        "review_queue": 57,
        "by_field": {"eligible": 0, "script": 1, "domain": 25, "risk": 39},
    }
    assert len(differences) == 57
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-27",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 100,
        "eligible": 100,
        "excluded": 0,
        "by_selection_basis": {"codex_synthesis": 100},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-27",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 100,
        "confirmed_cases": 100,
        "resolved_disagreements": 57,
        "confirmed_exact_matches": 43,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-27",
        maintainer_decisions=decision,
    )


def test_thirty_second_synthesis_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-032.json")
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-032-2026-07-27.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-032-2026-07-27.json"
    )
    adjustments_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-adjustments-batch-032-2026-07-27.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-032-2026-07-27.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-032-2026-07-27.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-032-2026-07-27.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 32)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == "balanced-remaining-deterministic-sha256-v1"
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "aosp-framework-zh-rcn-v1": 16,
            "census-newsroom-zh-hans-v1": 16,
            "chromium-strings-zh-cn-v1": 16,
            "kubernetes-docs-zh-cn-v1": 16,
            "osha-disaster-cleanup-simplified-v1": 16,
            "ready-gov-home-fires-zh-hans-v1": 16,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert all(isinstance(case["quality_flags"], list) for case in gemini["cases"])
    assert gemini["execution"] == {
        "cli": "@google/gemini-cli",
        "cli_version": "0.52.0",
        "session_id": (
            "40f6f6d0-5cba-4883-ac5b-73b69978ccaf,"
            "e3429365-fd9a-4426-a6f0-4d7e2428e3af,"
            "3891fd21-c2c0-48d1-a25f-d41ca8852042,"
            "a28b5e81-c9f6-494e-bf0a-375e17366c74,"
            "8ad29bbf-3d74-4848-8667-13d7d3f83273,"
            "ad1d42fe-5800-4369-8caa-aec7f2eebebb"
        ),
        "tool_calls": 6,
        "total_errors": 0,
        "structural_normalization": "quality_flags_null_to_empty_array",
        "structural_normalization_cases": 62,
    }
    assert gemini["stats"]["policy_violations"] == 0
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 48,
        "review_queue": 48,
        "by_field": {"eligible": 2, "script": 4, "domain": 6, "risk": 43},
    }
    assert len(differences) == 48
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert set(overrides) == {
        "osha-disaster-cleanup-simplified-v1/sentence-029",
        "osha-disaster-cleanup-simplified-v1/sentence-066",
        "ready-gov-home-fires-zh-hans-v1/sentence-069",
        "ready-gov-home-fires-zh-hans-v1/sentence-074",
    }
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-27",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 92,
        "excluded": 4,
        "by_selection_basis": {"agreement": 48, "codex": 44, "codex_synthesis": 4},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-27",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 48,
        "confirmed_exact_matches": 48,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-27",
        maintainer_decisions=decision,
    )


def test_thirty_third_synthesis_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-033.json")
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-033-2026-07-27.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-033-2026-07-27.json"
    )
    adjustments_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-adjustments-batch-033-2026-07-27.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-033-2026-07-27.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-033-2026-07-27.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-033-2026-07-27.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 33)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == "balanced-remaining-deterministic-sha256-v1"
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "aosp-framework-zh-rcn-v1": 16,
            "census-newsroom-zh-hans-v1": 16,
            "chromium-strings-zh-cn-v1": 16,
            "kubernetes-docs-zh-cn-v1": 16,
            "osha-disaster-cleanup-simplified-v1": 16,
            "ready-gov-home-fires-zh-hans-v1": 16,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert all(isinstance(case["quality_flags"], list) for case in gemini["cases"])
    assert gemini["execution"] == {
        "cli": "@google/gemini-cli",
        "cli_version": "0.52.0",
        "session_id": (
            "90ce21bc-00a5-43de-b0c1-8860f92d8756,"
            "54758c1f-4ae8-4182-be7e-18aa57450797,"
            "faaffe2d-007d-4d49-9c5c-0e80b5359a4c,"
            "5a6dfbad-1c4b-41f3-8ee4-3ce5a1f8e648,"
            "fa573059-57b5-4e4d-8370-2135e9eedb33,"
            "7603fd73-f780-4835-8f73-8dd7eb2208d0"
        ),
        "tool_calls": 6,
        "total_errors": 0,
    }
    assert gemini["stats"]["policy_violations"] == 0
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 47,
        "review_queue": 49,
        "by_field": {"eligible": 5, "script": 1, "domain": 7, "risk": 48},
    }
    assert len(differences) == 49
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert set(overrides) == {"census-newsroom-zh-hans-v1/page-02-sentence-006"}
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=set(),
        generated_date="2026-07-27",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 91,
        "excluded": 5,
        "by_selection_basis": {"agreement": 47, "codex": 48, "codex_synthesis": 1},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-27",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 49,
        "confirmed_exact_matches": 47,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-27",
        maintainer_decisions=decision,
    )


def test_thirty_fourth_synthesis_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-034.json")
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-034-2026-07-27.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-034-2026-07-27.json"
    )
    adjustments_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-adjustments-batch-034-2026-07-27.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-034-2026-07-27.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-034-2026-07-27.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-034-2026-07-27.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    adjustments = load(adjustments_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 34)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == "balanced-remaining-deterministic-sha256-v1"
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "massive-1-0-zh-cn-v1": 32,
            "ready-gov-drought-zh-hans-v1": 32,
            "zhtw-project-llm-social-baseline-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert gemini["execution"] == {
        "cli": "@google/gemini-cli",
        "cli_version": "0.52.0",
        "session_id": (
            "44090521-6f26-4960-9fa0-43f4cb968102,"
            "1103f74f-ca15-4f67-b86d-c715b2fd200e,"
            "ede77efb-1128-4891-a7d0-54d297ac2825"
        ),
        "tool_calls": 3,
        "total_errors": 0,
    }
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 39,
        "review_queue": 57,
        "by_field": {"eligible": 2, "script": 0, "domain": 45, "risk": 31},
    }
    assert len(differences) == 57
    overrides = {case["id"]: case["classification"] for case in adjustments["cases"]}
    assert set(overrides) == {
        "ready-gov-drought-zh-hans-v1/sentence-008",
        "ready-gov-drought-zh-hans-v1/sentence-023",
        "ready-gov-drought-zh-hans-v1/sentence-026",
        "ready-gov-drought-zh-hans-v1/sentence-048",
        "ready-gov-drought-zh-hans-v1/sentence-063",
        "zhtw-project-llm-social-baseline-v1/llm-028",
    }
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids={"zhtw-project-llm-social-baseline-v1/llm-046"},
        generated_date="2026-07-27",
        overrides=overrides,
        override_basis="codex_synthesis",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 92,
        "excluded": 4,
        "by_selection_basis": {
            "agreement": 39,
            "codex": 50,
            "codex_synthesis": 6,
            "gemini": 1,
        },
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-27",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 57,
        "confirmed_exact_matches": 39,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-27",
        maintainer_decisions=decision,
    )


def test_thirty_fifth_synthesis_decision_is_reproducible() -> None:
    prefix = ROOT / "docs/reports"
    packet_path = ACCURACY_ROOT / ("review-packets/blind-v2-source-classification-batch-035.json")
    codex_path = prefix / (
        "blind-v2-source-classification-codex-first-pass-batch-035-2026-07-27.json"
    )
    gemini_path = prefix / (
        "blind-v2-source-classification-gemini-independent-batch-035-2026-07-27.json"
    )
    synthesis_path = prefix / (
        "blind-v2-source-classification-codex-synthesis-batch-035-2026-07-27.json"
    )
    decision_path = prefix / (
        "blind-v2-source-classification-maintainer-decision-batch-035-2026-07-27.json"
    )
    diff_path = prefix / "blind-v2-source-classification-diff-batch-035-2026-07-27.md"
    packet = load(packet_path)
    codex = load(codex_path)
    gemini = load(gemini_path)
    synthesis = load(synthesis_path)
    decision = load(decision_path)
    packet_ids = [case["id"] for case in packet["cases"]]
    prior_ids = {
        case["id"]
        for batch_number in range(1, 35)
        for case in load(
            ACCURACY_ROOT
            / f"review-packets/blind-v2-source-classification-batch-{batch_number:03d}.json"
        )["cases"]
    }
    packet_hash = hashlib.sha256(packet_path.read_bytes()).hexdigest()

    assert packet["selection_policy"] == "balanced-remaining-deterministic-sha256-v1"
    assert packet["stats"] == {
        "total": 96,
        "by_source": {
            "census-newsroom-zh-hans-v1": 32,
            "massive-1-0-zh-cn-v1": 32,
            "zhtw-project-llm-social-baseline-v1": 32,
        },
    }
    assert set(packet_ids).isdisjoint(prior_ids)
    assert codex["packet_sha256"] == gemini["packet_sha256"] == packet_hash
    assert [case["id"] for case in codex["cases"]] == packet_ids
    assert [case["id"] for case in gemini["cases"]] == packet_ids
    assert gemini["execution"] == {
        "cli": "@google/gemini-cli",
        "cli_version": "0.52.0",
        "session_id": (
            "d7cc5f57-52a8-4596-ac63-cf7803e4b17b,"
            "92e0e4b1-d217-4ac7-ad81-c6b573543933,"
            "f3621105-3b2c-47a6-93ad-8128af43217f"
        ),
        "tool_calls": 0,
        "total_errors": 0,
    }
    stats, differences = build_comparison(packet, codex, gemini)
    assert stats == {
        "total": 96,
        "exact": 61,
        "review_queue": 35,
        "by_field": {"eligible": 6, "script": 1, "domain": 15, "risk": 29},
    }
    assert len(differences) == 35
    gemini_case_ids = {
        "census-newsroom-zh-hans-v1/page-02-sentence-002",
        "census-newsroom-zh-hans-v1/page-04-sentence-010",
        "census-newsroom-zh-hans-v1/page-05-sentence-010",
        "zhtw-project-llm-social-baseline-v1/llm-003",
        "zhtw-project-llm-social-baseline-v1/llm-009",
    }
    assert synthesis == build_synthesis(
        codex,
        gemini,
        gemini_case_ids=gemini_case_ids,
        generated_date="2026-07-27",
    )
    assert synthesis["stats"] == {
        "total": 96,
        "eligible": 90,
        "excluded": 6,
        "by_selection_basis": {"agreement": 61, "codex": 30, "gemini": 5},
    }
    assert decision == build_decision(
        packet_path,
        codex_path,
        gemini_path,
        maintainer="tim",
        decision_date="2026-07-27",
        selected_advisory="synthesis",
        synthesis_path=synthesis_path,
    )
    assert decision["stats"] == {
        "packet_cases": 96,
        "confirmed_cases": 96,
        "resolved_disagreements": 35,
        "confirmed_exact_matches": 61,
        "remaining_cases": 0,
    }
    assert diff_path.read_text(encoding="utf-8") == render_markdown(
        packet,
        codex,
        gemini,
        generated_date="2026-07-27",
        maintainer_decisions=decision,
    )
