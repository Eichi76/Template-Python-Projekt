import tomllib

from template_python_projekt.render import merge_toml_strings


def test_merge_toml_prefers_existing() -> None:
    existing = '''
[tool.poetry]
name = "user_project"
version = "1.2.3"
[tool.poetry.dependencies]
python = "^3.12"
custom = "1.0"
'''

    template = '''
[tool.poetry]
name = "template_project"
description = "A template"
[tool.poetry.dependencies]
python = "^3.12"
requests = "^2.0"
'''

    merged = merge_toml_strings(existing, template)

    assert merged["tool"]["poetry"]["name"] == "user_project"
    assert merged["tool"]["poetry"]["description"] == "A template"

    deps = merged["tool"]["poetry"]["dependencies"]
    assert deps["custom"] == "1.0"
    assert deps["requests"] == "^2.0"
