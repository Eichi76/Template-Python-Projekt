## Plan: Manual Init für Issue #31

TL;DR - Was / Warum / Wie:
Erstelle eine nachvollziehbare, manuelle Anleitung, die das Verhalten des Starterskripts reproduziert (Issue #31). Vorgehen: Sub-Branch vom Parent `issue/5` anlegen, Dokumentation hinzufügen/ändern, Tests prüfen/aktualisieren, Linting/Typing/Pre-commit ausführen, Änderungen committen und am Ende einen PR mit deutschem Titel und ausführlicher Beschreibung öffnen und per Squash-Merge zusammenführen.

**Steps**
1. Branch erstellen (lokal):
   - Auschecken von `issue/5` und neuen Sub‑Branch anlegen: `issue/5-31-manual-init` (Benennung folgt `issue/5-<num>-<short>`). *depends on: aktueller Branch `issue/5` lokal vorhanden*
2. Issue‑Details sichern:
   - Hole den vollständigen Issue‑Text, Akzeptanzkriterien und Kommentare mit `gh issue view 31 --repo Eichi76/Template-Python-Projekt --json body,comments,labels` oder via MCP‑Tools; füge einen Link/Referenz in die neue Dokumentation und in den Commit‑Message/PR‑Beschreibung ein. *parallel mit Step 1*
3. Zielumfang festlegen (Dokumentstruktur):
   - Erstelle neue Datei `docs/manual_initialization.md` als konkrete Empfehlung, oder erweitere [docs/quickstart.md](docs/quickstart.md) / [docs/README.md](docs/README.md) falls Integration bevorzugt wird. Entscheide eine Option zu Beginn.
4. Implementierung der Dokumentation:
   - Beschreibe Schritt‑für‑Schritt die manuelle Reproduktion der Starter‑Skript‑Ausgabe: erwartete Ordner/Dateien, pyproject‑Merges, pre-commit, virtuelle Umgebung, typische Befehle.
   - Ziehe Referenzen aus [project_templates/cli-basic/docs/README.md](project_templates/cli-basic/docs/README.md) und [project_templates/cli-basic/src/main.py](project_templates/cli-basic/src/main.py) heran.
5. Tests prüfen und ggf. anpassen:
   - Führe relevante Tests lokal: `poetry run pytest -q tests/test_template_cli_basic.py tests/test_render_directory.py tests/test_docs_render.py`.
   - Falls Tests fehl schlagen, ergänze Tests oder passe Beispiel‑Outputs in `project_templates` an. *depends on Step 4*
6. Lint/Type/Pre-commit Durchlauf und Fixes:
   - `poetry run ruff check .` → alle Warnungen/Bugs beheben.
   - `poetry run mypy .` → Typfehler beheben (beachte mypy Einstellungen in `pyproject.toml`).
   - `pre-commit` Hooks ausführen und Issues ausgleichen (`poetry run pre-commit run --all-files` oder lokal `pre-commit run --all-files`).
   - Wiederhole bis lints/typing/Pre-commit grün sind.
7. Commits & Commit‑Strategie:
   - Kleine, thematisch geordnete Commits (z. B. `docs: add manual initialization guide`, `tests: add manual init checks`, `fix: ruff/mypy issues`).
   - Nutze aussagekräftige Commit‑Messages; referenziere Issue `#31` in der Nachricht.
8. Push & PR‑Vorbereitung:
   - Push den Branch: `git push -u origin issue/5-31-manual-init`.
   - Erstelle PR erst wenn alle Tasks abgeschlossen. PR darf kein Draft sein.
   - PR‑Titel auf Deutsch, z. B.: "Dokumentation: Manuelle Initialisierung reproduzierbar machen (Issue #31)"
   - PR‑Beschreibung: ausführliche Schritte, betroffene Dateien (Liste), Testanweisungen, Akzeptanzkriterien aus Issue #31, und Hinweis auf `poetry run ruff check .`, `poetry run mypy .`, `poetry run pytest -q` als Verifikation.
9. Merge:
   - Nach Abnahme per Squash‑Merge mergen.
   - Keine weiteren Reviewer nötig (Single‑Person Team) – setze Reviewer optional auf dich selbst.
10. Nacharbeiten:
   - Entferne temporäre Debug‑Änderungen.
   - Ergänze `CHANGELOG.md` falls nötig.

**Relevant files**
- [docs/manual_initialization.md](docs/manual_initialization.md) — neue empfohlene Datei (oder alternativ: Erweiterung von [docs/quickstart.md](docs/quickstart.md)).
- [docs/quickstart.md](docs/quickstart.md) — mögliche Integrationsstelle.
- [docs/README.md](docs/README.md) — übergeordnete Doku‑Referenz.
- [project_templates/cli-basic/docs/README.md](project_templates/cli-basic/docs/README.md) — Template‑Beispiele nutzen.
- [project_templates/cli-basic/src/main.py](project_templates/cli-basic/src/main.py) — Beispielverhalten des Starterskripts.
- [src/template_python_projekt/render.py](src/template_python_projekt/render.py) — relevante Logik/Referenz.
- Tests:
  - [tests/test_template_cli_basic.py](tests/test_template_cli_basic.py)
  - [tests/test_render_directory.py](tests/test_render_directory.py)
  - [tests/test_docs_render.py](tests/test_docs_render.py)

**Verification**
1. Lint/Type/Pre-commit: `poetry run ruff check .`, `poetry run mypy .`, `poetry run pre-commit run --all-files` → keine Warnungen/Fehler.
2. Tests: `poetry run pytest -q --maxfail=1` → alle relevanten Tests grün.
3. Manuelle Prüfung: In einer frischen Umgebung (neues venv) die Schritte aus `docs/manual_initialization.md` durchführen und vergleichen mit Ergebnissen des Starterskripts (Dateien/Ordner/pyproject‑Merges).
4. PR‑Beschreibung enthält Link auf Issue #31 und eine Checkliste der erledigten Acceptance Criteria.

**Decisions / Annahmen**
- Die Anleitung wird als `docs/manual_initialization.md` neu angelegt, sofern nichts anderes gewünscht ist.
- Branchname: `issue/5-31-manual-init` (konform zu `issue/5-<num>-<short>`).
- PR wird nicht als Draft erstellt; Merge per Squash sobald alles erledigt ist.
- Keine weiteren Reviewer nötig (Single‑Person Team).

**Further Considerations / Offene Fragen**
1. Bevorzugst du eine neue Doku‑Datei (`docs/manual_initialization.md`) oder eine Integration in bestehende `docs/quickstart.md`? Empfehlung: neue Datei für bessere Auffindbarkeit.
2. Sollen im Zuge der Dokumentation Beispiel‑Änderungen in `project_templates` (z. B. zusätzliche README‑Beispiele) vorgenommen werden, oder beschränken wir uns nur auf Dokumentation?
3. Möchtest du, dass ich per `gh` CLI den Issue 31 vollständig downloade / verlinke und den Branch lokal anlege/pushe (benötigt Terminalzugriff und konfiguriertes `gh`/Token)?

---
Plan erstellt auf Basis der Repo‑Analyse und der Issue‑Meta‑Daten. Wenn du bestätigst, passe ich den Plan an (z.B. Dateinamen oder PR‑Titel) oder starte die Umsetzungsschritte (Branch anlegen, Dateien erzeugen, Änderungen lokal testen).