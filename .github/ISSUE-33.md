# Issue 33 — Contribution‑Guide: Wie fügt man neue Templates / Anpassungen hinzu

- **Repo:** Eichi76/Template-Python-Projekt
- **Issue‑Nummer:** 33
- **Titel:** Contribution‑Guide: Wie fügt ich neue Templates / Anpassungen hinzu
- **Author:** Eichi76
- **Assignees:** Eichi76
- **Estimate:** 6h
- **Tags / Dependencies:** feature-project-templates

## Acceptance Criteria
- `CONTRIBUTING.md` definiert Prozess, Tests zum Ausführen, Template‑Metadata‑Schema und eine PR‑Checklist.

## Hinweise
- PRs für diese Änderung sollen gegen den Parent‑Branch `issue/5` geöffnet werden.
- Branch‑Namenskonvention für Sub‑Issues: `issue/5-33-<short>` (Vorschlag: `issue/5-33-contrib-guide`).
- Lokale Checks:
  - `poetry run ruff check .`
  - `poetry run mypy .`
  - `pre-commit run --all-files`
  - `pytest -q --cov=src --cov-report=xml`

## Aktionsliste
- [x] Issue‑Details abrufen (Titel, Body, AC, Estimate, Tags)
- [ ] Worktree prüfen und Branch erstellen
- [ ] Implementierung (erstelle/ändere `CONTRIBUTING.md`, ggf. Templates/Tests)
- [ ] Linting, Typprüfung und Tests ausführen
- [ ] Commits und Pre‑commit Checks
- [ ] Branch pushen und PR erstellen
- [ ] Nach dem Merge aufräumen

## Quelle
Issue‑Daten via MCP: `title`, `body`, `comments`, `assignees`, `author`, `estimate`.
