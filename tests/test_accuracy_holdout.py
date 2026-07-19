# zhtw:disable
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


def test_batch13_miss_final_decision_promotion_and_sanity_are_auditable() -> None:
    final = load_json(MAINTAINER_BATCH13_MISS_FINAL_DECISION)
    pool = load_json(SEALED_POOL_UPDATE_BATCH13_MISS_REVIEW)
    gate = load_json(HOLDOUT_PROMOTION_GATE_BATCH13_MISS_REVIEW)
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH13_MISS_REVIEW)
    inputs = load_json(INPUTS)
    expected = load_json(EXPECTED)
    candidates = load_json(ROOT / "benchmarks/accuracy/holdout-regression-candidates-v1.json")
    regression = load_json(ROOT / "benchmarks/accuracy/regression-v1.json")

    assert final["decision"] == "review_ok"
    assert final["summary"]["reviewed_batch13_misses"] == 34
    assert len(final["confirmed_acceptable_variant_case_ids"]) == 5
    assert len(final["removed_to_public_regression_candidate_case_ids"]) == 22
    assert len(final["strict_private_holdout_signal_case_ids"]) == 7
    assert pool["summary"] == {
        "original_sealed_cases": 1030,
        "removed_cases": 22,
        "remaining_sealed_cases": 1008,
        "confirmed_acceptable_variants": 5,
        "strict_private_holdout_signals": 7,
    }
    assert not (set(pool["removed_case_ids"]) & {case["id"] for case in inputs["cases"]})
    assert len(inputs["cases"]) == len(expected["cases"]) == 1008
    assert expected["source_inputs_sha256"] == hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert gate["summary"] == {
        "candidate_cases": 22,
        "zhtw_exact_matches": 22,
        "expected_idempotent": 22,
        "promotion_ready": 22,
        "promoted_to_regression": 22,
        "full_sentence_mappings_added": 22,
        "identity_mappings_added": 22,
        "candidate_dataset_total_cases": 219,
        "regression_total_cases": 1251,
        "gate_passed": True,
    }
    assert candidates["stats"]["total_cases"] == 219
    assert regression["stats"]["by_classification"]["holdout_regression_promoted"] == 219
    assert sanity["summary"]["case_count"] == 1008
    assert sanity["summary"]["accepted"] == 955
    assert sanity["summary"]["misses"] == 53
    assert sanity["summary"]["accepted_accuracy"] == 0.9474206349206349
    assert sanity["interpretation_policy"]["denominator_changed"] is True
    assert sanity["interpretation_policy"]["pure_capability_gain_claim_allowed"] is False
    for report in (final, pool, gate, sanity):
        assert report.get("expected_values_included", False) is False
        assert report.get("inputs_included", False) is False
        assert "cases" not in report


def original_seed_ids_from_report(report_ids: list[str], input_ids: list[str]) -> list[str]:
    report_id_set = set(report_ids)
    return [case_id for case_id in input_ids if case_id in report_id_set]


def test_blind_v1_schema_files_exist() -> None:
    inputs_schema = load_json(INPUTS_SCHEMA)
    expected_schema = load_json(EXPECTED_SCHEMA)
    candidates_schema = load_json(HOLDOUT_CANDIDATES_SCHEMA)

    assert inputs_schema["title"] == "zhtw published evaluation input dataset"
    assert expected_schema["title"] == "zhtw published evaluation expected dataset"
    assert candidates_schema["title"] == "zhtw holdout regression candidates"
    assert inputs_schema["properties"]["target_total"]["const"] == 2000
    assert (
        expected_schema["properties"]["expected_policy"]["properties"]["expected_source"]["const"]
        == "human_review_only"
    )
    expected_policy = expected_schema["properties"]["expected_policy"]["properties"]
    assert expected_policy["approval_policy"]["enum"] == [
        "two_human_reviewers",
        "single_human_with_ai_advisory",
    ]
    assert expected_policy["minimum_human_reviewers"]["minimum"] == 1

    annotation = expected_schema["properties"]["cases"]["items"]["properties"]["annotation"]
    assert "approval_policy" in annotation["required"]
    assert "ai_advisory_reviewers" in annotation["required"]
    assert "source_reports" in annotation["required"]
    assert annotation["properties"]["ai_advisory_reviewers"]["items"]["enum"] == [
        "codex",
        "gemini_vertex",
        "gemini_cli",
    ]


def test_blind_v1_is_classified_as_published_evaluation() -> None:
    metadata = load_json(BLIND_V1_METADATA)

    assert metadata["benchmark_classification"] == "published_evaluation"
    assert metadata["fresh_holdout"] is False
    assert metadata["sealed"] is False
    assert metadata["inputs_sha256"] == hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert metadata["expected_sha256"] == private_expected_sha256()
    assert metadata["superseding_plan"] == ("docs/plans/2026-07-19-external-benchmark-v2-plan.md")


def test_blind_v1_inputs_are_input_only_seed_pool() -> None:
    data = load_json(INPUTS)
    cases = data["cases"]

    assert data["name"] == "blind-v1.inputs"
    assert data["dataset"] == "blind-v1"
    assert data["status"] == "collecting_inputs"
    assert data["publish_state"] == "public_inputs_only"
    assert data["target_total"] == 2000
    assert data["source_policy"]["expected_not_in_inputs"] is True
    assert len(cases) == data["stats"]["total_collected"] == 1008

    case_ids = [case["id"] for case in cases]
    assert len(case_ids) == len(set(case_ids))
    assert not (load_all_removed_case_ids() & set(case_ids))
    assert not (
        {
            "blind-it-0002",
            "blind-ui-0020",
            "blind-formal-0003",
            "blind-it-0026",
            "blind-high-risk-0016",
            "blind-it-0080",
            "blind-it-0082",
            "blind-it-0084",
            "blind-high-risk-0028",
            "blind-high-risk-0030",
            "blind-it-0063",
            "blind-it-0064",
            "blind-it-0067",
            "blind-it-0070",
            "blind-it-0073",
            "blind-it-0076",
            "blind-it-0087",
            "blind-ui-0049",
            "blind-ui-0051",
            "blind-ui-0052",
            "blind-ui-0054",
            "blind-llm-0039",
            "blind-formal-0034",
            "blind-formal-0035",
            "blind-social-0034",
            "blind-social-0036",
            "blind-social-0040",
            "blind-social-0041",
            "blind-it-0088",
            "blind-it-0089",
            "blind-it-0092",
            "blind-it-0095",
            "blind-it-0096",
            "blind-it-0097",
            "blind-it-0105",
            "blind-ui-0070",
            "blind-ui-0074",
            "blind-ui-0079",
            "blind-ui-0087",
            "blind-llm-0051",
        }
        & set(case_ids)
    )
    forbidden_case_fields = {"expected", "acceptable", "review", "annotation"}
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["input"]
        assert case["source"]["license"] == "MIT-compatible project original text"
        assert case["notes"] == "Input only; expected must be human reviewed separately."

    by_domain = Counter(case["domain"] for case in cases)
    by_risk = Counter(case["risk"] for case in cases)
    assert dict(sorted(by_domain.items())) == data["stats"]["by_domain"]
    assert dict(sorted(by_risk.items())) == data["stats"]["by_risk"]
    assert by_domain == {
        "formal": 164,
        "high_risk": 128,
        "it": 189,
        "llm": 159,
        "social": 180,
        "ui": 188,
    }
    assert by_risk == {
        "baseline_guard": 161,
        "candidate_gap": 564,
        "over_conversion_guard": 283,
    }

    targets = {batch["id"]: batch["target_cases"] for batch in data["batches"]}
    assert sum(targets.values()) == data["target_total"]
    assert targets == {
        "blind-it-api-cli": 500,
        "blind-ui-i18n": 400,
        "blind-llm-content": 300,
        "blind-formal-news": 300,
        "blind-social-daily": 300,
        "blind-high-risk": 200,
    }


def test_holdout_input_pool_expansion_omits_expected_and_input_text() -> None:
    inputs = load_json(INPUTS)
    report = load_json(INPUT_POOL_EXPANSION)
    input_ids = {case["id"] for case in inputs["cases"]}

    assert report["report_type"] == "holdout_input_pool_expansion"
    assert report["dataset"] == "blind-v1"
    assert report["expected_values_included"] is False
    assert report["inputs_included"] is False
    assert report["new_cases_include_only_ids_and_metadata"] is True
    assert "cases" not in report
    assert "inputs" not in report
    assert report["summary"] == {
        "previous_input_cases": 73,
        "added_input_cases": 127,
        "current_input_cases": 200,
        "target_total": 2000,
        "added_by_domain": {
            "formal": 18,
            "high_risk": 10,
            "it": 37,
            "llm": 17,
            "social": 18,
            "ui": 27,
        },
        "current_by_domain": {
            "formal": 30,
            "high_risk": 20,
            "it": 50,
            "llm": 30,
            "social": 30,
            "ui": 40,
        },
        "added_by_risk": {
            "baseline_guard": 17,
            "candidate_gap": 79,
            "over_conversion_guard": 31,
        },
        "current_by_risk": {
            "baseline_guard": 30,
            "candidate_gap": 120,
            "over_conversion_guard": 50,
        },
    }
    assert len(report["new_case_ids"]) == 127
    assert set(report["new_case_ids"]) <= input_ids | load_all_removed_case_ids()
    assert report["policy"]["expected_not_generated"] is True
    assert report["policy"]["converter_outputs_not_used"] is True


def test_holdout_expansion_advisory_reports_are_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expansion = load_json(INPUT_POOL_EXPANSION)
    codex = load_json(CODEX_EXPANSION_FIRST_PASS)
    gemini = load_json(GEMINI_EXPANSION_ADVISORY)
    diff = load_json(CODEX_GEMINI_EXPANSION_DIFF_REVIEW)

    input_ids = {case["id"] for case in inputs["cases"]}
    expansion_ids = set(expansion["new_case_ids"])

    assert codex["review_stage"] == "first_pass_advisory"
    assert codex["reviewer"] == "codex"
    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["summary"] == {
        "total_cases": 127,
        "by_domain": {
            "formal": 18,
            "high_risk": 10,
            "it": 37,
            "llm": 17,
            "social": 18,
            "ui": 27,
        },
        "by_confidence": {"high": 87, "medium": 40},
        "review_needed": 71,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in codex["cases"]} == expansion_ids
    assert expansion_ids <= input_ids | load_all_removed_case_ids()
    assert all(case["codex_expected"] for case in codex["cases"])
    assert not any(case["promotion_allowed"] for case in codex["cases"])

    assert gemini["review_stage"] == "independent_holdout_expected_review_aggregate"
    assert gemini["reviewer"] == "gemini_vertex"
    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert len(gemini["source_reports"]) == 8
    assert gemini["summary"] == {
        "total_cases": 127,
        "exact_matches_with_codex": 79,
        "differences_from_codex": 48,
        "needs_maintainer_review": 81,
        "by_domain": {
            "formal": 18,
            "high_risk": 10,
            "it": 37,
            "llm": 17,
            "social": 18,
            "ui": 27,
        },
        "by_gemini_confidence": {"high": 127},
        "promotion_allowed": False,
    }
    assert {case["id"] for case in gemini["review"]["cases"]} == expansion_ids
    assert {row["id"] for row in gemini["comparisons"]} == expansion_ids

    assert diff["review_stage"] == "codex_gemini_difference_review"
    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["summary"] == {
        "total_cases": 127,
        "exact_matches": 79,
        "differences": 48,
        "exact_but_policy_review": 33,
        "no_immediate_question": 46,
        "maintainer_queue_total": 81,
        "difference_recommendations": {
            "codex": 39,
            "gemini": 7,
            "third_value": 2,
        },
        "promotion_allowed": False,
    }
    difference_ids = {case["id"] for case in diff["differences"]}
    policy_ids = {case["id"] for case in diff["exact_but_policy_review"]}
    no_question_ids = {case["id"] for case in diff["no_immediate_question"]}
    assert difference_ids | policy_ids | no_question_ids == expansion_ids
    assert not (difference_ids & policy_ids)
    assert not (difference_ids & no_question_ids)
    assert not (policy_ids & no_question_ids)


def test_holdout_batch4_input_pool_expansion_omits_expected_and_input_text() -> None:
    inputs = load_json(INPUTS)
    report = load_json(INPUT_POOL_EXPANSION_BATCH4)
    input_ids = {case["id"] for case in inputs["cases"]}

    assert report["report_type"] == "holdout_input_pool_expansion"
    assert report["dataset"] == "blind-v1"
    assert report["batch"] == "batch4_100_cases"
    assert report["expected_values_included"] is False
    assert report["inputs_included"] is False
    assert report["new_cases_include_only_ids_and_metadata"] is True
    assert "cases" not in report
    assert "inputs" not in report
    assert report["summary"] == {
        "previous_input_cases": 161,
        "added_input_cases": 100,
        "current_input_cases": 261,
        "target_total": 2000,
        "added_by_domain": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "current_by_domain": {
            "formal": 41,
            "high_risk": 28,
            "it": 53,
            "llm": 43,
            "social": 44,
            "ui": 52,
        },
        "added_by_risk": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
        "current_by_risk": {
            "baseline_guard": 40,
            "candidate_gap": 154,
            "over_conversion_guard": 67,
        },
    }
    assert len(report["new_case_ids"]) == 100
    assert set(report["new_case_ids"]) <= input_ids | load_all_removed_case_ids()
    assert report["new_case_ids"][0] == "blind-it-0063"
    assert report["new_case_ids"][-1] == "blind-high-risk-0030"
    assert report["policy"]["expected_not_generated"] is True
    assert report["policy"]["converter_outputs_not_used"] is True


def test_holdout_batch5_input_pool_expansion_omits_expected_and_input_text() -> None:
    inputs = load_json(INPUTS)
    report = load_json(INPUT_POOL_EXPANSION_BATCH5)
    input_ids = {case["id"] for case in inputs["cases"]}

    assert report["report_type"] == "holdout_input_pool_expansion"
    assert report["dataset"] == "blind-v1"
    assert report["batch"] == "batch5_100_cases"
    assert report["expected_values_included"] is False
    assert report["inputs_included"] is False
    assert report["new_cases_include_only_ids_and_metadata"] is True
    assert "cases" not in report
    assert "inputs" not in report
    assert report["summary"] == {
        "previous_input_cases": 238,
        "added_input_cases": 100,
        "current_input_cases": 338,
        "target_total": 2000,
        "added_by_domain": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "current_by_domain": {
            "formal": 54,
            "high_risk": 36,
            "it": 68,
            "llm": 57,
            "social": 55,
            "ui": 68,
        },
        "added_by_risk": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
        "current_by_risk": {
            "baseline_guard": 53,
            "candidate_gap": 197,
            "over_conversion_guard": 88,
        },
    }
    assert len(report["new_case_ids"]) == 100
    assert set(report["new_case_ids"]) <= input_ids | load_all_removed_case_ids()
    assert report["new_case_ids"][0] == "blind-it-0088"
    assert report["new_case_ids"][-1] == "blind-high-risk-0040"
    assert report["policy"]["expected_not_generated"] is True
    assert report["policy"]["converter_outputs_not_used"] is True


def test_holdout_batch6_input_pool_expansion_omits_expected_and_input_text() -> None:
    inputs = load_json(INPUTS)
    report = load_json(INPUT_POOL_EXPANSION_BATCH6)
    input_ids = {case["id"] for case in inputs["cases"]}

    assert report["report_type"] == "holdout_input_pool_expansion"
    assert report["dataset"] == "blind-v1"
    assert report["batch"] == "batch6_100_cases"
    assert report["expected_values_included"] is False
    assert report["inputs_included"] is False
    assert report["new_cases_include_only_ids_and_metadata"] is True
    assert "cases" not in report
    assert "inputs" not in report
    assert report["source_inputs_sha256"] == (
        "be3ab808d2f2bb71b1c86e66cd95eb182446693412c1ebbecdf5aa632f35d35e"
    )
    assert report["summary"] == {
        "previous_input_cases": 326,
        "added_input_cases": 100,
        "current_input_cases": 426,
        "target_total": 2000,
        "added_by_domain": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "current_by_domain": {
            "formal": 69,
            "high_risk": 46,
            "it": 86,
            "llm": 71,
            "social": 70,
            "ui": 84,
        },
        "added_by_risk": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
        "current_by_risk": {
            "baseline_guard": 67,
            "candidate_gap": 246,
            "over_conversion_guard": 113,
        },
        "private_expected_cases_currently_reviewed": 326,
        "new_cases_pending_expected_review": 100,
    }
    assert len(report["new_case_ids"]) == 100
    assert set(report["new_case_ids"]) <= input_ids | load_all_removed_case_ids()
    assert set(report["new_case_ids"]) & load_all_removed_case_ids() == set(
        load_json(SEALED_POOL_UPDATE_BATCH6_MISS_REVIEW)["removed_case_ids"]
    )
    assert report["new_case_ids"][0] == "blind-it-0113"
    assert report["new_case_ids"][-1] == "blind-high-risk-0050"
    assert report["policy"]["expected_not_generated"] is True
    assert report["policy"]["converter_outputs_not_used"] is True


def test_holdout_batch7_input_pool_expansion_omits_expected_and_input_text() -> None:
    inputs = load_json(INPUTS)
    report = load_json(INPUT_POOL_EXPANSION_BATCH7)
    input_ids = {case["id"] for case in inputs["cases"]}

    assert report["report_type"] == "holdout_input_pool_expansion"
    assert report["dataset"] == "blind-v1"
    assert report["batch"] == "batch7_100_cases"
    assert report["expected_values_included"] is False
    assert report["inputs_included"] is False
    assert report["new_cases_include_only_ids_and_metadata"] is True
    assert "cases" not in report
    assert "inputs" not in report
    assert report["source_inputs_sha256"] == (
        "27a3ec40cf4f5df586524d3ec307f3fcbf164a1e1ece097cc8637cd484cb5dc1"
    )
    assert report["summary"] == {
        "previous_input_cases": 415,
        "added_input_cases": 100,
        "current_input_cases": 515,
        "target_total": 2000,
        "added_by_domain": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "current_by_domain": {
            "formal": 84,
            "high_risk": 56,
            "it": 101,
            "llm": 86,
            "social": 85,
            "ui": 103,
        },
        "added_by_risk": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
        "current_by_risk": {
            "baseline_guard": 81,
            "candidate_gap": 296,
            "over_conversion_guard": 138,
        },
        "private_expected_cases_currently_reviewed": 415,
        "new_cases_pending_expected_review": 100,
    }
    assert len(report["new_case_ids"]) == 100
    assert set(report["new_case_ids"]) <= input_ids | load_all_removed_case_ids()
    assert report["new_case_ids"][0] == "blind-it-0138"
    assert report["new_case_ids"][-1] == "blind-high-risk-0060"
    assert report["policy"]["expected_not_generated"] is True
    assert report["policy"]["converter_outputs_not_used"] is True


def test_holdout_batch8_input_pool_expansion_omits_expected_and_input_text() -> None:
    inputs = load_json(INPUTS)
    report = load_json(INPUT_POOL_EXPANSION_BATCH8)
    input_ids = {case["id"] for case in inputs["cases"]}

    assert report["report_type"] == "holdout_input_pool_expansion"
    assert report["dataset"] == "blind-v1"
    assert report["batch"] == "batch8_100_cases"
    assert report["expected_values_included"] is False
    assert report["inputs_included"] is False
    assert report["new_cases_include_only_ids_and_metadata"] is True
    assert "cases" not in report
    assert "inputs" not in report
    assert report["source_inputs_sha256"] == (
        "287b30b7d08ac7761fc78624e8db5f9f9d2664a214feef6b06dfe401cdd719cb"
    )
    assert report["summary"] == {
        "previous_input_cases": 498,
        "added_input_cases": 100,
        "current_input_cases": 598,
        "target_total": 2000,
        "added_by_domain": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "current_by_domain": {
            "formal": 98,
            "high_risk": 66,
            "it": 115,
            "llm": 99,
            "social": 99,
            "ui": 121,
        },
        "added_by_risk": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
        "current_by_risk": {
            "baseline_guard": 94,
            "candidate_gap": 341,
            "over_conversion_guard": 163,
        },
        "private_expected_cases_currently_reviewed": 498,
        "new_cases_pending_expected_review": 100,
    }
    assert len(report["new_case_ids"]) == 100
    assert set(report["new_case_ids"]) <= input_ids | load_all_removed_case_ids()
    assert set(report["new_case_ids"]) & load_all_removed_case_ids() == set(
        load_json(SEALED_POOL_UPDATE_BATCH8_MISS_REVIEW)["removed_case_ids"]
    )
    assert report["new_case_ids"][0] == "blind-it-0163"
    assert report["new_case_ids"][-1] == "blind-high-risk-0070"
    assert report["policy"]["expected_not_generated"] is True
    assert report["policy"]["converter_outputs_not_used"] is True
    assert report["policy"]["private_expected_not_modified"] is True


def test_holdout_batch9_input_pool_expansion_omits_expected_and_input_text() -> None:
    inputs = load_json(INPUTS)
    report = load_json(INPUT_POOL_EXPANSION_BATCH9)
    input_ids = {case["id"] for case in inputs["cases"]}

    assert report["report_type"] == "holdout_input_pool_expansion"
    assert report["dataset"] == "blind-v1"
    assert report["batch"] == "batch9_100_cases"
    assert report["expected_values_included"] is False
    assert report["inputs_included"] is False
    assert report["new_cases_include_only_ids_and_metadata"] is True
    assert "cases" not in report
    assert "inputs" not in report
    assert report["source_inputs_sha256"] == (
        "0ac742ac9885cdae198bed6fc376c2fb5c3e991573ae4cb4ac2072cfef3e937d"
    )
    assert report["source_inputs_sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert report["summary"] == {
        "previous_input_cases": 583,
        "added_input_cases": 100,
        "current_input_cases": 683,
        "target_total": 2000,
        "added_by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "current_by_domain": {
            "formal": 112,
            "high_risk": 76,
            "it": 132,
            "llm": 113,
            "social": 114,
            "ui": 136,
        },
        "added_by_risk": {
            "candidate_gap": 60,
            "baseline_guard": 15,
            "over_conversion_guard": 25,
        },
        "current_by_risk": {
            "baseline_guard": 109,
            "candidate_gap": 386,
            "over_conversion_guard": 188,
        },
        "private_expected_cases_currently_reviewed": 583,
        "new_cases_pending_expected_review": 100,
    }
    assert len(report["new_case_ids"]) == 100
    assert set(report["new_case_ids"]) <= input_ids | load_all_removed_case_ids()
    assert report["new_case_ids"][0] == "blind-it-0188"
    assert report["new_case_ids"][-1] == "blind-high-risk-0080"
    assert report["policy"]["expected_not_generated"] is True
    assert report["policy"]["converter_outputs_not_used"] is True
    assert report["policy"]["private_expected_not_modified"] is True


def test_holdout_batch10_input_pool_expansion_omits_expected_and_input_text() -> None:
    inputs = load_json(INPUTS)
    expected = load_json(EXPECTED)
    report = load_json(INPUT_POOL_EXPANSION_BATCH10)
    input_ids = {case["id"] for case in inputs["cases"]}
    expected_ids = {case["id"] for case in expected["cases"]}

    assert report["report_type"] == "holdout_input_pool_expansion"
    assert report["dataset"] == "blind-v1"
    assert report["batch"] == "batch10_100_cases"
    assert report["expected_values_included"] is False
    assert report["inputs_included"] is False
    assert report["new_cases_include_only_ids_and_metadata"] is True
    assert "cases" not in report
    assert "inputs" not in report
    assert report["source_inputs_sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert report["summary"] == {
        "previous_input_cases": 667,
        "added_input_cases": 100,
        "current_input_cases": 767,
        "target_total": 2000,
        "added_by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "current_by_domain": {
            "formal": 125,
            "high_risk": 86,
            "it": 149,
            "llm": 126,
            "social": 129,
            "ui": 152,
        },
        "added_by_risk": {
            "candidate_gap": 60,
            "baseline_guard": 15,
            "over_conversion_guard": 25,
        },
        "current_by_risk": {
            "baseline_guard": 122,
            "candidate_gap": 432,
            "over_conversion_guard": 213,
        },
        "private_expected_cases_currently_reviewed": 667,
        "new_cases_pending_expected_review": 100,
    }
    assert len(report["new_case_ids"]) == 100
    removed_ids = load_all_removed_case_ids()
    assert set(report["new_case_ids"]) <= input_ids | removed_ids
    assert set(report["new_case_ids"]) <= expected_ids | removed_ids
    assert report["new_case_ids"][0] == "blind-it-0213"
    assert report["new_case_ids"][-1] == "blind-high-risk-0090"
    assert report["policy"]["expected_not_generated"] is True
    assert report["policy"]["converter_outputs_not_used"] is True
    assert report["policy"]["private_expected_not_modified"] is True


def test_holdout_batch11_input_pool_expansion_omits_expected_and_input_text() -> None:
    inputs = load_json(INPUTS)
    expected = load_json(EXPECTED)
    report = load_json(INPUT_POOL_EXPANSION_BATCH11)
    input_ids = {case["id"] for case in inputs["cases"]}
    expected_ids = {case["id"] for case in expected["cases"]}
    batch11_ids = set(report["new_case_ids"])

    assert report["report_type"] == "holdout_input_pool_expansion"
    assert report["dataset"] == "blind-v1"
    assert report["batch"] == "batch11_100_cases"
    assert report["expected_values_included"] is False
    assert report["inputs_included"] is False
    assert report["new_cases_include_only_ids_and_metadata"] is True
    assert "cases" not in report
    assert "inputs" not in report
    assert report["source_inputs_sha256"] == (
        "e7018d35e078a53ff1c59e4a8281b787151fd11c158859ad882defc82b93aff9"
    )
    assert report["source_inputs_sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert report["summary"] == {
        "previous_input_cases": 751,
        "added_input_cases": 100,
        "current_input_cases": 851,
        "target_total": 2000,
        "added_by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "current_by_domain": {
            "formal": 137,
            "high_risk": 96,
            "it": 167,
            "llm": 141,
            "social": 144,
            "ui": 166,
        },
        "added_by_risk": {
            "candidate_gap": 60,
            "baseline_guard": 15,
            "over_conversion_guard": 25,
        },
        "current_by_risk": {
            "baseline_guard": 134,
            "candidate_gap": 479,
            "over_conversion_guard": 238,
        },
        "private_expected_cases_currently_reviewed": 751,
        "new_cases_pending_expected_review": 100,
    }
    assert len(batch11_ids) == 100
    removed_ids = load_all_removed_case_ids()
    assert batch11_ids <= input_ids | removed_ids
    assert batch11_ids <= expected_ids | removed_ids
    assert report["new_case_ids"][0] == "blind-it-0238"
    assert report["new_case_ids"][-1] == "blind-high-risk-0100"
    assert report["policy"]["expected_not_generated"] is True
    assert report["policy"]["converter_outputs_not_used"] is True
    assert report["policy"]["private_expected_not_modified"] is True


def test_holdout_batch12_input_pool_expansion_is_fresh_and_input_only() -> None:
    inputs = load_json(INPUTS)
    expected = load_json(EXPECTED)
    report = load_json(INPUT_POOL_EXPANSION_BATCH12)
    input_ids = {case["id"] for case in inputs["cases"]}
    expected_ids = {case["id"] for case in expected["cases"]}
    batch12_ids = set(report["new_case_ids"])

    assert report["report_type"] == "holdout_input_pool_expansion"
    assert report["batch"] == "batch12_100_cases"
    assert report["expected_values_included"] is False
    assert report["inputs_included"] is False
    assert report["new_cases_include_only_ids_and_metadata"] is True
    assert "cases" not in report
    assert "inputs" not in report
    assert report["source_inputs_sha256"] == (
        "c1082299113239bfe88590425ccd6c4b4b0f0d769ddea18ce457a11050863deb"
    )
    assert report["source_inputs_sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert report["summary"] == {
        "previous_input_cases": 841,
        "added_input_cases": 100,
        "current_input_cases": 941,
        "target_total": 2000,
        "added_by_domain": {
            "formal": 20,
            "high_risk": 20,
            "it": 15,
            "llm": 10,
            "social": 20,
            "ui": 15,
        },
        "current_by_domain": {
            "formal": 153,
            "high_risk": 116,
            "it": 178,
            "llm": 149,
            "social": 164,
            "ui": 181,
        },
        "added_by_risk": {
            "baseline_guard": 16,
            "candidate_gap": 47,
            "over_conversion_guard": 37,
        },
        "current_by_risk": {
            "baseline_guard": 149,
            "candidate_gap": 521,
            "over_conversion_guard": 271,
        },
        "private_expected_cases_currently_reviewed": 841,
        "new_cases_pending_expected_review": 100,
    }
    assert len(batch12_ids) == 100
    batch12_removed_ids = set(load_json(SEALED_POOL_UPDATE_BATCH12_MISS_REVIEW)["removed_case_ids"])
    assert batch12_ids <= input_ids | batch12_removed_ids
    assert batch12_ids <= expected_ids | batch12_removed_ids
    assert batch12_ids & batch12_removed_ids == batch12_removed_ids
    assert report["new_case_ids"][0] == "blind-formal-0154"
    assert report["new_case_ids"][-1] == "blind-llm-0162"
    assert report["policy"]["input_only_before_expected_review"] is True
    assert report["policy"]["converter_outputs_used"] is False
    assert report["policy"]["competitor_outputs_used"] is False
    assert report["policy"]["private_expected_not_modified"] is True


def test_holdout_batch12_advisories_and_confirmation_are_not_ground_truth() -> None:
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH12)
    codex = load_json(CODEX_BATCH12_FIRST_PASS)
    gemini = load_json(GEMINI_BATCH12_ADVISORY)
    diff = load_json(CODEX_GEMINI_BATCH12_DIFF_REVIEW)
    packet = load_json(MAINTAINER_BATCH12_CONFIRMATION)
    batch12_ids = set(expansion["new_case_ids"])

    assert codex["review_stage"] == "first_pass_advisory"
    assert codex["reviewer"] == "codex"
    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "formal": 20,
            "high_risk": 20,
            "it": 15,
            "llm": 10,
            "social": 20,
            "ui": 15,
        },
        "by_risk": {
            "baseline_guard": 16,
            "candidate_gap": 47,
            "over_conversion_guard": 37,
        },
        "by_confidence": {"high": 79, "medium": 21},
        "review_needed": 21,
        "acceptable_variants_proposed": 11,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in codex["cases"]} == batch12_ids

    assert gemini["review_stage"] == "independent_holdout_expected_review"
    assert gemini["model_requested"] == "gemini-2.5-pro"
    assert gemini["model_observed"] == ["gemini-2.5-pro"]
    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["independence_policy"] == {
        "codex_values_seen": False,
        "current_expected_seen": False,
        "zhtw_output_seen": False,
        "competitor_output_seen": False,
        "workspace_files_seen": False,
        "input_only_cases_seen": True,
        "tool_calls": 0,
    }
    assert gemini["summary"]["total_cases"] == 100
    assert gemini["summary"]["quality_flags"] == 1
    assert {case["id"] for case in gemini["cases"]} == batch12_ids

    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["summary"] == {
        "total_cases": 100,
        "exact_matches": 87,
        "differences": 13,
        "exact_but_policy_review": 31,
        "no_immediate_question": 56,
        "maintainer_queue_total": 44,
        "difference_recommendations": {"codex": 7, "gemini": 6},
        "gemini_quality_flags": 1,
        "promotion_allowed": False,
    }
    difference_ids = {case["id"] for case in diff["differences"]}
    policy_ids = {case["id"] for case in diff["exact_but_policy_review"]}
    no_question_ids = {case["id"] for case in diff["no_immediate_question"]}
    assert difference_ids | policy_ids | no_question_ids == batch12_ids
    assert not (difference_ids & policy_ids)
    assert not (difference_ids & no_question_ids)
    assert not (policy_ids & no_question_ids)

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert {case["id"] for case in packet["cases"]} == difference_ids | policy_ids
    assert set(packet["no_immediate_question_case_ids"]) == no_question_ids
    assert packet["policy"]["private_expected_not_modified"] is True


def test_holdout_batch12_final_decision_updates_private_expected() -> None:
    expected = load_json(EXPECTED)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH12)
    packet = load_json(MAINTAINER_BATCH12_CONFIRMATION)
    decision = load_json(MAINTAINER_BATCH12_FINAL_DECISION)
    batch12_ids = set(expansion["new_case_ids"])
    batch12_cases = [case for case in expected["cases"] if case["id"] in batch12_ids]

    assert decision["review_stage"] == "maintainer_final_decision_summary"
    assert decision["scope"] == "batch12_100_cases"
    assert decision["maintainer"] == "tim"
    assert decision["decision"] == "review_ok"
    assert decision["expected_values_included"] is False
    assert decision["acceptable_values_included"] is False
    assert decision["inputs_included"] is False
    assert decision["outputs_included"] is False
    assert "cases" not in decision
    assert decision["private_expected_sha256"] == (
        "617f048425d75605e1997b8952432792f417444b3c4facec89bc5bd7a160dd22"
    )
    assert decision["private_expected_sha256"] != private_expected_sha256()
    assert decision["source_inputs_sha256"] == (
        "c1082299113239bfe88590425ccd6c4b4b0f0d769ddea18ce457a11050863deb"
    )
    assert decision["source_inputs_sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert decision["summary"] == {
        "batch12_cases": 100,
        "total_private_expected_cases": 941,
        "status": "sealed_private",
        "approval_policy": "single_human_with_ai_advisory",
        "minimum_human_reviewers": 1,
        "ai_advisory_review_allowed": True,
        "private_expected_updated": True,
        "accepted_recommended_expected": 44,
        "accepted_exact_no_immediate_question": 56,
        "primary_differences_adjudicated": 13,
        "acceptable_variant_cases": 23,
        "acceptable_variant_values": 32,
        "by_expected_source_for_batch12": {
            "human_adjudication": 13,
            "human_first_pass": 87,
        },
        "by_disagreement_for_batch12": {"false": 87, "true": 13},
        "by_expected_source_total": {
            "human_adjudication": 181,
            "human_first_pass": 760,
        },
        "by_disagreement_total": {"false": 763, "true": 178},
        "by_domain_for_batch12": {
            "formal": 20,
            "high_risk": 20,
            "it": 15,
            "llm": 10,
            "social": 20,
            "ui": 15,
        },
        "by_risk_for_batch12": {
            "baseline_guard": 16,
            "candidate_gap": 47,
            "over_conversion_guard": 37,
        },
    }
    removed_ids = set(load_json(SEALED_POOL_UPDATE_BATCH12_MISS_REVIEW)["removed_case_ids"])
    assert {case["id"] for case in batch12_cases} == batch12_ids - removed_ids
    assert decision["confirmed_case_ids"] == {
        "review_packet": [case["id"] for case in packet["cases"]],
        "no_immediate_question": packet["no_immediate_question_case_ids"],
    }


def test_holdout_batch12_miss_semantic_review_is_advisory_and_sanitized() -> None:
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH12)
    codex = load_json(BATCH12_MISS_CLASSIFICATION)
    gemini = load_json(GEMINI_BATCH12_MISS_SEMANTIC_REVIEW)
    diff = load_json(CODEX_GEMINI_BATCH12_MISS_DIFF)
    packet = load_json(MAINTAINER_BATCH12_MISS_CONFIRMATION)
    partial_decision = load_json(MAINTAINER_BATCH12_MISS_PARTIAL_DECISION)
    batch12_ids = set(expansion["new_case_ids"])
    codex_ids = {case["id"] for case in codex["cases"]}
    gemini_ids = {case["id"] for case in gemini["cases"]}
    difference_ids = {case["id"] for case in diff["differences"]}
    no_question_ids = {case["id"] for case in diff["no_immediate_question"]}
    resolved_ids = {case["id"] for case in diff["maintainer_resolved"]}
    forbidden_fields = {"input", "expected", "acceptable", "output", "zhtw_output"}

    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "acceptable_values_included": False,
        "zhtw_outputs_included": False,
        "classification_metadata_only": True,
    }
    assert codex["summary"] == {
        "total_misses": 15,
        "by_action": {
            "add_zhtw_output_as_acceptable_variant": 7,
            "move_to_public_regression_candidate": 8,
        },
        "by_domain": {
            "formal": 2,
            "high_risk": 3,
            "it": 4,
            "llm": 3,
            "social": 2,
            "ui": 1,
        },
        "by_risk": {
            "baseline_guard": 2,
            "candidate_gap": 8,
            "over_conversion_guard": 5,
        },
        "promotion_allowed": False,
    }
    assert len(codex_ids) == 15
    assert codex_ids <= batch12_ids
    assert all(not (forbidden_fields & set(case)) for case in codex["cases"])

    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["model_observed"] == ["gemini-2.5-pro"]
    assert gemini["independence_policy"] == {
        "codex_classification_seen": False,
        "current_expected_seen": False,
        "zhtw_output_seen": False,
        "competitor_output_seen": False,
        "workspace_files_seen": False,
        "input_only_cases_seen": True,
        "tool_calls": 0,
    }
    assert gemini_ids == codex_ids

    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["summary"] == {
        "total_cases": 15,
        "classification_agreements": 7,
        "classification_differences": 8,
        "recommended_acceptable_variants": 7,
        "recommended_public_regression_candidates": 8,
        "recommended_strict_private_signals": 0,
        "maintainer_queue": 6,
        "no_immediate_question": 7,
        "promotion_allowed": False,
        "maintainer_resolved": 2,
    }
    assert difference_ids | no_question_ids | resolved_ids == codex_ids
    assert not (difference_ids & no_question_ids)
    assert not (difference_ids & resolved_ids)
    assert not (no_question_ids & resolved_ids)
    assert all(not (forbidden_fields & set(case)) for case in diff["differences"])
    assert all(not (forbidden_fields & set(case)) for case in diff["no_immediate_question"])

    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["summary"]["review_cases"] == 6
    assert {case["id"] for case in packet["cases"]} == difference_ids
    assert set(packet["no_immediate_question_case_ids"]) == no_question_ids
    assert set(packet["maintainer_resolved_case_ids"]) == resolved_ids
    assert packet["policy"] == {
        "private_expected_not_modified": True,
        "sealed_pool_not_modified": True,
        "dictionary_not_modified": True,
        "maintainer_confirmation_required": True,
        "codex_and_gemini_are_advisory_only": True,
    }
    assert partial_decision["maintainer"] == "tim"
    assert partial_decision["resolved_case_ids"] == sorted(resolved_ids)
    assert partial_decision["resolved_action"] == "move_to_public_regression_candidate"
    assert partial_decision["remaining_maintainer_queue"] == 6
    assert partial_decision["private_expected_updated"] is False
    assert partial_decision["sealed_pool_updated"] is False
    assert partial_decision["dictionary_updated"] is False


def test_holdout_batch12_miss_final_decision_updates_pool_and_promotion_gate() -> None:
    decision = load_json(MAINTAINER_BATCH12_MISS_FINAL_DECISION)
    pool_update = load_json(SEALED_POOL_UPDATE_BATCH12_MISS_REVIEW)
    gate = load_json(HOLDOUT_PROMOTION_GATE_BATCH12_MISS_REVIEW)
    inputs = load_json(INPUTS)
    expected = load_json(EXPECTED)
    candidates = load_json(HOLDOUT_CANDIDATES)
    regression = load_json(REGRESSION)

    acceptable_ids = set(decision["confirmed_acceptable_variant_case_ids"])
    removed_ids = set(decision["removed_to_public_regression_candidate_case_ids"])
    strict_ids = set(decision["strict_private_holdout_signal_case_ids"])
    input_ids = {case["id"] for case in inputs["cases"]}
    expected_ids = {case["id"] for case in expected["cases"]}

    assert decision["decision"] == "review_ok"
    assert decision["promotion_allowed"] is True
    assert decision["private_expected_updated"] is True
    assert decision["sealed_pool_updated"] is True
    assert decision["dictionary_updated"] is True
    assert len(acceptable_ids) == 4
    assert len(removed_ids) == 11
    assert strict_ids == set()
    assert acceptable_ids <= input_ids
    assert acceptable_ids <= expected_ids
    assert not (removed_ids & input_ids)
    assert not (removed_ids & expected_ids)
    assert decision["source_inputs_sha256_after"] == (
        "9297eaf5688b87b0d89d83dceb04f9ce3fa62944f6cbde83b485bc0524e7f780"
    )
    assert decision["source_inputs_sha256_after"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert decision["private_expected_sha256_after"] == (
        "81246822bffc1423b1460b0bfe7f1ed2539060f31880f8b49424e85c25b6052e"
    )
    assert decision["private_expected_sha256_after"] != private_expected_sha256()
    assert decision["candidate_dataset_sha256_after_promotion"] == (
        "74461c47e7dcc1c1f6296bbc82eeabb4eb13f9dafe821eaefa478776296fc1a7"
    )
    assert decision["regression_sha256_after_promotion"] == (
        "e3313f2dc54c0e0f5d7adfb7688528913f3a3118655457bfa0567f121fb6754c"
    )
    assert (
        decision["candidate_dataset_sha256_after_promotion"]
        != hashlib.sha256(HOLDOUT_CANDIDATES.read_bytes()).hexdigest()
    )
    assert (
        decision["regression_sha256_after_promotion"]
        != hashlib.sha256(REGRESSION.read_bytes()).hexdigest()
    )
    assert decision["summary"] == {
        "reviewed_batch12_misses": 15,
        "confirmed_acceptable_variants": 4,
        "removed_to_public_regression_candidates": 11,
        "strict_private_holdout_signals": 0,
        "remaining_sealed_input_cases": 930,
        "remaining_private_expected_cases": 930,
        "candidate_dataset_total_cases": 197,
        "dictionary_updated": True,
        "promotion_gate_pending": False,
        "promotion_gate_passed": True,
        "promoted_to_regression": 11,
        "full_sentence_mappings_added": 11,
        "identity_mappings_added": 11,
        "regression_total_cases": 1229,
    }
    assert (
        pool_update["removed_case_ids"]
        == decision["removed_to_public_regression_candidate_case_ids"]
    )
    assert pool_update["remaining_inputs_sha256"] == (
        "9297eaf5688b87b0d89d83dceb04f9ce3fa62944f6cbde83b485bc0524e7f780"
    )
    assert pool_update["remaining_inputs_sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert pool_update["remaining_expected_sha256"] == (
        "81246822bffc1423b1460b0bfe7f1ed2539060f31880f8b49424e85c25b6052e"
    )
    assert pool_update["remaining_expected_sha256"] != private_expected_sha256()
    assert gate["promoted_case_ids"] == pool_update["removed_case_ids"]
    assert gate["source_candidates_sha256"] == (
        "74461c47e7dcc1c1f6296bbc82eeabb4eb13f9dafe821eaefa478776296fc1a7"
    )
    assert gate["regression_sha256"] == (
        "e3313f2dc54c0e0f5d7adfb7688528913f3a3118655457bfa0567f121fb6754c"
    )
    assert candidates["stats"]["total_cases"] == 219
    assert regression["stats"]["by_classification"]["holdout_regression_promoted"] == 219
    for report in (decision, pool_update, gate):
        assert report["expected_values_included"] is False
        assert report["inputs_included"] is False
        assert "cases" not in report


def test_holdout_batch13_review_and_first_benchmark_are_auditable() -> None:
    inputs = load_json(INPUTS)
    expected = load_json(EXPECTED)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH13)
    codex = load_json(CODEX_BATCH13_FIRST_PASS)
    gemini = load_json(GEMINI_BATCH13_ADVISORY)
    diff = load_json(CODEX_GEMINI_BATCH13_DIFF_REVIEW)
    packet = load_json(MAINTAINER_BATCH13_CONFIRMATION)
    final = load_json(MAINTAINER_BATCH13_FINAL_DECISION)
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH13)

    batch13_ids = set(expansion["new_case_ids"])
    input_ids = {case["id"] for case in inputs["cases"]}
    expected_ids = {case["id"] for case in expected["cases"]}
    removed_ids = set(load_json(SEALED_POOL_UPDATE_BATCH13_MISS_REVIEW)["removed_case_ids"])

    assert expansion["batch"] == "batch13_100_cases"
    assert expansion["source_inputs_sha256"] == final["source_inputs_sha256"]
    assert expansion["expected_values_included"] is False
    assert expansion["inputs_included"] is False
    assert "cases" not in expansion
    assert expansion["summary"] == {
        "previous_input_cases": 930,
        "added_input_cases": 100,
        "current_input_cases": 1030,
        "target_total": 2000,
        "added_by_domain": {
            "formal": 15,
            "high_risk": 15,
            "it": 20,
            "llm": 15,
            "social": 20,
            "ui": 15,
        },
        "current_by_domain": {
            "formal": 166,
            "high_risk": 130,
            "it": 195,
            "llm": 162,
            "social": 182,
            "ui": 195,
        },
        "added_by_risk": {
            "baseline_guard": 18,
            "candidate_gap": 64,
            "over_conversion_guard": 18,
        },
        "current_by_risk": {
            "baseline_guard": 165,
            "candidate_gap": 581,
            "over_conversion_guard": 284,
        },
        "private_expected_cases_currently_reviewed": 930,
        "new_cases_pending_expected_review": 100,
    }
    assert len(batch13_ids) == 100
    assert batch13_ids <= input_ids | removed_ids
    assert batch13_ids <= expected_ids | removed_ids
    assert len(expected_ids) == 1008

    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["summary"]["by_confidence"] == {"high": 78, "medium": 22}
    assert codex["summary"]["review_needed"] == 22
    assert {case["id"] for case in codex["cases"]} == batch13_ids

    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["model_requested"] == "gemini-2.5-pro"
    assert gemini["model_observed"] == ["gemini-2.5-pro"]
    assert gemini["quality_flags"] == []
    assert gemini["independence_policy"] == {
        "codex_values_seen": False,
        "current_expected_seen": False,
        "zhtw_output_seen": False,
        "competitor_output_seen": False,
        "workspace_files_seen": False,
        "input_only_cases_seen": True,
        "tool_calls": 0,
    }
    assert {case["id"] for case in gemini["cases"]} == batch13_ids
    for raw_path in gemini["raw_reports"]:
        raw = load_json(ROOT / raw_path)
        assert raw["stats"]["tools"]["totalCalls"] == 0
        assert raw["stats"]["files"] == {"totalLinesAdded": 0, "totalLinesRemoved": 0}

    assert diff["summary"] == {
        "total_cases": 100,
        "exact_matches": 66,
        "differences": 34,
        "exact_but_policy_review": 19,
        "no_immediate_question": 47,
        "maintainer_queue_total": 53,
        "difference_recommendations": {"codex": 29, "gemini": 5},
        "gemini_quality_flags": 0,
        "promotion_allowed": False,
    }
    difference_ids = {case["id"] for case in diff["differences"]}
    policy_ids = {case["id"] for case in diff["exact_but_policy_review"]}
    no_question_ids = {case["id"] for case in diff["no_immediate_question"]}
    assert difference_ids | policy_ids | no_question_ids == batch13_ids
    assert not (difference_ids & policy_ids)
    assert not (difference_ids & no_question_ids)
    assert not (policy_ids & no_question_ids)

    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["summary"] == {
        "review_cases": 53,
        "difference_cases": 34,
        "exact_policy_review_cases": 19,
        "no_immediate_question_cases": 47,
    }
    assert {case["id"] for case in packet["cases"]} == difference_ids | policy_ids
    assert set(packet["no_immediate_question_case_ids"]) == no_question_ids
    assert packet["policy"]["private_expected_not_modified"] is True
    assert all(case["maintainer_decision"] is None for case in packet["cases"])

    assert final["decision"] == "review_ok"
    assert final["private_expected_updated"] is True
    assert final["source_inputs_sha256"] == expansion["source_inputs_sha256"]
    assert final["private_expected_sha256"] == sanity["expected"]["sha256"]
    assert set(final["confirmed_case_ids"]) == batch13_ids
    assert final["summary"]["human_adjudication"] == 35
    assert final["summary"]["human_first_pass"] == 65
    assert final["summary"]["benchmark_pending"] is False
    assert final["summary"]["batch13_accepted"] == 66
    assert final["summary"]["batch13_misses"] == 34

    assert sanity["review_stage"] == "after_batch13_final_decision"
    assert sanity["inputs"]["sha256"] == final["source_inputs_sha256"]
    assert sanity["expected"]["sha256"] == final["private_expected_sha256"]
    assert sanity["interpretation_policy"] == {
        "fresh_batch_before_tuning": True,
        "batch13_capability_claim_allowed": True,
        "approval_policy": "single_human_with_ai_advisory",
        "market_best_claim_allowed": False,
    }
    assert sanity["summary"]["case_count"] == 1030
    assert sanity["summary"]["accepted"] == 950
    assert sanity["summary"]["misses"] == 80
    assert sanity["summary"]["accepted_accuracy"] == 0.9223300970873787
    assert sanity["batch13_summary"] == {
        "case_count": 100,
        "accepted": 66,
        "misses": 34,
        "primary_exact": 57,
        "acceptable_exact": 9,
        "idempotent": 100,
        "accepted_accuracy": 0.66,
        "by_domain": {
            "formal": {"total": 15, "accepted": 13, "misses": 2},
            "high_risk": {"total": 15, "accepted": 10, "misses": 5},
            "it": {"total": 20, "accepted": 10, "misses": 10},
            "llm": {"total": 15, "accepted": 9, "misses": 6},
            "social": {"total": 20, "accepted": 17, "misses": 3},
            "ui": {"total": 15, "accepted": 7, "misses": 8},
        },
        "misses_by_risk": {
            "baseline_guard": 4,
            "candidate_gap": 28,
            "over_conversion_guard": 2,
        },
    }
    for key in (
        "expected_values_included",
        "acceptable_values_included",
        "rows_included",
        "inputs_included",
        "outputs_included",
        "benchmark_rows_included",
    ):
        assert sanity[key] is False
    assert "rows" not in sanity


def test_holdout_batch13_miss_review_is_independent_and_sanitized() -> None:
    codex = load_json(BATCH13_MISS_CLASSIFICATION)
    gemini = load_json(GEMINI_BATCH13_MISS_SEMANTIC_REVIEW)
    diff = load_json(CODEX_GEMINI_BATCH13_MISS_DIFF)
    packet = load_json(MAINTAINER_BATCH13_MISS_CONFIRMATION)
    raw = load_json(ROOT / gemini["source_raw"])
    forbidden_fields = {"input", "expected", "acceptable", "output", "zhtw_output"}

    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["summary"] == {
        "total_misses": 34,
        "by_action": {
            "add_zhtw_output_as_acceptable_variant": 5,
            "keep_strict_private_signal": 9,
            "move_to_public_regression_candidate": 20,
        },
        "by_domain": {
            "formal": 2,
            "high_risk": 5,
            "it": 10,
            "llm": 6,
            "social": 3,
            "ui": 8,
        },
        "by_risk": {
            "baseline_guard": 4,
            "candidate_gap": 28,
            "over_conversion_guard": 2,
        },
        "by_confidence": {"high": 20, "medium": 14},
        "promotion_allowed": False,
    }
    assert all(not (forbidden_fields & set(case)) for case in codex["cases"])

    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["model_observed"] == ["gemini-2.5-pro"]
    assert gemini["independence_policy"] == {
        "codex_classification_seen": False,
        "current_expected_seen": False,
        "zhtw_output_seen": False,
        "competitor_output_seen": False,
        "workspace_files_seen": False,
        "input_only_cases_seen": True,
        "tool_calls": 0,
    }
    assert gemini["summary"] == {
        "total_cases": 34,
        "by_action": {
            "add_zhtw_output_as_acceptable_variant": 3,
            "keep_strict_private_signal": 3,
            "move_to_public_regression_candidate": 28,
        },
        "by_confidence": {"high": 34},
        "review_needed": 0,
        "promotion_allowed": False,
    }
    assert all(not (forbidden_fields & set(case)) for case in gemini["cases"])
    assert raw["stats"]["tools"]["totalCalls"] == 0
    assert raw["stats"]["files"] == {"totalLinesAdded": 0, "totalLinesRemoved": 0}

    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["summary"] == {
        "total_cases": 34,
        "classification_agreements": 19,
        "classification_differences": 15,
        "recommended_by_action": {
            "add_zhtw_output_as_acceptable_variant": 5,
            "keep_strict_private_signal": 7,
            "move_to_public_regression_candidate": 22,
        },
        "maintainer_queue": 19,
        "no_immediate_question": 15,
        "promotion_allowed": False,
    }
    difference_ids = {case["id"] for case in diff["differences"]}
    agreement_ids = {case["id"] for case in diff["agreements"]}
    queue_ids = set(diff["maintainer_queue_case_ids"])
    no_question_ids = set(diff["no_immediate_question_case_ids"])
    assert len(difference_ids) == 15
    assert len(agreement_ids) == 19
    assert len(queue_ids) == 19
    assert len(no_question_ids) == 15
    assert difference_ids | agreement_ids == queue_ids | no_question_ids
    assert not (difference_ids & agreement_ids)
    assert not (queue_ids & no_question_ids)
    assert all(not (forbidden_fields & set(case)) for case in diff["differences"])

    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["summary"] == {
        "review_cases": 19,
        "classification_difference_cases": 15,
        "high_risk_or_medium_agreement_cases": 4,
        "no_immediate_question_cases": 15,
    }
    assert {case["id"] for case in packet["cases"]} == queue_ids
    assert set(packet["no_immediate_question_case_ids"]) == no_question_ids
    assert all(not (forbidden_fields & set(case)) for case in packet["cases"])
    assert all(case["maintainer_decision"] is None for case in packet["cases"])
    assert packet["policy"] == {
        "private_expected_not_modified": True,
        "sealed_pool_not_modified": True,
        "dictionary_not_modified": True,
        "maintainer_confirmation_required": True,
        "codex_and_gemini_are_advisory_only": True,
    }


def test_holdout_batch4_advisory_reports_are_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH4)
    codex = load_json(CODEX_BATCH4_FIRST_PASS)
    gemini = load_json(GEMINI_BATCH4_ADVISORY)
    diff = load_json(CODEX_GEMINI_BATCH4_DIFF_REVIEW)
    packet = load_json(MAINTAINER_BATCH4_CONFIRMATION)

    input_ids = {case["id"] for case in inputs["cases"]}
    batch4_ids = set(expansion["new_case_ids"])

    assert batch4_ids <= input_ids | load_all_removed_case_ids()
    assert codex["review_stage"] == "first_pass_advisory"
    assert codex["reviewer"] == "codex"
    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "by_confidence": {"high": 75, "medium": 25},
        "review_needed": 53,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in codex["cases"]} == batch4_ids
    assert all(case["codex_expected"] for case in codex["cases"])
    assert not any(case["promotion_allowed"] for case in codex["cases"])

    assert gemini["review_stage"] == "independent_holdout_expected_review"
    assert gemini["reviewer"] == "gemini_vertex"
    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["summary"] == {
        "total_cases": 100,
        "exact_matches_with_codex": 74,
        "differences_from_codex": 26,
        "needs_maintainer_review": 64,
        "by_domain": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "by_gemini_confidence": {"high": 100},
        "promotion_allowed": False,
    }
    assert len(gemini["postprocess"]["issue_tags_repaired_from_case_metadata"]) == 17
    assert {case["id"] for case in gemini["review"]["cases"]} == batch4_ids
    assert {row["id"] for row in gemini["comparisons"]} == batch4_ids

    assert diff["review_stage"] == "codex_gemini_difference_review"
    assert diff["scope"] == "batch4_100_cases"
    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["summary"] == {
        "total_cases": 100,
        "exact_matches": 74,
        "differences": 26,
        "exact_but_policy_review": 38,
        "no_immediate_question": 36,
        "maintainer_queue_total": 64,
        "difference_recommendations": {
            "codex": 21,
            "gemini": 4,
            "third_value": 1,
        },
        "promotion_allowed": False,
    }
    assert len(diff["differences"]) == 26
    assert len(diff["exact_but_policy_review"]) == 38
    assert len(diff["no_immediate_question"]) == 36
    assert (
        {case["id"] for case in diff["differences"]}
        | {case["id"] for case in diff["exact_but_policy_review"]}
        | {case["id"] for case in diff["no_immediate_question"]}
    ) == batch4_ids

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch4_100_cases"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["summary"] == {
        "total_review_cases": 64,
        "difference_cases": 26,
        "policy_review_cases": 38,
        "no_immediate_question": 36,
        "difference_recommendations": {
            "codex": 21,
            "gemini": 4,
            "third_value": 1,
        },
        "by_domain": {
            "formal": 8,
            "high_risk": 10,
            "it": 19,
            "llm": 7,
            "social": 9,
            "ui": 11,
        },
        "by_risk": {
            "baseline_guard": 6,
            "candidate_gap": 33,
            "over_conversion_guard": 25,
        },
        "by_policy_reason": {
            "Codex confidence medium": 11,
            "Codex confidence medium, over-conversion guard": 1,
            "high-risk domain": 4,
            "high-risk domain, over-conversion guard": 3,
            "over-conversion guard": 19,
        },
        "promotion_allowed": False,
    }
    assert len(packet["cases"]) == 64
    assert len(packet["no_immediate_question_case_ids"]) == 36
    assert {case["kind"] for case in packet["cases"]} == {
        "difference",
        "exact_but_policy_review",
    }
    assert all(case["recommended_expected"] for case in packet["cases"])


def test_holdout_batch5_advisory_reports_are_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH5)
    codex = load_json(CODEX_BATCH5_FIRST_PASS)
    gemini = load_json(GEMINI_BATCH5_ADVISORY)
    diff = load_json(CODEX_GEMINI_BATCH5_DIFF_REVIEW)
    packet = load_json(MAINTAINER_BATCH5_CONFIRMATION)

    input_ids = {case["id"] for case in inputs["cases"]}
    batch5_ids = set(expansion["new_case_ids"])

    assert batch5_ids <= input_ids | load_all_removed_case_ids()
    assert codex["review_stage"] == "first_pass_advisory"
    assert codex["reviewer"] == "codex"
    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "by_risk": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
        "by_confidence": {"high": 80, "medium": 20},
        "review_needed": 46,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in codex["cases"]} == batch5_ids
    assert all(case["codex_expected"] for case in codex["cases"])
    assert not any(case["promotion_allowed"] for case in codex["cases"])

    assert gemini["review_stage"] == "independent_holdout_expected_review"
    assert gemini["reviewer"] == "gemini_cli"
    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["model_requested"] == "gemini-2.5-flash"
    assert gemini["chunking"] == {
        "strategy": "by_domain",
        "domain_order": ["it", "ui", "llm", "formal", "social", "high_risk"],
    }
    assert gemini["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "by_risk": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
        "by_confidence": {"high": 95, "medium": 5},
        "review_needed": 39,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in gemini["cases"]} == batch5_ids
    assert all(case["gemini_expected"] for case in gemini["cases"])
    assert not any(case["promotion_allowed"] for case in gemini["cases"])

    assert diff["review_stage"] == "codex_gemini_difference_review"
    assert diff["scope"] == "batch5_100_cases"
    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["summary"] == {
        "total_cases": 100,
        "exact_matches": 92,
        "differences": 8,
        "exact_but_policy_review": 42,
        "no_immediate_question": 50,
        "maintainer_queue_total": 50,
        "difference_recommendations": {
            "codex": 5,
            "gemini": 3,
        },
        "zhtw_current_status_for_differences": {
            "in_recommended_acceptable": 5,
            "matches_recommended": 1,
            "needs_followup_if_confirmed": 2,
        },
        "promotion_allowed": False,
    }
    difference_ids = {case["id"] for case in diff["differences"]}
    policy_ids = {case["id"] for case in diff["exact_but_policy_review"]}
    no_question_ids = {case["id"] for case in diff["no_immediate_question"]}
    assert difference_ids == {
        "blind-high-risk-0031",
        "blind-it-0094",
        "blind-llm-0055",
        "blind-social-0052",
        "blind-ui-0068",
        "blind-ui-0069",
        "blind-ui-0074",
        "blind-ui-0077",
    }
    assert difference_ids | policy_ids | no_question_ids == batch5_ids
    assert not (difference_ids & policy_ids)
    assert not (difference_ids & no_question_ids)
    assert not (policy_ids & no_question_ids)
    assert all("zhtw_current" in case for case in diff["differences"])

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch5_100_cases"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["source_diff_review"] == (
        "docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch5-100-cases-2026-07-09.json"
    )
    assert packet["summary"] == {
        "total_review_cases": 50,
        "difference_cases": 8,
        "policy_review_cases": 42,
        "no_immediate_question": 50,
        "difference_recommendations": {
            "codex": 5,
            "gemini": 3,
        },
        "by_domain": {
            "formal": 6,
            "high_risk": 10,
            "it": 9,
            "llm": 7,
            "social": 7,
            "ui": 11,
        },
        "by_risk": {
            "baseline_guard": 2,
            "candidate_gap": 23,
            "over_conversion_guard": 25,
        },
        "by_policy_reason": {
            "Codex confidence medium": 16,
            "Gemini confidence medium": 4,
            "high-risk domain": 9,
            "over-conversion guard": 25,
        },
        "zhtw_current_status_for_differences": {
            "in_recommended_acceptable": 5,
            "matches_recommended": 1,
            "needs_followup_if_confirmed": 2,
        },
        "promotion_allowed": False,
    }
    assert len(packet["cases"]) == 50
    assert len(packet["no_immediate_question_case_ids"]) == 50
    assert {case["kind"] for case in packet["cases"]} == {
        "difference",
        "exact_but_policy_review",
    }
    assert {case["id"] for case in packet["cases"]} == difference_ids | policy_ids
    assert all(case["recommended_expected"] for case in packet["cases"])
    assert all("zhtw_current" in case for case in packet["cases"])


def test_holdout_batch6_codex_first_pass_is_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH6)
    codex = load_json(CODEX_BATCH6_FIRST_PASS)

    input_ids = {case["id"] for case in inputs["cases"]}
    batch6_ids = set(expansion["new_case_ids"])

    assert batch6_ids <= input_ids | load_all_removed_case_ids()
    assert batch6_ids & load_all_removed_case_ids() == set(
        load_json(SEALED_POOL_UPDATE_BATCH6_MISS_REVIEW)["removed_case_ids"]
    )
    assert codex["review_stage"] == "first_pass_advisory"
    assert codex["reviewer"] == "codex"
    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["source_expansion_report"] == (
        "docs/reports/holdout-input-pool-expansion-blind-v1-batch6-100-cases-2026-07-09.json"
    )
    assert codex["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 60,
            "over_conversion_guard": 25,
            "baseline_guard": 15,
        },
        "by_confidence": {"high": 80, "medium": 20},
        "review_needed": 50,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in codex["cases"]} == batch6_ids
    assert all(case["codex_expected"] for case in codex["cases"])
    assert not any(case["promotion_allowed"] for case in codex["cases"])
    assert sum(1 for case in codex["cases"] if case["review_needed"]) == 50
    assert all(
        case["review_needed"]
        for case in codex["cases"]
        if case["risk"] == "over_conversion_guard"
        or case["domain"] == "high_risk"
        or case["confidence"] == "medium"
    )
    assert not any(
        case["review_needed"]
        for case in codex["cases"]
        if case["risk"] != "over_conversion_guard"
        and case["domain"] != "high_risk"
        and case["confidence"] == "high"
    )


def test_holdout_batch7_codex_first_pass_is_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH7)
    codex = load_json(CODEX_BATCH7_FIRST_PASS)

    input_ids = {case["id"] for case in inputs["cases"]}
    batch7_ids = set(expansion["new_case_ids"])

    assert batch7_ids <= input_ids | load_all_removed_case_ids()
    assert codex["review_stage"] == "first_pass_advisory"
    assert codex["reviewer"] == "codex"
    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["source_expansion_report"] == (
        "docs/reports/holdout-input-pool-expansion-blind-v1-batch7-100-cases-2026-07-10.json"
    )
    assert codex["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 60,
            "baseline_guard": 15,
            "over_conversion_guard": 25,
        },
        "by_confidence": {"medium": 20, "high": 80},
        "review_needed": 50,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in codex["cases"]} == batch7_ids
    assert all(case["codex_expected"] for case in codex["cases"])
    assert not any(case["promotion_allowed"] for case in codex["cases"])
    assert sum(1 for case in codex["cases"] if case["review_needed"]) == 50
    assert all(
        case["review_needed"]
        for case in codex["cases"]
        if case["risk"] == "over_conversion_guard"
        or case["domain"] == "high_risk"
        or case["confidence"] == "medium"
    )
    assert not any(
        case["review_needed"]
        for case in codex["cases"]
        if case["risk"] != "over_conversion_guard"
        and case["domain"] != "high_risk"
        and case["confidence"] == "high"
    )


def test_holdout_batch8_codex_first_pass_is_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH8)
    codex = load_json(CODEX_BATCH8_FIRST_PASS)

    input_ids = {case["id"] for case in inputs["cases"]}
    batch8_ids = set(expansion["new_case_ids"])

    assert batch8_ids <= input_ids | load_all_removed_case_ids()
    assert codex["review_stage"] == "first_pass_advisory"
    assert codex["reviewer"] == "codex"
    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["source_expansion_report"] == (
        "docs/reports/holdout-input-pool-expansion-blind-v1-batch8-100-cases-2026-07-10.json"
    )
    assert codex["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 60,
            "baseline_guard": 15,
            "over_conversion_guard": 25,
        },
        "by_confidence": {"medium": 20, "high": 80},
        "review_needed": 50,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in codex["cases"]} == batch8_ids
    assert all(case["codex_expected"] for case in codex["cases"])
    assert not any(case["promotion_allowed"] for case in codex["cases"])
    assert sum(1 for case in codex["cases"] if case["review_needed"]) == 50
    assert all(
        case["review_needed"]
        for case in codex["cases"]
        if case["risk"] == "over_conversion_guard"
        or case["domain"] == "high_risk"
        or case["confidence"] == "medium"
    )
    assert not any(
        case["review_needed"]
        for case in codex["cases"]
        if case["risk"] != "over_conversion_guard"
        and case["domain"] != "high_risk"
        and case["confidence"] == "high"
    )


def test_holdout_batch6_gemini_cli_advisory_is_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH6)
    gemini = load_json(GEMINI_BATCH6_ADVISORY)

    input_ids = {case["id"] for case in inputs["cases"]}
    batch6_ids = set(expansion["new_case_ids"])

    assert batch6_ids <= input_ids | load_all_removed_case_ids()
    assert batch6_ids & load_all_removed_case_ids() == set(
        load_json(SEALED_POOL_UPDATE_BATCH6_MISS_REVIEW)["removed_case_ids"]
    )
    assert gemini["review_stage"] == "independent_holdout_expected_review"
    assert gemini["reviewer"] == "gemini_cli"
    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["model_requested"] == "gemini-2.5-flash"
    assert gemini["chunking"] == {
        "strategy": "by_domain",
        "domain_order": ["it", "ui", "llm", "formal", "social", "high_risk"],
    }
    assert gemini["source_expansion_report"] == (
        "docs/reports/holdout-input-pool-expansion-blind-v1-batch6-100-cases-2026-07-09.json"
    )
    assert "GEMINI_API_KEY" in gemini["policy"]
    assert gemini["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 60,
            "over_conversion_guard": 25,
            "baseline_guard": 15,
        },
        "by_confidence": {"high": 100},
        "review_needed": 70,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in gemini["cases"]} == batch6_ids
    assert all(case["gemini_expected"] for case in gemini["cases"])
    assert not any(case["promotion_allowed"] for case in gemini["cases"])
    assert sum(1 for case in gemini["cases"] if case["review_needed"]) == 70
    assert all(
        case["review_needed"]
        for case in gemini["cases"]
        if case["risk"] == "over_conversion_guard"
        or case["domain"] == "high_risk"
        or case["confidence"] in {"medium", "low"}
    )


def test_holdout_batch6_diff_review_and_confirmation_are_not_ground_truth() -> None:
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH6)
    diff = load_json(CODEX_GEMINI_BATCH6_DIFF_REVIEW)
    packet = load_json(MAINTAINER_BATCH6_CONFIRMATION)

    batch6_ids = set(expansion["new_case_ids"])

    assert diff["review_stage"] == "codex_gemini_difference_review"
    assert diff["scope"] == "batch6_100_cases"
    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["source_codex_report"] == (
        "docs/reports/holdout-codex-first-pass-blind-v1-batch6-100-cases-2026-07-10.json"
    )
    assert diff["source_gemini_report"] == (
        "docs/reports/holdout-gemini-cli-advisory-blind-v1-batch6-100-cases-2026-07-10.json"
    )
    assert diff["summary"] == {
        "total_cases": 100,
        "exact_matches": 80,
        "differences": 20,
        "exact_but_policy_review": 56,
        "no_immediate_question": 24,
        "maintainer_queue_total": 76,
        "difference_recommendations": {
            "codex": 13,
            "gemini": 4,
            "third": 3,
        },
        "zhtw_current_status_for_differences": {
            "needs_followup_if_confirmed": 9,
            "in_recommended_acceptable": 8,
            "matches_recommended": 3,
        },
        "promotion_allowed": False,
    }
    difference_ids = {case["id"] for case in diff["differences"]}
    policy_ids = {case["id"] for case in diff["exact_but_policy_review"]}
    no_question_ids = {case["id"] for case in diff["no_immediate_question"]}
    assert difference_ids == {
        "blind-it-0113",
        "blind-it-0115",
        "blind-it-0117",
        "blind-it-0123",
        "blind-it-0124",
        "blind-it-0130",
        "blind-it-0133",
        "blind-it-0136",
        "blind-ui-0089",
        "blind-ui-0090",
        "blind-ui-0091",
        "blind-ui-0094",
        "blind-ui-0096",
        "blind-ui-0097",
        "blind-ui-0102",
        "blind-ui-0106",
        "blind-ui-0107",
        "blind-llm-0069",
        "blind-llm-0070",
        "blind-formal-0065",
    }
    assert difference_ids | policy_ids | no_question_ids == batch6_ids
    assert len(policy_ids) == 56
    assert len(no_question_ids) == 24
    assert all(case["recommended_expected"] for case in diff["differences"])
    assert all("zhtw_current" in case for case in diff["differences"])

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch6_100_cases"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["source_diff_review"] == (
        "docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch6-100-cases-2026-07-10.json"
    )
    assert packet["summary"] == {
        "total_review_cases": 76,
        "difference_cases": 20,
        "policy_review_cases": 56,
        "no_immediate_question": 24,
        "difference_recommendations": {
            "codex": 13,
            "gemini": 4,
            "third": 3,
        },
        "by_domain": {
            "it": 17,
            "ui": 18,
            "llm": 12,
            "formal": 12,
            "social": 7,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 45,
            "over_conversion_guard": 25,
            "baseline_guard": 6,
        },
        "by_policy_reason": {
            "Codex confidence medium": 20,
            "Gemini review-needed variant": 37,
            "over-conversion guard": 25,
            "high-risk domain": 10,
        },
        "zhtw_current_status_for_differences": {
            "needs_followup_if_confirmed": 9,
            "in_recommended_acceptable": 8,
            "matches_recommended": 3,
        },
        "promotion_allowed": False,
    }
    assert len(packet["cases"]) == 76
    assert len(packet["no_immediate_question_case_ids"]) == 24
    assert {case["kind"] for case in packet["cases"]} == {
        "difference",
        "exact_but_policy_review",
    }
    assert {case["id"] for case in packet["cases"]} == difference_ids | policy_ids
    assert set(packet["no_immediate_question_case_ids"]) == no_question_ids
    assert all(case["recommended_expected"] for case in packet["cases"])
    assert all("zhtw_current" in case for case in packet["cases"])


def test_holdout_batch7_gemini_cli_advisory_is_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH7)
    gemini = load_json(GEMINI_BATCH7_ADVISORY)

    input_ids = {case["id"] for case in inputs["cases"]}
    batch7_ids = set(expansion["new_case_ids"])

    assert batch7_ids <= input_ids | load_all_removed_case_ids()
    assert gemini["review_stage"] == "independent_holdout_expected_review"
    assert gemini["reviewer"] == "gemini_cli"
    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["model_requested"] == "gemini-2.5-flash"
    assert gemini["chunking"] == {
        "strategy": "by_domain",
        "domain_order": ["it", "ui", "llm", "formal", "social", "high_risk"],
    }
    assert gemini["source_expansion_report"] == (
        "docs/reports/holdout-input-pool-expansion-blind-v1-batch7-100-cases-2026-07-10.json"
    )
    assert "GEMINI_API_KEY" in gemini["policy"]
    assert gemini["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 60,
            "baseline_guard": 15,
            "over_conversion_guard": 25,
        },
        "by_confidence": {"high": 100},
        "review_needed": 32,
        "promotion_allowed": False,
    }
    assert gemini["postprocess"] == {
        "malformed_acceptable_removed": [
            {
                "id": "blind-social-0080",
                "removed_acceptable": "禮這家店的排隊系統會傳送簡訊提醒。",
            }
        ]
    }
    assert {case["id"] for case in gemini["cases"]} == batch7_ids
    assert all(case["gemini_expected"] for case in gemini["cases"])
    assert not any(case["promotion_allowed"] for case in gemini["cases"])
    assert sum(1 for case in gemini["cases"] if case["review_needed"]) == 32
    assert all(
        case["review_needed"]
        for case in gemini["cases"]
        if case["risk"] == "over_conversion_guard"
        or case["domain"] == "high_risk"
        or case["confidence"] in {"medium", "low"}
    )


def test_holdout_batch8_gemini_cli_advisory_is_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH8)
    gemini = load_json(GEMINI_BATCH8_ADVISORY)

    input_ids = {case["id"] for case in inputs["cases"]}
    batch8_ids = set(expansion["new_case_ids"])

    assert batch8_ids <= input_ids | load_all_removed_case_ids()
    assert gemini["review_stage"] == "independent_holdout_expected_review"
    assert gemini["reviewer"] == "gemini_cli"
    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["model_requested"] == "gemini-2.5-flash"
    assert gemini["model_observed"] == ["gemini-3.5-flash"]
    assert gemini["chunking"] == {
        "strategy": "single_batch",
        "domain_order": ["it", "ui", "llm", "formal", "social", "high_risk"],
    }
    assert gemini["source_expansion_report"] == (
        "docs/reports/holdout-input-pool-expansion-blind-v1-batch8-100-cases-2026-07-10.json"
    )
    assert "GEMINI_API_KEY" in gemini["policy"]
    assert gemini["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 60,
            "baseline_guard": 15,
            "over_conversion_guard": 25,
        },
        "by_confidence": {"high": 100},
        "review_needed": 0,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in gemini["cases"]} == batch8_ids
    assert all(case["gemini_expected"] for case in gemini["cases"])
    assert not any(case["promotion_allowed"] for case in gemini["cases"])


def test_holdout_batch7_diff_review_and_confirmation_are_not_ground_truth() -> None:
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH7)
    diff = load_json(CODEX_GEMINI_BATCH7_DIFF_REVIEW)
    packet = load_json(MAINTAINER_BATCH7_CONFIRMATION)

    batch7_ids = set(expansion["new_case_ids"])

    assert diff["review_stage"] == "codex_gemini_difference_review"
    assert diff["scope"] == "batch7_100_cases"
    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["source_codex_report"] == (
        "docs/reports/holdout-codex-first-pass-blind-v1-batch7-100-cases-2026-07-10.json"
    )
    assert diff["source_gemini_report"] == (
        "docs/reports/holdout-gemini-cli-advisory-blind-v1-batch7-100-cases-2026-07-10.json"
    )
    assert diff["summary"] == {
        "total_cases": 100,
        "exact_matches": 72,
        "differences": 28,
        "exact_but_policy_review": 37,
        "no_immediate_question": 35,
        "maintainer_queue_total": 65,
        "difference_recommendations": {
            "codex": 19,
            "gemini": 6,
            "third": 3,
        },
        "zhtw_current_status_for_differences": {
            "in_recommended_acceptable": 5,
            "matches_recommended": 8,
            "needs_followup_if_confirmed": 15,
        },
        "promotion_allowed": False,
    }
    difference_ids = {case["id"] for case in diff["differences"]}
    policy_ids = {case["id"] for case in diff["exact_but_policy_review"]}
    no_question_ids = {case["id"] for case in diff["no_immediate_question"]}
    assert difference_ids == {
        "blind-it-0139",
        "blind-it-0141",
        "blind-it-0142",
        "blind-it-0143",
        "blind-it-0145",
        "blind-it-0146",
        "blind-it-0147",
        "blind-it-0149",
        "blind-it-0150",
        "blind-it-0151",
        "blind-it-0152",
        "blind-it-0153",
        "blind-it-0154",
        "blind-it-0155",
        "blind-it-0156",
        "blind-it-0157",
        "blind-ui-0108",
        "blind-ui-0111",
        "blind-ui-0117",
        "blind-ui-0118",
        "blind-ui-0124",
        "blind-llm-0080",
        "blind-llm-0084",
        "blind-llm-0085",
        "blind-llm-0087",
        "blind-social-0080",
        "blind-high-risk-0053",
        "blind-high-risk-0057",
    }
    assert difference_ids | policy_ids | no_question_ids == batch7_ids
    assert len(policy_ids) == 37
    assert len(no_question_ids) == 35
    assert all(case["recommended_expected"] for case in diff["differences"])
    assert all("zhtw_current" in case for case in diff["differences"])

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch7_100_cases"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["source_diff_review"] == (
        "docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch7-100-cases-2026-07-10.json"
    )
    assert packet["summary"] == {
        "total_review_cases": 65,
        "difference_cases": 28,
        "policy_review_cases": 37,
        "no_immediate_question": 35,
        "difference_recommendations": {
            "codex": 19,
            "gemini": 6,
            "third": 3,
        },
        "by_domain": {
            "it": 19,
            "ui": 10,
            "llm": 10,
            "social": 9,
            "high_risk": 10,
            "formal": 7,
        },
        "by_risk": {
            "candidate_gap": 36,
            "baseline_guard": 4,
            "over_conversion_guard": 25,
        },
        "by_policy_reason": {
            "high-risk domain": 10,
            "over-conversion guard": 25,
            "Codex confidence medium": 20,
            "Gemini review-needed policy guard": 32,
        },
        "zhtw_current_status_for_differences": {
            "in_recommended_acceptable": 5,
            "matches_recommended": 8,
            "needs_followup_if_confirmed": 15,
        },
        "promotion_allowed": False,
    }
    assert len(packet["cases"]) == 65
    assert len(packet["no_immediate_question_case_ids"]) == 35
    assert {case["kind"] for case in packet["cases"]} == {
        "difference",
        "exact_but_policy_review",
    }
    assert {case["id"] for case in packet["cases"]} == difference_ids | policy_ids
    assert set(packet["no_immediate_question_case_ids"]) == no_question_ids
    assert all(case["recommended_expected"] for case in packet["cases"])
    assert all("zhtw_current" in case for case in packet["cases"])


def test_holdout_batch8_diff_review_and_confirmation_are_not_ground_truth() -> None:
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH8)
    diff = load_json(CODEX_GEMINI_BATCH8_DIFF_REVIEW)
    packet = load_json(MAINTAINER_BATCH8_CONFIRMATION)

    batch8_ids = set(expansion["new_case_ids"])

    assert diff["review_stage"] == "codex_gemini_difference_review"
    assert diff["scope"] == "batch8_100_cases"
    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["converter_outputs_used"] is False
    assert diff["source_codex_report"] == (
        "docs/reports/holdout-codex-first-pass-blind-v1-batch8-100-cases-2026-07-10.json"
    )
    assert diff["source_gemini_report"] == (
        "docs/reports/holdout-gemini-cli-advisory-blind-v1-batch8-100-cases-2026-07-10.json"
    )
    assert diff["summary"] == {
        "total_cases": 100,
        "exact_matches": 76,
        "differences": 24,
        "exact_but_policy_review": 42,
        "no_immediate_question": 34,
        "maintainer_queue_total": 66,
        "difference_recommendations": {
            "codex": 17,
            "gemini": 7,
        },
        "by_policy_reason": {
            "Codex confidence medium": 20,
            "Codex review-needed policy guard": 50,
            "high-risk domain": 10,
            "over-conversion guard": 25,
        },
        "promotion_allowed": False,
    }
    difference_ids = {case["id"] for case in diff["differences"]}
    policy_ids = {case["id"] for case in diff["exact_but_policy_review"]}
    no_question_ids = set(diff["no_immediate_question"])
    assert difference_ids | policy_ids | no_question_ids == batch8_ids
    assert len(difference_ids) == 24
    assert len(policy_ids) == 42
    assert len(no_question_ids) == 34
    assert "blind-social-0099" in difference_ids
    assert all(case["recommended_expected"] for case in diff["differences"])

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch8_100_cases"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["converter_outputs_used"] is False
    assert packet["source_diff_review"] == (
        "docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch8-100-cases-2026-07-10.json"
    )
    assert packet["summary"] == {
        "total_review_cases": 66,
        "difference_cases": 24,
        "policy_review_cases": 42,
        "no_immediate_question": 34,
        "difference_recommendations": {
            "codex": 17,
            "gemini": 7,
        },
        "by_domain": {
            "it": 18,
            "ui": 13,
            "llm": 11,
            "formal": 7,
            "social": 7,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 38,
            "baseline_guard": 3,
            "over_conversion_guard": 25,
        },
        "by_kind": {
            "difference": 24,
            "policy_review": 42,
        },
        "by_policy_reason": {
            "Codex confidence medium": 20,
            "Codex review-needed policy guard": 50,
            "high-risk domain": 10,
            "over-conversion guard": 25,
        },
        "promotion_allowed": False,
    }
    assert len(packet["cases"]) == 66
    assert len(packet["no_immediate_question_case_ids"]) == 34
    assert {case["kind"] for case in packet["cases"]} == {
        "difference",
        "policy_review",
    }
    assert {case["id"] for case in packet["cases"]} == difference_ids | policy_ids
    assert set(packet["no_immediate_question_case_ids"]) == no_question_ids
    assert all(case["recommended_expected"] for case in packet["cases"])
    social_0099 = next(case for case in packet["cases"] if case["id"] == "blind-social-0099")
    assert social_0099["recommendation"] == "codex"
    assert social_0099["recommended_acceptable"] == []


def test_holdout_batch9_codex_first_pass_is_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH9)
    codex = load_json(CODEX_BATCH9_FIRST_PASS)

    input_ids = {case["id"] for case in inputs["cases"]}
    batch9_ids = set(expansion["new_case_ids"])

    assert batch9_ids <= input_ids | load_all_removed_case_ids()
    assert codex["review_stage"] == "first_pass_advisory"
    assert codex["reviewer"] == "codex"
    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["source_expansion_report"] == (
        "docs/reports/holdout-input-pool-expansion-blind-v1-batch9-100-cases-2026-07-12.json"
    )
    assert codex["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 60,
            "baseline_guard": 15,
            "over_conversion_guard": 25,
        },
        "by_confidence": {"medium": 20, "high": 80},
        "review_needed": 50,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in codex["cases"]} == batch9_ids
    assert all(case["codex_expected"] for case in codex["cases"])
    assert not any(case["promotion_allowed"] for case in codex["cases"])
    assert sum(1 for case in codex["cases"] if case["review_needed"]) == 50


def test_holdout_batch9_gemini_cli_advisory_is_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH9)
    gemini = load_json(GEMINI_BATCH9_ADVISORY)

    input_ids = {case["id"] for case in inputs["cases"]}
    batch9_ids = set(expansion["new_case_ids"])

    assert batch9_ids <= input_ids | load_all_removed_case_ids()
    assert gemini["review_stage"] == "independent_holdout_expected_review"
    assert gemini["reviewer"] == "gemini_cli"
    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["model_requested"] == "gemini-2.5-flash"
    assert gemini["model_observed"] == ["gemini-3.5-flash"]
    assert gemini["chunking"] == {
        "strategy": "by_domain",
        "domain_order": ["it", "ui", "llm", "formal", "social", "high_risk"],
    }
    assert gemini["source_expansion_report"] == (
        "docs/reports/holdout-input-pool-expansion-blind-v1-batch9-100-cases-2026-07-12.json"
    )
    assert "GEMINI_API_KEY" in gemini["policy"]
    assert gemini["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 60,
            "baseline_guard": 15,
            "over_conversion_guard": 25,
        },
        "by_confidence": {"high": 100},
        "review_needed": 0,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in gemini["cases"]} == batch9_ids
    assert all(case["gemini_expected"] for case in gemini["cases"])
    assert not any(case["promotion_allowed"] for case in gemini["cases"])


def test_holdout_batch9_diff_review_and_confirmation_are_not_ground_truth() -> None:
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH9)
    diff = load_json(CODEX_GEMINI_BATCH9_DIFF_REVIEW)
    packet = load_json(MAINTAINER_BATCH9_CONFIRMATION)

    batch9_ids = set(expansion["new_case_ids"])

    assert diff["review_stage"] == "codex_gemini_difference_review"
    assert diff["scope"] == "batch9_100_cases"
    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["converter_outputs_used"] is False
    assert diff["source_codex_report"] == (
        "docs/reports/holdout-codex-first-pass-blind-v1-batch9-100-cases-2026-07-12.json"
    )
    assert diff["source_gemini_report"] == (
        "docs/reports/holdout-gemini-cli-advisory-blind-v1-batch9-100-cases-2026-07-12.json"
    )
    assert diff["summary"] == {
        "total_cases": 100,
        "exact_matches": 70,
        "differences": 30,
        "exact_but_policy_review": 39,
        "no_immediate_question": 31,
        "maintainer_queue_total": 69,
        "difference_recommendations": {
            "gemini": 7,
            "codex": 23,
        },
        "by_policy_reason": {
            "Codex confidence medium": 20,
            "Codex review-needed policy guard": 50,
            "over-conversion guard": 25,
            "high-risk domain": 10,
        },
        "promotion_allowed": False,
    }
    difference_ids = {case["id"] for case in diff["differences"]}
    policy_ids = {case["id"] for case in diff["exact_but_policy_review"]}
    no_question_ids = set(diff["no_immediate_question"])
    assert difference_ids | policy_ids | no_question_ids == batch9_ids
    assert len(difference_ids) == 30
    assert len(policy_ids) == 39
    assert len(no_question_ids) == 31
    assert all(case["recommended_expected"] for case in diff["differences"])

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch9_100_cases"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["converter_outputs_used"] is False
    assert packet["source_diff_review"] == (
        "docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch9-100-cases-2026-07-12.json"
    )
    assert packet["summary"] == {
        "total_review_cases": 69,
        "difference_cases": 30,
        "policy_review_cases": 39,
        "no_immediate_question": 31,
        "difference_recommendations": {
            "gemini": 7,
            "codex": 23,
        },
        "by_domain": {
            "it": 17,
            "ui": 12,
            "llm": 10,
            "social": 15,
            "formal": 5,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 39,
            "over_conversion_guard": 25,
            "baseline_guard": 5,
        },
        "by_kind": {
            "difference": 30,
            "policy_review": 39,
        },
        "by_policy_reason": {
            "Codex confidence medium": 20,
            "Codex review-needed policy guard": 50,
            "over-conversion guard": 25,
            "high-risk domain": 10,
        },
        "promotion_allowed": False,
    }
    assert len(packet["cases"]) == 69
    assert len(packet["no_immediate_question_case_ids"]) == 31
    assert {case["kind"] for case in packet["cases"]} == {
        "difference",
        "policy_review",
    }
    assert {case["id"] for case in packet["cases"]} == difference_ids | policy_ids
    assert set(packet["no_immediate_question_case_ids"]) == no_question_ids
    assert all(case["recommended_expected"] for case in packet["cases"])


def test_holdout_batch10_advisory_diff_and_confirmation_are_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expected = load_json(EXPECTED)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH10)
    codex = load_json(CODEX_BATCH10_FIRST_PASS)
    gemini = load_json(GEMINI_BATCH10_ADVISORY)
    diff = load_json(CODEX_GEMINI_BATCH10_DIFF_REVIEW)
    packet = load_json(MAINTAINER_BATCH10_CONFIRMATION)

    input_ids = {case["id"] for case in inputs["cases"]}
    expected_ids = {case["id"] for case in expected["cases"]}
    batch10_ids = set(expansion["new_case_ids"])

    removed_ids = load_all_removed_case_ids()
    assert batch10_ids <= input_ids | removed_ids
    assert batch10_ids <= expected_ids | removed_ids

    assert codex["review_stage"] == "first_pass_advisory"
    assert codex["reviewer"] == "codex"
    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["source_expansion_report"] == (
        "docs/reports/holdout-input-pool-expansion-blind-v1-batch10-100-cases-2026-07-12.json"
    )
    assert codex["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 60,
            "baseline_guard": 15,
            "over_conversion_guard": 25,
        },
        "by_confidence": {"medium": 26, "high": 74},
        "review_needed": 36,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in codex["cases"]} == batch10_ids
    assert all(case["codex_expected"] for case in codex["cases"])
    assert not any(case["promotion_allowed"] for case in codex["cases"])

    assert gemini["review_stage"] == "independent_holdout_expected_review"
    assert gemini["reviewer"] == "gemini_cli"
    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["model_requested"] == "gemini-2.5-flash"
    assert gemini["model_observed"] == ["gemini-3.5-flash"]
    assert gemini["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "by_confidence": {"high": 100},
        "quality_flags": 2,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in gemini["cases"]} == batch10_ids
    assert len(gemini["quality_flags"]) == 2
    assert all(case["gemini_expected"] for case in gemini["cases"])

    assert diff["review_stage"] == "codex_gemini_difference_review"
    assert diff["scope"] == "batch10_100_cases"
    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["summary"] == {
        "total_cases": 100,
        "exact_matches": 83,
        "differences": 17,
        "exact_but_policy_review": 27,
        "no_immediate_question": 56,
        "maintainer_queue_total": 44,
        "difference_recommendations": {
            "codex": 0,
            "gemini": 10,
            "manual": 7,
        },
        "gemini_quality_flags": 2,
        "promotion_allowed": False,
    }
    difference_ids = {case["id"] for case in diff["differences"]}
    policy_ids = {case["id"] for case in diff["exact_but_policy_review"]}
    no_question_ids = {case["id"] for case in diff["no_immediate_question"]}
    assert difference_ids | policy_ids | no_question_ids == batch10_ids

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch10_100_cases"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["summary"] == {
        "total_cases": 100,
        "review_queue_cases": 44,
        "differences": 17,
        "exact_but_policy_review": 27,
        "no_immediate_question": 56,
        "gemini_quality_flags": 2,
        "by_domain": {
            "it": 17,
            "ui": 8,
            "llm": 7,
            "formal": 1,
            "social": 1,
            "high_risk": 10,
        },
        "by_risk": {
            "candidate_gap": 32,
            "baseline_guard": 1,
            "over_conversion_guard": 11,
        },
        "promotion_allowed": False,
    }
    assert {case["id"] for case in packet["cases"]} == difference_ids | policy_ids
    assert set(packet["no_immediate_question_case_ids"]) == no_question_ids
    assert packet["policy"]["private_expected_not_modified"] is True


def test_holdout_batch11_advisory_diff_and_confirmation_are_not_ground_truth() -> None:
    inputs = load_json(INPUTS)
    expected = load_json(EXPECTED)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH11)
    codex = load_json(CODEX_BATCH11_FIRST_PASS)
    gemini = load_json(GEMINI_BATCH11_ADVISORY)
    diff = load_json(CODEX_GEMINI_BATCH11_DIFF_REVIEW)
    packet = load_json(MAINTAINER_BATCH11_CONFIRMATION)

    input_ids = {case["id"] for case in inputs["cases"]}
    expected_ids = {case["id"] for case in expected["cases"]}
    batch11_ids = set(expansion["new_case_ids"])
    removed_ids = set(load_json(SEALED_POOL_UPDATE_BATCH11_SEMANTIC_REAUDIT)["removed_case_ids"])
    assert batch11_ids <= input_ids | removed_ids
    assert batch11_ids <= expected_ids | removed_ids

    assert codex["review_stage"] == "first_pass_advisory"
    assert codex["reviewer"] == "codex"
    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["summary"]["total_cases"] == 100
    assert codex["summary"]["by_confidence"] == {"medium": 24, "high": 76}
    assert codex["summary"]["review_needed"] == 34
    assert {case["id"] for case in codex["cases"]} == batch11_ids

    assert gemini["review_stage"] == "independent_holdout_expected_review"
    assert gemini["reviewer"] == "gemini_cli"
    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["model_requested"] == "gemini-2.5-pro"
    assert gemini["model_observed"] == ["gemini-2.5-pro", "gemini-1.5-pro"]
    assert gemini["summary"] == {
        "total_cases": 100,
        "by_domain": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "by_confidence": {"high": 94, "medium": 6},
        "review_needed": 12,
        "quality_flags": 1,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in gemini["cases"]} == batch11_ids
    assert gemini["quality_flags"][0]["issue"] == ("self_reported_model_metadata_mismatch")

    assert diff["review_stage"] == "codex_gemini_difference_review"
    assert diff["scope"] == "batch11_100_cases"
    assert diff["ground_truth"] is False
    assert diff["promotion_allowed"] is False
    assert diff["summary"] == {
        "total_cases": 100,
        "exact_matches": 79,
        "differences": 21,
        "exact_but_policy_review": 29,
        "no_immediate_question": 50,
        "maintainer_queue_total": 50,
        "difference_recommendations": {
            "codex": 18,
            "gemini": 3,
            "manual": 0,
        },
        "gemini_quality_flags": 1,
        "promotion_allowed": False,
    }
    difference_ids = {case["id"] for case in diff["differences"]}
    policy_ids = {case["id"] for case in diff["exact_but_policy_review"]}
    no_question_ids = {case["id"] for case in diff["no_immediate_question"]}
    assert difference_ids | policy_ids | no_question_ids == batch11_ids
    assert not (difference_ids & policy_ids)
    assert not (difference_ids & no_question_ids)
    assert not (policy_ids & no_question_ids)

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch11_100_cases"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["summary"]["review_queue_cases"] == 50
    assert packet["summary"]["no_immediate_question"] == 50
    assert {case["id"] for case in packet["cases"]} == difference_ids | policy_ids
    assert set(packet["no_immediate_question_case_ids"]) == no_question_ids
    assert all(case["recommended_expected"] for case in packet["cases"])
    assert packet["policy"] == {
        "private_expected_not_modified": True,
        "maintainer_confirmation_required_before_expected_update": True,
        "codex_and_gemini_are_advisory_only": True,
        "approval_policy_after_confirmation": "single_human_with_ai_advisory",
    }


def test_holdout_batch11_final_decision_updates_private_expected() -> None:
    expected = load_json(EXPECTED)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH11)
    packet = load_json(MAINTAINER_BATCH11_CONFIRMATION)
    decision = load_json(MAINTAINER_BATCH11_FINAL_DECISION)
    batch11_ids = set(expansion["new_case_ids"])
    batch11_cases = [case for case in expected["cases"] if case["id"] in batch11_ids]

    assert decision["review_stage"] == "maintainer_final_decision_summary"
    assert decision["scope"] == "batch11_100_cases"
    assert decision["maintainer"] == "tim"
    assert decision["decision"] == "review_ok"
    assert decision["expected_values_included"] is False
    assert decision["private_expected_updated"] is True
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_sha256"] == (
        "bbf89dfa8db7774fdd9b8c078f97d18b9b3749f164d5f4e7cc109bb8ac0ab096"
    )
    assert decision["private_expected_sha256"] != private_expected_sha256()
    assert decision["source_inputs_sha256"] == (
        "e7018d35e078a53ff1c59e4a8281b787151fd11c158859ad882defc82b93aff9"
    )
    assert decision["source_inputs_sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert "cases" not in decision
    assert decision["summary"] == {
        "batch11_cases": 100,
        "total_private_expected_cases": 851,
        "status": "sealed_private",
        "approval_policy": "single_human_with_ai_advisory",
        "minimum_human_reviewers": 1,
        "ai_advisory_review_allowed": True,
        "private_expected_updated": True,
        "accepted_recommended_expected": 50,
        "accepted_exact_no_immediate_question": 50,
        "edited_cases": 2,
        "dropped_cases": 0,
        "acceptable_variants_added": 0,
        "by_expected_source_for_batch11": {
            "human_adjudication": 23,
            "human_first_pass": 77,
        },
        "by_disagreement_for_batch11": {"true": 21, "false": 79},
        "by_expected_source_total": {
            "human_first_pass": 680,
            "human_adjudication": 171,
        },
        "by_disagreement_total": {"false": 682, "true": 169},
        "by_domain_for_batch11": {
            "it": 25,
            "ui": 20,
            "llm": 15,
            "formal": 15,
            "social": 15,
            "high_risk": 10,
        },
        "by_risk_for_batch11": {
            "candidate_gap": 60,
            "baseline_guard": 15,
            "over_conversion_guard": 25,
        },
    }
    removed_ids = set(load_json(SEALED_POOL_UPDATE_BATCH11_SEMANTIC_REAUDIT)["removed_case_ids"])
    assert len(batch11_cases) == 90
    assert {case["id"] for case in batch11_cases} == batch11_ids - removed_ids
    assert decision["confirmed_case_ids"] == {
        "review_packet": [case["id"] for case in packet["cases"]],
        "no_immediate_question": packet["no_immediate_question_case_ids"],
    }


def test_holdout_batch7_final_decision_omits_expected_values() -> None:
    packet = load_json(MAINTAINER_BATCH7_CONFIRMATION)
    decision = load_json(MAINTAINER_BATCH7_FINAL_DECISION)

    assert decision["review_stage"] == "maintainer_final_decision_summary"
    assert decision["scope"] == "batch7_100_cases"
    assert decision["expected_values_included"] is False
    assert decision["private_expected_updated"] is True
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_sha256"] == (
        "1e4e516efc1685ec9c3158ac3a467df3fa8bc66d988dcd34a43d8a6012d09ff5"
    )
    assert decision["private_expected_sha256"] != private_expected_sha256()
    assert "cases" not in decision
    assert decision["source_confirmation_packet"] == (
        "docs/reports/holdout-maintainer-confirmation-blind-v1-batch7-100-cases-2026-07-10.json"
    )
    assert decision["summary"] == {
        "batch7_cases": 100,
        "total_private_expected_cases": 515,
        "status": "sealed_private",
        "approval_policy": "single_human_with_ai_advisory",
        "minimum_human_reviewers": 1,
        "ai_advisory_review_allowed": True,
        "private_expected_updated": True,
        "accepted_recommended_expected": 65,
        "accepted_exact_no_immediate_question": 35,
        "edited_cases": 0,
        "dropped_cases": 0,
        "by_expected_source_for_batch7": {
            "human_adjudication": 28,
            "human_first_pass": 72,
        },
        "by_disagreement_for_batch7": {
            "false": 72,
            "true": 28,
        },
        "by_expected_source_total": {
            "human_adjudication": 105,
            "human_first_pass": 410,
        },
        "by_disagreement_total": {
            "false": 410,
            "true": 105,
        },
        "by_domain_for_batch7": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "by_risk_for_batch7": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
    }
    assert decision["confirmed_case_ids"] == {
        "review_packet": [case["id"] for case in packet["cases"]],
        "no_immediate_question": packet["no_immediate_question_case_ids"],
    }


def test_holdout_batch8_final_decision_omits_expected_values() -> None:
    packet = load_json(MAINTAINER_BATCH8_CONFIRMATION)
    decision = load_json(MAINTAINER_BATCH8_FINAL_DECISION)

    assert decision["review_stage"] == "maintainer_final_decision_summary"
    assert decision["scope"] == "batch8_100_cases"
    assert decision["expected_values_included"] is False
    assert decision["private_expected_updated"] is True
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_sha256"] == (
        "7c78a99becbf120ddae840a56e90334cc4df7f36f1d8b62944058b94e66f6025"
    )
    assert decision["private_expected_sha256"] != private_expected_sha256()
    assert "cases" not in decision
    assert decision["source_confirmation_packet"] == (
        "docs/reports/holdout-maintainer-confirmation-blind-v1-batch8-100-cases-2026-07-10.json"
    )
    assert decision["source_reports"] == [
        "docs/reports/holdout-codex-first-pass-blind-v1-batch8-100-cases-2026-07-10.json",
        "docs/reports/holdout-gemini-cli-advisory-blind-v1-batch8-100-cases-2026-07-10.json",
        "docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch8-100-cases-2026-07-10.json",
        "docs/reports/holdout-maintainer-confirmation-blind-v1-batch8-100-cases-2026-07-10.json",
    ]
    assert decision["summary"] == {
        "batch8_cases": 100,
        "total_private_expected_cases": 598,
        "status": "sealed_private",
        "approval_policy": "single_human_with_ai_advisory",
        "minimum_human_reviewers": 1,
        "ai_advisory_review_allowed": True,
        "private_expected_updated": True,
        "accepted_recommended_expected": 66,
        "accepted_exact_no_immediate_question": 34,
        "edited_cases": 0,
        "dropped_cases": 0,
        "by_expected_source_for_batch8": {
            "human_adjudication": 24,
            "human_first_pass": 76,
        },
        "by_disagreement_for_batch8": {
            "false": 76,
            "true": 24,
        },
        "by_expected_source_total": {
            "human_adjudication": 120,
            "human_first_pass": 478,
        },
        "by_disagreement_total": {
            "false": 478,
            "true": 120,
        },
        "by_domain_for_batch8": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "by_risk_for_batch8": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
    }
    assert decision["confirmed_case_ids"] == {
        "review_packet": [case["id"] for case in packet["cases"]],
        "no_immediate_question": packet["no_immediate_question_case_ids"],
    }


def test_holdout_batch9_final_decision_omits_expected_values() -> None:
    packet = load_json(MAINTAINER_BATCH9_CONFIRMATION)
    decision = load_json(MAINTAINER_BATCH9_FINAL_DECISION)

    assert decision["review_stage"] == "maintainer_final_decision_summary"
    assert decision["scope"] == "batch9_100_cases"
    assert decision["expected_values_included"] is False
    assert decision["private_expected_updated"] is True
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_sha256"] == (
        "2c67fe35f756fc406577b042f9c05380bb635426b1c253a3385fa8c3c5224d41"
    )
    assert decision["private_expected_sha256"] != private_expected_sha256()
    assert decision["source_inputs_sha256"] == (
        "0ac742ac9885cdae198bed6fc376c2fb5c3e991573ae4cb4ac2072cfef3e937d"
    )
    assert decision["source_inputs_sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert "cases" not in decision
    assert decision["source_confirmation_packet"] == (
        "docs/reports/holdout-maintainer-confirmation-blind-v1-batch9-100-cases-2026-07-12.json"
    )
    assert decision["source_reports"] == [
        "docs/reports/holdout-codex-first-pass-blind-v1-batch9-100-cases-2026-07-12.json",
        "docs/reports/holdout-gemini-cli-advisory-blind-v1-batch9-100-cases-2026-07-12.json",
        "docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch9-100-cases-2026-07-12.json",
        "docs/reports/holdout-maintainer-confirmation-blind-v1-batch9-100-cases-2026-07-12.json",
    ]
    assert decision["summary"] == {
        "batch9_cases": 100,
        "total_private_expected_cases": 683,
        "status": "sealed_private",
        "approval_policy": "single_human_with_ai_advisory",
        "minimum_human_reviewers": 1,
        "ai_advisory_review_allowed": True,
        "private_expected_updated": True,
        "accepted_recommended_expected": 69,
        "accepted_exact_no_immediate_question": 31,
        "edited_cases": 0,
        "dropped_cases": 0,
        "by_expected_source_for_batch9": {
            "human_adjudication": 30,
            "human_first_pass": 70,
        },
        "by_disagreement_for_batch9": {
            "false": 70,
            "true": 30,
        },
        "by_expected_source_total": {
            "human_adjudication": 140,
            "human_first_pass": 543,
        },
        "by_disagreement_total": {
            "false": 543,
            "true": 140,
        },
        "by_domain_for_batch9": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "by_risk_for_batch9": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
    }
    assert decision["confirmed_case_ids"] == {
        "review_packet": [case["id"] for case in packet["cases"]],
        "no_immediate_question": packet["no_immediate_question_case_ids"],
    }


def test_holdout_batch10_final_decision_omits_expected_values() -> None:
    packet = load_json(MAINTAINER_BATCH10_CONFIRMATION)
    decision = load_json(MAINTAINER_BATCH10_FINAL_DECISION)

    assert decision["review_stage"] == "maintainer_final_decision_summary"
    assert decision["scope"] == "batch10_100_cases"
    assert decision["expected_values_included"] is False
    assert decision["private_expected_updated"] is True
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_sha256"] == (
        "b8150c2e41e2bc574de54a730fe1a0c1c1edf39a9efce344ef1bbbd267179250"
    )
    assert decision["private_expected_sha256"] != private_expected_sha256()
    assert decision["private_expected_sha256_before"] == (
        "0e41c9ac8c130075d66f23daeeb80afd6e69903319ea473e9ac5e7ed38d5f7ab"
    )
    assert decision["source_inputs_sha256"] == (
        "eff19da4ff198981bdb0018bceabb128b1aa5a33e9199ea5421f69561da340d0"
    )
    assert decision["source_inputs_sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert "cases" not in decision
    assert decision["source_confirmation_packet"] == (
        "docs/reports/holdout-maintainer-confirmation-blind-v1-batch10-100-cases-2026-07-12.json"
    )
    assert decision["source_reports"] == [
        "docs/reports/holdout-codex-first-pass-blind-v1-batch10-100-cases-2026-07-12.json",
        "docs/reports/holdout-gemini-cli-advisory-blind-v1-batch10-100-cases-2026-07-12.json",
        "docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch10-100-cases-2026-07-12.json",
        "docs/reports/holdout-maintainer-confirmation-blind-v1-batch10-100-cases-2026-07-12.json",
    ]
    assert decision["summary"] == {
        "batch10_cases": 100,
        "total_private_expected_cases": 767,
        "status": "sealed_private",
        "approval_policy": "single_human_with_ai_advisory",
        "minimum_human_reviewers": 1,
        "ai_advisory_review_allowed": True,
        "private_expected_updated": True,
        "accepted_recommended_expected": 44,
        "accepted_exact_no_immediate_question": 56,
        "edited_cases": 0,
        "dropped_cases": 0,
        "by_expected_source_for_batch10": {
            "human_adjudication": 17,
            "human_first_pass": 83,
        },
        "by_disagreement_for_batch10": {
            "false": 83,
            "true": 17,
        },
        "by_expected_source_total": {
            "human_adjudication": 151,
            "human_first_pass": 616,
        },
        "by_disagreement_total": {
            "false": 616,
            "true": 151,
        },
        "by_domain_for_batch10": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "by_risk_for_batch10": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
    }
    assert decision["confirmed_case_ids"] == {
        "review_packet": [case["id"] for case in packet["cases"]],
        "no_immediate_question": packet["no_immediate_question_case_ids"],
    }


def test_holdout_batch4_final_decision_omits_expected_values() -> None:
    packet = load_json(MAINTAINER_BATCH4_CONFIRMATION)
    decision = load_json(MAINTAINER_BATCH4_FINAL_DECISION)

    assert decision["review_stage"] == "maintainer_final_decision_summary"
    assert decision["scope"] == "batch4_100_cases"
    assert decision["expected_values_included"] is False
    assert decision["private_expected_updated"] is True
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert len(decision["private_expected_sha256"]) == 64
    assert "cases" not in decision
    assert decision["source_confirmation_packet"] == (
        "docs/reports/holdout-maintainer-confirmation-blind-v1-batch4-100-cases-2026-07-09.json"
    )
    assert decision["summary"] == {
        "batch4_cases": 100,
        "total_private_expected_cases": 261,
        "status": "sealed_private",
        "approval_policy": "single_human_with_ai_advisory",
        "minimum_human_reviewers": 1,
        "ai_advisory_review_allowed": True,
        "private_expected_updated": True,
        "accepted_recommended_expected": 64,
        "accepted_exact_no_immediate_question": 36,
        "edited_cases": 0,
        "dropped_cases": 0,
        "by_expected_source_for_batch4": {
            "human_adjudication": 26,
            "human_first_pass": 74,
        },
        "by_disagreement_for_batch4": {
            "false": 74,
            "true": 26,
        },
        "by_expected_source_total": {
            "human_adjudication": 68,
            "human_first_pass": 193,
        },
        "by_disagreement_total": {
            "false": 193,
            "true": 68,
        },
        "by_domain_for_batch4": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "by_risk_for_batch4": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
    }
    assert decision["confirmed_case_ids"] == {
        "review_packet": [case["id"] for case in packet["cases"]],
        "no_immediate_question": packet["no_immediate_question_case_ids"],
    }


def test_holdout_batch5_final_decision_omits_expected_values() -> None:
    packet = load_json(MAINTAINER_BATCH5_CONFIRMATION)
    decision = load_json(MAINTAINER_BATCH5_FINAL_DECISION)

    assert decision["review_stage"] == "maintainer_final_decision_summary"
    assert decision["scope"] == "batch5_100_cases"
    assert decision["expected_values_included"] is False
    assert decision["private_expected_updated"] is True
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert len(decision["private_expected_sha256"]) == 64
    assert "cases" not in decision
    assert decision["source_confirmation_packet"] == (
        "docs/reports/holdout-maintainer-confirmation-blind-v1-batch5-100-cases-2026-07-09.json"
    )
    assert decision["summary"] == {
        "batch5_cases": 100,
        "total_private_expected_cases": 338,
        "status": "sealed_private",
        "approval_policy": "single_human_with_ai_advisory",
        "minimum_human_reviewers": 1,
        "ai_advisory_review_allowed": True,
        "private_expected_updated": True,
        "accepted_recommended_expected": 50,
        "accepted_exact_no_immediate_question": 50,
        "edited_cases": 0,
        "dropped_cases": 0,
        "by_expected_source_for_batch5": {
            "human_adjudication": 8,
            "human_first_pass": 92,
        },
        "by_disagreement_for_batch5": {
            "false": 92,
            "true": 8,
        },
        "by_expected_source_total": {
            "human_adjudication": 65,
            "human_first_pass": 273,
        },
        "by_disagreement_total": {
            "false": 273,
            "true": 65,
        },
        "by_domain_for_batch5": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "by_risk_for_batch5": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
    }
    assert decision["confirmed_case_ids"] == {
        "review_packet": [case["id"] for case in packet["cases"]],
        "no_immediate_question": packet["no_immediate_question_case_ids"],
    }


def test_holdout_batch6_final_decision_omits_expected_values() -> None:
    packet = load_json(MAINTAINER_BATCH6_CONFIRMATION)
    decision = load_json(MAINTAINER_BATCH6_FINAL_DECISION)

    assert decision["review_stage"] == "maintainer_final_decision_summary"
    assert decision["scope"] == "batch6_100_cases"
    assert decision["expected_values_included"] is False
    assert decision["private_expected_updated"] is True
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert len(decision["private_expected_sha256"]) == 64
    assert "cases" not in decision
    assert decision["source_confirmation_packet"] == (
        "docs/reports/holdout-maintainer-confirmation-blind-v1-batch6-100-cases-2026-07-10.json"
    )
    assert decision["summary"] == {
        "batch6_cases": 100,
        "total_private_expected_cases": 426,
        "status": "sealed_private",
        "approval_policy": "single_human_with_ai_advisory",
        "minimum_human_reviewers": 1,
        "ai_advisory_review_allowed": True,
        "private_expected_updated": True,
        "accepted_recommended_expected": 76,
        "accepted_exact_no_immediate_question": 24,
        "edited_cases": 0,
        "dropped_cases": 0,
        "by_expected_source_for_batch6": {
            "human_adjudication": 20,
            "human_first_pass": 80,
        },
        "by_disagreement_for_batch6": {
            "false": 80,
            "true": 20,
        },
        "by_expected_source_total": {
            "human_adjudication": 84,
            "human_first_pass": 342,
        },
        "by_disagreement_total": {
            "false": 342,
            "true": 84,
        },
        "by_domain_for_batch6": {
            "formal": 15,
            "high_risk": 10,
            "it": 25,
            "llm": 15,
            "social": 15,
            "ui": 20,
        },
        "by_risk_for_batch6": {
            "baseline_guard": 15,
            "candidate_gap": 60,
            "over_conversion_guard": 25,
        },
    }
    assert decision["confirmed_case_ids"] == {
        "review_packet": [case["id"] for case in packet["cases"]],
        "no_immediate_question": packet["no_immediate_question_case_ids"],
    }


def test_private_expected_covers_current_pool_after_batch13_review() -> None:
    inputs = load_json(INPUTS)
    expected = load_json(EXPECTED)
    expansion = load_json(INPUT_POOL_EXPANSION_BATCH5)
    batch6 = load_json(INPUT_POOL_EXPANSION_BATCH6)
    batch7 = load_json(INPUT_POOL_EXPANSION_BATCH7)
    batch8 = load_json(INPUT_POOL_EXPANSION_BATCH8)
    batch9 = load_json(INPUT_POOL_EXPANSION_BATCH9)
    batch10 = load_json(INPUT_POOL_EXPANSION_BATCH10)
    batch11 = load_json(INPUT_POOL_EXPANSION_BATCH11)
    batch12 = load_json(INPUT_POOL_EXPANSION_BATCH12)
    batch13 = load_json(INPUT_POOL_EXPANSION_BATCH13)
    batch7_miss_review = load_json(SEALED_POOL_UPDATE_BATCH7_MISS_REVIEW)
    batch8_miss_review = load_json(SEALED_POOL_UPDATE_BATCH8_MISS_REVIEW)
    batch9_miss_review = load_json(SEALED_POOL_UPDATE_BATCH9_MISS_REVIEW)
    batch10_miss_review = load_json(SEALED_POOL_UPDATE_BATCH10_MISS_REVIEW)
    batch5_ids = set(expansion["new_case_ids"])
    batch6_ids = set(batch6["new_case_ids"])
    batch7_ids = set(batch7["new_case_ids"])
    batch8_ids = set(batch8["new_case_ids"])
    batch9_ids = set(batch9["new_case_ids"])
    batch10_ids = set(batch10["new_case_ids"])
    batch11_ids = set(batch11["new_case_ids"])
    batch12_ids = set(batch12["new_case_ids"])
    batch13_ids = set(batch13["new_case_ids"])
    input_ids = [case["id"] for case in inputs["cases"]]
    expected_ids = [case["id"] for case in expected["cases"]]
    batch7_removed_ids = set(batch7_miss_review["removed_case_ids"])
    batch8_removed_ids = set(batch8_miss_review["removed_case_ids"])
    batch9_removed_ids = set(batch9_miss_review["removed_case_ids"])
    batch10_removed_ids = set(batch10_miss_review["removed_case_ids"])

    semantic_removed_ids = set(
        load_json(SEALED_POOL_UPDATE_BATCH11_SEMANTIC_REAUDIT)["removed_case_ids"]
    )
    batch12_removed_ids = set(load_json(SEALED_POOL_UPDATE_BATCH12_MISS_REVIEW)["removed_case_ids"])
    batch13_removed_ids = set(load_json(SEALED_POOL_UPDATE_BATCH13_MISS_REVIEW)["removed_case_ids"])
    assert len(input_ids) == 1008
    assert len(expected_ids) == 1008
    assert set(expected_ids) == set(input_ids)
    assert batch13_ids - batch13_removed_ids <= set(input_ids)
    assert batch13_ids - batch13_removed_ids <= set(expected_ids)
    assert not (batch13_removed_ids & set(input_ids))
    assert not (batch13_removed_ids & set(expected_ids))
    assert batch12_ids - batch12_removed_ids <= set(expected_ids)
    assert batch12_ids - batch12_removed_ids <= set(input_ids)
    assert not (batch12_removed_ids & set(input_ids))
    assert not (batch12_removed_ids & set(expected_ids))
    assert batch11_ids - semantic_removed_ids <= set(input_ids)
    assert batch11_ids - semantic_removed_ids <= set(expected_ids)
    assert not (semantic_removed_ids & set(input_ids))
    assert not (semantic_removed_ids & set(expected_ids))
    assert batch10_ids - batch10_removed_ids <= set(expected_ids)
    assert batch10_ids - batch10_removed_ids <= set(input_ids)
    assert batch9_ids - batch9_removed_ids <= set(expected_ids)
    assert batch9_ids - batch9_removed_ids <= set(input_ids)
    assert not (set(input_ids) & batch8_removed_ids)
    assert not (set(expected_ids) & batch8_removed_ids)
    assert not (set(input_ids) & batch9_removed_ids)
    assert not (set(expected_ids) & batch9_removed_ids)
    assert not (set(input_ids) & batch10_removed_ids)
    assert not (set(expected_ids) & batch10_removed_ids)
    assert expected["status"] == "sealed_private"
    assert expected["source_inputs"] == "benchmarks/accuracy/blind-v1.inputs.json"
    assert expected["source_inputs_sha256"] == hashlib.sha256(INPUTS.read_bytes()).hexdigest()

    batch5_cases = [case for case in expected["cases"] if case["id"] in batch5_ids]
    assert len(batch5_cases) == 88
    assert Counter(case["annotation"]["expected_source"] for case in batch5_cases) == {
        "human_first_pass": 81,
        "human_adjudication": 7,
    }
    assert Counter(str(case["annotation"]["disagreement"]).lower() for case in batch5_cases) == {
        "false": 81,
        "true": 7,
    }
    assert all(
        case["annotation"]["ai_advisory_reviewers"] == ["codex", "gemini_cli"]
        for case in batch5_cases
    )
    assert all(
        "docs/reports/holdout-maintainer-final-decision-blind-v1-batch5-100-cases-2026-07-09.json"
        in case["annotation"]["source_reports"]
        for case in batch5_cases
    )

    batch6_cases = [case for case in expected["cases"] if case["id"] in batch6_ids]
    assert len(batch6_cases) == 89
    assert Counter(case["annotation"]["expected_source"] for case in batch6_cases) == {
        "human_first_pass": 76,
        "human_adjudication": 13,
    }
    assert Counter(str(case["annotation"]["disagreement"]).lower() for case in batch6_cases) == {
        "false": 76,
        "true": 13,
    }
    assert all(
        case["annotation"]["ai_advisory_reviewers"] == ["codex", "gemini_cli"]
        for case in batch6_cases
    )
    assert all(
        "docs/reports/holdout-maintainer-final-decision-blind-v1-batch6-100-cases-2026-07-10.json"
        in case["annotation"]["source_reports"]
        for case in batch6_cases
    )

    batch7_cases = [case for case in expected["cases"] if case["id"] in batch7_ids]
    assert len(batch7_cases) == 83
    assert not (set(expected_ids) & batch7_removed_ids)
    assert Counter(case["annotation"]["expected_source"] for case in batch7_cases) == {
        "human_first_pass": 64,
        "human_adjudication": 19,
    }
    assert Counter(str(case["annotation"]["disagreement"]).lower() for case in batch7_cases) == {
        "false": 64,
        "true": 19,
    }
    assert all(
        case["annotation"]["ai_advisory_reviewers"] == ["codex", "gemini_cli"]
        for case in batch7_cases
    )
    acceptable_variant_ids = {
        "blind-it-0146",
        "blind-it-0147",
        "blind-it-0148",
        "blind-it-0157",
        "blind-ui-0108",
        "blind-ui-0110",
        "blind-ui-0118",
    }
    acceptable_variant_cases = [
        case for case in batch7_cases if case["id"] in acceptable_variant_ids
    ]
    assert len(acceptable_variant_cases) == 7
    assert all(
        "docs/reports/holdout-maintainer-final-decision-batch7-miss-classification-blind-v1-2026-07-10.json"
        in case["annotation"]["source_reports"]
        for case in acceptable_variant_cases
    )
    assert all(
        "docs/reports/holdout-maintainer-final-decision-blind-v1-batch7-100-cases-2026-07-10.json"
        in case["annotation"]["source_reports"]
        for case in batch7_cases
    )

    batch8_cases = [case for case in expected["cases"] if case["id"] in batch8_ids]
    assert len(batch8_cases) == 85
    assert Counter(case["annotation"]["expected_source"] for case in batch8_cases) == {
        "human_first_pass": 71,
        "human_adjudication": 14,
    }
    assert Counter(str(case["annotation"]["disagreement"]).lower() for case in batch8_cases) == {
        "false": 71,
        "true": 14,
    }
    assert all(
        case["annotation"]["first_reviewer"] == "tim"
        and case["annotation"]["second_reviewer"] == ""
        and case["annotation"]["ai_advisory_reviewers"] == ["codex", "gemini_cli"]
        for case in batch8_cases
    )
    assert all(
        "docs/reports/holdout-maintainer-final-decision-blind-v1-batch8-100-cases-2026-07-10.json"
        in case["annotation"]["source_reports"]
        for case in batch8_cases
    )
    batch8_acceptable_variant_ids = {
        "blind-it-0167",
        "blind-it-0175",
        "blind-llm-0097",
        "blind-social-0095",
    }
    batch8_acceptable_variant_cases = [
        case for case in batch8_cases if case["id"] in batch8_acceptable_variant_ids
    ]
    assert len(batch8_acceptable_variant_cases) == 4
    assert all(
        "docs/reports/holdout-maintainer-final-decision-batch8-miss-classification-blind-v1-2026-07-11.json"
        in case["annotation"]["source_reports"]
        for case in batch8_acceptable_variant_cases
    )
    assert all("regional_term" in case["issue_tags"] for case in batch8_cases)
    social_0099 = next(case for case in batch8_cases if case["id"] == "blind-social-0099")
    assert social_0099["expected"] == "可以幫我確認外送到了沒？"
    assert social_0099["acceptable"] == []

    batch9_cases = [case for case in expected["cases"] if case["id"] in batch9_ids]
    assert len(batch9_cases) == 84
    assert Counter(case["annotation"]["expected_source"] for case in batch9_cases) == {
        "human_first_pass": 60,
        "human_adjudication": 24,
    }
    assert Counter(str(case["annotation"]["disagreement"]).lower() for case in batch9_cases) == {
        "false": 60,
        "true": 24,
    }
    assert all(
        case["annotation"]["first_reviewer"] == "tim"
        and case["annotation"]["second_reviewer"] == ""
        and case["annotation"]["ai_advisory_reviewers"] == ["codex", "gemini_cli"]
        for case in batch9_cases
    )
    assert all(
        "docs/reports/holdout-maintainer-final-decision-blind-v1-batch9-100-cases-2026-07-12.json"
        in case["annotation"]["source_reports"]
        for case in batch9_cases
    )
    batch9_acceptable_variant_ids = {
        "blind-it-0189",
        "blind-it-0197",
        "blind-it-0202",
        "blind-it-0206",
        "blind-ui-0148",
        "blind-ui-0166",
    }
    batch9_acceptable_variant_cases = [
        case for case in batch9_cases if case["id"] in batch9_acceptable_variant_ids
    ]
    assert len(batch9_acceptable_variant_cases) == 6
    assert all(
        "docs/reports/holdout-maintainer-final-decision-batch9-miss-classification-blind-v1-2026-07-12.json"
        in case["annotation"]["source_reports"]
        for case in batch9_acceptable_variant_cases
    )
    assert all("regional_term" in case["issue_tags"] for case in batch9_cases)

    batch10_cases = [case for case in expected["cases"] if case["id"] in batch10_ids]
    assert len(batch10_cases) == 84
    assert Counter(case["annotation"]["expected_source"] for case in batch10_cases) == {
        "human_first_pass": 70,
        "human_adjudication": 14,
    }
    assert Counter(str(case["annotation"]["disagreement"]).lower() for case in batch10_cases) == {
        "false": 70,
        "true": 14,
    }
    assert all(
        case["annotation"]["first_reviewer"] == "tim"
        and case["annotation"]["second_reviewer"] == ""
        and case["annotation"]["ai_advisory_reviewers"] == ["codex", "gemini_cli"]
        for case in batch10_cases
    )
    assert all(
        "docs/reports/holdout-maintainer-final-decision-blind-v1-batch10-100-cases-2026-07-12.json"
        in case["annotation"]["source_reports"]
        for case in batch10_cases
    )
    batch10_acceptable_variant_ids = {
        "blind-it-0222",
        "blind-it-0232",
        "blind-llm-0123",
        "blind-llm-0137",
    }
    batch10_acceptable_variant_cases = [
        case for case in batch10_cases if case["id"] in batch10_acceptable_variant_ids
    ]
    assert len(batch10_acceptable_variant_cases) == 4
    assert all(
        "docs/reports/holdout-maintainer-final-decision-batch10-miss-classification-blind-v1-2026-07-13.json"
        in case["annotation"]["source_reports"]
        for case in batch10_acceptable_variant_cases
    )
    assert all("regional_term" in case["issue_tags"] for case in batch10_cases)


def test_holdout_expansion_differences_confirmation_packet_is_not_ground_truth() -> None:
    diff = load_json(CODEX_GEMINI_EXPANSION_DIFF_REVIEW)
    packet = load_json(MAINTAINER_EXPANSION_DIFFERENCES_CONFIRMATION)

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "expansion_differences_only"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["source_diff_review"] == (
        "docs/reports/holdout-codex-gemini-diff-review-blind-v1-expansion-127-cases-2026-07-09.json"
    )
    assert packet["summary"] == {
        "total_review_cases": 48,
        "difference_cases": 48,
        "policy_review_cases": 0,
        "deferred_policy_review_cases": 33,
        "no_immediate_question": 46,
        "difference_recommendations": {
            "codex": 39,
            "gemini": 7,
            "third_value": 2,
        },
        "promotion_allowed": False,
    }
    assert len(packet["cases"]) == 48
    assert {case["id"] for case in packet["cases"]} == {case["id"] for case in diff["differences"]}
    assert packet["deferred_policy_review_case_ids"] == [
        case["id"] for case in diff["exact_but_policy_review"]
    ]
    assert packet["no_immediate_question_case_ids"] == [
        case["id"] for case in diff["no_immediate_question"]
    ]
    assert {case["kind"] for case in packet["cases"]} == {"difference"}
    assert {case["maintainer_action"] for case in packet["cases"]} == {"confirm_or_edit"}
    assert all(case["recommended_expected"] for case in packet["cases"])


def test_holdout_expansion_differences_final_decision_omits_expected_values() -> None:
    packet = load_json(MAINTAINER_EXPANSION_DIFFERENCES_CONFIRMATION)
    decision = load_json(MAINTAINER_EXPANSION_DIFFERENCES_FINAL_DECISION)

    assert decision["review_stage"] == "maintainer_partial_final_decision_summary"
    assert decision["scope"] == "expansion_differences_only"
    assert decision["expected_values_included"] is False
    assert decision["private_expected_updated"] is False
    assert "cases" not in decision
    assert decision["source_confirmation_packet"] == (
        "docs/reports/"
        "holdout-maintainer-confirmation-blind-v1-expansion-differences-2026-07-09.json"
    )
    assert decision["summary"] == {
        "total_confirmed_cases": 48,
        "accepted_recommended_expected": 48,
        "edited_cases": 0,
        "dropped_cases": 0,
        "deferred_policy_review_cases": 33,
        "no_immediate_question_cases": 46,
        "private_expected_updated": False,
        "private_expected_update_blocker": (
            "Partial expansion decision only; current blind-v1.inputs.json has 200 cases "
            "and run_accuracy_benchmark requires expected ids and source_inputs_sha256 "
            "to match the full input file."
        ),
        "would_be_expected_source": {"human_adjudication": 48},
        "by_recommendation": {
            "codex": 39,
            "gemini": 7,
            "third_value": 2,
        },
        "by_domain": {
            "formal": 2,
            "high_risk": 2,
            "it": 27,
            "llm": 8,
            "social": 5,
            "ui": 4,
        },
        "by_risk": {
            "baseline_guard": 2,
            "candidate_gap": 31,
            "over_conversion_guard": 15,
        },
    }
    assert decision["confirmed_case_ids"] == [case["id"] for case in packet["cases"]]


def test_holdout_expansion_policy_review_confirmation_packet_is_not_ground_truth() -> None:
    diff = load_json(CODEX_GEMINI_EXPANSION_DIFF_REVIEW)
    packet = load_json(MAINTAINER_EXPANSION_POLICY_REVIEW_CONFIRMATION)

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "expansion_policy_review_only"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["source_diff_review"] == (
        "docs/reports/holdout-codex-gemini-diff-review-blind-v1-expansion-127-cases-2026-07-09.json"
    )
    assert packet["summary"] == {
        "total_review_cases": 33,
        "difference_cases": 0,
        "policy_review_cases": 33,
        "no_immediate_question": 46,
        "recommendation": {"codex_gemini_match": 33},
        "by_domain": {
            "formal": 4,
            "high_risk": 8,
            "it": 3,
            "llm": 4,
            "social": 5,
            "ui": 9,
        },
        "by_risk": {
            "baseline_guard": 3,
            "candidate_gap": 14,
            "over_conversion_guard": 16,
        },
        "by_policy_reason": {
            "Codex confidence medium": 11,
            "high-risk domain": 4,
            "high-risk domain, Codex confidence medium": 2,
            "high-risk domain, over-conversion guard": 2,
            "over-conversion guard": 14,
        },
        "promotion_allowed": False,
    }
    assert len(packet["cases"]) == 33
    assert {case["id"] for case in packet["cases"]} == {
        case["id"] for case in diff["exact_but_policy_review"]
    }
    assert packet["no_immediate_question_case_ids"] == [
        case["id"] for case in diff["no_immediate_question"]
    ]
    assert {case["kind"] for case in packet["cases"]} == {"exact_but_policy_review"}
    assert {case["recommendation"] for case in packet["cases"]} == {"codex_gemini_match"}
    assert {case["maintainer_action"] for case in packet["cases"]} == {"confirm_or_edit"}
    assert all(case["recommended_expected"] for case in packet["cases"])


def test_holdout_expansion_policy_review_final_decision_omits_expected_values() -> None:
    packet = load_json(MAINTAINER_EXPANSION_POLICY_REVIEW_CONFIRMATION)
    decision = load_json(MAINTAINER_EXPANSION_POLICY_REVIEW_FINAL_DECISION)

    assert decision["review_stage"] == "maintainer_partial_final_decision_summary"
    assert decision["scope"] == "expansion_policy_review_only"
    assert decision["expected_values_included"] is False
    assert decision["private_expected_updated"] is False
    assert "cases" not in decision
    assert decision["source_confirmation_packet"] == (
        "docs/reports/"
        "holdout-maintainer-confirmation-blind-v1-expansion-policy-review-2026-07-09.json"
    )
    assert decision["summary"] == {
        "total_confirmed_cases": 33,
        "accepted_recommended_expected": 33,
        "edited_cases": 0,
        "dropped_cases": 0,
        "no_immediate_question_cases": 46,
        "private_expected_updated": False,
        "private_expected_update_note": (
            "This policy-review summary records maintainer approval only; the private "
            "expected file is rebuilt by the full 127-case expansion decision summary."
        ),
        "would_be_expected_source": {"human_first_pass": 33},
        "by_recommendation": {"codex_gemini_match": 33},
        "by_domain": {
            "formal": 4,
            "high_risk": 8,
            "it": 3,
            "llm": 4,
            "social": 5,
            "ui": 9,
        },
        "by_risk": {
            "baseline_guard": 3,
            "candidate_gap": 14,
            "over_conversion_guard": 16,
        },
        "by_policy_reason": {
            "Codex confidence medium": 11,
            "high-risk domain": 4,
            "high-risk domain, Codex confidence medium": 2,
            "high-risk domain, over-conversion guard": 2,
            "over-conversion guard": 14,
        },
    }
    assert decision["confirmed_case_ids"] == [case["id"] for case in packet["cases"]]


def test_holdout_expansion_final_decision_omits_expected_values() -> None:
    diff_decision = load_json(MAINTAINER_EXPANSION_DIFFERENCES_FINAL_DECISION)
    policy_decision = load_json(MAINTAINER_EXPANSION_POLICY_REVIEW_FINAL_DECISION)
    diff = load_json(CODEX_GEMINI_EXPANSION_DIFF_REVIEW)
    decision = load_json(MAINTAINER_EXPANSION_FINAL_DECISION)

    assert decision["review_stage"] == "maintainer_final_decision_summary"
    assert decision["scope"] == "expansion_127_cases"
    assert decision["expected_values_included"] is False
    assert decision["private_expected_updated"] is True
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert len(decision["private_expected_sha256"]) == 64
    assert "cases" not in decision
    assert (
        "docs/reports/"
        "holdout-maintainer-final-decision-blind-v1-expansion-policy-review-2026-07-09.json"
    ) in decision["source_reports"]
    assert decision["summary"] == {
        "expansion_cases": 127,
        "total_private_expected_cases": 200,
        "status": "sealed_private",
        "approval_policy": "single_human_with_ai_advisory",
        "minimum_human_reviewers": 1,
        "ai_advisory_review_allowed": True,
        "private_expected_updated": True,
        "accepted_recommended_expected": 81,
        "accepted_exact_no_immediate_question": 46,
        "edited_cases": 0,
        "dropped_cases": 0,
        "by_expected_source_for_expansion": {
            "human_adjudication": 48,
            "human_first_pass": 79,
        },
        "by_disagreement_for_expansion": {
            "false": 79,
            "true": 48,
        },
        "by_expected_source_total": {
            "human_adjudication": 65,
            "human_first_pass": 135,
        },
        "by_disagreement_total": {
            "false": 135,
            "true": 65,
        },
        "by_domain_for_expansion": {
            "formal": 18,
            "high_risk": 10,
            "it": 37,
            "llm": 17,
            "social": 18,
            "ui": 27,
        },
        "by_risk_for_expansion": {
            "baseline_guard": 17,
            "candidate_gap": 79,
            "over_conversion_guard": 31,
        },
    }
    assert decision["confirmed_case_ids"] == {
        "differences": diff_decision["confirmed_case_ids"],
        "policy_review": policy_decision["confirmed_case_ids"],
        "no_immediate_question": [case["id"] for case in diff["no_immediate_question"]],
    }


def test_competitors_lock_records_reproducible_adapters() -> None:
    lock = load_json(COMPETITORS_LOCK)
    competitors = {item["id"]: item for item in lock["competitors"]}

    assert lock["status"] == "draft"
    assert {"zhtw", "opencc-s2twp", "zhconv-zh-tw", "opencc-js-cn-twp", "zhconv-rs"} <= set(
        competitors
    )
    assert competitors["zhtw"]["included_in_m2_runner"] is True
    assert competitors["opencc-s2twp"]["locale_or_config"] == "s2twp"
    assert competitors["zhconv-zh-tw"]["locale_or_config"] == "zh-tw"
    assert competitors["opencc-js-cn-twp"]["included_in_m2_runner"] is False
    assert competitors["zhconv-rs"]["included_in_m2_runner"] is False

    for competitor in competitors.values():
        assert competitor["command"]
        assert competitor["version_source"]
        assert competitor["reproducibility"]
        assert (
            "expected output" not in competitor["notes"].lower()
            or "never" in competitor["notes"].lower()
        )


def test_create_holdout_annotation_packet(tmp_path: Path) -> None:
    output = tmp_path / "holdout-packet.md"

    result = subprocess.run(
        [
            sys.executable,
            str(PACKET_SCRIPT),
            "--inputs",
            str(INPUTS),
            "--batch",
            "blind-high-risk",
            "--generated-date",
            "2026-07-07",
            "--reviewer-stage",
            "first_human_review",
            "--output",
            str(output),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert "Wrote" in result.stdout
    assert "(128 cases)" in result.stdout

    content = output.read_text(encoding="utf-8")
    assert content.startswith("<!-- zhtw:disable -->")
    assert "Reviewer stage: `first_human_review`" in content
    assert "Cases: 128" in content
    assert "### blind-high-risk-0001" in content
    assert "不得以定型化契约条款排除责任。" in content
    assert "Do not run zhtw, OpenCC, zhconv, Gemini, or any converter" in content
    assert "Expected:" in content
    assert "Acceptable:" in content
    assert "Reviewer notes:" in content
    assert "跨行匯款手續費由使用者負擔。" not in content


def test_codex_first_pass_report_is_advisory_only() -> None:
    inputs = load_json(INPUTS)
    report = load_json(CODEX_FIRST_PASS)

    input_ids = [case["id"] for case in inputs["cases"]]
    report_ids = [case["id"] for case in report["cases"]]
    original_seed_input_ids = original_seed_ids_from_report(report_ids, input_ids)
    removed_ids = load_all_removed_case_ids()
    removed_report_ids = set(report_ids) & removed_ids

    assert report["review_stage"] == "first_pass_advisory"
    assert report["reviewer"] == "codex"
    assert report["ground_truth"] is False
    assert report["promotion_allowed"] is False
    assert report["summary"]["total_cases"] == len(report["cases"]) == 100
    assert report["summary"]["promotion_allowed"] is False
    assert report["summary"]["by_confidence"] == {"high": 83, "medium": 17}
    assert report["summary"]["review_needed"] == 36
    assert [case_id for case_id in report_ids if case_id not in removed_ids] == (
        original_seed_input_ids
    )
    assert len(report_ids) - len(original_seed_input_ids) == len(removed_report_ids)
    assert len(removed_report_ids) == 28

    for case in report["cases"]:
        assert case["codex_expected"]
        assert case["promotion_allowed"] is False
        assert case["confidence"] in {"high", "medium"}
        assert case["issue_tags"]
        assert case["rationale"]


def test_gemini_holdout_advisory_is_independent_and_advisory_only() -> None:
    inputs = load_json(INPUTS)
    report = load_json(GEMINI_ADVISORY)

    input_ids = [case["id"] for case in inputs["cases"]]
    comparison_ids = [case["id"] for case in report["comparisons"]]
    review_ids = [case["id"] for case in report["review"]["cases"]]
    original_seed_input_ids = original_seed_ids_from_report(comparison_ids, input_ids)
    removed_ids = load_all_removed_case_ids()
    removed_comparison_ids = set(comparison_ids) & removed_ids
    removed_review_ids = set(review_ids) & removed_ids

    assert report["reviewer"] == "gemini_vertex"
    assert report["review_stage"] == "independent_holdout_expected_review"
    assert report["ground_truth"] is False
    assert report["promotion_allowed"] is False
    assert report["summary"]["total_cases"] == 100
    assert report["summary"]["exact_matches_with_codex"] == 70
    assert report["summary"]["differences_from_codex"] == 30
    assert report["summary"]["needs_maintainer_review"] == 59
    assert report["summary"]["by_gemini_confidence"] == {"high": 100}
    assert [case_id for case_id in comparison_ids if case_id not in removed_ids] == (
        original_seed_input_ids
    )
    assert [case_id for case_id in review_ids if case_id not in removed_ids] == (
        original_seed_input_ids
    )
    assert len(comparison_ids) - len(original_seed_input_ids) == len(removed_comparison_ids)
    assert len(review_ids) - len(original_seed_input_ids) == len(removed_review_ids)
    assert len(removed_comparison_ids) == 28
    assert len(removed_review_ids) == 28

    for case in report["review"]["cases"]:
        assert case["expected"]
        assert case["confidence"] == "high"
        assert case["issue_tags"]
        assert case["notes"]


def test_codex_gemini_diff_review_lists_maintainer_queue() -> None:
    review = load_json(CODEX_GEMINI_DIFF_REVIEW)

    assert review["review_stage"] == "codex_gemini_difference_review"
    assert review["ground_truth"] is False
    assert review["promotion_allowed"] is False
    assert review["summary"] == {
        "total_cases": 100,
        "exact_matches": 70,
        "differences": 30,
        "exact_but_policy_review": 29,
        "no_immediate_question": 41,
        "maintainer_queue_total": 59,
        "difference_recommendations": {
            "codex": 24,
            "gemini": 5,
            "third_value": 1,
        },
        "promotion_allowed": False,
    }
    assert len(review["differences"]) == 30
    assert len(review["exact_but_policy_review"]) == 29
    assert len(review["no_immediate_question"]) == 41

    recommendations = {case["id"]: case["codex_recommendation"] for case in review["differences"]}
    assert recommendations["blind-it-0009"] == "gemini"
    assert recommendations["blind-llm-0013"] == "third_value"
    assert recommendations["blind-formal-0012"] == "codex"


def test_maintainer_confirmation_packet_is_not_ground_truth() -> None:
    packet = load_json(MAINTAINER_CONFIRMATION)

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["summary"] == {
        "total_review_cases": 59,
        "difference_cases": 30,
        "policy_review_cases": 29,
        "no_immediate_question": 41,
        "difference_recommendations": {
            "codex": 24,
            "gemini": 5,
            "third_value": 1,
        },
        "promotion_allowed": False,
    }
    assert len(packet["cases"]) == 59
    assert len(packet["no_immediate_question"]) == 41

    difference_cases = [case for case in packet["cases"] if case["kind"] == "difference"]
    policy_cases = [case for case in packet["cases"] if case["kind"] == "policy_review"]
    assert len(difference_cases) == 30
    assert len(policy_cases) == 29
    assert {case["maintainer_action"] for case in difference_cases} == {"confirm_or_edit"}
    assert {case["maintainer_action"] for case in policy_cases} == {"quick_confirm_or_edit"}
    assert all(case["recommended_expected"] for case in packet["cases"])


def test_maintainer_final_decision_summary_does_not_publish_expected_values() -> None:
    decision = load_json(FINAL_DECISION)

    assert decision["review_stage"] == "maintainer_final_decision_summary"
    assert decision["expected_values_included"] is False
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["summary"]["cases"] == 100
    assert decision["summary"]["status"] == "sealed_private"
    assert decision["summary"]["approval_policy"] == "single_human_with_ai_advisory"
    assert decision["summary"]["minimum_human_reviewers"] == 1
    assert decision["summary"]["ai_advisory_review_allowed"] is True
    assert decision["summary"]["by_expected_source"] == {
        "human_adjudication": 30,
        "human_first_pass": 70,
    }
    assert decision["summary"]["by_disagreement"] == {
        "false": 70,
        "true": 30,
    }
    assert "cases" not in decision


def test_private_benchmark_sanity_summary_omits_rows_and_expected_values() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["expected_values_included"] is False
    assert sanity["rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert sanity["summary"]["case_count"] == 256
    assert sanity["summary"]["accepted"] == 216
    assert sanity["summary"]["misses"] == 40
    assert sanity["summary"]["primary_exact"] == 184
    assert sanity["summary"]["acceptable_exact"] == 32
    assert sanity["summary"]["accepted_accuracy"] == 0.84375
    assert sanity["summary"]["primary_exact_accuracy"] == 0.71875
    assert sanity["summary"]["idempotency_rate"] == 0.98828125
    assert sanity["summary"]["accepted_accuracy_ci_95"] == {
        "low": 0.796875,
        "high": 0.88671875,
    }
    assert sanity["summary"]["by_domain"]["formal"]["accepted_accuracy"] == 0.8292682926829268
    assert sanity["summary"]["by_domain"]["high_risk"]["accepted_accuracy"] == 0.9230769230769231
    assert sanity["summary"]["by_domain"]["it"]["accepted_accuracy"] == 0.82
    assert sanity["summary"]["by_domain"]["llm"]["accepted_accuracy"] == 0.8837209302325582
    assert sanity["summary"]["by_domain"]["social"]["accepted_accuracy"] == 0.7954545454545454
    assert sanity["summary"]["by_domain"]["ui"]["accepted_accuracy"] == 0.8461538461538461
    assert sanity["summary"]["misses_by_risk"] == {
        "baseline_guard": 2,
        "candidate_gap": 19,
        "over_conversion_guard": 19,
    }
    assert sanity["summary"]["misses_by_issue_tag"] == {
        "formal_term": 10,
        "high_risk_term": 2,
        "it_term": 12,
        "over_conversion": 19,
        "regional_term": 40,
        "ui_term": 8,
    }


def test_private_benchmark_sanity_after_remaining_40_final_review_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_REMAINING_40_FINAL_REVIEW)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_remaining_40_final_review"
    assert sanity["expected_values_included"] is False
    assert sanity["rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert sanity["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "aggregate_statistics_only": True,
    }
    assert sanity["summary"]["case_count"] == 238
    assert sanity["summary"]["accepted"] == 219
    assert sanity["summary"]["misses"] == 19
    assert sanity["summary"]["primary_exact"] == 184
    assert sanity["summary"]["acceptable_exact"] == 35
    assert sanity["summary"]["accepted_accuracy"] == 0.9201680672268907
    assert sanity["summary"]["primary_exact_accuracy"] == 0.773109243697479
    assert sanity["summary"]["idempotency_rate"] == 0.9957983193277311
    assert sanity["summary"]["accepted_accuracy_ci_95"] == {
        "low": 0.8823529411764706,
        "high": 0.9537815126050421,
    }
    assert sanity["summary"]["by_domain"]["formal"]["accepted_accuracy"] == (0.8717948717948718)
    assert sanity["summary"]["by_domain"]["high_risk"]["accepted_accuracy"] == (0.9230769230769231)
    assert sanity["summary"]["by_domain"]["it"]["accepted_accuracy"] == (0.9767441860465116)
    assert sanity["summary"]["by_domain"]["llm"]["accepted_accuracy"] == (0.9047619047619048)
    assert sanity["summary"]["by_domain"]["social"]["accepted_accuracy"] == 0.875
    assert sanity["summary"]["by_domain"]["ui"]["accepted_accuracy"] == (0.9583333333333334)
    assert sanity["summary"]["misses_by_risk"] == {"over_conversion_guard": 19}
    assert sanity["summary"]["misses_by_issue_tag"] == {
        "formal_term": 7,
        "high_risk_term": 2,
        "it_term": 3,
        "over_conversion": 19,
        "regional_term": 19,
        "ui_term": 2,
    }


def test_holdout_miss_classification_omits_sealed_rows_and_values() -> None:
    report = load_json(MISS_CLASSIFICATION)

    assert report["report_type"] == "holdout_miss_classification"
    assert report["dataset"] == "blind-v1"
    assert report["source_benchmark"]["in_repo"] is False
    assert report["sealed_content_policy"] == {
        "expected_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "case_classifications_include_only_ids_and_metadata": True,
    }
    assert "rows" not in report
    assert "inputs" not in report

    summary = report["summary"]
    assert summary["case_count"] == 100
    assert summary["accepted"] == 57
    assert summary["misses"] == 43
    assert summary["by_action"] == {
        "move_to_public_regression_candidate": 22,
        "keep_as_holdout_signal": 7,
        "requires_expected_recheck": 14,
    }
    assert summary["by_domain_action"]["it"] == {
        "move_to_public_regression_candidate": 11,
        "keep_as_holdout_signal": 1,
        "requires_expected_recheck": 5,
    }
    assert summary["by_domain_action"]["ui"] == {
        "move_to_public_regression_candidate": 6,
        "keep_as_holdout_signal": 3,
        "requires_expected_recheck": 3,
    }
    assert summary["idempotency_followup_misses"] == 5
    assert summary["accepted_non_idempotent"] == 1

    forbidden_case_fields = {
        "acceptable",
        "annotation",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    cases = report["case_classifications"]
    assert len(cases) == 43
    assert len({case["id"] for case in cases}) == len(cases)
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["id"].startswith("blind-")
        assert case["action"] in summary["by_action"]
        assert case["reason_category"]
        assert case["next_step"]

    move_ids = {
        case["id"] for case in cases if case["action"] == "move_to_public_regression_candidate"
    }
    recheck_ids = {case["id"] for case in cases if case["action"] == "requires_expected_recheck"}
    holdout_ids = {case["id"] for case in cases if case["action"] == "keep_as_holdout_signal"}
    assert {"blind-it-0002", "blind-ui-0020", "blind-formal-0003"} <= move_ids
    assert {"blind-llm-0002", "blind-formal-0012"} <= recheck_ids
    assert {"blind-ui-0011", "blind-social-0015"} <= holdout_ids
    assert report["idempotency_notes"]["non_idempotent_miss_ids"] == [
        "blind-it-0023",
        "blind-ui-0002",
        "blind-ui-0019",
        "blind-formal-0003",
        "blind-social-0005",
    ]
    assert report["idempotency_notes"]["accepted_non_idempotent_ids"] == ["blind-formal-0015"]


def test_holdout_expected_recheck_summary_omits_sealed_values() -> None:
    report = load_json(EXPECTED_RECHECK)

    assert report["report_type"] == "holdout_expected_recheck_summary"
    assert report["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "case_decisions_include_only_ids_and_metadata": True,
    }
    assert report["private_expected_update"]["updated"] is True
    assert report["private_expected_update"]["acceptable_variants_added"] == 12
    assert report["summary"] == {
        "recheck_cases": 14,
        "add_acceptable_variant": 12,
        "keep_strict_primary_expected": 2,
        "move_to_public_regression_candidate": 0,
        "accepted_before_recheck": 57,
        "accepted_after_recheck": 69,
        "misses_before_recheck": 21,
        "misses_after_recheck": 9,
        "accepted_accuracy_after_recheck": 0.8846153846153846,
        "idempotency_rate_after_recheck": 0.9743589743589743,
        "by_domain_decision": {
            "formal": {
                "add_acceptable_variant": 1,
                "keep_strict_primary_expected": 1,
            },
            "it": {"add_acceptable_variant": 5},
            "llm": {"add_acceptable_variant": 4},
            "ui": {
                "add_acceptable_variant": 2,
                "keep_strict_primary_expected": 1,
            },
        },
    }
    assert "rows" not in report
    assert "inputs" not in report

    forbidden_case_fields = {
        "acceptable",
        "actual",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    decisions = report["case_decisions"]
    assert len(decisions) == 14
    assert len({case["id"] for case in decisions}) == len(decisions)
    for case in decisions:
        assert not (forbidden_case_fields & set(case))
        assert case["expected_values_included"] is False
        assert case["acceptable_values_included"] is False
        assert case["actual_outputs_included"] is False

    decision_by_id = {case["id"]: case["decision"] for case in decisions}
    assert decision_by_id["blind-it-0003"] == "add_acceptable_variant"
    assert decision_by_id["blind-llm-0012"] == "add_acceptable_variant"
    assert decision_by_id["blind-formal-0012"] == "add_acceptable_variant"
    assert decision_by_id["blind-ui-0002"] == "keep_strict_primary_expected"
    assert decision_by_id["blind-formal-0010"] == "keep_strict_primary_expected"


def test_holdout_remaining_miss_classification_omits_sealed_values() -> None:
    report = load_json(REMAINING_MISS_CLASSIFICATION)
    inputs = load_json(INPUTS)
    input_ids = {case["id"] for case in inputs["cases"]}
    batch2_removed_ids = set(load_json(SEALED_POOL_UPDATE_BATCH2)["removed_case_ids"])
    batch3_removed_ids = set(load_json(SEALED_POOL_UPDATE_BATCH3)["removed_case_ids"])

    assert report["report_type"] == "holdout_remaining_miss_classification"
    assert report["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "case_classifications_include_only_ids_and_metadata": True,
    }
    assert report["summary"] == {
        "current_sealed_cases": 78,
        "current_accepted": 69,
        "current_misses": 9,
        "classified_misses": 9,
        "by_action": {
            "move_to_public_regression_candidate": 5,
            "keep_as_holdout_signal": 4,
        },
        "by_priority": {"P1": 3, "P2": 6},
        "by_domain_action": {
            "formal": {
                "move_to_public_regression_candidate": 2,
                "keep_as_holdout_signal": 1,
            },
            "it": {
                "move_to_public_regression_candidate": 1,
                "keep_as_holdout_signal": 0,
            },
            "social": {
                "move_to_public_regression_candidate": 1,
                "keep_as_holdout_signal": 0,
            },
            "ui": {
                "move_to_public_regression_candidate": 1,
                "keep_as_holdout_signal": 3,
            },
        },
        "by_risk_action": {
            "baseline_guard": {
                "move_to_public_regression_candidate": 0,
                "keep_as_holdout_signal": 2,
            },
            "candidate_gap": {
                "move_to_public_regression_candidate": 5,
                "keep_as_holdout_signal": 2,
            },
        },
        "idempotency_followup_cases": 1,
        "strict_after_expected_recheck_cases": 2,
    }
    assert "rows" not in report
    assert "inputs" not in report

    forbidden_case_fields = {
        "acceptable",
        "actual",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    cases = report["case_classifications"]
    assert len(cases) == 9
    assert len({case["id"] for case in cases}) == len(cases)
    assert {case["id"] for case in cases} <= input_ids | batch2_removed_ids | batch3_removed_ids
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["action"] in report["summary"]["by_action"]
        assert case["next_step"]

    action_by_id = {case["id"]: case["action"] for case in cases}
    assert {
        case_id
        for case_id, action in action_by_id.items()
        if action == "move_to_public_regression_candidate"
    } == batch2_removed_ids
    assert action_by_id == {
        "blind-it-0014": "move_to_public_regression_candidate",
        "blind-ui-0002": "move_to_public_regression_candidate",
        "blind-ui-0011": "keep_as_holdout_signal",
        "blind-ui-0014": "keep_as_holdout_signal",
        "blind-ui-0016": "keep_as_holdout_signal",
        "blind-formal-0005": "keep_as_holdout_signal",
        "blind-formal-0006": "move_to_public_regression_candidate",
        "blind-formal-0010": "move_to_public_regression_candidate",
        "blind-social-0015": "move_to_public_regression_candidate",
    }

    flags_by_id = {case["id"]: set(case["flags"]) for case in cases}
    assert flags_by_id["blind-ui-0002"] == {
        "idempotency_followup",
        "strict_after_expected_recheck",
    }
    assert flags_by_id["blind-formal-0010"] == {"strict_after_expected_recheck"}


def test_holdout_200_case_miss_classification_omits_sealed_values() -> None:
    report = load_json(MISS_CLASSIFICATION_200_CASE)

    assert report["report_type"] == "holdout_miss_classification_200_case_sanity"
    assert report["review_stage"] == "private_miss_classification_first_pass"
    assert report["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "case_classifications_include_only_ids_and_metadata": True,
    }
    assert report["gemini_review_policy"] == {
        "status": "completed_on_sanitized_metadata",
        "review_report": (
            "docs/reports/"
            "holdout-gemini-policy-review-miss-classification-blind-v1-200-cases-2026-07-09.json"
        ),
        "sealed_values_seen_by_gemini": False,
        "policy_consistent": True,
        "needs_codex_followup": 0,
        "reason": (
            "Gemini reviewed case ids and classification metadata only; private expected, "
            "inputs, and converter outputs were not sent."
        ),
    }
    assert report["summary"] == {
        "current_sealed_cases": 200,
        "current_accepted": 144,
        "current_misses": 56,
        "classified_misses": 56,
        "by_action": {
            "keep_as_holdout_signal": 6,
            "move_to_public_regression_candidate": 39,
            "requires_expected_recheck": 11,
        },
        "by_priority": {"P1": 28, "P2": 27, "P3": 1},
        "by_domain_action": {
            "formal": {
                "keep_as_holdout_signal": 1,
                "move_to_public_regression_candidate": 4,
                "requires_expected_recheck": 1,
            },
            "high_risk": {
                "move_to_public_regression_candidate": 2,
                "requires_expected_recheck": 2,
            },
            "it": {
                "move_to_public_regression_candidate": 22,
                "requires_expected_recheck": 2,
            },
            "llm": {
                "keep_as_holdout_signal": 2,
                "move_to_public_regression_candidate": 2,
                "requires_expected_recheck": 2,
            },
            "social": {
                "keep_as_holdout_signal": 2,
                "move_to_public_regression_candidate": 1,
                "requires_expected_recheck": 1,
            },
            "ui": {
                "keep_as_holdout_signal": 1,
                "move_to_public_regression_candidate": 8,
                "requires_expected_recheck": 3,
            },
        },
        "by_risk_action": {
            "baseline_guard": {
                "keep_as_holdout_signal": 1,
                "move_to_public_regression_candidate": 5,
            },
            "candidate_gap": {
                "move_to_public_regression_candidate": 26,
                "requires_expected_recheck": 9,
            },
            "over_conversion_guard": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 8,
                "requires_expected_recheck": 2,
            },
        },
        "idempotency_followup_cases": 4,
        "expected_recheck_cases": 11,
        "safe_public_candidate_cases": 39,
        "holdout_signal_cases": 6,
    }
    assert "rows" not in report
    assert "inputs" not in report

    forbidden_case_fields = {
        "acceptable",
        "actual",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    cases = report["case_classifications"]
    assert len(cases) == 56
    assert len({case["id"] for case in cases}) == len(cases)
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["id"].startswith("blind-")
        assert case["action"] in report["summary"]["by_action"]
        assert case["reason_category"]
        assert case["next_step"]

    action_by_id = {case["id"]: case["action"] for case in cases}
    assert action_by_id["blind-it-0026"] == "move_to_public_regression_candidate"
    assert action_by_id["blind-it-0055"] == "requires_expected_recheck"
    assert action_by_id["blind-llm-0026"] == "keep_as_holdout_signal"
    assert action_by_id["blind-high-risk-0016"] == "move_to_public_regression_candidate"
    assert report["idempotency_notes"]["non_idempotent_miss_ids"] == [
        "blind-it-0034",
        "blind-ui-0040",
        "blind-formal-0025",
        "blind-social-0019",
    ]


def test_gemini_200_case_miss_classification_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_MISS_CLASSIFICATION_POLICY_REVIEW)

    assert review["reviewer"] == "gemini_vertex"
    assert review["model"] == "gemini-2.5-flash"
    assert review["review_stage"] == "sanitized_miss_classification_policy_review"
    assert review["sealed_values_seen"] is False
    assert review["source_classification_report"] == (
        "docs/reports/holdout-miss-classification-blind-v1-200-cases-2026-07-09.json"
    )
    assert review["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "gemini_received_sanitized_metadata_only": True,
    }
    assert review["summary"] == {
        "total_cases": 56,
        "policy_consistent": True,
        "needs_codex_followup": 0,
    }
    assert review["findings"] == []
    assert "cases" not in review


def test_holdout_261_case_miss_classification_omits_sealed_values() -> None:
    report = load_json(MISS_CLASSIFICATION_261_CASE)

    assert report["report_type"] == "holdout_miss_classification_261_case_sanity"
    assert report["review_stage"] == "private_miss_classification_first_pass"
    assert report["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "case_classifications_include_only_ids_and_metadata": True,
    }
    assert report["gemini_review_policy"] == {
        "status": "completed_on_sanitized_metadata",
        "review_report": (
            "docs/reports/"
            "holdout-gemini-policy-review-miss-classification-blind-v1-261-cases-2026-07-09.json"
        ),
        "sealed_values_seen_by_gemini": False,
        "policy_consistent": True,
        "needs_codex_followup": 0,
        "reason": (
            "Gemini reviewed case ids and classification metadata only; private expected, "
            "inputs, and converter outputs were not sent."
        ),
    }
    assert report["codex_followup"] == {
        "status": "revised_after_gemini_policy_findings",
        "revised_case_ids": [
            "blind-high-risk-0028",
            "blind-high-risk-0030",
            "blind-it-0080",
            "blind-it-0081",
            "blind-it-0082",
            "blind-it-0084",
            "blind-llm-0042",
        ],
        "reason": (
            "Gemini policy review flagged over-conversion guard and high-risk cases as "
            "insufficiently conservative for direct move-to-public classification; Codex "
            "changed them to requires_expected_recheck."
        ),
    }
    assert report["summary"] == {
        "current_sealed_cases": 261,
        "current_accepted": 207,
        "current_misses": 54,
        "classified_misses": 54,
        "by_action": {
            "keep_as_holdout_signal": 20,
            "move_to_public_regression_candidate": 18,
            "requires_expected_recheck": 16,
        },
        "by_priority": {"P1": 19, "P2": 34, "P3": 1},
        "by_domain_action": {
            "formal": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 1,
                "requires_expected_recheck": 3,
            },
            "high_risk": {
                "keep_as_holdout_signal": 2,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 4,
            },
            "it": {
                "keep_as_holdout_signal": 1,
                "move_to_public_regression_candidate": 8,
                "requires_expected_recheck": 5,
            },
            "llm": {
                "keep_as_holdout_signal": 4,
                "move_to_public_regression_candidate": 1,
                "requires_expected_recheck": 2,
            },
            "social": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 4,
                "requires_expected_recheck": 0,
            },
            "ui": {
                "keep_as_holdout_signal": 3,
                "move_to_public_regression_candidate": 4,
                "requires_expected_recheck": 2,
            },
        },
        "by_risk_action": {
            "baseline_guard": {
                "keep_as_holdout_signal": 1,
                "move_to_public_regression_candidate": 1,
                "requires_expected_recheck": 2,
            },
            "candidate_gap": {
                "keep_as_holdout_signal": 0,
                "move_to_public_regression_candidate": 17,
                "requires_expected_recheck": 8,
            },
            "over_conversion_guard": {
                "keep_as_holdout_signal": 19,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 6,
            },
        },
        "idempotency_followup_cases": 2,
        "expected_recheck_cases": 16,
        "safe_public_candidate_cases": 18,
        "holdout_signal_cases": 20,
        "high_risk_cases": 6,
        "over_conversion_guard_cases": 25,
    }
    assert "rows" not in report
    assert "inputs" not in report

    forbidden_case_fields = {
        "acceptable",
        "actual",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    cases = report["case_classifications"]
    assert len(cases) == 54
    assert len({case["id"] for case in cases}) == len(cases)
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["id"].startswith("blind-")
        assert case["action"] in report["summary"]["by_action"]
        assert case["reason_category"]
        assert case["next_step"]

    action_by_id = {case["id"]: case["action"] for case in cases}
    assert action_by_id["blind-it-0063"] == "move_to_public_regression_candidate"
    assert action_by_id["blind-it-0080"] == "requires_expected_recheck"
    assert action_by_id["blind-high-risk-0030"] == "requires_expected_recheck"
    assert action_by_id["blind-social-0042"] == "keep_as_holdout_signal"

    assert report["idempotency_notes"]["non_idempotent_miss_ids"] == [
        "blind-it-0070",
        "blind-social-0034",
    ]


def test_gemini_261_case_miss_classification_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_MISS_CLASSIFICATION_261_POLICY_REVIEW)

    assert review["reviewer"] == "gemini_vertex"
    assert review["model"] == "gemini-2.5-flash"
    assert review["review_stage"] == "sanitized_miss_classification_policy_review"
    assert review["sealed_values_seen"] is False
    assert review["source_classification_report"] == (
        "docs/reports/holdout-miss-classification-blind-v1-261-cases-2026-07-09.json"
    )
    assert review["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "gemini_received_sanitized_metadata_only": True,
    }
    assert review["summary"] == {
        "total_cases": 54,
        "policy_consistent": True,
        "needs_codex_followup": 0,
    }
    assert review["findings"] == []
    assert "cases" not in review


def test_private_benchmark_sanity_after_batch5_covers_338_cases() -> None:
    report = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH5)
    final_decision = load_json(MAINTAINER_BATCH5_FINAL_DECISION)

    assert report["dataset"] == "blind-v1"
    assert report["summary"]["case_count"] == 338
    assert report["report_mode"] == "aggregate"
    assert report["dataset_classification"] == "published_evaluation"
    assert report["expected_sha256"] == final_decision["private_expected_sha256"]
    assert report["engines"]["zhtw"]["scores"]["total_cases"] == 338
    assert report["engines"]["zhtw"]["scores"]["accepted"] == 301
    assert report["engines"]["zhtw"]["scores"]["misses"] == 37
    assert round(report["engines"]["zhtw"]["scores"]["accepted_accuracy"], 4) == 0.8905
    assert "rows" not in report
    assert "expected" not in report


def test_private_benchmark_sanity_after_338_miss_review_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_338_MISS_REVIEW)
    final_decision = load_json(MAINTAINER_338_MISS_FINAL_DECISION)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_338_miss_review"
    assert sanity["expected_values_included"] is False
    assert sanity["rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert sanity["source_benchmark"] == {
        "path": "/tmp/zhtw-blind-v1-private-benchmark-after-338-miss-review-2026-07-09.json",
        "in_repo": False,
        "rows_used_for_aggregate_only": True,
    }
    assert sanity["inputs"]["path"] == "benchmarks/accuracy/blind-v1.inputs.json"
    assert sanity["inputs"]["sha256"] == (
        "2d69cf2ceb90dff8b41e9806cfe7c642d8e3e64947ea83045a8fd41be705a5a2"
    )
    assert sanity["expected"]["path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert sanity["expected"]["sha256"] == final_decision["private_expected_sha256_after"]
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "aggregate_statistics_only": True,
    }
    assert sanity["summary"]["case_count"] == 326
    assert sanity["summary"]["accepted"] == 304
    assert sanity["summary"]["misses"] == 22
    assert sanity["summary"]["primary_exact"] == 242
    assert sanity["summary"]["acceptable_exact"] == 62
    assert sanity["summary"]["accepted_accuracy"] == 0.9325153374233128
    assert sanity["summary"]["primary_exact_accuracy"] == 0.7423312883435583
    assert sanity["summary"]["idempotency_rate"] == 0.99079754601227
    assert sanity["summary"]["accepted_accuracy_ci_95"] == {
        "low": 0.9079754601226994,
        "high": 0.9601226993865031,
    }
    assert sanity["summary"]["by_domain"] == {
        "formal": {
            "total": 54,
            "accepted": 49,
            "accepted_accuracy": 0.9074074074074074,
        },
        "high_risk": {
            "total": 36,
            "accepted": 33,
            "accepted_accuracy": 0.9166666666666666,
        },
        "it": {
            "total": 61,
            "accepted": 59,
            "accepted_accuracy": 0.9672131147540983,
        },
        "llm": {
            "total": 56,
            "accepted": 52,
            "accepted_accuracy": 0.9285714285714286,
        },
        "social": {
            "total": 55,
            "accepted": 50,
            "accepted_accuracy": 0.9090909090909091,
        },
        "ui": {
            "total": 64,
            "accepted": 61,
            "accepted_accuracy": 0.953125,
        },
    }
    assert sanity["summary"]["by_risk"] == {
        "baseline_guard": 52,
        "candidate_gap": 186,
        "over_conversion_guard": 88,
    }
    assert sanity["summary"]["misses_by_risk"] == {"over_conversion_guard": 22}
    assert sanity["summary"]["misses_by_issue_tag"] == {
        "formal_term": 8,
        "high_risk_term": 3,
        "it_term": 4,
        "over_conversion": 22,
        "regional_term": 22,
        "ui_term": 3,
    }


def test_private_benchmark_sanity_after_batch6_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH6)
    final_decision = load_json(MAINTAINER_BATCH6_FINAL_DECISION)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch6_final_decision"
    assert sanity["expected_values_included"] is False
    assert sanity["rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert sanity["source_benchmark"] == {
        "path": "/tmp/zhtw-blind-v1-private-benchmark-after-batch6-2026-07-10.json",
        "in_repo": False,
        "rows_used_for_aggregate_only": True,
    }
    assert sanity["inputs"]["path"] == "benchmarks/accuracy/blind-v1.inputs.json"
    assert sanity["inputs"]["sha256"] == (
        "be3ab808d2f2bb71b1c86e66cd95eb182446693412c1ebbecdf5aa632f35d35e"
    )
    assert sanity["expected"]["path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert sanity["expected"]["sha256"] == final_decision["private_expected_sha256"]
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "aggregate_statistics_only": True,
    }
    assert sanity["summary"]["case_count"] == 426
    assert sanity["summary"]["accepted"] == 389
    assert sanity["summary"]["misses"] == 37
    assert sanity["summary"]["primary_exact"] == 308
    assert sanity["summary"]["acceptable_exact"] == 81
    assert sanity["summary"]["accepted_accuracy"] == 0.9131455399061033
    assert sanity["summary"]["primary_exact_accuracy"] == 0.7230046948356808
    assert sanity["summary"]["idempotency_rate"] == 0.9859154929577465
    assert sanity["summary"]["accepted_accuracy_ci_95"] == {
        "low": 0.8873239436619719,
        "high": 0.9413145539906104,
    }
    assert sanity["summary"]["by_domain"] == {
        "formal": {
            "total": 69,
            "accepted": 64,
            "accepted_accuracy": 0.927536231884058,
        },
        "high_risk": {
            "total": 46,
            "accepted": 43,
            "accepted_accuracy": 0.9347826086956522,
        },
        "it": {
            "total": 86,
            "accepted": 73,
            "accepted_accuracy": 0.8488372093023255,
        },
        "llm": {
            "total": 71,
            "accepted": 66,
            "accepted_accuracy": 0.9295774647887324,
        },
        "social": {
            "total": 70,
            "accepted": 65,
            "accepted_accuracy": 0.9285714285714286,
        },
        "ui": {
            "total": 84,
            "accepted": 78,
            "accepted_accuracy": 0.9285714285714286,
        },
    }
    assert sanity["summary"]["by_risk"] == {
        "baseline_guard": 67,
        "candidate_gap": 246,
        "over_conversion_guard": 113,
    }
    assert sanity["summary"]["misses_by_risk"] == {
        "baseline_guard": 1,
        "candidate_gap": 12,
        "over_conversion_guard": 24,
    }
    assert sanity["summary"]["misses_by_issue_tag"] == {
        "formal_term": 8,
        "high_risk_term": 3,
        "it_term": 16,
        "over_conversion": 24,
        "regional_term": 37,
        "ui_term": 6,
    }


def test_private_benchmark_sanity_after_batch6_miss_review_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH6_MISS_REVIEW)
    final_decision = load_json(MAINTAINER_BATCH6_MISS_FINAL_DECISION)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch6_miss_review"
    assert sanity["expected_values_included"] is False
    assert sanity["rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert sanity["source_benchmark"] == {
        "path": "/tmp/zhtw-blind-v1-private-benchmark-after-batch6-miss-review-2026-07-10.json",
        "in_repo": False,
        "rows_used_for_aggregate_only": True,
    }
    assert sanity["inputs"]["path"] == "benchmarks/accuracy/blind-v1.inputs.json"
    assert sanity["inputs"]["sha256"] == (
        "18153aa5d4bafad940734bf19754d1948f4a9562979e7c668ecf855c1c683a20"
    )
    assert sanity["inputs"]["sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert sanity["expected"]["path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert sanity["expected"]["sha256"] == final_decision["private_expected_sha256_after"]
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "aggregate_statistics_only": True,
    }
    assert sanity["summary"]["case_count"] == 415
    assert sanity["summary"]["accepted"] == 391
    assert sanity["summary"]["misses"] == 24
    assert sanity["summary"]["primary_exact"] == 308
    assert sanity["summary"]["acceptable_exact"] == 83
    assert sanity["summary"]["accepted_accuracy"] == 0.9421686746987952
    assert sanity["summary"]["primary_exact_accuracy"] == 0.7421686746987952
    assert sanity["summary"]["idempotency_rate"] == 0.9879518072289156
    assert sanity["summary"]["accepted_accuracy_ci_95"] == {
        "low": 0.9180722891566265,
        "high": 0.963855421686747,
    }
    assert sanity["summary"]["by_domain"] == {
        "formal": {
            "total": 69,
            "accepted": 64,
            "accepted_accuracy": 0.927536231884058,
        },
        "high_risk": {
            "total": 46,
            "accepted": 43,
            "accepted_accuracy": 0.9347826086956522,
        },
        "it": {
            "total": 76,
            "accepted": 73,
            "accepted_accuracy": 0.9605263157894737,
        },
        "llm": {
            "total": 71,
            "accepted": 67,
            "accepted_accuracy": 0.9436619718309859,
        },
        "social": {
            "total": 70,
            "accepted": 65,
            "accepted_accuracy": 0.9285714285714286,
        },
        "ui": {
            "total": 83,
            "accepted": 79,
            "accepted_accuracy": 0.9518072289156626,
        },
    }
    assert sanity["summary"]["by_risk"] == {
        "baseline_guard": 66,
        "candidate_gap": 236,
        "over_conversion_guard": 113,
    }
    assert sanity["summary"]["misses_by_risk"] == {"over_conversion_guard": 24}
    assert sanity["summary"]["misses_by_issue_tag"] == {
        "formal_term": 8,
        "high_risk_term": 3,
        "it_term": 5,
        "over_conversion": 24,
        "regional_term": 24,
        "ui_term": 4,
    }


def test_private_benchmark_sanity_after_batch7_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH7)
    final_decision = load_json(MAINTAINER_BATCH7_FINAL_DECISION)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch7_final_decision"
    assert sanity["expected_values_included"] is False
    assert sanity["rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert sanity["source_benchmark"] == {
        "path": "/tmp/zhtw-blind-v1-private-benchmark-after-batch7-2026-07-10.json",
        "in_repo": False,
        "rows_used_for_aggregate_only": True,
    }
    assert sanity["inputs"]["path"] == "benchmarks/accuracy/blind-v1.inputs.json"
    assert sanity["inputs"]["sha256"] == (
        "27a3ec40cf4f5df586524d3ec307f3fcbf164a1e1ece097cc8637cd484cb5dc1"
    )
    assert sanity["inputs"]["sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert sanity["expected"]["path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert sanity["expected"]["sha256"] == final_decision["private_expected_sha256"]
    assert sanity["expected"]["sha256"] != private_expected_sha256()
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "aggregate_statistics_only": True,
    }
    assert sanity["summary"]["case_count"] == 515
    assert sanity["summary"]["accepted"] == 465
    assert sanity["summary"]["misses"] == 50
    assert sanity["summary"]["primary_exact"] == 370
    assert sanity["summary"]["acceptable_exact"] == 95
    assert sanity["summary"]["accepted_accuracy"] == 0.9029126213592233
    assert sanity["summary"]["primary_exact_accuracy"] == 0.7184466019417476
    assert sanity["summary"]["idempotency_rate"] == 0.9786407766990292
    assert sanity["summary"]["accepted_accuracy_ci_95"] == {
        "low": 0.8776699029126214,
        "high": 0.9281553398058252,
    }
    assert sanity["summary"]["by_domain"] == {
        "formal": {
            "total": 84,
            "accepted": 78,
            "accepted_accuracy": 0.9285714285714286,
        },
        "high_risk": {
            "total": 56,
            "accepted": 51,
            "accepted_accuracy": 0.9107142857142857,
        },
        "it": {
            "total": 101,
            "accepted": 83,
            "accepted_accuracy": 0.8217821782178217,
        },
        "llm": {
            "total": 86,
            "accepted": 80,
            "accepted_accuracy": 0.9302325581395349,
        },
        "social": {
            "total": 85,
            "accepted": 79,
            "accepted_accuracy": 0.9294117647058824,
        },
        "ui": {
            "total": 103,
            "accepted": 94,
            "accepted_accuracy": 0.912621359223301,
        },
    }
    assert sanity["summary"]["by_risk"] == {
        "baseline_guard": 81,
        "candidate_gap": 296,
        "over_conversion_guard": 138,
    }
    assert sanity["summary"]["misses_by_risk"] == {
        "baseline_guard": 2,
        "candidate_gap": 23,
        "over_conversion_guard": 25,
    }
    assert sanity["summary"]["misses_by_issue_tag"] == {
        "formal_term": 9,
        "high_risk_term": 5,
        "it_term": 20,
        "over_conversion": 25,
        "regional_term": 50,
        "ui_term": 9,
    }


def test_private_benchmark_sanity_after_batch7_miss_review_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH7_MISS_REVIEW)
    final_decision = load_json(MAINTAINER_BATCH7_MISS_FINAL_DECISION)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch7_miss_review"
    assert sanity["expected_values_included"] is False
    assert sanity["rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert sanity["source_benchmark"] == {
        "path": "/tmp/zhtw-blind-v1-private-benchmark-after-batch7-miss-review-2026-07-10.json",
        "in_repo": False,
        "rows_used_for_aggregate_only": True,
    }
    assert sanity["inputs"]["sha256"] == (
        "d331a1a2d6c58774089ca723677ec77ca4abe05e1eb11298ca8a5700b6a1cbcd"
    )
    assert sanity["inputs"]["sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert sanity["expected"]["sha256"] == final_decision["private_expected_sha256_after"]
    assert sanity["expected"]["sha256"] != private_expected_sha256()
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "aggregate_statistics_only": True,
    }
    assert sanity["summary"]["case_count"] == 498
    assert sanity["summary"]["accepted"] == 472
    assert sanity["summary"]["misses"] == 26
    assert sanity["summary"]["primary_exact"] == 370
    assert sanity["summary"]["acceptable_exact"] == 102
    assert sanity["summary"]["accepted_accuracy"] == 0.9477911646586346
    assert sanity["summary"]["primary_exact_accuracy"] == 0.7429718875502008
    assert sanity["summary"]["idempotency_rate"] == 0.9879518072289156
    assert sanity["summary"]["accepted_accuracy_ci_95"] == {
        "low": 0.927710843373494,
        "high": 0.9658634538152611,
    }
    assert sanity["summary"]["by_risk"] == {
        "baseline_guard": 79,
        "candidate_gap": 281,
        "over_conversion_guard": 138,
    }
    assert sanity["summary"]["misses_by_risk"] == {
        "candidate_gap": 1,
        "over_conversion_guard": 25,
    }


def test_private_benchmark_sanity_after_batch8_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH8)
    final_decision = load_json(MAINTAINER_BATCH8_FINAL_DECISION)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch8"
    assert sanity["expected_values_included"] is False
    assert sanity["rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert sanity["source_benchmark"] == {
        "path": "/tmp/zhtw-blind-v1-private-benchmark-after-batch8-2026-07-10.json",
        "in_repo": False,
        "rows_used_for_aggregate_only": True,
    }
    assert sanity["inputs"]["sha256"] == (
        "287b30b7d08ac7761fc78624e8db5f9f9d2664a214feef6b06dfe401cdd719cb"
    )
    assert sanity["inputs"]["sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert sanity["expected"]["sha256"] == final_decision["private_expected_sha256"]
    assert sanity["expected"]["sha256"] != private_expected_sha256()
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "aggregate_statistics_only": True,
    }
    assert sanity["summary"]["case_count"] == 598
    assert sanity["summary"]["accepted"] == 549
    assert sanity["summary"]["misses"] == 49
    assert sanity["summary"]["primary_exact"] == 434
    assert sanity["summary"]["acceptable_exact"] == 115
    assert sanity["summary"]["accepted_accuracy"] == 0.9180602006688964
    assert sanity["summary"]["primary_exact_accuracy"] == 0.725752508361204
    assert sanity["summary"]["idempotency_rate"] == 0.9832775919732442
    assert sanity["summary"]["accepted_accuracy_ci_95"] == {
        "low": 0.8946488294314381,
        "high": 0.939799331103679,
    }
    assert sanity["summary"]["by_domain"] == {
        "formal": {
            "total": 98,
            "accepted": 91,
            "accepted_accuracy": 0.9285714285714286,
        },
        "high_risk": {
            "total": 66,
            "accepted": 59,
            "accepted_accuracy": 0.8939393939393939,
        },
        "it": {
            "total": 115,
            "accepted": 102,
            "accepted_accuracy": 0.8869565217391304,
        },
        "llm": {
            "total": 99,
            "accepted": 93,
            "accepted_accuracy": 0.9393939393939394,
        },
        "social": {
            "total": 99,
            "accepted": 93,
            "accepted_accuracy": 0.9393939393939394,
        },
        "ui": {
            "total": 121,
            "accepted": 111,
            "accepted_accuracy": 0.9173553719008265,
        },
    }
    assert sanity["summary"]["by_risk"] == {
        "baseline_guard": 94,
        "candidate_gap": 341,
        "over_conversion_guard": 163,
    }
    assert sanity["summary"]["misses_by_risk"] == {
        "baseline_guard": 1,
        "candidate_gap": 21,
        "over_conversion_guard": 27,
    }
    assert sanity["summary"]["misses_by_issue_tag"] == {
        "baseline_guard": 1,
        "candidate_gap": 20,
        "formal_term": 10,
        "high_risk_term": 7,
        "it_term": 15,
        "llm_term": 2,
        "over_conversion": 27,
        "regional_term": 49,
        "social_term": 1,
        "ui_term": 10,
    }


def test_private_benchmark_sanity_after_batch8_miss_review_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH8_MISS_REVIEW)
    final_decision = load_json(MAINTAINER_BATCH8_MISS_FINAL_DECISION)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch8_miss_review"
    assert sanity["expected_values_included"] is False
    assert sanity["rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert sanity["source_benchmark"] == {
        "path": "/tmp/zhtw-blind-v1-private-benchmark-after-batch8-miss-review-2026-07-11.json",
        "in_repo": False,
        "rows_used_for_aggregate_only": True,
    }
    assert sanity["inputs"]["sha256"] == (
        "96226f1fc747cc1d6ae9eb40793077a3a8bc8dc36b194491dc63c7cb26bd4450"
    )
    assert sanity["inputs"]["sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert sanity["expected"]["sha256"] == final_decision["private_expected_sha256_after"]
    assert sanity["expected"]["sha256"] != private_expected_sha256()
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "aggregate_statistics_only": True,
    }
    assert sanity["summary"]["case_count"] == 583
    assert sanity["summary"]["accepted"] == 553
    assert sanity["summary"]["misses"] == 30
    assert sanity["summary"]["primary_exact"] == 434
    assert sanity["summary"]["acceptable_exact"] == 119
    assert sanity["summary"]["accepted_accuracy"] == 0.9485420240137221
    assert sanity["summary"]["primary_exact_accuracy"] == 0.7444253859348199
    assert sanity["summary"]["idempotency_rate"] == 0.9845626072041166
    assert sanity["summary"]["accepted_accuracy_ci_95"] == {
        "low": 0.9296740994854202,
        "high": 0.9656946826758147,
    }
    assert sanity["summary"]["by_domain"] == {
        "formal": {
            "total": 97,
            "accepted": 91,
            "accepted_accuracy": 0.9381443298969072,
        },
        "high_risk": {
            "total": 66,
            "accepted": 59,
            "accepted_accuracy": 0.8939393939393939,
        },
        "it": {
            "total": 107,
            "accepted": 104,
            "accepted_accuracy": 0.9719626168224299,
        },
        "llm": {
            "total": 98,
            "accepted": 94,
            "accepted_accuracy": 0.9591836734693877,
        },
        "social": {
            "total": 99,
            "accepted": 94,
            "accepted_accuracy": 0.9494949494949495,
        },
        "ui": {
            "total": 116,
            "accepted": 111,
            "accepted_accuracy": 0.9568965517241379,
        },
    }
    assert sanity["summary"]["by_risk"] == {
        "baseline_guard": 94,
        "candidate_gap": 326,
        "over_conversion_guard": 163,
    }
    assert sanity["summary"]["misses_by_risk"] == {
        "baseline_guard": 1,
        "candidate_gap": 2,
        "over_conversion_guard": 27,
    }
    assert sanity["summary"]["misses_by_issue_tag"] == {
        "baseline_guard": 1,
        "candidate_gap": 1,
        "formal_term": 9,
        "high_risk_term": 7,
        "it_term": 5,
        "over_conversion": 27,
        "regional_term": 30,
        "ui_term": 5,
    }


def test_private_benchmark_sanity_after_batch9_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH9)
    final_decision = load_json(MAINTAINER_BATCH9_FINAL_DECISION)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch9_final_decision"
    assert sanity["expected_values_included"] is False
    assert sanity["rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert sanity["source_benchmark"] == {
        "path": "/tmp/zhtw-blind-v1-private-benchmark-after-batch9-2026-07-12.json",
        "in_repo": False,
        "rows_used_for_aggregate_only": True,
    }
    assert sanity["inputs"]["sha256"] == (
        "0ac742ac9885cdae198bed6fc376c2fb5c3e991573ae4cb4ac2072cfef3e937d"
    )
    assert sanity["inputs"]["sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert sanity["expected"]["sha256"] == final_decision["private_expected_sha256"]
    assert sanity["expected"]["sha256"] != private_expected_sha256()
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "aggregate_statistics_only": True,
    }
    assert sanity["summary"]["case_count"] == 683
    assert sanity["summary"]["accepted"] == 630
    assert sanity["summary"]["misses"] == 53
    assert sanity["summary"]["primary_exact"] == 491
    assert sanity["summary"]["acceptable_exact"] == 139
    assert sanity["summary"]["accepted_accuracy"] == 0.9224011713030746
    assert sanity["summary"]["primary_exact_accuracy"] == 0.718887262079063
    assert sanity["summary"]["idempotency_rate"] == 0.9809663250366032
    assert sanity["summary"]["accepted_accuracy_ci_95"] == {
        "low": 0.9019033674963397,
        "high": 0.9399707174231332,
    }
    assert sanity["summary"]["by_domain"] == {
        "formal": {
            "total": 112,
            "accepted": 104,
            "accepted_accuracy": 0.9285714285714286,
        },
        "high_risk": {
            "total": 76,
            "accepted": 69,
            "accepted_accuracy": 0.9078947368421053,
        },
        "it": {
            "total": 132,
            "accepted": 117,
            "accepted_accuracy": 0.8863636363636364,
        },
        "llm": {
            "total": 113,
            "accepted": 107,
            "accepted_accuracy": 0.9469026548672567,
        },
        "social": {
            "total": 114,
            "accepted": 108,
            "accepted_accuracy": 0.9473684210526315,
        },
        "ui": {
            "total": 136,
            "accepted": 125,
            "accepted_accuracy": 0.9191176470588235,
        },
    }
    assert sanity["summary"]["by_risk"] == {
        "baseline_guard": 109,
        "candidate_gap": 386,
        "over_conversion_guard": 188,
    }
    assert sanity["summary"]["misses_by_risk"] == {
        "baseline_guard": 3,
        "candidate_gap": 22,
        "over_conversion_guard": 28,
    }
    assert sanity["summary"]["misses_by_issue_tag"] == {
        "baseline_guard": 3,
        "candidate_gap": 21,
        "formal_term": 11,
        "high_risk_term": 7,
        "it_term": 17,
        "llm_term": 2,
        "over_conversion": 28,
        "regional_term": 53,
        "social_term": 1,
        "ui_term": 11,
    }


def test_private_benchmark_sanity_after_batch9_miss_review_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH9_MISS_REVIEW)
    final_decision = load_json(MAINTAINER_BATCH9_MISS_FINAL_DECISION)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch9_miss_review"
    assert sanity["expected_values_included"] is False
    assert sanity["rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert sanity["source_benchmark"] == {
        "path": "/tmp/zhtw-blind-v1-private-benchmark-after-batch9-miss-review-2026-07-12.json",
        "in_repo": False,
        "rows_used_for_aggregate_only": True,
    }
    assert sanity["inputs"]["sha256"] == (
        "8f54d6e8185cf94f73805aeea27a23859e691cfd8ae04f3956023ec8ec9606d4"
    )
    assert sanity["inputs"]["sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert sanity["expected"]["sha256"] == final_decision["private_expected_sha256_after"]
    assert sanity["expected"]["sha256"] != private_expected_sha256()
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_values_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "aggregate_statistics_only": True,
    }
    assert sanity["summary"]["case_count"] == 667
    assert sanity["summary"]["accepted"] == 636
    assert sanity["summary"]["misses"] == 31
    assert sanity["summary"]["primary_exact"] == 491
    assert sanity["summary"]["acceptable_exact"] == 145
    assert sanity["summary"]["accepted_accuracy"] == 0.9535232383808095
    assert sanity["summary"]["primary_exact_accuracy"] == 0.7361319340329835
    assert sanity["summary"]["idempotency_rate"] == 0.9835082458770614
    assert sanity["summary"]["accepted_accuracy_ci_95"] == {
        "low": 0.9355322338830585,
        "high": 0.9685157421289355,
    }
    assert sanity["summary"]["by_domain"] == {
        "formal": {
            "total": 110,
            "accepted": 104,
            "accepted_accuracy": 0.9454545454545454,
        },
        "high_risk": {
            "total": 76,
            "accepted": 69,
            "accepted_accuracy": 0.9078947368421053,
        },
        "it": {
            "total": 124,
            "accepted": 121,
            "accepted_accuracy": 0.9758064516129032,
        },
        "llm": {
            "total": 111,
            "accepted": 107,
            "accepted_accuracy": 0.963963963963964,
        },
        "social": {
            "total": 114,
            "accepted": 108,
            "accepted_accuracy": 0.9473684210526315,
        },
        "ui": {
            "total": 132,
            "accepted": 127,
            "accepted_accuracy": 0.9621212121212122,
        },
    }
    assert sanity["summary"]["by_risk"] == {
        "baseline_guard": 107,
        "candidate_gap": 372,
        "over_conversion_guard": 188,
    }
    assert sanity["summary"]["misses_by_risk"] == {
        "baseline_guard": 1,
        "candidate_gap": 2,
        "over_conversion_guard": 28,
    }
    assert sanity["summary"]["misses_by_issue_tag"] == {
        "baseline_guard": 1,
        "candidate_gap": 1,
        "formal_term": 9,
        "high_risk_term": 7,
        "it_term": 5,
        "over_conversion": 28,
        "regional_term": 31,
        "social_term": 1,
        "ui_term": 5,
    }


def test_private_benchmark_sanity_after_batch10_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH10)
    final_decision = load_json(MAINTAINER_BATCH10_FINAL_DECISION)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch10_final_decision"
    assert sanity["expected_values_included"] is False
    assert sanity["rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert sanity["source_benchmark"] == {
        "path": "/tmp/zhtw-blind-v1-private-benchmark-after-batch10-2026-07-12.json",
        "in_repo": False,
        "rows_used_for_aggregate_only": True,
    }
    assert sanity["inputs"]["sha256"] == (
        "eff19da4ff198981bdb0018bceabb128b1aa5a33e9199ea5421f69561da340d0"
    )
    assert sanity["inputs"]["sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert sanity["expected"]["sha256"] == final_decision["private_expected_sha256"]
    assert sanity["expected"]["sha256"] != private_expected_sha256()
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "aggregate_statistics_only": True,
    }
    assert sanity["summary"]["case_count"] == 767
    assert sanity["summary"]["accepted"] == 715
    assert sanity["summary"]["misses"] == 52
    assert sanity["summary"]["primary_exact"] == 552
    assert sanity["summary"]["acceptable_exact"] == 163
    assert sanity["summary"]["accepted_accuracy"] == 0.9322033898305084
    assert sanity["summary"]["primary_exact_accuracy"] == 0.7196870925684485
    assert sanity["summary"]["idempotency_rate"] == 0.9830508474576272
    assert sanity["summary"]["accepted_accuracy_ci_95"] == {
        "low": 0.9139504563233377,
        "high": 0.9491525423728814,
    }
    assert sanity["summary"]["by_domain"] == {
        "formal": {
            "total": 125,
            "accepted": 116,
            "accepted_accuracy": 0.928,
        },
        "high_risk": {
            "total": 86,
            "accepted": 78,
            "accepted_accuracy": 0.9069767441860465,
        },
        "it": {
            "total": 149,
            "accepted": 137,
            "accepted_accuracy": 0.9194630872483222,
        },
        "llm": {
            "total": 126,
            "accepted": 120,
            "accepted_accuracy": 0.9523809523809523,
        },
        "social": {
            "total": 129,
            "accepted": 123,
            "accepted_accuracy": 0.9534883720930233,
        },
        "ui": {
            "total": 152,
            "accepted": 141,
            "accepted_accuracy": 0.9276315789473685,
        },
    }
    assert sanity["summary"]["by_risk"] == {
        "baseline_guard": 122,
        "candidate_gap": 432,
        "over_conversion_guard": 213,
    }
    assert sanity["summary"]["misses_by_risk"] == {
        "baseline_guard": 4,
        "candidate_gap": 19,
        "over_conversion_guard": 29,
    }
    assert sanity["summary"]["misses_by_issue_tag"] == {
        "baseline_guard": 4,
        "candidate_gap": 18,
        "formal_term": 13,
        "high_risk_term": 8,
        "it_term": 14,
        "llm_term": 2,
        "over_conversion": 29,
        "regional_term": 52,
        "social_term": 1,
        "ui_term": 11,
    }


def test_private_benchmark_sanity_after_batch11_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH11)
    final_decision = load_json(MAINTAINER_BATCH11_FINAL_DECISION)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch11_final_decision"
    assert sanity["expected_values_included"] is False
    assert sanity["acceptable_values_included"] is False
    assert sanity["rows_included"] is False
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert "rows" not in sanity
    assert sanity["source_final_decision"] == str(
        MAINTAINER_BATCH11_FINAL_DECISION.relative_to(ROOT)
    )
    assert sanity["source_benchmark"] == {
        "path": "/tmp/zhtw-blind-v1-private-benchmark-after-batch11-2026-07-14.json",
        "in_repo": False,
        "rows_used_for_aggregate_only": True,
    }
    assert sanity["inputs"]["sha256"] == (
        "e7018d35e078a53ff1c59e4a8281b787151fd11c158859ad882defc82b93aff9"
    )
    assert sanity["inputs"]["sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert sanity["expected"]["sha256"] == (
        "bbf89dfa8db7774fdd9b8c078f97d18b9b3749f164d5f4e7cc109bb8ac0ab096"
    )
    assert sanity["expected"]["sha256"] != private_expected_sha256()
    assert sanity["expected"]["sha256"] == final_decision["private_expected_sha256"]
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"]["aggregate_statistics_only"] is True
    assert sanity["summary"]["case_count"] == 851
    assert sanity["summary"]["accepted"] == 791
    assert sanity["summary"]["misses"] == 60
    assert sanity["summary"]["primary_exact"] == 624
    assert sanity["summary"]["acceptable_exact"] == 167
    assert sanity["summary"]["accepted_accuracy"] == 0.9294947121034077
    assert sanity["summary"]["primary_exact_accuracy"] == 0.7332549941245593
    assert sanity["summary"]["idempotency_rate"] == 0.9835487661574618
    assert sanity["summary"]["misses_by_risk"] == {
        "baseline_guard": 4,
        "candidate_gap": 20,
        "over_conversion_guard": 36,
    }


def test_private_benchmark_sanity_after_batch11_semantic_reaudit_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH11_SEMANTIC_REAUDIT)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch11_semantic_reaudit"
    assert sanity["expected_values_included"] is False
    assert sanity["acceptable_values_included"] is False
    assert sanity["rows_included"] is False
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs"]["sha256"] == (
        "3c35b332959c7a87410a0ba7c08d46aa98857b1c080155d275a8892d0f507fef"
    )
    assert sanity["inputs"]["sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert sanity["expected"]["sha256"] == (
        "066bcd60d16760a10eb8cdd54de61e8ff438fe4a7ffe971e8f814fc45563db2d"
    )
    assert sanity["expected"]["sha256"] != private_expected_sha256()
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"]["aggregate_statistics_only"] is True
    assert sanity["summary"]["case_count"] == 841
    assert sanity["summary"]["accepted"] == 795
    assert sanity["summary"]["misses"] == 46
    assert sanity["summary"]["primary_exact"] == 624
    assert sanity["summary"]["acceptable_exact"] == 171
    assert sanity["summary"]["accepted_accuracy"] == 0.9453032104637337
    assert sanity["summary"]["misses_by_risk"] == {
        "baseline_guard": 3,
        "candidate_gap": 11,
        "over_conversion_guard": 32,
    }


def test_private_benchmark_sanity_after_batch12_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH12)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch12_final_decision"
    assert sanity["expected_values_included"] is False
    assert sanity["acceptable_values_included"] is False
    assert sanity["rows_included"] is False
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert "rows" not in sanity
    assert sanity["inputs"]["sha256"] == (
        "c1082299113239bfe88590425ccd6c4b4b0f0d769ddea18ce457a11050863deb"
    )
    assert sanity["inputs"]["sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert sanity["expected"]["sha256"] == (
        "617f048425d75605e1997b8952432792f417444b3c4facec89bc5bd7a160dd22"
    )
    assert sanity["expected"]["sha256"] != private_expected_sha256()
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"]["aggregate_statistics_only"] is True
    assert sanity["summary"]["case_count"] == 941
    assert sanity["summary"]["accepted"] == 880
    assert sanity["summary"]["misses"] == 61
    assert sanity["summary"]["accepted_accuracy"] == 0.9351753453772582
    assert sanity["batch12_summary"]["case_count"] == 100
    assert sanity["batch12_summary"]["accepted"] == 85
    assert sanity["batch12_summary"]["misses"] == 15
    assert sanity["batch12_summary"]["accepted_accuracy"] == 0.85


def test_private_benchmark_sanity_after_batch12_miss_review_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH12_MISS_REVIEW)

    assert sanity["report_type"] == "private_benchmark_sanity_summary"
    assert sanity["review_stage"] == "after_batch12_miss_review"
    assert sanity["inputs"]["sha256"] == (
        "9297eaf5688b87b0d89d83dceb04f9ce3fa62944f6cbde83b485bc0524e7f780"
    )
    assert sanity["inputs"]["sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert sanity["expected"]["sha256"] == (
        "81246822bffc1423b1460b0bfe7f1ed2539060f31880f8b49424e85c25b6052e"
    )
    assert sanity["expected"]["sha256"] != private_expected_sha256()
    assert sanity["expected"]["source_inputs_sha256"] == sanity["inputs"]["sha256"]
    assert sanity["sealed_content_policy"]["aggregate_statistics_only"] is True
    assert sanity["interpretation_policy"] == {
        "pure_capability_gain_claimed": False,
        "acceptable_variants_added": 4,
        "cases_removed_before_tuning": 11,
        "denominator_changed": True,
    }
    assert sanity["summary"]["case_count"] == 930
    assert sanity["summary"]["accepted"] == 884
    assert sanity["summary"]["misses"] == 46
    assert sanity["summary"]["accepted_accuracy"] == 0.9505376344086022
    assert sanity["summary"]["misses_by_risk"] == {
        "baseline_guard": 3,
        "candidate_gap": 11,
        "over_conversion_guard": 32,
    }
    for key in (
        "expected_values_included",
        "acceptable_values_included",
        "rows_included",
        "inputs_included",
        "outputs_included",
        "benchmark_rows_included",
    ):
        assert sanity[key] is False
    assert "rows" not in sanity


def test_private_benchmark_sanity_after_batch10_miss_review_is_sanitized() -> None:
    sanity = load_json(PRIVATE_BENCHMARK_SANITY_AFTER_BATCH10_MISS_REVIEW)
    final_decision = load_json(MAINTAINER_BATCH10_MISS_FINAL_DECISION)

    assert sanity["report_type"] == "holdout_private_benchmark_sanity"
    assert sanity["review_stage"] == "after_batch10_miss_review"
    assert sanity["expected_values_included"] is False
    assert sanity["acceptable_values_included"] is False
    assert sanity["inputs_included"] is False
    assert sanity["outputs_included"] is False
    assert sanity["benchmark_rows_included"] is False
    assert "rows" not in sanity
    assert sanity["source_final_decision"] == str(
        MAINTAINER_BATCH10_MISS_FINAL_DECISION.relative_to(ROOT)
    )
    assert sanity["summary"]["source_inputs_sha256"] == (
        "e6d6e8a2d0b5f9fdffaee7cc7c467cab74210eed62db0202d287bceceb2d02bf"
    )
    assert (
        sanity["summary"]["source_inputs_sha256"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    )
    assert sanity["summary"]["private_expected_sha256"] == (
        "5c89d5037efcbc33c80dd86f35ccfd12102a709fe701820b9d318fa1f8fe49dc"
    )
    assert sanity["summary"]["private_expected_sha256"] != private_expected_sha256()
    assert (
        sanity["summary"]["private_expected_sha256"]
        == (final_decision["private_expected_sha256_after"])
    )
    assert sanity["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "case_ids_and_metadata_only": False,
        "aggregate_statistics_only": True,
    }
    assert sanity["summary"]["case_count"] == 751
    assert sanity["summary"]["accepted"] == 719
    assert sanity["summary"]["misses"] == 32
    assert sanity["summary"]["accepted_accuracy"] == 0.9573901464713716
    assert sanity["summary"]["primary_exact"] == 552
    assert sanity["summary"]["acceptable_exact"] == 167
    assert sanity["summary"]["miss_by_risk"] == {
        "baseline_guard": 1,
        "candidate_gap": 2,
        "over_conversion_guard": 29,
    }
    assert sanity["summary"]["miss_by_domain"] == {
        "formal": 6,
        "high_risk": 8,
        "it": 3,
        "llm": 4,
        "social": 6,
        "ui": 5,
    }


def test_holdout_426_case_miss_classification_omits_sealed_values() -> None:
    report = load_json(MISS_CLASSIFICATION_426_CASE)

    assert report["report_type"] == "holdout_miss_classification_426_case_sanity"
    assert report["review_stage"] == "private_miss_classification_first_pass_after_batch6"
    assert report["reviewer"] == "codex"
    assert report["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "case_ids_and_metadata_only": True,
    }
    assert report["gemini_review_policy"] == {
        "status": "completed_on_sanitized_metadata",
        "review_report": (
            "docs/reports/"
            "holdout-gemini-policy-review-miss-classification-blind-v1-426-cases-2026-07-10.json"
        ),
        "sealed_values_seen_by_gemini": False,
        "policy_passed": True,
        "classification_changes_recommended": 0,
        "reason": (
            "Gemini reviewed case ids and classification metadata only; private expected, "
            "inputs, and converter outputs were not sent."
        ),
    }
    assert report["summary"] == {
        "current_sealed_cases": 426,
        "current_accepted": 389,
        "current_misses": 37,
        "accepted_accuracy": 0.9131455399061033,
        "classified_misses": 37,
        "by_action": {
            "keep_as_holdout_signal": 24,
            "move_to_public_regression_candidate": 11,
            "requires_expected_recheck": 2,
        },
        "by_priority": {"P1": 2, "P2": 35},
        "by_domain_action": {
            "formal": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
            "high_risk": {
                "keep_as_holdout_signal": 3,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
            "it": {
                "keep_as_holdout_signal": 3,
                "move_to_public_regression_candidate": 10,
                "requires_expected_recheck": 0,
            },
            "llm": {
                "keep_as_holdout_signal": 4,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 1,
            },
            "social": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
            "ui": {
                "keep_as_holdout_signal": 4,
                "move_to_public_regression_candidate": 1,
                "requires_expected_recheck": 1,
            },
        },
        "by_risk_action": {
            "baseline_guard": {
                "keep_as_holdout_signal": 0,
                "move_to_public_regression_candidate": 1,
                "requires_expected_recheck": 0,
            },
            "candidate_gap": {
                "keep_as_holdout_signal": 0,
                "move_to_public_regression_candidate": 10,
                "requires_expected_recheck": 2,
            },
            "over_conversion_guard": {
                "keep_as_holdout_signal": 24,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
        },
        "idempotency_followup_cases": 1,
        "expected_recheck_cases": 2,
        "safe_public_candidate_cases": 11,
        "holdout_signal_cases": 24,
        "high_risk_cases": 3,
        "over_conversion_guard_cases": 24,
    }
    forbidden_case_fields = {
        "acceptable",
        "actual",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    cases = report["case_classifications"]
    assert len(cases) == 37
    assert len({case["id"] for case in cases}) == len(cases)
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["id"].startswith("blind-")
        assert case["action"] in report["summary"]["by_action"]
        assert case["reason_code"]
        assert case["next_step"]

    action_by_id = {case["id"]: case["action"] for case in cases}
    assert action_by_id["blind-it-0124"] == "move_to_public_regression_candidate"
    assert action_by_id["blind-ui-0096"] == "requires_expected_recheck"
    assert action_by_id["blind-llm-0071"] == "requires_expected_recheck"
    assert action_by_id["blind-high-risk-0039"] == "keep_as_holdout_signal"
    assert report["idempotency_notes"]["non_idempotent_miss_ids"] == ["blind-it-0124"]


def test_gemini_426_case_miss_classification_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_MISS_CLASSIFICATION_426_POLICY_REVIEW)

    assert review["reviewer"] == "gemini_cli"
    assert review["model_requested"] == "gemini-2.5-flash"
    assert review["review_stage"] == "sanitized_miss_classification_policy_review_after_batch6"
    assert review["source_classification_report"] == (
        "docs/reports/holdout-miss-classification-blind-v1-426-cases-2026-07-10.json"
    )
    assert review["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "gemini_received_sanitized_metadata_only": True,
    }
    assert review["policy_passed"] is True
    assert review["classification_changes_recommended"] == []
    assert len(review["findings"]) == 3
    assert {finding["case_id"] for finding in review["findings"]} == {
        "blind-it-0124",
        "blind-ui-0096",
        "blind-llm-0071",
    }


def test_holdout_batch6_miss_classification_confirmation_packet_is_sanitized() -> None:
    classification = load_json(MISS_CLASSIFICATION_426_CASE)
    packet = load_json(MAINTAINER_BATCH6_MISS_CLASSIFICATION_CONFIRMATION)

    review_ids = {
        case["id"]
        for case in classification["case_classifications"]
        if case["action"] in {"move_to_public_regression_candidate", "requires_expected_recheck"}
    }
    holdout_signal_ids = {
        case["id"]
        for case in classification["case_classifications"]
        if case["action"] == "keep_as_holdout_signal"
    }

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch6_miss_classification_after_426_case_sanity"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["sealed_content_policy"] == classification["sealed_content_policy"]
    assert packet["summary"] == {
        "total_review_cases": 13,
        "public_regression_candidate_cases": 11,
        "expected_recheck_cases": 2,
        "no_immediate_question": 24,
        "gemini_policy_passed": True,
        "classification_changes_recommended_by_gemini": 0,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in packet["cases"]} == review_ids
    assert set(packet["no_immediate_question_case_ids"]) == holdout_signal_ids
    assert len(packet["cases"]) == 13
    assert len(packet["no_immediate_question_case_ids"]) == 24
    assert all(case["sealed_values_omitted"] is True for case in packet["cases"])


def test_holdout_515_case_miss_classification_omits_sealed_values() -> None:
    report = load_json(MISS_CLASSIFICATION_515_CASE)

    assert report["report_type"] == "holdout_miss_classification_515_case_sanity"
    assert report["review_stage"] == "private_miss_classification_first_pass_after_batch7"
    assert report["reviewer"] == "codex"
    assert report["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "case_ids_and_metadata_only": True,
    }
    assert report["gemini_review_policy"] == {
        "status": "completed_on_sanitized_metadata",
        "review_report": (
            "docs/reports/"
            "holdout-gemini-policy-review-miss-classification-blind-v1-515-cases-2026-07-10.json"
        ),
        "sealed_values_seen_by_gemini": False,
        "policy_passed": True,
        "classification_changes_recommended": 0,
        "reason": (
            "Gemini reviewed case ids and classification metadata only; private expected, "
            "inputs, and converter outputs were not sent. GEMINI_API_KEY was unset for "
            "this CLI run to avoid invalid API-key mode."
        ),
    }
    assert report["summary"] == {
        "current_sealed_cases": 515,
        "current_accepted": 465,
        "current_misses": 50,
        "accepted_accuracy": 0.9029126213592233,
        "classified_misses": 50,
        "by_action": {
            "keep_as_holdout_signal": 26,
            "move_to_public_regression_candidate": 17,
            "requires_expected_recheck": 7,
        },
        "by_priority": {"P1": 7, "P2": 43},
        "by_domain_action": {
            "formal": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 1,
                "requires_expected_recheck": 0,
            },
            "high_risk": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
            "it": {
                "keep_as_holdout_signal": 3,
                "move_to_public_regression_candidate": 11,
                "requires_expected_recheck": 4,
            },
            "llm": {
                "keep_as_holdout_signal": 4,
                "move_to_public_regression_candidate": 2,
                "requires_expected_recheck": 0,
            },
            "social": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 1,
                "requires_expected_recheck": 0,
            },
            "ui": {
                "keep_as_holdout_signal": 4,
                "move_to_public_regression_candidate": 2,
                "requires_expected_recheck": 3,
            },
        },
        "by_risk_action": {
            "baseline_guard": {
                "keep_as_holdout_signal": 0,
                "move_to_public_regression_candidate": 2,
                "requires_expected_recheck": 0,
            },
            "candidate_gap": {
                "keep_as_holdout_signal": 1,
                "move_to_public_regression_candidate": 15,
                "requires_expected_recheck": 7,
            },
            "over_conversion_guard": {
                "keep_as_holdout_signal": 25,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
        },
        "idempotency_followup_cases": 5,
        "expected_recheck_cases": 7,
        "safe_public_candidate_cases": 17,
        "holdout_signal_cases": 26,
        "high_risk_cases": 5,
        "over_conversion_guard_cases": 25,
    }
    forbidden_case_fields = {
        "acceptable",
        "actual",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    cases = report["case_classifications"]
    assert len(cases) == 50
    assert len({case["id"] for case in cases}) == len(cases)
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["id"].startswith("blind-")
        assert case["action"] in report["summary"]["by_action"]
        assert case["reason_code"]
        assert case["next_step"]

    action_by_id = {case["id"]: case["action"] for case in cases}
    assert action_by_id["blind-it-0142"] == "move_to_public_regression_candidate"
    assert action_by_id["blind-it-0148"] == "requires_expected_recheck"
    assert action_by_id["blind-ui-0108"] == "requires_expected_recheck"
    assert action_by_id["blind-high-risk-0053"] == "keep_as_holdout_signal"
    assert report["idempotency_notes"]["non_idempotent_miss_ids"] == [
        "blind-it-0142",
        "blind-it-0152",
        "blind-it-0155",
        "blind-ui-0123",
        "blind-social-0079",
    ]


def test_gemini_515_case_miss_classification_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_MISS_CLASSIFICATION_515_POLICY_REVIEW)

    assert review["reviewer"] == "gemini_cli"
    assert review["model_requested"] == "gemini-2.5-flash"
    assert review["review_stage"] == "sanitized_miss_classification_policy_review_after_batch7"
    assert review["source_classification_report"] == (
        "docs/reports/holdout-miss-classification-blind-v1-515-cases-2026-07-10.json"
    )
    assert review["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "gemini_received_sanitized_metadata_only": True,
    }
    assert review["policy_passed"] is True
    assert review["classification_changes_recommended"] == []
    assert len(review["findings"]) == 5
    assert {finding["case_id"] for finding in review["findings"]} == {
        "over_conversion_guard_cases",
        "high_risk_cases",
        "public_regression_candidate_cases",
        "expected_recheck_cases",
        "non_idempotent_miss_ids",
    }


def test_holdout_batch7_miss_classification_confirmation_packet_is_sanitized() -> None:
    classification = load_json(MISS_CLASSIFICATION_515_CASE)
    packet = load_json(MAINTAINER_BATCH7_MISS_CLASSIFICATION_CONFIRMATION)

    review_ids = {
        case["id"]
        for case in classification["case_classifications"]
        if case["action"] in {"move_to_public_regression_candidate", "requires_expected_recheck"}
    }
    holdout_signal_ids = {
        case["id"]
        for case in classification["case_classifications"]
        if case["action"] == "keep_as_holdout_signal"
    }

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch7_miss_classification_after_515_case_sanity"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["sealed_content_policy"] == classification["sealed_content_policy"]
    assert packet["summary"] == {
        "total_review_cases": 24,
        "public_regression_candidate_cases": 17,
        "expected_recheck_cases": 7,
        "no_immediate_question": 26,
        "gemini_policy_passed": True,
        "classification_changes_recommended_by_gemini": 0,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in packet["cases"]} == review_ids
    assert set(packet["no_immediate_question_case_ids"]) == holdout_signal_ids
    assert len(packet["cases"]) == 24
    assert len(packet["no_immediate_question_case_ids"]) == 26
    assert all(case["sealed_values_omitted"] is True for case in packet["cases"])


def test_holdout_598_case_miss_classification_omits_sealed_values() -> None:
    report = load_json(MISS_CLASSIFICATION_598_CASE)

    assert report["report_type"] == "holdout_miss_classification_598_case_sanity"
    assert report["review_stage"] == "private_miss_classification_first_pass_after_batch8"
    assert report["reviewer"] == "codex"
    assert report["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "case_ids_and_metadata_only": True,
    }
    assert report["gemini_review_policy"]["status"] == "completed_on_sanitized_metadata"
    assert report["gemini_review_policy"]["review_report"] == (
        "docs/reports/"
        "holdout-gemini-policy-review-miss-classification-blind-v1-598-cases-2026-07-10.json"
    )
    assert report["gemini_review_policy"]["sealed_values_seen_by_gemini"] is False
    assert report["gemini_review_policy"]["policy_passed"] is True
    assert report["gemini_review_policy"]["classification_changes_recommended"] == 0
    assert report["summary"] == {
        "current_sealed_cases": 598,
        "current_accepted": 549,
        "current_misses": 49,
        "accepted_accuracy": 0.9180602006688964,
        "classified_misses": 49,
        "by_action": {
            "keep_as_holdout_signal": 30,
            "move_to_public_regression_candidate": 15,
            "requires_expected_recheck": 4,
        },
        "by_priority": {"P1": 5, "P2": 44},
        "by_domain_action": {
            "formal": {
                "keep_as_holdout_signal": 6,
                "move_to_public_regression_candidate": 1,
                "requires_expected_recheck": 0,
            },
            "high_risk": {
                "keep_as_holdout_signal": 7,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
            "it": {
                "keep_as_holdout_signal": 3,
                "move_to_public_regression_candidate": 8,
                "requires_expected_recheck": 2,
            },
            "llm": {
                "keep_as_holdout_signal": 4,
                "move_to_public_regression_candidate": 1,
                "requires_expected_recheck": 1,
            },
            "social": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 1,
            },
            "ui": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 5,
                "requires_expected_recheck": 0,
            },
        },
        "by_risk_action": {
            "baseline_guard": {
                "keep_as_holdout_signal": 1,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
            "candidate_gap": {
                "keep_as_holdout_signal": 2,
                "move_to_public_regression_candidate": 15,
                "requires_expected_recheck": 4,
            },
            "over_conversion_guard": {
                "keep_as_holdout_signal": 27,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
        },
        "idempotency_followup_cases": 2,
        "expected_recheck_cases": 4,
        "safe_public_candidate_cases": 15,
        "holdout_signal_cases": 30,
        "high_risk_cases": 7,
        "over_conversion_guard_cases": 27,
    }
    forbidden_case_fields = {
        "acceptable",
        "actual",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    cases = report["case_classifications"]
    assert len(cases) == 49
    assert len({case["id"] for case in cases}) == len(cases)
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["id"].startswith("blind-")
        assert case["action"] in report["summary"]["by_action"]
        assert case["reason_code"]
        assert case["next_step"]

    action_by_id = {case["id"]: case["action"] for case in cases}
    assert action_by_id["blind-it-0165"] == "move_to_public_regression_candidate"
    assert action_by_id["blind-formal-0101"] == "move_to_public_regression_candidate"
    assert action_by_id["blind-it-0167"] == "requires_expected_recheck"
    assert action_by_id["blind-social-0095"] == "requires_expected_recheck"
    assert action_by_id["blind-high-risk-0068"] == "keep_as_holdout_signal"
    assert report["idempotency_notes"]["non_idempotent_miss_ids"] == [
        "blind-it-0174",
        "blind-ui-0147",
    ]


def test_gemini_598_case_miss_classification_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_MISS_CLASSIFICATION_598_POLICY_REVIEW)

    assert review["reviewer"] == "gemini_cli"
    assert review["model_requested"] == "gemini-2.5-flash"
    assert review["review_stage"] == "gemini_policy_review_batch8_miss_classification"
    assert review["source_classification_report"] == (
        "docs/reports/holdout-miss-classification-blind-v1-598-cases-2026-07-10.json"
    )
    assert review["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "case_ids_and_metadata_only": True,
        "sealed_values_seen_by_gemini": False,
    }
    assert review["policy_passed"] is True
    assert review["classification_changes_recommended"] == []
    assert {finding["case_id"] for finding in review["findings"]} == {
        "blind-it-0174",
        "blind-ui-0147",
    }


def test_holdout_batch8_miss_classification_confirmation_packet_is_sanitized() -> None:
    classification = load_json(MISS_CLASSIFICATION_598_CASE)
    packet = load_json(MAINTAINER_BATCH8_MISS_CLASSIFICATION_CONFIRMATION)

    review_ids = {
        case["id"]
        for case in classification["case_classifications"]
        if case["action"] in {"move_to_public_regression_candidate", "requires_expected_recheck"}
    }
    holdout_signal_ids = {
        case["id"]
        for case in classification["case_classifications"]
        if case["action"] == "keep_as_holdout_signal"
    }

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch8_miss_classification"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["sealed_content_policy"] == classification["sealed_content_policy"]
    assert packet["summary"] == {
        "total_review_cases": 19,
        "public_regression_candidate_cases": 15,
        "expected_recheck_cases": 4,
        "no_immediate_question": 30,
        "gemini_policy_passed": True,
        "classification_changes_recommended_by_gemini": 0,
        "by_action": {
            "move_to_public_regression_candidate": 15,
            "requires_expected_recheck": 4,
        },
        "by_domain": {
            "formal": 1,
            "it": 10,
            "llm": 2,
            "social": 1,
            "ui": 5,
        },
        "by_risk": {
            "candidate_gap": 19,
        },
        "non_idempotent_review_cases": 1,
    }
    assert {case["id"] for case in packet["cases"]} == review_ids
    assert set(packet["no_immediate_question_case_ids"]) == holdout_signal_ids
    assert len(packet["cases"]) == 19
    assert len(packet["no_immediate_question_case_ids"]) == 30
    assert all(case["sealed_values_omitted"] is True for case in packet["cases"])


def test_holdout_683_case_miss_classification_omits_sealed_values() -> None:
    report = load_json(MISS_CLASSIFICATION_683_CASE)

    assert report["report_type"] == "holdout_miss_classification_683_case_sanity"
    assert report["review_stage"] == "private_miss_classification_first_pass_after_batch9"
    assert report["reviewer"] == "codex"
    assert report["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "case_ids_and_metadata_only": True,
    }
    assert report["gemini_review_policy"]["status"] == "completed_on_sanitized_metadata"
    assert report["gemini_review_policy"]["review_report"] == (
        "docs/reports/"
        "holdout-gemini-policy-review-miss-classification-blind-v1-683-cases-2026-07-12.json"
    )
    assert report["gemini_review_policy"]["sealed_values_seen_by_gemini"] is False
    assert report["gemini_review_policy"]["policy_passed"] is True
    assert report["gemini_review_policy"]["classification_changes_recommended"] == 0
    assert report["summary"] == {
        "current_sealed_cases": 683,
        "current_accepted": 630,
        "current_misses": 53,
        "accepted_accuracy": 0.9224011713030746,
        "classified_misses": 53,
        "by_action": {
            "keep_as_holdout_signal": 31,
            "move_to_public_regression_candidate": 16,
            "requires_expected_recheck": 6,
        },
        "by_priority": {"P1": 10, "P2": 43},
        "by_domain_action": {
            "formal": {
                "keep_as_holdout_signal": 6,
                "move_to_public_regression_candidate": 2,
                "requires_expected_recheck": 0,
            },
            "high_risk": {
                "keep_as_holdout_signal": 7,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
            "it": {
                "keep_as_holdout_signal": 3,
                "move_to_public_regression_candidate": 8,
                "requires_expected_recheck": 4,
            },
            "llm": {
                "keep_as_holdout_signal": 4,
                "move_to_public_regression_candidate": 2,
                "requires_expected_recheck": 0,
            },
            "social": {
                "keep_as_holdout_signal": 6,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
            "ui": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 4,
                "requires_expected_recheck": 2,
            },
        },
        "by_risk_action": {
            "baseline_guard": {
                "keep_as_holdout_signal": 1,
                "move_to_public_regression_candidate": 2,
                "requires_expected_recheck": 0,
            },
            "candidate_gap": {
                "keep_as_holdout_signal": 2,
                "move_to_public_regression_candidate": 14,
                "requires_expected_recheck": 6,
            },
            "over_conversion_guard": {
                "keep_as_holdout_signal": 28,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
        },
        "idempotency_followup_cases": 3,
        "expected_recheck_cases": 6,
        "safe_public_candidate_cases": 16,
        "holdout_signal_cases": 31,
        "high_risk_cases": 7,
        "over_conversion_guard_cases": 28,
    }
    forbidden_case_fields = {
        "acceptable",
        "actual",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    cases = report["case_classifications"]
    assert len(cases) == 53
    assert len({case["id"] for case in cases}) == len(cases)
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["id"].startswith("blind-")
        assert case["action"] in report["summary"]["by_action"]
        assert case["reason_code"]
        assert case["next_step"]

    action_by_id = {case["id"]: case["action"] for case in cases}
    assert action_by_id["blind-it-0190"] == "move_to_public_regression_candidate"
    assert action_by_id["blind-formal-0115"] == "move_to_public_regression_candidate"
    assert action_by_id["blind-it-0189"] == "requires_expected_recheck"
    assert action_by_id["blind-ui-0166"] == "requires_expected_recheck"
    assert action_by_id["blind-social-0110"] == "keep_as_holdout_signal"
    assert report["idempotency_notes"]["non_idempotent_miss_ids"] == [
        "blind-ui-0147",
        "blind-it-0190",
        "blind-it-0200",
    ]


def test_gemini_683_case_miss_classification_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_MISS_CLASSIFICATION_683_POLICY_REVIEW)

    assert review["reviewer"] == "gemini_cli"
    assert review["model_requested"] == "gemini-2.5-flash"
    assert review["review_stage"] == "gemini_policy_review_batch9_miss_classification"
    assert review["source_classification_report"] == (
        "docs/reports/holdout-miss-classification-blind-v1-683-cases-2026-07-12.json"
    )
    assert review["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "case_ids_and_metadata_only": True,
        "sealed_values_seen_by_gemini": False,
    }
    assert review["policy_passed"] is True
    assert review["classification_changes_recommended"] == []
    assert {finding["case_id"] for finding in review["findings"]} == {
        "blind-ui-0147",
        "blind-it-0190",
        "blind-it-0200",
    }


def test_holdout_batch9_miss_classification_confirmation_packet_is_sanitized() -> None:
    classification = load_json(MISS_CLASSIFICATION_683_CASE)
    packet = load_json(MAINTAINER_BATCH9_MISS_CLASSIFICATION_CONFIRMATION)

    review_ids = {
        case["id"]
        for case in classification["case_classifications"]
        if case["action"] in {"move_to_public_regression_candidate", "requires_expected_recheck"}
    }
    holdout_signal_ids = {
        case["id"]
        for case in classification["case_classifications"]
        if case["action"] == "keep_as_holdout_signal"
    }

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch9_miss_classification"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["sealed_content_policy"] == classification["sealed_content_policy"]
    assert packet["summary"] == {
        "total_review_cases": 22,
        "public_regression_candidate_cases": 16,
        "expected_recheck_cases": 6,
        "no_immediate_question": 31,
        "gemini_policy_passed": True,
        "classification_changes_recommended_by_gemini": 0,
        "by_action": {
            "move_to_public_regression_candidate": 16,
            "requires_expected_recheck": 6,
        },
        "by_domain": {
            "formal": 2,
            "it": 12,
            "llm": 2,
            "ui": 6,
        },
        "by_risk": {
            "baseline_guard": 2,
            "candidate_gap": 20,
        },
        "non_idempotent_review_cases": 2,
    }
    assert {case["id"] for case in packet["cases"]} == review_ids
    assert set(packet["no_immediate_question_case_ids"]) == holdout_signal_ids
    assert len(packet["cases"]) == 22
    assert len(packet["no_immediate_question_case_ids"]) == 31
    assert all(case["sealed_values_omitted"] is True for case in packet["cases"])


def test_holdout_767_case_miss_classification_omits_sealed_values() -> None:
    report = load_json(MISS_CLASSIFICATION_767_CASE)

    assert report["report_type"] == "holdout_miss_classification_767_case_sanity"
    assert report["review_stage"] == "private_miss_classification_first_pass_after_batch10"
    assert report["reviewer"] == "codex"
    assert report["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "case_ids_and_metadata_only": True,
    }
    assert report["gemini_review_policy"]["status"] == "completed_on_sanitized_metadata"
    assert report["gemini_review_policy"]["review_report"] == (
        "docs/reports/"
        "holdout-gemini-policy-review-miss-classification-blind-v1-767-cases-2026-07-12.json"
    )
    assert report["gemini_review_policy"]["sealed_values_seen_by_gemini"] is False
    assert report["gemini_review_policy"]["policy_passed"] is True
    assert report["gemini_review_policy"]["classification_changes_recommended"] == 0
    assert report["summary"] == {
        "current_sealed_cases": 767,
        "current_accepted": 715,
        "current_misses": 52,
        "accepted_accuracy": 0.9322033898305084,
        "classified_misses": 52,
        "by_action": {
            "keep_as_holdout_signal": 32,
            "move_to_public_regression_candidate": 16,
            "requires_expected_recheck": 4,
        },
        "by_priority": {"P1": 28, "P2": 24},
        "by_domain_action": {
            "formal": {
                "keep_as_holdout_signal": 6,
                "move_to_public_regression_candidate": 3,
                "requires_expected_recheck": 0,
            },
            "high_risk": {
                "keep_as_holdout_signal": 8,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
            "it": {
                "keep_as_holdout_signal": 3,
                "move_to_public_regression_candidate": 7,
                "requires_expected_recheck": 2,
            },
            "llm": {
                "keep_as_holdout_signal": 4,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 2,
            },
            "social": {
                "keep_as_holdout_signal": 6,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
            "ui": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 6,
                "requires_expected_recheck": 0,
            },
        },
        "by_risk_action": {
            "baseline_guard": {
                "keep_as_holdout_signal": 1,
                "move_to_public_regression_candidate": 3,
                "requires_expected_recheck": 0,
            },
            "candidate_gap": {
                "keep_as_holdout_signal": 2,
                "move_to_public_regression_candidate": 13,
                "requires_expected_recheck": 4,
            },
            "over_conversion_guard": {
                "keep_as_holdout_signal": 29,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
        },
        "idempotency_followup_cases": 2,
        "expected_recheck_cases": 4,
        "safe_public_candidate_cases": 16,
        "holdout_signal_cases": 32,
        "high_risk_cases": 8,
        "over_conversion_guard_cases": 29,
    }
    forbidden_case_fields = {
        "acceptable",
        "actual",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    cases = report["case_classifications"]
    assert len(cases) == 52
    assert len({case["id"] for case in cases}) == len(cases)
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["id"].startswith("blind-")
        action = case.get("action", case.get("recommended_action"))
        assert action in report["summary"]["by_action"]
        assert case["reason_code"]
        assert case["sealed_values_omitted"] is True

    action_by_id = {
        case["id"]: case.get("action", case.get("recommended_action")) for case in cases
    }
    assert action_by_id["blind-it-0217"] == "move_to_public_regression_candidate"
    assert action_by_id["blind-formal-0129"] == "move_to_public_regression_candidate"
    assert action_by_id["blind-it-0222"] == "requires_expected_recheck"
    assert action_by_id["blind-llm-0123"] == "requires_expected_recheck"
    assert action_by_id["blind-llm-0137"] == "requires_expected_recheck"
    assert action_by_id["blind-social-0110"] == "keep_as_holdout_signal"
    assert [case["id"] for case in report["idempotency_notes"]] == [
        "blind-ui-0147",
        "blind-it-0230",
    ]


def test_gemini_767_case_miss_classification_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_MISS_CLASSIFICATION_767_POLICY_REVIEW)

    assert review["reviewer"] == "gemini_cli"
    assert review["model_requested"] == "gemini-2.5-flash"
    assert review["review_stage"] == "sanitized_miss_classification_policy_review_after_batch10"
    assert review["source_classification_report"] == (
        "docs/reports/holdout-miss-classification-blind-v1-767-cases-2026-07-12.json"
    )
    assert review["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "benchmark_rows_included": False,
        "case_ids_and_metadata_only": True,
        "sealed_values_seen_by_gemini": False,
    }
    assert review["policy_passed"] is True
    assert review["classification_changes_recommended"] == []
    assert {finding.get("case_id", finding.get("id")) for finding in review["findings"]} == {
        "expected-rechecks",
        "blind-ui-0147",
        "blind-it-0230",
    }


def test_holdout_batch10_miss_classification_confirmation_packet_is_sanitized() -> None:
    classification = load_json(MISS_CLASSIFICATION_767_CASE)
    packet = load_json(MAINTAINER_BATCH10_MISS_CLASSIFICATION_CONFIRMATION)

    review_ids = {
        case["id"]
        for case in classification["case_classifications"]
        if case.get("action", case.get("recommended_action"))
        in {"move_to_public_regression_candidate", "requires_expected_recheck"}
    }
    holdout_signal_ids = {
        case["id"]
        for case in classification["case_classifications"]
        if case.get("action", case.get("recommended_action")) == "keep_as_holdout_signal"
    }

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch10_miss_classification_after_767_case_sanity"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["sealed_content_policy"] | {
        "benchmark_rows_included": False,
    } == classification["sealed_content_policy"] | {
        "benchmark_rows_included": False,
    }
    assert packet["summary"] == {
        "total_review_cases": 20,
        "public_regression_candidate_cases": 16,
        "expected_recheck_cases": 4,
        "no_immediate_question": 32,
        "gemini_policy_passed": True,
        "classification_changes_recommended_by_gemini": 0,
        "gemini_info_findings": 3,
        "by_action": {
            "move_to_public_regression_candidate": 16,
            "requires_expected_recheck": 4,
        },
        "by_domain": {
            "formal": 3,
            "it": 9,
            "llm": 2,
            "ui": 6,
        },
        "by_risk": {
            "baseline_guard": 3,
            "candidate_gap": 17,
        },
        "non_idempotent_review_cases": 1,
    }
    assert {case["id"] for case in packet["cases"]} == review_ids
    assert set(packet["no_immediate_question_case_ids"]) == holdout_signal_ids
    assert len(packet["cases"]) == 20
    assert len(packet["no_immediate_question_case_ids"]) == 32
    assert all(case["sealed_values_omitted"] is True for case in packet["cases"])


def test_holdout_batch11_miss_classification_workflow_is_sanitized() -> None:
    classification = load_json(MISS_CLASSIFICATION_851_CASE)
    gemini = load_json(GEMINI_MISS_CLASSIFICATION_851_POLICY_REVIEW)
    packet = load_json(MAINTAINER_BATCH11_MISS_CLASSIFICATION_CONFIRMATION)

    forbidden_case_fields = {
        "acceptable",
        "actual",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    cases = classification["case_classifications"]
    review_ids = {case["id"] for case in cases if case["needs_maintainer_review"]}
    holdout_ids = {case["id"] for case in cases if not case["needs_maintainer_review"]}

    assert classification["report_type"] == "holdout_miss_classification"
    assert classification["review_stage"] == ("codex_first_pass_after_batch11_final_decision")
    assert classification["reviewer"] == "codex"
    assert classification["summary"]["classified_misses"] == 60
    assert classification["summary"]["previously_confirmed_holdout_signals"] == 32
    assert classification["summary"]["new_batch11_misses"] == 28
    assert classification["summary"]["by_action"] == {
        "keep_as_holdout_signal": 35,
        "requires_expected_recheck": 11,
        "move_to_public_regression_candidate": 14,
    }
    assert classification["gemini_review_policy"] == {
        "status": "completed_on_sanitized_metadata",
        "review_report": (
            "docs/reports/holdout-gemini-policy-review-miss-classification-"
            "blind-v1-851-cases-2026-07-14.json"
        ),
        "sealed_values_seen_by_gemini": False,
        "policy_passed": True,
        "classification_changes_recommended": 0,
    }
    assert len(cases) == 60
    assert len({case["id"] for case in cases}) == 60
    assert all(not (forbidden_case_fields & set(case)) for case in cases)
    assert all(case["sealed_values_omitted"] is True for case in cases)

    assert gemini["reviewer"] == "gemini_cli"
    assert gemini["model_requested"] == "gemini-2.5-pro"
    assert gemini["review_stage"] == ("gemini_policy_review_batch11_miss_classification")
    assert gemini["policy_passed"] is True
    assert gemini["classification_changes_recommended"] == []
    assert gemini["sealed_content_policy"]["sealed_values_seen_by_gemini"] is False

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch11_miss_classification_after_851_case_sanity"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["summary"] == {
        "total_review_cases": 25,
        "public_regression_candidate_cases": 14,
        "expected_recheck_cases": 11,
        "no_immediate_question": 35,
        "gemini_policy_passed": True,
        "classification_changes_recommended_by_gemini": 0,
        "by_action": {
            "requires_expected_recheck": 11,
            "move_to_public_regression_candidate": 14,
        },
        "by_domain": {"it": 10, "ui": 4, "llm": 3, "formal": 6, "social": 2},
        "by_risk": {
            "candidate_gap": 17,
            "baseline_guard": 3,
            "over_conversion_guard": 5,
        },
        "non_idempotent_review_cases": 1,
    }
    assert {case["id"] for case in packet["cases"]} == review_ids
    assert set(packet["no_immediate_question_case_ids"]) == holdout_ids
    assert all(case["sealed_values_omitted"] is True for case in packet["cases"])


def test_holdout_batch11_semantic_reaudit_narrows_maintainer_queue() -> None:
    codex = load_json(CODEX_BATCH11_SEMANTIC_REAUDIT)
    gemini = load_json(GEMINI_BATCH11_SEMANTIC_REAUDIT)
    packet = load_json(MAINTAINER_BATCH11_SEMANTIC_REAUDIT_CONFIRMATION)
    forbidden_case_fields = {
        "acceptable",
        "actual",
        "expected",
        "input",
        "output",
        "zhtw_output",
    }

    assert codex["review_stage"] == ("semantic_correctness_reaudit_after_overcorrection_concern")
    assert codex["ground_truth"] is False
    assert codex["promotion_allowed"] is False
    assert codex["revised_policy"] == {
        "measure_conversion_correctness_not_house_style": True,
        "valid_taiwan_synonyms_are_acceptable": True,
        "do_not_tune_from_strict_style_preference": True,
        "maintainer_explicit_preferences_override_ai_advisory": True,
    }
    assert codex["summary"] == {
        "total_cases": 25,
        "by_revised_action": {
            "add_zhtw_output_as_acceptable_variant": 4,
            "move_to_public_regression_candidate": 10,
            "keep_as_strict_private_holdout_signal": 11,
        },
        "explicit_maintainer_preferences_recorded": 19,
        "pending_maintainer_confirmation": 6,
        "promotion_allowed": False,
    }
    assert len(codex["cases"]) == 25
    assert all(not (forbidden_case_fields & set(case)) for case in codex["cases"])

    assert gemini["review_stage"] == "independent_input_only_semantic_reaudit"
    assert gemini["ground_truth"] is False
    assert gemini["promotion_allowed"] is False
    assert gemini["independence_policy"] == {
        "codex_values_seen": False,
        "current_expected_seen": False,
        "zhtw_output_seen": False,
        "prior_miss_classification_seen": False,
        "input_only_cases_seen": True,
    }
    assert len(gemini["cases"]) == 25

    assert packet["review_stage"] == "maintainer_confirmation_packet"
    assert packet["scope"] == "batch11_semantic_reaudit_6_cases"
    assert packet["ground_truth"] is False
    assert packet["promotion_allowed"] is False
    assert packet["summary"] == {
        "review_cases": 6,
        "acceptable_variant_cases": 4,
        "public_regression_candidate_cases": 2,
        "already_resolved_by_maintainer_preference": 19,
        "promotion_allowed": False,
    }
    assert {case["id"] for case in packet["cases"]} == {
        "blind-it-0238",
        "blind-it-0242",
        "blind-it-0244",
        "blind-it-0246",
        "blind-ui-0189",
        "blind-llm-0140",
    }


def test_holdout_batch11_semantic_reaudit_final_decision_is_applied() -> None:
    decision = load_json(MAINTAINER_BATCH11_SEMANTIC_REAUDIT_FINAL_DECISION)
    expected = load_json(EXPECTED)
    pool_update = load_json(SEALED_POOL_UPDATE_BATCH11_SEMANTIC_REAUDIT)
    expected_by_id = {case["id"]: case for case in expected["cases"]}
    acceptable_ids = set(decision["confirmed_acceptable_variant_case_ids"])
    removed_ids = set(decision["removed_to_public_regression_candidate_case_ids"])
    strict_signal_ids = set(decision["strict_private_holdout_signal_case_ids"])

    assert decision["review_stage"] == ("maintainer_final_decision_batch11_semantic_reaudit")
    assert decision["decision"] == "review_ok"
    assert decision["maintainer"] == "tim"
    assert decision["expected_values_included"] is False
    assert decision["inputs_included"] is False
    assert decision["private_expected_sha256_after"] == (
        "066bcd60d16760a10eb8cdd54de61e8ff438fe4a7ffe971e8f814fc45563db2d"
    )
    assert decision["private_expected_sha256_after"] != private_expected_sha256()
    assert decision["source_inputs_sha256_after"] == (
        "3c35b332959c7a87410a0ba7c08d46aa98857b1c080155d275a8892d0f507fef"
    )
    assert decision["source_inputs_sha256_after"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert len(acceptable_ids) == 4
    assert len(removed_ids) == 10
    assert len(strict_signal_ids) == 11
    assert removed_ids == set(pool_update["removed_case_ids"])
    assert not (removed_ids & set(expected_by_id))
    assert strict_signal_ids <= set(expected_by_id)
    assert all(len(expected_by_id[case_id]["acceptable"]) == 1 for case_id in acceptable_ids)
    assert decision["summary"] == {
        "reviewed_semantic_reaudit_cases": 25,
        "maintainer_confirmed_acceptable_variants": 4,
        "removed_from_sealed_to_public_regression_candidates": 10,
        "strict_private_holdout_signals": 11,
        "remaining_private_expected_cases": 841,
        "remaining_sealed_input_cases": 841,
        "public_candidates_promoted_to_regression": 10,
        "regression_total_cases": 1218,
        "converter_or_dictionary_updated": True,
        "promotion_gate_pending": False,
        "candidate_dataset_total_cases": 186,
        "promotion_gate_passed": True,
        "full_sentence_mappings_added": 10,
        "identity_mappings_added": 10,
    }


def test_batch7_miss_final_decision_omits_sealed_values() -> None:
    decision = load_json(MAINTAINER_BATCH7_MISS_FINAL_DECISION)

    assert decision["report_type"] == (
        "holdout_maintainer_final_decision_batch7_miss_classification"
    )
    assert decision["review_stage"] == ("maintainer_final_decision_batch7_miss_classification")
    assert decision["maintainer"] == "tim"
    assert decision["decision"] == "review_ok"
    assert decision["private_expected_updated"] is True
    assert decision["expected_values_included"] is False
    assert decision["acceptable_values_included"] is False
    assert decision["inputs_included"] is False
    assert decision["outputs_included"] is False
    assert decision["benchmark_rows_included"] is False
    assert decision["source_inputs_sha256_after"] == (
        "d331a1a2d6c58774089ca723677ec77ca4abe05e1eb11298ca8a5700b6a1cbcd"
    )
    assert decision["private_expected_sha256_after"] != private_expected_sha256()
    assert decision["summary"]["reviewed_maintainer_cases"] == 24
    assert decision["summary"]["maintainer_confirmed_acceptable_variants"] == 7
    assert decision["summary"]["removed_from_sealed_to_public_regression_candidates"] == 17
    assert decision["summary"]["remaining_private_expected_cases"] == 498
    assert decision["summary"]["remaining_sealed_input_cases"] == 498
    assert decision["summary"]["public_candidates_promoted_to_regression"] == 17
    assert decision["summary"]["projected_remaining_private_benchmark"] == {
        "case_count": 498,
        "accepted": 472,
        "misses": 26,
        "accepted_accuracy": 0.9477911646586346,
    }
    assert decision["confirmed_acceptable_variant_case_ids"] == [
        "blind-it-0146",
        "blind-it-0147",
        "blind-it-0148",
        "blind-it-0157",
        "blind-ui-0108",
        "blind-ui-0110",
        "blind-ui-0118",
    ]
    assert decision["removed_to_public_regression_candidate_case_ids"] == [
        "blind-it-0138",
        "blind-it-0140",
        "blind-it-0142",
        "blind-it-0145",
        "blind-it-0150",
        "blind-it-0151",
        "blind-it-0152",
        "blind-it-0153",
        "blind-it-0155",
        "blind-it-0156",
        "blind-it-0158",
        "blind-ui-0119",
        "blind-ui-0123",
        "blind-llm-0083",
        "blind-llm-0085",
        "blind-formal-0084",
        "blind-social-0079",
    ]
    assert len(decision["kept_sealed_holdout_signal_case_ids"]) == 26
    assert "cases" not in decision
    assert "rows" not in decision
    assert "inputs" not in decision


def test_batch8_miss_final_decision_omits_sealed_values() -> None:
    decision = load_json(MAINTAINER_BATCH8_MISS_FINAL_DECISION)

    assert decision["report_type"] == (
        "holdout_maintainer_final_decision_batch8_miss_classification"
    )
    assert decision["review_stage"] == ("maintainer_final_decision_batch8_miss_classification")
    assert decision["maintainer"] == "tim"
    assert decision["decision"] == "review_ok"
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_updated"] is True
    assert decision["expected_values_included"] is False
    assert decision["acceptable_values_included"] is False
    assert decision["inputs_included"] is False
    assert decision["outputs_included"] is False
    assert decision["benchmark_rows_included"] is False
    assert decision["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "case_ids_and_metadata_only": True,
    }
    assert decision["source_inputs_sha256_after"] == (
        "96226f1fc747cc1d6ae9eb40793077a3a8bc8dc36b194491dc63c7cb26bd4450"
    )
    assert decision["source_inputs_sha256_after"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert decision["private_expected_sha256_after"] != private_expected_sha256()
    assert decision["summary"]["reviewed_maintainer_cases"] == 19
    assert decision["summary"]["maintainer_confirmed_acceptable_variants"] == 4
    assert decision["summary"]["removed_from_sealed_to_public_regression_candidates"] == 15
    assert decision["summary"]["remaining_private_expected_cases"] == 583
    assert decision["summary"]["remaining_sealed_input_cases"] == 583
    assert decision["summary"]["public_candidates_promoted_to_regression"] == 15
    assert decision["summary"]["projected_remaining_private_benchmark"] == {
        "case_count": 583,
        "accepted": 553,
        "misses": 30,
        "accepted_accuracy": 0.9485420240137221,
    }
    assert decision["confirmed_acceptable_variant_case_ids"] == [
        "blind-it-0167",
        "blind-it-0175",
        "blind-llm-0097",
        "blind-social-0095",
    ]
    assert decision["removed_to_public_regression_candidate_case_ids"] == [
        "blind-it-0165",
        "blind-it-0166",
        "blind-it-0168",
        "blind-it-0169",
        "blind-it-0171",
        "blind-it-0173",
        "blind-it-0174",
        "blind-it-0177",
        "blind-ui-0130",
        "blind-ui-0131",
        "blind-ui-0136",
        "blind-ui-0138",
        "blind-ui-0139",
        "blind-llm-0098",
        "blind-formal-0101",
    ]
    assert len(decision["kept_sealed_holdout_signal_case_ids"]) == 30
    assert decision["source_gemini_public_promotion_policy_review"] == (
        "docs/reports/holdout-gemini-policy-review-batch8-miss-public-promotion-2026-07-11.json"
    )
    assert "cases" not in decision
    assert "rows" not in decision
    assert "inputs" not in decision


def test_batch9_miss_final_decision_omits_sealed_values() -> None:
    decision = load_json(MAINTAINER_BATCH9_MISS_FINAL_DECISION)

    assert decision["report_type"] == (
        "holdout_maintainer_final_decision_batch9_miss_classification"
    )
    assert decision["review_stage"] == ("maintainer_final_decision_batch9_miss_classification")
    assert decision["maintainer"] == "tim"
    assert decision["decision"] == "review_ok"
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_updated"] is True
    assert decision["expected_values_included"] is False
    assert decision["acceptable_values_included"] is False
    assert decision["inputs_included"] is False
    assert decision["outputs_included"] is False
    assert decision["benchmark_rows_included"] is False
    assert decision["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "case_ids_and_metadata_only": True,
    }
    assert decision["source_inputs_sha256_before"] == (
        "0ac742ac9885cdae198bed6fc376c2fb5c3e991573ae4cb4ac2072cfef3e937d"
    )
    assert decision["source_inputs_sha256_after"] == (
        "8f54d6e8185cf94f73805aeea27a23859e691cfd8ae04f3956023ec8ec9606d4"
    )
    assert decision["source_inputs_sha256_after"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert decision["private_expected_sha256_after"] != private_expected_sha256()
    assert decision["summary"]["reviewed_maintainer_cases"] == 22
    assert decision["summary"]["maintainer_confirmed_acceptable_variants"] == 6
    assert decision["summary"]["removed_from_sealed_to_public_regression_candidates"] == 16
    assert decision["summary"]["remaining_private_expected_cases"] == 667
    assert decision["summary"]["remaining_sealed_input_cases"] == 667
    assert decision["summary"]["public_candidates_promoted_to_regression"] == 16
    assert decision["summary"]["projected_remaining_private_benchmark"] == {
        "case_count": 667,
        "accepted": 636,
        "misses": 31,
        "accepted_accuracy": 0.9535232383808095,
    }
    assert decision["confirmed_acceptable_variant_case_ids"] == [
        "blind-it-0189",
        "blind-it-0197",
        "blind-it-0202",
        "blind-it-0206",
        "blind-ui-0148",
        "blind-ui-0166",
    ]
    assert decision["removed_to_public_regression_candidate_case_ids"] == [
        "blind-it-0190",
        "blind-it-0195",
        "blind-it-0200",
        "blind-it-0201",
        "blind-it-0203",
        "blind-it-0208",
        "blind-it-0209",
        "blind-it-0210",
        "blind-ui-0150",
        "blind-ui-0157",
        "blind-ui-0160",
        "blind-ui-0164",
        "blind-llm-0116",
        "blind-llm-0122",
        "blind-formal-0115",
        "blind-formal-0116",
    ]
    assert len(decision["kept_sealed_holdout_signal_case_ids"]) == 31
    assert decision["source_gemini_public_promotion_policy_review"] == (
        "docs/reports/holdout-gemini-policy-review-batch9-miss-public-promotion-2026-07-12.json"
    )
    assert "cases" not in decision
    assert "rows" not in decision
    assert "inputs" not in decision


def test_batch6_miss_final_decision_omits_sealed_values() -> None:
    decision = load_json(MAINTAINER_BATCH6_MISS_FINAL_DECISION)

    assert decision["report_type"] == (
        "holdout_maintainer_final_decision_batch6_miss_classification"
    )
    assert decision["review_stage"] == ("maintainer_final_decision_batch6_miss_classification")
    assert decision["maintainer"] == "tim"
    assert decision["decision"] == "review_ok"
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_updated"] is True
    assert decision["expected_values_included"] is False
    assert decision["acceptable_values_included"] is False
    assert decision["inputs_included"] is False
    assert decision["outputs_included"] is False
    assert decision["benchmark_rows_included"] is False
    assert decision["sealed_content_policy"] == {
        "case_ids_and_aggregate_counts_only": True,
        "expected_values_omitted": True,
        "acceptable_values_omitted": True,
        "input_values_omitted": True,
        "actual_values_omitted": True,
        "remaining_sealed_rows_omitted": True,
        "removed_cases_are_public_candidates_after_decision": True,
    }
    assert decision["summary"]["reviewed_maintainer_cases"] == 13
    assert decision["summary"]["maintainer_confirmed_acceptable_variants"] == 2
    assert decision["summary"]["removed_from_sealed_to_public_regression_candidates"] == 11
    assert decision["summary"]["remaining_private_expected_cases"] == 415
    assert decision["summary"]["remaining_sealed_input_cases"] == 415
    assert decision["summary"]["public_candidates_promoted_to_regression"] == 11
    assert decision["summary"]["projected_remaining_private_benchmark"] == {
        "case_count": 415,
        "accepted": 391,
        "misses": 24,
        "accepted_accuracy": 0.9421686746987952,
    }
    assert decision["confirmed_acceptable_variant_case_ids"] == [
        "blind-ui-0096",
        "blind-llm-0071",
    ]
    assert decision["removed_to_public_regression_candidate_case_ids"] == [
        "blind-it-0113",
        "blind-it-0115",
        "blind-it-0117",
        "blind-it-0119",
        "blind-it-0121",
        "blind-it-0123",
        "blind-it-0124",
        "blind-it-0125",
        "blind-it-0126",
        "blind-it-0136",
        "blind-ui-0089",
    ]
    assert len(decision["kept_sealed_holdout_signal_case_ids"]) == 24
    assert "cases" not in decision
    assert "rows" not in decision
    assert "inputs" not in decision


def test_gemini_batch6_miss_public_promotion_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_BATCH6_MISS_PUBLIC_PROMOTION_POLICY_REVIEW)

    assert review["report_type"] == ("holdout_gemini_policy_review_batch6_miss_public_promotion")
    assert review["reviewer"] == "gemini_cli"
    assert review["review_stage"] == "public_regression_promotion_policy_review"
    assert review["source_promotion_gate"] == (
        "docs/reports/holdout-regression-promotion-gate-blind-v1-batch6-miss-review-2026-07-10.json"
    )
    assert review["sealed_values_seen"] is False
    assert review["public_values_seen"] is True
    assert review["sealed_content_policy"] == {
        "reviewed_cases_removed_from_sealed_before_tuning": True,
        "remaining_sealed_holdout_signal_cases_used_for_tuning": False,
        "opencc_or_competitor_outputs_used_for_expected": False,
        "gemini_received_public_candidate_values_only": True,
    }
    assert review["summary"] == {
        "checked": 11,
        "promotion_ready": 11,
        "policy_consistent": True,
        "risk_level": "low",
        "blocking_findings": 0,
        "info_findings": 3,
    }
    assert "GOOGLE_GENERATIVE_AI_API_KEY unset" in " ".join(review["tool_notes"])
    assert "cases" not in review
    assert "rows" not in review
    assert "inputs" not in review


def test_gemini_batch7_miss_public_promotion_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_BATCH7_MISS_PUBLIC_PROMOTION_POLICY_REVIEW)

    assert review["report_type"] == ("holdout_gemini_policy_review_batch7_miss_public_promotion")
    assert review["reviewer"] == "gemini_cli"
    assert review["model_requested"] == "gemini-2.5-flash"
    assert review["review_stage"] == "public_regression_promotion_policy_review"
    assert review["source_promotion_gate"] == (
        "docs/reports/holdout-regression-promotion-gate-blind-v1-batch7-miss-review-2026-07-10.json"
    )
    assert review["sealed_values_seen"] is False
    assert review["public_values_seen"] is True
    assert review["sealed_content_policy"] == {
        "reviewed_cases_removed_from_sealed_before_tuning": True,
        "remaining_sealed_holdout_signal_cases_used_for_tuning": False,
        "opencc_or_competitor_outputs_used_for_expected": False,
        "gemini_received_public_candidate_values_only": True,
    }
    assert review["summary"] == {
        "checked": 17,
        "promotion_ready": 17,
        "policy_consistent": True,
        "risk_level": "low",
        "blocking_findings": 0,
        "info_findings": 0,
    }
    assert "cases" not in review
    assert "rows" not in review
    assert "inputs" not in review


def test_gemini_batch8_miss_public_promotion_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_BATCH8_MISS_PUBLIC_PROMOTION_POLICY_REVIEW)

    assert review["report_type"] == ("holdout_gemini_policy_review_batch8_miss_public_promotion")
    assert review["reviewer"] == "gemini_cli"
    assert review["model_requested"] == "gemini-2.5-flash"
    assert review["review_stage"] == "public_regression_promotion_policy_review"
    assert review["source_promotion_gate"] == (
        "docs/reports/holdout-regression-promotion-gate-blind-v1-batch8-miss-review-2026-07-11.json"
    )
    assert review["sealed_values_seen"] is False
    assert review["public_values_seen"] is True
    assert review["sealed_content_policy"] == {
        "reviewed_cases_removed_from_sealed_before_tuning": True,
        "remaining_sealed_holdout_signal_cases_used_for_tuning": False,
        "opencc_or_competitor_outputs_used_for_expected": False,
        "gemini_received_public_candidate_values_only": True,
    }
    assert review["summary"] == {
        "checked": 15,
        "promotion_ready": 15,
        "policy_consistent": True,
        "risk_level": "low",
        "blocking_findings": 0,
        "info_findings": 0,
    }
    assert "cases" not in review
    assert "rows" not in review
    assert "inputs" not in review


def test_gemini_batch9_miss_public_promotion_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_BATCH9_MISS_PUBLIC_PROMOTION_POLICY_REVIEW)

    assert review["report_type"] == ("holdout_gemini_policy_review_batch9_miss_public_promotion")
    assert review["reviewer"] == "gemini_cli"
    assert review["model_requested"] == "gemini-2.5-flash"
    assert review["review_stage"] == "public_regression_promotion_policy_review"
    assert review["source_promotion_gate"] == (
        "docs/reports/holdout-regression-promotion-gate-blind-v1-batch9-miss-review-2026-07-12.json"
    )
    assert review["sealed_values_seen"] is False
    assert review["public_values_seen"] is True
    assert review["sealed_content_policy"] == {
        "reviewed_cases_removed_from_sealed_before_tuning": True,
        "remaining_sealed_holdout_signal_cases_used_for_tuning": False,
        "opencc_or_competitor_outputs_used_for_expected": False,
        "gemini_received_public_candidate_values_only": True,
    }
    assert review["summary"] == {
        "checked": 16,
        "promotion_ready": 16,
        "policy_consistent": True,
        "risk_level": "low",
        "blocking_findings": 0,
        "info_findings": 3,
    }
    assert all(finding["severity"] == "info" for finding in review["findings"])
    assert "cases" not in review
    assert "rows" not in review
    assert "inputs" not in review


def test_holdout_338_case_miss_classification_omits_sealed_values() -> None:
    report = load_json(MISS_CLASSIFICATION_338_CASE)

    assert report["report_type"] == "holdout_miss_classification_338_case_sanity"
    assert report["review_stage"] == "private_miss_classification_first_pass_after_batch5"
    assert report["reviewer"] == "codex"
    assert report["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "case_ids_and_metadata_only": True,
    }
    assert report["summary"] == {
        "current_sealed_cases": 338,
        "current_accepted": 301,
        "current_misses": 37,
        "accepted_accuracy": 0.8905325443786982,
        "classified_misses": 37,
        "by_action": {
            "keep_as_holdout_signal": 22,
            "move_to_public_regression_candidate": 12,
            "requires_expected_recheck": 3,
        },
        "by_priority": {"P1": 3, "P2": 34},
        "by_domain_action": {
            "formal": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
            "high_risk": {
                "keep_as_holdout_signal": 3,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
            "it": {
                "keep_as_holdout_signal": 2,
                "move_to_public_regression_candidate": 7,
                "requires_expected_recheck": 2,
            },
            "llm": {
                "keep_as_holdout_signal": 4,
                "move_to_public_regression_candidate": 1,
                "requires_expected_recheck": 0,
            },
            "social": {
                "keep_as_holdout_signal": 5,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
            "ui": {
                "keep_as_holdout_signal": 3,
                "move_to_public_regression_candidate": 4,
                "requires_expected_recheck": 1,
            },
        },
        "by_risk_action": {
            "baseline_guard": {
                "keep_as_holdout_signal": 0,
                "move_to_public_regression_candidate": 1,
                "requires_expected_recheck": 0,
            },
            "candidate_gap": {
                "keep_as_holdout_signal": 0,
                "move_to_public_regression_candidate": 11,
                "requires_expected_recheck": 3,
            },
            "over_conversion_guard": {
                "keep_as_holdout_signal": 22,
                "move_to_public_regression_candidate": 0,
                "requires_expected_recheck": 0,
            },
        },
        "idempotency_followup_cases": 0,
        "expected_recheck_cases": 3,
        "safe_public_candidate_cases": 12,
        "holdout_signal_cases": 22,
        "high_risk_cases": 3,
        "over_conversion_guard_cases": 22,
    }
    forbidden_case_fields = {
        "acceptable",
        "actual",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    cases = report["case_classifications"]
    assert len(cases) == 37
    assert len({case["id"] for case in cases}) == len(cases)
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["sealed_values_omitted"] is True
        assert case["action"] in report["summary"]["by_action"]
        assert case["next_step"]

    action_by_id = {case["id"]: case["action"] for case in cases}
    assert action_by_id["blind-it-0088"] == "move_to_public_regression_candidate"
    assert action_by_id["blind-it-0090"] == "requires_expected_recheck"
    assert action_by_id["blind-ui-0073"] == "requires_expected_recheck"
    assert action_by_id["blind-high-risk-0039"] == "keep_as_holdout_signal"


def test_gemini_338_case_miss_classification_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_MISS_CLASSIFICATION_338_POLICY_REVIEW)

    assert review["reviewer"] == "gemini_cli"
    assert review["review_stage"] == "sanitized_miss_classification_policy_review_after_batch5"
    assert review["source_classification_report"] == (
        "docs/reports/holdout-miss-classification-blind-v1-338-cases-2026-07-09.json"
    )
    assert review["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
    }
    assert review["policy_passed"] is True
    assert len(review["findings"]) == 2
    assert {finding["severity"] for finding in review["findings"]} == {"low"}
    assert review["classification_changes_recommended"] == []
    assert "cases" not in review


def test_338_miss_final_decision_omits_sealed_values() -> None:
    decision = load_json(MAINTAINER_338_MISS_FINAL_DECISION)

    assert decision["report_type"] == ("holdout_maintainer_final_decision_338_miss_classification")
    assert decision["review_stage"] == "maintainer_final_decision_338_miss_classification"
    assert decision["maintainer"] == "tim"
    assert decision["decision"] == "review_ok"
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_updated"] is True
    assert decision["expected_values_included"] is False
    assert decision["acceptable_values_included"] is False
    assert decision["inputs_included"] is False
    assert decision["outputs_included"] is False
    assert decision["benchmark_rows_included"] is False
    assert decision["sealed_content_policy"] == {
        "case_ids_and_aggregate_counts_only": True,
        "expected_values_omitted": True,
        "acceptable_values_omitted": True,
        "input_values_omitted": True,
        "actual_values_omitted": True,
        "remaining_sealed_rows_omitted": True,
        "removed_cases_are_public_candidates_after_decision": True,
    }
    assert decision["summary"]["reviewed_maintainer_cases"] == 15
    assert decision["summary"]["maintainer_confirmed_acceptable_variants"] == 3
    assert decision["summary"]["removed_from_sealed_to_public_regression_candidates"] == 12
    assert decision["summary"]["remaining_private_expected_cases"] == 326
    assert decision["summary"]["remaining_sealed_input_cases"] == 326
    assert decision["summary"]["public_candidates_promoted_to_regression"] == 12
    assert decision["confirmed_acceptable_variant_case_ids"] == [
        "blind-it-0090",
        "blind-it-0094",
        "blind-ui-0073",
    ]
    assert decision["removed_to_public_regression_candidate_case_ids"] == [
        "blind-it-0088",
        "blind-it-0089",
        "blind-it-0092",
        "blind-it-0095",
        "blind-it-0096",
        "blind-it-0097",
        "blind-it-0105",
        "blind-ui-0070",
        "blind-ui-0074",
        "blind-ui-0079",
        "blind-ui-0087",
        "blind-llm-0051",
    ]
    assert len(decision["kept_sealed_holdout_signal_case_ids"]) == 22
    assert "cases" not in decision
    assert "rows" not in decision
    assert "inputs" not in decision


def test_gemini_338_miss_public_promotion_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_338_MISS_PUBLIC_PROMOTION_POLICY_REVIEW)

    assert review["report_type"] == ("holdout_gemini_policy_review_338_miss_public_promotion")
    assert review["reviewer"] == "gemini_cli"
    assert review["review_stage"] == "public_regression_promotion_policy_review"
    assert review["source_promotion_gate"] == (
        "docs/reports/holdout-regression-promotion-gate-blind-v1-338-miss-review-2026-07-09.json"
    )
    assert review["sealed_values_seen"] is False
    assert review["public_values_seen"] is True
    assert review["sealed_content_policy"] == {
        "reviewed_cases_removed_from_sealed_before_tuning": True,
        "remaining_sealed_holdout_signal_cases_used_for_tuning": False,
        "opencc_or_competitor_outputs_used_for_expected": False,
        "gemini_received_public_candidate_values_only": True,
    }
    assert review["summary"] == {
        "checked": 12,
        "promotion_ready": 12,
        "policy_consistent": True,
        "risk_level": "low",
        "blocking_findings": 0,
        "info_findings": 4,
    }
    assert "API_KEY_INVALID" in " ".join(review["tool_notes"])
    assert "cases" not in review
    assert "rows" not in review
    assert "inputs" not in review


def test_holdout_261_case_requires_expected_recheck_omits_sealed_values() -> None:
    report = load_json(REQUIRES_EXPECTED_RECHECK_261_CASE)

    assert report["report_type"] == "holdout_requires_expected_recheck"
    assert report["review_stage"] == "codex_private_recheck_first_pass"
    assert report["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "case_recommendations_include_only_ids_and_metadata": True,
    }
    assert report["policy"] == {
        "codex_is_advisory_only": True,
        "private_expected_updated": False,
        "converter_or_dictionary_updated": False,
        "gemini_review_required_before_maintainer": True,
        "maintainer_confirmation_required_for_acceptable_variants": True,
        "move_to_public_requires_sealed_removal_before_tuning": True,
        "strict_cases_must_not_be_used_for_tuning": True,
    }
    assert report["gemini_review_policy"] == {
        "status": "completed_on_sanitized_metadata",
        "review_report": (
            "docs/reports/"
            "holdout-gemini-policy-review-requires-expected-recheck-blind-v1-261-cases-2026-07-09.json"
        ),
        "sealed_values_seen_by_gemini": False,
        "policy_consistent": True,
        "needs_codex_followup": 0,
        "reason": (
            "Gemini reviewed case ids and recheck recommendation metadata only; private "
            "expected, inputs, and converter outputs were not sent."
        ),
    }
    assert report["summary"] == {
        "current_sealed_cases": 261,
        "current_accepted": 207,
        "current_misses": 54,
        "recheck_cases": 16,
        "maintainer_review_required": 16,
        "recommended_acceptable_variant_candidates": 9,
        "recommended_move_to_public_regression_candidate": 5,
        "recommended_keep_strict_primary_expected": 2,
        "by_recommendation": {
            "maintainer_confirm_add_acceptable_variant": 9,
            "maintainer_confirm_keep_strict_primary_expected": 2,
            "maintainer_confirm_move_to_public_regression_candidate": 5,
        },
        "by_priority": {"P1": 5, "P2": 10, "P3": 1},
        "by_domain_recommendation": {
            "formal": {
                "maintainer_confirm_add_acceptable_variant": 2,
                "maintainer_confirm_keep_strict_primary_expected": 1,
            },
            "high_risk": {
                "maintainer_confirm_add_acceptable_variant": 2,
                "maintainer_confirm_move_to_public_regression_candidate": 2,
            },
            "it": {
                "maintainer_confirm_add_acceptable_variant": 2,
                "maintainer_confirm_move_to_public_regression_candidate": 3,
            },
            "llm": {"maintainer_confirm_add_acceptable_variant": 2},
            "ui": {
                "maintainer_confirm_add_acceptable_variant": 1,
                "maintainer_confirm_keep_strict_primary_expected": 1,
            },
        },
        "by_risk_recommendation": {
            "baseline_guard": {
                "maintainer_confirm_add_acceptable_variant": 1,
                "maintainer_confirm_move_to_public_regression_candidate": 1,
            },
            "candidate_gap": {
                "maintainer_confirm_add_acceptable_variant": 6,
                "maintainer_confirm_keep_strict_primary_expected": 2,
            },
            "over_conversion_guard": {
                "maintainer_confirm_add_acceptable_variant": 2,
                "maintainer_confirm_move_to_public_regression_candidate": 4,
            },
        },
        "hypothetical_if_all_acceptable_recommendations_confirmed": {
            "accepted": 216,
            "misses": 45,
            "accepted_accuracy": 0.8275862068965517,
            "note": (
                "This is not an updated benchmark result; private expected is unchanged "
                "until maintainer confirms acceptable variants."
            ),
        },
    }
    assert "rows" not in report
    assert "inputs" not in report
    assert "cases" not in report

    forbidden_case_fields = {
        "acceptable",
        "actual",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    recommendations = report["case_recommendations"]
    assert len(recommendations) == 16
    assert len({case["id"] for case in recommendations}) == len(recommendations)
    for case in recommendations:
        assert not (forbidden_case_fields & set(case))
        assert case["id"].startswith("blind-")
        assert case["recommendation"] in report["summary"]["by_recommendation"]
        assert case["needs_maintainer_review"] is True
        assert case["next_step"]

    recommendation_by_id = {case["id"]: case["recommendation"] for case in recommendations}
    assert recommendation_by_id["blind-it-0081"] == ("maintainer_confirm_add_acceptable_variant")
    assert recommendation_by_id["blind-it-0080"] == (
        "maintainer_confirm_move_to_public_regression_candidate"
    )
    assert recommendation_by_id["blind-ui-0048"] == (
        "maintainer_confirm_keep_strict_primary_expected"
    )
    assert recommendation_by_id["blind-high-risk-0030"] == (
        "maintainer_confirm_move_to_public_regression_candidate"
    )


def test_gemini_261_case_requires_expected_recheck_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_REQUIRES_EXPECTED_RECHECK_261_POLICY_REVIEW)

    assert review["reviewer"] == "gemini_vertex"
    assert review["model"] == "gemini-2.5-flash"
    assert review["review_stage"] == "sanitized_requires_expected_recheck_policy_review"
    assert review["sealed_values_seen"] is False
    assert review["source_recheck_report"] == (
        "docs/reports/holdout-requires-expected-recheck-blind-v1-261-cases-2026-07-09.json"
    )
    assert review["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "gemini_received_sanitized_metadata_only": True,
    }
    assert review["summary"] == {
        "total_cases": 16,
        "policy_consistent": True,
        "needs_codex_followup": 0,
    }
    assert review["findings"] == []
    assert "cases" not in review


def test_261_case_requires_expected_recheck_final_decision_is_sanitized() -> None:
    decision = load_json(REQUIRES_EXPECTED_RECHECK_261_FINAL_DECISION)

    assert decision["report_type"] == "holdout_maintainer_final_decision_requires_expected_recheck"
    assert decision["review_stage"] == "maintainer_final_decision_requires_expected_recheck"
    assert decision["maintainer"] == "tim"
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_updated"] is True
    assert len(decision["private_expected_sha256"]) == 64
    assert decision["expected_values_included"] is False
    assert decision["acceptable_values_included"] is False
    assert decision["inputs_included"] is False
    assert decision["outputs_included"] is False
    assert decision["benchmark_rows_included"] is False
    assert decision["summary"] == {
        "reviewed_recheck_cases": 16,
        "maintainer_confirmed_acceptable_variants": 9,
        "private_expected_cases_updated": 9,
        "removed_from_sealed_to_public_regression_candidates": 5,
        "kept_strict_primary_expected": 2,
        "primary_expected_changed": 0,
        "converter_or_dictionary_changed_for_public_candidates_after_sealed_removal": True,
        "private_expected_updated": True,
        "previous_private_expected_cases": 261,
        "remaining_private_expected_cases": 256,
        "by_domain_confirmed_acceptable_variant": {
            "formal": 2,
            "high_risk": 2,
            "it": 2,
            "llm": 2,
            "ui": 1,
        },
        "by_domain_removed_to_public_regression_candidate": {
            "high_risk": 2,
            "it": 3,
        },
        "by_domain_kept_strict": {
            "formal": 1,
            "ui": 1,
        },
        "by_risk_confirmed_acceptable_variant": {
            "baseline_guard": 1,
            "candidate_gap": 6,
            "over_conversion_guard": 2,
        },
        "by_risk_removed_to_public_regression_candidate": {
            "baseline_guard": 1,
            "over_conversion_guard": 4,
        },
        "by_risk_kept_strict": {
            "candidate_gap": 2,
        },
    }
    assert decision["confirmed_acceptable_variant_case_ids"] == [
        "blind-formal-0036",
        "blind-formal-0041",
        "blind-high-risk-0022",
        "blind-high-risk-0024",
        "blind-it-0081",
        "blind-it-0085",
        "blind-llm-0035",
        "blind-llm-0042",
        "blind-ui-0059",
    ]
    assert decision["removed_to_public_regression_candidate_case_ids"] == [
        "blind-it-0080",
        "blind-it-0082",
        "blind-it-0084",
        "blind-high-risk-0028",
        "blind-high-risk-0030",
    ]
    assert decision["kept_strict_primary_expected_case_ids"] == [
        "blind-ui-0048",
        "blind-formal-0035",
    ]
    assert "cases" not in decision


def test_post_batch3_recheck_omits_sealed_values() -> None:
    report = load_json(POST_BATCH3_RECHECK)
    inputs = load_json(INPUTS)
    input_ids = {case["id"] for case in inputs["cases"]}

    assert report["report_type"] == "holdout_post_batch3_miss_recheck"
    assert report["review_stage"] == "codex_first_pass_expected_acceptable_recheck"
    assert report["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "case_recommendations_include_only_ids_and_metadata": True,
    }
    assert report["policy"] == {
        "codex_is_advisory_only": True,
        "private_expected_updated": False,
        "converter_or_dictionary_updated": False,
        "gemini_review_required_before_maintainer": True,
        "maintainer_confirmation_required_for_acceptable_variants": True,
        "holdout_signal_cases_must_not_be_used_for_tuning": True,
    }
    assert report["summary"] == {
        "current_sealed_cases": 161,
        "current_accepted": 144,
        "current_misses": 17,
        "classified_misses": 17,
        "maintainer_review_required": 11,
        "recommended_acceptable_variant_candidates": 11,
        "keep_as_holdout_signal": 6,
        "by_recommendation": {
            "keep_as_holdout_signal": 6,
            "maintainer_confirm_add_acceptable_variant": 11,
        },
        "by_priority": {"P1": 3, "P2": 14},
        "by_domain_recommendation": {
            "formal": {
                "keep_as_holdout_signal": 1,
                "maintainer_confirm_add_acceptable_variant": 1,
            },
            "high_risk": {"maintainer_confirm_add_acceptable_variant": 2},
            "it": {"maintainer_confirm_add_acceptable_variant": 2},
            "llm": {
                "keep_as_holdout_signal": 2,
                "maintainer_confirm_add_acceptable_variant": 2,
            },
            "social": {
                "keep_as_holdout_signal": 2,
                "maintainer_confirm_add_acceptable_variant": 1,
            },
            "ui": {
                "keep_as_holdout_signal": 1,
                "maintainer_confirm_add_acceptable_variant": 3,
            },
        },
        "by_risk_recommendation": {
            "baseline_guard": {"keep_as_holdout_signal": 1},
            "candidate_gap": {"maintainer_confirm_add_acceptable_variant": 9},
            "over_conversion_guard": {
                "keep_as_holdout_signal": 5,
                "maintainer_confirm_add_acceptable_variant": 2,
            },
        },
        "idempotent_misses": 17,
        "non_idempotent_misses": 0,
        "hypothetical_if_all_acceptable_recommendations_confirmed": {
            "accepted": 155,
            "misses": 6,
            "accepted_accuracy": 0.9627329192546584,
            "note": (
                "This is not an updated benchmark result; private expected is unchanged "
                "until maintainer confirms acceptable variants."
            ),
        },
    }
    assert report["private_review_packet"]["in_repo"] is False
    assert report["private_review_packet"]["contains_sealed_values"] is True
    assert "rows" not in report
    assert "inputs" not in report

    forbidden_case_fields = {
        "acceptable",
        "actual",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    cases = report["case_recommendations"]
    assert len(cases) == 17
    assert len({case["id"] for case in cases}) == len(cases)
    assert {case["id"] for case in cases} <= input_ids
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["current_benchmark_result"] == {
            "accepted": False,
            "primary_exact": False,
            "acceptable_exact": False,
            "idempotent": True,
        }
        assert case["recommendation"] in report["summary"]["by_recommendation"]
        assert case["reason_category"]
        assert case["next_step"]

    recommendation_by_id = {case["id"]: case["recommendation"] for case in cases}
    assert {
        case_id
        for case_id, recommendation in recommendation_by_id.items()
        if recommendation == "keep_as_holdout_signal"
    } == {
        "blind-ui-0011",
        "blind-llm-0026",
        "blind-llm-0028",
        "blind-formal-0029",
        "blind-social-0025",
        "blind-social-0026",
    }
    assert {
        case_id
        for case_id, recommendation in recommendation_by_id.items()
        if recommendation == "maintainer_confirm_add_acceptable_variant"
    } == {
        "blind-ui-0014",
        "blind-ui-0016",
        "blind-it-0036",
        "blind-it-0055",
        "blind-ui-0039",
        "blind-llm-0017",
        "blind-llm-0023",
        "blind-formal-0023",
        "blind-social-0024",
        "blind-high-risk-0011",
        "blind-high-risk-0012",
    }
    flags_by_id = {case["id"]: set(case["flags"]) for case in cases}
    assert flags_by_id["blind-it-0055"] == {
        "over_conversion_guard",
        "multi_term_variant",
    }
    assert flags_by_id["blind-high-risk-0011"] == {
        "high_risk",
        "medical_term_variant",
    }
    assert flags_by_id["blind-high-risk-0012"] == {
        "high_risk",
        "finance_term_variant",
    }


def test_gemini_post_batch3_recheck_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_POST_BATCH3_RECHECK_POLICY_REVIEW)

    assert review["reviewer"] == "gemini_vertex"
    assert review["model"] == "gemini-2.5-flash"
    assert review["review_stage"] == "sanitized_post_batch3_recheck_policy_review"
    assert review["sealed_values_seen"] is False
    assert review["source_recheck_report"] == (
        "docs/reports/holdout-post-batch3-miss-recheck-blind-v1-2026-07-09.json"
    )
    assert review["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "gemini_received_sanitized_metadata_only": True,
    }
    assert review["summary"] == {
        "total_cases": 17,
        "policy_consistent": True,
        "needs_codex_followup": 0,
    }
    assert review["findings"] == []
    assert "cases" not in review


def test_post_batch3_final_decision_omits_sealed_values() -> None:
    decision = load_json(POST_BATCH3_FINAL_DECISION)

    assert decision["dataset"] == "blind-v1"
    assert decision["review_stage"] == "maintainer_final_decision_post_batch3_recheck"
    assert decision["maintainer"] == "tim"
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_updated"] is True
    assert decision["expected_values_included"] is False
    assert decision["acceptable_values_included"] is False
    assert decision["inputs_included"] is False
    assert decision["outputs_included"] is False
    assert decision["benchmark_rows_included"] is False
    assert decision["summary"] == {
        "reviewed_recheck_cases": 17,
        "maintainer_confirmed_acceptable_variants": 11,
        "private_expected_cases_updated": 11,
        "skipped_existing_variants": 0,
        "kept_as_holdout_signal": 6,
        "primary_expected_changed": 0,
        "converter_or_dictionary_changed": False,
        "private_expected_updated": True,
        "by_domain": {
            "formal": 1,
            "high_risk": 2,
            "it": 2,
            "llm": 2,
            "social": 1,
            "ui": 3,
        },
        "by_risk": {
            "candidate_gap": 9,
            "over_conversion_guard": 2,
        },
        "by_priority": {
            "P1": 3,
            "P2": 8,
        },
        "by_reason_category": {
            "valid_ai_generation_term_variant": 2,
            "valid_current_state_term_variant": 1,
            "valid_debug_mode_term_variant": 1,
            "valid_finance_delivery_verb_variant_needs_confirmation": 1,
            "valid_medical_patient_term_variant_needs_confirmation": 1,
            "valid_page_position_term_variant": 1,
            "valid_record_graph_variant": 1,
            "valid_replace_verb_variant": 1,
            "valid_send_to_chat_variant_needs_confirmation": 1,
            "valid_taipei_and_field_name_variant_needs_confirmation": 1,
        },
    }
    assert decision["confirmed_case_ids"] == [
        "blind-formal-0023",
        "blind-high-risk-0011",
        "blind-high-risk-0012",
        "blind-it-0036",
        "blind-it-0055",
        "blind-llm-0017",
        "blind-llm-0023",
        "blind-social-0024",
        "blind-ui-0014",
        "blind-ui-0016",
        "blind-ui-0039",
    ]
    assert set(decision["kept_as_holdout_signal_case_ids"]) == {
        "blind-ui-0011",
        "blind-llm-0026",
        "blind-llm-0028",
        "blind-formal-0029",
        "blind-social-0025",
        "blind-social-0026",
    }
    assert "cases" not in decision


def test_remaining_signal_summary_omits_sealed_values() -> None:
    report = load_json(REMAINING_SIGNAL_SUMMARY)
    inputs = load_json(INPUTS)
    input_ids = {case["id"] for case in inputs["cases"]}

    assert report["report_type"] == "holdout_remaining_signal_summary"
    assert report["review_stage"] == "post_batch3_remaining_signal_summary"
    assert report["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "case_signals_include_only_ids_and_metadata": True,
    }
    assert report["policy"] == {
        "summary_only": True,
        "private_expected_updated": False,
        "converter_or_dictionary_updated": False,
        "do_not_tune_from_these_cases": True,
        "must_remove_from_sealed_before_any_future_tuning": True,
        "gemini_policy_review_required": True,
    }
    assert report["summary"] == {
        "current_sealed_cases": 161,
        "current_accepted": 155,
        "current_misses": 6,
        "remaining_signal_cases": 6,
        "converter_or_dictionary_updated": False,
        "private_expected_updated": False,
        "all_remaining_misses_are_holdout_signals": True,
        "by_domain": {
            "formal": 1,
            "llm": 2,
            "social": 2,
            "ui": 1,
        },
        "by_risk": {
            "baseline_guard": 1,
            "over_conversion_guard": 5,
        },
        "by_signal_category": {
            "graph_variant_over_conversion_signal": 5,
            "strict_ui_wording_signal": 1,
        },
        "by_issue_tag": {
            "formal_term": 1,
            "over_conversion": 5,
            "regional_term": 6,
            "ui_term": 1,
        },
        "idempotent_signal_cases": 6,
        "non_idempotent_signal_cases": 0,
    }
    assert "rows" not in report
    assert "inputs" not in report

    forbidden_case_fields = {
        "acceptable",
        "actual",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    cases = report["case_signals"]
    assert len(cases) == 6
    assert len({case["id"] for case in cases}) == len(cases)
    assert {case["id"] for case in cases} <= input_ids
    assert {case["id"] for case in cases} == {
        "blind-formal-0029",
        "blind-llm-0026",
        "blind-llm-0028",
        "blind-social-0025",
        "blind-social-0026",
        "blind-ui-0011",
    }
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["decision"] == "remain_sealed_holdout_signal"
        assert case["next_step"] == "keep_sealed_and_do_not_tune_against_this_case"
        assert case["current_benchmark_result"] == {
            "accepted": False,
            "primary_exact": False,
            "acceptable_exact": False,
            "idempotent": True,
        }
        assert "converter_or_dictionary_tuning" in case["prohibited_uses"]
        assert case["reason_category"]


def test_gemini_remaining_signal_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_REMAINING_SIGNAL_POLICY_REVIEW)

    assert review["reviewer"] == "gemini_vertex"
    assert review["model"] == "gemini-2.5-flash"
    assert review["review_stage"] == "sanitized_remaining_signal_policy_review"
    assert review["sealed_values_seen"] is False
    assert review["source_signal_report"] == (
        "docs/reports/holdout-remaining-signal-summary-blind-v1-2026-07-09.json"
    )
    assert review["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "gemini_received_sanitized_metadata_only": True,
    }
    assert review["summary"] == {
        "total_cases": 6,
        "policy_consistent": True,
        "needs_codex_followup": 0,
    }
    assert review["findings"] == []
    assert "cases" not in review


def test_remaining_signal_summary_after_batch6_miss_review_omits_sealed_values() -> None:
    report = load_json(REMAINING_SIGNAL_SUMMARY_AFTER_BATCH6_MISS_REVIEW)
    inputs = load_json(INPUTS)
    input_ids = {case["id"] for case in inputs["cases"]}

    assert report["report_type"] == "holdout_remaining_signal_summary"
    assert report["review_stage"] == ("after_batch6_miss_review_remaining_signal_summary")
    assert report["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "case_signals_include_only_ids_and_metadata": True,
    }
    assert report["policy"] == {
        "summary_only": True,
        "private_expected_updated": False,
        "converter_or_dictionary_updated": False,
        "do_not_tune_from_these_cases": True,
        "must_remove_from_sealed_before_any_future_tuning": True,
        "gemini_policy_review_required": True,
    }
    assert report["summary"] == {
        "current_sealed_cases": 415,
        "current_accepted": 391,
        "current_misses": 24,
        "remaining_signal_cases": 24,
        "converter_or_dictionary_updated": False,
        "private_expected_updated": False,
        "all_remaining_misses_are_holdout_signals": True,
        "by_domain": {
            "formal": 5,
            "high_risk": 3,
            "it": 3,
            "llm": 4,
            "social": 5,
            "ui": 4,
        },
        "by_risk": {"over_conversion_guard": 24},
        "by_signal_category": {
            "existing_taiwan_term_over_conversion_signal": 21,
            "high_risk_existing_term_over_conversion_signal": 3,
        },
        "by_issue_tag": {
            "formal_term": 8,
            "high_risk_term": 3,
            "it_term": 5,
            "over_conversion": 24,
            "regional_term": 24,
            "ui_term": 4,
        },
        "idempotent_signal_cases": 24,
        "non_idempotent_signal_cases": 0,
    }
    assert "rows" not in report
    assert "inputs" not in report

    forbidden_case_fields = {
        "acceptable",
        "actual",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    cases = report["case_signals"]
    assert len(cases) == 24
    assert len({case["id"] for case in cases}) == len(cases)
    assert {case["id"] for case in cases} <= input_ids
    assert {case["id"] for case in cases} == {
        "blind-llm-0026",
        "blind-llm-0028",
        "blind-formal-0029",
        "blind-social-0025",
        "blind-social-0026",
        "blind-it-0083",
        "blind-ui-0060",
        "blind-ui-0061",
        "blind-llm-0043",
        "blind-llm-0044",
        "blind-formal-0043",
        "blind-formal-0044",
        "blind-formal-0045",
        "blind-formal-0046",
        "blind-social-0042",
        "blind-social-0043",
        "blind-social-0044",
        "blind-high-risk-0026",
        "blind-high-risk-0027",
        "blind-it-0108",
        "blind-ui-0081",
        "blind-high-risk-0039",
        "blind-it-0131",
        "blind-ui-0102",
    }
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["decision"] == "remain_sealed_holdout_signal"
        assert case["next_step"] == "keep_sealed_and_do_not_tune_against_this_case"
        assert case["current_benchmark_result"] == {
            "accepted": False,
            "primary_exact": False,
            "acceptable_exact": False,
            "idempotent": True,
        }
        assert case["risk"] == "over_conversion_guard"
        assert "converter_or_dictionary_tuning" in case["prohibited_uses"]
        assert case["sealed_values_omitted"] is True


def test_gemini_remaining_signal_policy_review_after_batch6_is_sanitized() -> None:
    review = load_json(GEMINI_REMAINING_SIGNAL_POLICY_REVIEW_AFTER_BATCH6_MISS_REVIEW)

    assert review["report_type"] == (
        "holdout_gemini_policy_review_remaining_signal_after_batch6_miss_review"
    )
    assert review["reviewer"] == "gemini_cli"
    assert review["model_requested"] == "gemini-2.5-flash"
    assert review["review_stage"] == (
        "sanitized_remaining_signal_policy_review_after_batch6_miss_review"
    )
    assert review["sealed_values_seen"] is False
    assert review["source_signal_report"] == (
        "docs/reports/"
        "holdout-remaining-signal-summary-blind-v1-after-batch6-miss-review-2026-07-10.json"
    )
    assert review["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "gemini_received_sanitized_metadata_only": True,
    }
    assert review["summary"] == {
        "total_cases": 24,
        "policy_passed": True,
        "findings": 0,
        "changes_recommended": 0,
    }
    assert review["findings"] == []
    assert review["changes_recommended"] == []
    assert "cases" not in review
    assert "rows" not in review
    assert "inputs" not in review


def test_remaining_signal_summary_after_batch10_miss_review_omits_sealed_values() -> None:
    report = load_json(REMAINING_SIGNAL_SUMMARY_AFTER_BATCH10_MISS_REVIEW)
    inputs = load_json(INPUTS)
    input_ids = {case["id"] for case in inputs["cases"]}

    assert report["report_type"] == ("holdout_remaining_signal_summary_after_batch10_miss_review")
    assert report["review_stage"] == ("after_batch10_miss_review_remaining_signal_summary")
    assert report["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "benchmark_rows_included": False,
        "case_ids_and_metadata_only": True,
    }
    assert report["policy"] == {
        "converter_or_dictionary_updated_from_remaining_signals": False,
        "private_expected_updated_from_remaining_signals": False,
        "public_promotion_allowed": False,
        "requires_independent_public_reproduction_before_tuning": True,
        "do_not_use_sealed_text_for_dictionary_or_converter_changes": True,
    }
    assert report["summary"] == {
        "current_sealed_cases": 751,
        "current_accepted": 719,
        "current_misses": 32,
        "remaining_signal_cases": 32,
        "all_remaining_misses_are_holdout_signals": True,
        "maintainer_review_cases": 0,
        "public_regression_candidate_cases": 0,
        "expected_recheck_cases": 0,
        "converter_or_dictionary_updated_from_remaining_signals": False,
        "private_expected_updated_from_remaining_signals": False,
        "by_domain": {
            "formal": 6,
            "high_risk": 8,
            "it": 3,
            "llm": 4,
            "social": 6,
            "ui": 5,
        },
        "by_risk": {
            "baseline_guard": 1,
            "candidate_gap": 2,
            "over_conversion_guard": 29,
        },
        "by_signal_category": {
            "high_risk_holdout_signal": 8,
            "over_conversion_guard_holdout_signal": 24,
        },
        "by_issue_tag": {
            "baseline_guard": 1,
            "candidate_gap": 1,
            "formal_term": 10,
            "high_risk_term": 8,
            "it_term": 5,
            "over_conversion": 29,
            "regional_term": 32,
            "social_term": 1,
            "ui_term": 5,
        },
        "idempotent_signal_cases": 31,
        "non_idempotent_signal_cases": 1,
        "non_idempotent_signal_case_ids": ["blind-ui-0147"],
    }
    assert "rows" not in report
    assert "inputs" not in report

    forbidden_case_fields = {
        "acceptable",
        "actual",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    cases = report["case_signals"]
    assert len(cases) == 32
    assert len({case["id"] for case in cases}) == len(cases)
    assert {case["id"] for case in cases} <= input_ids
    assert {case["id"] for case in cases} == {
        "blind-llm-0026",
        "blind-llm-0028",
        "blind-formal-0029",
        "blind-social-0025",
        "blind-social-0026",
        "blind-it-0083",
        "blind-ui-0060",
        "blind-ui-0061",
        "blind-llm-0043",
        "blind-llm-0044",
        "blind-formal-0043",
        "blind-formal-0044",
        "blind-formal-0045",
        "blind-formal-0046",
        "blind-social-0042",
        "blind-social-0043",
        "blind-social-0044",
        "blind-high-risk-0026",
        "blind-high-risk-0027",
        "blind-it-0108",
        "blind-ui-0081",
        "blind-high-risk-0039",
        "blind-it-0131",
        "blind-ui-0102",
        "blind-high-risk-0053",
        "blind-high-risk-0058",
        "blind-ui-0147",
        "blind-formal-0105",
        "blind-high-risk-0064",
        "blind-high-risk-0068",
        "blind-social-0110",
        "blind-high-risk-0084",
    }
    for case in cases:
        assert not (forbidden_case_fields & set(case))
        assert case["recommended_action"] == "keep_as_private_holdout_signal"
        assert case["next_step"] == (
            "use_independent_public_inputs_before_any_converter_or_dictionary_change"
        )
        assert case["sealed_values_omitted"] is True
        assert "holdout_signal_do_not_tune" in case["flags"]


def test_gemini_remaining_signal_policy_review_after_batch10_is_sanitized() -> None:
    review = load_json(GEMINI_REMAINING_SIGNAL_POLICY_REVIEW_AFTER_BATCH10_MISS_REVIEW)

    assert review["report_type"] == (
        "holdout_gemini_policy_review_remaining_signal_after_batch10_miss_review"
    )
    assert review["reviewer"] == "gemini_cli"
    assert review["model_requested"] == "gemini-2.5-pro"
    assert review["auth_type"] == "vertex-ai"
    assert review["review_stage"] == ("remaining_signal_policy_review_after_batch10_miss_review")
    assert review["review_status"] == "completed"
    assert review["sealed_values_seen"] is False
    assert review["source_signal_report"] == (
        "docs/reports/"
        "holdout-remaining-signal-summary-blind-v1-after-batch10-miss-review-2026-07-13.json"
    )
    assert review["sealed_content_policy"] == {
        "inputs_included": False,
        "expected_values_included": False,
        "actual_values_included": False,
        "acceptable_values_included": False,
        "benchmark_rows_included": False,
        "case_ids_and_metadata_only": True,
        "sealed_values_seen_by_gemini": False,
    }
    assert review["summary"] == {
        "total_cases": 32,
        "policy_passed": True,
        "findings": 5,
        "blocking_findings": 0,
        "changes_recommended": 0,
        "blocked": False,
    }
    assert [finding["id"] for finding in review["findings"]] == [
        "sealed_content_policy",
        "case_data_omission",
        "main_tuning_policy",
        "case_recommendations",
        "idempotency_followup",
    ]
    assert [finding["severity"] for finding in review["findings"]] == [
        "INFO",
        "INFO",
        "INFO",
        "INFO",
        "LOW",
    ]
    assert review["changes_recommended"] == []
    assert review["raw_gemini_response_report"] == (
        "docs/reports/"
        "holdout-gemini-policy-review-remaining-signal-blind-v1-after-batch10-miss-review-2026-07-13.raw.json"
    )
    assert "cases" not in review
    assert "rows" not in review
    assert "inputs" not in review


def test_holdout_remaining_40_miss_classification_omits_sealed_values() -> None:
    report = load_json(REMAINING_40_MISS_CLASSIFICATION)

    assert report["report_type"] == "holdout_remaining_40_miss_classification"
    assert report["review_stage"] == (
        "codex_private_miss_classification_first_pass_after_batch4_recheck"
    )
    assert report["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "case_recommendations_include_only_ids_and_metadata": True,
    }
    assert report["policy"] == {
        "codex_is_advisory_only": True,
        "private_expected_updated": False,
        "converter_or_dictionary_updated": False,
        "gemini_review_required_before_maintainer": True,
        "maintainer_confirmation_required_for_acceptable_variants": True,
        "move_to_public_requires_sealed_removal_before_tuning": True,
        "holdout_signal_cases_must_not_be_used_for_tuning": True,
    }
    assert report["gemini_review_policy"] == {
        "status": "completed",
        "reviewer": "gemini_vertex",
        "model": "gemini-2.5-flash",
        "report": (
            "docs/reports/"
            "holdout-gemini-policy-review-remaining-40-miss-classification-blind-v1-2026-07-09.json"
        ),
        "policy_consistent": True,
        "needs_codex_followup": 0,
        "findings": 2,
        "sealed_values_seen_by_gemini": False,
    }
    assert report["summary"] == {
        "current_sealed_cases": 256,
        "current_accepted": 216,
        "current_misses": 40,
        "classified_misses": 40,
        "maintainer_review_required": 21,
        "recommended_move_to_public_regression_candidate": 17,
        "recommended_acceptable_variant_candidates": 2,
        "requires_expected_recheck": 2,
        "keep_as_holdout_signal": 19,
        "by_recommendation": {
            "keep_as_holdout_signal": 19,
            "maintainer_confirm_add_acceptable_variant": 2,
            "maintainer_confirm_move_to_public_regression_candidate": 17,
            "requires_expected_recheck": 2,
        },
        "by_priority": {"P1": 17, "P2": 4, "P3": 19},
        "by_domain_recommendation": {
            "formal": {
                "keep_as_holdout_signal": 5,
                "maintainer_confirm_move_to_public_regression_candidate": 2,
            },
            "high_risk": {"keep_as_holdout_signal": 2},
            "it": {
                "keep_as_holdout_signal": 1,
                "maintainer_confirm_move_to_public_regression_candidate": 6,
                "requires_expected_recheck": 2,
            },
            "llm": {
                "keep_as_holdout_signal": 4,
                "maintainer_confirm_move_to_public_regression_candidate": 1,
            },
            "social": {
                "keep_as_holdout_signal": 5,
                "maintainer_confirm_move_to_public_regression_candidate": 4,
            },
            "ui": {
                "keep_as_holdout_signal": 2,
                "maintainer_confirm_add_acceptable_variant": 2,
                "maintainer_confirm_move_to_public_regression_candidate": 4,
            },
        },
        "by_risk_recommendation": {
            "baseline_guard": {
                "maintainer_confirm_add_acceptable_variant": 1,
                "maintainer_confirm_move_to_public_regression_candidate": 1,
            },
            "candidate_gap": {
                "maintainer_confirm_add_acceptable_variant": 1,
                "maintainer_confirm_move_to_public_regression_candidate": 16,
                "requires_expected_recheck": 2,
            },
            "over_conversion_guard": {"keep_as_holdout_signal": 19},
        },
        "idempotent_misses": 38,
        "non_idempotent_misses": 2,
        "high_risk_cases": 2,
        "over_conversion_guard_cases": 19,
        "hypothetical_if_all_acceptable_recommendations_confirmed": {
            "accepted": 218,
            "misses": 38,
            "accepted_accuracy": 0.8515625,
            "note": (
                "This is not an updated benchmark result; private expected is unchanged "
                "until maintainer confirms acceptable variants."
            ),
        },
        "hypothetical_if_move_candidates_removed_and_acceptable_confirmed": {
            "remaining_sealed_cases": 239,
            "accepted": 218,
            "misses": 21,
            "accepted_accuracy": 0.9121338912133892,
            "note": (
                "This is not an updated benchmark result; move candidates must be removed "
                "from sealed holdout before any tuning."
            ),
        },
    }
    assert "rows" not in report
    assert "inputs" not in report
    assert "cases" not in report

    forbidden_case_fields = {
        "acceptable",
        "actual",
        "evaluations",
        "expected",
        "input",
        "normalized_output",
        "output",
    }
    recommendations = report["case_recommendations"]
    assert len(recommendations) == 40
    assert len({case["id"] for case in recommendations}) == len(recommendations)
    for case in recommendations:
        assert not (forbidden_case_fields & set(case))
        assert case["id"].startswith("blind-")
        assert case["recommendation"] in report["summary"]["by_recommendation"]
        assert case["reason_category"]
        assert case["next_step"]

    recommendation_by_id = {case["id"]: case["recommendation"] for case in recommendations}
    assert {
        case_id
        for case_id, recommendation in recommendation_by_id.items()
        if recommendation == "maintainer_confirm_move_to_public_regression_candidate"
    } == {
        "blind-it-0063",
        "blind-it-0064",
        "blind-it-0067",
        "blind-it-0073",
        "blind-it-0076",
        "blind-it-0087",
        "blind-ui-0049",
        "blind-ui-0051",
        "blind-ui-0052",
        "blind-ui-0054",
        "blind-llm-0039",
        "blind-formal-0034",
        "blind-formal-0035",
        "blind-social-0034",
        "blind-social-0036",
        "blind-social-0040",
        "blind-social-0041",
    }
    assert {
        case_id
        for case_id, recommendation in recommendation_by_id.items()
        if recommendation == "maintainer_confirm_add_acceptable_variant"
    } == {"blind-ui-0011", "blind-ui-0048"}
    assert {
        case_id
        for case_id, recommendation in recommendation_by_id.items()
        if recommendation == "requires_expected_recheck"
    } == {"blind-it-0069", "blind-it-0070"}
    assert {
        case_id
        for case_id, recommendation in recommendation_by_id.items()
        if recommendation == "keep_as_holdout_signal"
    } == {
        "blind-llm-0026",
        "blind-llm-0028",
        "blind-formal-0029",
        "blind-social-0025",
        "blind-social-0026",
        "blind-it-0083",
        "blind-ui-0060",
        "blind-ui-0061",
        "blind-llm-0043",
        "blind-llm-0044",
        "blind-formal-0043",
        "blind-formal-0044",
        "blind-formal-0045",
        "blind-formal-0046",
        "blind-social-0042",
        "blind-social-0043",
        "blind-social-0044",
        "blind-high-risk-0026",
        "blind-high-risk-0027",
    }


def test_gemini_remaining_40_miss_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_REMAINING_40_MISS_POLICY_REVIEW)

    assert review["reviewer"] == "gemini_vertex"
    assert review["model"] == "gemini-2.5-flash"
    assert review["review_stage"] == ("sanitized_remaining_40_miss_classification_policy_review")
    assert review["sealed_values_seen"] is False
    assert review["source_classification_report"] == (
        "docs/reports/holdout-remaining-40-miss-classification-blind-v1-2026-07-09.json"
    )
    assert review["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "gemini_received_sanitized_metadata_only": True,
    }
    assert review["summary"] == {
        "total_cases": 40,
        "policy_consistent": True,
        "needs_codex_followup": 0,
        "findings": 2,
        "info_findings": 2,
        "warning_findings": 0,
        "error_findings": 0,
    }
    assert {finding["id"] for finding in review["findings"]} == {
        "blind-it-0070",
        "blind-social-0034",
    }
    assert all(finding["severity"] == "info" for finding in review["findings"])
    assert review["needs_codex_followup"] == []
    assert "cases" not in review
    assert "rows" not in review
    assert "inputs" not in review


def test_gemini_remaining_40_public_promotion_policy_review_is_sanitized() -> None:
    review = load_json(GEMINI_REMAINING_40_PUBLIC_PROMOTION_POLICY_REVIEW)

    assert review["report_type"] == ("holdout_gemini_policy_review_remaining_40_public_promotion")
    assert review["reviewer"] == "gemini_cli"
    assert review["review_stage"] == "public_regression_promotion_policy_review"
    assert review["source_promotion_gate"] == (
        "docs/reports/"
        "holdout-regression-promotion-gate-blind-v1-remaining-40-final-review-2026-07-09.json"
    )
    assert review["sealed_values_seen"] is False
    assert review["public_values_seen"] is True
    assert review["sealed_content_policy"] == {
        "reviewed_cases_removed_from_sealed_before_tuning": True,
        "remaining_sealed_holdout_signal_cases_used_for_tuning": False,
        "opencc_or_competitor_outputs_used_for_expected": False,
        "gemini_received_public_candidate_values_only": True,
    }
    assert review["summary"] == {
        "checked": 18,
        "promotion_ready": 18,
        "policy_consistent": True,
        "risk_level": "low",
        "blocking_findings": 0,
        "info_findings": 2,
    }
    assert "cases" not in review
    assert "rows" not in review
    assert "inputs" not in review


def test_remaining_40_final_decision_omits_sealed_values() -> None:
    decision = load_json(REMAINING_40_FINAL_DECISION)

    assert decision["report_type"] == (
        "holdout_maintainer_final_decision_remaining_40_miss_classification"
    )
    assert decision["review_stage"] == (
        "maintainer_final_decision_remaining_40_miss_classification"
    )
    assert decision["maintainer"] == "tim"
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_updated"] is True
    assert len(decision["private_expected_sha256"]) == 64
    assert decision["expected_values_included"] is False
    assert decision["acceptable_values_included"] is False
    assert decision["inputs_included"] is False
    assert decision["outputs_included"] is False
    assert decision["benchmark_rows_included"] is False
    assert decision["sealed_content_policy"] == {
        "expected_values_included": False,
        "acceptable_values_included": False,
        "actual_outputs_included": False,
        "inputs_included": False,
        "benchmark_rows_included": False,
        "case_ids_and_aggregate_counts_only": True,
    }
    assert decision["summary"] == {
        "reviewed_maintainer_cases": 21,
        "maintainer_confirmed_acceptable_variants": 3,
        "private_expected_cases_updated": 3,
        "removed_from_sealed_to_public_regression_candidates": 18,
        "moved_expected_recheck_to_public_regression_candidate": 1,
        "primary_expected_changed": 0,
        "converter_or_dictionary_changed": False,
        "private_expected_updated": True,
        "previous_private_expected_cases": 256,
        "remaining_private_expected_cases": 238,
        "previous_sealed_input_cases": 256,
        "remaining_sealed_input_cases": 238,
        "public_candidates_added": 18,
        "public_candidates_requiring_zhtw_fix": 18,
        "by_domain_confirmed_acceptable_variant": {"it": 1, "ui": 2},
        "by_domain_removed_to_public_regression_candidate": {
            "formal": 2,
            "it": 7,
            "llm": 1,
            "social": 4,
            "ui": 4,
        },
        "by_risk_confirmed_acceptable_variant": {
            "baseline_guard": 1,
            "candidate_gap": 2,
        },
        "by_risk_removed_to_public_regression_candidate": {
            "baseline_guard": 1,
            "candidate_gap": 17,
        },
        "post_decision_private_benchmark_expected": {
            "remaining_sealed_cases": 238,
            "accepted": 219,
            "misses": 19,
            "accepted_accuracy": 0.9201680672268907,
            "note": "Expected benchmark projection before rerunning private benchmark sanity.",
        },
    }
    assert decision["confirmed_acceptable_variant_case_ids"] == [
        "blind-ui-0011",
        "blind-ui-0048",
        "blind-it-0069",
    ]
    assert decision["removed_to_public_regression_candidate_case_ids"] == [
        "blind-it-0063",
        "blind-it-0064",
        "blind-it-0067",
        "blind-it-0070",
        "blind-it-0073",
        "blind-it-0076",
        "blind-it-0087",
        "blind-ui-0049",
        "blind-ui-0051",
        "blind-ui-0052",
        "blind-ui-0054",
        "blind-llm-0039",
        "blind-formal-0034",
        "blind-formal-0035",
        "blind-social-0034",
        "blind-social-0036",
        "blind-social-0040",
        "blind-social-0041",
    ]
    assert len(decision["kept_sealed_holdout_signal_case_ids"]) == 19
    assert "cases" not in decision
    assert "rows" not in decision
    assert "inputs" not in decision


def test_batch10_miss_final_decision_omits_sealed_values() -> None:
    decision = load_json(MAINTAINER_BATCH10_MISS_FINAL_DECISION)

    assert decision["report_type"] == (
        "holdout_maintainer_final_decision_batch10_miss_classification"
    )
    assert decision["review_stage"] == ("maintainer_final_decision_batch10_miss_classification")
    assert decision["maintainer"] == "tim"
    assert decision["decision"] == "review_ok"
    assert decision["private_expected_path"] == "benchmarks/accuracy/blind-v1.expected.json"
    assert decision["private_expected_updated"] is True
    assert decision["expected_values_included"] is False
    assert decision["acceptable_values_included"] is False
    assert decision["inputs_included"] is False
    assert decision["outputs_included"] is False
    assert decision["benchmark_rows_included"] is False
    assert decision["source_inputs_sha256_before"] == (
        "eff19da4ff198981bdb0018bceabb128b1aa5a33e9199ea5421f69561da340d0"
    )
    assert decision["source_inputs_sha256_after"] == (
        "e6d6e8a2d0b5f9fdffaee7cc7c467cab74210eed62db0202d287bceceb2d02bf"
    )
    assert decision["source_inputs_sha256_after"] != hashlib.sha256(INPUTS.read_bytes()).hexdigest()
    assert decision["private_expected_sha256_after"] == (
        "5c89d5037efcbc33c80dd86f35ccfd12102a709fe701820b9d318fa1f8fe49dc"
    )
    assert decision["private_expected_sha256_after"] != private_expected_sha256()
    assert decision["summary"]["reviewed_maintainer_cases"] == 20
    assert decision["summary"]["maintainer_confirmed_acceptable_variants"] == 4
    assert decision["summary"]["removed_from_sealed_to_public_regression_candidates"] == 16
    assert decision["summary"]["remaining_private_expected_cases"] == 751
    assert decision["summary"]["remaining_sealed_input_cases"] == 751
    assert decision["summary"]["public_candidates_promoted_to_regression"] == 16
    assert decision["removed_to_public_regression_candidate_case_ids"] == [
        "blind-it-0217",
        "blind-it-0220",
        "blind-it-0223",
        "blind-it-0230",
        "blind-it-0235",
        "blind-it-0236",
        "blind-it-0237",
        "blind-ui-0169",
        "blind-ui-0170",
        "blind-ui-0175",
        "blind-ui-0181",
        "blind-ui-0183",
        "blind-ui-0184",
        "blind-formal-0129",
        "blind-formal-0131",
        "blind-formal-0134",
    ]
    assert decision["confirmed_acceptable_variant_case_ids"] == [
        "blind-it-0222",
        "blind-it-0232",
        "blind-llm-0123",
        "blind-llm-0137",
    ]
    assert len(decision["kept_sealed_holdout_signal_case_ids"]) == 32
    assert "cases" not in decision
    assert "rows" not in decision
    assert "inputs" not in decision


def test_holdout_public_regression_candidates_are_promoted_safely() -> None:
    candidates = load_json(HOLDOUT_CANDIDATES)
    gate = load_json(HOLDOUT_PROMOTION_GATE)
    gate_batch2 = load_json(HOLDOUT_PROMOTION_GATE_BATCH2)
    gate_batch3 = load_json(HOLDOUT_PROMOTION_GATE_BATCH3)
    gate_batch4_recheck = load_json(HOLDOUT_PROMOTION_GATE_BATCH4_RECHECK)
    gate_remaining_40 = load_json(HOLDOUT_PROMOTION_GATE_REMAINING_40_FINAL_REVIEW)
    gate_338_miss_review = load_json(HOLDOUT_PROMOTION_GATE_338_MISS_REVIEW)
    gate_batch6_miss_review = load_json(HOLDOUT_PROMOTION_GATE_BATCH6_MISS_REVIEW)
    gate_batch7_miss_review = load_json(HOLDOUT_PROMOTION_GATE_BATCH7_MISS_REVIEW)
    gate_batch8_miss_review = load_json(HOLDOUT_PROMOTION_GATE_BATCH8_MISS_REVIEW)
    gate_batch9_miss_review = load_json(HOLDOUT_PROMOTION_GATE_BATCH9_MISS_REVIEW)
    gate_batch10_miss_review = load_json(HOLDOUT_PROMOTION_GATE_BATCH10_MISS_REVIEW)
    gate_batch11_semantic_reaudit = load_json(HOLDOUT_PROMOTION_GATE_BATCH11_SEMANTIC_REAUDIT)
    gate_batch12_miss_review = load_json(HOLDOUT_PROMOTION_GATE_BATCH12_MISS_REVIEW)
    gate_batch13_miss_review = load_json(HOLDOUT_PROMOTION_GATE_BATCH13_MISS_REVIEW)
    pool_update = load_json(SEALED_POOL_UPDATE)
    pool_update_batch2 = load_json(SEALED_POOL_UPDATE_BATCH2)
    pool_update_batch3 = load_json(SEALED_POOL_UPDATE_BATCH3)
    pool_update_batch4_recheck = load_json(SEALED_POOL_UPDATE_BATCH4_RECHECK)
    pool_update_remaining_40 = load_json(SEALED_POOL_UPDATE_REMAINING_40_FINAL_REVIEW)
    pool_update_338_miss_review = load_json(SEALED_POOL_UPDATE_338_MISS_REVIEW)
    pool_update_batch6_miss_review = load_json(SEALED_POOL_UPDATE_BATCH6_MISS_REVIEW)
    pool_update_batch7_miss_review = load_json(SEALED_POOL_UPDATE_BATCH7_MISS_REVIEW)
    pool_update_batch8_miss_review = load_json(SEALED_POOL_UPDATE_BATCH8_MISS_REVIEW)
    pool_update_batch9_miss_review = load_json(SEALED_POOL_UPDATE_BATCH9_MISS_REVIEW)
    pool_update_batch10_miss_review = load_json(SEALED_POOL_UPDATE_BATCH10_MISS_REVIEW)
    pool_update_batch11_semantic_reaudit = load_json(SEALED_POOL_UPDATE_BATCH11_SEMANTIC_REAUDIT)
    pool_update_batch12_miss_review = load_json(SEALED_POOL_UPDATE_BATCH12_MISS_REVIEW)
    pool_update_batch13_miss_review = load_json(SEALED_POOL_UPDATE_BATCH13_MISS_REVIEW)
    inputs = load_json(INPUTS)

    candidate_cases = candidates["cases"]
    candidate_ids = [case["id"] for case in candidate_cases]
    remaining_input_ids = {case["id"] for case in inputs["cases"]}
    first_removed_ids = pool_update["removed_case_ids"]
    batch2_removed_ids = pool_update_batch2["removed_case_ids"]
    batch3_removed_ids = pool_update_batch3["removed_case_ids"]
    batch4_recheck_removed_ids = pool_update_batch4_recheck["removed_case_ids"]
    remaining_40_removed_ids = pool_update_remaining_40["removed_case_ids"]
    miss_338_removed_ids = pool_update_338_miss_review["removed_case_ids"]
    batch6_miss_removed_ids = pool_update_batch6_miss_review["removed_case_ids"]
    batch7_miss_removed_ids = pool_update_batch7_miss_review["removed_case_ids"]
    batch8_miss_removed_ids = pool_update_batch8_miss_review["removed_case_ids"]
    batch9_miss_removed_ids = pool_update_batch9_miss_review["removed_case_ids"]
    batch10_miss_removed_ids = pool_update_batch10_miss_review["removed_case_ids"]
    batch11_semantic_removed_ids = pool_update_batch11_semantic_reaudit["removed_case_ids"]
    batch12_miss_removed_ids = pool_update_batch12_miss_review["removed_case_ids"]
    batch13_miss_removed_ids = pool_update_batch13_miss_review["removed_case_ids"]

    assert candidates["status"] == "promoted"
    assert candidates["stats"]["total_cases"] == 219
    assert candidates["stats"]["by_domain"] == {
        "formal": 24,
        "high_risk": 7,
        "it": 108,
        "llm": 18,
        "social": 13,
        "ui": 49,
    }
    assert candidates["stats"]["by_risk"] == {
        "baseline_guard": 25,
        "candidate_gap": 171,
        "over_conversion_guard": 23,
    }
    assert candidates["stats"]["by_promotion_status"] == {
        "promoted_to_regression": 219,
    }
    assert candidates["stats"]["by_expected_source"] == {
        "human_adjudication": 126,
        "human_first_pass": 93,
    }
    assert not (set(candidate_ids) & remaining_input_ids)
    assert set(candidate_ids) == (
        set(first_removed_ids)
        | set(batch2_removed_ids)
        | set(batch3_removed_ids)
        | set(batch4_recheck_removed_ids)
        | set(remaining_40_removed_ids)
        | set(miss_338_removed_ids)
        | set(batch6_miss_removed_ids)
        | set(batch7_miss_removed_ids)
        | set(batch8_miss_removed_ids)
        | set(batch9_miss_removed_ids)
        | set(batch10_miss_removed_ids)
        | set(batch11_semantic_removed_ids)
        | set(batch12_miss_removed_ids)
        | set(batch13_miss_removed_ids)
    )

    assert pool_update["expected_values_included"] is False
    assert pool_update["inputs_included"] is False
    assert pool_update["summary"]["original_input_cases"] == 100
    assert pool_update["summary"]["removed_to_public_regression_candidates"] == 22
    assert pool_update["summary"]["remaining_sealed_input_cases"] == 78
    assert pool_update["removed_case_ids"] == candidate_ids[:22]

    assert pool_update_batch2["expected_values_included"] is False
    assert pool_update_batch2["inputs_included"] is False
    assert pool_update_batch2["summary"]["original_input_cases"] == 78
    assert pool_update_batch2["summary"]["removed_to_public_regression_candidates"] == 5
    assert pool_update_batch2["summary"]["remaining_sealed_input_cases"] == 73
    assert pool_update_batch2["removed_case_ids"] == candidate_ids[22:27]

    assert pool_update_batch3["expected_values_included"] is False
    assert pool_update_batch3["inputs_included"] is False
    assert pool_update_batch3["summary"]["original_input_cases"] == 200
    assert pool_update_batch3["summary"]["removed_to_public_regression_candidates"] == 39
    assert pool_update_batch3["summary"]["remaining_sealed_input_cases"] == 161
    assert pool_update_batch3["removed_case_ids"] == candidate_ids[27:66]

    assert pool_update_batch4_recheck["expected_values_included"] is False
    assert pool_update_batch4_recheck["inputs_included"] is False
    assert pool_update_batch4_recheck["summary"]["original_input_cases"] == 261
    assert pool_update_batch4_recheck["summary"]["removed_to_public_regression_candidates"] == 5
    assert pool_update_batch4_recheck["summary"]["remaining_sealed_input_cases"] == 256
    assert pool_update_batch4_recheck["removed_case_ids"] == candidate_ids[66:71]

    assert pool_update_remaining_40["expected_values_included"] is False
    assert pool_update_remaining_40["inputs_included"] is False
    assert pool_update_remaining_40["summary"]["original_input_cases"] == 256
    assert pool_update_remaining_40["summary"]["removed_to_public_regression_candidates"] == 18
    assert pool_update_remaining_40["summary"]["remaining_sealed_input_cases"] == 238
    assert pool_update_remaining_40["removed_case_ids"] == candidate_ids[71:89]

    assert pool_update_338_miss_review["expected_values_included"] is False
    assert pool_update_338_miss_review["inputs_included"] is False
    assert pool_update_338_miss_review["summary"]["original_input_cases"] == 338
    assert pool_update_338_miss_review["summary"]["removed_to_public_regression_candidates"] == 12
    assert pool_update_338_miss_review["summary"]["remaining_sealed_input_cases"] == 326
    assert pool_update_338_miss_review["summary"]["private_expected_acceptable_variants_added"] == 3
    assert pool_update_338_miss_review["removed_case_ids"] == candidate_ids[89:101]

    assert pool_update_batch6_miss_review["expected_values_included"] is False
    assert pool_update_batch6_miss_review["inputs_included"] is False
    assert pool_update_batch6_miss_review["summary"]["original_input_cases"] == 426
    assert (
        pool_update_batch6_miss_review["summary"]["removed_to_public_regression_candidates"] == 11
    )
    assert pool_update_batch6_miss_review["summary"]["remaining_sealed_input_cases"] == 415
    assert (
        pool_update_batch6_miss_review["summary"]["private_expected_acceptable_variants_added"] == 2
    )
    assert pool_update_batch6_miss_review["removed_case_ids"] == candidate_ids[101:112]
    assert pool_update_batch7_miss_review["expected_values_included"] is False
    assert pool_update_batch7_miss_review["inputs_included"] is False
    assert pool_update_batch7_miss_review["summary"]["original_input_cases"] == 515
    assert (
        pool_update_batch7_miss_review["summary"]["removed_to_public_regression_candidates"] == 17
    )
    assert pool_update_batch7_miss_review["summary"]["remaining_sealed_input_cases"] == 498
    assert (
        pool_update_batch7_miss_review["summary"]["private_expected_acceptable_variants_added"] == 7
    )
    assert pool_update_batch7_miss_review["removed_case_ids"] == candidate_ids[112:129]
    assert pool_update_batch8_miss_review["expected_values_included"] is False
    assert pool_update_batch8_miss_review["inputs_included"] is False
    assert pool_update_batch8_miss_review["summary"]["original_input_cases"] == 598
    assert (
        pool_update_batch8_miss_review["summary"]["removed_to_public_regression_candidates"] == 15
    )
    assert pool_update_batch8_miss_review["summary"]["remaining_sealed_input_cases"] == 583
    assert (
        pool_update_batch8_miss_review["summary"]["private_expected_acceptable_variants_added"] == 4
    )
    assert pool_update_batch8_miss_review["removed_case_ids"] == candidate_ids[129:144]
    assert pool_update_batch9_miss_review["expected_values_included"] is False
    assert pool_update_batch9_miss_review["inputs_included"] is False
    assert pool_update_batch9_miss_review["summary"]["original_input_cases"] == 683
    assert (
        pool_update_batch9_miss_review["summary"]["removed_to_public_regression_candidates"] == 16
    )
    assert pool_update_batch9_miss_review["summary"]["remaining_sealed_input_cases"] == 667
    assert (
        pool_update_batch9_miss_review["summary"]["private_expected_acceptable_variants_added"] == 6
    )
    assert pool_update_batch9_miss_review["removed_case_ids"] == candidate_ids[144:160]
    assert pool_update_batch10_miss_review["expected_values_included"] is False
    assert pool_update_batch10_miss_review["inputs_included"] is False
    assert pool_update_batch10_miss_review["summary"]["original_input_cases"] == 767
    assert (
        pool_update_batch10_miss_review["summary"]["removed_to_public_regression_candidates"] == 16
    )
    assert pool_update_batch10_miss_review["summary"]["remaining_sealed_input_cases"] == 751
    assert (
        pool_update_batch10_miss_review["summary"]["private_expected_acceptable_variants_added"]
        == 4
    )
    assert pool_update_batch10_miss_review["removed_case_ids"] == candidate_ids[160:176]
    assert pool_update_batch11_semantic_reaudit["expected_values_included"] is False
    assert pool_update_batch11_semantic_reaudit["inputs_included"] is False
    assert pool_update_batch11_semantic_reaudit["summary"] == {
        "original_sealed_cases": 851,
        "removed_cases": 10,
        "remaining_sealed_cases": 841,
        "confirmed_acceptable_variants": 4,
        "strict_private_holdout_signals": 11,
    }
    assert batch11_semantic_removed_ids == candidate_ids[176:186]
    assert pool_update_batch12_miss_review["expected_values_included"] is False
    assert pool_update_batch12_miss_review["inputs_included"] is False
    assert pool_update_batch12_miss_review["summary"] == {
        "original_sealed_cases": 941,
        "removed_cases": 11,
        "remaining_sealed_cases": 930,
        "confirmed_acceptable_variants": 4,
        "strict_private_holdout_signals": 0,
    }
    assert batch12_miss_removed_ids == candidate_ids[186:197]
    assert pool_update_batch13_miss_review["summary"] == {
        "original_sealed_cases": 1030,
        "removed_cases": 22,
        "remaining_sealed_cases": 1008,
        "confirmed_acceptable_variants": 5,
        "strict_private_holdout_signals": 7,
    }
    assert batch13_miss_removed_ids == candidate_ids[197:219]

    assert gate["summary"] == {
        "checked": 22,
        "promotion_ready": 22,
        "needs_zhtw_fix": 0,
        "convert_matches": 22,
        "convert_mismatches": 0,
        "expected_idempotent": 22,
        "expected_not_idempotent": 0,
        "output_idempotent": 22,
        "output_not_idempotent": 0,
    }
    assert gate_batch2["summary"] == {
        "checked": 5,
        "promotion_ready": 5,
        "needs_zhtw_fix": 0,
        "convert_matches": 5,
        "convert_mismatches": 0,
        "expected_idempotent": 5,
        "expected_not_idempotent": 0,
        "output_idempotent": 5,
        "output_not_idempotent": 0,
    }
    assert gate_batch3["summary"] == {
        "checked": 39,
        "promotion_ready": 39,
        "needs_zhtw_fix": 0,
        "convert_matches": 39,
        "convert_mismatches": 0,
        "expected_idempotent": 39,
        "expected_not_idempotent": 0,
        "output_idempotent": 39,
        "output_not_idempotent": 0,
    }
    assert gate_batch4_recheck["summary"] == {
        "checked": 5,
        "promotion_ready": 5,
        "needs_zhtw_fix": 0,
        "convert_matches": 5,
        "convert_mismatches": 0,
        "expected_idempotent": 5,
        "expected_not_idempotent": 0,
        "output_idempotent": 5,
        "output_not_idempotent": 0,
    }
    assert gate_remaining_40["summary"] == {
        "checked": 18,
        "promotion_ready": 18,
        "needs_zhtw_fix": 0,
        "convert_matches": 18,
        "convert_mismatches": 0,
        "expected_idempotent": 18,
        "expected_not_idempotent": 0,
        "output_idempotent": 18,
        "output_not_idempotent": 0,
    }
    assert gate_338_miss_review["summary"] == {
        "checked": 12,
        "promotion_ready": 12,
        "needs_zhtw_fix": 0,
        "convert_matches": 12,
        "convert_mismatches": 0,
        "expected_idempotent": 12,
        "expected_not_idempotent": 0,
        "output_idempotent": 12,
        "output_not_idempotent": 0,
    }
    assert gate_batch6_miss_review["summary"] == {
        "checked": 11,
        "promotion_ready": 11,
        "needs_zhtw_fix": 0,
        "convert_matches": 11,
        "convert_mismatches": 0,
        "expected_idempotent": 11,
        "expected_not_idempotent": 0,
        "output_idempotent": 11,
        "output_not_idempotent": 0,
    }
    assert gate_batch7_miss_review["summary"] == {
        "checked": 17,
        "promotion_ready": 17,
        "needs_zhtw_fix": 0,
        "convert_matches": 17,
        "convert_mismatches": 0,
        "expected_idempotent": 17,
        "expected_not_idempotent": 0,
        "output_idempotent": 17,
        "output_not_idempotent": 0,
    }
    assert gate_batch8_miss_review["summary"] == {
        "checked": 15,
        "promotion_ready": 15,
        "needs_zhtw_fix": 0,
        "convert_matches": 15,
        "convert_mismatches": 0,
        "expected_idempotent": 15,
        "expected_not_idempotent": 0,
        "output_idempotent": 15,
        "output_not_idempotent": 0,
    }
    assert gate_batch9_miss_review["summary"] == {
        "checked": 16,
        "promotion_ready": 16,
        "needs_zhtw_fix": 0,
        "convert_matches": 16,
        "convert_mismatches": 0,
        "expected_idempotent": 16,
        "expected_not_idempotent": 0,
        "output_idempotent": 16,
        "output_not_idempotent": 0,
    }
    assert gate_batch10_miss_review["summary"] == {
        "checked": 16,
        "promotion_ready": 16,
        "needs_zhtw_fix": 0,
        "convert_matches": 16,
        "convert_mismatches": 0,
        "expected_idempotent": 16,
        "expected_not_idempotent": 0,
        "output_idempotent": 16,
        "output_not_idempotent": 0,
    }
    assert gate_batch11_semantic_reaudit["summary"] == {
        "candidate_cases": 10,
        "zhtw_exact_matches": 10,
        "promotion_ready": 10,
        "promoted_to_regression": 10,
        "full_sentence_mappings_added": 10,
        "identity_mappings_added": 10,
        "regression_total_cases": 1218,
        "gate_passed": True,
    }
    assert gate_batch12_miss_review["summary"] == {
        "candidate_cases": 11,
        "zhtw_exact_matches": 11,
        "expected_idempotent": 11,
        "promotion_ready": 11,
        "promoted_to_regression": 11,
        "full_sentence_mappings_added": 11,
        "identity_mappings_added": 11,
        "candidate_dataset_total_cases": 197,
        "regression_total_cases": 1229,
        "gate_passed": True,
    }
    assert gate_batch13_miss_review["summary"] == {
        "candidate_cases": 22,
        "zhtw_exact_matches": 22,
        "expected_idempotent": 22,
        "promotion_ready": 22,
        "promoted_to_regression": 22,
        "full_sentence_mappings_added": 22,
        "identity_mappings_added": 22,
        "candidate_dataset_total_cases": 219,
        "regression_total_cases": 1251,
        "gate_passed": True,
    }
    gate_by_id = {
        case["id"]: case
        for case in (
            gate["cases"]
            + gate_batch2["cases"]
            + gate_batch3["cases"]
            + gate_batch4_recheck["cases"]
            + gate_remaining_40["cases"]
            + gate_338_miss_review["cases"]
            + gate_batch6_miss_review["cases"]
            + gate_batch7_miss_review["cases"]
            + gate_batch8_miss_review["cases"]
            + gate_batch9_miss_review["cases"]
            + gate_batch10_miss_review["cases"]
        )
    }
    gate_by_id.update(
        {
            case_id: {"status": "promotion_ready"}
            for case_id in gate_batch11_semantic_reaudit["promoted_case_ids"]
        }
    )
    gate_by_id.update(
        {
            case_id: {"status": "promotion_ready"}
            for case_id in gate_batch12_miss_review["promoted_case_ids"]
        }
    )
    gate_by_id.update(
        {
            case_id: {"status": "promotion_ready"}
            for case_id in gate_batch13_miss_review["promoted_case_ids"]
        }
    )
    for case in candidate_cases:
        if case["id"] in batch13_miss_removed_ids:
            expected_gate_report = str(HOLDOUT_PROMOTION_GATE_BATCH13_MISS_REVIEW.relative_to(ROOT))
        elif case["id"] in batch12_miss_removed_ids:
            expected_gate_report = str(HOLDOUT_PROMOTION_GATE_BATCH12_MISS_REVIEW.relative_to(ROOT))
        elif case["id"] in batch11_semantic_removed_ids:
            expected_gate_report = str(
                HOLDOUT_PROMOTION_GATE_BATCH11_SEMANTIC_REAUDIT.relative_to(ROOT)
            )
        elif case["id"] in batch10_miss_removed_ids:
            expected_gate_report = str(HOLDOUT_PROMOTION_GATE_BATCH10_MISS_REVIEW.relative_to(ROOT))
        elif case["id"] in batch9_miss_removed_ids:
            expected_gate_report = str(HOLDOUT_PROMOTION_GATE_BATCH9_MISS_REVIEW.relative_to(ROOT))
        elif case["id"] in batch8_miss_removed_ids:
            expected_gate_report = str(HOLDOUT_PROMOTION_GATE_BATCH8_MISS_REVIEW.relative_to(ROOT))
        elif case["id"] in batch7_miss_removed_ids:
            expected_gate_report = str(HOLDOUT_PROMOTION_GATE_BATCH7_MISS_REVIEW.relative_to(ROOT))
        elif case["id"] in batch6_miss_removed_ids:
            expected_gate_report = str(HOLDOUT_PROMOTION_GATE_BATCH6_MISS_REVIEW.relative_to(ROOT))
        elif case["id"] in miss_338_removed_ids:
            expected_gate_report = str(HOLDOUT_PROMOTION_GATE_338_MISS_REVIEW.relative_to(ROOT))
        elif case["id"] in remaining_40_removed_ids:
            expected_gate_report = str(
                HOLDOUT_PROMOTION_GATE_REMAINING_40_FINAL_REVIEW.relative_to(ROOT)
            )
        elif case["id"] in batch4_recheck_removed_ids:
            expected_gate_report = str(HOLDOUT_PROMOTION_GATE_BATCH4_RECHECK.relative_to(ROOT))
        elif case["id"] in batch3_removed_ids:
            expected_gate_report = str(HOLDOUT_PROMOTION_GATE_BATCH3.relative_to(ROOT))
        elif case["id"] in batch2_removed_ids:
            expected_gate_report = str(HOLDOUT_PROMOTION_GATE_BATCH2.relative_to(ROOT))
        else:
            expected_gate_report = str(HOLDOUT_PROMOTION_GATE.relative_to(ROOT))

        assert case["source"]["type"] == "sealed_holdout_removed_case"
        assert case["review"]["approval_policy"] == "single_human_with_ai_advisory"
        assert case["promotion"]["status"] in {
            "needs_zhtw_fix",
            "promoted_to_regression",
        }
        assert case["promotion"]["gate_report"] == expected_gate_report
        assert case["promotion"]["promoted_id"] == f"holdout/{case['id']}"
        assert gate_by_id[case["id"]]["status"] == case["promotion"]["status"].replace(
            "promoted_to_regression", "promotion_ready"
        )
        if case["promotion"]["status"] == "promoted_to_regression":
            assert convert(case["input"]) == case["expected"]
            assert convert(case["expected"]) == case["expected"]
        else:
            assert case["id"] in remaining_40_removed_ids
            assert convert(case["input"]) != case["expected"]


def test_run_accuracy_benchmark_with_temp_fixture(tmp_path: Path) -> None:
    inputs_path = tmp_path / "blind.inputs.json"
    expected_path = tmp_path / "blind.expected.json"
    output_prefix = tmp_path / "accuracy-benchmark-test"
    input_text = "这个函数会抛出异常。"
    expected_text = convert(input_text)

    inputs_path.write_text(
        json.dumps(
            {
                "version": 1,
                "name": "blind-v1.inputs",
                "dataset": "blind-v1",
                "description": "test fixture",
                "generated_date": "2026-07-07",
                "status": "frozen_inputs",
                "publish_state": "public_inputs_only",
                "target_total": 2000,
                "source_policy": {
                    "expected_not_in_inputs": True,
                    "allowed_input_sources": ["test"],
                    "forbidden_expected_sources": ["zhtw output"],
                    "copyright_policy": "test",
                },
                "annotation_protocol": {
                    "review_order": ["first", "second", "adjudication"],
                    "minimum_human_reviewers": 2,
                    "adjudication_required_on_disagreement": True,
                    "normalization": ["Unicode NFC"],
                },
                "batches": [
                    {
                        "id": "test-batch",
                        "domain": "it",
                        "target_cases": 1,
                        "priority": 1,
                        "focus": ["test"],
                    }
                ],
                "stats": {
                    "total_collected": 1,
                    "by_domain": {"it": 1},
                    "by_risk": {"candidate_gap": 1},
                },
                "cases": [
                    {
                        "id": "fixture-0001",
                        "batch": "test-batch",
                        "domain": "it",
                        "input": input_text,
                        "risk": "candidate_gap",
                        "source": {
                            "type": "test",
                            "citation": "test",
                            "license": "test",
                        },
                        "tags": ["test"],
                        "notes": "test",
                    }
                ],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    inputs_hash = hashlib.sha256(inputs_path.read_bytes()).hexdigest()
    expected_path.write_text(
        json.dumps(
            {
                "version": 1,
                "name": "blind-v1.expected",
                "dataset": "blind-v1",
                "description": "test fixture",
                "generated_date": "2026-07-07",
                "status": "sealed_private",
                "source_inputs": str(inputs_path),
                "source_inputs_sha256": inputs_hash,
                "expected_policy": {
                    "expected_source": "human_review_only",
                    "forbidden_expected_sources": ["zhtw output"],
                    "minimum_human_reviewers": 2,
                    "adjudication_required_on_disagreement": True,
                    "normalization": ["Unicode NFC"],
                },
                "cases": [
                    {
                        "id": "fixture-0001",
                        "expected": expected_text,
                        "acceptable": [],
                        "annotation": {
                            "expected_source": "human_first_pass",
                            "first_reviewer": "fixture",
                            "second_reviewer": "fixture",
                            "adjudicator": "",
                            "disagreement": False,
                            "decision_date": "2026-07-07",
                            "notes": (
                                "fixture expected equals current zhtw output for runner plumbing"
                            ),
                        },
                        "issue_tags": ["it_term"],
                    }
                ],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            str(RUNNER),
            "--inputs",
            str(inputs_path),
            "--expected",
            str(expected_path),
            "--competitors-lock",
            str(COMPETITORS_LOCK),
            "--competitors",
            "zhtw",
            "--formats",
            "json,md",
            "--output-prefix",
            str(output_prefix),
            "--generated-date",
            "2026-07-07",
            "--fail-on-zhtw-miss",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert "cases=1 zhtw_accepted=1 zhtw_misses=0" in result.stdout

    payload = load_json(output_prefix.with_suffix(".json"))
    assert payload["report_mode"] == "aggregate"
    assert payload["dataset_classification"] == "published_evaluation"
    assert payload["summary"]["case_count"] == 1
    assert payload["engines"]["zhtw"]["scores"]["accepted_accuracy"] == 1.0
    assert payload["engines"]["zhtw"]["scores"]["primary_exact_accuracy"] == 1.0
    assert "rows" not in payload
    assert "expected" not in payload
    assert payload["expected_sha256"] == hashlib.sha256(expected_path.read_bytes()).hexdigest()
    assert payload["provenance"]["zhtw_version"] == "4.4.2"
    assert len(payload["provenance"]["git_sha"]) == 40
    assert (
        output_prefix.with_suffix(".md")
        .read_text(encoding="utf-8")
        .startswith("<!-- zhtw:disable -->")
    )

    detailed_prefix = tmp_path / "accuracy-benchmark-detailed"
    detailed_result = subprocess.run(
        [
            sys.executable,
            str(RUNNER),
            "--inputs",
            str(inputs_path),
            "--expected",
            str(expected_path),
            "--competitors-lock",
            str(COMPETITORS_LOCK),
            "--competitors",
            "zhtw",
            "--formats",
            "json",
            "--output-prefix",
            str(detailed_prefix),
            "--report-mode",
            "detailed",
            "--generated-date",
            "2026-07-07",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert detailed_result.returncode == 0, detailed_result.stdout + detailed_result.stderr
    detailed = load_json(detailed_prefix.with_suffix(".json"))
    assert detailed["report_mode"] == "detailed"
    assert detailed["private_expected"]["path"] == str(expected_path)
    assert detailed["rows"][0]["evaluations"]["zhtw"]["accepted"] is True
