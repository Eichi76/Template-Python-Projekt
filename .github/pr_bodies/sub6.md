Implementiert das MVC‑Skelett für die Templates `cli-basic` und `ui-pyside6`.

Änderungen:
- `project_templates/cli-basic/src/` mit `__init__.py`, `model/`, `view/`, `controller/`, `main.py`
- `project_templates/ui-pyside6/src/` mit `__init__.py`, `model/`, `view/`, `controller/`, `main.py`
- `tests/test_template_cli_basic.py`

Bezieht sich auf: #6

Checklist:
- [x] Tests hinzugefügt (lokal: 1 passed)
- [x] Lint & mypy lokal grün (pre-commit ausgeführt)
- [ ] README aktualisiert (falls nötig)

Testschritte (lokal):

```bash
python project_templates/cli-basic/src/main.py --help
poetry run pytest -q
```
