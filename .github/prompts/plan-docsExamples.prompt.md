## Plan: Issue #34 — Dokumentation für Beispielprojekte

TL;DR: Ergänze für jedes Beispielprojekt (CLI und PySide6) eine README/Docs‑Seite mit Ausführungen zu Ausführen, Debuggen, Testen und Packaging plus Beispielausgabe. Implementierung erfolgt in einem Sub‑Branch von `issue/5`, alle Änderungen testen, linten und typprüfen; erst am Ende PR öffnen und per Squash‑Merge zusammenführen.

**Steps**
1. Discovery: Inhalte des Issue #34 prüfen und Abhängigkeiten bestätigen (*done*).
2. Branch anlegen: Von `issue/5` aus einen Sub‑Branch erstellen mit Namen `issue/5-34-docs-examples`.
3. Scoping: Liste aller Beispiel‑Templates ermitteln — mindestens `project_templates/cli-basic` und `project_templates/ui-pyside6`.
4. Implementierung (parallel pro Template):
   - `cli-basic`: Erstelle/ergänze `project_templates/cli-basic/docs/README.md.jinja` mit Run/Debug/Test/Packaging‑Schritten und Beispielausgabe.
   - `ui-pyside6`: Erstelle/ergänze `project_templates/ui-pyside6/README.md.jinja` (oder `docs/` falls vorhanden) mit gleichen Inhalten plus Hinweise zu PySide6‑Start und Packaging.
   - Falls Vorlagen bereits `index.md.jinja` oder `README.md.jinja` enthalten, erweitere diese statt neue Dateien anzulegen.
5. Test‑ & Template‑Check: Passe ggf. `tests/` an oder ergänze kleinere Tests, die sicherstellen, dass die README‑Renders keine Fehler erzeugen (z. B. `tests/test_template_renderer.py` prüfen).
6. Lokale Qualitätssicherung:
   - Lint: `poetry run ruff check .` — alle Warnungen/Fehler beheben.
   - Typprüfung: `poetry run mypy .` — Fehler beheben.
   - Pre‑commit: `pre-commit run --all-files` — auftretende Probleme beheben.
   - Tests: `poetry run pytest -q` — grün.
7. Commit‑Schritte:
   - Committen in sinnvollen Einheiten mit deutschen Commit‑Nachrichten (Kurz, präzise).
   - Bei mehreren Commits rebase/squash lokal nach Bedarf, damit PR sauber ist.
8. Push: Branch ins Remote pushen (`git push -u origin issue/5-34-docs-examples`).
9. PR erstellen (erst wenn alle Implementierungen und QA abgeschlossen):
   - Verwende `gh` oder MCP‑Tooling. PR‑Regeln: deutscher Titel, ausführliche Beschreibung (Changes, Test‑Schritte, Überlegungen), kein Draft, keine Reviewer, Merge via Squash.
10. After‑merge: Tag/Release falls nötig, evtl. `CHANGELOG` aktualisieren.

**Relevant files**
- project_templates/cli-basic/docs/index.md.jinja — erweitern/prüfen
- project_templates/cli-basic/docs/README.md.jinja — neu/erweitern
- project_templates/ui-pyside6/src/__init__.py — evtl. Beispiel‑Aufruf referenzieren
- project_templates/ui-pyside6/README.md.jinja oder project_templates/ui-pyside6/docs/* — neu/erweitern
- docs/manual_initialization.md — falls Einträge zur Nutzung der Templates nötig sind
- tests/test_template_renderer.py — prüfen/ergänzen

**Verification**
1. Lokale Renderprüfung: `python -m src.template_python_projekt.render` (sofern Render‑CLI existiert) für betroffene Templates ausführen.
2. Lint: `poetry run ruff check .` → 0 Fehler
3. Typen: `poetry run mypy .` → 0 Errors
4. Pre‑commit: `pre-commit run --all-files` → sauber
5. Tests: `poetry run pytest -q --maxfail=1` → alle Tests grün
6. Manuelle Verifikation: README‑Anweisungen folgen und CLI/UI Demos starten

**Decisions / Annahmen**
- Branchname: `issue/5-34-docs-examples` (von `issue/5`).
- PR erst öffnen wenn alles implementiert und getestet ist. Kein vorzeitiger Draft‑PR.
- Single‑person team → keine Reviewer, PR dennoch mit vollständiger Beschreibung.
- Merge: Squash‑Merge.

**Further Considerations**
1. Sollen die Beispiel‑README Dateien als Jinja Templates in `project_templates/*` gehalten werden (empfohlen), oder als fertige Markdown Dateien? Empfehlung: Jinja, um Variablen/Platzhalter konsistent zu halten.
2. Wenn Packaging‑Schritte projektabhängig sind (poetry vs pip), bitte Kurzvarianten je Template dokumentieren.
3. Wünschst du, dass ich die PR‑Beschreibungsvorlage vorformuliere (ja/nein)?

---
Checkliste (kurz):
- [ ] Branch erstellt
- [ ] Docs für `cli-basic` aktualisiert
- [ ] Docs für `ui-pyside6` aktualisiert
- [ ] Tests angepasst/ausgeführt
- [ ] Lint & mypy grün
- [ ] Pre‑commit sauber
- [ ] Push & PR erstellt (deutscher Titel + ausführliche Beschreibung)
