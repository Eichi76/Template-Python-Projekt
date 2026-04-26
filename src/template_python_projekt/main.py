"""CLI entrypoint for the Template-Python-Projekt starter script.

This is a minimal CLI skeleton for Sub-Issue #19. It provides the flags
and calls into the renderer API when available.
"""

from __future__ import annotations

import argparse
import sys


# package import (renderer to be implemented in Sub-Issue #20)
try:
    from . import render
except Exception as exc:  # pragma: no cover - renderer may not exist yet
    if isinstance(exc, (ImportError, ModuleNotFoundError)):
        render = None  # type: ignore
    else:
        raise


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="starter")
    p.add_argument("--template", required=True, help="Template name (e.g. cli-basic)")
    p.add_argument("--name", required=True, help="Name of the generated project")
    p.add_argument("--dest", default=".", help="Destination directory")
    p.add_argument("--dry-run", action="store_true", help="Show actions without writing files")
    p.add_argument("--force", action="store_true", help="Overwrite existing files if necessary")
    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    # Basic informational output; real work is delegated to the renderer.
    info = (
        f"starter: template={args.template}, name={args.name}, "
        f"dest={args.dest}, dry_run={args.dry_run}, force={args.force}"
    )
    print(info)

    if render and hasattr(render, "render_project"):
        try:
            render.render_project(
                template_name=args.template,
                project_name=args.name,
                dest=args.dest,
                dry_run=args.dry_run,
                force=args.force,
            )
        except Exception as exc:  # noqa: BLE001 - top-level CLI should report unexpected errors
            print(f"Error: {exc}", file=sys.stderr)
            return 2
        else:
            return 0

    # Renderer not implemented yet — act as a no-op success for dry-run,
    # otherwise inform the user.
    if args.dry_run:
        return 0

    print("Render-Funktion ist noch nicht implementiert. Siehe Sub-Issue #20.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
