from __future__ import annotations

from pathlib import Path

from template_python_projekt.render import render_template_file


def test_render_index_exists_and_renders() -> None:
    path = Path("project_templates/cli-basic/docs/index.md.jinja")
    assert path.exists()
    out = render_template_file(path, {"project_name": "DemoProject", "author": "Tester"})
    assert "DemoProject" in out
    assert "Kurzanleitung" in out
