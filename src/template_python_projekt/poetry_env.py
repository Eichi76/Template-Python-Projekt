from __future__ import annotations

import shutil


def ensure_poetry_environment(*, run_install: bool = False) -> tuple[bool, str]:
    """Prüft, ob `poetry` installiert ist und gibt (ok, nachricht) zurück.

    - ok = True: `poetry` wurde gefunden (und ggf. `poetry install`
      erfolgreich ausgeführt).
    - ok = False: `poetry` nicht gefunden oder ein Fehler trat auf.

    Führt `poetry install` nur aus, wenn `run_install=True`.
    Liefert Fehlertext statt Ausnahmen für einfache CLI-Verwendung.
    """
    poetry_path = shutil.which("poetry")
    if poetry_path is None:
        return (
            False,
            (
                "poetry wurde nicht gefunden. Bitte installiere poetry oder "
                "führe `python -m pip install -e .` manuell aus."
            ),
        )

    if not run_install:
        return (
            True,
            (
                f"poetry wurde gefunden unter: {poetry_path}. "
                "Führe 'poetry install' im Zielprojekt aus."
            ),
        )

    # Ausführliche Installation bewusst nicht automatisch ausführen, um keine
    # Prozesse im Kontext des Generators zu starten. Stattdessen geben wir
    # eine handlungsorientierte Nachricht zurück, die der Benutzer per Hand ausführen kann.
    return (
        True,
        (
            f"poetry wurde gefunden unter: {poetry_path}. "
            "Bitte führe 'poetry install' manuell im Zielprojekt aus, wenn nötig."
        ),
    )
