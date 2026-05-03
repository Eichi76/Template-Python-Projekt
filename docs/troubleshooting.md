# Troubleshooting & FAQ

Dieses Dokument fasst die häufigsten Probleme beim Arbeiten mit dem
Template‑Projekt zusammen und bietet kurze Lösungshinweise.

Kurz: Wenn ein Werkzeug fehlt oder ein Hook scheitert, reproduziere das
Problem lokal und folge den in dieser Datei beschriebenen Schritten.

## Top-10 Fehlerfälle

### 1) `poetry` fehlt / `poetry` nicht gefunden

Symptom: `poetry`-Befehle schlagen fehl.

Ursache: Poetry ist nicht installiert oder nicht im PATH.

Lösung:

- `python -m pip install --user poetry`
- `poetry --version`

### 2) `node` fehlt

Symptom: Node‑abhängige Tools melden `node: command not found`.

Ursache: Node ist nicht installiert oder veraltet.

Lösung:

- Installiere Node (LTS), z. B. [Node.js](https://nodejs.org)
- `node --version`

### 3) `pre-commit` schlägt fehl

Symptom: Hooks verhindern Commits oder melden Fehler.

Ursache: Style/Format oder fehlende Tools.

Lösung:

- `pre-commit run --all-files`
- Falls Hooks automatisch fixen, `git add` und erneut prüfen.

### 4) Merge‑Konflikte

Symptom: `git merge`/PR zeigt Konflikte.

Ursache: Änderungen an denselben Zeilen in mehreren Branches.

Lösung:

- `git fetch origin` && `git rebase origin/main`
- Konflikte manuell lösen, testen und committen.

### 5) Dateiberechtigungen / Schreibschutz

Symptom: Schreibfehler beim Erstellen oder Ändern von Dateien.

Ursache: Fehlende Dateirechte oder schreibgeschützte Ordner.

Lösung:

- Prüfe Dateirechte; passe Rechte an oder nutze erhöhte Rechte.

### 6) virtuelle Umgebung / falsche Python-Version

Symptom: mypy/pytest/ruff melden Inkompatibilitäten.

Ursache: Falsche Python‑Version oder aktive Umgebung.

Lösung:

- `python -m venv .venv` und aktivieren
- `poetry install --with dev` oder `pip install -e .`

### 7) `pyproject.toml` Merge-/Formatprobleme

Symptom: TOML‑Blöcke kollidieren nach Merge.

Ursache: Manuelle Änderungen in verschiedenen Branches.

Lösung:

- Vergleiche mit Tools oder `tomllib`, teste `poetry lock` danach.

### 8) Template Rendering Fehler

Symptom: Gerenderte Dateien enthalten Platzhalter oder fehlen Werte.

Ursache: Fehlende Variablen oder Jinja‑Syntaxfehler.

Lösung:

- Renderer lokal testen, z. B.:

  ```bash
  python -c "from template_python_projekt import render; \
  print(render.render_template_file('path', {'name':'x'}))"
  ```

### 9) Fehlende Templates / falscher Name

Symptom: `FileNotFoundError: Template not found` beim Rendern.

Ursache: Template fehlt oder falscher Pfad/Name.

Lösung:

- Prüfe `project_templates/<name>/src` und nutze den korrekten Namen.

### 10) CI‑Fehler nach Push

Symptom: GitHub Actions fehlschlagen (Tests/Lint).

Ursache: Unterschiede zwischen lokaler Umgebung und CI.

Lösung:

- Reproduziere CI‑Schritte lokal: `poetry run ruff check .` und `pytest -q`.

## Debugging‑Tipps

- Zuerst lokal reproduzieren: `ruff`, `mypy`, `pytest`.
- Nutze `--verbose` für mehr Logs.

## Nützliche Befehle

- `poetry install --with dev`
- `pre-commit run --all-files`
- `pytest -q --cov=src --cov-report=xml`

## Weiterführende Links

- README.md und `docs/README.md` für Template‑Konventionen.
