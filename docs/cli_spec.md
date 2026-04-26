# CLI Spezifikation — Starter Script

Flags

- `--template <name>` (erforderlich): Name der Vorlage, z. B. `cli-basic`.
- `--name <project-name>` (erforderlich): Zielprojektname.
- `--dest <path>` (optional, Default `.`): Zielverzeichnis für das neue Projekt.
- `--dry-run` (optional): Vorschau; es werden keine Änderungen geschrieben.
- `--force` (optional): Überschreibe vorhandene Dateien, wenn nötig.

Exit Codes

- `0`: Erfolg (oder dry-run Vorschau erfolgreich).
- `1`: Allgemeiner Fehler (z. B. Renderer nicht implementiert).
- `2`: Laufzeitfehler bei der Ausführung der Render-Logik.

Beispiele

```bash
python -m template_python_projekt --template cli-basic --name myproj --dry-run
python -m template_python_projekt --template cli-basic --name myproj --dest ./out
```

Hinweis

- Diese Spezifikation ist der Ausgangspunkt für Sub-Issue #19.

  Die tatsächliche Implementierung delegiert die Projektgenerierung an
  `render.render_project(...)` (Sub-Issue #20).
