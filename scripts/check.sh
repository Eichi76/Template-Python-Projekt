#!/usr/bin/env bash
set -euo pipefail

echo "Running check script (Unix shell)..."

poetry env check
poetry run pytest -q
pre-commit run --all-files

if [ -f package.json ]; then
  echo "Found package.json — running npm run lint:md"
  npm run lint:md || true
else
  echo "No package.json found — skipping npm lint"
fi
