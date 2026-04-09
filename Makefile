# Makefile — zhtw monorepo unified entry point

.PHONY: export test test-python test-java release help

PYTHON := uv run python
VERSION ?=

# === Core ===

export: ## Export SDK data (zhtw-data.json + golden-test.json)
	$(PYTHON) -m zhtw export --output sdk/data --verbose

test-python: ## Run Python tests
	$(PYTHON) -m pytest tests/ -v

test-java: ## Run Java SDK tests
	cd sdk/java && mvn test --batch-mode

test: test-python test-java ## Run all tests (Python + Java SDK)

# === Release ===

release: ## One-command release: make release VERSION=x.y.z
ifndef VERSION
	$(error VERSION is required. Usage: make release VERSION=3.4.0)
endif
	@echo "🔍 Validating..."
	$(PYTHON) -m pytest tests/ -q
	@if git tag -l "v$(VERSION)" | grep -q "v$(VERSION)"; then \
		echo "❌ Tag v$(VERSION) already exists"; exit 1; \
	fi
	@echo "📝 Updating version to $(VERSION)..."
	@sed -i '' 's/^version = .*/version = "$(VERSION)"/' pyproject.toml
	@sed -i '' 's/^__version__ = .*/__version__ = "$(VERSION)"/' src/zhtw/__init__.py
	@sed -i '' 's/<version>.*<\/version>/<version>$(VERSION)<\/version>/' sdk/java/pom.xml
	@sed -i '' 's/"version": ".*"/"version": "$(VERSION)"/' sdk/typescript/package.json
	@sed -i '' 's/^version = .*/version = "$(VERSION)"/' sdk/rust/Cargo.toml
	@sed -i '' 's/<Version>.*<\/Version>/<Version>$(VERSION)<\/Version>/' sdk/dotnet/Zhtw.csproj
	@echo "📦 Exporting SDK data..."
	$(PYTHON) -m zhtw export --output sdk/data --verbose
	@echo "📋 Commit, tag, and push..."
	git add -A
	git commit -m "chore: release v$(VERSION)"
	git tag -a "v$(VERSION)" -m "v$(VERSION)"
	git push && git push origin "v$(VERSION)"
	gh release create "v$(VERSION)" --title "v$(VERSION)" --generate-notes
	@echo "✅ Released v$(VERSION)"

# === Help ===

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
