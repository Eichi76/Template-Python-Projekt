# Commit‑Anleitung für generierte Projekte

Verwende beim Erstellen von Commits das
[konventionelle Commit‑Format](https://www.conventionalcommits.org/de/v1.0.0/).
Dadurch arbeiten automatische Release‑ und Changelog‑Workflows sauber.

Beispiele:

- `feat: füge neuen CLI‑Befehl hinzu`
- `fix: behebe Absturz in Datei‑Parser`
- `docs: aktualisiere README für Installation`
- `chore: aktualisiere dev‑Dependencies`

Hinweise:

- Schreibe Commit‑Nachrichten auf Deutsch, kurz und aussagekräftig.
- Beginne die Überschrift mit einem Typ
  (`feat`, `fix`, `docs`, `chore`, `refactor`, `test`).
- Ergänze bei Bedarf einen kurzen Body, der das *Warum* erklärt.
- Verwende bei Breaking Changes das Format
  `BREAKING CHANGE: <Beschreibung>` im Body.

Pre‑Commit:

- Vor dem Commit sollten Formatierung und Linter ausgeführt
  werden: `ruff`, `isort`, `mypy`.
- Nutze `git commit` mit den standardmäßigen pre‑commit Hooks;
  diese laufen automatisch, wenn konfiguriert.

Beispiel für einen vollständigen Commit:

```text
feat: füge Template‑Renderer für Jinja2 hinzu

Der Renderer versucht zuerst Jinja2, fällt bei fehlender
Abhängigkeit auf ein sicheres Fallback zurück.

BREAKING CHANGE: API von `render_template_file` wurde
geringfügig angepasst
```
