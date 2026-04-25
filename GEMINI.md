# Goal

Transpile WebFOCUS programming language codebases to PostgreSQL (PL/pgSQL) using a multi-pass source-to-source compiler architecture.

# Structure

- `CONCEPT.md`: High-level architecture (Frontend, ASG, IR, Backend) and Business/Use Cases.
- `DESIGN.md`: Detailed design of the transpiler pipeline and the chosen tech stack (ANTLR4, SSA IR, Jinja2).
- `ROADMAP.md`: Task tracking for the transpiler development, organized by chapters.
- `TECHNICAL_DEBTS.md`: Log of architectural or implementation debts.
- `WEBFOCUS_TO_POSTGRE.md`: The core strategy and technical reasoning for the migration target.
- `/specifications/`: External documentation and manuals converted to Markdown.
- `/src/`: Transpiler source code (ANTLR4 grammars, ASG/IR logic, Jinja2 templates).
- `/test/`: Test suite, including real-world WebFOCUS samples and regression tests.

# HOWTO

- Keep `src/install.sh` to install all tools and dependencies (including ANTLR4 runtime).
- Develop the ANTLR4 grammar based on the official manuals in `/specifications/`.
- Use `https://docs.tibco.com/pub/wf-wf/8207.27.0/doc/pdf/TIB_wfwf_8207.27.0_cr_language.pdf` as the primary reference.

# Testing Locally & with Github Action Workflow

- Maintain a CI/CD pipeline that runs on every commit.
- Use `test/install.sh` to install testing-specific dependencies.
- Verify transpilation results against expected PL/pgSQL patterns.
- Add caching to the Github action workflows to speed up builds.

# Jules Agent Instructions

## ROADMAP rules
- The `ROADMAP.md` is automatically managed by the `Jules Automation` workflow.
- When working on tasks from the `ROADMAP.md`, always **execute from bottom to top**.
- New tasks are added to the top of the list.
- Tasks are marked as completed with a timestamp when the corresponding issue is closed.
