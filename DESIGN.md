# DESIGN

## Detailed Design
The transpiler is designed as a pipeline that transforms WebFOCUS code into PostgreSQL-compatible logic.

### 1. Frontend: ANTLR4 Parser
- Utilizes ANTLR4 for its powerful LL(*) parsing capabilities and mature ecosystem.
- Generates an Abstract Syntax Tree (AST) from WebFOCUS source files, including Dialogue Manager and TABLE FILE requests.

### 2. Semantic Analysis: Abstract Semantic Graph (ASG)
- A Custom Object Model (Python) builds the ASG from the AST.
- Resolves Dialogue Manager variables (`&VARS`), `DEFINE` computations, and `MATCH` joins.
- Maintains a Symbol Table for scope management and type tracking.

### 3. Optimization: SSA-based Intermediate Representation (IR)
- Translates the ASG into a Control Flow Graph (CFG) using Static Single Assignment (SSA) form.
- Performs dead code elimination, constant propagation, and attempts to collapse row-based procedural logic into set-based relational algebra.

### 4. Backend: Jinja2 Emitter
- Uses Jinja2 templates to produce the final output.
- Emits PL/pgSQL for data-heavy logic and stored procedures.
- Generates decoupled application logic for presentation-related features.

## Architecture
Multi-pass source-to-source compiler architecture with clear separation between language frontend, semantic mid-tier, and database backend.

## Tech Stack
- **Python:** Primary development language for transpiler logic.
- **ANTLR4:** Parser generator for lexing and parsing.
- **Jinja2:** Template engine for code generation.
- **GitHub Actions:** CI/CD for automated testing and verification.
- **Read the Docs:** Hosting for technical documentation and language specifications.
