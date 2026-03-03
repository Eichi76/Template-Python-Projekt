# Copilot‑Hinweise für generierte Projekte

Dieses Dokument enthält Empfehlungen, wie GitHub Copilot in Projekten
verwendet werden sollte, die mit diesem Generator erstellt wurden.

Empfehlungen:

- Beschreibe die gewünschte Funktionalität klar in der Kommentar‑ oder
  TODO‑Zeile, bevor du Vorschläge akzeptierst.
- Überprüfe stets generierten Code auf Sicherheit, Lizenzkonformität und
  Stil (Linting, Typen).
- Akzeptiere Vorschläge von Copilot selektiv — passe Variablennamen,
  Docstrings und Tests an.
- Verwende Copilot, um Boilerplate zu erzeugen (z. B. CLI‑Parser, Tests),
  aber schreibe kritische Logik selbst.

Workflow‑Tipps:

- Führe nach Einfügen von Code sofort `ruff` und `mypy` aus.
- Ergänze Tests für jede nicht‑triviale Funktion, die Copilot erzeugt.
- Vermeide das direkte Kopieren von großen Codefragmenten aus
  unbekannten Quellen ohne Lizenzprüfung.

Beispiel‑Kommentar für Copilot:

```python
# TODO: Implementiere eine robuste Funktion `load_config(path: str) -> dict`
# - liest YAML/TOML/JSON (fallback)
# - validiert gegen Schema
# - wirft verständliche Fehler
```

Wenn du möchtest, kannst du diese Hinweise in generierten Projekten
anpassen oder erweitern.
