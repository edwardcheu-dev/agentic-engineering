# Learning Log — agentic-engineering

## How to use this log
Each week:
- add one entry
- link the PR
- link `docs/week-XX/notes.md`
- write the 3 biggest takeaways

---

## Week 01 — Repo scaffold + baseline checks

- Dates: Dec 22, 2025

- PR: (link)

- Notes: docs/week-01/notes.md



### Goal

- Create repo scaffold and make `ruff`, `pyright`, and `pytest` pass locally and in CI.

- Establish a secure and effective authentication workflow for the Gemini CLI.



### What shipped

- **Repo Structure**: Standard Python `src/` layout with `uv` for dependency management.

- **Tooling**: `ruff` (lint/format), `pyright` (types), `pytest` (tests), and `just` (task runner).

- **Auth**: Switched from brittle `.env` API keys to robust Google Cloud ADC (`gcloud` auth).

- **Automation**: `Justfile` for standard commands, `pre-commit` hooks for local checks, and GitHub Actions for CI.

- **Documentation**: Engineering manuals for CI/CD and PR workflows, plus a "Macro Library" of reusable prompts.

- **Workflow**: Automated weekly review generation via `@prompts/prepare_weekly_review.md`.



### Commands I ran (copy/paste)

- `just check`

- `just doctor`

- `just verify-code`

- `just verify-docs`



### Gemini CLI muscle drills

- [x] Ran `/memory show`

- [x] Used `@README.md` in a prompt

- [x] Ran `!uv run pytest -q` from inside Gemini CLI

- [x] Verified checkpointing + `/restore` exists



### What I learned

1. **Src Layout vs. Pytest**: `pytest` requires an editable install (via `hatchling` build backend) to correctly resolve imports in a `src/` layout.

2. **Environment Variable Scope**: `python-dotenv` only affects the Python process; `direnv` is needed to inject variables into the shell for subprocesses (like the Gemini CLI).

3. **Workflow Automation**: Delegating CI checks to a local task runner (`just`) ensures consistency between local dev and CI environments.



### Next week

- (To be defined in Week 02)
