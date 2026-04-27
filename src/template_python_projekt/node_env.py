from __future__ import annotations

import shutil


def ensure_node_and_markdownlint(*, run_install: bool = False) -> tuple[bool, str]:
    """Prüft, ob `node` und ein `markdownlint`-CLI vorhanden sind.

    Rückgabe: `(ok, nachricht)`
    - ok = True: Node ist vorhanden; wenn `markdownlint` nicht gefunden wurde,
      enthält die Nachricht eine Anleitung zur Installation (kein automatisches
      Installieren).
    - ok = False: Node nicht gefunden.

    Der Helper führt keine automatischen `npm`-Installationen aus, sondern gibt
    handlungsorientierte Hinweise zurück.
    """
    # `run_install` kept for API parity with other helpers; nicht automatisch verwenden
    _ = run_install

    node_path = shutil.which("node")
    if node_path is None:
        return (
            False,
            (
                "node wurde nicht gefunden. Bitte installiere Node.js (z.B. von "
                "https://nodejs.org/) oder stelle sicher, dass 'node' im PATH liegt."
            ),
        )

    # Prüfe auf bekannte CLI-Namen für markdownlint
    md_cli = shutil.which("markdownlint") or shutil.which("markdownlint-cli")
    if md_cli:
        return (True, f"Node gefunden unter: {node_path}. markdownlint gefunden unter: {md_cli}.")

    # Wenn markdownlint fehlt, geben wir eine Anleitung zurück.
    install_msg = (
        "Node wurde gefunden. 'markdownlint' (markdownlint-cli) wurde nicht gefunden.\n"
        "Installationsoptionen:\n"
        "- Global (sofort nutzbar): `npm install -g markdownlint-cli`\n"
        "- Projekt/DevDependency: Füge "
        '  "markdownlint-cli": "^0.XX" zu `devDependencies` in `package.json` hinzu'
        " und führe `npm install` aus.\n"
        "Ich führe keine Installation automatisch aus; führe einen der obigen Befehle manuell aus."
    )

    return (True, install_msg)
