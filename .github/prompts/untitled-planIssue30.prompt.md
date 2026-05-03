## Plan: Sub-Issue 30 Umsetzung

TL;DR - Was, warum, wie: Implementiere Sub‑Issue #30 auf Basis des Parent‑Branches `issue/5` in einem Sub‑Branch `issue/5-30-cli-docs`. Fokus: Änderungen an CLI‑Doku und zugehörigen Templates/Tests; lokale Verifikation durch `pytest`, `ruff` und `mypy`. PRs werden erst geöffnet wenn die Umsetzung komplett ist; kein Draft, deutscher Titel, ausführliche Beschreibung, Squash‑Merge.

**Issue‑Details (Issue #30)**
- **Titel:** Detaillierte Anleitung: Nutzung des Starterskripts (CLI Optionen & Beispiele)
- **Akzeptanzkriterien:** Alle Flags dokumentiert mit Beispielen und Defaults.
- **Estimate:** 4h
- **Dependencies/Tags:** task-docs-usage
- **Test‑Anweisungen:** Run documented examples and ensure outputs match.
- **Labels:** documentation, task, priority:medium, area:docs
- **Milestone:** Sprint 3
- **Issue‑URL:** https://github.com/Eichi76/Template-Python-Projekt/issues/30

**Steps**
1. Issue‑Details holen (*abhängig von GitHub*):
   - Hole Issue‑Text/Kommentare mit der `gh` CLI: `gh issue view 30 --repo Eichi76/Template-Python-Projekt --json title,body,comments`.
   - Notiere Anforderungen, erwartete Dateien und Akzeptanzkriterien.
2. Lokale Basis vorbereiten:
   - Checkout Parent: `git fetch origin && git checkout issue/5 && git pull --ff-only`.
   - Erstelle Sub‑Branch: `git checkout -b issue/5-30-cli-docs` (Branchname: `issue/5-30-cli-docs`).
3. Analyse & Scope festlegen:
   - Finde relevante Dateien (erste Empfehlung):
     - `src/template_python_projekt/render.py` — Rendering‑Logik prüfen
     - `src/template_python_projekt/main.py` — CLI‑Entry prüfen
     - `project_templates/cli-basic/docs/index.md.jinja` — Doku‑Template
     - `project_templates/cli-basic/src/main.py` — beispielhafte CLI‑Logik
     - Tests: `tests/test_template_cli_basic.py`, `tests/test_render_directory.py`
   - Ergänze die Liste wenn Issue‑Text zusätzliche Dateien nennt.
4. Implementierung (iterativ, Commit‑granular):
   - Kleine, in sich geschlossene Commits pro Änderung (Code, Tests, Templates, Docs).
   - Bei jeder Änderung lokale Prüfungen ausführen (siehe Verifikation).
5. Linting, Typechecking, Pre‑commit vor Push:
   - Lint: `poetry run ruff check .` — alle Warnungen beheben.
   - Typecheck: `poetry run mypy .` — Fehler/Warnungen beheben.
   - Pre‑commit: `pre-commit run --all-files` — Hook‑Warnungen beheben.
6. Tests ausführen:
   - Relevante Tests lokal: `pytest -q tests/test_template_cli_basic.py tests/test_render_directory.py`.
   - Falls neue Tests hinzugefügt: `pytest -q` gesamtes Testsuite.
7. Commit‑Message & Push:
   - Commit‑Message prägnant und Issue referenzierend: `git commit -m "issue/5-30: CLI‑Dokus erweitern — <kurze Beschreibung>"`.
   - Push Branch: `git push --set-upstream origin issue/5-30-cli-docs`.
8. Pull Request (erst wenn Issue fertig):
   - Öffne PR gegen `issue/5`, kein Draft.
   - PR‑Titel (Deutsch): z.B. "Issue 5‑30: CLI‑Dokumentation ergänzen und Templates anpassen".
   - PR‑Beschreibung ausführlich: Hintergrund, gemachte Änderungen, geänderte Dateien, wie man lokal testet, Checkliste (Lints, Typchecks, Tests), evtl. Screenshots/Beispiele.
   - Keine Reviewer (single‑person Team). Markiere ggf. CI/Checks als bestanden.
9. Merge (nach Abnahme durch dich selbst):
   - Verwende `Squash and merge` über GitHub UI.
   - Merge‑Commit Nachricht: deutsche Zusammenfassung + Referenz auf Issue #30.
10. Nacharbeiten:
   - `git checkout issue/5 && git pull` und `git branch -d issue/5-30-cli-docs` lokal löschen.
   - Falls nötig: Release/Changelog aktualisieren.

**Relevant files**
- `src/template_python_projekt/render.py` — Rendering‑Logik prüfen/erweitern
- `src/template_python_projekt/main.py` — CLI‑Entry/Argumente
- `project_templates/cli-basic/docs/index.md.jinja` — Doku‑Template anpassen
- `project_templates/cli-basic/src/main.py` — CLI‑Beispielcode
- `tests/test_template_cli_basic.py` — CLI‑Template Tests
- `tests/test_render_directory.py` — Rendering Tests
- `.github/prompts/plan-parentIssueFive.prompt.md` — Branch/Issue‑Konventionen referenzieren
- `pyproject.toml` — Linter/Typecheck Konfiguration
- `.pre-commit-config.yaml` — Pre‑commit Hooks

**Verification**
1. Lint & Typecheck: `poetry run ruff check .` → keine Warnungen; `poetry run mypy .` → keine Fehler.
2. Pre‑commit Hooks: `pre-commit run --all-files` → alle Hooks erfolgreich.
3. Tests: `pytest -q` → alle Tests grün; insbesondere `tests/test_template_cli_basic.py` und `tests/test_render_directory.py`.
4. Manuelle Prüfung: Rendered docs prüfen (z. B. lokal generierte Dateien öffnen), CLI‑Beispiel durchlaufen.
5. PR‑Verifikation: GitHub Checks (CI) grün, keine Lint/Type‑Failures in CI.

**Decisions / Annahmen**
- Branchname: `issue/5-30-cli-docs` (Nummer 30, kurzer beschreibender Suffix "cli-docs").
- Basis-Branch: `issue/5` (nicht `main`).
- Keine Draft‑PRs und keine Reviewer (Single‑Person Team).
- Merge‑Strategie: `Squash and merge`.
- GitHub Issue‑Details können via `gh` CLI oder MCP abgerufen werden (Token in Powershell env).

**Further Considerations**
1. Falls Issue‑Text weitere Dateien/Module nennt, erweitere Step 3 entsprechend.
2. Wenn Änderungen am API‑Shape nötig sind, ergänze Typannotationen und erweitere Tests.
3. Wenn CI zusätzliche Checks hat, führe diese lokal nach Möglichkeit aus (z. B. `isort`, `black` falls konfiguriert).

**Detaillierte TODO‑Liste & Workflow (ausführlich)**

1) Vorbereitung (10–15min)
- Sicherstellen, dass lokales `issue/5` aktuell ist: `git fetch origin` -> `git checkout issue/5` -> `git pull --ff-only origin issue/5`.
- Sub‑Branch erstellen (Konvention): `git checkout -b issue/5-30-cli-docs`.
- Notiere Issue‑Akzeptanzkriterien lokal in einer kurzen TODO‑Datei (z. B. `docs/.issue-30-scope.md`).

