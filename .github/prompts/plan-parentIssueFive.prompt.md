## Plan: Parent Issue #5 umsetzen

TL;DR - Ziel: Parent Issue #5 durch sequenzielle Abarbeitung der Sub‑Issues #29–#36 umsetzen. Ansatz: Für jedes Sub‑Issue lokal einen Branch `issue/5-<num>-<short>` anlegen, Änderungen vollständig abschließen, Lint/Typecheck/Tests grün bekommen, erst dann einen PR gegen `issue/5` eröffnen und nach Abschluss mergen. Reihenfolge: 29 → 30 → 31 → 32 → 33 → 34 → 35 → 36.

**Steps**
1. Basis: erstelle lokalen Parent‑Branch `issue/5` von `main`.
2. Für jedes Sub‑Issue (in Reihenfolge) führe die folgenden Schritte sequenziell aus:
   - a) Branch anlegen: `git checkout -b issue/5-<num>-<short>` (erst unmittelbar bevor du mit dem Sub‑Issue beginnst).
   - b) Implementieren: Änderungen in relevanten Dateien vornehmen.
   - c) Lokale Checks: `poetry run ruff check .`, `poetry run mypy .`, `pytest -q`.
   - d) Pre‑commit: `git add` + `git commit` — falls pre‑commit fehlschlägt, alle Linter/Formatter Probleme beheben und erneut committen.
   - e) Push: `git push -u origin issue/5-<num>-<short>`.
   - f) PR öffnen (mit `gh pr create` oder über Web): Ziel-Branch `issue/5`. Kein Draft‑PR; erst öffnen wenn Sub‑Issue komplett.
   - g) PR Titel (Deutsch) und ausführliche Beschreibung (siehe PR‑Template unten).
   - h) Merge nach erfolgreichem Durchlaufen der CI und Tests: `Squash and merge` empfohlen, Merge in `issue/5`.
   - i) Lokaler `git checkout issue/5` → `git pull` um den gemergten Stand zu aktualisieren.
3. Nach Abschluss aller Sub‑Issues: finaler PR von `issue/5` → `main` erstellen, Tests/Linting ausführen, in `main` mergen.

**Branch‑Namensschema**
- Parent: `issue/5`
- Sub‑Issues: `issue/5-29-quickstart`, `issue/5-30-cli-docs`, `issue/5-31-manual-init`, `issue/5-32-troubleshooting`, `issue/5-33-contributing`, `issue/5-34-examples-docs`, `issue/5-35-postinit-check`, `issue/5-36-migration-updates`.

**PR Titel & Beschreibung (Vorlage)**
- PR Titel (Deutsch): „ISSUE #<num>: <kurzer deutscher Titel>"
- PR Beschreibung (ausführlich):
  - Kurzbeschreibung: Was wurde geändert und warum.
  - Dateien: Liste der geänderten kritischen Dateien.
  - Checkliste:
    - [ ] Lokale Linting: `poetry run ruff check .` erfolgreich
    - [ ] Typechecking: `poetry run mypy .` erfolgreich
    - [ ] Tests: `pytest -q` alle grünen
    - [ ] Pre‑commit Hooks laufen durch
    - [ ] Änderungen dokumentiert (Docs/README oder gezielte MD)
  - Testing‑Anleitung (Kurz): Befehle zum lokalen Verifizieren.
  - Merge‑Hinweis: `Squash and merge` in `issue/5` nach CI‑Grün, kein Reviewer erforderlich (single‑person team).

**Verifikation (je Sub‑Issue)**
- Lint: `poetry run ruff check .`
- Typecheck: `poetry run mypy .`
- Tests: `pytest -q --maxfail=1`
- Pre‑commit lokal: `pre-commit run --all-files` (wenn installiert)
- CI: `.github/workflows/ci.yml` sollte nach Änderung erfolgreich durchlaufen.

