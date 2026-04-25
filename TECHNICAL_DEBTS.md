# TECHNICAL DEBTS

This file logs technical debts such as outdated components, security flaws, or old patterns.

- [ ] **Architectural Migration:** The project is transitioning from a Lark-based syntax parser to an ANTLR4-based multi-pass transpiler. Existing Lark parsers in `src/wf_parser.py` and `src/master_file_parser.py` need to be migrated to ANTLR4.
- [ ] **Lark Dependency:** Remove `lark` from `requirements.txt` once the migration to ANTLR4 is complete.
- [ ] **Test Suite Alignment:** Existing tests for Lark parsers must be updated to target the new ANTLR4 frontend.
