from __future__ import annotations

from pathlib import Path


def test_render_template_file(tmp_path: Path) -> None:
    from template_python_projekt.render import render_template_file

    tpl = tmp_path / "tpl"
    tpl.mkdir()
    f = tpl / "greeting.txt"
    f.write_text("Hello {{name}}!\n")

    out = render_template_file(f, {"name": "Bob"})
    assert out == "Hello Bob!\n"


def test_render_directory_mapping(tmp_path: Path) -> None:
    from template_python_projekt.render import render_directory

    tpl = tmp_path / "tpl"
    tpl.mkdir()
    (tpl / "a.txt").write_text("A: {{a}}")
    (tpl / "sub").mkdir()
    (tpl / "sub" / "b.txt").write_text("B: {{b}}")

    rendered = render_directory(tpl, {"a": "1", "b": "2"})
    assert rendered["a.txt"] == "A: 1"
    assert rendered["sub/b.txt"] == "B: 2"
