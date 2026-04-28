# Railroad Diagram Concept for WebFocus Syntax

This document outlines the architecture for representing WebFocus syntax in "Railroad Diagrams" similar to the Oracle documentation style.

## Objective
Provide a clear, visual, and always up-to-date representation of the WebFocus grammar (from ANTLR4) to facilitate development and documentation, maintaining high visual parity with Oracle's syntax diagrams.

---

## Architecture Overview

The system follows a four-step pipeline to transform raw ANTLR4 grammars into professional documentation.

### Step 1: Extraction (W3C EBNF)
The `WebFocusReport.g4` and `MasterFile.g4` grammars are converted into standard W3C EBNF format.
*   **Why:** W3C EBNF is the industry standard for railroad generators and allows leveraging powerful layout engines.

### Step 2: Transformation (Automated Pruning & Inlining)
A Python script automatically simplifies the grammar for documentation purposes.
*   **Mechanism:** Technical rules (e.g., recursive expression tiers) are "pruned" or "inlined" into their parent rules.
*   **Control:** Rules are tagged in the `.g4` files (e.g., `// @internal`) to guide the transformation.

### Step 3: Rendering (Gunther Rademacher's RR)
The simplified EBNF is rendered into SVGs using Gunther Rademacher's RR tool.
*   **Visual Style:** Configured to match Oracle documentation (rounded terminals, rectangular non-terminals, clean horizontal flow).

### Step 4: Automation and Distribution
*   **Scripted Generation:** A central orchestration script handles the entire pipeline without manual intervention.
*   **Script Testing:** Conversion and pruning logic are covered by unit tests to prevent documentation regressions.
*   **Distribution:**
    *   **Releases:** A `.zip` archive of the documentation is included in every release.
    *   **Live Docs:** Documentation is automatically published to GitHub Pages on every push to `main`.

---

## Implementation Example: `TABLE FILE`

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

## Appendix: Examples

### `JOIN` Command

#### 1. Source (ANTLR4)
```antlr
join_command: JOIN (CLEAR asterisk | (LEFT? OUTER)? qualified_name IN qualified_name TO ALL? qualified_name IN qualified_name (AS NAME)?) SEMI?;
```

#### 2. Intermediate (Pruned EBNF)
Technical details like `asterisk` are inlined or simplified:
```ebnf
JOIN_COMMAND ::= 'JOIN' ( 'CLEAR' '*' | [ [ 'LEFT' ] 'OUTER' ] qualified_name 'IN' qualified_name 'TO' [ 'ALL' ] qualified_name 'IN' qualified_name [ 'AS' NAME ] ) ';'?
```

#### 3. Conceptual "Oracle Style" Output
*   **Optional Clauses:** `LEFT`, `OUTER`, and `ALL` are shown as optional branches.
*   **Choice:** The diagram branches between the `CLEAR` variant and the full `JOIN` syntax.
*   **Terminals:** Keywords like `JOIN`, `CLEAR`, `IN`, `TO`, `AS` are in rounded boxes.
*   **Non-Terminals:** `qualified_name` and `NAME` are in rectangular boxes.

## Appendix: Discarded Alternatives

### Extraction
*   **Direct ANTLR4 Metadata:** Discarded due to limited customization and poor visual layout.
*   **Custom Python Parser for .g4:** Discarded due to high maintenance effort to keep in sync with ANTLR4.

### Transformation
*   **Raw Grammar Rendering:** Discarded as too "noisy" for documentation.
*   **Manual Rule Curation:** Discarded due to high risk of "Documentation Rot".

### Rendering
*   **Tab Atkins' Railroad-diagrams:** Discarded as it requires a custom compiler from EBNF to its specific DSL.
*   **Mermaid.js:** Discarded as visuals are too far from the "Oracle Style".
