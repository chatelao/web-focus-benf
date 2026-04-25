# CONCEPT

## Overall structure
The project is a Multi-Pass Source-to-Source Compiler (Transpiler) designed to migrate legacy WebFOCUS codebases to modern PostgreSQL environments. It formally defines the WebFOCUS syntax and provides a robust translation layer to PL/pgSQL and decoupled middle-tier application logic.

## Business Cases & Use Cases
- Business Case 1: Migrating legacy reporting systems to open-source relational databases.
- Business Case 2: Standardizing WebFOCUS development through formal specification.
- Use Case 1: Automated transpilation of WebFOCUS requests to PostgreSQL Stored Procedures.
- Use Case 2: Analysis and optimization of legacy procedural logic for set-based execution.

## High-Level Architecture
The architecture follows a multi-pass compiler pattern:
1.  **Frontend (ANTLR4):** Lexes and parses WebFOCUS code into an Abstract Syntax Tree (AST).
2.  **Semantic Analysis (ASG & Symbol Table):** Enhances the AST with semantic meaning, resolving variables (Dialogue Manager) and tracking field/variable state.
3.  **Optimization (SSA-based IR):** Converts the ASG into a Control Flow Graph (CFG) in Static Single Assignment (SSA) form to optimize logic and enable set-based transformations.
4.  **Backend (Jinja2 Emitter):** Generates optimized PL/pgSQL code and middle-tier presentation logic from the IR.
