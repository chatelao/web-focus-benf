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
- [x] **2.4 ASG Builder:** Implement the visitor to transform ANTLR4 parse tree to ASG.
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

- [x] **3.1 CFG Generation:**
  - [x] 3.1.1 IR Infrastructure: Define `BasicBlock` and `ControlFlowGraph` classes. (Implemented in `src/ir.py`)
  - [x] 3.1.2 IR Instructions: Define base `Instruction` nodes and common types (e.g., `Assign`, `Jump`, `Branch`). (Implemented in `src/ir.py`)
  - [x] 3.1.3 Basic Blocks Construction:
    - [x] 3.1.3.1 Linear Partitioning: Group sequential non-branching commands into basic blocks. (Implemented in `src/ir_builder.py`)
    - [x] 3.1.3.2 Label and Jump Mapping: Implement block splitting for `Label` nodes and block termination for `Goto` nodes. (Implemented in `src/ir_builder.py`)
  - [x] 3.1.4 Control Flow Edges:
    - [x] 3.1.4.1 Conditional Branching: Implement edges and block splitting for `IfDM` nodes. (Implemented in `src/ir_builder.py`)
    - [x] 3.1.4.2 Loop Deconstruction:
      - [x] 3.1.4.2.1 Basic REPEAT structure (loop header, back edges).
      - [x] 3.1.4.2.2 Conditional Loops: WHILE/UNTIL support.
      - [x] 3.1.4.2.3 Iterative Loops: TIMES/FOR support.
- [x] **3.2 SSA Transformation:**
  - [x] 3.2.1 Dominator Analysis: Compute dominator tree and frontiers. (Implemented in `src/dominators.py`)
  - [x] 3.2.2 Phi-node Insertion: Handle merge points in control flow. (Implemented in `src/ssa_transformer.py`)
    - [x] 3.2.2.1 Variable Discovery: Identify all variables and their defining blocks.
    - [x] 3.2.2.2 Iterative Placement: Implement the algorithm to place `Phi` instructions in dominance frontiers.
  - [x] 3.2.3 Variable Renaming: Implement versioning for all variables. (Implemented in `src/ssa_transformer.py`)
    - [x] 3.2.3.1 Usage Analysis: Identify variable usages in expressions and instructions.
    - [x] 3.2.3.2 Renaming Algorithm: Implement recursive DFS over dominator tree for variable versioning.
- [x] **3.3 Optimization Passes:**
  - [x] 3.3.1 Constant Propagation: Substitute variables with literal values. (Implemented in `src/optimizer.py`)
  - [x] 3.3.2 Dead Code Elimination:
    - [x] 3.3.2.1 Reachability Analysis: Remove unreachable blocks from CFG. (Implemented in `src/optimizer.py`)
    - [x] 3.3.2.2 Unused Assignment Elimination: Remove SSA assignments with no consumers. (Implemented in `src/optimizer.py`)
