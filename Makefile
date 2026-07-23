# Makefile — zhtw monorepo unified entry point

.PHONY: export export-check precision-benchmark benchmark-validate benchmark-competitor-build benchmark-competitor-probe benchmark-ud-import-check benchmark-ud-report benchmark-naer-import-check benchmark-naer-report benchmark-blind-v2-source-import-check benchmark-blind-v2-source-classification-check benchmark-blind-v2-pool-validate benchmark-blind-v2-replacements-validate benchmark-blind-v2-sample benchmark-blind-v2-decisions-validate benchmark-blind-v2-ledger-validate accuracy-annotation-status accuracy-blind-review-packet accuracy-gemini-advisory accuracy-promotion-gate accuracy-promote-backlog accuracy-holdout-annotation-packet accuracy-holdout-gemini-advisory accuracy-benchmark test test-all test-python test-java test-typescript test-rust test-go test-dotnet test-corpus-prepare release-gate version-check bump release help

PYTHON := uv run python
VERSION ?=
BATCH ?= it-api-cli
DATE ?= $(shell date +%F)
ISSUE ?=
MAINTAINER ?= tim
REVIEWED_AT ?=
ID_FROM ?=
ID_TO ?=
COMPETITORS ?= zhtw
REVIEWER_STAGE ?= first_human_review
HOLDOUT_BATCH ?=
COMPETITOR_ENV_HASH := $(shell jq -r '.environment.environment_sha256' benchmarks/accuracy/competitors.lock.json)
COMPETITOR_IMAGE ?= zhtw-benchmark-competitors:$(shell printf '%s' '$(COMPETITOR_ENV_HASH)' | cut -c1-12)
BLIND_V2_POOL ?= benchmarks/accuracy/blind-v2.candidate-pool.json
BLIND_V2_INPUTS ?= benchmarks/accuracy/blind-v2.inputs.json
BLIND_V2_REPLACEMENTS ?= benchmarks/accuracy/blind-v2.replacements.json
BLIND_V2_DECISIONS ?= benchmarks/accuracy/blind-v2.final-decisions.json
BLIND_V2_LEDGER ?= benchmarks/accuracy/private/blind-v2.evaluation-ledger.jsonl
BLIND_V2_N ?= 1960

# === Core ===

export: ## Export SDK data (zhtw-data.json + golden-test.json)
	$(PYTHON) -m zhtw export --output sdk/data --verbose
	@mkdir -p sdk/rust/zhtw/data
	@cp sdk/data/zhtw-data.json sdk/rust/zhtw/data/zhtw-data.json
	@echo "  synced crate-local copy → sdk/rust/zhtw/data/zhtw-data.json"
	@cp sdk/data/zhtw-data.json sdk/go/zhtw/zhtw-data.json
	@echo "  synced Go embed copy → sdk/go/zhtw/zhtw-data.json"

export-check: ## Verify committed SDK data exactly matches a fresh export
	@tmp=$$(mktemp -d); \
	  trap 'rm -rf "$$tmp"' EXIT; \
	  $(PYTHON) -m zhtw export --output "$$tmp" >/dev/null; \
	  for f in zhtw-data.json golden-test.json; do \
	    if ! cmp -s "sdk/data/$$f" "$$tmp/$$f"; then \
	      echo "❌ sdk/data/$$f is stale — run 'make export'"; \
	      exit 1; \
	    fi; \
	  done; \
	  cmp -s sdk/data/zhtw-data.json sdk/rust/zhtw/data/zhtw-data.json || \
	    { echo "❌ Rust SDK data copy is stale — run 'make export'"; exit 1; }; \
	  cmp -s sdk/data/zhtw-data.json sdk/go/zhtw/zhtw-data.json || \
	    { echo "❌ Go SDK data copy is stale — run 'make export'"; exit 1; }; \
	  echo "✅ SDK data matches a fresh export"

precision-benchmark: ## Compare zhtw precision with optional competitor converters
	$(PYTHON) scripts/competitor_benchmark.py

accuracy-annotation-status: ## Report M1 annotation backlog progress
	$(PYTHON) scripts/accuracy_annotation_status.py

accuracy-blind-review-packet: ## Create a blind review packet for annotation cases
	$(PYTHON) scripts/create_blind_review_packet.py --batch $(BATCH) --generated-date $(DATE) --output docs/reports/annotation-blind-review-packet-$(BATCH)-$(DATE).md

accuracy-gemini-advisory: ## Generate Gemini Vertex advisory review for annotation cases
	$(PYTHON) scripts/generate_gemini_vertex_advisory.py --batch $(BATCH) --generated-date $(DATE) $(if $(ID_FROM),--id-from $(ID_FROM),) $(if $(ID_TO),--id-to $(ID_TO),) --output-json docs/reports/annotation-gemini-vertex-advisory-$(BATCH)-$(DATE).json --output-md docs/reports/annotation-gemini-vertex-advisory-$(BATCH)-$(DATE).md --update-backlog

