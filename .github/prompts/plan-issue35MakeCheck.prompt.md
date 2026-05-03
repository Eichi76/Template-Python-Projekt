## Plan: Issue #35 — "make check" Validierungsziel

TL;DR: Implementiere ein `make check` Ziel (oder äquivalentes Script) im Repo-Root, das nacheinander `poetry env check`, `pytest -q`, `pre-commit run --all-files` und optional `npm run lint:md` ausführt. Erzeuge einen Sub-Branch von `issue/5` namens `issue/5-35-make-check`. Verifiziere lokal Linting (`poetry run ruff check .`), Typprüfung (`poetry run mypy .`) und Pre-commit-Hooks; behebe Warnungen; öffne erst nach vollständiger Implementierung einen PR mit deutschem Titel und ausführlicher Beschreibung; merge per Squash.

**Schritte**
1. Vorbereitung
- Lokales Repo auf aktuellen `issue/5` bringen: `git fetch && git checkout issue/5 && git pull`.
- Erstelle Sub-Branch: `git checkout -b issue/5-35-make-check` (*depends on step 1*).

2. Implementieren: `make check`
- Im Repo-Root eine `Makefile` (oder `scripts/check.sh` + `Makefile`-Target) hinzufügen/erweitern.
- Implementiere Target `check` mit folgenden Schritten in dieser Reihenfolge:
  - `poetry env check` (prüft Poetry/Environment)
  - `poetry run pytest -q` (Tests)
  - `pre-commit run --all-files`
  - Optional: `npm run lint:md` (nur wenn `package.json` / node‑Linter für Markdown vorhanden)
- Stelle sicher, dass jedes Kommando bei Fehler non-zero zurückgibt, damit `make check` bei Fehlern stoppt.

3. Tests & Anpassungen
- Falls Tests fehlschlagen: Tests anpassen oder Issue spezifisch fixen (Tests müssen grün laufen).
- Falls Pre-commit-Hooks Warnungen ausgeben: Code gemäß Hooks anpassen (Automatisieren, falls möglich).
- Falls `npm run lint:md` in `project_templates/common` oder Root nicht existiert: dokumentiere optionales Flag oder skip mit Info im Makefile.

4. Linting & Typing
- Führe `poetry run ruff check .` aus und behebe Warnungen.
- Führe `poetry run mypy .` aus und behebe Typfehler/Unannotated-Defs.
- Achte auf `pyproject.toml` mypy/ruff Einstellungen (z. B. `line-length`, `disallow_untyped_defs`).

5. Commit, Pre-commit & Push
- Committe Änderungen atomar, mit klaren Messages (z. B. `Add make check target + docs`).
- Führe `pre-commit run --all-files` lokal; behebe verbleibende Issues.
- Push Branch: `git push --set-upstream origin issue/5-35-make-check`.

6. Pull Request
- Öffne PR gegen `issue/5` (NOT gegen `main`).
- PR-Regeln: kein Draft-PRs; erst öffnen, wenn alles implementiert und alle Checks grün.
- PR-Namen (Deutsch): `Issue #35: "make check" Ziel hinzufügen — Validierungs-Workflow`.
- PR-Beschreibung: ausführliche deutsche Beschreibung mit
  - Kontext (Issue #35 verlinken)
  - Was geändert wurde (Makefile, evtl. scripts, Tests, docs)
  - Wie lokal geprüft (Befehle und erwartetes Verhalten)
  - Acceptance Criteria / Checkliste (als ToDo-Liste) mit Haken
  - Hinweis: Merge-Strategie: Squash-Merge; keine Reviewer erforderlich (single-person team)

7. Merge & Aufräumen
- Nach finaler Verifikation: Squash-Merge PR in `issue/5`.
- Lokales Aufräumen: `git checkout issue/5 && git pull` und `git branch -d issue/5-35-make-check` und `git push origin --delete issue/5-35-make-check` (optional).

**Relevante Dateien / Orte zum Anpassen**
- `Makefile` (neu/erweitern) — Root
- `scripts/check.sh` (optional) — Root
- `pyproject.toml` — (prüfen / dokumentieren) Root
- `src/template_python_projekt/__main__.py` oder `main.py` — nur falls CLI-Entrypoints angepasst werden sollen
- `project_templates/common/package.json.jinja` oder `project_templates/*/package.json.jinja` — falls `npm run lint:md` referenziert werden soll
- `.pre-commit-config` oder `pyproject.toml` (pre-commit hooks) — sicherstellen, dass Hooks vorhanden und dokumentiert sind
- `tests/` — ggf. neue Tests oder Anpassungen

**Verification (konkrete Befehle, in Backticks)**
- `git checkout issue/5 && git pull`
- `git checkout -b issue/5-35-make-check`
- `make check` → gesamter Workflow muss erfolgreich durchlaufen
- `poetry run ruff check .` → keine Warnungen
- `poetry run mypy .` → keine Fehler
- `poetry run pytest -q` → alle Tests grün
- `pre-commit run --all-files` → keine Fehler

**PR-Vorlage (Deutsch)**
- Titel: `Issue #35: "make check" Ziel hinzufügen — Validierungs-Workflow`
- Beschreibung:
  - Kurzbeschreibung des Problems und weshalb `make check` nötig ist.
  - Liste der durchgeführten Änderungen (Dateipfade).
  - Anleitung zur lokalen Prüfung (s. Verification-Befehle).
  - Acceptance-Criteria (Checkboxen):
    - [ ] `make check` führt `poetry env check` aus
    - [ ] `make check` führt `pytest -q` aus
    - [ ] `make check` führt `pre-commit run --all-files` aus
    - [ ] Optional: `npm run lint:md` ausgeführt oder dokumentiert
  - Merge-Hinweis: Squash‑Merge, kein externer Reviewer benötigt.

**Entscheidungen & Annahmen**
- Branch von `issue/5` erstellen (wie gefordert).
- Branch-Name: `issue/5-35-make-check` (Nummer = Issue Nummer 35, Kurz = `make-check`).
- Keine Draft-PRs; PR erst öffnen, wenn alle Checks grün sind.
- Single-person team → keine Reviewer, PR trotzdem mit ausführlicher Beschreibung.
- `npm run lint:md` ist optional und nur aktiviert, wenn `package.json` bzw. Linter konfiguriert ist.

**Weiteres / Offene Fragen**
1. Soll `make check` zwingend `npm run lint:md` ausführen, oder soll das optional/conditional sein? Empfehlung: optional aufgrund heterogener Repos.
2. Möchtest du ein separates `scripts/check.sh`-Script, das von `Makefile` aufgerufen wird (besser für Windows/PowerShell-Kompatibilität), oder reicht ein reines `Makefile`-Target? Empfehlung: beides — `Makefile` ruft `scripts/check.ps1`/`scripts/check.sh` je nach Plattform.

Speichere ich diesen Plan jetzt in `/memories/session/plan.md` (geschehen). Möchtest du, dass ich jetzt das `Makefile`-Patch vorschlage und die Änderungen in einem Branch implementiere (nur Planmodus: ich kann den nächsten Schritt planen oder, mit Freigabe, implementieren)?
