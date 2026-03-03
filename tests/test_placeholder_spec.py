from pathlib import Path

from template_python_projekt.render import render_template_file


def test_placeholder_spec_renders():
    spec = Path("project_templates/common/PLACEHOLDER_SPEC.md.jinja")
    assert spec.exists(), "PLACEHOLDER_SPEC template missing"

    ctx = {"project_name": "example", "project_description": "Desc"}
    rendered = render_template_file(spec, ctx)

    assert "{{" not in rendered and "}}" not in rendered
    assert "Jinja2" in rendered
    # Der Fallback-Renderer kann Platzhalter in Codebeispielen auflösen;
    # akzeptiere entweder den literal-Namen `project_name` oder den ersetzten Wert.
    assert ("project_name" in rendered) or ("example" in rendered)
