# Migration Roadmap: Lark to ANTLR4/Jinja2 Transpiler

This document outlines the strategic transition from the legacy Lark-based parser to the modern Multi-Pass Source-to-Source Compiler architecture targeting PostgreSQL.

## Phase 1: Frontend Migration (Lark to ANTLR4)
The current Lark-based parsers (`wf_parser.py` and `master_file_parser.py`) are legacy technical debt and must be replaced by ANTLR4 grammars.

**Note on Dual Grammar Architecture:**
The frontend is split into two distinct ANTLR4 grammars to reflect the dual nature of WebFOCUS:
1. `MasterFile.g4`: Handles data descriptions and metadata (Synonyms).
2. `WebFocusReport.g4`: Handles procedural report logic and `TABLE FILE` requests.

- [x] **1.1 Master File Grammar:** Complete the transition of Master File parsing from Lark to ANTLR4. (Completed: `src/MasterFile.g4` is implemented and used by `src/master_file_parser.py`)
- [x] 1.2 WebFOCUS Report Grammar: Port the EBNF grammar from `src/wf_parser.py` to ANTLR4 (.g4) format.
  - [x] **1.2.1 Core request structure:** TABLE FILE verb, END command, and qualified names. (Implemented in `src/WebFocusReport.g4`)
  - [x] **1.2.2 Verb commands:** PRINT, SUM, LIST, COUNT, WRITE, ADD and field lists with AS phrases. (Implemented in `src/WebFocusReport.g4`)
  - [x] **1.2.3 Sort phrases:** BY and ACROSS with sort options (HIGHEST, LOWEST, etc.). (Implemented in `src/WebFocusReport.g4`)
  - [x] **1.2.4 Formatting:** HEADING, FOOTING, and ON (SUBHEAD/SUBFOOT). (Implemented in `src/WebFocusReport.g4`)
  - [x] **1.2.5 Summarization and Output:** SUBTOTAL, SUMMARIZE, RECOMPUTE and ON TABLE (HOLD, PCHOLD, etc.). (Implemented in `src/WebFocusReport.g4`)
  - [x] 1.2.6 Expressions and WHERE clauses: Support filtering with relational operators. (Implemented in `src/WebFocusReport.g4`)
- [x] 1.3 Dialogue Manager Grammar: Define ANTLR4 grammar rules for procedural Dialogue Manager commands.
  - [x] 1.3.1 Variable Assignment: -SET and system variables. (Implemented in `src/WebFocusReport.g4`)
  - [x] 1.3.2 Control Flow:
    - [x] 1.3.2.1 Labels and -GOTO. (Implemented in `src/WebFocusReport.g4`)
    - [x] 1.3.2.2 Conditional Branching: -IF ... THEN ... ELSE ... (Implemented in `src/WebFocusReport.g4`)
    - [x] 1.3.2.3 Loops: -REPEAT with WHILE/UNTIL/STEP. (Implemented in `src/WebFocusReport.g4`)
  - [x] 1.3.3 File/Execution and Misc:
    - [x] 1.3.3.1 File Inclusion: -INCLUDE. (Implemented in `src/WebFocusReport.g4`)
    - [x] 1.3.3.2 Execution Control: -RUN and -EXIT. (Implemented in `src/WebFocusReport.g4`)
    - [x] 1.3.3.3 Output and Comments: -TYPE and -*. (Implemented in `src/WebFocusReport.g4`)
- [x] **1.4 Unified Lexer/Parser:** Ensure the ANTLR4 frontend can handle the context-sensitive nature of WebFOCUS where Dialogue Manager and TABLE FILE requests are interleaved.
  - [x] 1.4.1 Environment Commands: Support `JOIN` and `SET` (non-DM) commands. (Implemented in `src/WebFocusReport.g4`)
  - [x] 1.4.2 Virtual Fields: Support `DEFINE FILE ... END` for temporary field definitions.
    - [x] 1.4.2.1 Block Structure: Support `DEFINE FILE filename ... END`.
    - [x] 1.4.2.2 Basic Assignments: Support `field/format = expression;` within the block.
    - [x] 1.4.2.3 Expressions: Full support for arithmetic, character, and logical expressions in `DEFINE`.
  - [x] 1.4.3 Calculated Values: Support `COMPUTE field[/format] = expression;` within report requests.