- [ ] **3.4 Relational Lifting:**
- [x] **3.4.1 Loop Analysis:** (Basic loop lifting to PL/pgSQL state machine implemented)
    - [x] 3.4.1.1 Identification of constant vs. data-driven loops.
    - [x] 3.4.1.2 Lifting loops to PL/pgSQL procedural state machine. (Implemented in `src/emitter.py`)
    - [x] 3.4.1.3 Identification of simple loops for native `FOR`/`WHILE` optimization.
      - [x] 3.4.1.3.1 Constant-bound `FOR` loops (TIMES/FOR).
        - [x] 3.4.1.3.1.1 Pattern matching of REPEAT...TIMES in CFG.
        - [x] 3.4.1.3.1.2 Pattern matching of REPEAT...FOR with literal bounds.
        - [x] 3.4.1.3.1.3 Native `FOR` loop emission in PL/pgSQL.
      - [x] 3.4.1.3.2 Simple `WHILE` loops with non-mutating condition variables.
    - [ ] 3.4.1.4 Identification of loops over data sources for relational lifting.
      - [x] 3.4.1.4.1 Identification of `REPEAT` loops containing `-READ` instructions.
      - [x] 3.4.1.4.2 Analysis of I/O dependencies and record-at-a-time patterns.
      - [x] 3.4.1.4.2.1 Identify loop-carried dependencies for variables within `-READ` loops.
      - [x] 3.4.1.4.2.2 Map `-READ` variables to Master File fields to determine the underlying relational source.
      - [x] 3.4.1.4.3 Detection of procedural aggregations and filters within data loops.
      - [x] 3.4.1.4.3.1 Pattern matching for procedural accumulators (e.g., `VAR = VAR + READ_VAR`).
      - [x] 3.4.1.4.3.2 Pattern matching for procedural filters (e.g., conditional jumps skipping logic based on `-READ` values).
      - [x] 3.4.1.4.4 Implementation of Relational Lift pass to map loops to set-based SQL.
      - [x] 3.4.1.4.4.1 Synthesize SQL `SELECT` with `WHERE` and `GROUP BY` from detected patterns.
      - [x] 3.4.1.4.4.2 Replace procedural loop with a single `ir.Report` instruction in the CFG.
  - [ ] 3.4.2 Predicate Pushdown:
    - [x] 3.4.2.1 Filter Lifting: Move WHERE conditions to SQL. (Implemented in `src/emitter.py`)
    - [x] 3.4.2.2 Total Lifting: Move WHERE TOTAL conditions to SQL HAVING. (Implemented in `src/emitter.py`)
  - [x] 3.4.3 Projection Pruning: Identify unused fields. (Implemented via Join Pruning in `src/emitter.py`)
  - [x] 3.4.4 Aggregation Lifting: Identify and lift aggregations (SUM, AVG) to SQL. (Implemented in `src/emitter.py`)
  - [x] 3.4.5 Virtual Field Lifting: Move DEFINE calculations to SQL.
    - [x] 3.4.5.1 Expression Tracking: Track virtual fields defined via `ir.Define`. (Implemented in `src/emitter.py`)
    - [x] 3.4.5.2 Selection Substitution: Inline virtual field expressions into `SELECT` statements. (Implemented in `src/emitter.py`)
    - [x] 3.4.5.3 Predicate Substitution: Inline virtual field expressions into `WHERE` clauses. (Implemented in `src/emitter.py`)
  - [x] 3.4.6 Join Lifting: Translate JOIN commands to SQL JOINs.
    - [x] 3.4.6.1 Join Context Management: Maintain a mapping of joined tables and their join conditions. (Implemented in `src/emitter.py`)
    - [x] 3.4.6.2 SQL JOIN Generation: Emit `JOIN` clauses in the generated SQL queries. (Implemented in `src/emitter.py`)
    - [x] 3.4.6.3 Field Qualification: Ensure fields are correctly qualified with table names in multi-table queries. (Implemented in `src/emitter.py`)

## Phase 4: Backend Emission (Jinja2)
Use Jinja2 templates to generate the final PostgreSQL and middle-tier code.

- [x] **4.1 PL/pgSQL Emission Infrastructure:**
  - [x] 4.1.1 Template Environment: Setup Jinja2 and base layout templates.
- [x] **4.1.2 Variable Mapping: Implement mapping between SSA versions and PL/pgSQL variables.
    - [x] 4.1.2.1 Variable Discovery: Identify all unique SSA variables in the CFG. (Implemented in `src/emitter.py`)
    - [x] 4.1.2.2 Name Sanitization: Map WebFOCUS/SSA names to SQL-safe identifiers. (Implemented in `src/emitter.py`)
    - [x] 4.1.2.3 Type Mapping: Map WebFOCUS types (I, F, A) to PostgreSQL types. (Implemented in `src/type_mapper.py`)
    - [x] 4.1.2.4 Type Integration: Use `TypeInferrer` and `type_mapper` for accurate PL/pgSQL variable declarations.
