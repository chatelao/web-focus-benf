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
- [x] 2.1 Integrate Gunther Rademacher's RR tool into the toolchain.
    - [x] 2.1.1 Verify Java environment availability (required for RR tool).
    - [x] 2.1.2 Download/Provision Gunther Rademacher's RR tool (`rr.war` or executable jar).
    - [x] 2.1.3 Implement a basic Python wrapper to execute the RR tool on generated EBNF.
- [x] 2.2 Configure visual styles (colors, fonts, shapes) to match Oracle documentation style.
    - [x] 2.2.1 Research and define Oracle-style color palette and fonts (CSS properties).
    - [x] 2.2.2 Update `RRTool` wrapper to support additional styling flags (`-suppressebnf`, `-offset`).
    - [x] 2.2.3 Update `generate_railroad.py` to expose styling flags and implement CSS post-processing for XHTML to match Oracle style.
- [x] 2.3 Create a template for the documentation HTML container.
- [x] 2.4 **Verification:** Automated check that generated SVGs are valid and non-empty.

## Phase 3: Automation & Orchestration (Scripts)
- [x] 3.1 Create `scripts/generate_railroad.py` to orchestrate the entire pipeline.
- [x] 3.2 Implement support for incremental updates.
- [x] 3.3 Add command-line interface for manual triggers.
- [x] 3.4 **Pipeline Test:** Integrate the generation script into a local pre-commit hook to catch breakages early.

## Phase 4: Quality Assurance & Regression Testing
- [x] 4.1 Implement integration tests to verify the end-to-end generation process.
- [x] 4.2 **Golden Master Testing:** Maintain a "Golden" set of EBNF/SVGs and fail if changes occur without explicit approval.
- [x] 4.3 Add validation step to ensure generated EBNF is syntactically valid for the RR tool.

## Phase 5: Distribution & CI/CD
- [ ] 5.1 Update GitHub Actions to package the generated documentation as a downloadable artifact.
    - [x] 5.1.1 Archive `docs/` as a workflow artifact in CI/CD.
    - [ ] 5.1.2 (Optional) Automate attachment of documentation zip to GitHub Releases.
- [x] 5.2 Configure GitHub Actions to publish the syntax documentation to GitHub Pages.
- [x] 5.3 Ensure documentation is published on every push/merge to the `main` branch.
- [x] 5.4 **CI Verification:** Ensure the documentation build fails the CI pipeline if any generation or validation step fails.

## Phase 6: User Experience & Navigation
- [x] 6.1 Add generation metadata (date, version) to the documentation index.
- [x] 6.2 Integrate links to railroad diagrams into the project README.
- [x] 6.3 Add 'Back to Index' navigation to generated diagrams.
- [x] 6.4 Implement rule-filtering capability in grammar documentation.
- [x] 6.5 Add 'Clear' button to the search input.
- [x] 6.6 Display result count during filtering.
- [x] 6.7 Implement highlighting for the active (target) rule.

## Phase 7: Advanced Documentation Features
- [x] 7.1 Implement cross-references (links) between rules in railroad diagrams.

## Phase 8: Content Enrichment
- [x] 8.1 Extract and display rule descriptions from ANTLR4 comments.

## Phase 9: Advanced Rule Organization & Search
- [x] 9.1 Implement rule categorization using `@category` tags.
- [x] 9.2 Group rules by category in the generated documentation.
- [x] 9.3 Enhance search functionality to include rule descriptions and handle category groupings.
