from pathlib import Path

from template_python_projekt import render


def _read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def test_render_update_mode_skip_overwrite_and_backup(tmp_path):
    # Prepare an existing project file that would conflict with template
    project_name = "projx"
    dest = tmp_path
    dest_root = dest / project_name
    dest_root.mkdir(parents=True)
    target_file = dest_root / "main.py"
    target_file.write_text("# ORIGINAL\n", encoding="utf-8")

    # Ensure skip keeps original content
    render.render_project("cli-basic", project_name, dest, dry_run=False, update_mode="skip")
    assert _read(target_file).startswith("# ORIGINAL")

    # Overwrite replaces content with template content
    render.render_project("cli-basic", project_name, dest, dry_run=False, update_mode="overwrite")
    content_after_overwrite = _read(target_file)
    assert not content_after_overwrite.startswith("# ORIGINAL")
    assert "Minimal CLI entrypoint" in content_after_overwrite or "def create_parser" in content_after_overwrite

    # Backup mode also writes the new content (and would backup the old one internally)
    target_file.write_text("# ORIGINAL2\n", encoding="utf-8")
    render.render_project("cli-basic", project_name, dest, dry_run=False, update_mode="backup")
    content_after_backup = _read(target_file)
    assert not content_after_backup.startswith("# ORIGINAL2")
