# Changelog

Alle signifikanten Änderungen am Projekt werden hier dokumentiert.

## 2026-03-03 — Version 0.2.0

Release:

- Zusammenführung der `project_templates` Ergänzungen und Begleit‑Tools in
  `main` (siehe PR #51).
- Enthält: neue `project_templates/common` Vorlagen,
  `scripts/validate_templates.py`, `render_directory` Helfer und Tests.

Details:

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
  - `CHANGELOG`
  - `PLACEHOLDER_SPEC`
- Tooling: `scripts/validate_templates.py` zum lokalen Rendern/Validieren von `project_templates/*`.
- Verbesserter Fallback‑Renderer in `src/template_python_projekt/render.py`.

Hinweise:

- Lokale Prüfungen: `ruff`, `mypy`, `pytest` sollten wie gewohnt ausgeführt werden.

## 2026-03-03 — project_templates: Beispiel‑Templates, Doku & Hilfen

Hinzugefügt:

- `project_templates/cli-basic/` — minimaler MVC‑Skeleton mit `src/` und `main.py`.
- `project_templates/ui-pyside6/` — Platzhalter‑UI‑Template mit `src/`.
- Dokumentationsvorlagen `project_templates/*/docs/*.md.jinja` und einen
  robusten Template‑Renderer in `src/template_python_projekt/render.py`
  (versucht Jinja2, sicheres Fallback wenn nicht verfügbar).
- GitHub‑Vorlagen unter `project_templates/common/.github/`:
  - `ISSUE_TEMPLATE/bug_report.md`
  - `ISSUE_TEMPLATE/feature_request.md`
  - `PULL_REQUEST_TEMPLATE.md`
- Hilfedateien für generierte Projekte:
  - `project_templates/common/commit-instructions.md`
  - `project_templates/common/copilot-instructions.md`
- Tests: `tests/test_template_cli_basic.py` und `tests/test_docs_render.py`.

Hinweis:

Die Änderungen wurden in mehreren Sub‑PRs umgesetzt (u. a. PR #37,
PR #38, PR #39 und PR #40) und als Parent‑PR #41 in `main` gemergt.

Bitte führe nach dem Pull die übliche Überprüfung lokal aus
(Linter, Typecheck, Tests):

```bash
git checkout main && git pull
poetry install --with dev
ruff check .
poetry run mypy src
pytest -q
```