accuracy-promotion-gate: ## Check approved annotation cases against current zhtw output
	$(PYTHON) scripts/check_accuracy_backlog.py --generated-date $(DATE) --output-json docs/reports/annotation-promotion-gate-$(DATE).json --output-md docs/reports/annotation-promotion-gate-$(DATE).md

accuracy-promote-backlog: ## Promote promotion-ready annotation cases into regression-v1
	$(PYTHON) scripts/promote_accuracy_backlog.py --gate docs/reports/annotation-promotion-gate-$(DATE).json

accuracy-holdout-annotation-packet: ## Create a human annotation packet for sealed holdout inputs
	$(PYTHON) scripts/create_holdout_annotation_packet.py --generated-date $(DATE) --reviewer-stage $(REVIEWER_STAGE) $(if $(HOLDOUT_BATCH),--batch $(HOLDOUT_BATCH),) $(if $(ID_FROM),--id-from $(ID_FROM),) $(if $(ID_TO),--id-to $(ID_TO),) --output docs/reports/holdout-annotation-packet-blind-v1-$(REVIEWER_STAGE)-$(DATE).md

accuracy-holdout-gemini-advisory: ## Generate Gemini Vertex advisory for sealed holdout inputs
	$(PYTHON) scripts/generate_holdout_gemini_vertex_advisory.py --generated-date $(DATE) $(if $(HOLDOUT_BATCH),--batch $(HOLDOUT_BATCH),) $(if $(ID_FROM),--id-from $(ID_FROM),) $(if $(ID_TO),--id-to $(ID_TO),) --output-json docs/reports/holdout-gemini-vertex-advisory-blind-v1-0001-0100-$(DATE).json --output-md docs/reports/holdout-gemini-vertex-advisory-blind-v1-0001-0100-$(DATE).md

benchmark-validate: ## Validate benchmark manifests, licenses, hashes, and preregistrations
	$(PYTHON) scripts/validate_benchmark_assets.py
	$(PYTHON) scripts/audit_benchmark_publication.py

benchmark-competitor-build: ## Build the digest-pinned competitor environment
	docker build --build-arg ENVIRONMENT_HASH=$(COMPETITOR_ENV_HASH) --tag $(COMPETITOR_IMAGE) --file benchmarks/accuracy/competitor-env/Dockerfile benchmarks/accuracy/competitor-env

benchmark-competitor-probe: benchmark-competitor-build ## Probe every locked competitor adapter
	$(PYTHON) scripts/validate_competitor_environment.py --image $(COMPETITOR_IMAGE)

benchmark-ud-import-check: ## Download pinned UD sources and verify normalized output
	$(PYTHON) scripts/import_ud_gsd_benchmark.py --check

benchmark-ud-report: ## Run the public UD GSD/GSDSimp secondary track
	$(PYTHON) scripts/run_ud_gsd_benchmark.py --generated-date $(DATE) --output-prefix docs/reports/ud-gsd-benchmark-$(DATE)

benchmark-naer-import-check: ## Download pinned NAER source and verify normalized output
	$(PYTHON) scripts/import_naer_terms_benchmark.py --check

benchmark-naer-report: ## Run the public NAER computer terminology secondary track
	$(PYTHON) scripts/run_naer_terms_benchmark.py --generated-date $(DATE) --output-prefix docs/reports/naer-terms-benchmark-$(DATE)

benchmark-blind-v2-source-import-check: ## Download pinned Blind-v2 source pilots and verify input-only outputs
	$(PYTHON) scripts/import_blind_v2_source_pilot.py --manifest benchmarks/accuracy/manifests/flores-200-zho-hans-v1.json --check
	$(PYTHON) scripts/import_blind_v2_source_pilot.py --manifest benchmarks/accuracy/manifests/ud-chinese-cfl-v1.json --check
	$(PYTHON) scripts/import_blind_v2_source_pilot.py --manifest benchmarks/accuracy/manifests/cdc-stacks-111808-v1.json --check
	$(PYTHON) scripts/import_blind_v2_source_pilot.py --manifest benchmarks/accuracy/manifests/cdc-stacks-120024-v1.json --check
	$(PYTHON) scripts/import_blind_v2_source_pilot.py --manifest benchmarks/accuracy/manifests/cdc-stacks-116683-v1.json --check
	$(PYTHON) scripts/import_blind_v2_source_pilot.py --manifest benchmarks/accuracy/manifests/zhtw-project-ui-i18n-v1.json --check
	$(PYTHON) scripts/import_blind_v2_source_pilot.py --manifest benchmarks/accuracy/manifests/zhtw-project-llm-product-v1.json --check
	$(PYTHON) scripts/import_blind_v2_source_pilot.py --manifest benchmarks/accuracy/manifests/zhtw-project-it-api-cli-v1.json --check
	$(PYTHON) scripts/import_blind_v2_source_pilot.py --manifest benchmarks/accuracy/manifests/massive-1-0-zh-cn-v1.json --check
	$(PYTHON) scripts/import_blind_v2_source_pilot.py --manifest benchmarks/accuracy/manifests/ftc-small-business-simplified-v1.json --check
	$(PYTHON) scripts/import_blind_v2_source_pilot.py --manifest benchmarks/accuracy/manifests/nps-essential-acadia-simplified-v1.json --check
	$(PYTHON) scripts/import_blind_v2_source_pilot.py --manifest benchmarks/accuracy/manifests/ready-gov-floods-zh-hans-v1.json --check
	$(PYTHON) scripts/import_blind_v2_source_pilot.py --manifest benchmarks/accuracy/manifests/ready-gov-hurricanes-zh-hans-v1.json --check
	$(PYTHON) scripts/import_blind_v2_source_pilot.py --manifest benchmarks/accuracy/manifests/ready-gov-earthquakes-zh-hans-v1.json --check

