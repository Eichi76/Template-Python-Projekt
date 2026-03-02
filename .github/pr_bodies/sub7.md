Fügt Beispiel‑Dokumentations‑Templates und einen kleinen Renderer hinzu.

Änderungen:
- `project_templates/cli-basic/docs/index.md.jinja` (Beispiel‑Jinja‑Template)
- `project_templates/cli-basic/docs/README.md` (Dokumentation zum Rendering)
- `src/template_python_projekt/render.py` (Renderer mit `jinja2`‑Support und Fallback)
- `tests/test_docs_render.py` (Unit‑Test für Rendering)

Bezieht sich auf: #7

Checklist:
- [x] Tests hinzugefügt und lokal grün
- [x] Lint & mypy lokal grün
- [ ] README bei Bedarf erweitern

Testschritte (lokal):

```bash
poetry run pytest tests/test_docs_render.py -q
python -c "from template_python_projekt.render import render_template_file; print(render_template_file('project_templates/cli-basic/docs/index.md.jinja', {'project_name':'Demo','author':'X'}))"
```
