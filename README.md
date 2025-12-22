# agentic-engineering

A 52-week, single evolving project to build practical muscle memory for:

- Agentic coding workflows (using Gemini CLI)
- LLM engineering in Python (tests, evals, RAG, reliability, CI)

This repo is designed to be our shared long-term memory: you can paste the repo link and we can resume with full context.

## How to navigate (repo memory map)

Read in this order when resuming:

1. `PROJECT_STATE.md` — current week + what to do next
2. `ROADMAP.md` — the full 52-week plan (kept current in git)
3. `LEARNING_LOG.md` — weekly entries + PR links
4. `docs/week-XX/` — detailed weekly notes and artifacts
5. `GEMINI.md` — workflow rules for the agent in this repo

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
just check
```
(Or run specific steps: `just fmt`, `just lint`, `just type`, `just test`)

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

## Reusable Prompts (Macro Library)
This repo builds a library of standard operating procedures (SOPs) for the agent in `prompts/`.
- **Why**: To standardize complex tasks (like preparing commits) and reduce typing.
- **How**: Use `@prompts/<name>.md` to inject the instruction.
- **Example**: `@prompts/commit_package.md` instructs the agent to prepare a commit without executing it.

## Security notes
- Treat this repo as public forever.
- No secrets in git history.
- `.geminiignore` reduces accidental secret exposure to agent tooling.
- Gemini CLI supports `@<path>` for injecting file/dir content into prompts, and `!<cmd>` to run shell commands from inside the CLI.