benchmark-blind-v2-permissioned-intake-check: ## Validate the collecting permissioned user-report batch
	$(PYTHON) scripts/validate_permissioned_user_reports.py benchmarks/accuracy/sources/permissioned-user-report-batch-001.json

benchmark-blind-v2-permissioned-issue-preview: ## Preview a permissioned GitHub issue (ISSUE=N)
	@test -n "$(ISSUE)" || (echo "ISSUE is required" >&2; exit 2)
	$(PYTHON) scripts/import_permissioned_user_report_issue.py --issue $(ISSUE)

benchmark-blind-v2-permissioned-issue-import: ## Import a reviewed issue (ISSUE=N REVIEWED_AT=ISO8601)
	@test -n "$(ISSUE)" || (echo "ISSUE is required" >&2; exit 2)
	@test -n "$(REVIEWED_AT)" || (echo "REVIEWED_AT is required" >&2; exit 2)
	$(PYTHON) scripts/import_permissioned_user_report_issue.py --issue $(ISSUE) --write --maintainer $(MAINTAINER) --reviewed-at $(REVIEWED_AT)

benchmark-blind-v2-permissioned-ready-check: ## Require a complete 100-case permissioned user-report batch
	$(PYTHON) scripts/validate_permissioned_user_reports.py --require-ready benchmarks/accuracy/sources/permissioned-user-report-batch-001.json

