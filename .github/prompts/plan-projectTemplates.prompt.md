TL;DR — Plan zur Umsetzung von Parent Issue #2 (project_templates) durch Erledigung der Sub‑Issues #6, #7, #8, #9

Ziel
- Parent Issue #2 wird durch Implementierung und Merge der Sub‑Issues #6, #7, #8 und #9 abgeschlossen.
- Branch‑Schema: Parent `issue/2`; Sub‑Branches `issue/2-<N>-<short>`.
- PR‑Workflow: Sub‑PRs → Base `issue/2`; Parent‑PR → Base `main`.
- Linting/Typing: `poetry run ruff check .` & `poetry run mypy .` — Fehler müssen behoben werden.

Issue‑Zusammenfassung
- Parent #2: „project_templates‑Verzeichnis erstellen und konfigurieren" — Acceptance: mind. zwei Templates `cli-basic/` und `ui-pyside6/`, jeweils `metadata.yml`, plus `project_templates/README.md`.
- Sub #6: „src/ Verzeichnis mit MVC‑Skelett erstellen" — Acceptance: jedes Template `src/{model,view,controller,__init__.py}` + runnable `main.py`.
- Sub #7: „docs/ Template‑System für technische Dokumentation erstellen" — Acceptance: `project_templates/*/docs/` mit Markdown + Jinja2 templates, README erklärt Rendering.
- Sub #8: „Templates für Issues und Pull Requests im project_templates vorbereiten" — Acceptance: `project_templates/common/.github/ISSUE_TEMPLATE/` + `PULL_REQUEST_TEMPLATE.md`.
- Sub #9: „commit-instructions.md und copilot-instructions.md im project_templates erstellen" — Acceptance: beide Dateien mit Beispielen und Linter‑Hinweisen.

Vorbedingungen (lokal)
- `gh` konfiguriert, `git` aktuell, `poetry` aktiv (virt. env).
- Arbeitskopie: `git checkout main` ; `git pull origin main`.

Branching & PRs
1) Parent‑Branch anlegen
```bash
git checkout main
git pull origin main
git checkout -b issue/2
git push -u origin issue/2
```

2) Sub‑Branches (je Sub‑Issue)
Benennung & Beispiele:
- #6: `issue/2-6-mvc-skeleton`
- #7: `issue/2-7-docs-templates`
- #8: `issue/2-8-gh-templates`
- #9: `issue/2-9-commit-copilot`

Beispiel erstellen (Sub #6):
```bash
git checkout issue/2
git checkout -b issue/2-6-mvc-skeleton
```
Commit & Push nach Implementierung:
```bash
git add .
git commit -m "feat(issue/2-6): MVC skeleton for templates"
git push -u origin issue/2-6-mvc-skeleton
```

3) PRs erstellen (Base = `issue/2`)
Beispiel:
```bash
gh pr create --title "Sub‑Issue #6: MVC skeleton for templates" \
  --body "Implements project_templates/*/src MVC skeleton.\n\nRefs: #6\n\nChecklist:\n- Tests added\n- Lint & mypy green\n- README updated" \
  --head issue/2-6-mvc-skeleton --base issue/2
```
Merge nach Review:
```bash
gh pr merge <PR-NUM> --merge
```

4) Parent‑PR → `main` (nachmerge aller Sub‑PRs in `issue/2`)
```bash
git checkout issue/2
git pull origin issue/2
poetry run ruff check .
poetry run mypy .
poetry run pytest -q --cov=src --cov-report=xml
gh pr create --title "Issue #2: project_templates directory and templates" \
  --body "Includes: #6, #7, #8, #9\n\nSummary of changes and acceptance tests." \
  --head issue/2 --base main
gh pr merge <PARENT-PR> --merge
gh issue close 2 --repo Eichi76/Template-Python-Projekt
```

Konkrete Aufgaben pro Sub‑Issue

Sub #6 (`issue/2-6-mvc-skeleton`)
- Dateien anlegen:
  - `project_templates/cli-basic/src/model/__init__.py`
  - `project_templates/cli-basic/src/view/__init__.py`
  - `project_templates/cli-basic/src/controller/__init__.py`
  - `project_templates/cli-basic/src/main.py` — einfache CLI (`argparse`/`typer`) mit `--help`.
  - gleiche minimalen placeholders für `project_templates/ui-pyside6/...`.
