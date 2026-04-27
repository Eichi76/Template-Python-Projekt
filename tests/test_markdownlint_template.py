from pathlib import Path
from typing import Any

from template_python_projekt.render import render_template_file


def test_package_and_markdownlint_templates_render() -> None:
    pkg = Path("project_templates/common/package.json.jinja")
    mdcfg = Path("project_templates/common/.markdownlint.json.jinja")

    assert pkg.exists(), "package.json template missing"
    assert mdcfg.exists(), ".markdownlint.json template missing"

    ctx: dict[str, Any] = {"project_name": "example"}
    rendered_pkg = render_template_file(pkg, ctx)
    rendered_cfg = render_template_file(mdcfg, ctx)

    assert "{{" not in rendered_pkg and "}}" not in rendered_pkg
    assert "lint:md" in rendered_pkg
    assert "MD013" in rendered_cfg
