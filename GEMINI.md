# agentic-engineering — GEMINI.md

You are the Gemini CLI agent working inside this repository.

## Mission
Help me build deep muscle memory for agentic coding + LLM engineering in Python over 52 weeks.
This is a single, evolving project. Prefer small, reviewable changes.

## Non-negotiables (follow these always)
- Never request, print, or store secrets (API keys, tokens). Do not read `.env` files.
- Keep diffs small. If a change feels large, propose a staged plan.
- Prefer test-first or test-with changes. Add/adjust tests for behavior changes.
- No network calls in unit tests.
- Use existing project conventions (ruff, pyright, pytest).
- When you want to edit files, first propose: (1) which files, (2) what changes, (3) how we’ll verify.
- Never run `git commit`, `git push`, or merge operations unless explicitly asked.
- **Copy-paste safety**: Never provide content intended for copy-pasting (commit messages, PR descriptions, log entries) inside triple-backtick code blocks. Provide them as plain text to avoid automatic line-numbering in the terminal.

## Repo “memory” (read these first when helping)
- PROJECT_STATE.md (where we are now)
- ROADMAP.md (52-week plan)
- LEARNING_LOG.md (weekly narrative)

## How we work (the loop)
1) Clarify goal + acceptance criteria
2) Write/adjust tests
3) Implement
4) Verify:
   - Code changes: `just verify-code`
   - Doc changes: `just verify-docs`
   - Mixed/Unsure: `just verify`
5) Summarize changes + next step suggestion

## Reusable prompts (repo macro library)
- Reusable prompts live in prompts/ (version controlled).
- Include them with @prompts/<name>.md instead of copy/pasting.
- Default safety: do not run git commit / git push unless I explicitly ask.

## Commands I run often
- `uv sync --dev`
- `uv run ruff check .`
- `uv run ruff format .`
- `uv run pyright`
- `uv run pytest -q`

## Gemini CLI usage (preferred)
- Use `@path` to include only relevant files/dirs.
- Use `!<cmd>` to run commands (git, uv, pytest) from inside Gemini CLI.
- If a tool edit goes wrong, use `/restore` to roll back.

## Definitions (keep them crisp)
- PR gating: checks that MUST pass before merge (lint/type/test/etc.)
- Nightly: scheduled CI run for slower/heavier checks
- Real LLM smoke tests: tiny end-to-end checks that hit a real model to verify the pipeline is alive (not a full eval)

## Output style
- Be concrete: commands, filenames, and short checklists.
- When uncertain, ask a single targeted question instead of guessing.
