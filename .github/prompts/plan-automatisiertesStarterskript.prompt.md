NOTE: PR‑Bodies werden vorerst NICHT erstellt; PRs erst öffnen nach kompletter Bearbeitung eines Sub‑Issues.

## Plan: Umsetzung von Parent Issue #4 (Sub-Issues #19–#28)

TL;DR - Was, warum, wie
- Ziel: Parent Issue #4 („Automatisiertes Starterskript entwickeln und integrieren") vollständig umsetzen, indem sequenziell die Sub-Issues #19–#28 bearbeitet werden.
- Warum: Saubere, nachvollziehbare Feature‑Entwicklung mit isolierten Branches, Tests und Linter‑Checks; keine Draft‑PRs, keine vorzeitigen Merges.
- Wie: Für jedes Sub‑Issue: Branch erstellen, implementieren, lokale Checks (`ruff`, `mypy`, Tests, `pre-commit`), pushen, PR öffnen (Deutsch, ausführliche Beschreibung), CI abwarten, mergen. Reihenfolge: #19 → #20 → #21 → #22 → #23 → #24 → #25 → #26 → #27 → #28.

**Steps**
1. Vorbereitung (einmalig)
- Lokales Setup prüfen: `poetry install --with dev` oder `python -m pip install -e .` + Dev-Tools.
- Parent-Branch: `git checkout -b issue/4` (pushen: `git push -u origin issue/4`).
- Sicherstellen, dass `gh` Zugriff hat (Token in env) und `poetry`, `node` (optional) installiert sind.

2. Für jedes Sub‑Issue (sequenziell, Nummernreihe beachten)
- 2.1 Branch erstellen beim Start der Arbeit an dem Sub‑Issue:
  - `git checkout -b issue/4-<num>-<short>` (Beispiel: `git checkout -b issue/4-19-cli-design`).
- 2.2 Implementieren: Folge der Issue‑Aufgaben (siehe "Issue‑Spezifika" unten).
- 2.3 Lokale Checks wiederholt ausführen während Entwicklung:
  - `poetry run ruff check .`
  - `poetry run mypy .`
  - `pytest -q --maxfail=1` (oder gezielt: `pytest tests/test_xxx.py`).
- 2.4 Committieren (prägnante Commit‑Message, Referenz auf Issue):
  - `git add -A`
  - `git commit -m "Fixes #<num>: Kurze Beschreibung"`
- 2.5 Pre-commit Hooks prüfen: Falls Hooks fehlschlagen, Fehler beheben, nicht umgehen.
- 2.6 Push: `git push origin issue/4-<num>-<short>`
- 2.7 PR öffnen (nicht Draft) mit `gh` und deutschen Titel + ausführlicher Beschreibung (Vorlage unten):
  - `gh pr create --base issue/4 --head issue/4-<num>-<short> --title "Feature: <Kurzbeschreibung in DE>" --body "<ausführliche PR-Beschreibung>"`
  - 2.8 Merge: Nur wenn alle Checks grün sind, PR nicht als Draft, und alle Akzeptanzkriterien erfüllt sind. PRs von Sub‑Issue‑Branches werden immer per Squash‑Merge zusammengeführt (z. B. über die GitHub‑UI oder `gh pr merge --squash`).

3. Parent-Branch Integration
- Nach Abschluss aller Sub‑Issues: lokaler Rebase/Merge auf `issue/4` (z. B. `git checkout issue/4` + `git merge --no-ff issue/4-19-cli-design` usw. oder PRs direkt gegen `issue/4`).
- Finaler PR von `issue/4` → `main` öffnen, Tests/Lint prüfen, mergen.

**Issue‑Spezifika (kurz, pro Sub‑Issue)**
- Parent: `issue/4` — Sammelbranch, Basis aller Sub‑Issue‑PRs.

- #19 — CLI‑Schnittstelle (low)
  - Aufgaben: CLI‑Spec schreiben, `--help` implementieren (z. B. `argparse` oder `click`), Exit‑Codes definieren.
  - Dateien: `src/template_python_projekt/__init__.py`, `src/template_python_projekt/main.py` (neues CLI entrypoint), ggf. `pyproject.toml` entry points.
  - Tests: neue Tests in `tests/test_template_cli_basic.py`.
  - Beispiel‑Branch: `issue/4-19-cli-design`.

- #20 — Platzhalter‑Renderer (medium)
  - Aufgaben: Erweiterung/Implementierung in `src/template_python_projekt/render.py` für sichere Placeholder‑Ersetzung, Unit‑Tests.
  - Dateien: `src/template_python_projekt/render.py`, evtl. neue `tests/test_template_renderer.py`.
  - Besonderheiten: sichere Behandlung binary Dateien, newline/encoding.
  - Branch: `issue/4-20-placeholder-engine`.

- #21 — pyproject/package.json Merge (medium)
  - Aufgaben: Merge‑Logik (behalte user‑values), Validierung (`poetry check`).
  - Dateien: `src/template_python_projekt/render.py`, Tests: `tests/test_pyproject_template.py`.
  - Branch: `issue/4-21-merge-metadata`.

