# CI/CD Engineering Guide

This document explains the Continuous Integration (CI) setup for `agentic-engineering`. We use **GitHub Actions** to automatically verify code quality on every push and pull request.

## The Workflow File
Location: `.github/workflows/ci.yml`

Our CI pipeline is designed to be a **mirror of our local development workflow**. We achieve this using `just`.

### Triggers
The workflow runs on:
- **Push** to the `main` branch.
- **Pull Request** targeting the `main` branch.

### The Pipeline Steps

1.  **Checkout Code**: Uses `actions/checkout` to pull the latest code.
2.  **Setup Python**: Uses `actions/setup-python` to install Python 3.12.
3.  **Install `uv`**: Uses `astral-sh/setup-uv` for fast dependency management.
4.  **Install `just`**: Uses `extractions/setup-just` to get our task runner.
5.  **Install Dependencies**: Runs `uv sync --dev` to install the project environment.
6.  **Run Checks**: Runs `just check`.

### Why `just check`?
Instead of defining `lint`, `format`, and `test` steps separately in YAML, we call `just check`.
- **Consistency**: The exact same command runs locally and in CI.
- **Maintainability**: If we add a new check (e.g., security scanning) to the `Justfile`, CI picks it up automatically without editing YAML.

## Setting up CI (Step-by-Step for Future Projects)

If you need to recreate this setup:

1.  **Create the Workflow Directory**:
    ```bash
    mkdir -p .github/workflows
    ```
2.  **Define the Workflow**: Create a file (e.g., `ci.yml`) in that directory.
3.  **Use the Standard Template**:
    (See the content of `.github/workflows/ci.yml` in this repo).
4.  **Push to GitHub**: GitHub detects the file and starts the runner automatically.
5.  **View Results**: Go to the "Actions" tab in your GitHub repository.