**Relevante Dateien (überblicksweise, referenziert in Issue‑Analyse)**
- [src/template_python_projekt/main.py](src/template_python_projekt/main.py)
- [src/template_python_projekt/render.py](src/template_python_projekt/render.py)
- [src/template_python_projekt/node_env.py](src/template_python_projekt/node_env.py)
- [src/template_python_projekt/poetry_env.py](src/template_python_projekt/poetry_env.py)
- [scripts/validate_templates.py](scripts/validate_templates.py)
- [docs/README.md](docs/README.md)
- [project_templates/cli-basic](project_templates/cli-basic)
- [project_templates/ui-pyside6](project_templates/ui-pyside6)
- Tests: [tests/test_template_cli_basic.py](tests/test_template_cli_basic.py), [tests/test_validate_templates.py](tests/test_validate_templates.py), [tests/test_pyproject_merge.py](tests/test_pyproject_merge.py)

**Detaillierte TODOs pro Sub‑Issue (sequenziell ausführbar)**

1) Sub‑Issue #29 — Quickstart: Von Scratch zum 'ready to use' Projekt
- Ziel: konkreten Quickstart‑Guide erstellen und Beispielbefehle hinzufügen.
- Schritte:
  - Branch: `issue/5-29-quickstart` anlegen.
  - Dateiänderungen: ergänze oder erstelle [docs/quickstart.md](docs/quickstart.md) (neue Datei) mit folgenden Abschnitten: Voraussetzungen, System‑Setup (poetry, node), `python -m pip install -e .`, Beispiel: `python -m template_python_projekt --template cli-basic --name demo` und erwartete Ausgabe/Ordnerstruktur.
  - Ergänze kurze Verifizierung: Befehl, um Demo zu starten und Tests lokal laufen zu lassen.
  - Lint/Test, Commit, Push, PR gegen `issue/5`, Merge.

2) Sub‑Issue #30 — Detaillierte Anleitung: Nutzung des Starterskripts
- Ziel: vollständige CLI‑Dokumentation.
- Schritte:
  - Branch: `issue/5-30-cli-docs`.
  - Update [src/template_python_projekt/main.py] wenn Flags unvollständig dokumentiert sind (nur, falls nötig), ansonsten dokumentiere Flags in [docs/cli_spec.md] oder erweitere [docs/README.md].
  - Füge Beispiel‑Usecases (z. B. `--template`, `--name`, `--force`, `--dry-run`) und erwartete Outcomes hinzu.
  - Automatischer Test: erweitere oder verlinke `tests/test_template_cli_basic.py` mit minimaler CLI smoke test falls hilfreich.
  - Lint/Test, Commit, Push, PR → Merge.

3) Sub‑Issue #31 — Manuelle Initialisierung: Schritte ohne Starterskript
- Ziel: Dokumentierte manuelle Schritte, die das Starter‑Skript reproduzieren.
- Schritte:
  - Branch: `issue/5-31-manual-init`.
  - Dokument: `docs/manual_init.md` mit konkreten Kopiervorgängen, Merge‑Hinweisen (pyproject), und den wichtigsten Template‑Platzhaltern.
  - Referenziere / verlinke `src/template_python_projekt/render.py` und `project_templates/common/pyproject.toml.jinja`.
  - Ergänze Falls nötig Tests zu `test_pyproject_merge.py` mit einem zusätzlichen realistischen Merge‑Case.
  - Lint/Test, Commit, Push, PR → Merge.

4) Sub‑Issue #32 — Troubleshooting & FAQ
- Ziel: FAQ mit Top‑10 Fehlern + fixes.
- Schritte:
  - Branch: `issue/5-32-troubleshooting`.
  - Update [docs/README.md] oder neue `docs/faq.md` mit Abschnitten: `poetry missing`, `node missing`, `pre-commit fails`, `merge conflicts`, `permission errors`.
  - Ergänze Code‑Snippets/Commands zum Beheben (z. B. `python -m pip install -e .`, `poetry install --with dev`, `pre-commit run --all-files`).
  - Verlinke zu [src/template_python_projekt/node_env.py] und [src/template_python_projekt/poetry_env.py].
  - Lint/Test, Commit, Push, PR → Merge.

