from __future__ import annotations

import argparse
from pathlib import Path

from template_python_projekt.render import render_directory


def validate_templates(templates_root: Path, context: dict) -> dict[str, list[str]]:
    """Validate templates under `templates_root`.

    Returns a mapping from template name -> list of error messages. An empty
    mapping entry or empty list means no errors for that template.
    """
    templates_root = Path(templates_root)
    if not templates_root.exists():
        msg = f"templates_root does not exist: {templates_root}"
        raise FileNotFoundError(msg)

    errors: dict[str, list[str]] = {}
    for tpl in sorted(templates_root.iterdir()):
        if not tpl.exists():
            continue
        # render all files in this template folder
        rendered = render_directory(tpl, context)

        tpl_errors: list[str] = []
        for rel, content in rendered.items():
            if "{{" in content or "}}" in content:
                tpl_errors.append(f"unresolved placeholder in {rel}")
        if tpl_errors:
            errors[tpl.name] = tpl_errors

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate project_templates rendering")
    parser.add_argument("templates_root", nargs="?", default="project_templates")
    args = parser.parse_args(argv)

    ctx = {
        "project_name": "example",
        "project_description": "Example project",
        "author": "Example",
        "license": "MIT",
    }

    errors = validate_templates(Path(args.templates_root), ctx)
    if errors:
        for tpl, errs in errors.items():
            print(f"Template: {tpl}")
            for e in errs:
                print("  - ", e)
        return 2

    print("All templates rendered without unresolved placeholders.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
