import shutil

import pytest

from template_python_projekt.node_env import ensure_node_and_markdownlint


def test_node_missing(monkeypatch):
    monkeypatch.setattr(shutil, "which", lambda name: None)
    ok, msg = ensure_node_and_markdownlint(run_install=False)
    assert ok is False
    assert "node wurde nicht gefunden" in msg


def test_node_present_but_no_md(monkeypatch):
    def fake_which(name: str):
        if name == "node":
            return "/usr/bin/node"
        return None

    monkeypatch.setattr(shutil, "which", fake_which)
    ok, msg = ensure_node_and_markdownlint(run_install=False)
    assert ok is True
    assert "markdownlint" in msg


def test_node_and_md_present(monkeypatch):
    def fake_which(name: str):
        if name == "node":
            return "/usr/bin/node"
        if name == "markdownlint":
            return "/usr/bin/markdownlint"
        return None

    monkeypatch.setattr(shutil, "which", fake_which)
    ok, msg = ensure_node_and_markdownlint(run_install=False)
    assert ok is True
    assert "markdownlint gefunden" in msg
