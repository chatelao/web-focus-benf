# WEBFOCUS_TO_POSTGRE.md

## Concept: Migrating WebFOCUS Codebase to PostgreSQL

To successfully translate all features of a proprietary 4GL like WebFOCUS—which includes procedural logic, variable state, formatting, and database routing—a simple syntax parser like Lark is entirely insufficient.

### The Required Compiler Architecture

The most suitable construct is a full **Multi-Pass Source-to-Source Compiler (Transpiler) Architecture** utilizing an **Abstract Semantic Graph (ASG)** and an **Intermediate Representation (IR)**.

Furthermore, because WebFOCUS is a reporting engine and PostgreSQL is a relational database, you cannot target standard SQL; you must target a combination of **PL/pgSQL** (for procedural data logic) and a **decoupled middle-tier application** (for presentation logic).

To map legacy procedural state to modern relational systems, the architecture must move beyond syntax and understand context. The transpiler must ingest the WebFOCUS code, resolve its internal variables (`&VARIABLES` from the Dialogue Manager), build a mathematical representation of the logic (the ASG), optimize it from row-based processing to set-based relational algebra, and finally emit PL/pgSQL.

### Core Elements & Verified Sources

| Transpiler Construct | Role in WebFOCUS to PostgreSQL Migration | Verified Source / Reference |
| --- | --- | --- |
| **Advanced Parser Generator (e.g., ANTLR4)** | Replaces basic parsers (like Lark) to handle the extreme context-sensitivity and ambiguous grammar of legacy 4GLs, producing the initial Abstract Syntax Tree (AST). | *"The Definitive ANTLR 4 Reference"* by Terence Parr (ISBN: 978-1934356999) |
| **Abstract Semantic Graph (ASG) & Symbol Table** | Upgrades the AST by attaching meaning. It tracks the state of Dialogue Manager variables, `DEFINE` computations, and `MATCH` joins across the entire script execution lifecycle. | *"Compilers: Principles, Techniques, and Tools"* (The Dragon Book) by Aho, Lam, Sethi, Ullman |
| **Control Flow Graph (CFG) Optimizer** | Analyzes the WebFOCUS procedural loops and branching, attempting to collapse iterative row-by-row legacy processing into set-based, declarative SQL statements wherever possible. | [LLVM Compiler Infrastructure (IR and Optimization)](https://llvm.org/docs/Passes.html) |
| **PL/pgSQL Emitter** | The backend of the transpiler that writes the final output. It maps WebFOCUS features that cannot be vectorized (like complex stateful loops) into PostgreSQL Stored Procedures and Functions. | [PostgreSQL Official PL/pgSQL Documentation](https://www.postgresql.org/docs/current/plpgsql.html) |
