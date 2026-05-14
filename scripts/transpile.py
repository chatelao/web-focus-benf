import argparse
import os
import sys
from antlr4 import CommonTokenStream, InputStream

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

try:
    import asg
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

def collect_stats(code, asg_nodes):
    """Collects metrics from the source code and ASG."""
    stats = {
        'loc': len(code.splitlines()),
        'report_requests': 0,
        'dm_commands': 0,
        'details': {}
    }

    for node in asg_nodes:
        if isinstance(node, (asg.ReportRequest, asg.MatchRequest)):
            stats['report_requests'] += 1
        elif isinstance(node, asg.Command):
            class_name = node.__class__.__name__
            if class_name.endswith('DM'):
                stats['dm_commands'] += 1
                stats['details'][class_name] = stats['details'].get(class_name, 0) + 1
    return stats

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

    stats = collect_stats(code, asg_nodes)

    # 3. IR Construction
    ir_builder = IRBuilder()
    cfg = ir_builder.build(asg_nodes)

    # 4. SSA Transformation
    ssa_transformer = SSATransformer()
    ssa_transformer.transform(cfg)

    # 5. Backend Emission
    emitter = PostgresEmitter(metadata_registry=metadata_registry)
    output_sql = emitter.emit(cfg)

    return output_sql, stats

def transpile_file(input_path, output_path, metadata_registry, show_stats=False):
    """Transpiles a single file."""
    try:
        with open(input_path, 'r') as f:
            code = f.read()

        sql, stats = transpile_code(code, metadata_registry)

        if output_path:
            with open(output_path, 'w') as f:
                f.write(sql)
            print(f"Successfully transpiled: {input_path} -> {output_path}")
        else:
            print(sql)

        if show_stats:
            print(f"\n--- Statistics for {input_path} ---")
            print(f"Lines of Code: {stats['loc']}")
            print(f"Report Requests: {stats['report_requests']}")
            print(f"Dialogue Manager Commands: {stats['dm_commands']}")
            for cmd, count in stats['details'].items():
                print(f"  - {cmd}: {count}")

        return stats
    except Exception as e:
        print(f"Error transpiling {input_path}: {e}", file=sys.stderr)
        return None

def transpile_directory(input_dir, output_dir, metadata_registry, show_stats=False):
    """Transpiles all .fex files in a directory recursively."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    total_stats = {
        'loc': 0,
        'report_requests': 0,
        'dm_commands': 0,
        'details': {},
        'files_processed': 0
    }

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

                stats = transpile_file(input_path, output_path, metadata_registry)
                if stats:
                    total_stats['loc'] += stats['loc']
                    total_stats['report_requests'] += stats['report_requests']
                    total_stats['dm_commands'] += stats['dm_commands']
                    total_stats['files_processed'] += 1
                    for cmd, count in stats['details'].items():
                        total_stats['details'][cmd] = total_stats['details'].get(cmd, 0) + count

    if show_stats:
        print("\n--- Cumulative Statistics ---")
        print(f"Files Processed: {total_stats['files_processed']}")
        print(f"Total Lines of Code: {total_stats['loc']}")
        print(f"Total Report Requests: {total_stats['report_requests']}")
        print(f"Total Dialogue Manager Commands: {total_stats['dm_commands']}")
        for cmd, count in sorted(total_stats['details'].items()):
            print(f"  - {cmd}: {count}")

def main():
    parser = argparse.ArgumentParser(description="WebFOCUS to PostgreSQL Transpiler CLI")
    parser.add_argument("input", help="Input .fex file or directory")
    parser.add_argument("-o", "--output", help="Output .sql file or directory")
    parser.add_argument("-m", "--master-path", action="append", help="Search path for Master Files (.mas)")
    parser.add_argument("--stats", action="store_true", help="Display source code statistics")

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
        transpile_directory(args.input, args.output, metadata, show_stats=args.stats)
    elif os.path.isfile(args.input):
        transpile_file(args.input, args.output, metadata, show_stats=args.stats)
    else:
        print(f"Error: Input path '{args.input}' not found.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
