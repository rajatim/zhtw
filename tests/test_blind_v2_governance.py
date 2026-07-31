"""Tests for Blind-v2 candidate, sampling, decision, and ledger governance."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

import pytest

import scripts.blind_v2_governance as governance
from scripts.blind_v2_governance import (
    _expected_stats,
    _near_duplicate_pairs,
    append_ledger_event,
    apportion,
    build_final_decisions,
    build_frozen_pool,
    build_inputs,
    build_replacement_ledger,
    character_ngrams,
    deterministic_sample,
    jaccard,
    normalize_for_dedupe,
    reference_texts,
    stratum_quotas,
    validate_decisions,
    validate_ledger,
    validate_ledger_events,
    validate_pool,
    validate_replacements,
    validate_schema,
)

ROOT = Path(__file__).resolve().parents[1]
ACCURACY_ROOT = ROOT / "benchmarks" / "accuracy"
FROZEN_POOL = ACCURACY_ROOT / "blind-v2.candidate-pool.json"
REPLACEMENTS = ACCURACY_ROOT / "blind-v2.replacements.json"
INPUTS = ACCURACY_ROOT / "blind-v2.inputs.json"
FREEZE_REPORT = ROOT / "docs/reports/blind-v2-pool-freeze-2026-07-30.json"
ANNOTATION_DECISIONS = ACCURACY_ROOT / "blind-v2.annotation-decisions.json"
FINAL_DECISIONS = ACCURACY_ROOT / "blind-v2.final-decisions.json"


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def candidate(
    number: int,
    *,
    domain: str = "it_api_cli",
    risk: str = "candidate_gap",
    source_class: str = "project_original",
    source_id: str | None = None,
    text: str | None = None,
) -> dict[str, Any]:
    digest = hashlib.sha256(str(number).encode()).hexdigest()
    return {
        "id": f"blind-v2-candidate-{number:06d}",
        "domain": domain,
        "risk": risk,
        "input": text or f"候選句 {digest}",
        "source": {
            "class": source_class,
            "id": source_id or f"source-{number:06d}",
            "citation": f"Fixture source {number}",
            "license": "MIT",
            "created_at": "2026-07-19",
        },
        "tags": ["fixture"],
        "notes": "Input only.",
    }


def pool_fixture(cases: list[dict[str, Any]], *, formal_n: int = 600) -> dict[str, Any]:
    return {
        "version": 1,
        "id": "blind-v2-candidate-pool-v1",
        "status": "collecting",
        "created_at": "2026-07-19T00:00:00Z",
        "formal_n": formal_n,
        "power_analysis": {
            "method": "paired_mcnemar_normal_approximation",
            "discordant_rate": 0.03,
            "minimum_detectable_effect": 0.02,
            "alpha": 0.05,
            "target_power": 0.8,
            "required_cases": 587,
        },
        "seed": 20260719,
        "source_policy": {
            "maximum_source_fraction": 0.1,
            "maximum_source_class_fraction": 0.35,
        },
        "deduplication": {
            "normalization": "unicode-nfc-collapse-whitespace-v1",
            "ngram_size": 5,
            "near_duplicate_threshold": 0.85,
            "reference_globs": [
                "benchmarks/accuracy/*.json",
                "docs/reports/*.json",
                "src/zhtw/data/terms/**/*.json",
            ],
            "reference_snapshot_sha256": "0" * 64,
        },
        "stats": _expected_stats(cases),
        "cases": cases,
    }


def sample_pool_fixture(multiplier: int = 2) -> dict[str, Any]:
    cases: list[dict[str, Any]] = []
    number = 1
    for domain, risks in stratum_quotas(600).items():
        for risk, required in risks.items():
            for _ in range(required * multiplier):
                source_classes = (
                    "project_original",
                    "permissioned",
                    "public_domain",
                    "permissive_license",
                )
                cases.append(
                    candidate(
                        number,
                        domain=domain,
                        risk=risk,
                        source_class=source_classes[number % len(source_classes)],
                    )
                )
                number += 1
    return pool_fixture(cases)


def ledger_event(run_id: str, event: str) -> dict[str, Any]:
    return {
        "version": 1,
        "dataset": "blind-v2",
        "run_id": run_id,
        "event": event,
        "recorded_at": "2026-07-19T00:00:00Z",
        "operator": "maintainer",
        "reason": "formal one-shot evaluation",
        "preregistration_sha256": "a" * 64,
        "inputs_sha256": "b" * 64,
        "expected_sha256": "c" * 64,
        "zhtw_git_sha": "d" * 40,
        "competitor_lock_sha256": "e" * 64,
        "exit_status": None if event == "run_started" else (0 if event == "score_exposed" else 1),
        "detailed_rows_read": False,
    }


def write_ledger(path: Path, events: list[dict[str, Any]]) -> None:
    path.write_text("".join(json.dumps(event) + "\n" for event in events), encoding="utf-8")


def test_dedupe_normalization_and_jaccard_are_fixed() -> None:
    assert normalize_for_dedupe("A\u030a  候選\r\n文字") == "Å 候選 文字"
    left = character_ngrams("這是一段候選測試文字")
    right = character_ngrams("這是一段候選測試文本")

    assert left == character_ngrams("這是一段候選測試文字")
    assert jaccard(left, right) == len(left & right) / len(left | right)


def test_quota_apportionment_preserves_total_and_declared_ratios() -> None:
    assert apportion(7, (("first", 1), ("second", 1))) == {"first": 4, "second": 3}
    quotas = stratum_quotas(1960)

    assert sum(sum(risks.values()) for risks in quotas.values()) == 1960
    assert {domain: sum(risks.values()) for domain, risks in quotas.items()} == {
        "it_api_cli": 490,
        "ui_i18n": 392,
        "llm_generated": 294,
        "formal_news": 294,
        "social_daily": 294,
        "high_stakes": 196,
    }
    assert quotas["it_api_cli"] == {
        "candidate_gap": 196,
        "over_conversion_guard": 196,
        "baseline_guard": 98,
    }


def test_candidate_pool_schema_and_policy_validation(tmp_path: Path) -> None:
    source_classes = (
        "project_original",
        "permissioned",
        "public_domain",
        "permissive_license",
    )
    cases = [candidate(number, source_class=source_classes[number % 4]) for number in range(1, 21)]
    pool = pool_fixture(cases)
    path = tmp_path / "pool.json"
    write_json(path, pool)

    assert validate_pool(path, check_references=False) == []

    pool["cases"][0]["expected"] = "不得出現在 input-only pool"
    write_json(path, pool)
    errors = validate_pool(path, check_references=False)
    assert any("Additional properties" in error and "expected" in error for error in errors)


def test_frozen_candidate_pool_requires_three_times_formal_n(tmp_path: Path) -> None:
    cases = [candidate(number) for number in range(1, 11)]
    pool = pool_fixture(cases)
    pool["status"] = "frozen"
    path = tmp_path / "pool.json"
    write_json(path, pool)

    errors = validate_pool(path, check_references=False)

    assert any("requires at least 1800 cases" in error for error in errors)


def test_freeze_records_canonical_pool_hash_and_empty_replacement_ledger(
    tmp_path: Path,
) -> None:
    pool = sample_pool_fixture(multiplier=3)
    pool_path = tmp_path / "pool.json"
    write_json(pool_path, pool)

    frozen, report = build_frozen_pool(
        pool_path,
        frozen_at="2026-07-30T08:30:00+08:00",
        check_references=False,
    )
    frozen_path = tmp_path / "frozen.json"
    frozen_path.write_bytes(governance.canonical_json_bytes(frozen))
    ledger = build_replacement_ledger(frozen_path, check_references=False)

    assert frozen["status"] == "frozen"
    assert report["source_pool_sha256"] == hashlib.sha256(frozen_path.read_bytes()).hexdigest()
    assert report["candidate_count"] == 1800
    assert ledger == {
        "version": 1,
        "dataset": "blind-v2",
        "source_pool_sha256": report["source_pool_sha256"],
        "seed": 20260719,
        "formal_n": 600,
        "events": [],
    }


def test_committed_frozen_pool_and_sample_are_reproducible() -> None:
    pool = governance.load_json(FROZEN_POOL)
    replacements = governance.load_json(REPLACEMENTS)
    inputs = governance.load_json(INPUTS)
    freeze_report = governance.load_json(FREEZE_REPORT)

    assert pool["status"] == "frozen"
    assert pool["stats"]["total"] == 5896
    assert pool["formal_n"] == 1960
    assert freeze_report["frozen_at"] == "2026-07-30T08:37:49+08:00"
    assert freeze_report["source_pool_sha256"] == governance.sha256_file(FROZEN_POOL)
    assert freeze_report["candidate_count"] == pool["stats"]["total"]
    assert freeze_report["converter_output_used"] is False
    assert freeze_report["expected_text_used"] is False
    assert governance.sha256_file(FROZEN_POOL) == (
        "79ab3c476c7e254e7c7a166a3fb595caf03dd4b50d86b91aa5de6c0df9375a4b"
    )
    assert governance.sha256_file(REPLACEMENTS) == (
        "e0393540e7b7385252bd6c1b7019065b66c939ca26f54dedb5f73003bf501069"
    )
    assert governance.sha256_file(INPUTS) == (
        "ddef836456ee29decf019dae981c1017b9728524c42808ae2d7c2c894299820a"
    )
    assert validate_pool(FROZEN_POOL, require_ready=True, check_references=False) == []
    replacement_errors, excluded_ids = validate_replacements(FROZEN_POOL, REPLACEMENTS)
    assert replacement_errors == []
    assert excluded_ids == set()
    assert replacements["events"] == []

    rebuilt = build_inputs(
        FROZEN_POOL,
        pool,
        pool["formal_n"],
        replacement_ledger_sha256=governance.sha256_file(REPLACEMENTS),
        excluded_ids=excluded_ids,
    )
    assert rebuilt == inputs
    assert validate_schema(inputs, governance.INPUTS_SCHEMA) == []
    assert inputs["selected_n"] == 1960
    assert len(inputs["cases"]) == 1960


def test_pool_recomputes_power_requirement(tmp_path: Path) -> None:
    cases = [candidate(number) for number in range(1, 11)]
    pool = pool_fixture(cases)
    pool["power_analysis"]["required_cases"] = 600
    path = tmp_path / "pool.json"
    write_json(path, pool)

    errors = validate_pool(path, check_references=False)

    assert any("required_cases does not match recomputed power" in error for error in errors)


def test_exact_and_near_duplicate_candidates_are_detected(tmp_path: Path) -> None:
    source_classes = (
        "project_original",
        "permissioned",
        "public_domain",
        "permissive_license",
    )
    cases = [candidate(number, source_class=source_classes[number % 4]) for number in range(1, 21)]
    cases[1]["input"] = cases[0]["input"]
    pool = pool_fixture(cases)
    path = tmp_path / "pool.json"
    write_json(path, pool)

    errors = validate_pool(path, check_references=False)
    assert any("exact duplicate candidates" in error for error in errors)

    pairs = list(
        _near_duplicate_pairs(
            [
                (
                    "first",
                    "这是一段用于检测近似重复的候选句子，内容刻意写得足够长，"
                    "以确认五字符集合在只有结尾文字不同时仍会超过预设阈值甲。",
                ),
                (
                    "second",
                    "这是一段用于检测近似重复的候选句子，内容刻意写得足够长，"
                    "以确认五字符集合在只有结尾文字不同时仍会超过预设阈值乙。",
                ),
            ],
            0.85,
        )
    )
    assert pairs and pairs[0][:2] == ("first", "second")


def test_source_caps_are_enforced_when_pool_is_ready(tmp_path: Path) -> None:
    cases = [candidate(number, source_id="one-source") for number in range(1, 21)]
    pool = pool_fixture(cases)
    path = tmp_path / "pool.json"
    write_json(path, pool)

    assert validate_pool(path, check_references=False) == []

    errors = validate_pool(path, require_ready=True, check_references=False)

    assert any("source class project_original exceeds 35%" in error for error in errors)
    assert any("source one-source exceeds 10%" in error for error in errors)


def test_deterministic_stratified_sample_is_order_independent(tmp_path: Path) -> None:
    pool = sample_pool_fixture()
    selected, quotas = deterministic_sample(pool, selected_n=600)
    reversed_pool = {**pool, "cases": list(reversed(pool["cases"]))}
    selected_reversed, reversed_quotas = deterministic_sample(reversed_pool, selected_n=600)

    assert [case["id"] for case in selected] == [case["id"] for case in selected_reversed]
    assert quotas == reversed_quotas == stratum_quotas(600)
    assert len(selected) == 600

    pool_path = tmp_path / "pool.json"
    write_json(pool_path, pool)
    inputs = build_inputs(pool_path, pool, 600)
    assert validate_schema(inputs, ACCURACY_ROOT / "blind-v2.inputs.schema.json") == []


def test_sampling_fails_when_a_stratum_is_short() -> None:
    pool = sample_pool_fixture(multiplier=1)
    pool["cases"] = [
        case
        for case in pool["cases"]
        if not (case["domain"] == "high_stakes" and case["risk"] == "baseline_guard")
    ]

    try:
        deterministic_sample(pool, selected_n=600)
    except ValueError as exc:
        assert "high_stakes/baseline_guard" in str(exc)
    else:
        raise AssertionError("short stratum must fail")


def test_final_decisions_require_exact_n_of_n_coverage(tmp_path: Path) -> None:
    pool = sample_pool_fixture(multiplier=1)
    pool_path = tmp_path / "pool.json"
    inputs_path = tmp_path / "inputs.json"
    write_json(pool_path, pool)
    inputs = build_inputs(pool_path, pool, 600)
    write_json(inputs_path, inputs)
    ids = [case["id"] for case in inputs["cases"]]
    decisions = {
        "version": 1,
        "dataset": "blind-v2",
        "inputs_sha256": hashlib.sha256(inputs_path.read_bytes()).hexdigest(),
        "approval_policy": "single_human_with_ai_advisory",
        "total_cases": 600,
        "batches": [
            {
                "id": "batch-001",
                "packet_sha256": "a" * 64,
                "decision_method": "batch_human_confirmation",
                "maintainer": "tim",
                "decision_date": "2026-07-19",
                "case_ids": ids,
                "summary": "Maintainer reviewed every input/expected pair in this packet.",
            }
        ],
    }
    decisions_path = tmp_path / "decisions.json"
    write_json(decisions_path, decisions)

    assert validate_decisions(inputs_path, decisions_path) == []

    decisions["batches"][0]["case_ids"].pop()
    write_json(decisions_path, decisions)
    assert any(
        "do not cover N/N" in error for error in validate_decisions(inputs_path, decisions_path)
    )


def test_final_decisions_reproduce_confirmed_annotation_ledger() -> None:
    generated = build_final_decisions(INPUTS, ANNOTATION_DECISIONS)
    committed = json.loads(FINAL_DECISIONS.read_text(encoding="utf-8"))

    assert generated == committed
    assert validate_decisions(INPUTS, FINAL_DECISIONS) == []
    assert sum(len(batch["case_ids"]) for batch in generated["batches"]) == 1960
    serialized = json.dumps(generated)
    assert '"expected"' not in serialized
    assert '"acceptable"' not in serialized
    assert '"output"' not in serialized


def test_replacement_ledger_requires_next_deterministic_reserve(tmp_path: Path) -> None:
    pool = sample_pool_fixture(multiplier=2)
    pool_path = tmp_path / "pool.json"
    write_json(pool_path, pool)
    initial, _ = deterministic_sample(pool, selected_n=600)
    excluded_id = initial[0]["id"]
    updated, _ = deterministic_sample(pool, selected_n=600, excluded_ids={excluded_id})
    replacement_id = next(iter({case["id"] for case in updated} - {case["id"] for case in initial}))
    ledger = {
        "version": 1,
        "dataset": "blind-v2",
        "source_pool_sha256": hashlib.sha256(pool_path.read_bytes()).hexdigest(),
        "seed": 20260719,
        "formal_n": 600,
        "events": [
            {
                "excluded_id": excluded_id,
                "replacement_id": replacement_id,
                "reason": "expected_unresolvable",
                "maintainer": "tim",
                "decision_date": "2026-07-19",
                "note": "The sentence does not provide enough context for one expected value.",
            }
        ],
    }
    ledger_path = tmp_path / "replacements.json"
    write_json(ledger_path, ledger)

    assert validate_replacements(pool_path, ledger_path) == ([], {excluded_id})

    ledger["events"][0]["replacement_id"] = initial[1]["id"]
    write_json(ledger_path, ledger)
    errors, _ = validate_replacements(pool_path, ledger_path)
    assert any("not the next deterministic reserve" in error for error in errors)


def test_one_shot_ledger_allows_interrupted_retry_but_blocks_score_reuse(tmp_path: Path) -> None:
    ledger = tmp_path / "evaluation-ledger.jsonl"
    write_ledger(
        ledger,
        [
            ledger_event("run-1", "run_started"),
            ledger_event("run-1", "run_interrupted"),
            ledger_event("run-2", "run_started"),
            ledger_event("run-2", "run_interrupted"),
        ],
    )
    assert validate_ledger(ledger) == []

    write_ledger(
        ledger,
        [
            ledger_event("run-1", "run_started"),
            ledger_event("run-1", "score_exposed"),
            ledger_event("run-2", "run_started"),
            ledger_event("run-2", "score_exposed"),
        ],
    )
    errors = validate_ledger(ledger)
    assert any("already exposed a score" in error for error in errors)
    assert any("more than one score" in error for error in errors)


def test_one_shot_ledger_rejects_overlapping_runs(tmp_path: Path) -> None:
    events = [ledger_event("run-1", "run_started"), ledger_event("run-2", "run_started")]

    assert any("overlapping active runs" in error for error in validate_ledger_events(events))


def test_one_shot_ledger_rejects_reused_run_id_and_changed_terminal_hashes() -> None:
    reused = [
        ledger_event("run-1", "run_started"),
        ledger_event("run-1", "run_interrupted"),
        ledger_event("run-1", "run_started"),
        ledger_event("run-1", "run_interrupted"),
    ]
    assert any("starts more than once" in error for error in validate_ledger_events(reused))

    changed = [ledger_event("run-1", "run_started"), ledger_event("run-1", "run_interrupted")]
    changed[1]["expected_sha256"] = "f" * 64
    assert any("changes immutable hashes" in error for error in validate_ledger_events(changed))


def test_append_ledger_event_requires_a_valid_transition(tmp_path: Path) -> None:
    ledger = tmp_path / "evaluation-ledger.jsonl"
    append_ledger_event(ledger, ledger_event("run-1", "run_started"))
    append_ledger_event(ledger, ledger_event("run-1", "run_interrupted"))

    assert validate_ledger(ledger) == []
    with pytest.raises(ValueError, match="ends without run_started"):
        append_ledger_event(ledger, ledger_event("run-2", "score_exposed"))


def test_blind_v2_private_artifacts_are_gitignored() -> None:
    private_paths = (
        "benchmarks/accuracy/blind-v2.expected.json",
        "benchmarks/accuracy/private/blind-v2.evaluation-ledger.jsonl",
        "docs/reports/blind-v2-private-annotation-batch-001-packet.json",
        "docs/reports/blind-v2-private-codex-advisory.json",
        "docs/reports/blind-v2-private-agy-independent-batch-001.json",
        "docs/reports/blind-v2-private-codex-synthesis-batch-001.json",
    )
    for path in private_paths:
        result = subprocess.run(
            ["git", "check-ignore", "--no-index", "--quiet", "--", path],
            cwd=ROOT,
            check=False,
        )
        assert result.returncode == 0, path


def test_reference_scan_does_not_read_untracked_json(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    paths = (
        tmp_path / "benchmarks/accuracy/untracked.json",
        tmp_path / "docs/reports/untracked.json",
        tmp_path / "src/zhtw/data/terms/cn/untracked.json",
    )
    for path in paths:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("private expected, not valid JSON", encoding="utf-8")
    monkeypatch.setattr(governance, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(governance, "_is_tracked", lambda path: False)
    pool = pool_fixture([])

    texts, errors, _ = reference_texts(pool, tmp_path / "pool.json")

    assert texts == []
    assert errors == []


def test_tracked_check_does_not_treat_git_failure_as_untracked(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    path = tmp_path / "report.json"
    monkeypatch.setattr(governance, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(
        governance.subprocess,
        "run",
        lambda *args, **kwargs: subprocess.CompletedProcess(
            args[0], 128, stdout="", stderr="fatal: invalid git configuration"
        ),
    )

    with pytest.raises(RuntimeError, match="git ls-files failed"):
        governance._is_tracked(path)


def test_reference_snapshot_ignores_tracked_json_without_reference_text(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    reports = tmp_path / "docs/reports"
    reports.mkdir(parents=True)
    metadata = reports / "metadata.json"
    metadata.write_text('{"status": "reviewed"}\n', encoding="utf-8")
    reference = reports / "reference.json"
    reference.write_text('{"input": "候選參考句"}\n', encoding="utf-8")
    monkeypatch.setattr(governance, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(governance, "_is_tracked", lambda path: True)
    pool = pool_fixture([])
    pool["deduplication"]["reference_globs"] = ["docs/reports/*.json"]

    texts, errors, snapshot_hash = reference_texts(pool, tmp_path / "pool.json")
    reference.unlink()
    _, second_errors, metadata_only_hash = reference_texts(pool, tmp_path / "pool.json")

    assert texts == ["候選參考句"]
    assert errors == second_errors == []
    assert snapshot_hash != metadata_only_hash


def test_reference_scan_ignores_blind_v2_governance_reports(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    reports = tmp_path / "docs/reports"
    reports.mkdir(parents=True)
    governance_report = reports / "blind-v2-source-classification-maintainer-decision.json"
    governance_report.write_text('{"input": "治理報告不應成為參考"}\n', encoding="utf-8")
    benchmark_report = reports / "accuracy-public-cases.json"
    benchmark_report.write_text('{"input": "公開評測案例仍須去重"}\n', encoding="utf-8")
    monkeypatch.setattr(governance, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(governance, "_is_tracked", lambda path: True)
    pool = pool_fixture([])
    pool["deduplication"]["reference_globs"] = ["docs/reports/*.json"]

    texts, errors, _ = reference_texts(pool, tmp_path / "pool.json")

    assert errors == []
    assert texts == ["公開評測案例仍須去重"]
