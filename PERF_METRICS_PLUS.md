# Performance Metrics for Synthetic AFP Generation

To create accurate synthetic test files that mirror real-world production runs, the existing performance metrics provide a solid baseline. However, to achieve high-fidelity synthetic generation, additional "structural" and "distributional" metrics are required.

## 1. Analysis of Existing Metrics

The current metrics capture **Aggregate Throughput** and **Functional Density**:
- **Mnemonic Counts**: Identifies the "vocabulary" of the AFP stream (e.g., high volume of `AMB`, `AMI`, `TRN`).
- **PTX Expansion Ratio**: Measures the overhead of XML/intermediate representations vs. raw binary (currently **18.33**).
- **PTOCA Breakdown**: Highlights the cost of specific layout actions (e.g., `GAD`/`GBSEG` taking significant write time).

## 2. Proposed Metrics for "Plus" Accuracy

To generate synthetic files that stress-test the transpiler/renderer in the same way as the source files, the following metrics should be tracked:

### A. Structural & Hierarchical Metrics
- **Nesting Depth Statistics**: Max and average depth of nested groups (BOG/EOG, BPG/EPG). Synthetic files should match the complexity of the document's logical structure.
- **Pages per Document / Objects per Page**: Distributions of how many pages are in a typical "print job" and how many objects (images, text blocks) reside on each.
- **Resource Reference Count**: How many unique `MCF` (Map Coded Font) or `MIO` (Map Image Object) calls exist vs. how many times they are invoked.

### B. Spatial & Layout Distributions
- **Coordinate Delta Analysis**: Instead of just counts of `AMB`/`AMI`, we need the distribution of movement values. Are jumps usually small (kerning) or large (new columns)?
- **PTX Sequence Density**: How many `TRN` (Transparent Data) commands are grouped within a single `PTX` block before a layout change occurs.
- **Field Overlap Frequency**: Metrics on how often text fields or graphics overlap, which is critical for verifying Z-order handling in synthetic outputs.

### C. Content & Entropy Metrics
- **Character Set Distribution**: Beyond count per Charset (e.g., IBM01141), tracking character frequency helps generate synthetic text that triggers similar encoding edge cases.
- **String Length Histograms**: The `Avg Payload` for `TRN` is **21.20 bytes**, but knowing the variance (min/max) is crucial for boundary testing buffer sizes.
- **Redundancy/Repetition Index**: Measures how much text is repeated (e.g., headers/footers) vs. unique data. This impacts the efficiency of synthetic file compression.

### D. Relational (Markov) Metrics
- **Command Transition Matrix**: The probability that mnemonic $X$ is followed by mnemonic $Y$. For example, a `SEC` (Set Extended Color) is almost always followed by a `TRN` or `DIR`. Modeling these transitions ensures synthetic files follow "legal" and "typical" AFP sequences.
- **State Change Frequency**: How often fonts (`SCFL`), orientations (`STO`), or colors (`SEC`) change relative to the amount of text.

## 3. Implementation Value

By capturing these "Plus" metrics, the synthetic generator can:
1. **Profile-Driven Scaling**: Generate a 1GB file that isn't just "large," but has the same *complexity density* as a 10MB production sample.
2. **Regression Fidelity**: Ensure that optimizations for PTOCA processing (like `AMB`/`AMI` handling) are tested against realistic jump patterns.
3. **Collision Testing**: Use spatial metrics to intentionally create edge cases where text and graphics nearly collide, ensuring the renderer's precision.
