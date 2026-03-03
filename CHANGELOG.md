# Changelog

Alle signifikanten Änderungen am Projekt werden hier dokumentiert.

## [Unreleased]

### Added (Unreleased)

- Platz für laufende Änderungen bis zum nächsten Release.

### Changed (Unreleased)

-

### Fixed (Unreleased)

-

## [0.2.0] - 2026-03-03

### Added

- Zusammenführung der `project_templates` Ergänzungen und Begleit‑Tools in
  `main` (siehe PR #51).
- Neue `project_templates/common` Vorlagen.
- `scripts/validate_templates.py` zum lokalen Rendern/Validieren von
  `project_templates/*`.
- `render_directory` Helfer und zugehörige Tests.

### Details

- Diverse Template‑Vorlagen:
  - `pyproject.toml`
  - `.pre-commit`
  - `.vscode`
  - `.editorconfig`
  - `.gitignore`
  - `package.json`
  - `markdownlint`
  - `poetry.toml`
  - `README`
  - `PLACEHOLDER_SPEC`
- Verbesserter Fallback‑Renderer in `src/template_python_projekt/render.py`.

### Notes

- Lokale Prüfungen: `ruff`, `mypy`, `pytest` sollten wie gewohnt ausgeführt werden.

### Quick local check

```bash
git checkout main && git pull
poetry install --with dev
ruff check .
poetry run mypy src
pytest -q
```

[Unreleased]: https://github.com/Eichi76/Template-Python-Projekt/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/Eichi76/Template-Python-Projekt/compare/v0.1.0...v0.2.0
