# Quickstart — Von Scratch zum "ready to use" Projekt

Dieses Quickstart beschreibt in wenigen Schritten, wie ein neues Projekt aus
den Vorlagen erzeugt und lokal verifiziert wird.

Voraussetzungen

- Python 3.12
- `poetry` (empfohlen) oder `pip` für Entwicklungsinstallation
- Optional: `node`/`npm` für Templates, die JS/MD‑Tools nutzen

Schritte

1. Repository klonen

```bash
git clone https://github.com/Eichi76/Template-Python-Projekt.git
cd Template-Python-Projekt
```

1. Parent‑Branch auschecken (optional, für Issue‑Workflows)

```bash
git checkout issue/5
```

1. Paket für Entwicklung installieren

Mit Poetry:

```bash
poetry install --with dev
```

Alternativ (pip editable):

```bash
python -m pip install -e .
```

1. Projekt aus Template erzeugen (Beispiel: CLI‑Template)

```bash
python -m template_python_projekt --template cli-basic --name demo
```

Erwartetes Ergebnis:

Ein neues Verzeichnis `demo/` mit der typischen MVC‑Struktur
(`model/`, `view/`, `controller/`). Zusätzlich werden eine
`pyproject.toml` und eine Beispiel‑`README.md` erzeugt.

1. Verifizieren

- Linting:

```bash
poetry run ruff check .
```

- Typecheck:

```bash
poetry run mypy .
```

- Tests (im Projekt‑Root):

```bash
pytest -q
```

Häufige Probleme

- `poetry` fehlt: siehe `docs/README.md` (Troubleshooting).
- Schreibrechte: Stelle sicher, dass das Zielverzeichnis beschreibbar ist.

Nächste Schritte

- Ergänze diesen Quickstart mit Screenshots, Beispielausgaben und
  optionalen CI‑Skripten zum Smoke‑Test.

- Siehe auch die detaillierte Anleitung zur manuellen Initialisierung:
  [Manuelle Initialisierung](manual_initialization.md) — reproduziert das
  Verhalten des Starterskripts Schritt für Schritt (Issue #31).
