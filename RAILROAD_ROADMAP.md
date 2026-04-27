# Railroad Diagram Implementation Roadmap

This document outlines the tasks required to implement the automated railroad diagram generation as defined in `RAILROAD_CONCEPT.md`.

## Phase 1: Extraction & Transformation (ANTLR4 to EBNF)
- [ ] 1.1 Develop ANTLR4 to W3C EBNF conversion script.
- [ ] 1.2 Implement rule tagging system in `WebFocusReport.g4` (e.g., `// @internal`).
- [ ] 1.3 Develop automated rule pruning and inlining logic for technical/internal rules.
- [ ] 1.4 Support `MasterFile.g4` extraction in addition to `WebFocusReport.g4`.

## Phase 2: Rendering (EBNF to Railroad SVGs)
- [ ] 2.1 Integrate Gunther Rademacher's RR tool into the toolchain.
- [ ] 2.2 Configure visual styles (colors, fonts, shapes) to match Oracle documentation style.
- [ ] 2.3 Create a template for the documentation HTML container.

## Phase 3: Automation & Orchestration (Scripts)
- [ ] 3.1 Create `scripts/generate_railroad.py` to orchestrate the entire pipeline.
- [ ] 3.2 Implement support for incremental updates (only regenerate changed rules).
- [ ] 3.3 Add command-line interface for manual triggers and parameter configuration.

## Phase 4: Testing & QA
- [ ] 4.1 Implement unit tests for the EBNF conversion logic in `test/test_railroad_extraction.py`.
- [ ] 4.2 Implement integration tests to verify the end-to-end generation process.
- [ ] 4.3 Add validation step to ensure generated EBNF is syntactically valid for the RR tool.

## Phase 5: Distribution & CI/CD
- [ ] 5.1 Update GitHub Actions to package the generated documentation into a `.zip` artifact for every release.
- [ ] 5.2 Configure GitHub Actions to publish the syntax documentation to GitHub Pages.
- [ ] 5.3 Ensure documentation is published on every push/merge to the `main` branch.
- [ ] 5.4 Implement a "documentation preview" for Pull Requests (optional/bonus).