- Tests:
  - `tests/test_template_cli_basic.py` — importierbarkeit und `--help` check.
- Acceptance (lokal):
  ```bash
  python project_templates/cli-basic/src/main.py --help
  pytest tests/test_template_cli_basic.py -q
  ```

Sub #7 (`issue/2-7-docs-templates`)
- Dateien anlegen:
  - `project_templates/cli-basic/docs/index.md.jinja`
  - `project_templates/cli-basic/docs/README.md` — erklärt Variablen + Render‑Schritte
  - optional: `src/template_python_projekt/render.py` (kleines Rendering‑Tool) — verwendet `jinja2`.
- Tests:
  - `tests/test_docs_render.py` — rendert Beispiel via `jinja2.Environment`.
- Acceptance:
  ```bash
  python -c "import jinja2; print('ok')"
  pytest -q tests/test_docs_render.py
  ```

Sub #8 (`issue/2-8-gh-templates`)
- Dateien anlegen:
  - `project_templates/common/.github/ISSUE_TEMPLATE/bug.md`
  - `project_templates/common/.github/ISSUE_TEMPLATE/feature_request.md`
  - `project_templates/common/PULL_REQUEST_TEMPLATE.md`
- Tests:
  - `tests/test_templates_exist.py` — existence checks.
- Acceptance:
  ```bash
  cat project_templates/common/.github/ISSUE_TEMPLATE/bug.md
  ```

Sub #9 (`issue/2-9-commit-copilot`)
- Dateien anlegen:
  - `project_templates/common/.github/commit-instructions.md`
  - `project_templates/common/.github/copilot-instructions.md`
- Inhalte: Beispiele (Conventional Commits auf Deutsch), Linter/Mypy Hinweise, pre-commit checklist.
- Tests:
  - `tests/test_instructions_present.py` — prüft Schlüsselwörter wie "Conventional Commits", "ruff", "mypy".
- Acceptance:
  ```bash
  grep -n "Conventional Commits" project_templates -R || true
  ```

Qualitätssicherung (für alle Änderungen)
- Lint & Typprüfung vor Commit:
```bash
poetry run ruff check .
poetry run mypy .
pre-commit run --all-files
```
- Tests:
```bash
poetry run pytest -q --cov=src --cov-report=xml
```
- Keinerlei Linter‑Fehler ignorieren; Fehler werden behoben.

Checkliste vor Merge (je Sub‑PR)
- [ ] Tests vorhanden und lokal grün
- [ ] `poetry run ruff check .` — keine Fehler
- [ ] `poetry run mypy .` — keine Fehler
- [ ] `pre-commit run --all-files` — keine Fehler
- [ ] README/Dokumentation aktualisiert (falls notwendig)
- [ ] PR‑Body mit Acceptance Criteria & Test‑Schritten

Optional: CI/Workflow
- `.github/workflows/ci.yml` mit Schritten:
  - `poetry install --with dev`
  - `poetry run ruff check .`
  - `poetry run mypy .`
  - `poetry run pytest -q --cov=src --cov-report=xml`
  - optional: upload zu `codecov`.

Commit‑und PR‑Konventionen
- Commit‑Subject (Deutsch, ≤50 Zeichen) + Conventional type:
  - `feat(issue/2-6): MVC skeleton for templates`
  - `docs(issue/2-7): add docs rendering examples`
  - `chore(issue/2-8): add GH issue/PR templates`
  - `docs(issue/2-9): add commit/codestyle instructions`
- PR‑Bodies: Referenziere Issue (`Refs: #6`) und Checklist.

Nächste Schritte (ausführbar)
- Ich kann jetzt die Sub‑Branches anlegen und Boilerplate‑Dateien (Templates + Tests) erzeugen, committen & pushen und PRs öffnen.
- Bitte bestätige: Soll ich jetzt automatisch die Sub‑Branches und Dateien anlegen und PRs erstellen? (Antwort: `Ja` oder `Nein`)

---
Datei erstellt als: `untitled-plan-projectTemplates.prompt.md` (im Projekt‑Root).
