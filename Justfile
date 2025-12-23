set shell := ["bash", "-c"]

# List available commands
default:
    @just --list

# Run all PR-gating checks (formatting, linting, types, tests)
check: check-fmt lint type test

# Check code formatting (fails if unformatted)
check-fmt:
    uv run ruff format --check .

# Auto-format code and fix lint issues
fmt:
    uv run ruff check --fix .
    uv run ruff format .

# Run linting
lint:
    uv run ruff check .

# Run type checking
type:
    uv run pyright

# Run tests
test:
    uv run pytest -q

# Run the environment doctor
doctor:
    uv run ae doctor

# Install pre-commit hooks
install-hooks:
    uv run pre-commit install

# Update pre-commit hooks to their latest versions
update-hooks:
    uv run pre-commit autoupdate

# Run pre-commit hooks on all files (useful for fixing whitespace/formatting)
fix-hooks:
    uv run pre-commit run --all-files

# === Pre-commit Verification Flows ===

# Verify code changes (full suite)
verify-code: check

# Verify documentation changes (minimal check)
verify-docs:
    @echo "Verifying docs..."
    @echo "- Check for broken links (manual)"
    @echo "- Review rendered markdown"
    git status
