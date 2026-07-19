# Makefile — zhtw monorepo unified entry point

.PHONY: export export-check precision-benchmark benchmark-validate accuracy-annotation-status accuracy-blind-review-packet accuracy-gemini-advisory accuracy-promotion-gate accuracy-promote-backlog accuracy-holdout-annotation-packet accuracy-holdout-gemini-advisory accuracy-benchmark test test-all test-python test-java test-typescript test-rust test-go test-dotnet test-corpus-prepare release-gate version-check bump release help

PYTHON := uv run python
VERSION ?=
BATCH ?= it-api-cli
DATE ?= $(shell date +%F)
ID_FROM ?=
ID_TO ?=
COMPETITORS ?= zhtw
REVIEWER_STAGE ?= first_human_review
HOLDOUT_BATCH ?=

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