- [x] **4.2 Procedural Logic Emission:**
  - [x] 4.2.1 Variable Declaration: Generate `DECLARE` section for all discovered variables. (Implemented in `src/templates/base.sql.j2`)
  - [x] 4.2.2 Expression Translation: Transform WebFOCUS expressions to PostgreSQL-compatible SQL. (Implemented in `src/emitter.py`)
  - [x] 4.2.3 Statement Emission:
    - [x] 4.2.3.1 Assignments: Generate `v_target := expression;` for `ir.Assign`. (Implemented in `src/emitter.py`)
    - [x] 4.2.3.2 Phi Resolution: Generate move instructions to resolve Phi nodes at block entries. (Implemented in `src/emitter.py`)
    - [x] 4.2.3.3 Messaging: Generate `RAISE NOTICE` for `ir.Type`. (Implemented in `src/emitter.py`)
  - [x] 4.2.4 Control Flow (State Machine):
    - [x] 4.2.4.1 Block Dispatcher: Implement a `WHILE` loop and `CASE` statement to navigate basic blocks. (Implemented in `src/emitter.py`)
    - [x] 4.2.4.2 Jump/Branch Translation: Update the next block state variable based on `ir.Jump` and `ir.Branch`. (Implemented in `src/emitter.py`)
- [x] **4.3 Relational Request Emission:**
  - [x] 4.3.1 SQL Query Generation: Transform `ir.Report` nodes to optimized PostgreSQL queries.
    - [x] 4.3.1.1 Projection: Mapping PRINT/SUM and field selections. (Implemented in `src/emitter.py`)
    - [x] 4.3.1.2 Data Sources: Mapping filenames to SQL tables (using `MetadataRegistry`). (Implemented in `src/emitter.py`)
    - [x] 4.3.1.3 Filtering: Mapping WHERE clauses to SQL `WHERE`. (Implemented in `src/emitter.py`)
    - [x] 4.3.1.4 Grouping: Mapping BY/ACROSS phrases to SQL `GROUP BY`. (Implemented in `src/emitter.py`)
    - [x] 4.3.1.5 Aggregations: Mapping prefix operators to SQL aggregate functions.
      - [x] 4.3.1.5.1 Basic operators: SUM, AVE, MIN, MAX, CNT, TOT. (Implemented in `src/emitter.py`)
      - [x] 4.3.1.5.2 Advanced operators: FST, LST (First/Last via ordered aggregates or window functions). (Implemented in `src/emitter.py`)
      - [x] 4.3.1.5.3 Statistical operators: MDN, MDE, ASQ (Median, Mode, Average Square). (Implemented in `src/emitter.py`)
      - [x] 4.3.1.5.4 Percentage operators: PCT, RPCT (Percentage, Row Percentage). (Implemented in `src/emitter.py`)
      - [x] 4.3.1.5.5 Rank and Distinct: RNK, DST. (Implemented in `src/emitter.py`)
    - [x] 4.3.1.6 Post-Aggregation Filtering: Mapping WHERE TOTAL to SQL `HAVING`. (Implemented in `src/emitter.py`)
    - [x] 4.3.1.7 Sorting: Mapping sort options to SQL `ORDER BY`. (Implemented in `src/emitter.py`)
    - [x] 4.3.1.8 Calculated Values: Mapping COMPUTE command to SQL expressions. (Implemented in `src/emitter.py`)
    - [x] 4.3.1.9 Presentation Metadata: Mapping RECAP and SUMMARIZE commands to SQL comments. (Implemented in `src/emitter.py`)
  - [x] 4.3.2 Data Source Mapping: Resolve TABLE FILE references to database tables/views. (Implemented in `src/emitter.py` via `MetadataRegistry`)

## Phase 5: Verification and Parity
Ensure the new system produces correct results and maintains parity with the legacy parser.

