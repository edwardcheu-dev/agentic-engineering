# Git Tagging Guide

This guide explains how to use git tags in `agentic-engineering` to mark the boundaries of each learning week.

## Why use Tags?
- **Weekly Boundaries**: Tags like `week-01` mark the exact state of the repo at the end of a week.
- **Automation**: Our `@prompts/prepare_weekly_review.md` uses tags to calculate the diff for the current week.

## Creating a Tag
At the end of the week, after merging your PR and pulling `main`:

```bash
git tag -a week-XX -m "End of Week XX"
git push origin week-XX
```

## Moving a Tag (Retagging)
Sometimes you merge "one last cleanup" PR after tagging. To keep the weekly boundary clean, you should move the tag to the latest commit.

### 1. Delete Local Tag
```bash
git tag -d week-XX
```

### 2. Delete Remote Tag
```bash
git push origin :refs/tags/week-XX
```

### 3. Create New Tag
```bash
git tag -a week-XX -m "End of Week XX (Finalized)"
```

### 4. Push New Tag
```bash
git push origin week-XX
```

## Verifying Tags
To see the list of tags:
```bash
git tag -n
```
