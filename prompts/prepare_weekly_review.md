# Weekly Review & PR Preparation Prompt

This prompt helps the user wrap up the week by analyzing recent work, updating project logs, and preparing the weekly Pull Request.

## Objective
Analyze the git history since the last weekly tag (or the beginning of the repo if no tags exist) to generate:
1.  Updates for `LEARNING_LOG.md`.
2.  Updates for `PROJECT_STATE.md`.
3.  A comprehensive Pull Request (PR) title and description.

## Workflow

### 1. Analyze Context
Run the following commands to gather context:
- `git describe --tags --abbrev=0` (to find the last tag).
    - If this fails (no tags), assume we are in Week 01 and look at `git log --oneline`.
    - If it succeeds (e.g., `week-01`), look at `git log --oneline <tag>..HEAD`.
- Read `@PROJECT_STATE.md` to know the current week number and theme.
- Read `@LEARNING_LOG.md` to see the current structure.

### 2. Generate Content
Based on the commit history and file diffs:

#### A. LEARNING_LOG.md Draft
Draft a new entry (or update the existing placeholder) for the current week.
- **Goal**: Summarize the week's theme.
- **What shipped**: Bullet points derived from `feat`, `fix`, `docs`, and `config` commits.
- **Commands run**: List the standard verification commands (`just check`, `just doctor`).
- **Learned**: Synthesize "Surprises" or "Notes" from `docs/week-XX/notes.md` if available, or infer from refactor commits.

#### B. PROJECT_STATE.md Updates
- Update "Current week" status.
- Check off items in the "Week XX acceptance checklist" based on what was accomplished.

#### C. Pull Request Draft
Draft the title and body for the PR.
- **Title**: `Week <XX> — <Theme>`
- **Body**: Use the template from `.github/PULL_REQUEST_TEMPLATE.md`, but pre-fill it with:
    - **What changed**: A high-level summary of the commits.
    - **Why**: The motivation (e.g., "To establish the baseline repo structure").
    - **Verification**: Confirm `just check` passes.

## Output Format

Please present the drafts clearly:

### 1. Proposed `LEARNING_LOG.md` Entry
(Provide as plain text, no code blocks)

### 2. Proposed `PROJECT_STATE.md` Changes
(Describe what lines to change or check off)

### 3. Proposed Pull Request
**Title:** ...
**Body:**
(Provide as plain text, no code blocks)

### 4. Verification
- Confirm that `docs/week-XX/notes.md` exists and is populated.
- Confirm `just verify-code` passes.

## Instructions for the Agent
- Do NOT edit files yet. Just propose the content for review.
- If the user approves, you will then apply the changes to the markdown files.
