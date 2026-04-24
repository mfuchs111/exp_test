# Multica-Workflow

## Isolierte Worktrees pro Task

Multica führt jeden Task in einem eigenen, isolierten Git-Worktree aus. Das bedeutet:

- Jeder Agent bekommt einen dedizierten Branch (z. B. `agent/docsagent/<run-id>`).
- Änderungen eines Agenten berühren die Arbeit anderer Agenten nicht.
- Der lokale Review-Clone des Users wird durch die Arbeit eines Agenten **nicht automatisch verändert**.

## Wann ändert sich GitHub?

Änderungen werden erst dann auf GitHub sichtbar, wenn der Agent:

1. einen Commit erstellt (`git commit`) und
2. den Branch pusht (`git push -u origin HEAD`).

Erst nach dem Push kann ein Pull Request geöffnet und der Branch in `main` gemergt werden.
