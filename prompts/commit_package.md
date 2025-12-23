Please prepare a commit package for the current working tree.

Requirements:

Do NOT run git commit, git push, merges, or any destructive commands.
Inspect changes using (preferably) read-only commands such as:
git status --porcelain=v1
git diff
git diff --stat
Summarize the changes in plain English.
Commit message:

Propose ONE Conventional Commits message: type(scope): subject (scope optional).
Provide the message as plain text (no code blocks) to avoid line-number rendering issues in some terminal interfaces. Do NOT include prefixes like "Message:", "Commit 1:", or any line numbers/bullet points for the subject line. If splitting commits, provide each message clearly separated.
Staging plan:

Provide an exact staging plan using explicit file paths (no git add -A).
Prefer git add <file1> <file2>. Use git add -p only when it materially improves separation; explain what hunks to include/exclude.
Checklist:

Files touched (grouped by purpose: docs / config / code / tests).
Commands to run before committing:
If any Python code/tests changed: just verify-code
If docs-only: just verify-docs
If both/uncertain: just verify
Risk notes:
Call out any potential secret exposure (e.g., .env*, credentials files, tokens). Never print secret values; if a file may contain secrets, warn and stop.
Verification (exact commands):

git status
git diff
git diff --staged (after staging)
git show (after commit)
Output format (use these headings):

Summary
Suggested commit(s)
Staging plan (commands)
Checklist
Verification commands
Context: This is a public repo. Treat any secrets as critical; never print env var values.
