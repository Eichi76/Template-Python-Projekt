from pathlib import Path

from template_python_projekt.render import render_template_file


def test_readme_and_changelog_templates_render():
    readme = Path("project_templates/common/README.md.jinja")
    changelog = Path("project_templates/common/CHANGELOG.md.jinja")

    assert readme.exists(), "README template missing"
    assert changelog.exists(), "CHANGELOG template missing"

    ctx = {"project_name": "example_project", "project_description": "Beschreibung"}
    rendered_readme = render_template_file(readme, ctx)
    rendered_changelog = render_template_file(changelog, ctx)

    assert "{{" not in rendered_readme and "}}" not in rendered_readme
    assert "example_project" in rendered_readme
    assert "Unreleased" in rendered_changelog