benchmark-blind-v2-source-classification-check: ## Verify deterministic input-only source classification packet
	$(PYTHON) scripts/create_blind_v2_source_classification_packet.py --generated-date 2026-07-20 --batch-number 1 --output benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-001.json --markdown-output benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-001.md --check
	$(PYTHON) scripts/record_blind_v2_source_classification_decision.py --packet benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-001.json --codex docs/reports/blind-v2-source-classification-codex-first-pass-batch-001-2026-07-20.json --gemini docs/reports/blind-v2-source-classification-gemini-independent-batch-001-2026-07-20.json --maintainer tim --decision-date 2026-07-21 --selected-advisory codex --output docs/reports/blind-v2-source-classification-maintainer-decision-batch-001-2026-07-21.json --check
	$(PYTHON) scripts/compare_blind_v2_source_classifications.py --packet benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-001.json --codex docs/reports/blind-v2-source-classification-codex-first-pass-batch-001-2026-07-20.json --gemini docs/reports/blind-v2-source-classification-gemini-independent-batch-001-2026-07-20.json --maintainer-decisions docs/reports/blind-v2-source-classification-maintainer-decision-batch-001-2026-07-21.json --generated-date 2026-07-20 --output docs/reports/blind-v2-source-classification-diff-batch-001-2026-07-20.md --check
	$(PYTHON) scripts/create_blind_v2_source_classification_packet.py --generated-date 2026-07-21 --batch-number 2 --output benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-002.json --markdown-output benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-002.md --check
	$(PYTHON) scripts/record_blind_v2_source_classification_decision.py --packet benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-002.json --codex docs/reports/blind-v2-source-classification-codex-first-pass-batch-002-2026-07-21.json --gemini docs/reports/blind-v2-source-classification-gemini-independent-batch-002-2026-07-21.json --maintainer tim --decision-date 2026-07-21 --selected-advisory codex --output docs/reports/blind-v2-source-classification-maintainer-decision-batch-002-2026-07-21.json --check
	$(PYTHON) scripts/compare_blind_v2_source_classifications.py --packet benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-002.json --codex docs/reports/blind-v2-source-classification-codex-first-pass-batch-002-2026-07-21.json --gemini docs/reports/blind-v2-source-classification-gemini-independent-batch-002-2026-07-21.json --maintainer-decisions docs/reports/blind-v2-source-classification-maintainer-decision-batch-002-2026-07-21.json --generated-date 2026-07-21 --output docs/reports/blind-v2-source-classification-diff-batch-002-2026-07-21.md --check
	$(PYTHON) scripts/create_blind_v2_source_classification_packet.py --source benchmarks/accuracy/external/cdc-stacks-111808-v1.json --source benchmarks/accuracy/external/cdc-stacks-120024-v1.json --source benchmarks/accuracy/external/cdc-stacks-116683-v1.json --all-source-cases --batch-number 3 --generated-date 2026-07-22 --output benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-003.json --markdown-output benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-003.md --check
	$(PYTHON) scripts/record_blind_v2_source_classification_decision.py --packet benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-003.json --codex docs/reports/blind-v2-source-classification-codex-first-pass-batch-003-2026-07-22.json --gemini docs/reports/blind-v2-source-classification-gemini-independent-batch-003-2026-07-22.json --maintainer tim --decision-date 2026-07-22 --selected-advisory codex --output docs/reports/blind-v2-source-classification-maintainer-decision-batch-003-2026-07-22.json --check
	$(PYTHON) scripts/compare_blind_v2_source_classifications.py --packet benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-003.json --codex docs/reports/blind-v2-source-classification-codex-first-pass-batch-003-2026-07-22.json --gemini docs/reports/blind-v2-source-classification-gemini-independent-batch-003-2026-07-22.json --maintainer-decisions docs/reports/blind-v2-source-classification-maintainer-decision-batch-003-2026-07-22.json --generated-date 2026-07-22 --output docs/reports/blind-v2-source-classification-diff-batch-003-2026-07-22.md --check
	$(PYTHON) scripts/create_blind_v2_source_classification_packet.py --source benchmarks/accuracy/external/zhtw-project-ui-i18n-v1.json --source benchmarks/accuracy/external/zhtw-project-llm-product-v1.json --all-source-cases --batch-number 4 --generated-date 2026-07-23 --output benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-004.json --markdown-output benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-004.md --check
	$(PYTHON) scripts/record_blind_v2_source_classification_decision.py --packet benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-004.json --codex docs/reports/blind-v2-source-classification-codex-first-pass-batch-004-2026-07-23.json --gemini docs/reports/blind-v2-source-classification-gemini-independent-batch-004-2026-07-23.json --synthesis docs/reports/blind-v2-source-classification-codex-synthesis-batch-004-2026-07-23.json --maintainer tim --decision-date 2026-07-23 --selected-advisory synthesis --output docs/reports/blind-v2-source-classification-maintainer-decision-batch-004-2026-07-23.json --check
	$(PYTHON) scripts/compare_blind_v2_source_classifications.py --packet benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-004.json --codex docs/reports/blind-v2-source-classification-codex-first-pass-batch-004-2026-07-23.json --gemini docs/reports/blind-v2-source-classification-gemini-independent-batch-004-2026-07-23.json --maintainer-decisions docs/reports/blind-v2-source-classification-maintainer-decision-batch-004-2026-07-23.json --generated-date 2026-07-23 --output docs/reports/blind-v2-source-classification-diff-batch-004-2026-07-23.md --check
	$(PYTHON) scripts/create_blind_v2_source_classification_packet.py --source benchmarks/accuracy/external/massive-1-0-zh-cn-v1.json --batch-size 100 --batch-number 5 --selection-round 1 --generated-date 2026-07-23 --output benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-005.json --markdown-output benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-005.md --check
	$(PYTHON) scripts/record_blind_v2_source_classification_decision.py --packet benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-005.json --codex docs/reports/blind-v2-source-classification-codex-first-pass-batch-005-2026-07-23.json --gemini docs/reports/blind-v2-source-classification-gemini-independent-batch-005-2026-07-23.json --synthesis docs/reports/blind-v2-source-classification-codex-synthesis-batch-005-2026-07-23.json --maintainer tim --decision-date 2026-07-23 --selected-advisory synthesis --output docs/reports/blind-v2-source-classification-maintainer-decision-batch-005-2026-07-23.json --check
	$(PYTHON) scripts/compare_blind_v2_source_classifications.py --packet benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-005.json --codex docs/reports/blind-v2-source-classification-codex-first-pass-batch-005-2026-07-23.json --gemini docs/reports/blind-v2-source-classification-gemini-independent-batch-005-2026-07-23.json --maintainer-decisions docs/reports/blind-v2-source-classification-maintainer-decision-batch-005-2026-07-23.json --generated-date 2026-07-23 --output docs/reports/blind-v2-source-classification-diff-batch-005-2026-07-23.md --check
	$(PYTHON) scripts/create_blind_v2_source_classification_packet.py --source benchmarks/accuracy/external/zhtw-project-it-api-cli-v1.json --all-source-cases --batch-number 6 --generated-date 2026-07-23 --output benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-006.json --markdown-output benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-006.md --check
	$(PYTHON) scripts/record_blind_v2_source_classification_decision.py --packet benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-006.json --codex docs/reports/blind-v2-source-classification-codex-first-pass-batch-006-2026-07-23.json --gemini docs/reports/blind-v2-source-classification-gemini-independent-batch-006-2026-07-23.json --synthesis docs/reports/blind-v2-source-classification-codex-synthesis-batch-006-2026-07-23.json --maintainer tim --decision-date 2026-07-23 --selected-advisory synthesis --output docs/reports/blind-v2-source-classification-maintainer-decision-batch-006-2026-07-23.json --check
	$(PYTHON) scripts/compare_blind_v2_source_classifications.py --packet benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-006.json --codex docs/reports/blind-v2-source-classification-codex-first-pass-batch-006-2026-07-23.json --gemini docs/reports/blind-v2-source-classification-gemini-independent-batch-006-2026-07-23.json --maintainer-decisions docs/reports/blind-v2-source-classification-maintainer-decision-batch-006-2026-07-23.json --generated-date 2026-07-23 --output docs/reports/blind-v2-source-classification-diff-batch-006-2026-07-23.md --check
	$(PYTHON) scripts/create_blind_v2_source_classification_packet.py --source benchmarks/accuracy/external/ftc-small-business-simplified-v1.json --all-source-cases --batch-number 7 --generated-date 2026-07-23 --output benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-007.json --markdown-output benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-007.md --check
	$(PYTHON) scripts/record_blind_v2_source_classification_decision.py --packet benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-007.json --codex docs/reports/blind-v2-source-classification-codex-first-pass-batch-007-2026-07-23.json --gemini docs/reports/blind-v2-source-classification-gemini-independent-batch-007-2026-07-23.json --synthesis docs/reports/blind-v2-source-classification-codex-synthesis-batch-007-2026-07-23.json --maintainer tim --decision-date 2026-07-23 --selected-advisory synthesis --output docs/reports/blind-v2-source-classification-maintainer-decision-batch-007-2026-07-23.json --check
	$(PYTHON) scripts/compare_blind_v2_source_classifications.py --packet benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-007.json --codex docs/reports/blind-v2-source-classification-codex-first-pass-batch-007-2026-07-23.json --gemini docs/reports/blind-v2-source-classification-gemini-independent-batch-007-2026-07-23.json --maintainer-decisions docs/reports/blind-v2-source-classification-maintainer-decision-batch-007-2026-07-23.json --generated-date 2026-07-23 --output docs/reports/blind-v2-source-classification-diff-batch-007-2026-07-23.md --check
	$(PYTHON) scripts/create_blind_v2_source_classification_packet.py --source benchmarks/accuracy/external/nps-essential-acadia-simplified-v1.json --all-source-cases --batch-number 8 --generated-date 2026-07-23 --output benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-008.json --markdown-output benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-008.md --check
	$(PYTHON) scripts/record_blind_v2_source_classification_decision.py --packet benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-008.json --codex docs/reports/blind-v2-source-classification-codex-first-pass-batch-008-2026-07-23.json --gemini docs/reports/blind-v2-source-classification-gemini-independent-batch-008-2026-07-23.json --synthesis docs/reports/blind-v2-source-classification-codex-synthesis-batch-008-2026-07-23.json --maintainer tim --decision-date 2026-07-23 --selected-advisory synthesis --output docs/reports/blind-v2-source-classification-maintainer-decision-batch-008-2026-07-23.json --check
	$(PYTHON) scripts/compare_blind_v2_source_classifications.py --packet benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-008.json --codex docs/reports/blind-v2-source-classification-codex-first-pass-batch-008-2026-07-23.json --gemini docs/reports/blind-v2-source-classification-gemini-independent-batch-008-2026-07-23.json --maintainer-decisions docs/reports/blind-v2-source-classification-maintainer-decision-batch-008-2026-07-23.json --generated-date 2026-07-23 --output docs/reports/blind-v2-source-classification-diff-batch-008-2026-07-23.md --check
	$(PYTHON) scripts/create_blind_v2_source_classification_packet.py --source benchmarks/accuracy/external/ready-gov-floods-zh-hans-v1.json --source benchmarks/accuracy/external/ready-gov-hurricanes-zh-hans-v1.json --source benchmarks/accuracy/external/ready-gov-earthquakes-zh-hans-v1.json --batch-size 100 --batch-number 9 --selection-round 1 --generated-date 2026-07-23 --output benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-009.json --markdown-output benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-009.md --check
	$(PYTHON) scripts/record_blind_v2_source_classification_decision.py --packet benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-009.json --codex docs/reports/blind-v2-source-classification-codex-first-pass-batch-009-2026-07-23.json --gemini docs/reports/blind-v2-source-classification-gemini-independent-batch-009-2026-07-23.json --synthesis docs/reports/blind-v2-source-classification-codex-synthesis-batch-009-2026-07-23.json --maintainer tim --decision-date 2026-07-23 --selected-advisory synthesis --output docs/reports/blind-v2-source-classification-maintainer-decision-batch-009-2026-07-23.json --check
	$(PYTHON) scripts/compare_blind_v2_source_classifications.py --packet benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-009.json --codex docs/reports/blind-v2-source-classification-codex-first-pass-batch-009-2026-07-23.json --gemini docs/reports/blind-v2-source-classification-gemini-independent-batch-009-2026-07-23.json --maintainer-decisions docs/reports/blind-v2-source-classification-maintainer-decision-batch-009-2026-07-23.json --generated-date 2026-07-23 --output docs/reports/blind-v2-source-classification-diff-batch-009-2026-07-23.md --check

