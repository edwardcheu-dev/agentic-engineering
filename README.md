# agentic-engineering

A long-lived, public “Learning Factory” to build practical muscle memory for:
- Agentic coding workflows (using Gemini CLI)
- Production-grade LLM + agentic applications (MCP / A2A / MAS / context engineering included)

## The Learning Factory (how progress works)
This repo is not a fixed calendar curriculum.

It is a **traceable flywheel**:

1) **Competency Map defines targets** (what “good” looks like + rubrics)
2) **Products generate evidence** (apps built specifically to exercise competencies)
3) **Knowledge Base distills reusable blueprints** (playbooks/patterns/templates/reference)

Key rule:
> Every competency must have **evidence** (code/evals) and **distillation** (KB artifact).
> If it doesn’t, it’s not “learned,” it’s “experienced once.”

Canonical sources of truth:
- Competencies: `docs/competency/COMPETENCY_MAP.md`
- Scores: `docs/competency/SCORECARD.md`
- Traceability (competency ↔ KB ↔ evidence ↔ products): `docs/competency/TRACEABILITY.md`
- KB index: `docs/kb/index.md`
- Product registry: `docs/products/README.md`

## How to navigate (repo memory map)
Read in this order when resuming:

1. `AGENT_CONTEXT.md` — the repo’s “north star” + always-load pointers
2. `PROJECT_STATE.md` — what we’re doing now + next actions
3. `docs/competency/COMPETENCY_MAP.md` — the targets (IDs + definitions)
4. `docs/competency/TRACEABILITY.md` — what is proven vs missing
5. `docs/kb/index.md` — the distilled blueprint knowledge
6. `docs/products/README.md` — product registry + why each exists
7. `LEARNING_LOG.md` — time-based record (PR links + competency IDs)
8. `docs/weeks/YYYY-Www/` — raw weekly notes and artifacts
9. `GEMINI.md` — how the agent should behave in this repo

## Rule of gravity (where things belong)
- Still true in 6 months → **KB** (`docs/kb/<DOMAIN>/<COMPETENCY_ID>/`)
- A decision with tradeoffs → **ADR** (`docs/decisions/`)
- What happened / experiments tried → **Weeks** (`docs/weeks/`)

## Engineering Manuals (legacy - to be migrated to `docs/kb/`)
Technical guides for maintaining and contributing to this repo:

- **[CI/CD Guide](docs/kb/ops/ops-01/ci_cd.md)**: How our GitHub Actions pipeline works.
- **[PR Workflow](docs/kb/acw/acw-03/pr_workflow.md)**: How to create, verify, and merge Pull Requests.
- **[Git Tagging](docs/kb/ops/ops-01/git_tagging.md)**: How to manage weekly tags (create, move, delete).

## Macro Library (Prompts)
SOPs for the agent in `prompts/`:

- **[@prompts/commit_package.md](prompts/commit_package.md)**: Prepares a conventional commit package (message + staging plan) without executing it.
- **[@prompts/prepare_weekly_review.md](prompts/prepare_weekly_review.md)**: Drafts `LEARNING_LOG.md` updates and PR descriptions from git history.
- **[@prompts/session_bootstrap.md](prompts/session_bootstrap.md)**: Goal → acceptance criteria → competencies → plan → verify → distillation.
- **[@prompts/score_competencies.md](prompts/score_competencies.md)**: Updates scorecard + gaps + smallest next deltas.
- **[@prompts/distill_to_kb.md](prompts/distill_to_kb.md)**: Converts weekly notes into KB artifacts (+ ADR suggestions).
- **[@prompts/create_adr.md](prompts/create_adr.md)**: Creates/updates an ADR with context + decision + consequences.
- **[@prompts/migrate_three_pillars.md](prompts/migrate_three_pillars.md)**: Migration in PR-sized steps.

## Quickstart

### Prerequisites

- Python 3.12+
- `uv` installed: <https://docs.astral.sh/uv/>
- `just` installed: <https://github.com/casey/just> (`brew install just`)

### Install dependencies

```bash
uv sync --dev
```

### Run the "PR gating" checks
```bash
just verify
```
Or run specific suites:
- **Code only**: `just verify-code` (lint, type, test)
- **Docs only**: `just verify-docs` (links, format)

### Run the CLI
```bash
just doctor
```

### Setup Pre-commit hooks
```bash
uv run pre-commit install
```

## Environment variables (safe public-repo setup)
- Commit: `.env.example` (placeholders only)
- Never commit: `.env` or any real secrets

Setup:
```bash
cp .env.example .env
```
Then edit `.env` locally to set:
- `GOOGLE_CLOUD_PROJECT`
- `GOOGLE_CLOUD_LOCATION`
The codebase should only check whether the variable is set (never print the value).

## Gemini CLI workflow (muscle-memory loop)
- Use `GEMINI.md` as the repo's working agreement.
- Use `@path/to/file_or_dir` to share context with the model.
- Use `!<cmd>` to run checks (e.g., `!git status`, `!uv run pytest -q`) and keep a tight verify loop.
- Use `/memory show` to confirm which project memory files are loaded.
- Checkpointing is enabled in `.gemini/settings.json`; use `/restore` if a tool edit goes wrong.

## Security notes
- Treat this repo as public forever.
- No secrets in git history.
- `.geminiignore` reduces accidental secret exposure to agent tooling.
- Gemini CLI supports `@<path>` for injecting file/dir content into prompts, and `!<cmd>` to run shell commands from inside the CLI.
