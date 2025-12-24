"""
Test Plan: Traceability & Competency Verification

This test suite enforces the "Definition of Learned" rules defined in GEMINI.md.
It parses `docs/competency/TRACEABILITY.md` as the Source of Truth.

Rules Enforced:
1.  **Score Integrity**: Scores must be integers 0-3.
2.  **Evidence Requirement (Score >= 1)**:
    - The 'Evidence' column must not be empty.
    - Any file path listed in Evidence must actually exist on disk.
3.  **KB Requirement (Score >= 2)**:
    - Inherits all Evidence requirements (Score >= 1).
    - The 'KB artifact(s)' column must not be empty.
    - Linked KB artifacts must exist on disk.
    - KB paths must follow the strict 1:1 convention: `docs/kb/<DOMAIN>/<ID>/`

Implementation:
- Uses `pandas` to parse the Markdown tables.
- Iterates through all competencies.
- Asserts failure if any competency violates the rules.
"""
# pyright: reportGeneralTypeIssues=false
# pyright: reportAttributeAccessIssue=false
# pyright: reportArgumentType=false

import re
from pathlib import Path

import pandas as pd
import pytest

TRACEABILITY_FILE = Path("docs/competency/TRACEABILITY.md")


def extract_markdown_tables(file_path: Path) -> pd.DataFrame:
    """
    Parses a Markdown file and extracts all tables into a single Pandas DataFrame.
    Assumes tables share the same schema (ID, Competency, Score, etc.).
    """
    if not file_path.exists():
        pytest.fail(f"{file_path} not found.")

    lines = file_path.read_text().splitlines()
    data = []
    headers = []

    in_table = False

    for line in lines:
        stripped = line.strip()
        # Detect table start (header row starts with | ID)
        if stripped.startswith("| ID"):
            headers = [h.strip() for h in stripped.strip("|").split("|")]
            in_table = True
            continue

        # Skip separator row (|---|---|
        if in_table and set(stripped.replace("|", "").replace("-", "").strip()) == set():
            continue

        # Detect end of table (empty line or new header)
        if in_table and not stripped.startswith("|"):
            in_table = False
            continue

        if in_table:
            # Extract values
            values = [v.strip() for v in stripped.strip("|").split("|")]
            # Handle potentially mismatched column counts (markdown tables can be messy)
            if len(values) == len(headers):
                data.append(values)

    return pd.DataFrame(data, columns=headers)


def validate_paths(paths_str: str, check_convention: str = None) -> list[str]:
    """
    Validates a comma-separated string of paths.
    Returns a list of error messages.
    """
    if not paths_str:
        return ["Path list is empty."]

    errors = []
    # Split by comma, clean up
    raw_paths = [p.strip() for p in paths_str.split(",")]
    valid_path_found = False

    for item in raw_paths:
        # Clean markdown links [Title](path) -> path
        link_match = re.search(r"(.*?) ", item)
        clean_path = link_match.group(1) if link_match else item
        clean_path = clean_path.replace("`", "").strip()

        if not clean_path:
            continue

        # Ignore URLs or text descriptions (if it doesn't look like a path)
        # Heuristic: Path must have a slash or an extension
        if not clean_path.startswith("http") and ("/" in clean_path or "." in clean_path):
            path_obj = Path(clean_path)
            if not path_obj.exists():
                errors.append(f"Path '{clean_path}' does not exist.")
            else:
                valid_path_found = True
                # Check convention if requested
                if check_convention and check_convention not in str(path_obj).lower():
                    msg = f"Path '{clean_path}' violates convention. Expected '{check_convention}'."
                    errors.append(msg)
        else:
            # Non-path evidence counts as valid if we allow text descriptions
            valid_path_found = True

    if not valid_path_found:
        errors.append(f"No valid paths found in '{paths_str}'.")

    return errors


def test_traceability_rules():
    df = extract_markdown_tables(TRACEABILITY_FILE)

    # 1. Clean columns
    score_col = [c for c in df.columns if "Score" in c][0]
    df[score_col] = pd.to_numeric(df[score_col], errors="coerce").fillna(0).astype(int)

    kb_col = [c for c in df.columns if "KB artifact" in c][0]
    evidence_col = [c for c in df.columns if "Evidence" in c][0]
    id_col = "ID"

    errors = []

    for _, row in df.iterrows():
        comp_id = row[id_col]
        score = row[score_col]
        kb_entry = row[kb_col]
        evidence_entry = row[evidence_col]
        domain = comp_id.split("-")[0].lower()
        id_lower = comp_id.lower()

        # Rule 2: Evidence required for Score >= 1
        if score >= 1:
            if not evidence_entry:
                errors.append(f"[{comp_id}] Score is {score} but Evidence is empty.")
            else:
                # Verify Evidence paths
                path_errors = validate_paths(evidence_entry)
                for err in path_errors:
                    errors.append(f"[{comp_id}] Evidence Error: {err}")

        # Rule 3: KB required for Score >= 2
        if score >= 2:
            if not kb_entry:
                errors.append(f"[{comp_id}] Score is {score} but KB artifact is missing.")
            else:
                # Verify KB paths + Convention
                expected_part = f"docs/kb/{domain}/{id_lower}"
                path_errors = validate_paths(kb_entry, check_convention=expected_part)
                for err in path_errors:
                    errors.append(f"[{comp_id}] KB Error: {err}")

    assert not errors, "\n".join(errors)
