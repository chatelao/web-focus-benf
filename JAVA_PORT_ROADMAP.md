# Java Port Roadmap: WebFOCUS to PostgreSQL Transpiler

This document outlines the strategic porting of the WebFOCUS to PostgreSQL Transpiler from Python to Java, as defined in `JAVA_PORT_DESIGN.md`.

## Phase 1: Infrastructure & Project Setup
- [x] 1.1 Maven Project Initialization: Setup `pom.xml` with dependencies (ANTLR4, Picocli, FreeMarker, Jackson, JGraphT, JUnit 5).
- [x] 1.2 ANTLR4 Configuration: Integrate `antlr4-maven-plugin` and verify grammar compilation.
- [x] 1.3 CLI Foundation: Implement basic command-line interface using Picocli (transpile, check, lineage).
- [x] 1.4 Logging & Diagnostics: Setup SLF4J/Logback and initial diagnostic reporting.

## Phase 2: ASG & IR Models (Data Structures)
- [x] 2.1 ASG Node Porting: Implement Java `record` types or immutable classes for ASG nodes (`asg.py` parity).
  - [x] 2.1.1 Base Nodes: ASGNode, Expression, Statement, Command.
  - [x] 2.1.2 Expressions:
    - [x] 2.1.2.1 Literals, Identifiers, AmperVars.
    - [x] 2.1.2.2 Binary and Unary operations.
    - [x] 2.1.2.3 Function calls and Built-in functions.
    - [x] 2.1.2.4 Conditional expressions:
      - [x] 2.1.2.4.1 IfExpression (IF-THEN-ELSE).
      - [x] 2.1.2.4.2 DecodeExpression (DECODE).
    - [x] 2.1.2.5 Set-based expressions (IN, BETWEEN, IS MISSING).
  - [x] 2.1.3 Dialogue Manager Commands:
    - [x] 2.1.3.1 Control Flow: Goto, Label, IfDM.
    - [x] 2.1.3.2 Variables & Defaults: SetDM, DefaultDM.
    - [x] 2.1.3.3 Output: TypeDM, HtmlFormDM.
    - [x] 2.1.3.4 Loops: Repeat.
    - [x] 2.1.3.5 I/O: ReadDM, WriteDM, IncludeDM.
    - [x] 2.1.3.6 Execution Control: RunDM, ExitDM.
  - [x] 2.1.4 Report Commands:
    - [x] 2.1.4.1 Basic: ReportRequest, VerbCommand, SortCommand, WhereClause, etc.
    - [x] 2.1.4.2 Output: OutputCommand (HOLD, PCHOLD, etc.).
    - [x] 2.1.4.3 Multi-file: MatchRequest, SubMatch, AfterMatchPhrase, MoreClause, MoreSubRequest.
  - [x] 2.1.5 Data Model Nodes: MasterFile, Segment, Field.
- [ ] 2.2 IR Instruction Porting: Implement IR instruction set and Control Flow Graph (CFG) structures using JGraphT.
  - [x] 2.2.1 Base IR Infrastructure (IRNode, Instruction, BasicBlock, ControlFlowGraph).
  - [ ] 2.2.2 Control Flow Instructions (Label, Jump, Branch, Phi).
  - [ ] 2.2.3 Data & Assignment Instructions (Assign, SetEnv, Default).
  - [ ] 2.2.4 Procedure & I/O Instructions (Call, Type, HtmlForm, Read, Write).
  - [ ] 2.2.5 Relational Instructions (Join, JoinClear, Define, Report, Match).
  - [ ] 2.2.6 Layout Instructions (CompoundLayout, CompoundEnd).
- [ ] 2.3 Metadata Models: Port Master File and Segment metadata models.

## Phase 3: Frontend & Semantic Analysis
- [ ] 3.1 ASG Builder: Port `asg_builder.py` to Java `WebFocusReportVisitor` implementation.
- [ ] 3.2 Symbol Table: Port hierarchical symbol resolution and scoping logic.
- [ ] 3.3 Type System: Port `TypeInferrer` and `TypeMapper` to Java.
- [ ] 3.4 Master File Parser: Port `master_file_parser.py` to Java implementation.

## Phase 4: Optimization (SSA & Relational Lifting)
- [ ] 4.1 SSA Transformer: Port SSA transformation logic (dominator analysis, Phi-node insertion, variable renaming).
- [ ] 4.2 Constant Propagation: Implement IR-level constant folding.
- [ ] 4.3 Dead Code Elimination: Implement reachability analysis and unused assignment removal.
- [ ] 4.4 Relational Lifting: Port advanced pattern matching for set-based SQL synthesis.

## Phase 5: Backend & Emission (FreeMarker)
- [ ] 5.1 Template Migration: Convert Jinja2 `.sql` templates to Apache FreeMarker syntax.
- [ ] 5.2 Postgres Emitter: Implement IR-to-SQL translation logic using FreeMarker.
- [ ] 5.3 Variable Mapping: Implement Java-based mapping between SSA versions and SQL identifiers.

## Phase 6: Verification & Parity
- [x] 6.1 Unit Test Porting: Port core unit tests to JUnit 5 (ASG parity complete).
- [ ] 6.2 Golden File Verification: Compare Java output against Python "Golden Files" for functional parity.
- [ ] 6.3 E2E Integration: Execute generated Java output against live PostgreSQL and verify result-set parity.
