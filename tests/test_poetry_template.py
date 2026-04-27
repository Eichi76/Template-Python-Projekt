from pathlib import Path
from typing import Any

from template_python_projekt.render import render_template_file


def test_poetry_template_renders() -> None:
    tpl = Path("project_templates/common/poetry.toml.jinja")
    assert tpl.exists(), "poetry.toml template missing"

    ctx: dict[str, Any] = {"virtualenvs_in_project": "true"}
    rendered = render_template_file(tpl, ctx)

    assert "{{" not in rendered and "}}" not in rendered
    assert "virtualenvs" in rendered
    assert "in-project" in rendered