benchmark-blind-v2-pool-validate: ## Validate Blind-v2 source, dedupe, quota, and size policy
	$(PYTHON) scripts/blind_v2_governance.py validate-pool $(BLIND_V2_POOL) --require-ready

benchmark-blind-v2-pool-collecting-check: ## Rebuild and validate the current collecting pool
	$(PYTHON) scripts/promote_blind_v2_candidates.py --decision docs/reports/blind-v2-source-classification-maintainer-decision-batch-001-2026-07-21.json --decision docs/reports/blind-v2-source-classification-maintainer-decision-batch-002-2026-07-21.json --decision docs/reports/blind-v2-source-classification-maintainer-decision-batch-003-2026-07-22.json --decision docs/reports/blind-v2-source-classification-maintainer-decision-batch-004-2026-07-23.json --decision docs/reports/blind-v2-source-classification-maintainer-decision-batch-005-2026-07-23.json --decision docs/reports/blind-v2-source-classification-maintainer-decision-batch-006-2026-07-23.json --decision docs/reports/blind-v2-source-classification-maintainer-decision-batch-007-2026-07-23.json --decision docs/reports/blind-v2-source-classification-maintainer-decision-batch-008-2026-07-23.json --decision docs/reports/blind-v2-source-classification-maintainer-decision-batch-009-2026-07-23.json --created-at 2026-07-23T00:00:00+08:00 --output $(BLIND_V2_POOL) --report docs/reports/blind-v2-candidate-promotion-batches-001-009-2026-07-23.md --check
	$(PYTHON) scripts/blind_v2_governance.py validate-pool $(BLIND_V2_POOL)

