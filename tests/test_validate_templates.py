from pathlib import Path

from scripts.validate_templates import validate_templates


def test_validate_templates_smoke():
    root = Path("project_templates")
    ctx = {"project_name": "example", "project_description": "Desc", "author": "Me", "license": "MIT"}
    errors = validate_templates(root, ctx)
    # Expect no unresolved placeholders for the repository templates
    assert errors == {}
