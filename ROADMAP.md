# ROADMAP
- [x] 0.7 Implement a next modest, feasible and reasonable MIGRATION_ROADMAP.md step (#51) (completed at 2026-04-25 19:33:12)

- [x] 0.6 Add an on the fly rendered SYSTEM_OVERVIEW.plantuml to the README.md and insure it is shown in rtd too (#49) (completed at 2026-04-25 20:17:55)
- [x] 0.5 Analyze why there are 2 .g4 files in `/src`and update MIGRATION_ROADMAP.md according the task open (#48) (completed at 2026-04-25 19:18:42)
- [x] 0.4 Erstelle ein .plantuml mit einer Systemübersicht, füge als "note" überall die offenen Punkte hinzug (#45) (completed at 2026-04-25 19:10:51)
- [x] 0.3 Implement a next modest, feasible and reasonable MIGRATION_ROADMAP.md step (#44) (completed at 2026-04-25 19:01:32)
- [x] 0.1 Add a MIGRATION_ROADMAP.md from the current system to the new antlr/ninja final solution (#41) (completed at 2026-04-25 18:41:52)

## Chapter 1: Project Foundation & Meta
- [x] 1.1 Merge Agents.md into gemini.md (#12) (completed at 2026-04-23 13:24:59)
- [x] 1.2 Please reorder the ROADMAP.md - Keep topics per Chapter (#11) (completed at 2026-04-23 10:04:12)
- [x] 1.3 Add more details to the ROADMAP.md (#6) (completed at 2026-04-22 12:05:23)
- [ ] 1.4 Reverse engineer the WebFOCUS programming language syntax and functionality
  - [ ] 1.4.1 Document Dialogue Manager syntax and behavior
  - [ ] 1.4.2 Document TABLE FILE verb and sort phrase semantics
  - [ ] 1.4.3 Document Master File attribute meanings
- [ ] 1.5 Create a 'readthedocs' documentation of the analytics
- [x] 1.6 Setup the empty CI/CD pipeline (completed at 2026-04-25 02:46:03)
- [x] 1.7 Implement a next modest, feasible and reasonable roadmap step (#37) (completed at 2026-04-25 08:53:59)
- [x] 1.8 Implement a next modest, feasible and reasonable roadmap step (#34) (completed at 2026-04-25 08:47:08)
- [x] 1.9 Solve the technical debts in modest and reasonable steps (#33) (completed at 2026-04-25 08:46:43)
- [x] 1.10 Implement a next modest and reasonable roadmap step (#31) (completed at 2026-04-25 04:54:24)
- [x] 1.11 Rewrite all necessary documents, specifications and plans to align with the new target described in WEBFOCUS_TO_POSTGRE.md (#29) (completed at 2026-04-25 04:22:00)
- [x] 1.12 roadmap - split the lexer and parser parts if reasonable or find another way to break the implementation in smaller steps e.g. language feature etc. (#14) (completed at 2026-04-23 10:09:07)
- [x] 1.13 Find a use a modern compiler framework to lex, parse and build a AST from the language syntax with the goal to transform to sql (#18) (completed at 2026-04-25 02:12:11)

## Chapter 2: Specifications & Manuals
- [x] 2.1 Move each manual into one subdirectory and split it per chapter (#10) (completed at 2026-04-23 13:27:16)
- [x] 2.2 Download all necessary standard, manuals, handbooks, etc. to `specifications` and convert to ".md" if pdf retrieved (#8) (completed at 2026-04-23 09:07:44)
- [x] 2.3 Download all necessary standard, manuals, handbooks, etc. to `specifications` and convert to ".md" if pdf retrieved (#5) (completed at 2026-04-23 09:07:44)

## Chapter 3: Frontend - ANTLR4 Parser & Grammar
- [ ] 3.1 Migrate core parser from Lark to ANTLR4
  - [ ] 3.1.1 Migrate Lark grammar to ANTLR4 format (#39)
  - [ ] 3.1.2 Implement ANTLR4 Lexer and Parser in Python
  - [ ] 3.1.3 Integrate ANTLR4 parser into WebFocusParser dispatcher
  - [ ] 3.1.4 Migrate existing Lark test cases to ANTLR4
- [ ] 3.2 Define ANTLR4 grammar for Dialogue Manager commands (-SET, -IF, etc.)
- [x] 3.3 Define EBNF and Implement Parser for Master Files (Describing Data) (completed at 2026-04-25 02:46:02)
- [ ] 3.4 Define EBNF and Implement Parser for basic TABLE FILE requests (Creating Reports)
  - [x] 3.4.1 Support basic verbs (PRINT, LIST, SUM, COUNT, WRITE, ADD) and wildcard (*) (completed at 2026-04-25 03:26:52)
  - [x] 3.4.2 Support AS phrases for column titles (completed at 2026-04-25 03:43:51)
  - [x] 3.4.3 Support BY and ACROSS sort phrases (completed at 2026-04-25 03:43:52)
  - [x] 3.4.4 Support Prefix Operators (AVE., MIN., MAX., etc.) (completed at 2026-04-25 04:40:41)
  - [x] 3.4.5 Support FOOTING command (completed at 2026-04-25 04:40:54)
  - [x] 3.4.6 Support SUBHEAD and SUBFOOT commands (completed at 2026-04-25 05:00:17)
  - [x] 3.4.7 Support SUB-TOTAL and SUMMARIZE commands (completed at 2026-04-25 08:54:11)
  - [x] 3.4.8 Support ON TABLE formatting commands (PCHOLD, etc.) (completed at 2026-04-25 08:53:59)
  - [ ] 3.4.9 Support HEADING and other formatting commands
- [ ] 3.5 Define EBNF and Implement Parser for Expressions and WHERE clauses

## Chapter 4: Middle-tier - Semantic Analysis & Optimization
- [ ] 4.1 Implement Abstract Semantic Graph (ASG) and Symbol Table
  - [ ] 4.1.1 Define ASG node classes for WebFOCUS constructs
  - [ ] 4.1.2 Implement Symbol Table for variable scope and type tracking
  - [ ] 4.1.3 Implement ASG builder from ANTLR4 AST
- [ ] 4.2 Develop SSA-based Intermediate Representation (IR) for optimization
  - [ ] 4.2.1 Define IR instruction set and CFG structure
  - [ ] 4.2.2 Implement CFG generator from ASG
  - [ ] 4.2.3 Implement SSA transformation (phi-nodes, renaming)
  - [ ] 4.2.4 Implement basic optimization passes (DCE, Constant Propagation)
- [ ] 4.3 Implement set-based optimization passes for common TABLE FILE patterns

## Chapter 5: Backend - PL/pgSQL Emission
- [ ] 5.1 Implement PL/pgSQL Emitter using Jinja2
  - [ ] 5.1.1 Setup Jinja2 environment and base templates
  - [ ] 5.1.2 Implement emitter for TABLE FILE relational logic
  - [ ] 5.1.3 Implement emitter for Dialogue Manager procedural logic
- [ ] 5.2 Map WebFOCUS formatting commands to decoupled presentation logic

## Chapter 6: Tooling & Integration
- [ ] 6.1 Integrate parser results into the documentation generator
- [ ] 6.2 Develop a CLI tool for automated WebFOCUS code analysis
- [ ] 6.3 Create a comprehensive test suite for the transpiler using real-world WebFOCUS samples
  - [x] 6.3.1 Collect and organize real-world WebFOCUS samples in `test/samples/` (completed at 2026-04-25 03:28:06)
  - [ ] 6.3.2 Implement an automated test runner for samples
  - [ ] 6.3.3 Verify grammar coverage against samples