## Phase 2: Semantic Analysis (ASG Construction)
Move beyond syntax trees to an Abstract Semantic Graph (ASG) that understands the meaning of the code.

- [x] **2.1 Custom Object Model:**
  - [x] 2.1.1 Base ASG nodes: Implement base classes for Expressions, Commands, and Statements. (Implemented in `src/asg.py`)
  - [x] 2.1.2 Data Model nodes: Implement nodes for Master Files, Segments, and Fields. (Implemented in `src/asg.py`)
  - [x] 2.1.3 Procedural nodes:
    - [x] 2.1.3.1 DM Control Flow: Implement nodes for -GOTO, -IF, and -REPEAT. (Implemented in `src/asg.py`)
    - [x] 2.1.3.2 DM Actions: Implement nodes for -SET, -TYPE, and -INCLUDE. (Implemented in `src/asg.py`)
  - [x] 2.1.4 Report Request nodes: Implement nodes for TABLE FILE, Verbs, Sort phrases, Filters, and Formatting. (Implemented in `src/asg.py`)
  - [x] 2.1.5 Environment and Virtual Field nodes: Implement nodes for JOIN, SET, and DEFINE. (Implemented in `src/asg.py`)
  - [x] 2.1.6 Expression nodes: Implement nodes for arithmetic and logical operations. (Implemented in `src/asg.py`)
- [x] **2.2 Symbol Table:**
  - [x] 2.2.1 Scoping: Implement block-level and global scopes. (Implemented in `src/symbol_table.py`)
  - [x] 2.2.2 Variable Resolution:
    - [x] 2.2.2.1 Dialogue Manager variables. (Implemented in `src/symbol_resolver.py`)
    - [x] 2.2.2.2 Field references. (Implemented in `src/symbol_resolver.py`)
  - [x] 2.2.3 Metadata Integration:
    - [x] 2.2.3.1 Master File Registry: Management of loaded Master Files. (Implemented in `src/metadata_registry.py`)
    - [x] 2.2.3.2 Schema Binding: Resolving field names to Master File segments. (Implemented in `src/symbol_resolver.py`)
- [x] **2.3 Type Inference:**
  - [x] 2.3.1 Literal Typing: Infer types for numeric and string constants. (Implemented in `src/type_inferrer.py`)
  - [x] 2.3.2 Expression Typing:
    - [x] 2.3.2.1 Arithmetic Expressions. (Implemented in `src/type_inferrer.py`)
    - [x] 2.3.2.2 Logical and Relational Expressions. (Implemented in `src/type_inferrer.py`)
    - [x] 2.3.2.3 Built-in Functions. (Implemented in `src/type_inferrer.py`)
  - [x] 2.3.3 Metadata Typing: Resolve field types from Master File metadata. (Implemented in `src/type_inferrer.py`)
