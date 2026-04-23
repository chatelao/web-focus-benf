# ROADMAP
- [x] roadmap - split the lexer and parser parts if reasonable or find another way to break the implementation in smaller steps e.g. language feature etc. (#14) (completed at 2026-04-23 10:09:07)

## Chapter 1: Project Foundation & Meta
- [ ] Merge Agents.md into gemini.md (#12)
- [x] Please reorder the ROADMAP.md - Keep topics per Chapter (and subchapters if necessary) (#11) (completed at 2026-04-23 10:04:12)
- [x] Add more details to the ROADMAP.md (#6) (completed at 2026-04-22 12:05:23)
- [ ] Reverse engineer the WebFOCUS programming language syntax and functionality
- [ ] Create a 'readthedocs' documentation of the analytics
- [ ] Setup the empty CI/CD pipeline

## Chapter 2: Specifications & Manuals
- [ ] https://github.com/chatelao/web-focus-benf/tree/main/specifications - Move each manual into one subdirectory and split it per chapter (#10)
- [x] Download all necessary standard, manuals, handbooks, etc. to `specifictions` and convewrt to ".md" if pdf retrieved (#8) (completed at 2026-04-23 09:07:44)
- [x] Download all necessary standard, manuals, handbooks, etc. to `specifications` and convert to ".md" if pdf retrieved (#5) (completed at 2026-04-23 09:07:44)

## Chapter 3: Core Parser & Grammar
- [ ] Implement a Lexer for WebFOCUS core syntax in Python
- [ ] Define EBNF and Implement Parser for Master Files (Describing Data)
- [ ] Define EBNF and Implement Parser for basic TABLE FILE requests (Creating Reports)
- [ ] Define EBNF and Implement Parser for Expressions and WHERE clauses
- [ ] Define EBNF and Implement Parser for Dialogue Manager commands (-SET, -IF, etc.)

## Chapter 4: Tooling & Integration
- [ ] Integrate parser results into the documentation generator
- [ ] Develop a CLI tool for automated WebFOCUS code analysis
- [ ] Create a comprehensive test suite for the parser using real-world WebFOCUS samples
