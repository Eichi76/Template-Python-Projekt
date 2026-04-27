import shutil

import pytest

from template_python_projekt.poetry_env import ensure_poetry_environment


def test_poetry_missing(monkeypatch):
    monkeypatch.setattr(shutil, "which", lambda name: None)
    ok, msg = ensure_poetry_environment(run_install=False)
    assert ok is False
    assert "poetry wurde nicht gefunden" in msg


def test_poetry_present_no_install(monkeypatch):
    monkeypatch.setattr(shutil, "which", lambda name: "/usr/bin/poetry")
    ok, msg = ensure_poetry_environment(run_install=False)
    assert ok is True
    assert "poetry wurde gefunden" in msg
