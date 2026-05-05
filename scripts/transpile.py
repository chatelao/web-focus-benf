import argparse
import os
import sys
from antlr4 import CommonTokenStream, InputStream

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

try:
    from WebFocusReportLexer import WebFocusReportLexer
    from WebFocusReportParser import WebFocusReportParser
    from asg_builder import ReportASGBuilder
    from ir_builder import IRBuilder
    from ssa_transformer import SSATransformer
    from emitter import PostgresEmitter
    from metadata_registry import MetadataRegistry
except ImportError as e:
    print(f"Error: Could not import transpiler modules. Ensure 'src' is in PYTHONPATH. {e}")
    sys.exit(1)

def transpile_code(code, metadata_registry):
    """Executes the full transpilation pipeline on a string of WebFOCUS code."""
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
    emitter = PostgresEmitter(metadata_registry=metadata_registry)
    output_sql = emitter.emit(cfg)

    return output_sql

def transpile_file(input_path, output_path, metadata_registry):
    """Transpiles a single file."""
    try:
        with open(input_path, 'r') as f:
            code = f.read()

        sql = transpile_code(code, metadata_registry)

        if output_path:
            with open(output_path, 'w') as f:
                f.write(sql)
            print(f"Successfully transpiled: {input_path} -> {output_path}")
        else:
            print(sql)
    except Exception as e:
        print(f"Error transpiling {input_path}: {e}", file=sys.stderr)

def transpile_directory(input_dir, output_dir, metadata_registry):
    """Transpiles all .fex files in a directory recursively."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.fex'):
                rel_path = os.path.relpath(root, input_dir)
                target_dir = os.path.join(output_dir, rel_path)

                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)

                input_path = os.path.join(root, file)
                output_filename = os.path.splitext(file)[0] + '.sql'
                output_path = os.path.join(target_dir, output_filename)

                transpile_file(input_path, output_path, metadata_registry)

def main():
    parser = argparse.ArgumentParser(description="WebFOCUS to PostgreSQL Transpiler CLI")
    parser.add_argument("input", help="Input .fex file or directory")
    parser.add_argument("-o", "--output", help="Output .sql file or directory")
    parser.add_argument("-m", "--master-path", action="append", help="Search path for Master Files (.mas)")

    args = parser.parse_args()

    metadata = MetadataRegistry()
    if args.master_path:
        for path in args.master_path:
            metadata.add_search_path(path)

    # Default search path: same as input file/dir
    if os.path.isdir(args.input):
        metadata.add_search_path(args.input)
    else:
        metadata.add_search_path(os.path.dirname(args.input))

    if os.path.isdir(args.input):
        if not args.output:
            print("Error: Output directory must be specified when transpiling a directory.", file=sys.stderr)
            sys.exit(1)
        transpile_directory(args.input, args.output, metadata)
    elif os.path.isfile(args.input):
        transpile_file(args.input, args.output, metadata)
    else:
        print(f"Error: Input path '{args.input}' not found.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
