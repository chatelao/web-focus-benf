# Railroad Diagram Implementation Roadmap

This document outlines the tasks required to implement the automated railroad diagram generation as defined in `RAILROAD_CONCEPT.md`.

## Phase 1: Extraction & Transformation (ANTLR4 to EBNF)
- [x] 1.1 Develop ANTLR4 to W3C EBNF conversion script.
    - [x] 1.1.1 Implement parser rule extraction and basic EBNF mapping (terminals/non-terminals).
    - [x] 1.1.2 Implement cardinality mapping (optional, repeat, one-or-more).
    - [x] 1.1.3 Implement grouping and alternatives mapping.
    - [x] 1.1.4 Implement lexer rule to terminal string conversion.
    - [x] 1.1.5 **Early Testing:** Implement unit tests for each mapping component.
- [x] 1.2 Implement rule tagging system in `WebFocusReport.g4` and `MasterFile.g4` (e.g., `// @internal`, `// @inline`).
- [x] 1.3 Develop automated rule pruning and inlining logic for technical/internal rules.
    - [x] 1.3.1 Implement multi-pass rule collection and `[internal]` rule removal.
    - [x] 1.3.2 Implement `[inline]` rule substitution logic (parenthesized replacement).
    - [x] 1.3.3 Add recursion protection to prevent infinite inlining loops.
    - [x] 1.3.4 Update existing unit tests to verify pruning/inlining behavior.
    - [x] 1.3.5 **Verification:** Run the updated script on `WebFocusReport.g4` and verify reduced rule count in EBNF.
- [x] 1.4 Support `MasterFile.g4` extraction.
- [x] 1.5 **Drift Prevention:** Implement a "Grammar Coverage" check to ensure all non-internal rules are present in the EBNF output.

## Phase 2: Rendering (EBNF to Railroad SVGs)
- [ ] 2.1 Integrate Gunther Rademacher's RR tool into the toolchain.
    - [x] 2.1.1 Verify Java environment availability (required for RR tool).
    - [x] 2.1.2 Download/Provision Gunther Rademacher's RR tool (`rr.war` or executable jar).
    - [x] 2.1.3 Implement a basic Python wrapper to execute the RR tool on generated EBNF.
- [ ] 2.2 Configure visual styles (colors, fonts, shapes) to match Oracle documentation style.
- [ ] 2.3 Create a template for the documentation HTML container.
- [ ] 2.4 **Verification:** Automated check that generated SVGs are valid and non-empty.

## Phase 3: Automation & Orchestration (Scripts)
- [ ] 3.1 Create `scripts/generate_railroad.py` to orchestrate the entire pipeline.
- [ ] 3.2 Implement support for incremental updates.
- [ ] 3.3 Add command-line interface for manual triggers.
- [ ] 3.4 **Pipeline Test:** Integrate the generation script into a local pre-commit hook to catch breakages early.

## Phase 4: Quality Assurance & Regression Testing
- [ ] 4.1 Implement integration tests to verify the end-to-end generation process.
- [ ] 4.2 **Golden Master Testing:** Maintain a "Golden" set of EBNF/SVGs and fail if changes occur without explicit approval.
- [ ] 4.3 Add validation step to ensure generated EBNF is syntactically valid for the RR tool.

## Phase 5: Distribution & CI/CD
- [ ] 5.1 Update GitHub Actions to package the generated documentation into a `.zip` artifact for every release.
- [ ] 5.2 Configure GitHub Actions to publish the syntax documentation to GitHub Pages.
- [ ] 5.3 Ensure documentation is published on every push/merge to the `main` branch.
- [ ] 5.4 **CI Verification:** Ensure the documentation build fails the CI pipeline if any generation or validation step fails.
