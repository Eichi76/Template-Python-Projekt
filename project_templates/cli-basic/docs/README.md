# Dokumentation: cli-basic

Dieses Verzeichnis enthält Beispiel-Markdown-Templates für die technische
Dokumentation des `cli-basic` Templates.

## Rendering

Verwenden Sie `jinja2`, um Dateien mit der Endung `*.md.jinja` zu rendern.
Alternativ kann das Hilfsmodul `src/template_python_projekt/render.py`
verwendet werden; es nutzt `jinja2` falls verfügbar, sonst einen einfachen
Fallback.

## Erwartete Struktur

```text
project_templates/cli-basic/docs/
  ├─ index.md.jinja
  └─ README.md
```

## Beispiel-Variablen

- `project_name`: Name des Projekts
- `author`: Autor