2) Discovery: gezielte Dateiuntersuchung (15–30min)
- Prüfe `src/template_python_projekt/main.py` auf CLI‑Flags/Argumente.
- Prüfe `src/template_python_projekt/render.py` auf Template‑Platzhalter, die Doku‑Ausgabe beeinflussen.
- Öffne `project_templates/cli-basic/docs/index.md.jinja` und `project_templates/cli-basic/src/main.py` auf Beispiel‑Dokumentation und Beispiele.
- Notiere fehlende Beispiele/Defaults und markiere Stellen zum Ergänzen.

3) Änderungen planen (5–10min)
- Lege feste Arbeitspakete (A–D):
  A) Dokumentationstexte & Beispiele in `project_templates/cli-basic/docs/index.md.jinja` ergänzen.
  B) Falls CLI‑Flags fehlen oder unklar sind: `src/template_python_projekt/main.py` kommentieren/ergänzen (help text, defaults).
  C) Tests: Ergänze/aktualisiere `tests/test_template_cli_basic.py` mit Szenarien für dokumentierte Beispiele.
  D) Render‑Verifikation: ggf. kleine Testfälle in `tests/test_render_directory.py` hinzufügen.

4) Umsetzung (iterativ, je Arbeitspaket)
- Für jedes Arbeitspaket:
  - Erstelle lokalen Commit mit sinnvoller Message: `issue/5-30: [A] Kurze Beschreibung`.
  - Führe Lint & Typecheck lokal: `poetry run ruff check .` und `poetry run mypy .` und behebe Warnungen.
  - Führe relevante Tests aus: `pytest -q tests/test_template_cli_basic.py` (oder gesamte Suite wenn nötig).
  - Pre‑commit Hooks prüfen: `pre-commit run --all-files`.
  - Push: `git push --set-upstream origin issue/5-30-cli-docs` (erst nachdem mehrere Commits fertig sind oder am Ende der Arbeit).

