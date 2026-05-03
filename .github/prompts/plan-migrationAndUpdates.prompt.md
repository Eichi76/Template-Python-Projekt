## Plan: Migration & Updates (Issue #36)

TL;DR - Erstelle eine Dokumentationsseite mit einer sicheren Update-/Migrations‑Checkliste, Beispiele für Migrationen in Templates, und ergänze den Renderer um eine nicht-interaktive "Update Existing"-Strategie plus Tests. Umsetzung erfolgt in einem Sub-Branch von `issue/5` namens `issue/5-36-migration`.

**Steps**
1. Discovery (bereits durchgeführt): Zusammenstellung relevanter Dateien, Lücken: Docs, Renderer, Templates, Tests.
2. Branch: Erstelle lokalen Branch `issue/5-36-migration` von `issue/5`. (*blocks: none*)
3. Documentation: Neue Seite `docs/migration_and_updates.md` anlegen mit:
   - Einleitung, Risiken, Backup-Hinweis
   - Schritt-für-Schritt Checkliste (Backup, Abhängigkeiten prüfen, Tests laufen lassen, Änderungen anwenden, Konflikt-Handling)
   - Konkrete Beispiele: Update `pyproject.toml`, Merge-Muster für `README.md` und `src`-Änderungen
   - Troubleshooting-Abschnitt
   (Depends on step 2)
4. Templates: Ergänze `project_templates/common/` und `project_templates/cli-basic/` um Beispiel-Abschnitte oder `migration_examples/`-Vorlagen für typische Update‑Szenarien (z. B. `pyproject.toml`-Änderung). (Parallel mit 3)
5. CLI/Renderer: Implementiere eine nicht-interaktive Update-Strategie in [src/template_python_projekt/render.py](src/template_python_projekt/render.py):
   - Neue Option/Parameter `update_mode` mit Strategien: `skip`, `overwrite`, `backup` (default `backup`)
   - Beim Rendern bestehender Dateien: erst in Temp schreiben, dann je nach Strategie handeln (backup vorhandener Datei `.bak.TIMESTAMP`, oder skip)
   - Exponiere Option in [src/template_python_projekt/main.py](src/template_python_projekt/main.py) CLI, dokumentiere Usage in `docs/migration_and_updates.md`.
   (Depends on step 2)
6. Tests: Füge Tests hinzu:
   - `tests/test_migration_docs.py` — Validiert Inhalte/Links der neuen Doc-Seite
   - `tests/test_render_update_mode.py` — Unit-Tests für `render.py` Update-Strategien (simulate existing file, assert backup/overwrite/skip behavior)
   (Depends on step 5)
7. Lint & Typecheck: Vor jedem Commit `poetry run ruff check .` und `poetry run mypy .` ausführen; Warnungen beheben.
8. Pre-commit: Achte auf pre-commit-Hooks; falls sie Fehler/Warnungen melden, beheben bevor push.
9. Commit & Push: Committe lokal in logischen Einzelschritten (Docs, Templates, Renderer, Tests). Push branch `issue/5-36-migration`.
10. PR: Erstelle nach Abschluss einen Pull Request (kein Draft). PR-Name auf Deutsch (z. B. "Migration: Migrations‑Leitfaden und sichere Update‑Strategie"), ausführliche Beschreibung (Summary, was geändert wurde, How to test, Test-Commands, Merge-Strategie: squash). Keine weiteren Reviewer nötig. (Depends on step 9)
11. Merge: Nach QA per `squash-merge` in `issue/5` oder `main` wie vereinbart.

**Relevant files**
- [docs/manual_initialization.md](docs/manual_initialization.md) — Referenz: bestehende Init-Anweisungen
- [docs/quickstart.md](docs/quickstart.md) — Referenz für Examples
- [docs/troubleshooting.md](docs/troubleshooting.md) — erweitern mit Migration-Troubles
- [src/template_python_projekt/render.py](src/template_python_projekt/render.py) — Renderer-Änderung (Update-Strategie)
- [src/template_python_projekt/main.py](src/template_python_projekt/main.py) — CLI-Flag
- [project_templates/common/pyproject.toml.jinja](project_templates/common/pyproject.toml.jinja) — Beispiel-Migration
- [project_templates/cli-basic/docs/README.md.jinja](project_templates/cli-basic/docs/README.md.jinja) — Beispiel-Docs

**Verification**
1. Dokumentation: `poetry run pytest -q tests/test_migration_docs.py` (neue Tests grün)
2. Renderer behavior: `poetry run pytest -q tests/test_render_update_mode.py` (backup/overwrite/skip verified)
3. Lint & Typecheck: `poetry run ruff check .` → 0 Issues; `poetry run mypy .` → 0 Errors
4. Full test-suite: `poetry run pytest -q` passes

**Decisions / Annahmen**
- CLI-Update-Strategie ist nicht interaktiv (keine Prompts), da CI/automatisierte Runs benötigt werden.
- Backup statt überschreiben als default, um Sicherheit zu maximieren.
- Branch-Name: `issue/5-36-migration` (Sub-Issue 36)
- Pull Request: Deutsche Titel & ausführliche Beschreibung, Merge per `squash`.

**Further Considerations**
1. Möchtest du die Update-Strategie als dominante CLI-Option (`--update`/`--no-update`) oder als Konfig in `pyproject.toml`? Empfehlung: CLI-Flag + Dokumentation.
2. Soll ein opt-in Auto-merge-Tool für einfache textuelle Dateien (README/pyproject) implementiert werden? Option B: nur Backup + manuelles Merge.

*Geschätzter Aufwand*: ca. 6h (wie im Issue angegeben) — aufgeteilt: Docs 2h, Renderer 2.5h, Tests 1h, Integration 0.5h.
