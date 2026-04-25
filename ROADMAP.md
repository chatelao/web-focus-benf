# ROADMAP
- [x] Implement a next modest and reasonable roadmap step (#24) (completed at 2026-04-25 03:43:52)
- [ ] Implement a next modest and reasonable roadmap step (#24)
- [ ] Implement a next modest and reasonable roadmap step
- [x] Implement a next modest and reasonable roadmap step (#22) (completed at 2026-04-25 03:26:35)
- [x] Implement a next modest and reasonable roadmap step (#20) (completed at 2026-04-25 02:46:03)
- [x] Find a use a modern compiler framework to lex, parse and build a AST from the language syntax with the goal to transform to sql (#18) (completed at 2026-04-25 02:12:11)
- [x] roadmap - split the lexer and parser parts if reasonable or find another way to break the implementation in smaller steps e.g. language feature etc. (#14) (completed at 2026-04-23 10:09:07)

## Chapter 1: Project Foundation & Meta
- [x] Merge Agents.md into gemini.md (#12) (completed at 2026-04-23 13:24:59)
- [x] Please reorder the ROADMAP.md - Keep topics per Chapter (and subchapters if necessary) (#11) (completed at 2026-04-23 10:04:12)
- [x] Add more details to the ROADMAP.md (#6) (completed at 2026-04-22 12:05:23)
- [ ] Reverse engineer the WebFOCUS programming language syntax and functionality
- [ ] Create a 'readthedocs' documentation of the analytics
- [x] Setup the empty CI/CD pipeline (completed at 2026-04-25 02:46:03)

## Chapter 2: Specifications & Manuals
- [x] https://github.com/chatelao/web-focus-benf/tree/main/specifications - Move each manual into one subdirectory and split it per chapter (#10) (completed at 2026-04-23 13:27:16)
- [x] Download all necessary standard, manuals, handbooks, etc. to `specifictions` and convewrt to ".md" if pdf retrieved (#8) (completed at 2026-04-23 09:07:44)
- [x] Download all necessary standard, manuals, handbooks, etc. to `specifications` and convert to ".md" if pdf retrieved (#5) (completed at 2026-04-23 09:07:44)

## Chapter 3: Core Parser & Grammar
- [ ] Implement a Lexer for WebFOCUS core syntax in Python
- [x] Define EBNF and Implement Parser for Master Files (Describing Data) (completed at 2026-04-25 02:46:02)
- [ ] Define EBNF and Implement Parser for basic TABLE FILE requests (Creating Reports)
  - [x] Support basic verbs (PRINT, LIST, SUM, COUNT, WRITE, ADD) and wildcard (*) (completed at 2026-04-25 03:26:52)
  - [x] Support AS phrases for column titles (completed at 2026-04-25 03:43:51)
  - [x] Support BY and ACROSS sort phrases (completed at 2026-04-25 03:43:52)
  - [ ] Support HEADING, FOOTING, and other formatting commands
  - [ ] Support Prefix Operators (AVE., MIN., MAX., etc.)
- [ ] Define EBNF and Implement Parser for Expressions and WHERE clauses
- [ ] Define EBNF and Implement Parser for Dialogue Manager commands (-SET, -IF, etc.)

## Chapter 4: Tooling & Integration
- [ ] Integrate parser results into the documentation generator
- [ ] Develop a CLI tool for automated WebFOCUS code analysis
- [ ] Create a comprehensive test suite for the parser using real-world WebFOCUS samples
  - [x] Collect and organize real-world WebFOCUS samples in `test/samples/` (completed at 2026-04-25 03:28:06)
  - [ ] Implement an automated test runner for samples
  - [ ] Verify grammar coverage against samples
