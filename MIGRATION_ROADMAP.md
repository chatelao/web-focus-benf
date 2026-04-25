# Migration Roadmap: Lark to ANTLR4/Jinja2 Transpiler

This document outlines the strategic transition from the legacy Lark-based parser to the modern Multi-Pass Source-to-Source Compiler architecture targeting PostgreSQL.

## Phase 1: Frontend Migration (Lark to ANTLR4)
The current Lark-based parsers (`wf_parser.py` and `master_file_parser.py`) are legacy technical debt and must be replaced by ANTLR4 grammars.

**Note on Dual Grammar Architecture:**
The frontend is split into two distinct ANTLR4 grammars to reflect the dual nature of WebFOCUS:
1. `MasterFile.g4`: Handles data descriptions and metadata (Synonyms).
2. `WebFocusReport.g4`: Handles procedural report logic and `TABLE FILE` requests.

- [x] **1.1 Master File Grammar:** Complete the transition of Master File parsing from Lark to ANTLR4. (Completed: `src/MasterFile.g4` is implemented and used by `src/master_file_parser.py`)
- [ ] **1.2 WebFOCUS Report Grammar:** Port the EBNF grammar from `src/wf_parser.py` to ANTLR4 (.g4) format.
  - [x] **1.2.1 Core request structure:** TABLE FILE verb, END command, and qualified names. (Implemented in `src/WebFocusReport.g4`)
  - [x] **1.2.2 Verb commands:** PRINT, SUM, LIST, COUNT, WRITE, ADD and field lists with AS phrases. (Implemented in `src/WebFocusReport.g4`)
  - [ ] **1.2.3 Sort phrases:** BY and ACROSS with sort options (HIGHEST, LOWEST, etc.).
  - [ ] **1.2.4 Formatting:** HEADING, FOOTING, and ON (SUBHEAD/SUBFOOT).
  - [ ] **1.2.5 Summarization and Output:** SUBTOTAL, SUMMARIZE, RECOMPUTE and ON TABLE (HOLD, PCHOLD, etc.).
- [ ] **1.3 Dialogue Manager Grammar:** Define ANTLR4 grammar rules for procedural Dialogue Manager commands (-SET, -IF, -GOTO, etc.).
- [ ] **1.4 Unified Lexer/Parser:** Ensure the ANTLR4 frontend can handle the context-sensitive nature of WebFOCUS where Dialogue Manager and TABLE FILE requests are interleaved.

## Phase 2: Semantic Analysis (ASG Construction)
Move beyond syntax trees to an Abstract Semantic Graph (ASG) that understands the meaning of the code.

- [ ] **2.1 Custom Object Model:** Implement the Python classes representing WebFOCUS semantic constructs.
- [ ] **2.2 Symbol Table:** Build a robust symbol table to track variable state, especially for Dialogue Manager variables (`&VARS`).
- [ ] **2.3 Type Inference:** Implement logic to infer data types from Master Files and `DEFINE` statements.

## Phase 3: Optimization (SSA-based IR)
Transform the ASG into a Control Flow Graph (CFG) using Static Single Assignment (SSA) form to enable relational optimizations.

- [ ] **3.1 CFG Generation:** Map procedural logic to a graph-based representation.
- [ ] **3.2 SSA Transformation:** Implement phi-nodes and variable renaming for precise analysis.
- [ ] **3.3 Relational Lifting:** Identify row-based procedural loops that can be "lifted" into set-based SQL queries.

## Phase 4: Backend Emission (Jinja2)
Use Jinja2 templates to generate the final PostgreSQL and middle-tier code.

- [ ] **4.1 PL/pgSQL Templates:** Create Jinja2 templates for Stored Procedures and Functions.
- [ ] **4.2 Query Emitter:** Implement logic to generate optimized PostgreSQL queries from the IR.
- [ ] **4.3 Presentation Logic:** Generate decoupled middle-tier logic for formatting and reporting.

## Phase 5: Verification and Parity
Ensure the new system produces correct results and maintains parity with the legacy parser.

- [ ] **5.1 Regression Suite:** Run the existing test suite against the new ANTLR4-based frontend.
- [ ] **5.2 Sample Validation:** Validate the transpiler output against real-world WebFOCUS samples in `test/samples/`.
- [ ] **5.3 Performance Benchmarking:** Compare the execution of the generated PL/pgSQL against original WebFOCUS report execution.

## Phase 6: Decommissioning
- [ ] **6.1 Remove Lark Dependency:** Delete Lark-related code and remove `lark` from `requirements.txt`.
- [ ] **6.2 Clean Up Technical Debt:** Close out remaining items in `TECHNICAL_DEBTS.md`.
