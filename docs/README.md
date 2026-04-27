# Dokumentation — Template Python Projekt

Dieses Dokument beschreibt die wichtigsten Konzepte, die CLI‑Nutzung,
Template‑Konventionen und die Tooling‑/CI‑Integration des Starter‑Templates.

## Übersicht

Zweck: Aus Vorlagen in `project_templates/*` ein neues, lauffähiges
Python‑Projekt zu erzeugen. Das Starter‑Skript legt ein klassisches
MVC‑Layout an und sorgt für reproduzierbare Tooling‑Konfigurationen.

Zielgruppe: Entwickler, die schnell neue Projekte mit einheitlicher
Konfiguration erstellen wollen.

## CLI‑Usage

Das Paket stellt ein CLI bereit (Entry‑Point: `template_python_projekt`).
Wichtige Flags:

- `--template <name>` — Name des Vorlagenordners in `project_templates/`.
- `--name <project_name>` — Zieldirectory / Projektname.
- `--dry-run` — Keine Dateien schreiben; zeigt geplante Änderungen.
- `--force` — Überschreibt vorhandene Dateien (nicht empfohlen ohne Backup).

Beispiel:

```bash
python -m template_python_projekt --template cli-basic --name my_project
# dry-run:
python -m template_python_projekt --template cli-basic --name my_project --dry-run
```

## Rendering‑Konzept

- `render.py` rendert Dateien aus `project_templates/<tmpl>/src`.
- Wenn verfügbar, wird `jinja2` verwendet; sonst ein sparsamer Fallback
  für `{{ var }}` und `{{ var | default('value') }}`.
- Beim Schreiben wird ein atomarer Write verwendet (temporäre Datei
  im Zielverzeichnis + `os.replace`) — verhindert partielle Dateien.
- Vor dem Überschreiben vorhandener Dateien werden Backups angelegt.
- Bei Fehlern wird ein Best‑Effort Rollback versucht (Backups wiederherstellen,
  neu erstellte Dateien entfernen).

Nutze `--dry-run`, um Konflikte oder Überschreibungen vorab zu prüfen.

## Template‑Struktur

Erwartete Struktur unter `project_templates/<name>/src/`:

- `model/`, `view/`, `controller/` — Beispielmodule
- `__init__.py`, `main.py` — Paketentrypoints
- `docs/` — projektbezogene Markdown‑Vorlagen

Dateinamen mit Suffix `.jinja` werden beim Rendern ohne Suffix abgelegt.

## Konfig / Tooling

- Verwende `poetry` für Paket/Dev‑Dependencies. Installieren:

```bash
poetry install --with dev
```

- Lint/Format: `ruff`, `isort` (Konfiguration in `pyproject.toml`).
- Typprüfung: `mypy` (strenge Einstellungen in `pyproject.toml`).
- Tests: `pytest` (Tests liegen in `tests/`).
- Pre‑commit: Hooks sind in `pyproject.toml`/`.pre-commit-config.yaml` konfiguriert.

Lokale Prüfungen (empfohlen vor PR):

```bash
poetry run ruff check .
poetry run mypy .
poetry run pytest -q
poetry run pre-commit run --all-files
```

## CI

Eine GitHub Actions Workflow Datei `.github/workflows/ci.yml` führt
`ruff`, `mypy` und `pytest` aus (Python 3.12). Die CI‑Konfiguration ist so
gehalten, dass lokale `poetry run` Befehle sie reproduzieren.

## Best Practices

- Verwende `--dry-run` vor tatsächlichem Schreiben bei Änderungen.
- Achte auf binäre Dateien in Templates — sie sollten nicht als Text gerendert
  werden.
- Behalte Template‑Defaults sinnvoll und dokumentiert (z. B. `default()` im Jinja
  oder Fallback‑Werte im Render‑Context).

## Fehlerbehandlung & Rollback

- Vor Überschreiben vorhandener Dateien werden Backups im temporären Ordner
  angelegt — bei Fehlern versucht das Tool, diese Backups wiederherzustellen.
- Atomare Writes verhindern halbgeschriebene Dateien bei Abbrüchen.
- In kritischen Umgebungen: Vorher `git init` im Zielverzeichnis/Commit als
  zusätzlichen Schutz verwenden.

## Troubleshooting

- `gh` Fehler/401: `gh auth login --web` ausführen und Token prüfen.
- Poetry: Bei Installationsproblemen `poetry cache clear --all` ausführen und
  anschließend erneut installieren.
- Ruff/Mypy Fehler: `poetry run ruff check .` und `poetry run mypy .` lokal
  ausführen und Fehler beheben.

## Contributing

- Branch‑Naming: `issue/4-<num>-<short>` (Sub‑Issue Branches gegen `issue/4`).
- Commit‑Konvention: `Fixes #<num>: Kurze Beschreibung` (wenn das Issue geschlossen
  werden soll).
- Tests und Lint müssen vor PR grün sein.

## Beispiele — minimaler Workflow

```bash
# 1) Installieren (einmalig)
poetry install --with dev

# 2) Neues Projekt mit Template erzeugen (dry-run)
python -m template_python_projekt --template cli-basic --name demo_proj --dry-run

# 3) Ohne dry-run schreiben
python -m template_python_projekt --template cli-basic --name demo_proj
```

---

Bei Fragen oder wenn du konkrete Textpassagen bevorzugst (Ton: ausführlich/kurz),
sage Bescheid — ich passe die Abschnitte an.
