# Pull Request (PR) Workflow Guide

This guide explains how to contribute changes to `agentic-engineering` using Pull Requests. A PR is how you propose changes, allow CI to verify them, and record your progress.

## Why use Pull Requests?
- **Safety**: GitHub Actions automatically runs `just check` on your PR.
- **Documentation**: PRs provide a permanent history of *why* a change was made.
- **Checklist**: Our PR template ensures you don't forget to update logs or run tests.

## The 5-Step Workflow

### 1. Create a Feature Branch
Always work on a separate branch. This keeps `main` clean and stable.
```bash
git checkout -b your-feature-name
```

### 2. Make Changes & Commit
As you work, use our commit package SOP to prepare clean, conventional commits.
```bash
# Prepare with the agent
@prompts/commit_package.md

# Stage and commit (example)
git add <files>
git commit -m "feat: your description"
```

### 3. Push to GitHub
Upload your branch to the remote repository.
```bash
git push -u origin your-feature-name
```

### 4. Open the Pull Request
1.  Go to the repository on GitHub.
2.  You will see a "Compare & pull request" button. Click it.
3.  Fill out the **PR Template**:
    -   Link to the specific week.
    -   Explain **What** and **Why**.
    -   Tick the verification boxes.
4.  Click "Create pull request".

### 5. Verify & Merge
-   **Wait for CI**: Ensure the "ci" check passes (green checkmark).
-   **Review**: Read your own diff one last time on the "Files changed" tab.
-   **Merge**: Once satisfied, click "Squash and merge". This keeps the `main` history clean.
-   **Cleanup**: Delete the feature branch after merging.

## Tips for Success
- **Small PRs**: Prefer small, focused PRs over giant ones. They are easier to verify and reason about.
- **Update Logs**: Every PR in this project should usually update `LEARNING_LOG.md` and the weekly notes.
- **Draft PRs**: If you want to save your work but aren't ready to merge, use the "Convert to draft" option on GitHub.
