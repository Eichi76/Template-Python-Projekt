Plan: Sub-Issue 33 Umsetzung

TL;DR
Erstelle einen Sub‑Branch von `issue/5` namens `issue/5-33-contrib-guide`; implementiere einen `CONTRIBUTING.md`, passe Tests an, fixe Lint/Type/Pre‑commit, pushe und eröffne erst bei Fertigstellung einen PR gegen `issue/5`.

Schritte

1. Issue‑Details holen
   - PowerShell: `gh issue view 33 --repo Eichi76/Template-Python-Projekt --json title,body,comments`
   - Notiere Titel, Acceptance Criteria, Estimate, Tags/Dependencies.

2. Worktree prüfen & Branch anlegen
   - `git fetch`
   - `git checkout issue/5`
   - `git pull --ff-only origin issue/5`
   - Branch erstellen: `git checkout -b issue/5-33-contrib-guide`

3. Implementieren
   - Erstelle/ändere `CONTRIBUTING.md` gemäß Acceptance Criteria: Prozess, Tests, Template‑Metadata‑Schema, PR‑Checklist.
   - Falls nötig, ergänze/aktualisiere Template‑Vorlagen in `project_templates/`.
   - Ergänze oder passe Tests in `tests/` an, die das Verhalten absichern.

4. Lokale Qualitätssicherung (iterativ)
   - Ruff: `poetry run ruff check .` → Fehler/Warnungen beheben.
   - Mypy: `poetry run mypy .` → Typfehler beheben (repo verlangt `disallow_untyped_defs = true`).
   - Pre‑commit: `pre-commit run --all-files` → Hooks ausführen und Probleme fixen.
   - Tests: `pytest -q --cov=src --cov-report=xml` → Tests grün.
   - Iteriere bis alle Checks grün sind.

5. Commits
   - Kleine, thematische Commits mit klaren Nachrichten.
   - Pre‑commit Hooks laufen beim Commit — behebe auftretende Warnungen vor Push.

6. Push & PR (erst wenn fertig)
   - Push: `git push -u origin issue/5-33-contrib-guide`
   - PR erstellen gegen `issue/5` (kein Draft):
     - Deutscher Titel, z. B. „Issue 33: Contribution‑Guide für Templates hinzufügen“
     - Ausführliche Beschreibung: Motivation, Änderungen, Tests, Migrationsschritte, Follow‑ups, Verweis auf Issue #33.
   - PR Merge: Squash‑Merge nach eigener Prüfung (kein weiterer Reviewer nötig).

7. Nach dem Merge
   - `git checkout issue/5 && git pull`
   - `git branch -d issue/5-33-contrib-guide`

Relevante Dateien
- `pyproject.toml` — Python‑Version, `mypy`/`ruff` Einstellungen.
- `.pre-commit-config.yaml` — Hooks (ruff/isort/mypy).
- `.github/workflows/ci.yml` — CI‑Python‑Version und Actions.
- `project_templates/` — Template‑Vorlagen.
- `src/template_python_projekt/` — Starter/Renderer Code (bei Bedarf anpassen).
- `tests/` — Tests anpassen/erweitern.

Verifikation
1. `poetry run ruff check .` → keine Errors/Warnungen.
2. `poetry run mypy .` → keine Typfehler.
3. `pre-commit run --all-files` → alle Hooks grün.
4. `pytest -q --cov=src --cov-report=xml` → alle Tests grün.

PowerShell Kurzbefehle
```powershell
# Issue Info holen
gh issue view 33 --repo Eichi76/Template-Python-Projekt --json title,body,comments

# Branch erstellen
git fetch
git checkout issue/5
git pull --ff-only origin issue/5
git checkout -b issue/5-33-contrib-guide

# Qualität & Tests
poetry run ruff check .
poetry run mypy .
pre-commit run --all-files
pytest -q --cov=src --cov-report=xml

# Push
git push -u origin issue/5-33-contrib-guide

# PR (gh)
gh pr create --base issue/5 --title "Issue 33: Contribution‑Guide für Templates hinzufügen" --body "<ausführliche Beschreibung>" --repo Eichi76/Template-Python-Projekt
```

Entscheidungen / Annahmen
- PRs werden gegen `issue/5` gemerged.
- Kein Reviewprozess nötig — du mergest selbst.
- Branchname: `issue/5-33-contrib-guide`.

Nächste Schritte
- Auf Wunsch erzeuge ich den Branch lokal oder bereite die PR‑Beschreibung vor.
