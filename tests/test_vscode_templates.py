from pathlib import Path
from typing import Any

from template_python_projekt.render import render_template_file


def test_vscode_settings_launch_tasks_render() -> None:
    base = Path("project_templates/common/.vscode")
    settings = base / "settings.json.jinja"
    launch = base / "launch.json.jinja"
    tasks = base / "tasks.json.jinja"

    assert settings.exists()
    assert launch.exists()
    assert tasks.exists()

    ctx: dict[str, Any] = {"module_name": "example_project"}

    for p in (settings, launch, tasks):
        rendered = render_template_file(p, ctx)
        assert "{{" not in rendered and "}}" not in rendered

    rendered_launch = render_template_file(launch, ctx)
    assert "configurations" in rendered_launch

    rendered_tasks = render_template_file(tasks, ctx)
    assert "tasks" in rendered_tasks
