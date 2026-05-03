# Contribution Guide

Dieses Dokument beschreibt, wie Beiträge zu diesem Repository eingereicht,
getestet und gemerged werden sollen. Ziel ist ein reproduzierbarer Prozess
für neue Templates und Anpassungen an bestehenden Templates.

## Kurzer Workflow

- Basis‑Branch für Feature‑Arbeit: `issue/5` (Sub‑Branches im Format
  `issue/5-<num>-<short>`).
- Erstelle lokalen Branch, implementiere Änderungen, sorge dafür, dass alle
  Checks grün sind und öffne erst dann einen Pull Request gegen `issue/5`.
- PR‑Titel auf Deutsch, Merge per Squash‑Merge.
- Single‑Person‑Team: keine weiteren Reviewer nötig.

## Branching

- Hole zuerst den aktuellen Parent‑Branch:

```powershell
git fetch
git checkout issue/5
git pull --ff-only origin issue/5
git checkout -b issue/5-33-contrib-guide
```

Ersetze `33` und `contrib-guide` entsprechend Issue‑Nummer und kurzer
Beschreibung.

## Tests & lokale Checks

Führe vor Commits und Pushs stets die folgenden Befehle aus:

```powershell
# Lint
poetry run ruff check .

# Typechecking
poetry run mypy .

# Pre-commit Hooks (lokal)
pre-commit run --all-files

# Tests
pytest -q --cov=src --cov-report=xml
```

Wenn ein Check fehlschlägt, behebe die Fehler lokal und wiederhole die
Befehle. Commits sollten die Hooks passieren (pre-commit ist konfiguriert).

## Template‑Metadata‑Schema (Empfehlung)

Neue oder geänderte Templates sollten eine kurze Metadaten‑Sektion (YAML)
enthalten, die vom Renderer erwartet wird. Beispiel (`template.yaml`):

```yaml
name: "cli-basic"
version: "0.1.0"
description: "Minimal template für CLI‑Projekte"
author: "Your Name <mail@example.com>"
tags:
  - cli
  - basic
compatibility:
  python: ">=3.12,<3.13"
tests:
  - "pytest"
```

Dokumentiere alle erforderlichen Metafelder in der jeweiligen
Template‑README.

## PR‑Checklist (für die Beschreibung)

Eine PR Beschreibung muss mindestens enthalten:

- Deutschen Titel, z. B. „Issue 33: Contribution‑Guide für Templates
  hinzufügen“
- Kurze Zusammenfassung der Änderungen
- Motivation / Problem, das gelöst wird
- Akzeptanzkriterien (siehe Issue #33)
- Liste der ausgeführten Checks (ruff, mypy, pre-commit, pytest) und deren
  Status
- Hinweise zur manuellen Verifikation (Schritte, Dateien zu prüfen)
- Falls relevant: Migrationsschritte, Breaking Changes, Follow‑ups

Beispiel `gh`‑Befehl zum Erstellen des PRs (erst ausführen, wenn alles grün
ist):

```powershell
gh pr create --base issue/5 --title "Issue 33: Contribution‑Guide für
Templates hinzufügen" --body "<ausführliche Beschreibung>" --repo
Eichi76/Template-Python-Projekt
```

## Commit‑Konventionen

- Schreibe klare Commit‑Nachrichten; gruppiere Änderungen thematisch.
- Pre‑commit Hooks laufen beim Commit; falls Hooks Fehler melden, behebe
  diese vor Push.

## Verantwortlichkeit & Review

- Da dieses Repo als Single‑Person‑Team geführt wird, genügt die eigene
  Prüfung; PRs werden nach eigener Abnahme per Squash‑Merge zusammengeführt.

## Fragen

Bei Rückfragen oder Unklarheiten verweise auf Issue #33 oder öffne ein
kurzes Issue/PR‑Kommentar.
