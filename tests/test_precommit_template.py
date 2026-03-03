from pathlib import Path

from template_python_projekt.render import render_template_file


def test_precommit_template_renders_and_contains_hooks() -> None:
    template_path = Path("project_templates/common/.pre-commit-config.yaml.jinja")
    assert template_path.exists(), f"Template not found: {template_path}"

    context = {
        "ruff_rev": "v0.31.0",
        "isort_rev": "5.12.0",
        "mypy_rev": "1.0.0",
    }

    rendered = render_template_file(template_path, context)

    # ensure no unresolved placeholders remain
    assert "{{" not in rendered and "}}" not in rendered

    # basic smoke checks for expected content
    assert "repos:" in rendered
    assert "ruff" in rendered or "isort" in rendered
