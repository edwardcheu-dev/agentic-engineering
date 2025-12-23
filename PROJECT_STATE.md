# PROJECT_STATE (source of truth)

Keep this file current. It is the fastest way to resume work.

## Current week

- Week: 01
- Theme: Repo scaffold + baseline checks
- Status: Complete (PR ready)

## Week 01 acceptance checklist

Repo + tooling:

- [x] Repo pushed to GitHub (`agentic-engineering`)
- [x] Install: `uv sync --dev`
- [x] Local checks pass:
  - [x] `uv run ruff check .`
  - [x] `uv run ruff format --check .`
  - [x] `uv run pyright`
  - [x] `uv run pytest -q`
- [x] GitHub Actions CI passes on PR and on `main`

Documentation + memory:

- [x] `ROADMAP.md` exists and includes the 52-week plan
- [x] `LEARNING_LOG.md` has a Week 01 entry (even if short)
- [x] `docs/week-01/notes.md` updated with outputs and notes

## Working agreements (do not drift)

- No secrets in git (ever).
- Keep diffs small; prefer incremental PRs.
- Prefer: acceptance criteria → tests → implementation → verification.
- Unit tests never make network calls.

## Resume order (when coming back later)

1. `ROADMAP.md`
2. `LEARNING_LOG.md`
3. `docs/week-01/notes.md`
4. `GEMINI.md`

## Next actions (do these in order)

1. Run checks and paste outputs into `docs/week-01/notes.md`:

    - `uv sync --dev`
    - `uv run ruff check .`
    - `uv run ruff format --check .`
    - `uv run pyright`
    - `uv run pytest -q`

2. Confirm `.env.example` is tracked and `.env` is ignored:

    - `git check-ignore -v .env`
    - `git check-ignore -v .env.example`

3. Push to GitHub and paste the repo link.
