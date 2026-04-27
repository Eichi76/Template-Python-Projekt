import subprocess
import sys


def _run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, "-m", "template_python_projekt"] + args, capture_output=True, text=True)


def test_help_shows_usage() -> None:
    r = _run(["--help"])
    assert r.returncode == 0
    assert "usage" in r.stdout.lower() or "usage" in r.stderr.lower()


def test_missing_required_args_fails() -> None:
    # missing --template and --name should cause non-zero exit (argparse)
    r = _run([])
    assert r.returncode != 0