5) Sub‑Issue #33 — Contribution‑Guide
- Ziel: `CONTRIBUTING.md` erstellen.
- Schritte:
  - Branch: `issue/5-33-contributing`.
  - Erstelle `CONTRIBUTING.md` mit: Branch‑Naming, Commit‑Konvention, Test­anleitung, CI‑Checks, PR‑Checklist (siehe PR Vorlage oben), How‑to add templates (schema), und Pfade zu `project_templates/common/README.md.jinja`.
  - Lint/Test, Commit, Push, PR → Merge.

6) Sub‑Issue #34 — Beispielprojekte Dokumentation (CLI & PySide6)
- Ziel: READMEs für `project_templates/cli-basic` und `project_templates/ui-pyside6`.
- Schritte:
  - Branch: `issue/5-34-examples-docs`.
  - In `project_templates/cli-basic/docs/README.md.jinja` und `project_templates/ui-pyside6/docs/README.md.jinja` konkrete Run/Debug/Test/Packaging Schritte ergänzen.
  - Für UI: Hinweise zu Headless/CI (oder markiere Demo als manuell).
  - Lint/Test, Commit, Push, PR → Merge.

7) Sub‑Issue #35 — Post‑Init Validierung: Checkliste & Automatische Prüfungen
- Ziel: `scripts/check.sh` oder `Makefile` Target `check` erstellen, das folgende ausführt: `poetry install --with dev` (optional), `poetry run ruff check .`, `poetry run mypy .`, `pytest -q`, `pre-commit run --all-files`.
- Schritte:
  - Branch: `issue/5-35-postinit-check`.
  - Erstelle `Makefile` oder `scripts/check.sh` (preferiere `scripts/check.sh` für Windows-kompatible PowerShell: `scripts/check.ps1` + `scripts/check.sh` für *nix). Implementiere und dokumentiere Verwendung.
  - Ergänze `scripts/validate_templates.py` bzw. erweitere Tests in `tests/test_validate_templates.py` falls nötig.
  - Lint/Test, Commit, Push, PR → Merge.

8) Sub‑Issue #36 — Migration & Updates: Beste Praxis
- Ziel: Migrations‑Guide und Beispiele für sichere Updates.
- Schritte:
  - Branch: `issue/5-36-migration-updates`.
  - Dokument: `docs/migration.md` mit Schritt‑für‑Schritt, Beispiel‑pyproject Merge‑Flows, Hinweise zu `render.py` Merge‑Funktionen und Testcases.
  - Ergänze Tests in `tests/test_pyproject_merge.py` für zusätzliche Fälle.
  - Lint/Test, Commit, Push, PR → Merge.

**Verification (End to End) nach allen Sub‑Issues**
- Lokale: `poetry run ruff check .`, `poetry run mypy .`, `pytest -q` erfolgreich.
- CI: `.github/workflows/ci.yml` grünes Ergebnis.
- Dokumentation: `docs/README.md` enthält Links zu neuen `docs/*.md` Dateien.
- Optional: ein CI Smoke job, der `python -m template_python_projekt --template cli-basic --name demo --target /tmp/demo` ausführt und anschließend die `scripts/check` aufruft.

**Decisions / Annahmen**
- PRs werden in `issue/5` gemerged, nicht direkt in `main`.
- Merge‑Strategie: `Squash and merge` empfohlen für Sub‑Issue PRs.
- Einzelperson Team → keine Reviewer nötig; PRs sollten dennoch die Checkliste enthalten.
- Branches werden nur dann erstellt, wenn das Sub‑Issue aktuell bearbeitet wird.

**Further Considerations**
1. Möchtest du, dass ich die ersten Dateien (z. B. `docs/quickstart.md`, `CONTRIBUTING.md`, `scripts/check.ps1`) als Draft erstelle? Option A: Ja, erstelle die Dateien. Option B: Nein, nur Plan und then du implementierst.
2. Soll ich zusätzlich CI‑Job‑Vorlage für Quickstart Smoke Test anlegen (separater PR nach #29/#35)?
