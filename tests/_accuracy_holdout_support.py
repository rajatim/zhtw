# zhtw:disable
# ruff: noqa: F401
"""Tests for the accuracy benchmark scaffolding."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import pytest

from zhtw.converter import convert

ROOT = Path(__file__).resolve().parents[1]
INPUTS = ROOT / "benchmarks" / "accuracy" / "blind-v1.inputs.json"
INPUTS_SCHEMA = ROOT / "benchmarks" / "accuracy" / "blind-v1.inputs.schema.json"
EXPECTED = ROOT / "benchmarks" / "accuracy" / "blind-v1.expected.json"
EXPECTED_SCHEMA = ROOT / "benchmarks" / "accuracy" / "blind-v1.expected.schema.json"
BLIND_V1_METADATA = ROOT / "benchmarks" / "accuracy" / "blind-v1.metadata.json"
COMPETITORS_LOCK = ROOT / "benchmarks" / "accuracy" / "competitors.lock.json"
RUNNER = ROOT / "scripts" / "run_accuracy_benchmark.py"
PACKET_SCRIPT = ROOT / "scripts" / "create_holdout_annotation_packet.py"
CODEX_FIRST_PASS = (
    ROOT / "docs" / "reports" / "holdout-codex-first-pass-blind-v1-0001-0100-2026-07-08.json"
)
GEMINI_ADVISORY = (
    ROOT / "docs" / "reports" / "holdout-gemini-vertex-advisory-blind-v1-0001-0100-2026-07-08.json"
)
CODEX_GEMINI_DIFF_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-codex-gemini-diff-review-blind-v1-0001-0100-2026-07-08.json"
)
MAINTAINER_CONFIRMATION = (
    ROOT / "docs" / "reports" / "holdout-maintainer-confirmation-blind-v1-0001-0100-2026-07-08.json"
)
FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-blind-v1-0001-0100-2026-07-08.json"
)
PRIVATE_BENCHMARK_SANITY = (
    ROOT / "docs" / "reports" / "holdout-private-benchmark-sanity-blind-v1-2026-07-09.json"
)
PRIVATE_BENCHMARK_SANITY_AFTER_REMAINING_40_FINAL_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-private-benchmark-sanity-blind-v1-after-remaining-40-final-review-2026-07-09.json"
)
PRIVATE_BENCHMARK_SANITY_AFTER_BATCH5 = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-private-benchmark-sanity-blind-v1-after-batch5-2026-07-09.json"
)
PRIVATE_BENCHMARK_SANITY_AFTER_338_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-private-benchmark-sanity-blind-v1-after-338-miss-review-2026-07-09.json"
)
PRIVATE_BENCHMARK_SANITY_AFTER_BATCH6 = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-private-benchmark-sanity-blind-v1-after-batch6-2026-07-10.json"
)
PRIVATE_BENCHMARK_SANITY_AFTER_BATCH6_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-private-benchmark-sanity-blind-v1-after-batch6-miss-review-2026-07-10.json"
)
PRIVATE_BENCHMARK_SANITY_AFTER_BATCH7 = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-private-benchmark-sanity-blind-v1-after-batch7-2026-07-10.json"
)
PRIVATE_BENCHMARK_SANITY_AFTER_BATCH7_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-private-benchmark-sanity-blind-v1-after-batch7-miss-review-2026-07-10.json"
)
PRIVATE_BENCHMARK_SANITY_AFTER_BATCH8 = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-private-benchmark-sanity-blind-v1-after-batch8-2026-07-10.json"
)
PRIVATE_BENCHMARK_SANITY_AFTER_BATCH8_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-private-benchmark-sanity-blind-v1-after-batch8-miss-review-2026-07-11.json"
)
PRIVATE_BENCHMARK_SANITY_AFTER_BATCH9 = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-private-benchmark-sanity-blind-v1-after-batch9-2026-07-12.json"
)
PRIVATE_BENCHMARK_SANITY_AFTER_BATCH9_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-private-benchmark-sanity-blind-v1-after-batch9-miss-review-2026-07-12.json"
)
PRIVATE_BENCHMARK_SANITY_AFTER_BATCH10 = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-private-benchmark-sanity-blind-v1-after-batch10-2026-07-12.json"
)
PRIVATE_BENCHMARK_SANITY_AFTER_BATCH10_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-private-benchmark-sanity-blind-v1-after-batch10-miss-review-2026-07-13.json"
)
PRIVATE_BENCHMARK_SANITY_AFTER_BATCH11 = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-private-benchmark-sanity-blind-v1-after-batch11-2026-07-14.json"
)
PRIVATE_BENCHMARK_SANITY_AFTER_BATCH11_SEMANTIC_REAUDIT = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-private-benchmark-sanity-blind-v1-after-batch11-semantic-reaudit-2026-07-14.json"
)
PRIVATE_BENCHMARK_SANITY_AFTER_BATCH12 = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-private-benchmark-sanity-blind-v1-after-batch12-2026-07-14.json"
)
PRIVATE_BENCHMARK_SANITY_AFTER_BATCH12_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-private-benchmark-sanity-blind-v1-after-batch12-miss-review-2026-07-14.json"
)
PRIVATE_BENCHMARK_SANITY_AFTER_BATCH13 = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-private-benchmark-sanity-blind-v1-after-batch13-2026-07-14.json"
)
PRIVATE_BENCHMARK_SANITY_AFTER_BATCH13_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-private-benchmark-sanity-blind-v1-after-batch13-miss-review-2026-07-14.json"
)
MISS_CLASSIFICATION = (
    ROOT / "docs" / "reports" / "holdout-miss-classification-blind-v1-2026-07-08.json"
)
EXPECTED_RECHECK = ROOT / "docs" / "reports" / "holdout-expected-recheck-blind-v1-2026-07-09.json"
REMAINING_MISS_CLASSIFICATION = (
    ROOT / "docs" / "reports" / "holdout-remaining-miss-classification-blind-v1-2026-07-09.json"
)
MISS_CLASSIFICATION_200_CASE = (
    ROOT / "docs" / "reports" / "holdout-miss-classification-blind-v1-200-cases-2026-07-09.json"
)
GEMINI_MISS_CLASSIFICATION_POLICY_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-policy-review-miss-classification-blind-v1-200-cases-2026-07-09.json"
)
MISS_CLASSIFICATION_261_CASE = (
    ROOT / "docs" / "reports" / "holdout-miss-classification-blind-v1-261-cases-2026-07-09.json"
)
MISS_CLASSIFICATION_338_CASE = (
    ROOT / "docs" / "reports" / "holdout-miss-classification-blind-v1-338-cases-2026-07-09.json"
)
MISS_CLASSIFICATION_426_CASE = (
    ROOT / "docs" / "reports" / "holdout-miss-classification-blind-v1-426-cases-2026-07-10.json"
)
MISS_CLASSIFICATION_515_CASE = (
    ROOT / "docs" / "reports" / "holdout-miss-classification-blind-v1-515-cases-2026-07-10.json"
)
MISS_CLASSIFICATION_598_CASE = (
    ROOT / "docs" / "reports" / "holdout-miss-classification-blind-v1-598-cases-2026-07-10.json"
)
MISS_CLASSIFICATION_683_CASE = (
    ROOT / "docs" / "reports" / "holdout-miss-classification-blind-v1-683-cases-2026-07-12.json"
)
MISS_CLASSIFICATION_767_CASE = (
    ROOT / "docs" / "reports" / "holdout-miss-classification-blind-v1-767-cases-2026-07-12.json"
)
MISS_CLASSIFICATION_851_CASE = (
    ROOT / "docs" / "reports" / "holdout-miss-classification-blind-v1-851-cases-2026-07-14.json"
)
GEMINI_MISS_CLASSIFICATION_261_POLICY_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-policy-review-miss-classification-blind-v1-261-cases-2026-07-09.json"
)
GEMINI_MISS_CLASSIFICATION_338_POLICY_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-policy-review-miss-classification-blind-v1-338-cases-2026-07-09.json"
)
GEMINI_MISS_CLASSIFICATION_426_POLICY_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-policy-review-miss-classification-blind-v1-426-cases-2026-07-10.json"
)
GEMINI_MISS_CLASSIFICATION_515_POLICY_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-policy-review-miss-classification-blind-v1-515-cases-2026-07-10.json"
)
GEMINI_MISS_CLASSIFICATION_598_POLICY_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-policy-review-miss-classification-blind-v1-598-cases-2026-07-10.json"
)
GEMINI_MISS_CLASSIFICATION_683_POLICY_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-policy-review-miss-classification-blind-v1-683-cases-2026-07-12.json"
)
GEMINI_MISS_CLASSIFICATION_767_POLICY_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-policy-review-miss-classification-blind-v1-767-cases-2026-07-12.json"
)
GEMINI_MISS_CLASSIFICATION_851_POLICY_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-policy-review-miss-classification-blind-v1-851-cases-2026-07-14.json"
)
MAINTAINER_BATCH6_MISS_CLASSIFICATION_CONFIRMATION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-confirmation-blind-v1-batch6-miss-classification-2026-07-10.json"
)
MAINTAINER_BATCH7_MISS_CLASSIFICATION_CONFIRMATION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-confirmation-blind-v1-batch7-miss-classification-2026-07-10.json"
)
MAINTAINER_BATCH8_MISS_CLASSIFICATION_CONFIRMATION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-confirmation-blind-v1-batch8-miss-classification-2026-07-10.json"
)
MAINTAINER_BATCH9_MISS_CLASSIFICATION_CONFIRMATION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-confirmation-blind-v1-batch9-miss-classification-2026-07-12.json"
)
MAINTAINER_BATCH10_MISS_CLASSIFICATION_CONFIRMATION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-confirmation-blind-v1-batch10-miss-classification-2026-07-12.json"
)
MAINTAINER_BATCH11_MISS_CLASSIFICATION_CONFIRMATION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-confirmation-blind-v1-batch11-miss-classification-2026-07-14.json"
)
CODEX_BATCH11_SEMANTIC_REAUDIT = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-codex-semantic-reaudit-blind-v1-batch11-25-cases-2026-07-14.json"
)
GEMINI_BATCH11_SEMANTIC_REAUDIT = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-independent-semantic-reaudit-blind-v1-batch11-25-cases-2026-07-14.json"
)
MAINTAINER_BATCH11_SEMANTIC_REAUDIT_CONFIRMATION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-confirmation-blind-v1-batch11-semantic-reaudit-6-cases-2026-07-14.json"
)
MAINTAINER_BATCH11_SEMANTIC_REAUDIT_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-blind-v1-batch11-semantic-reaudit-2026-07-14.json"
)
REQUIRES_EXPECTED_RECHECK_261_CASE = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-requires-expected-recheck-blind-v1-261-cases-2026-07-09.json"
)
GEMINI_REQUIRES_EXPECTED_RECHECK_261_POLICY_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-policy-review-requires-expected-recheck-blind-v1-261-cases-2026-07-09.json"
)
REQUIRES_EXPECTED_RECHECK_261_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / (
        "holdout-maintainer-final-decision-requires-expected-recheck-"
        "blind-v1-261-cases-2026-07-09.json"
    )
)
POST_BATCH3_RECHECK = (
    ROOT / "docs" / "reports" / "holdout-post-batch3-miss-recheck-blind-v1-2026-07-09.json"
)
GEMINI_POST_BATCH3_RECHECK_POLICY_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-policy-review-post-batch3-recheck-blind-v1-2026-07-09.json"
)
POST_BATCH3_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-post-batch3-recheck-blind-v1-2026-07-09.json"
)
REMAINING_SIGNAL_SUMMARY = (
    ROOT / "docs" / "reports" / "holdout-remaining-signal-summary-blind-v1-2026-07-09.json"
)
REMAINING_SIGNAL_SUMMARY_AFTER_BATCH6_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-remaining-signal-summary-blind-v1-after-batch6-miss-review-2026-07-10.json"
)
REMAINING_SIGNAL_SUMMARY_AFTER_BATCH10_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-remaining-signal-summary-blind-v1-after-batch10-miss-review-2026-07-13.json"
)
GEMINI_REMAINING_SIGNAL_POLICY_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-policy-review-remaining-signal-blind-v1-2026-07-09.json"
)
GEMINI_REMAINING_SIGNAL_POLICY_REVIEW_AFTER_BATCH6_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / (
        "holdout-gemini-policy-review-remaining-signal-blind-v1-"
        "after-batch6-miss-review-2026-07-10.json"
    )
)
GEMINI_REMAINING_SIGNAL_POLICY_REVIEW_AFTER_BATCH10_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / (
        "holdout-gemini-policy-review-remaining-signal-blind-v1-"
        "after-batch10-miss-review-2026-07-13.json"
    )
)
REMAINING_40_MISS_CLASSIFICATION = (
    ROOT / "docs" / "reports" / "holdout-remaining-40-miss-classification-blind-v1-2026-07-09.json"
)
GEMINI_REMAINING_40_MISS_POLICY_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-policy-review-remaining-40-miss-classification-blind-v1-2026-07-09.json"
)
GEMINI_REMAINING_40_PUBLIC_PROMOTION_POLICY_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-policy-review-remaining-40-public-promotion-2026-07-09.json"
)
GEMINI_338_MISS_PUBLIC_PROMOTION_POLICY_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-policy-review-338-miss-public-promotion-2026-07-09.json"
)
GEMINI_BATCH6_MISS_PUBLIC_PROMOTION_POLICY_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-policy-review-batch6-miss-public-promotion-2026-07-10.json"
)
GEMINI_BATCH7_MISS_PUBLIC_PROMOTION_POLICY_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-policy-review-batch7-miss-public-promotion-2026-07-10.json"
)
GEMINI_BATCH8_MISS_PUBLIC_PROMOTION_POLICY_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-policy-review-batch8-miss-public-promotion-2026-07-11.json"
)
GEMINI_BATCH9_MISS_PUBLIC_PROMOTION_POLICY_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-policy-review-batch9-miss-public-promotion-2026-07-12.json"
)
REMAINING_40_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-remaining-40-miss-classification-blind-v1-2026-07-09.json"
)
MAINTAINER_338_MISS_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-338-miss-classification-blind-v1-2026-07-09.json"
)
MAINTAINER_BATCH6_MISS_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-batch6-miss-classification-blind-v1-2026-07-10.json"
)
MAINTAINER_BATCH7_MISS_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-batch7-miss-classification-blind-v1-2026-07-10.json"
)
MAINTAINER_BATCH8_MISS_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-batch8-miss-classification-blind-v1-2026-07-11.json"
)
MAINTAINER_BATCH9_MISS_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-batch9-miss-classification-blind-v1-2026-07-12.json"
)
MAINTAINER_BATCH10_MISS_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-batch10-miss-classification-blind-v1-2026-07-13.json"
)
INPUT_POOL_EXPANSION = (
    ROOT / "docs" / "reports" / "holdout-input-pool-expansion-blind-v1-2026-07-09.json"
)
INPUT_POOL_EXPANSION_BATCH4 = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-input-pool-expansion-blind-v1-batch4-100-cases-2026-07-09.json"
)
INPUT_POOL_EXPANSION_BATCH5 = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-input-pool-expansion-blind-v1-batch5-100-cases-2026-07-09.json"
)
INPUT_POOL_EXPANSION_BATCH6 = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-input-pool-expansion-blind-v1-batch6-100-cases-2026-07-09.json"
)
INPUT_POOL_EXPANSION_BATCH7 = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-input-pool-expansion-blind-v1-batch7-100-cases-2026-07-10.json"
)
INPUT_POOL_EXPANSION_BATCH8 = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-input-pool-expansion-blind-v1-batch8-100-cases-2026-07-10.json"
)
INPUT_POOL_EXPANSION_BATCH9 = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-input-pool-expansion-blind-v1-batch9-100-cases-2026-07-12.json"
)
INPUT_POOL_EXPANSION_BATCH10 = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-input-pool-expansion-blind-v1-batch10-100-cases-2026-07-12.json"
)
INPUT_POOL_EXPANSION_BATCH11 = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-input-pool-expansion-blind-v1-batch11-100-cases-2026-07-13.json"
)
INPUT_POOL_EXPANSION_BATCH12 = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-input-pool-expansion-blind-v1-batch12-100-cases-2026-07-14.json"
)
INPUT_POOL_EXPANSION_BATCH13 = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-input-pool-expansion-blind-v1-batch13-100-cases-2026-07-14.json"
)
CODEX_EXPANSION_FIRST_PASS = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-codex-first-pass-blind-v1-expansion-127-cases-2026-07-09.json"
)
CODEX_BATCH4_FIRST_PASS = (
    ROOT / "docs" / "reports" / "holdout-codex-first-pass-blind-v1-batch4-100-cases-2026-07-09.json"
)
CODEX_BATCH5_FIRST_PASS = (
    ROOT / "docs" / "reports" / "holdout-codex-first-pass-blind-v1-batch5-100-cases-2026-07-09.json"
)
CODEX_BATCH6_FIRST_PASS = (
    ROOT / "docs" / "reports" / "holdout-codex-first-pass-blind-v1-batch6-100-cases-2026-07-10.json"
)
CODEX_BATCH7_FIRST_PASS = (
    ROOT / "docs" / "reports" / "holdout-codex-first-pass-blind-v1-batch7-100-cases-2026-07-10.json"
)
CODEX_BATCH8_FIRST_PASS = (
    ROOT / "docs" / "reports" / "holdout-codex-first-pass-blind-v1-batch8-100-cases-2026-07-10.json"
)
CODEX_BATCH9_FIRST_PASS = (
    ROOT / "docs" / "reports" / "holdout-codex-first-pass-blind-v1-batch9-100-cases-2026-07-12.json"
)
CODEX_BATCH10_FIRST_PASS = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-codex-first-pass-blind-v1-batch10-100-cases-2026-07-12.json"
)
CODEX_BATCH11_FIRST_PASS = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-codex-first-pass-blind-v1-batch11-100-cases-2026-07-13.json"
)
CODEX_BATCH12_FIRST_PASS = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-codex-first-pass-blind-v1-batch12-100-cases-2026-07-14.json"
)
CODEX_BATCH13_FIRST_PASS = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-codex-first-pass-blind-v1-batch13-100-cases-2026-07-14.json"
)
GEMINI_EXPANSION_ADVISORY = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-vertex-advisory-blind-v1-expansion-127-cases-2026-07-09.json"
)
GEMINI_BATCH4_ADVISORY = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-vertex-advisory-blind-v1-batch4-100-cases-2026-07-09.json"
)
GEMINI_BATCH5_ADVISORY = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-cli-advisory-blind-v1-batch5-100-cases-2026-07-09.json"
)
GEMINI_BATCH6_ADVISORY = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-cli-advisory-blind-v1-batch6-100-cases-2026-07-10.json"
)
GEMINI_BATCH7_ADVISORY = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-cli-advisory-blind-v1-batch7-100-cases-2026-07-10.json"
)
GEMINI_BATCH8_ADVISORY = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-cli-advisory-blind-v1-batch8-100-cases-2026-07-10.json"
)
GEMINI_BATCH9_ADVISORY = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-cli-advisory-blind-v1-batch9-100-cases-2026-07-12.json"
)
GEMINI_BATCH10_ADVISORY = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-cli-advisory-blind-v1-batch10-100-cases-2026-07-12.json"
)
GEMINI_BATCH11_ADVISORY = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-cli-advisory-blind-v1-batch11-100-cases-2026-07-14.json"
)
GEMINI_BATCH12_ADVISORY = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-cli-advisory-blind-v1-batch12-100-cases-2026-07-14.json"
)
GEMINI_BATCH13_ADVISORY = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-cli-advisory-blind-v1-batch13-100-cases-2026-07-14.json"
)
CODEX_GEMINI_EXPANSION_DIFF_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-codex-gemini-diff-review-blind-v1-expansion-127-cases-2026-07-09.json"
)
CODEX_GEMINI_BATCH4_DIFF_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-codex-gemini-diff-review-blind-v1-batch4-100-cases-2026-07-09.json"
)
CODEX_GEMINI_BATCH5_DIFF_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-codex-gemini-diff-review-blind-v1-batch5-100-cases-2026-07-09.json"
)
CODEX_GEMINI_BATCH6_DIFF_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-codex-gemini-diff-review-blind-v1-batch6-100-cases-2026-07-10.json"
)
CODEX_GEMINI_BATCH7_DIFF_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-codex-gemini-diff-review-blind-v1-batch7-100-cases-2026-07-10.json"
)
CODEX_GEMINI_BATCH8_DIFF_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-codex-gemini-diff-review-blind-v1-batch8-100-cases-2026-07-10.json"
)
CODEX_GEMINI_BATCH9_DIFF_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-codex-gemini-diff-review-blind-v1-batch9-100-cases-2026-07-12.json"
)
CODEX_GEMINI_BATCH10_DIFF_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-codex-gemini-diff-review-blind-v1-batch10-100-cases-2026-07-12.json"
)
CODEX_GEMINI_BATCH11_DIFF_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-codex-gemini-diff-review-blind-v1-batch11-100-cases-2026-07-14.json"
)
CODEX_GEMINI_BATCH12_DIFF_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-codex-gemini-diff-review-blind-v1-batch12-100-cases-2026-07-14.json"
)
CODEX_GEMINI_BATCH13_DIFF_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-codex-gemini-diff-review-blind-v1-batch13-100-cases-2026-07-14.json"
)
MAINTAINER_EXPANSION_DIFFERENCES_CONFIRMATION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-confirmation-blind-v1-expansion-differences-2026-07-09.json"
)
MAINTAINER_BATCH4_CONFIRMATION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-confirmation-blind-v1-batch4-100-cases-2026-07-09.json"
)
MAINTAINER_BATCH5_CONFIRMATION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-confirmation-blind-v1-batch5-100-cases-2026-07-09.json"
)
MAINTAINER_BATCH6_CONFIRMATION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-confirmation-blind-v1-batch6-100-cases-2026-07-10.json"
)
MAINTAINER_BATCH7_CONFIRMATION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-confirmation-blind-v1-batch7-100-cases-2026-07-10.json"
)
MAINTAINER_BATCH8_CONFIRMATION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-confirmation-blind-v1-batch8-100-cases-2026-07-10.json"
)
MAINTAINER_BATCH9_CONFIRMATION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-confirmation-blind-v1-batch9-100-cases-2026-07-12.json"
)
MAINTAINER_BATCH10_CONFIRMATION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-confirmation-blind-v1-batch10-100-cases-2026-07-12.json"
)
MAINTAINER_BATCH11_CONFIRMATION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-confirmation-blind-v1-batch11-100-cases-2026-07-14.json"
)
MAINTAINER_BATCH12_CONFIRMATION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-confirmation-blind-v1-batch12-100-cases-2026-07-14.json"
)
MAINTAINER_BATCH13_CONFIRMATION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-confirmation-blind-v1-batch13-100-cases-2026-07-14.json"
)
MAINTAINER_BATCH13_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-blind-v1-batch13-100-cases-2026-07-14.json"
)
BATCH13_MISS_CLASSIFICATION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-miss-classification-blind-v1-batch13-34-cases-2026-07-14.json"
)
GEMINI_BATCH13_MISS_SEMANTIC_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-independent-semantic-review-blind-v1-batch13-34-misses-2026-07-14.json"
)
CODEX_GEMINI_BATCH13_MISS_DIFF = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-codex-gemini-miss-review-diff-blind-v1-batch13-34-cases-2026-07-14.json"
)
MAINTAINER_BATCH13_MISS_CONFIRMATION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-confirmation-blind-v1-batch13-miss-review-19-cases-2026-07-14.json"
)
MAINTAINER_BATCH13_MISS_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-blind-v1-batch13-miss-review-2026-07-14.json"
)
MAINTAINER_BATCH12_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-blind-v1-batch12-100-cases-2026-07-14.json"
)
BATCH12_MISS_CLASSIFICATION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-miss-classification-blind-v1-batch12-15-cases-2026-07-14.json"
)
GEMINI_BATCH12_MISS_SEMANTIC_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-gemini-independent-semantic-review-blind-v1-batch12-15-misses-2026-07-14.json"
)
CODEX_GEMINI_BATCH12_MISS_DIFF = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-codex-gemini-miss-review-diff-blind-v1-batch12-15-cases-2026-07-14.json"
)
MAINTAINER_BATCH12_MISS_CONFIRMATION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-confirmation-blind-v1-batch12-miss-review-8-cases-2026-07-14.json"
)
MAINTAINER_BATCH12_MISS_PARTIAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-partial-decision-blind-v1-batch12-miss-review-2026-07-14.json"
)
MAINTAINER_BATCH12_MISS_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-blind-v1-batch12-miss-review-2026-07-14.json"
)
MAINTAINER_BATCH4_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-blind-v1-batch4-100-cases-2026-07-09.json"
)
MAINTAINER_BATCH5_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-blind-v1-batch5-100-cases-2026-07-09.json"
)
MAINTAINER_BATCH6_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-blind-v1-batch6-100-cases-2026-07-10.json"
)
MAINTAINER_BATCH7_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-blind-v1-batch7-100-cases-2026-07-10.json"
)
MAINTAINER_BATCH8_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-blind-v1-batch8-100-cases-2026-07-10.json"
)
MAINTAINER_BATCH9_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-blind-v1-batch9-100-cases-2026-07-12.json"
)
MAINTAINER_BATCH10_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-blind-v1-batch10-100-cases-2026-07-12.json"
)
MAINTAINER_BATCH11_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-blind-v1-batch11-100-cases-2026-07-14.json"
)
MAINTAINER_EXPANSION_DIFFERENCES_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-blind-v1-expansion-differences-2026-07-09.json"
)
MAINTAINER_EXPANSION_POLICY_REVIEW_CONFIRMATION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-confirmation-blind-v1-expansion-policy-review-2026-07-09.json"
)
MAINTAINER_EXPANSION_POLICY_REVIEW_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-blind-v1-expansion-policy-review-2026-07-09.json"
)
MAINTAINER_EXPANSION_FINAL_DECISION = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-maintainer-final-decision-blind-v1-expansion-127-cases-2026-07-09.json"
)
HOLDOUT_CANDIDATES = ROOT / "benchmarks" / "accuracy" / "holdout-regression-candidates-v1.json"
REGRESSION = ROOT / "benchmarks" / "accuracy" / "regression-v1.json"
HOLDOUT_CANDIDATES_SCHEMA = (
    ROOT / "benchmarks" / "accuracy" / "holdout-regression-candidates-v1.schema.json"
)
HOLDOUT_PROMOTION_GATE = (
    ROOT / "docs" / "reports" / "holdout-regression-promotion-gate-blind-v1-2026-07-09.json"
)
HOLDOUT_PROMOTION_GATE_BATCH2 = (
    ROOT / "docs" / "reports" / "holdout-regression-promotion-gate-blind-v1-batch2-2026-07-09.json"
)
HOLDOUT_PROMOTION_GATE_BATCH3 = (
    ROOT / "docs" / "reports" / "holdout-regression-promotion-gate-blind-v1-batch3-2026-07-09.json"
)
HOLDOUT_PROMOTION_GATE_BATCH4_RECHECK = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-regression-promotion-gate-blind-v1-batch4-recheck-2026-07-09.json"
)
HOLDOUT_PROMOTION_GATE_REMAINING_40_FINAL_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-regression-promotion-gate-blind-v1-remaining-40-final-review-2026-07-09.json"
)
HOLDOUT_PROMOTION_GATE_338_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-regression-promotion-gate-blind-v1-338-miss-review-2026-07-09.json"
)
HOLDOUT_PROMOTION_GATE_BATCH6_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-regression-promotion-gate-blind-v1-batch6-miss-review-2026-07-10.json"
)
HOLDOUT_PROMOTION_GATE_BATCH7_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-regression-promotion-gate-blind-v1-batch7-miss-review-2026-07-10.json"
)
HOLDOUT_PROMOTION_GATE_BATCH8_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-regression-promotion-gate-blind-v1-batch8-miss-review-2026-07-11.json"
)
HOLDOUT_PROMOTION_GATE_BATCH9_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-regression-promotion-gate-blind-v1-batch9-miss-review-2026-07-12.json"
)
HOLDOUT_PROMOTION_GATE_BATCH10_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-regression-promotion-gate-blind-v1-batch10-miss-review-2026-07-13.json"
)
HOLDOUT_PROMOTION_GATE_BATCH11_SEMANTIC_REAUDIT = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-regression-promotion-gate-blind-v1-batch11-semantic-reaudit-2026-07-14.json"
)
HOLDOUT_PROMOTION_GATE_BATCH12_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-regression-promotion-gate-blind-v1-batch12-miss-review-2026-07-14.json"
)
HOLDOUT_PROMOTION_GATE_BATCH13_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-regression-promotion-gate-blind-v1-batch13-miss-review-2026-07-14.json"
)
SEALED_POOL_UPDATE = (
    ROOT / "docs" / "reports" / "holdout-sealed-pool-update-blind-v1-2026-07-09.json"
)
SEALED_POOL_UPDATE_BATCH2 = (
    ROOT / "docs" / "reports" / "holdout-sealed-pool-update-blind-v1-batch2-2026-07-09.json"
)
SEALED_POOL_UPDATE_BATCH3 = (
    ROOT / "docs" / "reports" / "holdout-sealed-pool-update-blind-v1-batch3-2026-07-09.json"
)
SEALED_POOL_UPDATE_BATCH4_RECHECK = (
    ROOT / "docs" / "reports" / "holdout-sealed-pool-update-blind-v1-batch4-recheck-2026-07-09.json"
)
SEALED_POOL_UPDATE_REMAINING_40_FINAL_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-sealed-pool-update-blind-v1-remaining-40-final-review-2026-07-09.json"
)
SEALED_POOL_UPDATE_338_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-sealed-pool-update-blind-v1-338-miss-review-2026-07-09.json"
)
SEALED_POOL_UPDATE_BATCH6_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-sealed-pool-update-blind-v1-batch6-miss-review-2026-07-10.json"
)
SEALED_POOL_UPDATE_BATCH7_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-sealed-pool-update-blind-v1-batch7-miss-review-2026-07-10.json"
)
SEALED_POOL_UPDATE_BATCH8_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-sealed-pool-update-blind-v1-batch8-miss-review-2026-07-11.json"
)
SEALED_POOL_UPDATE_BATCH9_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-sealed-pool-update-blind-v1-batch9-miss-review-2026-07-12.json"
)
SEALED_POOL_UPDATE_BATCH10_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-sealed-pool-update-blind-v1-batch10-miss-review-2026-07-13.json"
)
SEALED_POOL_UPDATE_BATCH11_SEMANTIC_REAUDIT = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-sealed-pool-update-blind-v1-batch11-semantic-reaudit-2026-07-14.json"
)
SEALED_POOL_UPDATE_BATCH12_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-sealed-pool-update-blind-v1-batch12-miss-review-2026-07-14.json"
)
SEALED_POOL_UPDATE_BATCH13_MISS_REVIEW = (
    ROOT
    / "docs"
    / "reports"
    / "holdout-sealed-pool-update-blind-v1-batch13-miss-review-2026-07-14.json"
)


def load_json(path: Path) -> dict[str, Any]:
    if path == EXPECTED and not path.exists():
        pytest.skip("sealed holdout expected file is not available")
    return json.loads(path.read_text(encoding="utf-8"))


def private_expected_sha256() -> str:
    if not EXPECTED.exists():
        pytest.skip("sealed holdout expected file is not available")
    return hashlib.sha256(EXPECTED.read_bytes()).hexdigest()


def load_all_removed_case_ids() -> set[str]:
    return (
        set(load_json(SEALED_POOL_UPDATE)["removed_case_ids"])
        | set(load_json(SEALED_POOL_UPDATE_BATCH2)["removed_case_ids"])
        | set(load_json(SEALED_POOL_UPDATE_BATCH3)["removed_case_ids"])
        | set(load_json(SEALED_POOL_UPDATE_BATCH4_RECHECK)["removed_case_ids"])
        | set(load_json(SEALED_POOL_UPDATE_REMAINING_40_FINAL_REVIEW)["removed_case_ids"])
        | set(load_json(SEALED_POOL_UPDATE_338_MISS_REVIEW)["removed_case_ids"])
        | set(load_json(SEALED_POOL_UPDATE_BATCH6_MISS_REVIEW)["removed_case_ids"])
        | set(load_json(SEALED_POOL_UPDATE_BATCH7_MISS_REVIEW)["removed_case_ids"])
        | set(load_json(SEALED_POOL_UPDATE_BATCH8_MISS_REVIEW)["removed_case_ids"])
        | set(load_json(SEALED_POOL_UPDATE_BATCH9_MISS_REVIEW)["removed_case_ids"])
        | set(load_json(SEALED_POOL_UPDATE_BATCH10_MISS_REVIEW)["removed_case_ids"])
        | set(load_json(SEALED_POOL_UPDATE_BATCH11_SEMANTIC_REAUDIT)["removed_case_ids"])
        | set(load_json(SEALED_POOL_UPDATE_BATCH12_MISS_REVIEW)["removed_case_ids"])
        | set(load_json(SEALED_POOL_UPDATE_BATCH13_MISS_REVIEW)["removed_case_ids"])
    )


def original_seed_ids_from_report(report_ids: list[str], input_ids: list[str]) -> list[str]:
    expansion_ids = set(input_ids) - set(report_ids)
    return [case_id for case_id in input_ids if case_id not in expansion_ids]