5) Tests & Verifikation (kontinuierlich)
- Vor PR: Alle Tests lokal grün: `pytest -q`.
- Lint/Typecheck sauber: `poetry run ruff check .` → 0 Warnungen; `poetry run mypy .` → 0 Fehler.
- Pre‑commit Hooks ohne Fehler: `pre-commit run --all-files`.
- Manuelle Ausführung der dokumentierten Beispiele: Starterskript mit dokumentierten Flags laufen lassen und Ausgabe vergleichen (siehe Issue „Test Commands"). Notiere Ergebnisse in `docs/.issue-30-test-results.md`.

6) PR‑Vorbereitung (abschließend)
- PR öffnen erst wenn alle Tasks abgeschlossen.
- PR‑Branch: `issue/5-30-cli-docs` → Target: `issue/5`.
- PR‑Titel (Deutsch, Beispiel): `Issue 5‑30: Detaillierte Anleitung zur Nutzung des Starterskripts (CLI‑Optionen & Beispiele)`.
- PR‑Beschreibung (ausführlich; Punkte):
  - Kurzbeschreibung & Hintergrund.
  - Erfüllte Akzeptanzkriterien (Liste, Häkchen für abgeschlossen).
  - Änderungen (Dateiliste mit Pfaden).
  - Wie lokal testen (Kurzbefehle & erwartete Ausgaben).
  - Lint/Typecheck/Tests Status (ergebnisbasiert).
  - Hinweise für Maintainer (falls relevant).
- Merge‑Strategie: `Squash and merge` über GitHub UI.

7) Commit‑/Branch‑Konventionen
- Branchname: `issue/5-30-cli-docs`.
- Commit‑Prefix: `issue/5-30:` gefolgt von kurzen deutschen Beschreibungen.
- Keine Draft‑PRs; PRs erst bei kompletter Umsetzung.

8) Post‑Merge
- Lokal: `git checkout issue/5 && git pull`.
- Optional: `git branch -d issue/5-30-cli-docs`.
- Aktualisiere ggf. `CHANGELOG.md` oder `docs/README.md` falls Dokumentation eine sichtbare Änderung für Nutzer darstellt.

**Konkrete Dateiaufgaben (checkbare ToDos)**n- [ ] A. `project_templates/cli-basic/docs/index.md.jinja`: Für jedes CLI‑Flag: Beschreibung, Default, Beispielaufruf, erwartete Ausgabe.
- [ ] B. `src/template_python_projekt/main.py`: Kanalisiere oder erweitere `--help`/Docstrings falls notwendig.
- [ ] C. `src/template_python_projekt/render.py`: Sicherstellen, dass die Doku‑Platzhalter korrekt gerendert werden (z. B. Defaults eingefügt).
- [ ] D. `tests/test_template_cli_basic.py`: Neue Tests für die dokumentierten Beispiele hinzufügen (Mocks/fixtures verwenden falls nötig).
- [ ] E. `tests/test_render_directory.py`: Falls Rendering‑Änderungen, ergänzende Tests.
- [ ] F. Dokumentations‑Artefakte: `docs/.issue-30-scope.md`, `docs/.issue-30-test-results.md`.

**PR‑Beschreibung Vorlage (Deutsch, kopierbar)**
Titel: Issue 5‑30: Detaillierte Anleitung zur Nutzung des Starterskripts (CLI‑Optionen & Beispiele)

Beschreibung:
- Zusammenfassung: Erweiterte Dokumentation des Starterskripts, Beschreibungen aller CLI‑Flags, Defaults und Anwendungsbeispiele.
- Erfüllte Akzeptanzkriterien:
  - [x] Alle Flags dokumentiert
  - [x] Beispiele mit erwarteter Ausgabe
- Änderungen (kurz):
  - `project_templates/cli-basic/docs/index.md.jinja` — Ergänzte Flag‑Beschreibungen und Beispiele
  - `tests/test_template_cli_basic.py` — Neue Tests für Beispiele
- Lokales Testen:
  - `poetry run pytest -q tests/test_template_cli_basic.py`
  - `poetry run ruff check .` und `poetry run mypy .`
  - Manuelle Ausführung: `python -m template_python_projekt --help` (oder `python -m template_python_projekt.cli` je nach Entry)
- Hinweise:
  - Single‑person Team: keine Reviewer nötig.
  - Merge: Squash‑Merge.

**Risiken & Mitigations**
- Risiko: Unklare Flags in Code → Prüfung: `main.py` und Unit‑Tests erweitern.
- Risiko: Template‑Placeholder fehlen → Anpassung in `render.py` und Ergänzung von Integrations‑Tests.
- Mitigation: Kleine, verifizierbare Commits + Tests pro Änderungspaket.

**Zeitschätzung**
- Total: ~4h (Issue Estimate) verteilt auf: Discovery 30min, Implementierung 2–2.5h, Tests/PR 30–60min.
