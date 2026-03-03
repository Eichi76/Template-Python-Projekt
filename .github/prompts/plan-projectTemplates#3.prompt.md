## Plan: Issue #3 umsetzen

TL;DR — Was, wie, warum
Implementiere Parent Issue #3 durch sequentielle Abarbeitung der Sub‑Issues #10–#18. Für jedes Sub‑Issue wird ein eigener Branch `issue/3-<num>-<slug>` erstellt, lokal implementiert, mit `ruff`/`mypy`/`pytest` geprüft, gepusht und per PR (Ziel: `issue/3`) gemerged. Am Ende wird `issue/3` in `main` gemerged. Entscheidungen (festgelegt): volle Jinja2‑Syntax erlaubt; pre-commit hooks: `ruff, isort, mypy` (kein Black); `render_directory` helper in `src/template_python_projekt/render.py` hinzufügen; `scripts/validate_templates.py` nur für lokale/manual Ausführung (CI führt nur statische Prüfungen).

**Steps**
1. Parent‑Branch anlegen: `git checkout main && git pull` → `git checkout -b issue/3` → `git push -u origin issue/3`.
2. Für jedes Sub‑Issue (10→18) sequenziell:
   - `git checkout issue/3 && git checkout -b issue/3-<num>-<slug>`
   - Implementieren (siehe Per‑Issue TODOs). Committe erst wenn `poetry run ruff check .` und `poetry run mypy .` lokal grün sind; `pre-commit` Fehler fixen, nicht umgehen.
   - `git push -u origin issue/3-<num>-<slug>`
   - Öffne PR: Ziel `issue/3`. Deutscher PR‑Titel + ausführliche Beschreibung (Template weiter unten). Kein Reviewer nötig. Nach Erfolg merge in `issue/3` (Squash empfohlen).
3. Nach allen Sub‑Merges: PR `issue/3` → `main` (deutscher Titel + Release/Upgrade‑Hinweisen), merge.

**Verification (lokal vor Push)**
- Lint & Types: `poetry run ruff check .` ; `poetry run mypy .`
- Tests: `pytest -q` (oder gezielte Tests)
- Pre‑commit (bei Bedarf): `pre-commit run --all-files`
- Template render smoke: benutze `src/template_python_projekt/render.py` `render_template_file` / `render_directory` und prüfe, dass keine `{{` übrig bleiben.

**Per‑Sub‑Issue TODOs (konkret, sequenziell)**

- Sub‑Issue 10 — Branch: `issue/3-10-pyproject-template`
  - Dateien anlegen: `project_templates/common/pyproject.toml.jinja` (Placeholders: `{{ project_name }}`, `{{ author }}`, `{{ license }}`, kommentierte `[tool.*]`‑Abschnitte).
  - Docs: Update `project_templates/common/README.md` (Erklärung der Platzhalter, Hinweis `poetry check`).
  - Test: `tests/test_pyproject_template.py` — rendert Template, `tomllib` parse, assert keine `{{`.
  - PR‑Titel: Vorlage: pyproject.toml mit Dependencies & Linter‑Einstellungen
  - PR‑Beschreibung (Abschnitte): Zusammenfassung; Änderungen (Dateiliste); Tests; Testanweisungen; Offene Fragen.
  - Komplexität: Medium

- Sub‑Issue 11 — Branch: `issue/3-11-pre-commit-template`
  - Dateien: `project_templates/common/.pre-commit-config.yaml.jinja` mit Hooks `ruff`, `isort`, `mypy` (versions/args als Platzhalter).
  - Docs: Update `project_templates/common/commit-instructions.md`.
  - Test: `tests/test_precommit_template.py` — render & YAML‑Syntax prüfen. (kein automatischer `pre-commit run` in CI)
  - PR‑Titel: Vorlage: .pre-commit-config.yaml und empfohlene Hooks
  - Komplexität: Medium

- Sub‑Issue 12 — Branch: `issue/3-12-vscode-templates`
  - Dateien: `project_templates/common/.vscode/settings.json.jinja`, `launch.json.jinja`, `tasks.json.jinja` (Tasks für `ruff check`, `pytest`).
  - Docs: Hinweise in common README.
  - PR‑Titel: Vorlage: .vscode (launch, settings, tasks)
  - Komplexität: Low‑Medium

- Sub‑Issue 13 — Branch: `issue/3-13-editorconfig-gitignore`
  - Dateien: `project_templates/common/.editorconfig.jinja` (`indent_size = 4`, `max_line_length = 100`), `project_templates/common/.gitignore.jinja` (Python defaults).
  - Test: `tests/test_editorconfig_gitignore.py` — render & existenz/syntax.
  - PR‑Titel: Vorlage: .editorconfig und .gitignore
  - Komplexität: Low

- Sub‑Issue 14 — Branch: `issue/3-14-package-markdownlint`
  - Dateien: `project_templates/common/package.json.jinja` (Script `"lint:md": "markdownlint -c .markdownlint.json \"**/*.md\""`), `project_templates/common/.markdownlint.json.jinja`. Verwende `npm`.
  - Docs: README Hinweis zu `npm install` & `npm run lint:md`.
  - Test: `tests/test_markdownlint_template.py` — render & Syntax (JSON).
  - PR‑Titel: Vorlage: package.json & Markdownlint Setup
  - Komplexität: Medium