- [x] **5.1 Regression Testing:**
  - [x] 5.1.1 Frontend Parity: Run the existing test suite against the new ANTLR4-based frontend. (Verified via `test/test_antlr_wf_parser.py`)
  - [x] 5.1.2 End-to-End Tests: Verify PL/pgSQL output for a subset of core features.
    - [x] 5.1.2.1 Basic Reporting: PRINT/SUM requests with WHERE clauses. (Verified via `test/test_e2e_basic_reporting.py`)
    - [x] 5.1.2.2 Advanced Filtering: Complex WHERE clauses, BETWEEN, IN, MISSING. (Verified via `test/test_e2e_advanced_filtering.py`)
    - [x] 5.1.2.3 Calculated Fields: DEFINE and COMPUTE expression lifting. (Verified via `test/test_e2e_calculated_fields.py`)
    - [x] 5.1.2.4 Data Integration: Multi-table JOINs and virtual field lifting from joined files. (Verified via `test/test_e2e_data_integration.py`)
    - [x] 5.1.2.5 Control Flow: DM variable resolution and PL/pgSQL state machine execution. (Verified via `test/test_e2e_control_flow.py`)
  - [x] 5.1.3 Grammar Coverage: Ensure all core EBNF features are implemented and tested.
    - [x] 5.1.3.1 Support `ALL` keyword in `JOIN` commands.
    - [x] 5.1.3.2 Support hyphenated `SET` keywords (e.g., `ONLINE-FMT`).
    - [x] 5.1.3.3 Support `COMPOUND LAYOUT` structure.
      - [x] 5.1.3.3.1 Grammar support for `COMPOUND LAYOUT` and `COMPOUND END`.
      - [x] 5.1.3.3.2 Grammar support for layout components (SECTION, PAGELAYOUT, COMPONENT).
      - [x] 5.1.3.3.3 ASG support for multi-component documents.
      - [x] 5.1.3.3.4 Emitter support for sequential component execution.
    - [x] 5.1.3.4 Support inline format specifications (e.g., `SUM FIELD/I08M`).
    - [x] 5.1.3.5 Support `RECAP` command in report requests.
    - [x] 5.1.3.6 Support `ACROSS-TOTAL` for cross-tabulation summaries.
    - [x] 5.1.3.7 Support `AND COMPUTE` and `AS` phrase in report requests.
    - [x] 5.1.3.8 Support Hierarchical Reporting (Project 3).
      - [x] 5.1.3.8.1 Procedural commands: `HIERARCHY` in `BY`, `WHEN` clause, and `SHOW UP/DOWN`.
      - [x] 5.1.3.8.2 Master File extensions: `DIMENSION`, `HIERARCHY`, and `HRY_` attributes.
    - [x] 5.1.3.9 Support Data Merge (Project 4).
      - [x] 5.1.3.9.1 Grammar for `ON TABLE MERGE INTO`.
      - [x] 5.1.3.9.2 Grammar for `MATCHING`, `WHEN MATCHED`, `WHEN NOT MATCHED`.
    - [x] 5.1.3.10 Support Drill Through (Project 5).
      - [x] 5.1.3.10.1 Support `-HTMLFORM` Dialogue Manager command.
      - [x] 5.1.3.10.2 Support `OPEN` and `CLOSE` options for `PCHOLD`.
      - [x] 5.1.3.10.3 Support `PAGE-BREAK` option for `ON field`.
      - [x] 5.1.3.10.4 Support `DRILLTHROUGH` in `SET STYLE` blocks.
    - [x] 5.1.3.11 Support `DECODE` expression.
      - [x] 5.1.3.11.1 Grammar support for `DECODE` syntax.
      - [x] 5.1.3.11.2 ASG support for `DecodeExpression`.
      - [x] 5.1.3.11.3 Emitter support for translating `DECODE` to SQL `CASE`.
    - [x] 5.1.3.12 Support `MATCH FILE` command.
      - [x] 5.1.3.12.1 Grammar support for `MATCH FILE`, `RUN`, `AFTER MATCH`, and merge phrases (`OLD-OR-NEW`, `OLD-AND-NEW`, `OLD-NOT-NEW`, `NEW-NOT-OLD`, `OLD-NOR-NEW`, `OLD`, `NEW`).
      - [x] 5.1.3.12.2 ASG support for `MatchRequest`, `SubMatch`, and `AfterMatchPhrase`.
      - [x] 5.1.3.12.3 Emitter support for `MATCH` logic.
        - [x] 5.1.3.12.3.1 IR support for `MATCH FILE`.
        - [x] 5.1.3.12.3.2 Basic SQL generation for `MATCH` (merging two files).
        - [x] 5.1.3.12.3.3 Support for all merge phrases (OLD-OR-NEW, etc.) and multi-file chaining.
        - [x] 5.1.3.12.3.4 Support COMPUTE and virtual fields in MATCH sub-requests.
    - [x] 5.1.3.13 Support `MORE` phrase (Universal Concatenation).
      - [x] 5.1.3.13.1 Grammar support for `MORE` phrase in `TABLE` and `MATCH` requests.
      - [x] 5.1.3.13.2 ASG support for `MoreClause` and sub-requests.
      - [x] 5.1.3.13.3 Emitter support for `UNION ALL`.
    - [x] 5.1.3.14 Support `-READ`, `-WRITE`, and `-DEFAULT` Dialogue Manager commands.
      - [x] 5.1.3.14.1 Grammar support for `-READ`, `-WRITE`, and `-DEFAULT`.
      - [x] 5.1.3.14.2 ASG support for `ReadDM`, `WriteDM`, and `DefaultDM` nodes.
      - [x] 5.1.3.14.3 IR and Emitter support for Dialogue Manager I/O and defaults.
  - [x] 5.1.4 Semantic Parity: Verify that ASG and IR transformations preserve source semantics.
    - [x] 5.1.4.1 Symbol Resolution Validation:
      - [x] 5.1.4.1.1 Global vs. Local scope resolution for AmperVars.
      - [x] 5.1.4.1.2 Multi-segment field resolution in joined Master Files.
      - [x] 5.1.4.1.3 Virtual field shadowing rules (DEFINE vs. Master File).
      - [x] 5.1.4.1.4 Symbol resolution within complex expression structures (tuples in lists).
    - [x] 5.1.4.2 Type Consistency:
      - [x] 5.1.4.2.1 Numeric precision mapping (I, F, D, P to PostgreSQL).
      - [x] 5.1.4.2.2 Alpha-numeric string truncation and padding semantics. (Verified via `test/test_alpha_parity.py`)
      - [x] 5.1.4.2.3 Date/Time format conversion parity. (Verified via `test/test_date_parity.py`)
    - [x] 5.1.4.3 Constant Folding Parity:
      - [x] 5.1.4.3.1 Arithmetic expression folding.
      - [x] 5.1.4.3.2 Character concatenation folding.
      - [x] 5.1.4.3.3 Boolean logic short-circuiting parity.
    - [x] 5.1.4.4 Extended Relational Operators Parity: CONTAINS, OMITS, EXCEEDS, INCLUDES, EXCLUDES. (Verified via `test/test_e2e_extended_filtering.py`)
