from pathlib import Path
from typing import Any

from template_python_projekt.render import render_template_file


def test_editorconfig_and_gitignore_render() -> None:
    editor = Path("project_templates/common/.editorconfig.jinja")
    gitignore = Path("project_templates/common/.gitignore.jinja")

    assert editor.exists(), ".editorconfig template missing"
    assert gitignore.exists(), ".gitignore template missing"

    ctx: dict[str, Any] = {}
    ed = render_template_file(editor, ctx)
    gi = render_template_file(gitignore, ctx)

    assert "{{" not in ed and "}}" not in ed
    assert "__pycache__" in gi
    assert "venv/" in gi or ".venv/" in gi
