from pathlib import Path


def test_troubleshooting_doc_exists_and_contains_keywords() -> None:
    p = Path("docs/troubleshooting.md")
    assert p.exists(), "docs/troubleshooting.md fehlt"
    text = p.read_text(encoding="utf-8")
    for kw in ("poetry", "node", "pre-commit", "merge"):
        assert kw in text, f"Schlüsselwort '{kw}' nicht in docs/troubleshooting.md gefunden"
