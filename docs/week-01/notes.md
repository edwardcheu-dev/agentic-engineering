# Week 01 — Repo scaffold + baseline checks

## Goal
- Create repo scaffold and make ruff/pyright/pytest pass locally and in CI.

## What I did
- Ran `uv run ruff check .` to lint the Python files.
- Noticed there are unused imports.
- Ran `uv run ruff check . --fix` to apply auto-fixes and added this to the practical workflow.
- Encountered a bug when running pytest due to the project itself is not "installed" in the virtual environment.
- The Fix: added [build-system] to `pyproject.toml` at the bottom.
```pyproject.toml
// ...existing code...
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

## Gemini CLI drills
- [ ] Ran `/memory show`
- [ ] Used `@README.md` in a prompt
- [ ] Ran `!uv run pytest -q` from inside Gemini CLI
- [ ] Verified checkpointing + `/restore` exists

## Verification outputs
Paste outputs here:
- `uv run ruff check .`
```bash
agentic-engineering % uv run ruff check .
F401 [*] `sys` imported but unused
 --> src/agentic_engineering/doctor.py:5:8
  |
3 | import os
4 | import platform
5 | import sys
  |        ^^^
6 | from dataclasses import dataclass
  |
help: Remove unused import: `sys`

Found 1 error.
[*] 1 fixable with the `--fix` option.
```
- `uv run ruff check . --fix`
```bash
agentic-engineering % uv run ruff check . --fix
Found 1 error (1 fixed, 0 remaining).
```

- `uv run ruff format`
```bash
agentic-engineering % uv run ruff format
4 files left unchanged
```

- `uv run ruff check .`
```bash
agentic-engineering % uv run ruff check .
All checks passed!
```

- `uv run pyright`
```bash
agentic-engineering % uv run pyright
0 errors, 0 warnings, 0 informations
```
- `uv run pytest -q`
```bash
agentic-engineering % uv run pytest -q
..                                          [100%]
2 passed in 0.01s
```
- `uv run ae doctor`
```bash
agentic-engineering % uv run ae doctor
agentic-engineering doctor
- python_version: 3.12.12
- platform: macOS-15.6.1-arm64-arm-64bit
- GEMINI_API_KEY set: True
```

## Notes / surprises
- Error `ModuleNotFoundError: No module named 'agentic_engineering'` occurs because my source code is in a `src` directory (a "src layout"), and `pytest` does not automatically add the `src` folder to the Python path.
```bash
=============================================================== ERRORS ===============================================================
_____________________________________________ ERROR collecting tests/unit/test_doctor.py _____________________________________________
ImportError while importing test module '/Users/edwardcheu/AE/agentic-engineering/tests/unit/test_doctor.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
../../.local/share/uv/python/cpython-3.12.12-macos-aarch64-none/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tests/unit/test_doctor.py:1: in <module>
    from agentic_engineering.doctor import collect_doctor_report, render_doctor_report
E   ModuleNotFoundError: No module named 'agentic_engineering'
====================================================== short test summary info =======================================================
ERROR tests/unit/test_doctor.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
1 error in 0.03s
```
- Issue: `ae` and `agentic_engineering` module being missing due to project not being installed.
```bash
agentic-engineering % uv run ae doctor
error: Failed to spawn: `ae`
  Caused by: No such file or directory (os error 2)
agentic-engineering % uv run python -m agentic_engineering doctor
/Users/edwardcheu/AE/agentic-engineering/.venv/bin/python3: No module named agentic_engineering
```
- Issue: GEMINI_API_KEY set: False
Root cause: .env file isn't loaded into the Python process.
The fix: Add `python-dotenv`
  1. Add the dependency:
  ```bash
  uv add python-dotenv
  ```
  2. Update `src/agentic_engineering/__main__.py`:
  ```python
  // ...existing code...
  import argparse
  from dotenv import load_dotenv
  
  // ...existing code...
  def main(argv: list[str] | None = None) -> int:
      load_dotenv()  # <--- Add this line
      parser = build_parser()
  // ...existing code...
  ```

- **Surprise: `python-dotenv` vs. Shell/Gemini CLI**
  - Even after setting up `python-dotenv`, the Gemini CLI still couldn't find the API key. 
  - **Realization**: `python-dotenv` only loads variables into the *Python process memory*. It doesn't export them to the shell, so external tools (like the Gemini CLI) or `echo` commands still see nothing.

- **The Fix: `direnv` for Shell-Level Environment Management**
  - To make the key available to *everything* in the terminal (Python, Gemini CLI, shell scripts), I switched to `direnv`.
  - **The "Gotcha"**: Simply creating an `.envrc` with `dotenv` isn't enough. You must hook `direnv` into your shell.
  - **Step 1**: Add the hook to `~/.zshrc`:
    ```bash
    echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc
    ```
  - **Step 2**: Allow the directory:
    ```bash
    direnv allow
    ```

- **Verification & Cleanup**
  - Confirming the key is present in the shell:
    ```bash
    echo "${GEMINI_API_KEY:+set}"  # should print "set"
    ```
  - Now that `direnv` handles the environment globally for this folder, I have remove `python-dotenv` to keep the code lean and verifirf the main script still picks it up from the shell.
