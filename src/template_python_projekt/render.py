"""Hilfsfunktionen zum Rendern von Templates im Projekt.

Dieses Modul bevorzugt `jinja2`, wenn es verfügbar ist; andernfalls fällt
es auf ein kleines, gezielt eingeschränktes regexp-basiertes Subset zurück,
das die in unseren Templates verwendeten Muster `{{ var }}` und
`{{ var | default('value') }}` unterstützt.
"""

from __future__ import annotations

import re
import tomllib
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
            out_text = str(template.render(**context))
        except _jinja2.exceptions.TemplateError:
            # Bei Template-Fehlern auf die einfache Fallback-Implementation unten zurückgreifen
            pass
        else:
            # Wenn die Quelldatei mit einem Newline endet, erhalten wir diesen
            # in der gerenderten Ausgabe ebenfalls (Tests erwarten das).
            if text.endswith("\n") and not out_text.endswith("\n"):
                out_text += "\n"
            return out_text

    # Fallback: einfache Jinja2-Ausdrücke aus unseren Templates unterstützen,
    # insbesondere die Muster `{{ var }}` und `{{ var | default('value')}`.
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
    # Verbleibende einfache {{ var }} ohne Default durch leeren String ersetzen
    final = re.sub(r"\{\{\s*[A-Za-z0-9_]+\s*\}\}", "", result)
    if text.endswith("\n") and not final.endswith("\n"):
        final += "\n"
    return final


def render_directory(path: str | Path, context: dict[str, Any]) -> dict[str, str]:
    """Render alle Dateien in *path* und gib ein Mapping von relativen Pfaden -> Inhalt zurück.

    Die Funktion durchläuft *path* rekursiv, rendert jede Datei mit
    :func:`render_template_file` und liefert ein Dictionary, dessen Schlüssel
    POSIX-artige relative Pfade (als Strings) sind und deren Werte die
    gerenderten Dateiinhalte sind.
    """
    root = Path(path)
    if not root.exists():
        msg = f"Pfad existiert nicht: {root}"
        raise FileNotFoundError(msg)

    rendered: dict[str, str] = {}
    for p in sorted(root.rglob("*")):
        if p.is_dir():
            continue
        rel = p.relative_to(root).as_posix()
        rendered[rel] = render_template_file(p, context)
    return rendered


def render_project(
    template_name: str,
    project_name: str,
    dest: str | Path = ".",
    *,
    dry_run: bool = False,
    force: bool = False,
) -> dict[str, str]:
    """Render ein Template-Projekt in *project_templates/<template_name>/src*.

    - Bei *dry_run=True* werden keine Dateien geschrieben; stattdessen wird ein
      Mapping von Zielpfad -> Inhalt zurückgegeben und geplante Aktionen ausgegeben.
    - Falls eine Zieldatei bereits existiert und *force=False*, wird ein
      ``FileExistsError`` mit den konfligierenden Pfaden geworfen.

    Die Funktion entfernt automatisch die Suffix `.jinja` von Ziel-Dateinamen.
    """
    root = Path(__file__).resolve().parents[2]
    template_dir = root / "project_templates" / template_name / "src"
    if not template_dir.exists():
        msg = f"Template not found: {template_dir}"
        raise FileNotFoundError(msg)

    rendered = render_directory(template_dir, {"name": project_name})

    planned: dict[str, str] = {}
    conflicts: list[str] = []
    dest_root = Path(dest) / project_name

    for rel, content in rendered.items():
        target = dest_root / rel
        # Entferne .jinja Suffix falls vorhanden
        if target.suffix == ".jinja":
            target = target.with_suffix("")
        planned[str(target)] = content
        if target.exists() and not force:
            conflicts.append(str(target))

    if conflicts:
        raise FileExistsError("Conflicting files exist: " + ", ".join(conflicts))

    if dry_run:
        for t in planned:
            print("Would write:", t)
        return planned

    # Schreibe die Dateien tatsächlich
    for t, content in planned.items():
        p = Path(t)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")

    return planned


__all__ = ["render_directory", "render_template_file"]


def _merge_dicts(existing: dict[str, Any], template: dict[str, Any]) -> dict[str, Any]:
    """Verschmilzt rekursiv zwei Dictionaries, wobei Werte aus *existing* bevorzugt werden.

    Bei Mapping-Werten wird die Verschmelzung rekursiv angewandt. Bei anderen
    Typen wird der Wert aus *existing* beibehalten, falls vorhanden; sonst
    wird der Wert aus *template* verwendet.
    """
    out: dict[str, Any] = dict(template)
    # Zuerst die Template-Werte übernehmen, danach mit vorhandenen Werten
    # aus `existing` überschreiben bzw. beibehalten

    for key, eval_ in existing.items():
        if key in out and isinstance(out[key], dict) and isinstance(eval_, dict):
            out[key] = _merge_dicts(eval_, out[key])
        else:
            out[key] = eval_

    return out


def merge_toml_strings(existing_toml: str, template_toml: str) -> dict[str, Any]:
    """Parst zwei TOML-Strings und liefert ein gemergtes Mapping zurück.

    Die Funktion gibt eine Python-Struktur zurück, die die zusammengeführte
    TOML-Struktur repräsentiert. Sie versucht bewusst nicht, TOML wieder zu
    serialisieren - Aufrufer können ihre bevorzugte TOML-Bibliothek zum
    Schreiben verwenden.
    """

    existing = tomllib.loads(existing_toml) if existing_toml.strip() else {}
    template = tomllib.loads(template_toml) if template_toml.strip() else {}

    return _merge_dicts(existing, template)
