# Manuelle Initialisierung — Reproduzieren des Starterskripts (Issue #31)

Zweck

- Beschreibt die Schritte, mit denen das Verhalten des Starterskripts
  `template_python_projekt` nachvollzogen werden kann.

Akzeptanzkriterien

- Ein Nutzer kann die Ausgabe und die Struktur reproduzieren, die das
  Starterskript erzeugt.
- Alle in den Templates erzeugten Dateien und Merge‑Schritte sind
  dokumentiert.
- Die Anleitung ist in einer frischen Umgebung ausführbar.

Voraussetzungen

- `python >=3.12` installiert
- `poetry` oder `python -m pip` zur lokalen Installation
- Git und ein frisches Arbeitsverzeichnis für den Test

Kurzanleitung (Beispielablauf)

1. Repository klonen

```bash
git clone https://github.com/Eichi76/Template-Python-Projekt.git
cd Template-Python-Projekt
```

1. Installieren (empfohlen: Poetry)

```bash
poetry install --with dev
# oder: python -m pip install -e .
```

1. Virtuelle Umgebung aktivieren (falls nicht durch Poetry verwaltet)

1. Starterskript ausführen (Beispiel)

```bash
python -m template_python_projekt --template cli-basic \
  --output /pfad/zum/zielprojekt
```

1. Erwartete Ausgabe / Struktur prüfen

- `pyproject.toml` im Zielprojekt vorhanden und zusammengeführte
  Einstellungen enthalten
- Ordnerstruktur: `src/`, `model/`, `view/`, `controller/` wie in den
  `project_templates/*` Vorlagen
- `README.md` und `pre-commit-config.yaml` (falls das Template sie
  enthält) vorhanden

1. Manuelle Reproduktionsschritte (was das Starterskript intern macht)

- Kopiere Dateien und Templates aus
  `project_templates/<template>/src/` nach dem Zielprojekt
- Führe die Merge‑Logik für `pyproject.toml` aus (ggf. nur bestimmte
  Felder)
- Kopiere die `pre-commit` Konfiguration und installiere lokale Hooks

Empfohlene Befehle zur Verifikation

```bash
# Linting
poetry run ruff check .
# Type checks
poetry run mypy .
# Tests
poetry run pytest -q tests/test_template_cli_basic.py
```

Häufige Prüfpunkte / Troubleshooting

- Fehlende Abhängigkeiten: `poetry install` erneut ausführen
- Merge‑Konflikte in `pyproject.toml`: prüfen, welche Felder vom
  Template erwartet werden
- Line‑Endings / Rechte: sicherstellen, dass `pre-commit` installiert
  ist

Weiteres

- Ergänze hier Beispiele für spezifische Template‑Outputs, falls du
  konkrete Vergleichsoutputs (z. B. vollständiges `pyproject.toml`) wünschst.

Referenzen

- `project_templates/cli-basic/`
- `src/template_python_projekt/render.py`
- Issue: [#31](https://github.com/Eichi76/Template-Python-Projekt/issues/31)
