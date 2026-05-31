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
  - [x] 2.1.5 Data Model Nodes: MasterFile, Segment, Field, DefineAssignment, Dimension, Hierarchy.
- [ ] 2.2 IR Instruction Porting: Implement IR instruction set and Control Flow Graph (CFG) structures using JGraphT.
  - [x] 2.2.1 Base IR Infrastructure (IRNode, Instruction, BasicBlock, ControlFlowGraph).
  - [x] 2.2.2 Control Flow Instructions (Label, Jump, Branch, Phi).
  - [x] 2.2.3 Data & Assignment Instructions (Assign, SetEnv, Default).
  - [x] 2.2.4 Procedure & I/O Instructions (Call, Type, HtmlForm, Read, Write).
  - [x] 2.2.5 Relational Instructions:
    - [x] 2.2.5.1 Join-related IR (Join, JoinClear).
    - [x] 2.2.5.2 Data-driven IR (Define, Report, Match).
  - [x] 2.2.6 Layout Instructions:
    - [x] 2.2.6.1 Layout blocks (CompoundLayout, CompoundEnd).
- [ ] 2.3 Metadata Models: Port Master File and Segment metadata models.

## Phase 3: Frontend & Semantic Analysis
- [ ] 3.1 ASG Builder Infrastructure:
  - [ ] 3.1.1 Base Visitor: Implement `WebFocusReportVisitor` and `MasterFileVisitor` skeleton.
  - [ ] 3.1.2 Dispatcher Logic: Implement node traversal and construction orchestration.
- [ ] 3.2 Expression & Command Builders:
  - [ ] 3.2.1 Expression Builder: Support all arithmetic, character, and logical expressions.
  - [ ] 3.2.2 Dialogue Manager Builder: Port visitor logic for -SET, -IF, -GOTO, -REPEAT, etc.
  - [ ] 3.2.3 Report Request Builder: Port visitor logic for TABLE FILE, verbs, sorts, and filters.
  - [ ] 3.2.4 Environment Builder: Port visitor logic for JOIN, SET, and DEFINE FILE.
- [ ] 3.3 Master File Parser & Builder:
  - [ ] 3.3.1 Port `MasterFileParserWrapper` and `MasterFileASGBuilder` to Java.
- [ ] 3.4 Symbol Table & Scoping:
  - [ ] 3.4.1 Implement hierarchical `SymbolTable` (block-level and global).
  - [ ] 3.4.2 Port `SymbolResolver` for AmperVars and database field resolution.
- [ ] 3.5 Type System:
  - [ ] 3.5.1 Implement `TypeInferrer` for literal and expression typing.
  - [ ] 3.5.2 Implement `TypeMapper` for metadata-driven type resolution.

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
