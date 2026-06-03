import argparse
import sys
import os
import json

# Add the current directory to sys.path so it can find the other modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from wf_parser import WebFocusParser
from asg_builder import ReportASGBuilder
from ir_builder import IRBuilder
from lineage_analyzer import LineageAnalyzer
from emitter import PostgresEmitter

def get_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)

def main():
    parser = argparse.ArgumentParser(description="WebFOCUS Transpiler CLI (Python)")
    parser.add_argument("-i", "--input", required=True, help="Input .fex file")
    parser.add_argument("-o", "--output", help="Output .sql file")
    parser.add_argument("--stats", action="store_true", help="Display source code statistics")
    parser.add_argument("--lineage", action="store_true", help="Output data lineage in JSON format")

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: File not found: {args.input}")
        sys.exit(1)

    try:
        with open(args.input, 'r') as f:
            content = f.read()

        if args.stats:
            loc = len(content.splitlines())
            print(f"Lines of Code (LOC): {loc}")

        parser_obj = WebFocusParser()
        ast = parser_obj.parse(content)

        asg_builder = ReportASGBuilder()
        asg = asg_builder.visit(ast)

        ir_builder = IRBuilder()
        cfg = ir_builder.build(asg)

        if args.lineage:
            analyzer = LineageAnalyzer()
            lineage = analyzer.analyze(cfg)
            print(json.dumps(lineage, indent=2))

        if args.output:
            # For PyInstaller, we need to find the templates folder
            template_dir = get_resource_path("templates")

            emitter = PostgresEmitter(template_dir=template_dir)
            sql = emitter.emit(cfg)
            with open(args.output, 'w') as f:
                f.write(sql)
            print(f"Transpiled to {args.output}")

        if not args.lineage and not args.stats and not args.output:
            print("Successfully parsed and built IR.")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
