"""
Test Suite: Traceability Failure Modes

This verification suite ensures that `test_traceability.py` correctly detects violations.
It uses a mocked `TRACEABILITY.md` content to trigger expected failures.
"""
# pyright: reportGeneralTypeIssues=false
# pyright: reportAttributeAccessIssue=false
# pyright: reportArgumentType=false

from unittest.mock import patch

import pytest

from tests.unit.test_traceability import (  # type: ignore
    extract_markdown_tables,
    test_traceability_rules,
)

# Mock content with intentional violations

# Split lines to satisfy line length limit
MOCK_BROKEN_TRACEABILITY = """
| ID | Competency | Score (0-3) | KB artifact(s) | Evidence | Product usage | Status | Notes |
|---|---|---|---|---|---|---|---|
| TST-01 | Missing Evidence | 1 | | | | Evidence only | Score 1 requires evidence |
| TST-02 | Broken Evidence Path | 1 | | `docs/fake_evidence.md` | | Evidence only | Path missing |
| TST-03 | Broken KB Path | 2 | `docs/kb/wrong/place.md` | `README.md` | | Complete | Bad path |
"""


@pytest.fixture
def mock_traceability_df(tmp_path):
    """Creates a DataFrame from the broken mock content."""
    # We create a temporary file to use the existing extraction logic
    p = tmp_path / "TRACEABILITY.md"
    p.write_text(MOCK_BROKEN_TRACEABILITY)
    return extract_markdown_tables(p)


def test_traceability_validator_catches_errors(mock_traceability_df):
    """
    Verifies that the validator raises an AssertionError with specific messages
    when fed broken traceability data.
    """

    # We verify that extract_markdown_tables works on our mock
    assert not mock_traceability_df.empty

    # We patch the extractor in the main test to return our broken DF
    with patch(
        "tests.unit.test_traceability.extract_markdown_tables", return_value=mock_traceability_df
    ):
        with pytest.raises(AssertionError) as excinfo:
            test_traceability_rules()

        error_msg = str(excinfo.value)

        # 1. Check Score 1 missing evidence
        assert "[TST-01] Score is 1 but Evidence is empty." in error_msg

        # 2. Check Score 1 broken evidence path
        # Note: README.md exists, but docs/fake_evidence.md does not.
        assert "Evidence Error: Path 'docs/fake_evidence.md' does not exist." in error_msg
        assert "TST-02" in error_msg

        # 3. Check Score 2 KB existence
        # (it fails existence before convention because the file isn't there)
        # TST-03 has valid evidence (README.md)
        assert "KB Error: Path 'docs/kb/wrong/place.md' does not exist." in error_msg
        assert "TST-03" in error_msg