benchmark-blind-v2-replacements-validate: ## Validate deterministic Blind-v2 replacements
	$(PYTHON) scripts/blind_v2_governance.py validate-replacements $(BLIND_V2_POOL) $(BLIND_V2_REPLACEMENTS)

benchmark-blind-v2-sample: ## Deterministically sample the frozen Blind-v2 pool
	$(PYTHON) scripts/blind_v2_governance.py sample $(BLIND_V2_POOL) --selected-n $(BLIND_V2_N) --replacements $(BLIND_V2_REPLACEMENTS) --output $(BLIND_V2_INPUTS)

benchmark-blind-v2-decisions-validate: ## Require maintainer decisions for every Blind-v2 case
	$(PYTHON) scripts/blind_v2_governance.py validate-decisions $(BLIND_V2_INPUTS) $(BLIND_V2_DECISIONS)

benchmark-blind-v2-ledger-validate: ## Validate the private Blind-v2 one-shot ledger
	$(PYTHON) scripts/blind_v2_governance.py validate-ledger $(BLIND_V2_LEDGER)

accuracy-benchmark: ## Run the published blind-v1 evaluation benchmark
	$(PYTHON) scripts/run_accuracy_benchmark.py --inputs benchmarks/accuracy/blind-v1.inputs.json --expected benchmarks/accuracy/blind-v1.expected.json --competitors-lock benchmarks/accuracy/competitors.lock.json --competitors $(COMPETITORS) --generated-date $(DATE) --output-prefix docs/reports/accuracy-benchmark-$(DATE)

test-python: ## Run Python tests
	$(PYTHON) -m pytest tests/ -v

test-java: ## Run Java SDK tests
	cd sdk/java && mvn verify --batch-mode

test-typescript: ## Run TypeScript SDK tests and type-check
	cd sdk/typescript && pnpm install --frozen-lockfile && pnpm exec tsc --noEmit && pnpm test && pnpm build

test-rust: ## Run Rust SDK and WASM host tests
	cd sdk/rust && cargo test --workspace --release

test-go: ## Run Go SDK tests, vet, and lint
	cd sdk/go && go test ./... -race
	cd sdk/go && go vet ./...
	cd sdk/go && go run github.com/golangci/golangci-lint/cmd/golangci-lint@v1.64.8 run

