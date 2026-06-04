# Roadmap for Specification Formatting Improvements

This document outlines the strategic plan to improve the formatting and structure of the Markdown files in the `specifications/` directory. These files, originally converted from PDF sources, contain significant artifacts and structural inconsistencies that hinder readability and automated processing.

## 1. Objectives

*   **Remove PDF Artifacts**: Eliminate page numbers, headers, footers, and form-feed characters.
*   **Standardize Structure**: Ensure consistent use of Markdown headers (H1-H6).
*   **Semantic Formatting**: Properly fence code blocks and syntax examples.
*   **Table Conversion**: Transform ASCII/plain-text tables into proper Markdown tables.
*   **Link Verification**: Fix internal cross-references and page-based links.
*   **Compliance**: Achieve full compliance with GitHub Flavored Markdown (GFM).

## 2. Identified Issues

Based on initial analysis, the following issues are prevalent:
1.  **Page Headers/Footers**: Repeated titles like "Creating Reports With TIBCO® WebFOCUS Language" and page numbers.
2.  **Form Feeds**: `\f` characters or placeholder symbols representing page breaks.
3.  **Flat Hierarchy**: Section titles are often plain text instead of Markdown headers.
4.  **Unfenced Code**: WebFOCUS syntax examples are treated as normal text or indented incorrectly.
5.  **Broken Lists**: Numbered and bulleted lists often have broken alignment or split across "pages".
6.  **Plain Text Tables**: Tables are represented using spaces and dashes, making them hard to read and parse.

## 3. Phased Implementation

### Phase 1: Automated Cleanup (Cleaning the Noise)
*   - [x] **Task 1.1**: Develop regex-based scripts to identify and remove recurring PDF headers and footers.
*   - [x] **Task 1.2**: Remove page numbers and form-feed characters.
    *   - [x] **Task 1.2.1**: Remove form-feed (`\f`) characters.
    *   - [x] **Task 1.2.2**: Remove isolated page numbers.
*   - [x] **Task 1.3**: Normalize line endings and remove excessive blank lines caused by page breaks.

### Phase 2: Structural Reform (Establishing Hierarchy)
*   - [ ] **Task 2.1**: Standardize Headers.
    *   - [x] **Task 2.1.1**: Standardize Chapter Headings (Convert "Chapter X" to `# Chapter X: [Title]`).
    *   - [x] **Task 2.1.2**: Standardize Section Headings.
        *   - [x] **Task 2.1.2.1**: Extract section titles from "In this chapter/appendix" lists.
        *   - [x] **Task 2.1.2.2**: Convert identified section titles to `##` headers.
*   - [ ] **Task 2.2**: Reconstruct the Table of Contents (TOC) using standard Markdown list syntax with working anchors.
*   - [ ] **Task 2.3**: Repair Paragraph Wrapping.
    *   - [ ] **Task 2.3.1**: Identify lines ending in hyphens or lacking terminal punctuation for rejoining.
    *   - [ ] **Task 2.3.2**: Rejoin broken paragraphs into single continuous blocks.

### Phase 3: Semantic Enrichment (Formatting Content)
*   - [ ] **Task 3.1**: Code Block Fencing.
    *   - [ ] **Task 3.1.1**: Identify and fence WebFOCUS code blocks (` ```fex `).
    *   - [ ] **Task 3.1.2**: Identify and fence SQL code blocks (` ```sql `).
*   - [ ] **Task 3.2**: Convert ASCII tables into GFM tables.
*   - [ ] **Task 3.3**: Replace "on page X" references with relative Markdown links (e.g., `[See Sorting](#sorting)`).
*   - [ ] **Task 3.4**: Standardize list indentation and bullet styles.

### Phase 4: Validation and QA
*   - [ ] **Task 4.1**: Run `markdownlint` across all files to enforce style consistency.
*   - [ ] **Task 4.2**: Use `mdformat` to ensure uniform spacing and wrapping.
*   - [ ] **Task 4.3**: Perform manual spot-checks on complex diagrams and nested structures.

## 4. Proposed Tools

*   **Scripts**: Python/Sed/Awk for regex-based batch cleaning.
*   **Linters**: `markdownlint` for enforcing rules.
*   **Formatters**: `mdformat` or `prettier`.
*   **Validation**: `markdown-link-check` for verifying internal and external links.

## 5. Prioritization

1.  **High**: Phase 1 (Cleanup) and Phase 2.1 (Headers). This makes the files readable immediately.
2.  **Medium**: Phase 3.1 (Code Blocks) and 3.4 (Lists).
3.  **Low**: Phase 3.2 (Table conversion) and 3.3 (Link fixing).

---
*Last Updated: 2024-05-23*