- #22 — Poetry environment + Installation (medium)
  - Aufgaben: Automatisches Auslösen von `poetry install` oder Hinweise, Fehlerhandling.
  - Dateien: `src/template_python_projekt/render.py`, eventuell `scripts/` Hilfsfunktionen.
  - Branch: `issue/4-22-poetry-env`.

- #23 — Node & markdownlint (low)
  - Aufgaben: Prüfe Node; falls vorhanden `npm install -g markdownlint-cli` oder lokale `package.json` Anpassungen; dokumentiere Fallback.
  - Dateien: `src/template_python_projekt/render.py`, `project_templates/*/common package.json.jinja`.
  - Branch: `issue/4-23-markdownlint`.

- #24 — pre-commit Hooks (low)
  - Aufgaben: `pre-commit install` im Zielprojekt; template für `.pre-commit-config.yaml` sicherstellen.
  - Dateien: `project_templates/*`, `src/template_python_projekt/render.py`.
  - Branch: `issue/4-24-precommit`.

- #25 — Dry‑Run & Validierung (medium)
  - Aufgaben: Implementiere `--dry-run` für CLI, prüfe Konflikte ohne zu schreiben.
  - Dateien: `src/template_python_projekt/render.py`, Tests: `tests/test_render_directory.py`.
  - Branch: `issue/4-25-dry-run`.

- #26 — Fehlerbehandlung & Rollback (medium)
  - Aufgaben: Backup vor Änderung, atomare Writes, Rollback bei Fehlern.
  - Dateien: `src/template_python_projekt/render.py`.
  - Branch: `issue/4-26-rollback`.

- #27 — Tests & CI (high)
  - Aufgaben: Unit- und Integrationstests ergänzen; CI Workflow (`.github/workflows/ci.yml`) ergänzen für ruff, mypy, pytest.
  - Dateien: `tests/*`, add/modify `.github/workflows/*`.
  - Branch: `issue/4-27-ci-tests`.

- #28 — Dokumentation (low)
  - Aufgaben: `docs/README.md` erweitern mit Examples, Troubleshooting, CLI‑Usage.
  - Dateien: `docs/README.md`, README.md Ergänzungen.
  - Branch: `issue/4-28-docs`.

**Verifizierungs‑Schritte (pro Sub‑Issue)**
1. Lint & Typecheck: `poetry run ruff check .` und `poetry run mypy .` — beide müssen lokal grün sein.
2. Tests: `pytest -q` — alle relevanten Tests grün (bei Änderung gezielt ausführen).
3. Pre-commit: `pre-commit run --all-files` (oder Commiten und beobachten).
4. CI: Prüfe GitHub Actions nach Push/PR; fixe CI‑Fehler lokal.
5. Merge: PR erst mergen, wenn alle Checks bestanden.

**PR‑Titel und -Beschreibung (Vorlagen)**
- PR‑Titel (DE): `Feature: <Kurzbeschreibung>` oder `Fix: <Kurzbeschreibung>` bei Bugfixes.
- PR‑Beschreibung (Template):
  ## Zusammenfassung
  <Kurzbeschreibung in DE>

  ## Änderungen
  - <Aufzählung der Änderungen / Dateien>

  ## Akzeptanzkriterien
  - [ ] <Kriterium 1>
  - [ ] <Kriterium 2>

  ## Testanweisungen
  ```bash
  poetry run ruff check .
  poetry run mypy .
  pytest -q tests/test_xxx.py
  ```

  ## Verwandte Issues
  - Parent: #4
  - Dieses PR schließt: #<num>

**Konkrete `gh` Beispiele**
- PR erstellen gegen Parent-Branch `issue/4`:
  gh pr create --base issue/4 --head issue/4-19-cli-design --title "Feature: CLI-Schnittstelle für Starterskript" --body "## Zusammenfassung\nImplementiert CLI...\n"

- Merge nach Erfolg: `gh pr merge <PR_NUM_OR_URL> --merge --body "Merge von Sub-Issue <num>"`

**CI / Konfigurations‑Risiken**
- `pyproject.toml` enthält ruff/mypy settings; CI prüft diese. Falls CI-Checks strenger sind, lokale Umgebung anpassen.
- Pre-commit Hooks können lokale Abbrüche verursachen — immer lokal ausführen, Fehler beheben.

**Entscheidungen & Annahmen**
- PRs werden gegen `issue/4` geöffnet (nicht direkt gegen `main`), Parent-Branch sammelt alle Sub-Issue-Merges.
- Kein Review-Prozess nötig (Single‑Person‑Team).
- Keine Draft‑PRs: PRs sind fertig zum Review/Merge, wenn geöffnet.

**Weiterführende Punkte / Fragen**
1. Möchtest du, dass ich jetzt direkt die Issues via `gh` abhole und die exakten Issue‑Bodies in den Plan einbaue? (empfohlen)
2. Sollen PR‑Beschreibungen automatisiert aus Issue‑Inhalt generiert werden? (ja/nein)

---

Ende der Plan‑Erweiterung.
