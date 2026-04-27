# Railroad Diagram Concept for WebFocus Syntax

This document outlines the concept for representing WebFocus syntax in "Railroad Diagrams" similar to the Oracle documentation style.

## Objective
Provide a clear, visual, and always up-to-date representation of the WebFocus grammar (from ANTLR4) to facilitate development and documentation, maintaining high visual parity with Oracle's syntax diagrams.

---

## Step 1: Extraction (From .g4 to Intermediate Format)

### Variant 1.1: Direct ANTLR4 Metadata Extraction
Use ANTLR4's internal representation or a tool that reads `.g4` files directly and produces a visual output.
*   **Pros:** Single toolchain, no conversion step.
*   **Cons:** Limited customization; output often looks like generic trees rather than railroad diagrams.

### Variant 1.2: Conversion to W3C EBNF
Convert the `WebFocusReport.g4` grammar into standard W3C EBNF format.
*   **Pros:** Compatible with the most powerful railroad generators (like Gunther Rademacher's RR).
*   **Cons:** Requires a conversion script to handle ANTLR4-specific syntax (e.g., lexer fragments, semantic predicates).

### Variant 1.3: Custom Python Parser for .g4
Write a lightweight Python script that parses the `.g4` files and generates a JSON-based description of the rules.
*   **Pros:** Full control over which rules are exported (e.g., skipping internal lexer rules).
*   **Cons:** High maintenance effort as the parser must be kept in sync with ANTLR4 features.

**Best Selection: Variant 1.2 (Conversion to W3C EBNF)**
*   **Justification:** W3C EBNF is the "lingua franca" for railroad generators. It allows us to leverage professional tools that already implement the complex layout logic required for Oracle-style diagrams.

---

## Step 2: Transformation (Rule Optimization)

### Variant 2.1: Raw Grammar Rendering
Render every single rule defined in the ANTLR4 grammar.
*   **Pros:** 100% accurate to the implementation.
*   **Cons:** "Noise" from technical rules (e.g., `dm_primary`, `dm_additive_expression`) makes the diagrams hard to read for end-users.

### Variant 2.2: Manual Rule Curation
Hand-pick and define a separate "Documentation Grammar" that simplifies complex recursions into user-friendly railroad structures.
*   **Pros:** Most readable and professional output.
*   **Cons:** High risk of "Documentation Rot" where the diagram doesn't match the actual parser.

### Variant 2.3: Automated Rule Pruning & Inlining
Use a script to automatically inline "internal" rules (those marked with a prefix or specific comment) into their parent rules for the diagram only.
*   **Pros:** Combines implementation accuracy with documentation readability.
*   **Cons:** Requires sophisticated logic to handle recursive inlining without creating infinite loops.

**Best Selection: Variant 2.3 (Automated Rule Pruning & Inlining)**
*   **Justification:** By tagging rules in `WebFocusReport.g4` (e.g., using comments like `// @internal`), we can automate the simplification process. This ensures the diagrams stay updated while remaining "Oracle-clean".

---

## Step 3: Rendering (Visual Style)

### Variant 3.1: Gunther Rademacher's RR (Railroad Diagram Generator)
A Java-based tool (and web service) that produces high-quality SVGs.
*   **Pros:** Extremely mature, handles very complex grammars, output is very close to Oracle style (rounded corners, clean lines).
*   **Cons:** Java dependency; styling is primarily controlled via internal logic rather than CSS.

### Variant 3.2: Tab Atkins' Railroad-diagrams (JS/Python)
A library used by the CSS Working Group for their specifications.
*   **Pros:** Purely declarative, highly customizable via CSS, fits perfectly into a modern web-based documentation site.
*   **Cons:** Requires a custom "compiler" from EBNF to the library's specific DSL.

### Variant 3.3: Mermaid.js
Use the popular Mermaid.js library's flowchart or experimental railroad support.
*   **Pros:** Easy integration into Markdown (GitHub natively supports it).
*   **Cons:** Visuals are currently too far from the "Oracle Style"; layout logic for complex syntax is suboptimal.

**Best Selection: Variant 3.1 (Gunther Rademacher's RR)**
*   **Justification:** This tool is the industry standard for creating "Oracle-like" diagrams. Its layout engine handles the density of SQL-like languages (which WebFocus is) much better than general-purpose diagramming libraries. It provides the exact "look and feel" requested.

---

## Implementation Example: `TABLE FILE`

Using the selected variants (W3C EBNF -> Automated Pruning -> RR), the `TABLE FILE` command from `src/WebFocusReport.g4` would be visualized as follows:

### 1. Source (ANTLR4)
```antlr
request: table_file (verb_command | by_command | across_command | ...)* end_command;
table_file: TABLE FILE qualified_name;
end_command: END;
```

### 2. Intermediate (Pruned EBNF)
The internal `table_file` and `end_command` are inlined for the user view:
```ebnf
TABLE_REQUEST ::= 'TABLE' 'FILE' qualified_name ( VERB_PHRASE | SORT_PHRASE | ... )* 'END'
```

### 3. Conceptual "Oracle Style" Output
*   **Terminals (`TABLE`, `FILE`, `END`):** Shown in rounded rectangles with a light background.
*   **Non-Terminals (`qualified_name`):** Shown in rectangles.
*   **Loops (the `*` part):** A return line going back to the start of the optional block, with standard Oracle-style arrowheads.

---

## Conclusion

By using **Gunther Rademacher's RR** with a **pre-processing step to inline technical ANTLR4 rules**, we achieve a documentation suite that is:
1.  **Visually Identical** to Oracle SQL documentation.
2.  **Maintenance-Free** because it is derived directly from the code.
3.  **Scalable** to the full complexity of the WebFocus language.
