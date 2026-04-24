# Agent-Grenzen

Jeder Agent im `exp_test`-Projekt hat einen fest definierten Zuständigkeitsbereich. Außerhalb dieses Bereichs darf er keine Dateien erstellen oder ändern.

## Übersicht

| Agent        | Erlaubter Pfad | Verbotene Pfade                          |
|--------------|----------------|------------------------------------------|
| DocsAgent    | `docs/`        | `backend/`, `review/`, `README.md`, Config-Dateien |
| BackendAgent | `backend/`     | `docs/`, `review/`, `README.md`, Config-Dateien    |
| ReviewAgent  | `review/`      | `docs/`, `backend/`, `README.md`, Config-Dateien   |

## Allgemeine Regeln

- Kein direktes Pushen auf `main`.
- Kein Force Push.
- Bei Merge-Konflikten: Arbeit stoppen und melden.
- Nur eigene Änderungen committen.
