# GEMINI.md — agentic-engineering

You are the Gemini CLI agent working inside this repository.

## Mission
Operate this repo as a long-lived public **Learning Factory** for production LLM + agentic systems.

The repo has 3 pillars (control plane):
1) **Competency Map (North Star):** `docs/competency/`
2) **Products (Vehicles):** `docs/products/`
3) **Knowledge Base (Blueprint):** `docs/kb/` (most important)

Supporting:
- ADRs: `docs/decisions/`
- Weekly raw notes: `docs/weeks/`

## Non-negotiables (do not drift)
- Treat this repo as public forever.
- Never request, print, or store secrets (keys/tokens). Do not read `.env` files.
- Keep diffs small; propose staged plans if a change feels large.
- Prefer: acceptance criteria → evidence/tests → implementation → verification.
- Unit tests never make network calls.
- Do not run `git commit`, `git push`, or merge unless explicitly asked.

## Definition of “learned” (enforced)
For any meaningful work session / PR, you must be able to answer:
- Which **competency IDs** did this touch?
- What **evidence** changed? (tests/evals/docs/ADRs)
- What **distilled knowledge** was created/updated? (KB artifact)

If it doesn’t include evidence + KB distillation, it is incomplete.

## Always-load files (start here)
Load these first (or request them if missing):
- `AGENT_CONTEXT.md`
- `PROJECT_STATE.md`
- `docs/competency/COMPETENCY_MAP.md`
- `docs/competency/SCORECARD.md`
- `docs/competency/TRACEABILITY.md`
- `docs/products/README.md`
- `docs/kb/index.md`
- `LEARNING_LOG.md`
- `README.md`

Then load only targeted additional context:
- product docs under `docs/products/<product>/`
- specific KB pages in `docs/kb/`
- specific code under `src/`

## Operating modes (declare one at the top of your response)
You must declare a mode whenever you propose work:

- **Mode: Build** — ship a product increment (features, tests, evals)
- **Mode: Distill** — convert raw notes/decisions into KB artifacts
- **Mode: Calibrate** — score competencies, identify gaps, pick smallest deltas
- **Mode: Migrate** — repo re-org / docs restructuring in small PRs

## What you must output when proposing changes
Whenever you propose a change, include:

1) **Target competency IDs** (e.g., CTX-03, EVAL-05)
2) **Acceptance criteria** (observable)
3) **Plan (PR-sized)** including files to touch
4) **Verification steps** (`just verify*`)
5) **Distillation plan** (which KB page(s) updated/created)
6) **Traceability update** (what links you will add in TRACEABILITY)

## Rule of gravity (where content belongs)
- Still true in 6 months → KB (`docs/kb/`)
- Decision + tradeoffs → ADR (`docs/decisions/`)
- What happened / experiments → Weeks (`docs/weeks/`)

## Frequently used commands
- `uv sync --dev`
- `just verify`
- `just verify-code`
- `just verify-docs`

## Gemini CLI usage conventions
- Use `@path` to include only relevant files/dirs.
- Use `!<cmd>` to run commands.
- Use `/memory show` to confirm loaded memory files.
- Use `/restore` if tool edits go wrong.

## Output style
- Be concrete: filenames, commands, small checklists.
- Ask a single targeted question if something is ambiguous.
