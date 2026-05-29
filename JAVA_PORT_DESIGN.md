# Java Port Design: WebFOCUS to PostgreSQL Transpiler

## 1. Introduction
This document outlines the high-level concept for porting the WebFOCUS to PostgreSQL Transpiler from Python to Java. The goal is to provide a robust, enterprise-ready JVM-based tool that maintains 100% functional parity with the existing Python implementation while leveraging the Java ecosystem for performance and integration.

## 2. Business Requirements & Use Cases
The business objectives remain unchanged from the original `CONCEPT.md`:

- **Business Case 1:** Migrating legacy reporting systems to open-source relational databases (PostgreSQL).
- **Business Case 2:** Standardizing WebFOCUS development through formal specification.
- **Use Case 1:** Automated transpilation of WebFOCUS requests to PostgreSQL Stored Procedures.
- **Use Case 2:** Analysis and optimization of legacy procedural logic for set-based execution.

## 3. Tech Stack Mapping

| Component | Python Implementation (Current) | Java Port (Target) |
| --- | --- | --- |
| **Language** | Python 3.10+ | Java 21 (LTS) |
| **Parser Generator** | ANTLR4 (Python3 Runtime) | ANTLR4 (Java Runtime) |
| **Template Engine** | Jinja2 | Apache FreeMarker |
| **CLI Framework** | argparse | Picocli |
| **Build System** | pip / requirements.txt | Apache Maven 3.9+ |
| **Testing** | unittest / pytest | JUnit 5 + AssertJ |
| **Logging** | logging module | SLF4J + Logback |
| **JSON/Serialization** | json module | Jackson |

## 4. Architecture

The Java port will follow the same multi-pass compiler architecture:

### 4.1 Frontend (ANTLR4 Java)
- Re-use the existing `.g4` grammars (`WebFocusReport.g4`, `MasterFile.g4`).
- Generate Java Lexer, Parser, and Visitors using the ANTLR4 Maven plugin.
- Implement `WebFocusReportVisitor` to construct the Java-based ASG.

### 4.2 Semantic Analysis (ASG & Symbol Table)
- **ASG Nodes:** Implement as Java `record` types or immutable classes where appropriate to represent the Abstract Semantic Graph.
- **Symbol Table:** Use a hierarchical `Map`-based structure to track Dialogue Manager variables and database fields.
- **Type System:** Port the `TypeInferrer` and `TypeMapper` logic to Java's type system.

### 4.3 Optimization (SSA-based IR)
- **Control Flow Graph (CFG):** Implement using a graph library (e.g., JGraphT) or a custom adjacency-list structure.
- **SSA Transformation:** Port the SSA transformer logic, including Phi-node insertion and variable renaming.
- **Optimizers:** Implement `ConstantPropagator`, `DeadCodeElimination`, and `RelationalLiftingOptimizer` as separate passes over the CFG.

### 4.4 Backend (FreeMarker Emitter)
- Use **Apache FreeMarker** to manage SQL templates.
- Port existing Jinja2 templates (`.sql`) to FreeMarker syntax (mostly syntax mapping like `{{ var }}` to `${var}`).
- Implement a `PostgresEmitter` class that traverses the optimized IR and populates FreeMarker models.

## 5. CLI Tool Design
The CLI will be implemented using **Picocli** to provide a professional command-line interface.

### Commands & Options
- `transpile`: Main command to convert `.fex` files.
    - `-i, --input`: Input file or directory.
    - `-o, --output`: Output directory.
    - `-m, --master-path`: Search paths for Master Files.
    - `--stats`: Display source code diagnostics and complexity.
- `check`: Validate WebFOCUS syntax without full transpilation.
- `lineage`: Output data lineage in JSON format.

### Example Usage
```bash
java -jar wf2pg-transpiler.jar transpile -i ./reports -o ./dist -m ./metadata --stats
```

## 6. Build & Dependency Management (Maven)
A `pom.xml` will manage dependencies:
- `antlr4-runtime`
- `freemarker`
- `picocli`
- `jackson-databind`
- `junit-jupiter`
- `slf4j-api`

## 7. Migration Strategy
1. **Infrastructure:** Set up Maven project and ANTLR4 plugin.
2. **ASG/IR Models:** Port the core data structures (`asg.py`, `ir.py`).
3. **Frontend:** Port `asg_builder.py` to Java Visitor implementation.
4. **Logic:** Port Symbol Table and Type Inference.
5. **Optimization:** Port SSA transformer and Relational Lifting logic.
6. **Backend:** Port Emitter and Templates.
7. **Verification:** Use the existing Python test suite to generate "Golden Files" and verify Java output parity.