- [x] **5.2 Sample Validation:**
  - [x] 5.2.1 Core Samples: Validate transpiler output against samples in `test/samples/`. (Verified via `test/test_core_samples.py`)
  - [x] 5.2.2 Documentation Examples: Validate against samples in `test/documentation_examples/`. (Verified via `test/test_documentation_examples.py`)
    - [x] 5.2.2.1 Project 1: Joined Report.
    - [x] 5.2.2.2 Project 2: Compound Layout.
    - [x] 5.2.2.3 Project 3: Hierarchical Cube.
      - [x] 5.2.2.3.1 Parse `newgl.mas` with hierarchical metadata.
      - [x] 5.2.2.3.2 Parse `hierarchical_report.fex`.
      - [x] 5.2.2.3.3 End-to-end PL/pgSQL emission for hierarchical report.
    - [x] 5.2.2.4 Project 4: Data Merge.
      - [x] 5.2.2.4.1 Parse `data_merge.fex`.
      - [x] 5.2.2.4.2 End-to-end PL/pgSQL emission for MERGE.
    - [x] 5.2.2.5 Project 5: Drill Through.
      - [x] 5.2.2.5.1 Parse `main_controller.fex`.
      - [x] 5.2.2.5.2 Parse `summary_report.fex`.
      - [x] 5.2.2.5.3 Parse `detail_report.fex`.
      - [x] 5.2.2.5.4 End-to-end PL/pgSQL emission for Drill Through.
  - [ ] 5.2.3 Real-world Samples:
    - [ ] 5.2.3.1 Sales and Revenue Dashboard: Complex aggregations, multi-table joins, and temporal filtering.
    - [ ] 5.2.3.2 Inventory Management: Multi-step `MATCH FILE` chaining and `MORE` phrase for historical vs. current reconciliation.
    - [ ] 5.2.3.3 HR Organizational Hierarchy: Leveraging `BY...HIERARCHY`, `WHEN`, and `SHOW` for recursive reporting.
    - [ ] 5.2.3.4 Financial Reconciliation: Complex `RECAP` logic, `COMPUTE` with conditional branching, and Dialogue Manager orchestration.
