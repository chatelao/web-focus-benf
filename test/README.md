# WebFOCUS Transpiler Test Suite

This directory contains the test suite for the WebFOCUS to PostgreSQL transpiler. The tests are designed to verify the correctness of the ANTLR4 grammars and the parser implementation.

## Test Files Overview

- **`test_antlr_wf_parser.py`**: Focuses on verifying the ANTLR4 parser for WebFOCUS report requests. It covers:
    - Summarization commands (`SUMMARIZE`, `RECOMPUTE`, `SUBTOTAL`).
    - Output commands (`HOLD`, `PCHOLD`, `SAVE`, `SAVB`).
    - `WHERE` clauses and relational operators.
    - Basic `TABLE FILE` requests and sort phrases (`BY`, `ACROSS`).
    - Formatting commands (`HEADING`, `FOOTING`, `SUBHEAD`).
    - Verification of all `.fex` files in `test/samples/`.

- **`test_dm_commands.py`**: Tests procedural Dialogue Manager commands:
    - Conditional logic (`-IF ... THEN ... ELSE`).
    - Output and comments (`-TYPE`, `-*`).
    - Interleaved Dialogue Manager and `TABLE FILE` requests.

- **`test_dm_control_flow.py`**: Specifically targets control flow logic:
    - Labels and `-GOTO` branching.
    - Interleaved control flow within `TABLE FILE` blocks.

- **`test_master_file_parser.py`**: Verifies the parsing of WebFOCUS Master Files (`.mas`):
    - File, Segment, and Field declarations.
    - Attribute parsing (ALIAS, USAGE, TITLE, etc.).
    - `DEFINE` and `VARIABLE` declarations.

- **`test_prototype_parser.py`**: Integration tests using the `WebFocusParser` dispatcher. It ensures that both Master Files and Report Requests are correctly identified and parsed.

## Running Tests

To run the full test suite, ensure the `src` directory is in your `PYTHONPATH`:

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
python3 -m unittest discover test
```

For verbose output:

```bash
python3 -m unittest discover -v test
```

## Coverage Report

To generate a coverage report, install the `coverage` package:

```bash
pip install coverage
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
coverage run -m unittest discover test
coverage report -m
```

## Samples

The `test/samples/` directory contains real-world WebFOCUS `.fex` files used for regression testing and grammar verification. New samples should be added here to expand coverage.
