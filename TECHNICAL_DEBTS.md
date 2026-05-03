# TECHNICAL DEBTS

This file logs technical debts such as outdated components, security flaws, or old patterns.

- [x] **Architectural Migration:** The project is transitioning from a Lark-based syntax parser to an ANTLR4-based multi-pass transpiler. Existing Lark parsers in `src/wf_parser.py` and `src/master_file_parser.py` have been migrated to ANTLR4. (Completed at 2026-04-27 12:00:00)
- [x] **Lark Dependency:** Remove `lark` from `requirements.txt` once the migration to ANTLR4 is complete. (Completed at 2026-05-03 10:20:00)
- [x] **Test Suite Alignment:** Existing tests for Lark parsers must be updated to target the new ANTLR4 frontend. (Completed at 2026-05-03 10:15:00)
