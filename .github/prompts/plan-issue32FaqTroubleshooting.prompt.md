## Plan: Issue #32 umsetzen (FAQ / Troubleshooting)

TL;DR: Erstelle eine Troubleshooting‑/FAQ‑Seite mit den Top‑10-Warnfällen (poetry/node/pre-commit/merge conflicts etc.), verlinke sie in der Dokumentation, füge einen simplen Test hinzu, arbeite auf einem Sub‑Branch von `issue/5` und schließe mit einer deutschen PR‑Beschreibung und Squash‑Merge ab.

**Akzeptanzkriterien (aus Issue #32)**
- FAQ deckt mindestens die Top‑10 wahrscheinlichen Fehler ab (z. B. `poetry` fehlt, `node` fehlt, `pre-commit` schlägt fehl, Merge‑Konflikte).
- Dokument ist in `docs/` verfügbar und von der `docs/README.md` referenziert.

**Steps (detailliert)**
1. Issue‑Kontext bestätigen (bereits abgerufen)
   - Issue: "Troubleshooting & FAQ für häufige Probleme" (Estimate: 4h).
   - Acceptance Criteria beachten: Top‑10 Fälle dokumentieren.

2. Sub‑Branch erstellen (vom Parent `issue/5`)
   - Fetch & Checkout:

```bash
git fetch origin
git checkout origin/issue/5 -b issue/5-32-faq-troubleshooting
```

   - Push erst, wenn du bereit bist zu teilen (`git push -u origin issue/5-32-faq-troubleshooting`).

3. Struktur & Inhalte erstellen
   - Neue Datei: `docs/troubleshooting.md` (oder `docs/faq.md`). Inhalt:
     - Kurzbeschreibung / Zweck
     - Top‑10 Fehler (je Abschnitt: Symptom, Ursache, Lösung/Workaround, relevante Befehle)
     - Hinweise zu Debugging (Logs, `--verbose` flags, typische Pfade)
     - Verweise auf `pyproject.toml`, `pre-commit`, `poetry`, `node`, und Git‑Merge Tipps
   - Update: `docs/README.md` → Link / Abschnitt "Troubleshooting / FAQ".
   - Optional: `README.md` Kurzverweis (wenn sinnvoll).

4. Tests hinzufügen
   - Neuer Test: `tests/test_troubleshooting_doc.py` mit einfachen Checks:
     - Datei `docs/troubleshooting.md` existiert
     - Enthält Headings/Keywords (`poetry`, `node`, `pre-commit`, `merge`) — einfache substring asserts
   - Beispiel (pytest): prüfe `Path('docs/troubleshooting.md').read_text()` enthält erwartete Strings.

5. Lokale Validierung & Qualitätssicherung
   - Markdown sanity: `markdownlint` falls vorhanden (repo hat `test_markdownlint_template.py`).
   - Lint & Typecheck für den Code (nicht für docs):

```bash
poetry run ruff check .
poetry run mypy .
```

   - Tests ausführen:

```bash
pytest -q --cov=src --cov-report=xml
```

   - Pre‑commit Hooks:

```bash
pre-commit run --all-files
```

   - Behebe auftretende Warnungen/Fehler bevor commit/push.

6. Commits & Commit‑Konvention
   - Kleine, thematische Commits (z. B. `docs: add troubleshooting/faq skeleton`, `docs: add node/poetry preflight steps`, `tests: add doc presence tests`).
   - Achte auf pre-commit Auto‑Fixes; passe Commit‑Messages an falls Hooks fehlschlagen.

7. PR Erstellung (erst nach Abschluss aller Checks)
   - PR nicht als Draft.
   - Deutscher Titel, z. B.: `Docs: Issue #32 – Troubleshooting & FAQ für häufige Probleme`
   - Ausführliche PR‑Beschreibung (Deutsch):
     - Kurzfassung der Änderungen
     - Vollständige Liste der Top‑10 Fehler, die dokumentiert wurden
     - Verlinkte Dateien: `docs/troubleshooting.md`, `docs/README.md`, evtl. `README.md`
     - Test‑Summary (neue Tests, Befehle zum Ausführen)
     - Hinweise: Lint/MyPy/Pre‑commit Status
   - PR erstellen mit `gh`:

```bash
gh pr create --base main --head issue/5-32-faq-troubleshooting --title "Docs: Issue #32 – Troubleshooting & FAQ für häufige Probleme" --body "<ausführliche Beschreibung in Deutsch>"
```

   - Keine Reviewer required (Single‑Person Team). Tags/Milestone setzen falls gewünscht.

8. Merge & Cleanup
   - Nach finaler Prüfung Squash‑Merge.
   - Beispiel mit `gh`:

```bash
gh pr merge <PR_NUMBER> --squash --delete-branch
```

   - Lokal aufräumen: `git checkout issue/5` ; `git branch -D issue/5-32-faq-troubleshooting`.

**Relevante Dateien / Stellen**
- `docs/troubleshooting.md` — neu: die FAQ/ Troubleshooting Seite
- `docs/README.md` — Link/Navigation aktualisieren
- `README.md` — optionaler Kurzverweis
- Tests: `tests/test_troubleshooting_doc.py` — neuer Test
- `pyproject.toml` — zeigt Linting/Typechecker Befehle (siehe `dependency-groups`)

**Verification (konkret)**
1. Datei vorhanden: `tests/test_troubleshooting_doc.py` besteht und `pytest -q` läuft durch
2. Inhalte: `docs/troubleshooting.md` enthält die Schlüsselwörter `poetry`, `node`, `pre-commit`, `merge`
3. Lint/MyPy: `poetry run ruff check .` und `poetry run mypy .` ohne neue Warnungen (für Code)
4. Pre-commit: `pre-commit run --all-files` → alle Hooks grün
5. PR‑Beschreibung auf Deutsch, inkl. How‑to‑verify-Anleitung

**Aufwandsabschätzung**
- Gemäß Issue: ~4 Stunden (Erfassen der Top‑10, Schreiben der Abschnitte, Tests, PR‑Erstellung)

**Entscheidungen / Annahmen**
- Dokumentation in `docs/` ist ausreichend; kein neues CLI‑Feature notwendig.
- Tests prüfen grundlegende Präsenz und Schlüsselwörter, keine semantische Validierung der Lösungen.
- PRs werden erst erstellt, wenn alle lokalen Checks bestanden sind.

**Nächste Schritte (Empfohlen)**
1. Bestätige, dass ich die Datei `docs/troubleshooting.md` anlegen soll (ich kann sie scaffolden).
2. Wenn ja: Soll ich direkt ein erstes Commit/Branch erstellen oder möchtest du lokal prüfen bevor Push/PR?