- [ ] **5.3 Performance Benchmarking:**
  - [ ] 5.3.1 Query Execution: Compare generated SQL performance vs original WebFOCUS execution.
    - [ ] 5.3.1.1 Establish baseline performance metrics for legacy reports in source environment.
    - [ ] 5.3.1.2 Measure execution time of generated PostgreSQL queries in target environment.
    - [ ] 5.3.1.3 Identify and document performance regressions or significant improvements.
  - [x] 5.3.2 Compilation Overhead: Measure transpilation time for large projects. (Implemented in `scripts/benchmark_compilation.py`)

## Phase 6: Decommissioning
- [ ] 6.1 Transition Tests: Ensure all legacy tests pass against the new transpiler architecture.
  - [ ] 6.1.1 Map legacy test cases to new transpiler test infrastructure.
  - [ ] 6.1.2 Verify parity for all legacy core reporting tests.
    - [ ] 6.1.2.1 Verb commands (PRINT, SUM, LIST, COUNT).
    - [ ] 6.1.2.2 Sort phrases (BY, ACROSS) and sort options.
    - [ ] 6.1.2.3 Selection criteria (WHERE, WHERE TOTAL).
    - [ ] 6.1.2.4 Calculated fields (DEFINE, COMPUTE).
    - [ ] 6.1.2.5 Joins and data source mapping.
  - [ ] 6.1.3 Verify parity for all legacy Dialogue Manager tests.
    - [ ] 6.1.3.1 Variable assignment (-SET, -DEFAULT).
    - [ ] 6.1.3.2 Control flow (-IF, -GOTO, -REPEAT).
    - [ ] 6.1.3.3 Dialogue Manager I/O (-READ, -WRITE).
    - [ ] 6.1.3.4 External interactions (-INCLUDE, -RUN, -HTMLFORM).
- [x] 6.2 Code Cleanup:
  - [x] 6.2.1 Remove Lark-related code (`wf_parser.py`, `master_file_parser.py`).
  - [x] 6.2.2 Remove `lark` from `requirements.txt`. (Completed: Verified absence in `requirements.txt`)
- [x] 6.3 Technical Debt: Close out remaining items in `TECHNICAL_DEBTS.md`. (Completed: All debts in `TECHNICAL_DEBTS.md` are marked as done)

## Phase 7: Continuous Integration & Runtime Verification
Ensure the generated PL/pgSQL code is not only syntactically correct but also executes correctly against a live PostgreSQL database.

- [x] **7.1 Live Database Environment:**
  - [x] 7.1.1 Configure a PostgreSQL service container in the CI/CD pipeline (GitHub Actions). (Implemented in `.github/workflows/cicd.yml`)
  - [x] 7.1.2 Implement a robust database connection utility for use in the test suite. (Implemented in `src/db_utils.py`)
- [x] **7.2 Data & Schema Fixtures:**
  - [x] 7.2.1 Implement an automated DDL generator that transforms Master File metadata into PostgreSQL `CREATE TABLE` statements. (Implemented in `src/ddl_generator.py`)
  - [x] 7.2.2 Develop a fixture loading mechanism to populate the live database with test data (from JSON/CSV) for each sample. (Implemented in `src/fixture_loader.py`)
- [ ] **7.3 Integration & Runtime Testing:**
  - [x] 7.3.1 Implement a runtime test runner.
    - [x] 7.3.1.1 Implement procedure execution and notice capturing in `RuntimeRunner`. (Implemented in `src/runtime_runner.py`)
    - [x] 7.3.1.2 Integrate `DDLGenerator` and `FixtureLoader` into `RuntimeRunner` for automated environment setup.
  - [ ] 7.3.2 Verify result-set parity by comparing the output of executed procedures against expected results.
    - [x] 7.3.2.1 Support `HOLD` command in `PostgresEmitter` using `CREATE TEMP TABLE`.
    - [x] 7.3.2.2 Enhance `RuntimeRunner` to fetch and return result sets from temporary tables.
    - [ ] 7.3.2.3 Add integration tests for result-set parity verification.
  - [x] 7.3.3 Implement comprehensive error reporting for runtime failures (e.g., SQL syntax errors, type mismatches during execution). (Implemented in `src/runtime_runner.py`)
