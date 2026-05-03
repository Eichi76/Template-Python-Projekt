# Migration & Updates — Beste Praxis

Diese Seite bietet eine Checkliste und sichere Vorgehensweisen zum
Aktualisieren bestehender Projekte, basierend auf Issue #36.

## Kurzüberblick

- Ziel: sichere, reproduzierbare Updates von Projekten, inklusive Backup- und
  Test-Schritten.

## Schnell-Checkliste

1. Vollständiges Backup / Git-Branch erstellen
2. Abhängigkeiten prüfen (`poetry show --outdated`)
3. Tests lokal laufen lassen (`poetry run pytest -q`)
4. Änderungen in temporäre Dateien rendern
5. Dateien vergleichen und Konflikte manuell lösen
6. Commit, Lint & Typecheck
7. Merge nach erfolgreicher QA

## Beispiele

(Platzhalter — konkrete Beispiele zu `pyproject.toml` und `README.md`
folgen in einem späteren Commit)

## Troubleshooting

(Platzhalter)

---

*Scaffold erstellt für Issue #36 — weitere Inhalte folgen.*
