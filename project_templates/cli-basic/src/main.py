"""Minimal CLI entrypoint for cli-basic template."""

from __future__ import annotations

import argparse


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cli-basic",
        description="CLI demo for cli-basic template",
    )
    parser.add_argument("--version", action="version", version="0.1.0")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = create_parser()
    _ = parser.parse_args(argv)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