- [ ] **2.4 ASG Builder:** Implement the visitor to transform ANTLR4 parse tree to ASG.
  - [x] 2.4.1 Visitor Infrastructure: Base visitor class and dispatcher. (Implemented in `src/asg_builder.py`)
  - [x] 2.4.2 Expression Builder: Support all arithmetic and logical expressions. (Implemented in `src/asg_builder.py`)
  - [x] 2.4.3 Dialogue Manager Builder: Support -SET, -IF, -GOTO, -REPEAT, etc. (Implemented in `src/asg_builder.py`)
  - [x] 2.4.4 Report Request Builder:
    - [x] 2.4.4.1 Core structure: TABLE FILE and END command. (Implemented in `src/asg_builder.py`)
    - [x] 2.4.4.2 Verbs and Fields: PRINT, SUM, etc., with AS phrases and prefix operators. (Implemented in `src/asg_builder.py`)
    - [x] 2.4.4.3 Sort phrases: BY and ACROSS with sort options. (Implemented in `src/asg_builder.py`)
    - [x] 2.4.4.4 Filtering:
      - [x] 2.4.4.4.1 WHERE clauses with relational expressions. (Implemented in `src/asg_builder.py`)
      - [x] 2.4.4.4.2 WHERE TOTAL clauses for post-aggregation filtering. (Implemented in `src/asg_builder.py`)
    - [x] 2.4.4.5 Formatting and Summarization:
      - [x] 2.4.4.5.1 HEADING and FOOTING commands. (Implemented in `src/asg_builder.py`)
      - [x] 2.4.4.5.2 ON TABLE/field commands (SUBTOTAL, SUMMARIZE, etc.). (Implemented in `src/asg_builder.py`)
      - [x] 2.4.4.5.3 COMPUTE command for calculated values. (Implemented in `src/asg_builder.py`)
  - [x] 2.4.5 Environment Builder:
    - [x] 2.4.5.1 Environment Commands:
      - [x] 2.4.5.1.1 JOIN command (CLEAR, LEFT OUTER, AS). (Implemented in `src/asg_builder.py`)
      - [x] 2.4.5.1.2 SET command for environment parameters. (Implemented in `src/asg_builder.py`)
    - [x] 2.4.5.2 Virtual Fields:
      - [x] 2.4.5.2.1 DEFINE FILE block structure. (Implemented in `src/asg_builder.py`)
      - [x] 2.4.5.2.2 DEFINE assignments with formats and expressions. (Implemented in `src/asg_builder.py`)
  - [x] 2.4.6 Master File Builder: Support FILENAME, SEGMENT, FIELD, and virtual fields in Master Files.

## Phase 3: Optimization (SSA-based IR)
Transform the ASG into a Control Flow Graph (CFG) using Static Single Assignment (SSA) form to enable relational optimizations.

- [ ] **3.1 CFG Generation:**
  - [x] 3.1.1 IR Infrastructure: Define `BasicBlock` and `ControlFlowGraph` classes. (Implemented in `src/ir.py`)
  - [x] 3.1.2 IR Instructions: Define base `Instruction` nodes and common types (e.g., `Assign`, `Jump`, `Branch`). (Implemented in `src/ir.py`)
  - [ ] 3.1.3 Basic Blocks Construction:
    - [x] 3.1.3.1 Linear Partitioning: Group sequential non-branching commands into basic blocks. (Implemented in `src/ir_builder.py`)
    - [x] 3.1.3.2 Label and Jump Mapping: Implement block splitting for `Label` nodes and block termination for `Goto` nodes. (Implemented in `src/ir_builder.py`)
  - [ ] 3.1.4 Control Flow Edges:
    - [ ] 3.1.4.1 Conditional Branching: Implement edges and block splitting for `IfDM` nodes.
    - [ ] 3.1.4.2 Loop Deconstruction: Implement edges and block structures for `Repeat` nodes.
- [ ] **3.2 SSA Transformation:**
  - [ ] 3.2.1 Dominator Analysis: Compute dominator tree and frontiers.
  - [ ] 3.2.2 Variable Renaming: Implement versioning for all variables.
  - [ ] 3.2.3 Phi-node Insertion: Handle merge points in control flow.
- [ ] **3.3 Relational Lifting:**
  - [ ] 3.3.1 Loop Analysis: Identify loops that iterate over data sources.
  - [ ] 3.3.2 Predicate Pushdown: Identify filters that can be moved to SQL WHERE.
  - [ ] 3.3.3 Projection Pruning: Identify unused fields.

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
