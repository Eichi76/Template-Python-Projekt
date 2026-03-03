"""Ein kleines Rendering-Hilfsmodul für Template-Dokumentation.

Versucht, `jinja2` zu importieren; falls nicht vorhanden, wird ein einfacher
`string.Template`-Fallback verwendet.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any


try:
    import jinja2

    _jinja2: Any | None = jinja2
except ImportError:
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
        r"\{\{\s*(?P<name>[A-Za-z0-9_]+)\s*(?:\|\s*default\((['\"])(?P<default>.*?)\2\)\s*)?\}\}",
    )
    result = pattern.sub(_replace, text)
    # Any remaining simple {{ var }} without default will be replaced by empty string
    return re.sub(r"\{\{\s*[A-Za-z0-9_]+\s*\}\}", "", result)
