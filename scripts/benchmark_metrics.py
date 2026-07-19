"""Deterministic metrics and statistics for accuracy benchmarks."""

from __future__ import annotations

import hashlib
import json
import math
import random
from dataclasses import asdict, dataclass
from statistics import NormalDist
from typing import Any


@dataclass(frozen=True)
class EditSpan:
    operation: str
    source_start: int
    source_end: int
    target_start: int
    target_end: int
    source_text: str
    target_text: str


def canonical_json_bytes(value: Any) -> bytes:
    """Serialize JSON deterministically for hashes and frozen fixtures."""
    return (
        json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode("utf-8")


def canonical_sha256(value: Any) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def align_edits(source: str, target: str) -> list[EditSpan]:
    """Return one minimum edit alignment using a fixed tie-break order.

    Unicode code points are the alignment unit. Equal-cost paths prefer match,
    substitution, deletion, then insertion.
    """
    source_chars = list(source)
    target_chars = list(target)
    source_size = len(source_chars)
    target_size = len(target_chars)
    costs = [[0] * (target_size + 1) for _ in range(source_size + 1)]
    back: list[list[str | None]] = [[None] * (target_size + 1) for _ in range(source_size + 1)]

    for source_index in range(1, source_size + 1):
        costs[source_index][0] = source_index
        back[source_index][0] = "delete"
    for target_index in range(1, target_size + 1):
        costs[0][target_index] = target_index
        back[0][target_index] = "insert"

    priority = {"match": 0, "substitute": 1, "delete": 2, "insert": 3}
    for source_index in range(1, source_size + 1):
        for target_index in range(1, target_size + 1):
            candidates: list[tuple[int, int, str]] = []
            if source_chars[source_index - 1] == target_chars[target_index - 1]:
                candidates.append(
                    (costs[source_index - 1][target_index - 1], priority["match"], "match")
                )
            else:
                candidates.append(
                    (
                        costs[source_index - 1][target_index - 1] + 1,
                        priority["substitute"],
                        "substitute",
                    )
                )
            candidates.extend(
                [
                    (costs[source_index - 1][target_index] + 1, priority["delete"], "delete"),
                    (costs[source_index][target_index - 1] + 1, priority["insert"], "insert"),
                ]
            )
            cost, _, operation = min(candidates)
            costs[source_index][target_index] = cost
            back[source_index][target_index] = operation

    atomic: list[EditSpan] = []
    source_index = source_size
    target_index = target_size
    while source_index or target_index:
        operation = back[source_index][target_index]
        if operation == "match":
            source_index -= 1
            target_index -= 1
        elif operation == "substitute":
            atomic.append(
                EditSpan(
                    operation=operation,
                    source_start=source_index - 1,
                    source_end=source_index,
                    target_start=target_index - 1,
                    target_end=target_index,
                    source_text=source_chars[source_index - 1],
                    target_text=target_chars[target_index - 1],
                )
            )
            source_index -= 1
            target_index -= 1
        elif operation == "delete":
            atomic.append(
                EditSpan(
                    operation=operation,
                    source_start=source_index - 1,
                    source_end=source_index,
                    target_start=target_index,
                    target_end=target_index,
                    source_text=source_chars[source_index - 1],
                    target_text="",
                )
            )
            source_index -= 1
        elif operation == "insert":
            atomic.append(
                EditSpan(
                    operation=operation,
                    source_start=source_index,
                    source_end=source_index,
                    target_start=target_index - 1,
                    target_end=target_index,
                    source_text="",
                    target_text=target_chars[target_index - 1],
                )
            )
            target_index -= 1
        else:
            raise RuntimeError("alignment backtrace is incomplete")

    atomic.reverse()
    return _merge_adjacent_edits(atomic)


def _merge_adjacent_edits(edits: list[EditSpan]) -> list[EditSpan]:
    merged: list[EditSpan] = []
    for edit in edits:
        if not merged:
            merged.append(edit)
            continue
        previous = merged[-1]
        contiguous = (
            previous.operation == edit.operation
            and previous.source_end == edit.source_start
            and previous.target_end == edit.target_start
        )
        if not contiguous:
            merged.append(edit)
            continue
        merged[-1] = EditSpan(
            operation=previous.operation,
            source_start=previous.source_start,
            source_end=edit.source_end,
            target_start=previous.target_start,
            target_end=edit.target_end,
            source_text=previous.source_text + edit.source_text,
            target_text=previous.target_text + edit.target_text,
        )
    return merged


def edit_span_payload(source: str, target: str) -> list[dict[str, Any]]:
    return [asdict(edit) for edit in align_edits(source, target)]


def changed_span_metrics(source: str, expected: str, output: str) -> dict[str, float | int]:
    required = {
        (edit.source_start, edit.source_end, edit.target_text)
        for edit in align_edits(source, expected)
    }
    produced = {
        (edit.source_start, edit.source_end, edit.target_text)
        for edit in align_edits(source, output)
    }
    correct = len(required & produced)
    precision = correct / len(produced) if produced else (1.0 if not required else 0.0)
    recall = correct / len(required) if required else (1.0 if not produced else 0.0)
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {
        "required_edits": len(required),
        "produced_edits": len(produced),
        "correct_edits": correct,
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }


def paired_comparison(
    candidate: list[bool],
    competitor: list[bool],
    *,
    rounds: int = 10_000,
    seed: int = 20260719,
) -> dict[str, Any]:
    if len(candidate) != len(competitor) or not candidate:
        raise ValueError("paired results must have the same non-zero length")
    deltas = [int(left) - int(right) for left, right in zip(candidate, competitor, strict=True)]
    rng = random.Random(seed)
    size = len(deltas)
    bootstrap = [
        sum(deltas[rng.randrange(size)] for _ in range(size)) / size for _ in range(rounds)
    ]
    bootstrap.sort()
    low = bootstrap[int(0.025 * (rounds - 1))]
    high = bootstrap[int(0.975 * (rounds - 1))]
    pairs = list(zip(candidate, competitor, strict=True))
    candidate_only = sum(left and not right for left, right in pairs)
    competitor_only = sum(right and not left for left, right in pairs)
    return {
        "case_count": size,
        "absolute_delta": sum(deltas) / size,
        "delta_ci_95": {"low": low, "high": high},
        "candidate_only_correct": candidate_only,
        "competitor_only_correct": competitor_only,
        "mcnemar_exact_p": _mcnemar_exact_p(candidate_only, competitor_only),
        "result": "winner" if low > 0 else "loser" if high < 0 else "statistical_tie",
        "bootstrap_rounds": rounds,
        "seed": seed,
    }


def _mcnemar_exact_p(left_only: int, right_only: int) -> float:
    discordant = left_only + right_only
    if discordant == 0:
        return 1.0
    tail = sum(math.comb(discordant, index) for index in range(min(left_only, right_only) + 1))
    return min(1.0, 2 * tail / (2**discordant))


def paired_power_analysis(
    *,
    discordant_rate: float,
    minimum_detectable_effect: float = 0.02,
    alpha: float = 0.05,
    target_power: float = 0.80,
    max_cases: int = 100_000,
) -> dict[str, Any]:
    if not 0 < minimum_detectable_effect < discordant_rate <= 1:
        raise ValueError("require 0 < minimum_detectable_effect < discordant_rate <= 1")
    if not 0 < alpha < 1 or not 0 < target_power < 1:
        raise ValueError("alpha and target_power must be between 0 and 1")

    normal = NormalDist()
    critical = normal.inv_cdf(1 - alpha / 2)

    def power(case_count: int) -> float:
        null_sd = math.sqrt(discordant_rate / case_count)
        alternative_sd = math.sqrt((discordant_rate - minimum_detectable_effect**2) / case_count)
        threshold = critical * null_sd
        upper = 1 - normal.cdf((threshold - minimum_detectable_effect) / alternative_sd)
        lower = normal.cdf((-threshold - minimum_detectable_effect) / alternative_sd)
        return min(1.0, upper + lower)

    required = next(
        (case_count for case_count in range(2, max_cases + 1) if power(case_count) >= target_power),
        None,
    )
    if required is None:
        raise ValueError("required sample size exceeds max_cases")
    return {
        "method": "paired_mcnemar_normal_approximation",
        "discordant_rate": discordant_rate,
        "minimum_detectable_effect": minimum_detectable_effect,
        "alpha": alpha,
        "target_power": target_power,
        "required_cases": required,
        "power_at_600": power(600),
        "power_at_1200": power(1200),
    }
