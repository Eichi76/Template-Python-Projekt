from __future__ import annotations

import subprocess
import sys


def test_cli_help() -> None:
    """Start the example CLI with `--help` and expect exit code 0."""
    res = subprocess.run([sys.executable, "project_templates/cli-basic/src/main.py", "--help"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert res.returncode == 0
