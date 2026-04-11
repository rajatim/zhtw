# Makefile — zhtw monorepo unified entry point

.PHONY: export test test-python test-java version-check bump release help

PYTHON := uv run python
VERSION ?=

# === Core ===

export: ## Export SDK data (zhtw-data.json + golden-test.json)
	$(PYTHON) -m zhtw export --output sdk/data --verbose
	@mkdir -p sdk/rust/zhtw/data
	@cp sdk/data/zhtw-data.json sdk/rust/zhtw/data/zhtw-data.json
	@echo "  synced crate-local copy → sdk/rust/zhtw/data/zhtw-data.json"
	@cp sdk/data/zhtw-data.json sdk/go/zhtw/zhtw-data.json
	@echo "  synced Go embed copy → sdk/go/zhtw/zhtw-data.json"

test-python: ## Run Python tests
	$(PYTHON) -m pytest tests/ -v

test-java: ## Run Java SDK tests
	cd sdk/java && mvn test --batch-mode

test: test-python test-java ## Run all tests (Python + Java SDK)

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
	@# README files: Maven dep version, Gradle (Kotlin + Groovy), pre-commit rev tag.
	@# Pattern requires the version starts with a digit so we never touch placeholders.
	@sed -i '' 's|<version>[0-9][0-9.]*</version>|<version>$(VERSION)</version>|g' README.md README.en.md
	@sed -i '' 's|com.rajatim:zhtw:[0-9][0-9.]*|com.rajatim:zhtw:$(VERSION)|g' README.md README.en.md
	@sed -i '' 's|rev: v[0-9][0-9.]*|rev: v$(VERSION)|g' README.md README.en.md
	@# README files: Rust crate version in TOML snippets.
	@sed -i '' 's|zhtw = "[0-9][0-9.]*"|zhtw = "$(VERSION)"|g' README.md README.en.md
	@# Java SDK benchmark report header
	@sed -i '' 's,| SDK Version | [0-9][0-9.]* |,| SDK Version | $(VERSION) |,' sdk/java/BENCHMARK.md
	@echo "📦 Regenerating sdk/data (embeds version)..."
	$(PYTHON) -m zhtw export --output sdk/data
	@mkdir -p sdk/rust/zhtw/data
	@cp sdk/data/zhtw-data.json sdk/rust/zhtw/data/zhtw-data.json
	@cp sdk/data/zhtw-data.json sdk/go/zhtw/zhtw-data.json
	@$(MAKE) version-check

# === Release ===

release: ## One-command release: make release VERSION=x.y.z
ifndef VERSION
	$(error VERSION is required. Usage: make release VERSION=4.0.0)
endif
	@echo "🔍 Validating..."
	$(PYTHON) -m pytest tests/ -q
	@if git tag -l "v$(VERSION)" | grep -q "v$(VERSION)"; then \
		echo "❌ Tag v$(VERSION) already exists"; exit 1; \
	fi
	@$(MAKE) bump VERSION=$(VERSION)
	@echo "📋 Commit, tag, and push..."
	git add -A
	git commit -m "chore: release v$(VERSION)"
	git tag -a "v$(VERSION)" -m "v$(VERSION)"
	git tag -a "sdk/go/v$(VERSION)" -m "sdk/go v$(VERSION)"
	git push && git push origin "v$(VERSION)" "sdk/go/v$(VERSION)"
	gh release create "v$(VERSION)" --title "v$(VERSION)" --generate-notes
	@echo "✅ Released v$(VERSION)"

# === Help ===

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
