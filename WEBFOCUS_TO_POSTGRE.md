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

## Detailed Reasoning on Implementation Alternatives

### 1. Advanced Parser Generator
*   **Alternative A: ANTLR4** – Highly mature, supports LL(*) parsing, and has a vast ecosystem of existing grammars.
*   **Alternative B: Tree-sitter** – Optimized for speed and incremental parsing (ideal for IDEs), but slightly less flexible for massive batch transpilation of legacy 4GL.
*   **Alternative C: Hand-written Recursive Descent** – Offers absolute control over the most "broken" or ambiguous parts of the grammar, but is extremely expensive to maintain.
*   **Final Choice: ANTLR4.** It provides the perfect balance of power and maintainability. Its Visitor/Listener patterns allow for clean separation between parsing and semantic analysis.

### 2. Abstract Semantic Graph (ASG) & Symbol Table
*   **Alternative A: Custom Object Model (Python/Java)** – Building a domain-specific hierarchy of classes to represent semantics.
*   **Alternative B: NetworkX (Graph Library)** – Leveraging a dedicated library for graph traversals and cycle detection.
*   **Alternative C: Persistent Graph Database (Neo4j)** – Useful for extremely large codebases where cross-script dependencies need to be queried.
*   **Final Choice: Custom Object Model.** Given the specific needs of WebFOCUS (tracking Dialogue Manager variables vs. database fields), a custom model allows for the most precise type-safety and semantic validation.

### 3. Control Flow Graph (CFG) Optimizer
*   **Alternative A: SSA-based Custom IR** – Implementing Static Single Assignment form to optimize variable usage and control flow.
*   **Alternative B: LLVM IR** – Mapping WebFOCUS to LLVM to use industrial-strength optimizers.
*   **Alternative C: MLIR (Multi-Level Intermediate Representation)** – A modern framework for building high-level dialect-aware compilers.
*   **Final Choice: SSA-based Custom IR.** SSA is the "gold standard" for identifying redundant logic and dead code. It is specifically suited for converting legacy procedural loops into declarative, set-based PostgreSQL logic.

### 4. PL/pgSQL Emitter
*   **Alternative A: Jinja2 (Templating)** – Using a powerful text-based templating engine.
*   **Alternative B: StringTemplate** – A stricter templating engine (often paired with ANTLR) that enforces model-view separation.
*   **Alternative C: Programmatic AST Unparsing** – Generating code by traversing the final IR and printing strings directly.
*   **Final Choice: Jinja2.** It is highly flexible and readable, making it easy to iterate on the generated PL/pgSQL code patterns and ensure they follow PostgreSQL best practices.
