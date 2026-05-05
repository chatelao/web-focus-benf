# HOWTO: Installation and Usage Guide

This guide describes how to install, run, and develop the WebFOCUS to PostgreSQL Transpiler.

## Prerequisites

- **Python 3**: The primary development language.
- **Java (JRE/JDK)**: Required if you need to rebuild the ANTLR4 grammars from `.g4` files.

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd web-focus-benf
   ```

2. **Install dependencies**:
   You can use the provided installation script:
   ```bash
   ./src/install.sh
   ```
   Or install via `pip` directly:
   ```bash
   pip install -r requirements.txt
   ```

   Dependencies include `antlr4-python3-runtime`, `jinja2`, `pytest`, and `pre-commit`.

## Project Structure

- `src/`: Core transpiler source code.
  - `WebFocusReport.g4`, `MasterFile.g4`: ANTLR4 grammar definitions.
  - `asg_builder.py`: Constructs the Abstract Semantic Graph.
  - `ir_builder.py`: Builds the SSA-based Intermediate Representation.
  - `emitter.py`: Generates PL/pgSQL using Jinja2 templates.
- `scripts/`: Utility scripts for benchmarking, grammar conversion, and railroad diagram generation.
- `test/`: Comprehensive test suite including unit tests and end-to-end samples.

## Usage

### Running the Benchmark/Sample Script
You can run the transpiler on a set of sample files to see it in action:
```bash
PYTHONPATH=src:. python3 scripts/benchmark_compilation.py
```
This script processes samples in `test/samples/` and `test/documentation_examples/`, reporting the time taken for each phase.

### Using the Transpiler as a Library
You can integrate the transpiler into your own Python code. Here is a basic example:

```python
import sys
import os
from antlr4 import InputStream, CommonTokenStream

# Add src to path if necessary
sys.path.append(os.path.abspath('src'))

from WebFocusReportLexer import WebFocusReportLexer
from WebFocusReportParser import WebFocusReportParser
from asg_builder import ReportASGBuilder
from ir_builder import IRBuilder
from ssa_transformer import SSATransformer
from emitter import PostgresEmitter
from metadata_registry import MetadataRegistry

def transpile(code):
    # 1. Parsing
    input_stream = InputStream(code)
    lexer = WebFocusReportLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = WebFocusReportParser(token_stream)
    tree = parser.start()

    # 2. ASG Construction
    builder = ReportASGBuilder()
    asg_nodes = builder.visit(tree)

    # 3. IR Construction
    ir_builder = IRBuilder()
    cfg = ir_builder.build(asg_nodes)

    # 4. SSA Transformation
    ssa_transformer = SSATransformer()
    ssa_transformer.transform(cfg)

    # 5. Backend Emission
    metadata = MetadataRegistry()
    emitter = PostgresEmitter(metadata_registry=metadata)
    output_sql = emitter.emit(cfg)

    return output_sql

if __name__ == "__main__":
    wf_code = "TABLE FILE CAR PRINT MODEL BY COUNTRY END"
    print(transpile(wf_code))
```

## Testing

Run the full test suite using `pytest`:
```bash
PYTHONPATH=src:. pytest
```
To run specific tests, provide the path to the test file:
```bash
PYTHONPATH=src:. pytest test/test_e2e_basic_reporting.py
```

## Development

### Rebuilding Grammars
If you modify `src/WebFocusReport.g4` or `src/MasterFile.g4`, you need to regenerate the Python lexer and parser:
```bash
./scripts/antlr4.sh -Dlanguage=Python3 src/WebFocusReport.g4 -visitor -o src/
./scripts/antlr4.sh -Dlanguage=Python3 src/MasterFile.g4 -visitor -o src/
```
*Note: This requires the `antlr-complete.jar` which is typically expected in the `build/` directory or as configured in `scripts/antlr4.sh`.*

### Railroad Diagrams
To generate visual railroad diagrams for the grammar:
```bash
python3 scripts/generate_railroad.py
```
