# Specifications Cleanup Roadmap

This document outlines a phased strategic plan for automated cleanup, structural reform, semantic enrichment, and GFM (GitHub Flavored Markdown) compliance of the WebFOCUS documentation located in the `specifications/` directory.

## Phase 1: Automated Cleanup
- [x] 1.1 Remove form feed characters (`\f`) from all markdown files.
- [ ] 1.2 Remove orphaned page numbers and headers/footers introduced by PDF-to-Markdown conversion.

## Phase 2: Structural Reform
- [ ] 2.1 Heading Normalization: Convert plain-text headers to proper Markdown `#` headers.
- [ ] 2.2 Fenced Code Blocks: Wrap WebFOCUS code examples and ASCII tables in fenced code blocks (```).

## Phase 3: Semantic Enrichment
- [ ] 3.1 Internal Cross-links: Resolve "on page X" references into internal Markdown links.

## Phase 4: GFM Compliance
- [ ] 4.1 Table Conversion: Convert ASCII tables to GFM table syntax.
