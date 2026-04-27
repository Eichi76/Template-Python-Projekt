Finaler Merge: `issue/4` → `main`

Zusammenfassung
--------------
Dieser PR fasst alle abgeschlossenen Sub‑Issues (#19–#28) zusammen und bereitet
den finalen Merge von `issue/4` in `main` vor.

Enthaltene Änderungen (Auszug)
-----------------------------
- Atomare Writes, Backup & Rollback im Template Renderer (`render.py`)
- CI Workflow für Tests/Lint (`.github/workflows/ci.yml`)
- Ausführliche Dokumentation (`docs/README.md`)

Checks (bereits lokal ausgeführt)
--------------------------------
- `poetry run ruff check .` — Passed
- `poetry run mypy .` — Passed
- `poetry run pytest -q` — All tests passed
- `poetry run pre-commit run --all-files` — All hooks passed

Merge‑Vorgaben
---------------
- Ziel: `main` (finaler Merge)
- Merge‑Methode: `squash and merge`
- Branches: `issue/4` kann nach Merge gelöscht werden

Bitte Review und dann Merge durchführen.
