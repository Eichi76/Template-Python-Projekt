"""Rendering helpers for templates used in the project.

This module prefers `jinja2` when available; otherwise it falls back to a
small, well-scoped regexp-based subset to support common `{{ var }}` and
`{{ var | default('value') }}` patterns used in the templates.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any


try:
    import jinja2

    _jinja2: Any | None = jinja2
except ImportError:  # pragma: no cover - import fallback
    _jinja2 = None


def render_template_file(path: str | Path, context: dict[str, Any]) -> str:
    path = Path(path)
    text = path.read_text(encoding="utf-8")

    if _jinja2 is not None:
        try:
            env = _jinja2.Environment(
                loader=_jinja2.FileSystemLoader(path.parent),
                autoescape=_jinja2.select_autoescape(),
            )
            template = env.get_template(path.name)
            return str(template.render(**context))
        except _jinja2.exceptions.TemplateError:
            # fall back to the simple fallback below
            pass

    # Fallback: support simple Jinja2 expressions used in our templates,
    # especially `{{ var }}` and `{{ var | default('value') }}` patterns.
    def _replace(match: re.Match[str]) -> str:
        name = match.group("name")
        default = match.group("default")
        if name in context and context[name] is not None:
            return str(context[name])
        if default is not None:
            return default
        return ""

    pattern: re.Pattern[str] = re.compile(
        r"\{\{\s*(?P<name>[A-Za-z0-9_]+)\s*(?:\|\s*default\((['\"]) (?P<default>.*?)\2\)\s*)?\}\}",
    )
    result = pattern.sub(_replace, text)
    # Any remaining simple {{ var }} without default will be replaced by empty string
    return re.sub(r"\{\{\s*[A-Za-z0-9_]+\s*\}\}", "", result)


def render_directory(path: str | Path, context: dict[str, Any]) -> dict[str, str]:
    """Render all files in *path* and return a mapping of relative paths -> content.

    The function walks *path* recursively, renders each file using
    :func:`render_template_file` and returns a dictionary where keys are
    POSIX-style relative paths (as strings) and values are the rendered file
    contents.
    """
    root = Path(path)
    if not root.exists():
        msg = f"Path does not exist: {root}"
        raise FileNotFoundError(msg)

    rendered: dict[str, str] = {}
    for p in sorted(root.rglob("*")):
        if p.is_dir():
            continue
        rel = p.relative_to(root).as_posix()
        rendered[rel] = render_template_file(p, context)
    return rendered


__all__ = ["render_directory", "render_template_file"]
