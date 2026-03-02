<!-- Copilot / AI-Agent instructions for Template-Python-Projekt -->
# Kurzgefasst

Dieses Repo ist ein Starter‑Template für neue Python‑Projekte. Ziel: ein CLI/Starter‑Skript (`src/template_python_projekt`) erzeugt aus Vorlagen unter `project_templates/*` ein neues Projekt im klassischen MVC‑Layout.

# Architektur — große Linien
- `src/template_python_projekt/` – das Starterpaket (veröffentlichen/installierbar aus `src/`).
- `project_templates/*/src/` – enthalten Beispiel‑`model/`, `view/`, `controller/` und `__init__.py` (quasi Blueprint‑Templates).
- `docs/README.md` – beschreibt Template‑Rendering‑Konventionen und erwartete Zielstruktur.

# Was ein AI‑Agent sofort wissen muss
- Paket‑Layout: das Projekt verwendet das `src/`-Layout; Imports sollten `template_python_projekt` referenzieren.
- Python‑Version: in `pyproject.toml` auf `>=3.12,<3.13` festgelegt — generiere Code für 3.12‑Kompatibilität.
- Tests: `pytest` wird verwendet (siehe `dependency-groups.test`). Coverage‑Werkzeuge (`pytest-cov`, `codecov-cli`) sind vorgesehen.
- Linting & Formatting: `ruff`, `isort` und `mypy` sind konfiguriert in `pyproject.toml`; Folge deren Einstellungen (z. B. `line-length = 100`, `disallow_untyped_defs = true`).

# Typische Dev‑Workflows & Befehle (konkret)
- Lokale Installation (wenn Poetry verwendet): `poetry install --with dev`.
- Alternativ (pip editable):
  - `python -m pip install -e .` — installiert Paket für Entwicklung.
  - Dev‑Tools manuell: `python -m pip install ruff mypy pytest pytest-cov pre-commit`.
- Tests: `pytest -q --cov=src --cov-report=xml` erzeugt Coverage‑Report für CI.
- Lint & Format:
  - `ruff check src tests` (fast linting, respektiert `pyproject.toml`).
  - `isort --profile black .` / `mypy src` wenn Typsicherheit geprüft werden soll.
- Pre‑commit: Repo enthält `pre-commit` in `pyproject.toml` dev‑Gruppe; runnen vor Commit.

# Projekt‑Konventionen & Patterns
- Template‑Generator: Änderungen am Generator in `src/template_python_projekt` müssen kompatible Template‑Konventionen in `project_templates/*` beibehalten (z. B. erwartete Ordnernamen `model`, `view`, `controller`).
- Tests liegen im Top‑Level `tests/` Ordner und importieren das Paket via `template_python_projekt`.
- Verwende explizite Typannotationen: `pyproject.toml` aktiviert strenge mypy‑Optionen (z. B. `disallow_untyped_defs = true`). Bevorzuge voll typisierte Signaturen.
- Halte Einrückung und Stil an `pyproject.toml` (4 spaces, line-length 100, double quotes für Strings laut Ruff‑Konfig).

# Integrationpunkte & externe Abhängigkeiten
- Keine externen Webservices automatisch eingebunden; CI‑Tools (z. B. Codecov) sind vorhanden in Abhängigkeiten, falls Coverage‑Upload benötigt wird.
- Packaging: `build-system` verwendet `poetry-core` — Releases sollten über die üblichen Poetry/PEP build‑Schritte erfolgen.

# Beispiele aus dem Repo (wo nachsehen)
- Starter‑Code: [src/template_python_projekt](src/template_python_projekt)
- Templates: [project_templates](project_templates)
- Projekt‑Metadaten und Tool‑Konfiguration: [pyproject.toml](pyproject.toml)
- Nutzung / Zweck: [README.md](README.md)

# Was nicht tun
- Keine Annahmen über nicht‑versionierte externe Konfigurationen treffen (z. B. CI‑Secrets).
- Keine Breaking‑API‑Änderungen am Starterpaket ohne Update der zugehörigen Templates in `project_templates/*`.

# Kurze Checkliste für PRs, die ein AI‑Agent erstellen soll
- `tests/`: neue Features müssen Tests haben und lokal mit `pytest` laufen.
- `pyproject.toml` bleiben: passe nur, wenn Tools oder supported Python‑Versionen geändert werden.
- Style / Type: `ruff` und `mypy` sollten lokal grün sein (oder dokumentierte Ausnahmen in `pyproject.toml`).

Wenn etwas unklar ist, bitte konkret fragen (z. B. "Welche Template‑Variablen sind erlaubt?").