test-dotnet: ## Run .NET SDK tests
	cd sdk/dotnet && DOTNET_ROLL_FORWARD=Major dotnet test tests/Zhtw.Tests/Zhtw.Tests.csproj -c Release

test-all: test-python test-java test-typescript test-rust test-go test-dotnet ## Run every SDK test suite

test: test-all ## Run every SDK test suite

test-corpus-prepare: ## Clone or verify the pinned public corpus
	@bash scripts/prepare-test-corpus.sh

release-gate: test-corpus-prepare ## Run the exact local/CI release gate
	@$(MAKE) version-check export-check
	uv run zhtw validate
	@$(MAKE) benchmark-validate
	uv run python scripts/audit_idempotency.py --sources cn,hk --curated-only --fail-on-issues
	@$(MAKE) test-all

# === Version management (mono-versioning) ===

version-check: ## Verify all SDK versions are aligned (mono-versioning)
	@PY_VER=$$(grep '^version = ' pyproject.toml | sed 's/version = "\(.*\)"/\1/'); \
	 INIT_VER=$$(grep '^__version__' src/zhtw/__init__.py | sed 's/__version__ = "\(.*\)"/\1/'); \
	 JAVA_VER=$$(sed -n 's|.*<version>\(.*\)</version>.*|\1|p' sdk/java/pom.xml | head -1); \
	 TS_VER=$$(grep '"version"' sdk/typescript/package.json | head -1 | sed 's/.*"version": "\(.*\)".*/\1/'); \
	 RUST_VER=$$(sed -n '/\[workspace\.package\]/,/^\[/ s/^version = "\(.*\)"/\1/p' sdk/rust/Cargo.toml); \
	 NET_VER=$$(sed -n 's|.*<Version>\(.*\)</Version>.*|\1|p' sdk/dotnet/Zhtw.csproj); \
	 DATA_VER=$$(grep -o '"version": *"[^"]*"' sdk/data/zhtw-data.json | head -1 | sed 's/.*"version": *"\(.*\)"/\1/'); \
	 WASM_VER=$$(grep '"version"' sdk/rust/zhtw-wasm/package.json | head -1 | sed 's/.*"version": "\(.*\)".*/\1/'); \
	 printf "  %-28s %s\n" "Python (pyproject.toml):" "$$PY_VER"; \
	 printf "  %-28s %s\n" "Python (__init__.py):"    "$$INIT_VER"; \
	 printf "  %-28s %s\n" "Java (sdk/java/pom.xml):" "$$JAVA_VER"; \
	 printf "  %-28s %s\n" "TypeScript (package.json):" "$$TS_VER"; \
	 printf "  %-28s %s\n" "Rust (Cargo.toml):"       "$$RUST_VER"; \
	 printf "  %-28s %s\n" ".NET (Zhtw.csproj):"      "$$NET_VER"; \
	 printf "  %-28s %s\n" "sdk/data/zhtw-data.json:" "$$DATA_VER"; \
	 printf "  %-28s %s\n" "WASM (zhtw-wasm/package.json):" "$$WASM_VER"; \
	 if [ "$$PY_VER" != "$$INIT_VER" ] || [ "$$PY_VER" != "$$JAVA_VER" ] || \
	    [ "$$PY_VER" != "$$TS_VER" ] || [ "$$PY_VER" != "$$RUST_VER" ] || \
	    [ "$$PY_VER" != "$$NET_VER" ] || [ "$$PY_VER" != "$$DATA_VER" ] || \
	    [ "$$PY_VER" != "$$WASM_VER" ]; then \
	   echo ""; \
	   echo "❌ Version mismatch — all SDKs must stay in sync (mono-versioning)"; \
	   echo "   Fix: run 'make bump VERSION=X.Y.Z' or 'make release VERSION=X.Y.Z'"; \
	   exit 1; \
	 fi; \
	 echo ""; \
	 echo "✅ All SDKs aligned at $$PY_VER"
	@if ! cmp -s sdk/data/zhtw-data.json sdk/rust/zhtw/data/zhtw-data.json 2>/dev/null; then \
	  echo ""; \
	  echo "❌ sdk/rust/zhtw/data/zhtw-data.json is out of sync"; \
	  echo "   Fix: run 'make export'"; \
	  exit 1; \
	fi
	@if ! cmp -s sdk/data/zhtw-data.json sdk/go/zhtw/zhtw-data.json 2>/dev/null; then \
	  echo ""; \
	  echo "❌ sdk/go/zhtw/zhtw-data.json is out of sync"; \
	  echo "   Fix: run 'make export'"; \
	  exit 1; \
	fi

bump: ## Bump all SDK versions without commit/tag/release: make bump VERSION=x.y.z
ifndef VERSION
	$(error VERSION is required. Usage: make bump VERSION=4.0.0)
