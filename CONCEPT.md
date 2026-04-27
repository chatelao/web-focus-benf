# CONCEPT

## Overview
The project is a Multi-Pass Source-to-Source Compiler (Transpiler) designed to migrate legacy WebFOCUS codebases to modern PostgreSQL environments. It formally defines the WebFOCUS syntax and provides a robust translation layer to PL/pgSQL and decoupled middle-tier application logic.

To successfully translate all features of a proprietary 4GL like WebFOCUS—which includes procedural logic, variable state, formatting, and database routing—a simple syntax parser is insufficient. The architecture must move beyond syntax and understand context, resolving internal variables, building an Abstract Semantic Graph (ASG), and optimizing it into set-based relational algebra.

## Business Cases & Use Cases
- Business Case 1: Migrating legacy reporting systems to open-source relational databases.
- Business Case 2: Standardizing WebFOCUS development through formal specification.
- Use Case 1: Automated transpilation of WebFOCUS requests to PostgreSQL Stored Procedures.
- Use Case 2: Analysis and optimization of legacy procedural logic for set-based execution.

## High-Level Architecture
The architecture follows a multi-pass compiler pattern utilizing an Abstract Semantic Graph (ASG) and an Intermediate Representation (IR).

| Transpiler Construct | Role in WebFOCUS to PostgreSQL Migration | Verified Source / Reference |
| --- | --- | --- |
| **Advanced Parser Generator (e.g., ANTLR4)** | Replaces basic parsers to handle the extreme context-sensitivity and ambiguous grammar of legacy 4GLs, producing the initial Abstract Syntax Tree (AST). | *"The Definitive ANTLR 4 Reference"* by Terence Parr (ISBN: 978-1934356999) |
| **Abstract Semantic Graph (ASG) & Symbol Table** | Upgrades the AST by attaching meaning. It tracks the state of Dialogue Manager variables, `DEFINE` computations, and `MATCH` joins across the entire script execution lifecycle. | *"Compilers: Principles, Techniques, and Tools"* (The Dragon Book) by Aho, Lam, Sethi, Ullman |
| **Control Flow Graph (CFG) Optimizer** | Analyzes the WebFOCUS procedural loops and branching, attempting to collapse iterative row-by-row legacy processing into set-based, declarative SQL statements wherever possible. | [LLVM Compiler Infrastructure (IR and Optimization)](https://llvm.org/docs/Passes.html) |
| **PL/pgSQL Emitter** | The backend of the transpiler that writes the final output. It maps WebFOCUS features that cannot be vectorized (like complex stateful loops) into PostgreSQL Stored Procedures and Functions. | [PostgreSQL Official PL/pgSQL Documentation](https://www.postgresql.org/docs/current/plpgsql.html) |

### 1. Frontend (ANTLR4)
*   **Implementation Choice: ANTLR4.** Highly mature, supports LL(*) parsing, and has a vast ecosystem of existing grammars. Its Visitor/Listener patterns allow for clean separation between parsing and semantic analysis.
*   **Role:** Lexes and parses WebFOCUS code into an Abstract Syntax Tree (AST).

### 2. Semantic Analysis (ASG & Symbol Table)
*   **Implementation Choice: Custom Object Model.** Given the specific needs of WebFOCUS (tracking Dialogue Manager variables vs. database fields), a custom model allows for the most precise type-safety and semantic validation.
*   **Role:** Enhances the AST with semantic meaning, resolving variables (Dialogue Manager) and tracking field/variable state.

### 3. Optimization (SSA-based IR)
*   **Implementation Choice: SSA-based Custom IR.** SSA (Static Single Assignment) is the "gold standard" for identifying redundant logic and dead code. It is specifically suited for converting legacy procedural loops into declarative, set-based PostgreSQL logic.
*   **Role:** Converts the ASG into a Control Flow Graph (CFG) in SSA form to optimize logic and enable set-based transformations.

### 4. Backend (Jinja2 Emitter)
*   **Implementation Choice: Jinja2.** It is highly flexible and readable, making it easy to iterate on the generated PL/pgSQL code patterns and ensure they follow PostgreSQL best practices.
*   **Role:** Generates optimized PL/pgSQL code and middle-tier presentation logic from the IR.
