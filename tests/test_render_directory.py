from pathlib import Path

from template_python_projekt.render import render_directory


def test_render_directory_basic(tmp_path: Path) -> None:
    d = tmp_path
    # create simple templates
    (d / "foo.txt.jinja").write_text("Hello {{ name }}\n", encoding="utf-8")
    sub = d / "sub"
    sub.mkdir()
    (sub / "bar.md.jinja").write_text("{{ greeting | default('Hi') }}, {{ name }}\n", encoding="utf-8")

    out = render_directory(d, {"name": "Alice"})

    assert "foo.txt.jinja" in out
    assert "sub/bar.md.jinja" in out
    assert "Alice" in out["foo.txt.jinja"]
    assert "Hi, Alice" in out["sub/bar.md.jinja"]