- Sub‑Issue 15 — Branch: `issue/3-15-readme-changelog`
  - Dateien: `project_templates/common/README.md.jinja` (Sections: Install, Usage, Contributing, License), `project_templates/common/CHANGELOG.md.jinja`.
  - Test: `tests/test_readme_render.py` — rendert und prüft Sektionen.
  - PR‑Titel: Vorlage: README.md und CHANGELOG.md mit Platzhaltern
  - Komplexität: Low‑Medium

- Sub‑Issue 16 — Branch: `issue/3-16-poetry-config`
  - Dateien: `project_templates/common/poetry.toml.jinja` (Placeholders, z. B. `virtualenvs.in-project`).
  - Test: `tests/test_poetry_config_template.py` — render & prüfe erwartete keys.
  - PR‑Titel: Vorlage: poetry.toml / Poetry‑Konfiguration
  - Komplexität: Low

- Sub‑Issue 17 — Branch: `issue/3-17-placeholder-spec`
  - Datei: `project_templates/common/PLACEHOLDER_SPEC.md` — dokumentiert volle Jinja2‑Syntax (Variables, Defaults, Filters), Escaping‑Regeln und Hinweise für TOML/JSON/MD.
  - Code‑Docs: Update `src/template_python_projekt/render.py` mit Verweis auf Spec. Implementiere dort zusätzlich den `render_directory` helper (`render_directory(template_dir, target_dir, context)`), wiederverwendbar von #18.
  - Test: `tests/test_placeholder_spec.py` — rendert Beispiele (TOML/JSON/MD) und assert no unresolved placeholders.
  - PR‑Titel: Konvention: Platzhalter‑Format & Ersetzungsregeln definieren
  - Komplexität: Medium

- Sub‑Issue 18 — Branch: `issue/3-18-validate-templates`
  - Script: `scripts/validate_templates.py` — CLI: rendert Template‑Verzeichnis mit `render_directory`, führt best‑effort checks: parse TOML, `pre-commit run --all-files` (falls `.pre-commit-config.yaml` vorhanden), `npm run lint:md` (falls `package.json` vorhanden), optional `python -m pip install -e .` fallback (nur lokal/manual). Script dokumentiert, dass CI nur statische Prüfungen macht.
  - Tests: `tests/test_validate_templates_smoke.py` — markiert `@pytest.mark.manual` / skip in CI.
  - PR‑Titel: Validierungsskript: Templates gegen Beispielprojekt prüfen
  - Komplexität: Medium‑High

**Dateien / Symbole, die angepasst/neu sind**
- Renderer: `src/template_python_projekt/render.py` — neue Funktion `render_directory(template_dir, target_dir, context)`; `render_template_file` beibehalten und dokumentiert.
- Neue Templates: `project_templates/common/*.jinja` (siehe Per‑Issue Liste).
- Tests: neue `tests/test_*.py` wie oben gelistet.
- Script: `scripts/validate_templates.py`.

**PR‑Eröffnungs‑Template (für jede Sub‑PR, deutsch)**
- Zusammenfassung: Ein Satz, was das PR liefert.
- Änderungen: Dateiliste mit kurzer Beschreibung.
- Tests: Hinzugefügte/aktualisierte Tests + wie lokal auszuführen (`poetry run pytest tests/test_... -q`).
- Lokale Test‑Schritte: 1) `git checkout issue/3-...` 2) `poetry install --with dev` 3) `poetry run ruff check .` 4) `poetry run mypy .` 5) `pytest -q` 6) Template render smoke: Verwende `from template_python_projekt.render import render_template_file; ...`.
- Offene Fragen/Risiken: listet verbleibende Entscheidungen (falls vorhanden).
- Hinweis: PR richtet sich an `issue/3`.

**Globale Notes / CI**
- CI führt nur statische Prüfungen: `ruff`, `mypy`, `pytest` (unit tests). Integrationstests / `scripts/validate_templates.py` heavy checks sind lokal/manual (markiert).
- Halte Commits klein & atomic; behandle pre-commit‑Fehler durch Fixes.
- Branch‑Naming-Konvention wie oben.

**Entscheidungen (zusammengefasst)**
- Platzhalter: Volle Jinja2‑Syntax (Expressions/Filters/Defaults).
- Pre‑commit Hooks: `ruff`, `isort`, `mypy` (kein Black).
- Node PM: `npm`.
- README DoD: Sections Install, Usage, Contributing, License.
- `render_directory` helper wird in `src/template_python_projekt/render.py` implementiert.
- `scripts/validate_templates.py` wird lokal/manual; Tests markiert, CI führt nur statische checks.

---

Status: TODO‑Liste angelegt; Planfile `untitled:plan-projectTemplates.prompt.md` erstellt mit vollständigem Plan.

Nächster Schritt: Soll ich jetzt mit Sub‑Issue #10 beginnen und die erste Branch/Datei‑Stubs erstellen? (Ich kann den Branch‑Befehl ausgeben und die Dateien in einem Commit vorbereiten.)
