# Week 01 — Repo scaffold + baseline checks

## Goal
- Create repo scaffold and make ruff/pyright/pytest pass locally and in CI.
- Establish a secure and effective authentication workflow for the Gemini CLI.

## What I did
1. **Repo Basics**:
    - Ran `uv run ruff check .` to lint Python files (found and fixed unused imports with `--fix`).
    - Added `[build-system]` to `pyproject.toml` to fix `pytest` import errors.

2. **The Auth & Environment Journey**:
    - *Attempt 1 (Standard .env)*: Tried using `python-dotenv` to load `GEMINI_API_KEY`.
    - *Observation*: The Gemini CLI (running as a subprocess) couldn't see variables loaded only into the Python process memory.
    - *Attempt 2 (Shell Integration)*: Switched to `direnv` to inject variables at the shell level. This worked for passing keys to subprocesses.
    - *Final Decision (Google Cloud ADC)*: Switched from a raw API Key to Google Cloud Application Default Credentials (ADC) for better integration and security defaults in this environment.

3. **Google Cloud ADC Setup**:
    - Set active project: `gcloud config set project MY_PROJECT_ID`
    - Configured quota project: `gcloud auth application-default set-quota-project MY_PROJECT_ID`
    - Set region: `gcloud config set ai/region global`
    - Authenticated: `gcloud auth login` & `gcloud auth application-default login`

## Gemini CLI drills
- [x] Ran `/memory show`
- [x] Used `@README.md` in a prompt
- [x] Ran `!uv run pytest -q` from inside Gemini CLI
- [x] Verified checkpointing + `/restore` exists

## Verification outputs

- **Linting & Formatting**:
```bash
agentic-engineering % uv run ruff check .
All checks passed!
agentic-engineering % uv run ruff format --check .
All checks passed!
```

- **Type Checking**:
```bash
agentic-engineering % uv run pyright
0 errors, 0 warnings, 0 informations
```

- **Tests**:
```bash
agentic-engineering % uv run pytest -q
..                                          [100%]
2 passed in 0.01s
```

- **CLI Doctor (Final State)**:
```bash
agentic-engineering % uv run ae doctor
agentic-engineering doctor
- python_version: 3.12.12
- platform: macOS-15.6.1-arm64-arm-64bit
- GOOGLE_CLOUD_PROJECT set: True
- GOOGLE_CLOUD_LOCATION set: True
```

## Notes / Surprises (The Learning Log)

### 1. The "Src Layout" vs. Pytest
**Issue**: `ModuleNotFoundError: No module named 'agentic_engineering'` when running tests.
**Cause**: `pytest` doesn't automatically add `src/` to the Python path.
**Fix**: Added a build backend to `pyproject.toml` so the project installs itself in editable mode during test runs.
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

### 2. `python-dotenv` vs. Subprocesses
**Surprise**: Even with `python-dotenv` loading the `.env` file, the Gemini CLI (spawned via `uv run`) couldn't find the API Key.
**Realization**: `python-dotenv` loads variables into the *current* Python process's `os.environ`. It does **not** export them to the parent shell or unrelated subprocesses unless explicitly passed.
**Fix**: Moved to `direnv` (shell-level) to ensure the environment is set before any command runs.

### 3. API Key vs. ADC
**Change**: Replaced `GEMINI_API_KEY` with Google Cloud ADC.
**Why**: The API key approach proved brittle for the specific Gemini CLI toolchain in this environment.
**Implementation**:
- Updated `doctor.py` to check for `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION`.
- Updated `README.md` to reflect the requirement for `gcloud` auth instead of a manual API key.