endif
	@echo "📝 Bumping all SDKs to $(VERSION)..."
	@sed -i '' 's/^version = .*/version = "$(VERSION)"/' pyproject.toml
	@sed -i '' 's/^__version__ = .*/__version__ = "$(VERSION)"/' src/zhtw/__init__.py
	@# Only match the project version (4-space indent, top level of <project>).
	@# Plugin versions are nested deeper (12+ spaces) and must not be touched.
	@sed -i '' 's|^    <version>[^<]*</version>|    <version>$(VERSION)</version>|' sdk/java/pom.xml
	@sed -i '' 's/"version": "[^"]*"/"version": "$(VERSION)"/' sdk/typescript/package.json
	@sed -i '' '/^\[workspace\.package\]/,/^\[/ s|^version = "[0-9][0-9.]*"|version = "$(VERSION)"|' sdk/rust/Cargo.toml
	@sed -i '' 's/"version": "[^"]*"/"version": "$(VERSION)"/' sdk/rust/zhtw-wasm/package.json
	@sed -i '' 's|<Version>[^<]*</Version>|<Version>$(VERSION)</Version>|' sdk/dotnet/Zhtw.csproj
	@# AGENTS.md 標頭版本（曾因不在 bump 清單而漂移）
	@sed -i '' 's|^> \*\*v[0-9][0-9.]*\*\*|> **v$(VERSION)**|' AGENTS.md
	@# README files: Maven dep version, Gradle (Kotlin + Groovy), pre-commit rev tag.
	@# Pattern requires the version starts with a digit so we never touch placeholders.
	@sed -i '' 's|<version>[0-9][0-9.]*</version>|<version>$(VERSION)</version>|g' README.md README.en.md
	@sed -i '' 's|com.rajatim:zhtw:[0-9][0-9.]*|com.rajatim:zhtw:$(VERSION)|g' README.md README.en.md
	@sed -i '' 's|rev: v[0-9][0-9.]*|rev: v$(VERSION)|g' README.md README.en.md
	@# README files: Rust crate version in TOML snippets.
	@sed -i '' 's|zhtw = "[0-9][0-9.]*"|zhtw = "$(VERSION)"|g' README.md README.en.md
	@# Java SDK benchmark report header
	@sed -i '' 's,| SDK Version | [0-9][0-9.]* |,| SDK Version | $(VERSION) |,' sdk/java/BENCHMARK.md
	@# README: standalone binary download URL (percent-encoded tag)
	@sed -i '' 's|sdk%2Fgo%2Fv[0-9][0-9.]*|sdk%2Fgo%2Fv$(VERSION)|g' README.md README.en.md
	@# SDK READMEs: version strings in install snippets
	@for f in sdk/java/README.md sdk/go/README.md sdk/dotnet/README.md sdk/rust/zhtw/README.md; do \
	  if [ -f "$$f" ]; then \
	    sed -i '' 's|<version>[0-9][0-9.]*</version>|<version>$(VERSION)</version>|g' "$$f"; \
	    sed -i '' 's|com.rajatim:zhtw:[0-9][0-9.]*|com.rajatim:zhtw:$(VERSION)|g' "$$f"; \
	    sed -i '' 's|zhtw = "[0-9][0-9.]*"|zhtw = "$(VERSION)"|g' "$$f"; \
	    sed -i '' 's|sdk%2Fgo%2Fv[0-9][0-9.]*|sdk%2Fgo%2Fv$(VERSION)|g' "$$f"; \
	  fi; \
	done
	@echo "📦 Regenerating sdk/data (embeds version)..."
	$(PYTHON) -m zhtw export --output sdk/data
	@mkdir -p sdk/rust/zhtw/data
	@cp sdk/data/zhtw-data.json sdk/rust/zhtw/data/zhtw-data.json
	@cp sdk/data/zhtw-data.json sdk/go/zhtw/zhtw-data.json
	@echo "🔒 Refreshing Cargo.lock..."
	@cd sdk/rust && cargo check --quiet 2>/dev/null || true
	@$(MAKE) version-check

# === Release ===

release: ## One-command release（閘門+測試+bump+tag+GH Release）: make release VERSION=x.y.z
ifndef VERSION
	$(error VERSION is required. Usage: make release VERSION=4.0.0)
endif
	@bash scripts/release.sh $(VERSION)

release-dry: ## Release 預演（只跑閘門與測試，不做任何變更）: make release-dry VERSION=x.y.z
ifndef VERSION
	$(error VERSION is required. Usage: make release-dry VERSION=4.0.0)
endif
	@DRY_RUN=1 bash scripts/release.sh $(VERSION)

release-verify: ## 發布後驗證（7 workflows + 7 registries + Homebrew）: make release-verify VERSION=x.y.z
ifndef VERSION
	$(error VERSION is required. Usage: make release-verify VERSION=4.0.0)
endif
	@bash scripts/release-verify.sh $(VERSION)

# === Help ===

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
