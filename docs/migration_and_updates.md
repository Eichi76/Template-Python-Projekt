# Migration & Updates — Beste Praxis

Diese Seite bietet eine Checkliste und sichere Vorgehensweisen zum
Aktualisieren bestehender Projekte, basierend auf Issue #36.

## Kurzüberblick

- Ziel: sichere, reproduzierbare Updates von Projekten, inklusive Backup- und
  Test-Schritten.

## Schnell-Checkliste

1. Vollständiges Backup / Git-Branch erstellen
1. Abhängigkeiten prüfen (`poetry show --outdated`)
1. Tests lokal laufen lassen (`poetry run pytest -q`)
1. Änderungen in temporäre Dateien rendern
1. Dateien vergleichen und Konflikte manuell lösen
1. Commit, Lint & Typecheck
1. Merge nach erfolgreicher QA

## Beispiele

(Platzhalter — konkrete Beispiele zu `pyproject.toml` und `README.md`
folgen in einem späteren Commit)

## Troubleshooting

(Platzhalter)

---

*Scaffold erstellt für Issue #36 — weitere Inhalte folgen.*

## Detaillierte Schritt-für-Schritt Anleitung

1. Vorbereitung

- Erstelle einen neuen Branch vom aktuellen Arbeitsbranch, z. B.:

  ```bash
  git checkout -b issue/5-36-migration issue/5
  ```

- Erstelle ein vollständiges Backup oder stelle sicher, dass alle
  Änderungen versioniert sind.

1. Abhängigkeiten prüfen

- Prüfe veraltete Abhängigkeiten:

  ```bash
  poetry show --outdated
  ```

1. Tests vorab laufen lassen

- Führe die Tests lokal über Poetry aus:

  ```bash
  poetry run pytest -q
  ```

- Behebe Fehler bevor du Änderungen an der Zielstruktur anwendest.

1. Dry Run / Render in temporäre Dateien

- Render die Templates in ein temporäres Verzeichnis, statt direkt zu
  überschreiben. Vergleiche die gerenderten Dateien mit den existierenden
  Dateien (diff).

1. Dateien vergleichen und Konflikte lösen

- Nutze `git diff`, `diff`-Tools oder `meld`/`kdiff3` um Änderungen zu prüfen.

1. Änderungen anwenden (Update-Strategien)

- Standard-Verhalten: `backup` — die bestehende Datei wird als
  `filename.bak.TIMESTAMP` gesichert und die neue Datei geschrieben.
- Alternativen: `skip` (bestehende Datei behalten) oder `overwrite` (direkt ersetzen).

- Beispiel-CLI (Später implementiert in `template_python_projekt`):

  ```bash
  python -m template_python_projekt \
    --update-mode backup \
    --render target_dir
  ```

1. Lint, Typecheck und Pre-commit

- Linting mit Ruff:

  ```bash
  poetry run ruff check .
  ```

- Typechecking mit mypy:

  ```bash
  poetry run mypy .
  ```

- Führe `pre-commit run --all-files` falls gewünscht aus und behebe Hinweise.

1. Commit & QA

- Committe die Änderungen in sinnvollen Schritten (Docs, Templates, Code, Tests).
- Führe die Tests erneut aus und verifiziere das Verhalten:

  ```bash
  poetry run pytest -q
  ```

1. Pull Request

- Erstelle den PR mit deutschem Titel, ausführlicher Beschreibung und How‑to‑Test.
- Merge per `squash` nach erfolgreicher QA.

## Konkrete Beispiele

### Beispiel: `pyproject.toml` update

1. Render die neue `pyproject.toml` in ein temporäres Verzeichnis.
1. Vergleiche die Abschnitte `tool.poetry.dependencies` und `tool.poetry.dev-dependencies`.
1. Übernimm nur notwendige Änderungen manuell oder per Patch.

### Beispiel: `README.md` Merge‑Muster

- Bewahre Projekt-spezifische Abschnitte (z. B. Usage, Beispiele) und
  übernehme generische Vorlagen-Änderungen.

## Troubleshooting — Häufige Probleme

- Markdownlint/Formatting-Fehler: `pre-commit` ausführen und Hinweise befolgen.
- Fehlende Type-Hinweise: mypy-Fehler lesen und schrittweise beheben.
- Merge-Konflikte: lieber manuell lösen, Backup-Dateien nutzen.

## Hinweise zur CLI-Integration

- Flag-Name: `--update-mode` (Werte: `backup`, `skip`, `overwrite`).
- Default: `backup`.
- Die CLI ist nicht-interaktiv; automatische Entscheidungen werden dokumentiert.
