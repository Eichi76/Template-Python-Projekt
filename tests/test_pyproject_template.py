import tomllib
from pathlib import Path

from template_python_projekt.render import render_template_file


def test_pyproject_template_renders_and_parses(tmp_path: Path) -> None:
    template_path = Path("project_templates/common/pyproject.toml.jinja")
    assert template_path.exists(), f"Template not found: {template_path}"

    context = {
        "project_name": "example_project",
        "description": "Eine Beispielbeschreibung",
        "author": "Test Autor <test@example.com>",
        "license": "MIT",
    }

    rendered = render_template_file(template_path, context)

    # ensure no unresolved placeholders remain
    assert "{{" not in rendered and "}}" not in rendered

    # write to temporary file and parse with tomllib
    out_file = tmp_path / "pyproject.toml"
    out_file.write_text(rendered, encoding="utf-8")

    parsed = tomllib.loads(out_file.read_text(encoding="utf-8"))
    assert parsed.get("tool", {}).get("poetry", {}).get("name") == "example_project"
