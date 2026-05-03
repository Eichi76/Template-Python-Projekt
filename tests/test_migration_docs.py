from pathlib import Path

import pytest


def test_migration_docs_content() -> None:
    """Validate that the migration docs contain key sections and commands."""
    p = Path("docs") / "migration_and_updates.md"
    assert p.exists(), "docs/migration_and_updates.md must exist"
    content = p.read_text(encoding="utf-8")
    assert "## Schnell-Checkliste" in content
    assert "poetry run pytest -q" in content
    assert "--update-mode" in content or "update-mode" in content
