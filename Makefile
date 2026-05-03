.PHONY: check check-unix check-windows

check: check-unix

check-unix:
	@echo "Running make check (Unix shell)"
	poetry env check
	poetry run pytest -q
	pre-commit run --all-files
	@if [ -f package.json ]; then \
		echo "Found package.json — running npm run lint:md"; \
		npm run lint:md || true; \
	else \
		echo "No package.json found — skipping npm lint"; \
	fi

check-windows:
	@echo "Running make check (PowerShell)"
	powershell -NoProfile -ExecutionPolicy Bypass -File ./scripts/check.ps1
