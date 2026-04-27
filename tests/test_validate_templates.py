from pathlib import Path
from typing import Any

from scripts.validate_templates import validate_templates


def test_validate_templates_smoke() -> None:
    root = Path("project_templates")
    ctx: dict[str, Any] = {"project_name": "example", "project_description": "Desc", "author": "Me", "license": "MIT"}
    errors = validate_templates(root, ctx)
    # Expect no unresolved placeholders for the repository templates
    assert errors == {}
