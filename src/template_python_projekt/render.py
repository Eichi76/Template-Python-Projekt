"""Ein kleines Rendering-Hilfsmodul für Template-Dokumentation.

Versucht, `jinja2` zu importieren; falls nicht vorhanden, wird ein einfacher
`string.Template`-Fallback verwendet.
"""

from __future__ import annotations

import re
from pathlib import Path
from string import Template
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

    # Fallback: convert Jinja-style `{{ var }}` to string.Template `${var}`
    converted = re.sub(r"\{\{\s*([A-Za-z0-9_]+)\s*\}\}", r"${\1}", text)
    t = Template(converted)
    return t.safe_substitute(**{k: str(v) for k, v in context.items()})
